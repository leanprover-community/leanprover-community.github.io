---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/01999dononcyclicgroupsexist.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [do non-cyclic groups exist?](https://leanprover-community.github.io/archive/116395maths/01999dononcyclicgroupsexist.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 05 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811479):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">order_of_element</span>

<span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">decidable_eq</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">PP</span> <span class="o">:</span> <span class="n">G</span>
<span class="bp">|</span> <span class="n">PM</span> <span class="o">:</span> <span class="n">G</span>
<span class="bp">|</span> <span class="n">MP</span> <span class="o">:</span> <span class="n">G</span>
<span class="bp">|</span> <span class="n">MM</span> <span class="o">:</span> <span class="n">G</span>

<span class="kn">namespace</span> <span class="n">G</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">G</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">elems</span> <span class="o">:=</span> <span class="o">{</span><span class="n">PP</span><span class="o">,</span><span class="n">PM</span><span class="o">,</span><span class="n">MP</span><span class="o">,</span><span class="n">MM</span><span class="o">},</span>
  <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">g</span><span class="bp">;</span><span class="n">simp</span>
<span class="o">}</span>

<span class="n">def</span> <span class="n">mul</span> <span class="o">:</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">G</span>
<span class="bp">|</span> <span class="n">PP</span> <span class="n">PP</span> <span class="o">:=</span> <span class="n">PP</span>
<span class="bp">|</span> <span class="n">PP</span> <span class="n">PM</span> <span class="o">:=</span> <span class="n">PM</span>
<span class="bp">|</span> <span class="n">PP</span> <span class="n">MP</span> <span class="o">:=</span> <span class="n">MP</span>
<span class="bp">|</span> <span class="n">PP</span> <span class="n">MM</span> <span class="o">:=</span> <span class="n">MM</span>
<span class="bp">|</span> <span class="n">PM</span> <span class="n">PP</span> <span class="o">:=</span> <span class="n">PM</span>
<span class="bp">|</span> <span class="n">PM</span> <span class="n">PM</span> <span class="o">:=</span> <span class="n">PP</span>
<span class="bp">|</span> <span class="n">PM</span> <span class="n">MP</span> <span class="o">:=</span> <span class="n">MM</span>
<span class="bp">|</span> <span class="n">PM</span> <span class="n">MM</span> <span class="o">:=</span> <span class="n">MP</span>
<span class="bp">|</span> <span class="n">MP</span> <span class="n">PP</span> <span class="o">:=</span> <span class="n">MP</span>
<span class="bp">|</span> <span class="n">MP</span> <span class="n">PM</span> <span class="o">:=</span> <span class="n">MM</span>
<span class="bp">|</span> <span class="n">MP</span> <span class="n">MP</span> <span class="o">:=</span> <span class="n">PP</span>
<span class="bp">|</span> <span class="n">MP</span> <span class="n">MM</span> <span class="o">:=</span> <span class="n">PM</span>
<span class="bp">|</span> <span class="n">MM</span> <span class="n">PP</span> <span class="o">:=</span> <span class="n">MM</span>
<span class="bp">|</span> <span class="n">MM</span> <span class="n">PM</span> <span class="o">:=</span> <span class="n">MP</span>
<span class="bp">|</span> <span class="n">MM</span> <span class="n">MP</span> <span class="o">:=</span> <span class="n">PM</span>
<span class="bp">|</span> <span class="n">MM</span> <span class="n">MM</span> <span class="o">:=</span> <span class="n">PP</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">group</span> <span class="n">G</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="n">mul</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="n">PP</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">inv</span> <span class="o">:=</span> <span class="n">id</span><span class="o">,</span>
  <span class="n">mul_left_inv</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="o">}</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">is_cyclic</span> <span class="n">G</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">G</span>
</pre></div>


<p>This is my attempt to prove that non-cyclic groups exist in Lean. I had perhaps naively thought that I was going to get the whole way there with <code>dec_trivial</code>, but I've just realised that my claim that a group is not cyclic is not immediately decidable. For each element <code>g</code> I need to come up with an element <code>h</code> such that <code>h</code> is not in the cyclic group generated by <code>g</code>, which involves showing that for all integers <code>n</code>, <code>h</code> isn't <code>g^n</code>. This suddenly looks a bit more painful than I wanted it to be. Any ideas on how to proceed?</p>
<p>This is motivated by a second year problem sheet question: "True or false? If <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi></mrow><annotation encoding="application/x-tex">G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">G</span></span></span></span> is abelian then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi></mrow><annotation encoding="application/x-tex">G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">G</span></span></span></span> is cyclic". [<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi></mrow><annotation encoding="application/x-tex">G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">G</span></span></span></span> a group]</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811568):
<p>Why not use C_2^2?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811605):
<p>I did...</p>

#### [ Kenny Lau (Nov 05 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811625):
<p>oh right, and then there (should) be some lemmas about orders of elements in product</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811629):
<p>The issue is that proving something isn't cyclic involves checking that infinitely many calculations don't work out</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811631):
<p>no, I mean <code>zmod 2 x zmod 2</code></p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811637):
<p>the problem is still there</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811641):
<p>I mean the problem I highlight is still there</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811648):
<p>It's just that there's less set-up ;-)</p>

#### [ Reid Barton (Nov 05 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811654):
<p>if you want to do it by dec_trivial, maybe prove that it suffices to consider n &lt; |G| by Lagrange</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811661):
<p>or even <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>0</mn><mo>≤</mo><mi>n</mi><mo>&lt;</mo><mi mathvariant="normal">∣</mi><mi>G</mi><mi mathvariant="normal">∣</mi></mrow><annotation encoding="application/x-tex">0\leq n&lt;|G|</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">0</span><span class="mrel">≤</span><span class="mord mathit">n</span><span class="mrel">&lt;</span><span class="mord mathrm">∣</span><span class="mord mathit">G</span><span class="mord mathrm">∣</span></span></span></span>. Is this already in Lean?</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811662):
<p>You just check that for every element of the group there is a proper subgroup that contains it</p>

#### [ Reid Barton (Nov 05 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811669):
<p>or maybe you could even do some pigeonhole argument</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811730):
<p>or you could prove that <code>is_cyclic</code> is decidable and then decide it</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811737):
<p>If I do the Lagrange thing then it becomes <code>dec_trivial</code> again because <span class="user-mention" data-user-id="110064">@Kenny Lau</span> recently PR'd a decidability instance for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>0</mn><mo>≤</mo><mi>n</mi><mo>&lt;</mo><mi>m</mi></mrow><annotation encoding="application/x-tex">0\leq n&lt;m</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathrm">0</span><span class="mrel">≤</span><span class="mord mathit">n</span><span class="mrel">&lt;</span><span class="mord mathit">m</span></span></span></span> I believe</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811744):
<p>Is <code>is_cyclic</code> decidable?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811751):
<p>For infinite groups it sounds scary</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811757):
<p>for finite groups everything is decidable</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811758):
<p>for finite groups I guess I believe you</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811759):
<p>right</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811789):
<p>It's easy to write a program to calculate the order of an element in a finite group, maybe Chris has already done it</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811829):
<p>so you just run that on everything and it comes up less than |G| each time</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811834):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> what do you recommend -- I suspect you know well what is there.</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811846):
<p>Definition of <code>is_cyclic</code> is not "there's an element of order equal to the order of the group" as this would not work for Z</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811858):
<p>I see. So for finite groups one wants "is_cyclic iff exists element of order |G|"</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811865):
<p>by the pigeonhole principle it works for finite groups though</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811943):
<p>technically, it does work for Z since it is cyclic</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811947):
<p>rofl</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811950):
<p>but it doesn't work for Z^2</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811953):
<p>indeed :-)</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811957):
<p>Wait</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811966):
<p>what is order of an element of infinite order?</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811969):
<p>infinite</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811970):
<p>I'm surprised it's not 37</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811975):
<p>oh Ok</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811981):
<p>oh you mean in lean</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811982):
<p>right</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811987):
<p>maybe 0?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146811994):
<p>exactly!</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812004):
<p>That's what i said</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812013):
<p>no, like actually 0</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812016):
<p>right</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812019):
<p>"the canonical junk value"</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812022):
<p>like characteristic 0</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812072):
<p>like not junk 0</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812091):
<p>oh, you're right: there is an argument which says the order really is zero</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812111):
<p>the order of an element should really be the ideal of Z consisting of n such that g^n=id</p>

#### [ Mario Carneiro (Nov 05 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812114):
<p>exactly</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812120):
<p>and if you really want a number, then choose the generator which is in nat</p>

#### [ Kevin Buzzard (Nov 05 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812131):
<p>fortunately, the order of an infinite group in Lean is probably 0 ;-)</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812186):
<p>I guess there are two order functions, one for cardinals and one for finite cardinals</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812188):
<p>so it's really not 0 here</p>

#### [ Mario Carneiro (Nov 05 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812332):
<p>I think you should stop worrying about infinite groups here</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812346):
<p>:-) Yeah, especially given that I proved that G was a fintype</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812370):
<p>Here's a challenge -- prove that permutations of a type are cyclic iff the type has at most 2 terms.</p>

#### [ Mario Carneiro (Nov 05 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812421):
<p>i.e. S3 is not cyclic</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812422):
<p>Could also say perms are abelian iff type has at most 2 terms.</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812428):
<p>Well, do we know that subgroups of a cyclic group are cyclic?</p>

#### [ Mario Carneiro (Nov 05 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812432):
<p>oh yeah, that's even easier</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812456):
<p>and subgroups of an abelian group are abelian</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812459):
<p>If only my minions had started on group theory!</p>

#### [ Mario Carneiro (Nov 05 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812469):
<p>do we have the fundamental theorem of cyclic groups?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812508):
<p>is there really a fundamental theorem of cyclic groups?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812519):
<p>Is there a fundamental theorem for an arbitrary subject?</p>

#### [ Mario Carneiro (Nov 05 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812525):
<p>the classification of finite cyclic groups also sounds pretty cool</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812527):
<p>I just had a rant in a lecture about how the fundamental theorem of algebra had a really terrible name</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812534):
<p>it was named when "algebra" meant the same as "equations", according to Wikipedia</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812555):
<p>or possibly "polynomial equations", my memory fails me</p>

#### [ Mario Carneiro (Nov 05 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812559):
<p>and now "geometry" means "equations"</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812563):
<p>only algebraic geometry</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812578):
<p>what's the fundamental theorem of geometry?</p>

#### [ Chris Hughes (Nov 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812621):
<p>What is the fundamental theorem of cyclic groups?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812625):
<p>Do we have that in Lean?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812637):
<p>I don't know what the FTCG is</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812644):
<p>It will either be the classification</p>

#### [ Mario Carneiro (Nov 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812648):
<p>every cyclic group is isomorphic to Z/nZ for some n, or Z</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812649):
<p>or the universal property</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812667):
<p>apparently it's the classification</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812685):
<p>what's the fundamental theorem of cyclic semimodules?</p>

#### [ Mario Carneiro (Nov 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812695):
<p>I'm pretty sure no one calls it a fundamental theorem except me</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812710):
<p>a semimodule is cyclic if it has a generator</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812796):
<p>People certainly talk about cyclic modules, and the fundamental theorem for them is that a module is cyclic iff it's isomorphic to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mi mathvariant="normal">/</mi><mi>I</mi></mrow><annotation encoding="application/x-tex">R/I</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.07847em;">I</span></span></span></span> for some ideal <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>I</mi></mrow><annotation encoding="application/x-tex">I</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">I</span></span></span></span> of the commutative ring <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span></p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812813):
<p>(and I guess there's an easy generalisation to the non-commutative case)</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812841):
<p>but I don't know enough about semirings to know how this generalises</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812849):
<p>e.g I don't know the definition of a semiring</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812863):
<p>or any examples other than <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">N</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{N}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">N</span></span></span></span></span></p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812937):
<p>Can you have a semimodule for nat whose underlying set is {0,1,2,3} and if you keep adding 1 you get the sequence 0,1,2,3,2,3,2,3,2,3,...?</p>

#### [ Reid Barton (Nov 05 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146812965):
<p>Yes</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813012):
<p>so the fundamental theorem has to deal with both the "tail" and the "loop"</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813027):
<p>eew and if the semiring is non-semiNoetherian then this might be pretty ghastly</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813031):
<p>I can see why they didn't catch on in the maths community</p>

#### [ Reid Barton (Nov 05 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813034):
<p>even if it's, like, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="double-struck">N</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">\mathbb{N}^2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">N</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span> I think things will get complicated</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813042):
<p>Maybe the toric variety guys think about that case</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813052):
<p>don't they do submonoids of N^2 etc?</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813140):
<p>For N^2 you can imagine a wildly complicated module where the two generators ("up" and "right") get you through some maze and if you deviate beyond some perimeter then you have to go back to the start</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813150):
<p>no it can't be that crazy</p>

#### [ Reid Barton (Nov 05 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813152):
<p>The difficulty is that a congruence (an equivalence relation "~" such that a ~ a' and b ~ b' implies a + a' ~ b + b') is no longer uniquely determined by the set of a for which a ~ 0</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813155):
<p>I would need some sort of free semiring for that sort of fun</p>

#### [ Reid Barton (Nov 05 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813249):
<p>when forming the quotient of some algebraic object, you're really quotienting out by a congruence</p>

#### [ Reid Barton (Nov 05 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813326):
<p>it's just that the ability to subtract lets us identify congruences with (for example) submodules, so now submodules are also the things you can quotient by</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813330):
<p>wait -- I thought we were trying to prove that C_2 x C_2 wasn't cyclic</p>

#### [ Kevin Buzzard (Nov 05 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/146813334):
<p>we seem to have wandered a bit</p>

#### [ Kevin Buzzard (Nov 08 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/147329052):
<p>I still can't prove that Z/2 x Z/2 is not cyclic using dec_trivial. Here's an even easier instance of things failing:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">order_of_element</span>

<span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">decidable_eq</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">P</span> <span class="o">:</span> <span class="n">G</span>
<span class="bp">|</span> <span class="n">M</span> <span class="o">:</span> <span class="n">G</span>

<span class="kn">namespace</span> <span class="n">G</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">G</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">elems</span> <span class="o">:=</span> <span class="o">{</span><span class="n">P</span><span class="o">,</span><span class="n">M</span><span class="o">},</span>
  <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">g</span><span class="bp">;</span><span class="n">simp</span>
<span class="o">}</span>

<span class="n">def</span> <span class="n">mul</span> <span class="o">:</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">G</span>
<span class="bp">|</span> <span class="n">P</span> <span class="n">P</span> <span class="o">:=</span> <span class="n">P</span>
<span class="bp">|</span> <span class="n">P</span> <span class="n">M</span> <span class="o">:=</span> <span class="n">M</span>
<span class="bp">|</span> <span class="n">M</span> <span class="n">P</span> <span class="o">:=</span> <span class="n">M</span>
<span class="bp">|</span> <span class="n">M</span> <span class="n">M</span> <span class="o">:=</span> <span class="n">P</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">group</span> <span class="n">G</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="n">mul</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="n">P</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">inv</span> <span class="o">:=</span> <span class="n">id</span><span class="o">,</span>
  <span class="n">mul_left_inv</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
<span class="o">}</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">to_bool</span> <span class="o">(</span><span class="n">M</span> <span class="err">∈</span> <span class="n">finset</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="n">pow</span> <span class="n">P</span><span class="o">)</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">order_of</span> <span class="n">P</span><span class="o">)))</span>
<span class="c1">-- #reduce to_bool (M ∈ finset.image (pow P) (finset.range (order_of P))) -- deterministic timeout</span>

<span class="c1">-- #eval to_bool (M ∈ gpowers P) -- maximum class-instance resolution depth has been reached</span>

<span class="c1">-- example : ¬ (M ∈ gpowers P) := dec_trivial -- max class-instance res</span>

<span class="kn">end</span> <span class="n">G</span>
</pre></div>

#### [ Kevin Buzzard (Nov 08 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/do%20non-cyclic%20groups%20exist%3F/near/147329238):
<p>Note also</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">decidable_gpowers</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">decidable_gpowers :</span>
<span class="cm">  Π {α : Type u_1} {a : α} [_inst_1 : group α] [_inst_2 : fintype α] [_inst_3 : decidable_eq α],</span>
<span class="cm">    decidable_pred (gpowers a)</span>
<span class="cm">-/</span>
</pre></div>


{% endraw %}
