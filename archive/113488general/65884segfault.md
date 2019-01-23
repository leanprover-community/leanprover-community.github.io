---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65884segfault.html
---

## Stream: [general](index.html)
### Topic: [segfault](65884segfault.html)

---


{% raw %}
#### [ Rob Lewis (Aug 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131243767):
I just managed to crash Lean, and realized it's been quite a while since the last time!
```lean
import tactic.wlog

example (x y : ℕ) : x ≤ y :=
begin 
  wlog : x ≤ y using [x x],
end 
```

#### [ Rob Lewis (Aug 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131243856):
@**Johannes Hölzl** This isn't really your problem in the end, but maybe it's possible to work around in `wlog`?

#### [ Kevin Buzzard (Aug 10 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131244268):
Oh nice! I absolutely agree -- Lean has been super-stable since they fixed some memory leak several months ago, it's been a joy to use. I do get the occasional segfault, almost always because my input file is garbage (e.g. I'm deleting hundreds of lines of a file and Lean just started to read a file which starts in the middle of a proof, or possibly even the middle of a word), and furthermore I've never been able to reproduce. It's very rare to get a reproducible segfault nowadays. I can reproduce here BTW.

#### [ Mario Carneiro (Aug 10 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833394):
Found it
```
open tactic
example (x : ℕ) : true :=
by do x ← get_local `x, revert_lst [x, x]
```

#### [ Mario Carneiro (Aug 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833409):
don't revert the same variable twice, I guess

#### [ Kevin Buzzard (Aug 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833419):
I remember my mother telling me that as a child

#### [ Mario Carneiro (Aug 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833424):
note that using `revert x` twice causes a regular error in the second call

#### [ Kevin Buzzard (Aug 10 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833506):
`revert_lst` has no docstring :-(

#### [ Mario Carneiro (Aug 10 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833511):
presumably it reverts a list

#### [ Kevin Buzzard (Aug 10 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131833614):
or a `lst`

#### [ Simon Hudon (Aug 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/131842254):
```quote
don't revert the same variable twice, I guess
```
I'll do what I want!

#### [ Kevin Buzzard (Sep 06 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133463161):
another wloggy segfault:

```lean
import tactic.wlog

example (m n : ℕ): false :=
begin
  wlog h : n + n ≤ m + m, -- segv
end
```

(as you can guess this is the first time I used wlog, I was just trying things out)

#### [ Simon Hudon (Sep 06 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133463196):
Dang! I don't remember putting segfault as one of the features

#### [ Simon Hudon (Sep 06 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133463264):
Can you edit the `mathlib` sources?

#### [ Mario Carneiro (Sep 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464351):
fixed

#### [ Simon Hudon (Sep 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464363):
What was the issue?

#### [ Mario Carneiro (Sep 06 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464406):
it triggered the `x <= y` special case and assumed `n + n` was a variable

#### [ Mario Carneiro (Sep 06 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464424):
I am not sure what happened after that, but possibly this got passed into `revert`

#### [ Mario Carneiro (Sep 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464482):
that's what caused the last segfault, at least

#### [ Simon Hudon (Sep 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464486):
I see. That was not a source of segfault I thought of

#### [ Simon Hudon (Sep 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464510):
Did you add Kevin's example to the test suite?

#### [ Mario Carneiro (Sep 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464520):
I think `wlog` parsing is currently way too complicated. It should be broken up and documented

#### [ Simon Hudon (Sep 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464532):
That makes sense, I really don't understand the tactic anymore.

#### [ Mario Carneiro (Sep 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464737):
This test fails now:
```
example {x y z : ℕ} : true :=
begin
  suffices : false, trivial,
  wlog h : x ≤ y + z,
  { guard_target x ≤ y + z ∨ x ≤ z + y,
    admit },
  { guard_hyp h := x ≤ y + z,
    guard_target false,
    admit }
end
```
what the heck is this supposed to do?

#### [ Simon Hudon (Sep 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464783):
Can you show the state right after `wlog`?

#### [ Mario Carneiro (Sep 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464784):
it fails

#### [ Mario Carneiro (Sep 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464841):
the error is ``To generate cases at least two permutations are required, i.e. `using [x y, y x]` or exactly 0 or 2 variables`` but the problem is that the given pattern `x ≤ y + z` has 3 variables

#### [ Simon Hudon (Sep 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464866):
It tries to prove false just to make sure that no call to `trivial` or assumption finishes the goal before we can see the result

#### [ Simon Hudon (Sep 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464900):
Ah I see. That's from when we only considered two variables

#### [ Simon Hudon (Sep 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464914):
It guessed `x` and `y`.

#### [ Mario Carneiro (Sep 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464971):
My question is, what is this supposed to do in the first place? It used to just take the last two variables and permute them, as you can see from the asserted target

#### [ Simon Hudon (Sep 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464977):
I'm surprised it hasn't failed before

#### [ Mario Carneiro (Sep 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133464999):
It was previously just matching the list of variables against `(x :: y :: _)` i.e. >= 2 vars, take the first 2

#### [ Mario Carneiro (Sep 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465010):
I changed this to `[x, y]` and now this test fails

#### [ Simon Hudon (Sep 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465041):
Why are you changing it to `[x,y]`?

#### [ Simon Hudon (Sep 06 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465126):
You were the one suggesting we guess the last two variables of the pattern.

#### [ Mario Carneiro (Sep 06 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465136):
No, that's what it was doing before I touched it

#### [ Mario Carneiro (Sep 06 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465154):
I don't understand why the code is written that way, but there is a test asserting this behavior

#### [ Simon Hudon (Sep 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465303):
I'm looking at master right now and what I see is `(x :: y :: _)`, not `[x, y]`

#### [ Mario Carneiro (Sep 06 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133465862):
https://github.com/leanprover/mathlib/blob/master/tactic/wlog.lean#L203

#### [ Simon Hudon (Sep 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466307):
My mistake, I must have done something wrong

#### [ Simon Hudon (Sep 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466314):
What happens if you switch it back to `(x :: y :: _)`?

#### [ Mario Carneiro (Sep 06 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466399):
then it works, although the behavior in that case is peculiar

#### [ Mario Carneiro (Sep 06 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466434):
it just permutes the last two variables discovered in the term, which is a bit weirdly nondeterministic

#### [ Simon Hudon (Sep 06 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466559):
What would you expect it to do in this case?

#### [ Mario Carneiro (Sep 06 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466711):
fail, or do all permutations of the n variables

#### [ Johan Commelin (Sep 06 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466801):
permutations are now in mathlib. Does that help?

#### [ Johan Commelin (Sep 06 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466835):
Ooh, wait. They were already for a long time... it is the signs that are new.

#### [ Mario Carneiro (Sep 06 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133466842):
we already had `list.permutations`

#### [ Simon Hudon (Sep 06 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467037):
I'm not sure if you recall but we have had that conversation before. You were in favor of guessing the variables, I was in favor of requiring that the user specify them

#### [ Mario Carneiro (Sep 06 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467099):
Actually both options are available here

#### [ Mario Carneiro (Sep 06 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467319):
honestly I have no idea why it's so complicated. 2 variables seems to be special cased in the parsing, so `wlog h : x ≤ y + z using x y z` just fails (previously it would just permute `x` and `y`)

#### [ Mario Carneiro (Sep 06 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467406):
Part of the problem is that I don't know the specification of the tactic, and the code is so ad hoc it's hard to tell what is intended and what is accident

#### [ Simon Hudon (Sep 06 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467904):
It's probably that I started it intending to support only two variables and @**Johannes Hölzl** probably didn't want to disturb too much

#### [ Simon Hudon (Sep 06 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467916):
Do you want to settle on a specification now?

#### [ Mario Carneiro (Sep 06 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133467987):
I'm trying to get one out of the docstring now

#### [ Mario Carneiro (Sep 06 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133468471):
There are I guess 24 combinations resulting from the parse:
```
wlog h? (: pat)? (:= r)? (using x y z)?
wlog h? (: pat)? (:= r)? (using [x y z, z y x])?
```
* `h` is just a name. If it is omitted, the default name is `case` (Although from the code it looks like if `r` is the name of a local constant then it is renamed to `h`?)

#### [ Mario Carneiro (Sep 06 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133468600):
* If `pat` and `r` are both omitted there is an error
* If `pat` is given but not `r` it becomes a subgoal
* If `r` is given but not `pat` it is reconstructed as the first disjunct of `r`'s type

#### [ Mario Carneiro (Sep 06 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133468776):
* If `using` list is omitted it is inferred as the set of distinct variables in `pat`
* If `using` is a list of variables then all permutations of those variables are considered
* If `using` is a nonempty list of permutations then the first permutation is considered as the list of variables (and the rest must actually be permutations)
* If `using` is an empty list of permutations it is treated as omitted

#### [ Mario Carneiro (Sep 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469008):
Oh, I think this is the justification for the last two variables thing:
```
(4) `wlog : R x y using x y` and `wlog : R x y`
  Produces the case `R x y ∨ R y x`. If `R` is ≤, then the disjunction discharged using linearity.
  If `using x y` is avoided then `x` and `y` are the last two variables appearing in the
  expression `R x y`. -/
```

#### [ Simon Hudon (Sep 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469052):
Yes, I think that was the entirety of the docstring before Johannes worked on `wlog`

#### [ Mario Carneiro (Sep 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469109):
I guess this is to allow for when the relation is itself parameterized in some variables

#### [ Mario Carneiro (Sep 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469133):
I wonder whether we can use type information to eliminate some permutations

#### [ Simon Hudon (Sep 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469134):
I think we can map those notations to a set of core parameters. Sometimes they are specified by the user, sometimes they have to be guessed. Working from there, we should say how they are guessed and what is done with those core parameters.

#### [ Mario Carneiro (Sep 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469179):
There is already a notion of core parameters, I think, which are used in `tactic.wlog` (noninteractive)

#### [ Simon Hudon (Sep 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469201):
Ah good so now we're only struggling with parsing / guessing

#### [ Simon Hudon (Sep 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469273):
Actually `R x y` was just a way of writing `x ≤ y` while not involving a specific relation.

#### [ Mario Carneiro (Sep 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469274):
Right, the parser is the behemoth

#### [ Mario Carneiro (Sep 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469287):
I think there was some example where a relation like `x = y [mod n]` came up

#### [ Mario Carneiro (Sep 06 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469307):
but even `has_le.le` can use variables, like the type or instance - we don't want to permute these

#### [ Simon Hudon (Sep 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469395):
That's true

#### [ Mario Carneiro (Sep 06 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469448):
I was thinking we can use permutations for which the permuted relation is well typed, but this has exponential growth for large relations

#### [ Mario Carneiro (Sep 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469562):
Alternatively, we can require that permuted variables have the same type as each other, but maybe there are counterexamples where you permute a<->b and c<->d where `c : T a` and `d : T b`

#### [ Mario Carneiro (Sep 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133469606):
then again, in this case you will certainly be providing the permutation list explicitly so we don't have to guess it

#### [ Mario Carneiro (Sep 06 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133470142):
actually, `tactic.wlog` is also doing some fancy footwork, and it has no segfault protection of its own

#### [ Mario Carneiro (Sep 06 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133470276):
The signature is
```
meta def wlog (vars' : list expr) (h_cases fst_case : expr) (perms : list (list expr)) : tactic unit
```
where `vars'` is the set of variables being permuted, `h_cases` is a local constant with the proof of the disjunction, `fst_case` is the pattern (with variables in the same order as the first permutation), and `perms` is a list of permutations of `vars'`

#### [ Kevin Buzzard (Sep 06 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471151):
Is there a case for splitting off the case of two variables and having two tactics? What I actually want to do is `wlog degree f ≤ degree g`. Is that not possible? (my goal is symmetric in the polynomials `f` and `g`).

#### [ Mario Carneiro (Sep 06 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471336):
It is possible, indeed the default behavior of wlog should do what you want

#### [ Mario Carneiro (Sep 06 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471354):
if not, just put `using f g` at the end

#### [ Mario Carneiro (Sep 06 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471434):
This example blows my mind:
```
  have h : p n i ∨ p i m ∨ p m i, from sorry,
  wlog : p n i := h using n m i,
```
It infers the permutation list `[n m i, i m n, m i n]`

#### [ Mario Carneiro (Sep 06 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133471727):
Oh! The example (and tactic) is actually broken, the test doesn't actually finish the proof so it doesn't notice

#### [ Simon Hudon (Sep 06 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/segfault/near/133472124):
It's sometimes baffling how much we can live with bugs in proof tactics


{% endraw %}
