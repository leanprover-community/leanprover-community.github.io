---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67981quotients.html
---

## Stream: [general](index.html)
### Topic: [quotients](67981quotients.html)

---


{% raw %}
#### [ Patrick Massot (Jul 15 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129697433):
<p>I still don't know much about quotients in Lean. I have the goal <code>{x : completion α × completion α | (g x.1, g x.2) ∈ r} ∈ uniformity.sets</code>. And <code>completion α</code> is the quotient of something, and <code>g</code> is induced by <code>h</code> defined before quotienting. So I'd like to rewrite the left hand side as the image under <code>lam y, (quotient.mk y.1,  quotient.mk y.2)</code> of the obvious set where  <code>(g x.1, g x.2)</code> becomes <code>(h y.1, h y.2)</code>. How can I do that? Should I do that?</p>

#### [ Chris Hughes (Jul 15 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698784):
<p>I proved it, but it's not pretty. I think there's a demand for more advanced versions of cases which can deal with quotients, bound variables, and things like turning <code>f : α → β × β</code> to <code>f₁ f₂ : α → β</code>.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">s</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">β</span> <span class="bp">×</span> <span class="n">β</span><span class="o">))</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">Hh</span> <span class="o">:</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">∘</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s</span> <span class="bp">×</span> <span class="n">quotient</span> <span class="n">s</span> <span class="bp">|</span> <span class="o">(</span><span class="n">g</span> <span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">g</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="err">∈</span> <span class="n">r</span><span class="o">}</span> <span class="bp">=</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="err">⟦</span><span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="err">⟧</span><span class="o">,</span> <span class="err">⟦</span><span class="n">a</span><span class="bp">.</span><span class="mi">2</span><span class="err">⟧</span><span class="o">))</span> <span class="err">&#39;&#39;</span> <span class="o">((</span><span class="bp">λ</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="n">h</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">h</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">Hh</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span>
  <span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">a₁</span><span class="o">,</span> <span class="n">a₂</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">a₁</span> <span class="n">a₂</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">a₁</span> <span class="n">a₂</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">a₁</span><span class="o">,</span> <span class="n">a₂</span><span class="o">),</span> <span class="n">h</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="bp">⟨⟨</span><span class="n">b₁</span><span class="o">,</span> <span class="n">b₂</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h₁</span><span class="o">,</span> <span class="n">h₂</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">show</span> <span class="o">(</span><span class="n">g</span> <span class="n">a₁</span><span class="o">,</span> <span class="n">g</span> <span class="n">a₂</span><span class="o">)</span> <span class="err">∈</span> <span class="n">r</span><span class="o">,</span> <span class="k">from</span>
    <span class="k">have</span> <span class="n">h₃</span> <span class="o">:</span> <span class="err">⟦</span><span class="n">b₁</span><span class="err">⟧</span> <span class="bp">=</span> <span class="n">a₁</span> <span class="bp">∧</span> <span class="err">⟦</span><span class="n">b₂</span><span class="err">⟧</span> <span class="bp">=</span> <span class="n">a₂</span> <span class="o">:=</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h₂</span><span class="o">,</span>
     <span class="n">h₃</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">▸</span> <span class="n">h₃</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">▸</span> <span class="n">h₁</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Jul 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698842):
<p><code>induction</code> for quotients is a feature I want in lean 4</p>

#### [ Chris Hughes (Jul 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698851):
<p>There's no reason why it can't be done in lean 3 is there?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698890):
<p>I'm not sure how replicable <code>induction</code> is</p>

#### [ Chris Hughes (Jul 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698894):
<p>Is it C++?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698895):
<p>mostly</p>

#### [ Chris Hughes (Jul 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698897):
<p>Isn't it just basically <code>revert, refine quotient.induction_on _ _, intros</code></p>

#### [ Chris Hughes (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698941):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">qindunction</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">texpr</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">types</span><span class="bp">.</span><span class="n">using_ident</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">e</span> <span class="err">←</span> <span class="n">to_expr</span> <span class="n">p</span><span class="o">,</span>
<span class="n">revert_kdependencies</span> <span class="n">e</span><span class="o">,</span>
<span class="n">refine</span> <span class="bp">``</span><span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="err">%%</span><span class="n">e</span> <span class="bp">_</span><span class="o">),</span>
<span class="n">intro</span> <span class="n">n</span><span class="o">,</span>
<span class="bp">`</span><span class="o">[</span><span class="n">intros</span><span class="o">]</span>
</pre></div>

#### [ Kevin Buzzard (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698945):
<p>Here's a really dumb question about quotients. It seems to me that instead of using the quotient type one could just use an inductive type: the quotient of <code>X</code> by <code>r</code> could be <code>{x : set X // I am an equivalence class}</code> and the facts about quotients that don't come for free in type theory could be added as axioms about this subtype. Why is it not done this way?</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698949):
<p>Then quotients would be easier to think about</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698951):
<p>Sure, you can do that</p>

#### [ Chris Hughes (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698953):
<p>Computablity perhaps?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698954):
<p>some facts need the axiom of choice</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698955):
<p>and it's not data when you do that</p>

#### [ Chris Hughes (Jul 15 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698961):
<p>It's very nice to have the definitional reduction of <code>quotient.lift</code></p>

#### [ Mario Carneiro (Jul 15 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698962):
<p>You can't get that with any construction</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699003):
<p>and that adds real power - <code>funext</code> is <em>proven using quotients</em></p>

#### [ Patrick Massot (Jul 15 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699004):
<p>Thank you very much Chris!</p>

#### [ Patrick Massot (Jul 15 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699006):
<p>I hope I'll be able to use that.</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699009):
<p>In fact, I highly recommend reading the proof of <code>funext</code>. It's quite the mind bender</p>

#### [ Patrick Massot (Jul 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699018):
<p>This is explained in TPIL</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699021):
<p>It's really not obvious why you can't use set-quotients to do the same proof</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699022):
<p>oh my goodness Chris is posting meta code. How things move on! Two weeks ago he was asking me what a monad was.</p>

#### [ Patrick Massot (Jul 15 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699068):
<p>Kevin, I don't understand why you'd want this set-theoretic construction. I actually spend quite a lot of time explaining to my students that this construction is a lie. What matter about quotients are the axioms enforced in Lean.</p>

#### [ Patrick Massot (Jul 15 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699086):
<p>To me the set theoretic quotient is the same level of lie as the Kuratowski pair definition</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699088):
<p>But an obvious question with that is why quotients and not other things?</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699127):
<p>Oh that's an interesting comment Patrick. The truth of the matter was that I was watching a school play with one of my kids in, which turned out to be over three hours long, and so I spent most of the last 90 minutes thinking about other ways of doing quotients in my head in the dark</p>

#### [ Patrick Massot (Jul 15 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699144):
<p>Mario, I'm not sure what is "that" in your latest message</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699157):
<p>Why do quotients get an axiomatic definition but, say, real numbers don't?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699207):
<p>is there a sense in which lean's type formers are "complete" with quotients but not without?</p>

#### [ Patrick Massot (Jul 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699212):
<p>I think most people in France teach the set-theoretic quotient and never explicitly say it's a lie. Students are expected to magically understand what really matters</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699213):
<blockquote>
<p>In fact, I highly recommend reading the proof of <code>funext</code>. It's quite the mind bender</p>
</blockquote>
<p>Funnily enough I tried this only recently, when I realised that I was going to have to learn how to use quotients. </p>
<p>I have been writing about "the three basic kinds of types", trying to explain them to mathematicians. All this came from my trying to figure out why there were three basic kinds of types at all -- inductive types and pi types sure, and now quotients -- why can't we just do them with inductive types? In some sense Patrick's comments are quite a good answer to this -- I am now thinking that the construction I've known all my working life is just a hack.</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699224):
<p>That's actually a good question - why are quotients not an inductive type?</p>

#### [ Patrick Massot (Jul 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699225):
<p>and I think almost no university seriously teaches the construction of real numbers</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699267):
<p>Quotients as sets of sets is the ZFC construction of the object which has the right universal property.</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699268):
<p>HoTT has an interesting answer to this: they are a "higher inductive type"</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699270):
<p>The point is that in type theory, set-quotients do not have the right universal property</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699274):
<p>?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699278):
<p>They lack the computation rule</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699280):
<p>which one is that?</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699281):
<p><code>lift f (mk a) = f a</code></p>

#### [ Chris Hughes (Jul 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699321):
<p>It is true, but not <code>rfl</code></p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699323):
<p>"lack" :-)</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699325):
<p>because in type theory <em>definitional equality matters</em></p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699326):
<p>Yes!</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699333):
<p>I understand this much better than I did a few months ago. Perhaps this is obvious to CS people. I think it really needs to be spelt out to mathematicians.</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699334):
<p>HoTT is of course all about exploring the nontrivial structure of equality, where definitional equality is the equalest equal</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699372):
<p>All equalities are equal, but some are more equal than others.</p>

#### [ Patrick Massot (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699375):
<p>Kevin, did you read the first chapter of the HoTT book?</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699376):
<p>no</p>

#### [ Patrick Massot (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699377):
<p>You should</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699380):
<p>It's a really good intro to dependent type theory</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699381):
<p>Thanks. I'm always looking for new things to read, even though reading is so 1990s</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699387):
<p>My kids don't read anything.</p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699390):
<p>They just google</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699393):
<p>Also you will find some decent material on HITs there</p>

#### [ Patrick Massot (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699394):
<p><a href="http://saunders.phil.cmu.edu/book/hott-online.pdf" target="_blank" title="http://saunders.phil.cmu.edu/book/hott-online.pdf">http://saunders.phil.cmu.edu/book/hott-online.pdf</a></p>

#### [ Mario Carneiro (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699395):
<p>HoTT has some much more exotic HITs than quotients</p>

#### [ Mario Carneiro (Jul 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699437):
<p>like "the circle" <code>S1</code>, which is "inductively generated" by <code>base : S1</code> and <code>loop : base = base</code></p>

#### [ Mario Carneiro (Jul 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699441):
<p>In HoTT you can prove that <code>loop</code> is not <code>rfl</code></p>

#### [ Kevin Buzzard (Jul 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699448):
<p>In HoTT can you define the notion of a finite set? Can you use the axiom of choice?</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699451):
<p>You can do pretty much everything in classical math</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699504):
<p>You have to state the axiom of choice carefully to be consistent with univalence (lean's <code>choice</code> is not consistent with univalence), but it is a reasonable interpretation of ZFC-esque axiom of choice</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699511):
<p>it's not provable though, it's an axiom</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699552):
<p>there are more details in the HoTT book for how the axiom of choice works</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699553):
<p>it uses the "propositional truncation" as a substitute for the <code>Prop</code> universe</p>

#### [ Patrick Massot (Jul 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699558):
<p>I was not referring to all this. I really mean Chapter one, about type theory, only slightly biased towards exotic stuff that will follow</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699602):
<p>Yes, of course that's more advanced material and more HoTT-y stuff</p>

#### [ Kevin Buzzard (Jul 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699604):
<p>I know you weren't Patrick, but I mentioned to my old university set theory teacher that I was now doing type theory and he asked me if it was HoTT and if so then could I define a finite set (because he'd heard that it was problematic)</p>

#### [ Kevin Buzzard (Jul 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699605):
<p>and I told him that it wasn't and that I had no idea about his question</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699618):
<p>If you are specifically interested in finite sets in HoTT, I've had a conversation with Floris on that exact topic (he's our resident expert)</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699658):
<p>Constructively, there are a few variations on what "finite" means</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699660):
<p>The simplest is something isomorphic to fin n</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699665):
<p>If we call that one "finite", then "subfinite" means a subset of a finite set</p>

#### [ Kevin Buzzard (Jul 15 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699667):
<p>and equality is undecidable...</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699702):
<p>and then there is an image of a finite set (I forget what this is called), and a subset of an image of a finite set</p>

#### [ Kevin Buzzard (Jul 15 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699707):
<p>If I assume AC and propext then all these are the same, right?</p>

#### [ Patrick Massot (Jul 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699708):
<p>Forget about HoTT Kevin, it's all constructive</p>

#### [ Patrick Massot (Jul 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699713):
<p>We have maths to do instead</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699717):
<p>With LEM, you know that the subset is decidable so subfinite and finite are the same</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699753):
<p>for images, I guess you can get a section out using AC so that becomes the same as finite too</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699764):
<p>I don't think you need propext for anything</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699765):
<p>Actually unique choice might be enough for the section thing, since it's a finite choice</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699782):
<p>Oh yeah, there's another gradation: "isomorphic to fin n" or "merely isomorphic to fin n"</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699822):
<p>where "merely" is a HoTT adjective meaning "in Prop" basically</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699825):
<p>that's like the difference between "fintype" and "finite" in lean</p>

#### [ Kevin Buzzard (Jul 15 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700080):
<blockquote>
<p>You can do pretty much everything in classical math</p>
<p>Forget about HoTT Kevin, it's all constructive</p>
</blockquote>
<p>?</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700138):
<p>It's very constructivity-aware, even if there are some classical axioms that are admissible</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700141):
<p>Lean's choice axiom is much more heavy handed</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700150):
<p>It's comparable to the status of equality reflection as a type theory axiom</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700190):
<p>lean doesn't have it, and as a result you have to do all these casts and things</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700193):
<p>if you have equality reflection then it is much more like working in ZFC, where typing is just a provable property like any other</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700242):
<p>So even though you can do everything in ZFC in lean, stuff that really doesn't respect types gets messy in lean</p>

#### [ Mario Carneiro (Jul 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700243):
<p>(I don't know how helpful this is as an analogy)</p>

#### [ Reid Barton (Jul 15 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129701773):
<p>For inducting on quotients, isn't there <code>induction _ using quot.ind</code>?</p>

#### [ Johan Commelin (Sep 26 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134662694):
<p>Currently there is <code>quotient_module.quotient</code> and <code>quotient_ring.quotient</code>. They are both defined in terms of <code>_root_.quotient</code>. To me it would make sense to define a <code>quotient_ring</code> as a <code>quotient_module</code> and then add the extra algebraic structure.</p>

#### [ Johan Commelin (Sep 26 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134662711):
<p>Is there a reason why this is not a good idea?</p>

#### [ Patrick Massot (Sep 26 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665140):
<p>Mario is working on module quotient: <a href="https://www.twitch.tv/videos/314424360" target="_blank" title="https://www.twitch.tv/videos/314424360">https://www.twitch.tv/videos/314424360</a></p>

#### [ Patrick Massot (Sep 26 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665214):
<p>It's exactly how I imagined Mario doing Lean before meeting him in Orsay</p>

#### [ Patrick Massot (Sep 26 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665218):
<p>No, wait!</p>

#### [ Patrick Massot (Sep 26 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665227):
<p>It seems that first thing was actually a trailer for the Venom movie</p>

#### [ Patrick Massot (Sep 26 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665228):
<p>Now I can see emacs</p>

#### [ Johan Commelin (Sep 26 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665632):
<p>Too bad I'm on a train... I don't think they want me to stream twitch over the train wifi</p>

#### [ Kevin Buzzard (Sep 26 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665660):
<p>The Dutch have free WiFi on every train in the country and then just moan about how slow it is ;-)</p>

#### [ Johan Commelin (Sep 26 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665783):
<p>I'm in Germany now. But yes, there is pretty good wifi coverage on the high speed trains in NL, DE, and FR</p>

#### [ Johan Commelin (Sep 26 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665798):
<p>I don't have experience with other countries</p>


{% endraw %}
