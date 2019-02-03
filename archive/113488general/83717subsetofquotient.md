---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83717subsetofquotient.html
---

## Stream: [general](index.html)
### Topic: [subset of quotient](83717subsetofquotient.html)

---


{% raw %}
#### [ Johan Commelin (Oct 01 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956599):
<p>For the perfectoid project we often need to work with subsets of quotient types. A mathematician would write</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foobar</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">QuotType</span> <span class="bp">|</span> <span class="n">formula</span> <span class="n">x</span><span class="o">}</span>
</pre></div>


<p>and afterwards bother with the proof obligation of showing that it is well-defined. Can we mimic this in Lean?<br>
I imagine that this subset notation would call the appropriate <code>lift</code> lemma, and generate a proof obligation that we can prove after the subset notation. Something like</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foobar</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">QuotType</span> <span class="bp">|</span> <span class="n">formula</span> <span class="n">x</span><span class="o">}</span> <span class="o">(</span><span class="k">by</span> <span class="n">proof_of_soundness</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956665):
<p>Maybe we could have <code>{ .. | .. } is_well_defined ..</code> be some fancy notation for this type of things?</p>

#### [ Kevin Buzzard (Oct 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956774):
<p>Do you mean <code>{[[x]] : QuotType | formula x}</code>?</p>

#### [ Johan Commelin (Oct 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956817):
<p>Does that work?</p>

#### [ Chris Hughes (Oct 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956818):
<p>Looks like the image of <code>quotient.mk</code> of some set.</p>

#### [ Chris Hughes (Oct 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956832):
<p><code>quotient.mk '' {x | formula x}</code></p>

#### [ Kenny Lau (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956838):
<p>there are two ways of forming subquotient</p>

#### [ Kenny Lau (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956842):
<p>and a theorem that they are the same</p>

#### [ Kenny Lau (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956843):
<p>(in maths, not in Lean)</p>

#### [ Johan Commelin (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956847):
<p>Right, I see where this is going...</p>

#### [ Johan Commelin (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956850):
<p>In particular, they aren't defeq</p>

#### [ Kenny Lau (Oct 01 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956970):
<p>few things are</p>

#### [ Johan Commelin (Oct 01 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956992):
<p>So Chris gives a workaround, but proving that his thing is the same as what I want is non-trivial.</p>

#### [ Chris Hughes (Oct 01 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134957502):
<p>But it's non trivial because there's mathematical content right?</p>

#### [ Johan Commelin (Oct 01 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134957509):
<p>Right, you have to prove that <code>formula</code> is constant on equivalence classes</p>

#### [ Chris Hughes (Oct 01 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134957645):
<p>The harder <code>lift</code> definition is probably the best one to use.</p>

#### [ Johan Commelin (Oct 01 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134957658):
<p>Yes, so I don't mind proving something hard, but I would like to keep a readable definition. Hence this question.</p>

#### [ Mario Carneiro (Oct 01 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134958313):
<p>To keep the definition readable, make the well definedness part a lemma that you prove immediately before</p>

#### [ Johan Commelin (Oct 01 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959001):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> That is certainly an option, but<br>
(1) the definition still won't be able to use subset notation;<br>
(2) it is not what mathematicians are used to. We always define something, and afterwards fill in the proof obligation of showing that the definition is well-defined.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959021):
<p>I think that it matches mathematical practice in that you aren't licensed to use the definition until you have proven the well definedness condition</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959030):
<p>in lean if you can say it you can use it, so you have to be intercepted right at the definition</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959080):
<p>I'm a little confused about what exactly you want to write though</p>

#### [ Johan Commelin (Oct 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959096):
<p>I completely agree.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959144):
<p>So my suggestion was to <em>syntactically</em> prove the well-definedness after the definition. But in fact it is just part of the definition.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959148):
<p>Most importantly, I would like the definition to be <em>very</em> readable.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959149):
<p>Isn't that what <code>quot.lift</code> already does?</p>

#### [ Johan Commelin (Oct 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959155):
<p>Yes. But then my subset notation goes out of the window.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959176):
<p>Can you be more specific?</p>

#### [ Johan Commelin (Oct 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959189):
<p>Any mathematician who first looks at Lean, and wants to look up the definition of <code>Spv</code> in the perfectoid project will not understand anything if he/she sees a <code>quot.lift</code>.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959229):
<p>That is completely foreign.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959232):
<p>And the stuff that follows it is barely recognisable.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959244):
<p>On the other hand</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foobar</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">QuotType</span> <span class="bp">|</span> <span class="n">formula</span> <span class="n">x</span><span class="o">}</span> <span class="n">is_well_defined</span> <span class="o">(</span><span class="k">by</span> <span class="n">proof_of_soundness</span><span class="o">)</span>
</pre></div>


<p>is very readable.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959255):
<p>But my Lean-fu is not sufficient to turn that into valid Lean.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959266):
<p>Currently in the perfectoid project we are stacking 5 subquotients on top of each other.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959302):
<p>And it becomes really horrible.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959324):
<p>(Well, <em>currently</em> there is no <code>quot</code>, but that isn't tenable either. So we need the <code>quot</code>, and we'dd like it to be readable.)</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959443):
<p>I am confused about why your def is not valid lean</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959455):
<p>I wrote what I thought you were trying to say but you have not adopted my change</p>

#### [ Johan Commelin (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959507):
<p>Sorry, which change are you talking about?</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959509):
<p>I mean, I wrote what I thought was invalid lean</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959513):
<p>I put the equiv class notation in</p>

#### [ Johan Commelin (Oct 01 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959525):
<p>Right. So now I tried using Chris's suggestion.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959533):
<p>But then you can define <code>Spa</code>, and you get stuck when you want to define the opens.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959614):
<p>To paraphrase Mario:</p>
<blockquote>
<p>But I <em>do not</em> want to be thinking about <code>quot.lift</code> and <code>subtype.val</code> when I am writing a proof<br>
the mindset is completely different, it is a distraction</p>
</blockquote>

#### [ Mario Carneiro (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959617):
<p>Is your <code>foobar</code> stuff about <code>Spa</code>? If so can you show what it looks like in situ</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959618):
<p>All I am saying is that you keep saying that something is invalid lean and it looks fine to me</p>

#### [ Chris Hughes (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959634):
<p>But the definitional equality of <code>quotient.lift</code> is really handy. Just give a docstring. Aiming to make your code usable by someone who doesn't know what <code>quotient.lift</code> is is probably impossible.</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959650):
<p>And I wrote something which was invalid lean and asked if it was what you meant and all you did was asked me if my invalid lean was valid</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959708):
<p>So we're clearly at cross purposes. My question is what is invalid about your lean</p>

#### [ Patrick Massot (Oct 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959722):
<p>Are we talking about <code>def foobar := {x : QuotType | formula x} is_well_defined (by proof_of_soundness)</code>?</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959728):
<p>In the case of <code>Spa</code>, I don't think you should try to get defeq just right, because <code>Spa</code> itself is not quite a quotient in the way we want it to be anyway</p>

#### [ Patrick Massot (Oct 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959729):
<p>It seems pretty invalid to me</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959735):
<p>I don't have access to lean right now so I'll just shut up and stop adding to the noise</p>

#### [ Johan Commelin (Oct 01 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959782):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Sorry, I finally understand. I think <code>{[[x]] : QuotType | formula x}</code> doesn't leave any room for the proof obligation that <code>formula x</code> only depends on <code>[[x]]</code>. That proof has to go somewhere. Mathematicians also do that.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959783):
<p>That's a perfectly valid definition, which means the image of such and such</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959806):
<p>why not <code>{q : QuotType | formula q}</code></p>

#### [ Mario Carneiro (Oct 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959814):
<p>and define <code>formula q</code> using a lift</p>

#### [ Johan Commelin (Oct 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959816):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">Spa</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Huber_pair</span><span class="o">)</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="err">&#39;&#39;</span> <span class="o">{</span><span class="n">v</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">A</span> <span class="bp">|</span> <span class="n">v</span><span class="bp">.</span><span class="n">is_continuous</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">r</span><span class="o">,</span> <span class="n">r</span> <span class="err">∈</span> <span class="n">A</span><span class="err">⁺</span> <span class="bp">→</span> <span class="n">v</span> <span class="n">r</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959855):
<p>This is what I have now.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959863):
<p>is <code>is_continuous</code> constant on equivalence classes?</p>

#### [ Johan Commelin (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959866):
<p>And</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">R</span><span class="o">]</span>

<span class="kn">structure</span> <span class="n">Valuation</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="err">Γ</span>   <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span>
<span class="o">(</span><span class="n">grp</span> <span class="o">:</span> <span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">)</span>
<span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="bp">@</span><span class="n">valuation</span> <span class="n">R</span> <span class="bp">_</span> <span class="err">Γ</span> <span class="n">grp</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">Valuation</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe_to_fun</span> <span class="o">(</span><span class="n">Valuation</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">F</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">v</span><span class="o">,</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">with_zero</span> <span class="n">v</span><span class="bp">.</span><span class="err">Γ</span><span class="o">,</span> <span class="n">coe</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">v</span><span class="o">,</span> <span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">val</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">linear_ordered_value_group</span> <span class="o">{</span><span class="n">v</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">}</span> <span class="o">:</span> <span class="n">linear_ordered_comm_group</span> <span class="n">v</span><span class="bp">.</span><span class="err">Γ</span> <span class="o">:=</span> <span class="n">v</span><span class="bp">.</span><span class="n">grp</span>

<span class="kn">end</span> <span class="n">Valuation</span>

<span class="kn">instance</span> <span class="n">Spv</span><span class="bp">.</span><span class="n">setoid</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">Valuation</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">v₁</span> <span class="n">v₂</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">v₁</span> <span class="n">r</span> <span class="bp">≤</span> <span class="n">v₁</span> <span class="n">s</span> <span class="bp">↔</span> <span class="n">v₂</span> <span class="n">r</span> <span class="bp">≤</span> <span class="n">v₂</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">v</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">refl</span> <span class="o">},</span>
    <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">h</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">symmetry</span><span class="o">,</span> <span class="n">exact</span> <span class="n">h</span> <span class="n">r</span> <span class="n">s</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">v₃</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">iff</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">h₁</span> <span class="n">r</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="n">r</span> <span class="n">s</span><span class="o">)</span> <span class="o">}</span>
  <span class="kn">end</span> <span class="o">}</span>

<span class="kn">definition</span> <span class="n">Spv</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="n">Spv</span><span class="bp">.</span><span class="n">setoid</span> <span class="n">R</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959871):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Yes it is, but the proof is sorried.</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959879):
<blockquote>
<p>is <code>is_continuous</code> constant on equivalence classes?</p>
</blockquote>
<p>yes, although I was waiting for module refactoring to prove it.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959891):
<p>Yep, that will need quite some module-juggling.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959900):
<p>And a bit of <code>tfae</code>-icing <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959913):
<p>It is mostly rings but I was using module refactoring as an excuse to put it off</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959944):
<p>what happened to the relations?</p>

#### [ Johan Commelin (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959946):
<p>Which relations?</p>

#### [ Johan Commelin (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959958):
<p>Aah, lol, they are gone</p>

#### [ Johan Commelin (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959961):
<p>They are in the setoid</p>

#### [ Johan Commelin (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959967):
<p>So there are no longer relations on <code>R</code>.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959982):
<p>The reason for that definition was because the quotient doesn't work</p>

#### [ Johan Commelin (Oct 01 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959989):
<p>So how can you define <code>lift</code> and friends using the relations?</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959992):
<p>it's not universe polymorphic enough, and your definition lives in a higher universe</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960044):
<p>That's what the whole thing about generating valuations is for</p>

#### [ Johan Commelin (Oct 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960045):
<p>To me <code>quot</code> is a bunch of <code>C++</code> magic that somehow works. But I don't know how to provide my own <code>lift</code> without at some point resorting to <code>quot.lift</code>.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960048):
<p>You do it the old fashioned way</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960050):
<p>with sets</p>

#### [ Johan Commelin (Oct 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960059):
<p>Sorry, I don't follow.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960068):
<p>Given a relation on <code>R</code>. How do you get a valuation?</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960073):
<blockquote>
<p>For the perfectoid project we often need to work with subsets of quotient types. A mathematician would write</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foobar</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">QuotType</span> <span class="bp">|</span> <span class="n">formula</span> <span class="n">x</span><span class="o">}</span>
</pre></div>


<p>and afterwards bother with the proof obligation of showing that it is well-defined. Can we mimic this in Lean?</p>
</blockquote>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">QuotType</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">formula</span> <span class="o">:</span> <span class="n">QuotType</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="kn">definition</span> <span class="n">X</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">QuotType</span> <span class="bp">|</span> <span class="n">formula</span> <span class="n">x</span><span class="o">}</span>
</pre></div>


<p>Mimicked. That was what I was trying to say.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960081):
<p>The relation is assumed to be the image of some valuation</p>

#### [ Johan Commelin (Oct 01 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960141):
<p>Could you write down the definition of <code>lift</code> (with a <code>sorry</code>)?</p>

#### [ Johan Commelin (Oct 01 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960150):
<p>I couldn't write down anything of which I was even sure that a proof existed.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960158):
<p>Wasn't this already done in an earlier version?</p>

#### [ Johan Commelin (Oct 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960261):
<p>No, only the claim that it should be done.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960265):
<p><code>mk</code> was done. That's not so hard.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960267):
<p>But <code>lift</code> wasn't.</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960269):
<p><code>mk</code> took me forever</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960279):
<p>Wasn't this the one where I had to invoke the first isomorphism theorem between objects in different universes?</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960288):
<p>yes</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960294):
<p>I thought I did most of the hard work for this</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960301):
<p>and that everything else was just noise modulo continuous being constant on equiv classes</p>

#### [ Johan Commelin (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960311):
<p>Hmm, sorry. That wasn't nice to say. You indeed need all the minimal_valuation stuff.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960357):
<p>But once that is there <code>mk</code> is not very hard.</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960360):
<p>I'm not offended, I am just aware that there are issues here I don't understand so am a bit scared of messing with stuff</p>

#### [ Johan Commelin (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960379):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">Spv</span> <span class="o">:=</span>
<span class="c1">-- quotient (Spv.setoid R)</span>
<span class="o">{</span><span class="n">ineq</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">R</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="bp">//</span> <span class="bp">∃</span> <span class="o">{</span><span class="err">Γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">],</span>
  <span class="k">by</span> <span class="n">exactI</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">valuation</span> <span class="n">R</span> <span class="err">Γ</span><span class="o">),</span> <span class="bp">∀</span> <span class="n">r</span> <span class="n">s</span> <span class="o">:</span> <span class="n">R</span><span class="o">,</span> <span class="n">v</span> <span class="n">r</span> <span class="bp">≤</span> <span class="n">v</span> <span class="n">s</span> <span class="bp">↔</span> <span class="n">ineq</span> <span class="n">r</span> <span class="n">s</span><span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960381):
<p>Voila, the old definition.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960396):
<p>I agree that the universe issue wasn't solved by what I did. (I'm really silly when it comes to universes.)</p>

#### [ Johan Commelin (Oct 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960467):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you think this would work?</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">lift</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₃</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">,</span> <span class="n">v₁</span> <span class="bp">≈</span> <span class="n">v₂</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">v₁</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">Spv</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Oct 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960497):
<p>can you post enough to make <code>Spv</code> compile? Stub out the definition of <code>valuation</code> and such</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960670):
<p>mathlib doesn't have <code>linear_ordered_comm_group</code></p>

#### [ Johan Commelin (Oct 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960675):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">valuations</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>
<span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">quotient_group</span>

<span class="n">universes</span> <span class="n">u₁</span> <span class="n">u₂</span> <span class="n">u₃</span>

<span class="kn">namespace</span> <span class="n">valuation</span>

<span class="n">class</span> <span class="n">is_valuation</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="err">Γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">]</span>
  <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">with_zero</span> <span class="err">Γ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">map_zero</span> <span class="o">:</span> <span class="n">v</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">map_one</span>  <span class="o">:</span> <span class="n">v</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span>
<span class="o">(</span><span class="n">map_mul</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">v</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">v</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">v</span> <span class="n">y</span><span class="o">)</span>
<span class="o">(</span><span class="n">map_add</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">v</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">v</span> <span class="n">x</span> <span class="bp">∨</span> <span class="n">v</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">v</span> <span class="n">y</span><span class="o">)</span>

<span class="kn">end</span> <span class="n">valuation</span>

<span class="n">def</span> <span class="n">valuation</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="err">Γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">)</span> <span class="o">[</span><span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">v</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">with_zero</span> <span class="err">Γ</span> <span class="bp">//</span> <span class="n">valuation</span><span class="bp">.</span><span class="n">is_valuation</span> <span class="n">v</span> <span class="o">}</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">R</span><span class="o">]</span>

<span class="kn">open</span> <span class="n">valuation</span>

<span class="kn">structure</span> <span class="n">Valuation</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="err">Γ</span>   <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span>
<span class="o">(</span><span class="n">grp</span> <span class="o">:</span> <span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">)</span>
<span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="bp">@</span><span class="n">valuation</span> <span class="n">R</span> <span class="bp">_</span> <span class="err">Γ</span> <span class="n">grp</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">Valuation</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe_to_fun</span> <span class="o">(</span><span class="n">Valuation</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">F</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">v</span><span class="o">,</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">with_zero</span> <span class="n">v</span><span class="bp">.</span><span class="err">Γ</span><span class="o">,</span> <span class="n">coe</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">v</span><span class="o">,</span> <span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">val</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">linear_ordered_value_group</span> <span class="o">{</span><span class="n">v</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">}</span> <span class="o">:</span> <span class="n">linear_ordered_comm_group</span> <span class="n">v</span><span class="bp">.</span><span class="err">Γ</span> <span class="o">:=</span> <span class="n">v</span><span class="bp">.</span><span class="n">grp</span>

<span class="kn">end</span> <span class="n">Valuation</span>

<span class="kn">instance</span> <span class="n">Spv</span><span class="bp">.</span><span class="n">setoid</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">Valuation</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">v₁</span> <span class="n">v₂</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">v₁</span> <span class="n">r</span> <span class="bp">≤</span> <span class="n">v₁</span> <span class="n">s</span> <span class="bp">↔</span> <span class="n">v₂</span> <span class="n">r</span> <span class="bp">≤</span> <span class="n">v₂</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">v</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">refl</span> <span class="o">},</span>
    <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">h</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">symmetry</span><span class="o">,</span> <span class="n">exact</span> <span class="n">h</span> <span class="n">r</span> <span class="n">s</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">v₃</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">iff</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">h₁</span> <span class="n">r</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="n">r</span> <span class="n">s</span><span class="o">)</span> <span class="o">}</span>
  <span class="kn">end</span> <span class="o">}</span>

<span class="kn">definition</span> <span class="n">Spv</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">ineq</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">R</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="bp">//</span> <span class="bp">∃</span> <span class="o">{</span><span class="err">Γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">],</span>
  <span class="k">by</span> <span class="n">exactI</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">valuation</span> <span class="n">R</span> <span class="err">Γ</span><span class="o">),</span> <span class="bp">∀</span> <span class="n">r</span> <span class="n">s</span> <span class="o">:</span> <span class="n">R</span><span class="o">,</span> <span class="n">v</span> <span class="n">r</span> <span class="bp">≤</span> <span class="n">v</span> <span class="n">s</span> <span class="bp">↔</span> <span class="n">ineq</span> <span class="n">r</span> <span class="n">s</span><span class="o">}</span>

<span class="kn">namespace</span> <span class="n">Spv</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span><span class="o">}</span> <span class="o">{</span><span class="err">Γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₂</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">]</span>

<span class="kn">definition</span> <span class="n">mk</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">valuation</span> <span class="n">R</span> <span class="err">Γ</span><span class="o">)</span> <span class="o">:</span> <span class="n">Spv</span> <span class="n">R</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span> <span class="n">v</span> <span class="n">r</span> <span class="bp">≤</span> <span class="n">v</span> <span class="n">s</span><span class="o">,</span>
  <span class="bp">⟨</span><span class="o">(</span><span class="n">minimal_value_group</span> <span class="n">v</span><span class="o">)</span><span class="bp">.</span><span class="err">Γ</span><span class="o">,</span>
    <span class="bp">⟨</span><span class="n">minimal_value_group</span><span class="bp">.</span><span class="n">linear_ordered_comm_group</span> <span class="n">v</span><span class="o">,</span>
      <span class="bp">⟨</span><span class="n">v</span><span class="bp">.</span><span class="n">minimal_valuation</span><span class="o">,</span> <span class="n">v</span><span class="bp">.</span><span class="n">minimal_valuation_equiv</span><span class="bp">⟩⟩⟩⟩</span>

<span class="kn">definition</span> <span class="n">lift</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₃</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">,</span> <span class="n">v₁</span> <span class="bp">≈</span> <span class="n">v₂</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">v₁</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v₂</span><span class="o">)</span> <span class="o">:</span>
<span class="n">Spv</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift</span> <span class="n">f</span> <span class="n">H</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960677):
<p>Aah, too bad mathlib doesn't have that.</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960745):
<p>mathlib has the decidable version</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960750):
<p>(rather core has it)</p>

#### [ Mario Carneiro (Oct 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960763):
<p>is there a reason that doesn't work here?</p>

#### [ Kevin Buzzard (Oct 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960848):
<blockquote>
<p>I agree that the universe issue wasn't solved by what I did. (I'm really silly when it comes to universes.)</p>
</blockquote>
<p>I don't know if there is a universe issue with your version. I find subtypes easier to use than quotient types but this might just be lack of practice. I am happy if you think a change will make it more readable but I don't want to run into universe issues. My understanding of the universe issues is that I should not let a valuation be an "equivalence class" of <code>v : R -&gt; with_zero Gamma</code> where Gamma is allowed to vary over any type in any universe. I instead restricted to Gamma varying over things in the same universe as R and then I had to work to show that if I had a Gamma in another universe it was equivalent to Gamma in R's universe. I think that these issues (which I don't understand fully) are not the same as the one Johan is talking about, which is defining Spv not to be the ordering on R but to be the equiv class of valuations which give the ordering, so my guess is that these changes should be fine <em>as long as the equiv reln is defined on valuations taking values in things in R's universe</em>. I am not 100% sure that this is the point but that's my current understanding; I'm currently about to start travelling for 2 hours by the way.</p>

#### [ Johan Commelin (Oct 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960849):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <del>Mathlib</del>core has the additive version...</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960919):
<p>Unfortunately, you can't even take an equivalence class over all valuations with type in the same universe as R, because this is already too big</p>

#### [ Johan Commelin (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960982):
<p>I have</p>
<div class="codehilite"><pre><span></span><span class="n">hv</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="o">{</span><span class="err">Γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">]</span> <span class="o">(</span><span class="n">v_1</span> <span class="o">:</span> <span class="n">valuation</span> <span class="n">R</span> <span class="err">Γ</span><span class="o">),</span>
    <span class="bp">∀</span> <span class="o">(</span><span class="n">r</span> <span class="n">s</span> <span class="o">:</span> <span class="n">R</span><span class="o">),</span> <span class="err">⇑</span><span class="n">v_1</span> <span class="n">r</span> <span class="bp">≤</span> <span class="err">⇑</span><span class="n">v_1</span> <span class="n">s</span> <span class="bp">↔</span> <span class="n">v</span> <span class="n">r</span> <span class="n">s</span>
</pre></div>


<p>in my local context. Somehow <code>cases hv</code> complains that it can only eliminate into <code>Prop</code>. <span class="emoji emoji-1f622" title="cry">:cry:</span></p>

#### [ Mario Carneiro (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960984):
<p>The best you can do is take an equivalence class over all valuations in some "small" collection of representatives</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960986):
<p>Use <code>classical.cases_on</code></p>

#### [ Johan Commelin (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960987):
<blockquote>
<p>Unfortunately, you can't even take an equivalence class over all valuations with type in the same universe as R, because this is already too big</p>
</blockquote>
<p>Like I just experienced (-;</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961003):
<p>I'm still struggling to get your file to compile, but that's what I was going to do</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961011):
<p>just use <code>classical.cases_on</code> three times and apply the function</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961053):
<p>You won't even need the well definedness assumption, it's just for show</p>

#### [ Johan Commelin (Oct 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961068):
<p>Let me try</p>

#### [ Johan Commelin (Oct 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961089):
<p>How do I "use" <code>classical.cases_on</code> with <code>hv</code>?</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961133):
<p><code>refine classical.cases_on hv (\lam Gamma h', _)</code></p>

#### [ Johan Commelin (Oct 01 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961136):
<p>I see</p>

#### [ Johan Commelin (Oct 01 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961138):
<p>Good old refine</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961139):
<p>You might be able to use a custom recursor with <code>induction</code> but I find <code>refine</code> the most straightforward</p>

#### [ Johan Commelin (Oct 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961152):
<div class="codehilite"><pre><span></span>type mismatch at application
  classical.cases_on hv
term
  hv
has type
  ∃ {Γ : Type u₁} [_inst_3 : linear_ordered_comm_group Γ] (v_1 : valuation R Γ),
    ∀ (r s : R), ⇑v_1 r ≤ ⇑v_1 s ↔ v r s : Prop
but is expected to have type
  Prop : Type
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961156):
<p>Also... lunch time</p>

#### [ Johan Commelin (Oct 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961157):
<p>See you later</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961159):
<p>lol</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961210):
<p>sorry, I think it's called <code>classical.rec_on</code></p>

#### [ Mario Carneiro (Oct 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961215):
<p>it's a bad name</p>

#### [ Mario Carneiro (Oct 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961221):
<p>it should be more like <code>exists.rec_on_classical</code></p>

#### [ Johan Commelin (Oct 01 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134963338):
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">lift</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₃</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">,</span> <span class="n">v₁</span> <span class="bp">≈</span> <span class="n">v₂</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">v₁</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v₂</span><span class="o">)</span> <span class="o">:</span>
<span class="n">Spv</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">v</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">v</span> <span class="k">with</span> <span class="n">v</span> <span class="n">hv</span><span class="o">,</span>
<span class="n">refine</span> <span class="n">classical</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">hv</span> <span class="o">(</span><span class="bp">λ</span> <span class="err">Γ</span> <span class="n">hv&#39;</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span>
<span class="n">refine</span> <span class="n">classical</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">hv&#39;</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">inst</span> <span class="n">hv&#39;&#39;</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span>
<span class="n">refine</span> <span class="n">classical</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">hv&#39;&#39;</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">v</span> <span class="n">h</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span>
<span class="n">exact</span> <span class="n">f</span> <span class="o">{</span><span class="err">Γ</span> <span class="o">:=</span> <span class="err">Γ</span><span class="o">,</span> <span class="n">grp</span> <span class="o">:=</span> <span class="n">inst</span><span class="o">,</span> <span class="n">val</span> <span class="o">:=</span> <span class="n">v</span><span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134963350):
<p>That kind of worked. But I didn't use <code>H</code></p>

#### [ Patrick Massot (Oct 01 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964015):
<p>Mario announced that you wouldn't need H</p>

#### [ Johan Commelin (Oct 01 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964138):
<p>So, is this some sort of "cheating" definition?</p>

#### [ Johan Commelin (Oct 01 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964152):
<p>I guess we should leave <code>H</code> in place, because otherwise <code>lift</code> can be abused.</p>

#### [ Reid Barton (Oct 01 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964277):
<p>You will need <code>H</code> to prove that <code>lift f H (mk v) = f v</code></p>

#### [ Johan Commelin (Oct 01 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964394):
<p>Good point. Let me prove such things now.</p>

#### [ Patrick Massot (Oct 01 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964400):
<p>It seems this is a very convenient way to setup things: define stuff without precondition, and prove they have the expected properties under the appropriate conditions. An extreme example is <a href="https://github.com/leanprover-community/mathlib/blob/b3b50ce67c8b73442372c5141e8836c64ea13826/analysis/topology/completion.lean#L442-L446" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/b3b50ce67c8b73442372c5141e8836c64ea13826/analysis/topology/completion.lean#L442-L446">https://github.com/leanprover-community/mathlib/blob/b3b50ce67c8b73442372c5141e8836c64ea13826/analysis/topology/completion.lean#L442-L446</a></p>

#### [ Johan Commelin (Oct 01 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134965116):
<p>Now I'm stuck on the following goal:</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">classical</span><span class="bp">.</span><span class="n">rec_on</span> <span class="bp">_</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="err">Γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">)</span>
       <span class="o">(</span><span class="n">hv&#39;</span> <span class="o">:</span>
         <span class="bp">∃</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">]</span> <span class="o">(</span><span class="n">v_1</span> <span class="o">:</span> <span class="n">valuation</span> <span class="n">R</span> <span class="err">Γ</span><span class="o">),</span>
           <span class="bp">∀</span> <span class="o">(</span><span class="n">r</span> <span class="n">s</span> <span class="o">:</span> <span class="n">R</span><span class="o">),</span> <span class="err">⇑</span><span class="n">v_1</span> <span class="n">r</span> <span class="bp">≤</span> <span class="err">⇑</span><span class="n">v_1</span> <span class="n">s</span> <span class="bp">↔</span> <span class="err">⇑</span><span class="o">(</span><span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">r</span> <span class="bp">≤</span> <span class="err">⇑</span><span class="o">(</span><span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">s</span><span class="o">),</span>
         <span class="n">classical</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">hv&#39;</span>
           <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">inst</span> <span class="o">:</span> <span class="n">linear_ordered_comm_group</span> <span class="err">Γ</span><span class="o">)</span>
            <span class="o">(</span><span class="n">hv&#39;&#39;</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">v_1</span> <span class="o">:</span> <span class="n">valuation</span> <span class="n">R</span> <span class="err">Γ</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">r</span> <span class="n">s</span> <span class="o">:</span> <span class="n">R</span><span class="o">),</span> <span class="err">⇑</span><span class="n">v_1</span> <span class="n">r</span> <span class="bp">≤</span> <span class="err">⇑</span><span class="n">v_1</span> <span class="n">s</span> <span class="bp">↔</span> <span class="err">⇑</span><span class="o">(</span><span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">r</span> <span class="bp">≤</span> <span class="err">⇑</span><span class="o">(</span><span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">s</span><span class="o">),</span>
              <span class="n">classical</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">hv&#39;&#39;</span>
                <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v_1</span> <span class="o">:</span> <span class="n">valuation</span> <span class="n">R</span> <span class="err">Γ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">r</span> <span class="n">s</span> <span class="o">:</span> <span class="n">R</span><span class="o">),</span> <span class="err">⇑</span><span class="n">v_1</span> <span class="n">r</span> <span class="bp">≤</span> <span class="err">⇑</span><span class="n">v_1</span> <span class="n">s</span> <span class="bp">↔</span> <span class="err">⇑</span><span class="o">(</span><span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">r</span> <span class="bp">≤</span> <span class="err">⇑</span><span class="o">(</span><span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="n">s</span><span class="o">),</span>
                   <span class="n">f</span> <span class="o">{</span><span class="err">Γ</span> <span class="o">:=</span> <span class="err">Γ</span><span class="o">,</span> <span class="n">grp</span> <span class="o">:=</span> <span class="n">inst</span><span class="o">,</span> <span class="n">val</span> <span class="o">:=</span> <span class="n">v_1</span><span class="o">})))</span> <span class="bp">=</span>
    <span class="n">f</span> <span class="n">v</span>
</pre></div>


<p>The maths is clear, but I have no idea how to work with this <code>classical.rec_on</code>. How do I fight those?</p>

#### [ Johan Commelin (Oct 01 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134965842):
<p>Ok, so I can turn it into the rather unhelpful:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">lift_mk</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₃</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">,</span> <span class="n">v₁</span> <span class="bp">≈</span> <span class="n">v₂</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">v₁</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v₂</span><span class="o">}</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
<span class="n">lift</span> <span class="n">f</span> <span class="n">H</span> <span class="o">(</span><span class="n">mk</span> <span class="n">v</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">H</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="c1">-- ⊢ {Γ := classical.some _, grp := classical.some _, val := classical.some _} ≈ v</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134965907):
<p>As you can see in the code, there is this bit saying <code>(hv'' : ∃ (v_1 : valuation R Γ), ∀ (r s : R), ⇑v_1 r ≤ ⇑v_1 s ↔ ⇑(v.val) r ≤ ⇑(v.val) s),</code>. I need to extract that, and use it to close my goal.</p>

#### [ Johan Commelin (Oct 01 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134966633):
<p>Ok, from browsing code I think that I should use <code>some_spec</code> or <code>some_spec2</code>. Can anyone confirm that this is reasonable? (I have yet to figure out how I should use them...)</p>

#### [ Johan Commelin (Oct 01 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967775):
<p>This is what I have now:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">lift_mk</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₃</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">,</span> <span class="n">v₁</span> <span class="bp">≈</span> <span class="n">v₂</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">v₁</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v₂</span><span class="o">}</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
<span class="n">lift</span> <span class="n">f</span> <span class="n">H</span> <span class="o">(</span><span class="n">mk</span> <span class="n">v</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">ineq</span> <span class="o">:=</span> <span class="n">mk</span> <span class="n">v</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">foo</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">ineq</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
  <span class="n">refine</span> <span class="n">H</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span>
<span class="kn">end</span>
<span class="c1">-- R : Type u₁,</span>
<span class="c1">-- _inst_1 : comm_ring R,</span>
<span class="c1">-- _inst_2 : decidable_eq R,</span>
<span class="c1">-- β : Type u₃,</span>
<span class="c1">-- f : Valuation R → β,</span>
<span class="c1">-- H : ∀ (v₁ v₂ : Valuation R), v₁ ≈ v₂ → f v₁ = f v₂,</span>
<span class="c1">-- v : Valuation R,</span>
<span class="c1">-- ineq : Spv R := mk v,</span>
<span class="c1">-- foo : ∀ (r s : R), ⇑(classical.some _) r ≤ ⇑(classical.some _) s ↔ ineq.val r s,</span>
<span class="c1">-- r s : R</span>
<span class="c1">-- ⊢ ⇑(classical.some _) r ≤ ⇑(classical.some _) s ↔ ⇑v r ≤ ⇑v s</span>
</pre></div>


<p>Looks deceptively close, but I can't finish it.</p>

#### [ Johannes Hölzl (Oct 01 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967787):
<p>Yes, if you want to proof something about <code>classical.some</code>. What you usually do is to define a the constant using <code>classical.some</code> and then proof when a corresponding value exists, then the constant has the properties.</p>

#### [ Johannes Hölzl (Oct 01 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967800):
<p>what is the type of <code>_</code> in <code>classical.some _</code>?</p>

#### [ Johan Commelin (Oct 01 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967891):
<p>Hooray!</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">lift_mk</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₃</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">,</span> <span class="n">v₁</span> <span class="bp">≈</span> <span class="n">v₂</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">v₁</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v₂</span><span class="o">}</span> <span class="o">(</span><span class="n">v</span> <span class="o">:</span> <span class="n">Valuation</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
<span class="n">lift</span> <span class="n">f</span> <span class="n">H</span> <span class="o">(</span><span class="n">mk</span> <span class="n">v</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">v</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">ineq</span> <span class="o">:=</span> <span class="n">mk</span> <span class="n">v</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">spec</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">mk</span> <span class="n">v</span><span class="o">)</span><span class="bp">.</span><span class="n">property</span><span class="o">,</span>
  <span class="n">refine</span> <span class="n">H</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">r</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">mk</span><span class="o">]</span> <span class="n">at</span> <span class="n">spec</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">spec</span> <span class="n">r</span> <span class="n">s</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967896):
<p>Somehow I managed to convince Lean!</p>

#### [ Andrew Ashworth (Oct 01 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967899):
<p>I agree <code>some_spec</code> is awkward, but for what it's worth, it is mentioned in TPIL. When I first saw the example provided in 11.6 I didn't have any idea how it worked.</p>

#### [ Andrew Ashworth (Oct 01 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967939):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">classical</span> <span class="n">function</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">prop_decidable</span>

<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">linv</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="k">if</span> <span class="n">ex</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="k">then</span> <span class="n">some</span> <span class="n">ex</span> <span class="k">else</span> <span class="n">arbitrary</span> <span class="n">α</span>

<span class="kn">theorem</span> <span class="n">linv_comp_self</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span>
    <span class="o">[</span><span class="n">inhabited</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">inj</span> <span class="o">:</span> <span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">linv</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span>
<span class="n">funext</span> <span class="o">(</span><span class="k">assume</span> <span class="n">a</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">ex</span>  <span class="o">:</span> <span class="bp">∃</span> <span class="n">a₁</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="n">a₁</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span><span class="o">,</span> <span class="k">from</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="n">a</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="k">have</span>   <span class="n">feq</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">some</span> <span class="n">ex</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span><span class="o">,</span> <span class="k">from</span> <span class="n">some_spec</span> <span class="n">ex</span><span class="o">,</span>
  <span class="k">calc</span> <span class="n">linv</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">some</span> <span class="n">ex</span> <span class="o">:</span>  <span class="n">dif_pos</span> <span class="n">ex</span>
             <span class="bp">...</span>    <span class="bp">=</span> <span class="n">a</span>       <span class="o">:</span>  <span class="n">inj</span> <span class="n">feq</span><span class="o">)</span>
</pre></div>


{% endraw %}
