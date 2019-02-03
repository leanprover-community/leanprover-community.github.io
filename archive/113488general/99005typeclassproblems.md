---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99005typeclassproblems.html
---

## Stream: [general](index.html)
### Topic: [typeclass problems](99005typeclassproblems.html)

---


{% raw %}
#### [ Kenny Lau (Jun 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128143681):
<p>This loop is breaking everything</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">25</span><span class="o">)</span> <span class="err">?</span><span class="n">x_99</span> <span class="o">:</span> <span class="n">out_param</span> <span class="o">(</span><span class="n">field</span> <span class="err">?</span><span class="n">x_97</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">field_extension</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_101</span> <span class="err">?</span><span class="n">x_102</span> <span class="err">?</span><span class="n">x_103</span> <span class="err">?</span><span class="n">x_104</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">26</span><span class="o">)</span> <span class="err">?</span><span class="n">x_104</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="err">?</span><span class="n">x_101</span> <span class="err">?</span><span class="n">x_102</span> <span class="err">?</span><span class="n">x_103</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">algebraic_field_extension</span><span class="bp">.</span><span class="n">to_field_extension</span> <span class="err">?</span><span class="n">x_105</span> <span class="err">?</span><span class="n">x_106</span> <span class="err">?</span><span class="n">x_107</span> <span class="err">?</span><span class="n">x_108</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">27</span><span class="o">)</span> <span class="err">?</span><span class="n">x_108</span> <span class="o">:</span> <span class="bp">@</span><span class="n">algebraic_field_extension</span> <span class="err">?</span><span class="n">x_105</span> <span class="err">?</span><span class="n">x_106</span> <span class="err">?</span><span class="n">x_107</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">algebraic_closure</span><span class="bp">.</span><span class="n">to_algebraic_field_extension</span> <span class="err">?</span><span class="n">x_109</span> <span class="err">?</span><span class="n">x_110</span> <span class="err">?</span><span class="n">x_111</span> <span class="err">?</span><span class="n">x_112</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128143694):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">alg_closed_field</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">field</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">alg_closed</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="n">deg</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">α</span> <span class="n">α</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>

<span class="n">class</span> <span class="n">field_extension</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">field</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">field_extension</span><span class="bp">.</span><span class="n">to_is_ring_hom</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">field_extension</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">field_extension</span><span class="bp">.</span><span class="n">f</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">field_extension</span><span class="bp">.</span><span class="n">hom</span> <span class="n">β</span>

<span class="kn">instance</span> <span class="n">field_extension</span><span class="bp">.</span><span class="n">to_algebra</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">field_extension</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">algebra</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">field_extension</span><span class="bp">.</span><span class="n">f</span> <span class="n">β</span> <span class="o">}</span>

<span class="n">class</span> <span class="n">algebraic_field_extension</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">field_extension</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">algebraic</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">α</span> <span class="n">β</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>

<span class="kn">set_option</span> <span class="n">old_structure_cmd</span> <span class="n">true</span>

<span class="n">class</span> <span class="n">algebraic_closure</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">alg_closed_field</span> <span class="n">β</span><span class="o">,</span> <span class="n">algebraic_field_extension</span> <span class="n">α</span> <span class="n">β</span>

<span class="kn">set_option</span> <span class="n">old_structure_cmd</span> <span class="n">false</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128143821):
<p>I'm not very good at dealing with typeclasses</p>

#### [ Kenny Lau (Jun 16 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144488):
<p>somehow the same setting with <code>ring</code> instead of <code>field</code> doesn't cause this problem:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">comm_ring</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
</pre></div>


<p>This doesn't cause any loops</p>

#### [ Kenny Lau (Jun 16 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144728):
<p>solution:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">is_alg_closed_field</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">alg_closed</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="n">deg</span> <span class="bp">&gt;</span> <span class="mi">1</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">α</span> <span class="n">α</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>

<span class="n">class</span> <span class="n">field_extension</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">field</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">field_extension</span><span class="bp">.</span><span class="n">to_is_ring_hom</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">field_extension</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">field_extension</span><span class="bp">.</span><span class="n">f</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">field_extension</span><span class="bp">.</span><span class="n">hom</span> <span class="n">β</span>

<span class="kn">instance</span> <span class="n">field_extension</span><span class="bp">.</span><span class="n">to_algebra</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">field_extension</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">algebra</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">field_extension</span><span class="bp">.</span><span class="n">f</span> <span class="n">β</span> <span class="o">}</span>

<span class="n">class</span> <span class="n">is_algebraic_field_extension</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">field_extension</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">algebraic</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">α</span> <span class="n">β</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>

<span class="n">class</span> <span class="n">is_algebraic_closure</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">field_extension</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span>
  <span class="kn">extends</span> <span class="n">is_alg_closed_field</span> <span class="n">β</span><span class="o">,</span> <span class="n">is_algebraic_field_extension</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Prop</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144742):
<p>TLDR: change <code>algebraic_field_extension</code> (not <code>Prop</code>) to <code>is_algebraic_field_extension</code> (<code>Prop</code>) etc</p>

#### [ Kenny Lau (Jun 16 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144825):
<p>update: it is not true that the <code>algebra</code> causes no problem</p>

#### [ Mario Carneiro (Jun 16 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144857):
<blockquote>
<p><code>out_param (field ?x_97)</code></p>
</blockquote>
<p>not the first time I've seen this today</p>

#### [ Kenny Lau (Jun 16 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144919):
<p>but <code>module</code> seems to be doing fine</p>

#### [ Mario Carneiro (Jun 16 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144929):
<p>What caused this typeclass search? You never want to find arbitrary fields</p>

#### [ Kenny Lau (Jun 16 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144937):
<p>what stops <code>ring.to_module</code> and <code>class module ... [ring _]</code> from forming a loop?</p>

#### [ Kenny Lau (Jun 16 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145013):
<blockquote>
<p>What caused this typeclass search? You never want to find arbitrary fields</p>
</blockquote>
<p>I have something involving rings and no fields at all. The searcher wants to know that it has addition. Somehow it got to fields, and then it started the loop</p>

#### [ Mario Carneiro (Jun 16 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145033):
<p>I don't mean just <code>field ?</code>, but also <code>ring ?</code> and other such things</p>

#### [ Mario Carneiro (Jun 16 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145047):
<p>the bad sign is a class on a metavar</p>

#### [ Kenny Lau (Jun 16 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145075):
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span>  <span class="n">class</span><span class="bp">-</span><span class="kn">instance</span> <span class="n">resolution</span> <span class="n">trace</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">pi</span><span class="bp">.</span><span class="n">has_zero</span> <span class="err">?</span><span class="n">x_1</span> <span class="err">?</span><span class="n">x_2</span> <span class="err">?</span><span class="n">x_3</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">has_zero</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">has_zero</span> <span class="err">?</span><span class="n">x_4</span> <span class="err">?</span><span class="n">x_5</span> <span class="err">?</span><span class="n">x_6</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">multiset</span><span class="bp">.</span><span class="n">has_zero</span> <span class="err">?</span><span class="n">x_7</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">unsigned</span><span class="bp">.</span><span class="n">has_zero</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">fin</span><span class="bp">.</span><span class="n">has_zero</span> <span class="err">?</span><span class="n">x_8</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">has_zero</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">has_zero</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">no_zero_divisors</span><span class="bp">.</span><span class="n">to_has_zero</span> <span class="err">?</span><span class="n">x_9</span> <span class="err">?</span><span class="n">x_10</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_10</span> <span class="o">:</span> <span class="n">no_zero_divisors</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">domain</span><span class="bp">.</span><span class="n">to_no_zero_divisors</span> <span class="err">?</span><span class="n">x_11</span> <span class="err">?</span><span class="n">x_12</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">2</span><span class="o">)</span> <span class="err">?</span><span class="n">x_12</span> <span class="o">:</span> <span class="n">domain</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_nonneg_ring</span><span class="bp">.</span><span class="n">to_domain</span> <span class="err">?</span><span class="n">x_13</span> <span class="err">?</span><span class="n">x_14</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">2</span><span class="o">)</span> <span class="err">?</span><span class="n">x_12</span> <span class="o">:</span> <span class="n">domain</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">to_domain</span> <span class="err">?</span><span class="n">x_13</span> <span class="err">?</span><span class="n">x_14</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">3</span><span class="o">)</span> <span class="err">?</span><span class="n">x_14</span> <span class="o">:</span> <span class="n">linear_ordered_ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_nonneg_ring</span><span class="bp">.</span><span class="n">to_linear_ordered_ring</span> <span class="err">?</span><span class="n">x_15</span> <span class="err">?</span><span class="n">x_16</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">3</span><span class="o">)</span> <span class="err">?</span><span class="n">x_14</span> <span class="o">:</span> <span class="n">linear_ordered_ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_ordered_field</span><span class="bp">.</span><span class="n">to_linear_ordered_ring</span> <span class="err">?</span><span class="n">x_15</span> <span class="err">?</span><span class="n">x_16</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">4</span><span class="o">)</span> <span class="err">?</span><span class="n">x_16</span> <span class="o">:</span> <span class="n">linear_ordered_field</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">discrete_linear_ordered_field</span><span class="bp">.</span><span class="n">to_linear_ordered_field</span> <span class="err">?</span><span class="n">x_17</span> <span class="err">?</span><span class="n">x_18</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">3</span><span class="o">)</span> <span class="err">?</span><span class="n">x_14</span> <span class="o">:</span> <span class="n">linear_ordered_ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_ordered_comm_ring</span><span class="bp">.</span><span class="n">to_linear_ordered_ring</span> <span class="err">?</span><span class="n">x_15</span> <span class="err">?</span><span class="n">x_16</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">4</span><span class="o">)</span> <span class="err">?</span><span class="n">x_16</span> <span class="o">:</span> <span class="n">linear_ordered_comm_ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">decidable_linear_ordered_comm_ring</span><span class="bp">.</span><span class="n">to_linear_ordered_comm_ring</span> <span class="err">?</span><span class="n">x_17</span> <span class="err">?</span><span class="n">x_18</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_18</span> <span class="o">:</span> <span class="n">decidable_linear_ordered_comm_ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_nonneg_ring</span><span class="bp">.</span><span class="n">to_decidable_linear_ordered_comm_ring</span> <span class="err">?</span><span class="n">x_19</span> <span class="err">?</span><span class="n">x_20</span> <span class="err">?</span><span class="n">x_21</span> <span class="err">?</span><span class="n">x_22</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_18</span> <span class="o">:</span> <span class="n">decidable_linear_ordered_comm_ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">decidable_linear_ordered_comm_ring</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_18</span> <span class="o">:</span> <span class="n">decidable_linear_ordered_comm_ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">discrete_linear_ordered_field</span><span class="bp">.</span><span class="n">to_decidable_linear_ordered_comm_ring</span> <span class="err">?</span><span class="n">x_19</span> <span class="err">?</span><span class="n">x_20</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">2</span><span class="o">)</span> <span class="err">?</span><span class="n">x_12</span> <span class="o">:</span> <span class="n">domain</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">division_ring</span><span class="bp">.</span><span class="n">to_domain</span> <span class="err">?</span><span class="n">x_13</span> <span class="err">?</span><span class="n">x_14</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">3</span><span class="o">)</span> <span class="err">?</span><span class="n">x_14</span> <span class="o">:</span> <span class="n">division_ring</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">field</span><span class="bp">.</span><span class="n">to_division_ring</span> <span class="err">?</span><span class="n">x_15</span> <span class="err">?</span><span class="n">x_16</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">4</span><span class="o">)</span> <span class="err">?</span><span class="n">x_16</span> <span class="o">:</span> <span class="n">field</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">field_extension</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_17</span> <span class="err">?</span><span class="n">x_18</span> <span class="err">?</span><span class="n">x_19</span> <span class="err">?</span><span class="n">x_20</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_20</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="err">?</span><span class="n">x_17</span> <span class="n">α</span> <span class="err">?</span><span class="n">x_19</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">algebraic_field_extension</span><span class="bp">.</span><span class="n">to_field_extension</span> <span class="err">?</span><span class="n">x_21</span> <span class="err">?</span><span class="n">x_22</span> <span class="err">?</span><span class="n">x_23</span> <span class="err">?</span><span class="n">x_24</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">6</span><span class="o">)</span> <span class="err">?</span><span class="n">x_24</span> <span class="o">:</span> <span class="bp">@</span><span class="n">algebraic_field_extension</span> <span class="err">?</span><span class="n">x_21</span> <span class="n">α</span> <span class="err">?</span><span class="n">x_23</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">algebraic_closure</span><span class="bp">.</span><span class="n">to_algebraic_field_extension</span> <span class="err">?</span><span class="n">x_25</span> <span class="err">?</span><span class="n">x_26</span> <span class="err">?</span><span class="n">x_27</span> <span class="err">?</span><span class="n">x_28</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_27</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_25</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">field_extension</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_29</span> <span class="err">?</span><span class="n">x_30</span> <span class="err">?</span><span class="n">x_31</span> <span class="err">?</span><span class="n">x_32</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">8</span><span class="o">)</span> <span class="err">?</span><span class="n">x_32</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="err">?</span><span class="n">x_29</span> <span class="err">?</span><span class="n">x_30</span> <span class="err">?</span><span class="n">x_31</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">algebraic_field_extension</span><span class="bp">.</span><span class="n">to_field_extension</span> <span class="err">?</span><span class="n">x_33</span> <span class="err">?</span><span class="n">x_34</span> <span class="err">?</span><span class="n">x_35</span> <span class="err">?</span><span class="n">x_36</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">9</span><span class="o">)</span> <span class="err">?</span><span class="n">x_36</span> <span class="o">:</span> <span class="bp">@</span><span class="n">algebraic_field_extension</span> <span class="err">?</span><span class="n">x_33</span> <span class="err">?</span><span class="n">x_34</span> <span class="err">?</span><span class="n">x_35</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">algebraic_closure</span><span class="bp">.</span><span class="n">to_algebraic_field_extension</span> <span class="err">?</span><span class="n">x_37</span> <span class="err">?</span><span class="n">x_38</span> <span class="err">?</span><span class="n">x_39</span> <span class="err">?</span><span class="n">x_40</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">10</span><span class="o">)</span> <span class="err">?</span><span class="n">x_39</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_37</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">field_extension</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_41</span> <span class="err">?</span><span class="n">x_42</span> <span class="err">?</span><span class="n">x_43</span> <span class="err">?</span><span class="n">x_44</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145120):
<p>loop the last 3 lines</p>

#### [ Mario Carneiro (Jun 16 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145133):
<p><code>field_extension.to_field</code></p>

#### [ Mario Carneiro (Jun 16 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145134):
<p>kill it</p>

#### [ Kenny Lau (Jun 16 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145145):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">field_extension</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">field</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145161):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
  <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">comm_ring</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">[</span><span class="n">hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145162):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">module</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">ring</span> <span class="n">α</span><span class="o">]</span>
  <span class="kn">extends</span> <span class="n">has_scalar</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span> <span class="n">add_comm_group</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">smul_add</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">r</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="n">r</span> <span class="err">•</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">r</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">r</span> <span class="err">•</span> <span class="n">y</span><span class="o">)</span>
<span class="o">(</span><span class="n">add_smul</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">r</span> <span class="n">s</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="o">(</span><span class="n">r</span> <span class="bp">+</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">r</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">s</span> <span class="err">•</span> <span class="n">x</span><span class="o">)</span>
<span class="o">(</span><span class="n">mul_smul</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">r</span> <span class="n">s</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="o">(</span><span class="n">r</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">r</span> <span class="err">•</span> <span class="n">s</span> <span class="err">•</span> <span class="n">x</span><span class="o">)</span>
<span class="o">(</span><span class="n">one_smul</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145165):
<p>(not that <code>algebra</code> is not causing problem)</p>

#### [ Kenny Lau (Jun 16 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145204):
<p>why does <code>module</code> have no problem</p>

#### [ Kenny Lau (Jun 16 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145313):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what should I replace it with?</p>

#### [ Kenny Lau (Jun 16 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145315):
<p>I see</p>

#### [ Kenny Lau (Jun 16 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128147101):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">subring</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">add_mem</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">},</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span>
<span class="o">(</span><span class="n">neg_mem</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span><span class="o">},</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="bp">-</span><span class="n">x</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span>
<span class="o">(</span><span class="n">mul_mem</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">},</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span>
<span class="o">(</span><span class="n">one_mem</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">subring</span>

<span class="kn">instance</span> <span class="n">subring</span><span class="bp">.</span><span class="n">to_comm_ring</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">subring</span> <span class="n">α</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">S</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add</span>            <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">,</span> <span class="n">add_mem</span> <span class="n">hx</span> <span class="n">hy</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">add_assoc</span>      <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">z</span><span class="o">,</span> <span class="n">hz</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">add_assoc</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span>
  <span class="n">zero</span>           <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="o">(</span><span class="n">add_neg_self</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">α</span><span class="o">))</span> <span class="err">$</span> <span class="n">add_mem</span> <span class="o">(</span><span class="n">one_mem</span> <span class="n">S</span><span class="o">)</span> <span class="err">$</span> <span class="n">neg_mem</span> <span class="err">$</span> <span class="n">one_mem</span> <span class="n">S</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">zero_add</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">zero_add</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">add_zero</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">add_zero</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">neg</span>            <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨-</span><span class="n">x</span><span class="o">,</span> <span class="n">neg_mem</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">add_left_neg</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">add_left_neg</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">add_comm</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">add_comm</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">mul</span>            <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">,</span> <span class="n">mul_mem</span> <span class="n">hx</span> <span class="n">hy</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_assoc</span>      <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">z</span><span class="o">,</span> <span class="n">hz</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">mul_assoc</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span>
  <span class="n">one</span>            <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">one_mem</span> <span class="n">S</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">one_mul</span>        <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">one_mul</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">mul_one</span>        <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">mul_one</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">left_distrib</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">z</span><span class="o">,</span> <span class="n">hz</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">left_distrib</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span>
  <span class="n">right_distrib</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">z</span><span class="o">,</span> <span class="n">hz</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">right_distrib</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span>
  <span class="n">mul_comm</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">mul_comm</span> <span class="n">x</span> <span class="n">y</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128147109):
<p>will this <code>instance</code> cause problems?</p>

#### [ Kenny Lau (Jun 16 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128147157):
<p>if so, what should I replace it with?</p>

#### [ Kenny Lau (Jun 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128150369):
<p>adding <code>by letI := subring.to_comm_ring _ S</code> to every definition and theorem is not very feasible</p>

#### [ Kenny Lau (Jun 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128150378):
<p>and is wasting me a lot of time</p>

#### [ Kenny Lau (Jun 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128150382):
<p>but as soon as I make it an instance, everything crashes</p>

#### [ Kenny Lau (Jun 16 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128162502):
<p>what is this</p>

#### [ Kenny Lau (Jun 16 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128162503):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Hausdorff_abelianization</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">topological_group</span> <span class="n">G</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">left_cosets</span> <span class="o">(</span><span class="n">abelianization</span> <span class="n">G</span><span class="o">)</span> <span class="bp">_</span> <span class="o">(</span><span class="n">closure</span> <span class="o">{</span><span class="mi">1</span><span class="o">})</span>
  <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128162544):
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_60</span> <span class="o">:</span> <span class="n">topological_group</span> <span class="n">G</span> <span class="o">:=</span> <span class="n">t</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
</pre></div>

#### [ Kenny Lau (Jun 16 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128162755):
<p>Lean, they <em>are</em> the same</p>

#### [ Kenny Lau (Jun 16 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128165992):
<p>if <code>subring.to_comm_ring</code> causes problems then why doesn't <code>subtype.group</code> cause problems?</p>

#### [ Kenny Lau (Jun 16 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128168992):
<blockquote>
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> it can be avoided by using universes instead of <code>Type*</code></p>
</blockquote>
<p><a href="#narrow/stream/113488-general/subject/unfolding.20notation.20in.20theorem.20vs.20def.2Finstance/near/128167978" title="#narrow/stream/113488-general/subject/unfolding.20notation.20in.20theorem.20vs.20def.2Finstance/near/128167978">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/unfolding.20notation.20in.20theorem.20vs.20def.2Finstance/near/128167978</a></p>

#### [ Kenny Lau (Jun 16 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128168993):
<p>oh and of <strong><em>course</em></strong> the same trick applies to this case</p>

#### [ Kenny Lau (Jun 16 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128168994):
<p>there's no loop any more</p>

#### [ Kenny Lau (Jun 16 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128168995):
<p>once I use <code>Type u</code> instead of <code>Type*</code></p>

#### [ Kenny Lau (Jun 16 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128169044):
<blockquote>
<p>Lean, they <em>are</em> the same</p>
</blockquote>
<p><a href="#narrow/stream/113488-general/subject/typeclass.20problems/near/128162755" title="#narrow/stream/113488-general/subject/typeclass.20problems/near/128162755">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/typeclass.20problems/near/128162755</a></p>

#### [ Kenny Lau (Jun 16 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128169046):
<p>ditto</p>

#### [ Kenny Lau (Jun 16 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174540):
<p>Is this a good instance?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Hausdorff_abelianization</span><span class="bp">.</span><span class="n">setoid</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
  <span class="o">[</span><span class="n">topological_group</span> <span class="n">G</span><span class="o">]</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">G</span> <span class="o">:=</span>
<span class="n">left_rel</span> <span class="o">(</span><span class="n">closure</span> <span class="o">(</span><span class="n">commutator_subgroup</span> <span class="n">G</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span><span class="o">))</span>
</pre></div>

#### [ Mario Carneiro (Jun 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174678):
<p>A local instance maybe</p>

#### [ Mario Carneiro (Jun 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174679):
<p>it looks a bit domain specific</p>

#### [ Kenny Lau (Jun 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174680):
<p>domain specific?</p>

#### [ Mario Carneiro (Jun 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174681):
<p>is there a reason that should be the canonical equivalence on any top group?</p>

#### [ Kenny Lau (Jun 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174686):
<p>it's the functor from TopGrp to AbelianHasudorffTopGrp</p>

#### [ Johan Commelin (Jun 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174688):
<p>Kenny, for every topological group G, there should be at most 1 instance of <code>setoid G</code>.</p>

#### [ Kenny Lau (Jun 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174689):
<p>I see</p>

#### [ Kenny Lau (Jun 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174690):
<p>ok this isn't canonical then</p>

#### [ Johan Commelin (Jun 16 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174737):
<p>So you should probably not make this an instance. But possibly define AbHausTopGrp, and make it an instance of that...</p>

#### [ Kenny Lau (Jun 16 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174743):
<p>I'm glad I didn't switch the first two words of the name of the category... :D</p>

#### [ Johan Commelin (Jun 16 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174782):
<p>I don't get what would be wrong with that? ... Am I overly naive, and missing a joke?</p>

#### [ Kenny Lau (Jun 16 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174789):
<p>it sounds similar to a rude word in german</p>

#### [ Johan Commelin (Jun 16 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174830):
<p>Ach so, ich muss noch viel Deutsch üben. Und ich kenn kein unhöfliche Worten.</p>

#### [ Kenny Lau (Jun 16 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174838):
<p>"Hau ab" means "piss off"</p>

#### [ Johan Commelin (Jun 16 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174879):
<p>Wunderbar</p>

#### [ Kenny Lau (Jun 18 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128218541):
<p><a href="/user_uploads/3121/THVijpQP7DblIbSyWC9G2hGx/2018-06-17-2.png" target="_blank" title="2018-06-17-2.png">2018-06-17-2.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/THVijpQP7DblIbSyWC9G2hGx/2018-06-17-2.png" target="_blank" title="2018-06-17-2.png"><img src="/user_uploads/3121/THVijpQP7DblIbSyWC9G2hGx/2018-06-17-2.png"></a></div>

#### [ Kenny Lau (Jun 18 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128218546):
<p>when I turn <code>trace.class_instances</code> on, there's nothing peculiar, except the <code>has_sizeof</code> thing getting pretty long</p>

#### [ Kenny Lau (Jun 18 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128218550):
<p>that option is not really helpful in my experience</p>

#### [ Kenny Lau (Jun 18 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128218552):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Jun 18 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219542):
<p>oh and the depth of the class instance search never went to 6</p>

#### [ Kenny Lau (Jun 18 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219604):
<p>and I don't think <code>cogroup.base_change_left</code> is the problem, after looking at the trace</p>

#### [ Kenny Lau (Jun 18 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219700):
<p>it's here: <a href="https://github.com/kckennylau/local-langlands-abelian/blob/master/src/torus.lean#L136" target="_blank" title="https://github.com/kckennylau/local-langlands-abelian/blob/master/src/torus.lean#L136">https://github.com/kckennylau/local-langlands-abelian/blob/master/src/torus.lean#L136</a></p>

#### [ Simon Hudon (Jun 18 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219741):
<p>Why does it need an instance of <code>has_sizeof</code>?</p>

#### [ Kenny Lau (Jun 18 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219742):
<p>no idea</p>

#### [ Kenny Lau (Jun 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219743):
<p>to build a structure, I think?</p>

#### [ Kenny Lau (Jun 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219748):
<p>Please help me, my deadline is in like 12 hours</p>

#### [ Simon Hudon (Jun 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219751):
<p>Your screenshot is not telling me much. If you comment one field declaration at a time, when does it stop failing?</p>

#### [ Kenny Lau (Jun 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219752):
<p>as soon as I remove the last field</p>

#### [ Kenny Lau (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219907):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> is there other information I can provide?</p>

#### [ Simon Hudon (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219909):
<p>I think your project needs mathlib</p>

#### [ Simon Hudon (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219910):
<p>I'm building it on my machine to have a closer look</p>

#### [ Kenny Lau (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219911):
<p>thank you very much</p>

#### [ Kenny Lau (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219912):
<p>yes, it does require mathlib</p>

#### [ Simon Hudon (Jun 18 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219951):
<p>Is it possible you did not commit the latest version of <code>leanpkg.toml</code>? (I don't need it, I can fix it but in general, that makes things smoother for people trying your project)</p>

#### [ Kenny Lau (Jun 18 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219960):
<p>oh I didn't really set it up</p>

#### [ Simon Hudon (Jun 18 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219961):
<p>Ah ok. Just to be sure, do you use Lean 3.4.1 and the latest mathlib?</p>

#### [ Kenny Lau (Jun 18 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219999):
<p>yes</p>

#### [ Kenny Lau (Jun 18 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220051):
<p>ok not exactly the latest</p>

#### [ Kenny Lau (Jun 18 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220052):
<p>i'm on mathlib commit fe590ca272a41bb321a13be505964e78cad1e731</p>

#### [ Kenny Lau (Jun 18 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220055):
<p>third from latest</p>

#### [ Simon Hudon (Jun 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220966):
<p>In this expression <code>(tensor_a F split.S T)</code> you get into trouble because <code>split.S</code> is a set but a type is expected. If you replace it with <code>subtype split.S</code>, type is required to have a <code>comm_ring</code> instance which you only have for <code>T</code></p>

#### [ Kenny Lau (Jun 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220967):
<p>:o</p>

#### [ Kenny Lau (Jun 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220968):
<p>thanks</p>

#### [ Kenny Lau (Jun 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220970):
<p>do you have a fix?</p>

#### [ Simon Hudon (Jun 18 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221062):
<p>No, it really depends on what you're trying to do. If you actually want <code>subtype split.S</code>, you'd need to add <code>[comm_ring (subtype split.S)]</code> to the local instances which would get hairy because <code>split</code> is a field. Maybe replacing <code>split.S</code> with <code>T</code> would suit your purpose, in which case, the fit is perfect because you already have a <code>comm_ring T</code> instance</p>

#### [ Kenny Lau (Jun 18 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221064):
<p>I can't just change my deifnition like that?</p>

#### [ Simon Hudon (Jun 18 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221065):
<p>Which one?</p>

#### [ Kenny Lau (Jun 18 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221070):
<p>replacing <code>split.S</code> with <code>T</code>?</p>

#### [ Simon Hudon (Jun 18 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221072):
<p>That might work. I haven't tried it but that would fix that particular problem</p>

#### [ Kenny Lau (Jun 18 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221074):
<p>I mean, it would be a wrong definition</p>

#### [ Simon Hudon (Jun 18 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221116):
<p>What would be the right definition?</p>

#### [ Kenny Lau (Jun 18 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221117):
<p><code>split.S</code> as it is</p>

#### [ Simon Hudon (Jun 18 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221121):
<p>That would be nonsense: that's not type correct.</p>

#### [ Simon Hudon (Jun 18 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221129):
<p>Unless your <code>tensor_a</code> definition is wrong and it should take a set there, not a type</p>

#### [ Kenny Lau (Jun 18 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221130):
<p>I'm coercing a set to a type</p>

#### [ Kenny Lau (Jun 18 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221134):
<p>it's done automatically</p>

#### [ Kenny Lau (Jun 18 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221135):
<p>I do it every time</p>

#### [ Simon Hudon (Jun 18 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221186):
<p>Right but that type is then expected to be a commutative ring. I'm not sure how that can be proved automatically</p>

#### [ Kenny Lau (Jun 18 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221190):
<p>I have a working version above it, one can trace class instance</p>

#### [ Kenny Lau (Jun 18 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221228):
<p>I think it will go through subfield -&gt; field -&gt; comm_ring</p>

#### [ Simon Hudon (Jun 18 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221235):
<p>How do you prove that it's a subfield?</p>

#### [ Kenny Lau (Jun 18 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221237):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">finite_Galois_intermediate_extension</span><span class="bp">.</span><span class="n">to_subfield</span>
</pre></div>

#### [ Kenny Lau (Jun 18 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221239):
<p>L132 of field_extensions.lean</p>

#### [ Kenny Lau (Jun 18 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221248):
<p>right, I just realized, there should be no problem, because there's a working version right above it!</p>

#### [ Simon Hudon (Jun 18 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221291):
<p>Which line?</p>

#### [ Kenny Lau (Jun 18 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221292):
<p>The <code>#check</code> one</p>

#### [ Kenny Lau (Jun 18 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221293):
<p>L139</p>

#### [ Kenny Lau (Jun 18 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221301):
<p>oops</p>

#### [ Kenny Lau (Jun 18 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221302):
<p>L123</p>

#### [ Kenny Lau (Jun 18 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221303):
<p><a href="https://github.com/kckennylau/local-langlands-abelian/blob/master/src/torus.lean#L123" target="_blank" title="https://github.com/kckennylau/local-langlands-abelian/blob/master/src/torus.lean#L123">https://github.com/kckennylau/local-langlands-abelian/blob/master/src/torus.lean#L123</a></p>

#### [ Kenny Lau (Jun 18 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221304):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">F</span><span class="o">]</span>
  <span class="o">(</span><span class="n">AC</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_alg_closed_field</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">[</span><span class="n">field_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_algebraic_closure</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">(</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">algebra</span> <span class="n">F</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">cogroup</span> <span class="n">F</span> <span class="n">T</span><span class="o">]</span>
<span class="o">(</span><span class="n">split</span> <span class="o">:</span> <span class="n">finite_Galois_intermediate_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">)</span>
<span class="o">(</span><span class="n">rank</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span>
<span class="bp">@</span><span class="n">cogroup_iso</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="bp">_</span> <span class="o">(</span><span class="n">tensor_a</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">tensor_a</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="n">base_change_left</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">GL₁ⁿ</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">rank</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span>
  <span class="o">(</span><span class="n">cogroup</span><span class="bp">.</span><span class="n">base_change_left</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">GL₁ⁿ</span><span class="bp">.</span><span class="n">cogroup</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Jun 18 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221344):
<p>If I change that <code>check</code> into a <code>def</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">F</span><span class="o">]</span>
  <span class="o">(</span><span class="n">AC</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_alg_closed_field</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">[</span><span class="n">field_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_algebraic_closure</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">(</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">algebra</span> <span class="n">F</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">cogroup</span> <span class="n">F</span> <span class="n">T</span><span class="o">]</span>
<span class="o">(</span><span class="n">split</span> <span class="o">:</span> <span class="n">finite_Galois_intermediate_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">)</span>
<span class="o">(</span><span class="n">rank</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span>
<span class="bp">@</span><span class="n">cogroup_iso</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="bp">_</span> <span class="o">(</span><span class="n">tensor_a</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">tensor_a</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="n">base_change_left</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">GL₁ⁿ</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">rank</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span>
  <span class="o">(</span><span class="n">cogroup</span><span class="bp">.</span><span class="n">base_change_left</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">GL₁ⁿ</span><span class="bp">.</span><span class="n">cogroup</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Jun 18 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221345):
<p>I get I lot of errors</p>

#### [ Kenny Lau (Jun 18 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221352):
<p>curious</p>

#### [ Simon Hudon (Jun 18 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221354):
<p><a href="/user_uploads/3121/K4n0zheF40urE2YaifViOPKA/Screen-Shot-2018-06-17-at-7.57.01-PM.png" target="_blank" title="Screen-Shot-2018-06-17-at-7.57.01-PM.png">Screen-Shot-2018-06-17-at-7.57.01-PM.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/K4n0zheF40urE2YaifViOPKA/Screen-Shot-2018-06-17-at-7.57.01-PM.png" target="_blank" title="Screen-Shot-2018-06-17-at-7.57.01-PM.png"><img src="/user_uploads/3121/K4n0zheF40urE2YaifViOPKA/Screen-Shot-2018-06-17-at-7.57.01-PM.png"></a></div>

#### [ Simon Hudon (Jun 18 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221356):
<p>I think you're asking a lot of type class inference</p>

#### [ Kenny Lau (Jun 18 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221395):
<p>heh...</p>

#### [ Kenny Lau (Jun 18 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221397):
<p>how about I move them before the colon</p>

#### [ Kenny Lau (Jun 18 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221398):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">F</span><span class="o">]</span>
  <span class="o">(</span><span class="n">AC</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_alg_closed_field</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">[</span><span class="n">field_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_algebraic_closure</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">(</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">algebra</span> <span class="n">F</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">cogroup</span> <span class="n">F</span> <span class="n">T</span><span class="o">]</span>
<span class="o">(</span><span class="n">split</span> <span class="o">:</span> <span class="n">finite_Galois_intermediate_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">)</span>
<span class="o">(</span><span class="n">rank</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">cogroup_iso</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="bp">_</span> <span class="o">(</span><span class="n">tensor_a</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">tensor_a</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="n">base_change_left</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">GL₁ⁿ</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">rank</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span>
  <span class="o">(</span><span class="n">cogroup</span><span class="bp">.</span><span class="n">base_change_left</span> <span class="n">F</span> <span class="n">split</span><span class="bp">.</span><span class="n">S</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">GL₁ⁿ</span><span class="bp">.</span><span class="n">cogroup</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jun 18 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221399):
<p>no errors!</p>

#### [ Kenny Lau (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221404):
<p>also I looked at the trace as I said before</p>

#### [ Simon Hudon (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221407):
<p>You're right, I didn't do it well</p>

#### [ Kenny Lau (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221408):
<p>there is no issue with the typeclass inferences</p>

#### [ Kenny Lau (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221409):
<p>and the max depth is 5</p>

#### [ Kenny Lau (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221412):
<p>there should not be any error</p>

#### [ Simon Hudon (Jun 18 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221463):
<p>Try:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">torus</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">F</span><span class="o">]</span>
  <span class="o">(</span><span class="n">AC</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_alg_closed_field</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">[</span><span class="n">field_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_algebraic_closure</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">(</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">algebra</span> <span class="n">F</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">cogroup</span> <span class="n">F</span> <span class="n">T</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">split</span> <span class="o">:</span> <span class="n">finite_Galois_intermediate_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">)</span>
<span class="o">(</span><span class="n">rank</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="o">(</span><span class="n">splits</span> <span class="o">:</span> <span class="n">foo</span> <span class="n">F</span> <span class="n">AC</span> <span class="n">T</span> <span class="n">split</span> <span class="n">rank</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jun 18 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221471):
<p>what the actual</p>

#### [ Kenny Lau (Jun 18 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221475):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> you need to see this</p>

#### [ Kenny Lau (Jun 18 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221518):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> what do you think</p>

#### [ Simon Hudon (Jun 18 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221525):
<p>I'm not actually sure why the other one wouldn't work. In general, there's nothing wrong with breaking down your definitions into smaller pieces though</p>

#### [ Kenny Lau (Jun 18 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221567):
<p>I see</p>

#### [ Kenny Lau (Jun 18 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221763):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> how should I break this loop?</p>

#### [ Kenny Lau (Jun 18 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221764):
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_31</span> <span class="o">:</span> <span class="n">field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_6</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_31</span> <span class="o">:</span> <span class="n">field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">subfield</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_34</span> <span class="err">?</span><span class="n">x_35</span> <span class="err">?</span><span class="n">x_36</span> <span class="err">?</span><span class="n">x_37</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_31</span> <span class="o">:</span> <span class="n">field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">topological_field</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_38</span> <span class="err">?</span><span class="n">x_39</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_31</span> <span class="o">:</span> <span class="n">field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_ordered_field</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_34</span> <span class="err">?</span><span class="n">x_35</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">6</span><span class="o">)</span> <span class="err">?</span><span class="n">x_35</span> <span class="o">:</span> <span class="n">linear_ordered_field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">discrete_linear_ordered_field</span><span class="bp">.</span><span class="n">to_linear_ordered_field</span> <span class="err">?</span><span class="n">x_36</span> <span class="err">?</span><span class="n">x_37</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_37</span> <span class="o">:</span> <span class="n">discrete_linear_ordered_field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="n">rat</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_31</span> <span class="o">:</span> <span class="n">field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">discrete_field</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_34</span> <span class="err">?</span><span class="n">x_35</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">6</span><span class="o">)</span> <span class="err">?</span><span class="n">x_35</span> <span class="o">:</span> <span class="n">discrete_field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="n">rat</span><span class="bp">.</span><span class="n">field_rat</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">6</span><span class="o">)</span> <span class="err">?</span><span class="n">x_35</span> <span class="o">:</span> <span class="n">discrete_field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">discrete_linear_ordered_field</span><span class="bp">.</span><span class="n">to_discrete_field</span> <span class="err">?</span><span class="n">x_36</span> <span class="err">?</span><span class="n">x_37</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_37</span> <span class="o">:</span> <span class="n">discrete_linear_ordered_field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="n">rat</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_30</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_28</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">subfield</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_34</span> <span class="err">?</span><span class="n">x_35</span> <span class="err">?</span><span class="n">x_36</span> <span class="err">?</span><span class="n">x_37</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">6</span><span class="o">)</span> <span class="err">?</span><span class="n">x_35</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_34</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_7</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">6</span><span class="o">)</span> <span class="err">?</span><span class="n">x_37</span> <span class="o">:</span> <span class="bp">@</span><span class="n">subfield</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="err">?</span><span class="n">x_36</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">finite_Galois_intermediate_extension</span><span class="bp">.</span><span class="n">to_subfield</span> <span class="err">?</span><span class="n">x_38</span> <span class="err">?</span><span class="n">x_39</span> <span class="err">?</span><span class="n">x_40</span> <span class="err">?</span><span class="n">x_41</span> <span class="err">?</span><span class="n">x_42</span> <span class="err">?</span><span class="n">x_43</span> <span class="err">?</span><span class="n">x_44</span> <span class="err">?</span><span class="n">x_45</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_39</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_38</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_7</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_41</span> <span class="o">:</span> <span class="n">field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_7</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_42</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_alg_closed_field</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_8</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_43</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="n">AC</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_9</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_43</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="n">AC</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">is_intermediate_field</span><span class="bp">.</span><span class="n">to_field_extension&#39;</span> <span class="err">?</span><span class="n">x_46</span> <span class="err">?</span><span class="n">x_47</span> <span class="err">?</span><span class="n">x_48</span> <span class="err">?</span><span class="n">x_49</span> <span class="err">?</span><span class="n">x_50</span> <span class="err">?</span><span class="n">x_51</span> <span class="err">?</span><span class="n">x_52</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_43</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="n">AC</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">is_intermediate_field</span><span class="bp">.</span><span class="n">to_field_extension</span> <span class="err">?</span><span class="n">x_53</span> <span class="err">?</span><span class="n">x_54</span> <span class="err">?</span><span class="n">x_55</span> <span class="err">?</span><span class="n">x_56</span> <span class="err">?</span><span class="n">x_57</span> <span class="err">?</span><span class="n">x_58</span> <span class="err">?</span><span class="n">x_59</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_42</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_alg_closed_field</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">is_algebraic_closure</span><span class="bp">.</span><span class="n">to_is_alg_closed_field</span> <span class="err">?</span><span class="n">x_46</span> <span class="err">?</span><span class="n">x_47</span> <span class="err">?</span><span class="n">x_48</span> <span class="err">?</span><span class="n">x_49</span> <span class="err">?</span><span class="n">x_50</span> <span class="err">?</span><span class="n">x_51</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">8</span><span class="o">)</span> <span class="err">?</span><span class="n">x_48</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_46</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_7</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">8</span><span class="o">)</span> <span class="err">?</span><span class="n">x_49</span> <span class="o">:</span> <span class="n">field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_7</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">8</span><span class="o">)</span> <span class="err">?</span><span class="n">x_50</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="n">AC</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_9</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">8</span><span class="o">)</span> <span class="err">?</span><span class="n">x_50</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="n">AC</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">is_intermediate_field</span><span class="bp">.</span><span class="n">to_field_extension&#39;</span> <span class="err">?</span><span class="n">x_52</span> <span class="err">?</span><span class="n">x_53</span> <span class="err">?</span><span class="n">x_54</span> <span class="err">?</span><span class="n">x_55</span> <span class="err">?</span><span class="n">x_56</span> <span class="err">?</span><span class="n">x_57</span> <span class="err">?</span><span class="n">x_58</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">8</span><span class="o">)</span> <span class="err">?</span><span class="n">x_50</span> <span class="o">:</span> <span class="bp">@</span><span class="n">field_extension</span> <span class="n">AC</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">is_intermediate_field</span><span class="bp">.</span><span class="n">to_field_extension</span> <span class="err">?</span><span class="n">x_59</span> <span class="err">?</span><span class="n">x_60</span> <span class="err">?</span><span class="n">x_61</span> <span class="err">?</span><span class="n">x_62</span> <span class="err">?</span><span class="n">x_63</span> <span class="err">?</span><span class="n">x_64</span> <span class="err">?</span><span class="n">x_65</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
</pre></div>

#### [ Simon Hudon (Jun 18 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221823):
<p>There seems to be a circular dependency between your instances. You should try to guarantee that something decreases (syntactically) whenever you apply an instance. For example, <code>instance [decidable_eq a] : decidable_eq (list a) := ... </code> is such an instance. It is about <code>list a</code> and all the instances it relies on involve simpler expressions.</p>

#### [ Kenny Lau (Jun 18 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221863):
<p>sorry but could you explain what you mean by decreasing?</p>

#### [ Simon Hudon (Jun 18 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221918):
<p>If you compare <code>a</code> and <code>list a</code> (one is a type in an assumed instance, the other, in the head of the instance) <code>list a</code> is a more complex expression than <code>a</code>. That means that if I look for an instance of <code>decidable_eq (list a)</code> and I apply the above instance, I'm decreasing the size of my problem so I'm getting closer to a solution. If every instance decreases the size of the problem, you can't search forever. (just like with structural recursion)</p>

#### [ Kenny Lau (Jun 18 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221973):
<p>hmm... but there are times at which I would need to infer simpler instances from complex instances?</p>

#### [ Simon Hudon (Jun 18 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221980):
<p>like <code>field</code> from <code>discrete_linear_ordered_field</code>?</p>

#### [ Kenny Lau (Jun 18 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221981):
<p>sure</p>

#### [ Kenny Lau (Jun 18 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221982):
<p>or sometimes I need to infer a single instance from like 10 instances</p>

#### [ Kenny Lau (Jun 18 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221984):
<p>do you have general workarounds?</p>

#### [ Simon Hudon (Jun 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222030):
<p>A single instance from 10 instances is not a problem as long as each instance is smaller than the initial one</p>

#### [ Kenny Lau (Jun 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222031):
<p>hmm I still don't know how to judge whether two instances are smaller</p>

#### [ Simon Hudon (Jun 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222032):
<p>In the case of <code>discrete_linear_ordered_field</code>, does it not <code>extend</code> <code>field</code>?</p>

#### [ Kenny Lau (Jun 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222034):
<p>I mean, your examples are quite obvious</p>

#### [ Kenny Lau (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222036):
<p>yes it does</p>

#### [ Kenny Lau (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222077):
<p>I think</p>

#### [ Simon Hudon (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222081):
<p>That should be enough, no? You don't need an instance on top of that</p>

#### [ Kenny Lau (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222082):
<p>this is a bad instance then?</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">subring</span><span class="bp">.</span><span class="n">to_comm_ring</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">subring</span> <span class="n">α</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">S</span> <span class="o">:=</span>
</pre></div>

#### [ Simon Hudon (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222085):
<p>You can compare by counting the number of symbols and operators in each types.</p>

#### [ Kenny Lau (Jun 18 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222096):
<p>that instance doesn't seem to be causing much problem though</p>

#### [ Kenny Lau (Jun 18 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222098):
<p>I guess it's because it requires <code>subring</code></p>

#### [ Kenny Lau (Jun 18 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222143):
<p>This seems to be the problem:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">finite_Galois_intermediate_extension</span><span class="bp">.</span><span class="n">to_subfield</span>
  <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">F</span><span class="o">]</span>
  <span class="o">(</span><span class="n">AC</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_alg_closed_field</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">[</span><span class="n">field_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span> <span class="o">[</span><span class="n">is_algebraic_closure</span> <span class="n">F</span> <span class="n">AC</span><span class="o">]</span>
  <span class="o">(</span><span class="n">E</span> <span class="o">:</span> <span class="n">finite_Galois_intermediate_extension</span> <span class="n">F</span> <span class="n">AC</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">subfield</span> <span class="bp">_</span> <span class="n">E</span><span class="bp">.</span><span class="n">S</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Simon Hudon (Jun 18 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222144):
<p><code>subring</code> is actually what I find problematic in it</p>

#### [ Kenny Lau (Jun 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222148):
<p>because I have an instance from subfield to field</p>

#### [ Kenny Lau (Jun 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222151):
<blockquote>
<p><code>subring</code> is actually what I find problematic in it</p>
</blockquote>
<p>how so?</p>

#### [ Simon Hudon (Jun 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222192):
<p>there are invisible operators: <code>comm_ring S</code> is actually <code>comm_ring (subtype S)</code> which is more complex than <code>comm_ring a</code>. However <code>subring a (subtype S)</code> is more complex than <code>comm_ring (subtype S)</code></p>

#### [ Kenny Lau (Jun 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222193):
<p>nah it's <code>subring a S</code></p>

#### [ Kenny Lau (Jun 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222194):
<p>there is no coercion there</p>

#### [ Simon Hudon (Jun 18 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222199):
<p>It might actually fly then</p>

#### [ Simon Hudon (Jun 18 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222201):
<p>Lean is actually more tolerant than what I'm used to and I'm not sure if that's a good thing or if it's just handing you enough rope to hang yourself with</p>

#### [ Kenny Lau (Jun 18 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222258):
<p>this should be the problem</p>

#### [ Kenny Lau (Jun 18 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222259):
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">5</span><span class="o">)</span> <span class="err">?</span><span class="n">x_30</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_28</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">subfield</span><span class="bp">.</span><span class="n">to_field</span> <span class="err">?</span><span class="n">x_34</span> <span class="err">?</span><span class="n">x_35</span> <span class="err">?</span><span class="n">x_36</span> <span class="err">?</span><span class="n">x_37</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">6</span><span class="o">)</span> <span class="err">?</span><span class="n">x_35</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_34</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_7</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">6</span><span class="o">)</span> <span class="err">?</span><span class="n">x_37</span> <span class="o">:</span> <span class="bp">@</span><span class="n">subfield</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="err">?</span><span class="n">x_36</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">finite_Galois_intermediate_extension</span><span class="bp">.</span><span class="n">to_subfield</span> <span class="err">?</span><span class="n">x_38</span> <span class="err">?</span><span class="n">x_39</span> <span class="err">?</span><span class="n">x_40</span> <span class="err">?</span><span class="n">x_41</span> <span class="err">?</span><span class="n">x_42</span> <span class="err">?</span><span class="n">x_43</span> <span class="err">?</span><span class="n">x_44</span> <span class="err">?</span><span class="n">x_45</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_39</span> <span class="o">:</span> <span class="n">field</span> <span class="err">?</span><span class="n">x_38</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_7</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_41</span> <span class="o">:</span> <span class="n">field</span> <span class="n">AC</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_7</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">7</span><span class="o">)</span> <span class="err">?</span><span class="n">x_42</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_alg_closed_field</span> <span class="n">AC</span> <span class="bp">_</span><span class="n">inst_7</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_8</span>
</pre></div>

#### [ Kenny Lau (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222298):
<p>right, subfield.to_field is the problem</p>

#### [ Simon Hudon (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222299):
<p>You can try commenting one instance at a time until the problem disappears</p>

#### [ Simon Hudon (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222302):
<p>cool</p>

#### [ Kenny Lau (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222303):
<p>that isn't how it works</p>

#### [ Kenny Lau (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222306):
<p>if I comment one instance out, a million lines of code will break</p>

#### [ Kenny Lau (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222355):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> a million things depend on <code>subfield.to_field</code> though...</p>

#### [ Kenny Lau (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222357):
<p>this is a huge abyss</p>

#### [ Simon Hudon (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222358):
<p>does <code>subfield</code> extend <code>field</code>?</p>

#### [ Kenny Lau (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222360):
<p>no</p>

#### [ Simon Hudon (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222361):
<p>Why not?</p>

#### [ Kenny Lau (Jun 18 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222364):
<p>just as <code>is_subgroup</code> does not extend <code>group</code></p>

#### [ Kenny Lau (Jun 18 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222368):
<p>and as I say this sentence</p>

#### [ Kenny Lau (Jun 18 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222370):
<p>why doesn't that cause problems?</p>

#### [ Simon Hudon (Jun 18 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222373):
<p>I'm not intimate enough with the algebraic hierarchy to know</p>

#### [ Kenny Lau (Jun 18 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222415):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">group</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">subtype.group : Π {α : Type u_1} [_inst_1 : group α] {s : set α} [_inst_2 : is_subgroup s], group ↥s</span>
<span class="cm">-/</span>
</pre></div>

#### [ Simon Hudon (Jun 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222425):
<p>Actually, because there's no coercion, that's not that big of a deal. A different instance must be worse</p>

#### [ Kenny Lau (Jun 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222427):
<p>hmm</p>

#### [ Kenny Lau (Jun 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222428):
<p>this is a huge mess</p>

#### [ Simon Hudon (Jun 18 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222472):
<p>Yeah, that's a problem with this way of doing type classes. You can't understand each instance in isolation</p>

#### [ Kenny Lau (Jun 18 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222566):
<p>I think depth first search is not very good</p>

#### [ Kevin Buzzard (Jun 18 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128234704):
<p>Kenny remember as a last resort you can just override the type class system and give it the instances yourself. I used to do this all the time when I got stuck on (much easier) stuff.</p>


{% endraw %}
