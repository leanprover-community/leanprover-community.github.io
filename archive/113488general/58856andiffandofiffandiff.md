---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58856andiffandofiffandiff.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [and_iff_and_of_iff_and_iff](https://leanprover-community.github.io/archive/113488general/58856andiffandofiffandiff.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135087802):
<p>Would this be a useful lemma for mathlib? If so, where should it go? I currently solve this by <code>split; intros; split,</code> but that is a bit of a hack, and creates 4 goals where usually 2 should suffice.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">and_iff_and_of_iff_and_iff</span> <span class="o">{</span><span class="n">P1</span> <span class="n">P2</span> <span class="n">Q1</span> <span class="n">Q2</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="n">P1</span> <span class="err">\</span><span class="n">iff</span> <span class="n">Q1</span><span class="o">)</span> <span class="err">\</span><span class="n">and</span> <span class="o">(</span><span class="n">P2</span> <span class="err">\</span><span class="n">iff</span> <span class="n">Q2</span><span class="o">))</span> <span class="o">:</span>
<span class="o">(</span><span class="n">P1</span> <span class="err">\</span><span class="n">and</span> <span class="n">P2</span><span class="o">)</span> <span class="err">\</span><span class="n">iff</span> <span class="o">(</span><span class="n">Q1</span> <span class="err">\</span><span class="n">and</span> <span class="n">Q2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Oct 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135087872):
<p>This looks like <code>and_congr</code></p>

#### [ Johan Commelin (Oct 03 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135087981):
<p>Cool, I'll use that! Is there a way that I could have discovered that name myself?</p>

#### [ Sean Leather (Oct 03 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088008):
<p>I also had trouble finding that. Like me, Johan may have been look for something <code>iff</code>-named instead of <code>and</code>- and <code>congr</code>-named.</p>

#### [ Sean Leather (Oct 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088104):
<p>I probably tried <code>git grep 'and.*iff'</code> and <code>git grep 'iff.*and'</code>.</p>

#### [ Mario Carneiro (Oct 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088105):
<p>That's true. This is a special pattern, like <code>ext</code>. <code>congr</code> lemmas mean if the inputs are equal then a function applied to those inputs is equal</p>

#### [ Mario Carneiro (Oct 03 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088176):
<p>There are similar theorems for all the propositional functions, and for regular functions <code>congr</code> the tactic will often generate these on the fly</p>

#### [ Mario Carneiro (Oct 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088308):
<p>You will also find custom <code>congr</code> lemmas for things like <code>list.map_congr</code>, where we want to insert an additional assumption into the hypothesis (if <code>\all x \in l, f x = g x</code> then <code>map f l = map g l</code>)</p>

#### [ Mario Carneiro (Oct 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088324):
<p>so many higher order functions have some kind of altered <code>congr</code> lemma</p>


{% endraw %}
