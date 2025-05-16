# How to speed up a Mathlib file

We explain how a slow Mathlib file can be made faster. These notes are based on
the experiment carried out in Mathlib PR
[#12412](https://github.com/leanprover-community/mathlib4/pull/12412).

1. The first step is to find out which parts of the code are slow. To do so, 
   add a line `set_option profiler true` after the `import` statements.
   This will produce lines of the form `<blah> took <number>ms` (or even `<number>s`)
   in the infoview, recording steps that took at least `100ms` (the lower bound in ms
   can be adapted via `set_option profiler.threshold <num>`).
2. For each such line, try to make the corresponding step faster following the
   instructions below.
3. The previous step can potentially be repeated with a lowered setting of
   `profiler.threshold`, to find and speed up things that are not very slow,
   but also not very fast. This will eventually deliver diminishing returns, however.
4. Remove the profiler options again and PR!

## Dealing with specific slow steps

Here we explain how one can try to speed up various parts of the code that cause
the profiler to produce messages in the infoview.

### `typeclass inference of <name> took <a long time>`

1. Add `set_option trace.Meta.synthInstance true in` immediately before the declaration
   causing the message.
2. Look at the generated instance synthesis trace in the infoview and find the instance(s)
   of `<name>` that are slow.
3. Use `#synth <name> <args>` before the declaration (possibly temporarily adding `variable`s
   to the context if needed) to obtain a suitable term providing the instance.
4. Add a line
   `@[local instance] lemma/def <some name> <possibly some args> : <name> <args> := <term>`
   before the declaration (or near the beginning of the current section/namespace).
   If the instance needs some local context from within the proof, add
   `have/let <some name> <possibly some args> : <name> <args> := <term>` at a suitable
   place in the proof instead.
5. Remove the `set_option` line before the declaration.

It may be the case that `<term>` again triggers a slow instance search, so this procedure
may need to be repeated.

**Trade-off:** Littering files with local instances is not nice and goes somewhat against
the purpose of the type class system.

Of course, an even better solution would be to find out *what* causes the type class search
to be slow in the cases discovered and then find a fix for that. This would likely benefit
many other files throughout Mathlib.

### `simp took <a long time>`

Replace the relevant `simp/simpa` call by `simp?/simpa?` and click on the `Try this:`
suggestion to replace it by a `simp/simpa only` call. In some cases it is also possible
to prune the list of lemmas to some extent.

**Trade-off:** Proofs can get several dense lines longer, and will now mention many lemmas by name, each of which might be renamed in the future, breaking your proof.

### `elaboration took <a long time>`

Look for `_`s in the declaration that triggers it, find out what they are filled by,
and replace them by the corresponding explicit arguments.

**Trade-off:** If the explicit arguments are long, this makes the statement longer
and potentially harder to read.

### `compilation of <name> took <a long time>`

Try to add `noncomputable` before the definition.

**Trade-off:** Definition is no longer kernel-reducible, but this should not be a
problem in most cases.

### `tactic execution of <tactic> took <a long time>`

Try to replace the slow tactic by calls to simpler ones.

* For example, a slow `nontriviality ... using ...` can be replaced by
  ```lean
  rcases subsingleton_or_nontrivial ... with H | H
  · -- get `Subsingleton` case out of the way
    ...
  -- now we have `Nontrivial ...`
  ```

* A slow `convert` can be avoided by doing the rewrites that are done following it
first and then using `refine` or `exact`.

**Trade-off:** The proof may get a bit longer and more pedestrian.
