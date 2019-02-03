---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/83644continuousfunctiontopitype.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [continuous function to pi type](https://leanprover-community.github.io/archive/116395maths/83644continuousfunctiontopitype.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 23 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969544):
<p>I have no clue how to prove this:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous</span><span class="bp">.</span><span class="n">pi_mk</span> <span class="o">{</span><span class="n">X</span> <span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="o">[</span><span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">X</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">))</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span>
<span class="o">:</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969599):
<p>Can you prove it in maths?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969600):
<p>:-)</p>

#### [ Kevin Buzzard (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969604):
<p>i.e. "is it true"</p>

#### [ Johan Commelin (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969606):
<p>Unless I made a stupid mistake: yes</p>

#### [ Mario Carneiro (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969651):
<p>how is the pi topology defined?</p>

#### [ Johan Commelin (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969652):
<p>It just says that Pi is some sort of categorical product on steroids</p>

#### [ Kevin Buzzard (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969654):
<p>what Mario said</p>

#### [ Johan Commelin (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969657):
<p>If I have continuous maps to all the factors, I get a continuous map to the Pi</p>

#### [ Kevin Buzzard (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969658):
<p>(in Lean)</p>

#### [ Johan Commelin (May 23 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969660):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="k">Pi</span><span class="bp">.</span><span class="n">topological_space</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">t₂</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">a</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">β</span> <span class="n">a</span><span class="o">)]</span>
 <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="bp">Π</span><span class="n">a</span><span class="o">,</span> <span class="n">β</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="err">⨆</span><span class="n">a</span><span class="o">,</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">induced</span> <span class="o">(</span><span class="bp">λ</span><span class="n">f</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">t₂</span> <span class="n">a</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (May 23 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969668):
<p>so look for theorems about continuity on induced</p>

#### [ Johan Commelin (May 23 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969677):
<p>There are loads of those... but how do I deal with the <code>⨆a,</code> that is in front?</p>

#### [ Mario Carneiro (May 23 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969678):
<p>look for continuity on a Sup</p>

#### [ Johan Commelin (May 23 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969728):
<p>there is only continuity for <code>sup</code>, not <code>Sup</code></p>

#### [ Mario Carneiro (May 23 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969736):
<p>I think it's called that... serach for the bigcup</p>

#### [ Johan Commelin (May 23 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969740):
<p>I'm already down 5 rabbit holes, I really hope I don't need to go down this one as well...</p>

#### [ Johan Commelin (May 23 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969744):
<p>Search for <code>⨆</code> gives <code>No results</code> in <code>continuity.lean</code></p>

#### [ Mario Carneiro (May 23 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969801):
<p>hm, looks like it is missing from the list at <code>continuity.lean</code></p>

#### [ Johan Commelin (May 23 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969827):
<p>Right, there is constructors for products of two topological spaces, and continous maps towards them, etc... but for Pi types this seems missing. And I don't know exactly how to prove this stuff...</p>

#### [ Johan Commelin (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969872):
<p>/me doesn't know anything about <code>Sup</code> and friends</p>

#### [ Mario Carneiro (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969877):
<p>okay, so use the existing theorems as guides and write your own version for continuity on supr</p>

#### [ Johan Commelin (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969887):
<p>\me goes down rabbit hole # 6</p>

#### [ Mario Carneiro (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969888):
<p>(or I can, if this is going too far afield)</p>

#### [ Mario Carneiro (May 23 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969895):
<p>I'm just showing you what I would do</p>

#### [ Johan Commelin (May 23 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969908):
<p>Well, I'm trying to prove that the face map between two standard simplices is continuous...</p>

#### [ Johan Commelin (May 23 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126969975):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> At the moment, I don't even know how to write the statement for <code>Sup</code></p>

#### [ Mario Carneiro (May 23 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126970325):
<p>here you go:</p>
<div class="codehilite"><pre><span></span>lemma continuous_Sup_dom {t₁ : set (tspace α)} {t₂ : tspace β}
  {t : tspace α} (h₁ : t ∈ t₁) : cont t t₂ f → cont (Sup t₁) t₂ f :=
continuous_le_dom (le_Sup h₁)

lemma continuous_Sup_rng {t₁ : tspace α} {t₂ : set (tspace β)}
  (h : ∀t∈t₂, cont t₁ t f) : cont t₁ (Sup t₂) f :=
continuous_Inf_rng
  (λ t ht, show t ≤ coinduced f t₁, from h t ht)
  continuous_coinduced_rng

lemma continuous_supr_dom {t₁ : ι → tspace α} {t₂ : tspace β}
  {i : ι} : cont (t₁ i) t₂ f → cont (supr t₁) t₂ f :=
continuous_Sup_dom ⟨i, rfl⟩

lemma continuous_supr_rng {t₁ : tspace α} {t₂ : ι → tspace β}
  (h : ∀i, cont t₁ (t₂ i) f) : cont t₁ (supr t₂) f :=
continuous_Sup_rng $ assume t ⟨i, (t_eq : t = t₂ i)⟩, t_eq.symm ▸ h i
</pre></div>

#### [ Mario Carneiro (May 23 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126970334):
<p>I just copied the Inf stuff and dualized everything</p>

#### [ Johan Commelin (May 23 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126970571):
<p>Ok, thanks!</p>

#### [ Johan Commelin (May 23 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126970576):
<p>Let me see if I can continue with rabbit hole # 5 (-;</p>

#### [ Johan Commelin (May 23 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126971289):
<p>Hurray!</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous</span><span class="bp">.</span><span class="n">pi_mk</span> <span class="o">{</span><span class="n">X</span> <span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="o">[</span><span class="n">t₁</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">t₂</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">X</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">))</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span>
<span class="o">:</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="k">let</span> <span class="n">YY</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">Y</span> <span class="n">i</span><span class="o">),</span>
<span class="n">apply</span> <span class="n">continuous_Sup_rng</span><span class="o">,</span>
<span class="n">intros</span> <span class="n">t</span> <span class="n">ht</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">ht</span> <span class="k">with</span> <span class="n">i</span> <span class="n">hi</span><span class="o">,</span>
<span class="n">simp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
<span class="n">rw</span> <span class="n">hi</span><span class="o">,</span>
<span class="n">apply</span> <span class="n">continuous_induced_rng</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp</span><span class="o">,</span>
<span class="n">exact</span> <span class="n">H</span> <span class="n">i</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (May 23 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972217):
<p>Ok, so now I'm stuck with this MWE:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous_sums</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="o">((</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">univ</span><span class="bp">.</span><span class="n">sum</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johan Commelin (May 23 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972240):
<p>Whatever I try, I'm pulled hard into all sorts of <code>foldr</code> stuff. And I'm completely out of my comfort zone.</p>

#### [ Mario Carneiro (May 23 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972265):
<p>that's not a trivial theorem</p>

#### [ Johan Commelin (May 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972267):
<p>I would like to mumble some think like... well, addition is continuous... if you repeatedly add, you get continuity by induction</p>

#### [ Johan Commelin (May 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972274):
<p>Can I <code>foldr</code> the continuity proof off <code>add</code>?</p>

#### [ Mario Carneiro (May 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972276):
<p>I guess you can prove it by induction on <code>n</code>, you will need to show that <code>fin (succ n) -&gt; R</code> is homeomorphic to <code>R x (fin n -&gt; R)</code></p>

#### [ Johan Commelin (May 23 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972319):
<p>To link back to the discussion with Kevin, from about an hour ago... do you think this could be made into a trivial theorem?</p>

#### [ Mario Carneiro (May 23 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972322):
<p>no</p>

#### [ Mario Carneiro (May 23 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972365):
<p>okay, maybe that's too strong, you might be able to prove it by induction on the set instead</p>

#### [ Johan Commelin (May 23 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972371):
<p>that sounds closer to what I wanted to mumble</p>

#### [ Mario Carneiro (May 23 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972379):
<p>in that case you want to use <code>finset.induction_on</code></p>

#### [ Mario Carneiro (May 23 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972424):
<p>and the IH says that a sum of continuous functions over set s is continuous</p>

#### [ Johan Commelin (May 23 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126972492):
<p>Ok, I'm going to try this. Thanks!</p>

#### [ Patrick Massot (May 23 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126974780):
<p>Johan, you may already know, but just in case: there very easy clean up steps you can run on such proofs. <code>YY</code> is never used. <code>unfold</code> is actually much less useful that one thinks in the beginning, so I always try to remove all <code>unfold</code> once a proof work. And then we always try to get rid of <code>simp</code> in the middle of proofs. The result is:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous</span><span class="bp">.</span><span class="n">pi_mk</span> <span class="o">{</span><span class="n">X</span> <span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="o">[</span><span class="n">t₁</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">t₂</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">X</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">))</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span>
<span class="o">:</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">apply</span> <span class="n">continuous_Sup_rng</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">t</span> <span class="n">ht</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">ht</span> <span class="k">with</span> <span class="n">i</span> <span class="n">hi</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">hi</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">continuous_induced_rng</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">H</span> <span class="n">i</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (May 23 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126974828):
<p>Out of curiosity, I also tried to build a term proof, but haven't succeeded because of the mysterious rewrite in the middle (which rewrites implicit arguments, which has the weird effect of not changing the visible goal)</p>

#### [ Patrick Massot (May 23 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126974838):
<p>I can't get more obfuscated than:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous</span><span class="bp">.</span><span class="n">pi_mk</span> <span class="o">{</span><span class="n">X</span> <span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="o">[</span><span class="n">t₁</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">t₂</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">X</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">))</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span>
<span class="o">:</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">continuous_Sup_rng</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">t</span> <span class="n">ht</span><span class="o">,</span> <span class="k">match</span> <span class="n">ht</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">hi</span> <span class="bp">;</span> <span class="n">apply</span> <span class="n">continuous_induced_rng</span> <span class="bp">;</span> <span class="n">exact</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)</span> <span class="kn">end</span>
</pre></div>

#### [ Johannes Hölzl (May 23 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126974960):
<p>For the sum proof: its easiest to generalize for finset, and then go from list to multiset to finset. I will add this to mathlib:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous_supr_rng</span>
  <span class="o">{</span><span class="n">ι</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">t₁</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">t₂</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">topological_space</span> <span class="n">β</span><span class="o">}</span>
  <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="bp">@</span><span class="n">continuous</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">t₁</span> <span class="o">(</span><span class="n">t₂</span> <span class="n">i</span><span class="o">)</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">continuous</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">t₁</span> <span class="o">(</span><span class="n">lattice</span><span class="bp">.</span><span class="n">supr</span> <span class="n">t₂</span><span class="o">)</span> <span class="n">f</span> <span class="o">:=</span>
<span class="n">continuous_iff_le_coinduced</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">supr_le</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">i</span><span class="o">,</span> <span class="n">continuous_iff_le_coinduced</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">h</span> <span class="n">i</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">continuous</span><span class="bp">.</span><span class="n">pi_mk</span>
  <span class="o">{</span><span class="n">X</span> <span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">t₁</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">t₂</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">)]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">X</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">))</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">continuous_supr_rng</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">i</span><span class="o">,</span> <span class="n">continuous_induced_rng</span> <span class="err">$</span> <span class="n">H</span> <span class="n">i</span>

<span class="kn">lemma</span> <span class="n">continuous_list_sum</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_add_monoid</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span>
  <span class="bp">∀</span><span class="n">l</span><span class="o">:</span><span class="n">list</span> <span class="n">γ</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span><span class="n">c</span><span class="err">∈</span><span class="n">l</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="n">c</span><span class="o">))</span> <span class="bp">→</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span><span class="n">a</span><span class="o">,</span> <span class="o">(</span><span class="n">l</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span><span class="n">c</span><span class="o">,</span> <span class="n">f</span> <span class="n">c</span> <span class="n">a</span><span class="o">))</span><span class="bp">.</span><span class="n">sum</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">[]</span>       <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">continuous_const</span><span class="o">]</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">f</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span> <span class="n">h</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">simp</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">continuous_add</span>
      <span class="o">(</span><span class="n">h</span> <span class="n">f</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">mem_cons_self</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
      <span class="o">(</span><span class="n">continuous_list_sum</span> <span class="n">l</span> <span class="o">(</span><span class="k">assume</span> <span class="n">c</span> <span class="n">hc</span><span class="o">,</span> <span class="n">h</span> <span class="n">c</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">mem_cons_of_mem</span> <span class="bp">_</span> <span class="n">hc</span><span class="o">)))</span>
  <span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">continuous_multiset_sum</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_add_monoid</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∀</span><span class="n">c</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="n">c</span><span class="o">))</span> <span class="bp">→</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span><span class="n">a</span><span class="o">,</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span><span class="n">c</span><span class="o">,</span> <span class="n">f</span> <span class="n">c</span> <span class="n">a</span><span class="o">))</span><span class="bp">.</span><span class="n">sum</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">quot</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">continuous_list_sum</span>

<span class="kn">lemma</span> <span class="n">continuous_finset_sum</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_add_monoid</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∀</span><span class="n">c</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="n">c</span><span class="o">))</span> <span class="bp">→</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span><span class="n">a</span><span class="o">,</span> <span class="n">s</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span><span class="n">c</span><span class="o">,</span> <span class="n">f</span> <span class="n">c</span> <span class="n">a</span><span class="o">))</span> <span class="o">:=</span>
<span class="n">continuous_multiset_sum</span> <span class="bp">_</span>
</pre></div>

#### [ Johan Commelin (May 23 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126975014):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Yes, you are completely right. But it seems the work is now already done (-;</p>

#### [ Mario Carneiro (May 23 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126975238):
<p>you can see how Johannes built the term proof for <code>pi_mk</code>; the key is to use <code>continuous_supr_rng</code> not <code>continuous_Sup_rng</code> because the definition uses <code>supr</code> (the indexed supremum) not <code>Sup</code> (the set supremum). In fact <code>supr</code> is defined in terms of <code>Sup</code>, but if you apply the wrong theorem it unfolds this definition and things get harder.</p>

#### [ Johan Commelin (May 23 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126975550):
<p>Yes, I will take a closer look. I think I can learn a lot from how Johannes improved my kludge</p>

#### [ Patrick Massot (May 23 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126975794):
<p>Sure. But this is too efficient in a sense. My message was focused on easy local clean up, that you can actually do without any understanding of the proof. Of course this is only the first step. Really efficient proofs like Johannes' require actual thinking</p>

#### [ Mario Carneiro (May 23 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126975891):
<p>you can also look at my term proof of <code>continuous_supr_rng</code>, which uses the <code>\t</code> for rewriting</p>

#### [ Patrick Massot (May 23 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126975965):
<p>I'm a bit frustrated by this \t thing. I know it's somehow the term version of <code>rw</code> and I see it everywhere in mathlib, but I was almost never able to use it</p>

#### [ Mario Carneiro (May 23 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126975978):
<p>I admit it was a bit delicate for me at first</p>

#### [ Mario Carneiro (May 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126976035):
<p>it is so much weaker than the lean 2 version, it fails whenever the expected type or the thing to rewrite with has metavariables</p>

#### [ Johan Commelin (May 23 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126976056):
<p>Anyway, I just proved that the face map between standard simplices is continuous!</p>

#### [ Johan Commelin (May 23 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126976057):
<p>The proof is not cleaned up. But it works (-;</p>

#### [ Mario Carneiro (May 23 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126976067):
<p>but it's often just the thing when you want to rewrite with an equality in the context</p>

#### [ Patrick Massot (May 23 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126976197):
<p>What about my attempt? Can you use \t there? (without switching to <code>continuous_supr_rng</code>)</p>

#### [ Mario Carneiro (May 23 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126976271):
<p>yes, the proof should be almost identical to the one I pointed at</p>

#### [ Johan Commelin (May 23 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126976317):
<p>Ok, like I said, the proofs are still ugly. But here goes nothing: <a href="https://github.com/jcommelin/mathlib/commit/fec9db2028bea163352f574055dad44029d04788" target="_blank" title="https://github.com/jcommelin/mathlib/commit/fec9db2028bea163352f574055dad44029d04788">https://github.com/jcommelin/mathlib/commit/fec9db2028bea163352f574055dad44029d04788</a></p>

#### [ Mario Carneiro (May 23 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126976321):
<div class="codehilite"><pre><span></span>lemma continuous.pi_mk
  {X I : Type*} {Y : I → Type*} [t₁ : topological_space X] [t₂ : Πi, topological_space (Y i)]
  (f : Πi, X → (Y i)) (H : Πi, continuous (f i)) :
  continuous (λ x i, f i x) :=
continuous_Sup_rng $ assume t ⟨i, e⟩, e.symm ▸ continuous_induced_rng (H i)
</pre></div>

#### [ Patrick Massot (May 23 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126980416):
<p>Hum, I think I stupidly missed the <code>eq.symm</code> when I tried</p>

#### [ Johannes Hölzl (May 23 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126981716):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I forgot that there is already <code>tendsto_sum</code>, so you could also derive <code>continuous_finset_sum</code> from this.<br>
Anyway, this all is now in mathlib.</p>

#### [ Johan Commelin (May 23 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20function%20to%20pi%20type/near/126985262):
<p>Thanks a lot! I will merge into my fork. Once I clean my stuff up, I think I will make a PR</p>


{% endraw %}
