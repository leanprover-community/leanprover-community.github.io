---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/14012modulogroupaction.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [modulo group action](https://leanprover-community.github.io/archive/116395maths/14012modulogroupaction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Sep 13 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133907297):
<p>Do I understand correctly that we have a file defining group action and a file defining left and right cosets in a group, but no link between those? And we don't have G\X if G acts on X?</p>

#### [ Kenny Lau (Sep 13 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133907861):
<p>we do have orbit-stabalizer theorem, if that's what you mean</p>

#### [ Chris Hughes (Sep 13 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133907907):
<p>I'm not sure exactly  what you mean, but it may well be part of my Sylow PR.</p>

#### [ Patrick Massot (Sep 13 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908423):
<p>No, I don't mean orbit stabilizer. I mean: if G acts on X, quotient X by "x equivalent to y if there exists g such that y = g x"</p>

#### [ Patrick Massot (Sep 13 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908526):
<p>This: <a href="https://github.com/leanprover/mathlib/pull/257/files#diff-a1c68f03014617e86345e35b6885b923R90" target="_blank" title="https://github.com/leanprover/mathlib/pull/257/files#diff-a1c68f03014617e86345e35b6885b923R90">https://github.com/leanprover/mathlib/pull/257/files#diff-a1c68f03014617e86345e35b6885b923R90</a></p>

#### [ Patrick Massot (Sep 13 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908563):
<p>What is the status of this PR?</p>

#### [ Chris Hughes (Sep 13 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908650):
<p>On hold because of the cardinals of finite sets issue.</p>

#### [ Patrick Massot (Sep 13 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908941):
<p>Is this something someone is working on?</p>

#### [ Chris Hughes (Sep 13 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908971):
<p>Not really.</p>

#### [ Chris Hughes (Sep 13 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133908998):
<p>I'm playing with tactics, and hope to be able to write a tactic to deal with it at some point.</p>

#### [ Chris Hughes (Sep 13 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909003):
<p>But it could take a while</p>

#### [ Chris Hughes (Sep 13 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909156):
<p>I could separate out the bits that aren't about finite sets, and PR them first if you're desperate for it. Do you want the fact that G acts on the cosets of a subgroup as well?</p>

#### [ Patrick Massot (Sep 13 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909216):
<p>I'm not desperate, I wrote:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">group_action</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">ρ</span> <span class="o">:</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_action</span> <span class="n">ρ</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">is_group_action</span><span class="bp">.</span><span class="n">inverse_left</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">G</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">ρ</span> <span class="n">g</span><span class="bp">⁻¹</span><span class="o">)</span> <span class="err">∘</span> <span class="n">ρ</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">change</span> <span class="n">ρ</span> <span class="n">g</span><span class="bp">⁻¹</span> <span class="o">(</span><span class="n">ρ</span> <span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span>  <span class="n">x</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span> <span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">mul</span> <span class="n">ρ</span> <span class="n">g</span><span class="bp">⁻¹</span> <span class="n">g</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">one</span> <span class="n">ρ</span><span class="o">]</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">is_group_action</span><span class="bp">.</span><span class="n">inverse_right</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">G</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">ρ</span> <span class="n">g</span><span class="o">)</span> <span class="err">∘</span> <span class="n">ρ</span> <span class="n">g</span><span class="bp">⁻¹</span> <span class="bp">=</span> <span class="n">id</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">is_group_action</span><span class="bp">.</span><span class="n">inverse_left</span> <span class="n">ρ</span> <span class="n">g</span><span class="bp">⁻¹</span>

<span class="n">def</span> <span class="n">action_rel</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">X</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">g</span><span class="o">,</span> <span class="n">ρ</span> <span class="n">g</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">G</span><span class="o">),</span>  <span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">one</span> <span class="n">ρ</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="k">begin</span>
  <span class="o">{</span> <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">rintros</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="n">existsi</span> <span class="n">g</span><span class="bp">⁻¹</span><span class="o">,</span>
      <span class="n">rw</span> <span class="err">←</span><span class="n">h</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">congr_fun</span> <span class="o">(</span><span class="n">is_group_action</span><span class="bp">.</span><span class="n">inverse_left</span> <span class="n">ρ</span> <span class="n">g</span><span class="o">)</span> <span class="n">x</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">rintros</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">g&#39;</span><span class="o">,</span> <span class="n">h&#39;</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="n">existsi</span> <span class="n">g&#39;</span><span class="bp">*</span><span class="n">g</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">is_monoid_action</span><span class="bp">.</span><span class="n">mul</span> <span class="n">ρ</span><span class="o">,</span> <span class="n">h</span><span class="o">,</span> <span class="n">h&#39;</span><span class="o">]</span> <span class="o">}</span> <span class="o">}</span>
  <span class="kn">end</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Patrick Massot (Sep 13 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909233):
<p>So I have my setoid</p>

#### [ Patrick Massot (Sep 13 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133909249):
<p>I don't think your PR contains much more in this direction</p>

#### [ Patrick Massot (Sep 13 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133910622):
<p>Does someone know where is the lemma saying that if a finite set surjects onto a type then this type is finite?</p>

#### [ Reid Barton (Sep 13 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133910888):
<p><code>fintype.of_surjective</code> I guess</p>

#### [ Patrick Massot (Sep 13 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/modulo%20group%20action/near/133911324):
<p>Thanks!</p>


{% endraw %}
