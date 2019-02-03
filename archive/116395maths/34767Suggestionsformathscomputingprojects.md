---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/34767Suggestionsformathscomputingprojects.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Suggestions for maths/computing projects](https://leanprover-community.github.io/archive/116395maths/34767Suggestionsformathscomputingprojects.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 29 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880233):
<p>In the UK the system is that the undergraduates come into university having chosen their major and can only do classes offered by the corresponding department(s). The third year undergraduates doing a joint maths/computing degree hence know quite a bit of maths and CS. I have been asked to suggest possible projects for these students. No other pure mathematicians ever get involved. If anyone has any suggestions for projects they they think might be appropriate then I would be very interested to hear them.</p>

#### [ Kevin Buzzard (Sep 29 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880247):
<p>I think 4th years can also take them so MSc level is ok</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880308):
<p>I will suggest a homological algebra project and a project to make <code>math.rat</code>, a class for rational numbers which behaves like a number theorist thinks -- eg you can talk about a math.rat being prime or induct on it if it's known to be a nat etc</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880349):
<p>I'll suggest a number field / Galois theory project maybe</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880351):
<p>I'm not sure why you need another type, like I mentioned before</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880360):
<p>But if there's anything mathsy that anyone wants done then let me know quick</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880363):
<p>just define the typeclasses <code>is_nat_prime</code>, <code>is_nat</code>, <code>is_rat</code> on any nice type</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880399):
<p>Mario are you ok with a typeclass <code>is_nat q</code> on rat in mathlib?</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880406):
<p>I think it should be generic in the type</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880409):
<p>I thought you had reservations about the <code>Prime</code> typeclass</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880410):
<p>On nat</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880413):
<p>it says <code>\ex n, nat.cast n = x</code>, in whatever generality that statement makes sense</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880419):
<p>Is it ok if it's data?</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880421):
<p>sure</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880463):
<p>the name <code>is_nat</code> is a bit misleading in that case, but I don't have a better suggestion</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880464):
<p>at least it's a subsingleton (in char 0)</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880466):
<p>is_of_nat?</p>

#### [ Kevin Buzzard (Sep 29 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880475):
<p>math.nat?</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880523):
<p>I don't think I want to ever use <code>math</code> as a namespace</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880526):
<p>if you do that it's like "wait, what were we doing before?"</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880527):
<p><code>the_real_nat</code></p>

#### [ Mario Carneiro (Sep 29 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880534):
<p>what about <code>natural</code>, <code>integral</code> etc?</p>

#### [ Mario Carneiro (Sep 29 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880547):
<p>like "x is a natural element of A"</p>

#### [ Reid Barton (Sep 29 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882048):
<p>How big a project are we talking about? Have you checked <a href="https://github.com/leanprover-community/mathlib/wiki/Potential-projects" target="_blank" title="https://github.com/leanprover-community/mathlib/wiki/Potential-projects">https://github.com/leanprover-community/mathlib/wiki/Potential-projects</a> for ideas?</p>

#### [ Reid Barton (Sep 29 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882089):
<p>One item I'd like to see that hasn't made it onto that list is covering space theory</p>

#### [ Mario Carneiro (Sep 29 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882161):
<p>I actually went to some effort to do covering space theory in metamath a while back. The big theorem was existence and uniqueness of lifts; it was hard to find an appropriately general statement so it might be of use</p>

#### [ Mario Carneiro (Sep 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882219):
<p>But we need simply connected and path connected spaces first</p>

#### [ Mario Carneiro (Sep 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882222):
<p>also connectedness</p>

#### [ Reid Barton (Sep 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882469):
<p>On an unrelated note,</p>
<blockquote>
<p>just define the typeclasses <code>is_nat_prime</code>, <code>is_nat</code>, <code>is_rat</code> on any nice type</p>
</blockquote>
<p>some lemmas like <code>@[simp] lemma pos_of_is_nat_prime (p : rat) [is_nat_prime p] : p &gt; 0</code> would make this padic norm stuff go a lot more smoothly</p>

#### [ Reid Barton (Sep 29 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882927):
<p>though maybe this doesn't really require the class--I'm still unclear on how exactly simp tries to satisfy side conditions</p>

#### [ Rob Lewis (Sep 29 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882928):
<p>Even just an <code>is_prime</code> class on <code>nat</code> would clean up the padic file a lot. Mario and I discussed this briefly in the first padics PR. I was planning to experiment with it soon.</p>

#### [ Mario Carneiro (Sep 29 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882983):
<p>I am considering just marking <code>prime</code> itself as a class, without changing the theorems</p>

#### [ Kevin Buzzard (Sep 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883042):
<p>One of my students wrote 1000 lines of Lean code on connectedness</p>

#### [ Kevin Buzzard (Sep 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883045):
<p>and never really bothered to mention this to anyone</p>

#### [ Kevin Buzzard (Sep 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883051):
<p><a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/connected_spaces.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/connected_spaces.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/connected_spaces.lean</a></p>

#### [ Rob Lewis (Sep 29 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883114):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> That would certainly work. I wonder if we'd eventually end up duplicating the statements of the theorems with versions that take instance arguments though.</p>

#### [ Kevin Buzzard (Sep 29 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883181):
<blockquote>
<p>How big a project are we talking about? Have you checked <a href="https://github.com/leanprover-community/mathlib/wiki/Potential-projects" target="_blank" title="https://github.com/leanprover-community/mathlib/wiki/Potential-projects">https://github.com/leanprover-community/mathlib/wiki/Potential-projects</a> for ideas?</p>
</blockquote>
<p>Maybe a term, maybe a year, and no I didn't check that -- thanks!</p>

#### [ Rob Lewis (Sep 29 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883196):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> We've had a few CS undergrads come to us looking for BS thesis projects and put together a short list for them. If you have students looking for projects more aligned toward programming/tactics than formalizing, we can share.</p>

#### [ Mario Carneiro (Sep 29 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883282):
<p>By the way, that connectedness file finishes with a big TFAE proof</p>

#### [ Johan Commelin (Sep 29 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134884436):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> How about quadratic forms over Q? Maybe that is too big. But Hasse-Minkowski would be really cool. And we have QR now...</p>

#### [ Johan Commelin (Sep 29 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134884476):
<p>And p-adics, and Hensels lemma... so I think a lot of prerequisites are in place.</p>

#### [ Patrick Massot (Sep 29 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134885324):
<p>What about doing more elementary stuff?</p>

#### [ Tobias Grosser (Sep 30 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134926064):
<p>I am very interested in having functionality similar to: <a href="http://ssr.msr-inria.inria.fr/doc/mathcomp-1.5/MathComp.mxalgebra.html" target="_blank" title="http://ssr.msr-inria.inria.fr/doc/mathcomp-1.5/MathComp.mxalgebra.html">http://ssr.msr-inria.inria.fr/doc/mathcomp-1.5/MathComp.mxalgebra.html</a></p>


{% endraw %}
