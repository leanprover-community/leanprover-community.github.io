---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49648foundationsofmathematics.html
---

## Stream: [maths](index.html)
### Topic: [foundations of mathematics](49648foundationsofmathematics.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875861):
<p>I spent some time over the last couple of days learning about Voevodsky's work in type theory. I found this paper <a href="https://arxiv.org/abs/1711.01477" target="_blank" title="https://arxiv.org/abs/1711.01477">https://arxiv.org/abs/1711.01477</a> by Dan Grayson quite illuminating.</p>

#### [ Kenny Lau (Apr 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875865):
<p>quite high</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875869):
<p>It seems to me that univalent foundations is similar to, but not the same as, DTT</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875870):
<p><code>a = b</code> is not a Prop in univalent foundations</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875877):
<p>In fact there seems to me to be no impredicative Prop universe in univalent foundations</p>

#### [ Patrick Massot (Apr 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875879):
<p>What happened to your project of documenting what's in mathlib?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875882):
<p>there are just some universes, and a Prop is basically defined to be a subsingleton</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875923):
<p>But the claim is the same as in Lean -- "we can use this set-up as a way of doing all of maths"</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875924):
<p>kenny would love hott</p>

#### [ Kenny Lau (Apr 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875926):
<blockquote>
<p>kenny would love hott</p>
</blockquote>
<p>nope</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875928):
<p>One major weakness (possibly only temporary) is that the model you're supposed to carry around is that a type can be thought of as a topological space</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875932):
<p>but apparently they can't construct the n-sphere from the axioms</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875935):
<p>so they add n-spheres as new inductive types</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875936):
<p>and then they can't prove the theory is consistent</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875937):
<p>This does not bode well, as far as I can see.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875938):
<blockquote>
<blockquote>
<p>kenny would love hott</p>
</blockquote>
<p>nope</p>
</blockquote>
<p>are you a fair-weather constructivist</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875941):
<p>I also re-watched Voevodsky's Newton Institute talk from last yeat</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875944):
<p>year</p>

#### [ Kenny Lau (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875945):
<p>abuse of topology</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875984):
<p>and his discussion about how he tried to persuade Suslin to re-prove some theorem of his constructively</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875985):
<p>because Voevodsky wanted to prove an old theorem of Voevodsky constructively in this univalent foundations way</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875994):
<p>but my impression was that Suslin had no interest in the question (perhaps unsurprisingly, as I know essentially 0 mathematicians who care about constructive maths)</p>

#### [ Kenny Lau (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875995):
<p>1</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875996):
<p>and it seemed that Voevodsky was losing interest in the whole project of checking the proof anyway (or perhaps he was stuck)</p>

#### [ Kenny Lau (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875997):
<p>Alessio Corto</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124875998):
<p>Alessio Corti</p>

#### [ Kenny Lau (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876037):
<p>sure</p>

#### [ Patrick Massot (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876039):
<p>To me it settles the question: HoTT is constructive ⇒ I don't care</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876042):
<p>I think Voevodsky is something else</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876045):
<p>I think HoTT might be a third thing</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876046):
<p>I'm not sure though</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876049):
<p>Is Univalent Foundations = HoTT? I'm not so sure</p>

#### [ Patrick Massot (Apr 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876060):
<p>More precisely: it's constructive ⇒ I think it's irrelevant to most mathematics</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876062):
<p>I completely agree.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876064):
<p>So here are some questions.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876103):
<p>We know that Lean will allow classical logic, and to be quite frank if it didn't allow it then I definitely would not be here.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876104):
<p>I should say Lean 3, because at some point one has to talk about what Lean 2 was</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876106):
<p>Univalent Foundations seems to have been implemented in Coq, but there are lots of rules about commands in Coq which you are _not allowed to use_ in Univalent Foundations</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876112):
<p>e.g. you are not allowed to make new inductive types</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876116):
<p>you have to stick to the ones they made in the core files</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876118):
<p>But I should get to the point.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876119):
<p>If I am interested in mathematics, done in classical logic</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876159):
<p>then what are my options for doing this in type theory?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876163):
<p>DTT I know, because Lean 3</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876164):
<p>HoTT?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876165):
<p>Univalent Foundations?</p>

#### [ Kenny Lau (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876167):
<p>Voevodsky is high</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876169):
<p>And if there is more than one option, why should I choose Lean 3?</p>

#### [ Kenny Lau (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876170):
<p>that settles it</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876171):
<p>Voevodsky is dead :-(</p>

#### [ Kenny Lau (Apr 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876177):
<p>oh rip</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876186):
<p>there are very few popular dtt languages; you've already listed two, coq and lean, and there is also agda and idris</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876227):
<p>i think ats might also be based on dtt</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876229):
<p>basically the only other contender is not based on dtt at all, which is isabelle</p>

#### [ Kenny Lau (Apr 10 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876230):
<p>how is she doing</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876287):
<p>It is worth noting that both Agda and Idris are primarily programming languages. Unlike Lean and Coq.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876298):
<p>isabelle is quite popular amongst mathematicians</p>

#### [ Kenny Lau (Apr 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876300):
<p>because it ain't constructive?</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876302):
<p>because they press Sledgehammer butan'</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876303):
<p>What are Isabelle's foundations?</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876308):
<p>Isabelle is a metalanguage, you can instantiate it with whatever you feel like. Isabelle/HOL is the most popular.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876351):
<p>i know little of isabelle. but my impression is most people work in set theory</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876352):
<p>This is what Hales used for Kepler, right?</p>

#### [ Kenny Lau (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876358):
<p>one should make a proof-assistant based on ZFC</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876360):
<p>As in ZF(C)? Mmm, I've always thought it's mostly just HOL.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876361):
<p>that's already been done 30 years ago</p>

#### [ Kenny Lau (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876366):
<p>who?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876369):
<p>Apparently proof assistants based on ZFC are hard to use</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876405):
<p>I think Mario told me this</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876407):
<p>the original big one was called mizar</p>

#### [ Kenny Lau (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876410):
<blockquote>
<p>Apparently proof assistants based on ZFC are hard to use</p>
</blockquote>
<p>another reason why ZFC is BS</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876411):
<p>I believe Isabelle/ZFC is also a thing.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876412):
<p>i recall sebastian gouzel was also slightly annoyed with isabelle</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876414):
<p>something about it being impossible to define the adeles</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876416):
<p>(whatever they may be)(</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876419):
<p>What do you mean by impossible?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876425):
<p>Kenny is supposed to be defining the adeles in Lean</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876426):
<p>once he's finished revising his mechanics</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876427):
<p>discussion of the adeles is beyond my pay grade</p>

#### [ Sean Leather (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876430):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span>:</p>
<blockquote>
<p>i think ats might also be based on dtt</p>
</blockquote>
<p><a href="https://groups.google.com/d/msg/ats-lang-users/k-6NMsZYllo/mePvbC3tCwAJ" target="_blank" title="https://groups.google.com/d/msg/ats-lang-users/k-6NMsZYllo/mePvbC3tCwAJ">Not quite</a></p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876477):
<p>There is certainly no obstruction to defining the adeles in Lean</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876478):
<p>There is once you don't have dependent types (a'la Isabelle).</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876479):
<p>yes, iirc he said that was a major draw for him to work in dtt</p>

#### [ Kenny Lau (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876482):
<blockquote>
<p>discussion of the adeles is beyond my pay grade</p>
</blockquote>
<p>it isn't quite hard to understand if you start simple, i.e. start with Q</p>

#### [ Patrick Massot (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876483):
<p><a href="https://gitter.im/leanprover_public/Lobby?at=5a2daedfffa3e379191e9195" target="_blank" title="https://gitter.im/leanprover_public/Lobby?at=5a2daedfffa3e379191e9195">https://gitter.im/leanprover_public/Lobby?at=5a2daedfffa3e379191e9195</a></p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876484):
<p>Kenny, the adeles of a general number field K are just (adeles of Q) tensor_Q K</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876491):
<p>and because you did tensor product</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876493):
<p>you can do adeles for a general number field</p>

#### [ Kenny Lau (Apr 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876496):
<p>wonderful</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876537):
<p>The adeles are an easy exercise given what we have</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876538):
<p>isabelle and coq currently have ::quite:: an advantage in library size</p>

#### [ Kenny Lau (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876539):
<p><strong><em>quite</em></strong></p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876540):
<p>leaving aside isabelle, why would you use lean over coq? mostly for nicer unicode syntax</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876541):
<p>But we seem to have a proof that isabelle is not suitable for all of mathematics?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876543):
<p>Lean &gt; Coq -- because tactics</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876552):
<p>however if you wanted to jump straight into doing research mathematics, you can't in lean because mathlib is far smaller than its coq competitors</p>

#### [ Kenny Lau (Apr 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876556):
<p>far smaller than it is coq competitors</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876560):
<p>and I think that nicer unicode syntax, whilst this might just be superficial for CS people, will I think be important to undergraduate mathematicians</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876563):
<p>Coq &gt; Lean because of existing tactics. Lean &gt; Coq because of the way you write tactics.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876602):
<p>But I am playing the long game</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876604):
<p>So I choose Lean. However this thread was basically my attempt to review this choice.</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876607):
<p>If you're playing the very long game, it might still be the case Coq &gt; Lean, Ltac2 is coming.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876611):
<p>If I can understand the claim that "Isabelle can't do the adeles" then we can cross Isabelle off the list</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876618):
<p>But what about HoTT?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876622):
<p>And what about UniMath?</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876623):
<p>hott is not ready for anything, it is a subject of research</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876624):
<p>And this does not apply to DTT</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876625):
<p>because Coq</p>

#### [ Kenny Lau (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876627):
<p>let's do things over NBG</p>

#### [ Kenny Lau (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876667):
<p>or just second order peano arithmetic</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876669):
<p>The original univalence axiom is not constructive. There's cubical type theory extension thereof tho: <a href="https://arxiv.org/abs/1611.02108" target="_blank" title="https://arxiv.org/abs/1611.02108">https://arxiv.org/abs/1611.02108</a></p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876670):
<p>dtt without any funny additions has been proven sound</p>

#### [ Kenny Lau (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876672):
<p>sound!</p>

#### [ Kenny Lau (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876673):
<p>sound in what?</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876674):
<p>as in you can do useful things with it and not summon false from anywhere</p>

#### [ Kenny Lau (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876675):
<p>how do you even define sound</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876676):
<p>by "proven sound" you mean "relative to ZFC + existence of infinitely many inaccessible cardinals" right?</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876679):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Funny you should say that. My table currently contains "Subsystems of second order arithmetic".</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876680):
<p>You can't prove that anything is sound, in some sense</p>

#### [ Kenny Lau (Apr 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876688):
<p>exactly</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876693):
<p>without assuming consistency of some less-likely-to-be-sound system</p>

#### [ Kenny Lau (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876742):
<p>forget about the reals</p>

#### [ Kenny Lau (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876744):
<p>just do peano arithmetic</p>

#### [ Kenny Lau (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876746):
<p>and then embed ZFC within</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876747):
<p>and then Goedel encode everything.</p>

#### [ Kenny Lau (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876748):
<p>and then you can do the reals</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876761):
<p>i think for undergraduates who are not trying to do research mathematics, lean is nicer for reading and writing tactics (though i doubt they will get around to writing tactics)</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876769):
<p>Actually, Coq has much nicer tactic-description syntax still.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876772):
<p>coq is the winner if you're trying to make something that will be around for years</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876814):
<p>it has been around for decades</p>

#### [ Kenny Lau (Apr 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876823):
<p>feit thompson e.g.</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876825):
<p>You can pattern match on goals themselves for example. There's no obscure monad with arbitrary <code>pexpr</code> transforming functions.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876835):
<p>i think writing tactics is beyond most mathematician's interest</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876837):
<p>realistically speaking</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876842):
<p>Realistically speaking, using Lean is beyond most mathematician's interest :P.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876845):
<p>also true</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876848):
<p>i think this has a sadder part though</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876851):
<p>using Lean is beyond most CS peoeple interest as well</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876901):
<p>well, most cs majors would rather have a tooth pulled than work with something that reminds them of their undergraduate discrete math course</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876956):
<p>most people studying CS want to be "programmers", there's no clear distinction between CS and software engineering in academia, for worse or worse</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876958):
<p>I agree about tactics. For now.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876961):
<p>But I am going to make mathematicians interested in Lean.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876964):
<p>if you split the two cleanly then academic CS may as well be in the math department along with the statisticians</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876970):
<p>and logicians</p>

#### [ Patrick Massot (Apr 10 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124876974):
<blockquote>
<p>But I am going to make mathematicians interested in Lean.</p>
</blockquote>
<p>Then we need more documentation, for instance your old project of describing mathlib</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877016):
<p>oh yeah sorry Patrick I didn't respond to your earlier question</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877019):
<p>I am still trying to figure out all the finite stuff</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877022):
<p>but multiset.lean is so long</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877033):
<p>My blog post about induction was just some consequence of me trying to understand finite stuff</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877035):
<p>For mathematicians, finite sets are so important and foundational</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877036):
<p>and I found them very hard to do in DTT</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877038):
<p>but I am slowly getting on top of them</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877039):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> well we then need to communicate better what to expect in a CS course at least... it is as you said, tooth extraction wins over discrete math for many students I teach...</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877078):
<p>My middle child is a budding CS student and he was moaning about discrete maths only 2 days ago</p>

#### [ Andrew Ashworth (Apr 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877082):
<p>surely he knows better than to moan about maths to you, haha</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877084):
<p>:-)</p>

#### [ Patrick Massot (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877085):
<p>I know I'm always writing the same thing, but did you read that Coq bigoperator paper?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877091):
<p>I was reading it yesterday</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877093):
<p>I learnt some stuff</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877095):
<p>For example I didn't really know how to prove that sum from 0 to n of f(i) equalled sum from 0 to n of f(n-i)</p>

#### [ Kevin Buzzard (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877099):
<p>but I can now see a nice way of doing it using bigoperators</p>

#### [ Sean Leather (Apr 10 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877102):
<p>Discrete math was one of my favorite undergrad courses.</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877154):
<p>I teach Java to students that had compulsory discrete math one semester prior. They think I'm evil when I want them to, and I quote, "remember what properties equivalence relations have"... :-\</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877208):
<p>In summary then, apparently HoTT isn't ready, UniMath I am still unsure about, Isabelle has problems with adeles, Mizar didn't catch on for some reason, so there's only DTT left?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877248):
<p>And if it turns out that Coq &gt; Lean then I just switch to Coq</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877250):
<p>that is a bonus. if lean ever dies everything you've learnt moves easily over to coq</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877260):
<p>Can I write a regular expression which turns all my Lean proofs into Coq proofs?</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877265):
<p>that's a little ambitious :)</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877266):
<p>Oh Ok</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877267):
<p>I don't know what you CS guys can do</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877310):
<p>I don't think it's a completely ridiculous idea.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877318):
<p>i mean, it's theoretically possible to write a transpiler. but who would do the work?</p>

#### [ Patrick Massot (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877329):
<p>Lean advantages over Coq are not only about unicode. You also get better overall ergonomics. And, most of all, less constructive stuff.</p>

#### [ Patrick Massot (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877335):
<p>And <em>much</em> better documentation</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877336):
<p>How is less constructive stuff a good thing?!</p>

#### [ Patrick Massot (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877340):
<p>It's a good thing for mathematics, not for everything</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877341):
<p>well.. lean, instead of having less constructive stuff, just has _less_ stuff :)</p>

#### [ Patrick Massot (Apr 10 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877382):
<p>From what I understand, in Coq you need to spend more energy fighting constructivism</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877385):
<p>In Dan Grayson's article he argues that constructive maths is better than normal maths because constructive maths is a generalisation of normal maths</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877386):
<p>I was like "..."</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877390):
<p>I should tell all the group theorists I know to move into monoid theory</p>

#### [ Patrick Massot (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877393):
<p>Exactly what I was about to write</p>

#### [ Patrick Massot (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877395):
<p>let's all do monoids!</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877396):
<p>actually let's just do set theory</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877398):
<p>who cares about structure</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877399):
<p>we have the classification theorem already</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877446):
<p>each one bijects with a unique cardinal</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877447):
<p>so off we go</p>

#### [ Moses Schönfinkel (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877448):
<p>this is surprisingly reminiscent of static vs dynamic typing discussion</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877449):
<p>also, unimath is basically hott</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877450):
<p>unimath is dtt + univalence</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877451):
<p>What is this documentation comment Patrick?</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877452):
<p>and then a bunch of mathematics</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877454):
<p>I thought Coq had some big chunky tomes</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877455):
<p>like, actual math, like i recall seeing a construction of the reals using dedekind cuts</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877463):
<p>so unimath is basically mathlib + univalence</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877464):
<p>equality is not a prop in unimath</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877465):
<p>apparently</p>

#### [ Kevin Buzzard (Apr 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877466):
<p>equality in unimath seems more like \equiv in Lean</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877508):
<p>if i knew more homotopy theory i'd feel more eager to say things about hott :)</p>

#### [ Patrick Massot (Apr 10 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877561):
<blockquote>
<p>What is this documentation comment Patrick?</p>
</blockquote>
<p>Coq has <em>no</em> documentation targeting mathematicians. TPIL is written for us, and beats anything I've seen about Coq by a very wide margin.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124877956):
<p>yes, the big three textbooks for coq are: <a href="https://softwarefoundations.cis.upenn.edu" target="_blank" title="https://softwarefoundations.cis.upenn.edu">software foundations</a>, <a href="http://adam.chlipala.net/cpdt/" target="_blank" title="http://adam.chlipala.net/cpdt/">certified programming with dependent types</a>, and <a href="https://www.labri.fr/perso/casteran/CoqArt/coqartF.pdf" target="_blank" title="https://www.labri.fr/perso/casteran/CoqArt/coqartF.pdf">coq'art</a>. ssreflect also has a good manual <a href="https://math-comp.github.io/mcb/book.pdf" target="_blank" title="https://math-comp.github.io/mcb/book.pdf">here</a>. notice all but the last is focused towards programmers...</p>

#### [ Patrick Massot (Apr 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124878169):
<p>SSReflect manual is clearly going in the right direction compared to the other three, but it's still much harder to read that TPIL (I tried reading it before switching to Lean).</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879260):
<p>I thought that Coq also had some useful introductory tutorials. But I agree with Patrick that TPIL is a very good read for mathematicians.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879285):
<p>Patrick -- I was going to write something else for mathematicians, where I enter tactic mode on page 1 and basically never leave, and also on page 1 I do mathematics rather than goofing around with logic, doing basic mathematical proofs of familiar statements like stuff involving congruences right from square 1. I show them the tactics they need and we go from there.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879333):
<p>I still think that term mode is too hard for mathematicians. You clearly have a programming background. I am guessing that you were happy with lambda notation for functions before you started reading these docs.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879336):
<p>I would like to suppress lambda notation for as long as possible.</p>

#### [ Patrick Massot (Apr 10 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879345):
<p>I agree wholeheartedly with all those goals</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879460):
<p>OK! Thanks for your opinion, I genuinely value it.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879481):
<p>We are both in the same sort of boat, trying to read books written for computer scientists with in some sense an "amateur" background (with me rather more amateurish than you when it comes to computing) but I really want to appeal to people who know no CS at all.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879699):
<p>Back to the point -- does anyone here know if one can do classical mathematics in UniMath?</p>

#### [ Andrew Ashworth (Apr 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124879899):
<p>I think so. <a href="https://github.com/HoTT/HoTT/issues/299" target="_blank" title="https://github.com/HoTT/HoTT/issues/299">https://github.com/HoTT/HoTT/issues/299</a></p>

#### [ Andrew Ashworth (Apr 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124880270):
<p>speaking of, i linked this a long time ago, but here you can see a comparison of the most popular proof languages</p>

#### [ Andrew Ashworth (Apr 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124880271):
<p><a href="http://www.cs.ru.nl/~freek/100/" target="_blank" title="http://www.cs.ru.nl/~freek/100/">http://www.cs.ru.nl/~freek/100/</a></p>

#### [ Simon Hudon (Apr 10 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124891320):
<blockquote>
<p>yes, the big three textbooks for coq are: <a href="https://softwarefoundations.cis.upenn.edu" target="_blank" title="https://softwarefoundations.cis.upenn.edu">software foundations</a>, <a href="http://adam.chlipala.net/cpdt/" target="_blank" title="http://adam.chlipala.net/cpdt/">certified programming with dependent types</a>, and <a href="https://www.labri.fr/perso/casteran/CoqArt/coqartF.pdf" target="_blank" title="https://www.labri.fr/perso/casteran/CoqArt/coqartF.pdf">coq'art</a>. ssreflect also has a good manual <a href="https://math-comp.github.io/mcb/book.pdf" target="_blank" title="https://math-comp.github.io/mcb/book.pdf">here</a>. notice all but the last is focused towards programmers...</p>
</blockquote>
<p>I think that suggests <span class="user-mention" data-user-id="110031">@Patrick Massot</span> has the right idea: if you want documentation for mathematicians, we need actual mathematicians to do it.</p>

#### [ Patrick Massot (Apr 10 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124891477):
<p>I don't if you count Avigad as mathematician but TPIL comes very close to what we want. You only to unemphasize term mode and put more math examples.</p>

#### [ Simon Hudon (Apr 10 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124891705):
<p>Right. What I meant is that building a theorem prover is something done by programmers so it kind of colors what they'll use the prover for in the documentation.</p>

#### [ Simon Hudon (Apr 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124891869):
<p>That's the curious difference between a prover and an accounting software. In accounting software, you do it for / with accountants / people who want to do accounting. With a prover, I have a feeling you start one when you need a prover that does stuff that the other provers don't do. You're kind of the first user of the prover so you assume the other users will want the prover for the same reason. Not that I built a prover with more than 1.5 users but ...</p>

#### [ Andrew Ashworth (Apr 10 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892093):
<blockquote>
<p>I don't if you count Avigad as mathematician but TPIL comes very close to what we want. You only to unemphasize term mode and put more math examples.</p>
</blockquote>
<p>term mode is not the enemy! i feel like if one wants to get anything done, you'll end up needing to know both modes <br>
personally my favorite code style for math is the isabelle style, as seen <a href="https://github.com/sgouezel/mathlib/blob/d4836822a625677b9f292e26fcafb4870bbf9f91/order/conditionally_complete_lattice.lean" target="_blank" title="https://github.com/sgouezel/mathlib/blob/d4836822a625677b9f292e26fcafb4870bbf9f91/order/conditionally_complete_lattice.lean">https://github.com/sgouezel/mathlib/blob/d4836822a625677b9f292e26fcafb4870bbf9f91/order/conditionally_complete_lattice.lean</a></p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892290):
<p>Term mode is not the enemy. But for a mathematician there are many things which you have to learn in order to work this sort of language, and term mode is somehow one of the more obscure things. Let's give them time to wrestle with how to steer this thing whilst they're proving that the square root of 2 is irrational, or whatever, in tactic mode, before telling them that lambda is no longer supposed to mean a real number.</p>

#### [ Andrew Ashworth (Apr 10 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892502):
<p>if logic and proof (jeremy's other textbook) was fully worked out in lean 3, is that something you'd be looking for?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892633):
<p>That's less Lean and less tactic mode!</p>

#### [ Patrick Massot (Apr 10 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892634):
<p>I didn't write "completely remove term mode" but "unemphasize" (I don't know if this word exists but I hope what I mean is clear)</p>

#### [ Andrew Ashworth (Apr 10 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892687):
<p>ah, true. only 50% of logic and proof is lean</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892690):
<p>I know exactly what I want, and I'm going to write it myself using Jeremy's cool org mode solution for generating books</p>

#### [ Patrick Massot (Apr 10 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892694):
<p>I'd be happy to help in any way</p>

#### [ Andrew Ashworth (Apr 10 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892704):
<p>very awesome, i think everyone here would love to peek at it as you write it</p>

#### [ Andrew Ashworth (Apr 10 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892705):
<p>at least i would, i read all your blog posts, hah</p>

#### [ Simon Hudon (Apr 10 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892755):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think he moved from org-mode to Restructured Text, didn't he?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892773):
<p>In some sense the main question I have for Patrick is how to write a book which has maths like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span></span></span></span> and <code>lean stuff like this</code> all coloured in correctly.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892777):
<p>Simon I was basing my org claim on this</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892778):
<p><a href="https://github.com/leanprover/mkleanbook" target="_blank" title="https://github.com/leanprover/mkleanbook">https://github.com/leanprover/mkleanbook</a></p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892816):
<p>and the fact that the files were called <code>blah.org</code></p>

#### [ Patrick Massot (Apr 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892832):
<p>This is not how TPIL is currently produced</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892838):
<p>You must be right</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892840):
<p>do you know how it's currently done?</p>

#### [ Patrick Massot (Apr 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892848):
<p>Sphinx</p>

#### [ Patrick Massot (Apr 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892854):
<p><a href="https://github.com/leanprover/theorem_proving_in_lean" target="_blank" title="https://github.com/leanprover/theorem_proving_in_lean">https://github.com/leanprover/theorem_proving_in_lean</a></p>

#### [ Patrick Massot (Apr 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892861):
<p>scroll down to README</p>

#### [ Andrew Ashworth (Apr 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892862):
<p>that said, there is nothing wrong with mkleanbook, the issue was other people didn't want to use emacs</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892869):
<p>what about getting things <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi><mi>n</mi><mi>m</mi><mi>a</mi><mi>t</mi><mi>h</mi><mi>s</mi><mi>m</mi><mi>o</mi><mi>d</mi><mi>e</mi></mrow><annotation encoding="application/x-tex">in maths mode</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">i</span><span class="mord mathit">n</span><span class="mord mathit">m</span><span class="mord mathit">a</span><span class="mord mathit">t</span><span class="mord mathit">h</span><span class="mord mathit">s</span><span class="mord mathit">m</span><span class="mord mathit">o</span><span class="mord mathit">d</span><span class="mord mathit">e</span></span></span></span>?</p>

#### [ Kevin Buzzard (Apr 10 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124892913):
<p>(although perhaps not regular sentences, they can stay in non maths mode)</p>

#### [ Simon Hudon (Apr 10 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124894266):
<p>Do you mean that you would format Lean code in math mode? I'd really like to see that</p>

#### [ Kevin Buzzard (Apr 10 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124895411):
<p>I mean I want to write maths and Lean code (at different times)</p>

#### [ Kevin Buzzard (Apr 10 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124895465):
<p>Ideally the maths I write would look as good as LaTeX and the Lean would be coloured in correctly</p>

#### [ Simon Hudon (Apr 10 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124895486):
<p>Ah ok! I think the setup they have for Lean documents should allow that</p>

#### [ Simon Hudon (Apr 10 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124895597):
<p>I'm soon going to give Pandoc a try. I heard good things about it and it looks easier to set up than Sphinx</p>

#### [ Simon Hudon (Apr 10 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124895678):
<p>Ideally, I'd like to get to a point where I don't have to switch between writing and checking Lean and writing and checking documentation.</p>

#### [ Mario Carneiro (Apr 10 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124900412):
<blockquote>
<p>One major weakness (possibly only temporary) is that the model you're supposed to carry around is that a type can be thought of as a topological space<br>
but apparently they can't construct the n-sphere from the axioms<br>
so they add n-spheres as new inductive types<br>
and then they can't prove the theory is consistent<br>
This does not bode well, as far as I can see.</p>
</blockquote>
<p>As far as I am aware, HoTT + all the HITs people care about, including S^n and quotients and things, is known consistent because of the existence of simplicial set models and such. The unknown consistency claim here may be particular to Univalent Foundations, I'm not sure.</p>

#### [ Mario Carneiro (Apr 10 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124900578):
<blockquote>
<p>Is Univalent Foundations = HoTT? I'm not so sure</p>
</blockquote>
<p>I think Univalent Foundations = HoTT + Propositional resizing, which means that everything you can prove is a proposition lives in the lowest universe. This is similar to Lean's <code>Prop</code> universe, but in Lean you can't prove that something lives in <code>Prop</code>, it either is or isn't by virtue of the form of the expression. Regular HoTT does not have this resizing rule, so there are "more propositions" in higher universes, which talk about correspondingly large objects.</p>

#### [ Mario Carneiro (Apr 10 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124900659):
<blockquote>
<p>If I am interested in mathematics, done in classical logic<br>
then what are my options for doing this in type theory?</p>
</blockquote>
<p>I think this is the wrong question. You can do mathematics in just about any system above a certain minimum threshold of complexity, which is somewhere around second order PA. It just gets less convenient as you remove features</p>

#### [ Mario Carneiro (Apr 10 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124900935):
<blockquote>
<p>I believe Isabelle/ZFC is also a thing.</p>
</blockquote>
<p>Pretty much all Isabelle work is done in Isabelle/HOL. Metamath is similar in that it is a general framework which allows you to define DTT, HOL, ZFC, PA or anything else, but 99% of the actual theorem proving work has gone into the ZFC database.</p>
<blockquote>
<p>Apparently proof assistants based on ZFC are hard to use<br>
I think Mario told me this</p>
</blockquote>
<p>I'm not 100% clear on this, because I hear conflicting messages, but this is the usual line:</p>
<ul>
<li>ZFC based stuff is hard to use in proof automation because there isn't much information on what is what, which helps in relevance filtering and eliminating proof steps that are not well typed</li>
<li>Type theory based stuff is hard for proof automation because keeping track of all the types is hard, and all the major tools are built in FOL with one big FOL universe, i.e. ZFC (or smaller FOL systems like first order equational theories, PA, etc.)</li>
</ul>

#### [ Mario Carneiro (Apr 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124901093):
<blockquote>
<p>If you're playing the very long game, it might still be the case Coq &gt; Lean, Ltac2 is coming.</p>
</blockquote>
<p>If you are playing a sufficiently long game, the best bet doesn't exist yet</p>
<blockquote>
<p>dtt without any funny additions has been proven sound</p>
</blockquote>
<p>DTT with inductive types, quotients and proof irrelevance is also sound, courtesy of yours truly</p>

#### [ Mario Carneiro (Apr 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124901174):
<blockquote>
<p>I am still trying to figure out all the finite stuff<br>
but multiset.lean is so long</p>
</blockquote>
<p>You don't need to read multiset.lean that carefully. The easy version is: it's lists up to permutation, with all the list functions lifted to multiset. All the lemmas are exactly what you would expect, given the definitions.</p>

#### [ Mario Carneiro (Apr 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124901284):
<blockquote>
<p>i mean, it's theoretically possible to write a transpiler. but who would do the work?</p>
</blockquote>
<p>I would, if I understood Coq's metatheory as well as I do Lean's. Since they were not nearly so careful with their kernel as Lean has been, I don't know if I will find the acceptable Gallina terms written up anywhere that isn't an approximation or out of date</p>

#### [ Mario Carneiro (Apr 10 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124901543):
<blockquote>
<p>equality in unimath seems more like \equiv in Lean</p>
</blockquote>
<p>This is exactly the right idea. However, there is something you really need to pay attention to which I think you have missed and are using to get a "free lunch" in your conception of HoTT: equality (the type constructor) is <em>not</em> the same as definitional equality. In Lean this isn't that big a deal because of proof irrelevance, but you absolutely cannot hold the view that one thing is as good as an equal thing when doing HoTT. In particular, it will not save you from your "up to equivalence" problems in the other thread, but I will discuss this more there.</p>

#### [ Mario Carneiro (Apr 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124902506):
<blockquote>
<p>I still think that term mode is too hard for mathematicians. You clearly have a programming background. I am guessing that you were happy with lambda notation for functions before you started reading these docs.<br>
I would like to suppress lambda notation for as long as possible.</p>
</blockquote>
<p>I don't think this is a good idea. The idea of a lambda itself, a function giving a result, is quite integral to mathematics and it's a surprise they haven't picked up the notation already (or something isomorphic, like <code>x \in A |-&gt; b(x)</code>).</p>
<p>If you want to write a tactic-centric lean tutorial, I would suggest to begin with a brief overview of the terms of the language, i.e. lambda, application, constants and variables, make sure they understand what a bound variable is, then move on with some statement along the lines "writing these terms directly is cumbersome, so here's a language for quickly constructing terms that is designed more for ease of use". You don't need to mention the Isar-inspired terms like <code>match</code> and <code>have</code> and <code>show</code> until later if you want, but the core type theory should be at least briefly described.</p>

#### [ Scott Morrison (Apr 11 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations%20of%20mathematics/near/124907734):
<p>It is a good point that mathematicians know perfectly well about lambdas, they just write them $x \mapsto f(x)$.</p>


{% endraw %}
