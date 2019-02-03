---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40085Inferringsetoidinstances.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Inferring setoid instances](https://leanprover-community.github.io/archive/113488general/40085Inferringsetoidinstances.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Jul 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129811730):
<p>I've had a bit of trouble with setoid instances in quotient rings and groups. Changes the brackets around <code>setoid</code> in <code>quotient.induction_on</code> and similar lemmas form <code>[]</code> to <code>{}</code> improves matters a lot. Is there a downside to this approach? There should always only be one possibility for <code>setoid</code> from the type of <code>q</code> right?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
  <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">β</span> <span class="err">⟦</span><span class="n">a</span><span class="err">⟧</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="n">q</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">q</span> <span class="n">h</span>
</pre></div>

#### [ Reid Barton (Jul 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812715):
<p>I have also thought the same thing "why not just infer the relation based on the type of <code>q</code>".</p>

#### [ Reid Barton (Jul 17 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812730):
<p>I'm guessing you have a type (like, a group) on which you have a relation that depends on some other variable (like, a subgroup) which isn't mentioned in the carrier type?</p>

#### [ Reid Barton (Jul 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812795):
<p>I also found these type class arguments annoying to deal with in this kind of situation, although I don't remember what I did about it.<br>
It's possible that switching to a different elaboration strategy fixed my problem, and I didn't look into exactly why.</p>

#### [ Reid Barton (Jul 17 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812897):
<p>Or maybe I just used <code>quot</code> methods instead. <a href="#narrow/stream/113488-general/topic/elab_as_eliminator" title="#narrow/stream/113488-general/topic/elab_as_eliminator">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elab_as_eliminator</a></p>

#### [ Reid Barton (Jul 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129812930):
<p>Yes, now I remember wondering whether mixing <code>quotient</code> with <code>quot.induction_on</code> was a sensible thing to do, and then I saw that TPIL does the same thing in the section on quotients.</p>

#### [ Chris Hughes (Jul 17 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129814544):
<p>I'm not sure what you mean by carrier type, but basically it's struggling to find the setoid instances for the standard relation for quotienting by an ideal. It's particularly bad when I have two ideals in my context, but at the moment I only have one and it's still struggling.</p>

#### [ Chris Hughes (Jul 17 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815018):
<p>Deleting my instance for preimage of a ring_hom is an ideal helps, even though my lemma has nothing to do with preimages or ring_homs.</p>

#### [ Reid Barton (Jul 17 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815052):
<p>By carrier I mean the type that you're putting an equivalence relation on.</p>

#### [ Reid Barton (Jul 17 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815143):
<p>in this case, (the underlying type of) the ring</p>

#### [ Reid Barton (Jul 17 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815513):
<p>The equivalence relation here depends on the ideal I, which cannot be inferred from the ring or from instance synthesis.<br>
Basically, when you have an instance which has non-typeclass variables to the left of the colon which don't also appear to the right of the colon, I don't see how Lean can ever select the instance by type class inference.</p>

#### [ Patrick Massot (Jul 17 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129815620):
<p>We certainly don't want Lean to guess which ideal we want to quotient. And one can always add local setoid instances if we have a whole section of file where the ideal is fixed.</p>

#### [ Chris Hughes (Jul 17 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129816521):
<p>@pat</p>
<blockquote>
<p>We certainly don't want Lean to guess which ideal we want to quotient. And one can always add local setoid instances if we have a whole section of file where the ideal is fixed.</p>
</blockquote>
<p>Not actually that easy to add a local attribute that depends on a variable.</p>

#### [ Patrick Massot (Jul 17 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836199):
<p>I see Mario merged your PR (before anyone added your name to the authors list). Did you solve your instance issue?</p>

#### [ Mario Carneiro (Jul 17 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836266):
<p>oops</p>

#### [ Chris Hughes (Jul 17 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836295):
<p>Not really. I think in general we shouldn't be using type class inference for quotient rings and groups, and maybe we need some infrastructure to deal with that, like a whole load of new quotient lemmas. But I'm not sure. I usually find a way round it, but it's a constant nuisance</p>

#### [ Kevin Buzzard (Jul 17 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836545):
<p>Here's another type class inference issue which Keji pointed out to me:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">subgroup</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">is_subgroup</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">set</span> <span class="n">G</span><span class="o">)</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">H1</span><span class="o">]</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">H2</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_subgroup</span> <span class="o">(</span><span class="n">H1</span> <span class="err">∩</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">inv_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span> <span class="n">Hyp</span><span class="o">,</span><span class="bp">⟨</span><span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="n">Hyp</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="n">Hyp</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>

<span class="o">}</span>
</pre></div>


<p>-&gt;</p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
G : Type,
_inst_1 : group G,
H1 H2 : set G,
_inst_2 : is_subgroup H1,
_inst_3 : is_subgroup H2
⊢ is_submonoid (H1 ∩ H2)
</pre></div>


<p>I just wanted to populate the fields of the structure but I couldn't figure out an easy way to do so without proving <code>is_submonoid (H1 ∩ H2)</code> first and making it an instance</p>

#### [ Kevin Buzzard (Jul 17 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836549):
<p>Is there a way round this?</p>

#### [ Patrick Massot (Jul 17 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129836743):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">set</span> <span class="n">G</span><span class="o">)</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">H1</span><span class="o">]</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">H2</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_subgroup</span> <span class="o">(</span><span class="n">H1</span> <span class="err">∩</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine_struct</span> <span class="o">{</span><span class="bp">..</span><span class="o">},</span>
  <span class="n">sorry</span><span class="o">,</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>state after first line looks good to me</p>

#### [ Chris Hughes (Jul 17 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837625):
<blockquote>
<p>I just wanted to populate the fields of the structure but I couldn't figure out an easy way to do so without proving <code>is_submonoid (H1 ∩ H2)</code> first and making it an instance</p>
</blockquote>
<p>It's probably good practice to make <code>inter.is_submonoid</code> an instance first anyway.</p>

#### [ Kevin Buzzard (Jul 17 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837657):
<p>Yeah but I was teaching.</p>

#### [ Kevin Buzzard (Jul 17 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837666):
<p>I just wanted it to look relatively easy. In the end I re-defined is_subgroup (and didn't import it)</p>

#### [ Patrick Massot (Jul 18 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837913):
<p>Full proof could be either</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">set</span> <span class="n">G</span><span class="o">)</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">H1</span><span class="o">]</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">H2</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_subgroup</span> <span class="o">(</span><span class="n">H1</span> <span class="err">∩</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">one_mem</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span> <span class="n">H1</span><span class="o">,</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span> <span class="n">H2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">a_in</span> <span class="n">b_in</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">a_in</span><span class="bp">.</span><span class="mi">1</span> <span class="n">b_in</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">a_in</span><span class="bp">.</span><span class="mi">2</span> <span class="n">b_in</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">inv_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span> <span class="n">Hyp</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="n">Hyp</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="n">Hyp</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span> <span class="o">}</span>
</pre></div>


<p>or</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">set</span> <span class="n">G</span><span class="o">)</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">H1</span><span class="o">]</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">H2</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_subgroup</span> <span class="o">(</span><span class="n">H1</span> <span class="err">∩</span> <span class="n">H2</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine_struct</span> <span class="o">{</span><span class="bp">..</span><span class="o">},</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span> <span class="n">H1</span><span class="o">,</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span> <span class="n">H2</span><span class="bp">⟩</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">a_in</span> <span class="n">b_in</span><span class="o">,</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">a_in</span><span class="bp">.</span><span class="mi">1</span> <span class="n">b_in</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">a_in</span><span class="bp">.</span><span class="mi">2</span> <span class="n">b_in</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">g</span> <span class="n">Hyp</span><span class="o">,</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="n">Hyp</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="n">Hyp</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>depending whether you want to get tactical or not. I'm not sure I understand your question</p>

#### [ Patrick Massot (Jul 18 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129837927):
<p>The teaching advantage of the tactical way is what I showed in my first answer: Lean tells you want it wants, even putting names on questions</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838009):
<p>I'm going to make a rather radical suggestion and suggest that perhaps <code>subgroup G</code> should be a type on its own, like <code>filter</code></p>

#### [ Kevin Buzzard (Jul 18 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838032):
<p>I am surprised the first one works! With no structure fields just the <code>{}</code> Lean complains it has no <code>inv_mem</code> and that type class inference fails to prove <code>is_submonoid</code>. I hadn't expected that just declaring the fields anyway would work.</p>

#### [ Kevin Buzzard (Jul 18 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838104):
<p>In particular Lean doesn't put all names on questions -- you have to look at what <code>is_submonoid</code> wants -- but that's not too hard.</p>

#### [ Patrick Massot (Jul 18 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838122):
<p>Did you try my suggestion with three <code>sorry</code>?</p>

#### [ Patrick Massot (Jul 18 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838129):
<p>The crucial part is Simon's <code>refine_struct</code> tactic</p>

#### [ Patrick Massot (Jul 18 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838188):
<p>Mario, do you mean bundling the subset and its properties?</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838197):
<p>yes, and adding a <code>has_mem</code> instance and so on</p>

#### [ Chris Hughes (Jul 18 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838198):
<p>How does that solve the <code>setoid</code> problem?</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838200):
<p>what setoid?</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838244):
<p>it solves the typeclass inference problem</p>

#### [ Patrick Massot (Jul 18 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838246):
<p>he wants quotients by subgroups</p>

#### [ Chris Hughes (Jul 18 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838247):
<p>The problem about inferrinf <code>setoid</code> instances for quotient groups and rings.</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838248):
<p>example?</p>

#### [ Chris Hughes (Jul 18 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838266):
<p>I don't have an MWE right now, but having two subgroups around means it uses the wrong one sometimes.</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838337):
<p>I don't mean MWE, just sketch the problem. I don't see how two quotient groups with different subgroups can be confused</p>

#### [ Chris Hughes (Jul 18 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838361):
<p>It always tries to use the setoid instance with the subgroup which comes last in the statement of the theorem.</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838410):
<p>why are you inferring a setoid instance?</p>

#### [ Reid Barton (Jul 18 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838430):
<p>Because the setoid argument to <code>quotient.induction_on</code> is a <code>[]</code> argument for some reason</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838483):
<p>you could use <code>quot.induction_on</code>...</p>

#### [ Chris Hughes (Jul 18 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838552):
<p>What do you suggest in place of <code>quotient.mk</code>?</p>

#### [ Chris Hughes (Jul 18 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838565):
<p>And there's no <code>quot.lift_on₂</code></p>

#### [ Mario Carneiro (Jul 18 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838568):
<p><code>quot.mk</code> of course</p>

#### [ Chris Hughes (Jul 18 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838612):
<p>Then I have a really long expression.</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838619):
<p>You usually want to make custom versions of all these anyway</p>

#### [ Chris Hughes (Jul 18 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838620):
<p>A <code>has_coe</code> instance seems like a sensible substitute.</p>

#### [ Chris Hughes (Jul 18 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838634):
<p>How about <code>quotient.exact</code>?</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838685):
<p>You can always use <code>@</code> if you like the <code>quotient</code> version</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/129838695):
<p>just put <code>(id _)</code> in the typeclass slot and it will unify for it instead of use typeclass inference</p>

#### [ Chris Hughes (Jul 20 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/130011028):
<p>I had a go at following Mario's recommendation and not using type class inference for setoids for quotient groups. I wanted to find a solution that made it easy, and initially it wasn't. <br>
I used the follwing definitions</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">quotients</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">φ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">{</span><span class="n">s₁</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">s₂</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">s₃</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">γ</span><span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">,</span> <span class="kn">reducible</span><span class="o">]</span>
<span class="n">def</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on&#39;</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₁</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">φ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">r</span> <span class="n">α</span> <span class="n">s₁</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">φ</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on</span> <span class="n">q</span> <span class="n">f</span> <span class="n">h</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">,</span> <span class="kn">reducible</span><span class="o">]</span>
<span class="n">def</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on₂&#39;</span> <span class="o">(</span><span class="n">q₁</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₁</span><span class="o">)</span> <span class="o">(</span><span class="n">q₂</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₂</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a₁</span> <span class="n">a₂</span> <span class="n">b₁</span> <span class="n">b₂</span><span class="o">,</span> <span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">r</span> <span class="n">α</span> <span class="n">s₁</span> <span class="n">a₁</span> <span class="n">b₁</span> <span class="bp">→</span> <span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">r</span> <span class="n">β</span> <span class="n">s₂</span> <span class="n">a₂</span> <span class="n">b₂</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a₁</span> <span class="n">a₂</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">b₁</span> <span class="n">b₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">γ</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on₂</span> <span class="n">q₁</span> <span class="n">q₂</span> <span class="n">f</span> <span class="n">h</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">lemma</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on&#39;</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₁</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₁</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">p</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">s₁</span><span class="bp">.</span><span class="mi">1</span> <span class="n">a</span><span class="o">))</span> <span class="o">:</span> <span class="n">p</span> <span class="n">q</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">q</span> <span class="n">h</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">lemma</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂&#39;</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₁</span> <span class="bp">→</span> <span class="n">quotient</span> <span class="n">s₂</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">q₁</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₁</span><span class="o">)</span>
  <span class="o">(</span><span class="n">q₂</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₂</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a₁</span> <span class="n">a₂</span><span class="o">,</span> <span class="n">p</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">s₁</span><span class="bp">.</span><span class="mi">1</span> <span class="n">a₁</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="n">β</span> <span class="n">s₂</span> <span class="n">a₂</span><span class="o">))</span> <span class="o">:</span> <span class="n">p</span> <span class="n">q₁</span> <span class="n">q₂</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">q₁</span> <span class="n">q₂</span> <span class="n">h</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">lemma</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₃&#39;</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₁</span> <span class="bp">→</span> <span class="n">quotient</span> <span class="n">s₂</span> <span class="bp">→</span> <span class="n">quotient</span> <span class="n">s₃</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
  <span class="o">(</span><span class="n">q₁</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₁</span><span class="o">)</span> <span class="o">(</span><span class="n">q₂</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₂</span><span class="o">)</span> <span class="o">(</span><span class="n">q₃</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">s₃</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a₁</span> <span class="n">a₂</span> <span class="n">a₃</span><span class="o">,</span> <span class="n">p</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">s₁</span><span class="bp">.</span><span class="mi">1</span> <span class="n">a₁</span><span class="o">)</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">s₂</span><span class="bp">.</span><span class="mi">1</span> <span class="n">a₂</span><span class="o">)</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">s₃</span><span class="bp">.</span><span class="mi">1</span> <span class="n">a₃</span><span class="o">))</span> <span class="o">:</span> <span class="n">p</span> <span class="n">q₁</span> <span class="n">q₂</span> <span class="n">q₃</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₃</span> <span class="n">q₁</span> <span class="n">q₂</span> <span class="n">q₃</span> <span class="n">h</span>

<span class="kn">end</span> <span class="n">quotients</span>
</pre></div>


<p>Using these definitions everything was easy. They differ from the library definitions in two ways, the absence of the <code>elab_strategy</code> attribute, not sure what this does, but it makes stuff harder for some reason, and the use of <code>{}</code> instead of <code>[]</code> for setoids. Using <code>quot</code> versions of these lemmas has two problems, one is the <code>elab_strategy</code> attribute, and the other is that <code>quot.lift_on₂</code> as well as <code>quot.exact</code> are not provable without the relations being equivalence relations.</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Inferring%20setoid%20instances/near/130014064):
<p>Hm, this sounds like reason enough to PR these theorems. (Since we all know that mathlib is collecting patches of core lean theorems.) I actually have no idea what the <code>elab_strategy</code> attribute does, I've never heard of it</p>


{% endraw %}
