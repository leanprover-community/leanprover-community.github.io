---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88094bertactic.html
---

## Stream: [general](index.html)
### Topic: [über-tactic](88094bertactic.html)

---


{% raw %}
#### [ Patrick Massot (Oct 03 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098666):
I'm trying to automate my demo file, for comparison. Is there any reason not to try to write a monster tactic trying all automation we have (except speed reason)? Something like:
```lean
meta def tactic.interactive.do_it : tactic unit := do
`[try {ext}],
`[try {split}],
`[apply_eq],
`[all_goals {finish <|> tauto <|> tidy}] <|> failure
```
can do everything that should be automatic in my demo file. It could even do more without the tidy bug.

#### [ Patrick Massot (Oct 03 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098676):
It uses Simon's apply function equalities tactic
```lean
open tactic 
meta def tactic.interactive.apply_eq : tactic unit :=
do l ← local_context,
   l.mmap $ λ h, try $ do {
     `(%%x = %%y) ← infer_type h,
     (vs,t) ← infer_type x >>= mk_local_pis,
     p' ← mk_app `eq [x.mk_app vs, y.mk_app vs],
     p' ← pis vs p',
     assert (to_string h.local_pp_name ++ "_ev" : string) p',
     vs ← intros,
     vs.reverse.mmap (λ v,
       do revert v,
          applyc ``congr_fun),
     exact h },
  return ()
```

#### [ Scott Morrison (Oct 03 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098839):
Patrick, you should investigate whether we could put `finish` or `tauto` inside `tidy`. I suspect they would be fine, I've actually never used them!

#### [ Johan Commelin (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098888):
While you're at it, you should also add `cc` and `linarith` to `über`.

#### [ Scott Morrison (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098891):
(A big downside, by the way, of using `tidy` merely as a tactic script writing tool is that we don't build up a library of test cases for it, making it harder to safely tweak.)

#### [ Simon Hudon (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098893):
@**Scott Morrison|110087**, didn't you add congr_fun to `solve_by_elim` recently?

#### [ Scott Morrison (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098899):
@**Simon Hudon**, yes, but the PR hasn't landed yet.

#### [ Simon Hudon (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098908):
Aaaaah! That's why!

#### [ Johan Commelin (Oct 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098947):
```quote
(A big downside, by the way, of using `tidy` merely as a tactic script writing tool is that we don't build up a library of test cases for it, making it harder to safely tweak.)
```
We need caching.

#### [ Scott Morrison (Oct 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098949):
(I need to deal with your suggestion to use `with` when passing attributes.)

#### [ Scott Morrison (Oct 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098965):
(I've also realised there is a mistake in `solve_by_elim` when dealing with multiple sub-goals, more on that later :-)

#### [ Simon Hudon (Oct 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098977):
I keep getting confused with the PRs that haven't been merged yet

#### [ Simon Hudon (Oct 03 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099176):
```quote
I'm trying to automate my demo file, for comparison. Is there any reason not to try to write a monster tactic trying all automation we have (except speed reason)?
```

Because proofs in first order logic and anything more expressive is undecidable, you can't build a tactic so that, when it fails, you can say "it tried everything". You could always try a little harder, maybe one more call to `ext` and then `simp` will do it.

#### [ Scott Morrison (Oct 03 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099531):
@**Patrick Massot**, another way to achieve this is to add the @[tidy] annotation to tactics that you want to try.

#### [ Johan Commelin (Oct 03 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099543):
Well, maybe if it fails we could conclude "it tried everything that is straightforward up to a reasonable depth". And then "probably this proof needs an *idea*".

#### [ Scott Morrison (Oct 03 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099562):
For example, if you write ``@[tidy] meta def la := `[linarith]``, then after that `tidy` will also try calling linarith.

#### [ Scott Morrison (Oct 03 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099620):
You could make an import, for example, that super-charged `tidy` with all these other things.

#### [ Johan Commelin (Oct 03 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099623):
Can you just `local attibute [tidy] linarith`?

#### [ Scott Morrison (Oct 03 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099636):
Probably not quite that: the `[tidy]` attribute has to be on a `tactic unit` or `tactic string`.

#### [ Scott Morrison (Oct 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099643):
Any arguments (e.g. to interactive tactics) will break it.

#### [ Scott Morrison (Oct 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099649):
Although this is completely fixable.

#### [ Scott Morrison (Oct 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099666):
(and we should do so at some point...)

#### [ Mario Carneiro (Oct 03 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099892):
I think super-tactics like this are not uncommon

#### [ Mario Carneiro (Oct 03 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099919):
Everyone wants to be the one tactic to rule them all

#### [ Mario Carneiro (Oct 03 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099975):
I think `tidy` has too unassuming a name for a supertactic

#### [ Mario Carneiro (Oct 03 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100008):
It should be called `crush` or `blast` or some similarly violent thing

#### [ Simon Hudon (Oct 03 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100025):
What about `nuke`?

#### [ Simon Hudon (Oct 03 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100094):
Either that or `solve_violently`

#### [ Johan Commelin (Oct 03 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100271):
We're all still waiting for Mjölnir

#### [ Simon Hudon (Oct 03 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100412):
I was always disappointed by what `destruct` does because it feels like a synonym to `destroy`. And now we can't use `destroy` as the name of a super tactic.

#### [ Simon Hudon (Oct 03 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100421):
But we can use `annihilate`

#### [ Johan Commelin (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100510):
You know Grothendieck's parable about proving strategies?

#### [ Johan Commelin (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100516):
We should also have `soak`

#### [ Johan Commelin (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100524):
But it is very time-expensive

#### [ Simon Hudon (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100529):
I do not. Please educate me

#### [ Johan Commelin (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100536):
Might take a couple of years to run. But it will produce a couple 1000 pages of beautiful math in the end....

#### [ Johan Commelin (Oct 03 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100575):
I'm searching for it... give me a second

#### [ Simon Hudon (Oct 03 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100632):
:D

#### [ Simon Hudon (Oct 03 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100648):
A similar approach to `by grad_student`

#### [ Johan Commelin (Oct 03 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100679):
https://mathoverflow.net/a/7156

#### [ Johan Commelin (Oct 03 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100757):
I think `soak` or `immerse` is different from `grad_student`. It is even more expensive...

#### [ Scott Morrison (Oct 03 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100786):
:avocado:

#### [ Simon Hudon (Oct 03 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100881):
I love it :D That's what I call putting a problem on the back burner

#### [ Patrick Massot (Oct 03 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104489):
Blindly adding the tidy attribute to tactics only gives me deterministic timeout

#### [ Patrick Massot (Oct 03 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104631):
especially with norm_num

#### [ Patrick Massot (Oct 03 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104661):
and apply_eq

#### [ Simon Hudon (Oct 03 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104737):
`apply_eq` never fails and I believe neither does `norm_num`. Does `tidy` repeated try its tactics?

#### [ Patrick Massot (Oct 03 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104776):
Wow, you're still not sleeping? Did you decide to simply skip that step?

#### [ Simon Hudon (Oct 03 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104850):
Yeah, I'll pick it up later. I have an appointment this morning so at some point I got afraid I would sleep right passed it if I managed to fall asleep so I got out of bed

#### [ Scott Morrison (Oct 03 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104875):
Yes, tidy relies on the "do something or fail" model for tactics.

#### [ Scott Morrison (Oct 03 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104876):
Speaking of sleeping.

#### [ Patrick Massot (Oct 03 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104959):
Do you still see a way to make use of norm_num inside tidy?

#### [ Simon Hudon (Oct 03 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105003):
You can write a tactic that checks if progress was made and fails if none was made

#### [ Patrick Massot (Oct 03 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105026):
how? comparing the new goal with previous goal?

#### [ Scott Morrison (Oct 03 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105072):
And a better solution is to change the behaviour of norm_num... Who wants tactics to silently fail, anyway? :-)

#### [ Scott Morrison (Oct 03 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105092):
Exactly. It's a fun exercise, perhaps the first tactic I ever wrote. :-)

#### [ Simon Hudon (Oct 03 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105096):
```lean
meta def guard_progress (tac : tactic unit) : tactic unit :=
do gs <- get_goals,
   tac,
   gs' <- get_goals,
   guard (gs ≠ gs')
```

#### [ Patrick Massot (Oct 03 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105120):
It was too fun for Simon to resist

#### [ Simon Hudon (Oct 03 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105126):
```quote
Exactly. It's a fun exercise, perhaps the first tactic I ever wrote. :-)
```
Which one?

#### [ Simon Hudon (Oct 03 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105132):
I'm so greedy. Sorry

#### [ Patrick Massot (Oct 03 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105229):
But you are both maligning norm_num, it can actually fail

#### [ Simon Hudon (Oct 03 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105261):
I can make up for this theft. @**Patrick Massot** If you didn't have `assert`, `assertv`, `define`, `definev`, `note` or `pose`, how to you create a new goal and an associated assumption?

#### [ Johan Commelin (Oct 03 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105355):
What are `note` and `pose`?

#### [ Patrick Massot (Oct 03 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105364):
I don't even understand the question

#### [ Johan Commelin (Oct 03 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105380):
Actually, I don't recognise any of those tactics.

#### [ Johan Commelin (Oct 03 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105394):
I only use `have foo : blah,`

#### [ Johan Commelin (Oct 03 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105405):
Or `suffices`

#### [ Patrick Massot (Oct 03 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105407):
Johan, this is all meta

#### [ Patrick Massot (Oct 03 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105428):
we are discussing tactic writing here, not plebeian proof writing

#### [ Simon Hudon (Oct 03 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105524):
You got it. There's also a non-condescending way to put it :P

#### [ Patrick Massot (Oct 03 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105640):
Hopefully the fact *I* wrote this (instead of Scott, you or any other tactic writer) was a clear enough hint about how to read it :wink:

#### [ Simon Hudon (Oct 03 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105736):
I thought so too. I just had to react to the tone :laughing:

#### [ Mario Carneiro (Oct 03 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105831):
By the way, those all used to be interactive tactics. I was the one who advocated for simplifying it all down to `have` and `let`

#### [ Mario Carneiro (Oct 03 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105852):
and `suffices` because why not

#### [ Simon Hudon (Oct 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105990):
That's a nice improvement

#### [ Simon Hudon (Oct 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106008):
It's especially nice that the same keywords work in tactic mode and in term mode

#### [ Patrick Massot (Oct 03 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106062):
it's also slightly confusing that the accepted syntaxes are not quite the same

#### [ Patrick Massot (Oct 03 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106078):
fortunately that issue is easily fixed by working only in tactic mode

#### [ Patrick Massot (Oct 03 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106213):
Returning to norm_num and tidy, I'm not able to make any progress on getting `example : (0 : ℝ) < (1 : ℝ) := by tidy` to work. I tried adding norm_num to the tidy set, either with or without progress guard but no luck

#### [ Simon Hudon (Oct 03 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106356):
That's annoying

#### [ Patrick Massot (Oct 03 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106366):
That's probably only me

#### [ Simon Hudon (Oct 03 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106393):
That's what I meant, you keep complaining ... :stuck_out_tongue_wink:

#### [ Patrick Massot (Oct 03 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106409):
What's fun is that the guard_progress trick works with apply_eq which is not meant to modify the goal

#### [ Patrick Massot (Oct 03 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106424):
My tactic writing is pure Brownian motion

#### [ Simon Hudon (Oct 03 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106468):
Ah! It's time for the next lesson

#### [ Johan Commelin (Oct 03 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106484):
If we have Brownian motions in mathlib, would this help you with tactic writing :stuck_out_tongue_wink: ?

#### [ Simon Hudon (Oct 03 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106499):
When you use `get_goals`, what exactly does it give you? First wrong assumption: it tells you the proposition that the goal aims to prove.

#### [ Simon Hudon (Oct 03 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106574):
```quote
If we have Brownian motions in mathlib, would this help you with tactic writing :stuck_out_tongue_wink: ?
```
Sorry to disappoint: my research area is scheduling in distributed and cyber-physical systems (keyword: scheduling) and I'm still constantly procrastinating and arriving late

#### [ Simon Hudon (Oct 03 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106597):
You may know all the theory there is on a subject, that doesn't mean that you can do the thing yourself

#### [ Simon Hudon (Oct 03 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106704):
```quote
When you use `get_goals`, what exactly does it give you? First wrong assumption: it tells you the proposition that the goal aims to prove.
```
What it actually gives you is a list of unassigned meta variables. An unassigned meta variable has a type and a set of local constants that it can see. It doesn't have a value yet. Just like a proof goal: you know what you have to prove but you don't have a proof yet.

#### [ Simon Hudon (Oct 03 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106832):
If your goal is `⊢ succ x < succ y`, you have a meta variable `?m_1 : succ x < succ y`. If you want to apply `succ_lt_succ`, It

#### [ Simon Hudon (Oct 03 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106985):
it's like creating a meta variable `?m_2 : x < y` and then you construct an expression `succ_lt_succ ?m_2` which you assign to `?m_1`. Then, you remove `?m_1` from the list of goals and you put `?m_2` instead. The goal changes because you have a different meta variable in the list of goals now.

#### [ Patrick Massot (Oct 03 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135107297):
so the short version is: the goal comes with its local context, right?

#### [ Simon Hudon (Oct 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135107588):
That is correct

#### [ Patrick Massot (Oct 03 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135107927):
I should stop playing, and focus on the archaic manual referee process, but I have https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/auto_demo.lean

#### [ Patrick Massot (Oct 03 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135108002):
This is part of my demo file with tidy everywhere

#### [ Patrick Massot (Oct 03 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135108465):
Thanks for all your help!

#### [ Edward Ayers (Oct 03 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135111366):
```quote
What about `nuke`?
```
Can emoji be tactic names?

#### [ Kevin Buzzard (Oct 03 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135113179):
This has come up before

#### [ Kevin Buzzard (Oct 03 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135113199):
and I believe there was a trick using quotations somehow

#### [ Patrick Massot (Oct 03 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135113247):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/algebra.20on.20subtypes/near/129927817


{% endraw %}
