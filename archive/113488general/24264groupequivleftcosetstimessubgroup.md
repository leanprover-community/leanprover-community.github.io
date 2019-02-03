---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24264groupequivleftcosetstimessubgroup.html
---

## Stream: [general](index.html)
### Topic: [group_equiv_left_cosets_times_subgroup](24264groupequivleftcosetstimessubgroup.html)

---


{% raw %}
#### [ Kenny Lau (Apr 16 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140026):
<div class="codehilite"><pre><span></span>import data.equiv group_theory.coset

universe u

namespace quotient

variables {α : Type u} [s : setoid α]

def fibre : quotient s → set α :=
λ Q, {x | ⟦x⟧ = Q}

end quotient

namespace equiv

variables {α : Type u} [s : setoid α]

def equiv_fibre : α ≃ Σ Q : quotient s, quotient.fibre Q :=
⟨λ x, ⟨⟦x⟧, x, rfl⟩, λ x, x.2.1, λ x, rfl,
 λ ⟨Q, x, (hx : ⟦x⟧ = Q)⟩, sigma.eq hx $ by subst hx⟩

end equiv

variables {G : Type u} [group G] (S : set G) [is_subgroup S]

instance left_rel : setoid G :=
⟨λ x y, x⁻¹ * y ∈ S,
 λ x, by simp [is_submonoid.one_mem],
 λ x y hxy, have _ := is_subgroup.inv_mem hxy, by simpa using this,
 λ x y z hxy hyz, have _ := is_submonoid.mul_mem hxy hyz, by simpa [mul_assoc] using this⟩

def left_cosets&#39; : Type u := quotient (left_rel S)

namespace is_subgroup

theorem fibre_equiv (L : left_cosets&#39; S) : nonempty (quotient.fibre L ≃ S) :=
⟨⟨λ x, ⟨(quotient.out L)⁻¹ * x.1, quotient.exact ((quotient.out_eq L).trans x.2.symm)⟩,
  λ x, ⟨quotient.out L * x.1, eq.trans (eq.symm $ quotient.sound $ by simpa [(≈), setoid.r] using x.2) (quotient.out_eq L)⟩,
  λ ⟨x, hx⟩, subtype.eq $ by simp,
  λ ⟨x, hx⟩, subtype.eq $ by simp⟩⟩

theorem group_equiv_left_cosets_times_subgroup&#39; : nonempty (G ≃ (left_cosets&#39; S × S)) :=
⟨calc G
    ≃ Σ L : left_cosets&#39; S, quotient.fibre L :
  equiv.equiv_fibre
... ≃ Σ L : left_cosets&#39; S, S :
  equiv.sigma_congr_right (λ L, classical.choice $ fibre_equiv _ _)
... ≃ (left_cosets&#39; S × S) :
  equiv.sigma_equiv_prod _ _ ⟩

end is_subgroup
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140057):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> do you think this is better than the one in mathlib?</p>

#### [ Kenny Lau (Apr 16 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140116):
<p><a href="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean">https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean</a></p>

#### [ Mario Carneiro (Apr 16 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140219):
<p>I suggest skipping the <code>nonempty</code> here, there's not much point to it</p>

#### [ Kenny Lau (Apr 16 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140222):
<p>it is uncomputable</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140223):
<p>ok</p>

#### [ Kenny Lau (Apr 16 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140224):
<p>but I'm making verseion 2 where that is computable</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140231):
<p>just use <code>noncomputable def</code> instead</p>

#### [ Kenny Lau (Apr 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140234):
<p>oh?</p>

#### [ Kenny Lau (Apr 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140235):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> what do you think</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140237):
<p>it's definitely a classical theorem, but wrapping in <code>nonempty</code> just means using <code>choice</code> later</p>

#### [ Johannes Hölzl (Apr 16 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140276):
<p>I agree with Mario, using nonempty was a bad idea on my side.</p>

#### [ Kenny Lau (Apr 16 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140277):
<p>ok</p>

#### [ Kenny Lau (Apr 16 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140433):
<div class="codehilite"><pre><span></span>import data.equiv group_theory.coset

universe u

namespace quotient

variables {α : Type u} [s : setoid α]

def fibre : quotient s → set α :=
λ Q, {x | ⟦x⟧ = Q}

end quotient

namespace equiv

variables {α : Type u} [s : setoid α]

def equiv_fibre : α ≃ Σ Q : quotient s, quotient.fibre Q :=
⟨λ x, ⟨⟦x⟧, x, rfl⟩, λ x, x.2.1, λ x, rfl,
 λ ⟨Q, x, (hx : ⟦x⟧ = Q)⟩, sigma.eq hx $ by subst hx⟩

end equiv

variables {G : Type u} [group G] (S : set G) [is_subgroup S]

instance left_rel : setoid G :=
⟨λ x y, x⁻¹ * y ∈ S,
 λ x, by simp [is_submonoid.one_mem],
 λ x y hxy, have _ := is_subgroup.inv_mem hxy, by simpa using this,
 λ x y z hxy hyz, have _ := is_submonoid.mul_mem hxy hyz, by simpa [mul_assoc] using this⟩

def left_cosets&#39; : Type u := quotient (left_rel S)

namespace is_subgroup

def fibre_equiv (g : G) : quotient.fibre ⟦g⟧ ≃ S :=
⟨λ x, ⟨x.1⁻¹ * g, quotient.exact x.2⟩,
 λ x, ⟨g * x⁻¹, quotient.sound $ by simpa [(≈), setoid.r] using x.2⟩,
 λ ⟨x, hx⟩, subtype.eq $ by simp,
 λ ⟨g, hg⟩, subtype.eq $ by simp⟩

noncomputable def group_equiv_left_cosets_times_subgroup&#39; :
  G ≃ (left_cosets&#39; S × S) :=
calc G ≃ Σ L : left_cosets&#39; S, quotient.fibre L :
  equiv.equiv_fibre
    ... ≃ Σ L : left_cosets&#39; S, quotient.fibre ⟦quotient.out L⟧ :
  equiv.sigma_congr_right (λ L, by simp)
    ... ≃ Σ L : left_cosets&#39; S, S :
  equiv.sigma_congr_right (λ L, fibre_equiv _ _)
    ... ≃ (left_cosets&#39; S × S) :
  equiv.sigma_equiv_prod _ _

end is_subgroup
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140434):
<p>version 2</p>

#### [ Kenny Lau (Apr 16 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140441):
<p>who is Mitchell Rowett?</p>

#### [ Kevin Buzzard (Apr 16 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140442):
<p>Student of Scott?</p>

#### [ Kevin Buzzard (Apr 16 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140443):
<p>UG I think</p>

#### [ Kenny Lau (Apr 16 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140486):
<p>would he/she mind if, you know, I basically refactor the whole thing</p>

#### [ Kevin Buzzard (Apr 16 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140487):
<p>Isn't the logic of doing the non-empty version that you can go from that to the noncomputable version but you can't go back?</p>

#### [ Kenny Lau (Apr 16 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140495):
<p>I don't get you</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140498):
<p>full file refactorings are permitted in mathlib, you don't need permission from the original author (and conversely, be prepared for your work to be refactored to unrecognizability in the future)</p>

#### [ Kenny Lau (Apr 16 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140537):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> should I refactor coset?</p>

#### [ Johannes Hölzl (Apr 16 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140538):
<p>Mitchel did the coset theory, the things your changing were mine. I think we can add a more general version of <code>equiv_fibre</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">equiv</span>

<span class="n">def</span> <span class="n">equiv_fibre</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="err">Σ</span><span class="n">b</span><span class="o">:</span><span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="o">{</span><span class="n">b</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨λ</span><span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">a</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">have</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">hx</span><span class="o">,</span> <span class="n">sigma</span><span class="bp">.</span><span class="n">eq</span> <span class="n">this</span> <span class="o">(</span><span class="k">by</span> <span class="n">subst</span> <span class="n">this</span><span class="bp">;</span> <span class="n">refl</span><span class="o">)</span><span class="bp">⟩</span>

<span class="kn">end</span> <span class="n">equiv</span>
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140540):
<p>how do you make those red rectangles?</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140543):
<p><code> ```lean ... ``` </code></p>

#### [ Johannes Hölzl (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140548):
<p>I don't know were they come from. I just copied stuff from vs code.</p>

#### [ Kenny Lau (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140550):
<p>I mean red rectangles</p>

#### [ Kenny Lau (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140551):
<p>oh, lean</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140553):
<p>the red rectangles are what happens when the syntax highlighter gets confused</p>

#### [ Kenny Lau (Apr 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140556):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> did I tell you how much I hate <code>{b}</code>?</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140601):
<p>On further review, I'm not sure it can be changed, the definition <code>singleton a = insert a empty</code> is in core.lean</p>

#### [ Johannes Hölzl (Apr 16 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140650):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  you shouldn't depend too much on definitional equality. It breaks modularity of the library.</p>

#### [ Kenny Lau (Apr 16 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140692):
<p>don't you like it when every theorem is just <code>rfl</code>?</p>

#### [ Johannes Hölzl (Apr 16 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140694):
<p>Of course I like it, but I also hate it to not be able to change a definition because it would break 1000 places in mathlib.</p>

#### [ Kenny Lau (Apr 16 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140699):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">coset</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>

<span class="n">def</span> <span class="n">fibre</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>

<span class="kn">namespace</span> <span class="n">equiv</span>

<span class="n">def</span> <span class="n">equiv_fibre</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">fibre</span> <span class="n">f</span> <span class="n">y</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">sigma</span><span class="bp">.</span><span class="n">eq</span> <span class="n">hx</span> <span class="err">$</span> <span class="k">by</span> <span class="n">subst</span> <span class="n">hx</span><span class="bp">⟩</span>

<span class="kn">end</span> <span class="n">equiv</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">G</span><span class="o">)</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">S</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">left_rel</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">G</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="bp">⁻¹</span> <span class="bp">*</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span><span class="o">],</span>
 <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hxy</span><span class="o">,</span> <span class="k">have</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="n">hxy</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">hxy</span> <span class="n">hyz</span><span class="o">,</span> <span class="k">have</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">hxy</span> <span class="n">hyz</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">mul_assoc</span><span class="o">]</span> <span class="kn">using</span> <span class="n">this</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">left_cosets&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="n">left_rel</span> <span class="n">S</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">is_subgroup</span>

<span class="n">def</span> <span class="n">fibre_equiv</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">G</span><span class="o">)</span> <span class="o">:</span> <span class="n">fibre</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="err">⟦</span><span class="n">g</span><span class="err">⟧</span> <span class="err">≃</span> <span class="n">S</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⁻¹</span> <span class="bp">*</span> <span class="n">g</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">exact</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">g</span> <span class="bp">*</span> <span class="n">x</span><span class="bp">⁻¹</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[(</span><span class="bp">≈</span><span class="o">),</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">r</span><span class="o">]</span> <span class="kn">using</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">hg</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">group_equiv_left_cosets_times_subgroup&#39;</span> <span class="o">:</span>
  <span class="n">G</span> <span class="err">≃</span> <span class="o">(</span><span class="n">left_cosets&#39;</span> <span class="n">S</span> <span class="bp">×</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">G</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">L</span> <span class="o">:</span> <span class="n">left_cosets&#39;</span> <span class="n">S</span><span class="o">,</span> <span class="n">fibre</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="n">L</span> <span class="o">:</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">equiv_fibre</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span>
    <span class="bp">...</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">L</span> <span class="o">:</span> <span class="n">left_cosets&#39;</span> <span class="n">S</span><span class="o">,</span> <span class="n">fibre</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="err">⟦</span><span class="n">quotient</span><span class="bp">.</span><span class="n">out</span> <span class="n">L</span><span class="err">⟧</span> <span class="o">:</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">sigma_congr_right</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">L</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">)</span>
    <span class="bp">...</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">L</span> <span class="o">:</span> <span class="n">left_cosets&#39;</span> <span class="n">S</span><span class="o">,</span> <span class="n">S</span> <span class="o">:</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">sigma_congr_right</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">L</span><span class="o">,</span> <span class="n">fibre_equiv</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
    <span class="bp">...</span> <span class="err">≃</span> <span class="o">(</span><span class="n">left_cosets&#39;</span> <span class="n">S</span> <span class="bp">×</span> <span class="n">S</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">sigma_equiv_prod</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="kn">end</span> <span class="n">is_subgroup</span>
</pre></div>

#### [ Johannes Hölzl (Apr 16 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140701):
<p>In Isabelle one can always change a definition, make it more general. And then just prove that it is the same.</p>

#### [ Kenny Lau (Apr 16 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140703):
<p>Isabelle is crap</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140750):
<p>be sure to have good reasons to make invective statements</p>

#### [ Kenny Lau (Apr 16 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140751):
<p>it's nonconstructive</p>

#### [ Johannes Hölzl (Apr 16 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140757):
<p>Well, your claim is also nonconstructive</p>

#### [ Kenny Lau (Apr 16 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140758):
<p>so how is version 3?</p>

#### [ Johannes Hölzl (Apr 16 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140802):
<p>I think we should stay with <code>f ⁻¹' {b}</code>.</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140854):
<p>the other advantage of not giving the definition a name is we don't need to debate if it should be <code>fibre</code> or <code>fiber</code> <span class="emoji emoji-1f643" title="upside down face">:upside_down_face:</span></p>

#### [ Kenny Lau (Apr 16 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140857):
<p>who cares about cosets of sub-not-groups?</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140863):
<p>I guess Patrick might, that is the same as the translate of a set</p>

#### [ Kenny Lau (Apr 16 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140905):
<p>why would he care?</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125140998):
<p>it relates to affine spaces and the group conjugation action. It also comes up with "neighborhoods of zero" in a topological group</p>

#### [ Kenny Lau (Apr 16 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141009):
<p>singleton is really unusable</p>

#### [ Kenny Lau (Apr 16 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141102):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">coset</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">namespace</span> <span class="n">equiv</span>

<span class="n">def</span> <span class="n">equiv_fib</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">α</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">sigma</span><span class="bp">.</span><span class="n">eq</span> <span class="n">hx</span> <span class="err">$</span> <span class="k">by</span> <span class="n">subst</span> <span class="n">hx</span><span class="bp">⟩</span>

<span class="kn">end</span> <span class="n">equiv</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">G</span><span class="o">)</span> <span class="o">[</span><span class="n">is_subgroup</span> <span class="n">S</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">left_rel</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">G</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="bp">⁻¹</span> <span class="bp">*</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span><span class="o">],</span>
 <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hxy</span><span class="o">,</span> <span class="k">have</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">is_subgroup</span><span class="bp">.</span><span class="n">inv_mem</span> <span class="n">hxy</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">hxy</span> <span class="n">hyz</span><span class="o">,</span> <span class="k">have</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">hxy</span> <span class="n">hyz</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">mul_assoc</span><span class="o">]</span> <span class="kn">using</span> <span class="n">this</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">left_cosets&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="n">left_rel</span> <span class="n">S</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">is_subgroup</span>

<span class="n">def</span> <span class="n">fib_equiv</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">G</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="err">⟦</span><span class="n">x</span><span class="err">⟧</span> <span class="bp">=</span> <span class="err">⟦</span><span class="n">g</span><span class="err">⟧</span><span class="o">}</span> <span class="err">≃</span> <span class="n">S</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⁻¹</span> <span class="bp">*</span> <span class="n">g</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">exact</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">g</span> <span class="bp">*</span> <span class="n">x</span><span class="bp">⁻¹</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[(</span><span class="bp">≈</span><span class="o">),</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">r</span><span class="o">]</span> <span class="kn">using</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">hg</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">group_equiv_left_cosets_times_subgroup&#39;</span> <span class="o">:</span>
  <span class="n">G</span> <span class="err">≃</span> <span class="o">(</span><span class="n">left_cosets&#39;</span> <span class="n">S</span> <span class="bp">×</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">G</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">L</span> <span class="o">:</span> <span class="n">left_cosets&#39;</span> <span class="n">S</span><span class="o">,</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="err">⟦</span><span class="n">x</span><span class="err">⟧</span> <span class="bp">=</span> <span class="n">L</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">equiv_fib</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span>
    <span class="bp">...</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">L</span> <span class="o">:</span> <span class="n">left_cosets&#39;</span> <span class="n">S</span><span class="o">,</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="err">⟦</span><span class="n">x</span><span class="err">⟧</span> <span class="bp">=</span> <span class="err">⟦</span><span class="n">quotient</span><span class="bp">.</span><span class="n">out</span> <span class="n">L</span><span class="err">⟧</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">sigma_congr_right</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">L</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">)</span>
    <span class="bp">...</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">L</span> <span class="o">:</span> <span class="n">left_cosets&#39;</span> <span class="n">S</span><span class="o">,</span> <span class="n">S</span> <span class="o">:</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">sigma_congr_right</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">L</span><span class="o">,</span> <span class="n">fib_equiv</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
    <span class="bp">...</span> <span class="err">≃</span> <span class="o">(</span><span class="n">left_cosets&#39;</span> <span class="n">S</span> <span class="bp">×</span> <span class="n">S</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">equiv</span><span class="bp">.</span><span class="n">sigma_equiv_prod</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="kn">end</span> <span class="n">is_subgroup</span>
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141108):
<p>conflict between <code>fibre</code> and <code>fiber</code> resolved :P</p>

#### [ Chris Hughes (Apr 16 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141154):
<p>Slightly shortened.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">equiv_fib</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">α</span> <span class="err">≃</span> <span class="err">Σ</span> <span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">hx</span><span class="bp">⟩⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141160):
<p>you win</p>

#### [ Mario Carneiro (Apr 16 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141203):
<p>it's a bit weird to write <code> ⟨hx⟩</code> in the last bit there, since it's refl. Use <code>λ ⟨_, x, rfl⟩, rfl</code> instead</p>

#### [ Kenny Lau (Apr 16 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141322):
<p>wait, how does that also work :o</p>

#### [ Kenny Lau (Apr 16 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group_equiv_left_cosets_times_subgroup/near/125141327):
<p>oh, automatic casing</p>


{% endraw %}
