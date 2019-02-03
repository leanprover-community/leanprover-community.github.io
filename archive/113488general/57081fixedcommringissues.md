---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57081fixedcommringissues.html
---

## Stream: [general](index.html)
### Topic: [(fixed) comm_ring issues](57081fixedcommringissues.html)

---


{% raw %}
#### [ Johan Commelin (Jul 18 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856041):
<p>I've got the following context/goal:</p>
<div class="codehilite"><pre><span></span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">,</span>
<span class="n">S</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_subring</span> <span class="n">R</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">S</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">comm_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">R</span><span class="o">,</span>
<span class="n">a_property</span> <span class="o">:</span> <span class="bp">@</span><span class="n">has_mem</span><span class="bp">.</span><span class="n">mem</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span> <span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">set</span><span class="bp">.</span><span class="n">has_mem</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">)</span> <span class="n">a</span> <span class="n">S</span><span class="o">,</span>
<span class="n">b</span> <span class="o">:</span> <span class="n">R</span><span class="o">,</span>
<span class="n">b_property</span> <span class="o">:</span> <span class="bp">@</span><span class="n">has_mem</span><span class="bp">.</span><span class="n">mem</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span> <span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">set</span><span class="bp">.</span><span class="n">has_mem</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">)</span> <span class="n">b</span> <span class="n">S</span>
<span class="err">⊢</span> <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">R</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_mul</span><span class="bp">.</span><span class="n">mul</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">mul_zero_class</span><span class="bp">.</span><span class="n">to_has_mul</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="o">(</span><span class="bp">@</span><span class="n">semiring</span><span class="bp">.</span><span class="n">to_mul_zero_class</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="o">(</span><span class="bp">@</span><span class="n">ring</span><span class="bp">.</span><span class="n">to_semiring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)))</span>
       <span class="n">a</span>
       <span class="n">b</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">has_mul</span><span class="bp">.</span><span class="n">mul</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">mul_zero_class</span><span class="bp">.</span><span class="n">to_has_mul</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="o">(</span><span class="bp">@</span><span class="n">semiring</span><span class="bp">.</span><span class="n">to_mul_zero_class</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="o">(</span><span class="bp">@</span><span class="n">ring</span><span class="bp">.</span><span class="n">to_semiring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)))</span>
       <span class="n">b</span>
       <span class="n">a</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Jul 18 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856049):
<p>For the record, here is my silly attempt to prove that subrings of comm rings are comm_ring:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">subset</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">S</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul_comm</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">mul_comm</span><span class="o">,</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">subset</span><span class="bp">.</span><span class="n">ring</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Jul 18 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856089):
<p>Somehow Lean turns R into a <code>semiring</code>, instead of a <code>comm_semigroup</code>... And therefore I can't apply <code>mul_comm</code>.</p>

#### [ Johan Commelin (Jul 18 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856104):
<p>For even more record:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">subset</span><span class="bp">.</span><span class="n">ring</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">S</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add_comm</span>      <span class="o">:=</span> <span class="k">assume</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">add_comm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">left_distrib</span>  <span class="o">:=</span> <span class="k">assume</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">left_distrib</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">right_distrib</span> <span class="o">:=</span> <span class="k">assume</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">right_distrib</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">add_group</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">monoid</span> <span class="o">}</span>
</pre></div>


<p>That was nice and easy... (and maybe with Scott's tactics it will become even easier!) but if I substitute <code>mul</code> for <code>add</code> it borks out.</p>

#### [ Johan Commelin (Jul 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856212):
<p>Fixed. Lean starts crying if I tell it that R is a ring and a comm_ring.</p>

#### [ Johan Commelin (Jul 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856214):
<p>And I understand why.</p>

#### [ Johan Commelin (Jul 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856255):
<p>It just means that I cannot use the <code>variables {R : Type} [ring R]</code> from the top of my file.</p>

#### [ Mario Carneiro (Jul 18 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856779):
<p>If you put <code>{R} [comm_ring R]</code> in the statement instead of just <code>[comm_ring R]</code> it will override the <code>R</code> in the enclosing section</p>

#### [ Johan Commelin (Jul 18 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856844):
<p>OTOH, then I still can't use the <code>variables {S : set R} [is_subring S]</code> from the top of my file.</p>

#### [ Johan Commelin (Jul 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129856857):
<p>What I would need is to somehow tell lean: "Hey, in addition to all the other hypotheses, please extend the ring instance into a comm_ring instance."</p>

#### [ Patrick Massot (Jul 18 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129857156):
<p>I don't understand what you are doing. Haven't you already done that in <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/subring.lean" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/subring.lean">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/subring.lean</a>?</p>

#### [ Johan Commelin (Jul 18 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129857310):
<p>Not the bit on commutative rings.</p>

#### [ Johan Commelin (Jul 18 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28fixed%29%20comm_ring%20issues/near/129857317):
<p>Only plain old rings</p>


{% endraw %}
