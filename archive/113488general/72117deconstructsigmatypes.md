---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72117deconstructsigmatypes.html
---

## Stream: [general](index.html)
### Topic: [deconstruct sigma types](72117deconstructsigmatypes.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 30 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871250):
<div class="codehilite"><pre><span></span><span class="c1">-- works fine</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)),</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span>

<span class="c1">-- doesn&#39;t work</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">(</span><span class="bp">⟨</span><span class="n">s</span><span class="o">,</span><span class="n">t</span><span class="bp">⟩</span> <span class="o">:</span> <span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)),</span> <span class="n">s</span>
<span class="c1">-- invalid binder, identifier expected</span>
<span class="c1">-- and other errors</span>
</pre></div>


<p>Can't I take a sigma type apart like this? Isn't a sigma type just a structure? I suspect I'm missing a trick?</p>

#### [ Kenny Lau (Nov 30 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871337):
<p>nooooo</p>

#### [ Kenny Lau (Nov 30 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871343):
<p>don’t deconstruct things in definitions</p>

#### [ Kevin Buzzard (Nov 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871461):
<div class="codehilite"><pre><span></span><span class="c1">-- works</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)),</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span><span class="n">t</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">x</span> <span class="k">in</span> <span class="n">s</span>
</pre></div>

#### [ Kevin Buzzard (Nov 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871469):
<p>Is this better Kenny?</p>

#### [ Kevin Buzzard (Nov 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871480):
<p>Or still bad?</p>

#### [ Mario Carneiro (Nov 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871492):
<p>drop the type ascription</p>

#### [ Kevin Buzzard (Nov 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871506):
<p>Heh, why would this help?</p>

#### [ Mario Carneiro (Nov 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871515):
<p>the syntax for lambda match is <code>λ ⟨s,t⟩, ...</code> with no type ascriptions permitted</p>

#### [ Kevin Buzzard (Nov 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871569):
<p>Oh!</p>

#### [ Mario Carneiro (Nov 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871573):
<p>the <code>⟨s,t⟩</code> is not actually a pair even though it looks like one</p>

#### [ Mario Carneiro (Nov 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871577):
<p>it's just syntax</p>

#### [ Kevin Buzzard (Nov 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871593):
<p>Kenny says it's a bad idea -- is the <code>let</code> thing OK or is it a bad idea for the same reason?</p>

#### [ Mario Carneiro (Nov 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871607):
<p>it's the same</p>

#### [ Kevin Buzzard (Nov 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871621):
<div class="codehilite"><pre><span></span><span class="c1">-- works</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span><span class="n">t</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">s</span>
</pre></div>

#### [ Mario Carneiro (Nov 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871638):
<p>The simpler way is just to pattern match right from the start</p>

#### [ Mario Carneiro (Nov 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871648):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span><span class="n">t</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">s</span>
</pre></div>

#### [ Mario Carneiro (Nov 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871724):
<p>I think the reason Kenny doesn't like those definitions is because it creates an auxiliary, and it doesn't unfold unless it's an explicit pair</p>

#### [ Mario Carneiro (Nov 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871743):
<p>as opposed to</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="err">Σ</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">p</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span>
</pre></div>

#### [ Johan Commelin (Nov 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148872806):
<p>It would be nice if what Kevin wants would just be syntactic sugar for the <code>p, p.1</code> version...</p>

#### [ Johan Commelin (Nov 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148872834):
<p>But I guess syntactic sugar will only take you so far...</p>

#### [ Mario Carneiro (Nov 30 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148873306):
<p>this is a thing: they are called lazy pattern matches in haskell, and they've been discussed on this chat before</p>

#### [ Patrick Massot (Nov 30 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148873412):
<p>Yeah, this is a very common fantasy on this chat</p>

#### [ Kevin Buzzard (Nov 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148874206):
<p>Reality: <code>set.image (λ x, let (⟨⟨⟨j,k⟩,f⟩,r⟩ : (Σ y : (Σ x : J × J, (R x.1) → (R x.2)), R y.1.1)) := x in
      (X ⟨j,r⟩ - X ⟨k,f r⟩)) {x | x.1 ∈ F})</code></p>

#### [ Kevin Buzzard (Nov 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148874226):
<p>well, that's actually just a small piece of the reality</p>

#### [ Kevin Buzzard (Nov 30 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148874243):
<p>We're making colimits in the category of commutative rings!</p>

#### [ Kevin Buzzard (Nov 30 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148874306):
<p>Without it, it will be <code>x.1.1.1</code> everywhere</p>


{% endraw %}
