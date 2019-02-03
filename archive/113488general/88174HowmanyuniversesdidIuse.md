---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88174HowmanyuniversesdidIuse.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [How many universes did I use?](https://leanprover-community.github.io/archive/113488general/88174HowmanyuniversesdidIuse.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046011):
<p>I proved a theorem in Lean (that an affine scheme is a scheme). Along the way I understood a little more about universes. In particular, I realised that the ZFC proof I knew that an affine scheme was a scheme "took place entirely within Type", by which I mean that every term I used was "good" -- here "good" is defined thus: (1) Type is good; (2) If X is a term of type Y and Y is good then X is good; (3) that's it. Once I realised this I went through a lot of files in my project that had lines of the form "universes u v w" and replaced them with "universe u", I also replaced many "Type v" and "Type *" with "Type u".</p>

#### [ Kevin Buzzard (May 24 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046019):
<p>How do I check that I caught all of them?</p>

#### [ Patrick Massot (May 24 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046082):
<p>What do you gain from these modifications?</p>

#### [ Mario Carneiro (May 24 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046330):
<p>Agreed - these modifications do nothing toward your goal of eliminating unverse use</p>

#### [ Mario Carneiro (May 24 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046359):
<p>What would help is using <code>Type</code> instead of <code>Type u</code> or <code>Type*</code>, but I don't recommend this</p>

#### [ Chris Hughes (May 24 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046363):
<p>Doesn't changing Type v to Type u just make the theorem less general, and just worse?</p>

#### [ Mario Carneiro (May 24 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046428):
<p>But your definition good is overly restrictive - <code>ring</code> is not good, not even <code>ring.{0}</code>, so <code>ring A</code> is also not good</p>

#### [ Mario Carneiro (May 24 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046459):
<p>In fact clearly delineating what parts of DTT make sense in ZFC is rather delicate</p>

#### [ Patrick Massot (May 24 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127046470):
<p>We should have asked how many questions he marked before answering this thread</p>

#### [ Kevin Buzzard (May 25 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073702):
<p>You're right that my definition of good is bad. I definitely don't want to put everything into Type because then other people won't want to use my code. But there <em>is</em> an underlying question here, and perhaps the answer is in Mario's comment "In fact clearly delineating what parts of DTT make sense in ZFC is rather delicate". I want to know the answer though. Is there any way I can find out whether my definition "would go through if I went through every file I used and removed all mention of universes, and changed all <code>Type u</code> and <code>Type*</code> to <code>Type</code>"?</p>

#### [ Chris Hughes (May 25 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073805):
<p>It would go through, but nobody would be able to define a scheme structure on anything outside Type if I understand the question. So it would just be a less general definition.</p>

#### [ Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073876):
<p>"It would go through" -- how do you know this?</p>

#### [ Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073878):
<p>Cardinals wouldn't, right?</p>

#### [ Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073882):
<p>I agree that it would be a bad idea to do so</p>

#### [ Kevin Buzzard (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073883):
<p>however I know people who care about this question.</p>

#### [ Kevin Buzzard (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073893):
<p>People whose _definition_ of mathematics is ZFC could argue that I am not doing mathematics if I use two universes.</p>

#### [ Mario Carneiro (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073894):
<p>I've attempted to do this in my lean type theory paper</p>

#### [ Chris Hughes (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073895):
<p>I misunderstood the question.</p>

#### [ Mario Carneiro (May 25 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073896):
<p>several natural definitions were tried and dismissed</p>

#### [ Kevin Buzzard (May 25 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073936):
<p>There are parts of mathlib which really use more than one universe, right?</p>

#### [ Mario Carneiro (May 25 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20many%20universes%20did%20I%20use%3F/near/127073948):
<p>All parts of mathlib are universe polymorphic, so it's often hard to say, the answer is "yes trivially" if you don't ask carefully</p>


{% endraw %}
