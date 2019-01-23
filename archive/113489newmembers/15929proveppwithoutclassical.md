---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/15929proveppwithoutclassical.html
---

## Stream: [new members](index.html)
### Topic: [prove ¬(p ↔ ¬p) without classical](15929proveppwithoutclassical.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Skiba (Aug 31 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133107905):
The examples at the end of chapter 3 of tutorial "Theorem proving in Lean" are very easy, except the one in subj. If I try to construct it as is, I have to construct false from two functions, which I can get by iff.mp and iff.mpr - but I have no objects to apply these functions. I found propext constant, which allowed me to convert iff to an equality of p = ¬p, but I don't see how to prove (p = ¬p) → false. In Idris language such proofs are built by "impossible" keyword, but I cannot find anything similar in Lean. Am I missing something basic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 31 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133108380):
Here's what I came up with:

```lean
example {p : Prop} [h : decidable p] (q : p ↔ ¬p) : false :=
match h with
| is_true  p  := iff.mp q p p
| is_false np := np (iff.mpr q np)
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 31 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133108711):
Perhaps the key to remember here is that `¬ p` means `p → false`, so both `iff.mp q p : p → false` and `np : p → false`. Then you just have to fill in the `p`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Skiba (Aug 31 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133108794):
Is not the idea of not using classical that I cannot prove by cases? I'm still at the beginning of the tutorial and did not learn what is decidable, but it looks too similar to excluded middle. I suppose it should also allow to prove ¬¬p  → p which should not work in constructive reasoning.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 31 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109087):
https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L343

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 31 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109264):
@**Sean Leather** if you use decidable you might as well use classical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 31 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109327):
True. Attempt # 2:

```lean
example {p : Prop} (q : p ↔ ¬p) : false :=
have h' : ¬p, from λ h, (iff.mp q h) h,
h' (iff.mpr q h')
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 31 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109343):
Why don't you like my solution?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 31 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109344):
```quote
you might as well use classical
```
This conclusion doesn't need any hypotheses.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 31 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109401):
```lean
example {p : Prop} (q : p ↔ ¬p) : false :=
q.1 (q.2 $ λ H, q.1 H H) (q.2 $ λ H, q.1 H H)

example {p : Prop} (q : p ↔ ¬p) : false :=
(λ H, q.1 H H) $ q.2 $ λ H, q.1 H H
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 31 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109467):
@**Kenny Lau** I was trying to avoid “shortcuts” like `.1` and `$`,  which may not have been covered, yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Skiba (Aug 31 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109539):
Thanks, guys! Excellent examples, will try to understand where did I miss the point.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 31 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109541):
```lean
example {p : Prop} : ¬(p ↔ ¬p) :=
λ q, iff.rec_on q (λ h1 h2, h1 (h2 (λ H, h1 H H)) (h2 (λ H, h1 H H)))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 31 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109629):
```lean
example {p : Prop} : ¬(p ↔ ¬p) :=
assume q : p ↔ ¬p, iff.rec_on q
(assume h1 : p → ¬p,
 assume h2 : ¬p → p,
 h1 (h2 (λ H, h1 H H)) (h2 (λ H, h1 H H)))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 31 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109671):
Are these cries for `hhhhhh`elp, Kenny? :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 31 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109676):
I just like to name my hypotheses `h`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 31 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109689):
Too bad there's only one `h` in the Latin alphabet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Skiba (Aug 31 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133109997):
@**Patrick Massot** I did like your solution, because the tutorial only states that there are implementations of these proofs in the standard library, but does not mention where to find them. But the easiest to follow is Sean's one, because I can see what I missed: although it's impossible to construct a p, it is still possible to construct ¬p, and the last line is trivial. I still did not completely understand, how it's done by λ h, (iff.mp q h) h, but it's a small piece to resolve already.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 31 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133110240):
@**Andrew Skiba** You know that `λ` and `assume` are the same?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Aug 31 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133110323):
When looking again at Theorem Proving in Lean, I realized that it mostly used `assume`. I use `λ` more myself, since it's shorter.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Skiba (Aug 31 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133114894):
```quote
@**Andrew Skiba** You know that `λ` and `assume` are the same?
```
Sure, this one is clear. I missed another point: although it's impossible to construct p from ¬¬p without em, it is easy to construct ¬p from ¬¬¬p. This is the key to solving this exercise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 31 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133114912):
constructive math is crazy...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 31 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133124674):
This problem seems to be a fairly popular question here [1](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Logic.20.26.20Proof/near/127708058) [2](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/(no.20topic)/near/132923537).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 31 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/prove%20%C2%AC%28p%20%E2%86%94%20%C2%ACp%29%20without%20classical/near/133125379):
Yeah, for some reason it's tripping up a lot of people working through TPIL. We need a FAQ!


{% endraw %}
