---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/78004Functionalextensionality.html
---

## [new members](index.html)
### [Functional extensionality](78004Functionalextensionality.html)

#### [Ken Roe (Jul 24 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Functional extensionality/near/130240450):
Is there a functionality extensionality theorem like the one shown below in one of the libraries:

```lean
theorem fun_ext {t} {u} :
    ∀ (a:t→u) (b:t→u), a=b → (λ (x:t), a)=(λ (x:t), b) := sorry.
```

#### [Chris Hughes (Jul 24 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Functional extensionality/near/130240630):
There's `funext`, but that's not the same as what you stated. The proof of the theorem you stated is `assume a b h, by rw  h`

#### [Ken Roe (Jul 25 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Functional extensionality/near/130242691):
Thanks.  I'm running into another issue.  It seems I cannot rewrite if meta variables are involved.  How is the following theorem completed (ignore the "admit"--I'd like to get the "rw h" to work.
```lean
theorem dd : (λ (x:ℕ), x*2)=(λ (x:ℕ), x+x) := begin
    have h:∀ x, x*2=x+x, intro, admit,
    rw h
end
```

#### [Simon Hudon (Jul 25 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Functional extensionality/near/130242967):
You can't rewrite bound variables. Use `simp only [h]` instead

#### [Simon Hudon (Jul 25 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Functional extensionality/near/130243044):
```quote
Is there a functionality extensionality theorem like the one shown below in one of the libraries:
```lean
theorem fun_ext {t} {u} :
    ∀ (a:t→u) (b:t→u), a=b → (λ (x:t), a)=(λ (x:t), b) := sorry
```
```

Isn't that normal rewriting?

