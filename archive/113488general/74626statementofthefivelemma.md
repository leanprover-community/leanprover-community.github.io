---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74626statementofthefivelemma.html
---

## Stream: [general](index.html)
### Topic: [statement of the five lemma](74626statementofthefivelemma.html)

---


{% raw %}
#### [ Johan Commelin (Apr 24 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606612):
<p>I just wrote a statement of the five lemma: <a href="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db" target="_blank" title="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db">https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db</a></p>

#### [ Johan Commelin (Apr 24 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606625):
<p>It seems extremely verbose to me. (And no, removing line breaks is not the solution <span class="emoji emoji-1f609" title="wink">:wink:</span> ...)</p>

#### [ Johan Commelin (Apr 24 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606670):
<p>If we ignore the facts that I am (i) not using lowercase greek for types, (ii) write types and conditions in the wrong order, and (iii) write lots of linebreaks; are there ways to improve this statement?</p>

#### [ Reid Barton (Apr 24 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606677):
<p>Not nearly as verbose as the proof, I'm sure <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Reid Barton (Apr 24 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606729):
<p>One thing you could do is package up the underlying set function and <code>is_group_hom</code> instance of each map into a single type</p>

#### [ Johan Commelin (Apr 24 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606737):
<p>I would love to just say: "Hey Lean, all these types are groups, and by the way, all my functions are homomorphisms"</p>

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606923):
<p>sancta mater dei</p>

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606929):
<p>you formalized five lemma</p>

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606933):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> this is dank</p>

#### [ Johan Commelin (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606936):
<p>no I did not</p>

#### [ Johan Commelin (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606938):
<p>Only the statement</p>

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606942):
<p>that’s what i mean</p>

#### [ Johan Commelin (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606945):
<p>Which is not so hard to formalise, right?</p>

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606946):
<p>formalize [sth] = formalize the statement of sth</p>

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606953):
<p>well I never got my hands dirty</p>

#### [ Johan Commelin (Apr 24 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606965):
<p>It's just a lot of repetitive strain injury inducing introductory blabla typing</p>

#### [ Johan Commelin (Apr 24 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606967):
<p>I'm scared of the proof atm</p>

#### [ Johan Commelin (Apr 24 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606972):
<p>But I hope that <code>cc</code> will do a lot of diagram chasing for me</p>

#### [ Johan Commelin (Apr 24 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607023):
<p>Currently my proof starts with <code>split, apply is_group_hom.inj_of_trivial_ker n</code>. And then I'm stuck, because I don't know how to prove that two subsets are equal...</p>

#### [ Johan Commelin (Apr 24 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607026):
<p>I really need a lot of handholding with Lean <span class="emoji emoji-1f616" title="confounded">:confounded:</span></p>

#### [ Johan Commelin (Apr 24 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607236):
<p>How do you split the goal <code>subset_1 = subset_2</code> into proving <code>x \in subset_1 \to x \in subset_2</code> and its converse?</p>

#### [ Reid Barton (Apr 24 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607243):
<p>You can apply <code>set.ext</code></p>

#### [ Reid Barton (Apr 24 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607246):
<p>(I was just about to write something longer, but you said just what it does.)</p>

#### [ Johan Commelin (Apr 24 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607252):
<p>Thanks, that helps. Now I get an <code>\iff</code>. How do I split it into two implications?</p>

#### [ Johan Commelin (Apr 24 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607258):
<p>(And more meta: what is the best way to discover the answer to these questions without spamming Zulip?)</p>

#### [ Johannes Hölzl (Apr 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607355):
<p>Either you use <code>iff.intro</code> or the anonymous constructor written as <code>\&lt; ... ,  ... \&gt;</code> where the VS Code plugin replaces the <code>\&lt;</code> and <code>\&gt;</code> .</p>

#### [ Johan Commelin (Apr 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607358):
<p>Ok, cool</p>

#### [ Johan Commelin (Apr 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607360):
<p>thanks!</p>

#### [ Johannes Hölzl (Apr 24 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607363):
<p>Alternatively: use <code>subset.antisymm</code> then you have it in the right form (the subset relation is defintional equal to forall x <code>subset_1 implies subset2</code></p>

#### [ Johan Commelin (Apr 24 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607504):
<p>What are the advantages of <code>subset.antisymm</code> over the other method?</p>

#### [ Kenny Lau (Apr 24 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607506):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> use split</p>

#### [ Kenny Lau (Apr 24 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607543):
<p>to break down an iff</p>

#### [ Reid Barton (Apr 24 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607552):
<p>In this specific case, I imagine there's probably a lemma that says that it suffices to show that <code>f x = 0 \to x = 0</code></p>

#### [ Johan Commelin (Apr 24 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607684):
<p>Yeah, I've got the trivial part now. If <code>x \in trivial subgroup \to x \in ker</code></p>

#### [ Johan Commelin (Apr 24 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607720):
<p>that's paraphrasing</p>

#### [ Johan Commelin (Apr 24 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607928):
<p>Can I easily rewrite the hypothesis <code>(com₁ : m ∘ f = r ∘ l)</code> into <code>com₁' : \fo x, (m (f x) = r (l x))</code> ?</p>

#### [ Sean Leather (Apr 24 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607939):
<p>Here's <a href="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db#gistcomment-2568165" target="_blank" title="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db#gistcomment-2568165">my attempt</a> to syntactically follow the lemma.</p>

#### [ Sean Leather (Apr 24 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607997):
<p>It probably won't help you prove anything, of course. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Kenny Lau (Apr 24 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608015):
<p>I mean, shouldn’t one prove the weak four lemmas first?</p>

#### [ Johan Commelin (Apr 24 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608057):
<p>One could, of course... but they are basically the two subgoals after the first split</p>

#### [ Johan Commelin (Apr 24 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608062):
<p>There is a good reason to do that though... because then you only have to prove one of them</p>

#### [ Johan Commelin (Apr 24 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608063):
<p>the other follows by duality</p>

#### [ Johan Commelin (Apr 24 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608077):
<p>Still, the proof is a very straightforward diagram chase... so I hope I can convince Lean that it is easy as well</p>

#### [ Johan Commelin (Apr 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608120):
<p>I want to tell lean "For every group_hom \phi that you can see, do this... <code>have := is_group_hom.one \phi</code>"</p>

#### [ Johan Commelin (Apr 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608121):
<p>And things like that</p>

#### [ Johan Commelin (Apr 24 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608129):
<p>And one it has figured out all these basic things, then <code>cc</code> might actually deduce the result</p>

#### [ Johan Commelin (Apr 24 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608176):
<p>But then <code>cc</code> needs to know how to deal with <code>\circ</code>, hence my previous question about rewriting <code>com\1</code></p>

#### [ Johan Commelin (Apr 24 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608213):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> Thanks for the refactoring. It is more readable now (except that I most I would give the arrows names like f_1, g_1 and f_2, g_2 etc...)</p>

#### [ Johan Commelin (Apr 24 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608215):
<p>But it is still a bit verbose, right?</p>

#### [ Reid Barton (Apr 24 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608216):
<p>I added a comment with an "artistic" layout</p>

#### [ Reid Barton (Apr 24 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608218):
<p>(warning: long lines)</p>

#### [ Johan Commelin (Apr 24 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608263):
<p>Ha! I like that one</p>

#### [ Johan Commelin (Apr 24 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608269):
<p>It really explains the diagram. Cool!</p>

#### [ Johan Commelin (Apr 24 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608285):
<p>It would be great of you could tell lean <code>[is_group_hom f g h i j k l]</code></p>

#### [ Johan Commelin (Apr 24 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608332):
<p>something like that, and it just understands that all of them are group homs</p>

#### [ Sean Leather (Apr 24 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608358):
<blockquote>
<p>It would be great of you could tell lean <code>[is_group_hom f g h i j k l]</code></p>
</blockquote>
<p>Something like that would be useful in your case, but you wouldn't want to remove the ability to use multiple-parameter type classes, which it looks like <code>is_group_hom</code> is there.</p>

#### [ Johan Commelin (Apr 24 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608362):
<p>Hmmz, I see</p>

#### [ Johan Commelin (Apr 24 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608415):
<p>Also: <code>↪</code> and <code>↠</code> for injective respectively surjective functions</p>

#### [ Johan Commelin (Apr 24 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608421):
<p>But I guess that might be a bit hard</p>

#### [ Johan Commelin (Apr 24 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608431):
<p>So <code>{f: A ↪ B}</code> means <code>{f: A → B} [function.injective f]</code></p>

#### [ Sean Leather (Apr 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608550):
<p>At the very least, you can <code>open function</code> to avoid having to prepend <code>function.</code>. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Johan Commelin (Apr 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608553):
<p>Aaah, ok. TIL :)</p>

#### [ Johan Commelin (Apr 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608559):
<p>Hmmz TIL is confusing in this context. I meant "Today I Learned"</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609111):
<blockquote>
<p>(And more meta: what is the best way to discover the answer to these questions without spamming Zulip?)</p>
</blockquote>
<p>Spam Zulip. I was in just this situation last September and spamming Zulip was by far the most efficient method. Mario often answered very quickly, and several others too. Now there are more people who can help, and the sooner you're up to speed the sooner you can help others. It's really important that mathematicians learn how to use this software as quickly as possible.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609118):
<p>PS I hope you're going to implement the abstract abelian category proof rather than all the diagram-chasing ;-)</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609134):
<p>[not serious]</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609181):
<p>although, in this crazy, world, who's to say that the abstract universal property proof won't be easier!</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609187):
<p>I find myself in a similar situation right now, as it happens.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609191):
<p>I would like to prove R[1/f][1/g] = R[1/fg] (unique isomorphism of R-algebras)</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609202):
<p>and I have set up all these universal properties and I know I can deduce it from those, and it will be really nice to do</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609215):
<p>but I suspect that if I were to ask Kenny he would just write down a proof with lots of quotient.mk's in which just did everything directly.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609269):
<p>i.e. we have an interface (i.e. a bunch of universal properties) which will enable me to prove my result, but now I realise that someone who knows the underlying implementation can just prove the result directly anyway.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609271):
<p>It might be the same here; you can deduce the 5 lemma from the axioms of an ab cat</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609272):
<p>or from the diagram chase</p>

#### [ Kevin Buzzard (Apr 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609277):
<p>and the proofs will be very different</p>

#### [ Johan Commelin (Apr 24 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609403):
<p>Yes, I see. I think it should be possible to have a diagram_chase tactic</p>

#### [ Johan Commelin (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609416):
<p>And my gut feeling is that <code>cc</code> is almost it. But you need to spam the context with a lot of information about group homomorphisms and kernels etc...</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609488):
<p><code>diagram_chase</code> tactic: I wonder if that's possible!</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609491):
<p>As far as I know these CS people don't really do this kind of maths</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609530):
<p>so you might find that this is actually a possibility once you formalise what you want</p>

#### [ Patrick Massot (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609541):
<p>That would be sooo nice</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609542):
<p>When drawing that snake map from ker(map3) to coker(map1) I always feel I'm making the unique move each time</p>

#### [ Patrick Massot (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609545):
<p>Is the new parser going to accept <code>tikz-cd</code> input?</p>

#### [ Sean Leather (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609546):
<blockquote>
<p>As far as I know these CS people don't really do this kind of maths</p>
</blockquote>
<p><span class="emoji emoji-1f632" title="astonished">:astonished:</span> Diagrams are pretty core to PLT.</p>

#### [ Patrick Massot (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609547):
<p>PLT?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609548):
<p>diagram-chasing in abelian groups is perhaps a bit different</p>

#### [ Sean Leather (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609549):
<p>Programming language theory.</p>

#### [ Patrick Massot (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609550):
<p>thks</p>

#### [ Sean Leather (Apr 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609591):
<blockquote>
<p>diagram-chasing in abelian groups is perhaps a bit different</p>
</blockquote>
<p>Okay. I'm not familiar with it, so that may be.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609593):
<p>Is the theory of abelian categories "complete" in some way?</p>

#### [ Johan Commelin (Apr 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609595):
<p>Yes, I was thinking about tikz-cd as well (-;</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609598):
<p>i.e. "the five lemma is true, so there should be a proof which an algorithm can construct"?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609608):
<p>Just think, we could pester Mario to spend weeks developing such an algorithm, and then use it to prove the five lemma and then say "actually, the five lemma is pretty much the only thing we ever use"</p>

#### [ Johan Commelin (Apr 24 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609609):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Did you see how <span class="user-mention" data-user-id="110032">@Reid Barton</span> rewrote the statement? <a href="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db" target="_blank" title="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db">https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db</a></p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609610):
<p>"but thanks anyway"</p>

#### [ Johan Commelin (Apr 24 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609611):
<p>Ouch</p>

#### [ Johan Commelin (Apr 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609653):
<p>And the snake lemma, and the rest of homological algebra</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609656):
<p>That PR will be rejected because the groups aren't all called alpha</p>

#### [ Johan Commelin (Apr 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609660):
<p>Yeah, I will relabel everything to be alpha_1 alpha_2 etc...</p>

#### [ Johan Commelin (Apr 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609661):
<p>who needs betas</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609716):
<p>I concur with Kenny's "dank" comment</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609717):
<p>This is absolutely great</p>

#### [ Patrick Massot (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609720):
<p>No, you should keep groups G. Mario and Johannes will end up understanding.</p>

#### [ Patrick Massot (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609721):
<p>Don't release pressure on this important issue</p>

#### [ Johan Commelin (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609724):
<p>Sure</p>

#### [ Johan Commelin (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609725):
<p>Was just kidding</p>

#### [ Johan Commelin (Apr 24 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609736):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Well, thanks. I thought it was a good test case</p>

#### [ Reid Barton (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125610505):
<blockquote>
<p>Is the theory of abelian categories "complete" in some way?</p>
</blockquote>
<p>No, <a href="https://mathoverflow.net/a/12799" target="_blank" title="https://mathoverflow.net/a/12799">https://mathoverflow.net/a/12799</a></p>

#### [ Reid Barton (Apr 24 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125610563):
<p>Most similar theories will admit embeddings of the word problem like this, I think. But in diagrams where there are only finitely many ways to compose morphisms (basically, "without loops"), maybe there is hope.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125611247):
<p>Thanks <span class="user-mention" data-user-id="110032">@Reid Barton</span> . I wondered if the abelian-ness of the situation saved our bacon but somehow this automorphism trick gets you back into a non-abelian situation</p>

#### [ Johan Commelin (Apr 24 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612399):
<p>I put an update in the comments of the gist: <a href="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db" target="_blank" title="https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db">https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db</a></p>

#### [ Johan Commelin (Apr 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612404):
<p>The first half of the proof is almost done</p>

#### [ Johan Commelin (Apr 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612413):
<p>There is one stupid <code>admit</code></p>

#### [ Johan Commelin (Apr 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612421):
<p>And I don't get why <code>apply_assumption</code> fails, because 2 lines above, there is <code>f_1 w = y</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612476):
<p>Your definition of im is not great</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612486):
<p>You defined <code>definition im (f : A → B) [is_group_hom f] := f '' (@set.univ A)</code></p>

#### [ Johan Commelin (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612488):
<p>No, no longer</p>

#### [ Johan Commelin (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612489):
<p>See the update</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612490):
<p>Oh OK</p>

#### [ Johan Commelin (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612493):
<p>It is now <code>set.range f</code></p>

#### [ Johan Commelin (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612498):
<p>I dunno if that is better (-;</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612548):
<p>That's definitely better</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612560):
<p>The problem with the old one</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612564):
<p><code>definition im (f : A → B) [is_group_hom f] := f '' (@set.univ A)</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612569):
<p>was that you can write <code>#print notation ''</code> to find out what <code>''</code> expands to</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612577):
<p>and see it expands to <code>set.image</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612581):
<p>and then <code>#print set.image</code> to find what that unfolds to</p>

#### [ Johan Commelin (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612584):
<p>I see...</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612586):
<p>and you see it becomes <code>\ex a, a \in set.univ and f a = b</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612625):
<p>in particular we have some clause which is always true</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612626):
<p>and in the way</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612628):
<p>With your new definition we can do stuff like this:</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612632):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">subgroup</span>

<span class="kn">open</span> <span class="n">function</span> <span class="n">is_group_hom</span>

<span class="n">universes</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">A</span><span class="o">]</span> <span class="o">[</span><span class="n">group</span> <span class="n">B</span><span class="o">]</span>
<span class="kn">definition</span> <span class="n">im</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">G</span> <span class="n">H</span> <span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">[</span><span class="n">group</span> <span class="n">H</span><span class="o">]</span> <span class="o">[</span><span class="n">group</span> <span class="n">K</span><span class="o">]</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">H</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">α</span><span class="o">]</span>
<span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">H</span> <span class="bp">→</span> <span class="n">K</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">Hexact</span> <span class="o">:</span> <span class="n">im</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">ker</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">H</span><span class="o">)</span> <span class="o">(</span><span class="n">Hker</span> <span class="o">:</span> <span class="n">β</span> <span class="n">h</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∃</span> <span class="n">g</span><span class="o">,</span> <span class="n">α</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">h</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="k">have</span> <span class="n">Hker2</span> <span class="o">:</span> <span class="n">h</span> <span class="err">∈</span> <span class="n">ker</span> <span class="n">β</span> <span class="o">:=</span> <span class="o">(</span><span class="n">mem_ker</span> <span class="n">β</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="n">Hker</span><span class="o">,</span>
<span class="n">rw</span> <span class="err">←</span><span class="n">Hexact</span> <span class="n">at</span> <span class="n">Hker2</span><span class="o">,</span>
<span class="n">exact</span> <span class="n">Hker2</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612635):
<p>because after the rewrite, <code>Hker2</code> is definitionally equivalent to what you want</p>

#### [ Kenny Lau (Apr 24 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612647):
<p>I still think you should prove the weak four lemmas first</p>

#### [ Johan Commelin (Apr 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612690):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I am almost done with the first one</p>

#### [ Johan Commelin (Apr 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612693):
<p>Just need to get rid of one stupid <code>admit</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612818):
<p>It's really hard to follow the argument without working hard</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612820):
<p>what is the problem which you're admitting defeat on?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612823):
<p>I see you want to prove y in im f1</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612825):
<p>and I see 100 assumptions</p>

#### [ Johan Commelin (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612827):
<p>Ok, so a minor change. I now have <code>local notation im := set.range</code></p>

#### [ Johan Commelin (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612830):
<p>with backticks around <code>im</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612838):
<p>if you open set you can just use range</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612839):
<p>but I think im is better</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612841):
<p>what is your maths proof of the thing you;re admitting?</p>

#### [ Johan Commelin (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612842):
<p>So, I want to prove <code>y ∈ im f</code></p>

#### [ Johan Commelin (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612845):
<p>and it should follow immediately from the two lines above it</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612888):
<p>I see</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612889):
<p>so name one of them and use rw?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612894):
<p>Although I am not an expert</p>

#### [ Johan Commelin (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612895):
<p>aha, I thought apply_assumption would just kill it off</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612899):
<p>I am skeptical about not naming any assumptions</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612900):
<p>I have never heard of apply_assumption</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612901):
<p>What does it do?</p>

#### [ Johan Commelin (Apr 24 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612915):
<p>It is like <code>apply foo</code>, where <code>foo</code> is an assumption</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612950):
<p>but you need 2 assumptions</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612955):
<p>to deduce what you want</p>

#### [ Johan Commelin (Apr 24 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612958):
<p>yeah, that's true</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612969):
<p>I don't think it's the end of the world to start calling useful hypotheses H1 H2 H3...</p>

#### [ Johan Commelin (Apr 24 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613012):
<p>But <code>rw</code> doesn't work either... I named one of the assumptions:<br>
<code>have foo : f₁ w = y</code></p>

#### [ Johan Commelin (Apr 24 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613017):
<p>And then I try <code>rw foo</code>, but it doesn't work</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613018):
<p>rw \l foo</p>

#### [ Johan Commelin (Apr 24 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613022):
<p>unknown identifier 'foo'</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613036):
<p>I think that you are not proving what you think you are proving</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613081):
<p><code>have foo : f₁ w = y, apply_assumption,</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613083):
<p>That's what you have now, right?</p>

#### [ Johan Commelin (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613085):
<p>Yes</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613091):
<p>so put your cursor just after the comma after the y</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613096):
<p>and you see that the first goal is f1 w = y</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613103):
<p>and there are two goals</p>

#### [ Johan Commelin (Apr 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613104):
<p>Yes</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613106):
<p>and now click after the comma after apply_assumption</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613110):
<p>and there are still 2 goals</p>

#### [ Johan Commelin (Apr 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613152):
<p>aaah</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613154):
<p>so your "proof" didn't prove it</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613164):
<p>this is nothing to do with the naming of the assumption</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613167):
<p>it was just never added to the local context</p>

#### [ Johan Commelin (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613172):
<p>ok, thanks!</p>

#### [ Johan Commelin (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613175):
<p>let me try again</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613178):
<p>Because your context is gigantic</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613180):
<p>you should keep a close eye on the number of goals</p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613183):
<p>which is displayed at the top of the output</p>


{% endraw %}
