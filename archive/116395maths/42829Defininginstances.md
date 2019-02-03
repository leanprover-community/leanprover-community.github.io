---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/42829Defininginstances.html
---

## Stream: [maths](index.html)
### Topic: [Defining instances](42829Defininginstances.html)

---


{% raw %}
#### [ Sebastien Gouezel (Oct 13 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135736954):
<p>I am trying to define an instance of a normed space starting from a norm satisfying the right axioms, but I would need some help. Here is the situation:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">normed_group_of_norm</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">a</span><span class="o">:</span> <span class="n">add_comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">b</span><span class="o">:</span> <span class="n">has_norm</span> <span class="n">α</span><span class="o">]</span>
<span class="o">(</span><span class="n">norm_triangle</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span> <span class="n">y</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">norm</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">norm</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">norm</span> <span class="n">y</span><span class="o">)</span>
<span class="o">(</span><span class="n">norm_zero</span> <span class="o">:</span> <span class="n">norm</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">eq_of_norm_eq_zero</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">),</span> <span class="n">norm</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">norm_neg</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">),</span> <span class="n">norm</span> <span class="o">(</span><span class="bp">-</span><span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">norm</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">normed_group</span> <span class="n">α</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">A</span><span class="o">:</span> <span class="n">metric_space</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">metric_space</span><span class="bp">.</span><span class="n">mk&#39;&#39;</span>
<span class="o">{</span> <span class="n">dist</span> <span class="o">:=</span> <span class="bp">λ</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">norm</span> <span class="o">(</span><span class="n">x</span> <span class="bp">-</span> <span class="n">y</span><span class="o">),</span>
  <span class="n">dist_self</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">norm_zero</span><span class="o">],</span>
  <span class="n">eq_of_dist_eq_zero</span> <span class="o">:=</span> <span class="bp">λ</span><span class="n">x</span> <span class="n">y</span> <span class="n">hxy</span><span class="o">,</span> <span class="n">sub_eq_zero</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">eq_of_norm_eq_zero</span> <span class="bp">_</span> <span class="n">hxy</span><span class="o">),</span>
  <span class="n">dist_comm</span> <span class="o">:=</span> <span class="bp">λ</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="k">begin</span> <span class="k">have</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">norm_neg</span> <span class="o">(</span><span class="n">x</span><span class="bp">-</span><span class="n">y</span><span class="o">),</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">A</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">A</span><span class="bp">.</span><span class="n">symm</span><span class="o">]</span> <span class="kn">end</span><span class="o">,</span>
  <span class="n">dist_triangle</span> <span class="o">:=</span><span class="bp">λ</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">norm_triangle</span> <span class="o">(</span><span class="n">x</span><span class="bp">-</span><span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">-</span><span class="n">z</span><span class="o">)</span>
<span class="o">},</span>
<span class="o">{</span>
   <span class="n">dist_eq</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
    <span class="bp">..</span><span class="n">a</span><span class="o">,</span> <span class="bp">..</span><span class="n">b</span><span class="o">,</span> <span class="bp">..</span><span class="n">A</span>
<span class="o">}</span>
</pre></div>


<p>A normed group is an abelian group together with a norm, with the property that the distance should be given by <code>dist x y = norm(x-y)</code>. It extends metric spaces, so I first define the metric space structure I want (<code>A</code> above), and then I just have to check this equality, which is by definition of <code>A</code>. But I do not see how to get access to the formula in the definition of <code>A</code>, so I am stuck...</p>

#### [ Kenny Lau (Oct 13 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135736958):
<p>don't we already have this?</p>

#### [ Sebastien Gouezel (Oct 13 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135737005):
<p>No, I don't think so. Normed groups are defined in <code>analysis/normed_space.lean</code>, but there is no constructor just in terms of a norm.</p>

#### [ Kenny Lau (Oct 13 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135737063):
<p>is there anything about <code>abs</code>?</p>

#### [ Sebastien Gouezel (Oct 13 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135737111):
<p>My question is not specifically about this situation, it is rather that there is something I don't know about the syntax or the way to access fields.</p>

#### [ Kenny Lau (Oct 13 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135737157):
<p>(maybe unrelated) I recall there's no wrapper for <code>norm_mul</code></p>

#### [ Sebastien Gouezel (Oct 13 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135737621):
<p>Here is the same question in a completely basic setting:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">my_test</span> <span class="o">:=</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">foo</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">A</span> <span class="o">:</span> <span class="n">my_test</span> <span class="o">:=</span> <span class="o">{</span><span class="n">f</span> <span class="o">:=</span> <span class="bp">λ</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="o">},</span>
<span class="k">have</span> <span class="n">B</span><span class="o">:</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">A</span><span class="bp">.</span><span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">intros</span> <span class="n">x</span><span class="o">,</span> <span class="n">sorry</span> <span class="kn">end</span><span class="o">,</span>
<span class="n">trivial</span>
</pre></div>


<p>I just want to get access to the definition of the field <code>f</code> in the structure I have constructed.</p>

#### [ Kenny Lau (Oct 13 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135737675):
<p>that isn't possible because <code>have</code> doesn't store data</p>

#### [ Johannes Hölzl (Oct 13 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135737677):
<p>Yes: you need to use <code>let m : metric_space A := ...</code> instead of the <code>have</code></p>

#### [ Sebastien Gouezel (Oct 13 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135737679):
<p>Thanks!</p>

#### [ Patrick Massot (Oct 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738014):
<p>Sébastien, I'm not sure I understand your question, but <a href="https://github.com/leanprover/mathlib/blob/master/analysis/normed_space.lean#L276" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/normed_space.lean#L276">https://github.com/leanprover/mathlib/blob/master/analysis/normed_space.lean#L276</a> does define a normed stuff instance explicitly</p>

#### [ Sebastien Gouezel (Oct 13 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738272):
<p>Yes, but the metric space structure had already been defined before on \R. I am maximally lazy here: starting just from the norm, I want to define simultaneously the metric space and the normed space. In the same way, when you have a distance, you don't want to define by hand the topological structure, then the uniform structure, then the metric space structure: you want a constructor that does all this for you.</p>

#### [ Sebastien Gouezel (Oct 13 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738327):
<p>And it works perfectly thanks to the hints of Kenny and Johannes:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">normed_group</span><span class="bp">.</span><span class="n">core</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_norm</span> <span class="n">α</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">norm_triangle</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span> <span class="n">y</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">norm</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">norm</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">norm</span> <span class="n">y</span><span class="o">)</span>
<span class="o">(</span><span class="n">norm_zero</span> <span class="o">:</span> <span class="n">norm</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">eq_of_norm_eq_zero</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">),</span> <span class="n">norm</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">norm_neg</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">),</span> <span class="n">norm</span> <span class="o">(</span><span class="bp">-</span><span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">norm</span> <span class="n">x</span><span class="o">)</span>

<span class="n">def</span> <span class="n">normed_group_of_norm</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">a</span><span class="o">:</span> <span class="n">add_comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">b</span><span class="o">:</span> <span class="n">has_norm</span> <span class="n">α</span><span class="o">]</span>
<span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">normed_group</span><span class="bp">.</span><span class="n">core</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">normed_group</span> <span class="n">α</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">A</span> <span class="o">:</span> <span class="n">metric_space</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">metric_space</span><span class="bp">.</span><span class="n">mk&#39;&#39;</span>
<span class="o">{</span> <span class="n">dist</span> <span class="o">:=</span> <span class="bp">λ</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">norm</span> <span class="o">(</span><span class="n">x</span> <span class="bp">-</span> <span class="n">y</span><span class="o">),</span>
  <span class="n">dist_self</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">m</span><span class="bp">.</span><span class="n">norm_zero</span><span class="o">],</span>
  <span class="n">eq_of_dist_eq_zero</span> <span class="o">:=</span> <span class="bp">λ</span><span class="n">x</span> <span class="n">y</span> <span class="n">hxy</span><span class="o">,</span> <span class="n">sub_eq_zero</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">m</span><span class="bp">.</span><span class="n">eq_of_norm_eq_zero</span> <span class="bp">_</span> <span class="n">hxy</span><span class="o">),</span>
  <span class="n">dist_comm</span> <span class="o">:=</span> <span class="bp">λ</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="k">begin</span> <span class="k">have</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">m</span><span class="bp">.</span><span class="n">norm_neg</span> <span class="o">(</span><span class="n">x</span><span class="bp">-</span><span class="n">y</span><span class="o">),</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">A</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">A</span><span class="bp">.</span><span class="n">symm</span><span class="o">]</span> <span class="kn">end</span><span class="o">,</span>
  <span class="n">dist_triangle</span> <span class="o">:=</span><span class="bp">λ</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">m</span><span class="bp">.</span><span class="n">norm_triangle</span> <span class="o">(</span><span class="n">x</span><span class="bp">-</span><span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">-</span><span class="n">z</span><span class="o">)</span>
<span class="o">}</span> <span class="k">in</span>
<span class="o">{</span> <span class="n">dist_eq</span> <span class="o">:=</span> <span class="bp">λ</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="bp">..</span><span class="n">a</span><span class="o">,</span> <span class="bp">..</span><span class="n">b</span><span class="o">,</span> <span class="bp">..</span><span class="n">A</span>
<span class="o">}</span>
</pre></div>


<p>(Don't try this, it depends on my emetric spaces pull request for the metric space constructor)</p>

#### [ Kenny Lau (Oct 13 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738347):
<p>I would define the metric space separately first</p>

#### [ Kenny Lau (Oct 13 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738348):
<p>and avoid <code>let</code></p>

#### [ Kenny Lau (Oct 13 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738385):
<p>if you still want to keep it, I would add <code>set_option zeta.compiler true</code></p>

#### [ Johan Commelin (Oct 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738400):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> The <code>let</code> statements aren't parsed away, they go all the way down to the kernel. Sometimes I wish there was a "syntactic sugar" variant, maybe called <code>where</code>.</p>

#### [ Johan Commelin (Oct 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738402):
<p>But like Kenny suggests, you might want to split it up any way.</p>

#### [ Sebastien Gouezel (Oct 13 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738462):
<p>How would you avoid the <code>let</code>? I insist on having one single constructor that takes a <code>normed_group.core</code> and gives a normed group, that's really the point here.</p>

#### [ Johan Commelin (Oct 13 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738665):
<p>This constructor could call another one, right?</p>

#### [ Johan Commelin (Oct 13 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738711):
<p>If you just factor out the <code>let</code>-statement into a separate <code>instance</code>. Or am I missing something?</p>

#### [ Johan Commelin (Oct 13 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20instances/near/135738727):
<p>Maybe some <code>refine_struct</code> magic could also help. But I'm not an expert on this.</p>


{% endraw %}
