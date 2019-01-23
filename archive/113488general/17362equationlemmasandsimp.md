---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17362equationlemmasandsimp.html
---

## Stream: [general](index.html)
### Topic: [equation lemmas and simp](17362equationlemmasandsimp.html)

---

#### [Sean Leather (Mar 01 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123126635):
What is the effect of putting `@[simp]` on a `def` defined with pattern-matching equations? Does it annotate the equation lemmas with `@[simp]`?

#### [Sean Leather (Mar 01 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123126899):
When I look at `#print <def-name>._main.equations._eqn_1`, it only has `@[_refl_lemma]`.

#### [Simon Hudon (Mar 01 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123126955):
what do you see if you look at the other equations? (see them listed in `#print prefix <def-name>`)

#### [Sean Leather (Mar 01 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127031):
I had to use a fully-qualified `<def-name>`, but that's a useful command:

```lean
#print prefix tts.typ.open
```
```lean
tts.typ.open : Π {V : Type}, list (typ V) → typ V → typ V
tts.typ.open._main : Π {V : Type}, list (typ V) → typ V → typ V
tts.typ.open._main._meta_aux : Π {V : Type}, list (typ V) → typ V → typ V
tts.typ.open._main.equations._eqn_1 : ∀ {V : Type} (ts : list (typ V)) (i : ℕ), typ.open._main ts (varb i) = option.get_or_else (list.nth ts i) (varb 0)
tts.typ.open._main.equations._eqn_2 : ∀ {V : Type} (ts : list (typ V)) (x : V), typ.open._main ts (varf x) = varf x
tts.typ.open._main.equations._eqn_3 : ∀ {V : Type} (ts : list (typ V)) (t₁ t₂ : typ V),
  typ.open._main ts (arr t₁ t₂) = arr (typ.open._main ts t₁) (typ.open._main ts t₂)
tts.typ.open._sunfold : Π {V : Type}, list (typ V) → typ V → typ V
tts.typ.open.equations._eqn_1 : ∀ {V : Type} (ts : list (typ V)) (i : ℕ), typ.open ts (varb i) = option.get_or_else (list.nth ts i) (varb 0)
tts.typ.open.equations._eqn_2 : ∀ {V : Type} (ts : list (typ V)) (x : V), typ.open ts (varf x) = varf x
tts.typ.open.equations._eqn_3 : ∀ {V : Type} (ts : list (typ V)) (t₁ t₂ : typ V),
  typ.open ts (arr t₁ t₂) = arr (typ.open ts t₁) (typ.open ts t₂)
```

#### [Simon Hudon (Mar 01 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127074):
What if you look at `#print tts.typ.open.equations._eqn_1 `?

#### [Sean Leather (Mar 01 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127075):
```lean
#print tts.typ.open.equations._eqn_1
```
```lean
@[_refl_lemma]
theorem tts.typ.open.equations._eqn_1 : ∀ {V : Type} (ts : list (typ V)) (i : ℕ), typ.open ts (varb i) = option.get_or_else (list.nth ts i) (varb 0) :=
λ {V : Type} (ts : list (typ V)), typ.open._main.equations._eqn_1 ts
```

#### [Simon Hudon (Mar 01 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127129):
That's curious. The effect I see is as if those equations were labeled with `simp`. I wonder if `simp` is implied by `_refl_lemma`

#### [Sean Leather (Mar 01 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127137):
`@[_refl_lemma]` is there whether or not I use `@[simp]`.

#### [Simon Hudon (Mar 01 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127138):
We can check something else:

```
run_cmd attribute.get_instances `simp >>= trace
```

#### [Simon Hudon (Mar 01 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127182):
Correction: 

```
run_cmd attribute.get_instances `simp >>= tactic.trace ∘ list.take 3
```

#### [Sean Leather (Mar 01 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127192):
```
parsing at line 7[tts.typ.open, finset.sort_to_finset, finset.sort_nodup]
```

#### [Sean Leather (Mar 01 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127237):
@**Simon Hudon**: What does that mean?

#### [Simon Hudon (Mar 01 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127248):
so the whole thing is labelled as `simp`. The `simp` tactic must have some logic to retrieve the equations related to a definition.

#### [Sean Leather (Mar 01 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127256):
Could be.

#### [Simon Hudon (Mar 01 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127303):
`attribute.get_instance ```simp``` ` gives you the list of the names that are labelled with `simp`. It works with any attribute. Every definition is appended at the beginning so taking only 3 of them was enough and I wanted to see if more than one name was being labelled

#### [Sean Leather (Mar 01 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127356):
`library/init/meta/simp_tactic.lean`:
```lean
/-- `get_eqn_lemmas_for deps d` returns the automatically generated equational lemmas for definition d.
   If deps is tt, then lemmas for automatically generated auxiliary declarations used to define d are also included. -/
meta constant get_eqn_lemmas_for : bool → name → tactic (list name)
```

#### [Simon Hudon (Mar 01 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127357):
```quote
Could be.
```
It could mean that the behavior can differ from that of using `simp` lemma or it could just be a way of compressing the list of `simp` lemmas.

#### [Simon Hudon (Mar 01 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127361):
Nice! Thanks!

#### [Sean Leather (Mar 01 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127419):
This is with `set_option trace.simplify true`:

```
3. [simplify.rewrite] [tts.typ.open.equations._eqn_3]: typ.open ts (arr t₁_a t₁_a_1) ==> arr (typ.open ts t₁_a) (typ.open ts t₁_a_1)
[simplify] eq: typ.open ts t₁_a
[simplify] eq: ts
[simplify] eq: t₁_a
[simplify] eq: typ.open
```

#### [Sean Leather (Mar 01 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127526):
So, it seems to be that `simp` uses the equation lemmas if a `def` is annotated with `@[simp]`. This makes me wonder why more definitions in the standard library and mathlib aren't `@[simp]`. It also makes me wonder if I should use `@[simp] def` more instead of writing equation lemmas myself.

#### [Sean Leather (Mar 01 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127584):
`library/init/meta/interactive.lean`:
```lean
private meta def simp_lemmas.resolve_and_add (s : simp_lemmas) (u : list name) (n : name) (ref : pexpr) : tactic (simp_lemmas × list name) :=
do
  p ← resolve_name n,
  check_no_overload p,
  -- unpack local refs
  let e := p.erase_annotations.get_app_fn.erase_annotations,
  match e with
  | const n _           :=
    (do b ← is_valid_simp_lemma_cnst n, guard b, save_const_type_info n ref, s ← s.add_simp n, return (s, u))
    <|>
    (do eqns ← get_eqn_lemmas_for tt n, guard (eqns.length > 0), save_const_type_info n ref, s ← add_simps s eqns, return (s, u))
    <|>
    (do env ← get_env, guard (env.is_projection n).is_some, return (s, n::u))
    <|>
    report_invalid_simp_lemma n
  | _ :=
    (do e ← i_to_expr_no_subgoals p, b ← is_valid_simp_lemma e, guard b, try (save_type_info e ref), s ← s.add e, return (s, u))
    <|>
    report_invalid_simp_lemma n
  end
```

#### [Simon Hudon (Mar 01 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127639):
To your second question: I think you should, it's often less repetitive

#### [Simon Hudon (Mar 01 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123127642):
I don't know how to answer your first question

#### [Sebastian Ullrich (Mar 01 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131391):
There's also `#print attribute simp`

#### [Sebastian Ullrich (Mar 01 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131399):
I believe Leo rather wants us to use `simp!` than to tag every single def with `[simp]`

#### [Sean Leather (Mar 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131449):
```quote
There's also `#print attribute simp`
```
`error: invalid #print command`

#### [Sebastian Ullrich (Mar 01 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131615):
Ah, this is fun. You can do `#print [refl]`, but not `#print [simp]`.

#### [Sean Leather (Mar 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131630):
[`simp!`](https://github.com/leanprover/lean/commit/368f17d0b1392a5a72c9eb974f15b14462cc1475#diff-f5ed07a9ca7e18052989b6ce28b7eb30):
```quote
* Add `iota_eqn : bool` field to `simp_config`. `simp {iota_eqn := tt}` uses all non trivial equation lemmas generated by equation/pattern-matching compiler. A lemma is considered non trivial if it is not of the form `forall x_1 ... x_n, f x_1 ... x_n = t` and a proof by reflexivity. `simp!` is a shorthand for `simp {iota_eqn := tt}`. For example, given the goal `... |- [1,2].map nat.succ = t`, `simp!` reduces the left-hand-side of the equation to `[nat.succ 1, nat.succ 2]`. In this example, `simp!` is equivalent to `simp [list.map]`.
```

#### [Moses Schönfinkel (Mar 01 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131668):
Getting closer to Coq `cbn` :).

#### [Sean Leather (Mar 01 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131694):
“non-trivial equation lemmas” - What does this imply about the trivial equation lemmas, which all of mine probably are?

#### [Sean Leather (Mar 01 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131778):
```quote
Ah, this is fun. You can do `#print [refl]`, but not `#print [simp]`.
```
Is that just a matter of forgetting to include `simp` somewhere?

#### [Sean Leather (Mar 01 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131796):
`#print [_refl_lemma]` works.

#### [Sebastian Ullrich (Mar 01 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131840):
No, `#print [simp]` is just a different syntax https://github.com/leanprover/lean/blob/39270fd46f49fecb30649f5ec527da7bbd4cdb13/tests/lean/run/simplifier_custom_relations.lean#L23

#### [Sebastian Ullrich (Mar 01 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131843):
So yeah, `#print [simp] default` works

#### [Sean Leather (Mar 01 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131887):
```quote
“non-trivial equation lemmas” - What does this imply about the trivial equation lemmas, which all of mine probably are?
```
Considering [this comment](httpsf//github.com/leanprover/lean/commit/368f17d0b1392a5a72c9eb974f15b14462cc1475#diff-f3c3d54612bd08c035a1578e952b2aeaR216), I think the description in `doc/changes.md` above is either confusing or misleading:
```diff
+(iota_eqn : bool           := ff) -- reduce using all equation lemmas generated by equation/pattern-matching compiler
```

#### [Sebastian Ullrich (Mar 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131894):
No, "non-trivial" basically means "defined by pattern matching"

#### [Sebastian Ullrich (Mar 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131895):
I.e. "more than one equation"

#### [Sean Leather (Mar 01 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123131966):
So, could you replace “*non trivial equation lemmas generated by equation/pattern-matching compiler. A lemma is considered non trivial if it is not of the form `forall x_1 ... x_n, f x_1 ... x_n = t` and a proof by reflexivity*” above with “*equation lemmas generated by equation/pattern-matching compiler*” and the statement would be the same?

#### [Sebastian Ullrich (Mar 01 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123132241):
I'm not sure anymore. Perhaps the `iota_eqn` comment should instead be extended with a "non-trivial"

#### [Sean Leather (Mar 01 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123132382):
```quote
So yeah, `#print [simp] default` works
```
Yeah, it's nice to see my equation lemmas appear in that list after adding `@[simp]` to a `def`.

#### [Sean Leather (Mar 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123132395):
I'm not sure if there are any alternative arguments to `#print [simp]`. It doesn't appear to take a prefix or identifier name: `unknown simp_lemmas collection`.

#### [Sean Leather (Mar 01 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123133132):
I get syntax errors on the second `simp!` in `induction xs; [simp!, {cases ts, simp!}]`.

#### [Sean Leather (Mar 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123133208):
But `induction xs; [simp!, {cases ts, simp {iota_eqn := tt}}]` works.

#### [Sebastian Ullrich (Mar 01 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20lemmas%20and%20simp/near/123133979):
`!}` is a separate token used for hole commands

