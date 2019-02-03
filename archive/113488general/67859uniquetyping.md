---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67859uniquetyping.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [unique typing](https://leanprover-community.github.io/archive/113488general/67859uniquetyping.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Mar 15 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123746502):
<p>Success! I managed to finally show that Lean's full type system has unique typing (which implies stuff like it is impossible to prove <code>Type 0 : Type 0</code>), even if you use "full" definitional equality, i.e. the transitive and undecidable ideal version of what lean checks. Since it uses a reduction that is guaranteed to run forever on subsingleton eliminators like <code>acc</code>, it yields an alternative semi-decision procedure for testing definitional equality.</p>

#### [ Simon Hudon (Mar 15 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123747869):
<p>Any chance it's a Lean proof?</p>

#### [ Moses Schönfinkel (Mar 15 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123747919):
<p>Good one.</p>

#### [ Mario Carneiro (Mar 15 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123748037):
<p>No, it's still in the informal stage, although the proof is sufficiently subtle that it might be a good idea to formalize it just to make sure it all actually works as advertised.</p>

#### [ Patrick Massot (Mar 15 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123748094):
<p>Wouldn't a Lean formalization be self-referential?</p>

#### [ Mario Carneiro (Mar 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123748257):
<p>Sure, but it wouldn't be the first time a proof assistant has proven parts of itself. Also unique typing is weaker than soundness - even if the type system is inconsistent there are many things that can't be defeq. I did not need to assume any inaccessible cardinals in the proof, it's a purely syntactic proof</p>

#### [ Simon Hudon (Mar 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123748490):
<p>I guess even if self-referential, it might be a good way to find errors. You might want to write it in Isabelle (or something else) if you want to avoid the self-referential criticism but even Lean would help get the details right</p>

#### [ Kevin Buzzard (Mar 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752285):
<p>Does your work shed any light on whether it is possible to make Lean's definitional equality "better" whilst still remaining decidable? Actually here is an even dumber question. Is the transitive closure of Lean's definitional equality still decidable? One's first thought is "of course not, if you want to prove <code>x=y</code> by finding <code>z</code> such that <code>x=z</code> and <code>z=y</code> then where do you start?", but if transitivity somehow only fails in some controlled way then perhaps there is some algorithm which spits out sensible choices for <code>z</code>.</p>

#### [ Gabriel Ebner (Mar 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752298):
<blockquote>
<p>Is the transitive closure of Lean's definitional equality still decidable?</p>
</blockquote>
<p>No.</p>

#### [ Kevin Buzzard (Mar 15 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752351):
<p>This doesn't surprise me at all. How does one go about proving this?</p>

#### [ Gabriel Ebner (Mar 15 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752355):
<p>It's the standard interaction between subsingleton elimination (in particular <code>acc.rec</code>) and proof irrelevancy.  See also <a href="https://leanprover.github.io/reference/expressions.html#computation" target="_blank" title="https://leanprover.github.io/reference/expressions.html#computation">https://leanprover.github.io/reference/expressions.html#computation</a></p>

#### [ Gabriel Ebner (Mar 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752490):
<p>The trick is that 1) you can encode functions with unbounded recursion using well-founded recursion (where the proof is e.g. exfalso), 2) you can evaluate such functions as many steps as you have nested <code>acc.intro</code>s, 3) by proof irrelevancy all such <code>acc.intro</code> terms are definitionally equal.  You can for example now ask whether the original function returns <code>0</code> when given <code>0</code> using a definitional equality test, and this problem is undecidable.</p>

#### [ Kevin Buzzard (Mar 15 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752623):
<p>Thanks for the added information. This will greatly decrease the amount of time it will take to me to understand your previous comment :-) I'm sure this is standard DTT stuff but I am still a beginner. Thanks.</p>

#### [ Kevin Buzzard (Mar 15 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123752686):
<p>Aah so in fact this seems to be exactly the trick used to show that defeq isn't transitive in the reference manual. I have never taken the time to understand that proof before -- I just verified that it worked and moved on. I think that at the time I knew so little Lean that it just looked too daunting to get to the bottom of.</p>

#### [ Mario Carneiro (Mar 15 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123767735):
<blockquote>
<p>Does your work shed any light on whether it is possible to make Lean's definitional equality "better" whilst still remaining decidable?</p>
</blockquote>
<p>The proof does a good job of pointing the finger squarely at subsingleton eliminators. That is, if there were no inductive types such that:</p>
<ul>
<li>The inductive type is a Prop family</li>
<li>The inductive type has one constructor</li>
<li>The constructor has at least one non-prop argument</li>
<li>The constructor has at least one recursive argument</li>
<li>All non-prop arguments appear in the output type</li>
</ul>
<p>then definitional equality would be decidable.</p>

#### [ Mario Carneiro (Mar 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123767813):
<p>Probably the same can be said about proof irrelevance, but that's baked in a bit more thoroughly, so it's less obvious how it would change the proof.</p>

#### [ Andrew Ashworth (Mar 15 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123768875):
<p>i was searching "subsingleton elimination" and one of the top results was this: <a href="https://www.cs.cmu.edu/~cangiuli/sigbovik/unintentional.pdf" target="_blank" title="https://www.cs.cmu.edu/~cangiuli/sigbovik/unintentional.pdf">https://www.cs.cmu.edu/~cangiuli/sigbovik/unintentional.pdf</a></p>

#### [ Andrew Ashworth (Mar 15 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123768881):
<p>not totally related but possibly humorous</p>

#### [ Mario Carneiro (Mar 15 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123768927):
<p>Oh, I was wrong about needing at least one non-prop argument. Here's an extremely simple type, simpler than <code>acc</code>, that also causes the same problems (non-transitivity, undecidability)</p>
<div class="codehilite"><pre><span></span>inductive T : Prop
| mk : T → T

variables (x : T) {α : Sort*} (f : α → α)
def fix : α := T.rec (λ _, f) x
example : fix x f = f (fix x f) :=
show fix (T.mk x) f = f (fix x f), from rfl
</pre></div>

#### [ Kevin Buzzard (Mar 15 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123770686):
<p>You have a variable of type <code>T</code> but I am not sure it's possible to construct anything of type T. </p>
<div class="codehilite"><pre><span></span>variable y : false
example : false := y
</pre></div>


<p>This has caused a lot more trouble than undecidability. I don't really understand what you're saying yet but I am still optimistic it's within my grasp. You seem to have proved that every function has a fixed point, given a variable of type <code>T</code>, a type for which there are no instances. What does this have to do with non-transitivity and undecidability? Sorry if this is all standard.</p>

#### [ Mario Carneiro (Mar 15 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771207):
<p>That's correct - I didn't mention it but <code>(x : T)</code> is an inconsistent context. <code>fix</code> is also inconsistent, but from a soundness perspective that's no surprise, inconsistent in, inconsistent out. The point is that this is a fixpoint operation that works definitionally, so I can execute unbounded computations exactly as one might use <code>fix</code> in haskell. For example, let <code>f : (nat -&gt; unit) -&gt; (nat -&gt; unit)</code> such that <code>f g n := if TM halts at n then () else g (n+1)</code>, then <code>fix f 0</code> evaluates all the steps of a turing machine, resulting in <code>()</code> if and only if the TM halts, so <code>fix x f 0 =?= ()</code> is undecidable.</p>

#### [ Mario Carneiro (Mar 15 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771287):
<p>Note that the other known examples of undecidable definitional equality problems also occur in inconsistent contexts. I'm not certain if it suffices to assume the context is consistent, but if "consistent" is replaced by "inhabited" (i.e. there is a concrete sequence of terms which satisfies the context) then it is equivalent to asking if reduction terminates in the empty context, which is also known as strong normalization. This is believed to be true, but I guess that will be another big chapter</p>

#### [ Kevin Buzzard (Mar 15 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771484):
<p>Strong Normalization is an open problem -- is that correct? I read it in the reference manual I guess. It feels to me a bit like the 3n+1 problem :-)</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771545):
<p>I don't think it is, although you have to pull out the big guns to prove it, since it implies that lean is consistent</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771552):
<p>Hmm let me dig out the quote.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771569):
<p>section 3.7</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771570):
<p>"The reduction relation is believed to be strongly normalizing, which is to say, every sequence of reductions applied to a term will eventually terminate."</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771572):
<p>These definitional equality problems are a little counter intuitive, because you want to reason that in an inconsistent context anything goes, but that's actually not the case. Even if you prove <code>0 = 1</code>, you still cannot prove that <code>0 == 1</code> definitionally</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771612):
<p>"Believed to be" is code for "no one's done the work". That's my job :)</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771614):
<p>Oh I see!</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771617):
<p>Is that your thesis problem?</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771626):
<p>It's one of the nearby problems, I'm not quite sure what my thesis will be exactly but something along these lines</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771632):
<p>I guess it depends on what I get done, but unique typing is a major step forward</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771675):
<p>soundness is the next step, by modeling everything in ZFC + omega inaccessibles</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771689):
<p>then strong normalization, where you use the rank of a term's ZFC interpretation as the wellfounded decreasing measure</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771691):
<p>I think that modeling Lean in ZFC + omega inaccessibles is how I initially tried to understand type theoy.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771739):
<p>Assuming that inductive structures don't add a bunch of axioms I wasn't expecting, this sounds straightforward to me and is probably all well-known. Is that right?</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771741):
<p>That's actually the easiest part, it's quite straightforward. But there are some places where I need to know that if a term is a Prop then it's not a Type, and unique typing was necessary for that</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771755):
<p>Oh so you use all this to prove strong normalization??</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771757):
<p>I thought you were just going to argue by induction on number of unicode characters in the term :-)</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771760):
<p>Like I said, big guns</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771807):
<p>remember from Godel that anything that implies Con(lean) is going to require some advanced mathematics</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771810):
<p>I know people who would say that anything that implies Con(lean) is going to require something that is strictly stronger than mathematics</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771814):
<p>If mathematics = lean, sure :)</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771817):
<p>beyond mathematics, rather than advanced mathematics</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771818):
<p>Oh, mathematics is ZFC :-)</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771819):
<p>Of this there is little doubt</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771826):
<p>You don't believe in the existence of grothendieck universes?</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771866):
<p>in the sense that 90% of mathematicians don't have a clue what mathematics is but know how to use it, 9.9% know what ZFC is and use that, and then the other 0.1% worry about other possibilities.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771875):
<p>Didn't I share that link from a recent Scholze paper recently?</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771876):
<p>And there's also some section in the stacks project</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771877):
<p>Real, serious, mathematicians actually occasionally go out of their way to justify to the rest of the world that what they are doing can be done in ZFC</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771883):
<p>I always get the sense from regular mathematicians that if large cardinals come up they just assume them and move on</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771884):
<p>Those are just the amateurs</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771885):
<p>like Wiles, I think</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771888):
<p>Yup</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771890):
<p>He doesn't know how to remove it, but he knows who to ask</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771931):
<p>This is how mathematics is actually done in 2018.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771932):
<p>It's farcical.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771933):
<p>We all believe we're working in ZFC</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771941):
<p>and occasionally someone writes a chapter in a paper saying "I know section 5 was full of categories of rings, but actually we could look at the category of rings which live in V_kappa for kappa=2^2^2^2^2^2^aleph_0 and it all still works, so it's OK we're doing ZFC"</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123771943):
<p>and then all of us amateurs go "oh that's a relief, it's still holding out"</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772003):
<p><a href="http://www.math.uni-bonn.de/people/scholze/EtCohDiamonds.pdf" target="_blank" title="http://www.math.uni-bonn.de/people/scholze/EtCohDiamonds.pdf">http://www.math.uni-bonn.de/people/scholze/EtCohDiamonds.pdf</a></p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772004):
<p>one of the best living mathematicians, 2017 paper, check out section 4</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772063):
<p>Algebraic geometry genius Johan de Jong's stacks project: <a href="https://stacks.math.columbia.edu/tag/000F" target="_blank" title="https://stacks.math.columbia.edu/tag/000F">https://stacks.math.columbia.edu/tag/000F</a> and <a href="https://stacks.math.columbia.edu/tag/000H" target="_blank" title="https://stacks.math.columbia.edu/tag/000H">https://stacks.math.columbia.edu/tag/000H</a></p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772066):
<p>All of that crap just so we can say "it's OK, we're still in ZFC"</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772150):
<p>What's happening is that large cardinals come up (99% of the time in the form "this functor from the category of rings to the category of sets is representable") and people either say nothing (the normal situation) or they note that functors are a bit problematic in ZFC but they read somewhere in the stacks project that it was all OK, or maybe Brian Conrad told them once. There is no formal reference that "everything is OK", but people know who to ask if they're worried</p>

#### [ Kevin Buzzard (Mar 16 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772206):
<p>Over the last year I have come to regard this position as farcical. What are the point of foundations? They're to make your life easier! Not so Scholze has to take time out from being a father of 2 small kids and generating a pile of amazing arithmetic algebraic geometry so he can write down some crap about cardinals just to prove that his latest theory fits into ZFC.</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772285):
<p>As far as Con(lean) is concerned, the easy/lazy approach (that I will take, at least at first) is to assume omega inaccessibles and prove it. You can be more refined though, since for a specific proof you only need n inaccessibles for some n &lt; omega. It might be possible to even trim down the universes themselves so that they aren't quite grothendieck universes, and then maybe you can fit it all in ZFC, but this probably fails in some extreme cases (like when constructing a model of ZFC in lean)</p>

#### [ Mario Carneiro (Mar 16 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unique%20typing/near/123772972):
<p>By the way, <a href="https://www.fing.edu.uy/~amiquel/publis/types02.pdf" target="_blank" title="https://www.fing.edu.uy/~amiquel/publis/types02.pdf">https://www.fing.edu.uy/~amiquel/publis/types02.pdf</a> "The not so simple proof-irrelevant model of CC" is my competition in the soundness part; I contend that it is exactly as simple as it looks, and they made some poor modeling decisions in there that made things complicated</p>


{% endraw %}
