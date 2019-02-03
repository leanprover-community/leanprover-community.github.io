---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47376freegroup.html
---

## Stream: [general](index.html)
### Topic: [free group](47376freegroup.html)

---


{% raw %}
#### [ Kenny Lau (Apr 01 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124469539):
<p>I have constructed the free group of a set here: <a href="https://github.com/kckennylau/Lean/blob/master/free_group.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/free_group.lean">https://github.com/kckennylau/Lean/blob/master/free_group.lean</a></p>

#### [ Kenny Lau (Apr 01 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124469545):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> what do you think of it?</p>

#### [ Kenny Lau (Apr 01 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124480775):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm onto something. My construction of the <em>real</em> free group is almost done.</p>

#### [ Kenny Lau (Apr 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124481322):
<p><a href="https://github.com/kckennylau/Lean/blob/master/free_group.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/free_group.lean">https://github.com/kckennylau/Lean/blob/master/free_group.lean</a></p>

#### [ Kenny Lau (Apr 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124481323):
<p><a href="https://github.com/leanprover/mathlib/pull/89" target="_blank" title="https://github.com/leanprover/mathlib/pull/89">https://github.com/leanprover/mathlib/pull/89</a></p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493682):
<p>Why not prove the adjoint functor theorem?</p>

#### [ Kenny Lau (Apr 01 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493728):
<p>that construction was my first construction</p>

#### [ Kenny Lau (Apr 01 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493731):
<p>see <a href="#narrow/stream/113488-general/topic/making.20isomorphism.20class.20a.20group" title="#narrow/stream/113488-general/topic/making.20isomorphism.20class.20a.20group">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making.20isomorphism.20class.20a.20group</a> for why it fails</p>

#### [ Kenny Lau (Apr 01 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493781):
<p>unfortunately I rewrote my second construction over my first</p>

#### [ Kenny Lau (Apr 01 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124493783):
<p>so see commit history for the construction from adjoint functor theorem</p>

#### [ Peter Jipsen (Apr 01 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124499636):
<p>Nice construction! Would it be possible to construct the free group directly on an inductive type of the group signature and then quotient by the group axioms (i.e. without using the inverse monoid)?</p>

#### [ Kenny Lau (Apr 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124499786):
<p>I find the divide-and-conquer approach more psychologically comfortable</p>

#### [ Peter Jipsen (Apr 01 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500101):
<p>Sure, I agree with that. Was just wondering how a direct (minimal) construction would compare -- I may try that as an exercise</p>

#### [ Kenny Lau (Apr 01 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500103):
<p>do let me know afterwards! :)</p>

#### [ Mario Carneiro (Apr 01 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500203):
<p>I agree that separating the construction into steps makes it clearer what is happening. Is it possible to use just the second stage to construct the free monoid as well?</p>

#### [ Kenny Lau (Apr 01 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500247):
<p>hmm, I don't know</p>

#### [ Kevin Buzzard (Apr 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500398):
<p>free commutative ring = polynomial ring <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>[</mo><mi>S</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">\mathbb{Z}[S]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500404):
<p>might be a nice way to think about it</p>

#### [ Kenny Lau (Apr 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500405):
<p>feel free to construct it ^^</p>

#### [ Kevin Buzzard (Apr 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500408):
<p>did you prove the adjoint functor theorem yet? ;-)</p>

#### [ Kenny Lau (Apr 01 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/124500452):
<p>heh</p>

#### [ Kenny Lau (Apr 17 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187323):
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>

<span class="kn">inductive</span> <span class="n">rel</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">L</span> <span class="n">L</span>
<span class="bp">|</span> <span class="n">symm</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span><span class="o">}</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="n">rel</span> <span class="n">L₂</span> <span class="n">L₁</span>
<span class="bp">|</span> <span class="n">trans</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">}</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="n">rel</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="bp">→</span> <span class="n">rel</span> <span class="n">L₁</span> <span class="n">L₃</span>
<span class="bp">|</span> <span class="n">append</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">L₄</span><span class="o">}</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="bp">→</span> <span class="n">rel</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">→</span> <span class="n">rel</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">L₃</span> <span class="bp">++</span> <span class="n">L₄</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">bnot</span> <span class="o">{</span><span class="n">x</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">rel</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">),</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)]</span> <span class="o">[]</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">α</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)])</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187324):
<p>How might I prove this?</p>

#### [ Kenny Lau (Apr 17 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187326):
<p>looks simple but somehow I can't do it</p>

#### [ Johannes Hölzl (Apr 17 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187372):
<p>You need to generalize <code>[(x, tt)]</code> and <code>[(y, tt)]</code> then you can use induction on it.</p>

#### [ Johannes Hölzl (Apr 17 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187383):
<p>Like</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">α</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">-&gt;</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">generalize</span> <span class="n">h1</span> <span class="o">:</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">x1</span><span class="o">,</span>
  <span class="n">generalize</span> <span class="n">h2</span> <span class="o">:</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">x2</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">h</span> <span class="n">generalizing</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
 <span class="bp">...</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187391):
<p>can I not do inversion (pattern matching)?</p>

#### [ Kenny Lau (Apr 17 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187452):
<p>your code doesn't work, and after I removed <code>intro h</code>, I get an impossible goal:</p>
<div class="codehilite"><pre><span></span><span class="n">case</span> <span class="n">rel</span><span class="bp">.</span><span class="n">refl</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">x1</span> <span class="n">x2</span> <span class="n">H</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">h1</span> <span class="o">:</span> <span class="n">H</span> <span class="bp">=</span> <span class="n">x1</span><span class="o">,</span>
<span class="n">h2</span> <span class="o">:</span> <span class="n">H</span> <span class="bp">=</span> <span class="n">x2</span><span class="o">,</span>
<span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>
</pre></div>

#### [ Johannes Hölzl (Apr 17 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187453):
<p><code>match</code> doesn't work, but <code>cases</code> could work. But I guess you need induction to finally proof it, as the <code>x</code> and <code>y</code> could come from the recursive call.</p>

#### [ Kenny Lau (Apr 17 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187468):
<p>never mind, ignore what I said about your code not working</p>

#### [ Kenny Lau (Apr 17 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187534):
<div class="codehilite"><pre><span></span><span class="n">case</span> <span class="n">rel</span><span class="bp">.</span><span class="n">symm</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">X</span> <span class="n">Y</span> <span class="n">L1</span> <span class="n">L2</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">H1</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L2</span><span class="o">,</span>
<span class="n">ih1</span> <span class="o">:</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L1</span> <span class="bp">→</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L2</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">,</span>
<span class="n">hx</span> <span class="o">:</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L2</span><span class="o">,</span>
<span class="n">hy</span> <span class="o">:</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L1</span>
<span class="err">⊢</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187535):
<p>I ran to an impossible goal</p>

#### [ Johannes Hölzl (Apr 17 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187539):
<p>did you use <code>induction h generalizing x y</code>?</p>

#### [ Johannes Hölzl (Apr 17 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187581):
<div class="codehilite"><pre><span></span><span class="n">case</span> <span class="n">rel</span><span class="bp">.</span><span class="n">symm</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="n">x1</span> <span class="n">x2</span> <span class="n">h_L₁</span> <span class="n">h_L₂</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">h_a</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">α</span> <span class="n">h_L₁</span> <span class="n">h_L₂</span><span class="o">,</span>
<span class="n">h_ih</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">h_L₁</span> <span class="bp">→</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">h_L₂</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">,</span>
<span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">h1</span> <span class="o">:</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">h_L₂</span><span class="o">,</span>
<span class="n">h2</span> <span class="o">:</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">h_L₁</span>
<span class="err">⊢</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187582):
<p>you're right, there's something wrong with me</p>

#### [ Johannes Hölzl (Apr 17 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187682):
<p>If you are working on free groups: you don't need the <code>refl</code>, <code>symm</code> and <code>trans</code> rules. For example I did a experiment a while back:<br>
<a href="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9" target="_blank" title="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9">https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9</a><br>
There I used <code>quot</code>, which doesn't require a <code>setoid</code>. Then lifting functions requires less proofs. Other things get a little bit more difficult.</p>

#### [ Kenny Lau (Apr 17 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187727):
<p>I, uh... prefer using setoid :P</p>

#### [ Kenny Lau (Apr 17 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187734):
<div class="codehilite"><pre><span></span><span class="n">case</span> <span class="n">free_group</span><span class="bp">.</span><span class="n">rel</span><span class="bp">.</span><span class="n">trans</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">X</span> <span class="n">Y</span> <span class="n">L1</span> <span class="n">L2</span> <span class="n">L3</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">H1</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L2</span><span class="o">,</span>
<span class="n">H2</span> <span class="o">:</span> <span class="n">rel</span> <span class="n">α</span> <span class="n">L2</span> <span class="n">L3</span><span class="o">,</span>
<span class="n">ih1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L1</span> <span class="bp">→</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L2</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">,</span>
<span class="n">ih2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L2</span> <span class="bp">→</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L3</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">,</span>
<span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">hx</span> <span class="o">:</span> <span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L1</span><span class="o">,</span>
<span class="n">hy</span> <span class="o">:</span> <span class="o">[(</span><span class="n">y</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L3</span>
<span class="err">⊢</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187735):
<p>an impossible goal</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187776):
<p>that's not impossible</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187783):
<p>it's just transitivity on the two ih</p>

#### [ Kenny Lau (Apr 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187787):
<p>but I can't use the assumption <code>[(y, tt)] = L2</code></p>

#### [ Kenny Lau (Apr 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187788):
<p>this can't be proved</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187802):
<p>Ah, I see</p>

#### [ Kenny Lau (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187809):
<p>is there really no way to use the equation compiler?</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187810):
<p>Didn't I show you how to solve this with a different representation?</p>

#### [ Kenny Lau (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187815):
<p>because that compiler is smarter than induction</p>

#### [ Johannes Hölzl (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187817):
<p>You first need to prove a stronger inversion rule: <code>rel [x] as -&gt; \exists y, as = [y]</code> (ups, this doesn't hold...)</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125187820):
<p>You want to focus on one-directional reduction</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188017):
<div class="codehilite"><pre><span></span>inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans {L₁ L₂ L₃} : red L₁ L₂ → red L₂ L₃ → red L₁ L₃
| cons {L₁ L₂} (a) : red L₁ L₂ → red (a :: L₁) (a :: L₂)
| bnot {x b L} : red ((x, b) :: (x, bnot b) :: L) L

theorem church_rosser : ∀ L₁ L₂, rel α L₁ L₂ → ∃ L₃, red α L₁ L₃ ∧ red α L₂ L₃ := sorry
</pre></div>

#### [ Kevin Buzzard (Apr 17 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188022):
<p>You could prove (easily by induction, I imagine) that for every function from alpha to Z/2Z (the additive group) the induced map from list (alpha x bool) to Z/2Z sending (x,b) to x and sending ++ to + has the property that two things related to each other go to the same place, and deduce it from that.</p>

#### [ Kenny Lau (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188035):
<p>seeing the word "church rosser" excites me</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188036):
<p>but x is in alpha, not Z/2Z</p>

#### [ Kevin Buzzard (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188038):
<p>right</p>

#### [ Kevin Buzzard (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188041):
<p>so if x wasn't y you just write down a function sending x to 1 and y to 0</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188042):
<p>so how is that a map from list (alpha x bool) to Z/2Z ?</p>

#### [ Kevin Buzzard (Apr 17 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188083):
<p>that's a map from alpha to Z/2Z</p>

#### [ Kenny Lau (Apr 17 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188086):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> "if x wasn't y"</p>

#### [ Kenny Lau (Apr 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188099):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> how would I prove symm?</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188100):
<p>To finish the proof given <code>church_rosser</code>, note that <code>red A L1 L2</code> implies <code>length L1 &gt;= length L2</code>, and they are the same length mod 2 so if one is a singleton so is the other</p>

#### [ Kevin Buzzard (Apr 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188101):
<p>I'm telling you how a mathematician would answer the original question</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188102):
<p>symm is trivial, since the target property is symmetric</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188142):
<p>the hard one is trans</p>

#### [ Kenny Lau (Apr 17 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188143):
<p>I don't get what you mean</p>

#### [ Kenny Lau (Apr 17 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188144):
<p><code>bnot</code> is clearly not symmetric</p>

#### [ Kevin Buzzard (Apr 17 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188146):
<p>I'm a bit confused about why a proof of what Mario calls Church Rosser can't just be "let L3 be L2"</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188149):
<p>note that <code>rel</code> becomes <code>red</code> in the result</p>

#### [ Kenny Lau (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188153):
<p>oh wait what</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188154):
<p><code>red</code> has no symmetry rule</p>

#### [ Kenny Lau (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188155):
<p>I thought you were telling me to rewrite rel to red lol</p>

#### [ Kevin Buzzard (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188157):
<p>oh, I didn't spot rel wasn't red</p>

#### [ Kenny Lau (Apr 17 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188158):
<p>high five</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188265):
<p>You will need this lemma for the trans case:</p>
<div class="codehilite"><pre><span></span>theorem church_rosser2 : ∀ L₁ L₂ L₃,
  red α L₁ L₂ → red α L₁ L₃ → ∃ L₄, red α L₂ L₄ ∧ red α L₃ L₄ := sorry
</pre></div>


<p>You can prove this by induction on one of the <code>red</code> assumptions</p>

#### [ Kenny Lau (Apr 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188437):
<p>which one?</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188441):
<p>it doesn't matter by symmetry</p>

#### [ Kenny Lau (Apr 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188443):
<p>but which one would you expand?</p>

#### [ Mario Carneiro (Apr 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188445):
<p>?</p>

#### [ Kenny Lau (Apr 17 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188452):
<p>never mind</p>

#### [ Kenny Lau (Apr 17 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188612):
<div class="codehilite"><pre><span></span><span class="n">case</span> <span class="n">free_group</span><span class="bp">.</span><span class="n">red</span><span class="bp">.</span><span class="n">trans</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">L₂</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="n">L1</span> <span class="n">L2</span> <span class="n">L3</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">H1</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L2</span><span class="o">,</span>
<span class="n">H2</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L2</span> <span class="n">L3</span><span class="o">,</span>
<span class="n">ih1</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L2</span> <span class="n">L₄</span><span class="o">),</span>
<span class="n">ih2</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L2</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L3</span> <span class="n">L₄</span><span class="o">),</span>
<span class="n">H1</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L₂</span>
<span class="err">⊢</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L3</span> <span class="n">L₄</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188613):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Apr 17 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188681):
<p>that's where <code>church_rosser2</code> comes in (also don't forget to generalize L₂)</p>

#### [ Kenny Lau (Apr 17 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188683):
<p>that's church_rosser2</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125188805):
<p>Actually on second thought I think you want to separate the transitivity part from the one-step reduction. That leads to the following proof skeleton:</p>
<div class="codehilite"><pre><span></span>inductive rel : list (α × bool) → list (α × bool) → Prop
| refl {L} : rel L L
| symm {L₁ L₂} : rel L₁ L₂ → rel L₂ L₁
| trans {L₁ L₂ L₃} : rel L₁ L₂ → rel L₂ L₃ → rel L₁ L₃
| append {L₁ L₂ L₃ L₄} : rel L₁ L₃ → rel L₂ L₄ → rel (L₁ ++ L₂) (L₃ ++ L₄)
| bnot {x b} : rel [(x, b), (x, bnot b)] []

inductive trans_gen {α} (R : α → α → Prop) (x : α) : α → Prop
| refl : trans_gen x
| trans {y z} : R y z → trans_gen y → trans_gen z

inductive red : list (α × bool) → list (α × bool) → Prop
| cons {L₁ L₂} (a) : red L₁ L₂ → red (a :: L₁) (a :: L₂)
| bnot {x b L} : red ((x, b) :: (x, bnot b) :: L) L

theorem church_rosser_1 : ∀ L₁ L₂ L₃,
  red α L₁ L₂ → red α L₁ L₃ → ∃ L₄, red α L₂ L₄ ∧ red α L₃ L₄ := sorry

theorem church_rosser_t1 : ∀ L₁ L₂ L₃,
  red α L₁ L₂ → trans_gen (red α) L₁ L₃ → ∃ L₄, trans_gen (red α) L₂ L₄ ∧ red α L₃ L₄ := sorry

theorem church_rosser_t : ∀ L₁ L₂ L₃,
  trans_gen (red α) L₁ L₂ → trans_gen (red α) L₁ L₃ → ∃ L₄, trans_gen (red α) L₂ L₄ ∧ trans_gen (red α) L₃ L₄ := sorry

theorem church_rosser : ∀ L₁ L₂, rel α L₁ L₂ →
  ∃ L₃, trans_gen (red α) L₁ L₃ ∧ trans_gen (red α) L₂ L₃ := sorry
</pre></div>


<p>This is important for the core of the proof, knowing that the one-step diamond property <code>church_rosser_1</code> holds is what allows you to do induction to get to <code>church_rosser_t</code></p>

#### [ Kenny Lau (Apr 17 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189880):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm stuck on church_rosser_1</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189895):
<p>You need to do induction on both arguments for that one</p>

#### [ Kenny Lau (Apr 17 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189899):
<p>even so</p>

#### [ Kenny Lau (Apr 17 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189902):
<div class="codehilite"><pre><span></span><span class="n">case</span> <span class="n">free_group</span><span class="bp">.</span><span class="n">red</span><span class="bp">.</span><span class="n">cons</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">L₁</span> <span class="n">L₃</span> <span class="n">L1</span> <span class="n">L2</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">x1</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">,</span>
<span class="n">H3</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L2</span><span class="o">,</span>
<span class="n">ih1</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">L₂</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span>
    <span class="n">red</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L2</span> <span class="n">L₄</span><span class="o">),</span>
<span class="n">L₂</span> <span class="n">L3</span> <span class="n">L4</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">x2</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">,</span>
<span class="n">H4</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L3</span> <span class="n">L4</span><span class="o">,</span>
<span class="n">ih2</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L4</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="o">(</span><span class="n">x1</span> <span class="bp">::</span> <span class="n">L2</span><span class="o">)</span> <span class="n">L₄</span>
<span class="err">⊢</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="o">(</span><span class="n">x2</span> <span class="bp">::</span> <span class="n">L4</span><span class="o">)</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="o">(</span><span class="n">x1</span> <span class="bp">::</span> <span class="n">L2</span><span class="o">)</span> <span class="n">L₄</span>
</pre></div>

#### [ Mario Carneiro (Apr 17 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189947):
<p>apply ih1?</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189953):
<p>and then destruct the exists's</p>

#### [ Kenny Lau (Apr 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189962):
<p>but I need the same list to clear the goal</p>

#### [ Kenny Lau (Apr 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189966):
<p>but x1 and x2 are different</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125189992):
<p>I'm just suggesting to apply <code>ih1</code> to <code>H3</code>, and then open up the assumptions <code>ih1</code> and <code>ih2</code></p>

#### [ Mario Carneiro (Apr 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190021):
<p>once you have done that you do inversion on <code>red α (x1 :: L2) L₄</code> and there are a few different cases</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190027):
<p>this is the tricky part, since you have to show that the rewriting is confluent meaning different contractions result in the same thing</p>

#### [ Kenny Lau (Apr 17 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190128):
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">L₁</span> <span class="n">L₃</span> <span class="n">L1</span> <span class="n">L2</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">x1</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">,</span>
<span class="n">H3</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L2</span><span class="o">,</span>
<span class="n">L₂</span> <span class="n">L3</span> <span class="n">L4</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">x2</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">,</span>
<span class="n">H4</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L3</span> <span class="n">L4</span><span class="o">,</span>
<span class="n">ih2</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L4</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="o">(</span><span class="n">x1</span> <span class="bp">::</span> <span class="n">L2</span><span class="o">)</span> <span class="n">L₄</span><span class="o">,</span>
<span class="n">ih1</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L2</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L2</span> <span class="n">L₄</span>
<span class="err">⊢</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="o">(</span><span class="n">x2</span> <span class="bp">::</span> <span class="n">L4</span><span class="o">)</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="o">(</span><span class="n">x1</span> <span class="bp">::</span> <span class="n">L2</span><span class="o">)</span> <span class="n">L₄</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190129):
<p>I don't think this is possible</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190132):
<p>It is, do cases on <code>ih1</code> and <code>ih2</code> now</p>

#### [ Kenny Lau (Apr 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190176):
<p>but I know nothing about <code>x2</code></p>

#### [ Mario Carneiro (Apr 17 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190257):
<p>hm, you seem to have forgotten something</p>

#### [ Mario Carneiro (Apr 17 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190266):
<p>I think you need to generalize one of the parameters before the secondary induction, or you will lose the relation with x2</p>

#### [ Kenny Lau (Apr 17 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190843):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> forgive me, but which parameter?</p>

#### [ Mario Carneiro (Apr 17 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190849):
<p>the one that has <code>x2</code> in it</p>

#### [ Kenny Lau (Apr 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190857):
<p>this is the state before the second induction</p>

#### [ Kenny Lau (Apr 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190858):
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">L₁</span> <span class="n">L₃</span> <span class="n">L1</span> <span class="n">L2</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">x1</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">,</span>
<span class="n">H3</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L2</span><span class="o">,</span>
<span class="n">ih1</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">L₂</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span>
    <span class="n">red</span> <span class="n">α</span> <span class="n">L1</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L2</span> <span class="n">L₄</span><span class="o">),</span>
<span class="n">L₂</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">H1</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="o">(</span><span class="n">x1</span> <span class="bp">::</span> <span class="n">L1</span><span class="o">)</span> <span class="n">L₂</span>
<span class="err">⊢</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="o">(</span><span class="n">x1</span> <span class="bp">::</span> <span class="n">L2</span><span class="o">)</span> <span class="n">L₄</span>
</pre></div>

#### [ Mario Carneiro (Apr 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190859):
<p>you want to get an equality constraint in the context so you can do injection on it</p>

#### [ Mario Carneiro (Apr 17 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190863):
<p><code>generalize h : x1 :: L1 = xL</code></p>

#### [ Kenny Lau (Apr 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190906):
<p>and then <code>generalizing</code> who?</p>

#### [ Mario Carneiro (Apr 17 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190959):
<p>I don't think you need any generalizing here, but you know what to change if the IH isn't strong enough</p>

#### [ Mario Carneiro (Apr 17 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125190968):
<p>actually you might not even need induction here; see if <code>cases H1</code> works</p>

#### [ Kevin Buzzard (Apr 17 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125191726):
<p>My way would be so much easier ;-)</p>

#### [ Kenny Lau (Apr 17 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195531):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> except it doesn't even work</p>

#### [ Kevin Buzzard (Apr 17 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195584):
<p>Oh rotten luck :-)</p>

#### [ Kevin Buzzard (Apr 17 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195585):
<p>It works in maths :-)</p>

#### [ Kevin Buzzard (Apr 17 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195606):
<p>first three properties are that = is an equiv relation, fourth is that the map is a group hom, fifth that Z/2 has exponent 2, and bob's your uncle</p>

#### [ Kenny Lau (Apr 17 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195660):
<p>oh wait, I misunderstood</p>

#### [ Kenny Lau (Apr 17 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195661):
<p>what's your method?</p>

#### [ Kenny Lau (Apr 17 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195696):
<p>you're using finsupp aren't you</p>

#### [ Kenny Lau (Apr 17 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195733):
<p>that's noncomputable</p>

#### [ Kenny Lau (Apr 17 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195843):
<p>if you form (Z/2Z)^S as a group, your set-theoretic function will be non-computable</p>

#### [ Johannes Hölzl (Apr 17 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195924):
<p>since a couple of weeks finsupp is computable</p>

#### [ Kenny Lau (Apr 17 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195973):
<p>right, but this instance is still not</p>

#### [ Kenny Lau (Apr 17 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125195992):
<p>in particular, <code>single</code> still needs decidable equality</p>

#### [ Kevin Buzzard (Apr 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196116):
<p>I said it works in maths ;-)</p>

#### [ Johannes Hölzl (Apr 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196117):
<p>well, then you need to use <code>classical.prop_decidable</code>.</p>

#### [ Kenny Lau (Apr 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196156):
<p>I thought you were talking about the adjoint functor theorem when I said it doesn't even work</p>

#### [ Kenny Lau (Apr 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196159):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> oh I forgot, we aren't on the same side</p>

#### [ Johannes Hölzl (Apr 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125196231):
<p>ok</p>

#### [ Kenny Lau (Apr 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197470):
<p>I think the main reason why this is hard is that reduction isn't straightforward</p>

#### [ Kenny Lau (Apr 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197471):
<p>if your list is [a,b,c,d]</p>

#### [ Kenny Lau (Apr 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197476):
<p>you can eliminate [b,c] or you can eliminate [c,d]</p>

#### [ Kenny Lau (Apr 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197517):
<p>then somehow you need to prove that [a,d] = [a,b]</p>

#### [ Kenny Lau (Apr 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197521):
<p>on the outside we know that to be true intuitively, but that doesn't mean this translates well on the inside</p>

#### [ Kenny Lau (Apr 17 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197599):
<p><a href="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9" target="_blank" title="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9">https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9</a></p>

#### [ Kenny Lau (Apr 17 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197603):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> oh and why don't you just put this onto mathlib lol</p>

#### [ Johannes Hölzl (Apr 17 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197789):
<p>Yours is slightly more general. I thought you want to fix your pull request and still try to get it into mathlib.</p>

#### [ Kenny Lau (Apr 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197801):
<p>actually I've written another free_group today, before this thread even started</p>

#### [ Johannes Hölzl (Apr 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197803):
<p>But as it looks it will take a little bit longer, so I can add my stuff first.</p>

#### [ Kenny Lau (Apr 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197804):
<p>(I live in GMT+8, so "today" started like 10 hours ago)</p>

#### [ Kenny Lau (Apr 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197809):
<p>and all this fuss is about I can't prove that the set-theoretic function is injective</p>

#### [ Kenny Lau (Apr 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197865):
<p><a href="https://gist.github.com/kckennylau/cda1c6c6bc781fe669692b8d725f43d0" target="_blank" title="https://gist.github.com/kckennylau/cda1c6c6bc781fe669692b8d725f43d0">https://gist.github.com/kckennylau/cda1c6c6bc781fe669692b8d725f43d0</a></p>

#### [ Kenny Lau (Apr 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197868):
<p>this is what the working part of my file looks like</p>

#### [ Kenny Lau (Apr 17 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197873):
<p>I think your file is slightly more general lol</p>

#### [ Kenny Lau (Apr 17 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197947):
<p>anyway, [a,d] and [a,b] aren't definitionally equal</p>

#### [ Kenny Lau (Apr 17 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197950):
<p>it just so happens that d=b</p>

#### [ Kenny Lau (Apr 17 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197952):
<p>but how am I supposed to know that</p>

#### [ Kenny Lau (Apr 17 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197963):
<p>I doubt church-rosser can be proved by me</p>

#### [ Johannes Hölzl (Apr 17 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125197970):
<p>So you don't want to follow the approach from stack overvlow anymore?</p>

#### [ Kenny Lau (Apr 17 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198007):
<p>nope</p>

#### [ Kenny Lau (Apr 17 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198018):
<p>I don't see any point</p>

#### [ Kenny Lau (Apr 17 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198021):
<p>I was overwhelmed by fear</p>

#### [ Kenny Lau (Apr 17 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198027):
<p>that I couldn't ever possibly define free group in one step</p>

#### [ Johannes Hölzl (Apr 17 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198125):
<p>don't worry, while theorem proving is a steep learning curve, it is a continuous curve after all</p>

#### [ Kenny Lau (Apr 17 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198145):
<p>you won't believe me if I told you that I prove limit commutes with multiplication in three steps</p>

#### [ Kenny Lau (Apr 17 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125198146):
<p>divide and conquer</p>

#### [ Kenny Lau (Apr 17 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199051):
<p>if <code>[(x,tt)]</code> is related to <code>[(y,tt)]</code>, part of the reason why it is so hard to prove <code>x=y</code> is that the reason they are related can be complicated</p>

#### [ Kenny Lau (Apr 17 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199070):
<p>since one can have <code>[(x,tt)] ~ [(x,tt), (x,ff), (x,tt)] ~ [(x,tt)]</code></p>

#### [ Kenny Lau (Apr 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199077):
<p>where the two <code>~</code>s deal with different pairs</p>

#### [ Kenny Lau (Apr 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199099):
<p>so this is hardly well-founded</p>

#### [ Kenny Lau (Apr 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199108):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> what do you think?</p>

#### [ Johannes Hölzl (Apr 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199232):
<p>it is not well-founded. but the non-symmetric reduction is well founded. as Mario mentioned the hard part is to proof the existence of diamonds</p>

#### [ Kenny Lau (Apr 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199240):
<p>would you have insights for the diamond?</p>

#### [ Kenny Lau (Apr 17 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199339):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> maybe give me more time to prove the diamonds?</p>

#### [ Kenny Lau (Apr 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199382):
<p>I'll see if I can incorporate other theorems you proved</p>

#### [ Kenny Lau (Apr 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199384):
<p>i.e. free_group of empty is unit</p>

#### [ Kenny Lau (Apr 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199385):
<p>free_group of unit is int</p>

#### [ Kenny Lau (Apr 17 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199467):
<div class="codehilite"><pre><span></span><span class="bp">|</span> <span class="n">bnot</span> <span class="o">{</span><span class="n">x</span> <span class="n">b</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199478):
<p>(I know this is essentially what you did, but I hadn't looked at your file when I came up with this, somehow)</p>

#### [ Kenny Lau (Apr 17 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199483):
<p>it's hard proving diamond even for one step bnot</p>

#### [ Kenny Lau (Apr 17 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199492):
<p>i.e. if L1 bnot L2, L1 bnot L3, then there is L4 such that L2 bnot L4 and L3 bnot L4</p>

#### [ Kenny Lau (Apr 17 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199555):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> what do you think?</p>

#### [ Johannes Hölzl (Apr 17 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199581):
<p>I didn't look into this, yet. I will see if I find some time to understand it.</p>

#### [ Kenny Lau (Apr 17 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199632):
<p>I mean, don't put your freegroup into mathlib yet</p>

#### [ Johannes Hölzl (Apr 17 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199694):
<p>okay. but mathlib seams to be broken anyway currently (EDIT: sorry, mathlib is not broken)</p>

#### [ Kenny Lau (Apr 17 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199706):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> which one would you use? <code>n+n</code>, <code>n*2</code>, <code>2*n</code></p>

#### [ Kenny Lau (Apr 17 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199708):
<p>for usability</p>

#### [ Kenny Lau (Apr 17 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199711):
<p>I think<code> 2*n</code> is maximum usability</p>

#### [ Johannes Hölzl (Apr 17 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199714):
<p>yes, looks good</p>

#### [ Kenny Lau (Apr 17 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125199742):
<p>I just answered my own question</p>

#### [ Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204798):
<p>I changed anew the definition:</p>

#### [ Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204801):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">red</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L</span> <span class="n">L</span>
<span class="bp">|</span> <span class="n">trans_bnot</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">x</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span><span class="o">)</span> <span class="n">L₃</span> <span class="bp">→</span> <span class="n">red</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₂</span><span class="o">)</span> <span class="n">L₃</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204804):
<p>hopefully this will be more usable</p>

#### [ Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204805):
<p>I still can't prove church-rosser though</p>

#### [ Kenny Lau (Apr 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125204811):
<p>I suspect I shouldn't do church-rosser in one step</p>

#### [ Kenny Lau (Apr 17 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205016):
<p><a href="/user_uploads/3121/SwM98KnlFnJesSDVnNnSYJK1/church-rosser-1.png" target="_blank" title="church-rosser-1.png">church-rosser-1.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/SwM98KnlFnJesSDVnNnSYJK1/church-rosser-1.png" target="_blank" title="church-rosser-1.png"><img src="/user_uploads/3121/SwM98KnlFnJesSDVnNnSYJK1/church-rosser-1.png"></a></div>

#### [ Kenny Lau (Apr 17 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205188):
<p>and induction on the rightmost solid arrow amounts to doing this:</p>

#### [ Kenny Lau (Apr 17 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205234):
<p><a href="/user_uploads/3121/HY4gl0SQ4kObK_7zXbz_B1e3/church-rosser-1.png" target="_blank" title="church-rosser-1.png">church-rosser-1.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/HY4gl0SQ4kObK_7zXbz_B1e3/church-rosser-1.png" target="_blank" title="church-rosser-1.png"><img src="/user_uploads/3121/HY4gl0SQ4kObK_7zXbz_B1e3/church-rosser-1.png"></a></div>

#### [ Kenny Lau (Apr 17 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205244):
<p>where <code>wordIH</code> is the word given by induction hypothesis</p>

#### [ Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205252):
<p>my new definition makes sure that it is decomposed into steps</p>

#### [ Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205254):
<p>whereas the old definition splits the arrow randomly in half</p>

#### [ Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205260):
<p>my new definition guarantees that it is split at the tail</p>

#### [ Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205266):
<p>oh no, my new definition splits it at the head</p>

#### [ Kenny Lau (Apr 17 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205268):
<p>brb</p>

#### [ Kenny Lau (Apr 17 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205402):
<p>I mean, even if I corrected the definition, I still don't know how to build <code>word4</code> from <code>wordIH</code></p>

#### [ Kenny Lau (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205405):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> any insight?</p>

#### [ Kevin Buzzard (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205454):
<p>I told you how I'd do it ;-)</p>

#### [ Kevin Buzzard (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205456):
<p>I've not thought about the constructive approach</p>

#### [ Kevin Buzzard (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205458):
<p>I've not been following the conversation here.</p>

#### [ Kevin Buzzard (Apr 17 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205466):
<p>My daughter is sick so I've not had much time today, and what little time I did have I spent thinking about Spec(R) being compact</p>

#### [ Kenny Lau (Apr 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205520):
<p>you just need to look at my latest picture</p>

#### [ Kenny Lau (Apr 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205521):
<p>"step" means a one-step reduction, i.e. reducing <code>w1++[a,a^-1]++w2</code> to <code>w1++w2</code></p>

#### [ Kenny Lau (Apr 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205528):
<p><code>wordIH</code> is given, and I would like to construct <code>word4</code></p>

#### [ Kenny Lau (Apr 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205531):
<p>I might have to destruct the bottom right solid arrow</p>

#### [ Kenny Lau (Apr 17 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205601):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'm astonished by the fact that I'm drawing a diagram to represent induction and that I'm drawing a diagram (the same diagram) to deal with free groups</p>

#### [ Kenny Lau (Apr 17 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205605):
<p>I've never looked into free group this deeply</p>

#### [ Kenny Lau (Apr 17 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125205629):
<p>I'll destruct the arrow I mentioned and see what comes up</p>

#### [ Mario Carneiro (Apr 17 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206778):
<p>The construction of many step CR from one step CR is like building a checkerboard of diamonds</p>

#### [ Kenny Lau (Apr 17 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206830):
<p>oh and I've changed to the "correct" definition now</p>

#### [ Kenny Lau (Apr 17 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206833):
<p>did you look at my picture?</p>

#### [ Mario Carneiro (Apr 17 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206835):
<p>You do induction on one of the <code>trans_rel</code> arguments to reduce to a line of diamonds, and then the other one to get one step out, one step back together</p>

#### [ Mario Carneiro (Apr 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206861):
<p>You want to use the IH to move the base point of the bottom diamond to wordIH</p>

#### [ Kenny Lau (Apr 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206878):
<p>base point?</p>

#### [ Mario Carneiro (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206917):
<p>You have word1''' -&gt; word3 and word1''' -&gt; wordIH, so wordIH -&gt; word4 &lt;- word3 for some word4</p>

#### [ Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206925):
<p>right, that's what I intend to do also</p>

#### [ Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206933):
<p>I proved transitivity independently</p>

#### [ Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206942):
<p>so I only need to focus on that diamond</p>

#### [ Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206947):
<p>and destruct the bottom right solid arrow</p>

#### [ Kenny Lau (Apr 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206953):
<p>right?</p>

#### [ Mario Carneiro (Apr 17 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206968):
<p>I'm not sure I follod</p>

#### [ Mario Carneiro (Apr 17 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125206978):
<p>Do you still have the three theorems <code>church_rosser_(1,t1,t)</code> or something similar?</p>

#### [ Kenny Lau (Apr 17 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207035):
<p>oh I am not using your definition now...</p>

#### [ Mario Carneiro (Apr 17 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207049):
<p>but do you have the thing with transitive closure of one step reduction</p>

#### [ Kenny Lau (Apr 17 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207067):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">red</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L</span> <span class="n">L</span>
<span class="bp">|</span> <span class="n">trans_bnot</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">x</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="o">(</span><span class="n">L₂</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₃</span><span class="o">)</span> <span class="bp">→</span> <span class="n">red</span> <span class="n">L₁</span> <span class="o">(</span><span class="n">L₂</span> <span class="bp">++</span> <span class="n">L₃</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">}</span> <span class="o">(</span><span class="n">H12</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">H23</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">)</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">H23</span> <span class="k">with</span> <span class="n">L1</span> <span class="n">L1</span> <span class="n">L2</span> <span class="n">L3</span> <span class="n">x</span> <span class="n">b</span> <span class="n">H</span> <span class="n">ih</span> <span class="n">generalizing</span> <span class="n">L₁</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span>
  <span class="o">{</span> <span class="n">assumption</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans_bnot</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans_bnot</span> <span class="o">(</span><span class="n">ih</span> <span class="n">H12</span><span class="o">)</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 17 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207071):
<p>this is what i'm using</p>

#### [ Kenny Lau (Apr 17 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207086):
<p>and unfinished church rosser:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">church_rosser</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">}</span> <span class="o">(</span><span class="n">H12</span> <span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">H13</span><span class="o">:</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₁</span> <span class="n">L₃</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="n">L₄</span><span class="o">,</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">α</span> <span class="n">L₃</span> <span class="n">L₄</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">H12</span> <span class="k">with</span> <span class="n">L1</span> <span class="n">L1</span> <span class="n">L2</span> <span class="n">L3</span> <span class="n">x1</span> <span class="n">b1</span> <span class="n">H1</span> <span class="n">ih1</span> <span class="n">generalizing</span> <span class="n">L₃</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">L₃</span><span class="o">,</span> <span class="n">H13</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_⟩</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans_bnot</span>
  <span class="o">{</span> <span class="n">specialize</span> <span class="n">ih1</span> <span class="n">H13</span><span class="o">,</span>
    <span class="n">rcases</span> <span class="n">ih1</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">L₄</span><span class="o">,</span> <span class="n">H24</span><span class="o">,</span> <span class="n">H34</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">revert</span> <span class="n">H24</span><span class="o">,</span>
    <span class="n">generalize</span> <span class="n">HL23</span> <span class="o">:</span> <span class="n">L2</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L3</span> <span class="bp">=</span> <span class="n">L23</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">H24</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">H24</span> <span class="k">with</span> <span class="n">L4</span> <span class="n">L4</span> <span class="n">L5</span> <span class="n">L6</span> <span class="n">x2</span> <span class="n">b2</span> <span class="n">H2</span> <span class="n">ih2</span><span class="o">,</span>
    <span class="n">case</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span>
    <span class="o">{</span> <span class="n">subst</span> <span class="n">HL23</span><span class="o">,</span>
      <span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans_bnot</span> <span class="n">H34</span><span class="bp">⟩</span> <span class="o">},</span>
    <span class="n">case</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans_bnot</span>
    <span class="o">{</span> <span class="n">subst</span> <span class="n">HL23</span><span class="o">,</span>
      <span class="n">admit</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 17 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207167):
<p>I think that trying to do it all at once will be harder, because then you have to commute a whole sequence of reductions past another</p>

#### [ Mario Carneiro (Apr 17 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207318):
<p>With one step reduction, the core of the proof is this: Suppose L -&gt; L1 and L -&gt; L2. Then L = A1 ++ [(x,b), (x, !b)] ++ A2 = B1 ++ [(y,c),(y,!c)] ++ B2 and L1 = A1 ++ A2, L2 = B1 ++ B2. There are three cases depending on whether |A1| = |B1|, |A1| = |B1| +- 1, or | |A1| - |B1| | &gt;= 2, but in each case the results are either equal or can be put together with a single step on each side.</p>

#### [ Kenny Lau (Apr 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207342):
<p>that's the hardest part of the theorem</p>

#### [ Mario Carneiro (Apr 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207348):
<p>So I guess you want <code>red</code> to be reflexive but not transitive, and then take its transitive closure to put the diamonds together</p>

#### [ Kenny Lau (Apr 17 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207393):
<p>I don't think I need to change my definition</p>

#### [ Mario Carneiro (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207524):
<p>One word of warning: the confluence property B &lt;- A -&gt; C implies \ex D s.t. B -&gt;* D &lt;-* C does <em>not</em> imply church rosser in general. It does if you have strong normalization, but that's a harder proof. That's why I'm wary of building transitivity into the -&gt; relation</p>

#### [ Kenny Lau (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207545):
<p>isn't that church rosser?</p>

#### [ Mario Carneiro (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207550):
<p>Note the location of the stars</p>

#### [ Kenny Lau (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207554):
<p>what are those?</p>

#### [ Mario Carneiro (Apr 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207557):
<p>one step out, many steps back in</p>

#### [ Mario Carneiro (Apr 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207595):
<p>that's notation for transitive closure</p>

#### [ Kenny Lau (Apr 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125207598):
<p>hmm</p>

#### [ Kenny Lau (Apr 18 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224401):
<blockquote>
<p>With one step reduction, the core of the proof is this: Suppose L -&gt; L1 and L -&gt; L2. Then L = A1 ++ [(x,b), (x, !b)] ++ A2 = B1 ++ [(y,c),(y,!c)] ++ B2 and L1 = A1 ++ A2, L2 = B1 ++ B2. There are three cases depending on whether |A1| = |B1|, |A1| = |B1| +- 1, or | |A1| - |B1| | &gt;= 2, but in each case the results are either equal or can be put together with a single step on each side.</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what is the best way to prove that there are three cases?</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224462):
<p><code>wlog</code> length A1 &lt;= length B1</p>

#### [ Kenny Lau (Apr 18 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224549):
<p>aha, i never tried wlog before</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224592):
<p>me neither, but this looks like a good use case</p>

#### [ Kenny Lau (Apr 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224731):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">partition</span> <span class="o">{</span><span class="n">L1</span> <span class="n">L2</span> <span class="n">L3</span> <span class="n">L4</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)}</span> <span class="o">{</span><span class="n">x1</span> <span class="n">b1</span> <span class="n">x2</span> <span class="n">b2</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">L1</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L2</span> <span class="bp">=</span> <span class="n">L3</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L4</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">L1</span> <span class="bp">=</span> <span class="n">L3</span> <span class="bp">∧</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span> <span class="bp">∧</span> <span class="n">b1</span> <span class="bp">=</span> <span class="n">b2</span> <span class="bp">∧</span> <span class="n">L2</span> <span class="bp">=</span> <span class="n">L4</span><span class="o">)</span> <span class="bp">∨</span>
  <span class="o">(</span><span class="n">L1</span> <span class="bp">=</span> <span class="n">L3</span> <span class="bp">++</span> <span class="o">[(</span><span class="n">x2</span><span class="o">,</span> <span class="n">b2</span><span class="o">)]</span> <span class="bp">∧</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span> <span class="bp">∧</span> <span class="n">b1</span> <span class="bp">=</span> <span class="n">bnot</span> <span class="n">b2</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L2</span> <span class="bp">=</span> <span class="n">L4</span><span class="o">)</span> <span class="bp">∨</span>
  <span class="o">(</span><span class="n">L1</span> <span class="bp">++</span> <span class="o">[(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)]</span> <span class="bp">=</span> <span class="n">L3</span> <span class="bp">∧</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span> <span class="bp">∧</span> <span class="n">b1</span> <span class="bp">=</span> <span class="n">bnot</span> <span class="n">b2</span> <span class="bp">∧</span> <span class="n">L2</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L4</span><span class="o">)</span> <span class="bp">∨</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">L5</span> <span class="n">L6</span><span class="o">,</span> <span class="n">L1</span> <span class="bp">=</span> <span class="n">L3</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L5</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L2</span> <span class="bp">=</span> <span class="n">L6</span><span class="o">)</span> <span class="bp">∨</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">L5</span> <span class="n">L6</span><span class="o">,</span> <span class="n">L1</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L5</span> <span class="bp">=</span> <span class="n">L3</span> <span class="bp">∧</span> <span class="n">L2</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L6</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224732):
<p>how is this?</p>

#### [ Kenny Lau (Apr 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224734):
<p>I don't think <code>length</code> is very usable</p>

#### [ Kenny Lau (Apr 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224774):
<p>it's obvious to mathematicians, but Lean doesn't really know how to count well</p>

#### [ Kenny Lau (Apr 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224776):
<p>it's just translating one inductive type into another</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224834):
<p>You can simplify this by assuming <code>length L1 &lt;= length L3</code>, and then two of the cases can be proven impossible (it's not hard to show that if L1 = L3 ++ [(x2, b2)] then length L3 &lt; length L1, and that's all you need)</p>

#### [ Kenny Lau (Apr 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224847):
<p>are you saying I don't need induction?</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224850):
<p>induction on what? To prove partition?</p>

#### [ Kenny Lau (Apr 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224851):
<p>right</p>

#### [ Kenny Lau (Apr 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224856):
<p>on the lists</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224895):
<p>You can use <code>append_inj</code> to use length information to get the decomposition</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224905):
<p>But you can also prove it by induction on one of the lists (generalizing everything else)</p>

#### [ Kenny Lau (Apr 18 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224956):
<p>I think I would need more lemmas than <code>append_inj</code> if I want to avoid induction completely</p>

#### [ Kenny Lau (Apr 18 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125224961):
<p><code>append_inj</code> doesn't seem to help in the case where <code>|A.length - B.length| &gt;= 2</code></p>

#### [ Mario Carneiro (Apr 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225016):
<p>hm, you could use <code>take_drop</code> but I agree it is probably messier than induction on the list</p>

#### [ Kenny Lau (Apr 18 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225031):
<p>I think a useful lemma if I want to avoid length and induction completely is <code>A++B=C++D -&gt; (exists F, A=C++F) or (exists F, A++F=C)</code></p>

#### [ Mario Carneiro (Apr 18 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225036):
<p>I think you can get that by using <code>prefix</code> appropriately</p>

#### [ Kenny Lau (Apr 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225079):
<p>I have never heard of prefix before. I've just learnt something new lol</p>

#### [ Kenny Lau (Apr 18 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225146):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm not seeing anything useful from the prefix lemmas</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225157):
<p>Here's what I'm thinking:</p>
<div class="codehilite"><pre><span></span>theorem prefix_of_prefix_length_le {l₁ l₂ l₃ : list α} : l₁ &lt;+: l₃ → l₂ &lt;+: l₃ → length l₁ ≤ length l₂ → l₁ &lt;+: l₂ :=
sorry
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225161):
<p>let's just focus on my lemma</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225163):
<p>and from that you get the version with the or</p>

#### [ Kenny Lau (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225164):
<p>aha</p>

#### [ Kenny Lau (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225204):
<p>totality of prefix descends from totality of natural numbers</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225207):
<p>exactly</p>

#### [ Kenny Lau (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225210):
<p>that's a very convoluted way of doing stuff</p>

#### [ Kenny Lau (Apr 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225213):
<p>I would rather use induction to prove my lemma</p>

#### [ Kenny Lau (Apr 18 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225271):
<p>disregarding this</p>

#### [ Kenny Lau (Apr 18 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225274):
<p>how would you prove your lemma</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225622):
<p>working on it</p>

#### [ Kenny Lau (Apr 18 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225623):
<p>me too</p>

#### [ Kenny Lau (Apr 18 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225624):
<p>I think I can do that, thanks</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225729):
<div class="codehilite"><pre><span></span>theorem prefix_of_prefix_length_le : ∀ {l₁ l₂ l₃ : list α},
 l₁ &lt;+: l₃ → l₂ &lt;+: l₃ → length l₁ ≤ length l₂ → l₁ &lt;+: l₂
| []      l₂ l₃ h₁ h₂ _ := nil_prefix _
| (a::l₁) (b::l₂) _ ⟨r₁, rfl⟩ ⟨r₂, e⟩ ll := begin
  injection e with _ e&#39;, subst b,
  rcases prefix_of_prefix_length_le ⟨_, rfl⟩ ⟨_, e&#39;⟩
    (le_of_succ_le_succ ll) with ⟨r₃, rfl⟩,
  exact ⟨r₃, rfl⟩
end

theorem prefix_or_prefix_of_prefix {l₁ l₂ l₃ : list α}
 (h₁ : l₁ &lt;+: l₃) (h₂ : l₂ &lt;+: l₃) : l₁ &lt;+: l₂ ∨ l₂ &lt;+: l₁ :=
(le_total (length l₁) (length l₂)).imp
  (prefix_of_prefix_length_le h₁ h₂)
  (prefix_of_prefix_length_le h₂ h₁)
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225731):
<p>oh nice thanks</p>

#### [ Kenny Lau (Apr 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225737):
<p>who is <code>nil_prefix</code>?</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225740):
<div class="codehilite"><pre><span></span>theorem nil_prefix (l : list α) : [] &lt;+: l := ⟨l, rfl⟩
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225742):
<p>did you just make it up?</p>

#### [ Mario Carneiro (Apr 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225772):
<p>yes</p>

#### [ Kenny Lau (Apr 18 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225787):
<p>thanks</p>

#### [ Kenny Lau (Apr 18 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125225936):
<p>does <code>A++B=A++C -&gt; B=C</code> have a name?</p>

#### [ Mario Carneiro (Apr 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226008):
<p><code>append_right_cancel</code></p>

#### [ Kenny Lau (Apr 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226009):
<p>oh, didn't think of cancel</p>

#### [ Kenny Lau (Apr 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226011):
<p>oh, and do you know that the lists form a monoid?</p>

#### [ Kenny Lau (Apr 18 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226013):
<p>by "you" I of course mean "Lean"</p>

#### [ Mario Carneiro (Apr 18 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226137):
<p>No, although all the lemmas are there, because I don't think we want <code>*</code> to mean append on lists</p>

#### [ Kenny Lau (Apr 18 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226138):
<p>I see</p>

#### [ Mario Carneiro (Apr 18 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226191):
<p>That was one of the main motivations Leo had for introducing the whole "notation free" algebraic hierarchy like <code>is_associative</code></p>

#### [ Kenny Lau (Apr 18 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226198):
<p>I'm not aware of what you're talking about</p>

#### [ Mario Carneiro (Apr 18 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226205):
<p>look at <code>is_associative</code> and friends</p>

#### [ Kenny Lau (Apr 18 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226208):
<p>where is it used?</p>

#### [ Mario Carneiro (Apr 18 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226250):
<p>that's probably what lean 4 algebraic hierarchy will look like</p>

#### [ Mario Carneiro (Apr 18 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226258):
<p>I'm not sold on it yet, and I don't think the tool support is there yet, so I'm sticking to "old style" structures like <code>monoid</code></p>

#### [ Kenny Lau (Apr 18 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226264):
<p>oh</p>

#### [ Mario Carneiro (Apr 18 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226267):
<p>but it gets used in some core lean stuff like <code>rb_map</code></p>

#### [ Kenny Lau (Apr 18 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226269):
<p>another thing I've never heard of :D</p>

#### [ Kenny Lau (Apr 18 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226857):
<p>what's the fastest way to destruct <code>L5 ++ L6 = [(x1, bnot b1)]</code>?</p>

#### [ Kenny Lau (Apr 18 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125226907):
<p>cases L5, lol</p>

#### [ Kenny Lau (Apr 18 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228253):
<p>I proved church rosser!!</p>

#### [ Kenny Lau (Apr 18 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228296):
<p>thanks for your help all along <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Apr 18 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228390):
<p>That theorem can of course also be used to show the existence and uniqueness of reduced words</p>

#### [ Kenny Lau (Apr 18 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228394):
<p>right, since I proved that red is decreasing in length</p>

#### [ Mario Carneiro (Apr 18 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228481):
<p>You need decidable equality for it to be constructive, but you can just remove matching pairs until you can't find any more, and that will be the unique representative of its equivalence class by church rosser</p>

#### [ Mario Carneiro (Apr 18 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228558):
<p>Here's a fun trick showing that the converse also holds: assuming [(x,tt), (y,ff)] has a reduced word representative, if it has length zero then x=y, and if it has length 2 then x != y</p>

#### [ Kenny Lau (Apr 18 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228564):
<p>aha</p>

#### [ Kenny Lau (Apr 18 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125228567):
<p>nice trick</p>

#### [ Kenny Lau (Apr 18 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125231206):
<div class="codehilite"><pre><span></span>inductive red : list (α × bool) → list (α × bool) → Prop
| refl {L} : red L L
| trans_bnot {L₁ L₂ L₃ x b} : red L₁ (L₂ ++ (x, b) :: (x, bnot b) :: L₃) → red L₁ (L₂ ++ L₃)
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125231212):
<p>how do I use the equation compiler to destruct this?</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232619):
<div class="codehilite"><pre><span></span>theorem T : ∀ L₁ L₂, red α L₁ L₂ → true
| L _ (red.refl _) := trivial
| _ _ (@red.trans_bnot _ L₁ L₂ L₃ x b IH) := trivial
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232627):
<p>oh, I get error because I didn't type <code>L</code>?</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232629):
<p>no, without the L you just get a placeholder name</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232669):
<p>You can also use <code>(@red.refl _ L)</code> to name the parameters</p>

#### [ Kenny Lau (Apr 18 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232671):
<p>then why do I always get error lol</p>

#### [ Kenny Lau (Apr 18 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232674):
<p>oh and I can't use recursion because this is a Prop, right</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232675):
<p>You can use recursion</p>

#### [ Kenny Lau (Apr 18 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232681):
<p>but I would have to provide custom well-founded proof?</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232682):
<p>but you can't generate a data type</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232684):
<p>maybe that's what you meant</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232743):
<p>it doesn't work for wellfounded either because the inductive type has two constructors, so there are multiple ways to prove a <code>red</code> statement</p>

#### [ Kenny Lau (Apr 18 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232802):
<p><a href="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9" target="_blank" title="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9">https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9</a></p>

#### [ Kenny Lau (Apr 18 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232806):
<p>this is interesting</p>

#### [ Kenny Lau (Apr 18 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232811):
<p>"map" and "prod" together give the UMP</p>

#### [ Kenny Lau (Apr 18 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232812):
<p>but I can also prove "map" and "prod" using UMP</p>

#### [ Kenny Lau (Apr 18 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125232813):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what would you prefer? or should I prove all three?</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233054):
<p>I think you should state the UMP just for "completeness", but I expect <code>map</code> and <code>prod</code> and their lemmas are the more useful version</p>

#### [ Kenny Lau (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233057):
<p>not just for completeness</p>

#### [ Kenny Lau (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233058):
<p>I'll actually prove map and prod from UMP</p>

#### [ Kenny Lau (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233061):
<p>then I don't need any induction again</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233064):
<p>The definitions of map and prod are constructive and done reasonably, I wouldn't want to make it more complicated</p>

#### [ Kenny Lau (Apr 18 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233072):
<p>everything in my file is constructive</p>

#### [ Kenny Lau (Apr 18 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233089):
<p>but you're right, I shouldn't use UMP to define map</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233094):
<p>I mean, you can compute with <code>map</code> there. Don't make the program slower</p>

#### [ Kenny Lau (Apr 18 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233097):
<p>oh</p>

#### [ Kenny Lau (Apr 18 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233344):
<div class="codehilite"><pre><span></span>instance is_group_hom.id [group α] : is_group_hom (@id α) :=
λ _ _, rfl
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233383):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> could you add this to mathlib?</p>

#### [ Mario Carneiro (Apr 18 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233403):
<p>K</p>

#### [ Kenny Lau (Apr 18 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125233430):
<p>obrigad</p>

#### [ Kenny Lau (Apr 18 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235275):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <code>prod</code> is really a specialization of the UMP though</p>

#### [ Kenny Lau (Apr 18 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235287):
<p>I mean, the definition would be identical</p>

#### [ Kenny Lau (Apr 18 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235290):
<p>defining <code>prod</code> using the UMP won't make anything slower</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235342):
<p>what is your def of ump?</p>

#### [ Kenny Lau (Apr 18 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235346):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_group</span><span class="bp">.</span><span class="n">aux</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">L</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">prod</span> <span class="err">$</span> <span class="n">L</span><span class="bp">.</span><span class="n">map</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">bool</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span><span class="bp">⁻¹</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span>

<span class="n">def</span> <span class="n">to_group</span> <span class="o">:</span> <span class="n">free_group</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">lift</span> <span class="o">(</span><span class="n">to_group</span><span class="bp">.</span><span class="n">aux</span> <span class="n">f</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="bp">⟨</span><span class="n">L₃</span><span class="o">,</span> <span class="n">H13</span><span class="o">,</span> <span class="n">H23</span><span class="bp">⟩</span><span class="o">,</span>
<span class="o">(</span><span class="n">red</span><span class="bp">.</span><span class="n">to_group</span> <span class="n">H13</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">red</span><span class="bp">.</span><span class="n">to_group</span> <span class="n">H23</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>
</pre></div>

#### [ Mario Carneiro (Apr 18 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235388):
<p>looks good</p>

#### [ Kenny Lau (Apr 18 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235392):
<p>update:</p>

#### [ Kenny Lau (Apr 18 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235393):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_group</span><span class="bp">.</span><span class="n">aux</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">L</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">prod</span> <span class="err">$</span> <span class="n">L</span><span class="bp">.</span><span class="n">map</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">cond</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span><span class="bp">⁻¹</span>
</pre></div>

#### [ Mario Carneiro (Apr 18 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235401):
<p>I guess <code>prod</code> is this specialized to id?\</p>

#### [ Kenny Lau (Apr 18 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235403):
<p>correct</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235446):
<p>ok, seems reasonable</p>

#### [ Kenny Lau (Apr 18 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235447):
<p>orbigad</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235449):
<p>the spelling keeps getting weirder :)</p>

#### [ Kenny Lau (Apr 18 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235450):
<p>sim</p>

#### [ Kenny Lau (Apr 18 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235518):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">prod</span><span class="bp">.</span><span class="n">eq_to_group</span> <span class="o">:</span> <span class="n">prod</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">to_group</span> <span class="n">id</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">prod</span><span class="bp">.</span><span class="n">mk</span> <span class="o">:</span> <span class="n">prod</span> <span class="err">⟦</span><span class="n">L</span><span class="err">⟧</span> <span class="bp">=</span> <span class="n">list</span><span class="bp">.</span><span class="n">prod</span> <span class="o">(</span><span class="n">L</span><span class="bp">.</span><span class="n">map</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">cond</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⁻¹</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235519):
<p>which one should I keep?</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235583):
<p><code>prod.eq_to_group </code> can be the definition, the other one should still be refl</p>

#### [ Kenny Lau (Apr 18 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235630):
<p>it is the definition, but I still want a simp lemma</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235633):
<p>it shouldnt be a simp lemma though</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235634):
<p>prod.eq_to_group  that is</p>

#### [ Kenny Lau (Apr 18 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235638):
<p>why not?</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235654):
<p>because it has its own lemmas</p>

#### [ Kenny Lau (Apr 18 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235661):
<p><a href="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9#file-free_group-lean-L119" target="_blank" title="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9#file-free_group-lean-L119">https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9#file-free_group-lean-L119</a></p>

#### [ Kenny Lau (Apr 18 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235662):
<p>why isn't this an instance?</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235705):
<p>it can be</p>

#### [ Johannes Hölzl (Apr 18 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235720):
<p>Yup, I wrote this before <code>is_group_hom</code> was a class.</p>

#### [ Kenny Lau (Apr 18 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235724):
<p>I see</p>

#### [ Kenny Lau (Apr 18 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235766):
<p>anyway, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I proved of.inj constructively :D</p>

#### [ Kenny Lau (Apr 18 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235773):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> oh, do you know that for any type <code>X</code>, <code>set X</code> is a group?</p>

#### [ Johannes Hölzl (Apr 18 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235774):
<p>you  mean with out assuming decidability of α?</p>

#### [ Kenny Lau (Apr 18 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235775):
<p>right</p>

#### [ Kenny Lau (Apr 18 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235819):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">of</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">of</span><span class="bp">.</span><span class="n">inj</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">of</span><span class="bp">.</span><span class="n">inj</span>

<span class="n">def</span> <span class="n">free_group</span><span class="bp">.</span><span class="n">of</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">},</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">free_group</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="err">⟦</span><span class="o">[(</span><span class="n">x</span><span class="o">,</span> <span class="n">tt</span><span class="o">)]</span><span class="err">⟧</span>

<span class="n">of</span><span class="bp">.</span><span class="n">inj</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">of</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">of</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>

<span class="n">propext</span>
</pre></div>

#### [ Johannes Hölzl (Apr 18 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235848):
<p>as long as the proof isn't longer</p>

#### [ Kenny Lau (Apr 18 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235859):
<p>aha</p>

#### [ Kenny Lau (Apr 18 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235860):
<p>our different values are reflected in as short as two lines</p>

#### [ Kenny Lau (Apr 18 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235903):
<p>the only lengthy part of my file is church rosser</p>

#### [ Kenny Lau (Apr 18 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235905):
<p>which your file doesn't even have</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235912):
<p>a group? With what, symmetric difference and complement?</p>

#### [ Kenny Lau (Apr 18 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235913):
<p>right</p>

#### [ Kenny Lau (Apr 18 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235914):
<p>it even forms a ring with multiplication being intersection</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235969):
<p>that seems more like bool -&gt; X</p>

#### [ Kenny Lau (Apr 18 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235970):
<p>X -&gt; bool</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235972):
<p>yeah that</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125235980):
<p>it's the indexed ring product of Z/2Z</p>

#### [ Kenny Lau (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236022):
<p>is there any easy way to prove that an add_group is a group?</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236024):
<p><code>multiplicative</code></p>

#### [ Kenny Lau (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236025):
<p>should I use it to define sum?</p>

#### [ Kenny Lau (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236026):
<p><a href="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9#file-free_group-lean-L168" target="_blank" title="https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9#file-free_group-lean-L168">https://gist.github.com/johoelzl/7e73916f39e3acef8796bfb6c089a9c9#file-free_group-lean-L168</a></p>

#### [ Mario Carneiro (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236027):
<p>sure</p>

#### [ Kenny Lau (Apr 18 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236029):
<p>wonderful</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236035):
<p>I am currently using it to define add_group.smul</p>

#### [ Kenny Lau (Apr 18 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236036):
<p>I see</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236040):
<p>it makes it easy to transfer theorems from additive to multiplicative and vice versa using <code>additive</code></p>

#### [ Mario Carneiro (Apr 18 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236082):
<p>this method is in contrast with <code>transport_to_additive</code>, which translates the whole theorem to additive land</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236083):
<p>rather than just applying the theorem with a funny instance</p>

#### [ Kenny Lau (Apr 18 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236102):
<p>how does it know to transfer list.prod to list.sum :o</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236153):
<p>LOTS of definitional unfolding</p>

#### [ Kenny Lau (Apr 18 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236154):
<p>but not 1 to 0</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236156):
<p>I was surprised by the same thing</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236158):
<p>1 should go to 0</p>

#### [ Kenny Lau (Apr 18 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236200):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">sum</span><span class="bp">.</span><span class="n">sum</span> <span class="o">:</span> <span class="n">sum</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">sum</span> <span class="n">y</span> <span class="o">:=</span>
<span class="n">to_group</span><span class="bp">.</span><span class="n">mul</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">sum</span><span class="bp">.</span><span class="n">one</span> <span class="o">:</span> <span class="n">sum</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">free_group</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">to_group</span><span class="bp">.</span><span class="n">one</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">sum</span><span class="bp">.</span><span class="n">inv</span> <span class="o">:</span> <span class="n">sum</span> <span class="n">x</span><span class="bp">⁻¹</span> <span class="bp">=</span> <span class="bp">-</span><span class="n">sum</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">to_group</span><span class="bp">.</span><span class="n">inv</span>
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236202):
<p>the middle one errors</p>

#### [ Mario Carneiro (Apr 18 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236204):
<p>you may need to specify the type</p>

#### [ Kenny Lau (Apr 18 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236205):
<p>nvm, this worked</p>

#### [ Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236218):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">sum</span><span class="bp">.</span><span class="n">of</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">sum</span> <span class="o">(</span><span class="n">of</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">of</span>

<span class="kn">instance</span> <span class="n">sum</span><span class="bp">.</span><span class="n">is_group_hom</span> <span class="o">:</span> <span class="n">is_group_hom</span> <span class="o">(</span><span class="bp">@</span><span class="n">sum</span> <span class="n">α</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">is_group_hom</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">sum</span><span class="bp">.</span><span class="n">sum</span> <span class="o">:</span> <span class="n">sum</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">sum</span> <span class="n">y</span> <span class="o">:=</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">mul</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">sum</span><span class="bp">.</span><span class="n">one</span> <span class="o">:</span> <span class="n">sum</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">free_group</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">one</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">sum</span><span class="bp">.</span><span class="n">inv</span> <span class="o">:</span> <span class="n">sum</span> <span class="n">x</span><span class="bp">⁻¹</span> <span class="bp">=</span> <span class="bp">-</span><span class="n">sum</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">prod</span><span class="bp">.</span><span class="n">inv</span>
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236221):
<p>shortwiring everything to prod</p>

#### [ Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236222):
<p>did I say short wiring</p>

#### [ Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236223):
<p>I mean short-circuiting</p>

#### [ Kenny Lau (Apr 18 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125236224):
<p>I had to google for this one. my english.</p>

#### [ Kenny Lau (Apr 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125237946):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">group</span><span class="bp">.</span><span class="n">gen</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="err">$</span> <span class="bp">@</span><span class="n">free_group</span><span class="bp">.</span><span class="n">to_group</span> <span class="n">s</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">val</span>
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125237947):
<p>completely pointless usage</p>

#### [ Kenny Lau (Apr 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125237949):
<p>(I know we have <code>group.closure</code> already)</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238075):
<p>maybe you should prove this as a theorem about <code>group.closure</code> then</p>

#### [ Kenny Lau (Apr 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238076):
<p>fazendo :)</p>

#### [ Kenny Lau (Apr 18 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238144):
<p>what is the idiomatic way to use the fact that 1 is in a subgroup?</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238197):
<p>isn't that a theorem?</p>

#### [ Kenny Lau (Apr 18 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238199):
<p>what is the name?</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238200):
<p>presumably <code>is_subgroup.ome_mem</code> or similar</p>

#### [ Kenny Lau (Apr 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238201):
<p>it isn't</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238208):
<p>it should be a field of <code>is_submonoid</code></p>

#### [ Kenny Lau (Apr 18 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238209):
<p>it is</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238249):
<p>so <code>is_submonoid.one_mem s</code> then</p>

#### [ Kenny Lau (Apr 18 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238251):
<p>but it doesn't look idiomatic</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238255):
<p>the group files seem to open <code>is_submonoid</code> to clean it up a bit</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238305):
<p>I guess it could go in the root namespace, but <code>one_mem</code> sounds a bit generic</p>

#### [ Johannes Hölzl (Apr 18 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238364):
<p>I never used <code>export</code>, but maybe it works to <code>export is_submonoid</code>in <code>is_subgroup</code>?</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238453):
<p><code>export</code> is like permanent <code>open</code></p>

#### [ Mario Carneiro (Apr 18 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238454):
<p>for example, <code>option.some</code> is <code>export</code>ed</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238468):
<p>I don't think it's namespaced, but I could be wrong</p>

#### [ Kenny Lau (Apr 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238509):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">useless</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="bp">@</span><span class="n">free_group</span><span class="bp">.</span><span class="n">to_group</span> <span class="n">s</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">=</span> <span class="n">group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">z</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">rcases</span> <span class="n">h</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">subst</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">x</span><span class="o">,</span> <span class="n">clear</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">L</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">L</span> <span class="k">with</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span><span class="o">,</span>
    <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
    <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span>
    <span class="o">{</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">ih</span> <span class="err">⊢</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">rcases</span> <span class="n">hd</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="bp">_</span> <span class="bp">|</span> <span class="bp">_⟩</span><span class="o">,</span>
        <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="o">(</span><span class="n">group</span><span class="bp">.</span><span class="n">subset_closure</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">)]</span> <span class="o">},</span>
        <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">group</span><span class="bp">.</span><span class="n">subset_closure</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">]</span> <span class="o">}</span> <span class="o">},</span>
      <span class="o">{</span> <span class="n">assumption</span> <span class="o">}</span> <span class="o">}</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">H</span> <span class="k">with</span> <span class="n">x</span> <span class="n">H</span> <span class="n">x</span> <span class="n">H</span> <span class="n">ih</span> <span class="n">x1</span> <span class="n">x2</span> <span class="n">H1</span> <span class="n">H2</span> <span class="n">ih1</span> <span class="n">ih2</span><span class="o">,</span>
    <span class="n">case</span> <span class="n">group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">basic</span>
    <span class="o">{</span> <span class="n">existsi</span> <span class="o">(</span><span class="n">of</span> <span class="o">(</span><span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span> <span class="o">:</span> <span class="n">s</span><span class="o">)),</span>
      <span class="n">simp</span> <span class="o">},</span>
    <span class="n">case</span> <span class="n">group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">one</span>
    <span class="o">{</span> <span class="n">existsi</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">free_group</span> <span class="n">s</span><span class="o">),</span>
      <span class="n">simp</span> <span class="o">},</span>
    <span class="n">case</span> <span class="n">group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">inv</span>
    <span class="o">{</span> <span class="n">cases</span> <span class="n">ih</span> <span class="k">with</span> <span class="n">y</span> <span class="n">h</span><span class="o">,</span>
      <span class="n">existsi</span> <span class="n">y</span><span class="bp">⁻¹</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="o">},</span>
    <span class="n">case</span> <span class="n">group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">mul</span>
    <span class="o">{</span> <span class="n">cases</span> <span class="n">ih1</span> <span class="k">with</span> <span class="n">y1</span> <span class="n">h1</span><span class="o">,</span>
      <span class="n">cases</span> <span class="n">ih2</span> <span class="k">with</span> <span class="n">y2</span> <span class="n">h2</span><span class="o">,</span>
      <span class="n">existsi</span> <span class="n">y1</span> <span class="bp">*</span> <span class="n">y2</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="o">]</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 18 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238562):
<p>isn't there a more "universal" kind of proof?</p>

#### [ Kenny Lau (Apr 18 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238569):
<p>you're right</p>

#### [ Mario Carneiro (Apr 18 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125238570):
<p>both <code>group.closure</code> and <code>free_group.to_group</code> have universal properties</p>

#### [ Kenny Lau (Apr 18 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239184):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">red</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L</span> <span class="n">L</span>
<span class="bp">|</span> <span class="n">trans_bnot</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">x</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="o">(</span><span class="n">L₂</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₃</span><span class="o">)</span> <span class="bp">→</span> <span class="n">red</span> <span class="n">L₁</span> <span class="o">(</span><span class="n">L₂</span> <span class="bp">++</span> <span class="n">L₃</span><span class="o">)</span>

<span class="n">def</span> <span class="n">reduce</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cond</span> <span class="n">b1</span>
    <span class="o">(</span><span class="n">cond</span> <span class="n">b2</span>
      <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">reduce</span> <span class="err">$</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">))</span>
      <span class="o">(</span><span class="k">if</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span> <span class="k">then</span> <span class="n">reduce</span> <span class="n">tl</span> <span class="k">else</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">reduce</span> <span class="n">tl</span><span class="o">)))</span>
    <span class="o">(</span><span class="n">cond</span> <span class="n">b2</span>
      <span class="o">(</span><span class="k">if</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span> <span class="k">then</span> <span class="n">reduce</span> <span class="n">tl</span> <span class="k">else</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">reduce</span> <span class="n">tl</span><span class="o">))</span>
      <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">reduce</span> <span class="err">$</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">)))</span>
<span class="bp">|</span> <span class="n">L</span> <span class="o">:=</span> <span class="n">L</span>

<span class="kn">theorem</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">eq_of_red</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">reduce</span> <span class="n">L₁</span> <span class="bp">=</span> <span class="n">reduce</span> <span class="n">L₂</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239185):
<p>would you have some insights?</p>

#### [ Kenny Lau (Apr 18 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239187):
<p>on how to prove the theorem at the bottom?</p>

#### [ Kenny Lau (Apr 18 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239239):
<p>oh nvm I'll just use induction</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239247):
<p>you could use <code>b1 = b2</code> instead of four cases there</p>

#### [ Kenny Lau (Apr 18 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239306):
<p>I don't like unfolding <code>ite</code>s</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239308):
<p>I also played around with free_groups: <a href="https://gist.github.com/johoelzl/4238422b0810a9d04bb41cfdb682e8ff#file-free_groups-lean-L426" target="_blank" title="https://gist.github.com/johoelzl/4238422b0810a9d04bb41cfdb682e8ff#file-free_groups-lean-L426">https://gist.github.com/johoelzl/4238422b0810a9d04bb41cfdb682e8ff#file-free_groups-lean-L426</a> <br>
Now it includes <code>normalize</code>.</p>

#### [ Kenny Lau (Apr 18 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239309):
<p>you win</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239310):
<p>Using <code>if _ then _ else _ </code> makes <code>normalize.step</code> much smaller.</p>

#### [ Kenny Lau (Apr 18 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239333):
<p>aha, I like your approach</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239336):
<p>you use <code>list.sizeof</code>? Why?</p>

#### [ Kenny Lau (Apr 18 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239337):
<p>do it one step first, and then the whole thing</p>

#### [ Kenny Lau (Apr 18 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239343):
<p>now I'm confused as to what I should do</p>

#### [ Kenny Lau (Apr 18 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239400):
<blockquote>
<p>you use <code>list.sizeof</code>? Why?</p>
</blockquote>
<p>to justify that the recursion is well-founded?</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239403):
<p>I never used well founded recursion before. <code>list.sizeof</code> was what the equation compiler proposed. Is there an easier way?</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239431):
<p>You (Johannes) didn't prove that <code>normalize</code> is related to the original input though, or that the result is unique in the equivalence class (it can be defined as a function on the free group itself)</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239434):
<p>so there's that if you want it kenny</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239435):
<p>well its not finished yet</p>

#### [ Kenny Lau (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239437):
<p>this is not good</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239439):
<p>You can use <code>list.length</code> instead of <code>sizeof</code></p>

#### [ Kenny Lau (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239440):
<p>we are writing our own free groups separately</p>

#### [ Kenny Lau (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239443):
<p>this is not good</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239445):
<p>they seem pretty similar</p>

#### [ Kenny Lau (Apr 18 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239514):
<p>they're different enough</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239515):
<p>I'm sure we ca merge them later</p>

#### [ Kenny Lau (Apr 18 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239518):
<p>I don't believe in hope</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239525):
<p>Oh, I see Johannes also proved church rosser</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239587):
<p>Yeah, the question was how to prove it. And then I couldn't sleep and remembered Tobias book on Term Rewriting and All That.</p>

#### [ Kenny Lau (Apr 18 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239601):
<p>this is not good</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239603):
<p>you should see how it compares to Kenny's proof</p>

#### [ Kenny Lau (Apr 18 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239607):
<p>I'm ashamed</p>

#### [ Kenny Lau (Apr 18 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239609):
<p>I need to work very hard to shorten my proof</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239678):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> why not incorporate both proofs? I think merging both would be helpful.</p>

#### [ Kenny Lau (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239686):
<p>our proofs are different enough</p>

#### [ Kenny Lau (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239688):
<p>our definitions are different enough</p>

#### [ Kenny Lau (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239689):
<p>this will be a disaster</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239696):
<p>they aren't that different, if I'm following the discussion well enough</p>

#### [ Kenny Lau (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239698):
<p>you haven't even seen my file</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239701):
<p>I am reading it from your posts</p>

#### [ Kenny Lau (Apr 18 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239702):
<p>I can see that</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239749):
<p>Why don't you post what you have and then we can compare and see what parts are better in each file?</p>

#### [ Kenny Lau (Apr 18 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239752):
<p>lemme finish my <code>reduce</code> first</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239810):
<p>here's what I use to do induction on <code>length</code>:</p>
<div class="codehilite"><pre><span></span>using_well_founded {
  rel_tac := λ_ _, `[exact ⟨_, inv_image.wf length nat.lt_wf⟩],
  dec_tac := tactic.assumption }
</pre></div>

#### [ Johannes Hölzl (Apr 18 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239813):
<p>Ah! that's perfect</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239886):
<p>I guess what we also want: a induction method which generalizes all indices of the major hypotheses. I often needed to write something like this:</p>
<div class="codehilite"><pre><span></span><span class="n">revert</span> <span class="n">h</span><span class="o">,</span>
<span class="n">generalize</span> <span class="n">eq_t</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">xs</span><span class="o">)</span> <span class="bp">=</span> <span class="n">t</span><span class="o">,</span>
<span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
<span class="n">induction</span> <span class="n">h</span><span class="o">,</span>
<span class="bp">...</span>
</pre></div>


<p>Or is there a better variant already available?</p>

#### [ Kenny Lau (Apr 18 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239899):
<p>same here</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239965):
<p>I recall discussing this with Sebastian. The problem with this is that it often cripples the inductive hypothesis (since the index can't get smaller or whatever), and it's hard to say what to generalize to recover it</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125239973):
<p>which makes it unclear how to proceed in general</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240027):
<p>I see. We surely don't want to do it in all cases. But something along the lines <code>induction h generalizing (t_eq : (a :: xs) = t)</code>. At least would be shorter to write.</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240082):
<p>hm, I guess there's no point in the <code>t</code> there since it will disappear after the induction. The form of the index is also unnecessary, unless you only want to generalize some indices and leave other index expressions</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240093):
<p>So it would suffice to just say <code>generalizing indices</code> or something</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240158):
<p>or equivalently, just have a <code>induction_g</code> command (name TBD) with the same syntax as <code>induction</code> that does this</p>

#### [ Kenny Lau (Apr 18 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240172):
<p>how do you destruct ite in equation compiler?</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240255):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm fine with <code>induction_g</code> or <code>generalizing indices</code>. I will take a look into this.</p>

#### [ Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240296):
<p>how do you destruct ite in term mode at all?</p>

#### [ Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240297):
<p>I recall asking this a long time ago</p>

#### [ Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240298):
<p>I can only destruct it in tactic mode</p>

#### [ Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240305):
<p>because it is <code>decidable.rec_on</code> something obscure</p>

#### [ Kenny Lau (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240307):
<p>i.e. a proof that the condition is decidable</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240308):
<p>it's easier in tactic mode to be sure</p>

#### [ Johannes Hölzl (Apr 18 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240310):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> do you mean rewriting with "destruct"? This is surely one thing where tactic mode is prefered.</p>

#### [ Kenny Lau (Apr 18 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240327):
<p>that's why I don't like using <code>ite</code></p>

#### [ Mario Carneiro (Apr 18 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240330):
<p>but you can <code>match (by apply_instance : decidable p) with ...</code> and then just use <code>show</code> to get rid of the ite in the branches</p>

#### [ Kenny Lau (Apr 18 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240342):
<p>hmm</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240394):
<p>this is what I used to do before <code>by_cases</code> got good</p>

#### [ Kenny Lau (Apr 18 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240545):
<p>I've got myself into certain trouble</p>

#### [ Kenny Lau (Apr 18 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240549):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">reduce</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cond</span> <span class="n">b1</span>
    <span class="o">(</span><span class="n">cond</span> <span class="n">b2</span>
      <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">reduce</span> <span class="err">$</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">))</span>
      <span class="o">(</span><span class="k">if</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span> <span class="k">then</span> <span class="n">reduce</span> <span class="n">tl</span> <span class="k">else</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">reduce</span> <span class="n">tl</span><span class="o">)))</span>
    <span class="o">(</span><span class="n">cond</span> <span class="n">b2</span>
      <span class="o">(</span><span class="k">if</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span> <span class="k">then</span> <span class="n">reduce</span> <span class="n">tl</span> <span class="k">else</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">reduce</span> <span class="n">tl</span><span class="o">))</span>
      <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">b1</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">reduce</span> <span class="err">$</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">)))</span>
<span class="bp">|</span> <span class="n">L</span> <span class="o">:=</span> <span class="n">L</span>

<span class="err">⊢</span> <span class="n">reduce</span> <span class="o">(</span><span class="n">L2</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L3</span><span class="o">)</span> <span class="bp">=</span> <span class="n">reduce</span> <span class="o">(</span><span class="n">L2</span> <span class="bp">++</span> <span class="n">L3</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 18 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240590):
<p>do you still have that church rosser proof?</p>

#### [ Kenny Lau (Apr 18 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240601):
<p>yes</p>

#### [ Kenny Lau (Apr 18 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240602):
<div class="codehilite"><pre><span></span><span class="n">church_rosser</span> <span class="o">:</span> <span class="n">red</span> <span class="err">?</span><span class="n">M_2</span> <span class="err">?</span><span class="n">M_3</span> <span class="bp">→</span> <span class="n">red</span> <span class="err">?</span><span class="n">M_2</span> <span class="err">?</span><span class="n">M_4</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="err">?</span><span class="n">M_1</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)),</span> <span class="n">red</span> <span class="err">?</span><span class="n">M_3</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span> <span class="err">?</span><span class="n">M_4</span> <span class="n">L₄</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 18 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240603):
<p>It suffices to show that reduce is following <em>some</em> reduction sequence</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240609):
<p>and that when it gets to the end there is no other possible reduction</p>

#### [ Kenny Lau (Apr 18 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240611):
<p>I've shown the former</p>

#### [ Kenny Lau (Apr 18 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240657):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">min</span> <span class="o">:</span> <span class="n">red</span> <span class="o">(</span><span class="n">reduce</span> <span class="n">L₁</span><span class="o">)</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="n">reduce</span> <span class="n">L₁</span> <span class="bp">=</span> <span class="n">L₂</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240658):
<p>issue?</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240660):
<p>Then if A ~ B then reduce A ~ A ~ B ~ reduce B, so by C-R there exists C such that reduce A -&gt; C &lt;- reduce B; but reduce A is minimal so reduce A = C = reduce B</p>

#### [ Kenny Lau (Apr 18 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240670):
<p>nice</p>

#### [ Kenny Lau (Apr 18 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240723):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> which list should I destruct?</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240725):
<p>where</p>

#### [ Kenny Lau (Apr 18 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240727):
<p>common sense would say the former, but I'm asking if I need to destruct the latter as well</p>

#### [ Kenny Lau (Apr 18 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240730):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">min</span> <span class="o">:</span> <span class="n">red</span> <span class="o">(</span><span class="n">reduce</span> <span class="n">L₁</span><span class="o">)</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="n">reduce</span> <span class="n">L₁</span> <span class="bp">=</span> <span class="n">L₂</span> <span class="o">:=</span>
</pre></div>

#### [ Mario Carneiro (Apr 18 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240741):
<p><code>red</code> means that you have some representation as append of stuff, right?</p>

#### [ Kenny Lau (Apr 18 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240744):
<p>not sure what you mean; don't think it's right anyway</p>

#### [ Kenny Lau (Apr 18 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240785):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">red</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L</span> <span class="n">L</span>
<span class="bp">|</span> <span class="n">trans_bnot</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">x</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="o">(</span><span class="n">L₂</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₃</span><span class="o">)</span> <span class="bp">→</span> <span class="n">red</span> <span class="n">L₁</span> <span class="o">(</span><span class="n">L₂</span> <span class="bp">++</span> <span class="n">L₃</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 18 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240786):
<p>I think you want to do induction on L1, along the same lines as the definition of <code>reduce</code></p>

#### [ Kenny Lau (Apr 18 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240787):
<p>right, but I'm asking if I need to destruct L2 as well</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240793):
<p>no, generalize it in the induction</p>

#### [ Kenny Lau (Apr 18 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240796):
<p>why shouldn't I do it in term mode?</p>

#### [ Mario Carneiro (Apr 18 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125240797):
<p>you can</p>

#### [ Kenny Lau (Apr 18 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241458):
<p>I give up using term mode</p>

#### [ Mario Carneiro (Apr 18 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241867):
<p>Here's a proof strategy: if <code>red (reduce L1) L2</code>, then by cases either <code>reduce L1 = L2</code> or <code>reduce L1 = L3 ++ (x, b) :: (x, bnot b) :: L4</code> and <code>L2 = L3 ++ L4</code>; so it suffices to prove the second case is impossible. Prove <code>\forall L3 L4 x b, reduce L1 != L3 ++ (x, b) :: (x, bnot b) :: L4</code> by induction on L1, which you can do in term mode so that the equation compiler sets up the weird induction</p>

#### [ Kenny Lau (Apr 18 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241913):
<p>aha</p>

#### [ Kenny Lau (Apr 18 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241914):
<p>muit obrigad</p>

#### [ Kenny Lau (Apr 18 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241923):
<p>that will be the first "not" I'm using in a while</p>

#### [ Kenny Lau (Apr 18 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125241976):
<p>are you sure I can do that by induction on L1 alone?</p>

#### [ Kenny Lau (Apr 18 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243339):
<p>my function is wrong</p>

#### [ Kenny Lau (Apr 18 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243343):
<p>hmm...</p>

#### [ Kenny Lau (Apr 18 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243417):
<p>reducing a word is more difficult than it seems</p>

#### [ Kenny Lau (Apr 18 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243624):
<p>I don't think there's an online algorithm to reduce a word</p>

#### [ Kenny Lau (Apr 18 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243629):
<p>so my function is bound to fail</p>

#### [ Kenny Lau (Apr 18 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243632):
<p>I'm using the CS usage of "online"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243809):
<p>just use greedy?</p>

#### [ Kenny Lau (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243849):
<p>is your greedy algorithm online?</p>

#### [ Kevin Buzzard (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243850):
<p>and remember to backtrack slightly when you kill <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∗</mo><msup><mi>x</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup></mrow><annotation encoding="application/x-tex">x * x^{-1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span><span class="mbin">∗</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Kenny Lau (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243851):
<p>right, that's my new plan now</p>

#### [ Kenny Lau (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243852):
<p>how am I writing program in Lean</p>

#### [ Kevin Buzzard (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243854):
<p>...when you should be revising?</p>

#### [ Kenny Lau (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243856):
<p>well</p>

#### [ Kevin Buzzard (Apr 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125243857):
<p>;-)</p>

#### [ Kevin Buzzard (Apr 18 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244111):
<blockquote>
<p>this will be a disaster</p>
</blockquote>
<p>No, it's great! Two smart people doing the same thing means that you can take the union of their ideas at the end -- either that, or you get two different ways of doing the same thing, each with their own benefits. Either way it's a win.</p>

#### [ Kenny Lau (Apr 18 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244117):
<p>there will be only one version in mathlib</p>

#### [ Kevin Buzzard (Apr 18 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244165):
<p>If the two approaches are sufficiently different and both have their uses, then they might both end up in there. If they are sufficiently similar then we end up with the best of both pieces of code. It's just a collaborative open source situation. I ask 200 people to do the same question when I'm teaching them and I don't worry about this at all. Every year I see an answer I haven't seen before, e.g. Chris' modal logic proof of the islanders question this year.</p>

#### [ Kenny Lau (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244170):
<p>there can't be two definitions of a free group</p>

#### [ Kevin Buzzard (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244173):
<p>There is generate and span</p>

#### [ Kevin Buzzard (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244175):
<p>two definitions of the submodule generated/spanned by a subset</p>

#### [ Kenny Lau (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244176):
<p>in my files</p>

#### [ Kenny Lau (Apr 18 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244181):
<p>only span is in mathlib</p>

#### [ Kenny Lau (Apr 18 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244346):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">L</span> <span class="o">[]</span> <span class="o">:=</span> <span class="n">L</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">(</span><span class="n">h</span><span class="bp">::</span><span class="n">t</span><span class="o">)</span> <span class="o">:=</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="n">t</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">tt</span><span class="o">)</span><span class="bp">::</span><span class="n">tl1</span><span class="o">)</span> <span class="o">((</span><span class="n">x2</span><span class="o">,</span><span class="n">tt</span><span class="o">)</span><span class="bp">::</span><span class="n">tl2</span><span class="o">)</span> <span class="o">:=</span>
    <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">((</span><span class="n">x2</span><span class="o">,</span><span class="n">tt</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x1</span><span class="o">,</span><span class="n">tt</span><span class="o">)</span><span class="bp">::</span><span class="n">tl1</span><span class="o">)</span> <span class="n">tl2</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">tt</span><span class="o">)</span><span class="bp">::</span><span class="n">tl1</span><span class="o">)</span> <span class="o">((</span><span class="n">x2</span><span class="o">,</span><span class="n">ff</span><span class="o">)</span><span class="bp">::</span><span class="n">tl2</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">if</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span>
    <span class="k">then</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="n">tl1</span> <span class="n">tl2</span>
    <span class="k">else</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">((</span><span class="n">x2</span><span class="o">,</span><span class="n">ff</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x1</span><span class="o">,</span><span class="n">tt</span><span class="o">)</span><span class="bp">::</span><span class="n">tl1</span><span class="o">)</span> <span class="n">tl2</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">ff</span><span class="o">)</span><span class="bp">::</span><span class="n">tl1</span><span class="o">)</span> <span class="o">((</span><span class="n">x2</span><span class="o">,</span><span class="n">tt</span><span class="o">)</span><span class="bp">::</span><span class="n">tl2</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">if</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span>
    <span class="k">then</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="n">tl1</span> <span class="n">tl2</span>
    <span class="k">else</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">((</span><span class="n">x2</span><span class="o">,</span><span class="n">tt</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x1</span><span class="o">,</span><span class="n">ff</span><span class="o">)</span><span class="bp">::</span><span class="n">tl1</span><span class="o">)</span> <span class="n">tl2</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x1</span><span class="o">,</span><span class="n">ff</span><span class="o">)</span><span class="bp">::</span><span class="n">tl1</span><span class="o">)</span> <span class="o">((</span><span class="n">x2</span><span class="o">,</span><span class="n">ff</span><span class="o">)</span><span class="bp">::</span><span class="n">tl2</span><span class="o">)</span> <span class="o">:=</span>
    <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">((</span><span class="n">x2</span><span class="o">,</span><span class="n">ff</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x1</span><span class="o">,</span><span class="n">ff</span><span class="o">)</span><span class="bp">::</span><span class="n">tl1</span><span class="o">)</span> <span class="n">tl2</span>

<span class="n">def</span> <span class="n">reduce</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">))</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">[]</span> <span class="n">L</span><span class="o">)</span><span class="bp">.</span><span class="n">reverse</span>
</pre></div>

#### [ Kenny Lau (Apr 18 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244347):
<p>this should be correct</p>

#### [ Kenny Lau (Apr 18 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125244461):
<p>but it would be difficult to prove anything about it</p>

#### [ Kevin Buzzard (Apr 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254855):
<p>heh</p>

#### [ Kevin Buzzard (Apr 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254858):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">is_comm_ring_hom</span><span class="bp">.</span><span class="n">id</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">map_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span><span class="n">rfl</span><span class="o">,</span><span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span><span class="n">rfl</span><span class="o">,</span><span class="n">map_one</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254868):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> could you add this to mathlib? ;-)</p>

#### [ Kevin Buzzard (Apr 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254923):
<p>Or tell me where to put it.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254943):
<p>in ring.lean, just after definition of is_ring_hom?</p>

#### [ Kevin Buzzard (Apr 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125254960):
<p>Is there a better proof? Some "meta-rfl" tactic?</p>

#### [ Patrick Massot (Apr 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255008):
<p>Sounds like a job for Scott's <code>obviously</code> tactic</p>

#### [ Patrick Massot (Apr 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255033):
<p>but it's not yet in mathlib</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255041):
<p>Patrick, this is what the world has come to. Kenny has defined localization maps and of course there are equivalence classes everywhere, and I'm not very experienced with using them. But Kenny has written a sufficiently good interface (universal properties of localization, basically guided by the needs I had for schemes) that I can work with localizations without ever needing to think about quotient types.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255053):
<p>So I need to prove that the canonical map R[1/S] -&gt; R[1/S] is the identity map</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255113):
<p>and I can either attempt to do this by unravelling the definition and getting my hands dirty</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255123):
<p>or I can do it by observing that the identity map is an R-algebra homomorphism R[1/S] -&gt; R[1/S] and hence it's the canonical map, by some universal property :P</p>

#### [ Patrick Massot (Apr 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255126):
<p>one could also take this as an exercise in tactic writing: write a tactic doing that kind of proof that <code>id</code> is a morphism of anything (this should be easy after reading <span class="user-mention" data-user-id="110026">@Simon Hudon</span> 's tutorial about how he wrote the pi instance tactic)</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255147):
<p>and because I don't like quotient types I will use the universal property.</p>

#### [ Patrick Massot (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255155):
<p>Nice</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255159):
<p>And I think this shows exactly the point that Mario was explaining to me the other day.</p>

#### [ Patrick Massot (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255176):
<p>About interfaces?</p>

#### [ Patrick Massot (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255179):
<p>Yes</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255182):
<p>If the interface (which he did actually describe as "a bunch of universal properties" at the time) is good enough</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255185):
<p>then you don't ever need to worry about the details</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255226):
<p>of how it is implemented</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255247):
<p>and indeed I can believe that any direct proof that it's the identity might break if some underlying way of implementing equivalence relations changed</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255255):
<p>but my universal property definition will never break</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255257):
<p>That is crazy.</p>

#### [ Patrick Massot (Apr 18 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255279):
<p>yes, it's great</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255306):
<p>tactic tutorial did you say??</p>

#### [ Patrick Massot (Apr 18 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255358):
<p>I think maths papers should also be written like this. Many math papers lack encapsulation of technical details</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255370):
<p>I don't know if we are the mad ones or the sane ones</p>

#### [ Patrick Massot (Apr 18 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255385):
<p>Yes, Simon is writing some tutorial</p>

#### [ Patrick Massot (Apr 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255395):
<p>Or at least he intends to do it, and I remind him from time to time.</p>

#### [ Patrick Massot (Apr 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255407):
<p>Which is really unfair because I lack time for all my Lean projects</p>

#### [ Patrick Massot (Apr 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255426):
<p>But in three weeks I'll be done with teaching and I hope I'll be able to work more seriously on Lean stuff</p>

#### [ Sean Leather (Apr 18 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255520):
<blockquote>
<p>If the interface (which he did actually describe as "a bunch of universal properties" at the time) is good enough<br>
then you don't ever need to worry about the details<br>
of how it is implemented</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think I agree with this. But, just for my education, what is the definition of “universal” here?</p>

#### [ Patrick Massot (Apr 18 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255607):
<p>I'm giving a graduate course and tomorrow and next lecture are about <a href="https://arxiv.org/abs/1201.2245" target="_blank" title="https://arxiv.org/abs/1201.2245">https://arxiv.org/abs/1201.2245</a> And a new version came out on arXiv on Monday, after five years without moving. Since then I've been reading like crazy to understand why she changed so many things</p>

#### [ Patrick Massot (Apr 18 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255629):
<p>Good news is the new version contains something which is much closer to an actual proof of the main theorem</p>

#### [ Patrick Massot (Apr 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255687):
<p>But that doesn't leave much time for Lean</p>

#### [ Patrick Massot (Apr 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255757):
<p>Sean: <a href="https://en.wikipedia.org/wiki/Universal_property" target="_blank" title="https://en.wikipedia.org/wiki/Universal_property">https://en.wikipedia.org/wiki/Universal_property</a></p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255801):
<p>Sean -- I asked Kenny to type up some basic constructions of localization of rings at multiplicative sets in Lean. Kenny read a book on commutative algebra and did it</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255811):
<p>I then realised I couldn't use his constructions at all because to access any element of the localized ring I needed to start playing around with quotient types</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255845):
<p>so I asked him if he could also prove various results of the form "if some situation is true, then there's a map from some ring to a localized ring"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255848):
<p>or "if some situation is true, then there's a map from a localized ring to some ring"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255849):
<p>and he did this</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255853):
<p>and then I realised that I still couldn't prove half the things I wanted to prove</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255911):
<p>so I asked him if he could prove various results of the form "if some situation is true, then there's a map from some ring to some localized ring and furthermore it is the unique map with some property"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255915):
<p>and similarly the other way around</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255920):
<p>and then I could prove everything I needed</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255922):
<p>but then to my surprise</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255938):
<p>I realised that statements of the form "this map that Kenny defined is the identity map"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255941):
<p>which I needed to prove</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125255953):
<p>even such statements as that, which my gut instinct said "this proof should be refl"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256011):
<p>I realised I was proving by showing that the identity map had the property required of Kenny's map, and hence was Kenny's map</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256017):
<p>and this has had the joyous consequence</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256020):
<p>that I never once have to write an equivalence class</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256021):
<p>which is great</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256023):
<p>because I don't know if it's just me</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256029):
<p>but whenever I type <code>\[[</code> it doesn't work properly</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256036):
<p>I get <code>\[[]]</code></p>

#### [ Kenny Lau (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256042):
<p>so you manually delete the extra closing brackets and press space to enter it</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256053):
<p>instead of <code>⟦</code></p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256058):
<p>aah, you are an equivalence relation expert</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256064):
<p>instead of doing that</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256068):
<p>I get you to write me an interface ;-)</p>

#### [ Sean Leather (Apr 18 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256142):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> So, am I right in that you are describing a sort of minimum set of properties for a given definition that allow you to prove something without having to unfold the given definition?</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256146):
<p>right</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256204):
<p>but somehow in the past I knew that this sort of thing was sometimes possible</p>

#### [ Sean Leather (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256208):
<p>That's what I thought. Is that the same thing as <a href="https://en.wikipedia.org/wiki/Universal_property" target="_blank" title="https://en.wikipedia.org/wiki/Universal_property">https://en.wikipedia.org/wiki/Universal_property</a> as <span class="user-mention" data-user-id="110031">@Patrick Massot</span> referred to? I didn't think so.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256211):
<p>but when it came to the identity map, I didn't care</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256219):
<p>because "one can easily check that this map is the identity map from the construction"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256226):
<p>at least, I would not be scared to write that in a maths paper</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256230):
<p>but in this situation I am so scared to prove anything directly from the construction</p>

#### [ Patrick Massot (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256240):
<p>Kevin, that's also the same idea in <a href="#narrow/stream/113488-general/subject/.60_.60.20style.20and.20order.20of.20goals/near/125119384" title="#narrow/stream/113488-general/subject/.60_.60.20style.20and.20order.20of.20goals/near/125119384">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.60_.60.20style.20and.20order.20of.20goals/near/125119384</a></p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256243):
<p>that it has only now dawned on me that even trivial things which I would usually prove directly from the construction can be done via the interface</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256246):
<p>Oh is it?</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256248):
<p>I didn't understand that comment</p>

#### [ Patrick Massot (Apr 18 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256256):
<p>I guessed so, that's why I'm referring to it now</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256297):
<p>That comment is starred for "come back to this when your daughter is not off school sick"</p>

#### [ Patrick Massot (Apr 18 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256299):
<p>I'm talking about the first bullet</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256318):
<p>I kind of think/hope that the general technique I picked up when working on those proofs was the thing Mario was trying to explain to me there</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256330):
<p>but I've not had time to internalise it yet.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256336):
<p>I can really see the light at the end of the tunnel for affine schemes now.</p>

#### [ Patrick Massot (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256346):
<p>Great!</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256348):
<p>Chris did the ghastly ring theory multinomial theorem lemma which I was putting off</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256394):
<p>and what is left, I believe, is the kind of mathematics which is really good fun to type into Lean</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256403):
<p>i.e. it's just universal property after universal property</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256425):
<p>The last 5 theorems I proved had proofs of the form <code>name_of_universal_property_theorem _ _ _ _</code></p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256441):
<p>i.e. exactly what one would write in mathematics:</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256446):
<p>"this follows from the universal property"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256456):
<p>except that one failed because Lean didn't know the identity was a ring hom ;-)</p>

#### [ Simon Hudon (Apr 18 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256511):
<p>Have I already published the tutorial?</p>

#### [ Patrick Massot (Apr 18 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256532):
<p>Not yet</p>

#### [ Patrick Massot (Apr 18 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256533):
<p>You are about to do it</p>

#### [ Simon Hudon (Apr 18 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125256542):
<p>Oh! Thanks for keeping me up-to-date!</p>

#### [ Kenny Lau (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267684):
<p>Done!</p>

#### [ Kenny Lau (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267686):
<p><a href="https://github.com/kckennylau/Lean/blob/master/free_group.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/free_group.lean">https://github.com/kckennylau/Lean/blob/master/free_group.lean</a></p>

#### [ Kenny Lau (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267689):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you see how to shorten my proofs?</p>

#### [ Kenny Lau (Apr 18 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267750):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span></p>

#### [ Johannes Hölzl (Apr 18 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125267882):
<p>What helped in my approach: not using <code>setoid</code> and <code>quotient</code> but <code>quot</code>. Also I introduced a <code>refl_trans</code> and <code>refl_cl</code> to handle the relations and a general version of Church-Rosser. I guess using <code>append_eq_append_iff</code>, together with <code>case_matching*</code> was useful automation.</p>

#### [ Johannes Hölzl (Apr 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125268207):
<p>I don't combine the transitive closure and the reduction relation.</p>

#### [ Kenny Lau (Apr 19 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290928):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do we mind reversing the direction of <code>red</code> to conform with wf conventions?</p>

#### [ Johannes Hölzl (Apr 19 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290929):
<p>no</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290933):
<p>I'm disinclined to because it would break reduction conventions</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290939):
<p>i.e. church rosser is completely different the other way around</p>

#### [ Kenny Lau (Apr 19 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290943):
<p>the automater doesn’t work well though</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290944):
<p>(it's called something like noetherian in this case)</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290988):
<p>If you use <code>tactic.assumption</code> as the discharger, it should reduce the <code>swap</code></p>

#### [ Mario Carneiro (Apr 19 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125290990):
<p>you could also state your hypothesis with <code>swap</code></p>

#### [ Kenny Lau (Apr 19 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291017):
<p>this is the problem</p>

#### [ Kenny Lau (Apr 19 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291018):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">bnot</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">x</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span><span class="o">)</span>

<span class="kn">inductive</span> <span class="n">red</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L</span> <span class="n">L</span>
<span class="bp">|</span> <span class="n">trans_step</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">free_group</span><span class="bp">.</span><span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">)</span> <span class="o">:</span>
    <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₃</span>
</pre></div>

#### [ Kenny Lau (Apr 19 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291019):
<p>so I defined things like this</p>

#### [ Kenny Lau (Apr 19 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291060):
<p>now I'm in this stage:</p>
<div class="codehilite"><pre><span></span><span class="n">H1</span> <span class="o">:</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L2</span> <span class="n">L₂</span><span class="o">,</span>
<span class="n">H2</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L2</span>
</pre></div>

#### [ Kenny Lau (Apr 19 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291064):
<p>so if I want to prove something with <code>L₁</code> and <code>L₂</code>, then I would recursion on <code>H2</code> right</p>

#### [ Kenny Lau (Apr 19 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291073):
<p>then somehow the automater wants me to prove this:</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">function</span><span class="bp">.</span><span class="n">swap</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₁</span> <span class="n">L₁</span>
</pre></div>

#### [ Mario Carneiro (Apr 19 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291111):
<p>What is the setup of your induction?</p>

#### [ Kenny Lau (Apr 19 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291122):
<p>I want to prove that red L1 L2 -&gt; red (inv L1) (inv L2)</p>

#### [ Kenny Lau (Apr 19 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291130):
<p>I’m starting to believe that my approach won’t work because it’s in the wrong direction</p>

#### [ Kenny Lau (Apr 19 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125291252):
<p>I’ll just define red differently then</p>

#### [ Kenny Lau (Apr 19 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125304550):
<p>I have renamed this thread to "free group"</p>

#### [ Kenny Lau (Apr 19 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125304556):
<p>in other news, I shortened the file a bit more: <a href="https://github.com/kckennylau/Lean/blob/master/free_group.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/free_group.lean">https://github.com/kckennylau/Lean/blob/master/free_group.lean</a></p>

#### [ Kenny Lau (Apr 19 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125304562):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> could you have a look?</p>

#### [ Kenny Lau (Apr 19 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125304769):
<p>not a single negation in my file :P</p>

#### [ Johannes Hölzl (Apr 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306426):
<p>Just looking at the proof: it looks like <code>red.step.church_rosser</code> could be made smaller by wlog after the case <code>list.prefix_or_prefix_of_append_eq_append </code>? At least the proof structure looks very similar.</p>

#### [ Kenny Lau (Apr 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306474):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I just shortened red.step.church_rosser by 10 lines</p>

#### [ Kenny Lau (Apr 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306477):
<p>now it spans 34 lines and does not depend on <code>list.prefix_or_prefix_of_append_eq_append</code></p>

#### [ Kenny Lau (Apr 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306478):
<p>I feel good</p>

#### [ Johannes Hölzl (Apr 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306483):
<p>nice</p>

#### [ Kenny Lau (Apr 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306484):
<p>this means I can now convert it to equation compiler and save more lines</p>

#### [ Kenny Lau (Apr 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306553):
<blockquote>
<p>Just looking at the proof: it looks like <code>red.step.church_rosser</code> could be made smaller by wlog after the case <code>list.prefix_or_prefix_of_append_eq_append </code>? At least the proof structure looks very similar.</p>
</blockquote>
<p>right, but I just can't find a way for wlog to work</p>

#### [ Kenny Lau (Apr 19 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306564):
<p><a href="#narrow/stream/113488-general/topic/wlog.20example" title="#narrow/stream/113488-general/topic/wlog.20example">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog.20example</a></p>

#### [ Kenny Lau (Apr 19 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306566):
<p>nobody replied</p>

#### [ Johannes Hölzl (Apr 19 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306654):
<p>I didn't mean to use directly the <code>wlog</code> tactic. I meant to do the following: state the theorem, and use it to proof one direction, and then the second one by the corresponding application of symmetry and AC (associativity and commutativity of append, and etc)</p>

#### [ Kenny Lau (Apr 19 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306704):
<p>that's disgusting</p>

#### [ Kenny Lau (Apr 19 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306709):
<p>I would rather wait for them to fix wlog</p>

#### [ Kenny Lau (Apr 19 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306788):
<div class="codehilite"><pre><span></span><span class="o">{</span> <span class="n">injections</span><span class="o">,</span> <span class="n">subst_vars</span><span class="o">,</span> <span class="n">simp</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Apr 19 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306791):
<p>I used this so much, this should be a tactic</p>

#### [ Johannes Hölzl (Apr 19 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306820):
<p>What? Why is it <strong>disgusting</strong>? That's how you do it. You can work on changing wlog yourself!</p>

#### [ Kenny Lau (Apr 19 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125306844):
<p>anyway</p>

#### [ Kenny Lau (Apr 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308690):
<p>13 lines lost!</p>

#### [ Kenny Lau (Apr 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308693):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">church_rosser</span><span class="bp">.</span><span class="n">aux2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)}</span> <span class="o">{</span><span class="n">x1</span> <span class="n">b1</span> <span class="n">x2</span> <span class="n">b2</span><span class="o">},</span>
  <span class="n">L₁</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₂</span> <span class="bp">=</span> <span class="n">L₃</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b2</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₄</span> <span class="bp">→</span>
  <span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span> <span class="bp">=</span> <span class="n">L₃</span> <span class="bp">++</span> <span class="n">L₄</span> <span class="bp">∨</span> <span class="bp">∃</span> <span class="n">L₅</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span><span class="o">)</span> <span class="n">L₅</span> <span class="bp">∧</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="o">(</span><span class="n">L₃</span> <span class="bp">++</span> <span class="n">L₄</span><span class="o">)</span> <span class="n">L₅</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="bp">_</span> <span class="o">[]</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span>  <span class="o">:=</span>
  <span class="k">by</span> <span class="n">injections</span><span class="bp">;</span> <span class="n">subst_vars</span><span class="bp">;</span> <span class="n">simp</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="bp">_</span> <span class="o">[(</span><span class="n">x3</span><span class="o">,</span><span class="n">b3</span><span class="o">)]</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">injections</span><span class="bp">;</span> <span class="n">subst_vars</span><span class="bp">;</span> <span class="n">simp</span>
<span class="bp">|</span> <span class="o">[(</span><span class="n">x3</span><span class="o">,</span><span class="n">b3</span><span class="o">)]</span> <span class="bp">_</span> <span class="o">[]</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">injections</span><span class="bp">;</span> <span class="n">subst_vars</span><span class="bp">;</span> <span class="n">simp</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="bp">_</span> <span class="o">((</span><span class="n">x3</span><span class="o">,</span><span class="n">b3</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x4</span><span class="o">,</span><span class="n">b4</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">injections</span><span class="bp">;</span> <span class="n">subst_vars</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">right</span><span class="bp">;</span> <span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">bnot</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">cons_bnot</span><span class="bp">⟩</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x3</span><span class="o">,</span><span class="n">b3</span><span class="o">)</span><span class="bp">::</span><span class="o">(</span><span class="n">x4</span><span class="o">,</span><span class="n">b4</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span> <span class="bp">_</span> <span class="o">[]</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="o">:=</span>
  <span class="k">by</span> <span class="n">injections</span><span class="bp">;</span> <span class="n">subst_vars</span><span class="bp">;</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">right</span><span class="bp">;</span> <span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">cons_bnot</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">bnot</span><span class="bp">⟩</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x3</span><span class="o">,</span><span class="n">b3</span><span class="o">)</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span> <span class="bp">_</span> <span class="o">((</span><span class="n">x4</span><span class="o">,</span><span class="n">b4</span><span class="o">)</span><span class="bp">::</span><span class="n">tl2</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="bp">⟨</span><span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="bp">.</span><span class="n">inj</span> <span class="n">H</span> <span class="k">in</span>
  <span class="k">match</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">church_rosser</span><span class="bp">.</span><span class="n">aux2</span> <span class="n">H2</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">H3</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H1</span><span class="o">,</span> <span class="n">H3</span><span class="o">]</span>
    <span class="bp">|</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="bp">⟨</span><span class="n">L₅</span><span class="o">,</span> <span class="n">H3</span><span class="o">,</span> <span class="n">H4</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">cons</span> <span class="n">H3</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">H1</span><span class="o">]</span> <span class="kn">using</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">cons</span> <span class="n">H4</span><span class="bp">⟩</span>
  <span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">church_rosser</span><span class="bp">.</span><span class="n">aux</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)},</span>
  <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="bp">→</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">→</span> <span class="n">L₁</span> <span class="bp">=</span> <span class="n">L₂</span> <span class="bp">→</span>
  <span class="n">L₃</span> <span class="bp">=</span> <span class="n">L₄</span> <span class="bp">∨</span> <span class="bp">∃</span> <span class="n">L₅</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₃</span> <span class="n">L₅</span> <span class="bp">∧</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₄</span> <span class="n">L₅</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">bnot</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">bnot</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">church_rosser</span><span class="bp">.</span><span class="n">aux2</span> <span class="n">H</span>

<span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">church_rosser</span> <span class="o">(</span><span class="n">H12</span> <span class="o">:</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">H13</span> <span class="o">:</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₁</span> <span class="n">L₃</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">L₂</span> <span class="bp">=</span> <span class="n">L₃</span> <span class="bp">∨</span> <span class="bp">∃</span> <span class="n">L₄</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">∧</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₃</span> <span class="n">L₄</span> <span class="o">:=</span>
<span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">church_rosser</span><span class="bp">.</span><span class="n">aux</span> <span class="n">H12</span> <span class="n">H13</span> <span class="n">rfl</span>
</pre></div>

#### [ Patrick Massot (Apr 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308696):
<p>Be careful not to drop to zero</p>

#### [ Kenny Lau (Apr 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308698):
<p>probably can delete some newlines</p>

#### [ Patrick Massot (Apr 19 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125308713):
<p>That's what my PhD advisor used to say</p>

#### [ Kenny Lau (Apr 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125340029):
<p><a href="https://github.com/kckennylau/Lean/blob/master/free_group.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/free_group.lean">https://github.com/kckennylau/Lean/blob/master/free_group.lean</a></p>

#### [ Kenny Lau (Apr 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125340064):
<p>now it is 531 lines</p>

#### [ Kenny Lau (Apr 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125340072):
<p>Johannes's file is 486 lines</p>

#### [ Kenny Lau (Apr 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125340073):
<p>only 45 lines to go :P</p>

#### [ Johannes Hölzl (Apr 20 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342476):
<p>But my file is not finished! There are a couple of proofs missing... So i guess 531 lines are good enough</p>

#### [ Kenny Lau (Apr 20 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342482):
<p>Could I insist to use <code>quotient</code>? <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span></p>

#### [ Kenny Lau (Apr 20 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342490):
<p>you seem to have developed some theories of the transitive and reflexive closure of general reduction propositions though</p>

#### [ Kenny Lau (Apr 20 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342492):
<p>maybe you could put that theories in another file and I can use it?</p>

#### [ Johannes Hölzl (Apr 20 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342550):
<p>Yes, I will put <code>refl_trans</code> and <code>refl_cl</code> somewhere in mathlib. I'm not sure yet about the naming.</p>

#### [ Kenny Lau (Apr 20 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342551):
<p>I would love it if you could prove that the result is a setoid ^^</p>

#### [ Kenny Lau (Apr 20 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342553):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">))</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">L₃</span><span class="o">,</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="bp">∧</span> <span class="n">red</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">L</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">L</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="bp">⟨</span><span class="n">L₃</span><span class="o">,</span> <span class="n">H13</span><span class="o">,</span> <span class="n">H23</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">L₃</span><span class="o">,</span> <span class="n">H23</span><span class="o">,</span> <span class="n">H13</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="bp">⟨</span><span class="n">L₄</span><span class="o">,</span> <span class="n">H14</span><span class="o">,</span> <span class="n">H24</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">L₅</span><span class="o">,</span> <span class="n">H25</span><span class="o">,</span> <span class="n">H35</span><span class="bp">⟩</span><span class="o">,</span>
   <span class="k">let</span> <span class="bp">⟨</span><span class="n">L₆</span><span class="o">,</span> <span class="n">H46</span><span class="o">,</span> <span class="n">H56</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">church_rosser</span> <span class="n">H24</span> <span class="n">H25</span> <span class="k">in</span>
   <span class="bp">⟨</span><span class="n">L₆</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans</span> <span class="n">H14</span> <span class="n">H46</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans</span> <span class="n">H35</span> <span class="n">H56</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Apr 20 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342590):
<p>the relation being "there is a common reduction"</p>

#### [ Johannes Hölzl (Apr 20 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342703):
<p>yep, makes sense.</p>

#### [ Kenny Lau (Apr 20 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342710):
<p>and I think this is better than the refl-symm-trans closure, because things are easier to prove</p>

#### [ Kenny Lau (Apr 20 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125342711):
<p>the symm makes everything work no well</p>

#### [ Kenny Lau (Apr 21 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477808):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I just proved that <code>red</code> is a partial order</p>

#### [ Kenny Lau (Apr 21 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477809):
<p>Should I be using <code>\le</code>?</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477851):
<p>No, it's not really a less-than kind of thing</p>

#### [ Kenny Lau (Apr 21 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477852):
<p>should I remove the proof?</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477853):
<p>I would prefer ~&gt;* if you want notation for red</p>

#### [ Kenny Lau (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477859):
<p>is there unicode?</p>

#### [ Kenny Lau (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477860):
<p>also, it kinda looks like something not nice, so you might want to think twice</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477862):
<p>That's a right squiggle arrow with a star</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477863):
<p>the right squiggle arrow is <code>red.step</code>, and the star is its reflexive transitive closure</p>

#### [ Kenny Lau (Apr 21 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477904):
<p>eh, is that an answer to any of my two questions...</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477953):
<p>there is unicode for the right squig arrow, pretty sure</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477955):
<p>I was explaining the notation in response to "not so nice" comment</p>

#### [ Kenny Lau (Apr 21 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477956):
<p>so you're saying I should define reflexive transitive closure?</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477959):
<p>you sort of did</p>

#### [ Kenny Lau (Apr 21 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477967):
<p>I mean define <code>~&gt;</code> and <code>*</code> separately</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125477969):
<p>You could do like Johannes did and prove C-R generically over r.t. closure</p>

#### [ Kenny Lau (Apr 21 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478010):
<p>would the notations work?</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478017):
<p>I doubt it, but you could locally define ~&gt;* to mean <code>rt_closure red.step</code> or something</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478165):
<p>I found this in unicode: ⇝ , but it's a bit hard to distinguish from the regular arrow in my font on vscode</p>

#### [ Kenny Lau (Apr 21 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478168):
<p>let's just stick with <code>red</code></p>

#### [ Kenny Lau (Apr 21 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478173):
<p>should I remove the proof?</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478175):
<p>are you using it?</p>

#### [ Kenny Lau (Apr 21 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478176):
<p>not really, as you said we don't want to use <code>\le</code></p>

#### [ Kenny Lau (Apr 21 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478177):
<p>I have the other theorems</p>

#### [ Kenny Lau (Apr 21 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478217):
<p>my proof is literally</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">(</span><span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">))</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="n">red</span><span class="o">,</span>
  <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">red</span><span class="bp">.</span><span class="n">antisymm</span> <span class="o">}</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478218):
<p>yeah, skip it</p>

#### [ Kenny Lau (Apr 21 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478219):
<p>ok</p>

#### [ Kenny Lau (Apr 21 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478477):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">bnot</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">x</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">{</span> <span class="n">L₂</span> <span class="bp">//</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="o">}</span> <span class="o">:=</span>
<span class="bp">_</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478481):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110044">@Chris Hughes</span> would you have some insights as to how I would prove this?</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478522):
<p>Even stronger, the set of all lists that are <code>red</code> related to the original is finite</p>

#### [ Kenny Lau (Apr 21 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478523):
<p>right, but this is the inductive step</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478528):
<p>because if <code>red L1 L2</code> then <code>L2 &lt;+ L1</code></p>

#### [ Kenny Lau (Apr 21 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478530):
<p>and then?</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478531):
<p>use <code>sublists</code></p>

#### [ Kenny Lau (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478557):
<p>but it is not in mathlib that sublists are finite</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478572):
<p>yes, that's <code>sublists</code></p>

#### [ Mario Carneiro (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478574):
<p>it's literally a list of all sublists of another</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478575):
<p>hence finite</p>

#### [ Kenny Lau (Apr 21 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478577):
<p>aha</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478587):
<p>then again it's probably not the most efficient enumeration strategy</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478635):
<p>have you proven that <code>red L1 L2</code> is decidable?</p>

#### [ Kenny Lau (Apr 21 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478636):
<p>let's say I have</p>

#### [ Kenny Lau (Apr 21 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478637):
<p>(I have not, but I will)</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478677):
<p>it's easier to prove that the free group relation (including symmetry) Is decidable, since then you can use <code>reduce</code></p>

#### [ Kenny Lau (Apr 21 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478681):
<p>I don't understand, sorry</p>

#### [ Kenny Lau (Apr 21 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478687):
<p>how would I use reduce to prove that red L1 L2 is decidable?</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478688):
<p>you can decide if L1 ~ L2 by just reducing both sides and testing for equality</p>

#### [ Kenny Lau (Apr 21 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478691):
<p>but that doesn't mean red is decidable</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478693):
<p>that doesn't give you decidability of <code>red</code> though</p>

#### [ Kenny Lau (Apr 21 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478788):
<p>how would that help?</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478797):
<p>I'm not sure how important it is to know that red is decidable, but you need that to build a fintype using filter and sublists the way I described</p>

#### [ Kenny Lau (Apr 21 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478798):
<p>aha</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478800):
<p>you could also directly enumerate the red related lists</p>

#### [ Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478803):
<p>which amounts to writing another reduce-like function</p>

#### [ Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478840):
<p>i.e. with a core</p>

#### [ Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478843):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">step</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">hd</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span> <span class="n">x</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">hd</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">∧</span> <span class="n">hd</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">bnot</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="k">then</span> <span class="n">tl</span> <span class="k">else</span> <span class="n">x</span><span class="bp">::</span><span class="n">hd</span><span class="bp">::</span><span class="n">tl</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="n">x</span> <span class="o">:=</span> <span class="o">[</span><span class="n">x</span><span class="o">]</span>

<span class="n">def</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">L</span> <span class="o">[]</span>       <span class="o">:=</span> <span class="n">L</span>
<span class="bp">|</span> <span class="n">L</span> <span class="o">(</span><span class="n">hd</span><span class="bp">::</span><span class="n">tl</span><span class="o">)</span> <span class="o">:=</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">(</span><span class="n">reduce</span><span class="bp">.</span><span class="n">step</span> <span class="n">L</span> <span class="n">hd</span><span class="o">)</span> <span class="n">tl</span>

<span class="n">def</span> <span class="n">reduce</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">))</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">reduce</span><span class="bp">.</span><span class="n">core</span> <span class="o">[]</span> <span class="n">L</span><span class="bp">.</span><span class="n">reverse</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478845):
<p>speaking of which, I don't understand why your definition is so convoluted</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478846):
<p>why the reverse?</p>

#### [ Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478848):
<p>because it gets reversed</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478849):
<p>...</p>

#### [ Kenny Lau (Apr 21 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478850):
<p>so I have a word <code>[a,b,c,d,e,f,g,h]</code></p>

#### [ Kenny Lau (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478852):
<p>my pointer goes from left to right</p>

#### [ Kenny Lau (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478857):
<p>and the left of the pointer gets reversed</p>

#### [ Kenny Lau (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478859):
<p>because the heads are at <code>d</code> and <code>e</code> respectively</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478860):
<p>you can output either reversed or not, depending on how you structure the recursive call</p>

#### [ Kenny Lau (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478861):
<p>after the traversal of the list, it will become <code>[h,g,f,c,b,a]</code></p>

#### [ Mario Carneiro (Apr 21 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478863):
<p>look at how <code>list.foldl</code> and <code>list.foldr</code> are defined</p>

#### [ Kenny Lau (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478898):
<p>basically</p>

#### [ Kenny Lau (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478907):
<p>I destructed the list once, so it has to get reversed</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478908):
<p>What's wrong with Johannes's definition of reduce?</p>

#### [ Kenny Lau (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478910):
<p>it's less efficient</p>

#### [ Kenny Lau (Apr 21 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478914):
<p>my algorithm is O(n)</p>

#### [ Kenny Lau (Apr 21 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478916):
<p>his algorithm is O(n^2)</p>

#### [ Kenny Lau (Apr 21 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125478921):
<p>[don't quote me on this]</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479008):
<p>To be clear, I'm talking about the following definition:</p>
<div class="codehilite"><pre><span></span>def reduce {α} [decidable_eq α] : list (α × bool) → list (α × bool)
| ((a₁, p) :: (a₂, n) :: xs) :=
  if a₁ = a₂ ∧ p ≠ n then reduce xs
  else (a₁, p) :: reduce ((a₂, n) :: xs)
| l := l
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479010):
<p>that's wrong</p>

#### [ Kenny Lau (Apr 21 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479011):
<p>as I painfully realized two days ago</p>

#### [ Kenny Lau (Apr 21 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479014):
<p>because <code>[a,b,b^-1,a^-1]</code> becomes <code>[a,a^-1]</code></p>

#### [ Mario Carneiro (Apr 21 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479112):
<p>Fair enough. What about this then:</p>
<div class="codehilite"><pre><span></span>def reduce {α} [decidable_eq α] : list (α × bool) → list (α × bool)
| ((a₁, p) :: xs) :=
  match reduce xs with
  | (a₂, n) :: xs&#39; :=
    if a₁ = a₂ ∧ p ≠ n then xs&#39;
    else (a₁, p) :: (a₂, n) :: xs&#39;
  | [] := [(a₁, p)]
  end
| l := l
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479117):
<p>(deleted)</p>

#### [ Kenny Lau (Apr 21 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479119):
<p>aha</p>

#### [ Kenny Lau (Apr 21 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479162):
<p>somehow my gut says this is n^2 also</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479164):
<p>it seems to work</p>
<div class="codehilite"><pre><span></span>#eval reduce [(0, tt), (1, tt), (1, ff), (0, ff), (0, tt), (0, ff)]
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479165):
<p>my gut might be wrong</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479166):
<p>I don't think it is since it's one-pass</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479173):
<p>this is what I mean by "depending on how you use the IH"</p>

#### [ Kenny Lau (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479174):
<p>interesting</p>

#### [ Kenny Lau (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479175):
<p>that's clever</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479176):
<p>you can either process and then call the IH, or call the IH and then process, or both</p>

#### [ Mario Carneiro (Apr 21 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479177):
<p>that's how <code>foldl</code> and <code>foldr</code> get different results</p>

#### [ Kenny Lau (Apr 21 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125479265):
<p>I have much more to learn</p>

#### [ Kenny Lau (Apr 21 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481027):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> the lifting theorem is really a pain</p>

#### [ Kenny Lau (Apr 21 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481028):
<p>I need some guidance from you</p>

#### [ Kenny Lau (Apr 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481029):
<p>it isn't really straightforward</p>

#### [ Kenny Lau (Apr 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481070):
<div class="codehilite"><pre><span></span><span class="n">L₂</span> <span class="n">L4</span> <span class="n">L5</span> <span class="n">L6</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">H45</span> <span class="o">:</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L4</span> <span class="n">L5</span><span class="o">,</span>
<span class="n">H56</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L5</span> <span class="n">L6</span><span class="o">,</span>
<span class="n">H26</span> <span class="o">:</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₂</span> <span class="n">L6</span><span class="o">,</span>
<span class="n">H24</span> <span class="o">:</span> <span class="n">L₂</span> <span class="bp">&lt;+</span> <span class="n">L4</span><span class="o">,</span>
<span class="n">ih</span> <span class="o">:</span> <span class="n">L₂</span> <span class="bp">&lt;+</span> <span class="n">L5</span> <span class="bp">→</span> <span class="n">red</span> <span class="n">L5</span> <span class="n">L₂</span>
<span class="err">⊢</span> <span class="n">red</span> <span class="n">L4</span> <span class="n">L₂</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481071):
<p>wrong thread</p>

#### [ Kenny Lau (Apr 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481077):
<p>this is the hardest part of the proof</p>

#### [ Kenny Lau (Apr 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481078):
<p>the rest is just induction</p>

#### [ Mario Carneiro (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481129):
<p>wait, I'm confused. What's the statement and proof so far?</p>

#### [ Kenny Lau (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481132):
<p>the thing I sent you just there</p>

#### [ Kenny Lau (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481133):
<p>is the inductive step</p>

#### [ Kenny Lau (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481135):
<p>the rest is just induction that I can do</p>

#### [ Mario Carneiro (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481137):
<p>I know, but it doesn't make any sense</p>

#### [ Kenny Lau (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481138):
<p>oh, the lifting theorem</p>

#### [ Mario Carneiro (Apr 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481139):
<p>I don't understand what got you to this point</p>

#### [ Kenny Lau (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481178):
<p>if reduce L1 = reduce L2 and L2 is a sublist of L1, then red L1 L2</p>

#### [ Mario Carneiro (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481181):
<p>ah, I was thinking about that but I'm not sure it's a theorem</p>

#### [ Kenny Lau (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481182):
<p>aha</p>

#### [ Kenny Lau (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481183):
<p>I thought it's true</p>

#### [ Kenny Lau (Apr 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481184):
<p>my gut tells me so</p>

#### [ Kenny Lau (Apr 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481190):
<p>now to make it more like the lifting theorem, we restate it:</p>

#### [ Kenny Lau (Apr 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481191):
<p>if red L1 L3 and red L2 L3, and that L2 is a sublist of L1, then red L1 L2</p>

#### [ Kenny Lau (Apr 21 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481233):
<p>I can't really come up with a counter-example</p>

#### [ Kenny Lau (Apr 21 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481234):
<p>I can think of examples where the lift is not really trivial</p>

#### [ Mario Carneiro (Apr 21 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481761):
<p>Okay, I'm still not on board with saying it's definitely true but we can try to prove it anyway. Let's show that if <code>red L1 L3</code> and <code>red L2 L3</code>, then <code>L2 &lt;+ L1</code> implies <code>red L1 L2</code>. Proof by induction on <code>red L2 L3</code>, reducing to the following lemma: if <code>red L1 L3</code> and <code>red.step L2 L3</code> and <code>L2 &lt;+ L1</code> then <code>red L1 L2</code>. Now you have some list details by comparing <code>red.step</code> with <code>&lt;+</code></p>

#### [ Mario Carneiro (Apr 21 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125481943):
<p>aha, counterexample: <code>abb⁻¹a⁻¹</code> has a sublist <code>bb⁻¹</code> which reduces to <code>[]</code>, but <code>abb⁻¹a⁻¹</code> does not reduce to <code>bb⁻¹</code></p>

#### [ Kenny Lau (Apr 21 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482387):
<p>aha!</p>

#### [ Kenny Lau (Apr 21 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482389):
<p>nice, thanks</p>

#### [ Kenny Lau (Apr 21 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482394):
<p>so, how might we prove that red is decidable?</p>

#### [ Mario Carneiro (Apr 21 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482941):
<div class="codehilite"><pre><span></span>def is_red {α} [decidable_eq α] : list (α × bool) → list (α × bool) → bool
| [] [] := tt
| [] ((b, q) :: ys) := ff
| ((a, p) :: xs) [] := is_red xs [(a, bnot p)]
| ((a, p) :: xs) ((b, q) :: ys) :=
  if (a, p) = (b, q) then is_red xs ys else
  is_red xs ((a, bnot p) :: (b, q) :: ys)
</pre></div>


<p>replace <code>bool</code> with <code>decidable</code> and insert proofs</p>

#### [ Kenny Lau (Apr 21 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125482944):
<p>aha</p>

#### [ Kenny Lau (Apr 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125484985):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> should I inject your name onto the top of the file</p>

#### [ Mario Carneiro (Apr 21 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125485472):
<p>If you want... I've got enough credits on mathlib already, I don't need to be stealing it from others ;)</p>

#### [ Mario Carneiro (Apr 21 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125485519):
<p>I guess the full combined file on free groups when it gets finished will be joint work of all three of us, there's been a lot of collaboration on it</p>

#### [ Kenny Lau (Apr 21 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125492272):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">of_cons</span> <span class="o">{</span><span class="n">x</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span> <span class="o">(</span><span class="n">x</span> <span class="bp">::</span> <span class="n">L₁</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="bp">::</span> <span class="n">L₂</span><span class="o">)</span> <span class="bp">→</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">generalize</span> <span class="n">H1</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">::</span> <span class="n">L₁</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">=</span> <span class="n">L1</span><span class="o">,</span>
  <span class="n">generalize</span> <span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">::</span> <span class="n">L₂</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">=</span> <span class="n">L2</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">H</span> <span class="k">with</span> <span class="n">L3</span> <span class="n">L3</span> <span class="n">L4</span> <span class="n">L5</span> <span class="n">H3</span> <span class="n">H4</span> <span class="n">ih</span> <span class="n">generalizing</span> <span class="n">x</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">H1</span><span class="bp">;</span> <span class="n">injections</span><span class="bp">;</span> <span class="n">subst_vars</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">red</span><span class="bp">.</span><span class="n">step_trans</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">H3</span> <span class="k">with</span> <span class="n">L6</span> <span class="n">L7</span> <span class="n">x1</span> <span class="n">b1</span><span class="o">,</span>
    <span class="n">subst_vars</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">L6</span> <span class="k">with</span> <span class="n">hd</span> <span class="n">tl</span><span class="o">,</span>
    <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
    <span class="o">{</span> <span class="n">injection</span> <span class="n">H1</span> <span class="k">with</span> <span class="n">H5</span> <span class="n">H6</span><span class="o">,</span>
      <span class="n">substs</span> <span class="n">H5</span> <span class="n">H6</span><span class="o">,</span>
      <span class="n">clear</span> <span class="n">H1</span> <span class="n">H3</span><span class="o">,</span>
      <span class="n">transitivity</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">exact</span> <span class="n">red</span><span class="bp">.</span><span class="n">cons</span> <span class="n">H4</span> <span class="o">},</span>
      <span class="o">{</span> <span class="n">simp</span> <span class="o">}</span> <span class="o">},</span>
    <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span>
    <span class="o">{</span> <span class="n">injection</span> <span class="n">H1</span> <span class="k">with</span> <span class="n">H5</span> <span class="n">H6</span><span class="o">,</span>
      <span class="n">substs</span> <span class="n">H5</span> <span class="n">H6</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">red</span><span class="bp">.</span><span class="n">trans</span> <span class="n">red</span><span class="bp">.</span><span class="n">bnot</span> <span class="o">(</span><span class="n">ih</span> <span class="n">rfl</span> <span class="n">rfl</span><span class="o">)</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/free%20group/near/125492273):
<p>why so long</p>


{% endraw %}
