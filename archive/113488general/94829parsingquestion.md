---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/94829parsingquestion.html
---

## [general](index.html)
### [parsing question](94829parsingquestion.html)

#### [Kevin Buzzard (Jan 19 2019 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing question/near/156445528):
tl;dr: what are the binding powers of `Π  _ , _` and `→` in Lean's dependent type theory? Does this even make sense?

I have around seven half-written blog posts and I'm trying to get some of them into shape (all part of my general moving back into more active Leaning now my course has finished). One of them is a very basic post about how you can use `#print notation` to figure out how Lean will parse `a + b * c` or `a ^ b ^ c` (i.e. how to find out that `*` has a higher precedence than `+`, and that `^` is right associative).

But I can't work out how to figure out how `∀ n : ℕ, n = 1 → true` will parse, short of just tying it. The problem is that `∀` and `→` are not notation, they are inbuilt. The comma is also playing a role here, I think; I guess it's part of the forall notation. Are there binding powers at play here that I cannot see? I know forall = Pi. I don't know how to work out whether the example is `(∀ n : ℕ, n = 1) → true` or `∀ n : ℕ, (n = 1 → true)` (short of trying it and discovering that it's the latter). There is presumably some underlying logic here.

#### [Kevin Buzzard (Jan 19 2019 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing question/near/156446241):
```lean
#print notation ->
-- _ `->`:25 _:24 := #1 → #2
```
If `→` is supposed to be exactly the same as `->` then this is evidence that the binding power of `→` is 25 (and the 24 agrees with the fact that `→` is right associative). But I don't know how to check this short of experimentation.

#### [Kevin Buzzard (Jan 19 2019 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing question/near/156446351):
```
`Σ`:1024 binders `,`:0 (scoped 0) := #0`
`Pi`:0 binders `,`:0 (scoped 0) := #0
```
Vast difference there between `Pi` and `Σ`.

#### [François G. Dorais (Jan 19 2019 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing question/near/156447636):
From init/core: `def std.prec.arrow : nat := 25`

#### [Kevin Buzzard (Jan 19 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing question/near/156448140):
ha ha, that does look relevant doesn't, it -- although I don't know for sure that this is referring to `→` it certainly looks like it is. So what about `Π` and `∀`? Here's another one I found in `#print notation` output:

```
`∃`:1024 binders `,`:0 (scoped 0) := #0`
```
which agrees with `Σ`.

#### [Kevin Buzzard (Jan 19 2019 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing question/near/156449546):
OK so the only difference between the 1024 and the 0 with `Σ` and `Pi` is that `Σ` eats the binders more greedily, and it seems to me that binders are highly restricted in what they can look like, so all attempts so far by me to construct terms  `Σ X, Y` and `Π X, Y` that parse seriously differently have failed. I think the key point is the ` ``,``:0 `which just means in practice "evaluate everything after this first and then eat the lot" for both sigma and pi.

#### [Mario Carneiro (Jan 19 2019 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parsing question/near/156451293):
I don't think that first binding power matters at all. Binders are a special parse mode anyway,  it's not clear how binding power would affect it. The important part is the `` `,`:0``, which means that everything after the comma is parsed with very low precedence, so that `\all x, P op Q` will always parse as `\all x, (P op Q)` for any choice of `op`.

