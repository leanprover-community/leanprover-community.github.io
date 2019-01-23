---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30186detectingterminalgoals.html
---

## Stream: [general](index.html)
### Topic: [detecting terminal goals](30186detectingterminalgoals.html)

---

#### [Scott Morrison (Apr 26 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718057):
I have a little tactic that is meant to determine with the current goal is "terminal", that is, no other goals depend on it.

#### [Scott Morrison (Apr 26 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718058):
Unfortunately it is not working at the moment.

#### [Scott Morrison (Apr 26 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718069):
(The idea is just that if you know your current goal is terminal, you can be much more aggressive in discharging it, because nothing can go wrong later.)

#### [Scott Morrison (Apr 26 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718108):
I currently have
````lean
meta def metavariables : tactic (list expr) :=
do r ← result,
   pure (r.fold [] $ λ e _ l,
     match e with
     | expr.mvar _ _ _ := insert e l
     | _ := l
     end)

meta def terminal_goal : tactic unit :=
  do goals ← get_goals,
     let current_goal := goals.head,
     other_goals ← metavariables,
     let other_goals := other_goals.erase current_goal,
     other_goals.mmap' $ λ g, (do t ← infer_type g, d ← kdepends_on t current_goal,
                                  monad.whenb d $ pp t >>= λ s, fail ("This is not a terminal goal: " ++ s.to_string ++ " depends on it."))
````

#### [Scott Morrison (Apr 26 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718118):
And this works great detecting when the current goal appears in the form `?m_1` in a later goal.

#### [Scott Morrison (Apr 26 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718123):
But fails to detect that the current goal appears as something like `?m_1[_]` in a later goal.

#### [Scott Morrison (Apr 26 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718134):
Q1. Is this already implemented somewhere, better?

#### [Scott Morrison (Apr 26 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718136):
Q2. Any suggestions how I fix it?

#### [Scott Morrison (Apr 26 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125718312):
Here's a MWE:
````
private structure D :=
 ( w : ℕ → Type )
 ( x : list (w 0) )
 
 private def test_terminal_goal : D :=
 begin
    split,
    swap,
    success_if_fail { terminal_goal }, -- succeeds, because terminal_goal correctly fails
    intros,
    success_if_fail { terminal_goal }, -- fails, because terminal_goal incorrectly succeeds
    exact ℕ,
    exact []
 end     
````

#### [Simon Hudon (Apr 26 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125723861):
I think I would do it as:

```
meta def terminal_goal' : tactic unit :=
do g :: gs ← get_goals,
   gs.for_each $ λ g', guard (g'.occurs g)
```

It works with your example but does it work with your use cases?

#### [Scott Morrison (Apr 27 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125757828):
@**Simon Hudon**, this doesn't seem to work in other cases. My tests are here: <https://gist.github.com/semorrison/5188f3c3e508148657be4d66f4875d8d> if you want to have a look. I have to run now, but will try to decipher why your version isn't working on the other tests later.

#### [Simon Hudon (Apr 27 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125758036):
Ok, I'll have a look when I wake up :)

#### [Scott Morrison (Apr 27 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125758093):
I don't really understand the logic of your suggestion: surely you meant `guard (¬ g.occurs g')` not `guard (g'.occurs g)`? In any case neither of those work. Sleep well. :-)

#### [Simon Hudon (Apr 27 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125758109):
Thanks :)

#### [Scott Morrison (Apr 28 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125804165):
When I see a goal with a "parametrised metavariable" like `?m_1[0]`, what does the underlying `expr` look like?  I can't decipher what it should be.

#### [Scott Morrison (Apr 28 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125804217):
Is it just an `app` of an `mvar`?

#### [Scott Morrison (Apr 28 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125805155):
Okay --- I've worked this all out. For anyone keeping score:
````
meta def metavariables : tactic (list expr) :=
do r ← result,
   pure (r.fold [] $ λ e _ l,
     match e with
     | expr.mvar _ _ _ := insert e l
     | _ := l
     end)

meta def propositional_goal : tactic unit :=
do goals ← get_goals,
   let current_goal := goals.head,
   current_goal_type ← infer_type current_goal,
   p ← is_prop current_goal_type,
   guard p

meta def subsingleton_goal : tactic unit :=
do goals ← get_goals,
   let current_goal := goals.head,
   current_goal_type ← infer_type current_goal >>= instantiate_mvars,
   to_expr ``(subsingleton %%current_goal_type) >>= mk_instance >> skip

meta def terminal_goal : tactic unit :=
propositional_goal <|> subsingleton_goal <|>
do goals ← get_goals,
   let current_goal := goals.head,
   other_goals ← metavariables,
   let other_goals := other_goals.erase current_goal,
   other_goals.mmap' $ λ g, (do t ← infer_type g, t ← instantiate_mvars t, trace t, d ← kdepends_on t current_goal,
                                monad.whenb d $ pp t >>= λ s, fail ("This is not a terminal goal: " ++ s.to_string ++ " depends on it."))
````

#### [Simon Hudon (Apr 28 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806640):
I don't know if you still need the answer but `?m_1[0]` is a regular meta variable. I think `[0]`signals the context that the variable can see. I don't know how to decode it though.

#### [Scott Morrison (Apr 28 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806851):
Thanks @**Simon Hudon**, all sorted out. `?m_1[0]` is encoded simply as an application of an `mvar` on the expressions appearing inside the `[ ... ]`. It turned out that I was missing an `instantiate_mvars`, which was preventing successfully detection of these sort of "dependent mvars". I've made a PR for my `terminal_goal` tactic and some relatives. https://github.com/leanprover/mathlib/pull/125

#### [Simon Hudon (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806862):
Oh, good! Sorry I couldn't help you any more than that

#### [Simon Hudon (Apr 28 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806864):
You have to be careful with those variables. They sneak up on you

#### [Scott Morrison (Apr 28 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125806959):
I can't believe that I've written code that successfully uses `instantiate_mvars`. What it actually means is still voodoo to me.

#### [Simon Hudon (Apr 28 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807129):
I can try to demystify if you like

#### [Simon Hudon (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807154):
Have you used `get_goals` and `set_goals`?

#### [Scott Morrison (Apr 28 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807155):
Yes, many times!

#### [Simon Hudon (Apr 28 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807201):
Good! And do you know that `get_goals` returns a list of expressions that are in fact unassigned meta variables?

#### [Scott Morrison (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807208):
Yes!

#### [Scott Morrison (Apr 28 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807213):
(If I were Kevin, I'd be promising to write documentation in exchange for your explanation. :-)

#### [Simon Hudon (Apr 28 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807272):
(Haha! Where's Kevin when we need him!)

Good. So think of the proof state as being made of two parts (for the sake of this explanation): list of goals which is an arbitrary list of meta variables and the set of all allowed meta variables, some of which are assigned a value.

#### [Scott Morrison (Apr 28 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807316):
Great!

#### [Simon Hudon (Apr 28 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807363):
The relationship between the proof state and whatever you're trying to prove is that, when you enter tactic mode, you create an unassigned variable, put it in the list of goals and that variable is in fact the proof that you're supposed to return. From that point on, the assertion you're trying to prove does not matter. Only the variables and the goals do.

#### [Simon Hudon (Apr 28 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807371):
I don't know if you've ever had that problem but sometimes, you succeed in leaving a tactic block and when you finish the proof, you're told that your proof contains unassigned variables. Does this ring a bell?

#### [Simon Hudon (Apr 28 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807911):
Long story short, `instantiate_mvar` finds all the `mvar` nodes in your expression and, if the meta variable has a value (or type `expr`) in the proof state it replaces `mvar` with it. That means that, if you're pattern matching (using `match`) on an expression and you're looking for `expr.app (expr.app (const `eq _) e0) e1` and that you mean `mvar` instead, even if that variable is assigned to a value that matches exactly what you're looking for, the pattern matching will fail. That's why it's prudent to use `instantiate_mvar` before matching on a `expr` of which you don't know for sure that it doesn't contain meta variables.

#### [Simon Hudon (Apr 28 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125807919):
I realize my explanation was a bit round about. I just needed to introduce the idea that the life span of meta variables is a whole proof and that it doesn't disappear once it's assigned.

#### [Scott Morrison (Apr 28 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808197):
I see.

#### [Scott Morrison (Apr 28 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808200):
I've encountered needing it in another strange place, as well, which I think matches with your explanation.

#### [Scott Morrison (Apr 28 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808204):
I was writing a tool for finding _all_ the possible rewrites of a given expression by a given rule.

#### [Scott Morrison (Apr 28 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808210):
Unfortunately the built-in rewrite has some problems --- once it has matched some of the parameters of your rewrite rule a particular way, it will subsequently only match the parameters the same way, when looking for further places the rule matches.

#### [Scott Morrison (Apr 28 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808211):
This even persists between different invocations of `rewrite_core`, because this information is actually stored in the tactic state.

#### [Scott Morrison (Apr 28 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808251):
To solve this, I had to write a tactic `lock_tactic_state (t : tactic A) : tactic A` which just discards any changes to the tactic state after invocation.

#### [Scott Morrison (Apr 28 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808255):
This throws away any information the tactic state was storing about how rewrite parameters had to match.

#### [Scott Morrison (Apr 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808262):
Unfortunately, the proofs that rewrite_core produced where suddenly full of metavariables!

#### [Scott Morrison (Apr 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808263):
I understand now that this is because these metavariables were _assigned_, but not _instantiated_, so when I discarded the `tactic_state` those assignments were being lost.

#### [Scott Morrison (Apr 28 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808300):
Calling `instantiate_mvars` on the proof term, before discarding the state, saved those assignments.

#### [Scott Morrison (Apr 28 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808303):
phew! :-)

#### [Scott Morrison (Apr 28 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808308):
(Sorry I missed the end  of your explanation; family things happening at this end. I'm going to ping you @**Simon Hudon** as I expect you'll find this other example interesting.)

#### [Simon Hudon (Apr 28 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808470):
I'd be curious to see how you implemented `lock_tactic_state`. Did you deconstruct the tactic value and extract the expected proof?

#### [Simon Hudon (Apr 28 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20terminal%20goals/near/125808523):
I'm looking forward to your next example. I'll probably see it when I wake up. Incidentally, Australia is way too far! Someone should move it closer to Europe and America, that way our days would overlap!

