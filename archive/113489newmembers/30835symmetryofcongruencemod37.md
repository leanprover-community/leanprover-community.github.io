---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/30835symmetryofcongruencemod37.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [symmetry of congruence mod 37](https://leanprover-community.github.io/archive/113489newmembers/30835symmetryofcongruencemod37.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Nicholas Siedlaczek (Dec 06 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151046285):
<p>I know what I am trying to achieve, however not sure about how to actually execute it in Lean.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">definition</span> <span class="n">R</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">),</span> <span class="n">k</span> <span class="bp">*</span> <span class="mi">37</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span>

<span class="kn">theorem</span> <span class="n">R_is_symmetric</span> <span class="o">:</span> <span class="n">symmetric</span> <span class="n">R</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">symmetric</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">R</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">existsi</span><span class="o">((</span><span class="bp">-</span><span class="n">k</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">),</span>

<span class="kn">end</span>
</pre></div>


<p>As you can see I have the hypothesis the k * 37 = x - y, however want to show existence of -k to show -k * 37 = y - x which will show that it is symmetric.<br>
Thanks</p>

#### [ Chris Hughes (Dec 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151046398):
<p>This should help. Use cases.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">R_is_symmetric</span> <span class="o">:</span> <span class="n">symmetric</span> <span class="n">R</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">symmetric</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">R</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">k</span> <span class="n">hk</span><span class="o">,</span>
  <span class="n">existsi</span><span class="o">(</span> <span class="bp">-</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">),</span>

<span class="kn">end</span>
</pre></div>

#### [ Nicholas Siedlaczek (Dec 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151046671):
<p>Thanks Chris</p>

#### [ Kevin Buzzard (Dec 06 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151050131):
<p>Are you an Imperial undergraduate doing my equivalence relation challenge <span class="user-mention" data-user-id="138693">@Nicholas Siedlaczek</span> ?</p>

#### [ Mario Carneiro (Dec 06 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151050456):
<p>I'm sure the 37 was a coincidence</p>

#### [ Patrick Massot (Dec 07 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151052405):
<p><span class="user-mention" data-user-id="138693">@Nicholas Siedlaczek</span> , after you're done with this, it will be useful to realize that all those <code>unfold</code> are only psychological comfort for you, but Lean doesn't need them. The tactic proof of your lemma needs no more than three lines, one for introductions (using tactic <code>rintros</code>), one for instanciating the existential (using tactic <code>use</code>, or <code>existsi</code> but you should get used to <code>use</code> which is newer and more powerful), and one for the tiny computation (using tactic <code>simp</code>).</p>

#### [ Nicholas Siedlaczek (Dec 07 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151052641):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Thanks so what you're saying is all <code>unfold</code> does is display to the user what it actually means and shows you what to prove while lean basically 'ignores' them and is of no consequences to it?</p>

#### [ Patrick Massot (Dec 07 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151052874):
<p>Sometimes it's useful also to Lean, eg for type class instance resolution but, in my experience, almost every unfold that I type is unnecessary.</p>

#### [ Patrick Massot (Dec 07 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151052898):
<p>In your case, the full proof is</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">R</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">),</span> <span class="n">k</span> <span class="bp">*</span> <span class="mi">37</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span>

<span class="kn">theorem</span> <span class="n">R_is_symmetric</span> <span class="o">:</span> <span class="n">symmetric</span> <span class="n">R</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rintros</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">use</span> <span class="bp">-</span><span class="n">k</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">[</span><span class="n">H</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Dec 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151053009):
<p>If you want to emphasize which part really uses tactics seriously, you can also write it as:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">R_is_symmetric</span> <span class="o">:</span> <span class="n">symmetric</span> <span class="n">R</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">⟨</span><span class="n">k</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨-</span><span class="n">k</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">[</span><span class="n">H</span><span class="o">]</span><span class="bp">⟩</span>
</pre></div>

#### [ Patrick Massot (Dec 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/symmetry%20of%20congruence%20mod%2037/near/151053075):
<p>It shows clearly that, in this proof, the only tactic which actually does work for you is the simplifier</p>


{% endraw %}
