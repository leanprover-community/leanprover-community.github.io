---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10818mathlibbroken.html
---

## Stream: [general](index.html)
### Topic: [mathlib broken?](10818mathlibbroken.html)

---


{% raw %}
#### [ Scott Morrison (Apr 04 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124599682):
Actually, it seems like the problem is just in mathlib.

#### [ Scott Morrison (Apr 04 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124599728):
Does anyone else get
````
/Users/scott/projects/lean/lean-category-theory/_target/deps/mathlib/data/nat/sqrt.lean:103:48: error: solve1 tactic failed, focused goal has not been solved

state:

n : ℕ,
sqrt_aux_is_sqrt :
 ∀ (m r : ℕ),
 r * r ≤ n →
 n < (r + 2 ^ (m + 1)) * (r + 2 ^ (m + 1)) → is_sqrt n (sqrt_aux (2 ^ m * 2 ^ m) (2 * r * 2 ^ m) (n - r * r)),
m r : ℕ,
h₁ : r * r ≤ n,
h₂ : n < (r + 2 ^ (m + 1 + 1)) * (r + 2 ^ (m + 1 + 1)),
a : n < (r + 2 ^ (m + 1)) * (r + 2 ^ (m + 1)),
this : is_sqrt n (sqrt_aux (2 ^ m * 2 ^ m) (r * 2 * 2 ^ m) (n - r * r))
⊢ is_sqrt n (sqrt_aux (2 ^ m * 2 ^ m) (r * (2 * 2 ^ m)) (n - r * r))
 ````

#### [ Scott Morrison (Apr 04 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124599971):
The `finish` [here](https://github.com/leanprover/mathlib/blob/master/order/complete_boolean_algebra.lean#L42) in mathlib/order/complete_boolean_algebra seems to take a long time to execute.

#### [ Mario Carneiro (Apr 04 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601878):
mathlib is currently broken. I am working on a fix

#### [ Kenny Lau (Apr 04 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601879):
actually what is the cause of the problem?

#### [ Kenny Lau (Apr 04 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601880):
I roughly saw something to do with `punit.eq`

#### [ Kenny Lau (Apr 04 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601881):
I checked the init and it is indeed there

#### [ Mario Carneiro (Apr 04 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601909):
The biggest change was the `has_pow` typeclass, which changes the way power functions are used across the library

#### [ Kenny Lau (Apr 04 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601924):
then why do I see `punit.eq`?

#### [ Mario Carneiro (Apr 04 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601925):
`group_power` needed to be heavily edited, and that caused downstream changes

#### [ Kenny Lau (Apr 04 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601936):
alright, good luck

#### [ Mario Carneiro (Apr 04 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601982):
(plus I have some HW due tomorrow which is interfering with my maintenance work)

#### [ Kenny Lau (Apr 04 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601983):
I see

#### [ Scott Morrison (Apr 04 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124602377):
Let us know if there is work that can be delegated. (Right now delegating might be more work than just fixing, but in the long run it may be worth thinking about sustainable models of mathlib maintenance.)

#### [ Mario Carneiro (Apr 04 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124602936):
For the moment I think I would rather do this work myself, and would indeed discourage others from trying to fix it on their own, because this creates merge headaches, especially in this sort of cross-library modification.

#### [ Mario Carneiro (Apr 04 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124602984):
I've got it 99% working, there's just one error in ordinal_notation that I need to check the original proof to fix. I could push it now, but it won't compile in travis

#### [ Scott Morrison (Apr 04 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124608602):
A  99% fix would still be helpful, as at the moment huge chunks of mathlib recompile every time I run leanpkg. This makes it almost impossible to work.

#### [ Mario Carneiro (Apr 04 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124609640):
I'll push a 99% fix if I can't get it working tonight.

#### [ Scott Morrison (Apr 04 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124609646):
no problem --- I'm managing as is, actually.

#### [ Kevin Buzzard (Apr 04 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616232):
```quote
For the moment I think I would rather do this work myself, and would indeed discourage others from trying to fix it on their own, because this creates merge headaches, especially in this sort of cross-library modification.
```
The folly of youth :-)

#### [ Kevin Buzzard (Apr 04 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616233):
"I am young and enthusiastic and I know I can fix it myself, so let me fix it myself"

#### [ Kevin Buzzard (Apr 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616270):
I am just the opposite nowadays

#### [ Kenny Lau (Apr 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616280):
a loucura da juventude

#### [ Kevin Buzzard (Apr 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616282):
"I am old and busy, and I know I can do it, so sure go ahead and do it, and then I can remove it from my job list and furthermore I can blame you later ;-)"

#### [ Mario Carneiro (Apr 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616285):
I see your point, but given that I've already done most of it, someone else jumping in at this point will only make things worse

#### [ Mario Carneiro (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616292):
If I hadn't started the work I'd agree with you

#### [ Kevin Buzzard (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616294):
I am sure you're right on this occasion.

#### [ Kevin Buzzard (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616300):
If you're in the middle then it's surely easiest just to keep going.

#### [ Kevin Buzzard (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616305):
I know now that the wise move is just to sit and wait and not upgrade Lean

#### [ Kevin Buzzard (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616306):
see my comment in travis

#### [ Mario Carneiro (Apr 04 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616356):
Indeed. My fix includes updating the leanpkg.toml file to explicitly reference the nightly it should work with, so hopefully going forward we shouldn't have the problem that updating breaks mathlib

#### [ Kevin Buzzard (Apr 04 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616437):
I think that all this leanpkg.toml tinkering is a really good idea

#### [ Kevin Buzzard (Apr 04 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616477):
because in the medium term future things will get more chaotic (when lean 4 appears)

#### [ Kevin Buzzard (Apr 04 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616484):
and if we have some pretty robust stuff available for making lean and mathlib not break for people wanting to stay on the bleeding edge

#### [ Kevin Buzzard (Apr 04 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616486):
this will be brilliant

#### [ Mario Carneiro (Apr 04 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617600):
okay, I missed my self imposed deadline, have my 99% fix

#### [ Kenny Lau (Apr 04 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617601):
e o teu HW?

#### [ Mario Carneiro (Apr 04 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617650):
nao terminei

#### [ Kenny Lau (Apr 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617665):
oh hey finalmente me falas em portugues

#### [ Mario Carneiro (Apr 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617667):
lol

#### [ Kenny Lau (Apr 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617669):
mdr

#### [ Mario Carneiro (Apr 04 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124619310):
@**Sebastian Ullrich** Could you troubleshoot the mathlib leanpkg.toml setup? Adding the lean_version just makes travis complain about it, and doesn't change the result.

#### [ Sebastian Ullrich (Apr 04 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124619473):
I'll try to build an MVP of leanup today that is sufficient for using it with Travis

#### [ Mario Carneiro (Apr 05 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124656640):
I think I've figured out the problem: Travis is using https://github.com/leanprover/lean-nightly/blob/gh-pages/build/lean-nightly-linux.tar.gz, which hasn't been updated in 15 days, presumably since the nightly publication process changed. Now I guess I have to go to https://github.com/leanprover/lean-nightly/releases and download the appropriate nightly, but that either requires parsing the TOML file or inserting the date in two more places in the travis.yml file. I assume this is what `leanup` is going to do?

#### [ Gabriel Ebner (Apr 05 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124660148):
Yes, see previous discussion here: https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/lean.20travis.20problems/near/124359348

#### [ Sebastian Ullrich (Apr 05 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124660826):
@**Mario Carneiro** Thanks for the quickfix :) . I'll have to supervise an exam today first, but after that I'll continue working on a proper leanup.


{% endraw %}
