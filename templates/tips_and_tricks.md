# Lean Tips and Tricks

This document contains some tips for intermediate and advanced users of Lean.
It is currently focussed around Lean 3.

### Commenting out large proofs using `sorry`

Sometimes skipping subportions of a proof is helpful (e.g. to disable a portion which is slow while working on the rest). The straightforward way to do so is to comment out the lines which constitute the subportion, but if a subgoal has been surrounded by braces, you can also temporarily skip it by prepending `sorry;`
```
sorry; { rw blah,
  ...
  HUGE PROOF,
  ... }
```
With this method only one line needs to be changed, syntax highlighting is usually preserved, and jumping to definition still works. It also has the advantage that it is extremely easy to remove all instances of `sorry;` from a file when finished using find and replace, and to quickly toggle this on and off to check things still work when desired.

### Memory and deterministic timeout
Lean has two configurable flags for configuring its resource usage, memory and execution time.
While the defaults for these are usually fairly sensible, when writing proofs it can be helpful to increase these options, if deterministic timeouts or out of memory issues slow down development.
This is especially helpful when using tactics like [`library_search`](/mathlib_docs/tactics.html#library_search), which may run for a long time but then produce a result that tells us a much faster tactic to use if they succeed.

To change these settings we can add the flags `-M <some number of megabytes>` (default 4096) for the memory limit and `-T <number of allocations>` (default 100000).
In VSCode this can be configured by opening the settings and searching for `Lean Memory Limit` and `Lean Time Limit`.
Mathlib itself enforces a deterministic timeout of 100000, and often tries to have individual tactic calls use much less, so it is good practice not to rely on a large value for this setting.


### Old mode
If you change a file early on in the import hierarchy and then attempt to work on a file that depends on it much later, then Lean will try to check all files in between to ensure they didn't break.
This behaviour can cause the Lean server to become unresponsive, or simply slow down development.
You can call lean with the "--old" flag to help in these situations, though it does come with some caveats.
In VSCode you can enable it by opening the VSCode settings and searching for "Lean: extra options" then add the flag `--old`.
For Emacs the variable `lean-extra-arguments` can be modified to add this flag.
This causes lean not to recompile oleans for unedited files and just assume everything worked, so in this situation it is helpful to avoid recompilation.
However you do then run the risk that your change broke or changed the meaning of some file in-between. Thus it most applicable when you are adding a new lemma/definition early in the hierarchy that you are sure won't break later files, rather than when you are changing existing definitions in an incompatible way.
It is possible to "prove false" when running lean with the old flag on; by changing a definition in an early file, later results about that definition may become incorrect if Lean is asked not to rebuild those files.
The old flag should therefore not be used when consistency of the whole project is important (e.g. in CI), though it can speed up development.

### The `#exit` command and `.`

The command `#exit` will cause lean to stop reading the file at the location it is inserted.
This can be helpful when working on proofs in the middle of a file with many results or slow results below the current location.
This is related to switching to `check visible lines` mode, but gives the user more precise control over which parts of the file are slow.

Likewise when working at the start of a file Lean will recheck the import lines, this can be prevented by placing a `.` character (which delimits lean declarations) on a newline after the import lines.
This can also be useful in other situations when Lean wants to recheck things above the lemma or definition you are changing unnecessarily.
Another alternative here is to add a [module doc-string](contribute/doc.html#header-comment) after the imports which also has the effect of separating the start of the file from the code.

### Profiling proofs

Sometimes long proofs are slow to execute and isolating the slow tactic or subgoals in an attempt to refactor or speed them up is necessary.
The basic option to enable this is `set_option profiler true`, which will print out timing information for tactic execution.
Commenting out subproofs (with the sorry trick above) you can isolate the slow part of the proof and explore options for rewriting it.


### Avoiding many nested parentheses with `$`

Lean is a functional language that uses parentheses `(..)` as the basic tool for grouping terms together that should be evaluated first.
In the following lemma we have to use 5 sets of nested parentheses in order to tell Lean we want to repeatedly apply `or.inl` and `or.inr`, each of these only take one argument so the bracketing starts to feel a bit excessive.
```lean
lemma many_ors : false ∨ false ∨ false ∨ false ∨ false ∨ true ∨ false :=
or.inr (or.inr (or.inr (or.inr (or.inr (or.inl trivial)))))
```
Such proofs take up a lot of unnecessary space, and the parenthesis do not aid understanding when the function being applied only has one argument. Additionally, manually inserting the right amount of parentheses is tricky, and sometimes results in annoying to find errors.
The `$` symbol may be used in this situation to give a cleaner looking proof.
This symbol can be thought of as inserting a left parenthesis at the point of the `$` and then adding a closing right parenthesis as far right as possible.
In this case its use looks like
```lean
lemma many_ors : false ∨ false ∨ false ∨ false ∨ false ∨ true ∨ false :=
or.inr $ or.inr $ or.inr $ or.inr $ or.inr $ or.inl trivial
```

By as far right as possible we mean that in the following example
```lean
some_function (a $ really $ long $ chain $ of $ applications) another_argument
```
lean evaluates as `some_function (a (really (long (chain (of applications))))) another_argument` together as intended, as the outer set of brackets still limits the scope of the `$` symbol.
If we were to remove the parentheses here, Lean would interpret `another_argument` as an argument to `applications` rather than to `some_function`.

In the first example another even more succinct explicit term mode proof is possible via the use of dot notation.
```lean
lemma many_ors : false ∨ false ∨ false ∨ false ∨ false ∨ true ∨ false :=
(or.inl trivial).inr.inr.inr.inr.inr
```
Here `(...).inr` causes Lean to look at the type of the bracketed term, find that it is of the form `or _ _`, and therefore expand this into `or.inr (...)`, as this function is in the `or` namespace.
All steps in this proof are nested `or`s therefore we can repeatedly use dot notation to write this proof.

This style is used often in mathlib to write nested function applications when the namespaces allow for a lot of information to be inferred by Lean.
For instance if we want to say that 7 times the square of a continuous real-valued function is continuous we can use dot notation to give a very short but still readable proof:
```lean
lemma a (f : ℝ → ℝ) (hf : continuous f) : continuous (7 • f ^ 2) :=
(hf.pow 2).nsmul 7
```
rather than
```lean
continuous.nsmul (continuous.pow hf 2) 7
```
Using dot notation allows us to refer to namespaced declarations succinctly without having to open all namespaces (and thus run the risk of overridden names).
