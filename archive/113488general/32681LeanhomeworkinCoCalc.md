---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32681LeanhomeworkinCoCalc.html
---

## Stream: [general](index.html)
### Topic: [Lean homework in CoCalc](32681LeanhomeworkinCoCalc.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 29 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20homework%20in%20CoCalc/near/148778475):
Here are my notes on setting Lean homework in CoCalc:

https://github.com/kbuzzard/xena/blob/master/CoCalc/CoCalc_notes.md

That link will be updated as people tell me better ways of getting round a kludgy hack with paths. Rather than go into details here, I will just hope that someone tells me a better way of doing it and then I'll update the link above. [The current issue is that when a student clicks on a `.lean` file CoCalc looks for `leanpkg.path` in their home directory, which my homework cannot access. @**William Stein** any ideas on how to make this less hacky?]

@**Patrick Massot** @**Jeremy Avigad** I've got it working, and am optimistic that it will be working even better soon. Jeremy, you might well be happy with CoCalc's installation of mathlib which is at `path /ext/lean/lean-3.4.1-linux/mathlib/`, but I am greedy and want both bleeding edge mathlib and also a library of my own, which is why I had to work harder.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 29 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20homework%20in%20CoCalc/near/148779171):
Thanks for the info, Kevin. I'm going to look into using CoCalc for my course in April. Just to check -- are you using the standard or basic course plan? As an instructor, do you have write access to a subdirectory of students' home folders?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 29 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20homework%20in%20CoCalc/near/148791090):
I bought 4 months of Standard Medium Course (70 people). I am running an unconventional course in an unconventional way -- I have 250 students, but Lean is just an optional extra, so I did not need 250 people.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20homework%20in%20CoCalc/near/148819746):
So today I used the "shared project" functionality of CoCalc and we had multiple people working on one lean file. I thought it would be chaos but it worked fine, and was very funny. What happened was that completely coincidentally I found two groups of people independently trying to define dihedral groups in Lean, and because I'd spent several hours earlier today thinking about CoCalc I suggested that we tried to do it together. This was slightly brave on my part because I had not thought at all about how imports worked for group projects, and initially there was some confusion about which version of mathlib we needed. I hacked together a solution though, and it worked really smoothly. I guess I should add a description of how it all worked to my notes.

