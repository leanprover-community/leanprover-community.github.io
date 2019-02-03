---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42739dsimpconfig.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [dsimp_config](https://leanprover-community.github.io/archive/113488general/42739dsimpconfig.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Edward Ayers (Oct 10 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/135537467):
<p>Please could someone help me fill in these holes in the docstring for <code>dsimp_config</code>?</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">dsimp_config</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">md</span>                        <span class="o">:=</span> <span class="kn">reducible</span><span class="o">)</span> <span class="c1">-- reduction mode: how aggressively constants are replaced with their definitions.</span>
<span class="o">(</span><span class="n">max_steps</span> <span class="o">:</span> <span class="n">nat</span>           <span class="o">:=</span> <span class="n">simp</span><span class="bp">.</span><span class="n">default_max_steps</span><span class="o">)</span> <span class="c1">-- The maximum number of steps allowed before failing.</span>
<span class="o">(</span><span class="n">canonize_instances</span> <span class="o">:</span> <span class="n">bool</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span> <span class="c1">-- [TODO] ???</span>
<span class="o">(</span><span class="n">single_pass</span> <span class="o">:</span> <span class="n">bool</span>        <span class="o">:=</span> <span class="n">ff</span><span class="o">)</span> <span class="c1">-- [TODO] Does this mean that _each_ simp-lemma can only be used once?</span>
<span class="o">(</span><span class="n">fail_if_unchanged</span>         <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span> <span class="c1">-- Don&#39;t throw if simp didn&#39;t do anything.</span>
<span class="o">(</span><span class="n">eta</span>                       <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span> <span class="c1">-- allow eta-equivalence: `(λ x, F $ x) ↝ F`</span>
<span class="o">(</span><span class="n">zeta</span> <span class="o">:</span> <span class="n">bool</span>               <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span> <span class="c1">-- do zeta-reductions: `let x : a := b in c ↝ c[x/b]`.</span>
<span class="o">(</span><span class="n">beta</span> <span class="o">:</span> <span class="n">bool</span>               <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span> <span class="c1">-- do beta-reductions: `(λ x, E) $ (y) ↝ E[x/y]`.</span>
<span class="o">(</span><span class="n">proj</span> <span class="o">:</span> <span class="n">bool</span>               <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span> <span class="c1">-- reduce projections: `⟨a,b⟩.1 ↝ a` [TODO] I think?</span>
<span class="o">(</span><span class="n">iota</span> <span class="o">:</span> <span class="n">bool</span>               <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span> <span class="c1">-- reduce recursors for inductive datatypes: eg `nat.rec_on (succ n) Z R ↝ R n $ nat.rec_on n Z R`</span>
<span class="o">(</span><span class="n">unfold_reducible</span>          <span class="o">:=</span> <span class="n">ff</span><span class="o">)</span> <span class="c1">-- if tt, definitions with `reducible` transparency will be unfolded (delta-reduced)</span>
<span class="o">(</span><span class="n">memoize</span>                   <span class="o">:=</span> <span class="n">tt</span><span class="o">)</span> <span class="c1">-- [TODO] what is being memoised?</span>
</pre></div>

#### [ Edward Ayers (Oct 10 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/135537599):
<p>(I'm working through <code>init/meta</code> in the Lean source and adding all the missing docstrings)</p>

#### [ Chris Hughes (Nov 15 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147772589):
<p><span class="user-mention" data-user-id="121918">@Edward Ayers</span> Is a copy of your Lean with docstring available online anywhere? It would be really useful.</p>

#### [ Edward Ayers (Nov 16 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147809879):
<p><a href="https://github.com/EdAyers/lean" target="_blank" title="https://github.com/EdAyers/lean">https://github.com/EdAyers/lean</a></p>

#### [ Edward Ayers (Nov 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147809934):
<p>Checkout the <code>doc</code> branch</p>

#### [ Edward Ayers (Nov 16 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147809977):
<p>I use the build from that branch as my main lean executable</p>

#### [ Patrick Massot (Nov 16 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810027):
<p>Do you mean you added stuff besides docstrings?</p>

#### [ Edward Ayers (Nov 16 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810032):
<p>No I haven't added anything except docstrings on that branch</p>

#### [ Edward Ayers (Nov 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810043):
<p>(hopefully, no guarantees)</p>

#### [ Edward Ayers (Nov 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810057):
<p>It builds mathlib though so its probably fine. I didn't sneak in <code>false</code> as an axiom anywhere.</p>

#### [ Edward Ayers (Nov 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810108):
<p>I also can't guarantee that the docstrings I added aren't misleading, they are more a side-effect of me trying to understand the sourcecode</p>

#### [ Chris Hughes (Nov 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dsimp_config/near/147810263):
<p>Thanks <span class="user-mention" data-user-id="121918">@Edward Ayers</span></p>


{% endraw %}
