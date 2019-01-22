---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/41672fullnames.html
---

## [general](index.html)
### [full names](41672fullnames.html)

#### [Patrick Massot (Jul 17 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832050):
Is there a way to ask Lean to list all fully qualified names (I mean including namespaces) defined by a particular file? I'd like to check I didn't messed up with name spaces

#### [Simon Hudon (Jul 17 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832621):
The way I would do it is I would write a command in a `run_cmd` block and use `environment.fold` to iterate over all the visible declarations, get their names and use `environment.in_current_file` to filter out any declaration that comes from outside. It will give you a list of fully qualified names.

#### [Simon Hudon (Jul 17 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832647):
Oh, and in a tactic, you use  `get_env` to get the current environment.

#### [Patrick Massot (Jul 17 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832672):
Thanks Simon, but I'm afraid you assume too much knowledge from me.

#### [Simon Hudon (Jul 17 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832755):
No worries, I like starting with a brief overview but I'm happy to go step by step with you if need be.

#### [Simon Hudon (Jul 17 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832776):
Let's start with a script that just prints all the visible names (even the ones from other files).

#### [Simon Hudon (Jul 17 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832960):
```lean
run_cmd 
do curr_env <- get_env,
   let decls := curr_env.fold [] list.cons, -- this loops over all the visible declarations and, using `list.cons`, accumulate them in a list
   let names := decls.map declaration.to_name, -- this takes the name of each declaration.
   trace names
```

#### [Simon Hudon (Jul 17 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129832979):
Does it make sense so far?

#### [Patrick Massot (Jul 17 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833046):
It makes sense to me but not to Lean

#### [Patrick Massot (Jul 17 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833049):
"type of sorry macro is not a sort"

#### [Patrick Massot (Jul 17 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833051):
probably missing import or open

#### [Simon Hudon (Jul 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833133):
that makes sense. Try `open tactic`.

#### [Kevin Buzzard (Jul 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833146):
```

#### [Kevin Buzzard (Jul 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833150):
`deep recursion was detected at 'formatter' (potential solution: increase stack space in your system)`

#### [Patrick Massot (Jul 17 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833151):
"deep recursion was detected at 'formatter' (potential solution: increase stack space in your system)"

#### [Patrick Massot (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833163):
:simple_smile:

#### [Patrick Massot (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833183):
Maybe we have infinitely nested namespaces

#### [Simon Hudon (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833186):
Interesting. What if you just do `trace names.length`?

#### [Patrick Massot (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833195):
22573

#### [Patrick Massot (Jul 17 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833201):
:laughing:

#### [Patrick Massot (Jul 17 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833250):
Maybe we should jump to the filtered version

#### [Simon Hudon (Jul 17 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833253):
Good. That will be good enough for now. The problem is that we have a lot of definitions but we don't care about all of them. Let's filter the list and then we can print them all out

#### [Simon Hudon (Jul 17 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833264):
You're using so few words to express my idea. I'm jealous

#### [Simon Hudon (Jul 17 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833280):
Do you have an idea on how to do the filtering?

#### [Patrick Massot (Jul 17 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833300):
Yes: using `environment.in_current_file`

#### [Patrick Massot (Jul 17 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833353):
I'm such a good student :open_mouth:

#### [Simon Hudon (Jul 17 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833372):
You get an A! Good job!

#### [Simon Hudon (Jul 17 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833461):
Once you've done that and defined a new list `local_names`, you can print them more nicely as `local_names.mmap' trace`

#### [Patrick Massot (Jul 17 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833763):
"code generation failed, VM does not have code for 'classical.choice'". I may have taken a wrong turn...

#### [Patrick Massot (Jul 17 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833821):
I was trying to get rid of that damn `environment.in_current_file curr_env has type   name → bool but is expected to have type   name → Prop`

#### [Patrick Massot (Jul 17 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833849):
I'm probably beaten for my preamble

#### [Patrick Massot (Jul 17 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833920):
Yeah, in a fresh file Lean complains it wants a decidable instance

#### [Patrick Massot (Jul 17 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833964):
(deleted)

#### [Patrick Massot (Jul 17 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129833972):
(deleted)

#### [Patrick Massot (Jul 17 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129834267):
I give up, it seems I don't know enough. I tried `let noms := names.filter (environment.in_current_file curr_env),` but Lean wants a decidable function to prop, not a function to bool

#### [Simon Hudon (Jul 17 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129834884):
Try `let noms := names.filter (λ n, curr_env.in_current_file n)`

#### [Patrick Massot (Jul 17 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129834993):
This works if there is mathematics preamble

#### [Simon Hudon (Jul 17 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835012):
Which preamble?

#### [Patrick Massot (Jul 17 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835022):
`local attribute [instance] classical.prop_decidable`

#### [Mario Carneiro (Jul 17 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835067):
that's obviously a bad idea if you are writing code

#### [Simon Hudon (Jul 17 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835078):
You shouldn't need that. Booleans are decidable propositions

#### [Patrick Massot (Jul 17 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835119):
Of course it means I should define the command in its own file and execute it where I need it

#### [Simon Hudon (Jul 17 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835136):
If you use `classical.prop_decidable` try `local attribute [instance, priority 0] classical.prop_decidable`. This way, if you have computable instances they will be chosen instead.

#### [Patrick Massot (Jul 17 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835321):
It mostly works, but I see the `quot` namespace is not filtered out

#### [Patrick Massot (Jul 17 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835352):
For the record, I think I wrote the solution at some point, but was confused by the decidability related error message

#### [Patrick Massot (Jul 17 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835516):
It would also be nice to filter out all `_proof_` and `_eqn_`

#### [Simon Hudon (Jul 17 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835564):
Let's say `quot.lift`is one of those that aren't filtered out. Try printing ``curr_env.in_current_file `quot.lift` just to double check.

#### [Mario Carneiro (Jul 17 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835591):
you can use `name.is_internal` to filter

#### [Mario Carneiro (Jul 17 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835612):
it checks that none of the name components have an initial underscore

#### [Patrick Massot (Jul 17 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835818):
Simon, could you try to fix quotes in your last message? I don't know where to put them

#### [Patrick Massot (Jul 17 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835860):
`name.is_internal` does allow to get rid of underscored stuff

#### [Mario Carneiro (Jul 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835902):
``curr_env.in_current_file `quot.lift``

#### [Mario Carneiro (Jul 17 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129835957):
better yet ```curr_env.in_current_file ``quot.lift```

#### [Patrick Massot (Jul 17 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836041):
Lean indeed answers `tt`

#### [Patrick Massot (Jul 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836105):
To make sure we are on the same page, the current version I have is:
```lean
open tactic

meta def print_names : tactic unit :=
do curr_env <- get_env,
   trace (to_string (curr_env.in_current_file ``quot.lift)),
   let decls := curr_env.fold [] list.cons, -- this loops over all the visible declarations and, using `list.cons`, accumulate them in a list
   let names := decls.map declaration.to_name, -- this takes the name of each declaration.
   let local_names := names.filter (λ x, environment.in_current_file curr_env x && not x.is_internal),
   local_names.mmap' trace
```

#### [Mario Carneiro (Jul 17 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836290):
you can see from the definition of `in_current_file` that it just checks that `decl_olean` returns none

#### [Mario Carneiro (Jul 17 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836307):
but `quot.lift` was never defined, it magically comes into being from the `init_quotient` one-time command

#### [Reid Barton (Jul 17 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836558):
If you also require that `decl_pos` is not `none`, that should get rid of `quot` stuff

#### [Mario Carneiro (Jul 17 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836623):
in a new file, I get this:
```
open tactic
#eval do env ← get_env,
  env.fold skip $ λ d t,
  let n := d.to_name in
  when (env.in_current_file n) (trace n) >> t

-- quot.mk
-- quot.ind
-- quot
-- quot.lift
-- _main
```

#### [Mario Carneiro (Jul 17 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836631):
I guess `_main` is the tactic I am `#eval`ing, the rest come from `init_quotient`

#### [Simon Hudon (Jul 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836707):
@**Mario Carneiro** You may want to use `mfold` instead of `fold` for monadic functions

#### [Mario Carneiro (Jul 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836719):
there is no `env.mfold`

#### [Mario Carneiro (Jul 17 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836802):
If I use `(env.decl_pos n).is_none` instead, I get
```
interactive.loc.has_reflect
prod.has_reflect
quot.mk
quot.ind
bool.has_reflect
sum.has_reflect
quot
quot.lift
option.has_reflect
pos.has_reflect
```

#### [Simon Hudon (Jul 17 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836820):
Sorry, you're right, I was thinking of expressions

#### [Mario Carneiro (Jul 17 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836848):
I'm not sure why e.g. `option.has_reflect` has no position, but I can confirm that vscode F12 has no idea where it is

#### [Mario Carneiro (Jul 17 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129836903):
```
attribute [derive has_reflect] bool prod sum option interactive.loc pos
```
I see

#### [Mario Carneiro (Jul 17 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837051):
@**Sebastian Ullrich** I am surprised to discover that there is no `add_decl` variant or option to set the position of a new declaration

#### [Sebastian Ullrich (Jul 17 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837226):
Yes, well, the Lean 3 meta API is just that incomplete

#### [Patrick Massot (Jul 17 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837293):
I know it's cheating, but can't we just filter out `quot.*` using a plain regex?

#### [Mario Carneiro (Jul 17 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837309):
You can, but it would be more accurate to say that it is only those four definitions specifically, not everything in `quot`

#### [Mario Carneiro (Jul 17 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837318):
also it wouldn't be a regex exactly

#### [Patrick Massot (Jul 17 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837368):
those four definitions specifically would be even better

#### [Mario Carneiro (Jul 17 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837376):
it is easy enough to filter out those four by name

#### [Mario Carneiro (Jul 17 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129837475):
```
meta def environment.in_current_file'
  (env : environment) (n : name) : bool :=
env.in_current_file n && (n ∉ [``quot, ``quot.mk, ``quot.lift, ``quot.ind])
```

#### [Patrick Massot (Jul 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840382):
I missed that last message. Thanks!

#### [Patrick Massot (Jul 18 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840429):
I think this command is really useful

#### [Patrick Massot (Jul 18 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840507):
It's much easier than trying to keep track of which namespaces we are in

#### [Patrick Massot (Jul 18 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840513):
Do we have mathlib guidelines about nested namespaces?

#### [Patrick Massot (Jul 18 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840549):
That command would be even nicer if we had versions listing only definitions or only instances or only lemmas/theorems

#### [Patrick Massot (Jul 18 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840589):
But I need to sleep now

#### [Patrick Massot (Jul 18 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840615):
We could even have a tree view

#### [Mario Carneiro (Jul 18 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840623):
what kind of guidelines do you mean?

#### [Patrick Massot (Jul 18 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840680):
it could be pushing towards flat hierarchy or deep hierarchy

#### [Mario Carneiro (Jul 18 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840688):
I would say it's currently more flat than deep

#### [Patrick Massot (Jul 18 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840689):
My completion file currently has:
```
uniform_space.completion_is_complete
uniform_space.completion_extension
uniform_space.completion_is_separated
uniform_space.completion_extension.lifts
uniform_space.completion_lift.uniform_continuity
uniform_space.completion_is_uniform_space
uniform_space.to_completion
uniform_space.eq_of_separated_of_uniform_continuous
uniform_space.completion_lift
uniform_space.completion_lift.unique
uniform_space.completion_extension.uniform_continuity
uniform_space.to_completion.dense
uniform_space.completion_lift.comp
uniform_space.completion_lift.lifts
uniform_space.completion_extension.unique
uniform_space.separated_of_uniform_continuous
uniform_space.nonempty_completion_iff
uniform_space.completion
uniform_space.to_completion.uniform_continuous
```

#### [Mario Carneiro (Jul 18 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840702):
there are some instances of large scale namespaces like `measure_theory`, but most definitions are only one namespace deep

#### [Patrick Massot (Jul 18 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840703):
everything is inside the uniform_space namespace. But then the completion, completion_lift and completion_extension get their sub-namespace

#### [Patrick Massot (Jul 18 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840757):
but this sub-namespacing could be replaced by underscores

#### [Mario Carneiro (Jul 18 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840758):
I think that makes sense - `completion` is defined on `uniform_space`, and theorems about `completion` should go in a namespace for it

#### [Patrick Massot (Jul 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840772):
because there is no structure involved, so we can't use the projection trick

#### [Mario Carneiro (Jul 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840782):
Even so I think that `uniform_space.completion` is better than `completion` because of the need for disambiguation here

#### [Patrick Massot (Jul 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840785):
I could also put (almost) everything from that file in a `uniform_space.completion` namespace

#### [Mario Carneiro (Jul 18 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840831):
you could use `completion.lift` instead of `completion_lift` for example

#### [Mario Carneiro (Jul 18 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840857):
I would avoid repeating things from the namespace in the name though

#### [Mario Carneiro (Jul 18 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840859):
`lattice.lattice` reads redundantly

#### [Patrick Massot (Jul 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840914):
There are two related but distinct thing. `completion_lift` is a definition, lifting a function (not necessarily uniformly continuous!) to completion, and a lemma `completion_lift.lifts`  saying that the lift indeed lifts the map, under uniform continuity assumption

#### [Mario Carneiro (Jul 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840920):
I might say `lift_is_lift` for something like that

#### [Patrick Massot (Jul 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840922):
Deciding and namespaces and names for these two things is exactly the kind of question I have

#### [Mario Carneiro (Jul 18 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840938):
although depending on what exactly "lift" means it might have a more specific name

#### [Mario Carneiro (Jul 18 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129840990):
i.e. if it is something like `lift o mk = id` (I'm making things up) then I might call it `lift_comp_mk`, but if it is `is_lift lift` then I would say `is_lift_lift` or `lift_is_lift`

#### [Patrick Massot (Jul 18 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841003):
https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L187

#### [Patrick Massot (Jul 18 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841058):
and its friend https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L136

#### [Mario Carneiro (Jul 18 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841063):
I would write that the other way and say `lift_to_completion`

#### [Mario Carneiro (Jul 18 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841075):
(probably `to_completion` should be a coercion)

#### [Patrick Massot (Jul 18 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841138):
I wouldn't be able to state those lemmas without writing `to_completion`, even with a coercion, right?

#### [Mario Carneiro (Jul 18 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841151):
you can say `coe`

#### [Patrick Massot (Jul 18 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841161):
I fear it would obscure the statement. But I could still define the coercion for later use

#### [Mario Carneiro (Jul 18 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841215):
Also I don't know if using all these composes in the statement doesn't make your work harder

#### [Mario Carneiro (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841229):
I know that's how mathematicians like to write it but sometimes it is nicer to just put a point in

#### [Patrick Massot (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841231):
Do you mean you would state `forall x, ...`?

#### [Mario Carneiro (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841252):
yes

#### [Patrick Massot (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841255):
True, I really think about this from a categorical perspective, there are no points at all

#### [Patrick Massot (Jul 18 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841258):
Only morphisms

#### [Mario Carneiro (Jul 18 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841307):
Certainly `completion_extension.lifts` should be stated as `completion_extension f \u x = f x`

#### [Patrick Massot (Jul 18 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841309):
Points would really obscure statements

#### [Mario Carneiro (Jul 18 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841334):
maybe, but none of the work done in this file so far is really categorical in nature

#### [Patrick Massot (Jul 18 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841335):
ok, that one could be clearer with a `forall x : a, completion_extension f  x = f x`

#### [Patrick Massot (Jul 18 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841389):
What? Everything building `completion_lift` from `completion_extension` is purely categorical

#### [Patrick Massot (Jul 18 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841429):
With proper mathlib help, there would be a single tactic to invoke to build `completion_lift` from `completion_extension`

#### [Mario Carneiro (Jul 18 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841430):
looks like just specializing theorems to me

#### [Mario Carneiro (Jul 18 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841486):
`completion_lift` should be called `completion.map` though

#### [Patrick Massot (Jul 18 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841504):
The composition proof has slightly more than specializing. `completion_extension.unique` is crucial

#### [Mario Carneiro (Jul 18 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841554):
but it is just specializing - `completion_lift.unique` just applies `completion_extension.unique`

#### [Patrick Massot (Jul 18 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841579):
I'm talking about the proof of `completion_lift.comp`, not `completion_lift.unique`

#### [Patrick Massot (Jul 18 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841594):
Anyway, I really need to sleep now. But I'll probably use all these suggestions tomorrow (although I should also be doing real work...)

#### [Patrick Massot (Jul 18 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129841636):
Thanks!

#### [Patrick Massot (Jul 19 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957604):
Returning to this full names thread since Kevin also had a use case, are we interested to have this in mathlib? The version I currently have here is:
```lean
import data.list.sort
import data.string
import tactic.basic

open tactic

/-- `run_cmd print_names` print all names defined in the current file. 
    This is useful when checking namespaces and writing doc -/
meta def print_names : tactic unit :=
do curr_env <- get_env,
   let decls := curr_env.fold [] list.cons, 
   let names := decls.map declaration.to_name, 
   let local_names := names.filter 
     (λ x, environment.in_current_file' curr_env x && not x.is_internal),
   let sorted_names := list.merge_sort (≤) (local_names.map to_string),
   sorted_names.mmap' trace
```
With some argument parsing skill we could make sorting optional, and have an optional prefix filtering.

#### [Mario Carneiro (Jul 19 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957823):
I think it should return a `list name` rather than printing it if you want to make this more widely usable

#### [Mario Carneiro (Jul 19 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957834):
why isn't it sorted in declaration order?

#### [Patrick Massot (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957907):
yesterday my main goal was to check namespaces, and alphabetical order was therefore more useful

#### [Mario Carneiro (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957910):
it all seems a bit ad hoc

#### [Kevin Buzzard (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957920):
Alphabetical order has been around for a while

#### [Kevin Buzzard (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957926):
but I guess you could call it ad hoc

#### [Patrick Massot (Jul 19 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957927):
I'm not even sure it's in declaration order before sorting

#### [Kevin Buzzard (Jul 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957933):
It's not universe-independent

#### [Mario Carneiro (Jul 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957940):
I think it's the right length for a small program that slices data the way you want

#### [Kevin Buzzard (Jul 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957944):
or even country-independent

#### [Patrick Massot (Jul 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129957971):
I don't understand what you mean by that length comment

#### [Mario Carneiro (Jul 19 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958036):
there isn't much mathlib can do to make that definition shorter without getting too specific

#### [Patrick Massot (Jul 19 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958105):
Ok, I'll keep it around here then

#### [Mario Carneiro (Jul 19 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958195):
If I add that exact tactic to mathlib, then of course your definition becomes very short (just a reference to my definition) but it also becomes less flexible - if you want to print them in a different order or get type information for each definition or something else you will have to start from scratch again (or copy paste the mathlib tactic)

#### [Patrick Massot (Jul 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958219):
I still have a question about that small function. I don't want to be rude, or break the etiquette of this fine place, by using words from imperative programming. But I don't really understand how the main l**p works. What does the first line do exactly?

#### [Mario Carneiro (Jul 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958228):
`get_env`?

#### [Patrick Massot (Jul 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958229):
What is `get_env` returning?

#### [Mario Carneiro (Jul 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958234):
a reference to the environment object

#### [Mario Carneiro (Jul 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958276):
which is the thing that stores all definitions

#### [Patrick Massot (Jul 19 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958351):
what's the point of not having directly the list that the second line creates?

#### [Patrick Massot (Jul 19 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958446):
hitting F12 only gives meta constant everywhere

#### [Mario Carneiro (Jul 19 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958530):
because the environment isn't stored as a list

#### [Patrick Massot (Jul 19 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958551):
I understand that, my question is: how is it more than a list of stuff?

#### [Mario Carneiro (Jul 19 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958597):
for one thing, it should have an index to speed up looking up definitions by name

#### [Patrick Massot (Jul 19 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958655):
Actually I understand nothing about this monad thing. What the difference between the first line and its arcane `a <- b` syntax and the friendlier looking lines with `let a := b`?

#### [Patrick Massot (Jul 19 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958675):
so it's closer to a python dictionary than list?

#### [Mario Carneiro (Jul 19 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129958982):
Literally, `a <- b` is syntax for the `bind` operator, while `let a := b` is just `let`

#### [Mario Carneiro (Jul 19 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959029):
Most operations which have a sequential character or otherwise non-functional behavior have to work inside a monad, and `bind` puts them together with a notation that is deliberately similar to `let a := b`

#### [Mario Carneiro (Jul 19 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959114):
yes, it is basically a dictionary, probably a hash map. In particular, looping over all definitions (which is what you are doing) is one of the least efficient things you can do with it, so it is rather slow

#### [Patrick Massot (Jul 19 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959174):
I'm sorry but I still don't see any difference between: "I want to call `curr_env` the thing returned by `get_env`" and "I want to call `decls` the thing returned by `curr_env.fold [] list.cons`"

#### [Patrick Massot (Jul 19 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959182):
but clearly I cannot switch between `<-` and `let`

#### [Mario Carneiro (Jul 19 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959252):
probably `get_env` is a bad example since it's basically functional, so consider the following instead:
```
do a <- random,
   b <- random,
   c <- random,
   return [a, b, c]
```
Let's say that `random` returns a random number. Then this program will probably return three different numbers

#### [Mario Carneiro (Jul 19 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959271):
On the other hand, with
```
let a := random,
    b := random,
    c := random in
[a, b, c]
```
there is no implementation of `random` that will cause three different numbers to be produced

#### [Kevin Buzzard (Jul 19 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959337):
Patrick do you know all about this monad business?

#### [Kevin Buzzard (Jul 19 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959350):
All of this `<-` is sugar for `monad.bind` etc

#### [Patrick Massot (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959412):
I don't see why you would get the same number with let

#### [Kevin Buzzard (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959413):
The part of "programming in Lean" about the state monad gave me some idea about what was going on here. The `<-` can change the state of things.

#### [Patrick Massot (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959428):
Kevin, I tried to read that part of PIL several time, but it doesn't stick at all

#### [Kevin Buzzard (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959432):
but in functional programming you can't change state

#### [Kevin Buzzard (Jul 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959435):
as there is no state

#### [Kevin Buzzard (Jul 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959448):
`<-` can expand to "...and let x = x + 1 while you're doing this"

#### [Mario Carneiro (Jul 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959454):
notice that the second program is definitionally equal to `[random, random, random]` and `(\lam x, [x, x, x]) random`

#### [Patrick Massot (Jul 19 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959537):
Sure. But then what happens at execution? Isn't random called three times?

#### [Kevin Buzzard (Jul 19 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959543):
with the same inputs maybe

#### [Patrick Massot (Jul 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959583):
there is no input

#### [Kevin Buzzard (Jul 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959587):
right

#### [Kevin Buzzard (Jul 19 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959594):
so the same thing happens three time

#### [Kevin Buzzard (Jul 19 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959603):
but with `<-` there are hidden variables

#### [Kevin Buzzard (Jul 19 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959626):
it's not a contradiction that "intro x" can do different things at different points in the middle of a tactic proof

#### [Kevin Buzzard (Jul 19 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959627):
because the goal might be different

#### [Mario Carneiro (Jul 19 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959724):
A very small example:
```lean
def counter (α) := nat → nat × α
instance : monad counter :=
{ pure := λ α a n, (n, a),
  bind := λ α β f g n, let (n', a) := f n in g a n' }

def count : counter nat := λ n, (n+1, n)

def run {α} (c : counter α) : α := (c 0).2

#eval run $ do
  a ← count,
  b ← count,
  c ← count,
  return [a, b, c]

-- [0, 1, 2]
```

#### [Mario Carneiro (Jul 19 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959800):
If I `#check` instead, it says
```
run (count >>= λ (a : ℕ), count >>= λ (b : ℕ), count >>= λ (c : ℕ), return [a, b, c]) : list ℕ
```

#### [Patrick Massot (Jul 20 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959869):
I have *no idea* what's going on in your snippet

#### [Kevin Buzzard (Jul 20 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959873):
`<-` is running `bind` which can change the nat. The nat is a variable which is hidden in the notation but still exists. If you unravel you can see the nat. `>>=` also means bind

#### [Mario Carneiro (Jul 20 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959876):
Start with the first line

#### [Mario Carneiro (Jul 20 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959884):
`counter A` is a function from `nat` to `nat x A`

#### [Kevin Buzzard (Jul 20 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959887):
`do` puts you into monad mode, and the monad here is `counter` which is hiding a nat.

#### [Patrick Massot (Jul 20 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129959894):
Zulip just told me your snippet was written yesterday. I probably mean it's too late to understand this

#### [Patrick Massot (Jul 20 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129960051):
I should really sleep. Since my family left for vacations, I'm drifting towards night. Today (Zulip claims I mean yesterday) I reached the point where I got up too late to have lunch with my colleagues. So I'll try to drift back. But I promise I'll try to understand your code tomorrow, after reading back a bit of PIL. Thank you!

#### [Mario Carneiro (Jul 20 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/129960242):
By the way, that code is roughly analogous to the following C code:
```
int state = 0;
int a = state++;
int b = state++;
int c = state++;
return [a, b, c]; // <- okay, not really C style...
```

#### [Kevin Buzzard (Jul 25 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/130303691):
```quote
Returning to this full names thread since Kevin also had a use case, are we interested to have this in mathlib? The version I currently have here is:
```lean
import data.list.sort
import data.string
import tactic.basic

open tactic

/-- `run_cmd print_names` print all names defined in the current file. 
    This is useful when checking namespaces and writing doc -/
meta def print_names : tactic unit :=
do curr_env <- get_env,
   let decls := curr_env.fold [] list.cons, 
   let names := decls.map declaration.to_name, 
   let local_names := names.filter 
     (λ x, environment.in_current_file' curr_env x && not x.is_internal),
   let sorted_names := list.merge_sort (≤) (local_names.map to_string),
   sorted_names.mmap' trace
```
```

Ooh this was just really handy for me. Faced with

```lean
namespace is_ring_hom

instance {S : set R} [is_subring S] : is_ring_hom (@subtype.val R S) :=
{ map_add := λ _ _, rfl,
  map_mul := λ _ _, rfl,
  map_one := rfl }

end is_ring_hom
```

and after 2 minutes of failing to guess what Lean might have called this instance, I ran the code and got it immediately. 
```

#### [Kevin Buzzard (Jul 25 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/130303706):
Answers on a postcard

#### [Reid Barton (Jul 26 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/130308592):
In this case I think `#print instances is_ring_hom` will tell you too.

#### [Kevin Buzzard (Jul 26 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/130327524):
Aah! I use `#print prefix` a fair bit but I don't think I'd internalised `#print instances`

#### [Patrick Massot (Aug 11 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131947719):
So we have this `print_names` command. We can put it in a file, import that file in another file, run the command there, and get our answer in the Lean messages window. How could we get the same information from the command line without modifying the file we want to inspect?

#### [Simon Hudon (Aug 11 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131958856):
In Haskell, ghc has the option `-e` which allows you to provide an expression to evaluate from the command line. Lean does not have that. What I would do is write a bash script to generate a .lean file that imports your `print_names` definition and the file you want to check, then call Lean on that file.

#### [Mario Carneiro (Aug 11 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131960186):
lean has a `--run` option

#### [Simon Hudon (Aug 11 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131961097):
I thought it only ran the `main` function

#### [Patrick Massot (Aug 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131965768):
That's also what the documentation and experiment suggest

#### [Patrick Massot (Aug 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131965831):
@**Sebastian Ullrich** do you confirm there is no way to do what I asked?

#### [Patrick Massot (Aug 11 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131965902):
More generally, it would help with documentation if we knew more about Lean's introspection capabilities. For instance, suppose we get hold of some definition of lemma using `get_env`, is there any way we could get a list of types of objects appearing in the statement or, even better, a list of all lemmas and definitions used in the proof (before it gets erased by proof irrelevance)?

#### [Simon Hudon (Aug 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966166):
```quote
is there any way we could get a list of types of objects appearing in the statement or, even better, a list of all lemmas and definitions used in the proof (before it gets erased by proof irrelevance)?
```

I believe that is possible. Let me just work something out.

#### [Simon Hudon (Aug 11 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966604):
Here's what I got. This version lists all the constants (definition, theorem, axiom or constant, actually) used in the *statement* of the theorem. I have worked out a version I thought would do the same about the proof but I run into weird errors.

```lean
meta def list_constant (e : expr) : list name :=
e.fold [] $ λ e _ cs,
if e.is_constant ∧ ¬ e.const_name ∈ cs 
  then e.const_name :: cs
  else cs

open declaration
meta def const_in_def (n : name) : tactic unit := 
do (thm _ _ t v) ← get_decl n,
   -- let v := v.get, 
   -- trace v.is_constant,
   trace $ list_constant t,
   return ()
   
#eval const_in_def `list.reverse_append
```

#### [Patrick Massot (Aug 11 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966679):
Nice!

#### [Patrick Massot (Aug 11 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966724):
I think I will play of lot with that function

#### [Simon Hudon (Aug 11 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131966786):
Cool! Please let me know if you manage to get `v.get` to work. What I think is that the proof tree might be stored nowhere so `v.get` can only fail. @**Sebastian Ullrich** and @**Gabriel Ebner** may shed some light on that.

#### [Gabriel Ebner (Aug 11 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967066):
What error are you getting?  This works just fine for me:
```lean
import data.list

meta def list_constant (e : expr) : list name :=
e.fold [] $ λ e _ cs,
if e.is_constant ∧ ¬ e.const_name ∈ cs
  then e.const_name :: cs
  else cs

open declaration tactic
meta def const_in_def (n : name) : tactic unit :=
do (thm _ _ t v) ← get_decl n,
   let v := v.get,
   trace $ list_constant v,
   trace $ list_constant t,
   return ()

#eval const_in_def `list.reverse_append
/-
scratch20180811.lean:17:0: information trace output
[list.append_assoc,
 list.reverse_cons,
 list.cons_append,
 list.cons,
 trivial,
 eq_self_iff_true,
 propext,
 list.append_nil,
 list.reverse_nil,
 eq.refl,
 has_append,
 list.nil_append,
 congr_arg,
 congr,
 eq.trans,
 id,
 true,
 list.nil,
 eq.mpr,
 list.has_append,
 has_append.append,
 list.reverse,
 eq,
 list.rec,
 list]
[list.has_append, has_append.append, list.reverse, eq, list]

-/
```

#### [Simon Hudon (Aug 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967321):
```
excessive memory consumption detected at 'replace' (potential solution: increase memory consumption threshold)
```

#### [Simon Hudon (Aug 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967322):
I'm invoking it from within emacs. Does that matter?

#### [Patrick Massot (Aug 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967371):
Gabriel's code also works here (in VScode).

#### [Patrick Massot (Aug 11 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967379):
and in command line as well

#### [Gabriel Ebner (Aug 11 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967430):
No it doesn't matter which editor you use.  Make sure you run `leanpkg build` before, this reduced the required amount of memory.  Typically, when you see excessive memory usage errors, the only way forward is to restart the server.

#### [Simon Hudon (Aug 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967502):
The plot thickens: I just called `#print list.reverse_append` and got:

```lean
@[simp]
theorem list.reverse_append : ∀ {α : Type u} (s t : list α), list.reverse (s ++ t) = list.reverse t ++ list.reverse s :=
[incorrect proof]
```

So I'll delete all the `.olean` files and build from scratch.

#### [Simon Hudon (Aug 11 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967760):
It did solve the problem. Thanks @**Gabriel Ebner** !

#### [Simon Hudon (Aug 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967822):
@**Patrick Massot**, if you want to restrict the output of that program to lemmas you can use  `tactic.is_proof` to filter those names. Other options can help you restrict it to types or functions.

#### [Patrick Massot (Aug 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967891):
you mean filter the output of list_constant?

#### [Simon Hudon (Aug 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967962):
Yes exactly.

#### [Patrick Massot (Aug 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967979):
Since we're at it, how would you list all file imported by the current file. That one I could implement in python with regex  :-)

#### [Simon Hudon (Aug 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967980):
for instance, you can do it as `cs.mfilter $ λ c, mk_const c >>= is_proof`

#### [Simon Hudon (Aug 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131967985):
(if `cs` is the result of `list_constant`)

#### [Patrick Massot (Aug 11 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968030):
What is the m doing in `mfilter`? Does it mean meta? Wouldn't it work with regular filter?

#### [Patrick Massot (Aug 11 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968084):
I would have simply written `cs.filter is_proof`

#### [Simon Hudon (Aug 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968163):
No the `m` is for monad becaus `mk_const` and `is_proof` use the `tactic` monad.

#### [Simon Hudon (Aug 11 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968171):
It works in trusted functions as well.

#### [Patrick Massot (Aug 11 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968218):
That's what I meant. To me monad = tactic monad = meta. I may try to refine that vision at some point

#### [Simon Hudon (Aug 11 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968221):
```quote
Since we're at it, how would you list all file imported by the current file. That one I could implement in python with regex  :-)
```
I'm stumped. I think there is very little information available about the file / module structure.

#### [Patrick Massot (Aug 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968236):
That's great. The only thing which is easy to do with regex is hard in Lean!

#### [Simon Hudon (Aug 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968240):
Ah! I see. a monad is a category theoretic concept of which `tactic` is only one instance. It's a good way of structuring programs when you want to prove things about them.

#### [Patrick Massot (Aug 11 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968284):
I'm half joking, I know there are other monads

#### [Simon Hudon (Aug 11 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968294):
Haha! Using the parser framework, you may decide to read the current file and do some of your regex work that way. And it all stays in Lean. I wouldn't call it a proper way but it would get the job done.

#### [Simon Hudon (Aug 11 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968350):
```quote
I'm half joking, I know there are other monads
```
The pedantic explanation that people throw around might actually clarify things for you :P "it's simple! A monad is just a monoid in the category of endofunctors"

... speaking of only half understanding ... :P

#### [Patrick Massot (Aug 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968362):
What is `mk_const` doing in your filtering stuff?

#### [Patrick Massot (Aug 11 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968408):
Actually I can't used the filtered list, I get `failed to synthesize type class instance for has_to_tactic_format (tactic (list name))`

#### [Simon Hudon (Aug 11 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968517):
I assume you tried `trace (mfilter ... )`. The `mfilter` expression is a monadic command so you have to execute it before using its result:

```lean
r <- mfilter /- rest -/,
trace r
```

#### [Patrick Massot (Aug 11 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968535):
indeed this works better

#### [Simon Hudon (Aug 11 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968593):
The comma here is as if you were using `>>=`, that is the sequential composition of two commands: the `mfilter` expression and the `trace` expression:

```lean
mfilter /- stuff -/ >>= λ r, trace r
```

or

```lean
mfilter /- stuff -/ >>= trace
```

after η-reduction.

#### [Patrick Massot (Aug 11 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131968936):
Thank you very much. I think I'll learn of lot from this. But right now I'm required for shooting stars hunting.

#### [Simon Hudon (Aug 11 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131969262):
Good luck!

#### [Scott Morrison (Aug 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131969820):
> The pedantic explanation that people throw around might actually clarify things for you :P "it's simple! A monad is just a monoid in the category of endofunctors"

But you also have to remember that if a computer scientist says that to you, they probably really mean "... in the category of endofuctors of the category of types"!

#### [Scott Morrison (Aug 11 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131969821):
(similarly if they just say `functor` they mean endofunctor of the category of types: we even have this in mathlib)

#### [Simon Hudon (Aug 11 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970139):
I stand corrected ... or my knowledge stands improved

#### [Simon Hudon (Aug 11 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970150):
I should really start taking advantage of the fact that so many category theorists hang around here. I've been thinking of doing a categorical treatment of liveness properties in temporal logic but it doesn't bode well: I already mess up the terminology!

#### [Scott Morrison (Aug 11 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970246):
Given that more computer scientists use "monad" now than mathematicians, my vote would be to give it to them (i.e. add "in the category of types" to the fancy-pants definition), and go back to using "triple", or "triad" from the earlier category theory literature for the general case)

#### [Simon Hudon (Aug 11 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970302):
What a shame! I thought we might make friends with mathematicians with those category theoretic ideas! Now you're giving us "we knew about monad before it was cool"

#### [Scott Morrison (Aug 12 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970709):
:-) I certainly learnt what a monad was from its CS usage before the category-theoretic obscurity.

#### [Scott Morrison (Aug 12 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970763):
btw @**Simon Hudon**, would you object if I added `@[extensionality]` to `propext`?

#### [Simon Hudon (Aug 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970830):
I find its CS usage has a pretty funny story. They didn't know how to do IO in a pure way in Haskell so they held they breath until someone unearthed an obscure category theory paper, found someone to explain it to computer scientists and help them translate those pies in the sky into physical world phenomena

#### [Simon Hudon (Aug 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970839):
No objections. Do you see any downside to doing it?

#### [Scott Morrison (Aug 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131970901):
My whole research field (tensor categories, topological field theory) is the same: just a toy for mathematicians who couldn't cope with quantum field theory, until some physicists came along and said "we've discovered this stuff we call 'topological matter'"

#### [Patrick Massot (Aug 12 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131971051):
```quote
Good luck!
```
We have been very lucky, including one amazing one. Now I'll go sleeping

#### [Simon Hudon (Aug 12 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/131971107):
I find it so mind blowing when that happens. My favorite example is Euler's number theory work being useful in cryptography after he had his fun with it.

#### [Patrick Massot (Aug 12 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/132010173):
(deleted)

#### [Chris Hughes (Sep 09 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133604168):
I had a go at making Simon's code return all the definitions used transitively. Why doesn't this work? I think it has something to do with `list.mmap`
```lean
import data.nat.basic data.list.basic

meta def list_constant (e : expr) : list name :=
e.fold [] $ λ e _ cs,
if e.is_constant ∧ ¬ e.const_name ∈ cs
  then e.const_name :: cs
  else cs

open declaration tactic
meta def const_in_def : Π (n : name), tactic (list name)
| n := do (thm _ _ t v) ← get_decl n,
let v := v.get,
let l := list_constant v,
m ← l.mmap const_in_def,
return (m.bind id).erase_dup

meta def const_in_def' (n : name) : tactic unit :=
do l ← const_in_def n,
  trace l,
  return ()

#eval const_in_def' `nat.mod_add_div
```

#### [Reid Barton (Sep 09 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133604311):
I see "match failed", is that what you mean by doesn't work?

#### [Reid Barton (Sep 09 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133604318):
I assume it's the match `(thm _ _ t v) ← get_decl n`, there are going to be constants reachable from anything as well as theorems.

#### [Reid Barton (Sep 09 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133604372):
If you add `trace n, ` at the start of that line you can see that it's processing `trivial`, which is a `defn`, not a `thm`

#### [Chris Hughes (Sep 09 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133606586):
Thanks. got it working now.

#### [Patrick Massot (Sep 09 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/full%20names/near/133620373):
You can have a look at https://github.com/leanprover-community/leancrawler/blob/master/src/leancrawler/deps.lean for more stuff you can extract from Lean (and of course you can also use the python part)

