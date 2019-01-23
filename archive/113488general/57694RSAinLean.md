---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57694RSAinLean.html
---

## Stream: [general](index.html)
### Topic: [RSA in Lean](57694RSAinLean.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784575):
I have to give a talk for high school students. Topic: cryptography.
I've done this before, and I would usually fool around in Python. Does anyone know of an implementation of DH or RSA in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784629):
lolno

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784633):
I stay away from Lean when I'm giving talks like this. I spend time talking about WhatsApp because that's what they know in the UK.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784638):
But you could do both, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784644):
then again, all you need is a bit of group exponentiation on `zmod` to implement DH

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784645):
My school talks are usually only 30-40 mins

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784651):
and I think RSA is about as easy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784655):
Aah, I have 75 minutes. The students are coming to an open day of the math department.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784661):
I might even be tempted to refuse to speak to schoolkids for so long. They're not used to concentrating for that kind of time (at least in the UK)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784706):
I would talk for 30, give them 15 minutes to do a project, and then talk for 30 more. Active learning!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784708):
You've got tenure :lol: Refusing is not on my list of options.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784715):
Right, that's what I was thinking.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784717):
They could spend the 15 minutes trying to install Lean :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784723):
So they could do their project with a hand calculator or python or whatever.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784726):
I was just thinking of demoing Lean. Not them playing with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784729):
oh no it takes a whole hour to install lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784741):
maybe a 7 minute talk, then an hour working together trying to install Lean, and then 8 minute wrap-up at the end.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784807):
I've done super-hard computations on my phone using the pari-gp app and a bluetooth keyboard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784809):
and the app is a one click install on Android.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784813):
You could give them some 5 digit numbers to factor on their stock calculator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784823):
but I would stay away from Lean. I've tried it with Math Olympiad level schoolkids and they found it tough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784830):
Ok, thanks for the advice. I'll stick to python.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784871):
on the other hand I should say that on some Wed in mid-Oct (18th?) I am giving another Lean school talk.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 12 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784881):
can I come? :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 12 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784909):
If you are interested in incorporating lean, you can just mention it without going in depth. Make them know formal proving is a thing, and move on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 12 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784986):
Right. That's also an option.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133785610):
```quote
can I come? :P
```
My recent experience with going to give school talks in the UK is that you can't get beyond the entrance until you've proved (or at least claimed) that you're the person they're expecting to give the talk, and they've given you something to wear around your neck saying "visitor".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133785614):
It's very different to how it was 20 years ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 12 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133785615):
so my guess is no


{% endraw %}
