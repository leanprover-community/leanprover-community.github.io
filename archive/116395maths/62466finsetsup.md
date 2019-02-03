---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62466finsetsup.html
---

## Stream: [maths](index.html)
### Topic: [finset sup](62466finsetsup.html)

---


{% raw %}
#### [ Sebastien Gouezel (Oct 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135087348):
<p>I can't find the lemma saying that, in a linear order (with bot, probably), the sup of a finset is <code>&lt; a</code> if all its elements are <code>&lt; a</code>(and <code>\bot &lt; a</code>). I guess it has to be somewhere, but there are so many files and so many different classes for orders. Some help would be most welcome!</p>

#### [ Johannes Hölzl (Oct 03 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135088713):
<p>I don't think we have the variant for <code>&lt;</code>. There is <code>le_max_of_mem</code>, where <code>a ∈ s.max</code> states that there exist a maximum and it is <code>a</code>.</p>

#### [ Johannes Hölzl (Oct 03 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135088730):
<p>when your order has a bottom element you can use <code>finset.sup_le</code></p>

#### [ Sebastien Gouezel (Oct 03 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135090992):
<p>I really need the version with <code>&lt;</code>. I think I am lost with the typeclass system. If I want to state my lemma, say, on <code>nnreal</code>, then everything works fine:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">nnreal</span><span class="o">}</span>
<span class="kn">lemma</span> <span class="n">sup_lt</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">nnreal</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="err">⊥</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span><span class="n">b</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">s</span><span class="bp">.</span><span class="n">sup</span> <span class="n">f</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_eq</span> <span class="n">β</span><span class="bp">;</span> <span class="k">from</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">sup_eq_max</span><span class="o">,</span> <span class="n">max_lt_iff</span><span class="o">]</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">})</span>
</pre></div>


<p>But I would like a lemma that applies in all interesting situations, for instance <code>ennreal</code>: a decidable linear order with bot. I don't know how to write this lemma properly. If I try</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span><span class="o">:</span> <span class="n">finset</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span>
<span class="kn">lemma</span> <span class="n">sup_lt2</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">order_bot</span> <span class="n">α</span><span class="o">]</span>  <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="err">⊥</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span><span class="n">b</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">s</span><span class="bp">.</span><span class="n">sup</span> <span class="n">f</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_eq</span> <span class="n">β</span><span class="bp">;</span> <span class="k">from</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">sup_eq_max</span><span class="o">,</span> <span class="n">max_lt_iff</span><span class="o">]</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}),</span>
</pre></div>


<p>then it does not work because <code>s.sup f</code> does not make sense as <code>α</code> is not of class <code>semilattice_sup_bot</code>.</p>
<p>And if I try</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span><span class="o">:</span> <span class="n">finset</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span>
<span class="kn">lemma</span> <span class="n">sup_lt3</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">]</span>  <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="err">⊥</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span><span class="n">b</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">s</span><span class="bp">.</span><span class="n">sup</span> <span class="n">f</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_eq</span> <span class="n">β</span><span class="bp">;</span> <span class="k">from</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">sup_eq_max</span><span class="o">,</span> <span class="n">max_lt_iff</span><span class="o">]</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}),</span>
</pre></div>


<p>it does not work either as the sup coming from the <code>decidable_linear_order</code> and the <code>semilattice_sup_bot</code> are not detected to be the same.</p>
<p>Is there a good way to write this lemma?</p>

#### [ Mario Carneiro (Oct 03 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135091562):
<p>You could use <code>is_total α (≤)</code> as a mixin</p>

#### [ Sebastien Gouezel (Oct 03 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135093300):
<p>Got it, thanks!</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span><span class="o">:</span> <span class="n">finset</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span>
<span class="kn">lemma</span> <span class="n">sup_lt</span> <span class="o">[</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">is_total</span> <span class="n">α</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)]</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="err">⊥</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span><span class="n">b</span> <span class="err">∈</span> <span class="n">q</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">q</span><span class="bp">.</span><span class="n">sup</span> <span class="n">f</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">A</span><span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">y</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">⊔</span> <span class="n">y</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">assume</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hx</span> <span class="n">hy</span><span class="o">,</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">is_total</span><span class="bp">.</span><span class="n">total</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="k">with</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">{</span><span class="n">simpa</span> <span class="o">[</span><span class="n">sup_of_le_right</span> <span class="n">h</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hy</span><span class="o">},</span>
  <span class="o">{</span><span class="n">simpa</span> <span class="o">[</span><span class="n">sup_of_le_left</span> <span class="n">h</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hx</span><span class="o">}</span>
<span class="kn">end</span><span class="o">,</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_eq</span> <span class="n">β</span><span class="bp">;</span> <span class="k">from</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">q</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">A</span><span class="o">]</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">})</span>
</pre></div>


<p>This applies cleanly in all situations I am interested in.<br>
(And I confirm I am 20 times more slow in Lean than Isabelle, but hopefully this will improve slightly over time :)</p>

#### [ Kevin Buzzard (Oct 03 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135096270):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> in the past you have done mathematics in Isabelle with "PhD student level" objects like Gromov-hyperbolic spaces. What attracted me to Lean was that I realised that there seemed to be no obstruction to doing pure mathematics with objects at this kind of level (e.g. we will have a definition of a perfectoid space soon and I'm sure we'll be able to prove basic lemmas about it). Is the same true of Isabelle? Disregarding the fact that Lean's maths library is no doubt much smaller than Isabelle's, are there any other reasons why one might prefer Isabelle to Lean when manipulating complex mathematical objects?</p>

#### [ Sebastien Gouezel (Oct 03 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135096989):
<p>There are very serious limitations in Isabelle. Doing perfectoids would be essentially impossible, I guess. For another example, I want to define the space of all compact metric spaces, put a distance on it (the so-called Gromov-Hausdorff distance), and then it makes sense to talk of the convergence of a sequence of compact metric spaces to a compact metric space, and put probability measures on the space of compact metric spaces, and so on. This is very common and useful in geometry and probability, but impossible to formalize in Isabelle, for lack of dependent types. My impression is that this will be perfectly doable in Lean. That's why I want to switch. But I miss a lot the automatisation level of Isabelle, which is way better than anything there is currently in Lean.</p>

#### [ Sebastien Gouezel (Oct 03 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097163):
<p>An important feature of Isabelle I dream to have in Lean is the simprocs. When you call <code>simp</code>, if it detects some pattern then it will automatically apply some algorithms. For instance, if it detects some algebraic expression, then it will simplify it within reasonable bouds. If you have something like <code>a+ exp( b + c + d - b + c) - a</code> and you just apply <code>simp</code>, it will transform it to <code>exp (2 * c+d)</code>, without the need to call an additional tactic like <code>ring</code> or <code>abel</code> -- note that both <code>ring</code> and <code>abel</code> would fail on this simple example.</p>

#### [ Mario Carneiro (Oct 03 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097464):
<p>I think <code>ring</code> will actually do that</p>

#### [ Mario Carneiro (Oct 03 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097473):
<p>this is the "failure mode" of <code>ring</code></p>

#### [ Sebastien Gouezel (Oct 03 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097488):
<p>Will it also simplify inside the exponential?</p>

#### [ Johan Commelin (Oct 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097662):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> But there are not theoretical reasons to why this sort of thing couldn't happen in Lean, right? It is just a matter of Lean being very young compared to Isabelle. Is that right?</p>

#### [ Patrick Massot (Oct 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097679):
<p>It seems it's also easier to build automation without dependent type</p>

#### [ Mario Carneiro (Oct 03 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097699):
<p>I think <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> was looking into simpprocs, not sure what progress has been made there</p>

#### [ Johannes Hölzl (Oct 03 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097703):
<p>no a lot yet</p>

#### [ Johan Commelin (Oct 03 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097704):
<blockquote>
<p>It seems it's also easier to build automation without dependent type</p>
</blockquote>
<p>Ok, so maybe Lean has a theoretical disadvantage...</p>

#### [ Sebastien Gouezel (Oct 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135098086):
<blockquote>
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> But there are not theoretical reasons to why this sort of thing couldn't happen in Lean, right? It is just a matter of Lean being very young compared to Isabelle. Is that right?</p>
</blockquote>
<p>I think so, yes. But to implement it you need to know the inner workings of simp, and I guess it is also very easy to run into performance issues.</p>

#### [ Kevin Buzzard (Oct 03 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135102923):
<p>I dream of a future where we simply do not care about performance issues -- like in normal maths. You write it once, you compile it once, you forget about it and only come back to it when someone else changes something and your proof actually breaks.</p>

#### [ Kevin Buzzard (Oct 03 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135102950):
<p>This is some sort of analogue of a mathematician proving a theorem and then publishing it and then everyone can use the result without having to wait for it to compile.</p>

#### [ Mario Carneiro (Oct 03 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135103468):
<p>Wait, are you saying that when you start working on a problem, you <em>don't</em> remind yourself what facts are known by proving them and the rest of basic maths from the axioms?</p>

#### [ Mario Carneiro (Oct 03 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135103539):
<p>I mean, who knows, maybe something you wrote today invalidates everything you have ever learned, how can you be sure unless you go over it all every day?</p>

#### [ Kevin Buzzard (Oct 03 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135104075):
<p>Naah -- often we rely on random facts which we read on the internet and for which the proof term is currently unavailable or incomplete. One makes much faster progress this way!</p>

#### [ Patrick Massot (Oct 03 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135104095):
<p>And this won't change until we get that module refactor</p>

#### [ Kevin Buzzard (Oct 03 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135104102):
<p>We even sometimes rely on "facts" for which it turns out that there is no proof term at all!</p>

#### [ Patrick Massot (Oct 03 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135104153):
<p>Waiting for Lean 4 is completely out of fashion now that we have this other fantasy</p>

#### [ Jared Corduan (Oct 03 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135114883):
<p>some folks aren't afraid to assume GCH :)</p>

#### [ Kevin Buzzard (Oct 03 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135128633):
<blockquote>
<p>There are very serious limitations in Isabelle. [snip] ...but impossible to formalize in Isabelle, for lack of dependent types.</p>
</blockquote>
<p>What do people mean by Isabelle here? Are we talking about Isabelle-HOL or something? Can there be an Isabelle-DTT?</p>

#### [ Kevin Buzzard (Oct 03 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135128950):
<blockquote>
<p>But I miss a lot the automatisation level of Isabelle, which is way better than anything there is currently in Lean.</p>
</blockquote>
<p>We need a plan for this. I am not sure I would be capable of supervising an MSc student to write tactics for automation. Of course it should probably all wait for Lean 4. <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> will you be supervising any more MSc students in the near future?</p>

#### [ Patrick Massot (Oct 03 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135128967):
<p>I'm not sure MSc is enough</p>

#### [ Kevin Buzzard (Oct 03 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135129210):
<p>Is writing a bunch of killer automation in Lean a PhD project for a CS student? And would you be able to get a post-doc afterwards?</p>

#### [ Patrick Massot (Oct 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135129236):
<p>It seems like Johannes, Rob and Jasmin are working on Lean automation and don't feel like this is MSc student level...</p>

#### [ Patrick Massot (Oct 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135129248):
<p>It seems to be more like a ERC grant proposal project</p>

#### [ Sebastien Gouezel (Oct 03 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135130316):
<blockquote>
<blockquote>
<p>There are very serious limitations in Isabelle. [snip] ...but impossible to formalize in Isabelle, for lack of dependent types.</p>
</blockquote>
<p>What do people mean by Isabelle here? Are we talking about Isabelle-HOL or something? Can there be an Isabelle-DTT?</p>
</blockquote>
<p>Yes, I am talking about Isabelle/HOL.</p>

#### [ Sebastien Gouezel (Oct 03 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135130413):
<p>You can develop any logic in Isabelle, this is a framework, in a sense. But Isabelle/HOL is the most developed (and usable, and used) instance.</p>


{% endraw %}
