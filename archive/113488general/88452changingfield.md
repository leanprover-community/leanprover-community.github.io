---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88452changingfield.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [changing `field`](https://leanprover-community.github.io/archive/113488general/88452changingfield.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Sep 03 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133230210):
<p>Before we get too involved in field theory, I would like to propose a change to <code>division_ring</code> and <code>field</code>. The problem is that these are defined in core, meaning that we would have to more or less completely ignore all the core definitions based on fields (which isn't much) and add primes or something to avoid name collision.</p>
<p>The change is simply to add <code>div_zero</code> and decidable equality as an axiom to both of them. This will make <code>field</code> the same as <code>discrete_field</code>, so we could just use that, but I think it is not worth the effort to explain to people that they should always use <code>discrete_field</code> instead of <code>field</code>, and there are already several examples of people thinking that <code>field</code> is the more useful one.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133231143):
<p>Mathematicians are not taught "discrete" fields so would probably gravitate to fields naturally given the choice. Isn't there something mentioned about this in one of the doc strings?</p>

#### [ François G. Dorais (Sep 05 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133381566):
<p>Would that imply hiding the current field definition? The distinction is useful for actual computation with real numbers, so there should be a way to go back to the not necessarily discrete case when necessary.</p>

#### [ Johannes Hölzl (Sep 05 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133383028):
<p>I don't think we should actually compute with the reals. If you want to compute with transcendental functions etc,  one needs to implement interval arithmetic or similar. This would be some kind of decision procedure.</p>

#### [ François G. Dorais (Sep 05 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133384484):
<p>I'm puzzled by "we" but just to clarify: hiding the current field and having only discrete fields means that I can't use mathlib at all for many of the things I want to do. Currently, I can still use parts of mathlib that don't rely on decidable equality.</p>

#### [ Reid Barton (Sep 05 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133384705):
<p>What's something you want to do with <code>field</code> that you can't do with <code>discrete_field</code>?<br>
I don't understand how you can get anything out of a real number (other than another real number).</p>

#### [ Reid Barton (Sep 05 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133384899):
<p>At least, not with the real numbers as implemented in mathlib.</p>

#### [ Chris Hughes (Sep 05 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386146):
<p>I think he might be worried because reals aren't really a discrete field. But that doesn't matter because you just cheat and use <code>classical.dec_eq</code> to make the instance.</p>

#### [ Reid Barton (Sep 05 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386420):
<p>I expect François has some specific things in mind, but maybe I misunderstood the meaning of "computation" or "do". I guess proving theorems in constructive real analysis is in some sense a computation, but I don't understand how you can actually run such a computation in Lean and get any useful data out.</p>

#### [ Reid Barton (Sep 05 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386546):
<p>Anyways I don't think you can shadow the existing <code>field</code>, except maybe with notation, which sounds super confusing.</p>

#### [ Reid Barton (Sep 05 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386607):
<p>So is the suggestion basically to rename/copy <code>discrete_field</code> to <code>field'</code>?</p>

#### [ Johannes Hölzl (Sep 05 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386664):
<p>With <em>we</em> I meant users of mathlib's reals.</p>

#### [ Johannes Hölzl (Sep 05 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386836):
<p>Proofs in mathlib shouldn't expect that any equalities on the reals hold by <strong>definitional equality</strong>, i.e. something like <code>(1 + 1 : real) = 2</code> is only by accident provable using <code>rfl</code>. To prove such a statement one would use <code>norm_num</code> or similar.</p>

#### [ Johannes Hölzl (Sep 05 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133387017):
<p>I also think that we currently are forced to use <code>discrete_field</code>. I think we need to wait until Lean 4 comes out to make such a change.</p>

#### [ Mario Carneiro (Sep 05 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133392499):
<p>To be clear, I am on board with not assuming decidable equality when it is not necessary, but there are essentially no examples of instances of <code>division_ring</code> and <code>field</code> that don't have decidable equality. The reason is that <code>has_inv</code> is a <em>total function</em>, which already excludes all the interesting intuitionistic examples of fields like the computable reals</p>

#### [ Mario Carneiro (Sep 05 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133392527):
<p>Basically, <code>field</code> is a worst-of-both-worlds halfway house between decidable fields and nondecidable fields</p>

#### [ Kenny Lau (Sep 05 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133392910):
<p>did the constructivist type theorists never think of this problem?</p>

#### [ Mario Carneiro (Sep 05 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133394241):
<p>The constructivists didn't write <code>field</code>, leo did. A constructivist would be opposed to totalizing <code>inv</code></p>

#### [ Chris Hughes (Sep 05 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133394523):
<p>What's the point in intuitionist reals? Is there a decidable predicate on reals other than true and false?</p>

#### [ Kenny Lau (Sep 05 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133394807):
<p>no, because every function is continuous, and {true, false} is discrete</p>

#### [ Kenny Lau (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133394863):
<p>but there are a lot of decidable predicates on the computable reals / algebraic reals</p>

#### [ Mario Carneiro (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395209):
<p>Careful there; there are decidable predicates on real algebraic numbers but not on computable real numbers (by Rice's theorem)</p>

#### [ Kenny Lau (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395279):
<p>is "I am an algebraic number" decidable over the computable real numbers?</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395290):
<p>Is pi algebraic?</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395296):
<p>That is pretty hard to decide</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395302):
<p>but pi is computable</p>

#### [ Kenny Lau (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395312):
<p>oh, if they were, then we would already know if e+pi is algebraic</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395315):
<p>well, maybe nobody decided yet</p>

#### [ Johan Commelin (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395328):
<p>I decide that it is not.</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395334):
<p>We don't know if every group scheme of order 4 is killed by 4, but there's an algorithm for finding out.</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395415):
<p>It turns into the question "is this completely explicit element of a polynomial ring in about 30 variables over the integers in this completely explicit ideal" and I think one can use Groebner basis techniques to figure it out.</p>

#### [ Chris Hughes (Sep 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395900):
<p>What's an explicit ideal?</p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396254):
<p>it's "here are about 100 explicit polynomials in the variables X1,X2,...,X30, and it's the ideal generated by them"</p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396265):
<p>The last time I asked, the computation was out of reach on a modern machine.</p>

#### [ Simon Hudon (Sep 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396352):
<blockquote>
<p>is "I am an algebraic number" decidable over the computable real numbers?</p>
</blockquote>
<p>Probably not. Rice's theorem which Mario refers to can be paraphrased as "if your predicate over computations is interesting then it's undecidable"</p>

#### [ Leonardo de Moura (Sep 05 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396718):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I did not develop <code>field</code>. It was developed by <span class="user-mention" data-user-id="110596">@Rob Lewis</span>  for Lean 2. I only maintained it and made modifications to make sure it worked with Lean 3. One good news is that the whole algebraic hierarchy has already been deleted from Lean 4.</p>

#### [ Leonardo de Moura (Sep 05 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396870):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I have no idea whether the "four leaf clover" is a positive or negative reaction :)</p>

#### [ Kenny Lau (Sep 05 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396886):
<blockquote>
<p>/me proposes <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span> as the default emoji for marking dreams and wishes that will be trivially realizable when Lean 4 emerges <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>
</blockquote>
<p><a href="#narrow/stream/113488-general/subject/source.20code.20browser/near/133246918" title="#narrow/stream/113488-general/subject/source.20code.20browser/near/133246918">Johan Commelin, 03/09/2018 08:07:17 (UTC)</a></p>

#### [ Johan Commelin (Sep 05 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396945):
<p><span class="user-mention" data-user-id="112857">@Leonardo de Moura</span> No worries. It's meant to be positive. Kudos for all the work you are doing!</p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396948):
<p>Moving the algebraic hierarchy out of core lean seems to be something everyone is excited about.</p>

#### [ Leonardo de Moura (Sep 05 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396988):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Ok, but this one is not in the dream/wish category since it was already deleted several weeks ago. Well, Lean 4 itself may still be a distant dream.</p>

#### [ Patrick Massot (Sep 05 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396999):
<p>Leo, you shouldn't worry about us. We are very happy to use Lean 3, and I'm sure Lean 4 will be even better. Please, do what you think you have to do, at the pace you think is good</p>

#### [ Leonardo de Moura (Sep 05 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397092):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I see. If this is the "happy mode", I wonder how you are going to react when you are not happy ;)</p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397166):
<p>We will work with whatever you come up with.</p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397170):
<p>When it's ready.</p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397200):
<p>and it will almost certainly be better, so we will almost certainly be happy.</p>

#### [ Patrick Massot (Sep 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397204):
<p>I hosted a Lean user meeting in my math department two weeks ago, with Kevin, Johan, Johannes, Mario, Scott, Reid, Chris and Rob. I can tell you everybody seemed very very happy.</p>

#### [ Simon Hudon (Sep 05 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397244):
<p>It doesn't look unhappy to me. Sure there's the occasional whining but I think a lot of it can be attributed to a bunch of mathematician who didn't expect they would need to understand functional programming.</p>

#### [ Patrick Massot (Sep 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397452):
<p>About the specific question of the algebraic hierarchy, it will probably be more convenient to have it outside of the core library but, as far as I know, the current state did not block anything in our experimentations. And the number of mathematicians trying to learn Lean seems to increase much faster than for other proof assistants, if I understand correctly what I heard from <a href="https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341" target="_blank" title="https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341">https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341</a></p>

#### [ François G. Dorais (Sep 06 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409655):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> You're right about <code>has_div</code> (and a few other <code>has_*</code> signatures are wrong too) but I thought I would be the only one to care about this and it wouldn't get fixed until Lean 4 anyway...<br>
In any case, my main goal is to avoid spending an awful lot of time proving trivial things about fields. If all the theorems are about discrete fields then I can't use them in much of my work and I have to re-do them on my own, perhaps by copy/paste most of the time but I might lose the clever tactics and have do do everything over again the painful way...<br>
<span class="user-mention" data-user-id="110032">@Reid Barton</span> Yes, you're right about the confusion. One of the main reasons why Lean is useful for me is that (avoiding non-computational axioms) everything I can do in lean is computable. It's not about writing a program to "do" things, it's reasoning about computational processes...</p>

#### [ Mario Carneiro (Sep 06 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409737):
<blockquote>
<p>If all the theorems are about discrete fields then I can't use them in much of my work and I have to re-do them on my own, perhaps by copy/paste most of the time but I might lose the clever tactics and have do do everything over again the painful way...</p>
</blockquote>
<p>What are you doing that needs non-discrete fields? Note that the name "discrete field" is a misnomer if you are any kind of regular mathematician, it has nothing to do with topology</p>

#### [ Mario Carneiro (Sep 06 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409849):
<p>We've more or less made the decision to not care about constructive math for its own sake in core lean and mathlib. Either your field is actually decidable (i.e. <code>rat</code>), in which case there is no problem, or it is not decidable (i.e. <code>real</code>) but in this case you are working classically anyway so everything is decidable.</p>

#### [ François G. Dorais (Sep 06 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409952):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I agree (and don't really care) about the name. The issue is that decidable equality is a rare luxury in my kind of work. (Admittedly, we're a small crowd, but I care about Lean and how it's useful to me...)</p>

#### [ Mario Carneiro (Sep 06 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409977):
<p>I'm asking what your kind of work is, that makes decidable equality a rarity</p>

#### [ Mario Carneiro (Sep 06 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409988):
<p>I also care about lean being useful to you, but I don't know what you need</p>

#### [ François G. Dorais (Sep 06 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133410606):
<p>I don't need anything specific. I'm happy as things are but the future is where things will be... In Lean 4, as far as I understand, there won't be any algebraic structures (except really basic stuff). So I'll inevitably have to deal with mathlib (or equivalent?) for that kind of basic stuff. If mathlib suddenly decides that all fields have decidable equality then I'll have to stop using it because that's simply not true for my applications. Though my applications are specialized, this is just common sense.</p>

#### [ François G. Dorais (Sep 06 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133411365):
<p>To answer your first question, I work in computability theory and reverse mathematics most of the time these days. Both of these areas use classical logic in the meta sense, but the bottom line is that equality of real numbers is not computable...</p>

#### [ Mario Carneiro (Sep 06 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133411854):
<p>I think that it is better to encode such facts directly, with a notion of computation, rather than trying to work in a weak logic with the hope that the proven theorems correspond to computable facts at a higher meta level</p>

#### [ Mario Carneiro (Sep 06 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133411933):
<p>I think that there is definitely a place for computable reals in mathlib, but I don't think they are an adequate replacement for the real reals</p>

#### [ Mario Carneiro (Sep 06 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412066):
<p>There are additional design considerations that go into it (e.g. efficiency, precision requests, etc), and certain operations (like total division) don't make sense, or at least don't have the same signature that lean wants to give them. At the same time I don't want these considerations to affect regular mathematics, where we just want to write <code>1 / 2</code> and not worry about the details, so it simply won't be a <code>field</code> or <code>field'</code> or whatever, it will be some special thing like <code>computable_field</code></p>

#### [ Mario Carneiro (Sep 06 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412245):
<p>To be perfectly honest, I don't think lean is a very good place to do reverse mathematics, unless you do a deep embedding. "no axioms" lean is already way stronger than ZFC</p>

#### [ Simon Hudon (Sep 06 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412358):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  Didn't you write your proof of soundness relative to ZFC?</p>

#### [ Simon Hudon (Sep 06 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412364):
<p>How does that work if Lean is stronger than ZFC?</p>

#### [ Mario Carneiro (Sep 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412392):
<p>ZFC + omega inaccessibles. I haven't fully checked but I believe that "no axioms" lean also has this consistency strength (I proved it relative to lean plus the big 3 axioms)</p>

#### [ Simon Hudon (Sep 06 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412620):
<p>the three big ones: choice, quot.ind and prop.ext?</p>


{% endraw %}
