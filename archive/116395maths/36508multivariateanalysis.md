---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36508multivariateanalysis.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [multivariate analysis](https://leanprover-community.github.io/archive/116395maths/36508multivariateanalysis.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jeremy Avigad (Oct 10 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135568640):
<p>Friends,</p>
<p>I apologize in advance for this long post. For various projects, I am going to need a good library for multivariate analysis. At minimum, I want to be able to reason about systems of differential equations and dynamical systems on R^n, optimization problems in R^n, etc. The general idea is to look for ways to make Lean and ITP useful for working on problems in applied mathematics. (In the long run, it would be great to have complex analysis, measure theory, optimization on function spaces, stochastic calculus, differential geometry, etc., etc. But the plan is to start small and try to find some compelling prototype applications rather than focus exclusively on building general theory.)</p>
<p>Two examples of the sort of thing it would be good to have are these:</p>
<p>(1) Some of Fabian Immler's very nice work on the dynamical systems background to the numeric calculations related to the Lorenz attractor. (The first paper on his web page is an excellent survey: <a href="http://home.in.tum.de/~immler/" target="_blank" title="http://home.in.tum.de/~immler/">http://home.in.tum.de/~immler/</a>)</p>
<p>(2) Damien Rouhling's very nice formalization of a solution to the inverted pendulum problem (<a href="https://hal.inria.fr/hal-01639819" target="_blank" title="https://hal.inria.fr/hal-01639819">https://hal.inria.fr/hal-01639819</a>) based on the mathcomp library and prior work with Cyril Cohen (<a href="https://hal.inria.fr/hal-01612293" target="_blank" title="https://hal.inria.fr/hal-01612293">https://hal.inria.fr/hal-01612293</a>). </p>
<p>So I can use the Isabelle and mathcomp libraries as a model.</p>
<p><a href="https://www.isa-afp.org/browser_info/current/AFP/Ordinary_Differential_Equations/index.html" target="_blank" title="https://www.isa-afp.org/browser_info/current/AFP/Ordinary_Differential_Equations/index.html">https://www.isa-afp.org/browser_info/current/AFP/Ordinary_Differential_Equations/index.html</a><br>
<a href="https://github.com/math-comp/analysis" target="_blank" title="https://github.com/math-comp/analysis">https://github.com/math-comp/analysis</a><br>
<a href="https://github.com/drouhling/LaSalle" target="_blank" title="https://github.com/drouhling/LaSalle">https://github.com/drouhling/LaSalle</a></p>
<p>Lots of things in that are already in the Lean library will be helpful: topological, limits, polynomials, matrices, the transcendental functions, normed spaces, and Johannes' work on integration. As far as I can tell, these are the things I should work on:</p>
<ul>
<li>The Frechet derivative, defined in general for functions between normed vector spaces</li>
<li>The spaces R^n as instances, connections between linear maps and matrices, polynomials and their derivatives, etc.</li>
<li>ODE's and the Picard-Lindelöf theorem.</li>
</ul>
<p>I am planning to work on this on a fork in my repository but push to a branch of leanprover-community/mathlib often, whenever things look decent.</p>
<p>As usual, lots of little questions and design decisions will arise, such as:</p>
<ul>
<li>how much to bundle (e.g. (f : real -&gt; real) [bounded f] [continous f] or (f : bounded_continuous_function R R))</li>
<li>how much to use type classes for</li>
<li>how to restrict to subdomains (continuous_on f s) or (continuous (restrict f s))</li>
<li>how to handle partial functions</li>
</ul>
<p>I will experiment and raise specific questions here as they come up.</p>
<p>Here is the reason for this long post:</p>
<p>(1) If any of you have advice, suggestions, requests, etc. please let me know.</p>
<p>(2) If any of you are working on related things, or plan to work on related things, please let me know so that we can coordinate and avoid duplication.</p>
<p>In particular, <span class="user-mention" data-user-id="110031">@Patrick Massot</span> , Mario pointed me your differential topology repo. Are you still working on it? Can I steal the chain rule? Is there anything you want me to do or to avoid?</p>

#### [ Kevin Buzzard (Oct 10 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135568777):
<p>You're going to embark upon this in Lean 3?</p>

#### [ Patrick Massot (Oct 10 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135568947):
<p>Of course you can steal anything from my differential topology repo, but I don't think you'll want to. I think everything that was decent has been incorporated into mathlib (the last piece was <a href="https://github.com/leanprover/mathlib/blob/master/analysis/bounded_linear_maps.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/bounded_linear_maps.lean">https://github.com/leanprover/mathlib/blob/master/analysis/bounded_linear_maps.lean</a>). The chain rule proof works but is horribly painful</p>

#### [ Patrick Massot (Oct 10 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569057):
<p>I'm not currently working on this. I'm very slow with Lean, and all my Lean effort is currently driven by the perfectoid project (it happens in the branch <a href="https://github.com/leanprover-community/mathlib/tree/completions" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/completions">https://github.com/leanprover-community/mathlib/tree/completions</a>). My initial hope was to investigate whether it would be possible to do differential topology in Lean because most mathematicians would be very surprised. But clearly I couldn't do that alone, so I preferred to join another project with more mathematicians involved (but we still can't do anything without Johannes and Mario)</p>

#### [ Patrick Massot (Oct 10 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569153):
<p>I really think we should finish the perfectoid project before starting another ambitious project, but if we ever finish perfectoid spaces then I'd be delighted to work on differentiable manifolds with you.</p>

#### [ Patrick Massot (Oct 10 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569166):
<p>Note also <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/banach_contraction.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/banach_contraction.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/banach_contraction.lean</a> that is still waiting for cleanup, but very relevant to your goals</p>

#### [ Kevin Buzzard (Oct 10 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569374):
<blockquote>
<p>I really think we should finish the perfectoid project before starting another ambitious project, but if we ever finish perfectoid spaces then I'd be delighted to work on differentiable manifolds with you.</p>
</blockquote>
<p>I see no obstructions to finishing perfectoid spaces other than the fact that most of the people involved are extremely busy.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569504):
<p>Every issue we have come up against has been solved or will be solved soon.</p>

#### [ Jeremy Avigad (Oct 10 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135570753):
<p>@Kevin, yes, of course, in Lean 3. Where else? <br>
@Patrick, thanks! There is no rush and of course I'd be happy to work together if/when you have time. I just want to make sure I am not stepping on anyone's toes in the meanwhile. The Banach fpt will indeed be helpful.</p>

#### [ Jeremy Avigad (Oct 15 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135800981):
<p>Here's a little report on some things I learned about limits, filters, and set-valued functions this weekend.</p>
<p>Suppose we want to formalize the notion of a limit, and say <code>f x</code> approaches something as <code>x</code> approaches something. The problem is that there are lots of variations on the "somethings" -- <code>x</code> can approach a value or infinity or negative infinity, or it can approach a value from the left or the right, etc. </p>
<p>The solution (described here <a href="http://home.informatik.tu-muenchen.de/~hoelzl/html-data/documents/hoelzl2013typeclasses.pdf" target="_blank" title="http://home.informatik.tu-muenchen.de/~hoelzl/html-data/documents/hoelzl2013typeclasses.pdf">http://home.informatik.tu-muenchen.de/~hoelzl/html-data/documents/hoelzl2013typeclasses.pdf</a> and implemented by Johannes in <code>order/filter.lean</code>) is to write down a general relation <code>tendsto f l1 l2</code>, where <code>l1</code> and <code>l2</code> are filters. The relation <code>tendsto f l1 l2</code> asserts that the preimage of any set in <code>l2</code> under <code>f</code> is an element of <code>l1</code>. Instantiating <code>l1</code>, for example, with the filter of neighborhoods of a point <code>a</code>, we have convergence as <code>x</code> approaches <code>a</code>.</p>
<p>One issue that comes up when doing ordinary calculus is that often we want to restrict attention to a subset of the domain. Think of all the theorems about a function <code>f</code> that is continuous or differentiable on a closed interval <code>[a, b]</code>. When assessing continuity at <code>a</code>, we want to ignore anything outside the interval. The filter technology gives a means of doing this; replacing <code>l1</code> by <code>inf l1 (principal s)</code> restricts the domain to <code>s</code>. The Isabelle library proves all the basic theorems with such restrictions. Replacing <code>s</code> by <code>univ</code> results in the unqualified version.</p>
<p>Mario pointed out to me that sometimes, when working with an interval <code>[a, b]</code>, it is more natural to work with a partial function <code>f</code> on that domain, rather than a total function taking arbitrary values. He has defined <code>data/pfun.lean</code> for that purpose. Working with it is rather pleasant; you write <code>y ∈ f x</code> to say that <code>f</code> is defined at <code>x</code> and equal to <code>y</code>.</p>
<p>The relation <code>tendsto</code> generalizes to a relation <code>ptendsto</code> for partial functions, and if we define <code>res f s</code> to be the restriction of a total function <code>f</code> to a partial function with domain <code>s</code>, we have</p>
<div class="codehilite"><pre><span></span>tendsto f (l₁ ⊓ principal s) l₂ ↔ ptendsto (pfun.res f s) l₁ l₂
</pre></div>


<p>Here both sides say that <code>f</code> tends to <code>l₂</code> along <code>l₁</code> when the domain is restricted to <code>s</code>, but they say it is different ways: the lhs restricts the filter, and the rhs restricts the function. We recover the usual notion of convergence when <code>s</code> is <code>univ</code>, so in a sense working with partial functions is more general, and it avoids the need to mention <code>s</code> explicitly everywhere.</p>
<p>There is a catch, however. When generalizing the <code>tendsto</code> relation, one has to generalize the notion of a <code>preimage</code> to partial functions. Here there are two choices for the preimage of <code>f</code> on <code>s</code>: we can define it as <code>{x | ∃ a ∈ f x, a ∈ s}</code> or <code>{x | ∀ a ∈ f x, a ∈ s}</code>. The first one may seem more natural, but it is the second one, which basically adds all the values outside the domain of <code>f</code> to the first, which gives the equivalence above.</p>
<p>The plot thickens. In set-valued analysis, one further generalizes partial functions to "set-valued functions," which map a value <code>x</code> to a set of values -- possibly the empty set, possibly a singleton, and possibly lots of values. A set-valued function from <code>α</code> to <code>β</code> is really just a relation, but thinking of it as a multi-valued function suggests natural and useful generalizations of definitions and theorems in ordinary analysis, as described in this classic book: <a href="https://www.springer.com/la/book/9780817648473" target="_blank" title="https://www.springer.com/la/book/9780817648473">https://www.springer.com/la/book/9780817648473</a>.</p>
<p>Here is the kicker: both versions of <code>preimage</code> suggested above generalize to relations, and both are considered in set-valued analysis:</p>
<div class="codehilite"><pre><span></span>def rel (α : Type*) (β : Type*):= α → β → Prop

namespace rel

variable (r : rel α β)

def preimage (s : set β) := {x | ∃ y ∈ s, r x y}

def core (s : set β) := {x | ∀ y, r x y → y ∈ s}

end rel
</pre></div>


<p>They give rise to two different notations of convergence. When talking about sequences of sets, the two notions are called "liminf" and "limsup". When used to define continuity of set-valued functions, we get "lower semicontinuity" and "upper continuity". </p>
<p>I implemented the general notions of convergence as <code>rtendsto</code> and <code>rtendsto'</code> in this file: <a href="https://github.com/avigad/mathlib/blob/multivariate/analysis/multivariate/limit.lean" target="_blank" title="https://github.com/avigad/mathlib/blob/multivariate/analysis/multivariate/limit.lean">https://github.com/avigad/mathlib/blob/multivariate/analysis/multivariate/limit.lean</a>. (Here the "r" is for relation.) At the very end, both versions are easily shown to be equivalent to <code>tendsto</code> in the function case, but in general, the two notions are different. In the case of a partial function, the definition is easily shown to be equivalent to <code>ptendsto</code> as defined above.</p>
<p>The bottom line: it seems to me that the fundamental notions of convergence we use should the be relational (set-valued) versions. They strictly generalize the cases of functions and partial functions, but it seems they are no harder to work with. I am inclined to stick with the general versions until there is good reason to specialize, and then to stick with partial functions unless/until there is good reason to restrict to functions.</p>
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> , <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> , what do you think?</p>

#### [ Floris van Doorn (Oct 15 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135806766):
<p>Could you explain briefly why we want to generalize to set-valued functions?</p>

#### [ Kevin Buzzard (Oct 15 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135812012):
<p>I haven't even got more than a few lines into this post and already I've learnt a ton of stuff; I'm currently looking at the "Type classes and filters..." papers by Johannes et al linked to at the top.</p>
<p>1) <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> you and me and others were talking about why the ordering on filters was the opposite of the naive inclusion ordering recently; a very clear and coherent answer is at the top of p7 of the pdf Jeremy links to.</p>
<p>2) <span class="user-mention" data-user-id="110031">@Patrick Massot</span> remember when we were discussing how one was supposed to pronounce <code>tendsto</code>, this fundamental relationship between filters in Lean, and I asked you what the notation was for it in Bourbaki and what terminology they used, and I think neither of us knew and we agreed to go and look it up and then neither of us did? It is described on p8 of this pdf (as <code>LIM</code> or <code>filterlime</code>). But see p2: "While filters have long been used to express limits in topology, our generic limit operator parameterized by two filters is novel (see Section 4.2)." :O Maybe it's not actually in Bourbaki! It seemed like such a natural notion that I assumed it was as old as the hills! Is this due to Johannes et al? Did you know this already? I've only just realised.</p>
<p>I think I'd seen this paper before, but now I have a much better understanding of a filter I got a lot more from it.</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135812795):
<p>No, I didn't know that about the two filters thing. But as a student it's hard to get <em>any</em> exposure to filters; for some reason mathematics teachers everywhere believe that filters are too complicated for anything before grad school, and think that 30 variations on L'Hopital's rule is easier...?</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135812874):
<p>(Needless to say I heartily disagree. I put filters at the same level of abstraction as topological spaces, and I think they should be taught together.)</p>

#### [ Kevin Buzzard (Oct 15 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813295):
<p>Some notes  for mathematicians on Jeremy's post; in <code>data/pfun.lean</code> there is a variant of <code>option</code> defined, called <code>roption</code>, which is noncomputably equivalent to <code>option</code>. One way of thinking about <code>option A</code> in classical maths is that it's the set of subsets of <code>A</code> of size at most 1 (so it's <code>A</code> plus one extra element, here modelled as the empty set). A partial function <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mo>→</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">A\to B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> is just a function <code>A -&gt; option B</code> (they use <code>roption</code> but I am too blinded by 30 years of classical mathematics to understand the difference properly) and the interpretation of <code>option B</code> as subsets of size at most 1 explains the observation Jeremy refers to as pleasant (and indeed it is pleasant). The "catch" Jeremy is talking about comes from the fact that with subsingletons (sets of size at most 1) the difference between exists and forall is that the empty set works with forall but not exists. </p>
<p>This subtlety that Jeremy has uncovered (choosing exists or forall when defining preimage) leads to there being two natural ways to do some things at this hugely abstract level, and he's observing that these two choices give rise to things like liminf and limsup. If you had asked me about this stuff last year I would have said "oh I'm sure it's all in Bourbaki somewhere" but I am genuinely now wondering if this is actually new mathematics. Can anyone here come up with some dusty old book from the 70s where it's all done like this to show these computer science people that they're re-inventing the wheel?  Or are they actually inventing the wheel?</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813542):
<p>Well, the problem with the exists definition of preimage is that it doesn't define a filter</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813549):
<p>because the preimage of univ under a partial function is not univ</p>

#### [ Kevin Buzzard (Oct 15 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813561):
<p>you can look at the filter generated by this?</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813606):
<p>Classically that's the same as this other preimage</p>

#### [ Kevin Buzzard (Oct 15 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813611):
<p>I thought you were going to say that</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813633):
<p>I don't know if this will help, but I think that A -&gt; roption B is actually the "real" partial function the way mathematicians think of it</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813686):
<p>Originally I defined a partial function as a subset of the domain and a function on that subset, but it's equivalent to A -&gt; roption B</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813691):
<p>It is A -&gt; option B that is the weird one</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813703):
<p>When was the last time you totalized your partial functions by adding a new value outside the original domain as a "null" value?</p>

#### [ Kevin Buzzard (Oct 15 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813718):
<blockquote>
<p>(Needless to say I heartily disagree. I put filters at the same level of abstraction as topological spaces, and I think they should be taught together.)</p>
</blockquote>
<p>I have already suggested that filters would be a great second year project topic in our department.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813838):
<p>They've already taught me what it means for a map between topological spaces to be continuous at a point. I was talking to a lecturer at another UK university last month and they explicitly raised this issue -- they were covering for the topology guy in a lecture, and were given his notes to read out, and the notes explicitly said that there was no notion of being continuous at a point for a map between topological spaces.</p>

#### [ Patrick Massot (Oct 15 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135816439):
<p>That paper by Johannes has been cited countless times here on Zulip (and previously on gitter). I think it's the first Lean-related paper I ever printed.</p>

#### [ Patrick Massot (Oct 15 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135816497):
<p>And indeed I wasn't able to find the general <code>tendsto</code> definition in Bourbaki</p>

#### [ Kevin Buzzard (Oct 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135831590):
<p>Yes I've certainly seen it before. But this is the first time I looked at it since I learnt about some of that filter stuff.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135831637):
<p>I actually understand the point of it now!</p>

#### [ Kevin Buzzard (Oct 15 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135832009):
<p>You computer scientists attach value to a completely different set of data to us. For you the theory of filters on a type is some beautiful tool which can help you to make other stuff. I don't think we attach much value to that theory at all. I think it's cool but if you ask me if it's in Bourbaki I would just say I don't know and don't really care, I'm sure it all works great and let's get on with the good stuff. I attach value to the Riemann Hypothesis, some random statement about the zeros of some completely randomly-defined function which is a pain to formalise because it involves analytic continuation but which at the end of the day is no different to any other function really, and the main point seems to be just that humans are worse at finding the zeros for that Riemann function than for some other functions like the identity function.</p>

#### [ Jeremy Avigad (Oct 16 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135865554):
<p><span class="user-mention" data-user-id="111080">@Floris van Doorn</span> <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  I haven't spent much time with it yet, but the book I linked to is a very nice introduction, and the opening chapter makes a good case for the generalization. CMU's library has an electronic copy, and I'd be glad to share it with you.<br>
<span class="user-mention" data-user-id="111080">@Floris van Doorn</span> If you Google around a bit, you'll see that the notion of a set-valued function gets used quite a lot in various branches of applied mathematics. For example, it is used to generalize differential questions to cases where instead of having a unique trajectory you only have some bounds on the possible evolutions of the system (<a href="https://en.wikipedia.org/wiki/Differential_inclusion" target="_blank" title="https://en.wikipedia.org/wiki/Differential_inclusion">https://en.wikipedia.org/wiki/Differential_inclusion</a>, <a href="https://bookstore.ams.org/gsm-41" target="_blank" title="https://bookstore.ams.org/gsm-41">https://bookstore.ams.org/gsm-41</a>). It is used in optimization problems, where a given parameterized problem can have multiple optimum values (<a href="https://www.springer.com/us/book/9783642542640" target="_blank" title="https://www.springer.com/us/book/9783642542640">https://www.springer.com/us/book/9783642542640</a>). It is used in nonsmooth convex analysis to generalize the derivative to the case where there can be multiple "tangent lines" beneath a curve (<a href="https://en.wikipedia.org/wiki/Subderivative" target="_blank" title="https://en.wikipedia.org/wiki/Subderivative">https://en.wikipedia.org/wiki/Subderivative</a>, <a href="https://www.degruyter.com/view/product/467711" target="_blank" title="https://www.degruyter.com/view/product/467711">https://www.degruyter.com/view/product/467711</a>). <br>
By the way, I think branches of applied mathematics like these are good targets for interactive theorem proving: not only is there a lot of symbolic and numeric computation, but the models tend to be complicated and unruly, and one can imagine that a interactive system can help people reason about them rigorously.<br>
That said, my goal isn't to do any of that right away, only develop the notions of limit in as great a generality as conveniently possible while heading toordinary (function-based) analysis.<br>
<span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  I wrote down the notion of a preimage that would make the theorem go through, and I was delighted to find essentially that notion in the book, at least in the particular setting they treat there. I don't think it is radically new or deep mathematics, but it is a nice was of organizing and unifying concepts. This happens a lot with formalization, and I am glad that you find it an interesting and valuable aspect of the whole business.</p>

#### [ Jeremy Avigad (Oct 16 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135865604):
<p>By the way, I seem to be incapable of writing a short Zulip post. Sorry about that.</p>

#### [ Scott Morrison (Oct 16 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135870229):
<p>(We had to train Kevin to remember to hit enter. :-)</p>

#### [ Mario Carneiro (Oct 16 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135870388):
<p>but not too much</p>

#### [ Jeremy Avigad (Nov 08 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147272989):
<p>Here is a progress report on a library for multivariate analysis. I wrote down the definition of the Frechet derivative, but before doing anything with that, I decided to expand the library for limits. It has taken more time than I thought it would. Currently everything is in one file in a branch on <code>leanprover_community</code>, <a href="https://github.com/leanprover-community/mathlib/blob/multivariate/analysis/multivariate/limit.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/multivariate/analysis/multivariate/limit.lean">https://github.com/leanprover-community/mathlib/blob/multivariate/analysis/multivariate/limit.lean</a>.<br>
It includes:</p>
<ul>
<li>operations like <code>dom</code>, <code>codom</code>, <code>image</code>, <code>preimage</code>, and <code>core</code> for relations and partial functions, and relationships to the notions for functions.</li>
<li>generalizations of <code>tendsto</code> to relations (<code>rtendsto</code> and <code>rtendsto'</code>) and partial functions (<code>ptendsto</code>) and relationships between them.</li>
<li>a filter for convergence at a point: <code>tendsto f (at_within a s) l</code> means that <code>f x</code> approaches <code>l</code> as <code>x</code> approaches <code>a</code> within the set <code>s</code>. We define <code>at_pt a := at_within a univ</code>. Note that we need to use "punctured" neighborhoods of <code>a</code>. For example, if <code>f x := if x = 0 then 1 else 0</code> we want <code>tendsto f (at_pt 0) (nhds 0)</code>.</li>
<li>Characterizations of <code>at_within a s</code> in terms of subtypes. For example, given <code>a</code> in a set <code>s</code>, we have <code>tendsto f (at_within a s) l ↔ tendsto (f ∘ (@subtype.val _ s)) (at_pt ⟨a, h⟩) l</code>. Roughly, <code>f</code> converges to <code>l</code> as <code>x</code> approaches <code>a</code> within <code>s</code> if and only <code>f</code> restricted to <code>subtype s</code> converges to <code>l</code> as <code>x</code> approach <code>a</code> on that subtype.</li>
<li>Unwrapping the definition of convergence at a point <code>a</code> within a set <code>s</code> in a metric space.<br>
I plan to develop properties of pointwise continuity along these lines (restricted to sets, on subtypes, with partial functions, etc., etc.) and then put these things in appropriate places and issue a pull request. And THEN I'll move on to derivatives.<br>
Comments and suggestions are welcome.</li>
</ul>

#### [ Mario Carneiro (Nov 08 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147274679):
<p>The move toward a <code>rel</code> type is unexpected, but I can see that we don't have as much as might be expected. As far as integrating it with mathlib, I would want to have a proof that <code>rel A B</code> is a complete lattice, and maybe we could use it for uniformities (once my work on generalizing filters to other lattices lands)</p>

#### [ Mario Carneiro (Nov 08 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147275134):
<p>Also I've mentioned this to you personally, but I would like to minimize the use of <code>at_pt</code> and <code>at_within</code> in our main developments where possible. I think that "punctured neighborhoods" make some undesirable hidden assumptions about separation properties of the underlying topological space, and overall they lead to additional complications. Of course they are necessary in some cases, particularly in functions that divide by zero at the limit point, but in particular they aren't needed for saying that a function is continuous at a point.</p>

#### [ Sebastien Gouezel (Nov 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147283724):
<blockquote>
<ul>
<li>generalizations of <code>tendsto</code> to relations (<code>rtendsto</code> and <code>rtendsto'</code>) and partial functions (<code>ptendsto</code>) and relationships between them.</li>
<li>a filter for convergence at a point: <code>tendsto f (at_within a s) l</code> means that <code>f x</code> approaches <code>l</code> as <code>x</code> approaches <code>a</code> within the set <code>s</code>. We define <code>at_pt a := at_within a univ</code>. Note that we need to use "punctured" neighborhoods of <code>a</code>. For example, if <code>f x := if x = 0 then 1 else 0</code> we want <code>tendsto f (at_pt 0) (nhds)</code></li>
</ul>
</blockquote>
<p>I would like to argue strongly against the use of punctured neighborhoods. For instance, in your last example, I definitely wouldn't want that <code>f</code> tends to <code>0</code> at <code>0</code>, because, well, it does not, for the commonly accepted definition of limit :)</p>
<p>I don't recall any instance in research mathematics where I have seen punctured neighborhoods: they are mainly used in undergraduate courses to define the derivative as <code>lim (f (x+h) - f(x))/h</code>when <code>h</code> tends to 0 and is different from <code>0</code>. However, when you do Frechet derivatives you can also write this as <code>f(x+h) = f(x) + Df(x) h + o(h)</code> (where by <code>o(h)</code> I mean the norm of <code>h</code> multiplied by a function which tends to 0 at 0). And then you don' need to divide by 0 any more.</p>
<p>On the other hand, plain neighborhoods are used all the time. That created a lot of issues for me in Isabelle when working with the analysis library, designed using punctured neighborhoods: I had to argue separately about the value at the point and the value in the punctured neighborhoods many many times. I would have been much more happy with some unpunctured <code>nhds_within a s</code>. </p>
<p>Any thoughts?</p>

#### [ Patrick Massot (Nov 08 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147285332):
<p>I also vote for keeping unpunctured neighborhoods as the default. The general filter machinery can then allow to use punctured neighborhoods in the rare cases where this is useful.</p>

#### [ Mario Carneiro (Nov 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147285403):
<p>It's interesting to hear that <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> , I had a conversation about this with Jeremy and he used Isabelle as a model for a lot of this, based on his previous experiences with the Isabelle analysis library</p>

#### [ Johannes Hölzl (Nov 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147286545):
<p>I think using <code>nhds</code> is much easier. The main reason for me is that composition is easier: <code>tendsto f (nhds x) (nhds y)</code> <code>tendsto g (nhds y) (nhds z)</code> composes nicely using just <code>tendsto.comp</code> while the <code>at</code> statements are <code>tendsto f (at x) (nhds y)</code> and then one needs a special composition rule. This doesn't happen only for <code>tendsto</code> but at other occasions too.</p>

#### [ Sebastien Gouezel (Nov 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147286728):
<p>I want to emphasize that Isabelle multivariate analysis is absolutely wonderful. Extremely well designed and handy to use. The only point that made me pester is the use of punctured neighborhoods. So, using Isabelle's library as a model looks like an excellent idea. And if you could remove the overuse of punctured neighborhoods to make it even better, I would be all the more happy.</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287093):
<p>well, if we aren't using punctured neighborhoods then we should discuss the alternative. The main application, I believe, is for derivatives of various kinds, where you have to divide by zero</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287172):
<p>In metamath I got around this by saying "the function <code>g(h) = if h = 0 then c else (f(x+h) - f(x))/h</code> is continuous at zero", which uses only regular neighborhoods</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287224):
<p>(here <code>c</code> is the claimed derivative of f at x)</p>

#### [ Sebastien Gouezel (Nov 08 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287780):
<p>A linear map <code>L</code> is a derivative of <code>f</code>at the point <code>x</code> along the set <code>s</code> if <code>(f(y)-f(x)-L (y-x))/norm(y-x)</code> tends to <code>0</code> when <code>y</code> tends to <code>x</code> along <code>s</code>. This works since <code>0/0 = 0</code>.</p>

#### [ Patrick Massot (Nov 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287876):
<p>And why dividing? Why not using the little-o definition?</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287882):
<p>I remember you wrote something like that in your definition patrick</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287887):
<p>but I think the little o function is basically unique</p>

#### [ Patrick Massot (Nov 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287892):
<p><a href="https://github.com/math-comp/analysis/blob/master/derive.v#L48" target="_blank" title="https://github.com/math-comp/analysis/blob/master/derive.v#L48">https://github.com/math-comp/analysis/blob/master/derive.v#L48</a></p>

#### [ Mario Carneiro (Nov 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287899):
<p>and you have to write it with division anyway</p>

#### [ Patrick Massot (Nov 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287909):
<p>why?</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287956):
<p>how else are you going to prove that this function exists in a concrete situation?</p>

#### [ Patrick Massot (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287964):
<p>And what do you mean "I wrote something like this"? I wrote <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L18" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L18">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L18</a></p>

#### [ Mario Carneiro (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287975):
<p>right, that</p>

#### [ Patrick Massot (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287976):
<p>And I wrote this because I didn't have a little-o library</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287980):
<p>that epsilon function is unique</p>

#### [ Sebastien Gouezel (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287981):
<p>I prefer the definition with little o, I am only afraid it requires more work to set up. But it avoids division, which is definitely a big plus.</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287983):
<p>and it's a division</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287990):
<p>so you may as well eliminate it</p>

#### [ Patrick Massot (Nov 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287998):
<p>Sébastien, have you seen <a href="https://hal.inria.fr/hal-01719918" target="_blank" title="https://hal.inria.fr/hal-01719918">https://hal.inria.fr/hal-01719918</a>?</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288004):
<p>I am on board if you can find a way to actually avoid division, but I don't think this achieves that</p>

#### [ Patrick Massot (Nov 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288049):
<p>Of course it requires more setup but we need little-o and big-O anyway.</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288063):
<p>this part -&gt; <code>∃ ε : E → F, (∀ h, f (a + h) = f a + L h + ∥h∥ • ε h)</code> can only be satisfied for one function epsilon</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288071):
<p>it's too strict</p>

#### [ Patrick Massot (Nov 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288078):
<p>Of course, but why would you care?</p>

#### [ Patrick Massot (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288084):
<p>And anyway I want little-o instead</p>

#### [ Patrick Massot (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288090):
<p>I want this proof: <a href="https://github.com/math-comp/analysis/blob/master/derive.v#L687" target="_blank" title="https://github.com/math-comp/analysis/blob/master/derive.v#L687">https://github.com/math-comp/analysis/blob/master/derive.v#L687</a></p>

#### [ Mario Carneiro (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288091):
<p>because then it isn't really avoiding division, it's just hiding it</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288098):
<p>and it comes back whenever you actually want to apply the definition</p>

#### [ Sebastien Gouezel (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288101):
<blockquote>
<p>Sébastien, have you seen <a href="https://hal.inria.fr/hal-01719918" target="_blank" title="https://hal.inria.fr/hal-01719918">https://hal.inria.fr/hal-01719918</a>?</p>
</blockquote>
<p>This has been available for a long time in Isabelle :) And Isabelle will also compute limits automatically for you, i.e., it has tactics to compute the limit, say, of <code>(sin x + cos x - e^x)/x^2</code> at <code>0</code>. Or at infinity. Or whatever.</p>

#### [ Patrick Massot (Nov 08 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288265):
<p>They claim to do better little-o/big-O than Isabelle. Have you read it in detail?</p>

#### [ Patrick Massot (Nov 08 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288273):
<p>Mario, the discussion about what I wrote in my calculus file is a bit pointless, this will soon be replaced by using little-o</p>

#### [ Sebastien Gouezel (Nov 08 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288274):
<p>No, I have not read the details (yet). And the limits tactics for Isabelle is very recent, to be honest.</p>

#### [ Patrick Massot (Nov 08 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288373):
<p>There is very preliminary work on porting this to Lean in <a href="https://github.com/leanprover-community/mathlib/blob/landau/analysis/landau.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/landau/analysis/landau.lean">https://github.com/leanprover-community/mathlib/blob/landau/analysis/landau.lean</a> (but it's currently a mess so don't look at it too closely)</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288449):
<p>I don't think being little o or not matters, it's the same definition with a different name</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288648):
<p>What about a definition like: for all <code>ε &gt; 0</code>, for all <code>h</code> near <code>nhds 0</code>, <code>|f (a + h) - f a - L h| &lt;= ε |h|</code></p>

#### [ Patrick Massot (Nov 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288651):
<p>Then I don't see how you would need to divide whenever you want to apply the definition. Let's try to prove that the identity on R is differentiable at 0, with derivative id. Then the definition asks you check that 0 is o(x). This is done in <a href="https://github.com/leanprover-community/mathlib/blob/landau/analysis/landau.lean#L26" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/landau/analysis/landau.lean#L26">https://github.com/leanprover-community/mathlib/blob/landau/analysis/landau.lean#L26</a>. Where do you see a division by x?</p>

#### [ Patrick Massot (Nov 08 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288703):
<p>Mario, what you wrote is exactly the little-o definition!</p>

#### [ Patrick Massot (Nov 08 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288721):
<p>Maybe the confusion comes from the fact we don't share the same definition of little-o</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288726):
<p>yes, I see that this matches your little o definition</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288783):
<p>However I'm not yet convinced of the <code>mklittleo</code> thing</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288787):
<p>I think it is best to just use the definition</p>

#### [ Patrick Massot (Nov 08 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288810):
<p>I'm tempted to first try to trust Cyril and its collaborators</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288849):
<p>was this file Cyril's work in Freiburg?</p>

#### [ Patrick Massot (Nov 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288856):
<p>He helped me write it, but all the ugly parts are solely my mistake</p>

#### [ Patrick Massot (Nov 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288861):
<p>He also helped me with big op and worked on parametricity</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288871):
<p>specifically, I don't think lean's notations will let us do the same trickery that coq does</p>

#### [ Patrick Massot (Nov 08 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288882):
<p>Some stuff work better with Lean parser, some work better in Coq</p>

#### [ Jeremy Avigad (Nov 08 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147301608):
<p>Serves me right for posting a message before going to sleep -- I missed all the fun discussion.</p>
<p>Regarding <code>rel</code>, there are two motivations for introducing it. First, when you are working with relations, it is a lot more pleasant to write <code>rel α β</code> than to write <code>α → β → Prop</code> repeatedly, and it is pleasant to be able to write <code>r.image</code>, <code>r.preimage</code>, <code>r.dom</code>, <code>r.codom</code>, etc. (So much so that I started withing that Lean had the convention that function types were implictly associated to the <code>function</code> namespace, so we could write <code>f.image</code>, <code>f.preimage</code>, etc. I have decided that I don't really like the <code>f '' s</code> and <code>f ⁻¹' s</code> notation, and I will start favoring <code>s.image</code> or <code>set.image f s</code> unless someone talks me out of it.) </p>
<p>I don't feel strongly that the library needs a calculus for relations, and I wouldn't mind keeping it in reserve until a compelling need arises. But if we do have one, I think <code>rel</code> is the way to go. So, if there are no objections, I'll follow Mario's suggestion and make it a lattice instance and prepare it for the library.</p>

#### [ Jeremy Avigad (Nov 08 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147302883):
<p>Setting aside the puncturing issue for a moment, I'll remind readers that <code>at_within a s</code> is basically just <code>nds a ⊓ principal s</code>. The point is that we want to say "f is differentiable on [a, b]" where "differentiable at a" is independent of what f does outside the interval. As far as I can tell, there are three options:</p>
<ul>
<li>Use "at_within" to restrict the domain of interest.</li>
<li>Lift f to a subtype, and make the statement about the subtype.</li>
<li>Restrict f to [a,b] to get a partial function, and make the statement about the partial function.</li>
</ul>
<p>I am most hopeful about the first approach. In my experience with Isabelle, it was easy, intuitive, and natural to relativize statements to sets. But my plan is to support all three in the library and prove equivalences, so we can try all the different approaches and go with whatever works best. </p>
<p>As far as subtypes, packing and unpacking information can be a royal pain in the neck, and for many purposes, like taking intersections or translating sets, we really want [a, b] to be a subset rather than a subtype. Also, as Mario pointed out to me, for some purposes it doesn't work: to define the derivative, we need a subtraction on the domain, and you don't get that if you restrict to a subtype.</p>
<p>Mario seems to think that the third approach will prove the most useful. I am not yet convinced, but I added all the pfun stuff to support it. To see what I am concerned about, take a look at the definition of the Frechet derivative, and now imagine what has to change if f is a partial function. All the operations on the codomain -- addition, substraction, scalar multiplication, the norm -- have to be lifted to partial functions as well. I am not convinced that it will be possible to do all the calculations in a reasonable way, even with some monad trickery, and that it will be worth it.</p>
<p>Anyhow, as I said, my plan is to develop the infrastructure and give it a try as long as it does not make progress too painful.</p>

#### [ Jeremy Avigad (Nov 08 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147303319):
<p>Finally, regarding the "puncturing" issue, I have no strong opinions here. As Johannes points out, it is often easier without it. If we take <code>at_within a s</code> with the definition above, we can have the punctured version with <code>at_within a (s \ {a})</code> if and when we need it.</p>
<p>I don't have my copy of Munkres handy, but I thought the punctured definition was mathematically standard. Googling around supports that:<br>
<a href="https://math.stackexchange.com/questions/1019388/why-are-punctured-neighborhoods-in-the-definition-of-the-limit-of-a-function/1019418" target="_blank" title="https://math.stackexchange.com/questions/1019388/why-are-punctured-neighborhoods-in-the-definition-of-the-limit-of-a-function/1019418">https://math.stackexchange.com/questions/1019388/why-are-punctured-neighborhoods-in-the-definition-of-the-limit-of-a-function/1019418</a><br>
<a href="https://en.wikipedia.org/wiki/Limit_(mathematics)#Limit_of_a_function" target="_blank" title="https://en.wikipedia.org/wiki/Limit_(mathematics)#Limit_of_a_function">https://en.wikipedia.org/wiki/Limit_(mathematics)#Limit_of_a_function</a><br>
But if nobody will stand up for it, I'll give "at_within" the simpler definition and work with that.</p>

#### [ Jeremy Avigad (Nov 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147303439):
<p>Oh, I'll also change the name "at_within" to "nhds_within". It is a better description of the new definition.</p>

#### [ Kevin Buzzard (Nov 08 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147304121):
<p>Just my two cents about punctured neighbourhoods -- I am not an analyst, but my impression is that one sees this punctured neighbourhood stuff precisely at the very beginning when one is formalising limits, and then it very quickly drops off the radar, not least because in practice 99% of functions which 99% of mathematicians deal with are continuous/differentiable/whatever so the issue doesn't <em>seem</em> to come up, at least on the informal level where mathematicians usually work. I am pretty sure that the only time we saw this punctured neighbourhood definition in my mathematical upbringing was in the very first course I took on limits.</p>

#### [ Jeremy Avigad (Nov 08 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147304208):
<p>That speaks in favor of making the simpler <code>nhds_within</code> fundamental, and puncturing explicitly only when we really need to.</p>

#### [ Jeremy Avigad (Nov 08 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147305049):
<p>BTW, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>, I have a new appreciation for <code>filter.comap</code>. It is quite natural for reasoning about induced topologies and subspace topologies:</p>
<div class="codehilite"><pre><span></span>theorem nhds_induced [T : topological_space α] (f : β → α) (a : β) :
  @nhds β (topological_space.induced f T) a = comap f (nhds (f a)) := ...

theorem nhds_subtype (s : set α) (a : {x // x ∈ s}) :
  nhds a = comap subtype.val (nhds a.val) :=
by rw nhds_induced
</pre></div>

#### [ Johannes Hölzl (Nov 08 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147309063):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> </p>
<blockquote>
<p>I have a new appreciation for <code>filter.comap</code>.</p>
</blockquote>
<p>Heh, yes I had the same revelation. I originally introduced it for a special case in uniform spaces. Only later I realized that it is a quiet nice way to express many operations (especially <code>tendsto</code> and <code>prod</code>). I think Manuel Eberl had a similar experience.</p>

#### [ Johannes Hölzl (Nov 08 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147309411):
<p>+1 for <code>nhds_within</code>, I also like <code>rel A B</code>. There are already complete lattice instances for <code>Prop</code> and for <code>-&gt;</code>, so its just about unfolding the definition and using <code>apply_instance</code> to get the complete lattice instance</p>

#### [ Cyril Cohen (Nov 08 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147315179):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> In my experience, keeping total functions, not using subtyping, and passing the domain around as a predicate (i.e. your solution 1) is the most usable presentation, at least in mathcomp...</p>

#### [ Jeremy Avigad (Nov 08 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147317356):
<p>That's helpful to hear. I'll try to keep an open mind, but it is good to know that there is at least one workable approach.</p>

#### [ Patrick Massot (Nov 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147321129):
<p>Jeremy, I don't know uses of calculus for relations, but if you want to develop stuff about relation, you should have a look at the beginning of <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean">https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean</a> to see what can be reused or refactored</p>

#### [ Patrick Massot (Nov 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147321463):
<p><code>filter.comap</code> is indeed essential when working with subspaces and quotients. It's used all over <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean">https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean</a>. It also plays a central role for topological group (the uniform structure is defined using comap, see <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_groups.lean#L27" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_groups.lean#L27">https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_groups.lean#L27</a>)</p>

#### [ Jeremy Avigad (Nov 08 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147322250):
<p>Interesting. This raises the question as to whether <code>rel A B</code> should be <code>A x B -&gt; Prop</code> (definitionally the same as <code>set (A x B)</code>) or <code>A -&gt; B -&gt; Prop</code>. I find the second to be a lot more convenient, but the uniform_spaces library uses the first. I suppose I can see what happens if I replace <code>set (A x B)</code> by my <code>rel A B</code> in the uniform spaces library, but rewriting that whole library and everything that depends on it doesn't sounds like fun. </p>
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>, what do you think? Maybe that should be a project for a rainy day?</p>

#### [ Patrick Massot (Nov 08 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147322408):
<blockquote>
<p>I have decided that I don't really like the <code>f '' s</code> and <code>f ⁻¹' s</code> notation, and I will start favoring <code>s.image</code> or <code>set.image f s</code> unless someone talks me out of it.) </p>
</blockquote>
<p>I'd like to try to talk you out of using <code>s.image f</code> instead of <code>f '' s</code> (and <code>s.preimage f</code> instead of <code>f ⁻¹' s</code>). I don't like these notations, but the alternative really seems attached to the wrong object. It's really a functor attached to <code>f</code> and applied on <code>s</code>, not the other way around. I think there is no good functoriality property of <code>s.image</code>.</p>

#### [ Patrick Massot (Nov 08 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147322498):
<p>Same with filters actually. If <code>F</code> is a filter on <code>a</code> and <code>f : a -&gt; b</code> then <code>map f F</code> is really the functor <code>f_*</code> applied to <code>F</code>.</p>

#### [ Patrick Massot (Nov 08 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147322513):
<p>The notation <code>F.map f</code> feels really weird</p>

#### [ Jeremy Avigad (Nov 08 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147323162):
<p>I know, I really wish I could write <code>f.image s</code>. O.k., maybe I'll just give up and use the notations.</p>

#### [ Reid Barton (Nov 08 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147324231):
<p><code>image f s</code> is also fine, I would say</p>

#### [ Reid Barton (Nov 08 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147324315):
<p>Can Lean disambiguate that from other things called <code>image</code> based on the type of <code>s</code>?</p>

#### [ Reid Barton (Nov 08 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147324342):
<p>(I assume you would have the <code>set</code> namespace open, but perhaps not?)</p>

#### [ Jeremy Avigad (Nov 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147325931):
<p>I usually don't open any more namespaces than I have to, but I can open it, or use <code>open set (image)</code>, or just write <code>set.image f s</code>.</p>

#### [ Patrick Massot (Nov 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358107):
<p>I should also point out that, although I don't see a need for calculus for relations right now, I do see a big need for differentiation of partially defined functions. The (traditional) definition of differentiable manifolds is full of partially defined functions and restrictions of partially defined functions, see <a href="https://en.wikipedia.org/wiki/Differentiable_manifold#Atlases" target="_blank" title="https://en.wikipedia.org/wiki/Differentiable_manifold#Atlases">https://en.wikipedia.org/wiki/Differentiable_manifold#Atlases</a></p>

#### [ Mario Carneiro (Nov 09 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358421):
<p>Right, this is the real application</p>

#### [ Mario Carneiro (Nov 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358433):
<p>The thing is that the derivative of a function or partial function is a relation, not a function</p>

#### [ Mario Carneiro (Nov 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358434):
<p>so if you want something that you can iterate you end up in relations</p>

#### [ Mario Carneiro (Nov 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358485):
<p>It's not even a functional relation in some edge cases</p>


{% endraw %}
