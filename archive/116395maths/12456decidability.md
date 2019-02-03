---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/12456decidability.html
---

## Stream: [maths](index.html)
### Topic: [decidability](12456decidability.html)

---


{% raw %}
#### [ Sebastien Gouezel (Nov 17 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882267):
<p>tldr; why do we have <code>linear_order</code> and <code>decidable_linear_order</code>?</p>
<p>I was bitten recently by the fact that some type classes are built on <code>linear_order</code>, while some theorems require <code>decidable_linear_order</code> (i.e., a linear order in which the relation <code>a ≤ b</code> is decidable).<br>
I think I understand why decidability is important from  a practical point of view: you want <code>dec_trivial</code> to be able to compute, to decide simple things, say on finite sets. What I don't get is why everything could not be said to be decidable, with the caveat that you should not use <code>dec_trivial</code> when something is not computable. Maybe with the possibility to replace noncomputable stuff by computable ones in some types for which you really care about computability. </p>
<p>Could we base all mathlib on <code>decidable_linear_order</code>, removing completely <code>linear_order</code>or would it have dreadful consequences? Let me emphasize that I don't care at all about constructivist mathematics, or the strength of axioms used to prove theorems: my question is really about practical consequences, not philosophical ones -- although I can perfectly hear an answer of the form "there is no practical consequence, but we want to keep it separate for philosophical reasons". </p>
<p>NB: the following typechecks</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="kn">instance</span> <span class="n">zou</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">decidable_linear_order</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span>
  <span class="n">decidable_le</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="k">assume</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec</span><span class="o">,</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="bp">..</span><span class="n">h</span>
<span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Nov 17 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882331):
<p>because <code>abs</code> wants to be computable</p>

#### [ Kenny Lau (Nov 17 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882335):
<p>(now it is not the case that <code>abs</code> is computable implies the order is decidable, which is something I would want Lean to know, because currently we have a noncomputable <code>abs</code> for real)</p>

#### [ Sebastien Gouezel (Nov 17 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882398):
<p>What do you mean, it wants to be computable?</p>

#### [ Kenny Lau (Nov 17 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882423):
<p>it means we want <code>abs</code> to be computable</p>

#### [ Kenny Lau (Nov 17 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882468):
<p>actually I don't know</p>

#### [ Kenny Lau (Nov 17 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147882474):
<p>I'll let other people answer this question</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147885253):
<p>Here's a guess. Some arguments work fine without decidability, some need decidability. As a mathematician I used to barely notice this because the moment I needed some prop to be decidable I'd just switch on <code>classical.decidable_prop</code> or whatever it's called and keep going. More recently I realised that there was a better way to do this -- instead of just switching this on all the time I'd just add the relevant decidability instances to the objects in the results that needed them. This seemed like a more canonical thing to do, because that way people who do care about these things can use my results anyway. Is that an answer to the question or is there more to it in this case?</p>

#### [ Chris Hughes (Nov 17 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147885430):
<p>I think sometimes you define <code>linear_order</code> on a class of types, such that it will be decidable on some of the types but not others, so you don't just want to use classical to define the instance. For reals it's okay to use classical decidability, since you're never going to have proper decidability.</p>

#### [ Sebastien Gouezel (Nov 17 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886086):
<p>There is more to it because of the typeclass system. Take for instance <code>conditionally_complete_linear_order</code>, which extends <code>linear_order</code>. In a theorem, you can not really state the assumption that your order is decidable: if you write <code>[conditionally_complete_linear_order α] [decidable_linear_order α]</code>, then the two statements are talking about different orders, so they don't talk to each other. What you would need is a mixin to add decidability, but it is not really there. And if you add <code>classical.decidable_prop</code> in the header or as a local instance (which I always do), the type class system is not able to use it to convert linear orders to decidable ones automagically. </p>
<p>What I can do for instance is change <code>conditionally_complete_linear_order</code> to extend <code>decidable_linear_order</code> instead of <code>linear_order</code>. Indeed, I have done it in my library, it solves all my typeclasses problems, and the library compiles fine. I wonder if the big guys would accept a PR like that, or if there is a reason to avoid this.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886650):
<p>Oh I see -- there really is an issue here. Yeah, typeclasses are not great for mathematics sometimes, this is why we have <code>distrib</code>s and stuff. But why can't you just add the assumption that your order is decidable? Can't you just make it an extra hypothesis and then feed it to the type class system?</p>

#### [ Chris Hughes (Nov 17 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886705):
<p>No because </p>
<blockquote>
<p>if you write <code>[conditionally_complete_linear_order α] [decidable_linear_order α]</code>, then the two statements are talking about different orders, so they don't talk to each other.</p>
</blockquote>

#### [ Sebastien Gouezel (Nov 17 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886779):
<p>The proper solution is certainly to define yet another class <code>conditionally_complete_decidable_linear_order</code>, defined just like <code>conditionally_complete_linear_order</code> but replacing <code>linear_order</code> with <code>decidable_linear_order</code>, and prove an instance going from it to <code>conditionally_complete_linear_order</code>. But this is getting super-heavy...</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886822):
<p>I mean why can't you just literally put <code>forall a b, decidable (a &lt;= b)</code> in?</p>

#### [ Kenny Lau (Nov 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886823):
<p>just use old structure cmd and you'll be done in one line</p>

#### [ Chris Hughes (Nov 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886829):
<p>Because <code>max</code> is defined on <code>decidable_linear_order</code> not <code>decidable_rel has_le.le</code></p>

#### [ Chris Hughes (Nov 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886830):
<p>As are a bunch of lemmas</p>

#### [ Sebastien Gouezel (Nov 17 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886835):
<p>If one could remove <code>linear_order</code>and cut the complexity in half, I certainly wouldn't mind :)</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886837):
<p>And you can't make the correct instance of <code>decidable_linear_order</code> from the pieces you have?</p>

#### [ Sebastien Gouezel (Nov 17 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886848):
<blockquote>
<p>And you can't make the correct instance of <code>decidable_linear_order</code> from the pieces you have?</p>
</blockquote>
<p>In each proof, yes you can. But not as a global instance, since there is already an arrow in the other direction and you want to avoid loops.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886898):
<p>These issues do seem to come up sometimes. I get the feeling that the type class system is not quite right for maths sometimes. Chris had problems with diamonds coming from very innocuous issues as well, where he had two instances of a singleton (but not a Prop) which were not defeq and this really hurt him.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147886950):
<p>The issue you raise really not mathematical. It's just showing that Lean cannot cope with a situation which comes up very naturally in mathematics.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887001):
<p>There was the whole metric space  / topological space farce too -- the topological space underlying the product of two metric spaces was canonically isomorphic to but not defeq to the product of the underlying topological spaces, and because the type class system was involved Johannes had to jump through all sorts of hoops. This was presented to Patrick and me as some sort of clever trick but all the time I could see that something was wrong in the underlying system. It seemed to be the case that type class inference works great if all functors are forgetful, but the moment you want to do something where you're not in this situation you are in trouble.</p>

#### [ Sebastien Gouezel (Nov 17 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887014):
<blockquote>
<p>The issue you raise really not mathematical. It's just showing that Lean cannot cope with a situation which comes up very naturally in mathematics.</p>
</blockquote>
<p>Let me disagree with this: in mathematics, everything is decidable, so there is just one class and the issue disappears.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887018):
<p>right -- but you are just talking about your specific problem. I'm saying that you are a mathematician running into problems with the type class inference system, and you are by no means alone</p>

#### [ Sebastien Gouezel (Nov 17 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887061):
<p>Yes, I can see I'm not alone!</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887062):
<p>I agree that the other issues are in some sense more non-mathematical than yours :-)</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887068):
<p>but also in Chris' issue there was just one instance, and the issue didn't disappear, because he had two copies of it and they weren't defeq even though they were trivially equal</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887082):
<p>All of us want, in some sense, to be able to insert proofs into the system. "Yes I know you now have two instances of [blah], but here's a proof that they're the same, now stop moaning"</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887124):
<p>You really want to put [decidable_linear_order] into your system and also a hypothesis that the underlying linear orders are the same one.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887126):
<p>But that can't be done</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887134):
<p>Who knows if this will be solved in Lean 4 Kenny. I thought Sebastian said that they weren't going to change the type class system.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887135):
<p>No doubt Mario will wake up at some point and come up with another workaround</p>

#### [ Kevin Buzzard (Nov 17 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887137):
<p>but is workarounds what we really want?</p>

#### [ Reid Barton (Nov 17 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147887551):
<p>I get the sense that <code>decidable_linear_order</code> should have been a mix-in, but we can't just change it because it's in core.</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895225):
<p>I am okay with <code>conditionally_complete_linear_order</code> extending <code>decidable_linear_order</code></p>

#### [ Mario Carneiro (Nov 18 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895226):
<p>your instance is called <code>classical.DLO</code> by the way</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895284):
<p>To quote myself from somewhere, we want to assume decidability when decidability is decidable. So when it's either definitely the case (like <code>rat</code>) or definitely not the case (like <code>real</code>). As chris points out there are times when you are doing a construction over generic types, and there decidability can sometimes cause problems</p>

#### [ Kenny Lau (Nov 18 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895287):
<blockquote>
<p>when decidability is decidable</p>
</blockquote>
<p>@.@"</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895330):
<p>But yes, this is in part because the typeclass exists, in core, and we have to deal with it.</p>

#### [ Reid Barton (Nov 18 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895338):
<p>just use <code>classical.decidable_decidable</code></p>

#### [ Mario Carneiro (Nov 18 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895341):
<p>For <code>conditionally_complete_linear_order</code>, this is already hopelessly non-computable (you can't define anything with the type of <code>Sup</code>) so decidability is fine</p>

#### [ Chris Hughes (Nov 18 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895437):
<p>Aren't integers a conditionally complete linear order?</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895442):
<p>there is no computable instance of it</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895449):
<p>because you can't compute a Sup</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895485):
<p>even on <code>bool</code> it's not computable</p>

#### [ Bryan Gin-ge Chen (Nov 18 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895882):
<p>This is a somewhat-related question I had from back when I was messing with partitions. How much extra stuff would we have to write if we wanted to have a computable Sup over finsets rather than arbitrary sets?</p>

#### [ Kenny Lau (Nov 18 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895924):
<p>zero, because it's there already</p>

#### [ Bryan Gin-ge Chen (Nov 18 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/decidability/near/147895978):
<p>Oh, you're right! I stared at <code>finset.sup</code> before but I didn't understand what I was looking at until now.</p>


{% endraw %}
