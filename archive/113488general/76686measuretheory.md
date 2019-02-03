---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76686measuretheory.html
---

## Stream: [general](index.html)
### Topic: [measure theory](76686measuretheory.html)

---


{% raw %}
#### [ Mario Carneiro (Jul 19 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954535):
<p>Hey, this is just an ad for the rather large commit I just put out. It doesn't add too much new stuff, instead it is doing what I do best, proving the same things other people did but better. :) It's focused primarily on the measure theory development, with the hope that I can bring down some of the compile times in that area. But there are some more substantive changes:</p>
<ul>
<li><code>outer_measure.trim</code> is the truncation of an outer measure to a measurable space</li>
<li><code>measure_space</code> was renamed to <code>measure</code>. There is a good sense of what a measure space could be, and this wasn't it.</li>
<li><code>measure</code> and <code>outer_measure</code> now have coe_fn instances so you don't need to refer to the underlying <code>measure_of</code> function.</li>
<li><code>measure</code> extends <code>outer_measure</code>, so in particular it contains a field that is the outer measure projection, rather than containing a function only defined on measurable sets and recovering the outer measure by extension. In order to ensure we don't add extra measures, we require that a measure is <code>trimmed</code> in the sense above.</li>
<li><code>is_complete</code> asserts that a measure is complete (every null set is measurable)</li>
<li><code>is_null_measurable</code> is the property of differing from a measurable set by a null set. It is proven that this is a sigma algebra, and a measure extends unchanged to this larger algebra; this is the completion of the measure.</li>
<li><code>lebesgue</code> has mostly the same theorems but the proofs are rather different. In particular the proof that intervals are measured correctly uses compactness instead of the least upper bound property.</li>
<li>Some more interval theorems were added; <code>Icc</code> is the closed interval</li>
</ul>

#### [ Kevin Buzzard (Jul 19 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954606):
<p>Mario do you know about Haar measure? There's a canonical measure on any locally compact Hausdorff topological group (for example the real numbers).</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954650):
<p>The proof is "do the same as for the real numbers, but with an arbitrary locally compact Hausdorff topological group".</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954654):
<p>although some details are a lot more fiddly if I'm honest...</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954682):
<p>I have heard of it, but I've never done anything with it besides getting uncomfortable about "unique up to a multiplicative constant"</p>

#### [ Patrick Massot (Jul 19 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954740):
<p>Lebesgue is also only determined up to a multiplicative constant on a finite dimensional real vector space</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954753):
<p>Well, who said [0,1] should have measure 1...</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954762):
<p>Oh, I forgot to mention I added scalar multiplication of measures; they are unfortunately not a module since the base "ring" is <code>ennreal</code></p>

#### [ Patrick Massot (Jul 19 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954773):
<p>If you talk about [0,1] then you've already chosen a basis of your 1-dimensional vector space</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954778):
<p>yes, my comment was supposed to be before yours :-)</p>

#### [ Patrick Massot (Jul 19 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954790):
<p>Too bad we miss an opportunity to enjoy module type class hell</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954845):
<p>If CS people are happy to divide by 0, why can't they multiply by infinity?</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954851):
<p>Just make it 0 :-)</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954869):
<p>actually <code>ennreal</code> is surprisingly nice as an ordered semiring</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954880):
<p>the fact that it is a complete lattice really helps</p>

#### [ Patrick Massot (Jul 19 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954881):
<p>That's the trouble: if I understand correctly Mario <em>is</em> happy to multiply by infinity</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954981):
<blockquote>
<p>a basis of your 1-dimensional vector space</p>
</blockquote>
<p>It's not a vector space</p>

#### [ Patrick Massot (Jul 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954991):
<p>affine space I should say</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955000):
<p>is there a notion of semi-vector space in the literature?</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955007):
<p>there are no negatives</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955061):
<p>I am amazed that this is not already in Lean</p>

#### [ Patrick Massot (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955062):
<p>You know we already don't want to talk about semirings</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955070):
<p>I guess a monoid is just a semi-module over N</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955085):
<p>I find of am as well. We have semi everything else, but modules pick right up at rings</p>

#### [ Kevin Buzzard (Jul 19 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955126):
<p>actually maybe that's a commutative monoid</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955195):
<p>A nat-semi-module is a commutative monoid</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955215):
<p>but if the scalar field is something else then it's different</p>

#### [ Patrick Massot (Jul 19 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129957474):
<p>I'm curious about all this integration stuff in mathlib. I never tried to use it or even looked at it. Can we do crazy things like proving the integral of <code>id</code> on <code>[1, 2]</code> is <code>3/2</code>?</p>

#### [ Sean Leather (Jul 20 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129979482):
<blockquote>
<p>Hey, this is just an ad for the rather large commit I just put out. It doesn't add too much new stuff, instead it is doing what I do best, proving the same things other people did but better. <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>
</blockquote>
<p>Thanks for that, <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>!</p>

#### [ Mario Carneiro (Jul 20 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129979507):
<p>you were the one who mentioned the issue with <code>meaure'_union</code>, right? I may have gone a bit overboard. :)</p>

#### [ Sean Leather (Jul 20 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129979565):
<blockquote>
<p>you were the one who mentioned the issue with <code>meaure'_union</code>, right? </p>
</blockquote>
<p>Indeed, I was.</p>
<blockquote>
<p>I may have gone a bit overboard. <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>
</blockquote>
<p>No problem! As long as you think it improved things.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981327):
<p>Actually I have a problem too -- Fermat's Last Theorem can't currently be proved by <code>finish</code> -- can you fix it for me Mario?</p>

#### [ Johan Commelin (Jul 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981388):
<p>Kevin, the proof is <code>by ᛗᛃᛟᛚᚾᛁᚱ</code></p>

#### [ Sean Leather (Jul 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981390):
<p>This is the <code>Mario</code> variation of the <code>ᛗᛃᛟᛚᚾᛁᚱ</code> tactic.</p>

#### [ Johan Commelin (Jul 20 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981468):
<p>Speaking of hammers... I would like the decomposition theorem for mixed Hodge modules.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981485):
<p>Yeah well I would like perfectoid spaces but I spent an hour last night writing the universal property of quotient groups :-/</p>

#### [ Kenny Lau (Jul 20 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981494):
<p>should have told me to write it lol</p>

#### [ Kevin Buzzard (Jul 20 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981498):
<p>Can you do algebraically closed fields Kenny? Chris' polynomials in one variable got accepted</p>

#### [ Kevin Buzzard (Jul 20 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981499):
<p>Things are happening :-)</p>

#### [ Kenny Lau (Jul 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981561):
<p>have you proved that k[X] is UFD?</p>

#### [ Kevin Buzzard (Jul 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981569):
<p><a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/quotient_group.lean" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/quotient_group.lean">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/quotient_group.lean</a></p>

#### [ Kevin Buzzard (Jul 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981574):
<p>Do we even have a definition of UFD? It's pretty ugly</p>

#### [ Kenny Lau (Jul 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981578):
<p>also I think we need "a in L/K: a is integral over K iff K(a) is finite"</p>

#### [ Kenny Lau (Jul 20 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981588):
<blockquote>
<p>Do we even have a definition of UFD? It's pretty ugly</p>
</blockquote>
<p>A is UFD iff (A\{0})/A* is a free monoid :)</p>

#### [ Kevin Buzzard (Jul 20 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981590):
<p>Blair is doing fdvs. Why not ask her if you can help?</p>

#### [ Kevin Buzzard (Jul 20 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981636):
<p>We need more UG maths!</p>

#### [ Johan Commelin (Jul 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981648):
<p>So we need more UG's, so that we can prove things <code>by UG</code>. You do have access to two hammers!</p>

#### [ Kenny Lau (Jul 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981650):
<p>let's say we've built L such that every polynomial in K[X] splits over L. How then do you show that L contains an algebraically closed field?</p>

#### [ Kenny Lau (Jul 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981660):
<p>I think we should prove that K[X] is ED, that might help</p>

#### [ Johan Commelin (Jul 20 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981699):
<p>That was almost there, right?</p>

#### [ Kenny Lau (Jul 20 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981706):
<p>how should we prove "L is algebraically closed iff every finite extension of L is L"? that would involve building splitting fields</p>

#### [ Johan Commelin (Jul 20 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981707):
<p>Except that the definition of ED wasn't optimal, so Chris had to work with degree + 1, or change the definition</p>

#### [ Johan Commelin (Jul 20 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981728):
<p>I guess you want to do separable closure at the same time</p>

#### [ Kenny Lau (Jul 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981783):
<p>my point is, there's a long way to go before we build algebraic closure</p>

#### [ Johannes Hölzl (Jul 20 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985250):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> there is no integral in mathlibs measure theory, yet.</p>

#### [ Johannes Hölzl (Jul 20 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985369):
<blockquote>
<p>Oh, I forgot to mention I added scalar multiplication of measures; they are unfortunately not a module since the base "ring" is <code>ennreal</code></p>
</blockquote>
<p>Yeah, semimodules would be nice to have. But up to now I didn't find any literature on them.</p>

#### [ Patrick Massot (Jul 20 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985492):
<p>Oh, I didn't even imagine that. I was concerned about the fact that we don't have derivative and that could be a problem when wanting to compute integrals.</p>

#### [ Johannes Hölzl (Jul 20 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985626):
<p>Well, the basic theory of integrals in measure theory doesn't need derivatives. It starts with integration over the Lebesgue measure. But there is some theory to be developed up to this point.</p>

#### [ Patrick Massot (Jul 20 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985681):
<p>Sure, that's why I though we could have integrals but no mean of computing one</p>

#### [ Patrick Massot (Jul 20 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985691):
<p>But let's have normed spaces first <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Kevin Buzzard (Jul 20 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985812):
<blockquote>
<blockquote>
<p>Oh, I forgot to mention I added scalar multiplication of measures; they are unfortunately not a module since the base "ring" is <code>ennreal</code></p>
</blockquote>
<p>Yeah, semimodules would be nice to have. But up to now I didn't find any literature on them.</p>
</blockquote>
<p>Maybe that's because most mathematicians think they're about as useless as <code>distrib</code>s? Having said that, the existence of distribs proves that computer scientists have very different opinions to mathematicians as to what is "nice to have". What would mathlib want semimodules for? Is this something to do with compile times or something?</p>

#### [ Kevin Buzzard (Jul 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985886):
<p>A related story : <span class="user-mention" data-user-id="110044">@Chris Hughes</span> decided to do group actions yesterday, and his first question was "wait -- there's no mention of the inverse in the definition?". "No", I replied. "Oh dear, then we'll have to make it monoid actions if we want to get it into mathlib..."</p>

#### [ Johannes Hölzl (Jul 20 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985954):
<p><code>semimodules</code> would help to abstract some basic proofs and syntax. we can abstract the scalar multiplication over <code>measure</code>, <code>outer_measure</code>, measurable functions into <code>ennreal</code>, integrable functions into <code>ennreal</code>, etc...</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014392):
<blockquote>
<p>there is no integral in mathlibs measure theory, yet.</p>
</blockquote>
<p>FYI I started working on that yesterday</p>

#### [ Kenny Lau (Jul 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014435):
<p>nice</p>

#### [ Patrick Massot (Jul 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014452):
<p>Does it mean you'll do derivatives as well?</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014469):
<p>no, like Johannes said, those two are completely unrelated except for a certain fundamental theorem</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014474):
<p>obviously the fundamental theorem can't be stated until we have both parts</p>

#### [ Patrick Massot (Jul 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014517):
<p>There are indeed completely unrelated except for their fundamental relation</p>

#### [ Patrick Massot (Jul 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014530):
<p>Anyway, it's already great to work on integrals</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014532):
<p>I don't even think they operate on the same kinds of spaces. There are spaces with integrals but no derivatives and vice versa</p>

#### [ Patrick Massot (Jul 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014540):
<p>sure</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014561):
<p>so it's not like they are really different sides of the same coin, as in you could use either one to define the other</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014627):
<p>but I guess people care about R -&gt; R and it's true there</p>

#### [ Patrick Massot (Jul 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014634):
<p>it's an important special case, especially for teaching purposes</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014658):
<p>especially when it gives people the weird impression that these things are fundamentally related</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014672):
<p>they are related, but not fundamentally</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014717):
<p>in the foundational sense</p>

#### [ Patrick Massot (Jul 20 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014722):
<p>Since you seem to be in an analytical mood, what about returning to the oldest open mathlib PR?</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014765):
<p>Well, measure theory isn't quite analysis</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014769):
<p>Let's put it next on the list</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014820):
<p>that will set us up for derivatives</p>

#### [ Kenny Lau (Oct 14 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776602):
<blockquote>
<blockquote>
<p>there is no integral in mathlibs measure theory, yet.</p>
</blockquote>
<p>FYI I started working on that yesterday</p>
</blockquote>
<p>how is it now?</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776650):
<p>Johannes has taken over on that development</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776653):
<p>I think it might be merged now? I heard some talk about it but I haven't checked</p>

#### [ Patrick Massot (Oct 14 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776655):
<p><a href="#narrow/stream/116395-maths/subject/How.20much.20of.20analysis.20is.20formalised.3F/near/135735421" title="#narrow/stream/116395-maths/subject/How.20much.20of.20analysis.20is.20formalised.3F/near/135735421">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/How.20much.20of.20analysis.20is.20formalised.3F/near/135735421</a></p>

#### [ Kenny Lau (Oct 14 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776663):
<p>ok</p>


{% endraw %}
