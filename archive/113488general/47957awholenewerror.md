---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47957awholenewerror.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [a whole new error](https://leanprover-community.github.io/archive/113488general/47957awholenewerror.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 21 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483415):
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">pattern</span><span class="o">,</span> <span class="err">&#39;</span><span class="n">choice</span> <span class="o">(</span><span class="n">frozen_name</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">cons</span><span class="o">)</span> <span class="o">(</span><span class="n">frozen_name</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span><span class="o">)</span><span class="err">&#39;</span> <span class="n">is</span> <span class="n">overloaded</span><span class="o">,</span> <span class="n">and</span> <span class="n">this</span> <span class="n">kind</span> <span class="n">of</span> <span class="n">overloading</span> <span class="n">is</span> <span class="n">not</span> <span class="n">currently</span> <span class="n">supported</span> <span class="k">in</span> <span class="n">patterns</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483454):
<p>use a local notation</p>

#### [ Mario Carneiro (Apr 21 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483456):
<p>what did you write to get that?</p>

#### [ Kenny Lau (Apr 21 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483501):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">reduce</span><span class="bp">.</span><span class="n">not</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)}</span> <span class="o">(</span><span class="n">x</span> <span class="n">b</span><span class="o">),</span> <span class="n">reduce</span> <span class="n">L₁</span> <span class="bp">=</span> <span class="n">L₂</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₃</span> <span class="bp">→</span> <span class="n">false</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">[]</span> <span class="n">L3</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">injections</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">[</span><span class="n">hd</span><span class="o">]</span> <span class="n">L3</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">injections</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">x</span><span class="o">,</span><span class="n">b</span><span class="o">)</span><span class="bp">::</span><span class="n">hd1</span><span class="o">)</span> <span class="n">L2</span> <span class="n">L3</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="n">H</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="k">match</span> <span class="n">reduce</span> <span class="n">hd1</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="n">H</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span><span class="n">b2</span><span class="o">)</span><span class="bp">::</span><span class="n">hd2</span> <span class="o">:=</span> <span class="bp">_</span>
  <span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483556):
<p>does it help to use <code>((x2,b2)::hd2 : list _)</code> instead?</p>

#### [ Kenny Lau (Apr 21 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125483605):
<p>well, it doesn't, but list.cons worked</p>

#### [ Mario Carneiro (Apr 21 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484552):
<div class="codehilite"><pre><span></span>theorem reduce.not : ∀ (L₁ L₂ L₃ : list (α × bool)) (x b), reduce L₁ ≠ L₂ ++ (x, b) :: (x, bnot b) :: L₃
| [] L2 L3 _ _ := λ h, by simpa using (list.append_eq_nil.1 h.symm).2
| ((x,b)::L1) L2 L3 x&#39; b&#39; := begin
  dsimp [reduce],
  cases r : reduce L1,
  { dsimp [reduce], intro h,
    have := congr_arg list.length h,
    simp [-add_comm] at this,
    exact absurd this dec_trivial },
  cases hd with y c,
  by_cases x = y ∧ ¬b = c; simp [reduce, h]; intro H,
  { rw H at r,
    exact reduce.not L1 ((y,c)::L2) L3 x&#39; b&#39; r },
  rcases L2 with _|⟨a, L2⟩,
  { injections, substs x&#39; y c b&#39;,
    refine h ⟨rfl, _⟩,
    cases b; exact dec_trivial },
  { refine reduce.not L1 L2 L3 x&#39; b&#39; _,
    injection H with _ H,
    rw [r, H], refl }
end
</pre></div>


<p>ah, I couldn't help myself</p>

#### [ Kenny Lau (Apr 21 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484554):
<p>thanksssss</p>

#### [ Kenny Lau (Apr 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484611):
<p>and I just realized that I only have two interface theorems</p>

#### [ Kenny Lau (Apr 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484612):
<p>and I don't have to change the rest</p>

#### [ Kenny Lau (Apr 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20whole%20new%20error/near/125484613):
<p>which is again a testimony of the theory of interface</p>


{% endraw %}
