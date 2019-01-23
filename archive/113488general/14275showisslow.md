---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14275showisslow.html
---

## Stream: [general](index.html)
### Topic: [show is slow](14275showisslow.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 04 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888169):
```lean
import data.real.basic 

set_option profiler true

theorem works_fine : (3 : ℝ) = ((3 : ℤ) : ℝ) := rfl
-- elaboration of works_fine took 31.9ms

theorem very_slow (n : ℤ) (x : ℝ) (H1 : x = ↑n) (H2 : n < 3) : x < 3 :=
begin
  show x < ((3 : ℤ) : ℝ), -- this is the bad line
  rw H1,
  rwa int.cast_lt,
end 

-- elaboration of very_slow took 5.4s

theorem much_faster (n : ℤ) (x : ℝ) (H1 : x = ↑n) (H2 : n < 3) : x < 3 :=
begin
  rw (show (3 : ℝ) = ((3 : ℤ) : ℝ), from rfl),
  rw H1,
  rwa int.cast_lt,
end 
-- elaboration of much_faster took 61.6ms

```

Note one elaboration time is in seconds not milliseconds. What have I done wrong here? I have somehow misused `show`, it seems.

#### [ Kevin Buzzard (Aug 04 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888235):
```lean
theorem very_slow (n : ℤ) (x : ℝ) (H1 : x = ↑n) (H2 : n < (3 : ℤ)) : x < (3 : ℝ) :=
begin
  show x < ((3 : ℤ) : ℝ), -- this is the bad line
  rw H1,
  rwa int.cast_lt,
end

```

doesn't fix it. I can't imagine what `show` is doing.

#### [ Mario Carneiro (Aug 04 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888627):
does `change` do any better?

#### [ Kevin Buzzard (Aug 04 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888631):
Progress:

```lean
import data.real.basic

set_option profiler true

theorem works_fine : (3 : ℝ) = ((3 : ℤ) : ℝ) := rfl
-- elaboration of works_fine took 14.3ms

theorem very_slow2 : (3 : ℝ) = ((3 : ℤ) : ℝ) :=
begin
  have H : (3 : ℝ) = ((3 : ℤ) : ℝ) := rfl,
  exact H
end
-- elaboration of very_slow2 took 5.83s
```

#### [ Kevin Buzzard (Aug 04 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888638):
(progress in the sense that the problem is now simpler and even more confusing)

#### [ Chris Hughes (Aug 04 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888802):
Don't use definitional reduction for reals is probably the best solution.
```lean
theorem very_slow (n : ℤ) (x : ℝ) (H1 : x = ↑n) (H2 : n < (3 : ℤ)) : x < (3 : ℝ) :=
begin
  have : (3 : ℝ) = ((3 : ℤ) : ℝ) := by simp,
  rwa [H1, this, int.cast_lt], 
end
```

#### [ Kevin Buzzard (Aug 04 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888858):
Sure there are workarounds, but what is surprising is that Lean is *sometimes* proving the result by `rfl` quickly and sometimes not

#### [ Kevin Buzzard (Aug 04 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888874):
```lean

theorem very_slow3 : (3 : ℝ) = ((3 : ℤ) : ℝ) :=
begin
  change (3 : ℝ) with ((3 : ℤ) : ℝ), 
  refl,
end

theorem very_slow4 : (3 : ℝ) = ((3 : ℤ) : ℝ) :=
begin
  change ((3 : ℤ) : ℝ) with (3 : ℝ), 
  refl,
end
```

same problem with change

#### [ Kevin Buzzard (Aug 04 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889010):
```lean
theorem very_slow : (3 : ℝ) = ((3 : ℤ) : ℝ) :=
begin
  have H : (3 : ℝ) = ((3 : ℤ) : ℝ) := rfl,
  exact H
end

theorem works_fine : (3 : ℝ) = ((3 : ℤ) : ℝ) :=
begin
  have H : (3 : ℝ) = ((3 : ℤ) : ℝ),
    refl,
  exact H,
end

```
Way beyond my pay grade

#### [ Mario Carneiro (Aug 04 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889117):
I have narrowed it down to
```
run_cmd assertv_core `h `((3 : ℝ) = ((3 : ℤ) : ℝ)) `(eq.refl (3 : ℝ))
```
which is slow, while
```
run_cmd assertv_core `h `((3 : ℝ) = ((3 : ℤ) : ℝ))
  `(show (3 : ℝ) = ((3 : ℤ) : ℝ), from eq.refl (3 : ℝ))
```
is fast

#### [ Kenny Lau (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889181):
how do I use `run_cmd`?

#### [ Mario Carneiro (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889191):
it accepts a `tactic A` and runs it in a dummy state

#### [ Kenny Lau (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889195):
```lean
import data.real.basic

run_cmd assertv_core `h `((3 : ℝ) = ((3 : ℤ) : ℝ)) `(eq.refl (3 : ℝ))
```

#### [ Kenny Lau (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889196):
this doesn't work

#### [ Mario Carneiro (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889199):
it's basically the same as `example : true := by tac`

#### [ Mario Carneiro (Aug 04 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889239):
`open tactic`

#### [ Kenny Lau (Aug 04 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889243):
lol

#### [ Kenny Lau (Aug 04 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889311):
```lean
run_cmd assertv_core `h `((2 : ℝ) = ((3 : ℤ) : ℝ))
  `(show (3 : ℝ) = ((3 : ℤ) : ℝ), from eq.refl (3 : ℝ))
```

#### [ Kenny Lau (Aug 04 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889312):
this is slow

#### [ Kenny Lau (Aug 04 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889315):
this timed out

#### [ Kenny Lau (Aug 04 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889317):
(it's 2 instead of 3 in the beginning)

#### [ Kenny Lau (Aug 04 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889333):
while this is fast (I changed the last 3 to 2 instead):
```lean
run_cmd assertv_core `h `((3 : ℝ) = ((3 : ℤ) : ℝ))
  `(show (3 : ℝ) = ((3 : ℤ) : ℝ), from eq.refl (2 : ℝ))
```

#### [ Kenny Lau (Aug 04 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889340):
so the `show` is slow

#### [ Mario Carneiro (Aug 04 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889463):
it's not a fair comparison when the statement isn't true though

#### [ Mario Carneiro (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889470):
because then lean does completely different things with regard to error reporting and stuff

#### [ Kenny Lau (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889473):
```lean
run_cmd assertv_core `h `((3 : ℝ) = ((3 : ℤ) : ℝ))
  `(show (2 : ℝ) = ((2 : ℤ) : ℝ), from eq.refl (2 : ℝ))
```

#### [ Kenny Lau (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889474):
the statement is true, and it is slow

#### [ Kenny Lau (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889477):
oh wait, this is fast:
```lean
run_cmd assertv_core `h `((3 : ℝ) = ((3 : ℤ) : ℝ))
  `(show (2 : ℝ) = ((2 : ℤ) : ℝ), from eq.refl (3 : ℝ))
```

#### [ Mario Carneiro (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889481):
In both cases it's going to fail because the types don't match

#### [ Kenny Lau (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889520):
but they expect `2` instead of `3`!

#### [ Kenny Lau (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889526):
```
type mismatch at application
  (λ (this : 2 = ↑2), this) (eq.refl 3)
term
  eq.refl 3
has type
  3 = 3
but is expected to have type
  2 = ↑2
```

#### [ Kenny Lau (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889527):
```
unexpected argument at application
  eq.refl 3
given argument
  3
expected argument
  2
```

#### [ Mario Carneiro (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889530):
`assertv_core` checks that the type of the last argument is the same as the second argument

#### [ Mario Carneiro (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889535):
so all of the numbers have to match

#### [ Mario Carneiro (Aug 04 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889593):
I think there is a bug in `assertv_core`. If I use `assert_core` instead, it works fine, which you can achieve by using the proof-omitted form of tactic `have`

#### [ Mario Carneiro (Aug 04 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889595):
```lean
theorem not_slow : (3 : ℝ) = ((3 : ℤ) : ℝ) :=
begin
  have H : (3 : ℝ) = ((3 : ℤ) : ℝ), exact rfl,
  exact H
end
```

#### [ Mario Carneiro (Aug 04 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889641):
note that `definev_core` is also slow, which is linked in to the `let` tactic

#### [ Kenny Lau (Aug 04 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889707):
```cpp
vm_obj assert_define_core(bool is_assert, name const & n, expr const & t, tactic_state const & s) {
    optional<metavar_decl> g = s.get_main_goal_decl();
    if (!g) return mk_no_goals_exception(s);
    type_context_old ctx     = mk_type_context_for(s);
    if (!is_sort(ctx.whnf(ctx.infer(t)))) {
        format msg("invalid ");
        if (is_assert) msg += format("assert"); else msg += format("define");
        msg += format(" tactic, expression is not a type");
        msg += pp_indented_expr(s, t);
        return tactic::mk_exception(msg, s);
    }
    local_context lctx   = g->get_context();
    expr new_M_1         = ctx.mk_metavar_decl(lctx, t);
    expr new_M_2, new_val;
    if (is_assert) {
        expr new_target  = mk_pi(n, t, g->get_type());
        new_M_2          = ctx.mk_metavar_decl(lctx, new_target);
        new_val          = mk_app(new_M_2, new_M_1);
    } else {
        expr new_target  = mk_let(n, t, new_M_1, g->get_type());
        new_M_2          = ctx.mk_metavar_decl(lctx, new_target);
        new_val          = new_M_2;
    }
    ctx.assign(head(s.goals()), new_val);
    list<expr> new_gs    = cons(new_M_1, cons(new_M_2, tail(s.goals())));
    return tactic::mk_success(set_mctx_goals(s, ctx.mctx(), new_gs));
}

vm_obj tactic_assert_core(vm_obj const & n, vm_obj const & t, vm_obj const & s) {
    return assert_define_core(true, to_name(n), to_expr(t), tactic::to_state(s));
}

vm_obj assertv_definev_core(bool is_assert, name const & n, expr const & t, expr const & v, tactic_state const & s) {
    optional<metavar_decl> g = s.get_main_goal_decl();
    if (!g) return mk_no_goals_exception(s);
    type_context_old ctx     = mk_type_context_for(s);
    expr v_type          = ctx.infer(v);
    if (!ctx.is_def_eq(t, v_type)) {
        auto thunk = [=]() {
            format msg("invalid ");
            if (is_assert) msg += format("assertv"); else msg += format("definev");
            msg += format(" tactic, value has type");
            msg += pp_indented_expr(s, v_type);
            msg += line() + format("but is expected to have type");
            msg += pp_indented_expr(s, t);
            return msg;
        };
        return tactic::mk_exception(thunk, s);
    }
    local_context lctx   = g->get_context();
    expr new_M, new_val;
    if (is_assert) {
        expr new_target  = mk_pi(n, t, g->get_type());
        new_M            = ctx.mk_metavar_decl(lctx, new_target);
        new_val          = mk_app(new_M, v);
    } else {
        expr new_target  = mk_let(n, t, v, g->get_type());
        new_M            = ctx.mk_metavar_decl(lctx, new_target);
        new_val          = new_M;
    }
    ctx.assign(head(s.goals()), new_val);
    list<expr> new_gs    = cons(new_M, tail(s.goals()));
    return tactic::mk_success(set_mctx_goals(s, ctx.mctx(), new_gs));
}

vm_obj tactic_assertv_core(vm_obj const & n, vm_obj const & e, vm_obj const & pr, vm_obj const & s) {
    return assertv_definev_core(true, to_name(n), to_expr(e), to_expr(pr), tactic::to_state(s));
}
```

#### [ Mario Carneiro (Aug 04 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889756):
the issue is somewhere in `assertv_definev_core`, but I don't see anything wrong

#### [ Mario Carneiro (Aug 04 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889764):
the `ctx.is_def_eq` call is potentially expensive, but you can test that in lean and it's not

#### [ Mario Carneiro (Aug 04 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130890110):
The mystery continues. As far as I can tell, the following lean code should do the same as `assertv_definev_core` in this case:
```
run_cmd do
  let t : expr := `((3 : ℝ) = ((3 : ℤ) : ℝ)),
  let v : expr := `(eq.refl (3:ℝ)),
  v_t ← infer_type v,
  is_def_eq t v_t,
  r ← target,
  let e := expr.pi `h binder_info.default t r,
  m ← mk_meta_var e,
  let e' := expr.app m v,
  exact e',
  set_goals [m]
```
yet it runs without any problems

#### [ Mario Carneiro (Aug 04 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130891358):
@**Sebastian Ullrich** Could you debug this for me? Here's a mathlib free version of the test:
```lean
structure Q := (num : ℕ)
def id' (n : ℕ) : Q := ⟨n / n.gcd 1⟩
instance : has_zero Q := ⟨⟨0⟩⟩
instance : has_one Q := ⟨⟨1⟩⟩
instance : has_add Q := ⟨λ ⟨n₁⟩ ⟨n₂⟩, id' (n₁ + n₂)⟩

run_cmd tactic.try_for 1000 (assertv_core `h
  `((4 : Q) = 4+0)
  `(show (4 : Q) = 4+0, from eq.refl (4 : Q)) >> admit) --works

run_cmd tactic.try_for 10000 (assertv_core `h
  `((4 : Q) = 4+0)
  `(eq.refl (4 : Q)) >> admit) --timeout
```

#### [ Johan Commelin (Aug 04 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130891933):
The `--works` version has `1000`, whereas the `--timeout` version has `10000`. I don't know if that matters...

#### [ Mario Carneiro (Aug 04 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130892761):
That's probably not needed, but it is saying that the first completes in <1000 ms and the second does not complete with <10000 ms so it is much worse

#### [ Simon Hudon (Aug 04 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130897379):
Is this something `norm_num` would help with?

#### [ Simon Hudon (Aug 04 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130897429):
If I understand correctly, `refl` is slow because it's unfolding the numerals.

#### [ Kevin Buzzard (Aug 04 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130897479):
refl isn't always slow. It's just slow if you invoke it the wrong way :-)

#### [ Kevin Buzzard (Aug 04 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130897489):
You can prove that the real 3 is the coercion of the integer 3 using simp as well, which is quick (but not as quick as when you use refl, if you use refl the right way)

#### [ Mario Carneiro (Aug 04 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130898142):
I don't think `rfl` wins over `simp` here even in the "good" case, at least not if your numbers are moderately large. Calculating `4 : real` directly requires a number of gcd calculations, which are slow


{% endraw %}
