---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39550leantravisproblems.html
---

## Stream: [general](index.html)
### Topic: [lean travis problems](39550leantravisproblems.html)

---

#### [Kevin Buzzard (Mar 29 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357753):
https://travis-ci.org/leanprover/lean/jobs/359716662#L1465

#### [Kenny Lau (Mar 29 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357759):
lol

#### [Kevin Buzzard (Mar 29 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357892):
travis is a real headache at the minute, but it affects end users because if mathlib works with lean HEAD but travis doesn't like lean HEAD then the nightly doesn't appear, and then end users who use the nightlies (like me) on more than one machine (like me) find themselves in situations where the nightly on one machine is too old for some reason, but the canonical upgrade process ("upgrade to current lean nightly and mathlib head") doesn't work.

#### [Kevin Buzzard (Mar 29 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357952):
Is travis trying to be too clever? I would imagine that Leo / Sebastian don't usually commit versions of Lean which don't compile for them.

#### [Gabriel Ebner (Mar 29 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357965):
The failure is in the external smt2_interface package.

#### [Gabriel Ebner (Mar 29 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358009):
And it shouldn't affect nightlies (they are uploaded in another configuration)

#### [Kevin Buzzard (Mar 29 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358010):
Oh that's good :-)

#### [Kevin Buzzard (Mar 29 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358069):
Since the recent incident where I upgraded Lean using my usual process and found mathlib not compiling, I've tried to become more aware of what actually happens here. So travis can give a red X at https://github.com/leanprover/lean/commits/master after a new commit but the nightly might change anyway?

#### [Kevin Buzzard (Mar 29 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358088):
Note that 8 out of the last 10 commits have been given red X's. Usually I would not care, but recent events have made me more cautious.

#### [Kenny Lau (Mar 29 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358094):
or just use git

#### [Gabriel Ebner (Mar 29 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358144):
```quote
Note that 8 out of the last 10 commits have been given red X's.
```
That's a diplomatic way to say "none of the last 20 builds have been successful". :smile:

#### [Kevin Buzzard (Mar 29 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358156):
I know I can use git Kenny, I am more concerned with people like Chris, who really don't want to have to download a bunch of stuff onto their (possibly low-spec) machine so they can spend hours compiling Lean.

#### [Gabriel Ebner (Mar 29 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358200):
There's already a PR for smt2_interface, I'll merge it and then travis should be green again.

#### [Kevin Buzzard (Mar 29 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358215):
I hope I'm not nagging. I just saw the effects of travis failure recently and was hoping not to have to go through it again. When Lean 3.4 appears there will be an alternative solution -- "get to 3.4 and then don't upgrade again".

#### [Kenny Lau (Mar 29 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358219):
stop that "don't upgrade again" crap

#### [Kevin Buzzard (Mar 29 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358270):
Kenny I need a solution which works for people who don't want to be bothered by upgrades. Imagine if all the software on your computer needed upgrading constantly and you had to build it from source.

#### [Kenny Lau (Mar 29 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358278):
not all softwares are beta

#### [Kevin Buzzard (Mar 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358376):
In practice I get people coming to Xena on Thursdays and they have managed to put their Lean in an unusable state and I just want to fix it with "download the nightly, use leanpkg upgrade/build, that's the end". This happened with Luca recently. He had edited a file in mathlib and then reverted his edits, but ended up with an olean file which did not match his lean file and this produced strange errors. We downloaded the nightly and fixed it really quickly. But with Chris more recently this approach did not work. Luca can't compile Lean from source without a huge amount of hassle.

#### [Gabriel Ebner (Mar 29 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358651):
@**Kevin Buzzard** The latest nightly is from Tuesday, did you expect a newer one?

#### [Gabriel Ebner (Mar 29 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358673):
@**Sebastian Ullrich** What is the recommended way to get nightlies in travis scripts these days (i.e. for mathib, etc.)?

#### [Kevin Buzzard (Mar 29 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358828):
@**Gabriel Ebner**  I was just expressing concern about the recent red X's. I have not cared about them in the past, but then they bit me, so now I am more wary.

#### [Kevin Buzzard (Mar 29 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358841):
Basically I reported a lean assertion violation in the lean issues tracker, and then thought "hmm maybe I should upgrade to the latest nightly to check it's still there" and then I thought "but wait, there's a red X so there's a chance that upgrading will break mathlib, which is far more of a problem to me than anything else"

#### [Gabriel Ebner (Mar 29 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358856):
To be fair, mathlib is broken with the current nightly.  (The `unit_eq` lemma is gone.)

#### [Kevin Buzzard (Mar 29 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358906):
My algorithm for dealing with the fact that this is beta software is "upgrade to latest nightly iff it won't cause a problem with mathlib".

#### [Kevin Buzzard (Mar 29 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358949):
My current test for this is "are there any signs of red X's in the list of commits? If not, was the last mathlib commit some time after the last Lean commit? If so, upgrade!"

#### [Kevin Buzzard (Mar 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358966):
I would be happy to be told about better tests. Ideally I want to be able to do the tests without bothering anyone else, but I would rather fail in the sense that I didn't upgrade when upgrading was possible, because failing by upgrading and then finding mathlib doesn't compile hurts me more (it's harder to roll back).

#### [Gabriel Ebner (Mar 29 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359097):
Why is it hard to roll back?  You can just download the previous nightly.  If you haven't seen it yet: https://github.com/leanprover/lean-nightly/releases

#### [Kevin Buzzard (Mar 29 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359107):
It's hard to roll back because `leanpkg upgrade` upgrades mathlib to HEAD

#### [Kevin Buzzard (Mar 29 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359110):
so I have to manually intervene and figure out which version of mathlib I had before and then switch to this commit.

#### [Kevin Buzzard (Mar 29 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359150):
and in the past I have not made a note of which commit I was switching from.

#### [Kevin Buzzard (Mar 29 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359166):
More generally, when students have done something dumb like editing mathlib files and they were using a nightly from 2 months ago, if the current nightly does not work then I have to decide which version of mathlib to checkout with which version of the nightly.

#### [Kevin Buzzard (Mar 29 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359169):
These are problems I actually see in practice.

#### [Kevin Buzzard (Mar 29 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359271):
I am well aware that this is software which is not quite "end-user ready" yet, but somehow I am just trying to give examples of the problems I see and am hoping that we are actually almost in a position to be able to solve them. I had not seen the nightly releases link -- thanks. I had heard talk about it but I hadn't really understood that it had happened.

#### [Kevin Buzzard (Mar 29 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359283):
If leanpkg could download the "approved mathlib commit" for each of the nightlies then this would be perfect. But maybe this is asking too much. I should however be able to download the nightly onto a student's machine, look at the commit #, and then guess an appropriate mathlib commit.

#### [Kevin Buzzard (Mar 29 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359321):
This is important because it means I don't need to compile Lean on a student's machine.

#### [Sebastian Ullrich (Mar 29 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359348):
@**Gabriel Ebner**
```quote
@**Sebastian Ullrich** What is the recommended way to get nightlies in travis scripts these days (i.e. for mathib, etc.)?
```
I was planning to figure out a script that also correctly takes `lean_version` into account, but at that point we're halfway to a proper `leanget` application that would also be useful to end users...

#### [Sebastian Ullrich (Mar 29 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124362031):
@**Gabriel Ebner** I guess this works :)
```
curl -s https://api.github.com/repos/leanprover/lean-nightly/releases | jq -r '.[0].assets | map(select(.name | contains("linux"))) | .[0].browser_download_url'
```

#### [Kevin Buzzard (Mar 29 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124363946):
I wonder if it works on a fresh OS X install?

#### [Kenny Lau (Mar 30 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124430175):
why does the latest build fail?

#### [Kenny Lau (Mar 31 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124433328):
@**Mario Carneiro**

