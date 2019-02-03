---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01949minimumoffiniteset.html
---

## Stream: [general](index.html)
### Topic: [minimum of finite set](01949minimumoffiniteset.html)

---


{% raw %}
#### [ Reid Barton (May 06 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126161321):
<p>I have a <code>finset</code> of rationals which I know is nonempty. How do I find its minimum element?</p>

#### [ Mario Carneiro (May 06 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126163639):
<p>I forget if there is a <code>max</code> operation on finsets, but you can <code>fold</code> with <code>max</code></p>

#### [ Sean Leather (May 06 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126170875):
<blockquote>
<p>I have a <code>finset</code> of rationals which I know is nonempty. How do I find its minimum element?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> See <a href="https://github.com/spl/tts/blob/master/src/data/finset/fresh.lean#L121-L154" target="_blank" title="https://github.com/spl/tts/blob/master/src/data/finset/fresh.lean#L121-L154">https://github.com/spl/tts/blob/master/src/data/finset/fresh.lean#L121-L154</a></p>
<p>I'd like to see something like this with <code>max</code> and <code>min</code> in mathlib. I haven't proposed it because I wasn't sure it was worth it, but, since you are also looking for it, perhaps it is.</p>

#### [ Sean Leather (May 07 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212361):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Is this something (after replacing <code>max</code> with <code>min</code>) that would be useful to you? I can work on it next.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>

<span class="kn">namespace</span> <span class="n">finset</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span>

<span class="n">def</span> <span class="n">max</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
  <span class="n">fold</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">max</span> <span class="n">a</span> <span class="n">id</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">max_empty</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">max</span> <span class="n">a</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">max</span><span class="o">]</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">max_insert</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∉</span> <span class="n">s</span><span class="o">)</span>
<span class="o">:</span> <span class="n">max</span> <span class="n">b</span> <span class="o">(</span><span class="n">insert</span> <span class="n">a</span> <span class="n">s</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">max</span> <span class="n">a</span> <span class="o">(</span><span class="n">max</span> <span class="n">b</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">max</span><span class="o">,</span> <span class="n">fold_insert</span> <span class="n">h</span><span class="o">]</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">max_singleton</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">max</span> <span class="n">b</span> <span class="o">{</span><span class="n">a</span><span class="o">}</span> <span class="bp">=</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">max</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">max</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">le_max_left</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">max</span> <span class="n">a</span> <span class="n">s</span> <span class="o">:=</span>
  <span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span>
    <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">max_empty</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">s</span> <span class="o">(</span><span class="n">hnm</span> <span class="o">:</span> <span class="n">b</span> <span class="err">∉</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">ih</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">max</span> <span class="n">a</span> <span class="n">s</span><span class="o">),</span>
     <span class="k">by</span> <span class="n">rw</span> <span class="n">max_insert</span> <span class="n">hnm</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">le_trans</span> <span class="n">ih</span> <span class="o">(</span><span class="n">le_max_right</span> <span class="n">b</span> <span class="o">(</span><span class="n">max</span> <span class="n">a</span> <span class="n">s</span><span class="o">)))</span>

<span class="kn">theorem</span> <span class="n">le_max_of_mem</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">max</span> <span class="n">b</span> <span class="n">s</span> <span class="o">:=</span>
  <span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">max_empty</span><span class="o">,</span> <span class="n">h</span><span class="o">])</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">c</span> <span class="n">s</span> <span class="o">(</span><span class="n">hnm</span> <span class="o">:</span> <span class="n">c</span> <span class="err">∉</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">ih</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">max</span> <span class="n">b</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">hins</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">insert</span> <span class="n">c</span> <span class="n">s</span><span class="o">),</span>
     <span class="k">begin</span>
       <span class="n">rw</span> <span class="n">max_insert</span> <span class="n">hnm</span><span class="o">,</span>
       <span class="n">cases</span> <span class="n">mem_insert</span><span class="bp">.</span><span class="n">mp</span> <span class="n">hins</span><span class="o">,</span>
       <span class="n">case</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="o">:</span> <span class="n">p</span> <span class="o">{</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">p</span><span class="o">,</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">le_max_left</span><span class="o">]</span> <span class="o">},</span>
       <span class="n">case</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="o">:</span> <span class="n">p</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">le_trans</span> <span class="o">(</span><span class="n">ih</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">le_max_right</span> <span class="n">c</span> <span class="o">(</span><span class="n">max</span> <span class="n">b</span> <span class="n">s</span><span class="o">))</span> <span class="o">}</span>
     <span class="kn">end</span><span class="o">)</span>

<span class="kn">end</span> <span class="n">finset</span>
</pre></div>

#### [ Patrick Massot (May 07 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212689):
<p>What's this <code>{a}</code> syntax in <code>max b {a}</code>?</p>

#### [ Sean Leather (May 07 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212753):
<p>It's notation for a singleton.</p>

#### [ Sean Leather (May 07 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212815):
<p>Actually, to correct myself, <code>{a}</code> is a singleton, but the notation comes from <code>init/core.lean</code>, I think:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> Type class used to implement the notation { a ∈ c | p a } -/</span>
<span class="n">class</span> <span class="n">has_sep</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">sep</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">→</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (May 07 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212817):
<p>Oh</p>

#### [ Patrick Massot (May 07 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212857):
<p>I was confused, I thought it was an implicit parameter right of colon</p>

#### [ Patrick Massot (May 07 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212858):
<p>The theorem even has "singleton" in its name...</p>

#### [ Sean Leather (May 07 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212913):
<p>Hmm, maybe it's not from <code>has_sep</code>. I thought I knew, but I don't know anymore.</p>

#### [ Sean Leather (May 07 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212976):
<p>Ah, right, it's this one:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> Type classes has_emptyc and has_insert are</span>
<span class="cm">   used to implement polymorphic notation for collections.</span>
<span class="cm">   Example: {a, b, c}. -/</span>
<span class="n">class</span> <span class="n">has_emptyc</span>   <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">emptyc</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
<span class="n">class</span> <span class="n">has_insert</span>   <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">insert</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (May 07 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126212990):
<p>So, if your type has <code>has_emptyc</code> and <code>has_insert</code> instances, you can use the <code>{..., ...}</code> notation.</p>

#### [ Sean Leather (May 07 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126213048):
<p>I agree that it can be confusing.</p>

#### [ Patrick Massot (May 07 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126213133):
<p>It's my fault, I wasn't paying enough attention. I shouldn't be watching Zulip while grading Sage notebooks (<span class="user-mention" data-user-id="116034">@William Stein</span> when will we get auto-grading Sage notebooks so that we can focus on understanding Lean code?).</p>

#### [ Sean Leather (May 07 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126213255):
<p>I don't think it's a great idea to overload <code>{...}</code> in this way, even if it isn't ambiguous to the parser. But it is notationally short, which makes it convenient.</p>

#### [ Patrick Massot (May 07 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126213294):
<p>And it's the maths notations, so it should win over any other interpretation</p>

#### [ Sean Leather (May 07 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126213343):
<p>True, but it doesn't see as much usage as implicit parameters, and it would be better to reserve short notation for things you type/read a lot.</p>

#### [ Sean Leather (May 07 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126213355):
<p>You pretty much only use this notation for singletons or examples.</p>

#### [ Sean Leather (May 07 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126214292):
<p>PR for <code>finset.max</code> and <code>finset.min</code>: <a href="https://github.com/leanprover/mathlib/pull/133" target="_blank" title="https://github.com/leanprover/mathlib/pull/133">https://github.com/leanprover/mathlib/pull/133</a></p>

#### [ Patrick Massot (May 07 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126215835):
<p>Nice. I will probably use it to build new normed spaces out of finitely many old ones.</p>

#### [ Reid Barton (May 07 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126223645):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> I think this approach with a starting element (<code>a</code>) would be fine for my current application, since I have a particular element which I know belongs to the set. From a general math perspective, though, it's odd not to be able to talk about the minimum of a nonempty set, without first choosing an element of the set.</p>

#### [ Reid Barton (May 07 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126223715):
<p>I've been considering an approach that starts from <code>fold1</code>of an associative, commutative operation on a nonempty multiset, though this <code>fold1</code> was quite a challenge to define.</p>

#### [ Reid Barton (May 07 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126223856):
<p>But <code>fold1</code> seems like something one ought to have anyways.</p>

#### [ Reid Barton (May 07 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126223869):
<p>A friend suggested that I could just sort the list (<code>finset.sort</code>) and take the first element</p>

#### [ Sean Leather (May 08 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251600):
<p>My thinking is that you can write different variations using <code>max [decidable_linear_order α] : α → finset α → α</code>. I believe this definition of <code>max</code> is the most general and least prescriptive since only <code>[decidable_linear_order α]</code> is required.</p>

#### [ Sean Leather (May 08 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251644):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <a href="https://github.com/leanprover/mathlib/pull/133#issuecomment-387110828" target="_blank" title="https://github.com/leanprover/mathlib/pull/133#issuecomment-387110828">suggested</a> <code>max [decidable_linear_order α] [inhabited α] : finset α → α</code>, but I'm not sure if that's better (<a href="https://github.com/leanprover/mathlib/pull/133#issuecomment-387300724" target="_blank" title="https://github.com/leanprover/mathlib/pull/133#issuecomment-387300724">my response</a>).</p>

#### [ Mario Carneiro (May 08 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251859):
<p>It is not true that <code>max</code> as suggested by Johannes is the same as <code>max_inhabited</code> that you wrote. If <code>s</code> is nonempty, then <code>max (default A) s</code> is the max of <code>default A</code> and the elements of <code>s</code>, while Johannes's <code>max</code> is the max of the elements of <code>s</code> only. It is closer to Reid's suggested max operation, except that the nonempty constraint is replaced by a default value.</p>

#### [ Sean Leather (May 08 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251868):
<p>Right. See the bottom of my response.</p>

#### [ Mario Carneiro (May 08 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251909):
<p>Given johannes's <code>max</code> function, you could recover your <code>max</code> function as <code>sean_max a s := @johannes_max A _ &lt;a&gt; (insert a s)</code></p>

#### [ Sean Leather (May 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251917):
<p>So they are equivalent?</p>

#### [ Mario Carneiro (May 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251924):
<p>Johannes's definition is more complicated since it requires casing on whether the list is empty</p>

#### [ Sean Leather (May 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251929):
<p>What is the definition?</p>

#### [ Mario Carneiro (May 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251966):
<p>there is not an easy expression for <code>johannes_max</code> using <code>sean_max</code>, you would need another quot.lift</p>

#### [ Mario Carneiro (May 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251969):
<p>You have to start from list, define <code>foldl1</code> and work your way up</p>

#### [ Sean Leather (May 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251977):
<p>Ah, something like that.</p>

#### [ Mario Carneiro (May 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251983):
<p>Alternatively, you could <code>sean_max</code> over <code>option A</code></p>

#### [ Mario Carneiro (May 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126251987):
<p>where <code>none</code> has the appropriate interpretation as a neutral element for max</p>

#### [ Sean Leather (May 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252030):
<p>You mean map/image <code>some</code> over the <code>finset</code>?</p>

#### [ Mario Carneiro (May 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252034):
<p>and that would give you both the partial <code>max</code> function and the inhabited max function (Johannes's max)</p>

#### [ Mario Carneiro (May 08 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252047):
<p>Any semigroup operation extends to a monoid if you add a neutral element</p>

#### [ Mario Carneiro (May 08 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252058):
<p>That means that you can take a semigroup operation like <code>max</code> and extend it to <code>option_max : option A -&gt; option A -&gt; option A</code> that is a monoid operation</p>

#### [ Mario Carneiro (May 08 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252096):
<p>and then you can <code>finset.prod</code> over this</p>

#### [ Mario Carneiro (May 08 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252112):
<p>This is essentially the same as adjoining a <code>-inf</code> element to the set</p>

#### [ Sean Leather (May 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252114):
<p>Can you not <code>finset.image some</code>?</p>

#### [ Mario Carneiro (May 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252120):
<p>That would be the input to the fold, yes</p>

#### [ Sean Leather (May 08 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252124):
<p>Right, okay.</p>

#### [ Mario Carneiro (May 08 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252178):
<p>The nice thing about this approach is that it naturally handles partiality, you don't need the <code>inhabited</code> thing; but it's easy to implement the inhabited version using <code>option.iget</code></p>

#### [ Sean Leather (May 08 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252244):
<p>Personally, I'm not a big fan of <code>inhabited</code>. I haven't found a need for it in anything I've done, and I feel like, if you need an <code>inhabited</code> type, why not use <code>option</code> in the first place?</p>

#### [ Sean Leather (May 08 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252258):
<p>But I'm happy to see <em>some</em> version of <code>finset.max</code> and <code>finset.min</code> go into mathlib, so I don't feel that strongly about which one... as long as it works with <code>nat</code>. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Mario Carneiro (May 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252472):
<p>I have a similar antipathy to <code>inhabited</code>, it's a somewhat lazy way to totalize functions like division on nonempty domains.</p>

#### [ Mario Carneiro (May 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252480):
<p>Arguments in favor would say that composing them is a lot cleaner than the monad stuff</p>

#### [ Mario Carneiro (May 08 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252500):
<p>i.e. <code>(x + 2) / (y + 2 / z)</code> is easier to read than <code>do a &lt;- 2 / z, (x + 2) / (y + a)</code> or some such</p>

#### [ Mario Carneiro (May 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126252566):
<p>The best situation is if you are literally working in a sup_bot semilattice, in which case you don't have to cheat and get a proper function</p>

#### [ Johannes Hölzl (May 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126253973):
<p>Working on <code>sup_bot_semilattice</code> is indeed very nice, e.g.  <a href="https://github.com/johoelzl/mason-stother/blob/master/Sup_fin.lean" target="_blank" title="https://github.com/johoelzl/mason-stother/blob/master/Sup_fin.lean">https://github.com/johoelzl/mason-stother/blob/master/Sup_fin.lean</a> But we don't have a lot of ordered types having this structure, I guess <code>nat</code>, <code>fin</code>, and <code>ennreal</code>.</p>

#### [ Johannes Hölzl (May 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126254143):
<p>I prefer the <code>inhabited</code> version over <code>option</code>. With <code>inhabited</code> you get not only a nicer syntax, but a lot of cases etc can be easily done in the proofs, while for <code>option</code> we are often forced to do it on the term itself.</p>

#### [ Sean Leather (May 08 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126265296):
<p>Just thinking about it a little more... It seems like there are two goals here: one for a <code>max</code> with no requirements other than <code>decidable_linear_order</code> (me) and one for a <code>max</code> that does not need the extra <code>a : α</code> (Johannes and Reid). In the latter case, which is more useful: an <code>inhabited α</code> predicate or a non-empty predicate (e.g. <code>s ≠ ∅</code> or <code>∃ a : α, a ∈ s</code>)? I'm guessing the non-empty predicate is more useful because <code>inhabited α</code> doesn't tell you anything about the <code>finset</code> itself, and if you use the <code>inhabited α</code> version and want to know that you are not getting the <code>inhabited.default</code>, you need to know if the <code>finset</code> is empty anyway.</p>

#### [ Johannes Hölzl (May 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126265564):
<p>It is the other way round, the <code>inhabited α</code> is more useful from a user perspective. We don't need to give <code>max</code> more information than necessary. For <code>max</code> it is enough to show that <code>α</code> is inhabited, it is <strong>not</strong> necessary to show that <code>s</code> is inhabited (from which at least <code>nonempty α</code> follows). It is very annoying when the user always needs to provide a prove that <code>s</code> is not empty, this is exactly what I want to avoid.<br>
After all, we are in a theorem prover! Carrying around this information explicitly is not necessary, as usually we can show it in a proof.</p>

#### [ Reid Barton (May 08 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126273572):
<p>My only worry about <code>inhabited</code> is that as, on the one hand, it is not a <code>Prop</code>, and on the other hand, we may not always have a canonical <code>inhabited</code> instance at hand and need to construct one from the knowledge that <code>s</code> is nonempty, we might end up in a situation where Lean thinks <code>max s</code> depends on the choice of <code>inhabited</code> instance, even though we know it doesn't really.</p>

#### [ Reid Barton (May 08 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126273648):
<p>On the other hand, taking a <code>nonempty α</code> instance would make <code>max</code> noncomputable, which is maybe sort of okay for a theorem prover but not very attractive for programming use.</p>

#### [ Reid Barton (May 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126273684):
<p>(As it turns out, the theorem I really need has the conclusion <code>∃x ∈ s, ∀y ∈ s, f y ≤ f x</code>, and for this, we need <code>s</code> to be nonempty anyways.)</p>

#### [ Reid Barton (May 08 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126273773):
<p>The advantage of <code>s ≠ ∅</code> here is that it is a <code>Prop</code>, but also sufficient to define <code>max</code> computably</p>

#### [ Reid Barton (May 08 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126274645):
<p>I'm kind of tempted to make <code>s ≠ ∅</code> into a type class argument, actually, but maybe that is going too far?</p>

#### [ Johannes Hölzl (May 08 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126274905):
<p>Of course a theorem like <code>s ≠ ∅ -&gt; ∃x ∈ s, ∀y ∈ s, f y ≤ f x</code> is a nice fit for <code>max</code> with such an assumption. I'm worried about complicated constructions, where you have an elaborate proof that <code>s</code> is not empty. Putting <code>s ≠ ∅</code> in a type class argument makes also some constructions very unpleasent, like using <code>finset.filter</code></p>

#### [ Reid Barton (May 09 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126322044):
<p>Maybe the version returning <code>option</code> is most flexible then. If you want the version that uses <code>inhabited</code>, you can apply <code>option.iget</code>.</p>

#### [ Sean Leather (May 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126330803):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Are you referring to <code>max [decidable_linear_order α] : finset α → option α</code>. that returns <code>none</code> for an empty <code>finset</code> and <code>some a</code> for a non-empty <code>finset</code>? That would be fine with me.</p>

#### [ Reid Barton (May 09 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126332611):
<p>Yes. Or more generally, <code>fold1 f : finset α → option α</code> for an associative and commutative operation <code>f</code>.</p>

#### [ Sean Leather (May 22 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126920643):
<p>For those not following along on GitHub, <a href="https://github.com/leanprover/mathlib/pull/133" target="_blank" title="https://github.com/leanprover/mathlib/pull/133">leanprove/mathlib#133</a> has been updated with new versions of the definitions under discussion:</p>
<div class="codehilite"><pre><span></span><span class="n">finset</span><span class="bp">.</span><span class="n">max</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">min</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span>
</pre></div>


<p>I think this proposal is better than the original. Thanks to everyone for the discussion and collaboration. Feedback welcome.</p>

#### [ Patrick Massot (May 23 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126981683):
<p>So, how do we use this new toy? Say I want to talk about the function "max of coordinates on ℝ^n", assuming n is a British natural number, so I get a well defined function from ℝ^n to ℝ</p>

#### [ Patrick Massot (May 23 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126982922):
<p>I can't even find the lemma saying the image of <code>finset</code> is a <code>finset</code></p>

#### [ Johannes Hölzl (May 23 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/minimum%20of%20finite%20set/near/126984645):
<p>Its already in the type of <code>finset.image</code>.<br>
To do what you want: <code>λx, (univ.image (λn, x n)).max.iget</code></p>


{% endraw %}
