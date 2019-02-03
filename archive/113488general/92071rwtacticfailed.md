---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92071rwtacticfailed.html
---

## Stream: [general](index.html)
### Topic: [rw tactic failed](92071rwtacticfailed.html)

---


{% raw %}
#### [ Kenny Lau (Apr 09 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840698):
<div class="codehilite"><pre><span></span>rewrite tactic failed, did not find instance of the pattern in the target expression
  @has_add.add.{?l_1} ?m_2
    (@add_semigroup.to_has_add.{?l_1} ?m_2
       (@add_monoid.to_add_semigroup.{?l_1} ?m_2 (@add_group.to_add_monoid.{?l_1} ?m_2 ?m_3)))
    (@has_smul.smul.{0 ?l_1} int ?m_2 (@add_group.has_smul.{?l_1} ?m_2 ?m_3) ?m_4 ?m_5)
    (@has_smul.smul.{0 ?l_1} int ?m_2 (@add_group.has_smul.{?l_1} ?m_2 ?m_3) ?m_6 ?m_5)


⊢ [..]
          (@has_add.add.{u₁} α₁
             (@add_semigroup.to_has_add.{u₁} α₁
                (@add_monoid.to_add_semigroup.{u₁} α₁
                   (@add_comm_monoid.to_add_monoid.{u₁} α₁
                      (@add_comm_group.to_add_comm_monoid.{u₁} α₁
                         (@module.to_add_comm_group.{u u₁} α α₁ (@comm_ring.to_ring.{u} α _inst_1) _inst_4)))))
             (@has_smul.smul.{0 u₁} int α₁
                (@add_group.has_smul.{u₁} α₁
                   (@add_comm_group.to_add_group.{u₁} α₁
                      (@module.to_add_comm_group.{u u₁} α α₁ (@comm_ring.to_ring.{u} α _inst_1) _inst_4)))
                n
                (f (@prod.fst.{v w} β γ (@prod.mk.{v w} β γ x y₁))
                   (@prod.snd.{v w} β γ (@prod.mk.{v w} β γ x y₁))))
             (@has_smul.smul.{0 u₁} int α₁
                (@add_group.has_smul.{u₁} α₁
                   (@add_comm_group.to_add_group.{u₁} α₁
                      (@module.to_add_comm_group.{u u₁} α α₁ (@comm_ring.to_ring.{u} α _inst_1) _inst_4)))
                n
                (f (@prod.fst.{v w} β γ (@prod.mk.{v w} β γ x y₂))
                   (@prod.snd.{v w} β γ (@prod.mk.{v w} β γ x y₂)))))
</pre></div>

#### [ Kenny Lau (Apr 09 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840702):
<p>Lean, it's right there</p>

#### [ Kenny Lau (Apr 09 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840706):
<p>I know you want <code> (@add_group.to_add_monoid.{?l_1} ?m_2 ?m_3) </code></p>

#### [ Kenny Lau (Apr 09 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840714):
<p>but isn't <code> (@add_comm_monoid.to_add_monoid.{u₁} α₁
                      (@add_comm_group.to_add_comm_monoid.{u₁} α₁
                         (@module.to_add_comm_group.{u u₁} α α₁ (@comm_ring.to_ring.{u} α _inst_1) _inst_4)) </code> good enough for you</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840765):
<p>they don't look the same to me</p>

#### [ Kenny Lau (Apr 09 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840772):
<p>they're both justifying why I have addition</p>

#### [ Kenny Lau (Apr 09 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840785):
<p>specifically here they're justifying why I have an add_monoid</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840789):
<p>can you do some BS "change" or "show" beforehand?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840855):
<p>Is this one of these dreaded diamond things?</p>

#### [ Kenny Lau (Apr 09 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840877):
<p>yes</p>

#### [ Kenny Lau (Apr 09 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840945):
<p>I think the main concern is the one in the <code>gsmul</code> thread</p>

#### [ Kenny Lau (Apr 09 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840947):
<p>overloading is not good</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840956):
<p>This is Mario's doing, right?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840967):
<p>So probably he will have some sensible solution</p>

#### [ Kenny Lau (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840979):
<p>well but that bullet wasn't in the global namespace before Lean updated</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840988):
<p>oh so it's Leo's doing?</p>

#### [ Kenny Lau (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840991):
<p>I would say so</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124840993):
<p>So probably Mario will have some clever workaround.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841050):
<p>I blame myself for all this</p>

#### [ Kenny Lau (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841057):
<p>you?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841059):
<p>I should never have mentioned that <code>^</code> had the wrong associativity</p>

#### [ Kenny Lau (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841066):
<p>what happened</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841075):
<p>I got annoyed that <code>2^3^2</code> was 64 not 512</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841079):
<p>so I opened an issue</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841091):
<p>and all of a sudden there were lots of changes to <code>^</code></p>

#### [ Kenny Lau (Apr 09 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841100):
<p>I see</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841109):
<p><a href="https://github.com/leanprover/lean/issues/1951" target="_blank" title="https://github.com/leanprover/lean/issues/1951">https://github.com/leanprover/lean/issues/1951</a></p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841168):
<p>led to <a href="https://github.com/leanprover/lean/commit/d387103aa2bebfc98220733d9607a16663ec1ef2" target="_blank" title="https://github.com/leanprover/lean/commit/d387103aa2bebfc98220733d9607a16663ec1ef2">https://github.com/leanprover/lean/commit/d387103aa2bebfc98220733d9607a16663ec1ef2</a></p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841186):
<p>and then to <a href="https://github.com/leanprover/lean/commit/8f55ec4c50379c612731ced2424fd3eda0cf69a6" target="_blank" title="https://github.com/leanprover/lean/commit/8f55ec4c50379c612731ced2424fd3eda0cf69a6">https://github.com/leanprover/lean/commit/8f55ec4c50379c612731ced2424fd3eda0cf69a6</a></p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841195):
<p>and hmm I don't see the bullet</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841205):
<p>maybe it's not my fault after all</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841287):
<p>nice to see presheaves being pulled into core lean though</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841289):
<p><a href="https://github.com/leanprover/lean/commit/6e0bf8473b1980e6692a61a924b4c6eae195619d" target="_blank" title="https://github.com/leanprover/lean/commit/6e0bf8473b1980e6692a61a924b4c6eae195619d">https://github.com/leanprover/lean/commit/6e0bf8473b1980e6692a61a924b4c6eae195619d</a></p>

#### [ Kenny Lau (Apr 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841295):
<p>oh</p>

#### [ Kenny Lau (Apr 09 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841296):
<p>what a subversion</p>

#### [ Kevin Buzzard (Apr 09 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124841420):
<p>Talking of presheaves, thanks for trying to fix that tensor product file. Presumably that's where this issue arose.</p>

#### [ Mario Carneiro (Apr 09 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20tactic%20failed/near/124849118):
<p>I removed the <code>has_smul</code> typeclass from <code>group_power</code>, which should fix the notation overloading problem. This puts us back at square one <code>local infix</code> type solutions for using <code>gsmul</code>, but it shouldn't interfere with the module smul notation now. I'm not sure about registering every abelian group as a Z-module with an instance, since module still uses an <code>out_param</code> for the scalar ring which might get stuck on <code>int</code></p>


{% endraw %}
