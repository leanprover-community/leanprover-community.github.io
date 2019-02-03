---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63294refinestruct.html
---

## Stream: [general](index.html)
### Topic: [refine_struct](63294refinestruct.html)

---


{% raw %}
#### [ Simon Hudon (May 31 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127375963):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I finally got around to writing a <code>refine_struct</code> tactic to generalize and simplify the automation of the <code>indexed_product</code> proofs. </p>
<p>You can see it in action here <a href="https://github.com/cipher1024/lean-differential-topology/blob/master/src/indexed_product.lean" target="_blank" title="https://github.com/cipher1024/lean-differential-topology/blob/master/src/indexed_product.lean">https://github.com/cipher1024/lean-differential-topology/blob/master/src/indexed_product.lean</a>.</p>
<p>You can use it as:</p>
<div class="codehilite"><pre><span></span>refine_struct { some_field := foo, .. },
repeat
{ intro x,
  have_field,
  apply (field x) }
</pre></div>


<p>In short, <code>refine_struct</code> acts a bit like <code>refine</code> but tags every goal it produces with the name of the field that requires it. Then you can use tactics such as <code>have_field</code> / <code>let_field</code> to add an assumption or a local definition that stands for the accessor of the current field. You can also use <code>apply_field</code> if you just want to use it as a rule.</p>
<p>Does it look useful in this state? My next step would be to PR it into <code>mathlib</code>.</p>

#### [ Patrick Massot (May 31 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127379709):
<p>Do you examples of using <code>have_field</code>, <code>let_field</code> and <code>aply_field</code>? I can see in the indexed product that you don't need to provide any data, which is already really nice, but I don't understand how the other tactics can be used</p>

#### [ Simon Hudon (May 31 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380010):
<p>I you were to write the proof of semigroup by hand, it would go like this:</p>
<div class="codehilite"><pre><span></span>instance semigroup [∀ i, semigroup $ f i] : semigroup (Π i : I, f i) :=
begin
  refine_struct { .. },
  { intros x y i, apply_field, apply (x i), apply (y i) },
  { have_field,
    intros, funext, simp!, apply field }
end
</pre></div>

#### [ Simon Hudon (May 31 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380073):
<p>The first proof constructs the semigroup operator and the second proves associativity. While the first proof only works for binary functions, the second one is pretty much what the tactic does.</p>

#### [ Simon Hudon (May 31 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380096):
<p>In the second proof, <code>apply_field</code> would work if <code>funext</code> didn't discard the goal's tags</p>

#### [ Patrick Massot (May 31 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380238):
<p>it seems <code>have_field</code> already discards it</p>

#### [ Patrick Massot (May 31 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380289):
<p>why <code>simp!</code> rather than <code>dsimp</code>?</p>

#### [ Simon Hudon (May 31 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380290):
<p>Yeah, you're right. I'll fix that</p>

#### [ Simon Hudon (May 31 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380298):
<p>No reasons, I hadn't thought of using <code>dsimp</code> that way</p>

#### [ Patrick Massot (May 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380361):
<p>just trying to say more precisely what Lean shoud do (I also tend to use <code>exact</code> when it works, instead of <code>apply</code> like you did)</p>

#### [ Patrick Massot (May 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380365):
<p>anyway, it looks very nice</p>

#### [ Patrick Massot (May 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380461):
<p>can you also do Kevin's <code>instance : comm_monoid ℕ+ </code> using it?</p>

#### [ Simon Hudon (May 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380471):
<p>I see. I would only use one command in that case but I wanted to demonstrate <code>apply_field</code>.</p>

#### [ Simon Hudon (May 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380474):
<p>Can you send me a link?</p>

#### [ Simon Hudon (May 31 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380480):
<p>Is it the transport problem?</p>

#### [ Patrick Massot (May 31 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380570):
<p>no, building this instance on pnat, given we already have it on nat</p>

#### [ Simon Hudon (May 31 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380583):
<p>It should be doable</p>

#### [ Patrick Massot (May 31 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380585):
<p><a href="https://github.com/leanprover/mathlib/blob/ad92a9ba47f417916aab365d13db653fa8991a84/data/pnat.lean#L52" target="_blank" title="https://github.com/leanprover/mathlib/blob/ad92a9ba47f417916aab365d13db653fa8991a84/data/pnat.lean#L52">https://github.com/leanprover/mathlib/blob/ad92a9ba47f417916aab365d13db653fa8991a84/data/pnat.lean#L52</a></p>

#### [ Simon Hudon (May 31 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380629):
<p>Thanks, I'll have a look after dinner :)</p>

#### [ Patrick Massot (May 31 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380638):
<p>Kevin complained about Lean not being smart enough to do it by itself</p>

#### [ Patrick Massot (May 31 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380644):
<p>Is it already dinner time in Quebec?</p>

#### [ Simon Hudon (May 31 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380864):
<p>Here's my first attempt:</p>
<div class="codehilite"><pre><span></span>instance : comm_monoid ℕ+ :=
begin
  refine_struct
    { mul       := λ m n : ℕ+, (⟨m.1 * n.1, mul_pos m.2 n.2⟩ : ℕ+),
      one       := succ_pnat 0, .. },
  repeat
  { have_field,
    intros, refine subtype.eq _, apply field }
end
</pre></div>

#### [ Simon Hudon (May 31 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380877):
<p>It's a mistake to expect Lean to be smart. Lean is effective.</p>

#### [ Simon Hudon (May 31 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380883):
<p>It is a bit early for dinner but my sister just had a baby so I'm giving her a hand</p>

#### [ Simon Hudon (May 31 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380942):
<p>Ok, I gotta run now</p>

#### [ Patrick Massot (May 31 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127380952):
<p>thanks!</p>

#### [ Patrick Massot (May 31 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127381384):
<p>Ok, so obvisouly I can add </p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">derive_field&#39;</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">b</span> <span class="err">←</span> <span class="n">target</span> <span class="bp">&gt;&gt;=</span> <span class="n">is_prop</span><span class="o">,</span>
  <span class="k">if</span> <span class="n">b</span> <span class="k">then</span> <span class="n">do</span>
     <span class="n">field</span> <span class="err">←</span> <span class="n">get_current_field</span><span class="o">,</span>
     <span class="n">intros</span><span class="o">,</span>
     <span class="bp">`</span><span class="o">[</span><span class="n">refine</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="bp">_</span><span class="o">],</span>
     <span class="n">applyc</span> <span class="n">field</span>
  <span class="k">else</span> <span class="n">do</span> <span class="n">skip</span>
</pre></div>


<p>And the instance becomes</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="bp">ℕ+</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine_struct</span>
    <span class="o">{</span> <span class="n">mul</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">,</span> <span class="o">(</span><span class="bp">⟨</span><span class="n">m</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">n</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">mul_pos</span> <span class="n">m</span><span class="bp">.</span><span class="mi">2</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">),</span>
      <span class="n">one</span>       <span class="o">:=</span> <span class="n">succ_pnat</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">..</span> <span class="o">}</span> <span class="bp">;</span> <span class="n">derive_field&#39;</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (May 31 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127381392):
<p>Question: can we start <code>derive_field</code> by some testing whether the target type is a pi type of a sub-type?</p>

#### [ Patrick Massot (May 31 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127381462):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> did you see that?</p>

#### [ Patrick Massot (May 31 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127381491):
<p>It's a mistake to expect Lean to be smart. Expect Simon to be smart.</p>

#### [ Simon Hudon (Jun 01 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391159):
<p>Haha! That was not quite my point ...</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391298):
<p>I think there is a good lesson in there though... "Computers don't prove theorems, people prove theorems"</p>

#### [ Simon Hudon (Jun 01 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391350):
<p>Is this the slogan for the new National Reasoning Association?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391370):
<p>the Bot Lobby</p>

#### [ Simon Hudon (Jun 01 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391558):
<p>Are you trying to emphasize the "people prove theorems" or the "computers are innocent"?</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391639):
<p>In all seriousness, I would say it's important not to lose sight of the fact that computers do nothing more than what you tell them to</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391646):
<p>so if you want magical tactics, you need magical people to support them</p>

#### [ Simon Hudon (Jun 01 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391662):
<p>Yeah, my point exactly</p>

#### [ Kevin Buzzard (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391818):
<p>or just sufficiently advanced technology</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391825):
<p>No</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391826):
<p>that's the point</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391868):
<p>the sufficiently advanced tech has to come from us</p>

#### [ Simon Hudon (Jun 01 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391890):
<p>The difference is that, from magic, you expect all your wildest dreams to be fulfilled while with effective technology, you expect a specific task to be handled. The technology is more useful because it's easier to know when it will work and when it won't</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127391891):
<p>it's one thing to expect miracles of "the CS community" in general, but that seems much less reasonable when you restrict scope to the &lt;=10 people who are actually involved in writing tactics that you will see</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127392976):
<p>That's why I have to learn. But I have so many other things I want to do :-/</p>

#### [ Kevin Buzzard (Jun 01 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127392977):
<p>It's wonderful being busy isn't it</p>

#### [ Simon Hudon (Jun 01 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127393040):
<p>It sounds like a sarcastic comment but I have found that since my schedule has been filling up, I've been able to get things done quicker</p>

#### [ Patrick Massot (Jun 01 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127403167):
<blockquote>
<p>Question: can we start <code>derive_field</code> by some testing whether the target type is a pi type of a sub-type?</p>
</blockquote>
<p>What about this question?</p>

#### [ Simon Hudon (Jun 01 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127412218):
<p>Yes that can be done. Are those the only two situations where you'd like to use <code>derive_field</code>?</p>

#### [ Simon Hudon (Jun 01 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127419299):
<p>I'm not sure what the best way to generalize <code>derive_field</code> is. I'm thinking of breaking it into <code>derive_method</code> and <code>derive_proof_of_law</code>. You could use them  as <code>refine_struct { .. } ; try { derive_field &lt;|&gt; derive_proof_of_law</code>. Then, we can add a tactic argument to <code>derive_proof_of_law</code> and use it as <code>derive_proof_of_law { intro }</code> or <code>derive_proof_of_law { refine subtype.eq _ }</code>. I don't know if that's simpler than having separate tactics for pi instances and for subtypes.</p>

#### [ Patrick Massot (Jun 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127424663):
<p>maybe two separate tactics make more sense actually (one for pi and one for subtypes)</p>

#### [ Simon Hudon (Jun 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127424840):
<p>The benefit over the previous automation is, even if you do need specialized code, the simplified code is much simpler than in the current version of <code>pi_instance</code></p>

#### [ Mario Carneiro (Jun 01 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refine_struct/near/127425124):
<p>I like this approach for exactly this reason. I wasn't a fan of <code>pi_instance</code> originally because it was a lot of code for a specialized problem; this puts most of the code in an obviously general setting and now <code>pi_instance</code> is both simpler and requires less input</p>


{% endraw %}
