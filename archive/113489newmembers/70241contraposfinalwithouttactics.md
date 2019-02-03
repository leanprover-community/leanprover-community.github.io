---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/70241contraposfinalwithouttactics.html
---

## Stream: [new members](index.html)
### Topic: [contrapos_final without tactics?](70241contraposfinalwithouttactics.html)

---


{% raw %}
#### [ Joseph Corneli (Jan 23 2019 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/contrapos_final%20without%20tactics%3F/near/156704881):
<p>I'm looking at <a href="https://github.com/kbuzzard/xena/blob/master/lean_together/contrapos_final.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/lean_together/contrapos_final.lean">https://github.com/kbuzzard/xena/blob/master/lean_together/contrapos_final.lean</a></p>
<p>The question at the end is:</p>
<div class="codehilite"><pre><span></span>theorem both_ways (P Q : Prop) : (P → Q) ↔ (¬ Q → ¬ P) := by ??
</pre></div>


<p>Here's a sensible seeming answer with tactics:</p>
<div class="codehilite"><pre><span></span>theorem both_ways (P Q : Prop) : (P → Q) ↔ (¬ Q → ¬ P) :=
begin
 split,
 apply contrapositive,
 apply other_way
end
</pre></div>


<p>I'm wondering how to do it without tactics.   I got started this way but this doesn't work.</p>
<div class="codehilite"><pre><span></span>theorem both_ways_again (P Q : Prop) : (P → Q) ↔ (¬ Q → ¬ P) :=
iff.intro (assume h1 : (P → Q), have (¬ Q → ¬ P), from contrapositive h1)
          (assume h2 : (¬ Q → ¬ P), have (P → Q), from other_way h2)
</pre></div>

#### [ Chris Hughes (Jan 23 2019 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/contrapos_final%20without%20tactics%3F/near/156705017):
<p>You want <code>show</code> instead of <code>have</code> I think.</p>

#### [ Rob Lewis (Jan 23 2019 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/contrapos_final%20without%20tactics%3F/near/156705048):
<p>The <code>(P Q : Prop)</code> arguments in <code>contrapositive</code> and <code>other_way</code> should be implicit, or you should put in placeholders when you use them.</p>

#### [ Rob Lewis (Jan 23 2019 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/contrapos_final%20without%20tactics%3F/near/156705101):
<p>Also what Chris says.</p>

#### [ Joseph Corneli (Jan 23 2019 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/contrapos_final%20without%20tactics%3F/near/156705905):
<p>OK, <code>show</code> is a definite, thanks.</p>
<p>Revision:</p>
<div class="codehilite"><pre><span></span>theorem both_ways&#39; {P Q : Prop} : (P → Q) ↔ (¬ Q → ¬ P) :=
iff.intro (assume h1 : (P → Q), show (¬ Q → ¬ P), from (contrapositive h1))
          (assume h2 : (¬ Q → ¬ P), show (P → Q), from (other_way h2))
</pre></div>


<p>I've modified the arguments for the lemmas be implicit, but Lean complains that it can't synthesise the placeholder.  I can't either!</p>
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
P Q : Prop
⊢ Type ?
</pre></div>

#### [ Joseph Corneli (Jan 23 2019 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/contrapos_final%20without%20tactics%3F/near/156706290):
<p>oh, wait a second, now the server has refreshed and it seems to be fine.</p>

#### [ Joseph Corneli (Jan 23 2019 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/contrapos_final%20without%20tactics%3F/near/156706332):
<p><span aria-label="tada" class="emoji emoji-1f389" role="img" title="tada">:tada:</span></p>


{% endraw %}
