---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60387declarationinspection.html
---

## Stream: [general](index.html)
### Topic: [declaration inspection](60387declarationinspection.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132184814):
I'm still trying to discover what a Lean file can reveal about itself. I found https://github.com/leanprover/lean/blob/master/library/init/meta/environment.lean and https://github.com/leanprover/lean/blob/master/library/init/meta/declaration.lean but there still very basic questions I can't answer. Say I have an environment and a declaration name. I can distinguish a lemma/theorem from a definition or constant (although I'm not sure what's the difference between definition and constant). But how can I distinguish between `def`, `class`, `instance`, `structure`, `inductive`? I saw the series of functions around https://github.com/leanprover/lean/blob/master/library/init/meta/environment.lean#L47 but trying them on examples only confuses me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132184954):
`class` means `@[class] structure` so you can use the attribute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132184971):
similarly `@[instance]` is an attribute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185017):
How do you get attributes of a declaration?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185129):
Can one strip off `Pi` from an `expr` and get to the first function appearing next? (This would be to understand what an instance declaration is an instance of)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185232):
`tactic.has_attribute`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185432):
Is it possible do use this outside of a tactic? (in meta land of course)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185506):
I doubt it, it looks like environment doesn't know anything about attributes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185695):
Do you see away to get the list of classes defined in the currently opened file then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 15 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132185760):
It also doesn't seem possible to get any information on what notation is defined.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186062):
```
import tactic.basic

class foo : Type.
structure bar : Type.
@[class] def baz : Type := nat

open tactic
run_cmd do
  env ← get_env,
  env.fold skip $ λ d t, do
    when (env.in_current_file' d.to_name) $ try $
      tactic.has_attribute `class d.to_name >>
      trace d.to_name,
    t
-- foo baz
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186126):
alternatively:
```
run_cmd do
  env ← get_env,
  l ← attribute.get_instances `class,
  l.mmap' $ λ n, do
    when (env.in_current_file' n) (trace n)
-- baz foo
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186311):
as I'm sure you've heard by now, this introspection stuff is getting an overhaul in lean 4, so fingers crossed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186593):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132186636):
What is the difference between `run_cmd` and `#eval` here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132187368):
Inside a function which will ultimately return a `tactic unit` can I have some `if` consuming a `tactic Prop` or `tactic bool`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132187933):
there is `mcond` as a shortcut for this, but you can always do `b <- tac, if b then ... else ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188027):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188037):
I'm sorry I'm very slowly getting used to monads

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188081):
Do you have ideas to traverse an `expr` until you see what an instance is an instance of?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188330):
```lean
meta def expr.get_pi_app_fn : expr → expr
| (expr.pi _ _ _ e) := e.get_pi_app_fn
| e                 := e.get_app_fn

run_cmd do
  d ← get_decl ``option.decidable_eq,
  expr.const n _ ← return d.type.get_pi_app_fn,
  trace n
-- decidable_eq
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188717):
great!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132188810):
I think I even understand this code (but wouldn't have none where to search)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132189258):
Two last questions and then I cook dinner: how would you distinguish between `inductive` and `structure` declarations? What does constant mean in the definition of the declaration type? How is is more constant than a definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197062):
Mario, do you also have hints for me?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197217):
`declaration.cnst` is the kind of declaration you get if you write `constant A : ℕ`. It's an undefined constant, basically the same as an axiom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197290):
You can have a `meta constant` but not a `meta axiom`. I'm not sure if there are any other differences between the two.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197349):
I'm sorry but this doesn't match what I'm seeing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197431):
I think `constant` is to `axiom` as `def` is to `theorem`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197478):
What are you seeing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197543):
The differences between def and theorem are when the bodies get elaborated, right? But there are no bodies in a constant or axiom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197609):
And you can have axioms with non-`Prop` type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197749):
Actually, it looks like using the `axiom` command with a non-`Prop` type creates a `declaration.cnst` in the end. (edit- scratch that, typo)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197798):
I'm going through the code now, trying to figure out the difference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132197808):
it is disambiguated in loads of places just so it can print `constant` instead of `axiom` but that's not so helpful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198136):
Sorry I was interrupted. Maybe there is a misunderstanding, I'm talking about https://github.com/leanprover/lean/blob/master/library/init/meta/declaration.lean#L67

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198153):
See 
```lean
import tactic
open tactic environment declaration

structure toto :=
(tata : Type)

#eval
do curr_env ← get_env,
   let decls := curr_env.fold [] list.cons,
   let local_decls := decls.filter
     (λ x, environment.in_current_file' curr_env (to_name x) && not (to_name x).is_internal),
   local_decls.mmap' (λ decl : declaration,
       match decl with
   | (thm _ _ _ _) := do trace "theorem"  
   | (defn _ _ _ _ _ _) := do trace "def"
   | (cnst _ _ _ _) := do trace "cnst"
   | (ax _ _ _) := do trace "ax"
  end)
```
lots of cnst there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198311):
"Built-ins" are implemented as constants too. So when you declare an inductive type, the constructors, recursor, etc. are constants.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198325):
If you change a line to `| (cnst nm _ _ _) := do trace "cnst", trace nm` you can see what the constants are called.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198345):
Did you know about `#print definition`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198404):
I just discovered that you can print definitions with `#print definition foo`. it's the same as `#print foo` but the printout is slightly different and it doesn't work on constants

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198494):
I had no idea, heh.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198658):
I know, maybe it's clearer with 
```lean
import tactic
open tactic environment declaration

structure toto :=
(tata : Type)

#eval
do curr_env ← get_env,
   let decls := curr_env.fold [] list.cons,
   let local_decls := decls.filter
     (λ x, environment.in_current_file' curr_env (to_name x) && not (to_name x).is_internal),
   local_decls.mmap' (λ decl : declaration,
       match decl with
   | (cnst _ _ _ _) := do trace decl.to_name
   | _ := do skip
  end)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198673):
you see that `toto` is also `cnst`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198710):
Oh, @**Patrick Massot** I found out that even lean internally doesn't store the list of attributes associated to a definition. When printing a definition with `#print`, it gets the list of all attributes and just asks for each whether `foo` has that attribute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198786):
but where does the answer come from then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198801):
Yeah. When you declare an inductive type `T`, you're basically saying, "there is a type `T`. This is how you create a `T` (the constructors). This is how you use a `T` (the recursors)."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 15 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198813):
You're not defining `T` in terms of something else, so there's no value for the declaration `T` to have.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198884):
Makes sense, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132198896):
Do you have an idea to distinguish between `inductive` and `structure`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199003):
I'm working on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199047):
in the meantime, I found something odd:
```
structure foo : Type.
#print foo
-- inductive foo : Type
-- constructors:
-- foo.mk : foo
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199052):
lean does not remember structureness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199131):
or at least, nullary structures don't count as structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199175):
```lean

structure toto :=
(tata : Type)
#print toto
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199245):
```lean
structure toto : Type 1
fields:
toto.tata : toto → Type
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199271):
Lean reconstructs structurehood based on structure like things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199282):
specifically, the projections

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132199802):
where do you see the code of `#print`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132200606):
are you looking at https://github.com/leanprover/lean/blob/703d12d594f1591296d529e72794a00ba42dbade/src/frontends/lean/structure_cmd.cpp#L111?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 15 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132200886):
I think this replicates lean's `is_structure` function
```lean
meta def name.deinternalize_field : name → name
| (name.mk_string s name.anonymous) :=
  let i := s.mk_iterator in
  if i.curr = '_' then i.next.next_to_string else s
| n := n

meta def environment.is_structure (env : environment) (n : name) : bool :=
option.is_some $ do
  guardb (env.is_inductive n),
  d ← (env.get n).to_option,
  [intro] ← pure (env.constructors_of n) | none,
  guard (env.inductive_num_indices n = 0),
  let nparams := env.inductive_num_params n,
  di ← (env.get intro).to_option,
  @nat.iterate (expr → option unit)
    (λ f e, do
      expr.pi _ _ _ body ← pure e | none,
      f body) nparams
    (λ e, do
      expr.pi x _ _ _ ← pure e | none,
      let f := n ++ x.deinternalize_field,
      env.is_projection f $> ())
    di.type
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 16 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132226399):
Nice!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132487331):
```quote
I think this replicates lean's `is_structure` function
```

I'm sorry, I wasted your time. For some mysterious reason I missed https://github.com/leanprover/lean/blob/776b440d5595e5eaa3f16e633c9ca85a834f147a/library/init/meta/environment.lean#L87 (and its implementation https://github.com/leanprover/lean/blob/776b440d5595e5eaa3f16e633c9ca85a834f147a/src/library/vm/vm_environment.cpp#L227)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132542303):
Does Lean keep any trace of whether something was declared as a lemma or a theorem? Or are they purely synonym from the parsing stage on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132542417):
pure synonyms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/declaration%20inspection/near/132542484):
thanks


{% endraw %}
