---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49997homeoequivetc.html
---

## Stream: [maths](index.html)
### Topic: [homeo equiv etc.](49997homeoequivetc.html)

---


{% raw %}
#### [ Patrick Massot (Apr 03 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593811):
<p>A more specific version of <a href="#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243" title="#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243</a> (it may be easier to understand my problem by looking at code) is <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L188" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L188">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L188</a> where I'm clearly very stupidly trying to Lean some trivial lemma. I'm completely tangled in coercions and type classes</p>

#### [ Patrick Massot (Apr 03 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593836):
<p>I need two version of <code>supp</code> because I don't know how to have only one</p>

#### [ Patrick Massot (Apr 03 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593899):
<p>Then we have a classical <code>rw</code> failure on line 193 (always the same thing, <code>rw</code> itself doesn't do some kind of elaboration or reduction that is needed, and I still can't quite point out what)</p>

#### [ Patrick Massot (Apr 03 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593923):
<p>Then I  would like line 196 to be unnecessary (with the ugly <code> (g.to_equiv).inv_fun</code> never appearing)</p>

#### [ Patrick Massot (Apr 03 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593970):
<p>And finally the computation which should be easy (but still the core of the proof) and cannot do it</p>

#### [ Patrick Massot (Apr 03 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593994):
<p>I'd like to know whether the full setup is broken from the beginning or I only need a couple a carefully crafted simp lemmas to hide this mess (and prove stuff).</p>

#### [ Chris Hughes (Apr 03 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124594355):
<p>cons_inj tells me about the lists being equal. Oops wrong topic.</p>

#### [ Patrick Massot (Apr 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688060):
<p>I can see this topic has not much success. Maybe the context is too complicated because of topology. But I really think this will come up in other places. The question is: how to do group theory with groups of transformations? As long as you don't need to use the inverse of a transformation, you can easily  functions and composition of function. But what about inverses? Say I'm working with permutations of a type (not necessarily encoded as <code>perm</code> in current mathlib). I define the support of a permutation f as the complement supp f of the fixed point set (no topology here). I want to prove supp gfg⁻¹ = g(supp f). And ideally I would really like f, g and g⁻¹ to live in a type endowed with a group structure, because I have other group theoretic stuff to do. What encoding should I use? How to then talk about the image of a subset as in g(supp f)?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688263):
<p>I got as far as cutting and pasting a 230 line file and then realising I didn't have the imports</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688289):
<p>You define <code>suppp f</code> to be <code>supp f</code>?</p>

#### [ Patrick Massot (Apr 05 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688345):
<p>If you want to directly play with code it's much faster to git clone</p>

#### [ Patrick Massot (Apr 05 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688349):
<p>Yes, that definition is part of the problem</p>

#### [ Patrick Massot (Apr 05 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688354):
<p>I couldn't avoid it</p>

#### [ Patrick Massot (Apr 05 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688432):
<p>It's part of coercion/extension hell</p>

#### [ Patrick Massot (Apr 05 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688448):
<p><code>supp</code> is defined on functions from <code>X</code> to <code>X</code></p>

#### [ Patrick Massot (Apr 05 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688450):
<p>homeos have coercions to functions</p>

#### [ Patrick Massot (Apr 05 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688494):
<p>but it's not enough</p>

#### [ Patrick Massot (Apr 05 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688499):
<p>try to replace <code>suppp</code> by <code>supp</code> in the statement following that def and it won't type check</p>

#### [ Patrick Massot (Apr 05 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688514):
<p>But it's probably easier to solve the problem as I described it today than to add the topology layer</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688561):
<p>It's just too hard to make it work.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688568):
<p>I have mathlib not compiling.</p>

#### [ Patrick Massot (Apr 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688569):
<p>make what work?</p>

#### [ Patrick Massot (Apr 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688572):
<p>I just pushed a version compatible with latest Lean nightly and mathlib head</p>

#### [ Patrick Massot (Apr 05 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688579):
<p>(only handling a renamed lemma)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688725):
<p>Now I have errors in commutators.lean and groups.lean</p>

#### [ Patrick Massot (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688738):
<p>those are old stuff irrelevant here</p>

#### [ Patrick Massot (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688742):
<p>they are not updated</p>

#### [ Patrick Massot (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688745):
<p>(this repo is my garbage repo, I'm sorry)</p>

#### [ Patrick Massot (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688748):
<p>Everything imported in <code>support.lean</code> is ok</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688757):
<p>OK it now compiles. What's the question?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688762):
<p>Not that I'm likely to be able to answer it...</p>

#### [ Patrick Massot (Apr 05 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688811):
<p>How do you sort out the mess with <code>supp</code> vs <code>suppp</code>, <code>fundamental</code> vs <code>fundamental''</code>, how to remove the sorries in the proof of <code>supp_conj</code></p>

#### [ Chris Hughes (Apr 05 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688881):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">equiv</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="kn">lemma</span> <span class="n">mul_apply</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="o">(</span><span class="n">b</span> <span class="n">x</span><span class="o">))</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">one_apply</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">α</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="n">def</span> <span class="n">support</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">a</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">x</span><span class="o">}</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">perm</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">support</span> <span class="o">(</span><span class="n">g</span> <span class="bp">*</span> <span class="n">f</span> <span class="bp">*</span> <span class="n">g</span><span class="bp">⁻¹</span><span class="o">)</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="n">g</span> <span class="o">(</span><span class="n">support</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">_</span> <span class="bp">≠</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">g</span><span class="bp">⁻¹</span> <span class="n">y</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h₁</span><span class="o">,</span> <span class="k">by</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_apply</span><span class="o">,</span> <span class="n">mul_apply</span><span class="o">,</span> <span class="n">h₁</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_apply</span><span class="o">,</span> <span class="n">mul_inv_self</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="n">h</span> <span class="n">rfl</span><span class="o">,</span>
<span class="k">show</span> <span class="o">(</span><span class="n">g</span> <span class="bp">*</span> <span class="n">g</span><span class="bp">⁻¹</span><span class="o">)</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">y</span><span class="o">,</span><span class="k">by</span> <span class="n">rw</span> <span class="n">mul_inv_self</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="bp">_</span> <span class="bp">≠</span> <span class="bp">_</span> <span class="bp">∧</span> <span class="bp">_</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">show</span> <span class="bp">_</span> <span class="bp">≠</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_apply</span><span class="o">,</span> <span class="err">←</span> <span class="n">hx</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_apply</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_apply</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">inv_mul_self</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">,</span> <span class="n">mul_apply</span><span class="o">],</span>
  <span class="k">assume</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">bijective</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h</span> <span class="n">at</span> <span class="n">hx</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">hx</span><span class="bp">.</span><span class="mi">1</span> <span class="n">rfl</span>
<span class="kn">end</span><span class="bp">⟩</span>
</pre></div>

#### [ Chris Hughes (Apr 05 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688971):
<p>(deleted)</p>

#### [ Chris Hughes (Apr 05 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689034):
<p>I proved a bit of stuff about permutations a few months ago.</p>

#### [ Patrick Massot (Apr 05 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689045):
<p>Thank you very much. Now I need to rewrite it in full tactic mode to see how it could help</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689055):
<p>The issue is that you are using coe everywhere?</p>

#### [ Patrick Massot (Apr 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689076):
<p>What do you mean using coe everywhere?</p>

#### [ Patrick Massot (Apr 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689123):
<p>I need homeomorphisms to be able to act as functions</p>

#### [ Patrick Massot (Apr 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689124):
<p>So yes, they coerce to functions</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689126):
<p>Is the reason the rw doesn't work on line 193 that you are pushing type class inference too hard?</p>

#### [ Patrick Massot (Apr 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689186):
<p>I have no idea</p>

#### [ Patrick Massot (Apr 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689188):
<p>Clearly there is something I'm doing wrong</p>

#### [ Patrick Massot (Apr 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689194):
<p>I only want to learn how to do it right</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689259):
<div class="codehilite"><pre><span></span>ambiguous overload, possible interpretations
  right_inverse
  function.right_inverse
</pre></div>

#### [ Patrick Massot (Apr 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689274):
<p>where do you see that?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689278):
<p>when I write <code>#check right_inverse</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689281):
<p>I don't know how to check types of objects in the middle of Lean code.</p>

#### [ Patrick Massot (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689282):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> don't you have a version of your proof before obfuscation?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689287):
<p>Is there an easy way to do that?</p>

#### [ Patrick Massot (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689288):
<p>This is something I wonder all the time</p>

#### [ Patrick Massot (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689291):
<p>it seems the answer is no</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689294):
<p>You'd wonder it more if you were reading someone else's code...</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689413):
<p>So what is <code> (g.to_equiv).to_fun</code>?</p>

#### [ Mario Carneiro (Apr 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689414):
<p>The reason this topic didn't get much discussion is because you basically said "there is something wrong, check out my code base and find the error"</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689418):
<p>he said lots of things</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689420):
<p>maybe there were lots of errors :-)</p>

#### [ Mario Carneiro (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689421):
<p>Could you at least post the error message?</p>

#### [ Mario Carneiro (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689430):
<p>(s)</p>

#### [ Patrick Massot (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689431):
<p>There is no error message. I can't prove stuff</p>

#### [ Patrick Massot (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689432):
<p>Because I'm clearly going against Lean</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689436):
<p>Are you being anti-idiomatic?</p>

#### [ Patrick Massot (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689437):
<p>Not writing idiomatic Lean</p>

#### [ Patrick Massot (Apr 05 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689479):
<p>exactly</p>

#### [ Mario Carneiro (Apr 05 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689487):
<p>what? I am not in a position to see what you are talking about unless you say it here</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689505):
<p>If you want to get to the bottom of the reason rewrite fails on line 193 you should write a MWE. But I know this isn't your real question.</p>

#### [ Chris Hughes (Apr 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689522):
<blockquote>
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> don't you have a version of your proof before obfuscation?</p>
</blockquote>
<p>That's how I wrote it first time. I shouldn't have opened the <code>perm</code> namespace, so if it didn't work that's probably why.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689526):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is there a way of checking the type of a term in the middle of a tactic proof?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689530):
<p>I tried to describe my problems in <a href="#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243" title="#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243</a> without code, and then I posted link to my actual code. Then I tried to describe a simplified problem. I don't what I could do better to ask for help</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689571):
<p>i.e. I can't check it outside the begin/end block because the term is only constructed within the block</p>

#### [ Patrick Massot (Apr 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689572):
<p>I'm honestly asking</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689582):
<p>So what is <code> (g.to_equiv).to_fun</code>?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689588):
<p>It's the function underlying the homeomorphism g</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689592):
<p>for <code>g : homeo X X</code></p>

#### [ Patrick Massot (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689595):
<p>But it goes through two conversions</p>

#### [ Patrick Massot (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689601):
<p>First to <code>equiv X X</code> and then to <code>X -&gt; X</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689602):
<p>When you write <code>g '' ...</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689604):
<p>what do you think happens there?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689607):
<p>That's mathlib notation for image of a subset</p>

#### [ Patrick Massot (Apr 05 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689647):
<p>Lean does figure out the coercions here</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689649):
<p><code>set.image</code> so it takes a function</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689653):
<p>and which function does it take?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689678):
<p>Is there some coe directly from homeo to the function?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689681):
<p><code>(g.to_equiv).to_fun</code></p>

#### [ Patrick Massot (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689684):
<p>yes</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689685):
<p>That's what it uses?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689691):
<p><code>instance : has_coe_to_fun (homeo α β) := ⟨_, λ f, f.to_fun⟩</code></p>

#### [ Patrick Massot (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689695):
<p>is defined in <code>homeos.lean</code></p>

#### [ Patrick Massot (Apr 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689723):
<p>It's indeed the same as <code>(g.to_equiv).to_fun</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689742):
<p>This is a funny error message then:</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689744):
<div class="codehilite"><pre><span></span>rewrite tactic failed, did not find instance of the pattern in the target expression
  (g.to_equiv).to_fun &#39;&#39; {a : X | (λ (x : X), f x ≠ x) a}
state:
X : Type,
_inst_3 : topological_space X,
f g : homeo X X
⊢ {x : X | conj g f x ≠ x} = g &#39;&#39; {x : X | f x ≠ x}
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689756):
<p>Is it definitionally the same?</p>

#### [ Chris Hughes (Apr 05 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689771):
<p>rw doesn't do definitionally equal things.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689776):
<p>oh yeah</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689779):
<p>that's the second time I've forgotten that this week</p>

#### [ Patrick Massot (Apr 05 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689785):
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="o">(</span><span class="n">g</span><span class="o">:</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">=</span> <span class="n">g</span><span class="bp">.</span><span class="n">to_equiv</span><span class="bp">.</span><span class="n">to_fun</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689829):
<p>Chris points out the problem</p>

#### [ Patrick Massot (Apr 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689831):
<p>Yes, I understand this is the problem with the rewrite</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689833):
<p>definitionally equivalent is not enough</p>

#### [ Patrick Massot (Apr 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689838):
<p>But I'd like to know the proper way of either not having this problem or workaround it</p>

#### [ Patrick Massot (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689850):
<p>without doing this <code>swap, exact ...</code> thing</p>

#### [ Chris Hughes (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689854):
<p>Never use <code>( g.to_equiv).to_fun</code>?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689863):
<p>I don't write this myself</p>

#### [ Chris Hughes (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689868):
<p>I usually use <code>show</code> otherwise.</p>

#### [ Patrick Massot (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689872):
<p>it only appears in goals and error messages</p>

#### [ Patrick Massot (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689928):
<p>What is this <code>λ h : _ ≠ _,</code> dark magic?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689929):
<p>I had problems with coercions when I was doing schemes so I just stopped using them completely</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689930):
<p>and wrote everything out in full</p>

#### [ Patrick Massot (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689933):
<p>How do you do it in tactic mode?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689935):
<p>show works in tactic mode</p>

#### [ Patrick Massot (Apr 05 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689952):
<p>Kevin, how would you do group theory with permutations of a Type without coercions?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689958):
<p><code> show _ ≠ _ </code> :-)</p>

#### [ Patrick Massot (Apr 05 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689962):
<p>You both need elements of the group to act on points and to have inverses</p>

#### [ Patrick Massot (Apr 05 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690007):
<p>Re: <code>_ ≠ _</code> he does this in place of <code>intro</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690009):
<p>I'm just saying that you just write the coercions explicitly.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690013):
<p>That was what I did when I got sick of getting type class inference to work. I just wrote down everything myself.</p>

#### [ Patrick Massot (Apr 05 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690085):
<p>There must be a better way</p>

#### [ Patrick Massot (Apr 05 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690100):
<p>In real world you would never need to distinguish the element of a group of transformation from themselves like this</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690118):
<p>the real world doesn't use dependent type theory</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690122):
<p>it uses one piece of notation to mean more than one thing</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690129):
<p>and we're so used to that, that this world can be kind of annoying sometimes</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690167):
<p>with their silly pedantic fussing</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690176):
<div class="codehilite"><pre><span></span>show {x : X | conj g f x ≠ x} = g.to_equiv.to_fun &#39;&#39; {x : X | f x ≠ x},
rw aux_1 g.right_inv,
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690178):
<p>works for 193 ;-)</p>

#### [ Patrick Massot (Apr 05 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690265):
<p>I don't understand what <code>show</code> does here</p>

#### [ Patrick Massot (Apr 05 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690267):
<p>Usually I need to supply a proof after <code>show</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690273):
<p>it rewrites the goal into a definitionally equivalent form</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690277):
<p>If the goal is X, then <code>show X,</code> does nothing</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690280):
<p>if the goal is definitionally equal to X, it changes the goal to X</p>

#### [ Patrick Massot (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690287):
<p>I can see it's doing that here. But what's the link with <code>show</code> I usually use?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690291):
<p>which I guess is in term mode</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690293):
<p>I don't know, this is the only show I use</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690294):
<p>tactic mode is the bomb</p>

#### [ Patrick Massot (Apr 05 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690370):
<p>I use <code>show</code> in arguments to <code>rw</code> and <code>simp</code> for easy stuff I don't want to state and name using <code>have</code> beforehand</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690467):
<p>Line 190: <code>lemma  supp_conj (f g : homeo X X) : supp (conj g f : homeo X X) = g '' supp f :=</code> works</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690530):
<p>i.e. I removed <code>suppp</code></p>

#### [ Patrick Massot (Apr 05 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690543):
<p>Very interesting</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690545):
<p>You are using <code>f</code> and <code>g</code> to mean two different things, and it guessed you wanted the map not the homeo here</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690553):
<p>the second suppp could just be removed, but the first one had to be persuaded</p>

#### [ Patrick Massot (Apr 05 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690561):
<p>Probably because <code>perm X</code> is also a group</p>

#### [ Patrick Massot (Apr 05 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690627):
<p>and Lean doesn't know the group structure on <code>homeo X X</code> is induced as a subgroup of <code>perm X</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690659):
<blockquote>
<p>Then I  would like line 196 to be unnecessary (with the ugly <code> (g.to_equiv).inv_fun</code> never appearing)</p>
</blockquote>
<p>I don't understand this one. Is there another name for <code>g.to_equiv.inv_fun</code>?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690712):
<p>It's <code>g⁻¹</code>!</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690856):
<p>You can put <code>show {x : X | conj g f x ≠ x} = {b : X | f (g⁻¹ b) ≠ g⁻¹ b}</code> on line 196 if you like...</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690867):
<p>but you are complaining about the congr?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690884):
<p>You want to prove two sets are equal and you don't want to use congr then funext?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690933):
<p>No I don't complain about congr and funext</p>

#### [ Patrick Massot (Apr 05 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691006):
<p>I don't complain at all actually, I try to learn</p>

#### [ Patrick Massot (Apr 05 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691011):
<p>I mean I complain that I'm not yet learned</p>

#### [ Patrick Massot (Apr 05 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691014):
<p>but I don't complain to anybody but me</p>

#### [ Patrick Massot (Apr 05 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691037):
<p>I really don't understand Chris's proof at all</p>

#### [ Patrick Massot (Apr 05 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691080):
<p>I can't translate it into tactic mode</p>

#### [ Patrick Massot (Apr 05 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691084):
<p>Hence I cannot understand it</p>

#### [ Patrick Massot (Apr 05 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691093):
<p>I have a really hard time imagining people actually thinking like this (without first writing the tactic proof and then obfuscate it in term mode)</p>

#### [ Patrick Massot (Apr 05 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691107):
<p>I do believe you Chris, but my imagination is failing me</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691169):
<p>Your comments before the computation seem a bit superficial to me, in the sense that I would not care about any of them myself if they came up in my Lean work.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691173):
<p>But the computation is a more serious matter.</p>

#### [ Patrick Massot (Apr 05 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691188):
<p>The computation is the actual proof</p>

#### [ Patrick Massot (Apr 05 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691198):
<p>everything before the computation is distraction</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691262):
<p>oh wait</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691271):
<p>the computation</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691277):
<p>you write Prop = Prop?</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691280):
<p>There's no other way?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691283):
<p>yes I write Prop = Prop</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691287):
<p>Maybe iff would be better with props</p>

#### [ Patrick Massot (Apr 05 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691305):
<p>That's because we see sets as map from X to  Prop</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691316):
<p>oh</p>

#### [ Patrick Massot (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691372):
<p>So the goal is really Prop = Prop</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691379):
<p>eew</p>

#### [ Patrick Massot (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691384):
<p>because we use funext to get rid of X here</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691387):
<p>Ok so your question really is something else</p>

#### [ Patrick Massot (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691394):
<p>But of course on paper I would write iff</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691400):
<p>You want to show <code>{x | p x} = {x | q x}</code></p>

#### [ Patrick Massot (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691406):
<p>x is in this set iff .. iff .. iff ... done</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691409):
<p>I don't think you should use congr and then funext</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691420):
<p>yes</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691423):
<p>iff</p>

#### [ Patrick Massot (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691429):
<p>Remember <code>{x | p x}</code> is only syntactic sugar for <code>p</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691433):
<p>sure</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691441):
<p>but there are lemmas like sets X and Y are equal iff X subseteq Y and Y subseteq X</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691480):
<p>or whatever</p>

#### [ Chris Hughes (Apr 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691493):
<p><code>set.ext</code> is what you're talking about</p>

#### [ Patrick Massot (Apr 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691494):
<p>Sure, but here I can prove (on paper) direct equality</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691503):
<p>But you can't prove any of your intermediate steps!</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691510):
<p>So surely this is an indication that trying to prove p x = q x is a bad idea</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691585):
<p>I would use set.ext instead of congr, funext</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691590):
<p>and then try the calc with iff's</p>

#### [ Patrick Massot (Apr 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691592):
<p>indeed <code>apply set.ext</code> transforms the goal to iff</p>

#### [ Patrick Massot (Apr 05 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691606):
<p>But my sorry where there because I couldn't use <code>rw</code>, not because I was proving <code>p x = q x</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691686):
<p>So what happens if you use set.ext and then try to push the calc through? I can't pass the <code>rw show  ∀ b, (g.to_equiv).inv_fun b = g⁻¹ b, from  λ b, rfl,</code> line</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691689):
<p>because I don't really know what's going on</p>

#### [ Patrick Massot (Apr 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691752):
<p>I don't understand what you don't know</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691755):
<p>I have never seen congr_n in my life</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691758):
<p>I don't know what all this rw show business is all about</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691762):
<p>how is that different to just show</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691771):
<p>can you just write it for me?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691786):
<p><code>congr_n 1</code> is like <code>congr</code> but stops after one step instead of recursing</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691837):
<p>how do you get from not X iff not Y to X iff Y?</p>

#### [ Patrick Massot (Apr 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691841):
<p>if the goal is <code>f (a + b) = f (c + d)</code> and you <code>congr_n 1</code>, the new goal will be <code>a+b = c+d</code>. With <code>congr</code> it would become two random goals  like <code>a=c</code> and <code>b = d</code></p>

#### [ Patrick Massot (Apr 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691847):
<p>In this case <code>f</code> is <code>not</code></p>

#### [ Patrick Massot (Apr 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691922):
<p>By the way, I don't know how to get rid of these <code>not</code> once I go to iff instead of =</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691924):
<p>not_iff_not.2</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691942):
<p>but there's a catch...</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691945):
<p><code> ⊢ decidable (f (g⁻¹ x) = g⁻¹ x) </code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691946):
<p>so I hope you are only interested in decidable topological spaces...</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691947):
<p>;-)</p>

#### [ Andrew Ashworth (Apr 05 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691985):
<p>It's funny, as you saw with Adam, most people with a cs background start out in term mode</p>

#### [ Kevin Buzzard (Apr 05 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691993):
<p>most people with a maths background think lambda is a real number</p>

#### [ Andrew Ashworth (Apr 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692004):
<p>I think it's simply familiarity with functional programming concepts</p>

#### [ Andrew Ashworth (Apr 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692026):
<p>Once you spend enough time looking at term mode statements they really do become more understandable <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Patrick Massot (Apr 06 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692030):
<p>I just found it using <code>find</code>!</p>

#### [ Patrick Massot (Apr 06 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692079):
<p><code>#find (¬ _ ↔ ¬ _) ↔ (_ ↔ _)</code> does work!</p>

#### [ Patrick Massot (Apr 06 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692081):
<p><span class="emoji emoji-1f389" title="tada">:tada:</span> <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span></p>

#### [ Kevin Buzzard (Apr 06 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692096):
<p>I found it by guessing what it was called ;-)</p>

#### [ Patrick Massot (Apr 06 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692100):
<p>Now what is this <code>decidable</code> crap? I have <code>noncomputable theory
local attribute [instance] classical.prop_decidable</code> on top of my file</p>

#### [ Kevin Buzzard (Apr 06 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692101):
<p>Even the iff's need some work. I'm beginning to think you were better off with =. but I have to go now, childcare calls</p>

#### [ Patrick Massot (Apr 06 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692146):
<p>Why isn't it enough</p>

#### [ Patrick Massot (Apr 06 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692156):
<p>I need to sleep actually, I have a train to catch at an insane time tomorrow to go and give a talk about fuzzy maths in Köln</p>

#### [ Patrick Massot (Apr 06 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692190):
<p>and why this <code>decidable</code> stuff didn't come up in my <code>=</code> instead of iff stuff?</p>

#### [ Patrick Massot (Apr 06 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692239):
<p>Anyway, thank you very much for your help, and thank Chris to</p>

#### [ Patrick Massot (Apr 06 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692343):
<p>I have enough food for thought on the train</p>

#### [ Patrick Massot (Apr 06 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692361):
<p>Except that I would like to understand how to tell Lean I really don't care about the <code>decidable</code> metaphysics</p>

#### [ Patrick Massot (Apr 06 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692389):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> is there a global command to say everything should be assumed to have decidable equality?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124693410):
<p>Is your problem simply that g is not an element of perm X? What happens if you define fp to be the permutation underlying f and gp for g, then use lemmas about groups acting on sets?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124693620):
<p>All those iff statements are going to follow from standard lemmas about groups acting on sets. I have no idea if they're there already but that is surely the way to finish the job. Groups acting on sets should be in mathlib (I don't know if it's there already) and then all the lemmas should be proved in the same file and then you just apply them and you're home</p>

#### [ Mario Carneiro (Apr 06 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124702399):
<blockquote>
<p>is there a global command to say everything should be assumed to have decidable equality? </p>
</blockquote>
<p><code>local attribute [instance] classical.prop_decidable</code> should do that</p>

#### [ Patrick Massot (Apr 06 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703691):
<p>Hum. It turns out I can indeed use <code>apply_instance</code> in both cases. This is the first time I need this tactic in a context where I'm not using <code>example</code> to check whether an instance is working</p>

#### [ Patrick Massot (Apr 06 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703700):
<p>Do you understand why <code> apply not_iff_not.2,</code> can spawn those goals without trying <code>apply_instance</code>?</p>

#### [ Mario Carneiro (Apr 06 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703801):
<p>What's the context?</p>

#### [ Mario Carneiro (Apr 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703841):
<p>Also, you should probably use <code>not_congr</code> instead, which doesn't have those extra assumptions</p>

#### [ Mario Carneiro (Apr 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703844):
<p>I'm currently working on doing what I can with your file</p>

#### [ Mario Carneiro (Apr 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703849):
<p>I don't think <code>aux_1</code> is true without assuming <code>f</code> and <code>g</code> are two-sided inverses</p>

#### [ Mario Carneiro (Apr 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703851):
<div class="codehilite"><pre><span></span>lemma aux_1 {α : Type*} {β : Type*} {f : α → β} {g : β → α}
  (h₁ : function.left_inverse g f) (h₂ : function.right_inverse g f)
  (p : α → Prop) : f &#39;&#39; {a : α | p a} = {b : β | p (g b)} :=
set.ext $ λ b, mem_image_iff_of_inverse h₁ h₂
</pre></div>

#### [ Mario Carneiro (Apr 06 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703946):
<p>This works for supp_conj:</p>
<div class="codehilite"><pre><span></span>lemma supp_conj (f g : homeo X X) : supp (conj g f : homeo X X) = g &#39;&#39; supp f :=
</pre></div>

#### [ Mario Carneiro (Apr 06 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705045):
<p>Here's a proof of supp_conj:</p>
<div class="codehilite"><pre><span></span>-- should be in equiv.lean
theorem equiv.left_inverse (f : α ≃ β) : left_inverse f.symm f := f.left_inv

theorem equiv.right_inverse (f : α ≃ β) : function.right_inverse f.symm f := f.right_inv

-- should be in homeos.lean
theorem homeo.left_inverse (f : homeo α β) : left_inverse f.symm f := f.left_inv

theorem homeo.right_inverse (f : homeo α β) : function.right_inverse f.symm f := f.right_inv

theorem homeo.bijective (f : homeo α β) : bijective f := f.to_equiv.bijective

@[simp] theorem aut_mul_val (f g : homeo α α) (x) : (f * g) x = f (g x) :=
homeo.comp_val _ _ _

@[simp] theorem aut_one_val (x) : (1 : homeo α α) x = x := rfl

@[simp] theorem aut_inv (f : homeo α α) : f⁻¹ = f.symm := rfl

lemma supp_conj (f g : homeo X X) : supp (conj g f : homeo X X) = g &#39;&#39; supp f :=
begin
  unfold supp,
  rw homeo.image_closure,
  congr_n 1,
  apply set.ext (λ x, _),
  rw mem_image_iff_of_inverse g.left_inverse g.right_inverse,
  apply not_congr,
  dsimp [conj],
  exact calc
     (g * f * g⁻¹) x = x
        ↔ g⁻¹ (g (f (g⁻¹ x))) = g⁻¹ x : by simp [(g⁻¹).bijective.1.eq_iff]
    ... ↔ (f (g⁻¹ x)) = g⁻¹ x : by rw [← aut_mul_val, mul_left_inv]; simp
end
</pre></div>

#### [ Patrick Massot (Apr 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705433):
<p>A million thanks!</p>

#### [ Patrick Massot (Apr 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705440):
<p>This looks very nice</p>

#### [ Patrick Massot (Apr 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705459):
<p>Right now I'm at the train station typing on my phone but I'll try this on the train</p>

#### [ Patrick Massot (Apr 06 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705561):
<p>Question about stuff you indicated as belonging to homeos.lean: are those restatements needed because of modeling mistakes I made or is it normal? I don't mind having them but I try to understand how to do things right.</p>

#### [ Mario Carneiro (Apr 06 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705616):
<p>It is normal. Since you have a <code>coe_fn</code> instance for homeo, the coercion there is not written by composing other coercions so you have to restate theorems about the underlying function if you want them as simp lemmas or projections</p>

#### [ Mario Carneiro (Apr 06 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705667):
<p>I put all the stuff together and PR'd it to your repo: <a href="https://github.com/PatrickMassot/lean-scratchpad/pull/1" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/pull/1">https://github.com/PatrickMassot/lean-scratchpad/pull/1</a></p>

#### [ Patrick Massot (Apr 06 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705762):
<p>Should I remove this coercion and have a coercion to equiv?</p>

#### [ Mario Carneiro (Apr 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705770):
<p>I think it is okay, especially if you expect it will get a lot of use. Otherwise the arrows can pile up</p>

#### [ Patrick Massot (Apr 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705945):
<p>Ok. Thank you very much</p>

#### [ Patrick Massot (Apr 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705948):
<p>I even managed to merge using the crappy train station wifi</p>

#### [ Mario Carneiro (Apr 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124706045):
<p>let me know if you want an explanation on something I did there</p>

#### [ Kevin Buzzard (Apr 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124714183):
<blockquote>
<p>I tried to describe my problems in <a href="#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243" title="#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243</a> without code, and then I posted link to my actual code. Then I tried to describe a simplified problem. I don't what I could do better to ask for help</p>
</blockquote>
<p>Write a MWE. I am much more inclined to look at code if I can just cut and paste it and it works first time. Git cloning and then downloading a new mathlib and building everything was a PITA and I couldn't possibly answer a question of the form "why does line 193 not work" without doing all that.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124714242):
<blockquote>
<p>I even managed to merge using the crappy train station wifi</p>
</blockquote>
<p>git is great for that isn't it.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124714355):
<blockquote>
<p>Should I remove this coercion and have a coercion to equiv?</p>
</blockquote>
<p>It seemed to me that one problem was you had coes from homeo to perm, from perm to fun and from homeo to fun. You had set it up so that the two maps from homeo to fun were definitionally equal (and if they weren't it would surely have been a nightmare) but even with definitional equality this didn't help with rw. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Can there be some version of rw which takes definitonal equality into account? i.e. "the user said rw (proof of X = Y) and I can't find X in the goal so I'll now start trying to find some term in the goal which is definitionally equal to X"?</p>

#### [ Chris Hughes (Apr 06 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124714443):
<p>I've read <code>erw</code> does that, but I've never managed to use it.</p>


{% endraw %}
