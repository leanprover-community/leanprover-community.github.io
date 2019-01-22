---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/04578isomorphismtheorems.html
---

## [maths](index.html)
### [isomorphism theorems](04578isomorphismtheorems.html)

#### [Kevin Buzzard (Sep 03 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133249273):
I need what is apparently called the "fourth isomorphism theorem" for R-modules, R a commutative ring. Of course more generally we will need all the isomorphism theorems for groups and R-modules, plus various extra bits and bobs. I might do some of this today in a coding session with the undergraduates. I propose doing the thing I actually want, which is that if $$R$$ is a general ring (commutativity not necessary) and $$N$$ is a sub-$$R$$-module of the $$R$$-module $$M$$ then there's a canonical order-preserving bijection between submodules of $$M/N$$ and submodules of $$M$$ containing $$N$$. My proposal is that I write this code at about 2pm today UK time so before then perhaps I should have a clue about the best way to say this. Here are some dumb questions.

The reason I want this is that I want that a quotient module of a Noetherian module is Noetherian. Because Noetherian modules are not yet in mathlib, but they are in mathlib-community, am I right in thinking I should be doing this work in a fork of the mathlib-community repo?

What should this file be called? `fourth_isomorphism_theorem.lean` sounds daft. Should it just be tagged onto quotient_module.lean in `linear_algebra`? I don't know how much more commutative algebra should up in this directory -- this stuff is not linear algebra any more.

Those of us who care about Galois insertions might now point out that the result I want is perhaps something to do with Galois insertions or Galois connections. Currently my instinct is to completely ignore all of this because I don't see what it buys us. I'd be interested in opinions. My proposal is to write an equiv between the type of submodules of M/N and the type of submodules of M containing N and then prove that it is order-preserving. Now my (good) understanding of `equiv` tells me exactly what I should be proving about the constructions. But my (poor) understanding of lattices doesn't tell me exactly what I should be proving about the order: I mean -- I know I should be proving that the constructions in each direction preserve inclusion, but should I be proving that some map is some morphism of lattices, or something? 

My goal is that a quotient module of a Noetherian module is Noetherian, and I want the proof to be "this set is well-founded, by definition of Noetherian module, and hence this subset is well-founded, so we're done". What structures should I be using to formalise this statement in order for it to be mathlib-ready?

#### [Kevin Buzzard (Sep 03 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133253484):
Gaargh. I've checked out the `noetherian` branch of community mathlib and it doesn't build. `order/conditionally_complete_lattice.lean` has a problem in line 128 for example: 

```lean
/--Adding a point to a set preserves its boundedness above.-/
@[simp] lemma bdd_above_insert : bdd_above (insert a s) ↔ bdd_above s :=
⟨show bdd_above (insert a s) → bdd_above s, from bdd_above_subset (by simp),
 show bdd_above s → bdd_above (insert a s), by rw[insert_eq]; finish⟩
```

->

```
α : Type u,
_inst_1 : semilattice_sup α,
s : set α,
a : α
⊢ bdd_above s → bdd_above (insert a s)
conditionally_complete_lattice.lean:131:62: error

solve1 tactic failed, focused goal has not been solved
state:
α : Type u,
_inst_1 : semilattice_sup α,
s : set α,
a : α,
a_1 : bdd_above s,
a_2 : ¬bdd_above (insert a s)
⊢ false
```

(`finish` is failing). Is there an easy fix for this?

#### [Kenny Lau (Sep 03 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133253600):
`finish [bdd_above_insert]`?

#### [Kevin Buzzard (Sep 03 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133253683):
but there are 100 errors

#### [Kevin Buzzard (Sep 03 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133253685):
so I'd rather find out what's going on

#### [Johan Commelin (Sep 03 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133253804):
Maybe your `olean` files aren't matching with this branch? Did you try a recompile from scratch?

#### [Kevin Buzzard (Sep 03 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133253841):
maybe I messed up. I thought I'd done exactly that

#### [Kevin Buzzard (Sep 03 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133253870):
I've removed all the olean files and am trying again

#### [Kevin Buzzard (Sep 03 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133253923):
Dumb question: if I clone a lean repo, make all the .olean files, and then checkout a different branch, do all the .olean files magically disappear?

#### [Johan Commelin (Sep 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254408):
Nope. They are in `.gitignore`. So git doesn't touch them.

#### [Johannes Hölzl (Sep 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254454):
Also, Lean should know which olean files to rebuild. But sometimes it happens that a olean file is flying around were the corresponding lean file was removed. This produces strange results sometimes...

#### [Johan Commelin (Sep 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254456):
So if you are on a very recent `mathlib:master`, and you've built. Then you checkout `noetherian` which is a couple of days old, then you get `olean`-files that are too new.

#### [Kevin Buzzard (Sep 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254459):
no there are still errors.

#### [Kevin Buzzard (Sep 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254464):
I removed all .olean files and the noetherian branch does not compile. Is this to do with "This branch is 2 commits ahead, 37 commits behind leanprover:master."?

#### [Kevin Buzzard (Sep 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254469):
Is there a magic merge type command I can type to rebase or whatever the right word is?

#### [Johan Commelin (Sep 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254480):
With `noetherian` checked out, you could try `git merge master`.

#### [Johan Commelin (Sep 03 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254519):
There shouldn't be any conflicts.

#### [Kevin Buzzard (Sep 03 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254531):
`git merge master` reports `already up to date` and nothing seemed to happen.

#### [Kevin Buzzard (Sep 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254533):
It would be really nice to get a working `noetherian.lean` by 2pm

#### [Kevin Buzzard (Sep 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254547):
I can happily dump the entire repo and clone again.

#### [Johan Commelin (Sep 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254553):
Give me 2 minutes

#### [Johan Commelin (Sep 03 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254638):
```shell
git checkout master
git pull
git checkout noetherian
git merge master
git push origin noetherian
```

#### [Johan Commelin (Sep 03 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254646):
Can you checkout `noetherian` and `git pull origin noetherian`?

#### [Kevin Buzzard (Sep 03 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254687):
I'm building using `nightly-2018-06-21`. Is this an issue?

#### [Kevin Buzzard (Sep 03 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254693):
I just cloned again from github

#### [Johan Commelin (Sep 03 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254704):
I'll also rebuild. But this machine is not the fastest in the world.

#### [Kevin Buzzard (Sep 03 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254881):
Will switching lean version change the behaviour of `finish`?

#### [Johan Commelin (Sep 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254935):
I'm glad your version of 2pm is still 90 minutes away...

#### [Kevin Buzzard (Sep 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254941):
Oh!

#### [Kevin Buzzard (Sep 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254944):
I might have found my erro

#### [Kevin Buzzard (Sep 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254945):
r

#### [Kevin Buzzard (Sep 03 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133254968):
I think I just don't understand branches. Maybe I thought I had pulled but I hadn't pulled.

#### [Johan Commelin (Sep 03 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255015):
Does my little log of shell commands make sense to you?

#### [Kevin Buzzard (Sep 03 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255019):
I just cloned the repo again

#### [Johan Commelin (Sep 03 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255040):
I pushed a commit that merges the latest master into `noetherian`

#### [Johan Commelin (Sep 03 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255302):
Woohow... I'm also getting boatloads of errors.

#### [Johan Commelin (Sep 03 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255308):
Did I break the system?

#### [Kevin Buzzard (Sep 03 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255417):
which version of Lean are you using?

#### [Johan Commelin (Sep 03 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255438):
Whatever `elan` gave me. I think/hope the most recent. Let me check.

#### [Johan Commelin (Sep 03 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255457):
`Lean (version 3.4.1, commit 17fe3decaf8a, Release)`

#### [Johan Commelin (Sep 03 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255549):
Everything is complaining that `data/set/basic.lean` uses sorry.

#### [Kevin Buzzard (Sep 03 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255648):
so `data/set/basic.lean` works fine in regular mathlib but I have an error in community mathlib

#### [Kevin Buzzard (Sep 03 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255745):
```lean
@[simp] theorem insert_diff_singleton {a : α} {s : set α} :
  insert a (s \ {a}) = insert a s :=
by simp [insert_eq, union_diff_self]
```
takes an age to compile and then I get a deterministic time-out

#### [Johannes Hölzl (Sep 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133255803):
what does `git status` say? Are there any changed files?

#### [Kevin Buzzard (Sep 03 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256008):
I only just cloned

#### [Kevin Buzzard (Sep 03 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256024):
```lean
buzzard@ebony:~/lean-projects/mathlib-community$ git status
On branch noetherian
Your branch is up-to-date with 'origin/noetherian'.
nothing to commit, working directory clean
buzzard@ebony:~/lean-projects/mathlib-community$ 

```

#### [Johan Commelin (Sep 03 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256027):
The latest commit on the `noetherian` branch is a merging in `master`. I just did that.

#### [Scott Morrison (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256033):
@**Johan Commelin**, rebasing might have been better than merging. :-) (Says someone who only learnt to rebase last week.)

#### [Kevin Buzzard (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256073):
The issue existed before the merge

#### [Scott Morrison (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256076):
I noticed the noetherian branch was broken, too.

#### [Scott Morrison (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256079):
Sorry, should have said something!

#### [Kevin Buzzard (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256096):
is the master branch broken?

#### [Kevin Buzzard (Sep 03 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256224):
[of community-mathlib]

#### [Scott Morrison (Sep 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256260):
no, it's good

#### [Kevin Buzzard (Sep 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256280):
which version of Lean are you using?

#### [Scott Morrison (Sep 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256283):
I'm guessing the culprit is Mario's changes data/set/basic

#### [Scott Morrison (Sep 03 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256361):
What are these "versions" of which you speak? I use elan, so running lean automatically runs whichever version each respository says it needs. :-)

#### [Scott Morrison (Sep 03 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256378):
Looking at the leanpkg.toml for mathlib, that's 3.4.1

#### [Johan Commelin (Sep 03 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256482):
Ok, what should we do?

#### [Johan Commelin (Sep 03 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256491):
Can we still rebase?

#### [Johan Commelin (Sep 03 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256511):
Then we can use a built latest master branch, and look at the 5 changes or so, that are introduced by noetherian

#### [Kevin Buzzard (Sep 03 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256573):
Oh I can work around this, I don't need it to compile. I will just work with mathlib master and not use the Noetherian branch.

#### [Johan Commelin (Sep 03 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256588):
Sure, but you want to work on noetherian modules, right?

#### [Johan Commelin (Sep 03 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256596):
So you want the TFAE theorem

#### [Johan Commelin (Sep 03 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256616):
And that is on the noetherian branch, and it depends on changes to `data/set/basic.lean` that seem to cause wreckage.

#### [Kevin Buzzard (Sep 03 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256624):
right

#### [Kevin Buzzard (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256675):
so I'll just not have noetherian modules and I can still do the thing I was planning on doing, which was proving the 4th isomorphism theorem for R-modules

#### [Kevin Buzzard (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256678):
we just don't get the application

#### [Johan Commelin (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256680):
@**Johannes Hölzl** @**Scott Morrison** would it be ok to rewrite history on this branch?

#### [Kevin Buzzard (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256690):
It's OK, I have changed my plans

#### [Scott Morrison (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256691):
fine with me :-)

#### [Johan Commelin (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256706):
And you don't get the lattice structure and all the other foundational stuff that Mario did.

#### [Kevin Buzzard (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256717):
I don't need this stuff right now

#### [Kevin Buzzard (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256723):
I just need it at some point

#### [Kevin Buzzard (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256725):
it's no longer time-critical

#### [Johannes Hölzl (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256729):
Should I rebase it?

#### [Johan Commelin (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256735):
Yes please.

#### [Kevin Buzzard (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256736):
I don't mind either way

#### [Johan Commelin (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133256739):
Throw away my merge commit.

#### [Johannes Hölzl (Sep 03 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133257077):
just a second I need to fix some stuff which broke by Marios `data/set/basic.lean` changes

#### [Johannes Hölzl (Sep 03 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133257831):
`noetherian` is now rebased and fixes the problems with the simp set. But maybe we just shouldn't add `singleton_union` and `union_singleton` to the simp set...

#### [Johan Commelin (Sep 03 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133258618):
Thanks a lot!

#### [Johan Commelin (Sep 03 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133258637):
@**Kevin Buzzard** A fresh clone should repair your issues.

#### [Kenny Lau (Sep 03 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133258753):
*A clone of Kevin Buzzard arrives with a wrench*

#### [Johan Commelin (Sep 03 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133266146):
@**Kevin Buzzard** What did you end up doing?

#### [Kevin Buzzard (Sep 03 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133267878):
```lean
import linear_algebra.quotient_module

open is_submodule

local attribute [instance] quotient_rel

definition module.correspondence_theorem (R : Type*) [ring R] (M : Type*) [module R M]
  (N : set M) [is_submodule N] :
{Xbar : set (quotient M N) // is_submodule Xbar} ≃ {X : set M // is_submodule X ∧ N ⊆ X} :=
{ to_fun := λ Xbar, ⟨quotient.mk ⁻¹' Xbar.1,⟨
    @@is_submodule.preimage _ _ _ Xbar.2 _ (is_linear_map_quotient_mk N),
    λ n Hn,begin
      show quotient.mk n ∈ Xbar.val,
      have : ⟦n⟧ = ⟦0⟧,
        apply quotient.sound,
        show n - 0 ∈ N,
        simpa,
      rw this,
      haveI := Xbar.property,
      show (0 : quotient M N) ∈ Xbar.val,
      exact @is_submodule.zero _ _ _ _ Xbar.val _,
end⟩⟩,
  inv_fun := λ X, ⟨((quotient.mk '' X.val) : set (quotient M N)),
    by haveI := X.2.1; exact is_submodule.image (is_linear_map_quotient_mk N)⟩,
  left_inv := λ ⟨Pbar,_⟩,subtype.eq $ set.image_preimage_eq quotient.exists_rep,
  right_inv := λ ⟨P,HP⟩, subtype.eq $ set.ext $ λ x,⟨begin
    intro H,
    have H2 : ∃ (y : M), y ∈ P ∧ y ≈ x,
      simpa using H,
    rcases H2 with ⟨y,H3,H4⟩,
    rw quotient_rel_eq at H4,
    have H5 : y - (y - x) ∈ P,
      refine @is_submodule.sub _ _ _ _ _ HP.1 _ _ H3 _, -- fixing type class inference issues
      exact HP.2 H4, -- goal still x ∈ P.val, but H5 is y - (y - x) ∈ P.val
    convert H5, -- goal is now x = y - (y - x)
    simp, -- solves this
  end
  ,by apply set.subset_preimage_image⟩,
}

```

#### [Kevin Buzzard (Sep 03 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133267879):
4th isomorphism theorem!

#### [Kevin Buzzard (Sep 03 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133267919):
I spent about an hour talking about the mathematics (some of the audience had not seen quotient groups before) and then about an hour writing the code, although I would never have done it if Chris hadn't shown up and occasionally made comments like "oh you need to put `local attribute [instance] quotient_rel`".

#### [Kevin Buzzard (Sep 03 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133267998):
It's only a bijection between the sets, but checking that it's inclusion-preserving will be trivial because this is just a diagram chase using functions, not using the module properties at all. Note the excessive number of `@`s in the proof; this is apparently (according to @**Chris Hughes** ) because Chris has figured out how to make type class inference work OK for quotient structures, but quotient modules haven't been through his filter yet.

#### [Kevin Buzzard (Sep 03 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133268001):
Chris -- what needs doing?

#### [Johan Commelin (Sep 03 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133268214):
Ok, that's really cool! So this was basically a very successful live Lean coding session in front of students!

#### [Kevin Buzzard (Sep 03 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133268371):
`to_fun` was particularly painful. There are tricks here which would have made my life a lot easier, someone just needs to take the tricks from quotient groups and apply them here.

#### [Johan Commelin (Sep 03 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133268612):
So, how far are we from showing that quotient of Noetherian is Noetherian?

#### [Johan Commelin (Sep 03 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133268620):
By now it is math-trivial...

#### [Johan Commelin (Sep 03 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133268689):
But in Lean? We need that a suitable sublattice of a well-founded lattice is well-founded. And we need to glue everything.

#### [Chris Hughes (Sep 03 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133268697):
Very easy. I think it's just an application of `inv_image_wf` with the isomorphism.

#### [Chris Hughes (Sep 03 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133268722):
But you also need `S \sub T \iff f S \sub f T`

#### [Kevin Buzzard (Sep 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133269273):
I'm just doing that now. I just used `tidy` for the first time :grinning:

#### [Kevin Buzzard (Sep 03 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133269333):
In fact both inclusions are `by tidy`

#### [Kevin Buzzard (Sep 03 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133271268):
OK dumb question: where is the construction which gives a module from a submodule?

#### [Johan Commelin (Sep 03 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133271286):
https://github.com/leanprover/mathlib/blob/master/linear_algebra/subtype_module.lean

#### [Kevin Buzzard (Sep 03 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133271296):
Thanks.

#### [Johan Commelin (Sep 03 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133271342):
This could potentially be `subtype_instance`d

#### [Kevin Buzzard (Sep 03 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133271824):
so now I find myself proving that a submodule of a submodule is a submodule :-/

#### [Johan Commelin (Sep 03 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133271968):
Yes... that is really annoying.

#### [Johan Commelin (Sep 03 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133272026):
In the end we'll want some lattice inclusion for that part of the story as well. And it seems you are already proving it.

#### [Kevin Buzzard (Sep 03 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133275777):
tidy is just pwning a lot of these goals. It's just a lot of chasing trivialities around and perhaps tidy is just the thing for it.

#### [Kevin Buzzard (Sep 03 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133275793):
Yes, my goal before I go to bed today is to prove that submodules and quotient modules of Noetherian modules are Noetherian.

#### [Johan Commelin (Sep 03 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133275837):
Do you check what kind of proofs `tidy` generates? Or do you just write `by tidy` and move on?

#### [Kevin Buzzard (Sep 03 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133277571):
I write `by tidy` and then observe that in contrast to Scott I am unable to immediately see what proofs it generates, so I am forced to move on.

#### [Patrick Massot (Sep 03 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133277630):
you could use the hole command to see what it does

#### [Kevin Buzzard (Sep 03 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133278197):
I need some advice. I have `f : equiv X Y` between two types both of which have ``le`. I have proved a <= b -> f a <= f b` and `c <= d -> f.symm c <= f.symm d` (so f is an equivalence of preorders). I now want to deduce `a  < b <-> f a < f b` and I just wrote a boring proof of this. I feel like I'm missing some trick.

#### [Chris Hughes (Sep 03 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133278580):
This is the least boring proof I could come up with
```lean
import data.equiv.basic
variables {α : Type*} {β : Type*} [preorder α] [preorder β]

example (f : α ≃ β) (hf : ∀ a b, a ≤ b → f a ≤ f b)
  (hf' : ∀ a b, a ≤ b → f.symm a ≤ f.symm b) : ∀ a b, a < b ↔ f a < f b :=
have ∀ a b, a ≤ b ↔ f a ≤ f b, from λ a b, 
⟨hf a b, λ h, by rw [← equiv.inverse_apply_apply f a, ← equiv.inverse_apply_apply f b];
  exact hf' (f a) (f b) h⟩,
λ a b, by simp [lt_iff_le_not_le, this]

```

#### [Kevin Buzzard (Sep 03 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133279287):
I am wondering now if this proof should be generated by a tactic. I have beefed up my f to an equivalence of sets-equipped-with-le and then anything that I can define in a reasonable way just using le should be the same on both sides.

#### [Mario Carneiro (Sep 04 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133280969):
You should use the theorems about order isomorphisms

#### [Kevin Buzzard (Sep 04 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133281184):
right.

#### [Kevin Buzzard (Sep 04 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133281198):
I am drowning in trivialities, switching between your `is_submodule M`, the subtype `{X : set M // is_submodule X}`, and related subtypes such as `{X : set M // is_submodule X \and X \sub N}`.

#### [Kevin Buzzard (Sep 04 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133281203):
furthermore there is a hot tub full of teenage girls about 10 metres from me and they're getting really loud

#### [Kevin Buzzard (Sep 04 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133281245):
I think it might be about time to tell my daughter to quieten down a bit. I can't really think straight any more

#### [Kevin Buzzard (Sep 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133298907):
OK sanity restored (they're all asleep). @**Mario Carneiro** or @**Patrick Massot**  I need advice -- mostly about management of code . I have proved subs of Noeth mods are Noeth and I have essentially proved quotients of Noeth mods are Noeth. Currently the proofs are horrible, it was getting harder and harder to work last night and some lemmas are called `temp_name` etc so I don't even feel it's ready to PR. But I have momentum and I'd like to finish the job. Currently in the `noetherian` branch of community mathlib (which I am actively working on) there's a bunch of stuff at the beginning of `noetherian.lean` which Mario wrote and which has nothing to do with Noetherian stuff -- it sets up a new type `submodule R M` which is the R-submodules of the R-module M. Mario set it up as a structure but it has precisely the structure of a subtype, it's the subsets of M with some property. The...whatever they're called...are called `N.s` (the subset) and `N.sub` (the proof it's a submodule) rather than `N.val` and `N.property`. Which is preferable and why? I propose moving this stuff somewhere else, because I want to use this language in the correspondence theorem. The proof that subquotients of Noetherian things are Noetherian naturally uses this submodule lattice all over the place but I want to use the same language for the correspondence theorem. Currently I've moved the definition of submodule to `submodule.lean` in `linear_algebra` even though it's not linear algebra in my opinion -- this is absolutely commutative ring theory. My main organisational problem is that I now want to prove things like "there's an injective map `submodule R (quotient M N) -> submodule R M` which I've proved in some sense -- I have a Lean theorem saying some interpretation of this -- but I am convinced I'm not using the right language. Mario proved `submodule R M` (see how much easier it is to understand if you use maths notation rather than alpha beta?) is a partial order so now I seem to want to prove theorems about order embeddings, and use the fact that if `X -> Y` is an order embedding then the order on `X` is induced from the order of `Y` somehow. Where do I look for this theorem and the relevant definitions -- are these theorems about orders, or semi-bot-sup-lattices, or what? Should this go into yet another file, called `submodule_order.lean` or does it all go in `submodule.lean` -- should this file be in ring theory or linear algebra, etc etc? 

What I'm trying to say is: the maths is now in Lean, but it's not in a good state. When I was writing the schemes repo I would just dump it all in and move on. But Scott and others have convinced me that this is not a good long term plan, so I now want to spend just an hour or two making it as mathlib-ready as I can before actually PR'ing it. If anyone has any comments on (a) the merits of creating random new files like submodule.lean and where they should go or (b) the abstract theorem I should be proving about the relationship between the partial orders `submodule R (quotient M N)` and `submodule R M` (there's an injective map from the left to the right which preserves the order relation; this must already be a concept in Lean) then I'd be grateful to hear them. I am reluctant to put any more commutative ring theory into `linear_algebra` by the way.

#### [Kenny Lau (Sep 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133298942):
did you sleep?

#### [Kevin Buzzard (Sep 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133298951):
I did. The joys of earplugs.

#### [Kevin Buzzard (Sep 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133298957):
I've just spent 2 hours tidying up though

#### [Kevin Buzzard (Sep 04 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133299046):
Kenny do you know what kind of Lean structure I have? I have two partial orders X and Y, an injection X -> Y, and a proof that a <= b iff f a <= f b. Furthermore (although I don't know if this is relevant) if f a <= d <= f b then there exists c such that f c = d.

#### [Kenny Lau (Sep 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133299103):
I don't even know what kind of mathematical structure you have

#### [Patrick Massot (Sep 04 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133299133):
Do you know about https://github.com/leanprover/mathlib/blob/master/order/order_iso.lean?

#### [Patrick Massot (Sep 04 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133299204):
It seems to be exactly the file you want

#### [Kevin Buzzard (Sep 04 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133299219):
right -- thanks. I've never looked at that file I don't think. This is exactly why I asked here :-)

#### [Kevin Buzzard (Sep 04 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133299231):
Aah so that's the meaning of the symbol `≼o` which I've seen several times before :-)

#### [Scott Morrison (Sep 04 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133299325):
Your PR should also certainly create a whole new folder `commutative_algebra`. It's time!

#### [Kevin Buzzard (Sep 04 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133299632):
Thanks Scott. OK so current proposal: new directory `commutative_algebra`, move file `noetherian.lean` into it, leave current files about modules where they are, nonsense about order embeddings in a file called something like `module_order.lean`(is this a bad name?) perhaps in ring_theory (because this part works for general rings), and now short proofs that subquotients of Noetherian modules are Noetherian ends up in Noetherian.lean. Hmm. Maybe even this part should be done for general rings; the theory very quickly becomes a commutative-ring-only theory, but this very basic part seems to work in general (we are doing "Noetherian left modules" I suspect, but I don't think it's an unreasonable convention to have "all modules over a non-comm ring, if not stated otherwise, are left modules" -- I think that's the current convention anyway.

#### [Kevin Buzzard (Sep 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396163):
The 4th isomorphism theorem needed some rewriting after Chris' changes to quotient modules. What is really striking now is that the theorem is still pretty much the same, but the *complete* proof that the correspondence is order-preserving is `by tidy`. Commutative algebra comes with a whole bunch of diagram chases and my intial impression is that `tidy` seems like it will be a really useful tool. I don't know if Mario is worried that compile times will go through the roof though...

```lean
import ring_theory.submodule
import linear_algebra.quotient_module -- I propose moving this to ring_theory
import tactic.tidy
import order.order_iso

open is_submodule
open quotient_module

definition module.correspondence_equiv (R) [ring R] (M) [module R M] (N : set M) [is_submodule N] :
(has_le.le : submodule R (quotient M N) → submodule R (quotient M N) → Prop) ≃o 
(has_le.le : {X : submodule R M // N ⊆ X} → {X : submodule R M // N ⊆ X} → Prop) := {
  to_fun := λ Xbar, ⟨submodule.pullback (mk : M → (quotient M N))
    (is_linear_map_quotient_mk N) Xbar,λ n Hn,begin
      show ↑n ∈ Xbar.s,
      haveI := Xbar.sub,
      have : ((0 : M) : quotient M N) ∈ Xbar.s,
        exact @is_submodule.zero _ _ _ _ Xbar.s _,
      suffices : (n : quotient M N) = (0 : M),
        rwa this,
      rw quotient_module.eq,
      simp [Hn],
    end⟩,
  inv_fun := λ X, submodule.pushforward mk (is_linear_map_quotient_mk N) X.val,
  left_inv := λ P, submodule.eq $ set.image_preimage_eq quotient_module.quotient.exists_rep,
  right_inv := λ ⟨P,HP⟩, subtype.eq $ begin
    show submodule.pullback mk _ (submodule.pushforward mk _ P) = P,
    ext x,
    split,swap,apply set.subset_preimage_image,
    rintro ⟨y,Hy,Hyx⟩,
    change (y : quotient M N) = x at Hyx,
    rw quotient_module.eq at Hyx,
    suffices : y - (y - x) ∈ P,
      simpa,
    haveI := P.sub,
    exact is_submodule.sub Hy (HP Hyx),
  end,
  ord := by tidy, -- I love you Scott Morrison
}
```

#### [Johan Commelin (Sep 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396242):
Well, `tidy` can also tell you the proof. That will shave a bit of time off future compiles.

#### [Johan Commelin (Sep 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396246):
Use the hole command, Luke!

#### [Kevin Buzzard (Sep 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396341):
`  ord := begin intros a b, dsimp at *, simp at *, fsplit, work_on_goal 0 { intros a_1 a_2 a_3, simp at *, solve_by_elim }, intros a_1 a_2 a_3, induction a_2, work_on_goal 0 { simp at *, solve_by_elim }, refl end, -- I love you Scott Morrison`

#### [Kevin Buzzard (Sep 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396363):
Should I use that proof instead? I am tempted to change the comment to "this proof brought to you by tidy"

#### [Patrick Massot (Sep 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396406):
I don't think we want that kind of proof in mathlib

#### [Patrick Massot (Sep 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396410):
But it should be very easy to clean

#### [Patrick Massot (Sep 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396471):
or else you can leave `by tidy`

#### [Patrick Massot (Sep 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396481):
we already have proofs by tidy (somewhat hidden by autoparam)

#### [Johan Commelin (Sep 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396482):
If you leave `tidy` there, what does the profiler say?

#### [Johan Commelin (Sep 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396489):
I guess it is pretty fast.

#### [Johan Commelin (Sep 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism theorems/near/133396503):
And the proof looks a lot more readable to me if it is just `tidy` (-;

