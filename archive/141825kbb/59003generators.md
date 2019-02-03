---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/59003generators.html
---

## Stream: [kbb](index.html)
### Topic: [generators](59003generators.html)

---


{% raw %}
#### [ Patrick Massot (Sep 12 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838138):
<p>I just saw Kenny's work on generating SL2Z. It looks impressive</p>

#### [ Patrick Massot (Sep 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838160):
<p>But I wonder how to properly generalize it.</p>

#### [ Kenny Lau (Sep 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838169):
<blockquote>
<p>I just saw Kenny's work on generating SL2Z. It looks impressive</p>
</blockquote>
<p>thanks!</p>

#### [ Patrick Massot (Sep 12 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838236):
<p>I would have expected to see a predicate saying: this set generate this group. And then a mechanism constructor the eliminator from this</p>

#### [ Patrick Massot (Sep 12 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838249):
<p>Is this counter-intuitive order related to constructivity?</p>

#### [ Kenny Lau (Sep 12 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838264):
<p>not constructivity</p>

#### [ Kenny Lau (Sep 12 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838278):
<p>it's just the same reason we don't take quot.exists_rep as an axiom, but rather quot.ind</p>

#### [ Patrick Massot (Sep 12 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838398):
<p>?</p>

#### [ Kenny Lau (Sep 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838466):
<p>it's easier to use</p>

#### [ Patrick Massot (Sep 12 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838826):
<p>Do you think there could be some tactic consuming a proof of generation and building the eliminator?</p>

#### [ Kenny Lau (Sep 12 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838930):
<p>I don't know about tactics</p>

#### [ Patrick Massot (Sep 12 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133838972):
<p>Maybe a tactic is not needed, I'm only trying to understand whether there could be an interface which looks more natural (to me at least)</p>

#### [ Patrick Massot (Sep 12 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839028):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you have any insight? We are discussing <a href="https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L49" target="_blank" title="https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L49">https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L49</a> and <a href="https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L97" target="_blank" title="https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L97">https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L97</a></p>

#### [ Mario Carneiro (Sep 12 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839676):
<div class="codehilite"><pre><span></span>protected theorem induction_on {C : SL2Z → Prop} (A : SL2Z)
  (H1 : C 1) (HS : ∀ B, C B → C (S * B))
  (HT : ∀ B, C B → C (T * B)) : C A :=
</pre></div>


<p>It's amazing how little this tells me</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839680):
<p>everything is letters</p>

#### [ Patrick Massot (Sep 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839695):
<p>S and T are explicit elements of SL2Z defined a few lines earlier</p>

#### [ Patrick Massot (Sep 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839707):
<p>So this theorem is a really weird way to state those elements generate SL2Z</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839714):
<p>there is an <code>SL2Z</code> attribute?</p>

#### [ Patrick Massot (Sep 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839766):
<p><a href="https://github.com/semorrison/kbb/blob/master/src/modular_group.lean#L6" target="_blank" title="https://github.com/semorrison/kbb/blob/master/src/modular_group.lean#L6">https://github.com/semorrison/kbb/blob/master/src/modular_group.lean#L6</a></p>

#### [ Mario Carneiro (Sep 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839773):
<p>seems like a fine induction statement</p>

#### [ Patrick Massot (Sep 12 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839785):
<p>Sure. But the question is: what is the proper general context and interface? Dealing with generating sets for groups</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839796):
<p>I don't think we have <code>span</code> for groups yet, I'm working on improving span for modules and we can do something similar in groups</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839840):
<p>I guess it's usually called closure in groups?</p>

#### [ Patrick Massot (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839844):
<p>I did spans for group a <em>very</em> long time ago</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839848):
<p>in mathlib?</p>

#### [ Patrick Massot (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839849):
<p>no</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839850):
<p>I think I recall</p>

#### [ Chris Hughes (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839853):
<p>I think closure is in mathlib</p>

#### [ Patrick Massot (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839856):
<p>It's the first thing I did</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839858):
<p>you were doing something with norms in groups</p>

#### [ Patrick Massot (Sep 12 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839885):
<p><a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/invariant_norms.lean#L107" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/invariant_norms.lean#L107">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/invariant_norms.lean#L107</a></p>

#### [ Mario Carneiro (Sep 12 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839888):
<p>But we don't need the general theory for this theorem, and it won't make the proof any easier</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839892):
<p>given what is currently available, this theorem is fine</p>

#### [ Patrick Massot (Sep 12 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839935):
<p>Yes. I was trying to formalize the trivial part of <a href="https://arxiv.org/abs/1803.07997" target="_blank" title="https://arxiv.org/abs/1803.07997">https://arxiv.org/abs/1803.07997</a></p>

#### [ Mario Carneiro (Sep 12 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839947):
<p>if and when we get spans in groups it would be natural to state <code>span {S, T} = top</code></p>

#### [ Kenny Lau (Sep 12 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133839970):
<p>guys, it's just closure</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840001):
<p>?</p>

#### [ Chris Hughes (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840002):
<p>From <code>subgroup.lean</code> </p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">in_closure</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">basic</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">in_closure</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:</span> <span class="n">in_closure</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="n">inv</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">in_closure</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">in_closure</span> <span class="n">a</span><span class="bp">⁻¹</span>
<span class="bp">|</span> <span class="n">mul</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">in_closure</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">in_closure</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">in_closure</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840007):
<p>It's not my question though: I would like to first prove the span is everything, and then deduce the eliminator, not the other way around</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840017):
<p>the proofs will be the same</p>

#### [ Patrick Massot (Sep 12 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840087):
<p>Even better then. We can write things like we do in maths and have the same proofs</p>

#### [ Mario Carneiro (Sep 12 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840112):
<p>ah, okay so you can write <code>closure {S, T} = univ</code></p>

#### [ Mario Carneiro (Sep 12 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840133):
<p>and the proof is to prove <code>in_closure {S, T}</code> by exactly the same induction argument as used in that big proof</p>

#### [ Patrick Massot (Sep 12 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840136):
<p>Mario, did you follow both links of the messages when I pinged you?</p>

#### [ Patrick Massot (Sep 12 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840151):
<p>The second linked line contains <code>closure {S, T} = univ</code></p>

#### [ Mario Carneiro (Sep 12 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840158):
<p>ah, so it does</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840236):
<p>However, the induction statement is a bit stronger than what you get from <code>closure</code></p>

#### [ Mario Carneiro (Sep 12 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840251):
<p>it says that <code>S</code> and <code>T</code> generate the group as a monoid</p>

#### [ Patrick Massot (Sep 12 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840253):
<p>My questions were: 1) could we directly prove <code>closure {S, T} = univ</code> without more pain (you seem to say yes) 2) could you generate the induction statement automatically from there?</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840273):
<p>there is no mention of inverses in the induction theorem</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840290):
<p>but in the closure of a group you need to also assume closure by inverses</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840314):
<p>so the real equivalent statement would be <code>monoid.closure {S, T} = univ</code></p>

#### [ Patrick Massot (Sep 12 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840371):
<p>Ok, let's assume we also define <code>monoid.closure</code>. How do we generate the eliminator?</p>

#### [ Patrick Massot (Sep 12 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840380):
<p>Would that be a tactic?</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840383):
<p>no, a theorem</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840392):
<p><code>monoid.closure</code> would be defined by an inductive type just like <code>in_closure</code> is</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840398):
<p>and its eliminator is basically exactly that theorem</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840409):
<p>You would prove that {x | C x} is a monoid containing <code>{S, T}</code> and so deduce it is <code>univ</code></p>

#### [ Patrick Massot (Sep 12 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840477):
<p>Would you need to redo that for every generating set of every group, or would you have a general theorem?</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840497):
<p>the general theorem <em>is</em> the eliminator for <code>in_closure</code></p>

#### [ Mario Carneiro (Sep 12 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133840526):
<p>the part that needs to be redone is the unfolding of the set <code>{S, T}</code> into two induction hypotheses about multiplying by <code>S</code> and <code>T</code></p>

#### [ Patrick Massot (Sep 12 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133841661):
<p>I tried to do the exercise, but clearly I missed something because it looks very complicated</p>

#### [ Patrick Massot (Sep 12 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133841998):
<p>I wrote, at the end of that file:</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">basic</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="n">mul</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span>


<span class="n">def</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="n">s</span> <span class="n">a</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">protected</span> <span class="kn">theorem</span> <span class="n">induction_on&#39;</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">SL2Z</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">SL2Z</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">C</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">HS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">S</span> <span class="bp">*</span> <span class="n">B</span><span class="o">))</span>
  <span class="o">(</span><span class="n">HT</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">T</span> <span class="bp">*</span> <span class="n">B</span><span class="o">))</span> <span class="o">:</span> <span class="n">C</span> <span class="n">A</span> <span class="o">:=</span>
<span class="k">begin</span>

  <span class="k">have</span> <span class="o">:</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="o">({</span><span class="n">S</span><span class="o">,</span> <span class="n">T</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">SL2Z</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">this</span> <span class="bp">_</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>The first sorry is irrelevant. But the tactic state after the first sorry is not what I was hoping for. I tried to move on but it looked too complicated to be what you suggested</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133842668):
<p>There is a theorem that <code>in_closure</code> can be generated by only left multiplication by the generators</p>

#### [ Mario Carneiro (Sep 12 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133842747):
<p>If you want it to be by definition, you will need the following definition for <code>monoid.in_closure</code></p>
<div class="codehilite"><pre><span></span>inductive monoid.in_closure (s : set α) : α → Prop
| one : monoid.in_closure 1
| mul_basic {a b : α} : a ∈ s → monoid.in_closure b → monoid.in_closure (a * b)
</pre></div>

#### [ Patrick Massot (Sep 12 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843061):
<p>Ok, thanks</p>

#### [ Patrick Massot (Sep 12 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843071):
<p>That theorem is indeed what I saw I needed to prove, and I was confused because it seemed to contradict the announced triviality</p>

#### [ Patrick Massot (Sep 12 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843094):
<p>With the stronger definition of <code>monoid.in_closure</code>, the new proof is</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">protected</span> <span class="kn">theorem</span> <span class="n">induction_on&#39;</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">SL2Z</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">SL2Z</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">C</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">HS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">S</span> <span class="bp">*</span> <span class="n">B</span><span class="o">))</span>
  <span class="o">(</span><span class="n">HT</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">T</span> <span class="bp">*</span> <span class="n">B</span><span class="o">))</span> <span class="o">:</span> <span class="n">C</span> <span class="n">A</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span> <span class="o">({</span><span class="n">S</span><span class="o">,</span> <span class="n">T</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">SL2Z</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">this</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">A</span> <span class="n">B</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="bp">;</span> <span class="n">intro</span> <span class="n">h</span> <span class="bp">;</span> <span class="n">finish</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Sep 12 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843118):
<p>which looks like it could admit a general version</p>

#### [ Patrick Massot (Sep 12 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843177):
<p>Now, I need to go to bed, but I'll probably come back to all this tomorrow</p>

#### [ Patrick Massot (Sep 12 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133843182):
<p>Thanks again!</p>

#### [ Johan Commelin (Sep 13 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860592):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> A really cool way to generalise this is to apply this strategy to the action of <code>SL2Z</code> on matrices with determinant <code>m</code>. You get the same sort of "Euclidean algorithm"-like induction steps. The end result is that you prove that every matrix is equivalent to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mtable><mtr><mtd><mstyle displaystyle="false" scriptlevel="0"><mrow><mi>a</mi></mrow></mstyle></mtd><mtd><mstyle displaystyle="false" scriptlevel="0"><mrow><mi>b</mi></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle displaystyle="false" scriptlevel="0"><mrow><mn>0</mn></mrow></mstyle></mtd><mtd><mstyle displaystyle="false" scriptlevel="0"><mrow><mi>d</mi></mrow></mstyle></mtd></mtr></mtable><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\begin{pmatrix} a &amp; b \\ 0 &amp; d \end{pmatrix}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:1.45em;"></span><span class="strut bottom" style="height:2.40003em;vertical-align:-0.95003em;"></span><span class="base"><span class="minner"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size3">(</span></span><span class="mord"><span class="mtable"><span class="col-align-c"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.45em;"><span style="top:-3.61em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathit">a</span></span></span><span style="top:-2.4099999999999997em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathrm">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.9500000000000004em;"></span></span></span></span><span class="arraycolsep" style="width:0.5em;"></span><span class="arraycolsep" style="width:0.5em;"></span><span class="col-align-c"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.45em;"><span style="top:-3.61em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathit">b</span></span></span><span style="top:-2.4099999999999997em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathit">d</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.9500000000000004em;"></span></span></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size3">)</span></span></span></span></span></span>, where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mo>⋅</mo><mi>d</mi><mo>=</mo><mi>m</mi><mo separator="true">,</mo><mspace width="1em"></mspace><mi>a</mi><mo>&gt;</mo><mn>0</mn><mo separator="true">,</mo><mspace width="1em"></mspace><mi>d</mi><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">a \cdot d = m,\quad a &gt; 0,\quad d &gt; 0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">a</span><span class="mbin">⋅</span><span class="mord mathit">d</span><span class="mrel">=</span><span class="mord mathit">m</span><span class="mpunct">,</span><span class="mord mathit"><span class="mspace quad"></span><span class="mord mathit">a</span></span><span class="mrel">&gt;</span><span class="mord mathrm">0</span><span class="mpunct">,</span><span class="mord mathit"><span class="mspace quad"></span><span class="mord mathit">d</span></span><span class="mrel">&gt;</span><span class="mord mathrm">0</span></span></span></span>, and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>0</mn><mo>≤</mo><mi>b</mi><mo>&lt;</mo><mi>d</mi></mrow><annotation encoding="application/x-tex">0 \le b &lt; d</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.83041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathrm">0</span><span class="mrel">≤</span><span class="mord mathit">b</span><span class="mrel">&lt;</span><span class="mord mathit">d</span></span></span></span>.</p>

#### [ Johan Commelin (Sep 13 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860598):
<p>In particular, the set of orbits is finite.</p>

#### [ Johan Commelin (Sep 13 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860606):
<p>If you apply this to the case <code>m = 1</code> you recover the result that <code>S</code> and <code>T</code> generate <code>SL2Z</code>.</p>

#### [ Johan Commelin (Sep 13 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860657):
<p>Once we know this set is finite for arbitrary <code>m : int</code>, then we can define Hecke operators!</p>

#### [ Johan Commelin (Sep 13 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133860676):
<p>I think that would be a really cool move.</p>

#### [ Johan Commelin (Sep 13 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865425):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> What do you think of this?</p>

#### [ Kenny Lau (Sep 13 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865474):
<p>great!</p>

#### [ Johan Commelin (Sep 13 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865482):
<p>How hard do you think it is to adapt your proof?</p>

#### [ Kenny Lau (Sep 13 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865538):
<p>maybe 30% hard!</p>

#### [ Kenny Lau (Sep 13 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865539):
<p>can't wait to see someone implement it!</p>

#### [ Johan Commelin (Sep 13 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865541):
<p>Lol</p>

#### [ Johan Commelin (Sep 13 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865606):
<p>Do we have notation for group actions?</p>

#### [ Kenny Lau (Sep 13 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865720):
<p>I used <code>\ci</code> a long time ago</p>

#### [ Johan Commelin (Sep 13 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865802):
<p>But it is not in mathlib?</p>

#### [ Kenny Lau (Sep 13 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865874):
<p>it isn't</p>

#### [ Johan Commelin (Sep 13 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865918):
<p>Hmm, so I generalised the simp lemmas a bit. Now I need to cook up a new induction statement.</p>

#### [ Johan Commelin (Sep 13 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133865931):
<p>Should <code>C 1</code> be replaced by the explicit representatives that I described above?</p>

#### [ Kenny Lau (Sep 13 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866151):
<p>sure</p>

#### [ Johan Commelin (Sep 13 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866338):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Does this look good?</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="kn">theorem</span> <span class="n">induction_on</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="o">(</span><span class="n">Mat</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">d</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h3</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">h4</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h5</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="n">d</span><span class="o">),</span> <span class="n">C</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">b</span><span class="o">,</span><span class="mi">0</span><span class="o">,</span><span class="n">d</span><span class="o">,</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h1</span><span class="o">]</span><span class="bp">⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="n">HS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="n">B</span><span class="o">))</span> <span class="o">(</span><span class="n">HT</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span> <span class="n">B</span><span class="o">))</span> <span class="o">:</span> <span class="n">C</span> <span class="n">A</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866356):
<p>what if m is negative?</p>

#### [ Kenny Lau (Sep 13 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866357):
<p>or 0?</p>

#### [ Johan Commelin (Sep 13 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866417):
<p>Hmm, good point, I guess I should drop my requirement on <code>d</code>.</p>

#### [ Johan Commelin (Sep 13 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866422):
<p>Let me think it through...</p>

#### [ Johan Commelin (Sep 13 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866507):
<p>For <code>m = 0</code> the statement might be false.</p>

#### [ Johan Commelin (Sep 13 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866514):
<p>You have matrices <code>(a, 0, 0, 0)</code>. And I think they are not sharing orbits, are they?</p>

#### [ Johan Commelin (Sep 13 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866572):
<p>So I drop <code>h3</code>, and <code>h5</code> becomes <code>b &lt; (abs d)</code>.</p>

#### [ Johan Commelin (Sep 13 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866862):
<p>What is the general strategy to kill this goal:</p>
<div class="codehilite"><pre><span></span><span class="n">H</span> <span class="o">:</span> <span class="n">C</span> <span class="o">{</span><span class="n">a</span> <span class="o">:=</span> <span class="n">B</span><span class="bp">.</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">B</span><span class="bp">.</span><span class="n">b</span><span class="o">,</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">B</span><span class="bp">.</span><span class="n">c</span><span class="o">,</span> <span class="n">d</span> <span class="o">:=</span> <span class="n">B</span><span class="bp">.</span><span class="n">d</span><span class="o">,</span> <span class="n">det</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">}</span>
<span class="err">⊢</span> <span class="n">C</span> <span class="n">B</span>
</pre></div>

#### [ Johan Commelin (Sep 13 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133866866):
<p><code>exact H</code> doesn't work. Somehow I'dd like to prove it by some extensionality or something.</p>

#### [ Patrick Massot (Sep 13 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867094):
<p>Did you try convert H ?</p>

#### [ Kenny Lau (Sep 13 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867109):
<p><code>cases B; exact H</code></p>

#### [ Patrick Massot (Sep 13 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867838):
<p>Kenny's solution is more efficient. But I think it's still good to keep in mind that <code>convert H, cases B, congr</code> works</p>

#### [ Patrick Massot (Sep 13 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867881):
<p>Because <code>convert H</code> is a natural thing to try when <code>exact H</code> refuses to work</p>

#### [ Kenny Lau (Sep 13 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867887):
<p>I disagree</p>

#### [ Kenny Lau (Sep 13 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867892):
<p><code>congr</code> can go uncontrollable</p>

#### [ Kenny Lau (Sep 13 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867893):
<p>(<code>convert</code> is just a kind of <code>congr</code>)</p>

#### [ Patrick Massot (Sep 13 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867908):
<p>I'm not saying this will always work</p>

#### [ Kenny Lau (Sep 13 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867912):
<p>I'm saying we shouldn't make <code>convert</code> our "first resort"</p>

#### [ Kenny Lau (Sep 13 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133867952):
<p>for lack of a better word</p>

#### [ Johan Commelin (Sep 13 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133868391):
<p>Here is what I've got so far</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">protected</span> <span class="kn">theorem</span> <span class="n">induction_on</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="o">(</span><span class="n">Mat</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">d</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h3</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h4</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">d</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">≤</span> <span class="bp">-</span><span class="n">d</span><span class="o">),</span> <span class="n">C</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">b</span><span class="o">,</span><span class="mi">0</span><span class="o">,</span><span class="n">d</span><span class="o">,</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h1</span><span class="o">]</span><span class="bp">⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="n">HS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="n">B</span><span class="o">))</span> <span class="o">(</span><span class="n">HT</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span> <span class="n">B</span><span class="o">))</span> <span class="o">:</span> <span class="n">C</span> <span class="n">A</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">hSid</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="n">B</span><span class="o">))))</span> <span class="bp">=</span> <span class="n">B</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">B</span><span class="o">,</span> <span class="k">by</span> <span class="n">ext</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">SL2Z_M_</span><span class="o">],</span>
<span class="k">have</span> <span class="n">HS&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="n">B</span><span class="o">)</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">B</span><span class="o">,</span>
  <span class="k">from</span> <span class="bp">λ</span> <span class="n">B</span> <span class="n">ih</span><span class="o">,</span> <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="o">(</span><span class="n">HS</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">HS</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">HS</span> <span class="bp">_</span> <span class="n">ih</span><span class="o">),</span> <span class="k">by</span> <span class="n">rwa</span> <span class="n">hSid</span> <span class="n">B</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
<span class="k">have</span> <span class="n">hTinv</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="n">B</span><span class="o">))))))</span> <span class="bp">=</span> <span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span><span class="bp">⁻¹</span> <span class="n">B</span><span class="o">,</span>
  <span class="k">from</span> <span class="bp">λ</span> <span class="n">B</span><span class="o">,</span> <span class="k">by</span> <span class="n">repeat</span> <span class="o">{</span><span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)]}</span><span class="bp">;</span> <span class="n">congr</span><span class="o">,</span>
<span class="k">have</span> <span class="n">HT&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span><span class="bp">⁻¹</span> <span class="n">B</span><span class="o">),</span>
  <span class="k">from</span> <span class="bp">λ</span> <span class="n">B</span> <span class="n">ih</span><span class="o">,</span> <span class="k">by</span> <span class="o">{</span><span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="o">(</span><span class="n">HS</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">HS</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">HS</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">HT</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">HS</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">HT</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">HS</span> <span class="bp">_</span> <span class="n">ih</span><span class="o">),</span> <span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="n">hTinv</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">},</span>
<span class="c1">-- have HT2 : ∀ n : ℤ, C (T^n),</span>
<span class="c1">--   from λ n, int.induction_on n H1</span>
<span class="c1">--     (λ i ih, by rw [add_comm, gpow_add]; from HT _ ih)</span>
<span class="c1">--     (λ i ih, by rw [sub_eq_neg_add, gpow_add]; from HT1 _ ih),</span>
<span class="k">have</span> <span class="n">HT3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span> <span class="n">B</span><span class="o">)</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">B</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">B</span> <span class="n">ih</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">HT&#39;</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span> <span class="n">B</span><span class="o">)</span> <span class="n">ih</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">simp</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">one</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">H</span>
  <span class="kn">end</span><span class="o">,</span>
<span class="k">have</span> <span class="n">HT4</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span><span class="bp">⁻¹</span> <span class="n">B</span><span class="o">)</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">B</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">B</span> <span class="n">ih</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">HT</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">T</span><span class="bp">⁻¹</span> <span class="n">B</span><span class="o">)</span> <span class="n">ih</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">simp</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">one</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">H</span>
  <span class="kn">end</span><span class="o">,</span>
<span class="k">have</span> <span class="n">HT5</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">B</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">),</span> <span class="n">C</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="o">(</span><span class="n">T</span><span class="err">^</span><span class="n">n</span><span class="o">)</span> <span class="n">B</span><span class="o">)</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">B</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">B</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">int</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">n</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">gpow_zero</span><span class="o">,</span> <span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">one</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)]</span><span class="bp">;</span> <span class="k">from</span> <span class="n">id</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="n">ih1</span> <span class="n">ih2</span><span class="o">,</span> <span class="n">ih1</span> <span class="err">$</span> <span class="n">HT3</span> <span class="bp">_</span> <span class="err">$</span> <span class="k">begin</span>
      <span class="n">conv</span> <span class="o">{</span> <span class="n">congr</span><span class="o">,</span> <span class="n">rw</span> <span class="err">←</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)</span> <span class="o">},</span>
      <span class="n">conv</span> <span class="n">at</span> <span class="n">ih2</span> <span class="o">{</span> <span class="n">congr</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="n">add_comm</span><span class="o">,</span> <span class="n">gpow_add</span><span class="o">,</span> <span class="n">gpow_one</span><span class="o">]</span> <span class="o">},</span>
      <span class="n">assumption</span> <span class="kn">end</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="n">ih1</span> <span class="n">ih2</span><span class="o">,</span> <span class="n">ih1</span> <span class="err">$</span> <span class="n">HT4</span> <span class="bp">_</span> <span class="err">$</span> <span class="k">begin</span>
      <span class="n">conv</span> <span class="o">{</span> <span class="n">congr</span><span class="o">,</span> <span class="n">rw</span> <span class="err">←</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)</span> <span class="o">},</span>
      <span class="n">conv</span> <span class="n">at</span> <span class="n">ih2</span> <span class="o">{</span> <span class="n">congr</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="n">sub_eq_neg_add</span><span class="o">,</span> <span class="n">gpow_add</span><span class="o">,</span> <span class="n">gpow_neg_one</span><span class="o">]</span> <span class="o">},</span>
      <span class="n">assumption</span> <span class="kn">end</span><span class="o">),</span>
</pre></div>

#### [ Patrick Massot (Sep 13 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133868669):
<p>Isn't it even more contrived to prove first the induction lemma in that case?</p>

#### [ Johan Commelin (Sep 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133868818):
<p>I don't know. But if we want Hecke operators, we need it.</p>

#### [ Patrick Massot (Sep 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133868845):
<p>Why don't you want to state the result you need in the way you would state it on paper, and then deduce the induction statement?</p>

#### [ Patrick Massot (Sep 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133869045):
<p>Is there an available written proof you are trying to follow?</p>

#### [ Johan Commelin (Sep 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133869613):
<p>No, I just cooked up a proof this morning.</p>

#### [ Johan Commelin (Sep 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133869619):
<p>There are probably proofs around, but I haven't found one yet.</p>

#### [ Patrick Massot (Sep 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133869714):
<p>Do you need help here?</p>

#### [ Johan Commelin (Sep 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870014):
<p>I'm learning <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Johan Commelin (Sep 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870584):
<p>I've pushed a proof that has 1 <code>sorry</code> for the case <code>A.c = 0</code>.</p>

#### [ Johan Commelin (Sep 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870594):
<p>I still need to learn how to juggle around hypotheses.</p>

#### [ Johan Commelin (Sep 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870643):
<p>A mathematician says: Ooh, if <code>A.a ≤ 0</code> then replace <code>A</code> by <code>-A</code>. I find it hard to make such a step in Lean.</p>

#### [ Johan Commelin (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870668):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Do you want to teach me?</p>

#### [ Patrick Massot (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870692):
<p>where did you push?</p>

#### [ Kenny Lau (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870698):
<p>well <code>S*S*A = -A</code></p>

#### [ Kenny Lau (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870707):
<p>so you prove it for <code>S*S*A</code> first</p>

#### [ Johan Commelin (Sep 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870708):
<p>Fail... I only commited. Now I pushed.</p>

#### [ Johan Commelin (Sep 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870763):
<p>I have <code>hneg : ∀ (B : Mat m), SL2Z_M_ m S (SL2Z_M_ m S B) = -B</code> in my context</p>

#### [ Patrick Massot (Sep 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870798):
<p>I also see <code>n n : ℕ,</code> which is a good recipe for confusion</p>

#### [ Johan Commelin (Sep 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870954):
<p>That is because of the <code>strong_induction</code></p>

#### [ Johan Commelin (Sep 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870981):
<p>I don't understand why <code>strong_induction</code> does this, but we could safely forget about the first <code>n</code>. It has played it's role, and the new <code>n</code> took over.</p>

#### [ Patrick Massot (Sep 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133870997):
<p>Why don't you use another name for the new <code>n</code>?</p>

#### [ Patrick Massot (Sep 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133871066):
<p>Anyway, I can't help with this sorry without knowing what is the paper proof</p>

#### [ Johan Commelin (Sep 13 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133871215):
<p>Never mind. I might have found a way out.</p>

#### [ Johan Commelin (Sep 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133876350):
<p>I did find a way out, but it is becoming pretty crazy. (I also had lunch. Please don't be worried that I kept banging my head against this wall for 3 hours.)</p>

#### [ Johan Commelin (Sep 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133876357):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Would you want to take over?</p>

#### [ Kenny Lau (Sep 13 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133876502):
<p>I’m not free now</p>

#### [ Johan Commelin (Sep 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133879346):
<p>There are 3 <code>sorry</code>s left in <a href="https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L118-L125" target="_blank" title="https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L118-L125">https://github.com/semorrison/kbb/blob/master/src/SL2Z_generators.lean#L118-L125</a>,</p>

#### [ Johan Commelin (Sep 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133879350):
<p>they should all be <code>by schoolkid</code>.</p>

#### [ Patrick Massot (Sep 13 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133886099):
<p>Let's say I try the first one</p>

#### [ Johan Commelin (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887384):
<p>Ooh, I was just trying that one.</p>

#### [ Patrick Massot (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887395):
<p>I'm almost there!</p>

#### [ Johan Commelin (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887396):
<p>I just finished a maths paper. So I am allowing myself some Lean time.</p>

#### [ Johan Commelin (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887413):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I only need <code>1 ≤ A.d * A.d</code></p>

#### [ Patrick Massot (Sep 13 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887417):
<p>I'm at <code>this : A.d * A.d &gt; 0
⊢ A.d * A.d - 1 ≥ 0</code></p>

#### [ Johan Commelin (Sep 13 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887434):
<p>Right, same place (-;</p>

#### [ Johan Commelin (Sep 13 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887447):
<p>I'll move to sorry₂</p>

#### [ Patrick Massot (Sep 13 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887464):
<p>Oh no, for Lean it's not the same place</p>

#### [ Patrick Massot (Sep 13 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133887759):
<p>I'm soo close <code>this : A.d * A.d &gt; 0 ⊢ 1 ≤ A.d * A.d</code></p>

#### [ Patrick Massot (Sep 13 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888301):
<p>Done!</p>

#### [ Patrick Massot (Sep 13 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888383):
<p>Should I move to the third one?</p>

#### [ Johan Commelin (Sep 13 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888446):
<p>Yes please.</p>

#### [ Johan Commelin (Sep 13 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888450):
<p>Did you push?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888471):
<p>Do you want me to push?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888556):
<p>I pushed</p>

#### [ Johan Commelin (Sep 13 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888816):
<p>This should be a standard lemma: <code>A.b / A.d * A.d ≤ A.b</code> But I can't find it...</p>

#### [ Patrick Massot (Sep 13 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888868):
<p>What is this <code>/</code>? Euclidean quotient?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133888951):
<p>seems so</p>

#### [ Johan Commelin (Sep 13 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889038):
<p>Right, so <code>(11 / (-3)) = -3</code></p>

#### [ Rob Lewis (Sep 13 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889145):
<p><code>int.div_mul_le</code>? Are you working over <code>int</code>? I'm not really following the context.</p>

#### [ Patrick Massot (Sep 13 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889184):
<p>bingo!</p>

#### [ Patrick Massot (Sep 13 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889768):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Are you sure this sorry is true?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889783):
<p>It actually looks really weird</p>

#### [ Johan Commelin (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889898):
<p>I'm done with 2</p>

#### [ Johan Commelin (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889907):
<p>You're worried about 3?</p>

#### [ Patrick Massot (Sep 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133889911):
<p>yes</p>

#### [ Johan Commelin (Sep 13 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890106):
<p>Hmm, I think it is fine. Proof by example: <code>abs (101 - (101/13 * 13)) ≤ abs(13)</code>, which reduces to <code>10 ≤ 13</code>.</p>

#### [ Johan Commelin (Sep 13 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890209):
<p>By the way, I pushed my fix of sorry₂</p>

#### [ Patrick Massot (Sep 13 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890585):
<p>hold on</p>

#### [ Patrick Massot (Sep 13 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890611):
<p>You sent me on a wrong track to make sure you'll be done first!</p>

#### [ Johan Commelin (Sep 13 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890810):
<p>Guess what, I have to catch a train. So I won't be Leaning for the next 90 minutes.</p>

#### [ Patrick Massot (Sep 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890829):
<p>And now you set me a deadline!</p>

#### [ Johan Commelin (Sep 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890833):
<p>And I haven't made any progress on sorry₃</p>

#### [ Johan Commelin (Sep 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890842):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> is online <span class="emoji emoji-23f3" title="time ticking">:time_ticking:</span></p>

#### [ Kenny Lau (Sep 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133890852):
<p>hi</p>

#### [ Patrick Massot (Sep 13 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133893902):
<p>done</p>

#### [ Patrick Massot (Sep 13 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133893911):
<p>so much suffering...</p>

#### [ Johan Commelin (Sep 13 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898166):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Thank you so much!</p>

#### [ Patrick Massot (Sep 13 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898533):
<p>The stupid lemma in the middle is now in mathlib</p>

#### [ Patrick Massot (Sep 13 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898624):
<p>I also removed a couple of simp that were in the middle of the proof hence frowned upon</p>

#### [ Johan Commelin (Sep 13 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898828):
<p>Ok, I realised that it might have been easier to assume <code>m &gt; 0</code>. And then deduce the result for negative <code>m</code> via an <code>SL2Z</code>-equivariant isom between <code>Mat m</code> and <code>Mat -m</code>.</p>

#### [ Johan Commelin (Sep 13 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898847):
<p>Anyway, the next step would be to use this horrible lemma to prove that for <code>m ≠ 0</code> the set of orbits of <code>SL2Z_M_</code> is finite.</p>

#### [ Johan Commelin (Sep 13 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133898860):
<p>Once we have that, we can define the Hecke operator.</p>

#### [ Johan Commelin (Sep 13 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133905932):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Are you interested in golfing what we came up with?</p>

#### [ Kenny Lau (Sep 13 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133905941):
<p>after I finish with my PR</p>

#### [ Patrick Massot (Sep 13 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133906100):
<p>Which PR?</p>

#### [ Kenny Lau (Sep 13 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133906246):
<p><a href="https://github.com/leanprover/mathlib/pull/345" target="_blank" title="https://github.com/leanprover/mathlib/pull/345">https://github.com/leanprover/mathlib/pull/345</a></p>

#### [ Patrick Massot (Sep 13 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133906679):
<p>Nice!</p>

#### [ Patrick Massot (Sep 13 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133912059):
<p>I made a small start on SL2Z\SL2ZM, simply telling Lean what this mean, and somehow stating what I think Johan told us we should prove in order to get finiteness</p>

#### [ Patrick Massot (Sep 13 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133912075):
<p>But what is stated may be false</p>

#### [ Patrick Massot (Sep 13 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133912087):
<p>and the names are stupid too</p>

#### [ Johan Commelin (Sep 14 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133922532):
<p>Thanks! That is exactly what I had in mind. (I do think we might need a bit more conditions in <code>reps</code>. I think we can/should just copy the condition from <code>H0</code> in the induction lemma.</p>

#### [ Johan Commelin (Sep 14 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133922587):
<p>The set of orbits is only finite if <code>m ≠ 0</code>. Otherwise it is parameterised by pairs of coprime integers (up to ±1).</p>

#### [ Patrick Massot (Sep 14 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133937043):
<p>Done</p>

#### [ Patrick Massot (Sep 14 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133937107):
<p>Note that a small modification of the setup is required to recover the generation theorem for SL2. The relevant action is not the action of the full SL2 on Mat m, but only the monoid spanned by S and T. But otherwise the proof should be the same</p>

#### [ Johan Commelin (Sep 14 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133937363):
<p>Cool!</p>

#### [ Johan Commelin (Sep 14 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133937413):
<p>I guess for the finiteness result that is still sorried, we could do the dual thing. Build an injection into a product of <code>fin</code>s.</p>

#### [ Kenny Lau (Sep 14 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938572):
<p>are we going to restate the SL2Z theorem as a special case?</p>

#### [ Kenny Lau (Sep 14 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938580):
<p>also, it doesn't compile because someone deleted mul_self_pos</p>

#### [ Patrick Massot (Sep 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938658):
<p>It does compile</p>

#### [ Patrick Massot (Sep 14 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938662):
<p><code>mul_self_pos</code> is now in mathlib</p>

#### [ Patrick Massot (Sep 14 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938669):
<p>Did you try to compile using <code>leanpkg build</code>? (hint: the correct answer is yes)</p>

#### [ Patrick Massot (Sep 14 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938729):
<p>Yes, we could restate the SL2Z theorem as a special case. It should cost much and will be convenient</p>

#### [ Patrick Massot (Sep 14 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938734):
<p>Feel free to do so, I need to do real work now</p>

#### [ Kenny Lau (Sep 14 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133938801):
<blockquote>
<p><code>mul_self_pos</code> is now in mathlib</p>
</blockquote>
<p>well I haven't updated mathlib, that's why</p>

#### [ Patrick Massot (Sep 14 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133939553):
<p>leanpkg will do that for you</p>

#### [ Patrick Massot (Sep 14 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133939561):
<p>Use leanpkg build</p>

#### [ Johan Commelin (Sep 14 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133939915):
<p>And restart Lean in VScode afterwards...</p>

#### [ Kenny Lau (Sep 14 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971124):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  you see... I might change your proof if you don't mind</p>

#### [ Johan Commelin (Sep 14 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971164):
<p>I just pushed a first start on hecke operators...</p>

#### [ Johan Commelin (Sep 14 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971202):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Please assume <code>m &gt; 0</code></p>

#### [ Kenny Lau (Sep 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971249):
<p>what do you mean</p>

#### [ Johan Commelin (Sep 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971264):
<p>It will probably make your life easier. And I now realise that we won't ever use <code>m &lt; 0</code></p>

#### [ Johan Commelin (Sep 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971274):
<p>Not in this project.</p>

#### [ Kenny Lau (Sep 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971281):
<p>oh well</p>

#### [ Johan Commelin (Sep 14 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971297):
<p>And outside the project, the can deduce the result by an <code>SL2Z</code>-equivariant map <code>Mat m → Mat -m</code></p>

#### [ Kenny Lau (Sep 14 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971327):
<p>right</p>

#### [ Patrick Massot (Sep 14 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971438):
<blockquote>
<p>Patrick Massot  you see... I might change your proof if you don't mind</p>
</blockquote>
<p>I have no idea what you are talking about</p>

#### [ Kenny Lau (Sep 14 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971446):
<p>your whole induction_on proof</p>

#### [ Patrick Massot (Sep 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971559):
<p>It's not my proof, I only contributed a handful of schoolkid lines</p>

#### [ Kenny Lau (Sep 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971567):
<p>oh, <span class="user-mention" data-user-id="112680">@Johan Commelin</span> then</p>

#### [ Johan Commelin (Sep 14 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133971673):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Sure, go ahead!</p>

#### [ Kenny Lau (Sep 14 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133972834):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> this is the original base case:</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="n">h0</span> <span class="o">:</span> <span class="n">A</span><span class="bp">.</span><span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">A</span><span class="bp">.</span><span class="n">a</span> <span class="bp">*</span> <span class="n">A</span><span class="bp">.</span><span class="n">d</span> <span class="bp">=</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">A</span><span class="bp">.</span><span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h3</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">A</span><span class="bp">.</span><span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h4</span> <span class="o">:</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="n">A</span><span class="bp">.</span><span class="n">b</span> <span class="bp">≤</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="n">A</span><span class="bp">.</span><span class="n">d</span><span class="o">),</span> <span class="n">C</span> <span class="n">A</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133972846):
<p>it can be changed to:</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="n">h0</span> <span class="o">:</span> <span class="n">A</span><span class="bp">.</span><span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">A</span><span class="bp">.</span><span class="n">a</span> <span class="bp">*</span> <span class="n">A</span><span class="bp">.</span><span class="n">d</span> <span class="bp">=</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">A</span><span class="bp">.</span><span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">h3</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">A</span><span class="bp">.</span><span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h4</span> <span class="o">:</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="n">A</span><span class="bp">.</span><span class="n">b</span> <span class="bp">&lt;</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="n">A</span><span class="bp">.</span><span class="n">d</span><span class="o">),</span> <span class="n">C</span> <span class="n">A</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Sep 14 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133972966):
<p>1) <code>h1</code> is redundant. It follows from <code>h0</code> and <code>A.det</code>. (I realised this half-way writing my own proof.)<br>
2) Now you have no upper-bound on <code>A.b</code>. So how will you prove finiteness of orbits?</p>

#### [ Kenny Lau (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973018):
<p>what do you mean I have no upper-bound on A.b?</p>

#### [ Kenny Lau (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973037):
<p>I changed two <code>le</code> to <code>lt</code></p>

#### [ Kenny Lau (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973041):
<p>it restricted things</p>

#### [ Johan Commelin (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973056):
<p>Aah, sorry, I didn't see the <code>h4</code>.</p>

#### [ Johan Commelin (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973068):
<p>Yes, I know you could make those restrictions, but I didn't know if it would make the proof easier.</p>

#### [ Johan Commelin (Sep 14 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973071):
<p>I thought things would get harder.</p>

#### [ Kenny Lau (Sep 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/generators/near/133973178):
<p>I always do more work to ensure that the users do less work</p>


{% endraw %}
