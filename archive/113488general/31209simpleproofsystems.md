---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31209simpleproofsystems.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simple proof systems](https://leanprover-community.github.io/archive/113488general/31209simpleproofsystems.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Oct 14 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758238):
<p>Sorry in advance for a rather vague question, hopefully I can make it clear what I'm looking for.<br>
Suppose I wanted to "compile" Lean formulas and proof terms to some other logical system. How "simple" could the target logical system be?</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758249):
<p>hm, it is a bit vague</p>

#### [ Reid Barton (Oct 14 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758299):
<p>I want a human-verifiable procedure for taking a theorem statement and turning it into a formula in some other system, and also a procedure for turning the Lean proof into a valid proof in the other system</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758300):
<p>you can go pretty simple for almost any system, by appropriate encoding in the language of PA</p>

#### [ Reid Barton (Oct 14 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758308):
<p>So one kind of simplicity which I would like is if the formulas of the target system could be described by an inductive type, and provability could be described by an inductive proposition</p>

#### [ Reid Barton (Oct 14 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758325):
<p>Is the encoding you have in mind sort of how like I could simulate a checker for any language by a universal Turing machine?</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758366):
<p>yes</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758372):
<p>I get the sense that misses your point though</p>

#### [ Reid Barton (Oct 14 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758373):
<p>I see.</p>

#### [ Reid Barton (Oct 14 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758390):
<p>I was hoping for a system more like: if I have a proof of P and a proof of P -&gt; Q, then I get a proof of Q. Plus a bunch of axioms. I'm pretty sure that I need additional rules to deal with quantifiers though.</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758395):
<p>like ZFC style?</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758404):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow></mrow><annotation encoding="application/x-tex"> </annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0em;"></span><span class="strut bottom" style="height:0em;vertical-align:0em;"></span><span class="base"></span></span></span> + FOL</p>

#### [ Reid Barton (Oct 14 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758465):
<p>I think so but then I think I have to deal with substitution and that seems a little bit more complicated than I would like</p>

#### [ Reid Barton (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758479):
<p>Is metamath based on something like this?</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758487):
<p>I was about to suggest metamath indeed</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758494):
<p>it doesn't have proper substitution</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758500):
<p>just direct substitution</p>

#### [ Reid Barton (Oct 14 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758502):
<p>I guess another way to frame the question is: Suppose you wanted to be as sure as possible that you had correctly implemented a proof checker which only accepts theorems provable in ZFC+U (or whatever).</p>

#### [ Reid Barton (Oct 14 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758544):
<p>The universal turing machine idea doesn't help you here, because you still need to write the "actual machine" (it is just part of the specification of what constitutes a proof, rather than being the checker itself)</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758553):
<p>I think you can avoid proper substitution in the axioms and what not by having it be an explicit judgment in the system</p>

#### [ Reid Barton (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758554):
<p>what's not "proper" about direct substitution? Something about not renaming bound variables?</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758555):
<p>yes</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758557):
<p>metamath has a notion of text substitution a la grep</p>

#### [ Reid Barton (Oct 14 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758558):
<p>I think I've heard phrases like "proof calculus with explicit substitution", is that relevant?</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758598):
<p>that's about having terms in the language that are a sort of "deferred substitution"</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758603):
<p>but you still have to do the substitution at some point</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758608):
<p>although you can build it into the steps of actual proof, which is basically what metamath does</p>

#### [ Reid Barton (Oct 14 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758616):
<p>but does that mean I can push the work of substitution into the proof itself</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758617):
<p>yes</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758619):
<p>that way all your substitutions are direct</p>

#### [ Reid Barton (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758662):
<p>and if I were to target one of these systems then is there some kind of bound on how large the proofs would become in terms of the size of the original Lean proof term?</p>

#### [ Reid Barton (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758665):
<p>like, a useful bound</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758681):
<p>no, but the problem in that case is not substitution</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758682):
<p>it is reduction</p>

#### [ Reid Barton (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758684):
<p>oh right</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758687):
<p>you can prove ridiculous theorems by <code>rfl</code> in lean</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758714):
<p>If you deduplicate the proof I think substitution is a "modest" overhead, maybe linear in the proof</p>

#### [ Reid Barton (Oct 14 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758715):
<p>how about something like linear in the size of the term plus the total number of reduction steps Lean has to do (if that makes sense)</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758756):
<p>My favorite characterization is "linear in the run time of the lean checker"</p>

#### [ Reid Barton (Oct 14 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758757):
<p>Sure</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758815):
<p>You need substitution of some kind built in to your system so that you can express a proof schema like "|- P and |- P -&gt; Q implies |- Q`</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758818):
<p>but direct substitution is good enough</p>

#### [ Reid Barton (Oct 14 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758819):
<p>Okay this was going to be exactly my next question: do I need some kind of substitution</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758823):
<p>Actually metamath also has a primitive notion of "disjoint variables" used in substitution</p>

#### [ Reid Barton (Oct 14 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758824):
<p>Well</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758829):
<p>meaning that you can say "P can be substituted for any expression not containing x"</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758872):
<p>again, this is grep style, so no provisos like "no free x", just "no x at all"</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758875):
<p>but that is good enough since you can build the rest into the proof system</p>

#### [ Reid Barton (Oct 14 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758885):
<p>this particular example though is substituting into a fixed formula, right? I could imagine representing it by a constructor of an inductive type</p>
<div class="codehilite"><pre><span></span><span class="bp">|</span> <span class="n">mp</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="n">formula</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="k">proof</span> <span class="n">P</span><span class="o">)</span> <span class="o">(</span><span class="n">pq</span> <span class="o">:</span> <span class="k">proof</span> <span class="o">(</span><span class="n">formula</span><span class="bp">.</span><span class="n">imp</span> <span class="n">P</span> <span class="n">Q</span><span class="o">))</span> <span class="o">:</span> <span class="k">proof</span> <span class="n">Q</span>
</pre></div>

#### [ Mario Carneiro (Oct 14 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758910):
<p>yes, here you have lifted the substitution to the beta rule of the metatheory (which is lean, I guess)</p>

#### [ Reid Barton (Oct 14 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758912):
<p>which is just a built-in part of the syntax of proofs</p>

#### [ Reid Barton (Oct 14 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758952):
<p>But then, I don't know how to deal with "forall elim" without invoking substitution in a more serious way</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758958):
<p>right, you need a true substitution there... but you can get around it with some different axiomatizations</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135758967):
<p>I think the safest/easiest way to do this while still being transparent about it is to have a judgment <code>P(x |-&gt; y) is Q</code></p>

#### [ Mario Carneiro (Oct 14 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759010):
<p>although when you get to the bottom you have to deal with <code>z(x |-&gt; y)</code> which depends on a disjointness requirement</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759014):
<p>which can be equality if you have decidable equality on the variables</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759020):
<p>metamath takes a more abstract approach and just axiomatizes what this "disjointness" should satisfy</p>

#### [ Reid Barton (Oct 14 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759023):
<p>Yes that's fine. This looks interesting.</p>

#### [ Reid Barton (Oct 14 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759034):
<p>So I have a rule of inference that takes <code>forall x, P x</code> and <code>y</code> and <code>P(x |-&gt; y) is Q</code> and concludes <code>Q</code></p>

#### [ Mario Carneiro (Oct 14 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759039):
<p>right</p>

#### [ Reid Barton (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759082):
<p>and <code>P(x |-&gt; y) is Q</code> is also defined by some other induction</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759085):
<p>right</p>

#### [ Reid Barton (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759092):
<p>I like this.<br>
Is this likely to mess up the "size of proof is linear in the Lean kernel runtime" property?</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759094):
<p>no</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759096):
<p>because lean has to do this too</p>

#### [ Reid Barton (Oct 14 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759101):
<p>oh, I see!</p>

#### [ Mario Carneiro (Oct 14 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759173):
<p>You can have a similar induction rule for deducing <code>x is free in P</code> for the elim rules</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759369):
<p>By the way metamath <a href="http://us.metamath.org/mpeuni/mmset.html#pcaxioms" target="_blank" title="http://us.metamath.org/mpeuni/mmset.html#pcaxioms">doesn't do it this way</a>, instead it uses a slightly tricky axiom system for pred calc that allows us to deduce these judgments without building them in directly, and lets the forall rule be the simple <code>|- (forall x, P) -&gt; P</code></p>

#### [ Mario Carneiro (Oct 14 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759489):
<p>But I think this is something like the difference between listing 20 obvious axioms for boolean algebras vs listing 3 incomprehensible ones and proving they are equivalent</p>

#### [ Reid Barton (Oct 14 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759619):
<p>So here is one reason why I have this question.<br>
Cryptography people tell me (not in this language of course, and I hope I am not mistranslating anything) that if I have some fancy indexed inductive type <code>proof P</code>, I can design some functions f, g and h with the following properties.</p>
<ul>
<li>f is a predicate on short strings (~300 bytes) which can be evaluated quickly (~20ms).</li>
<li>g is some even cheaper function on such strings, and h(P) is just a recursive hash of the contents of P.</li>
<li>Given a term of type <code>proof P</code> I can calculate a string x with f(x) = true and g(x) = h(P).</li>
<li>(Subject to some trusted setup and cryptographic hardness assumptions,) the only way to construct such an x is as above: I have to really know a term of type <code>proof P</code>, though I can also use other pairs (Q, y) which have been published as certificates of other statements as inputs to my term.</li>
</ul>
<p>The catch is that the third item is somewhat ridiculously expensive, though in the future it may become less ridiculously expensive.</p>

#### [ Reid Barton (Oct 14 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759630):
<p>As a ballpark estimate for ridiculously expensive, assume 1 constructor costs 1 second to compute</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759688):
<p>so I guess x is a "proof hash" of some sort, f means "this is a proof of something" and g means "this is the statement that is being proved"?</p>

#### [ Reid Barton (Oct 14 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759689):
<p>Right</p>

#### [ Reid Barton (Oct 14 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759757):
<p>Probably it is a bit better to think that the "proof hash" is a statement like "this is a proof of some statement which hashes to H"</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759809):
<p>I'm surprised the function g is easy</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759818):
<p>it's not even that easy to calculate the statement of a proof sometimes</p>

#### [ Reid Barton (Oct 14 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759821):
<p>I think that g can just be extracting some of the bits from the string though I confess I have not thought much about this particular aspect yet</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759828):
<p>I guess you can do something like that</p>

#### [ Reid Barton (Oct 14 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759830):
<p>I think the idea is that it was the job of the person producing the proof to include the information of what is being proved</p>

#### [ Reid Barton (Oct 14 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759883):
<p>This is really at a super early stage of "is it even conceivable that one could use this for theorem proving"--I'm trying to get a sense of what the minimal demands on the theorem proving side are</p>

#### [ Reid Barton (Oct 14 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759891):
<p>What I find to be really remarkable about these setups is that the cost to verify a proof is independent of the size of the proof</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759944):
<p>that's a good point. I wonder whether it can be used as a trusted alternative to caching</p>

#### [ Reid Barton (Oct 14 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135759954):
<p>So, ignoring some inconvenient details like the ~1000000x slowdown, you could use it as part of a "distributed theorem verification system", without requiring trusted provers</p>

#### [ Reid Barton (Oct 14 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760023):
<p>(Concretely, you could imagine some kind of database to which anyone can upload proof certificates, with the amazing property that in order to verify the correctness of any proof, you only need to check <em>that certificate</em> and not the proofs of any of the results which the proof relies on)</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760029):
<p>Unless they decided to modify <code>logic.basic</code> :)</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760085):
<p>In some sense we already have this, the difference is that you can do this check without even precomputing the proofs of earlier parts, or even knowing what the proofs are (e.g. proprietary proofs)</p>

#### [ Reid Barton (Oct 14 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760134):
<p>I think what we have is like a non-distributed version of this, where I trust the Lean kernel on my machine to only record as theorems the facts which it has checked. Or do you mean something else?</p>

#### [ Reid Barton (Oct 14 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760191):
<p>Solving the recompilation problem is somehow close to but not exactly the same as the problem this solves, I think.</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760192):
<p>That's true, but I'm pointing out that if you have mathlib, say, fully compiled, then you are currently in the state of trusting all the results in it, and if a new proof comes along that depends on these facts you only have to check <em>that proof</em> and not the rest of the library</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760197):
<p>In this crypto setup compilation is being replaced by certificate generation</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760251):
<p>where the difference is that if I send you a certificate you can have the same trust as if you created it yourself, while if I send you my compiled files then you don't know that I haven't tampered with them</p>

#### [ Reid Barton (Oct 14 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760254):
<p>Yes exactly</p>

#### [ Reid Barton (Oct 14 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760271):
<p>And if we had some massive proof of say FLT, then maybe it would be quite expensive for everyone to verify the whole proof, whether or not they do it incrementally over time. If the certificates can be computed by someone just once, then you can save total work (assuming there are &gt; 1000000 people who want to verify the proof)</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760330):
<p>I think this isn't a realistic threat model though</p>

#### [ Reid Barton (Oct 14 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760331):
<p>Anyways, I think that today we're not really anywhere close to wanting something like this, and the technology is also not really that feasible yet</p>

#### [ Reid Barton (Oct 14 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760372):
<p>Which part is not realistic?</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760373):
<p>I think when people get mathlib they usually don't do it because they want additional assurance that the theorems in it are true</p>

#### [ Reid Barton (Oct 14 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760374):
<p>Well not for mathlib</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760385):
<p>I am pretty sure that feit thompson is true because Gonthier checked it, and my running it on my machine did not increase my confidence in the theorem as much as it increased my confidence that I had installed Coq correctly</p>

#### [ Reid Barton (Oct 14 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760427):
<p>In some distant future world, you could imagine that instead of posting papers to arXiv, we publish formal proofs to some other service. I guess your claim is that in that scenario, you are not too worried about people claiming to publish proofs which are in fact bogus.</p>

#### [ Reid Barton (Oct 14 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760434):
<p>Especially given that anyone <em>could</em> verify the proof and everything underneath it, it would just be quite expensive for everybody to do so.</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760438):
<p>I would want the service to be spending effort on checking for bogus proofs</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760443):
<p>that's not my responsibility</p>

#### [ Reid Barton (Oct 14 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760447):
<p>Right, you could delegate to the service to check correctness which seems quite reasonable</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760487):
<p>I would be responsible for convincing myself that the service is doing its job to my satisfaction</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760492):
<p>meaning that this service should be easily checkable (i.e. small trusted kernel)</p>

#### [ Reid Barton (Oct 14 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760508):
<p>Plus you have to trust the people who operate the service to actually verify the proofs</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760567):
<p>I think there is room for some crypto cross checks at this point</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760577):
<p>i.e. the process of verification by the service also produces a certificate that I can check quickly</p>

#### [ Reid Barton (Oct 14 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760625):
<p>In general the way to produce a certificate that a computation was done correctly is the same process that I am talking about for generating proof certificates.</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760636):
<p>Although nowadays this check is replaced with me being able to download and check the proof myself if I want</p>

#### [ Reid Barton (Oct 14 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760637):
<p>(Namely, SNARKs and applications like TinyRAM)</p>

#### [ Reid Barton (Oct 14 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760645):
<p>Right so in actual crypto applications, there is the far more important property that the person producing the certificate doesn't have to give you the proof.</p>

#### [ Reid Barton (Oct 14 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760711):
<p>As I mentioned, this stuff is currently quite impractical for large applications.<br>
Probably a far more practical question would be: could Lean have a mode where it checks a given olean file against lean source, and is this faster than trying to recompute the proof from scratch.</p>

#### [ Reid Barton (Oct 14 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760762):
<p>Or more generally, what information could Lean write out to an .olean or other external certificate file which would make verifying the validity of a theorem more efficient</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760873):
<p>In principle lean should be able to check an olean file without reference to a lean file at all</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760883):
<p>and if you wanted you could view this as a "compiled file" same as the compiled binaries of any other program</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760886):
<p>in particular, it would be difficult to reverse engineer the sources from this</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760890):
<p>... I think. I need to write an olean viewer to be sure</p>

#### [ Reid Barton (Oct 14 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135760994):
<p>Do .olean files and the export textual format and what <code>#print foo</code> produces all contain roughly the same information?</p>

#### [ Reid Barton (Oct 14 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761081):
<p>looking at the export format it seems not to include all information about notation, which must be in .olean files, but aside from minor details like that</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761088):
<p>I think so</p>

#### [ Mario Carneiro (Oct 14 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761089):
<p>It should have the information necessary to construct an <code>environment</code> object from the imported environments</p>

#### [ Reid Barton (Oct 14 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761091):
<p>I wonder whether there is a way today to convince Lean to export an .olean file to textual format</p>

#### [ Mario Carneiro (Oct 14 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761139):
<p>That would be nice... I probably wouldn't even write such an exporter in lean</p>

#### [ Mario Carneiro (Oct 14 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761151):
<p>(that is, there is no particular advantage to writing it in lean)</p>

#### [ Reid Barton (Oct 14 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761215):
<p>I guess you could import the module for which you had the .olean from a new module, and then run it through <code>lean --export</code></p>

#### [ Reid Barton (Oct 14 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761310):
<p>it seems to work</p>

#### [ Reid Barton (Oct 14 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761322):
<p>though I wouldn't be 100% confident that lean importing an arbitrary .olean file and then exporting its contents and checking them in an external checker means lean is actually in a valid state after reading the .olean file</p>

#### [ Mario Carneiro (Oct 14 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761702):
<p>why? The checker doesn't matter for that</p>

#### [ Mario Carneiro (Oct 14 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761703):
<p>Lean itself will complain if the olean is bad</p>

#### [ Mario Carneiro (Oct 14 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135761709):
<p>although I'm not sure how you can induce that without writing the olean bits manually, since lean won't produce olean files for errored files</p>

#### [ Kevin Buzzard (Oct 14 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135771923):
<blockquote>
<p>I want a human-verifiable procedure for taking a theorem statement and turning it into a formula in some other system, and also a procedure for turning the Lean proof into a valid proof in the other system</p>
</blockquote>
<p>My understanding (which may be wrong) is: Computer scientists want (and occasionally some claim that they have built) a procedure for translating code written in one common language to code written in another common language, and the reason none of these procedures are ever used in practice is that in practice they are typically not very good at all.</p>
<blockquote>
<p>I am pretty sure that feit thompson is true because Gonthier checked it, and my running it on my machine did not increase my confidence in the theorem as much as it increased my confidence that I had installed Coq correctly</p>
</blockquote>
<p>My understanding (which is much more likely to be correct this time) is that Feit Thompson is true because the pure mathematics community did an <em>extremely</em> good job of checking it in the 1960s, decided it was correct, and awarded Thompson the Fields Medal as a consequence. This is exactly why pure mathematicians are not excited by Gonthier et al's verification. Checking 400 pages of lemmas about finite groups and undergraduate/MSc level representation theory and number theoy is not difficult for a team of humans to do, it can be broken down into manageable sub-jobs etc.</p>

#### [ Mario Carneiro (Oct 14 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135772552):
<p>Yeah, but I didn't understand what Thompson did at all, I at least have some idea of how Gonthier did it</p>

#### [ Mario Carneiro (Oct 14 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135772564):
<p>I think you should not forget that one of the applications of formal mathematics is that at least in principle you can pick it up and read it from <em>zero</em> prior knowledge of the field</p>

#### [ Mario Carneiro (Oct 14 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135772607):
<p>And I know several people who did exactly that, including myself</p>

#### [ Mario Carneiro (Oct 14 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135772725):
<p>(Note that that quote was about my subjective perception of the truth of the theorem, not the mathematics community at large.) The whole point of this crypto stuff is that just because <em>you</em> trust X body of knowledge / institution / person doesn't mean <em>I</em> do, and the problem is to figure out how to reliably transfer your trust to me</p>

#### [ Kevin Buzzard (Oct 14 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135776718):
<p>Aah I see! So this is a perfect analogy. I say "I am a mathematician and my tribe can guarantee that Feit-Thompson is proved" and you reply "I am a computer scientist and I require a different kind of justification than just assurances from your tribe".</p>

#### [ Patrick Massot (Oct 14 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135776739):
<blockquote>
<p>I think you should not forget that one of the applications of formal mathematics is that at least in principle you can pick it up and read it from <em>zero</em> prior knowledge of the field</p>
</blockquote>
<p>I thought mathlib didn't care about human readability?</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135776942):
<p>I'm talking about formal proof in general. Certainly it's more true of metamath than mathlib, because there are fewer skipped steps</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135776974):
<p>The point is that it doesn't matter if it's been written to be human readable in the mathematician's sense. In fact, it's better if it doesn't make too much use of tactics that do what Kevin wants (i.e. trivial for a mathematician steps omitted)</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135777021):
<p>because that way you can follow what's happening even if you aren't a mathematician</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135777103):
<p>the worst kind of proof for people who want to learn like this are the big complicated statement proven by some blasty tactic. It's like the movie ends just as it's setting up for the climax, you feel robbed</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135777177):
<p>luckily lean doesn't have too many blasty tactics yet, so it is still feasible to read a proof and get the details</p>

#### [ Kevin Buzzard (Oct 14 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135777934):
<p>I have been telling my maths students to never read any proofs in mathlib because they are all unreadable, and if they want to know why some theorem is true then to look it up on Wikipedia, which is written for humans. I am the anti-Paulson. I believe that proofs generated by computers in the future will inevitably be unreadable, and that anyone who attempts to make them readable will in some sense be holding the area back. I was always struck by something Johannes said to me months ago when I asked him why he'd changed my 10 line tactic proof into an incomprehensible two-line term proof, and he replied that he liked the challenge of finding a short efficient proof of something which was easy in maths. While he might not want to extrapolate this comment himself to longer proofs, I don't mind doing so.</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778173):
<p>My view is that there is a kind of readability that can't be harmed by "unreadable" proof style</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778177):
<p>because the information is still there to be given to the computer</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778228):
<p>and there are some enterprising kids that actually prefer this kind of exactitude to the "aimed for human level" style that is traditional in maths</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778285):
<p>This is where stuff like <code>#explode</code> is useful, when you just want to see EVERYTHING and make your own choices about what is important</p>

#### [ Mario Carneiro (Oct 14 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135778292):
<p>rather than whatever the author thought was important or trivial</p>

#### [ Patrick Massot (Oct 14 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135780253):
<blockquote>
<p>I have been telling my maths students to never read any proofs in mathlib because they are all unreadable, and if they want to know why some theorem is true then to look it up on Wikipedia, which is written for humans.</p>
</blockquote>
<p>I just did the exercise of reading the Wikipedia page on <a href="https://en.wikipedia.org/wiki/Topological_ring" target="_blank" title="https://en.wikipedia.org/wiki/Topological_ring">topological rings</a>. It's full of plain wrong statements...</p>

#### [ Kevin Buzzard (Oct 14 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135786040):
<p>You have a clear choice then :-) Human efforts with wrong statements, or <code>topological_structures.lean</code> written by Johannes and never meant to be read by a mathematician :-) Pure maths is two things and you are lucky enough to be able to choose which one you like best.</p>

#### [ Johan Commelin (Oct 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simple%20proof%20systems/near/135797803):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110032">@Reid Barton</span> I find this topic of cryptographic proof certificates really interesting! Do you know if anything like this has been implemented for some theorem prover? I've thought about this on and off (basically as an amateur) and I couldn't find anything written about it. Are there references that go beyond speculating how nice it would be to have this? From Reid's description it is still quite a leap to an actual (fast) implementation.</p>


{% endraw %}
