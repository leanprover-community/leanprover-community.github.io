---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54574coecoe.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [coe_coe](https://leanprover-community.github.io/archive/113488general/54574coecoe.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (May 01 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125958400):
<p>Just noticed the lemma <code>coe_coe</code>, which is tagged as <code>simp</code>, does this mean I need to be careful about tagging lemmas that make a double coercion into a single coercion with simp?</p>

#### [ Kenny Lau (May 01 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125960662):
<blockquote>
<p>Just noticed the lemma <code>coe_coe</code>, which is tagged as <code>simp</code>, does this mean I need to be careful about tagging lemmas that make a double coercion into a single coercion with simp?</p>
</blockquote>
<p>yes</p>

#### [ Chris Hughes (May 01 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125960853):
<p>What's the difference between <code>has_coe</code> and <code>has_coe_t</code>?</p>

#### [ Kenny Lau (May 01 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125960953):
<p>L37:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">has_coe</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">coe</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">b</span><span class="o">)</span>

<span class="c">/-</span><span class="cm">- Auxiliary class that contains the transitive closure of has_coe. -/</span>
<span class="n">class</span> <span class="n">has_coe_t</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">coe</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">b</span><span class="o">)</span>
</pre></div>


<hr>
<p>L94:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">coe_trans</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u₂</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u₃</span><span class="o">}</span> <span class="o">[</span><span class="n">has_coe</span> <span class="n">a</span> <span class="n">b</span><span class="o">]</span> <span class="o">[</span><span class="n">has_coe_t</span> <span class="n">b</span> <span class="n">c</span><span class="o">]</span> <span class="o">:</span> <span class="n">has_coe_t</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">coe_t</span> <span class="o">(</span><span class="n">coe_b</span> <span class="n">x</span> <span class="o">:</span> <span class="n">b</span><span class="o">)</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961550):
<p>Maybe the type class coercion system uses this instance?</p>

#### [ Kenny Lau (May 01 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961600):
<p>curiously, this <code>has_coe_t</code> appears literally nowhere</p>

#### [ Kevin Buzzard (May 01 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961607):
<p>Did you check the C++ bit?</p>

#### [ Kenny Lau (May 01 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961611):
<p>maybe it's because of this:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">coe_to_lift</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">has_coe_t</span> <span class="n">a</span> <span class="n">b</span><span class="o">]</span> <span class="o">:</span> <span class="n">has_lift_t</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">coe_t</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (May 01 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961620):
<p>so my conjecture is that they use <code>has_coe_t</code> to do transitive stuff, and then make <code>has_lift_t</code> the interface</p>

#### [ Kevin Buzzard (May 01 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961671):
<p>I remember Mario once saying something like he couldn't see the point of has_lift</p>

#### [ Kevin Buzzard (May 01 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961673):
<p>There's something about it in TPIL IIRC</p>

#### [ Chris Hughes (May 01 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125961919):
<p>So I don't need to worry unless it's a <code>coe_t</code>. The reason I noticed is because the coercion from pnat to int is a coe_t obviously, so it was being rewritten by coe_coe.</p>

#### [ Chris Hughes (May 01 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125962001):
<p>Which means I need double the lemmas</p>

#### [ Kevin Buzzard (May 01 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125962030):
<p>Has_lift gives you access to the \u uparrow notation but lean won't ever insert them for you if you're not has_coe</p>

#### [ Kevin Buzzard (May 01 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125962081):
<p>But each lemma is twice as easy to prove <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Mario Carneiro (May 02 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984523):
<p>You shouldn't need "double the lemmas", you just need to make sure that any simp lemmas LHS are already split up into multiple coe arrows</p>

#### [ Chris Hughes (May 02 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984671):
<p>But I also want the single arrows for rw's, because if I don't use simp, most of my coercions are single coercions</p>

#### [ Mario Carneiro (May 02 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984685):
<p>why are you using composite coercions to begin with?</p>

#### [ Mario Carneiro (May 02 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984693):
<p>I honestly wish the parser inserted multiple coe arrows, but the best I can do to recreate that is <code>coe_coe</code></p>

#### [ Mario Carneiro (May 02 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125984738):
<p>but you can always write <code>((a:B):C)</code> to get multiple coe arrows inserted</p>

#### [ Kevin Buzzard (May 02 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987058):
<p>He wants to go from <code>pnat</code> to <code>int</code></p>

#### [ Mario Carneiro (May 02 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987205):
<p>I can see that. But why? What is the simp lemma under consideration? Like I said, you can use <code>((n:nat):int)</code> to double-coerce</p>

#### [ Chris Hughes (May 02 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987207):
<p>But that means having to type ((n : nat):int) all the time, instead of just n.</p>

#### [ Mario Carneiro (May 02 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987218):
<p>all the time meaning only on the LHS of rules marked <code>[simp]</code></p>

#### [ Mario Carneiro (May 02 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987222):
<p>in proofs you can do whatever</p>

#### [ Mario Carneiro (May 02 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987263):
<p>but it is important to state your lemmas correctly</p>

#### [ Chris Hughes (May 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987270):
<p>But for any lemma marked simp, I also want it's single coercion corollary if I want to rewrite something.</p>

#### [ Mario Carneiro (May 02 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987271):
<p>like what?</p>

#### [ Mario Carneiro (May 02 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987314):
<p>just <code>rw coe_coe</code></p>

#### [ Chris Hughes (May 02 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987315):
<p>I could do that too.</p>

#### [ Mario Carneiro (May 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987320):
<p>I think you underestimate the number of "single coercion corollaries"</p>

#### [ Mario Carneiro (May 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987321):
<p>(hint: it's infinite)</p>

#### [ Kenny Lau (May 02 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987359):
<p>infinity doesn't exist</p>

#### [ Mario Carneiro (May 02 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coe_coe/near/125987364):
<p>and neither do those corollaries, in mathlib</p>


{% endraw %}
