---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/71776Timelineoflean4.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Timeline of lean 4?](https://leanprover-community.github.io/archive/113489newmembers/71776Timelineoflean4.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ HT (Jun 27 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128716259):
<p>Hi, when would lean 4 's repo be public?</p>

#### [ Patrick Massot (Jun 27 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128716334):
<p>I don't think anyone on earth has an answer to that question.</p>

#### [ Patrick Massot (Jun 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128716345):
<p>Leo and Sebastian are working, and they need time and peace.</p>

#### [ Patrick Massot (Jun 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128716360):
<p>We enjoy Lean 3 in the meantime.</p>

#### [ Patrick Massot (Jun 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128716416):
<p>And Sean plays with emojis</p>

#### [ Patrick Massot (Jun 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128716447):
<p>I can see this question wakes up many more people than inverting a partially injective function</p>

#### [ HT (Jun 27 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128716928):
<p>From programmer's aspect, C++ code generator and FFI is a bigger deal. I could see potential.</p>

#### [ Simon Hudon (Jun 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128717060):
<p>In the mean time, how comfortable are you with Lean?</p>

#### [ Sean Leather (Jun 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128717111):
<p>We're hoping that we can to translate all of the work and knowledge that has gone into Lean 3 code into Lean 4 code, when the latter comes out. So, you could start working with Lean 3 now with that in mind. Otherwise, you may have to wait for an indeterminate time.</p>

#### [ Simon Hudon (Jun 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128717168):
<p>I think it's safe to say that Lean 4 will be based on dependent type theory and make a similar use of functions and type classes so those are certainly worth knowing about even if their syntax changes</p>

#### [ HT (Jun 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128717396):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> It's the most clean and flexble one. It has best chance to unify programming and math.</p>

#### [ Simon Hudon (Jun 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128717509):
<p>To be fair, this unification is already happening. Coq has taken us a long way and so has Isabelle. Chances are that Lean will be another stepping stone in that lengthy process</p>

#### [ HT (Jun 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128718000):
<p>Those two looks like lots of math proving steps, it don't make sense to me. Lean and Fstar looks more like functional programming.</p>

#### [ Patrick Massot (Jun 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128718026):
<p>Lean looks like math much more than Coq (simply thanks to unicode use and less esoteric notations)</p>

#### [ Sean Leather (Jun 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128718083):
<p>In Lean, using tactics is, as in Coq, like proving steps in math.</p>

#### [ Reid Barton (Jun 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128718097):
<p>My impression is that people don't really use term mode in Coq, is that right?</p>

#### [ Sean Leather (Jun 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128718175):
<p>I've never seen it in any Coq tutorial.</p>

#### [ Simon Hudon (Jun 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128718179):
<blockquote>
<p>My impression is that people don't really use term mode in Coq, is that right?</p>
</blockquote>
<p>It's also my impression. The syntax of term mode is not geared for writing proofs</p>

#### [ HT (Jun 27 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128718442):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Lean also looks like programming more than Coq at the same time.</p>

#### [ HT (Jun 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128719177):
<p>On the other hand, Coq makes no sense to low level programming. Lean has potential to prevent flaming chips and overflows.</p>

#### [ Simon Hudon (Jun 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128719268):
<p>Why do you say that Coq makes no sense to low level programming?</p>

#### [ Reid Barton (Jun 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128719380):
<blockquote>
<blockquote>
<p>My impression is that people don't really use term mode in Coq, is that right?</p>
</blockquote>
<p>It's also my impression. The syntax of term mode is not geared for writing proofs</p>
</blockquote>
<p>Oh I see, I had a hidden assumption in my mind "for doing math".</p>

#### [ HT (Jun 27 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128719561):
<p>Coq don't generates C which POSIX is defined by, and had a huge irreducible runtime with gc that could fulfill memory.</p>

#### [ Simon Hudon (Jun 27 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128719610):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>  I don't understand what your addition changes</p>

#### [ Simon Hudon (Jun 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128719721):
<p><span class="user-mention" data-user-id="120163">@HT</span>  Coq has most of the major low-level verification frameworks that I know of.  I don't know if they prefer parsing C or generating C but a lot of low-level verification is done with Coq. See Iris, Bedrock and VST</p>

#### [ HT (Jun 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128719984):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> They actually make developers less productive because of extra barriers. At least four languages involved in, EDSL to generate C , C, Coq, OCaml.</p>

#### [ Reid Barton (Jun 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128720069):
<p>I assume people do use term mode for programming (e.g., for program extraction)?</p>

#### [ HT (Jun 27 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128720102):
<p>When bugs wasn't catched by types, debugging must includes huge runtime with gc, edsl, coq, ocaml.</p>

#### [ Simon Hudon (Jun 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128720187):
<p>If I understand you correctly, what your getting at is better tools. It's not about low-level programming. It's about being productive as programmers</p>

#### [ HT (Jun 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128720302):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Yes, Coq costs too much. I'm not sure why it's not about low-level programming, high level programming seldom encounters problems caused by runtime.</p>

#### [ Simon Hudon (Jun 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128720726):
<p>Your initial statement was "[it] doesn't make sense to low level programming". Is that still what you're arguing? If so, I argue that the frameworks I mentioned help understand low level programming.</p>

#### [ Simon Hudon (Jun 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128720823):
<p>Or maybe I should understand your point as being "it is difficult to use in low-level settings because of its awkward tools". In that case, I should agree. I haven't tried the frameworks in that context but it is consistent with my (small) experience with Coq</p>

#### [ HT (Jun 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128721112):
<p>To be more clear, I mean it doesn't make sense for programmers to cost so much barriers to correct code.</p>

#### [ Simon Hudon (Jun 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128721403):
<p>To be honest, that does not clarify your statement for me. It sounds like you're saying that a heavy run-time is one too many hurdles towards obtaining correct code.</p>

#### [ HT (Jun 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128721496):
<p>That's one point. And the other is there's too many concepts compounded in a inconsistent way.</p>

#### [ Simon Hudon (Jun 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128721558):
<p>Do you have an example to illustrate that point?</p>

#### [ HT (Jun 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722051):
<p>I got an example. <a href="https://gitlab.mpi-sws.org/FP/iris-coq/blob/master/theories/program_logic/hoare.v" target="_blank" title="https://gitlab.mpi-sws.org/FP/iris-coq/blob/master/theories/program_logic/hoare.v">https://gitlab.mpi-sws.org/FP/iris-coq/blob/master/theories/program_logic/hoare.v</a></p>

#### [ HT (Jun 27 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722108):
<p>Why do we need hoare logic if everything could be proved in dependent type?</p>

#### [ HT (Jun 27 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722327):
<p>I can not imagine I can convince any low level programmers costs so much time to learn several different theories nested in dependent types and three kinds of syntax, ocaml, coq, edsl, to start programming correct code.</p>

#### [ Simon Hudon (Jun 27 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722390):
<p>Those are separate things. Hoare logic is formulated in dependent types. And dependent types by themselves are not sufficient, you need program semantics and verification rules. Particularly in the case of low-level code, the most effective tool around is separation logic which is formulated as a Hoare logic. The whole thing is still couched on a dependent type theory. The same way you wouldn't use a programming language without libraries, you can't use a logic without a certain number of basic theory</p>

#### [ Simon Hudon (Jun 27 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722454):
<p>If you have something better than separation logic for low-level pointer reasoning, you should publish it. It's going to be worth a lot</p>

#### [ Simon Hudon (Jun 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722855):
<p>As for convincing people, it doesn't have to be all or nothing, there are middle grounds, gateway drugs if you want, where very little effort yields a great benefit. TLA+ for example is tremendous if you want to learn formal specifications and use them in a project. With its model checker, you get a great benefit from any degree of formalization that you care to go through. In some cases, that can be enough. In others,  you want a full functional proof of correctness. Then you have to invest time. Lean is not going to be a magic bullet any more than Coq is. With a wider community in the industry and in academia using formal proof, with can decrease the burden of writing formal proofs for sure but it's an ongoing process. Most importantly, it happens with people trying the tools, finding them lacking and adding their two cents</p>

#### [ Patrick Massot (Jun 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722868):
<p>I have good news for the Lean 4 timeline. It seems Sebastian will not waste time watching his country playing in the world cup.</p>

#### [ HT (Jun 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722890):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I may be wrong, I though linear type reduce the use of pointers like rust does. We just need to seperate different kind of resources in types.</p>

#### [ Patrick Massot (Jun 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128722996):
<p>Brazil is still in though.</p>

#### [ Simon Hudon (Jun 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128723118):
<p>That's true and linear types are one of the tools that I'm mentioning. But the operating word here is "reduce". Reducing the use of separation logic is a great achievement. But with Iris project, we see that as long as you use unsafe code in libraries, you will need to use a least a little bit of separation logic to verify them.</p>

#### [ Sebastian Ullrich (Jun 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128723182):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Today's events did not change anything in that regard :P</p>

#### [ HT (Jun 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128724356):
<p>I hope my point is clear, to write code fast and correct. Lean looks so handy to make most of the logic proved without much barriers. If I still needs something not covered by types, I'd write tests rather than involving additional layers of theories.</p>

#### [ Simon Hudon (Jun 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128724490):
<p>I agree in parts with your point. Lean and its tools are looking more and more like an IDE. You can use them to write programs without proofs, you can import various packages with varying levels of verification. You can be deterred by adding new logics to your system but making them available means that, when you decide that they're worth it, you can just reach for them.</p>

#### [ HT (Jun 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128724899):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Yes, that's what I expect, a programming language.</p>

#### [ Simon Hudon (Jun 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128724971):
<p>Glad we found a common ground. I think compared to Idris (which might also fit your criteria), Lean is a better prover</p>

#### [ HT (Jun 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128725149):
<p>I also think Lean is better in a consistent way. I feel something wrong with Idris but I'm not sure what it is.</p>

#### [ HT (Jun 27 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128725744):
<p>It makes me feel that Idris is a variant of Haskell injected with extra type ability inconsistently which actually causes bugs rather than an actual type theory like Lean.</p>

#### [ Sean Leather (Jun 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128759773):
<p>I previously <a href="#narrow/stream/113489-new-members/subject/Timeline.20of.20lean.204.3F/near/128717111" title="#narrow/stream/113489-new-members/subject/Timeline.20of.20lean.204.3F/near/128717111">wrote</a>:</p>
<blockquote>
<p>We're hoping that we can to translate all of the work and knowledge that has gone into Lean 3 code into Lean 4 code, when the latter comes out. So, you could start working with Lean 3 now with that in mind. Otherwise, you may have to wait for an indeterminate time.</p>
</blockquote>
<p>Simon <a href="#narrow/stream/113489-new-members/subject/Timeline.20of.20lean.204.3F/near/128717168" title="#narrow/stream/113489-new-members/subject/Timeline.20of.20lean.204.3F/near/128717168">responded</a>:</p>
<blockquote>
<p>I think it's safe to say that Lean 4 will be based on dependent type theory and make a similar use of functions and type classes so those are certainly worth knowing about even if their syntax changes</p>
</blockquote>
<p>I agree with Simon, but I think there's a big difference between translating knowledge of basic concepts into an implementation (of which there are many: Coq, Agda, and Idris to name some popular ones) and translating an existing codebase and deep knowledge of one language into another.</p>
<p>The <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/doc/lean4.md" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/doc/lean4.md">only public document</a> reflecting the Lean 4 plan (at least for when it was written) states:</p>
<blockquote>
<p>Users should not expect Lean 4 will be backward compatible with Lean 3.</p>
</blockquote>
<p>This is why I conservatively referred to “hope.” I think there is some risk of working in Lean 3 now if you wish to move to Lean 4 later. But I also think there is some confidence that Lean 4 will not be as radically different from Lean 3 as, say, Coq is from any version of Lean.</p>

#### [ Mario Carneiro (Jun 28 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Timeline%20of%20lean%204%3F/near/128759878):
<p>I think considerably more than Simon's list of concepts will carry over to lean 4. I know that "the syntax will stay more or less the same" modulo some easy regex fixes, but the elaborator may also change (semi by accident, because it will be re-implemented in lean), and this may cause more subtle breakage</p>


{% endraw %}
