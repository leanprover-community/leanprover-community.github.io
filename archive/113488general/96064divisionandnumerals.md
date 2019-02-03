---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96064divisionandnumerals.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [division and numerals](https://leanprover-community.github.io/archive/113488general/96064divisionandnumerals.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Dec 14 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151792143):
<div class="codehilite"><pre><span></span><span class="c1">-- example : 2 ∣ 4 := ⟨2, rfl⟩ -- fails</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">invalid constructor ⟨...⟩, &#39;has_dvd.dvd&#39; is not an inductive type</span>
<span class="cm">-/</span>
<span class="c1">--example : (2 : ℕ) ∣ 4 := ⟨2,rfl⟩ -- fails</span>
<span class="c1">--example : 2 ∣ (4 : ℕ) := ⟨2,rfl⟩ -- fails</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="err">∣</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">2</span><span class="o">,</span><span class="n">rfl</span><span class="bp">⟩</span> <span class="c1">-- works</span>
<span class="c1">--example (a : ℕ) : a ∣ a * 2 := ⟨2,rfl⟩ -- fails</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∣</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="mi">2</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">2</span><span class="o">,</span><span class="n">rfl</span><span class="bp">⟩</span> <span class="c1">-- works</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∣</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">2</span><span class="o">,</span><span class="n">rfl</span><span class="bp">⟩</span> <span class="c1">-- works</span>
</pre></div>


<p>Why do so many of these fail? In particular the fourth one: why does Lean need to be told that <code>a * 2</code> is a nat when it knows <code>a</code> is a nat? The type of <code>has_dvd.dvd</code> (the notation) is <code>α → α → Prop</code> and it is looking straight at two nats when it decides how to deal with what alpha is.</p>

#### [ Gabriel Ebner (Dec 14 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151793918):
<p>Now you know why <code>by exact</code> is so popular. <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Gabriel Ebner (Dec 14 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151794263):
<p>The reason is that while Lean does know at some point that <code>|</code> is the divisibility relation on a commutative semiring defined by <code>∃ x, ...</code>; Lean only figures this out too late, after <code>⟨2, rfl⟩</code> is elaborated.  It looks like a bug that could be fixed by synthesizing instances before elaborating anonymous constructors.</p>

#### [ Gabriel Ebner (Dec 14 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151794284):
<p>In this example, you can also force instances to be synthesized before elaborating the proof by using <code>lemma</code> instead of <code>example</code>.</p>

#### [ Gabriel Ebner (Dec 14 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151794384):
<p>(Oh, and <code>by exact foo</code> also changes the order in which things are elaborated.  Tactics are called last; this has the effect of elaborating <code>foo</code> later than the rest of the term, when typeclass instances, etc. will have hopefully been figured out.)</p>

#### [ Kevin Buzzard (Dec 14 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151798356):
<p>I now feel like I've asked this question several times. I think it's about time I understood the answer properly. My current understanding of the answer, which I guess I already had when I posted, is "it's all to do with when elaboration occurs". I hadn't realised this one was in the "lemma / example makes a difference" category and I know I've asked at least one of these before.</p>


{% endraw %}
