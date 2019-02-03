---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58005Cardinality.html
---

## Stream: [general](index.html)
### Topic: [Cardinality](58005Cardinality.html)

---


{% raw %}
#### [ Huyen Chau Nguyen (Jun 22 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128461092):
<p>Hey guys, I want to ask about the cardinality of sets. I'm totally newbie to Lean so the questions might be trivial and silly. Still, I need your help.</p>
<p>I would like to ask what is the function in mathlib that returns the number of elements of a set (of type set \N and not finset, but this set surely has a finite number of elements, it's not infinite set like R or N) and also which file i should have to import.</p>
<p>Thank you for your responses.</p>
<p>P.S.: I'm from Vn so please excuse-me for my English too.</p>

#### [ Sean Leather (Jun 22 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128461286):
<p>I haven't used <code>set</code> myself, but I think an answer can be found in <code>data/set/finite.lean</code> in mathlib:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">finite</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">fintype</span> <span class="n">s</span><span class="o">)</span>
</pre></div>


<p>Then, looking at <code>data/fintype.lean</code>, we see:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">elems</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">complete</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">elems</span><span class="o">)</span>
</pre></div>

#### [ Huyen Chau Nguyen (Jun 22 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128461714):
<p>My prob is that i have to define my set as a set and not finset and then i need to count its size. <br>
Thank you very much for your answer.  I dont totally understand it yet but i would explore your hint with those files first and might ask you guys more later ^^.</p>

#### [ Sean Leather (Jun 22 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128461975):
<p>You might want to think how you would define cardinality yourself. Consider the definition of <code>set</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">set</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
</pre></div>


<p>Without additional information, how do you count the number of elements? How do you even know a given <code>s : set α</code> is finite? For example, is <code>s : set ℕ</code> (whose type reduces to <code>ℕ → Prop</code>)  finite?</p>

#### [ Chris Hughes (Jun 22 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128462742):
<p><code>fintype.card</code> is the function you want.</p>

#### [ Huyen Chau Nguyen (Jun 22 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128463888):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span>  : my set is constructed from an argument n of integer, if n tends to inifinity then the set's number of element could tend to be infinite, but for any given n, the number of elements of that set is guaranteed to be bounded ( Im wondering if i misunderstood the notion of being finite :-? ).  </p>
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> okie thank you I'll check that out too .</p>

#### [ Johannes Hölzl (Jun 22 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128476931):
<p>If you know your set is bound by a natural number <code>n</code> you can write <code>((finset.range n).filter (λi, i &lt; 3)).card</code>, i.e. you first generate the finite set of all natural numbers up to <code>n</code> and then filter on a predicate (in this case<code>i &lt; 3</code>). Then using <code>card</code> we compute the cardinality.</p>

#### [ Johannes Hölzl (Jun 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cardinality/near/128476976):
<p>If you have a proof that a <code>s : set α</code> is finite (i.e. <code>finite s</code>), then you can use <code>set.finite.to_finset</code> to get the <code>finset</code> of a <code>set</code>.</p>


{% endraw %}
