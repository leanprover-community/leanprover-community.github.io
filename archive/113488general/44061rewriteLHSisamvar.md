---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44061rewriteLHSisamvar.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rewrite LHS is a mvar](https://leanprover-community.github.io/archive/113488general/44061rewriteLHSisamvar.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Mar 13 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653459):
<div class="codehilite"><pre><span></span>example (h : ∀ a : nat, a = 0) : 0 = 2 := by rw h
-- rewrite tactic failed, lemma lhs is a metavariable
example (h : ∀ a : nat, a = 0) : 0 = 2 := by rw ← h
-- rewrite tactic failed, lemma lhs is a metavariable
example (h : ∀ a : nat, 0 = a) : 0 = 2 := by rw h --ok
example (h : ∀ a : nat, 0 = a) : 0 = 2 := by rw ← h
-- rewrite tactic failed, did not find instance of the pattern in the target expression
--   ?m_1
</pre></div>


<p>rewrite talks about LHS but apparently it doesn't take into account symmetry</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653641):
<p><code>example (h : ∀ a : nat, a = 0) : 0 = 2 := by rw h 2 -- succeeds!</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653703):
<p>oh this is more complicated than I thought. Of course that succeeds.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653754):
<p>That first example is really hard. I can see why it fails. How should it have a clue what to set a?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653809):
<p>Actually, in my view none of them should fail. <code>rw</code> actually should not have any issues with the LHS being an arbitrary variable; it will just trigger very easily.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653812):
<p>How is <code>rw</code> supposed to do the first one?</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653819):
<p>It has a tool for showing an arbitrary thing is 0, but it has to match 0 = 2</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653820):
<p>I think if I were rw I would let a be the first nat I found in the goal</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653822):
<p>which is 0</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653827):
<p>and then rewrite and get <code>0=2</code> and then decide I failed</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653880):
<p>Isn't that how it works? I just spent some time trying to figure this out.</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653883):
<p>compare to when I wrap everything in <code>id</code>:</p>
<div class="codehilite"><pre><span></span>example (h : ∀ a : nat, id a = id 0) : id 0 = id 2 := by rw h -- ⊢ id 0 = id 2
example (h : ∀ a : nat, id a = id 0) : id 0 = id 2 := by rw ← h -- done
example (h : ∀ a : nat, id 0 = id a) : id 0 = id 2 := by rw h -- done
example (h : ∀ a : nat, id 0 = id a) : id 0 = id 2 := by rw ← h -- ⊢ id 0 = id 2
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653892):
<p>As I just said, I am unsurprised by the first one.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653895):
<p>Why do you think it should work?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653906):
<p><code>rw</code> should trigger on the first matching occurrence of the pattern. If the LHS is a metavar, that's just the first type correct subterm</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653909):
<p>and indeed this is a=0 for the first one</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653951):
<p>it matches <code>id 0</code> so sets a=0</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653954):
<p>and now you're doomed</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653958):
<p>No, that's intended behavior</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653960):
<p>I'm not expecting it to solve the goal, but it shouldn't fail</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653962):
<p>Aah I see.</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653975):
<p>the question is why I get a bunch of weird and inconsistent failures when I remove the <code>id</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653981):
<div class="codehilite"><pre><span></span>example (h : ∀ a : nat, a = 0) : 0 = 2 := by rw ← h
-- rewrite tactic failed, lemma lhs is a metavariable
example (h&#39; : ∀ a : nat, 0 = a) : 0 = 2 := by rw h&#39;
-- succeeds
</pre></div>

#### [ Kevin Buzzard (Mar 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123653983):
<p>I had imagined these were synonymous</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654025):
<p>exactly my point</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654032):
<p>there's a funny lhs metavar check that literally checks <em>the left side</em> even if that's the destination, not the source</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654035):
<p>I see. The issue is not that they fail, it's how they fail. I understand your point now.</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654103):
<p>and the final example is even stranger - <code>example (h : ∀ a : nat, 0 = a) : 0 = 2 := by rw ← h</code> is using backwards rewrite to circumvent the buggy lhs metavar check, and instead hits a search bug, probably what the lhs metavar check was trying to avoid</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654110):
<p><code>example (h : ∀ a : nat, id 0 = id a) : id 0 = id 2 := by rw ← h -- ⊢ id 0 = id 2</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654115):
<p>I have no idea what to do with this one. It seems there are two reasonable ways to behave?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654120):
<p>I would argue that all the <code>id</code> examples are consistent</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654163):
<p>First I could spot the id 0 on the LHS and just replace it with <code>id a</code></p>

#### [ Mario Carneiro (Mar 13 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654169):
<p>Here, just like the forward rewrite version, it is rewriting <code>id ?m</code> -&gt; <code>id 0</code> and spots the first matching pattern <code>id 0</code>, so <code>?m := 0</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654178):
<p>oh ha ha I missed the \l</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654182):
<p>It's this one that confuses me:</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654183):
<p><code>example (h : ∀ a : nat, id 0 = id a) : id 0 = id 2 := by rw h -- done</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654234):
<p>Presumably it doesn't spot the <code>id 0</code> in the goal and then announce that it's going to replace it with <code>id ?m</code></p>

#### [ Sebastian Ullrich (Mar 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654238):
<p><code>kabstract</code> with a metavar will only match other metavars, it's probably trying to avoid that</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654243):
<p>instead it has to decide what to do with the <code>a</code> first</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654262):
<p>why is that? As I said it seems inconsistent with the <code>id ?m</code> behavior. Is it being special cased? I feel like you would have to work hard to make that happen</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654329):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> actually that's exactly what it does. It is rewriting <code>id 0</code> -&gt; <code>id ?m</code>, and spots the first matching pattern <code>id 0</code>, but <code>?m</code> is unconstrained by this and the result is <code>id ?m = id 2</code>. The proof is finished with the automatic <code>refl</code> after <code>rw</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654360):
<p>ha ha</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654374):
<p>yes I just noticed that this works too:</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654377):
<p><code>example (h : ∀ a : nat, 0 = a) : 2 = 0 := by rw h -- done</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654386):
<p>and here we really seem to have no option other than to leave the metavariable alone and make the match</p>

#### [ Sebastian Ullrich (Mar 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite%20LHS%20is%20a%20mvar/near/123654477):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> It's using keyed matching, which uses structural equality for the head</p>


{% endraw %}
