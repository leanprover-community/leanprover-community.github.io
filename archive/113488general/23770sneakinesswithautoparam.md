---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23770sneakinesswithautoparam.html
---

## Stream: [general](index.html)
### Topic: [sneakiness with `auto_param`](23770sneakinesswithautoparam.html)

---


{% raw %}
#### [ Scott Morrison (Aug 08 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101629):
I would like to be able to change the tactic specified via `auto_param` to fill in a structure field automatically.

#### [ Scott Morrison (Aug 08 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101631):
I know I can't actually do it, so I would like a nice workaround.

#### [ Scott Morrison (Aug 08 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101653):
Somehow I want to write
```
structure F :=
(t : Type . sneaky) 
```
and then for a while during the development have `sneaky` do one thing, and then be able to utter a secret incantation, after which `sneaky` does something else.

#### [ Scott Morrison (Aug 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101699):
For example, the `sneaky` tactic could in some way inspect the environment, and delegate its actual work to a different tactic based on what it sees.

#### [ Scott Morrison (Aug 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101703):
Does anyone know what I'm looking for?

#### [ Scott Morrison (Aug 08 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101717):
I already do a little bit of this: my `tidy` tactic looks for definitions tagged with the `@[tidy]` attribute, and if they are of type `tactic unit` it also invokes them during it's attempt to solve a goal.

#### [ Scott Morrison (Aug 08 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131101773):
But now I want something slight different: e.g. have `sneaky` call the last-to-be-defined tactic tagged with @[sneaky_implementation], or something like that.

#### [ Mario Carneiro (Aug 08 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131103723):
Here's a way to do it if you want to have only one implementation at a given time:
```lean
@[user_attribute]
meta def sneaky_attr : user_attribute :=
{ name := `sneaky_impl,
  descr := "implementation for sneaky",
  before_unset := some $ λ _ _, skip,
  after_set := some $ λ n _ _, do
    env ← get_env,
    ns ← attribute.get_instances sneaky_attr.name,
    ns.mmap (λ n', when (n ≠ n') $ unset_attribute sneaky_attr.name n'),
    attribute.get_instances sneaky_attr.name >>= trace }

meta def sneaky : tactic unit :=
do [n] ← attribute.get_instances sneaky_attr.name,
  monad.join (mk_const n >>= eval_expr (tactic unit))

structure F :=
(t : Type . sneaky)

@[sneaky_impl] meta def mk_nat : tactic unit :=
trace "running mk_nat" >> `[exact nat]

example : F := {} -- running mk_nat

@[sneaky_impl] meta def mk_sorry : tactic unit :=
trace "running mk_sorry" >> `[sorry]

example : F := {} -- running mk_sorry
```

#### [ Mario Carneiro (Aug 08 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131103757):
Each time you define a tactic with `@[sneaky_impl]`, the last one to have it has it unset, and `sneaky` calls which ever definition has the attribute right now

#### [ Mario Carneiro (Aug 08 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131103813):
Alternatively, you could have the attributes remain permanently, but you just check which was the last to be written

#### [ Scott Morrison (Aug 08 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131103847):
awesome! I didn't know about those hooks on attributes.

#### [ Scott Morrison (Aug 08 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104078):
okay, so next I want approval to use this in mathlib. :-) Later in my category theory work, I really rely on most of the `functoriality` (oops, `map_comp` :slight_smile:) and `naturality` fields being filled in automatically by `tidy` or `obviously`. Of course, it's going to be a little while before `tidy` is mathlib ready, and maybe much longer before `obviously` is. I'd really like to be able to keep using them in my work, however... (in particular, I'm going to need to leave in "in action" everywhere in my later category theory stuff while I try and get them ready mathlib ready).

#### [ Scott Morrison (Aug 08 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104131):
So... the hope is that I can have the `id_comp`, `comp_id`, `assoc`, `map_id`, `map_comp` and `naturality` fields all invoke a tactic defined like `sneaky` above.

#### [ Scott Morrison (Aug 08 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104151):
In mathlib for now they will do nothing. In my development they will hook into whatever I want them to. Eventually, hopefully, they will start doing something in mathlib too.

#### [ Johan Commelin (Aug 08 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104206):
But what would the first mathlib version of `sneaky` do?

#### [ Scott Morrison (Aug 08 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104211):
`[skip]

#### [ Scott Morrison (Aug 08 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104221):
So if you don't provide the field explicitly, you just get the usual error message about an unsolved goal.

#### [ Johan Commelin (Aug 08 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104236):
Hmmm. Sorry, I don't get what your strategy is.

#### [ Johan Commelin (Aug 08 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104241):
Does that mean that you still have to prove this stuff by hand in mathlib?

#### [ Johan Commelin (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104264):
If so, why would you want a `sneaky`?

#### [ Scott Morrison (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104289):
If you look at https://github.com/leanprover/mathlib/blob/master/category_theory/category.lean#L43

#### [ Mario Carneiro (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104290):
because he wants the auto param for a structure defined in mathlib to call his tactic

#### [ Scott Morrison (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104296):
you'll see that `category.assoc` is already marked with the auto_param `obviously`.

#### [ Scott Morrison (Aug 08 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104301):
it's just that `obviously` in mathlib is just defined to be `skip`. ( a few lines above!)

#### [ Scott Morrison (Aug 08 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104311):
I want to leave it like that in mathlib (for now), but still be able to use it outside while I'm getting it ready.

#### [ Mario Carneiro (Aug 08 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104324):
I'm okay with this in principle. I always thought that the static nature of auto params made them a bit limited, but this is a nice way to forward reference

#### [ Mario Carneiro (Aug 08 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104334):
I just need to figure out how to structure it nicely

#### [ Scott Morrison (Aug 08 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104336):
obviously it would make sense to write something slightly more general than sneaky above :-)

#### [ Mario Carneiro (Aug 08 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104404):
One thing which bothers me about this proposal is that you probably want to have just one `sneaky` which then goes everywhere

#### [ Scott Morrison (Aug 08 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104410):
I'm not sure what you mean?

#### [ Scott Morrison (Aug 08 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104447):
I'm imagining we could set up an attribute that you use like `@[replace tidy] meta def foo : tactic unit := ...`

#### [ Scott Morrison (Aug 08 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104458):
and then as an auto_param you put in `(field : Type . invoke_tidy)`

#### [ Scott Morrison (Aug 08 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104513):
and `invoke_tidy` goes and finds the latest declaration tagged with @[replace tidy].

#### [ Mario Carneiro (Aug 08 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104524):
is `tidy` parametric here? what else can you `replace`

#### [ Scott Morrison (Aug 08 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104665):
well, I was imagining that other people might want to replace other things

#### [ Scott Morrison (Aug 08 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104677):
but maybe that's not helpful...

#### [ Mario Carneiro (Aug 08 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104681):
I agree. But how would that work?

#### [ Scott Morrison (Aug 08 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104762):
I don't really know about parameters to attributes, so I was just dreaming there.

#### [ Scott Morrison (Aug 08 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104790):
I was imagining that you'd only define an attribute once, just like `sneaky` but taking a parameter.

#### [ Scott Morrison (Aug 08 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104806):
For each value of that parameter you'd have to make a definition of an `invoke_XXX` tactic

#### [ Scott Morrison (Aug 08 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104888):
that would then invoke the last thing tagged with `@[replace XXX]`

#### [ Scott Morrison (Aug 08 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104918):
For me, I'm happy to have a single tactic for all of those fields (and many others later)

#### [ Scott Morrison (Aug 08 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104924):
as long as I can still hook into it post mathlib

#### [ Mario Carneiro (Aug 08 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104925):
Oh wow, I tried using `sneaky_impl` with local attributes and it actually went back to the old definition after the section closed

#### [ Mario Carneiro (Aug 08 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131104983):
```
@[sneaky_impl] meta def mk_nat : tactic unit :=
trace "running mk_nat" >> `[exact nat]

example : F := {} -- running mk_nat

section
meta def mk_sorry : tactic unit :=
trace "running mk_sorry" >> `[sorry]
local attribute [sneaky_impl] mk_sorry

example : F := {} -- running mk_sorry
end

example : F := {} -- running mk_nat
```

#### [ Scott Morrison (Aug 08 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105029):
Nice! (I think?)

#### [ Mario Carneiro (Aug 08 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105046):
I guess that's the power of functional data structures, you get "time travel" for free

#### [ Johan Commelin (Aug 08 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105102):
That means that you could add particular superpowers, but not others, to `tidy`, depending on the file you are working in?

#### [ Scott Morrison (Aug 08 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105180):
Yes

#### [ Scott Morrison (Aug 08 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105231):
I already do this all the time, actually, just at a whole file level.

#### [ Scott Morrison (Aug 08 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105243):
For me so far the definition of `tidy` has been invariant, except that it looks up everything marked with @[tidy] and tries those tactics too.

#### [ Scott Morrison (Aug 08 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131105253):
Mario's observation means you can do it at section level too, which I hadn't really appreciated.

#### [ Mario Carneiro (Aug 08 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131113251):
Check out https://github.com/leanprover/mathlib/blob/master/tactic/replacer.lean for my attempt at a general framework

#### [ Mario Carneiro (Aug 08 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sneakiness%20with%20%60auto_param%60/near/131113386):
```
def_replacer tidy
structure T := (t : Type . tidy)

@[tidy] meta def tac1 := tactic.trace "tac1"
example : T := {} -- tac1

@[tidy] meta def tac2 (prev : tactic unit) := prev >> tactic.trace "tac2"
example : T := {} -- tac1 tac2

@[tidy] meta def tac3 := tactic.trace "tac3"
example : T := {} -- tac3
```


{% endraw %}
