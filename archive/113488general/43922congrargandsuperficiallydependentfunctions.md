---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43922congrargandsuperficiallydependentfunctions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [congr_arg and superficially dependent functions](https://leanprover-community.github.io/archive/113488general/43922congrargandsuperficiallydependentfunctions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 02 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781762):
<p>I'm having trouble constructing <code>congr_arg</code> expressions, where the function superficially looks like a dependent function, but after some definitionally unfolding you can see that it isn't really.</p>

#### [ Scott Morrison (Aug 02 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781777):
<p>I've worked out how to get around this in interactive mode, but I can't do it with <code>expr</code>s.</p>

#### [ Scott Morrison (Aug 02 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781780):
<p>Here's my work so far.</p>

#### [ Scott Morrison (Aug 02 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781824):
<div class="codehilite"><pre><span></span>def F : Π n : ℕ, Type := λ n, ℕ
def G : Π n : ℕ, F n := λ n, begin dunfold F, exact 0 end

lemma test (m n : ℕ) (w : m = n) : G n == G m :=
begin
  -- This doesn&#39;t work, because `G` looks like a dependent function
  success_if_fail {
    have h := congr_arg G w
  },
  -- In fact it isn&#39;t really, and we can discover this with `dsimp`.
  let g := G,
  dsimp [F] at g,
  -- Now we can use congr_arg.
  let h := congr_arg g w,
  dsimp [g] at h,
  rw h,
end

-- Now I want to do this via `expr` munging:

open tactic

meta def mk_congr_arg_using_dsimp (G W : expr) (F : name) : tactic expr :=
-- I have no idea how to achieve this: this doesn&#39;t work, but is my best guess.
do
  s ← simp_lemmas.mk_default,
  t ← infer_type G,
  t&#39; ← s.dsimplify [F] t {fail_if_unchanged := ff},
  trace t&#39;,
  to_expr ```(congr_arg (%%G : %%t&#39;) %%W)

lemma test2 (m n : ℕ) (w : m = n) : G n == G m :=
begin
  let h := by tactic.get_local `w &gt;&gt;= λ W, mk_congr_arg_using_dsimp `(G) W `F,
  rw h,
end
</pre></div>

#### [ Scott Morrison (Aug 02 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130781907):
<p>If anyone could replace the definition of <code>mk_congr_arg_using_dsimp</code> so that <code>test2</code> works, that would be amazing. :-)</p>

#### [ Minchao Wu (Aug 03 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130826815):
<p>A quick solution:</p>
<div class="codehilite"><pre><span></span>meta def mk_congr_arg_using_dsimp (G W : expr) (F : name) : tactic unit :=
do
  eg ← to_expr ```(λ n:nat, id 0),
  t ← infer_type G,
  s ← simp_lemmas.mk_default,
  t&#39; ← s.dsimplify [F] t {fail_if_unchanged := ff},
  definev `g t&#39; eg,
  eg ← get_local `g,
  eeq ← to_expr ```(%%G = %%eg),
  assert `h eeq,
  try reflexivity

lemma test2 (m n : ℕ) (w : m = n) : G n == G m :=
begin
  tactic.get_local `w &gt;&gt;= λ W, mk_congr_arg_using_dsimp `(G) W `F,
  rw h
end
</pre></div>

#### [ Minchao Wu (Aug 03 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130827714):
<p>The attempt is to force lean to be aware that the two types of G collapse, however <code>(%%G : %%t')</code> doesn't do the trick. This introduces an additional local hypothesis which has the non-dependent type and proves that it is just <code>G</code>.</p>

#### [ Scott Morrison (Aug 03 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130827909):
<p>Thanks <span class="user-mention" data-user-id="110187">@Minchao Wu</span>. In the meantime I'd come up with my own solution:</p>
<div class="codehilite"><pre><span></span>-- Sometimes `mk_congr_arg` fails, when the function is &#39;superficially dependent&#39;.
-- This hack first dsimplifies the function before building the `congr_arg` expression.
-- Unfortunately it creates a dummy hypothesis that I can&#39;t work out how to avoid or dispose of cleanly.
meta def mk_congr_arg_using_dsimp (G W : expr) (u : list name) : tactic expr :=
do
  s ← simp_lemmas.mk_default,
  t ← infer_type G,
  t&#39; ← s.dsimplify u t {fail_if_unchanged := ff},
  tactic.definev `_mk_congr_arg_aux t&#39; G,
  to_expr ```(congr_arg _mk_congr_arg_aux %%W)
</pre></div>


<p>which is fairly similar!</p>

#### [ Scott Morrison (Aug 03 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130827938):
<p>The next question is how to achieve this without making the local hypothesis, so this tactic doesn't pollute the current goal.</p>

#### [ Minchao Wu (Aug 03 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr_arg%20and%20superficially%20dependent%20functions/near/130828082):
<p>Yeah I'm also wondering if there is a neater solution :)</p>


{% endraw %}
