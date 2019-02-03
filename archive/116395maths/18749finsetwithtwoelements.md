---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/18749finsetwithtwoelements.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [finset with two elements](https://leanprover-community.github.io/archive/116395maths/18749finsetwithtwoelements.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 08 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131097823):
<p><span class="user-mention" data-user-id="120276">@Morenikeji Neri</span> has proved <code>det(AB)=det(A)det(B)</code> modulo some lemma about switching two rows of a matrix making the sign change, which became a lemma about summing over a set of size 2, which has now been reduced to this:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">open</span> <span class="n">finset</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hdiff</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">t</span><span class="o">)</span> <span class="o">:</span>
<span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">s</span> <span class="bp">∨</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">t</span><span class="o">)</span> <span class="n">univ</span> <span class="bp">=</span> <span class="n">insert</span> <span class="n">s</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="n">t</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>This says (if I got it right) that if <code>s</code> and <code>t</code> are two distinct terms, then filtering over the predicate which says "I am <code>s</code> or <code>t</code>" gives me precisely the finset containing <code>s </code>and <code>t</code> (I built it using insert and singleton because there are lemmas like <code>sum_insert</code> and `sum_singleton).</p>
<p>I used to rant a lot about "easy in maths, hard in lean" stuff when I found it very frustrating that there was stuff which was easy in maths but which <em>I</em> found hard in Lean. As I get better at Lean I realise that I'm ranting less and just solving my own problems. But this one looks scary, because a finset is quite a complicated object for me -- I'm not sure I can steer <code>nodup</code> and I'm still quite an amateur when it comes to quotients. </p>
<p>This is about the third post I've written about this problem; the first two I've written, thought "actually I can make progress", and then deleted. But this one still looks scary. Can anyone suggest a way to progress on this?</p>

#### [ Kenny Lau (Aug 08 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131097900):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">open</span> <span class="n">finset</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hdiff</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">t</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">s</span> <span class="bp">∨</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">t</span><span class="o">)</span> <span class="n">univ</span> <span class="bp">=</span> <span class="n">insert</span> <span class="n">s</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="n">t</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Kenny Lau (Aug 08 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131097931):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">open</span> <span class="n">finset</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hdiff</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">≠</span> <span class="n">t</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">s</span> <span class="bp">∨</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">t</span><span class="o">)</span> <span class="n">univ</span> <span class="bp">=</span> <span class="n">insert</span> <span class="n">s</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="n">t</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ext</span><span class="bp">;</span> <span class="n">simp</span>
</pre></div>

#### [ Kevin Buzzard (Aug 08 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098109):
<p>:o</p>

#### [ Kevin Buzzard (Aug 08 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098117):
<p>I didn't even think to try simp, because "this was obviously much too complicated for a stupid thing like simp"</p>

#### [ Kevin Buzzard (Aug 08 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098122):
<p>Thanks Kenny!</p>

#### [ Kevin Buzzard (Aug 08 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098128):
<p>My simp-fu is still very weak.</p>

#### [ Rob Lewis (Aug 08 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098132):
<p>I think you don't even need the <code>Hdiff</code> argument!</p>

#### [ Kevin Buzzard (Aug 08 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098177):
<p>You might be right -- I didn't check to see what insert did when it was already in.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098193):
<p>multiset insert adds another one, I guess that was what scared me off.</p>

#### [ Mario Carneiro (Aug 08 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131098908):
<p>I would say the moral of the story here is the power of finset extensionality. Finsets are complicatedly defined, but it is not hard to show equalities between finsets because you can just reason about the set that they define</p>

#### [ Kevin Buzzard (Aug 08 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131099150):
<p>Yes -- it wasn't the <code>simp</code> that was the insight, it was the <code>ext</code>. The proof (of det AB = det A det B) is apparently complete now. Of course it's not remotely mathlib-ready...</p>

#### [ Kevin Buzzard (Aug 08 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20with%20two%20elements/near/131099565):
<p>By the way, the proof featured:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sum_equiv_classes</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_rel</span> <span class="n">h</span><span class="bp">.</span><span class="n">r</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">@</span><span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="n">β</span> <span class="bp">_</span><span class="o">)</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">h</span><span class="o">),</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="err">⟦</span><span class="n">b</span><span class="err">⟧</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="o">)</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>


<p>which I thought at the time was a good idea, but actually was a pain to apply because I didn't have an equivalence relation on a fintype, I had an equivalence relation on a finset, so there was a certain amount of inelegant scuffling around with <code>↥↑s</code> at some point. Wouldn't surprise me if I was missing a trick.</p>


{% endraw %}
