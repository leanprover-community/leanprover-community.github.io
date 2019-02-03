---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49854Lambdacalculus.html
---

## Stream: [general](index.html)
### Topic: [Lambda calculus](49854Lambdacalculus.html)

---


{% raw %}
#### [ Alexander Bentkamp (Dec 17 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152020148):
<p>Hello,<br>
Does anyone know of a formalization of the lambda calculus in Lean?<br>
In particular termination of beta/eta reduction?</p>

#### [ Patrick Massot (Dec 17 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152020719):
<p>I would have a look at <a href="https://github.com/leanprover/mathlib/tree/master/computability" target="_blank" title="https://github.com/leanprover/mathlib/tree/master/computability">https://github.com/leanprover/mathlib/tree/master/computability</a> (but maybe this is something else)</p>

#### [ Patrick Massot (Dec 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152020807):
<p>And, if it doesn't exist, maybe having a look at <a href="https://github.com/leanprover/mathlib/blob/5613d2ecc92ce8fae9555745bd94756dec61a323/group_theory/free_group.lean#L127" target="_blank" title="https://github.com/leanprover/mathlib/blob/5613d2ecc92ce8fae9555745bd94756dec61a323/group_theory/free_group.lean#L127">https://github.com/leanprover/mathlib/blob/5613d2ecc92ce8fae9555745bd94756dec61a323/group_theory/free_group.lean#L127</a> and <a href="https://github.com/leanprover/mathlib/blob/57194fa57e76721a517d6969ee88a6007f0722b3/logic/relation.lean#L288" target="_blank" title="https://github.com/leanprover/mathlib/blob/57194fa57e76721a517d6969ee88a6007f0722b3/logic/relation.lean#L288">https://github.com/leanprover/mathlib/blob/57194fa57e76721a517d6969ee88a6007f0722b3/logic/relation.lean#L288</a> could be a good idea</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152021502):
<p>I don't think lambda calculus has been done, although there are several projects in the same space</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152021571):
<p>I assume you are talking about simply typed lambda calculus, since of course the regular kind doesn't terminate</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152021611):
<p>I believe Jeremy has a formalization of lambda calculus, although he intended it for different purposes and I don't think he proved this property</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152021724):
<p>aha, here it is: <a href="https://github.com/avigad/embed/blob/master/src/exp.lean" target="_blank" title="https://github.com/avigad/embed/blob/master/src/exp.lean">https://github.com/avigad/embed/blob/master/src/exp.lean</a></p>

#### [ Mario Carneiro (Dec 17 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152021734):
<p>it's not much more than the definition</p>

#### [ Mario Carneiro (Dec 17 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152021811):
<p>I guess he never defined typechecking for lambda terms, since he was going for FOL</p>

#### [ Alexander Bentkamp (Dec 17 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152023395):
<p>Ok, thanks for the pointers. I will think about whether I'd like to work on this then. Actually, I'd like to formalize a unification procedure for lambda-terms, but I will need a formalization of the lambda-calculus for that first :-)</p>

#### [ Kenny Lau (Dec 17 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152023686):
<p>I might be missing something obvious here</p>

#### [ Kenny Lau (Dec 17 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152023688):
<p>but what happened to the Y-combinator?</p>

#### [ Kenny Lau (Dec 17 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152023697):
<p>oh, that's what "simply typed" rules out isn't it</p>

#### [ Alexander Bentkamp (Dec 17 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152023793):
<p>Yes, I wasn't very precise. I meant simply typed lambda calculus.</p>

#### [ Wojciech Nawrocki (Dec 19 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152218893):
<p>Hey, I'm actually working on this right now! Is there any particular formulation that you want to use? I'm trying to figure out inherently typed terms at the moment, but I have a formulation in raw terms with a typechecking procedure and a proof of progress, basically following "Software Foundations".</p>

#### [ Alexander Bentkamp (Dec 20 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152262213):
<p>Oh, that's great! As I said, I actually would like to formalize a unification procedure for lambda-terms. So if I could build on your library once it's finished, that would be perfect. I find it hard to predict which formulation would be more suitable for this, but I guess it doesn't matter too much.</p>

#### [ Wojciech Nawrocki (Dec 20 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152263621):
<p>It's not pretty code and definitely not suitable for a library, but I can upload it somewhere like git when I have a bit more time if that helps your project :)</p>

#### [ Wojciech Nawrocki (Dec 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152263723):
<p>By the way, you mean unification of the entire term assuming some holes on one (or both?) sides, not just types, right?</p>

#### [ Alexander Bentkamp (Dec 20 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152271412):
<p>Yes, with holes on both sides, but the holes are realized as free variables. In addition to that, there are also constant symbols. So for example, one could ask for unifiers of <code>f (X a) b</code> and <code>f c (Y d)</code>, where uppercase letters are variables and lowercase letters are constants. A unifier would be <code>{X ↦ λZ. c; Y ↦ λZ. b}</code>. The procedure is described here: <a href="https://www.sciencedirect.com/science/article/pii/0304397576900219" target="_blank" title="https://www.sciencedirect.com/science/article/pii/0304397576900219">https://www.sciencedirect.com/science/article/pii/0304397576900219</a></p>

#### [ Alexander Bentkamp (Dec 20 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152272457):
<p>So it sounds like you don't plan / don't have time to improve your code such that it would be usable as a library?  If I decide to formalize lambda calculus myself, I will ask you again for what you've done. But currently, I tend to using Isabelle/HOL instead for this project (Oh, oh, high treason in this chat I suppose).</p>

#### [ Wojciech Nawrocki (Dec 20 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152275053):
<p>Oh, I do hope to make it fairly readable, just not the very partial raw-term formulation, which is what I have currently, but rather the inherently-typed one which I only started on. That said, I'm using quantified type theory to support linear typing, which is more general than simply-typed lambda, but can be instantiated (I think..) to simply-typed lambda.</p>

#### [ Josh Pollock (Dec 20 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152293681):
<p>We actually did some stlc in lean in the University of Washington's graduate PL class last fall: <a href="https://courses.cs.washington.edu/courses/cse505/17au/lec11/lean/stlc.lean" target="_blank" title="https://courses.cs.washington.edu/courses/cse505/17au/lec11/lean/stlc.lean">https://courses.cs.washington.edu/courses/cse505/17au/lec11/lean/stlc.lean</a></p>

#### [ Alexander Bentkamp (Dec 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/152324240):
<p>Thanks! I'll have a closer look next year. Happy holidays :-)</p>

#### [ Patrick Thomas (Jan 02 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154197485):
<p>I just started learning lambda calculus. If you don't mind explaining, I was wondering why the condition <code>x2 \notin FV (e1) \/ x1 \notin FV (e)</code> is not a part of the definition for <code>lam_diff</code> in <code>is_subst</code>?</p>

#### [ Mario Carneiro (Jan 02 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154197511):
<p>are you referring to a particular formalization?</p>

#### [ Patrick Thomas (Jan 02 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154197586):
<p>Sorry, yes. The one that Josh Pollock posted a link to earlier in the thread.</p>

#### [ Mario Carneiro (Jan 02 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154197839):
<p>I think you are right. There are variable capturing substitutions that are admitted by <code>is_subst</code></p>

#### [ Patrick Thomas (Jan 02 2019 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154198088):
<p>If that is the case, would adding that condition be the simplest fix?</p>

#### [ Patrick Thomas (Jan 02 2019 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154201289):
<p>If I try to add connectives like <code>∧</code> and <code>∨</code> to the inductive definition, I seem to get an error of "...contains variables that are not parameters". Are these permitted in inductive definitions?</p>

#### [ Patrick Thomas (Jan 02 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154202553):
<p>Would this work?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">is_subst</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">string</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="c1">-- (λ y . P)[ x := N ] = (λ y . P [ x := N ]) if x ≠ y and y ∉ FV (N) or x ∉ FV (P)</span>
<span class="bp">|</span> <span class="n">lam_diff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">),</span>
    <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span>
    <span class="bp">→</span> <span class="o">((</span><span class="bp">¬</span> <span class="n">is_free</span> <span class="n">N</span> <span class="n">y</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="bp">¬</span> <span class="n">is_free</span> <span class="n">P</span> <span class="n">x</span><span class="o">))</span>
    <span class="bp">→</span> <span class="n">is_subst</span> <span class="n">P</span> <span class="n">x</span> <span class="n">N</span> <span class="n">e</span>
    <span class="bp">→</span> <span class="n">is_subst</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">y</span> <span class="n">P</span><span class="o">)</span> <span class="n">x</span> <span class="n">N</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">y</span> <span class="n">e</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jan 02 2019 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203012):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="kn">constant</span> <span class="n">is_free</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">string</span> <span class="bp">→</span> <span class="kt">Prop</span>

<span class="n">meta</span> <span class="kn">inductive</span> <span class="n">is_subst</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">string</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="c1">-- (λ y . P)[ x := N ] = (λ y . P [ x := N ]) if x ≠ y and y ∉ FV (N) or x ∉ FV (P)</span>
<span class="bp">|</span> <span class="n">lam_diff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">),</span>
    <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span>
    <span class="bp">→</span> <span class="o">((</span><span class="bp">¬</span> <span class="n">is_free</span> <span class="n">N</span> <span class="n">y</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="bp">¬</span> <span class="n">is_free</span> <span class="n">P</span> <span class="n">x</span><span class="o">))</span>
    <span class="bp">→</span> <span class="n">is_subst</span> <span class="n">P</span> <span class="n">x</span> <span class="n">N</span> <span class="n">e</span>
    <span class="bp">→</span> <span class="n">is_subst</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">y</span> <span class="n">sorry</span> <span class="n">P</span> <span class="n">sorry</span><span class="o">)</span> <span class="n">x</span> <span class="n">N</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">y</span> <span class="n">sorry</span> <span class="n">e</span> <span class="n">sorry</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jan 02 2019 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203014):
<p>this works for me verbatim</p>

#### [ Patrick Thomas (Jan 02 2019 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203290):
<p>Thank you. Do you think this would be a good fix for the definition?</p>

#### [ Kenny Lau (Jan 02 2019 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203316):
<p>no because it has <code>sorry</code></p>

#### [ Patrick Thomas (Jan 02 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203407):
<p>I'm sorry, I didn't mean verbatim, but if the definition was amended in this manner.</p>

#### [ Kenny Lau (Jan 02 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203425):
<p>my point is that I didn't change the part you complained about</p>

#### [ Kenny Lau (Jan 02 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203436):
<p>i.e. your diagnosis is not very accurate</p>

#### [ Patrick Thomas (Jan 02 2019 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203689):
<p>The diagnosis about the error message or about the definition in the link that Josh posted? My post may have been confusing. I don't get error messages for the code I posted, it was changed to avoid them. I was asking if it worked to fix the definition that Josh posted.</p>

#### [ Kenny Lau (Jan 02 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203786):
<p>oh... context...</p>

#### [ Patrick Thomas (Jan 02 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda%20calculus/near/154203800):
<p>Sorry about that.</p>


{% endraw %}
