---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01495Defininginverseasapartialfunction.html
---

## Stream: [general](index.html)
### Topic: [Defining inverse as a partial function.](01495Defininginverseasapartialfunction.html)

---


{% raw %}
#### [ Edward Ayers (Nov 01 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914681):
<p>I am investigating defining field inverses so that you have to also give the inverse a certificate that the number being put in is not zero. We can have a separate debate about whether that approach is better than having <code>inv(0) = 0</code>, but for now here are my ideas:</p>
<p>My first idea was to treat the 'non-zeroness' as a typeclass then piggyback on the type inference algorithm.</p>
<div class="codehilite"><pre><span></span>    <span class="kn">universe</span> <span class="n">u</span>
    <span class="n">class</span> <span class="n">not_zero</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">nz</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span>
    <span class="n">class</span> <span class="n">my_division_ring</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="o">(</span><span class="n">ring</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
    <span class="o">(</span><span class="n">inv</span><span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">x</span><span class="o">]:</span>  <span class="n">R</span><span class="o">)</span>
    <span class="o">(</span><span class="n">inv_l</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">y</span><span class="o">],</span> <span class="n">y</span> <span class="bp">*</span> <span class="o">(</span><span class="n">inv</span> <span class="n">y</span><span class="o">)</span>  <span class="bp">=</span> <span class="mi">1</span> <span class="o">)</span>
    <span class="o">(</span><span class="n">inv_r</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">y</span><span class="o">],</span> <span class="o">(</span><span class="n">inv</span> <span class="n">y</span><span class="o">)</span> <span class="bp">*</span> <span class="n">y</span>  <span class="bp">=</span> <span class="mi">1</span> <span class="o">)</span>
</pre></div>


<p>Sadly, I get a "failed to synthesize typeclass" error.<br>
Even more sadly, the last two lines of the error read:</p>
<div class="codehilite"><pre><span></span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">not_zero</span> <span class="n">y</span>
<span class="err">⊢</span> <span class="n">not_zero</span> <span class="n">y</span>
</pre></div>


<p>Why is the elaborator not spotting this? This seems like something the elaborator would be able to do. Supposing that the elaborator could do this, then my idea was that you could write things like:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">integral_domain</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">y</span><span class="o">]</span> <span class="o">:</span> <span class="n">not_zero</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>


<p>Are there any roadblocks that are stopping this dream from being a feasible way of defining the inverse function?</p>

#### [ Johan Commelin (Nov 01 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914772):
<p>Can this be solved with the <code>haveI</code> magic inserting the instance into the type class system at the right points?</p>

#### [ Edward Ayers (Nov 01 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914794):
<p>My second approach was to use auto_params:</p>
<div class="codehilite"><pre><span></span>    <span class="c1">-- eventually a sophisticated tactic that figures out if an elt is ≠ 0</span>
    <span class="n">meta</span> <span class="n">def</span> <span class="n">nz_tactic</span> <span class="o">:=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span>
    <span class="n">class</span> <span class="n">dvr</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="o">(</span><span class="n">ring</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
    <span class="o">(</span><span class="n">inv</span><span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">):</span>  <span class="n">R</span><span class="o">)</span>
    <span class="o">(</span><span class="n">inv_l</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">y</span><span class="bp">≠</span><span class="mi">0</span><span class="o">),</span> <span class="n">x</span> <span class="bp">*</span> <span class="o">(</span><span class="n">inv</span> <span class="n">y</span> <span class="n">p</span><span class="o">)</span>  <span class="bp">=</span> <span class="mi">1</span> <span class="o">)</span>
    <span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">dvr</span> <span class="n">R</span><span class="o">]</span>
    <span class="n">def</span> <span class="n">inv</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">nz</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">.</span> <span class="n">nz_tactic</span><span class="o">)</span> <span class="o">:</span> <span class="n">R</span> <span class="o">:=</span> <span class="n">dvr</span><span class="bp">.</span><span class="n">inv</span> <span class="n">y</span> <span class="n">nz</span>

    <span class="n">def</span> <span class="n">div</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">nz</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">.</span> <span class="n">nz_tactic</span><span class="o">)</span> <span class="o">:</span> <span class="n">R</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">*</span> <span class="o">(</span><span class="n">inv</span> <span class="n">y</span><span class="o">)</span>
    <span class="kn">infix</span> <span class="bp">`</span> <span class="bp">/.</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">div</span>

    <span class="kn">variables</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span>
    <span class="kn">variable</span> <span class="o">(</span><span class="n">xz</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">.</span> <span class="n">nz_tactic</span><span class="o">)</span> <span class="c1">-- I was really hoping that this would be allowed</span>

    <span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">xz</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">yz</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/.</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/.</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/.</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Edward Ayers (Nov 01 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914838):
<blockquote>
<p>Can this be solved with the <code>haveI</code> magic inserting the instance into the type class system at the right points?</p>
</blockquote>
<p>I don't understand what this means.</p>

#### [ Johan Commelin (Nov 01 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914840):
<p>Neither do I.</p>

#### [ Johan Commelin (Nov 01 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914853):
<p>The point is that the problem you described pops up quite often.</p>

#### [ Johan Commelin (Nov 01 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914861):
<p>And then you can write <code>haveI my_instance, blah</code> and then the type class system will pick up your instance.</p>

#### [ Johan Commelin (Nov 01 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914867):
<p>And the reason you have to do this explicitly is because Lean 3.4.x is pretty frozen.</p>

#### [ Edward Ayers (Nov 01 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914932):
<p>Please could you give a full example of <code>haveI</code>?</p>

#### [ Edward Ayers (Nov 01 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914948):
<p>I get <code>[Lean] unknown identifier 'haveI'</code> errors</p>

#### [ Johan Commelin (Nov 01 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136914955):
<p>I'll try. For starters, here are 56 examples: <a href="https://github.com/leanprover/mathlib/search?q=haveI&amp;unscoped_q=haveI" target="_blank" title="https://github.com/leanprover/mathlib/search?q=haveI&amp;unscoped_q=haveI">https://github.com/leanprover/mathlib/search?q=haveI&amp;unscoped_q=haveI</a></p>

#### [ Edward Ayers (Nov 01 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915006):
<p>ah it's a tactic</p>

#### [ Johan Commelin (Nov 01 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915020):
<p>Yes, and it has some friends, like <code>exactI</code> and I don't know what they do, and how they differ.</p>

#### [ Johan Commelin (Nov 01 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915021):
<p>I'm using them cargo-cult style.</p>

#### [ Edward Ayers (Nov 01 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915095):
<p>So my question now is: Is there a fundamental reason why the elaborator can't do my above example? Eg there might be cases where it causes the elaborator to take unbounded time or something.</p>

#### [ Johan Commelin (Nov 01 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915157):
<p>I think the fundamental reason was that Lean 3.4.x is frozen.</p>

#### [ Johan Commelin (Nov 01 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915207):
<p>Also, in your <code>inv_l</code> and <code>inv_r</code> you want <code>y = x</code>.</p>

#### [ Edward Ayers (Nov 01 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915310):
<p>That's not what I mean by reason. Why would the elaborator be able to do the below example but not the one at the top.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sq</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>  <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span>
</pre></div>


<p>It must be something to do with the fact that the elaborator is looking for typeclasses attached to the type of <code>a</code> and not to <code>a</code> itself.</p>

#### [ Edward Ayers (Nov 01 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915315):
<blockquote>
<p>Also, in your <code>inv_l</code> and <code>inv_r</code> you want <code>y = x</code>.</p>
</blockquote>
<p>fixed!</p>

#### [ Chris Hughes (Nov 01 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136915660):
<p>I think it;s actually to do with being left or right of the colon. This doesn't work</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">R</span><span class="o">),</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
</pre></div>

#### [ Edward Ayers (Nov 01 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136916579):
<p><code>    (inv_l (x : R) [not_zero x] : (x * (inv x)  = 1) )</code> has the same error though.</p>

#### [ Chris Hughes (Nov 01 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136916787):
<p>Maybe because it's part of a structure. Does the <code>ring</code> example work as part of a structure?</p>

#### [ Edward Ayers (Nov 01 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136916872):
<p>This works:</p>
<div class="codehilite"><pre><span></span>    <span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">my_division_ring</span> <span class="n">R</span><span class="o">]</span>
    <span class="n">def</span> <span class="n">inv</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">y</span><span class="o">]</span> <span class="o">:</span> <span class="n">R</span> <span class="o">:=</span> <span class="n">my_division_ring</span><span class="bp">.</span><span class="n">inv</span> <span class="n">y</span>
</pre></div>

#### [ Edward Ayers (Nov 01 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136916882):
<p>so maybe it is because it is part of a structure.</p>

#### [ Reid Barton (Nov 01 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136919570):
<p><code>by exactI</code> is the most succinct option here</p>

#### [ Edward Ayers (Nov 01 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136921820):
<p>Right but ideally I wouldn't even have to use a tactic.</p>

#### [ Edward Ayers (Nov 01 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136921827):
<p>The elaborator would just do it.</p>

#### [ Edward Ayers (Nov 01 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136923468):
<p>I think that I've got the elaborator to "just do it" now:</p>
<div class="codehilite"><pre><span></span>    <span class="n">class</span> <span class="n">not_zero</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">nz</span><span class="o">:</span><span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span>
    <span class="n">class</span> <span class="n">my_division_ring</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="o">(</span><span class="n">integral_domain</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
    <span class="o">(</span><span class="n">inv</span> <span class="o">:</span> <span class="bp">Π</span><span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">x</span><span class="o">],</span>  <span class="n">R</span><span class="o">)</span>
    <span class="o">(</span><span class="n">inv_l</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">nz</span><span class="o">:</span><span class="n">not_zero</span> <span class="n">x</span><span class="o">]</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">*</span> <span class="o">(</span><span class="bp">@</span><span class="n">inv</span> <span class="n">x</span> <span class="n">nz</span><span class="o">)</span>  <span class="bp">=</span> <span class="mi">1</span> <span class="o">)</span>
    <span class="o">(</span><span class="n">inv_r</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">nz</span><span class="o">:</span><span class="n">not_zero</span> <span class="n">x</span><span class="o">]</span> <span class="o">,</span> <span class="o">(</span><span class="bp">@</span><span class="n">inv</span> <span class="n">x</span> <span class="n">nz</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span>  <span class="bp">=</span> <span class="mi">1</span> <span class="o">)</span>

    <span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">my_division_ring</span> <span class="n">R</span><span class="o">]</span>
    <span class="n">def</span> <span class="n">inv</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">y</span><span class="o">]</span> <span class="o">:</span> <span class="n">R</span> <span class="o">:=</span> <span class="n">my_division_ring</span><span class="bp">.</span><span class="n">inv</span> <span class="n">y</span>

    <span class="n">def</span> <span class="n">div</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">y</span><span class="o">]</span> <span class="o">:</span> <span class="n">R</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">*</span> <span class="o">(</span><span class="n">inv</span> <span class="n">y</span><span class="o">)</span>
    <span class="kn">infix</span> <span class="bp">`</span> <span class="err">÷</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">div</span>

    <span class="kn">variables</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">x</span><span class="o">]</span> <span class="o">[</span><span class="n">not_zero</span> <span class="n">y</span><span class="o">]</span>
    <span class="kn">instance</span> <span class="o">:</span> <span class="n">not_zero</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">mul_ne_zero</span> <span class="o">(</span><span class="n">not_zero</span><span class="bp">.</span><span class="n">nz</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">not_zero</span><span class="bp">.</span><span class="n">nz</span> <span class="n">y</span><span class="o">)</span><span class="bp">⟩</span>

    <span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="err">÷</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="err">÷</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">1</span> <span class="err">÷</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Edward Ayers (Nov 01 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136923562):
<p>So I was badmouthing the elaborator but I only have to be explicit with <code>inv</code> within the class definition.</p>

#### [ Edward Ayers (Nov 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136923605):
<p>I much prefer this approach to making the inverse total.</p>

#### [ Edward Ayers (Nov 01 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136923739):
<p>But it has its own caveats</p>

#### [ Floris van Doorn (Nov 01 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136924201):
<p>One problem you'll run into is that sooner or later type class inference is not going to figure out that arguments are <code>not_zero</code>, because the reasons get too complicated. But if you're fine with writing</p>
<div class="codehilite"><pre><span></span>haveI : not_zero t := ...,
</pre></div>


<p>here and there, it should be fine.</p>

#### [ Edward Ayers (Nov 01 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136925306):
<p>Right. The problem is that the reasons get too complicated, so the elaborator would end up needing to be a general purpose prover. It seems to me that in practice, if a function needs an implicit guard proposition like <code>x != 0</code>, it is usually easy for a human to work out where the certificate is coming from, so it should be possible to make a tactic that can also figure it out 80% of the time. It would be so useful if one were able to augment the elaborator with ones own tactics, similar to the <code>(x:P . my_tactic)</code> syntax, but where I don't have to explicitly write out the tactic name all of the time and one can also write <code>variables {x : R} (x != 0 . my_tactic)</code>. <br>
 I think my ideal syntax would be to extend the typeclass brackets to also take arbitrary propositions.</p>
<div class="codehilite"><pre><span></span>    <span class="n">class</span> <span class="n">my_division_ring</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="o">(</span><span class="n">integral_domain</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
    <span class="o">(</span><span class="n">inv</span> <span class="o">:</span> <span class="bp">Π</span><span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">],</span>  <span class="n">R</span><span class="o">)</span>

    <span class="kn">variables</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">]</span> <span class="o">[</span><span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">]</span>
    <span class="kn">instance</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">mul_ne_zero</span> <span class="err">‹</span><span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="err">›</span> <span class="err">‹</span><span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span><span class="err">›</span>
</pre></div>


<p>I know that there are lots of practical difficulties that this would surface, but I think the idea makes sense. The meaning of <code>[x ≠ 0]</code> is that this is a fact that needs to be present but which should be hidden from the user as much as possible.</p>

#### [ Edward Ayers (Nov 01 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/136925627):
<p>You can already pretend that a proposition is a typeclass, but the elaborator doesn't know what to do with them because they don't have the <code>class</code> attribute on them.</p>

#### [ Simon Hudon (Nov 03 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137113111):
<p>I think you might consider auto params. It allows you to specify a tactic to use to prove non-zeroness</p>

#### [ Simon Hudon (Nov 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137113225):
<p><code>ˋ</code>lean<br>
(inv (x : R) (h : x /= 0 . prove_non_zero) : R)<br>
<code>ˋ</code></p>

#### [ Simon Hudon (Nov 03 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137113286):
<p>(Sorry for the bad formatting, I’m on my phone)</p>

#### [ Reid Barton (Nov 03 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137116158):
<p>Now I'm confused why this code that I found in Scott's limits branch actually does work:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">preserves_limits</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">D</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">preserves</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">J</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">small_category</span> <span class="n">J</span><span class="o">]</span> <span class="o">{</span><span class="n">K</span> <span class="o">:</span> <span class="n">J</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span> <span class="o">:</span> <span class="n">cone</span> <span class="n">K</span><span class="o">},</span> <span class="n">is_limit</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">is_limit</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">map_cone</span> <span class="n">c</span><span class="o">))</span>
</pre></div>

#### [ Reid Barton (Nov 03 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Defining%20inverse%20as%20a%20partial%20function./near/137116198):
<p><code>J \func C</code> depends on the <code>[small_category J]</code>, and if I delete the latter then I get errors.</p>


{% endraw %}
