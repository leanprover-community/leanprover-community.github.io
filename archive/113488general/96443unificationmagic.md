---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96443unificationmagic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [unification magic](https://leanprover-community.github.io/archive/113488general/96443unificationmagic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 23 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543006):
<p>I wrote a <code>noncomputable definition</code> which was an instance of a structure. The structure had 6 fields, and I was filling in the last one, which was a proof. The other 5 fields had already used a bunch of constructions. I was filling in this 6th field and I started by getting the syntax right and writing <code>_</code> for several things, including a function <code>_ : R -&gt; S</code> between two rings. Once I'd got the syntax correct and complete, Lean evaluated the term and to my surprise found no problems with it.  In particular I think it must have figured out which function I meant.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543009):
<p>Now there's only one sensible function <code>R -&gt; S</code>, and this function has almost certainly been mentioned earlier in the definition</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543015):
<p>however I could not really imagine how type class unification could solve this.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543018):
<p>Is this sort of thing sometimes possible?</p>

#### [ Simon Hudon (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543058):
<p>Is there a lemma in your structure about the function?</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543060):
<p>could well be</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543062):
<p>the function is used all over the place</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543065):
<p>It's just got rather a long name</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543066):
<p>so I couldn't be bothered to type it</p>

#### [ Simon Hudon (Apr 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543067):
<p>That's probably how it's inferred</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543074):
<p>It's a term, not a type.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543075):
<p>Perhaps that's what I was surprised about</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543122):
<p>actually looking at it now I can begin to see how this amazing thing is possible</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543124):
<p>ultimately this function f appears in the statement of the thing I'm trying to prove</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543133):
<p>I'm constructing a proof of <code>f x = blah</code></p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543134):
<p>and I skipped the definition of f</p>

#### [ Simon Hudon (Apr 23 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543136):
<p>Since we have dependent types, the line between types and terms is blurred. Similarly, if you have <code>f : Π n : ℕ, fin n → ℕ</code> and <code>x : fin (m+n)</code>, you can write <code>f _ x</code> and trust Lean to infer <code>m+n</code></p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543180):
<p>I guess what I am saying is that I thought I was getting a pretty good instinct of what unification could do for me</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543181):
<p>but it's even better than I thought</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543183):
<p>Does Coq not have term mode?</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543189):
<p>I used to be terrified of term mode</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543191):
<p>but now I use it a lot</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543196):
<p>all this was happening in term mode</p>

#### [ Simon Hudon (Apr 23 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543244):
<p>Ah ok! I thought you needed clarification.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543246):
<p>Writing the message myself was enough to get me thinking in the right way</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543251):
<p>That's the problem with these chat rooms</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543253):
<p>Sometimes I have a question about a maths paper and I start writing an email to the author and by the time I've finished the email, I've answered the question</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543254):
<p>but then I never send the email</p>

#### [ Simon Hudon (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543255):
<p>In a way, Coq has a term mode because terms can be used as proofs but I believe it doesn't have the <code>have</code> / <code>show</code> / <code>suffices</code> notation so it's not made for writing proofs.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543256):
<p>here I started writing the question and it was already mostly sent before I realised what had happened</p>

#### [ Simon Hudon (Apr 23 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543308):
<p>Haha! Yeah, I know the feeling. A while back, a supervisor told me that I should try asking my questions to a cactus or a rubber duck because I didn't actually need him there</p>

#### [ Simon Hudon (Apr 23 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543316):
<p>Maybe you can signal this is happening by tagging your own message with <span class="emoji emoji-1f4a1" title="light bulb">:light_bulb:</span></p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543357):
<p>nice idea :-)</p>

#### [ Simon Hudon (Apr 23 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543380):
<p>I wouldn't be surprised if people jump in anyway and ask you to explain your newfound insight</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543381):
<p>Thanks for listening :-)</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543428):
<p>I agree about the rubber duck suggestion. I feel silly talking to inanimate objects but as I already said, the technique I've used which really works for me is to start writing an email to someone who will know the answer, and really explain all the background and details about what you're confused about.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543434):
<p>And a lot of the time, the email ends up never sent and becomes an answer to your own question</p>

#### [ Simon Hudon (Apr 23 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543509):
<p>I feel silly talking to inanimate things too ... the worse is when they talk back!</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543554):
<p>I am pretty excited for lean 4 and playing around with {! !}</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543557):
<p>i think term mode has been a little neglected, which is a shame since writing programs with tactics is a bit scary</p>

#### [ Simon Hudon (Apr 23 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543561):
<p>But if someone walk into the room, it's pretty embarrassing too. Then I have to pretend that there's a song about inductive proofs of liveness.</p>

#### [ Simon Hudon (Apr 23 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543615):
<blockquote>
<p>i think term mode has been a little neglected, which is a shame since writing programs with tactics is a bit scary</p>
</blockquote>
<p>Why is it scary?</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543631):
<p>because i have no idea how certain tactics get compiled down to certain terms, or how those terms might be evaluated in the vm</p>

#### [ Simon Hudon (Apr 23 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543673):
<p>That's true. What about mixing terms and tactics?</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543679):
<p>sure. tactics are great for Props, which get erased</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543736):
<p>i mean, i don't doubt you can do crazy things with tactic automation, but it's another layer of abstraction on top of a bunch of stuff I don't understand already :)</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543743):
<p>i have a slightly ill feeling when I have to read other people's template and macro hackery</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543744):
<p>already</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543787):
<p>i'm hoping programming in lean gets updated at some point as well... i've been holding off on writing metaprograms in lean since there's little documentation</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543788):
<p>and I don't have the interest to hack away at it without some hand-holding</p>

#### [ Simon Hudon (Apr 23 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543842):
<p>Regardless of meta programming skills, it's true that tactics can easily obscure the operational aspect of programs</p>

#### [ Simon Hudon (Apr 23 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543885):
<p>If we had an execution model and performance specifications, maybe that wouldn't be so bad. What do you think?</p>

#### [ Moses Schönfinkel (Apr 23 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543891):
<p>I think he's talking about the entire pexpr stuff and magical functions to convert from and to varius opaque intermediate forms :)? At least that's what is fairly annoying for me and Ltac simply does better.</p>

#### [ Simon Hudon (Apr 23 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543935):
<p>Because in Ltac you don't have to perform conversions? It's funny because I find Ltac much more obscure at the operational level. I find I'm never sure what my tactics will actually do</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543941):
<p>you're assuming i'm even aware of these magical functions to intermediate forms</p>

#### [ Andrew Ashworth (Apr 23 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125543943):
<p>i cracked open PIL, saw it had only a few chapters finished, and then walked away back to term mode</p>

#### [ Kevin Buzzard (Apr 23 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification%20magic/near/125544405):
<p>My _impression_ is that the missing chapters in PIL are mostly stuff which is documented in TPIL</p>


{% endraw %}
