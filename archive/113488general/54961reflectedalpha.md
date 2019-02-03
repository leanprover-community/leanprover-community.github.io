---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54961reflectedalpha.html
---

## Stream: [general](index.html)
### Topic: [reflected \alpha](54961reflectedalpha.html)

---


{% raw %}
#### [ Keeley Hoek (Nov 21 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148091917):
<p>This probably counts as a newbie question, sorry:</p>
<p>What is the purpose of the typeclass instance <code>[reflected \alpha]</code> which <code>eval_expr</code> takes? Why can the typeclass system work out what it is most of the time, but sometimes when you pass a custom structure withh few boring nested structures it freaks out?</p>

#### [ Mario Carneiro (Nov 21 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148092166):
<p>it needs to know how to produce expressions from a VM value</p>

#### [ Mario Carneiro (Nov 21 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148092175):
<p>I don't know what the freakout problem is</p>

#### [ Keeley Hoek (Nov 21 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148093813):
<p>Ok<br>
I will try to concoct</p>

#### [ Keeley Hoek (Nov 21 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148097478):
<p>Consider this little snippet:</p>
<div class="codehilite"><pre><span></span>structure a_struct (α : Type) :=
(val : α)

def make_struct : a_struct unit := ⟨()⟩

meta def go (tv : Type) : tactic unit := do
  e ← tactic.mk_app `make_struct [],
  tactic.eval_expr (a_struct tv) e,                 /-  failed to synthesize type class instance for ⊢ reflected (a_struct tv) -/
  tactic.skip

#eval (go unit)
</pre></div>

#### [ Sebastian Ullrich (Nov 21 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148097603):
<p><code>reflected</code> can only be synthesized for closed (parts of) expressions, so <code>go</code> needs a <code>[reflected tv]</code> parameter</p>

#### [ Keeley Hoek (Nov 21 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148106110):
<p>In principle, is there any way to make something like this:</p>
<div class="codehilite"><pre><span></span>set_option trace.app_builder true

structure signature :=
(α : Type)

structure container_struct :=
(c : signature)
(val : c.α)

meta def go : tactic unit := tactic.down $ do
  e ← tactic.up $ tactic.mk_app `container_struct.mk [`({signature . α := nat}), `(2)],
  tactic.eval_expr container_struct e.down,
  tactic.up $ tactic.skip

run_cmd go

-- [app_builder] failed to create an &#39;container_struct.mk&#39;-application,
-- failed to solve unification constraint for #2 argument (?x_0.α =?= ℕ)
</pre></div>


<p>work? I'd really like to be able to persuade lean to be able to solve that constraint (why can't it? :'()</p>
<p>(Please mind the <code>tactic.up</code> and <code>tactic.down</code>s, which are just dealing with the fact that <code>container_struct</code> is <code>Type 1</code>.)</p>

#### [ Sebastian Ullrich (Nov 21 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148106771):
<p>That might be an issue with <code>tactic.mk_app</code>, can you try with the full <code>tactic.to_expr</code>?</p>

#### [ Keeley Hoek (Nov 21 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148107099):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Brilliant! Thanks so much, lots of time of potentially lost work saved</p>

#### [ Keeley Hoek (Nov 22 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148159497):
<p>Here's another mini-problem. I'm just going to store a variable <code>a</code> of arbitrary type <code>α</code> in a structure in two different ways:</p>
<div class="codehilite"><pre><span></span>structure struct_v1 (α : Type) :=
(a : α)

structure struct_v2 :=
(α : Type)
(a : α)

def v1_def : struct_v1 nat := ⟨3⟩

def v2_def : struct_v2 := ⟨nat, 3⟩
</pre></div>


<p>Now I'll try to dynamically fetch these structures, first for version 1, and second for version 2:</p>
<div class="codehilite"><pre><span></span>meta def go_1 (t : Type) : tactic unit :=
  let n := `v1_def in do
  e ← tactic.resolve_name n &gt;&gt;= tactic.to_expr,

-- failed to synthesize type class instance for
-- ⊢ reflected (struct_v1 t)
  tactic.eval_expr (struct_v1 t) e,

  return ()

run_cmd go_1 nat

meta def go_2 : tactic unit := tactic.down $
  let n := `v2_def in do
  e ← tactic.up $ tactic.resolve_name n &gt;&gt;= tactic.to_expr,
  tactic.eval_expr struct_v2 e.down,
  tactic.up $ return ()

run_cmd go_2
</pre></div>


<p>I get a reflection error in only the first way, even though the type could be arbitrary in either case. What's the difference between these constructions?</p>

#### [ Sebastian Ullrich (Nov 22 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflected%20%5Calpha/near/148162400):
<p>In both versions, you need a reflected term of the type. In version 2, that is already part of <code>v2_def</code>(defs are stored as <code>expr</code>s after all). In version 1, you need an explicit <code>[reflected t]</code>. That is the difference.</p>


{% endraw %}
