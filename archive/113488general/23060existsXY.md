---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23060existsXY.html
---

## Stream: [general](index.html)
### Topic: [exists (X) (Y)](23060existsXY.html)

---


{% raw %}
#### [ Kevin Buzzard (May 17 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126709974):
<p><code>topological_space.is_topological_basis</code> has, as part of its definition, <code>∃ (t₃ : set α) (H : t₃ ∈ s), x ∈ t₃ ∧ ...</code>, that is, "there exists a set with some property such that..."</p>

#### [ Kevin Buzzard (May 17 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126709984):
<p>So I've just sat down to write some trivial thing and it's ended up like this:</p>

#### [ Kevin Buzzard (May 17 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126709996):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)}</span>

<span class="kn">definition</span> <span class="n">basis_nhds</span> <span class="o">(</span><span class="n">HB</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span> <span class="bp">∧</span> <span class="n">U</span> <span class="err">∈</span> <span class="n">B</span><span class="o">}</span>

<span class="n">noncomputable</span> <span class="kn">instance</span> <span class="n">basis_nhds_has_so_called_sup</span> <span class="o">(</span><span class="n">HB</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="n">lattice</span><span class="bp">.</span><span class="n">has_sup</span> <span class="o">(</span><span class="n">basis_nhds</span> <span class="n">HB</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">sup</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Us</span> <span class="n">Vs</span><span class="o">,</span> <span class="k">begin</span>
    <span class="n">cases</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="bp">_</span> <span class="o">(</span><span class="n">HB</span><span class="bp">.</span><span class="mi">1</span> <span class="n">Us</span><span class="bp">.</span><span class="mi">1</span> <span class="n">Us</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span> <span class="n">Vs</span><span class="bp">.</span><span class="mi">1</span> <span class="n">Vs</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span> <span class="n">x</span> <span class="bp">⟨</span><span class="n">Us</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="n">Vs</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⟩</span><span class="o">))</span>
      <span class="k">with</span> <span class="n">W</span> <span class="n">HW</span><span class="o">,</span>
    <span class="n">cases</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="bp">_</span> <span class="n">HW</span><span class="o">)</span> <span class="k">with</span> <span class="n">HB</span> <span class="n">HW</span><span class="o">,</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">W</span><span class="o">,</span><span class="bp">⟨</span><span class="n">HW</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="n">HB</span><span class="bp">⟩⟩</span>
  <span class="kn">end</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 17 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710000):
<p>[this is all your fault <span class="user-mention" data-user-id="110064">@Kenny Lau</span> ]</p>

#### [ Kevin Buzzard (May 17 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710018):
<p>I want to define a function "sup", so I need some classical stuff to pull out witnesses for the exists</p>

#### [ Kevin Buzzard (May 17 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710067):
<p>and I have to run it twice because it's "exists this, such that exists that, such that..."</p>

#### [ Kevin Buzzard (May 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710139):
<p>Based on the "it's trivial so write a one-liner in term mode" principle I'd ideally like to write a one-liner in term mode, but writing <code>classical.indefinite_description</code> twice fills up most of the line already :-/</p>

#### [ Kevin Buzzard (May 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126710140):
<p>Is there a trick I'm missing?</p>

#### [ Reid Barton (May 17 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126717885):
<p>This only saves one of your lines, but for <code>∃ (H : p), q</code> where <code>p</code> is a <code>Prop</code>, check out <code>Exists.fst</code> and <code>Exists.snd</code>.<br>
You can eliminate the second line and change the third to <code>exact ⟨W,⟨HW.snd.1,HW.fst⟩⟩</code></p>

#### [ Reid Barton (May 17 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126718073):
<p>This little detail about how <code>∃ t₃∈s, ...</code> means <code>∃ t₃, ∃ H : (t₃∈s), ...</code> is a bit annoying in this case, but using <code>.fst</code> and <code>.snd</code> you can pretty much pretend it actually means <code>∃ t₃, t₃∈s ∧ ...</code></p>

#### [ Kevin Buzzard (May 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719052):
<p>Here's a mathlib-free version of what I'm moaning about:</p>

#### [ Kevin Buzzard (May 17 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719053):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">p</span> <span class="n">x</span><span class="o">),</span> <span class="n">q</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="bp">_</span> <span class="n">H</span><span class="o">)</span> <span class="k">with</span> <span class="n">x</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="bp">_</span> <span class="n">H2</span><span class="o">)</span> <span class="k">with</span> <span class="n">H3</span> <span class="n">H4</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">r</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="n">H3</span><span class="o">,</span><span class="n">H4</span><span class="bp">⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (May 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719176):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">p</span> <span class="n">x</span><span class="o">),</span> <span class="n">q</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="bp">_</span> <span class="n">H</span><span class="o">)</span> <span class="k">with</span> <span class="n">x</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">r</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="n">H2</span><span class="bp">.</span><span class="n">fst</span><span class="o">,</span><span class="n">H2</span><span class="bp">.</span><span class="n">snd</span><span class="bp">⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719179):
<p>Aah I see <span class="user-mention" data-user-id="110032">@Reid Barton</span>  -- thanks for these tips.</p>

#### [ Kevin Buzzard (May 17 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719190):
<p>I hadn't really internalised why there were two exists, or the trick with "exists proof".</p>

#### [ Reid Barton (May 17 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719195):
<p>or</p>
<div class="codehilite"><pre><span></span><span class="k">let</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="n">H2</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="bp">_</span> <span class="n">H</span> <span class="k">in</span> <span class="n">r</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="n">H2</span><span class="bp">.</span><span class="n">fst</span><span class="o">,</span><span class="n">H2</span><span class="bp">.</span><span class="n">snd</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 17 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126719240):
<p>let cases := classical.indefinite_description _ :-/</p>

#### [ Mario Carneiro (May 18 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722300):
<p>I would prefer to do the proof in two stages, first showing it's directed and then extracting the witness</p>
<div class="codehilite"><pre><span></span>section
variables {X : Type u} [topological_space X] {B : set (set X)}
variables (HB : topological_space.is_topological_basis B) (x : X)
include HB

definition basis_nhds := {U : set X // x ∈ U ∧ U ∈ B}

theorem basis_nhds_directed (U V : basis_nhds HB x) :
  ∃ W : basis_nhds HB x, W.1 ⊆ U.1 ∧ W.1 ⊆ V.1 :=
let ⟨W, h₁, h₂, h₃⟩ := HB.1 _ U.2.2 _ V.2.2 _ ⟨U.2.1, V.2.1⟩ in
⟨⟨W, h₂, h₁⟩, set.subset_inter_iff.1 h₃⟩

noncomputable instance basis_nhds_has_so_called_sup :
  lattice.has_sup (basis_nhds HB x) :=
{ sup := λ Us Vs, classical.some (basis_nhds_directed HB x Us Vs) }
end
</pre></div>


<p>You don't need <code>indefinite_description</code> here since you don't need the proof part for the definition</p>

#### [ Kevin Buzzard (May 18 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722619):
<p>Of course I need it the moment I want to prove <code>le_sup_left</code>, but I got distracted by all the function.comp shenannigans in the other thread and never got to this bit :-/</p>

#### [ Kevin Buzzard (May 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722676):
<p>This is a much better approach though -- my initial attempt ran into problems when I tried proving <code>le_sup_left</code> because my definition used tactics so wouldn't unfold definitionally when I wanted it to. This is a much better idea.</p>

#### [ Kevin Buzzard (May 18 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722729):
<p>So many tricks still to learn!</p>

#### [ Mario Carneiro (May 18 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722943):
<div class="codehilite"><pre><span></span>section
variables {X : Type u} [topological_space X] {B : set (set X)}
variables (HB : topological_space.is_topological_basis B) (x : X)
include HB

definition basis_nhds := {U : set X // x ∈ U ∧ U ∈ B}

instance : partial_order (basis_nhds HB x) :=
{ le := λ u v, v.1 ⊆ u.1,
  le_refl := λ u, set.subset.refl u.1,
  le_trans := λ u v w uv vw, set.subset.trans vw uv,
  le_antisymm := λ u v vu uv, subtype.eq $ set.subset.antisymm uv vu }

theorem basis_nhds_directed (U V : basis_nhds HB x) :
  ∃ W : basis_nhds HB x, U ≤ W ∧ V ≤ W :=
let ⟨W, h₁, h₂, h₃⟩ := HB.1 _ U.2.2 _ V.2.2 _ ⟨U.2.1, V.2.1⟩ in
⟨⟨W, h₂, h₁⟩, set.subset_inter_iff.1 h₃⟩

noncomputable instance basis_nhds_has_so_called_sup :
  lattice.has_sup (basis_nhds HB x) :=
{ sup := λ Us Vs, classical.some (basis_nhds_directed HB x Us Vs) }

theorem sup_le_left (u v : basis_nhds HB x) : u ≤ u ⊔ v :=
(classical.some_spec (basis_nhds_directed HB x u v)).1

theorem sup_le_right (u v : basis_nhds HB x) : v ≤ u ⊔ v :=
(classical.some_spec (basis_nhds_directed HB x u v)).2

end
</pre></div>

#### [ Kevin Buzzard (May 18 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126722994):
<p>Indeed</p>

#### [ Kevin Buzzard (May 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723001):
<p>You missed a trick with le_antisymm though</p>

#### [ Kevin Buzzard (May 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723005):
<p>Oh actually maybe you didn't</p>

#### [ Mario Carneiro (May 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723006):
<p>I guess you can throw a <code>function.swap</code> in there if you want to be "point-free"</p>

#### [ Kevin Buzzard (May 18 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723007):
<p>Because the order is the other way</p>

#### [ Mario Carneiro (May 18 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723050):
<p>but also that circ madness is limited in usefulness since it's nondependent</p>

#### [ Mario Carneiro (May 18 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723053):
<p>so for example it wouldn't work in the definition of <code>sup</code></p>

#### [ Kevin Buzzard (May 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723104):
<p>You mean the HB and x screw it up?</p>

#### [ Mario Carneiro (May 18 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723112):
<p>no, the u and v do - the type of <code>basis_nhds_directed HB x u v</code> depends on them</p>

#### [ Mario Carneiro (May 18 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723122):
<p>if it worked, it would look something like <code>((∘) ∘ (∘)) classical.some (basis_nhds_directed HB x)</code></p>

#### [ Kevin Buzzard (May 18 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723126):
<p>So now all I need is for that PR to be accepted <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Mario Carneiro (May 18 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723127):
<p>There is a <code>dcomp</code> function which is dependent, but I don't think it has nice notation</p>

#### [ Kevin Buzzard (May 18 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723172):
<p>Unfortunately it looks like it might still need some work by someone who is in the middle of exams...</p>

#### [ Mario Carneiro (May 18 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723187):
<p>hm, lean doesn't like <code>((∘') ∘' (∘'))</code></p>

#### [ Kevin Buzzard (May 18 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126723239):
<p>You're being sucked into the circ madness...</p>

#### [ Kevin Buzzard (May 18 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/126738602):
<p>So thanks for writing that proof for me Mario. I was completely on top of everything after Reid's comment about this trick for Exists so I knew I could write it, so I did the optimal thing of just writing it all myself anyway and then comparing with what you wrote. I missed the trick with <code>let ⟨W, h₁, h₂, h₃⟩ =...</code> -- I did the expansion using the trick Reid explained later on. But I also didn't use <code>include</code> and I carried <code>HB</code> around with me as an input variable. Aah, I see -- this is why you have used a section; include plays two roles and I'd only appreciated one of them until now. It can be used to insert hypotheses into the context in a tactic proof, but also to include variables into defintions in a section. I'll remark that I just learnt this by searching the pdf of TPIL for <code>include</code> -- I find the sphinx search very disappointing in this regard -- if you search the online docs for include then you just get the unenlightening response that the word is mentioned in every section, and are told the first occurrence of the word in each section; I would in this case far rather see all occurrences so I can try and spot which ones are in code blocks.</p>

#### [ Patrick Massot (Jun 01 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127424574):
<p>It tried to read this thread but I still don't understand how to use <code>exists</code> classical stuff. How do you tell Lean about <code>example (X Y : Type) (f : X → Y) :  (∀ y : Y, ∃ x : X, f x = y) → (∃ g : Y → X, f ∘ g = id)</code></p>

#### [ Reid Barton (Jun 01 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127424633):
<p>use <code>axiom_of_choice</code> on that hypothesis and then <code>funext</code></p>

#### [ Patrick Massot (Jun 01 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425370):
<p>Thanks you very much. </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>  <span class="o">(</span><span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
  <span class="n">replace</span> <span class="n">hyp</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">axiom_of_choice</span> <span class="n">hyp</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">hyp</span> <span class="k">with</span> <span class="n">g</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">g</span><span class="o">,</span>
  <span class="n">funext</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">H</span> <span class="n">y</span>
<span class="kn">end</span>
</pre></div>


<p>works. I still have questions: is it what you had in mind? is there a simpler solution? can we hide this to mathematicians? can we avoid frightening stuff like <code>∃ (f_1 : Π (x : Y), (λ (y : Y), X) x), ∀ (x : Y), (λ (y : Y) (x : X), f x = y) x (f_1 x)</code> which is defeq to <code>∃ f_1 : Y → X, ∀ (x : Y), f (f_1 x) = x</code>?</p>

#### [ Patrick Massot (Jun 01 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425457):
<p>the frightening is what you get from <code>classical.axiom_of_choice hyp</code></p>

#### [ Reid Barton (Jun 01 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425460):
<p><code>set_option pp.beta true</code> should help</p>

#### [ Patrick Massot (Jun 01 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425513):
<p>perfect</p>

#### [ Reid Barton (Jun 01 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425517):
<p>And yeah, that's pretty much what I had in mind (or you can write it more succinctly in term mode)</p>

#### [ Patrick Massot (Jun 01 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425532):
<p>Why is this <code>pp.beta</code> not true by default?</p>

#### [ Patrick Massot (Jun 01 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425612):
<p>Is there any way to merge the two lines <code>replace hyp := classical.axiom_of_choice hyp,  cases hyp with g H,</code> into one <code>I_really_mean hyp with g H</code>?</p>

#### [ Reid Barton (Jun 01 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425637):
<p><code>cases</code> can take an expression, so you can inline the redefinition of <code>hyp</code></p>

#### [ Patrick Massot (Jun 01 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425640):
<p>I tried that and couldn't succeed</p>

#### [ Reid Barton (Jun 01 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425681):
<div class="codehilite"><pre><span></span>  <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">classical</span><span class="bp">.</span><span class="n">axiom_of_choice</span> <span class="n">hyp</span> <span class="k">with</span> <span class="n">g</span> <span class="n">H</span><span class="o">,</span>
<span class="c1">-- etc.</span>
</pre></div>

#### [ Patrick Massot (Jun 01 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425701):
<p>Ok, Lean is afraid of you</p>

#### [ Reid Barton (Jun 01 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425704):
<p>or</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>  <span class="o">(</span><span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">hyp</span><span class="o">,</span>
  <span class="k">let</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">axiom_of_choice</span> <span class="n">hyp</span> <span class="k">in</span>
  <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">funext</span> <span class="n">H</span><span class="bp">⟩</span>
</pre></div>

#### [ Patrick Massot (Jun 01 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425711):
<p>it didn't work with me before you wrote it</p>

#### [ Patrick Massot (Jun 01 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425735):
<p>I also tried various stuff involving <code>let</code>...</p>

#### [ Reid Barton (Jun 01 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425809):
<p>just remember that everything in term mode is subtly different from the corresponding thing in tactic mode and you should be fine <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Patrick Massot (Jun 01 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425828):
<p>it's a bit confusing that the <code>funext</code> tactic takes the variable name as argument while the term version takes the quantified equality</p>

#### [ Patrick Massot (Jun 01 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127425906):
<p>Anyway, I have to go back home now. Thank you very much Reid!</p>

#### [ Kevin Buzzard (Jun 01 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127429106):
<p>Patrick I asked this very question here a month or two ago. Let me see if I can dig out the thread.</p>

#### [ Kevin Buzzard (Jun 01 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127429119):
<p>All I remember is that I used the axiom of choice twice and Mario pointed out that I should only be using it once</p>

#### [ Kevin Buzzard (Jun 01 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127429204):
<p><a href="#narrow/stream/113488-general/topic/cases.20eliminating.20into.20type" title="#narrow/stream/113488-general/topic/cases.20eliminating.20into.20type">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cases.20eliminating.20into.20type</a></p>

#### [ Kevin Buzzard (Jun 01 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127429208):
<p>Maybe that will have some relevant material</p>

#### [ Patrick Massot (Jun 01 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127431357):
<p>I thought so, bu I found the wrong thread when I searched. Thank you</p>

#### [ Patrick Massot (Jun 03 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127515866):
<p>So, <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> and <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, should I PR something like:</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">tactic</span>
<span class="kn">namespace</span> <span class="n">interactive</span>
<span class="kn">open</span> <span class="n">interactive</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span>

<span class="c">/-</span><span class="cm">-</span>
<span class="cm">  `choice hyp with g H` takes an hypothesis `hyp` of the form</span>
<span class="cm">  `∀ (y : Y), ∃ (x : X), P x y` for some `P : X → Y → Prop` and outputs into</span>
<span class="cm">  context a function `g : Y → X` and a proposition `H` stating</span>
<span class="cm">  `∀ (y : Y), P (g y) y`. It presumably also works with dependent versions</span>
<span class="cm">  (see the actual type of `classical.axiom_of_choice`)</span>
<span class="cm">-/</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">choice</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">cases_arg_p</span><span class="o">)</span> <span class="o">(</span><span class="n">ids</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">with_ident_list</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">cases</span> <span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="bp">``</span><span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">axiom_of_choice</span> <span class="err">%%</span><span class="o">(</span><span class="n">e</span><span class="bp">.</span><span class="mi">2</span><span class="o">)))</span> <span class="n">ids</span>

<span class="kn">end</span> <span class="n">interactive</span>
<span class="kn">end</span> <span class="n">tactic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span>  <span class="o">(</span><span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">g</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">X</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">P</span> <span class="o">(</span><span class="n">g</span> <span class="n">y</span><span class="o">)</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
  <span class="n">choice</span> <span class="n">hyp</span> <span class="k">with</span> <span class="n">g</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">g</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">H</span>
<span class="kn">end</span>
</pre></div>


<p>I know this is purely cosmetic, but I think it would help mathematicians to have a nice interface to choice.</p>

#### [ Patrick Massot (Jun 03 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127515910):
<p>Of course this is a version of what Simon wrote in the other thread</p>

#### [ Kevin Buzzard (Jun 03 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516186):
<p>This is really nice and I want to be showing this to my 1st years.</p>

#### [ Kevin Buzzard (Jun 03 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516187):
<p>It was on my todo list to  get this into a xena library.</p>

#### [ Kevin Buzzard (Jun 03 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516194):
<p>Patrick -- can choice be used to replace cases everywhere?</p>

#### [ Kevin Buzzard (Jun 03 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516301):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> it's important we make a good interface for mathematicians, so they can learn more quickly.</p>

#### [ Kenny Lau (Jun 03 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20%28X%29%20%28Y%29/near/127516364):
<p>Skolem normal form?</p>


{% endraw %}
