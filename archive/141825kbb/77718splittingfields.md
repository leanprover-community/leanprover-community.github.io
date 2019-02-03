---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/77718splittingfields.html
---

## Stream: [kbb](https://leanprover-community.github.io/archive/141825kbb/index.html)
### Topic: [splitting fields](https://leanprover-community.github.io/archive/141825kbb/77718splittingfields.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 14 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/133967305):
<p>It would be great if we could push the splitting fields branch to the point where we can define the Galois group of a splitting field.</p>

#### [ Johan Commelin (Sep 14 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/133967354):
<p>So far we can adjoint the root of an irreducible polynomial. There is a <code>sorry</code>d statement of the universal property of adjoining a root.</p>

#### [ Johan Commelin (Sep 14 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/133967371):
<p>Ooh, the branch I'm talking about is not in this repo, but in the community mathlib.</p>

#### [ Johan Commelin (Sep 14 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/133967448):
<p>If we combine this with the stuff on Hecke operators, then we'll have the formal abstract of Kevin's paper (modulo one fact that requires a Mjölnir to prove).</p>

#### [ Johan Commelin (Sep 17 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134084535):
<p>Little hole in the quotient ring api. I'll leave it to others to <span class="emoji emoji-1f3cc" title="golf">:golf:</span> </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">quotient_ring</span><span class="bp">.</span><span class="n">lift</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span>
<span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span>
<span class="n">quotient_ring</span><span class="bp">.</span><span class="n">quotient</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">lift</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">quotient_ring</span><span class="bp">.</span><span class="n">quotient_rel</span> <span class="n">S</span><span class="o">)</span> <span class="n">f</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">eq_of_sub_eq_zero</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">is_submodule</span><span class="bp">.</span><span class="n">quotient_rel_eq</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="n">only</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_sub</span> <span class="n">f</span><span class="o">]</span> <span class="kn">using</span> <span class="n">H</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Sep 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085269):
<p>Here is <code>adjoin_root.lift</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lift</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">L</span><span class="o">]</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">K</span> <span class="bp">→</span> <span class="n">L</span><span class="o">)</span> <span class="o">[</span><span class="n">is_field_hom</span> <span class="n">i</span><span class="o">]</span>
  <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">L</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="n">eval₂</span> <span class="n">i</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">adjoin_root</span> <span class="n">f</span><span class="o">)</span> <span class="bp">→</span> <span class="n">L</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="bp">@</span><span class="n">quotient_ring</span><span class="bp">.</span><span class="n">lift</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">span</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">ring</span><span class="bp">.</span><span class="n">to_module</span> <span class="o">({</span><span class="n">f</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">K</span><span class="o">)))</span> <span class="o">(</span><span class="n">is_ideal</span><span class="bp">.</span><span class="n">span</span> <span class="bp">_</span><span class="o">)</span>
    <span class="o">(</span><span class="n">eval₂</span> <span class="n">i</span> <span class="n">x</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">g</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">span_singleton</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">y</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">H</span><span class="o">,</span> <span class="n">eval₂_mul</span><span class="o">],</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Sep 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085272):
<p>Which can undoubtly be golfed</p>

#### [ Johan Commelin (Sep 17 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085351):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think the next step was some really crazy inductive proof, right?</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085364):
<p>yes</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085383):
<p>the next step is the splitting field for one polynomial</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085455):
<p>Do we know that every polynomial over a field has an irreducible factor?</p>

#### [ Johan Commelin (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085540):
<p>I think so</p>

#### [ Johan Commelin (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085543):
<p>We know that <code>polynomial K</code> is a PID</p>

#### [ Johan Commelin (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085545):
<p>and every PID is a UFD</p>

#### [ Johan Commelin (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085546):
<p>I think that latter fact is now also in mathlib</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085548):
<p>we have UFDs?</p>

#### [ Johan Commelin (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085554):
<p>Hmm, I guess there is a standard lemma on <code>lift_mk</code> or something?</p>

#### [ Johan Commelin (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085592):
<p>We'll also need that.</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085596):
<p>yes</p>

#### [ Johan Commelin (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085598):
<p>Yes, Johannes added UFD's after Orsay</p>

#### [ Johan Commelin (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085606):
<p>So we need this <code>lift_mk</code> for quotient rings, and then for adjoin root.</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085609):
<p>the fact you want about <code>lift</code> is composition with the coercion from <code>K</code>, and value at the root</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085677):
<p>is the proof constructive? (i.e. is there a function from a polynomial to its smallest irreducible factor or something)</p>

#### [ Johan Commelin (Sep 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085678):
<p>Not only stuff from <code>K</code>, right? Also <code>K[X]</code></p>

#### [ Johan Commelin (Sep 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085688):
<p>Hmm, factoring is hard.</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085689):
<p>that isn't needed, it follows by homness</p>

#### [ Johan Commelin (Sep 17 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085693):
<p>???</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085700):
<p>but I guess the quotient map is equal to the eval map, we want to know that</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085747):
<p>oh, you didn't prove <code>lift</code> is a field hom</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085751):
<p>we definitely need that</p>

#### [ Johan Commelin (Sep 17 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085864):
<p>I didn't even prove it is a ring hom</p>

#### [ Johan Commelin (Sep 17 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085866):
<p>Working on that now</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085909):
<p>I think those are the same</p>

#### [ Johan Commelin (Sep 17 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086046):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I need some help to get the right statements for these API things: this is in the <code>quotient_ring</code> namespace:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lift</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span>
<span class="n">quotient_ring</span><span class="bp">.</span><span class="n">quotient</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">lift</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">quotient_ring</span><span class="bp">.</span><span class="n">quotient_rel</span> <span class="n">S</span><span class="o">)</span> <span class="n">f</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">eq_of_sub_eq_zero</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">is_submodule</span><span class="bp">.</span><span class="n">quotient_rel_eq</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="n">only</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_sub</span> <span class="n">f</span><span class="o">]</span> <span class="kn">using</span> <span class="n">H</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">lift_mk</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">S</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">{</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
<span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a</span><span class="err">⟧</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>

<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Sep 17 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086049):
<p>Should the latter be a simp-lemma?</p>

#### [ Johan Commelin (Sep 17 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086054):
<p>At the moment the <code>⟦a⟧</code> notation is broken.</p>

#### [ Johan Commelin (Sep 17 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086097):
<p>This is my first time working with quotients in Lean...</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086098):
<p>I forget the details but I don't think <code>⟦⟧</code> is part of the interface</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086108):
<p>The only "public" functions are the map from <code>K</code>, and the root element</p>

#### [ Johan Commelin (Sep 17 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086163):
<p>No, I'm working on quotient rings at the moment.</p>

#### [ Johan Commelin (Sep 17 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086165):
<p>Splitting field will come later.</p>

#### [ Johan Commelin (Sep 17 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086167):
<p>We don't even have <code>lift</code> for quotient rings at the moment.</p>

#### [ Johan Commelin (Sep 17 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086182):
<p>I guess we want that notation for general quotient rings, right?</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086190):
<p>ah okay</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086193):
<p>you want to redefine <code>mk</code> for that</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086200):
<p>that way you can give it the right type and find it with typeclass inference</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086240):
<p>when you prove it is a ring hom</p>

#### [ Johan Commelin (Sep 17 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086263):
<p>Aah, <code>local attribute [instance] quotient_rel</code> fixes it.</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086321):
<p>that won't help outside the section</p>

#### [ Mario Carneiro (Sep 17 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086330):
<p>you still want a public <code>mk</code> function</p>

#### [ Johan Commelin (Sep 17 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086494):
<p>Right. Quotient rings already had that. But they didn't have <code>lift</code></p>

#### [ Mario Carneiro (Sep 17 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086539):
<p>in that case you should use it in the statement of <code>lift_mk</code></p>

#### [ Johan Commelin (Sep 17 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134087318):
<p>Ok, this is what I now have</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">quotient_ring</span> <span class="c1">-- move this to the right file</span>
<span class="kn">open</span> <span class="n">is_submodule</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">quotient_rel</span>

<span class="n">def</span> <span class="n">lift</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span>
<span class="n">quotient</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">lift</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">quotient_rel</span> <span class="n">S</span><span class="o">)</span> <span class="n">f</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">eq_of_sub_eq_zero</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">quotient_rel_eq</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="n">only</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_sub</span> <span class="n">f</span><span class="o">]</span> <span class="kn">using</span> <span class="n">H</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">lift_mk</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">S</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">{</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
<span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a</span><span class="err">⟧</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">quotient_ring</span><span class="bp">.</span><span class="n">is_ring_hom_mk</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">S</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">{</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">}</span> <span class="o">:</span>
<span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span> <span class="k">by</span> <span class="k">show</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="mi">1</span><span class="err">⟧</span> <span class="bp">=</span> <span class="mi">1</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_one</span> <span class="n">f</span><span class="o">],</span>
  <span class="n">map_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a₁</span> <span class="n">a₂</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">a₁</span> <span class="n">a₂</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">a₁</span> <span class="n">a₂</span><span class="o">,</span> <span class="k">begin</span>
    <span class="k">show</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="o">(</span><span class="n">mk</span> <span class="n">a₁</span> <span class="bp">+</span> <span class="n">mk</span> <span class="n">a₂</span><span class="o">)</span> <span class="bp">=</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a₁</span><span class="err">⟧</span> <span class="bp">+</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a₂</span><span class="err">⟧</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="n">quotient_ring</span><span class="bp">.</span><span class="n">is_ring_hom_mk</span> <span class="n">S</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">this</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="o">(</span><span class="err">⟦</span><span class="n">a₁</span> <span class="bp">+</span> <span class="n">a₂</span><span class="err">⟧</span><span class="o">)</span> <span class="bp">=</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a₁</span><span class="err">⟧</span> <span class="bp">+</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a₂</span><span class="err">⟧</span><span class="o">,</span>
    <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">lift_mk</span><span class="o">,</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">f</span><span class="o">],</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a₁</span> <span class="n">a₂</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">a₁</span> <span class="n">a₂</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">a₁</span> <span class="n">a₂</span><span class="o">,</span> <span class="k">begin</span>
    <span class="k">show</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="o">(</span><span class="n">mk</span> <span class="n">a₁</span> <span class="bp">*</span> <span class="n">mk</span> <span class="n">a₂</span><span class="o">)</span> <span class="bp">=</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a₁</span><span class="err">⟧</span> <span class="bp">*</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a₂</span><span class="err">⟧</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="n">quotient_ring</span><span class="bp">.</span><span class="n">is_ring_hom_mk</span> <span class="n">S</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">this</span><span class="bp">.</span><span class="n">map_mul</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="o">(</span><span class="err">⟦</span><span class="n">a₁</span> <span class="bp">*</span> <span class="n">a₂</span><span class="err">⟧</span><span class="o">)</span> <span class="bp">=</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a₁</span><span class="err">⟧</span> <span class="bp">*</span> <span class="n">lift</span> <span class="n">S</span> <span class="n">f</span> <span class="n">H</span> <span class="err">⟦</span><span class="n">a₂</span><span class="err">⟧</span><span class="o">,</span>
    <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">lift_mk</span><span class="o">,</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_mul</span> <span class="n">f</span><span class="o">],</span>
  <span class="kn">end</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">quotient_ring</span>
</pre></div>

#### [ Chris Hughes (Sep 17 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134087827):
<p>You should be able to use <code>quotient.lift'</code> instead of <code>@quotient.lift ...</code></p>

#### [ Johan Commelin (Sep 17 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134087890):
<p>Yes, I've been golfing them a bit. I didn't use the <code>lift'</code> version though.</p>

#### [ Johan Commelin (Sep 17 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134088444):
<p>Ok, I pushed a bunch of changes</p>

#### [ Johan Commelin (Sep 17 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134088461):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think I might want to try the induction proof now...</p>

#### [ Johan Commelin (Sep 17 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089038):
<p>Hmm, so we have UFD's but we don't know that <code>K[X]</code> is an example of a UFD</p>

#### [ Johan Commelin (Sep 17 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089066):
<p>What we need to know is that if we have a polynomial <code>f</code> with a root <code>x</code>, then we can factor <code>f</code> as <code>(X - x) * g</code>, and the degree of <code>g</code> is lower than <code>degree f</code>.</p>

#### [ Johan Commelin (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089116):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Did you have stuff like that in your QR project?</p>

#### [ Patrick Massot (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089125):
<p>This is Euclidean division</p>

#### [ Patrick Massot (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089129):
<p>I think we have that</p>

#### [ Chris Hughes (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089131):
<p>It's in polynomial.lean</p>

#### [ Johan Commelin (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089132):
<p>Great</p>

#### [ Chris Hughes (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089135):
<p>dvd_iff_is_root or something</p>

#### [ Chris Hughes (Sep 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089258):
<p>Can't find it. We have similar stuff. <code>p %ₘ (X - C a) = C (p.eval a)</code> and <code>dvd_iff_mod_by_monic_eq_zero</code></p>

#### [ Johan Commelin (Sep 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089262):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Have you thought about PID → UFD in Lean?</p>

#### [ Chris Hughes (Sep 17 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089321):
<p>Euclidean_domain -&gt; UFD might be easier, and that all that's needed.</p>

#### [ Johannes Hölzl (Sep 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089398):
<p>I didn't think about it yet, but I surely want it. I guess that's my project for today  :-)</p>

#### [ Johan Commelin (Sep 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089401):
<p>Awesome!</p>

#### [ Johan Commelin (Sep 17 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089414):
<p>Your version of UFD is not a Prop. Do we also want a version where it is a prop?</p>

#### [ Patrick Massot (Sep 17 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089423):
<p>Johan, what's your plan? Are you still working towards a specific goal before the birthday?</p>

#### [ Johannes Hölzl (Sep 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089464):
<p>when is the b-day again?</p>

#### [ Johan Commelin (Sep 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089469):
<p>Friday</p>

#### [ Johan Commelin (Sep 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089474):
<p>I'm not competent enough to work on <code>pi</code></p>

#### [ Johan Commelin (Sep 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089476):
<p>Maybe I shouldn't distract the experts, and let them work on that.</p>

#### [ Patrick Massot (Sep 17 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089490):
<p>I think what is really needed is Mario and Johannes telling us whether they think anything from the kbb repository could be PR'ed on Friday</p>

#### [ Johan Commelin (Sep 17 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134096940):
<p>How would you even show that <code>K[X]</code> is an example of a UFD, with the current definition of UFD? You have to give an algorithm that factors polynomials, right? I'm not sure if those even exist for arbitrary <code>K</code>...</p>

#### [ Johan Commelin (Sep 17 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134096959):
<p>Or should we just use choice, somehow?</p>

#### [ Johan Commelin (Sep 17 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134096976):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> did you have a particular plan here?</p>

#### [ Johannes Hölzl (Sep 17 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134096996):
<p>Yes, in the worst case I will use <code>choice</code>.</p>

#### [ Johan Commelin (Sep 17 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134097036):
<p>Ok, I see</p>

#### [ Johan Commelin (Sep 17 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134098587):
<p>Here is a little hole in the <code>polynomial</code> api:</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">polynomial</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_semiring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">R</span><span class="o">]</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_id</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span> <span class="n">map</span> <span class="n">id</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">polynomial</span>
</pre></div>

#### [ Johan Commelin (Sep 17 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134098592):
<p>How would I unsorry that?</p>

#### [ Johannes Hölzl (Sep 17 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134098676):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> By the way, <code>kbb</code> doesn't build for me: <code>SL2Z_M.finitely_many_orbits</code> is missing</p>

#### [ Johannes Hölzl (Sep 17 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134098925):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> <code>eval₂</code> is defined using the <code>finsupp.sum</code> operator. The combination of <code>single_eq_C_mul_X</code> and <code>finsupp.sum_single</code> should be enough. With <code>sum_single</code> you can proof that the polynomial <code>f</code> has a sum representation over <code>single</code> and with <code>single_eq_C_mul_X</code> you change the representation to <code>C (id a) * X^n</code></p>

#### [ Johan Commelin (Sep 17 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134099100):
<blockquote>
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> By the way, <code>kbb</code> doesn't build for me: <code>SL2Z_M.finitely_many_orbits</code> is missing</p>
</blockquote>
<p>Aaah, Kenny changed this. It is now</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">finiteness</span> <span class="o">(</span><span class="n">hm</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">quotient</span> <span class="err">$</span> <span class="n">action_rel</span> <span class="err">$</span> <span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">fintype</span><span class="bp">.</span><span class="n">of_equiv</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">reps</span><span class="bp">.</span><span class="n">fintype</span> <span class="n">m</span> <span class="n">hm</span><span class="o">)</span> <span class="o">(</span><span class="n">reps_equiv</span> <span class="n">m</span> <span class="n">hm</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>
</pre></div>


<p>on lines 344-345 of <code>SL2Z_generators.lean</code></p>

#### [ Johan Commelin (Sep 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134099131):
<p>I think that error was in the Hecke operator file? I'm afraid that file won't really see any improvements. I don't have the time, and probably it is not realistic to work on it before Friday anyway.</p>

#### [ Johan Commelin (Sep 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134099330):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_id</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span> <span class="n">map</span> <span class="n">id</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">map</span><span class="o">,</span><span class="n">eval₂</span><span class="o">]</span><span class="bp">;</span> <span class="n">conv</span> <span class="o">{</span> <span class="n">to_lhs</span><span class="o">,</span> <span class="n">congr</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">funext</span><span class="o">,</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">single_eq_C_mul_X</span> <span class="o">}</span><span class="bp">;</span> <span class="n">simp</span>
</pre></div>

#### [ Johan Commelin (Sep 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134099343):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Thanks, done <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Johan Commelin (Sep 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134114645):
<p>I think that progress on splitting fields will require a bit of an api for <code>k[x]</code> as UFD. Things like units of <code>R[x]</code> is units of <code>R</code>. Every polynomial in <code>k[x]</code> of degree (not <code>nat_degree</code>!) equal to 0 is a unit, and vice versa. All polynomials of degree 1 are irreducible. Etc...</p>

#### [ Johan Commelin (Sep 17 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134114670):
<p>I have not started on any of this. But I also found myself mentally blocked on writing down the definition of a splitting field.</p>

#### [ Johan Commelin (Sep 17 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134114674):
<p>I suspect those issues are related.</p>

#### [ Johannes Hölzl (Sep 19 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134259146):
<p>I don't know if this is still needed, but PID -&gt; UFD is finished now</p>

#### [ Patrick Massot (Sep 19 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134259321):
<p>Nice! I think the hope was to make progress on splitting field, which will probably not happen very soon. But this is good to know anyway.</p>

#### [ Johan Commelin (Sep 19 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134260767):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Cool. Thanks a lot! I think this should help with the splitting fields branch. The next steps there are probably proving that non-zero constants are exactly the units and linear polynomials are irreducible.</p>

#### [ Johan Commelin (Sep 19 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134260795):
<p>Once that is know, I think we can start some sort of construction of splitting fields that inducts on the degree of the polynomial.</p>


{% endraw %}
