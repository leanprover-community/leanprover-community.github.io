---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29201zeroring.html
---

## Stream: [maths](index.html)
### Topic: [zero ring](29201zeroring.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 09 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613106):
<p>I'm working with polynomials and the zero ring is constantly a special case. There is a class <code>nonzero_comm_ring</code> extending comm_ring with the proposition that <code>0 \ne 1</code>, and several of Chris' results on polynomials need this as a hypothesis (for example the fact that degree of <code>X</code> is 1, and every corollary of this). Of course everything is true (and trivial) for the zero ring, but often the proofs need to be separate because of this. Because of the constructor for <code>nonzero_comm_ring</code> I am coming around to the idea to be splitting on <code>(0 : R) = 1</code> for lemmas which are true in the case R=0 but where the proof in the non-zero case is far from working for the zero ring.</p>
<p>So I now find myself wanting to prove things such as "if R is a ring and 0 = 1 then R is a fintype". I don't really know how to make that an instance, and I am not sure whether it should be an instance. On the other hand if I made a new class <code>zero_ring</code> then in some sense my life would be easier. Having said that, making a class for such a silly edge case seems a bit ridiculous. Should I just stick to proving lemmas rather than making this a class? I am slightly concerned that really I should be working with <code>zero_semiring</code> or something.</p>
<p>Another issue is that if I put <code>0 = 1 -&gt; fintype R</code> into <code>ring.lean</code> then I have to add an import to <code>ring.lean</code> and I have this vague worry that I don't really know "which comes first" out of rings and fintypes.</p>

#### [ Reid Barton (Sep 09 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613814):
<blockquote>
<p>"if R is a ring and 0 = 1 then R is a fintype"</p>
</blockquote>
<p>Is this a real example, including the <code>fintype</code> part?</p>

#### [ Reid Barton (Sep 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613889):
<p>Your <code>zero_ring</code> could be "lifted" all the way up to <code>is_singleton</code>, except we don't have it.</p>

#### [ Chris Hughes (Sep 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613892):
<p>Rings definitely come before <code>fintype</code>. A more useful instance would perhaps be <code>0 = 1 -&gt; subsingleton R</code></p>

#### [ Reid Barton (Sep 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613899):
<p>You can also use <code>subsingleton</code> in this case, yeah</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613915):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">ring</span><span class="bp">.</span><span class="n">zero_of_zero_eq_one</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">h01</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">one_mul</span> <span class="n">a</span><span class="o">,</span><span class="err">←</span><span class="n">h01</span><span class="o">,</span><span class="n">zero_mul</span><span class="o">]</span>

<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">ring</span><span class="bp">.</span><span class="n">fintype_of_zero_eq_one</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">h01</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">elems</span> <span class="o">:=</span> <span class="o">{</span><span class="mi">0</span><span class="o">},</span>
  <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">begin</span>
    <span class="n">suffices</span><span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">ring</span><span class="bp">.</span><span class="n">zero_of_zero_eq_one</span> <span class="n">h01</span> <span class="n">x</span><span class="o">,</span>
  <span class="kn">end</span>
<span class="o">}</span>

<span class="kn">theorem</span> <span class="n">ring</span><span class="bp">.</span><span class="n">is_noetherian_of_zero_eq_one</span> <span class="o">{</span><span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">h01</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_noetherian_ring</span> <span class="n">R</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">ring</span><span class="bp">.</span><span class="n">is_noetherian_of_fintype</span> <span class="n">R</span> <span class="n">R</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">ring</span><span class="bp">.</span><span class="n">fintype_of_zero_eq_one</span> <span class="n">h01</span>
</pre></div>

#### [ Reid Barton (Sep 09 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613971):
<p>Aha I see. I was wondering how you were using the <code>fintype</code>, but this makes sense.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133613973):
<p>I am trying to prove the Hilbert basis theorem for the zero ring :-)</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614007):
<p>I've proved that if a module is a fintype then it's Noetherian so I figured I'd use that.</p>

#### [ Reid Barton (Sep 09 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614049):
<p>So you could use case analysis on whether R is a subsingleton, and show that if it isn't then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>0</mn><mo>≠</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">0 \ne 1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.716em;"></span><span class="strut bottom" style="height:0.9309999999999999em;vertical-align:-0.215em;"></span><span class="base"><span class="mord mathrm">0</span><span class="mrel">≠</span><span class="mord mathrm">1</span></span></span></span>.<br>
Then also make an instance that says that if R is a subsingleton then so is R[X].</p>

#### [ Reid Barton (Sep 09 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614079):
<p>Or write a lemma <code>∀ R, subsingleton R ∨ ((0 : R) ≠ 1)</code></p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614109):
<p>I see. You're suggesting that I use what we currently have in the type class system by using a different class to convey what I'm trying to say, rather than making a new class. Thanks!</p>

#### [ Reid Barton (Sep 09 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614126):
<p>Well, I would actually prefer that you make a new class but that it should be called <code>is_singleton</code> :)</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614395):
<p>Hmm. <code>subsingleton</code> is a Prop. Does this mean that type class inference won't get me from it to <code>fintype</code>?</p>

#### [ Chris Hughes (Sep 09 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614443):
<p>Not computably.</p>

#### [ Chris Hughes (Sep 09 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133614459):
<p>It will for rings though</p>

#### [ Kevin Buzzard (Sep 09 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133615195):
<p>Proof now looks like</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">ring</span><span class="bp">.</span><span class="n">is_noetherian_of_zero_eq_one</span> <span class="o">{</span><span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">h01</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_noetherian_ring</span> <span class="n">R</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">ring</span><span class="bp">.</span><span class="n">subsingleton_of_zero_eq_one</span> <span class="n">h01</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">ring</span><span class="bp">.</span><span class="n">is_noetherian_of_fintype</span> <span class="n">R</span> <span class="n">R</span>
</pre></div>

#### [ Patrick Massot (Sep 12 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133793917):
<p>I read that Kevin fights the zero ring. But what's the point of allowing this ring? Why don't we defined a ring with the assumption that 0 and 1 are different? Is it a trick in order to totalize certain constructions? Or is it needed from a categorical point of view (I guess it's a terminal object)?</p>

#### [ Johan Commelin (Sep 12 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133793951):
<p>I've never thought this through carefully, but I think it is indeed useful from a categorical point of view.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133794730):
<p>Funnily enough in my undergraduate ring theory course the lecturer made 0 not= 1 an axiom, and it caused them all sorts of problems. Whenever they formed a quotient ring R / I I would put my hand up and point out that they needed to assume that I was not R (which was not a natural thing to do on many occasions). On the other hand I was only an undergraduate and just assumed that this was an axiom of rings. It was only when I learnt algebraic geometry that I found out that it wasn't. Assuming 0 isn't 1 is a disastrous idea. In a separated scheme, the intersection of two affines is affine -- this sort of thing is used all the time. It would not be true if the empty scheme were not affine.</p>

#### [ Patrick Massot (Sep 12 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133794785):
<p>The quotient case is one of the examples I had in mind when I wrote "totalizing construction". The same probably happens with localization</p>

#### [ Patrick Massot (Sep 12 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133794890):
<blockquote>
<p>and i̶t̶  Kevin caused them all sorts of problems</p>
</blockquote>

#### [ Mario Carneiro (Sep 12 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ring/near/133812772):
<p>of course, Kevin's behavior there is exactly what lean would do to you if you tried to formalize it</p>


{% endraw %}
