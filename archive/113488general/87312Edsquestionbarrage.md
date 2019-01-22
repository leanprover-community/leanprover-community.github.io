---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87312Edsquestionbarrage.html
---

## [general](index.html)
### [Ed's question barrage](87312Edsquestionbarrage.html)

#### [Edward Ayers (Aug 11 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131947644):
Massive thanks to @**Mario Carneiro** for helping me. I'll buy you beers next time we are in the same physical location to within 100m.

#### [Edward Ayers (Aug 11 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948511):
In the constructor for `mvar` for `expr`, are the arguments pretty name, unique name, type? You said that `local_const`s type argument shouldn't be trusted because its sometimes a placeholder. Is that true for `mvar`s type arg too?

#### [Edward Ayers (Aug 11 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948744):
Also in `expr` what is `macro` used for?

#### [Edward Ayers (Aug 11 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948754):
Are they macros in the same sense as C macros?

#### [Mario Carneiro (Aug 11 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948868):
I am not sure about the reliability of `mvar` types; they aren't found in the local context so probably that's the only place the data is stored, meaning it has to be reliable

#### [Mario Carneiro (Aug 11 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948870):
still, `infer_type` should always work

#### [Mario Carneiro (Aug 11 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948884):
`expr.macro` is a C++ thing. Those are basically "promises" to build an expr by some C++ code, you can't build them in lean

#### [Mario Carneiro (Aug 11 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948888):
You can unfold a macro and force it to evaluate

#### [Mario Carneiro (Aug 11 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948951):
They are used for `sorry`, meta recursive calls (which are not compiled to recursors like the non-meta versions), builtin projections, and they also are ephemeral structures in some specialized tactics

#### [Edward Ayers (Aug 11 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949182):
What are some examples of meta recursive calls?

#### [Mario Carneiro (Aug 11 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949189):
`meta def rec := rec`

#### [Mario Carneiro (Aug 11 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949232):
```
meta def rec : nat -> nat | x := rec (x + 1)
```

#### [Edward Ayers (Aug 11 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949263):
What is a builtin projection?

#### [Mario Carneiro (Aug 11 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949560):
```
structure foo := (mynat : ℕ)
#print foo.mynat

-- @[reducible]
-- def foo.mynat : foo → ℕ :=
-- λ (c : foo), [foo.mynat c]
```
the thing in brackets is a macro

#### [Edward Ayers (Aug 11 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949625):
cool

#### [Edward Ayers (Aug 11 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949675):
I am reading `decalaration.lean`. And I came across
```quote
Reducibility hints are used in the convertibility checker.
When trying to solve a constraint such a

           (f ...) =?= (g ...)

where f and g are definitions, the checker has to decide which one will be unfolded.
  If      f (g) is opaque,     then g (f) is unfolded if it is also not marked as opaque,
  Else if f (g) is abbrev,     then f (g) is unfolded if g (f) is also not marked as abbrev,
  Else if f and g are regular, then we unfold the one with the biggest definitional height.
  Otherwise both are unfolded.
```
Is there a way I can get programmatic access to the "definitional height" of a declaration (other than expanding it and calculating it myself)?

#### [Edward Ayers (Aug 11 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949878):
Ah it's an argument to `regular`

#### [Edward Ayers (Aug 11 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949886):
sorry was on the next line.

#### [Edward Ayers (Aug 11 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131950012):
So to get the definitional height you would do
```lean
env <- tactic.get_env
defn _ _ _ _ (regular h _ _) _  <- environment.get env my_name
return h
```

#### [Edward Ayers (Aug 11 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131950392):
Is the convertability checker the same thing as the unifier?

#### [Edward Ayers (Aug 11 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131950628):
What's the best way of adding some arbitrary data to the environment?. Eg, I've calculated a table for a tactic and I don't want to regenerate this table for every invocation of the tactic, I just want to retrieve it from the environment somehow.

#### [Mario Carneiro (Aug 11 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951039):
You can make a `def` containing the data

#### [Edward Ayers (Aug 11 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951102):
makes sense.

#### [Edward Ayers (Aug 11 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951113):
That is so much more straightforward than the Isabelle way!

#### [Mario Carneiro (Aug 11 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951119):
your ability to store arbitrary data in the environment is limited; for the most part it's just `expr`s

#### [Mario Carneiro (Aug 11 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951166):
Ideally you would want to store any vm_obj in the environment, but I don't know any way to do that besides reflecting it to an expr

#### [Edward Ayers (Aug 11 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951168):
I'd make a def with `mk_local_def` right?

#### [Mario Carneiro (Aug 11 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951181):
no, that's for local constants

#### [Edward Ayers (Aug 11 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951225):
`add_meta_definition`?

#### [Mario Carneiro (Aug 11 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951229):
oh, I didn't know that one was there, that's useful

#### [Mario Carneiro (Aug 11 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951230):
yes

#### [Edward Ayers (Aug 11 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951295):
When I reflect to an `expr`, that means it actually has to build an `expr` tree which represents the data in some way right? It sounds like one would get performance issues if you wanted to save a gigantic rewrite table or similar.

#### [Mario Carneiro (Aug 11 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951461):
The `simp_lemmas` data structure is designed for handling big rewrite tables

#### [Mario Carneiro (Aug 11 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951519):
You can cache data in special types inside user attributes as well

#### [Edward Ayers (Aug 11 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131952210):
`simp_lemmas` looks good but I can only access the data through calls to `simp_lemmas.rewrite` so I am stuck with `simp`s implementation. Not necessarily a showstopper but I can't retrieve arbitrary exprs from it.

#### [Edward Ayers (Aug 11 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131952213):
Please could you give some examples of this?
```quote
You can cache data in special types inside user attributes as well
```

#### [Mario Carneiro (Aug 11 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131952632):
I'm referring to the `cache_ty` and `param_ty` in `user_attribute`, but it's not really a solution - `param_ty` has to be reflectable (so it is probably just stored as an `expr`) and `cache_ty` needs to be pure-functionally created from the list of all defs with the attribute in the environment (so it can only depend on things that are ultimately `expr`s). Still that cache has some promise

#### [Mario Carneiro (Aug 11 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131953023):
I'm not positive this is actually working the way you would want, but here's the general idea:
```
structure mydata := (n : nat)

@[user_attribute]
meta def mydata_attr : user_attribute (name_map mydata) unit :=
{ name := `mydata, descr := "stuff",
  cache_cfg := ⟨λ l, l.mfoldl (λ m n, do
    d ← get_decl n,
    v ← eval_expr mydata d.value,
    return (m.insert n v)) (name_map.mk _), []⟩ }

@[mydata] def X : mydata := ⟨500^2⟩

run_cmd do
  m ← mydata_attr.get_cache,
  v ← m.find ``X,
  trace v.n
```

#### [Edward Ayers (Aug 11 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131954639):
- In `pexpr`, has it already disambiguated overloaded operators such as `+`

#### [Edward Ayers (Aug 11 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131954645):
- is the process `pexpr -> expr` called "elaboration"?

#### [Edward Ayers (Aug 11 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131954830):
- Filling in the implicit arguments of a `pexpr` is the same problem as finding a proof. So does it make sense to think of the process `pexpr -> expr` as a kind of tactic driven by the structure of the `pexpr`?

#### [Edward Ayers (Aug 11 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131954891):
- It seems that you can't do `pexpr -> expr` without recursively infering the types of the subpexprs of the `pexpr`. Is this right? In which case why not cache all of the types and then you never have to call `infer_type`? My guess would be that it would take up too much space.

#### [Edward Ayers (Aug 11 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131955082):
- Why does the `eval_expr α e` tactic need to be given the type of `e` as well?

#### [Edward Ayers (Aug 11 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131955226):
- Is the `target` tactic the same as `get_goals >>= (list.head >> return)`?

#### [Edward Ayers (Aug 11 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131955636):
- The definition of `intro` is
```lean
meta def intro (n : name) : tactic expr :=
do t ← target,
   if expr.is_pi t ∨ expr.is_let t then intro_core n
   else whnf_target >> intro_core n
```
But I can't figure out what I am doing wrong in the last two examples below:
```lean
example : a -> b -> a :=
begin
    intro hello,
    sorry
end

example : a -> b -> a :=
begin
    intro_core hello, -- errors here "unknown identifier 'hello'"
    sorry
end

example : a -> b -> a :=
begin
    whnf_target,
    intro_core hello, -- errors here "unknown identifier 'hello'"
    sorry
end
```

#### [Edward Ayers (Aug 11 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956067):
- Does `get_unused_name n` just check if `n` is currently being used, and if not, sticks an `_1`/ `_2`/... on the end?

#### [Edward Ayers (Aug 11 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956115):
- If I invoke `local_context`, will that always be a list of `local_const`s or are there ways of getting other forms of `expr` in the context?

#### [Rob Lewis (Aug 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956118):
I can try to save Mario some time and answer a few of these....
```quote
- In `pexpr`, has it already disambiguated overloaded operators such as `+`
```
No. But note that `+` isn't "overloaded," exactly. `+` is notation for `has_add.add` which applies to any type with a `has_add` type class instance. A `pexpr` using `+` hasn't filled in the implicit type or the instance yet. And for notation that really is overloaded, a `pexpr` will represent the ambiguity with a macro, I think.

#### [Rob Lewis (Aug 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956125):
```quote
- is the process `pexpr -> expr` called "elaboration"?
```
Yes.

#### [Rob Lewis (Aug 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956131):
```quote
- Filling in the implicit arguments of a `pexpr` is the same problem as finding a proof. So does it make sense to think of the process `pexpr -> expr` as a kind of tactic driven by the structure of the `pexpr`?
```
Yeah, I guess. Notice the tactic `to_expr` does exactly this.

#### [Rob Lewis (Aug 11 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956175):
```quote
- It seems that you can't do `pexpr -> expr` without recursively infering the types of the subpexprs of the `pexpr`. Is this right? In which case why not cache all of the types and then you never have to call `infer_type`? My guess would be that it would take up too much space.
```
Are you asking why each `expr` object doesn't store its type? Yeah, this would take up a huge amount of space.

#### [Rob Lewis (Aug 11 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956234):
```quote
- Why does the `eval_expr α e` tactic need to be given the type of `e` as well?
```
I'm not 100% clear on how `eval_expr` works, but here's my intuition, anyway. If you didn't give the expected type, you'd have to "guess" it by inferring the type of `e`, which would give you an `expr`, not a type. You need a way to go from this `expr` to a type, which is why you have the `[reflected α]` instance.

#### [Kevin Buzzard (Aug 11 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956301):
```lean
example : a -> b -> a :=
begin
    intro_core hello, -- errors here "unknown identifier 'hello'"
    sorry
end
```

#### [Rob Lewis (Aug 11 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956302):
```quote
- Is the `target` tactic the same as `get_goals >>= (list.head >> return)`?
```
I think, roughly. It's the type of the first goal metavariable.

#### [Rob Lewis (Aug 11 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956314):
```quote
- The definition of `intro` is
```lean
meta def intro (n : name) : tactic expr :=
do t ← target,
   if expr.is_pi t ∨ expr.is_let t then intro_core n
   else whnf_target >> intro_core n
```
But I can't figure out what I am doing wrong in the last two examples below:
```lean
example : a -> b -> a :=
begin
    intro hello,
    sorry
end

example : a -> b -> a :=
begin
    intro_core hello, -- errors here "unknown identifier 'hello'"
    sorry
end

example : a -> b -> a :=
begin
    whnf_target,
    intro_core hello, -- errors here "unknown identifier 'hello'"
    sorry
end
```
```
You've noticed the difference between the tactic monad and "interactive mode." When you're using tactics for proofs, in begin/end blocks, they get parsed differently than when you're writing tactics. The `intro` in begin/end is actually tactic.interactive.intro.

#### [Edward Ayers (Aug 11 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956358):
```quote
I think, roughly. It's the type of the first goal metavariable.
```
The docs for `target` confused me because they say it returns the "main goal" but this seems to always be the first goal.

#### [Rob Lewis (Aug 11 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956359):
`intro_core` isn't an interactive tactic. It expects a name, which you'd have to give in the form `` `hello ``.

#### [Rob Lewis (Aug 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956373):
`tactic.intro` expects the same. `tactic.interactive.intro` expects some text to follow that it will parse into a name.

#### [Kevin Buzzard (Aug 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956386):
```lean
example : a -> b -> a :=
begin
    intro_core hello, -- errors here "unknown identifier 'hello'"
    sorry
end
```

The `intro` in a `begin end` block is `tactic.interactive.intro`not `tactic.intro`. I don't know if this helps or whether you're already way ahead of this, but it was something that confused me for a while.

PS just beaten to it by Rob :-)

#### [Mario Carneiro (Aug 11 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956462):
the "main goal" is the first goal

#### [Rob Lewis (Aug 11 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956469):
```quote
- If I invoke `local_context`, will that always be a list of `local_const`s or are there ways of getting other forms of `expr` in the context?
```
I think it's only `local_const` exprs, yes.

#### [Rob Lewis (Aug 11 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956568):
```quote
- Does `get_unused_name n` just check if `n` is currently being used, and if not, sticks an `_1`/ `_2`/... on the end?
```
This one I'm not sure, I've never really paid attention. It will give you a name that starts with `n` that won't conflict with anything.

#### [Mario Carneiro (Aug 11 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956570):
> Why does the eval_expr α e tactic need to be given the type of e as well?

This is done for typechecking purposes. You are given `e` which is an `expr`, but you want to return something of type `α`. What is `α`? You would need to have a function `e.type : expr -> Type` to define "the type of `e`", but that doesn't work because of universe issues. So instead you just assert the type you want and lean checks it (I think, maybe it just crashes if you got it wrong)

#### [Kevin Buzzard (Aug 11 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956630):
could `has_one.one` be an example of an `expr`? Or some such thing? I'm wondering when Lean decides that `1` should be a natural if it can't think of any better ideas.

#### [Mario Carneiro (Aug 11 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956680):
`has_one.one` has a big pi type, but `` `(has_one.one)`` is an expr

#### [Rob Lewis (Aug 11 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956690):
I think it's specifically numerals that default to `nat` if there's no other information, right? This happens at elaboration time.

#### [Edward Ayers (Aug 11 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131962977):
What's the best way to discover if `expr` e has form `Exists (a : A), B a`? Or alternatively `Exists p`?

#### [Simon Hudon (Aug 11 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131963019):
One simple way is to do:

```lean
do `(Exists %%p) <- pure e | fail "e is in bad shape",
       -- do stuff with `p`
```

#### [Edward Ayers (Aug 12 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131999207):
- Am I right in thinking that `rbtree` doesn't come with function to remove items from it?

#### [Mario Carneiro (Aug 12 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131999315):
I... guess you're right

#### [Mario Carneiro (Aug 12 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131999368):
that's a bit annoying, I was hoping not to have to touch `rbtree`

#### [Edward Ayers (Aug 12 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132001112):
Could I use `rb_map`, which does have this?

#### [Edward Ayers (Aug 12 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132002458):
If I do `a <|> b` for the `option` type, will the VM not evaluate `b` if `a` is `some _`?

#### [Edward Ayers (Aug 12 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132004998):
Is anyone doing 23 trees in mathlib?

#### [Edward Ayers (Aug 12 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132005004):
I've started coding it up

#### [Kevin Buzzard (Aug 12 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132005866):
Is it maths?

#### [Edward Ayers (Aug 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132006154):
It's a datastructure

#### [Edward Ayers (Aug 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132006159):
like rbtree

#### [Edward Ayers (Aug 13 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132012981):
Is there a way to have conditionals in `match` statements? Eg something like:
```lean
match x with
|(some y)  where  y > 5 := "hello"
|_ := "nope"
end
```

#### [Simon Hudon (Aug 13 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132013028):
`"nope"`

#### [Simon Hudon (Aug 13 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132013031):
No conditions built into `match`

#### [Mario Carneiro (Aug 13 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132015917):
> If I do a <|> b for the option type, will the VM not evaluate b if a is some _?

It will evaluate both sides, unless `option.orelse` is inlined. If you want to avoid this, you can make an `option.orelse'` that takes a `thunk (option A)` for its second argument

#### [Mario Carneiro (Aug 13 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132015937):
> Is anyone doing 23 trees in mathlib? I've started coding it up

I have no current plans for this, go ahead. We would be happy to take it

#### [Mario Carneiro (Aug 13 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132015940):
> Is there a way to have conditionals in match statements?

No, as Simon said; although in this case you can write the following:
```
match x with
| (some (y+6)) := "hello"
| _ := "nope"
end
```
I would recommend just using `if` though.

#### [Patrick Massot (Aug 13 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132015956):
What if he gets tired towards the middle of the task, and ends up with 11 trees instead of 23?

#### [Simon Hudon (Aug 13 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016137):
That's a linked list. We won't be so welcoming because we have those.

#### [Patrick Massot (Aug 13 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016190):
Damn it. What was the probability that roughly cutting in half the number 23 would lead to another meaningful sentence?

#### [Simon Hudon (Aug 13 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016191):
Btw, why do we want 2-3 trees while we have red-back trees? What do you get from 2-3 trees that you don't get from red-black trees?

#### [Mario Carneiro (Aug 13 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016192):
I guess with 12 trees he will have a trie

#### [Mario Carneiro (Aug 13 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016239):
different performance characteristics... I'm okay with implementing datastructures for their own sake because of this

#### [Mario Carneiro (Aug 13 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016289):
but it's true that rb trees already implement the same API as it were, so if you are a programmer who needs a map type and doesn't want to bother with writing data structures you can use them instead

#### [Simon Hudon (Aug 13 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016293):
As I understand it, a red-black tree is basically a 2-3 tree where the balancing invariant is formulated in terms of tree height instead of node degree, that's why I'm surprised it would get a different performance profile

#### [Mario Carneiro (Aug 13 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016412):
From https://www.cs.purdue.edu/homes/ayg/CS251/slides/chap13b.pdf , it seems like 2-3 trees or 2-3-4 trees are actually just simpler versions of rb trees

#### [Mario Carneiro (Aug 13 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016455):
the advantage of rb trees is normalizing the node layout, but this doesn't matter when you are writing inductives in lean

#### [Sebastian Ullrich (Aug 13 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016680):
Huh, that's an interesting slide format

#### [Kevin Buzzard (Aug 13 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132037220):
```quote
Huh, that's an interesting slide format
```
Judging by the name of the pdf, this might be a chapter from a book, and books are still traditionally in portrait format I guess.

#### [Gabriel Ebner (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132038925):
Those are definitely slides, but more like old-school ones for overhead projectors.

#### [Patrick Massot (Aug 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132038975):
Maybe Sebastian was referring to the Batman delirium at the end

#### [Edward Ayers (Aug 13 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062075):
Yes I'm just treating making 23 trees as another exercise. I copied the implementation details from Isabelle and then added dependent types to it. I managed to prove that my trees are balanced using just dependent types (each node has a height param in its type). It was fun to see that it worked and I learned a lot. I made no considerations for performance so `rbtree` is still better and more concise. The deletion algo for 23 trees is horrifying so there is likely a mistake in there, but at least I proved that it's balanced!

Here is a link to the source but I've made no attempt to make it readable yet. I haven't even tested it. 
https://github.com/EdAyers/mathlib/blob/tree23/data/tree23.lean

Some thoughts from doing this,
- It can be difficult to decide which typeclasses to use. Should I use `linear_order`? `decidable_rel`? And so on.
- The coercions from `decidable` to if statements are kind of magical.
-  There is a lemma `lt_min_key_imp_outside` which I basically did by taking a random walk through the space of valid tactics until `no goals` appeared. Any tips on how this can be tightened up would be appreciated.
- Proving anything about the `del` method will be a nightmare. So if the deletion method for rb trees is simpler then I am happy to abandon these.
- The main thing I learnt is that you are much better off using non-dependent-type driven datatypes and then restricting with propositions at the end. Using dependent types just makes coding too tedious.

#### [Edward Ayers (Aug 13 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062193):
I also had an attempt at proving some things about `rbtree`s but it is very tedious. I think that I am not using the automation very effectively.

#### [Edward Ayers (Aug 13 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062277):
I'm going to use `native.rb_tree` in the future instead, but I don't regret implementing this because it taught me a lot about Lean.

#### [Edward Ayers (Aug 13 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062574):
My dream was that I wouldn't have to write tests for my code, because I could just prove that it is correct!

#### [Simon Hudon (Aug 13 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062764):
Have you put your code somewhere on github. We can look at it to see if we can make your proving more effective

#### [Edward Ayers (Aug 13 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062860):
yes see link above in this thread

#### [Edward Ayers (Aug 13 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062870):
https://github.com/EdAyers/mathlib/blob/tree23/data/tree23.lean

#### [Edward Ayers (Aug 13 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062916):
I'll push the rbtree experiments in a few hours.

#### [Edward Ayers (Aug 15 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132190818):
Why is it that `#check λ x, x + 1` is ` ℕ → ℕ` and not `[has_add ?m] [has_one ?m] ?m -> ?m`

#### [Edward Ayers (Aug 15 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132190837):
What is causing the elaborator to default to `nat`?

#### [Bryan Gin-ge Chen (Aug 15 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132190906):
(deleted)

#### [Kenny Lau (Aug 15 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132190908):
I think `1` is default to `nat`

#### [Edward Ayers (Aug 15 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191067):
Right but where is the defaultness set?

#### [Kevin Buzzard (Aug 15 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191292):
At some point in the elaboration process, Lean *sometimes* says "if I can't figure out what that 1 is, I'm going to assume it's a nat". I think the point this occurs is near the end, if at all. Maybe you can even concoct something where `example` behaves differently to `definition` using this sort of thing.

#### [Kevin Buzzard (Aug 15 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191371):
(deleted nonsense)

#### [Edward Ayers (Aug 15 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191517):
Perhaps `1` is always `nat`, and there is a type coercion from `nat` to all of the other kinds of numbers?

#### [Kevin Buzzard (Aug 15 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191535):
That's not how it works, I'm pretty sure.

#### [Kevin Buzzard (Aug 15 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191555):
Unfortunately, as I found out earlier this week, it's very difficult to switch the number literal parser off.

#### [Kevin Buzzard (Aug 15 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191572):
`1` is `has_one.one`

#### [Edward Ayers (Aug 15 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191626):
The thing I can't figure out is if the `nat` default is set somewhere in `init` or whether it is baked in to the elaborator.

#### [Kevin Buzzard (Aug 15 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191902):
I think it is baked into the elaborator. I think that `#check` cannot possibly return `[has_add ?m] [has_one ?m] ...` because I don't think Lean thinks these are part of the expression.

#### [Kevin Buzzard (Aug 15 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191960):
So eventually it gets to a point where it can't figure out where this type class inference thing is coming from and at that point it decides it's going to go for nat. You should check all this with an expert.

#### [Mario Carneiro (Aug 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132192958):
The nat default is baked into the elaborator, but it is not necessary for it to operate

#### [Mario Carneiro (Aug 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132192998):
it could just as easily return `?m -> ?m`, and there would be (hidden) subgoals for those typeclasses

#### [Mario Carneiro (Aug 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132193030):
> Perhaps 1 is always nat, and there is a type coercion from nat to all of the other kinds of numbers?

Lean used to work like this, but the current version uses a polymorphic 1 function

#### [Mario Carneiro (Aug 15 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132193177):
I find the nat default distateful precisely because it's the only thing about lean definitions which is not configured within lean

#### [Mario Carneiro (Aug 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132193240):
if kevin decided to write his own core.lean with `xnat`, lean would probably complain

#### [Mario Carneiro (Aug 15 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132193396):
https://github.com/leanprover/lean/blob/master/src/frontends/lean/elaborator.cpp#L3609-L3610

#### [Edward Ayers (Aug 16 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132241830):
I can see why Leo did this though, since `nat` is initial with respect to `has_one` and `has_add` so you don't really lose any generality by doing this and 90% of the time you mean `nat` anyway.

#### [Mario Carneiro (Aug 16 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242032):
note again that lean does *not* use anything like `nat.cast` to get an arbitrary value of type `A` from a nat

#### [Mario Carneiro (Aug 16 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242070):
If you type `4 : A`, it is translated by the parser to `bit0 (bit0 1)`, where `bit0` and `has_one.one` are polymorphic functions

#### [Mario Carneiro (Aug 16 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242083):
this term will make absolutely no reference to `nat`

#### [Mario Carneiro (Aug 16 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242194):
The reason this was done, I believe, is that without a default type being assigned as a last resort, you can never write a numeral without a type ascription somewhere, so a beginner will type `#eval 2 + 2` and get a weird error message instead of the obvious answer

#### [Edward Ayers (Aug 16 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242196):
What is the difference between synthesizing and elaborating?

#### [Edward Ayers (Aug 16 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242261):
My guess is synthesizing is when the elaborator tries to guess an expr for a given type sig

#### [Mario Carneiro (Aug 16 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242270):
I'm not sure there is a difference, they are both fairly general terms

#### [Mario Carneiro (Aug 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242360):
elaboration is broadly the process of taking a parsed pre-expression, an AST, and including and inferring all missing type information to make it a valid term of the formal logic

#### [Mario Carneiro (Aug 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242385):
synthesis is just what you call putting data into one of these holes

#### [Edward Ayers (Aug 16 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242406):
Ok. So when you make the proof to a lemma by writing out a proof term. Making that a valid `expr` is elaboration. Does the process of making a valid proof term using `begin ... end` also count as elaboration?

#### [Mario Carneiro (Aug 16 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242407):
There are multiple methods used by the elaborator to synthesize expressions, but the major workhorses are unification and typeclass inference

#### [Mario Carneiro (Aug 16 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242482):
I'm not sure I would call tactic evaluation a part of elaboration, but it occurs in the middle of the elaboration cycle, yes

#### [Mario Carneiro (Aug 16 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242512):
you could view the tactic framework as a giant plugin to the elaborator

#### [Edward Ayers (Aug 16 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242526):
Yes that's how I'm viewing it. It's a beautiful way of doing it.

#### [Edward Ayers (Aug 16 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242701):
When I write `def asdf (myarg : mytype . mytactic) : ... := ...`. I can't quite figure out what the tactic is doing. Is Lean making a tactic state with the goal as `mytype` and `myarg` as a local constant?

#### [Edward Ayers (Aug 16 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242779):
So I use this by writing `asdf (myvalue)`. Or is the idea that the `mytactic` should be used to synthesize `myarg` if it is not provided explicitly?

#### [Edward Ayers (Aug 16 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243188):
Also, `expr` has the argument `elaborated := tt`. I am guessing that `expr tt` is a term that has been elaborated, and hence is valid. Whereas a `expr ff` has not been checked to be valid, eg I just made a nonsense term myself from the `expr` constructors. So `expr ff`/`expr tt` is like `term`/`cterm` in Isabelle.

#### [Edward Ayers (Aug 16 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243213):
But then I can make `expr tt` from the `expr` constructors too, so that can't be it.

#### [Edward Ayers (Aug 16 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243275):
But in that case I can't see what the difference could be between `expr tt` and `expr ff`.

#### [Mario Carneiro (Aug 16 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243775):
> Or is the idea that the mytactic should be used to synthesize myarg if it is not provided explicitly?

this

#### [Mario Carneiro (Aug 16 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243807):
it is a variant on optional parameters where the default value is synthesized by a tactic

#### [Mario Carneiro (Aug 16 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243887):
> Whereas a expr ff has not been checked to be valid, eg I just made a nonsense term myself from the expr constructors. 

Not quite. `expr ff` is the same as `pexpr`, and it represents those pre-expressions I mentioned

#### [Edward Ayers (Aug 16 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243924):
So an `expr ff` can have wildcard holes in it?

#### [Mario Carneiro (Aug 16 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243941):
They actually differ from `expr` structurally, i.e. if I write `x + y` then the `pexpr` for this is `has_add.add x y` with 2 arguments, and the `expr` is `has_add.add ?m1 ?m2 x y` or `has_add.add nat nat.has_add x y` with 4 arguments

#### [Edward Ayers (Aug 16 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244028):
nice

#### [Mario Carneiro (Aug 16 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244041):
they could have been defined as separate inductive types, but they share enough of the major structure that it seemed redundant

#### [Mario Carneiro (Aug 16 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244073):
lean 4 will have these separate, with `pexpr` becoming `syntax` which is completely different

#### [Mario Carneiro (Aug 16 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244129):
it will be much more like an AST for lean

#### [Edward Ayers (Aug 16 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244157):
Ah I just found `@[reducible] meta def pexpr := expr ff` in source

#### [Edward Ayers (Aug 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244276):
`meta constant pexpr.mk_placeholder : pexpr` seems to be the magic `constant` that lets you do placeholders. You can't use metavariables because you might not be in a tactic monad so you can't make fresh ones.

#### [Mario Carneiro (Aug 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244306):
mk_placeholder is basically the AST corresponding to `_` as a token

#### [Edward Ayers (Aug 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244319):
Am I right in thinking that *the* placeholder is distinct from metavars, but elaborating a `pexpr` turns these into metavars?

#### [Mario Carneiro (Aug 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244328):
there is only one, and it is elaborated to a new metavariable every time

#### [Edward Ayers (Aug 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244555):
Will the elaborator for Lean 4 be written in Lean rather than C++?

#### [Mario Carneiro (Aug 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244569):
parser yes, elaborator maybe

#### [Edward Ayers (Aug 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244612):
That would blow my mind

#### [Mario Carneiro (Aug 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244634):
I think the idea is to completely self host

#### [Edward Ayers (Aug 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244638):
I can't wait for Lean 4

#### [Mario Carneiro (Aug 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244653):
but it's hard, not the least because the lean VM is currently not efficient enough to support this

#### [Mario Carneiro (Aug 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244670):
so they will need to implement a real lean compiler to machine code

#### [Edward Ayers (Aug 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244677):
To do the elaborator in Lean you would need some kind of super simple bootstrap elaborator in C++ with everything explicit and build up from there.

#### [Mario Carneiro (Aug 16 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244767):
even in core lean for much of the files you don't have the tactic framework set up yet so it's all explicit terms

#### [Mario Carneiro (Aug 16 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244804):
I don't know exactly how the full bootstrap process would work, it might just run itself on the previous version of lean to avoid messy business

#### [Edward Ayers (Aug 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244873):
Right but then you can't build Lean from scratch which would be sad, you would then need to maintain both C++ and Lean elaborators.

#### [Mario Carneiro (Aug 16 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132245452):
@**Sebastian Ullrich** can tell you more about the extent of current bootstrapping plans

#### [Edward Ayers (Aug 16 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132248684):
I'm reading through the kernel code. Let me just write down what I think is happening and then I can be corrected.
- `expr.cpp` is doing roughly the same thing as `expr.lean`, just a big inductive type with helper methods.
- `type_checker` infers the type for a given `expr` or throws if it isn't a valid expr. Saying that a given `expr` typechecks is equivalent to saying that the `expr` can be built just using the inference rules of CIC (up to being able to synthesize metavars later). 
- You inject a `normalizer_extension` into the kernel to dictate how the typechecker should put terms in WHNF. If there is a bug in the injected `normalizer_extension` then the kernel will be compromised too. So quotients and inductives are normalizer_extensions.
- So the kernel is happy when it is given an environment, which is an ordered dictionary of declarations indexed by `name`, and all of the declarations' `expr`s typecheck.

#### [Edward Ayers (Aug 16 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132249735):
In the [system description](https://leanprover.github.io/papers/system.pdf) for Lean it says that the typechecker can also produce unification constraints, but this feature doesn't seem to be in the`type_checker.h`, although I could not be reading thoroughly enough, where is the code that does type_checking and also spits out some unification constraints?

#### [Leonardo de Moura (Aug 16 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132250626):
@**Edward Ayers** You have to go back in time to see the unification constraints :) https://github.com/leanprover/lean/blob/CADE25/src/kernel/type_checker.h
We abandoned this approach in Lean 3. Now, the kernel type checker is simpler and has no support for meta-variables (unification variables). The elaborator uses a different module for inferring types and solving unification constraints.

#### [Sebastian Ullrich (Aug 16 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132250884):
@**Mario Carneiro** 
```quote
I don't know exactly how the full bootstrap process would work, it might just run itself on the previous version of lean to avoid messy business
```
Yes, this is how all bootstrapping compilers work. But instead of a binary file, we want to store the previous version as extracted C++ code, which should be at least slightly more inspectable and git-friendly

#### [Edward Ayers (Aug 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132250969):
Thanks Leo. Also `elab_context.h` is confusing me. The comment talks about `tactic_context`. But I can't find any other mentions of `tactic_context`. I also can't spot the definition of `type_context`, only `type_context_old`

#### [Edward Ayers (Aug 16 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132252758):
I'm really keen to see the C++ code that is used to keep track of metavariables, local context and so on while a tactic or elaborator is being run. It seems to be `type_context_old` but I'm not sure because of the `old` suffix.

#### [Gabriel Ebner (Aug 16 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132252927):
`type_context` was renamed to `type_context_old` in the preparation of the changes for Lean 4.  You should really be looking at `type_context_old`, it was the `type_context` for most of Lean 3.

#### [Edward Ayers (Aug 16 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253032):
In the `type_context.h` there is a large comment starting with `NEW DESIGN notes. (This is work in progress)`, is this how Lean 3 works or is it how Lean 4 works?

#### [Gabriel Ebner (Aug 16 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253156):
This is a change that was introduced late in Lean 3, and the todo is also implemented now with the `unfreeze_local_intstances` tactic.

#### [Simon Hudon (Aug 16 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253773):
@**Edward Ayers** I recommend you start using different topics for your different questions so that other people may determine at a glance if the discussion is relevant to what they're working on.

#### [Edward Ayers (Aug 16 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253799):
ok will do

#### [Simon Hudon (Aug 16 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253828):
Thanks!

#### [Kevin Buzzard (Aug 16 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132257907):
I like the question barrage :-) but I do see Simon's logic. I often start new threads with more descriptive titles now and it works better for search when I come back to them later.

