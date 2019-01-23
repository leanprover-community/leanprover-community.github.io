---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/56392Usingrewritetosimplifyaboundvariableexpression.html
---

## Stream: [new members](index.html)
### Topic: [Using rewrite to simplify a bound variable expression](56392Usingrewritetosimplifyaboundvariableexpression.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Aug 06 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950190):
```lean
theorem fsimp3 { x : ℕ } : x=0 → f x = 1 :=
begin
    intro, unfold f, rw a
end

theorem fsimp4 {e : ℕ } : e=0 → (λ x : ℕ, x+(f x)=1+x)=(λ x : ℕ, 1=1) :=
begin
    intro,
    rewrite fsimp3, simp
end
```
How do I get the "rewrite fsimp3" tactic to work in the "fsimp4" proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950208):
Probably use `conv`. Do you want to post an MWE?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Aug 06 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950318):
Go ahead and post

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950372):
No, I was suggesting that _you_ post a minimal example that shows the problem --- in particular you haven't included the definition of `f`!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950374):
I think `def f (x : ℕ) := x + 1` probably serves your purpose.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950425):
`rw` does not work under a binder. You can either use `simp` instead, or use `conv` or `funext` to enter the binder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950432):
For conv, see https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Aug 06 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950433):
Oops--Missed that def
```lean
def f (x : ℕ) := x+1

theorem fsimp3 { x : ℕ } : x=0 → f x = 1 :=
begin
    intro, unfold f, rw a
end

theorem fsimp4 {e : ℕ } : e=0 → (λ x : ℕ, x+(f x)=1+x)=(λ x : ℕ, 1=1) :=
begin
    intro,
    rewrite fsimp3, simp
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950482):
I'm pretty confused how you intend to do anything using `rw fsimp3`, even under the binder.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950491):
You've only got `e=0`, but now want to say something about all `x`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Aug 06 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950780):
It looks like conv fails:
```lean
theorem fsimp4 {e : ℕ } : e=0 → (λ x : ℕ, x+(f x)=1+x)=(λ x : ℕ, 1=1) :=
begin
    intro, simp, conv
    begin
        to_lhs,
        funext,
        rw fsimp3, reflexivity,
    end
end
```
I get the error:
```lean
convert tactic failed, there are unsolved goals
state:
e : ℕ,
a : e = 0,
x : ℕ
⊢ x = 0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 06 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950786):
That's because, as Scott pointed out, what you're trying to prove is not true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Aug 06 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130950908):
Actually, I found the error:
```lean
theorem fsimp4 {e : ℕ } : e=0 → (λ x : ℕ, x+(f x)=1+x) e=(λ x : ℕ, 1=1) e :=
begin
    intro, conv
    begin
        to_lhs,
        simp, rw a,
        funext,
        rw fsimp3, skip, reflexivity
    end
end
```
However, the error I got is confusing.  The "x=0" got changed to "x" on the screen in the message.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20rewrite%20to%20simplify%20a%20bound%20variable%20expression/near/130951440):
this proof attempt is not valid for the same reason as before. You can't try to prove the functions are equal because they aren't. You can only prove that the functions *evaluated at `e`* are equal, so you need to do beta reduction first (using `dsimp`) and then try to prove it


{% endraw %}
