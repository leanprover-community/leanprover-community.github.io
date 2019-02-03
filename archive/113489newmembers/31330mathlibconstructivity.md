---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31330mathlibconstructivity.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [mathlib & constructivity](https://leanprover-community.github.io/archive/113489newmembers/31330mathlibconstructivity.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Olson (Sep 25 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134574550):
<p>is there a standard library structure for isomorphisms, like this type in Idris? <a href="https://github.com/idris-lang/Idris-dev/blob/bae730a7ffaeae09a835a35bac132c141f3b50b3/libs/base/Control/Isomorphism.idr#L10-L16" target="_blank" title="https://github.com/idris-lang/Idris-dev/blob/bae730a7ffaeae09a835a35bac132c141f3b50b3/libs/base/Control/Isomorphism.idr#L10-L16">https://github.com/idris-lang/Idris-dev/blob/bae730a7ffaeae09a835a35bac132c141f3b50b3/libs/base/Control/Isomorphism.idr#L10-L16</a></p>
<p>i'm not sure what name to search for</p>

#### [ Simon Hudon (Sep 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134574597):
<p>In mathlib, you may want <code>data.equiv.basic</code></p>

#### [ Simon Hudon (Sep 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134574603):
<p><a href="https://github.com/leanprover/mathlib/blob/master/data/equiv/basic.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/equiv/basic.lean">https://github.com/leanprover/mathlib/blob/master/data/equiv/basic.lean</a></p>

#### [ Scott Olson (Sep 25 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134575168):
<p>thanks, that looks like what i want</p>
<p>that brings me to another question, though... should i be using mathlib, in general? is it basically just expected that most people will be using it?</p>

#### [ Simon Hudon (Sep 25 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134575317):
<p>Most people use mathlib because it's the largest repository of definitions and theorems in Lean and it keeps growing. Most importantly it has a lot of useful stuff</p>

#### [ Mario Carneiro (Sep 25 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134575318):
<p>That is certainly the intent... it is like the standard library of most programming languages</p>

#### [ Scott Olson (Sep 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578662):
<p>is mathlib generally constructive or classical? or at least, does it clearly delimit which things depend on classical axioms? curious if i'll have to "wary" and check with <code>#print axioms</code></p>

#### [ Simon Hudon (Sep 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578810):
<p>You'll have to be wary. An effort is made to label classical theorems but people still use them pretty loosely</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578812):
<p>mathlib is mostly classical. In particular, we only worry about constructivity in so far as it avoids the <code>noncomputable</code> marking. In any props or theorems we use AC freely</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578903):
<p>There really isn't any point in being "wary" with <code>#print axioms</code>, because all you will achieve by doing that is get yourself in a tizzy about the many unnecessary uses of AC. Suffice it to say it is used in many difficult to avoid places in the foundation, some of which are in lean core and so are not even accessible to mathlib</p>

#### [ Scott Olson (Sep 25 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578908):
<p>is there a discussion somewhere on the pros and cons of being classical for something like mathlib or just Props in general?</p>

#### [ Scott Olson (Sep 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578921):
<p>the mathlib docs i've found so far just don't mention it</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578929):
<p>We've had the discussion off and on for a while. Lean 2 made a concerted effort to be both constructive and classical</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134578977):
<p>At the beginning I held out hope that we could avoid AC when unnecessary, but at this point it's clear this isn't going to happen</p>

#### [ Simon Hudon (Sep 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579016):
<p>I wonder if that's part of why mathlib was able to move quickly too</p>

#### [ Scott Olson (Sep 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579079):
<p>i don't have much understanding of the implications of using such axioms in a system like Lean. i understand <code>noncomputable</code> prevents even bytecode, but any axioms at all prevent the term from evaluating to a normal form, and i'm curious if that can cause problems in practice</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579097):
<p>We don't evaluate proofs at all in practice</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579099):
<p>it doesn't matter if they are classical or not because they aren't programs</p>

#### [ Scott Olson (Sep 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579154):
<p>that was my thinking for Prop, but i haven't been able to find much documentation talking about this point</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579155):
<p>The only mechanism we have for evaluating proofs is <code>#reduce</code> and it falls over on all but the most trivial examples</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579169):
<p>I guess there isn't much docs on this</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579187):
<p>The VM evaluates anything that is not a Prop and is not <code>noncomputable</code></p>

#### [ Simon Hudon (Sep 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579193):
<p>When computation is involved, you really need to look at defs that are in <code>Type 0</code> and over. Then an effort is often made to be efficient</p>

#### [ Scott Olson (Sep 25 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579239):
<p>that makes sense, thanks for all the responses</p>

#### [ Simon Hudon (Sep 25 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579246):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Scott Olson (Sep 25 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579260):
<p>i realized while talking to a friend just now that an interesting argument in favor of using fewer axioms is that it makes the proof potentially more "portable" to different formalisms, but that's somewhat aspirational and lacking it doesn't block anything in mathlib in the meantime</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579308):
<p>Unfortunately, the axioms that really prevent portability of lean proofs aren't turn-off-able</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579319):
<p>Most systems have some equivalent of the axiom of choice, but few have inductive types and a hierarchy of universes</p>

#### [ Kevin Buzzard (Sep 25 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579850):
<blockquote>
<p>i realized while talking to a friend just now that an interesting argument in favor of using fewer axioms is that it makes the proof potentially more "portable" to different formalisms, but that's somewhat aspirational and lacking it doesn't block anything in mathlib in the meantime</p>
</blockquote>
<p>I'm a pure mathematician (as are several other people here) and one of the things that attracted me to Lean is precisely the attitude that "we will do maths like regular pure mathematicians do" (i.e. assume things like the axiom of choice, which in my circles is regarded as "just another axiom, with no particular reason to fuss about it".)</p>

#### [ Sean Leather (Sep 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134579993):
<blockquote>
<p>I'm a pure mathematician (as are several other people here) and one of the things that attracted me to Lean is precisely the attitude that "we will do maths like regular pure mathematicians do" (i.e. assume things like the axiom of choice, which in my circles is regarded as "just another axiom, with no particular reason to fuss about it".)</p>
</blockquote>
<p>On the other hand, some of the things that attracted me to Lean included the ability to do constructive mathematics, the nice syntax, a fast theorem prover, and a comprehensive library. <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Scott Olson (Sep 25 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580185):
<p>i figured some of what i said might have given away my friend's and my bias towards constructive type theories :P</p>
<p>i can see why Lean attracted pure mathematicians who might have otherwise used Coq or similar, though. the experience out of the box with Lean in VSCode is the best i've seen from any theorem prover</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580336):
<p>I am also attracted to constructive mathematics generally, but the pure mathematicians have worn me down. :) I realize now that lean is not remotely geared towards limiting its axiom strength, and if you want a system for playing with axioms you should look elsewhere. "Having few axioms" only means having few interesting subsystems, and none of the available subsystems are recognizable to traditional mathematicians except possibly intuitionistic type theory</p>

#### [ Simon Hudon (Sep 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580385):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> how inconvenient is it for you that mathlib makes such liberal use of classical axioms?</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580400):
<p>Instead, it seems much more likely that lean will be able to support doing logic at the meta level, which is something that few systems can currently do well. This approach is much more flexible, of course, with regards to its axioms and with the permissible methods of proof</p>

#### [ Sean Leather (Sep 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580402):
<p>I haven't had any issues so far. I'm not even sure where I would run into any.</p>

#### [ Scott Olson (Sep 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580417):
<p>i figure i'll just adjust my expectations of what exactly i will play with in lean, but it will still be suitable for a lot of the stuff i want to experiment with</p>

#### [ Sean Leather (Sep 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580423):
<p>The only thing is this output:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">quot</span><span class="bp">.</span><span class="n">sound</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">r</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">r</span> <span class="n">b</span>
<span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">},</span> <span class="n">nonempty</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span>
<span class="n">propext</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">},</span> <span class="o">(</span><span class="n">a</span> <span class="bp">↔</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span>
</pre></div>

#### [ Simon Hudon (Sep 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580424):
<p>Is your requirement that functions be computable or actually to avoid the axioms?</p>

#### [ Sean Leather (Sep 25 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580482):
<p>Computable, I suppose. I don't do anything actively to avoid axioms, but I don't think I use anything that does use the axiom of choice.</p>

#### [ Scott Olson (Sep 25 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580506):
<p><code>#print axioms &lt;name&gt;</code> will list the axioms used (transitively) for the given thing</p>

#### [ Scott Olson (Sep 25 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580515):
<p>but as we discussed, this shouldn't be a problem in the bodies of proofs that will never need to be evaluated or examined by other proofs</p>

#### [ Sean Leather (Sep 25 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580569):
<blockquote>
<p><code>#print axioms &lt;name&gt;</code> will list the axioms used (transitively) for the given thing</p>
</blockquote>
<p>When I create an empty file, <code>#print axioms</code> shows what I wrote above. <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Scott Olson (Sep 25 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580583):
<p>yeah, <code>#print axioms</code> just prints the axioms that are currently in scope</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580592):
<p>Can anyone come up with a reasonable (not completely contrived) example of a computable function that uses AC/LEM in its definition?</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580884):
<p>I will amend "not completely contrived" to not eliminable, in the sense that there isn't a way to write the same function without the axiom, or at least it's not easy to do so</p>

#### [ Kevin Buzzard (Sep 25 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580946):
<p>on nat?</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580963):
<p>sure, I doubt it makes a difference but <code>nat -&gt; nat</code> is a fine target</p>

#### [ Kevin Buzzard (Sep 25 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134580976):
<p>I'm sure you're right but I'm such a noob at this sort of thing. A year ago I wouldn't even have been able to formalise the question rigorously.</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581031):
<p>To give a hint on why it's even possible: <code>nat.find</code> will calculate the smallest value satisfying a predicate, given only a proof that there is such a value (in Prop). This proof can rely on any axioms, and the function will still be computable</p>

#### [ Kevin Buzzard (Sep 25 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581033):
<p>What about f(n)=1 if Fermat's Last Theorem is true and 0 otherwise? It's completely contrived but I'm trying to get the hang of the question. All known proofs of FLT use AC.</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581117):
<p>That won't work because <code>f</code> is just the constant function <code>1</code>, it doesn't need any axioms for its definition</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581166):
<p>But I think you are on the right track. Can you think of any forall exists theorem on nat that relies on AC?</p>

#### [ Simon Hudon (Sep 25 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581211):
<p>I don't know how to formalize that statement but it seems like a computable function like you described cannot be constructed</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581378):
<p>Here is an example that relies on the input being in a nonoptimal form: if the input is a function <code>f : nat -&gt; nat</code> which is not the constant zero function, then you can computably find a nonzero <code>nat</code> in the range of <code>f</code></p>

#### [ Simon Hudon (Sep 25 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581503):
<p>That's true. I stand corrected</p>

#### [ Kevin Buzzard (Sep 25 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581579):
<blockquote>
<p>What about f(n)=1 if Fermat's Last Theorem is true and 0 otherwise? It's completely contrived but I'm trying to get the hang of the question. All known proofs of FLT use AC.</p>
</blockquote>
<p>So by "computable" you mean "externally provable to be equal to a certain given fixed computable function", rather than "provable in Lean with/without AC to be equal to a certain given fixed computable function"</p>

#### [ Kevin Buzzard (Sep 25 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581594):
<p>What about f(n)=1 if RH is true and 0 otherwise? Don't I need LEM to define this?</p>

#### [ Kevin Buzzard (Sep 25 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581599):
<p>I'm still struggling to move away from the "contrived" part, as you can see ;-)</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581758):
<p>If you pick something which is definitely not decidable, or not known to be decidable like RH, then the function won't be computable either. By "computable" I mean "passes lean's <code>noncomputable</code> check"; you can't write <code>def f := if RH then 1 else 0</code> because <code>RH</code> is not decidable</p>

#### [ Scott Olson (Sep 25 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581831):
<p>yeah, that would specifically require the classical instance for <code>decidable</code> that uses LEM internally, which is <code>noncomputable</code>, which forces <code>f</code> to be <code>noncomputable</code></p>

#### [ Kevin Buzzard (Sep 25 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581840):
<p>Here is something much less contrived but I am much less clear about whether it fits into the scope of this question. Let's say a pure mathematician proves that for every g&gt;=2 there is a computable upper bound <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi><mo>(</mo><mi>g</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">B(g)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">)</span></span></span></span> for the number of rational points on a smooth projective curve of genus g over the rationals, and their proof uses a bunch of algebraic geometry and AC / LEM everywhere. I suspect I could find arithmetic geometers who were prepared to conjecture that this mathematical statement was true. If this result got proved, and it turned out that a deep theorem implied that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi><mo>(</mo><mi>g</mi><mo>)</mo><mo>=</mo><mn>1</mn><mn>0</mn><mn>0</mn><mn>0</mn><mn>0</mn><mo>∗</mo><mi>g</mi></mrow><annotation encoding="application/x-tex">B(g)=10000*g</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathrm">1</span><span class="mord mathrm">0</span><span class="mord mathrm">0</span><span class="mord mathrm">0</span><span class="mord mathrm">0</span><span class="mbin">∗</span><span class="mord mathit" style="margin-right:0.03588em;">g</span></span></span></span>, this would <em>not</em> be an example, right? :-/</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581848):
<p>You can write <code>def f := if FLT then 1 else 0</code> only if you have already provided a computable proof of <code>decidable FLT</code>, which will involve a proof of FLT. This falls afoul of the second restriction because then you could just replace the definition of <code>f</code> with <code>1</code></p>

#### [ Mario Carneiro (Sep 25 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581943):
<p>You are right, this is an interesting situation. If we know a bound on the function then we can skip the clever maths and just use the bound</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134581957):
<p>Somehow it has to be an existence theorem with no bound</p>

#### [ Edward Ayers (Sep 25 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582212):
<p>How about <code>f(n)</code> is 1 if the nth turing machine halts and 0 otherwise? If I'm not mistaken the proof that <code>f</code> is total requires LEM.</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582251):
<p>I have been thinking about examples like that, but again it needs to be computable</p>

#### [ Edward Ayers (Sep 25 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582254):
<p>But that might be because I've never seen a constructive proof of halting problem</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582319):
<p>To define that function you have to know whether the nth turing machine halts</p>

#### [ Edward Ayers (Sep 25 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582433):
<p>Ah in that case I think that it's impossible.</p>

#### [ Edward Ayers (Sep 25 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582569):
<p>As in you can always rewrite the function to not use AC</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582624):
<p>Here's another way to put it: Find computable predicates <code>p(n), q(m,n)</code> such that if <code>p(n)</code> is true then there exists an <code>m</code> such that <code>q(m,n)</code>, but there is no computable upper bound on the least satisfying instance</p>

#### [ Scott Olson (Sep 25 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582743):
<p>so with <code>nat.find</code> we could find the least <code>nat</code> satisfying some predicate while only proving this search will actually terminate with, for example, a proof by contradiction (the kind that requires classical double negation elimination)?</p>

#### [ Edward Ayers (Sep 25 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582749):
<p>I can just run the <code>q</code> machine on each value of <code>m = 0,1,2,...</code> in turn. Since there exists an <code>m</code> where <code>q(m,n)</code> works, that program will halt. Right?</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582818):
<p>yes, that's the idea</p>

#### [ Edward Ayers (Sep 25 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582819):
<p>So it's impossible (to find such computable predicates)</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582821):
<p>that's the computable function</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134582980):
<p>hm, you may be right. The very constraint that makes it lean-computable will also produce a computable upper bound, namely this function</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583041):
<p>but I think maybe "computable upper bound" isn't what I want either; it needs to be an upper bound that you can't prove using lean without AC</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583046):
<p>you can't use this function as a proof because it requires a proof that it will halt to run</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583092):
<p>If we use something weaker than DTT, it should be possible to use some Ackermann-like function here</p>

#### [ Edward Ayers (Sep 25 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583167):
<p>Ok I think I see what you mean now. You want a pair <code>p(n), q(m,n)</code> where the existence of  a satisfying <code>m</code>is proved using AC or LEM.</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583218):
<p>exactly</p>

#### [ Johan Commelin (Sep 25 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583321):
<p>Can you prove that such a function exists using AC?</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583382):
<p>You can use whatever methods you like to prove the existence of such p and q, but they have to be computable functions</p>

#### [ Johan Commelin (Sep 25 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583448):
<p>Ok, I should have put more emphasis on <em>you</em> in my last post (-;</p>

#### [ Johan Commelin (Sep 25 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583453):
<p>I have no clue at all about all this computability stuff.</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583461):
<p>I don't have a solution to this puzzle</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583474):
<p>but I believe it is possible</p>

#### [ Edward Ayers (Sep 25 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583532):
<p>I am still not satisfied that the question is well posed. If I found a <code>p</code> and <code>q</code> with that property. I could take the AC proof, throw it away and replace it with a machine that just tries all <code>m</code>. Eventually it would find the <code>m</code> (which I know but Lean doesn't) and Lean would use that. But then I guess my new program would have to run in unsafe mode.</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583545):
<p>For a fixed <code>n</code> you can do that, but I don't think you can do that for all <code>n</code></p>

#### [ Mario Carneiro (Sep 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583553):
<p>i.e. if <code>p(5)</code> is true and it turns out that <code>q(100,5)</code> is the satisfying instance, then you can use an upper bound of 100 in the construction</p>

#### [ Johan Commelin (Sep 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583554):
<p>Mario, do you want a proof that can only prove the upper bound under the assumption of LEM/AC?</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583555):
<p>right</p>

#### [ Johan Commelin (Sep 25 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583557):
<p>Or is it enough that we know no such proof.</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583599):
<p>Even that would be nice</p>

#### [ Mario Carneiro (Sep 25 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583615):
<p>I'm worried that since no axioms lean has the same consistency strength as lean + AC, it will not be able to prove any new turing machines halt</p>

#### [ Johan Commelin (Sep 25 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583617):
<p>So, there are only finitely many abelian varieties of dimension <code>g</code> over <code>rat</code> with good reduction outside <code>{favourite finite list of primes}</code>.</p>

#### [ Johan Commelin (Sep 25 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583631):
<p>I don't think we know any upper bounds on this. The proof is a celebrated theorem of Faltings and uses classical maths all over the place.</p>

#### [ Johan Commelin (Sep 25 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583668):
<p>If your favourite finite list of primes is not empty, then this function is extremely hard to compute.</p>

#### [ Johan Commelin (Sep 25 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583691):
<p>(Otherwise it is <code>if g = 0 then 1 else 0</code>.)</p>

#### [ Johan Commelin (Sep 25 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583717):
<p>Does this mean that <code>f g = card (abelian varieties of dim g with good reduction outside blah)</code> is not computable?</p>

#### [ Johan Commelin (Sep 25 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583767):
<p>Hmmm.... I'm too much of a newbie when it comes to such questions.</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583893):
<p>hm, this theorem has AEA quantifier complexity, which is a bit hard to use</p>

#### [ Johan Commelin (Sep 25 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583936):
<p>AEA?</p>

#### [ Johan Commelin (Sep 25 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583941):
<p><code>\forall \exists \forall</code>?</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583954):
<p>"for all g, there exists an n such that all variety things don't have good reduction above n"</p>

#### [ Johan Commelin (Sep 25 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583971):
<p>No, I don't think that's what it says.</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134583978):
<p>I assume there is a way to enumerate abelian varieties?</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584022):
<p>and the theorem says this enumeration runs dry after a certain point</p>

#### [ Johan Commelin (Sep 25 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584026):
<p>For all <code>P : finset primes</code> and for all <code>g</code> there exists <code>n</code> such that <code>card { abvar of dim g and good reduction outside P }</code> is less than <code>n</code>.</p>

#### [ Johan Commelin (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584031):
<p>Well, an abelian variety is defined by a finite number of polynomials</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584040):
<p>right, so we enumerate all such things</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584042):
<p>and only a finite number of them will have good reduction</p>

#### [ Johan Commelin (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584046):
<p>Right (the polys are over Q), so we could do that.</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584054):
<p>so there is an upper bound on the last one with good reduction</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584057):
<p>thus AEA</p>

#### [ Johan Commelin (Sep 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584061):
<p>Right, but testing the good reduction has to happen at all primes outside <code>P</code></p>

#### [ Johan Commelin (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584107):
<p>So you can't enumerate that.</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584120):
<p>oh, I see</p>

#### [ Johan Commelin (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584123):
<p>But I guess you can compute some discriminant in terms of the polynomials</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584125):
<p>the property of having good reduction depends on all p?</p>

#### [ Johan Commelin (Sep 25 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584132):
<p>and then bad reduction at <code>p</code> implies that <code>p</code> divides the discriminant.</p>

#### [ Johan Commelin (Sep 25 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584139):
<p>This works for elliptic curves (the case <code>g = 1</code>)</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584145):
<p>then it is AEAE</p>

#### [ Johan Commelin (Sep 25 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584146):
<p>Lol</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584154):
<p>for all g/P, there exists n, such that for all abvars above n, there is a p such that the var has bad reduction at p</p>

#### [ Johan Commelin (Sep 25 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584195):
<p>No, it isn't about abvars above <code>n</code>, I think.</p>

#### [ Johan Commelin (Sep 25 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584196):
<p>At least I can't parse that.</p>

#### [ Johan Commelin (Sep 25 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584200):
<p>Ooh, wait, you enumerated them</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584204):
<p>that is to exclude the finite number of things with good reduction</p>

#### [ Johan Commelin (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584212):
<p>Hmmm.... but we still need a decision procedure to determine if a bunch of polynomials defines an AV</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584213):
<p>that's surely decidable</p>

#### [ Johan Commelin (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584220):
<p>Ok, if you say so... I have no idea how to do that...</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584232):
<p>I have no idea what an AV is, so there</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584277):
<p>but it surely can't be more than AE complexity</p>

#### [ Johan Commelin (Sep 25 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584296):
<p>It means that there exists a group structure on the solution set defined by the polynomials, and the solution set must be compact (in the algebro-geometric sense of compact)</p>

#### [ Johan Commelin (Sep 25 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584330):
<p>Both seem hard to check at first sight.</p>

#### [ Edward Ayers (Sep 25 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584389):
<blockquote>
<p>For a fixed <code>n</code> you can do that, but I don't think you can do that for all <code>n</code></p>
</blockquote>
<p>Is this argument on the right lines?<br>
If <code>p</code> and <code>q</code> are computable and we know that  for all <code>n</code>, if <code>p(n)</code> then there exists a <code>m</code> such that <code>q(m,n)</code>. Then there exists a computable function <code>n -&gt; m</code> using AC. So I can find the code which runs that function, and put that in Lean. So <code>n</code> doesn't have to be fixed.</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584411):
<p>but the code that runs that function uses AC</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584419):
<p>oh you mean the code of a computable function</p>

#### [ Edward Ayers (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584420):
<p>Right but I can find the code outside Lean and just put the code in</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584427):
<p>but then you need to know it codes a (total) computable function</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584429):
<p>and the proof of that uses AC</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584479):
<p>lean won't just let you run whatever function you like</p>

#### [ Edward Ayers (Sep 25 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584498):
<p>I can run the n-&gt;m in unsafe mode because it's not part of the proof. I just need to get the <code>m</code></p>

#### [ Mario Carneiro (Sep 25 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584554):
<p>the idea with this reduction is to build a computable function in no axioms lean, right? You can't run in unsafe mode since then you don't have a well defined term</p>

#### [ Mario Carneiro (Sep 25 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134584582):
<p>i.e. the <code>m</code> that you pick depends on <code>n</code>, so there is no closed term you can give for the function without unsafe lean stepping in to provide the <code>m</code></p>

#### [ Jared Corduan (Sep 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618450):
<p>how about this:<br>
let <code>A(n)</code> be some computable predicate that requires either <code>AC</code> or <code>LEM</code> to show that either <code>{n | A(n)}</code> or <code>{n | ~A(n)}</code>is infinite.  (in other words, <code>A</code> witnesses the nonconstructive nature of the infinite pigeon hole principle).</p>
<p>then let <code>q1(m, n)</code> be the statement that there is an <code>n &lt; x &lt; m</code> such that <code>A(x)</code> holds. and similarly define <code>q2(m, n)</code> with <code>~A(x)</code>.  both of these are computable since <code>A</code> is computable.  since either <code>{n | A(n)}</code> or <code>{n | ~A(n)}</code>is infinite, then for at least one of <code>q1</code> or <code>q2</code>we can show the existence of such an <code>m</code> for any given <code>n</code>.  but we need <code>AC</code> or <code>LEM</code> for the existence of the <code>m</code>s.</p>

#### [ Kenny Lau (Sep 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618503):
<p>is there a tl;dr for this thread?</p>

#### [ Patrick Massot (Sep 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618569):
<p>Do you really want me to write it?</p>

#### [ Kenny Lau (Sep 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618618):
<p>well this thread is way too long, a tl;dr would be good, I don't see why not</p>

#### [ Patrick Massot (Sep 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618657):
<p>Ok, let me try: constructivity questions are pointless.</p>

#### [ Kenny Lau (Sep 25 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618804):
<p>I don't think that's a very faithful summary, nor is it contributing to the discussion at hand</p>

#### [ Patrick Massot (Sep 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618832):
<p>I'm sorry, but you explicitly asked for it!</p>

#### [ Patrick Massot (Sep 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618922):
<p>Anyway, I should work instead of trolling</p>

#### [ Mario Carneiro (Sep 25 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134618948):
<p>I don't think that works, although it's so close I can taste it. What is the computable function that we are defining?</p>

#### [ Mario Carneiro (Sep 25 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619027):
<p>(Kenny, the gist is I posed a puzzle <a href="#narrow/stream/113489-new-members/subject/mathlib.20.26.20constructivity/near/134580592" title="#narrow/stream/113489-new-members/subject/mathlib.20.26.20constructivity/near/134580592">here</a> and people are trying to solve it.)</p>

#### [ Jared Corduan (Sep 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619086):
<p>well, it's one of two functions.  either 1) it is <code>f(n)</code> is the least <code>m&gt;n</code>such that <code>A(n)</code> or 2) it is <code>f(n)</code> is the least <code>m&gt;n</code>such that <code>~A(n)</code>.</p>

#### [ Jared Corduan (Sep 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619105):
<p>but I punted on giving you an actual <code>A</code>...</p>

#### [ Mario Carneiro (Sep 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619126):
<p>But we can't define either of those functions unless we have a proof (possibly using AC) that A(n) is infinite (resp. co-infinite)</p>

#### [ Jared Corduan (Sep 25 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619199):
<p>you can prove the infinite pigeon hole with <code>AC</code> and <code>LEM</code>, so all I'm missing is a good <code>A</code>, right?</p>

#### [ Mario Carneiro (Sep 25 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619312):
<p>right, but if we assume <code>A</code> is something about which we can prove very little, then we can't prove <code>A(n)</code> is infinite, so 1) can't be defined, and we can't prove <code>~A(n)</code> is infinite either, so 2) can't be defined</p>

#### [ Chris Hughes (Sep 25 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619345):
<p>What's the constructive proof that there exists a natural such that a^n=1 in a finite group?</p>

#### [ Mario Carneiro (Sep 25 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619367):
<p>If it is finite, then there is an upper bound on the cardinality, enumerate them all and test for equality</p>

#### [ Mario Carneiro (Sep 25 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619409):
<p>(you need decidable equality)</p>

#### [ Jared Corduan (Sep 25 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619454):
<p>ok, I might have misunderstood the problem!  I thought we wanted an <code>f</code> that needed <code>AC</code> and/or <code>LEM</code> in order to be defined, though it was built from these computable predicates.</p>

#### [ Mario Carneiro (Sep 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619495):
<p>That is what we want, but it also needs to be a term that represents a lean-computable function</p>

#### [ Mario Carneiro (Sep 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619527):
<p>It is okay if the proof of existence of the term is nonconstructive, like you tried, but the term itself must contain a proof that it halts since lean expects as much</p>

#### [ Jared Corduan (Sep 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134619598):
<p>ah ok, I'll have to think about that some more!</p>

#### [ Reid Barton (Sep 25 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620571):
<p>Could we do something like this? Inside Lean, build a language for programs in STLC or another system which Lean can prove is strongly normalizing, but incorporating the type <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mover accent="true"><mrow><mi mathvariant="double-struck">N</mi></mrow><mo>^</mo></mover></mrow><annotation encoding="application/x-tex">\hat \mathbb{N}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9523299999999999em;"></span><span class="strut bottom" style="height:0.9523299999999999em;vertical-align:0em;"></span><span class="base"><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9523299999999999em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathbb">N</span></span></span><span style="top:-3.25789em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>^</span></span></span></span></span></span></span></span></span></span> = nondecreasing functions nat -&gt; bool. Then the input to our function is a code for a function <code>f</code> from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mover accent="true"><mrow><mi mathvariant="double-struck">N</mi></mrow><mo>^</mo></mover></mrow><annotation encoding="application/x-tex">\hat \mathbb{N}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9523299999999999em;"></span><span class="strut bottom" style="height:0.9523299999999999em;vertical-align:0em;"></span><span class="base"><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9523299999999999em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathbb">N</span></span></span><span style="top:-3.25789em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>^</span></span></span></span></span></span></span></span></span></span> to <code>bool</code> together with a proof that <code>f inf = tt</code> (where <code>inf</code> <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>∈</mo><mover accent="true"><mrow><mi mathvariant="double-struck">N</mi></mrow><mo>^</mo></mover></mrow><annotation encoding="application/x-tex">\in \hat \mathbb{N}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9523299999999999em;"></span><span class="strut bottom" style="height:0.9914299999999999em;vertical-align:-0.0391em;"></span><span class="base"><span class="mrel">∈</span><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9523299999999999em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathbb">N</span></span></span><span style="top:-3.25789em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>^</span></span></span></span></span></span></span></span></span></span> is the constant function <code>ff</code>); we can enumerate such programs because the system is strongly terminating. In Lean+LEM, we can prove that every such function satisfies <code>f n = tt</code> for some finite <code>n</code>, and we ask that our function return the smallest such <code>n</code>.</p>

#### [ Reid Barton (Sep 25 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620748):
<p>Actually we don't even need the type <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mover accent="true"><mrow><mi mathvariant="double-struck">N</mi></mrow><mo>^</mo></mover></mrow><annotation encoding="application/x-tex">\hat \mathbb{N}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9523299999999999em;"></span><span class="strut bottom" style="height:0.9523299999999999em;vertical-align:0em;"></span><span class="base"><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9523299999999999em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathbb">N</span></span></span><span style="top:-3.25789em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>^</span></span></span></span></span></span></span></span></span></span>, we can just use the whole type <code>nat -&gt; bool</code>, but with the same idea.</p>

#### [ Reid Barton (Sep 25 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620778):
<p>If <code>f (const ff) = tt</code>, then there must be some finite <code>n</code> such that <code>f (\lam x, x &gt; n) = tt</code>.</p>

#### [ Reid Barton (Sep 25 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620813):
<p>Then we seek <code>g f = </code> the least <code>n</code> for which the above holds, provided that <code>f (const ff) = tt</code>, otherwise 37</p>

#### [ Reid Barton (Sep 25 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620905):
<p>(Compare <a href="http://math.andrej.com/2007/09/28/seemingly-impossible-functional-programs/" target="_blank" title="http://math.andrej.com/2007/09/28/seemingly-impossible-functional-programs/">http://math.andrej.com/2007/09/28/seemingly-impossible-functional-programs/</a>)</p>

#### [ Reid Barton (Sep 25 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134620946):
<p>Maybe this is actually still computable without LEM though</p>

#### [ Reid Barton (Sep 25 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134621676):
<p>Yeah, I doubt this can be made to work. If you can constructively define a normalizer for your language, then you can presumably modify it to keep track of the invocations of the argument, and return the largest number on which it is invoked, then search up to there. If you can't constructively define a normalizer for your language, then you should just use a normalizer for your language as the function we're looking for.</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134622225):
<p>Note that one way to "cheat" here is to have as input a nondecidable proposition, which you then use in the construction. I did something similar with my example of a function that takes as input a function that is not constant zero and returns a value in the range</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134622939):
<p>Here again we seem to be stuck: if we use STLC or something provably normalizing, then we won't need LEM to prove the compactness property, and if we use DTT functions then even AC won't help since compactness isn't provable (though true)</p>

#### [ Reid Barton (Sep 25 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623070):
<p>Yes. We would need a language whose power is just right so that the proof of normalization requires LEM, which I have no idea how to go about (or whether it is even plausible that such a language could exist).</p>

#### [ Reid Barton (Sep 25 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623309):
<p>Can we prove that Lean-with-N-universes is normalizing inside Lean-with-N+1-universes? What do we know about the relative consistency of AC?</p>

#### [ Reid Barton (Sep 25 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623359):
<p>Any term of type <code>nat -&gt; nat</code> is equal (in a meta sense) to one defined without using universe variables right?</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623378):
<p>I believe that Con(CIC+AC) = Con(CIC) for the same reasons as Con(ZF) = Con(ZFC)</p>

#### [ Reid Barton (Sep 25 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623467):
<p>I wonder whether we can just describe a meta-level procedure for taking a function defined in Lean+AC and producing an equal one defined in Lean (using one more universe) explicitly</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623469):
<p>I believe that lean-with-n-universes is normalizing in n+1 universes</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623492):
<p>I have to prove that lean is normalizing first though :)</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623545):
<p>any term of type nat -&gt; nat may contain universe variables but is parametric in them, so you get the same result no matter what they are set to</p>

#### [ Kenny Lau (Sep 25 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623572):
<blockquote>
<p>Any term of type <code>nat -&gt; nat</code> is equal (in a meta sense) to one defined without using universe variables right?</p>
</blockquote>
<p>I heard FLT uses universes</p>

#### [ Kenny Lau (Sep 25 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623574):
<p>Fermat's Last Theorem</p>

#### [ Reid Barton (Sep 25 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623625):
<p>by writing an evaluator for Lean+AC-in-N-universes in Lean-in-N+1-universes, and then at the meta level looking to see how many universes are actually used, picking N to be bigger than that and writing down a term in the model that corresponds to the given function</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623652):
<p>It may be that even without any universe variables you still need type 3 or something in the term</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623655):
<p>(re: kenny)</p>

#### [ Kenny Lau (Sep 25 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623688):
<p>but is it just because nobody has cleaned up the proof yet?</p>

#### [ Kenny Lau (Sep 25 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623694):
<p>do we really need type 3?</p>

#### [ Reid Barton (Sep 25 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623702):
<p>Kenny is taking over for Patrick on trolling duty</p>

#### [ Kenny Lau (Sep 25 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623811):
<p>i'm serious</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623831):
<p>We know that ZFC is equiconsistent with ZF, but I think that may include a double negation translation</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623845):
<p>(if you use IZF in place of ZF)</p>

#### [ Reid Barton (Sep 25 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623878):
<blockquote>
<p>I believe that Con(CIC+AC) = Con(CIC) for the same reasons as Con(ZF) = Con(ZFC)</p>
</blockquote>
<p>This is unclear to me because, in the case of ZF, we start from classical logic, at least in the version I know. But that's not to say that LEM is required for the relative consistency, only that I don't know whether it is.</p>

#### [ Mario Carneiro (Sep 25 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134623955):
<p>I also know that classical prop calc is equiconsistent with intuitionistic</p>

#### [ Reid Barton (Sep 25 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134624102):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <a href="https://mathoverflow.net/questions/35746/inaccessible-cardinals-and-andrew-wiless-proof" target="_blank" title="https://mathoverflow.net/questions/35746/inaccessible-cardinals-and-andrew-wiless-proof">https://mathoverflow.net/questions/35746/inaccessible-cardinals-and-andrew-wiless-proof</a> (See the first few answers.)</p>

#### [ Reid Barton (Sep 25 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134624631):
<p>Mario, right, that seems plausible then.</p>

#### [ Kevin Buzzard (Sep 26 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134652603):
<blockquote>
<p>What's the constructive proof that there exists a natural such that a^n=1 in a finite group?</p>
</blockquote>
<p>Let n be the order of the group ;-)</p>

#### [ Kevin Buzzard (Sep 26 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20%26%20constructivity/near/134652674):
<blockquote>
<blockquote>
<p>Any term of type <code>nat -&gt; nat</code> is equal (in a meta sense) to one defined without using universe variables right?</p>
</blockquote>
<p>I heard FLT uses universes</p>
</blockquote>
<p>Kenny that is fake news, but the rumour seems hard to kill. Some people might argue that "the proof is written using universes" (because at some point Wiles says the word "representable functor" and at some other point uses etale cohomology) but they can easily be expunged using standard tricks.</p>


{% endraw %}
