---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/68348Liealgebras.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Lie algebras](https://leanprover-community.github.io/archive/116395maths/68348Liealgebras.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jun 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997275):
<p>I am completely stuck on the sorried definition. Is this just to ambitious at the moment?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">module</span>

<span class="n">class</span> <span class="n">has_bracket</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">bracket</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span><span class="o">[</span><span class="bp">`</span> <span class="n">a</span> <span class="bp">`</span><span class="o">,</span><span class="bp">`</span> <span class="n">b</span> <span class="bp">`</span><span class="o">]</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">has_bracket</span><span class="bp">.</span><span class="n">bracket</span> <span class="n">a</span> <span class="n">b</span>

<span class="n">class</span> <span class="n">lie_algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="err">𝔤</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">extends</span> <span class="n">module</span> <span class="n">R</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">has_bracket</span> <span class="err">𝔤</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">left_linear</span>  <span class="o">:=</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">is_linear_map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]))</span>
<span class="o">(</span><span class="n">right_linear</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">is_linear_map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]))</span>
<span class="o">(</span><span class="n">alternating</span>  <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">x</span><span class="o">]</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">Jacobi_identity</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,[</span><span class="n">y</span><span class="o">,</span><span class="n">z</span><span class="o">]]</span> <span class="bp">+</span> <span class="o">[</span><span class="n">z</span><span class="o">,[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]]</span> <span class="bp">+</span> <span class="o">[</span><span class="n">y</span><span class="o">,[</span><span class="n">z</span><span class="o">,</span><span class="n">x</span><span class="o">]]</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">anti_comm</span>    <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]</span> <span class="bp">=</span> <span class="bp">-</span><span class="o">([</span><span class="n">y</span><span class="o">,</span><span class="n">x</span><span class="o">]))</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ri</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="err">𝔤</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">la</span> <span class="o">:</span> <span class="n">lie_algebra</span> <span class="n">R</span> <span class="err">𝔤</span><span class="o">]</span>
<span class="n">include</span> <span class="n">ri</span> <span class="n">la</span>

<span class="kn">section</span> <span class="n">from_ring</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">S</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">}</span>  <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">commutator_bracket</span> <span class="o">:</span> <span class="n">has_bracket</span> <span class="n">S</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="bp">*</span><span class="n">y</span> <span class="bp">-</span> <span class="n">y</span><span class="bp">*</span><span class="n">x</span><span class="bp">⟩</span>

<span class="kn">definition</span> <span class="n">ring</span><span class="bp">.</span><span class="n">to_lie_algebra</span> <span class="o">:</span> <span class="n">lie_algebra</span> <span class="n">R</span> <span class="n">S</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="c1">-- { sorry,</span>
<span class="c1">--   ..ring.to_module }</span>

<span class="kn">end</span> <span class="n">from_ring</span>
</pre></div>

#### [ Kevin Buzzard (Jun 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997433):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">ring</span><span class="bp">.</span><span class="n">to_lie_algebra</span> <span class="o">:</span> <span class="n">lie_algebra</span> <span class="n">R</span> <span class="n">S</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">constructor</span><span class="o">,</span> <span class="c1">-- fails</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997434):
<p>I am a bit surprised about this.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997547):
<p><code>{}</code> is more instructive</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997549):
<p>It says it can't prove <code>module R S</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997556):
<p>which is fair enough because you never mentioned <code>f</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997636):
<p>and <code>ring.to_module</code> is only the statement that <code>R</code> is an <code>R</code>-module</p>

#### [ Johan Commelin (Jun 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997692):
<p>Right. Thanks a lot!</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997693):
<p>I think when I was in your position a few months ago, wrestling with the type class inference system (but in a much less complex situation) Sebastian just pointed out that I could over-ride everything.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997709):
<p>so I would just go and make my own explicit instances of everything</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997714):
<p>and this got me a bit further</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997734):
<p>I guess <code>constructor</code> doesn't work because it didn't even get round to thinking about how to construct the extra fields, it just gets hung up with the fact that it can't even make the extension</p>

#### [ Johan Commelin (Jun 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997822):
<p>Ok, so I've got a proof of <code>module R S</code>. How do I feed it to the system?</p>

#### [ Johan Commelin (Jun 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997830):
<p>Because <code>@lie_algebra</code> is not interested in such a proof...</p>

#### [ Johan Commelin (Jun 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997887):
<p>Is the <code>extends module R _</code> giving me trouble? Does that <code>extends</code> imply that it wants do deduce the module structure by type class inference?</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997963):
<p>I used to ask this sort of question all the time. If you search for type class woes you'll find my thread where I asked about 10 questions of this nature.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127998035):
<p>Unfortunately I can't keep all the answers in my head and I still have not found the time to go through that thread and write down all the tips in a proper doc</p>

#### [ Johan Commelin (Jun 13 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127998455):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Misa stupid! In the definition of the class I shouldn't use <code>:=</code> but <code>:</code> for the axioms... it should be</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">lie_algebra</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="err">𝔤</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">extends</span> <span class="n">module</span> <span class="n">R</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">has_bracket</span> <span class="err">𝔤</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">left_linear</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">is_linear_map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]))</span>
<span class="o">(</span><span class="n">right_linear</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="n">is_linear_map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]))</span>
<span class="o">(</span><span class="n">alternating</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">x</span><span class="o">]</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">Jacobi_identity</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,[</span><span class="n">y</span><span class="o">,</span><span class="n">z</span><span class="o">]]</span> <span class="bp">+</span> <span class="o">[</span><span class="n">z</span><span class="o">,[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]]</span> <span class="bp">+</span> <span class="o">[</span><span class="n">y</span><span class="o">,[</span><span class="n">z</span><span class="o">,</span><span class="n">x</span><span class="o">]]</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">anti_comm</span>    <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="err">𝔤</span><span class="o">,</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span><span class="n">y</span><span class="o">]</span> <span class="bp">=</span> <span class="bp">-</span><span class="o">([</span><span class="n">y</span><span class="o">,</span><span class="n">x</span><span class="o">]))</span>
</pre></div>


<p>That messed up everything. Now that I've fixed it, all of a sudden problems vanish!</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127999527):
<p>Oh yeah. Sorry, I should have caught that.</p>

#### [ Johan Commelin (Jun 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000028):
<p>Yoohoo!</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">from_ring</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">S</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">}</span>  <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
<span class="kn">variable</span>  <span class="o">{</span><span class="n">central</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">),</span> <span class="n">f</span><span class="o">(</span><span class="n">r</span><span class="o">)</span> <span class="bp">*</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">f</span><span class="o">(</span><span class="n">r</span><span class="o">)}</span>

<span class="kn">instance</span> <span class="n">commutator_bracket</span> <span class="o">:</span> <span class="n">has_bracket</span> <span class="n">S</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="bp">*</span><span class="n">y</span> <span class="bp">-</span> <span class="n">y</span><span class="bp">*</span><span class="n">x</span><span class="bp">⟩</span>

<span class="n">include</span> <span class="n">central</span>
<span class="kn">definition</span> <span class="n">ring</span><span class="bp">.</span><span class="n">to_lie_algebra</span> <span class="o">:</span> <span class="n">lie_algebra</span> <span class="n">R</span> <span class="n">S</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">left_linear</span>  <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">intro</span> <span class="n">y</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">commutator_bracket</span><span class="o">],</span>
    <span class="n">constructor</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">x₁</span> <span class="n">x₂</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">left_distrib</span><span class="o">,</span><span class="n">right_distrib</span><span class="o">,</span><span class="n">mul_assoc</span><span class="o">]</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">r</span> <span class="n">x</span><span class="o">,</span>
      <span class="k">show</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">+</span> <span class="bp">-</span><span class="o">(</span><span class="n">y</span> <span class="bp">*</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">x</span><span class="o">))</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">+</span> <span class="bp">-</span><span class="o">(</span><span class="n">y</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)),</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">left_distrib</span><span class="o">,</span><span class="n">right_distrib</span><span class="o">,</span><span class="n">mul_assoc</span><span class="o">,</span><span class="n">central</span><span class="o">]</span> <span class="o">}</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">right_linear</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">commutator_bracket</span><span class="o">],</span>
    <span class="n">constructor</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">x₁</span> <span class="n">x₂</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">left_distrib</span><span class="o">,</span><span class="n">right_distrib</span><span class="o">,</span><span class="n">mul_assoc</span><span class="o">]</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">r</span> <span class="n">y</span><span class="o">,</span>
      <span class="k">show</span> <span class="n">x</span> <span class="bp">*</span> <span class="o">(</span><span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">+</span> <span class="bp">-</span><span class="o">(</span><span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">*</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">+</span> <span class="bp">-</span><span class="o">(</span><span class="n">y</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)),</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">left_distrib</span><span class="o">,</span><span class="n">right_distrib</span><span class="o">,</span><span class="n">mul_assoc</span><span class="o">,</span><span class="n">central</span><span class="o">]</span> <span class="o">}</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">alternating</span>  <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">commutator_bracket</span><span class="o">],</span>
    <span class="n">simp</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">Jacobi_identity</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">commutator_bracket</span><span class="o">],</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">left_distrib</span><span class="o">,</span><span class="n">right_distrib</span><span class="o">,</span><span class="n">mul_assoc</span><span class="o">],</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">anti_comm</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">commutator_bracket</span><span class="o">],</span>
    <span class="n">simp</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="bp">..</span><span class="n">restriction_of_scalars</span><span class="bp">.</span><span class="n">restriction_of_scalars</span> <span class="n">f</span> <span class="n">S</span>
<span class="o">}</span>

<span class="kn">end</span> <span class="n">from_ring</span>
</pre></div>

#### [ Johan Commelin (Jun 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000036):
<p>I like <code>simp</code>!</p>

#### [ Johan Commelin (Jun 13 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000082):
<p>It's a pity I can't use <code>ring</code> because I'm not in a commutative setting...</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000416):
<blockquote>
<p>It's a pity I can't use <code>ring</code> because I'm not in a commutative setting...</p>
</blockquote>
<p>I can tell you how to write the non-commutative version :-)</p>

#### [ Johan Commelin (Jun 13 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000429):
<p>Lol</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000435):
<p>actually there would be an issue</p>

#### [ Johan Commelin (Jun 13 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000446):
<p>Yes, I wouldn't be surprised if commutativity is essential [also: lunch]</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000491):
<p>There's even an issue with my baby ring tactic -- one needs to be able to put every polynomial into a "canonical form", so that two polynomials (e.g. x^2+1 and 0*x^3+x^2+1) are equal if and only if their canonical forms are equal.</p>

#### [ Chris Hughes (Jun 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000502):
<p>Make your polynomials a subtype, with a proof that the leading coeff is not zero</p>

#### [ Chris Hughes (Jun 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000509):
<p>Like finsets.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000510):
<p>In my baby ring tactic this isn't even present (yet). In the grown-up ring tactic Mario uses Gregoire-Mahboubi's strategy of writing everything in "horner form" because this is much more efficient for sparse polys</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000519):
<p>but in the non-comm case you would have to figure out a canonical form I guess, at least if you wanted to maximise the chance that the tactic worked.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000560):
<p>Chris -- this doesn't work for zero</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000566):
<p>I was going to go for the following:</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000571):
<p>either an empty list, or a non-empty list with last element non-zero</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000588):
<p>One would have to check non-zero-ness in the ground ring (which might be Z/2Z)</p>

#### [ Chris Hughes (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000589):
<p>What's the last element function?</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000593):
<p>I've seen one before</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000595):
<p>I've seen an n'th element function somewhere in list.lean</p>

#### [ Chris Hughes (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000596):
<p>How does it habdle the empty list? If it's option you're okay.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000599):
<p>unsurprisingly, there are all sorts of variants</p>

#### [ Kevin Buzzard (Jun 13 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000646):
<p>e.g. one which asks for a proof that n &lt; length before giving you a non-option n'th element</p>

#### [ Chris Hughes (Jun 13 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000696):
<p><code>list.head'</code> looks like the best one, depending on the order of your lists.</p>


{% endraw %}
