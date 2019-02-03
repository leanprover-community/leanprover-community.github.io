---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00534Howdidsimpprovemylemma.html
---

## Stream: [general](index.html)
### Topic: [How did simp prove my lemma?](00534Howdidsimpprovemylemma.html)

---


{% raw %}
#### [ Johan Commelin (Jul 31 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640952):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">simp_lemmas</span> <span class="n">true</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">i</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>


<p>I think the consensus is that this example should not be proven by <code>simp</code>. Can Lean tell me what the <em>morally correct</em> proof is?</p>

#### [ Kenny Lau (Jul 31 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640973):
<p><code>simp</code> does not prove it in the online version</p>

#### [ Johan Commelin (Jul 31 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640979):
<p>The trace option spits out a lot of noise, but I didn't find the lemma that prove this.</p>

#### [ Kenny Lau (Jul 31 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640991):
<p>neither does it in my local copy</p>

#### [ Kenny Lau (Jul 31 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130640993):
<p>but you can use <code>set_option trace.simplify.rewrite true</code></p>

#### [ Johan Commelin (Jul 31 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641048):
<p>My <code>simp</code> is stronger than yours!</p>
<div class="codehilite"><pre><span></span>0. [simplify.rewrite] [le_add_iff_nonneg_right]: i ≤ i + 1 ==&gt; 0 ≤ 1
</pre></div>

#### [ Kenny Lau (Jul 31 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641052):
<p>you imported stuff</p>

#### [ Patrick Massot (Jul 31 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641056):
<p>Cheater!</p>

#### [ Johan Commelin (Jul 31 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641165):
<p>O.o.... <span class="emoji emoji-1f629" title="distraught">:distraught:</span></p>

#### [ Johan Commelin (Jul 31 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641187):
<p>Apparently the category libs by Scott import stuff that give <code>simp</code> superpowers when dealing with integers.</p>

#### [ Johan Commelin (Jul 31 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641248):
<p>I didn't expect that that import would affect the proof.</p>

#### [ Patrick Massot (Jul 31 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641265):
<p>Don't forget that one import can hide thousands imports</p>

#### [ Johan Commelin (Jul 31 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641352):
<p>Yes, that is true. I think that means I should always import Scott's category libs.</p>

#### [ Scott Morrison (Jul 31 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641543):
<p>Eek, I have no idea how or why I could be responsible. :-)</p>

#### [ Johan Commelin (Jul 31 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641639):
<p>/me mumbles something about synergy...</p>

#### [ Chris Hughes (Jul 31 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641738):
<p>interesting<br>
<code>example : (0 : ℤ) ≤ 1 = true := rfl</code></p>

#### [ Kenny Lau (Jul 31 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641790):
<p>because <code>(0 : ℤ) ≤ 1</code> can be lifted to <code>bool</code>, because it is decidable</p>

#### [ Kenny Lau (Jul 31 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641797):
<p>but you already know this</p>

#### [ Gabriel Ebner (Jul 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641839):
<p>There is no bool in this example, the proposition is indeed definitionally equal to true.</p>

#### [ Chris Hughes (Jul 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641857):
<p><code>bool</code> isn't involved here. <code>true</code> is <code>true : Prop</code><br>
<code>example : (0 : ℕ) ≤ 1 = true := rfl --doesn't work</code></p>

#### [ Kenny Lau (Jul 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641891):
<p>oops, I misread</p>

#### [ Gabriel Ebner (Jul 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/How%20did%20simp%20prove%20my%20lemma%3F/near/130641897):
<p><a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/int/order.lean#L13-L17" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/int/order.lean#L13-L17">https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/int/order.lean#L13-L17</a></p>


{% endraw %}
