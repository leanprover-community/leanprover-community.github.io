---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80721Whatsnewinmathlib.html
---

## [general](index.html)
### [What's new in mathlib](80721Whatsnewinmathlib.html)

#### [Johan Commelin (Oct 02 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135038239):
There is a thread in the `#maths` stream: https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F
It is a place to announce recent merges to mathlib that have clear mathematical relevance.

#### [Johan Commelin (Oct 02 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135038253):
I propose to announce other general contributions in this thread.

#### [Johan Commelin (Oct 03 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135086366):
There is now a `choice` tactic that will help with applying the axiom of choice: https://github.com/leanprover/mathlib/blob/c2df6b1f3f62575649dbe128a2c5fc9e2de26ffb/docs/tactics.md#choice
Kudos to @**Patrick Massot** :tada:

#### [Johannes Hölzl (Oct 03 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135091616):
I changed the syntax to
```lean
choose a b h using show ∀ (y : Y), ∃ (a : A) (b : B), f a b = y, ...
```
Also it allows a arbitrary prefix of quantifiers and existentials.

#### [Mario Carneiro (Oct 03 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135091695):
Does that include higher than Pi^2 complexity?

#### [Mario Carneiro (Oct 03 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135091718):
i.e. after the first `choose` you might end up with a hypothesis that is again of the form AE and repeat

#### [Mario Carneiro (Oct 03 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135091734):
(I'm not sure how applicable this is, but it would be nice to say we have full skolemization)

#### [Kevin Buzzard (Oct 03 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135091910):
"Mathlib: aiming for full skolemization". I think this should be our catch phrase.

#### [Johannes Hölzl (Oct 03 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135092306):
It should handle quantifiers again. But problem is that it doesn't handle conjunctions currently. 
```lean
example (h : ∀n m : ℕ, ∃i, ∀n:ℕ, ∃j, m = n + i ∨ m + j = n) : true :=
begin
  choose i j h using h,
  guard_hyp i := ℕ → ℕ → ℕ,
  guard_hyp j := ℕ → ℕ → ℕ → ℕ,
  guard_hyp h := ∀ (n m n_1 : ℕ), m = n_1 + i n m ∨ m + j n m n_1 = n_1,
  trivial
end
```

#### [Johannes Hölzl (Oct 03 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135092364):
also, since it doesn't use `axiom_of_choice` but `classical.some` it can be used in `Type` and not only in `Prop`.

#### [Patrick Massot (Oct 03 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135104186):
Oh, I just noticed https://github.com/leanprover/mathlib/pull/383#issuecomment-426571007 it means I don't need `set_option pp.beta true` in my demo file anymore

#### [Johan Commelin (Oct 04 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135178667):
:bell: We have a new pair of tactics: `tfae_have` and `tfae_finish`. The help with proving "the following are equivalent".
Take a look at https://github.com/leanprover/mathlib/blob/b7d314f3f2f4b18a491b359aaeb889b5c83640bc/data/list/basic.lean#L3890 and at https://github.com/leanprover/mathlib/blob/b7d314f3f2f4b18a491b359aaeb889b5c83640bc/docs/tactics.md#tfae

#### [Johan Commelin (Oct 15 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135843553):
There have been valiant efforts by the community to improve the installation experience: https://github.com/leanprover/mathlib/commit/4dbe0cdfaee201cc15cd2a74fbe8731f8bd4642a

#### [Johan Commelin (Oct 15 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/135843730):
In this context I think it is worth pointing once more to Kevin's page: https://xenaproject.wordpress.com/installing-lean-and-mathlib/ which also links to two fantastic installation walkthrough videos by Scott.

#### [Scott Morrison (Nov 01 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909599):
New in Lean itself: the patches to deal with spaces in Windows user names have landed, https://github.com/leanprover/lean-nightly/releases.

#### [Scott Morrison (Nov 01 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909612):
In mathlib, my `fin_cases` tactic was merged. Sorry I haven't been paying attention to mathlib much recently; perhaps someone else can give some updates on recent merges?

#### [Kenny Lau (Nov 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909834):
```
cd /c/lean
git pull
cd build/release
ninja clean-olean
ninja
```
:P

#### [Scott Morrison (Nov 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909849):
?

#### [Kenny Lau (Nov 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909865):
that's how to manually update lean

#### [Keeley Hoek (Nov 01 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909925):
but kenny, this means you are yet to bask in the glorious `elan` way

#### [Keeley Hoek (Nov 01 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909927):
:D

#### [Kenny Lau (Nov 01 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909973):
maybe `elan` is yet to work for windows

#### [Keeley Hoek (Nov 01 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136909976):
nah it even has a windows binary and everything!

#### [Keeley Hoek (Nov 01 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136910034):
there is even scope for like a windows installer, but someone will have to be bothered to repair it

#### [Kenny Lau (Nov 01 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136910643):
```
[...]
Current installation options:

     default toolchain: stable
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation


error: toolchain 'stable' is not installed
info: caused by: not a directory: 'C:\Users\Kenny Lau\.elan\toolchains\stable'

Press the Enter key to continue.
```

#### [Keeley Hoek (Nov 01 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136910681):
I think the old space in the name strikes again

#### [Kenny Lau (Nov 01 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136910816):
I think the correct name is `stable-x86_64-pc-windows-msvc` not `stable`

#### [Keeley Hoek (Nov 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/136911316):
Is that because there was a folder created in `...\toolchains\` which is called that? How did you get that name?
My understanding of the `elan` toolchain code is that `stable` is a special keyword, along with `nightly`. In my testing I tend to get the error `
error: toolchain 'stable' is not installed` when `elan` is failing silently because of something.
I suppose I should stop talking about this in this thread... :o

#### [Reid Barton (Nov 05 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/146800725):
Gonna be a lot of stuff this week.

#### [Kenny Lau (Nov 05 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/146801829):
oh man

#### [Johan Commelin (Nov 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/146817419):
Keeley's PR's for extending `conv` mode with `ring` and `erw` have been merged.

#### [Keeley Hoek (Nov 06 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/146840826):
Woah, the pull-request list fits onto one page now!

#### [Kenny Lau (Nov 06 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/146891337):
https://math.stackexchange.com/q/2987631/328173

#### [Johan Commelin (Dec 17 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152046738):
We just got `elide`: https://github.com/leanprover/mathlib/blob/ebf3008ba84fec5363334fa77a947f43bd71a965/docs/tactics.md#elideunelide
Thanks Mario!

#### [Kenny Lau (Dec 17 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152047300):
interesting...

#### [Johan Commelin (Dec 20 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152242473):
#489 is merged. This adds a new command `#where`. Kudos to @**Keeley Hoek** :tada: 
If you insert `#where` in a file, Lean will print a message explaining what your current namespace is, and which variables are in use.

#### [Keeley Hoek (Dec 20 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152242572):
Mario needs a medal (or at least a high-five) for the insane response time after I fixed up his suggestions

#### [Johan Commelin (Dec 22 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152396140):
34 merged PRs in the past week!
https://github.com/leanprover/mathlib/pulse

#### [Mario Carneiro (Dec 22 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152396214):
and I'm sure there are more open PRs now than when I started :P

#### [Kevin Buzzard (Dec 22 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152396943):
https://xkcd.com/2086/

#### [Patrick Massot (Dec 22 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152397916):
```quote
and I'm sure there are more open PRs now than when I started :P
```
 You did ask for many small PR everywhere there could be one big...

#### [Reid Barton (Dec 22 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's new in mathlib/near/152398095):
I think most of the remaining PRs are fairly large though

