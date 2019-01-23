---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60068Whatissome.html
---

## Stream: [new members](index.html)
### Topic: [What is `some`?](60068Whatissome.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135790900):
I'm learning non-constructive definitions from *[An Introduction to Lean](https://leanprover.github.io/introduction_to_lean/introduction_to_lean.pdf)* (p. 25) and the command `some h` is used -- what does it mean?

#### [ Kenny Lau (Oct 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135790908):
`h : \alpha |- some h : option \alpha`

#### [ Chris Hughes (Oct 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135790924):
It's `classical.some`. Given a proof that `exists x, p x`, classical.some will return that `x`

#### [ Chris Hughes (Oct 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135790968):
Ignore Kenny, he's talking about `option.some` which is completely different.

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791033):
```quote
It's `classical.some`. Given a proof that `exists x, p x`, classical.some will return that `x`
```
Oh nice -- so it's the eliminator for `exists`? But how is it different from `exists.elim`, or doing cases on the proof?

#### [ Patrick Massot (Oct 14 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791057):
It's the non-broken one, yes

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791100):
`exists.elim` actually is broken? That explains a lot of problems I've had. Is it broken for finite sets too or only where choice is needed?

#### [ Chris Hughes (Oct 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791157):
Almost. If you're trying to make a proof then you don't need it, you can just use `cases` or `exists.elim`. It's only if you're trying to make data that you need it. The one difference is between this and other eliminators is that you don't have
`classical.some (exists.intro x h) = x`, since this would cause contradictions because of proof irrelevance. `exists.elim` is not actually broken, that's just something people like to say when making fun of constructive mathematics.

#### [ Kenny Lau (Oct 14 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791218):
`s/people/Patrick Massot/`

#### [ Kevin Buzzard (Oct 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791383):
Count me in too. Some of us don't care about constructive maths because we've spent decades doing normal maths and we're not going to change now. Others are younger and more open to these wacky ideas.

#### [ Kevin Buzzard (Oct 14 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791431):
Ps Abhi you should never have to ask what anything is. Copy and paste the code into a Lean session, make sure it compiles, and then just right-click on the thing that you want to know about.

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791496):
```quote
Ps Abhi you should never have to ask what anything is. Copy and paste the code into a Lean session, make sure it compiles, and then just right-click on the thing that you want to know about.
```
Yeah, I didn't realise it was something in the `classical` library. I thought it was something like `have`, which you can check, but won't really give anything useful.

#### [ Chris Hughes (Oct 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791502):
Sometimes the definitions can be a bit mysterious to a newcomer. `classical.some` is probably one of those

#### [ Kevin Buzzard (Oct 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791503):
[some.png](/user_uploads/3121/DmskDK_GG1JoMmyzIS7d-gMq/some.png) the `some` you're talking about is in `classical.lean`. Admittedly its definition is complicated :-/

#### [ Kevin Buzzard (Oct 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791520):
On the other hand, the last chapter of TPIL, which no doubt you have read because you've had all of about 8 days to learn about this stuff (;-) ) explains something about the `classical` stuff.

#### [ Patrick Massot (Oct 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791521):
it could be worse (of course you need to understand the `{... // ...}` notation

#### [ Mario Carneiro (Oct 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791627):
Yeah, I wouldn't say that's a particularly complicated definition. The complicated one is `epsilon`, which is surprisingly rarely used but is basically the same as `some` except you don't even need to prove existence first


{% endraw %}
