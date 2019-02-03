---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86749typeclassesdebugging.html
---

## Stream: [general](index.html)
### Topic: [type classes debugging](86749typeclassesdebugging.html)

---


{% raw %}
#### [ Sebastien Gouezel (Dec 29 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707443):
<p>A t2 space is a topological space with some separation property. Every metric space is a t2 space. If you try</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">success</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">letI</span> <span class="o">:</span> <span class="n">t2_space</span> <span class="n">s</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span>
  <span class="n">trivial</span>
<span class="kn">end</span>
</pre></div>


<p>it works fine: the subset <code>s</code> of <code>α</code> inherits a metric space structure, and is therefore t2. Now, try</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">fail</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">letI</span> <span class="o">:</span> <span class="n">t2_space</span> <span class="n">s</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span>
  <span class="n">trivial</span>
<span class="kn">end</span>
</pre></div>


<p>This should be a special case of the previous one, but it loops forever. I have no idea how to debug this kind of behavior.</p>

#### [ Kenny Lau (Dec 29 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707631):
<div class="codehilite"><pre><span></span><span class="n">subtype</span><span class="bp">.</span><span class="n">metric_space</span> <span class="o">:</span>
  <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">metric_space</span> <span class="n">α</span><span class="o">],</span> <span class="n">metric_space</span> <span class="o">(</span><span class="n">subtype</span> <span class="n">p</span><span class="o">)</span>
</pre></div>


<p>problematic instance</p>

#### [ Kenny Lau (Dec 29 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707791):
<div class="codehilite"><pre><span></span><span class="n">orderable_topology</span><span class="bp">.</span><span class="n">t2_space</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">orderable_topology</span> <span class="n">α</span><span class="o">],</span>
    <span class="n">t2_space</span> <span class="n">α</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">ordered_topology</span><span class="bp">.</span><span class="n">to_t2_space</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">ordered_topology</span> <span class="n">α</span><span class="o">],</span>
    <span class="n">t2_space</span> <span class="n">α</span>
</pre></div>


<p>Lean got stuck trying these two</p>

#### [ Kenny Lau (Dec 29 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707797):
<p>because R has like 10000 properties</p>

#### [ Kenny Lau (Dec 29 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707804):
<p>and the typeclass instance system is not clever enough</p>

#### [ Kenny Lau (Dec 29 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152707852):
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">0</span><span class="o">]</span> <span class="n">orderable_topology</span><span class="bp">.</span><span class="n">t2_space</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">0</span><span class="o">]</span> <span class="n">ordered_topology</span><span class="bp">.</span><span class="n">to_t2_space</span>
</pre></div>


<p>putting these two lines before the lemma is one solution <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span></p>

#### [ Sebastien Gouezel (Dec 29 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152708153):
<p>This works perfectly (and also in my use case, which involves subtypes of something more complicated than R). Thanks a lot! Could you tell us how you located the problematic instances?</p>

#### [ Kenny Lau (Dec 29 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152708162):
<p>I just... read through the instance trace</p>

#### [ Sebastien Gouezel (Dec 29 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152708502):
<p>Just to be sure: before the statement of the lemma, I insert</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">class_instances</span> <span class="n">true</span>
<span class="kn">set_option</span> <span class="n">class</span><span class="bp">.</span><span class="n">instance_max_depth</span> <span class="mi">15</span>
</pre></div>


<p>(the second line to ensure that the process terminates in a reasonable amount of time, the first one to get access to the trace). Then if I put the cursor on <code>apply_instance</code>, I get access to the trace. There, I can see indeed a lot of <code>@orderable_topology ↥s</code>. And I can see at depth (0) that it tries <code>@orderable_topology.t2_space</code>, and gets stuck there. OK, thanks again, I think I will be able to do this by myself next time.</p>

#### [ Mario Carneiro (Dec 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152715634):
<p>Not sure I get what the problem is. Is the <code>orderable_topology.t2_space</code> a wrong turn for the typeclass inference? I guess R is an orderable topology so I don't see the problem</p>

#### [ Mario Carneiro (Dec 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152715681):
<p>Although I guess <code>ordered_topology.to_t2_space</code> implies <code>orderable_topology.t2_space</code></p>

#### [ Reid Barton (Dec 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152715853):
<p>I think I had the same issue at <a href="#narrow/stream/116395-maths/subject/t2_space/near/147451283" title="#narrow/stream/116395-maths/subject/t2_space/near/147451283">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/t2_space/near/147451283</a></p>

#### [ Sebastien Gouezel (Dec 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152716158):
<p>I don't understand what is going on. The trace output is filled with entries like</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_4</span> <span class="o">:</span> <span class="bp">@</span><span class="n">orderable_topology</span> <span class="err">↥</span><span class="n">s</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="err">↥</span><span class="n">s</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">metric_space</span><span class="bp">.</span><span class="n">to_uniform_space&#39;</span> <span class="err">↥</span><span class="n">s</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">metric_space</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">metric_space</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span>
           <span class="o">(</span><span class="bp">@</span><span class="n">normed_group</span><span class="bp">.</span><span class="n">to_metric_space</span> <span class="n">ℝ</span>
              <span class="o">(</span><span class="bp">@</span><span class="n">normed_space</span><span class="bp">.</span><span class="n">to_normed_group</span> <span class="n">ℝ</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">normed_field</span>
                 <span class="o">(</span><span class="bp">@</span><span class="n">normed_field</span><span class="bp">.</span><span class="n">to_normed_space</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">normed_field</span><span class="o">))))))</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">linear_order</span><span class="bp">.</span><span class="n">to_partial_order</span> <span class="err">↥</span><span class="n">s</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">linear_order</span> <span class="n">ℝ</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">linear_ordered_semiring</span><span class="bp">.</span><span class="n">to_linear_order</span> <span class="n">ℝ</span>
           <span class="o">(</span><span class="bp">@</span><span class="n">decidable_linear_ordered_semiring</span><span class="bp">.</span><span class="n">to_linear_ordered_semiring</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">decidable_linear_ordered_semiring</span><span class="o">))</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)))</span> <span class="o">:=</span> <span class="n">ennreal</span><span class="bp">.</span><span class="n">orderable_topology</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
</pre></div>


<p>or</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_4</span> <span class="o">:</span> <span class="bp">@</span><span class="n">orderable_topology</span> <span class="err">↥</span><span class="n">s</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="err">↥</span><span class="n">s</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">metric_space</span><span class="bp">.</span><span class="n">to_uniform_space&#39;</span> <span class="err">↥</span><span class="n">s</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">metric_space</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">metric_space</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span>
           <span class="o">(</span><span class="bp">@</span><span class="n">normed_group</span><span class="bp">.</span><span class="n">to_metric_space</span> <span class="n">ℝ</span>
              <span class="o">(</span><span class="bp">@</span><span class="n">normed_space</span><span class="bp">.</span><span class="n">to_normed_group</span> <span class="n">ℝ</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">normed_field</span>
                 <span class="o">(</span><span class="bp">@</span><span class="n">normed_field</span><span class="bp">.</span><span class="n">to_normed_space</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">normed_field</span><span class="o">))))))</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">linear_order</span><span class="bp">.</span><span class="n">to_partial_order</span> <span class="err">↥</span><span class="n">s</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">linear_order</span> <span class="n">ℝ</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">decidable_linear_order</span><span class="bp">.</span><span class="n">to_linear_order</span> <span class="n">ℝ</span>
           <span class="o">(</span><span class="bp">@</span><span class="n">conditionally_complete_linear_order</span><span class="bp">.</span><span class="n">to_decidable_linear_order</span> <span class="n">ℝ</span>
              <span class="n">real</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">conditionally_complete_linear_order</span><span class="o">))</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)))</span> <span class="o">:=</span> <span class="n">ennreal</span><span class="bp">.</span><span class="n">orderable_topology</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
</pre></div>


<p>or</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_4</span> <span class="o">:</span> <span class="bp">@</span><span class="n">orderable_topology</span> <span class="err">↥</span><span class="n">s</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="err">↥</span><span class="n">s</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">metric_space</span><span class="bp">.</span><span class="n">to_uniform_space&#39;</span> <span class="err">↥</span><span class="n">s</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">metric_space</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">metric_space</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span>
           <span class="o">(</span><span class="bp">@</span><span class="n">normed_group</span><span class="bp">.</span><span class="n">to_metric_space</span> <span class="n">ℝ</span>
              <span class="o">(</span><span class="bp">@</span><span class="n">normed_ring</span><span class="bp">.</span><span class="n">to_normed_group</span> <span class="n">ℝ</span> <span class="o">(</span><span class="bp">@</span><span class="n">normed_field</span><span class="bp">.</span><span class="n">to_normed_ring</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">normed_field</span><span class="o">))))))</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">linear_order</span><span class="bp">.</span><span class="n">to_partial_order</span> <span class="err">↥</span><span class="n">s</span>
     <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">linear_order</span> <span class="n">ℝ</span>
        <span class="o">(</span><span class="bp">@</span><span class="n">linear_ordered_semiring</span><span class="bp">.</span><span class="n">to_linear_order</span> <span class="n">ℝ</span>
           <span class="o">(</span><span class="bp">@</span><span class="n">linear_ordered_ring</span><span class="bp">.</span><span class="n">to_linear_ordered_semiring</span> <span class="n">ℝ</span>
              <span class="o">(</span><span class="bp">@</span><span class="n">linear_ordered_field</span><span class="bp">.</span><span class="n">to_linear_ordered_ring</span> <span class="n">ℝ</span>
                 <span class="o">(</span><span class="bp">@</span><span class="n">discrete_linear_ordered_field</span><span class="bp">.</span><span class="n">to_linear_ordered_field</span> <span class="n">ℝ</span> <span class="n">real</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span><span class="o">))))</span>
        <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)))</span> <span class="o">:=</span> <span class="n">ennreal</span><span class="bp">.</span><span class="n">orderable_topology</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
</pre></div>


<p>All of them are subtly different. There are so many ways to use the different structures on ℝ that it gives rise to an exponential blowup. And, while lean has not checked that all the possibilities fail, it will not go and try a more successful path.</p>

#### [ Kenny Lau (Dec 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152716218):
<p>surely depth-first search is troublesome... but that doesn't mean breadth-first search would have no problems</p>

#### [ Mario Carneiro (Dec 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152716611):
<p>aha, even though R is an orderable topology its subspaces aren't necessarily</p>

#### [ Mario Carneiro (Dec 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20classes%20debugging/near/152716666):
<p>I think the <code>top_space</code> and <code>linear_order</code> arguments should be implicit in the two <code>t2_space</code> instances</p>


{% endraw %}
