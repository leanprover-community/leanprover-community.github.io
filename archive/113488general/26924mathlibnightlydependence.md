---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26924mathlibnightlydependence.html
---

## Stream: [general](index.html)
### Topic: [mathlib nightly dependence](26924mathlibnightlydependence.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969893):
could mathlib stop depending on nightlies?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969899):
In lieu of what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969905):
the latest lean commit that builds?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969907):
That's what we used to do, gave headaches for all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969909):
04-10 lean compiles, but I'm forced to detach head from lean and use the 04-04 version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969911):
just because it compiles doesn't mean it works with mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969915):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969956):
If I increase the nightly version that means I've tested it with the latest changes, other than that I make no guarantee

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969964):
By attaching to a particular nightly version it prevents the situation where Leo pushes some breaking change and mathlib is broken for a week while we figure out how to recover from it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124969967):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 12 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124970015):
It's fully possible that mathlib works with no changes on 4-10 nightly, and I'll probably update it next time I make a change to mathlib, but unless there's some feature that was just added that you need it shouldn't cause you any problems to just stay on 04-04

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124970060):
it doesn't work with 4-10

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 12 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124972134):
Also, mathlib is currently broken w.r.t. Lean head, until https://github.com/leanprover/lean/pull/1955 is merged

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 12 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973329):
@**Kenny Lau** Are you still compiling Lean yourself? Why?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973367):
why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 12 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973379):
Because of the added friction you complain about here...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 12 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973426):
If you haven't seen https://github.com/Kha/elan yet, it will solve the issue of how to obtain a Lean version compatible to mathlib. Though I don't know what OS you're using.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 12 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973498):
Also compiling yourself is bad for the climate :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973694):
@**Sebastian Ullrich**  oh well i'm on windows

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 12 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973702):
I'm still quite happy using a git submodule for Lean and the mathlib commit in `leanpkg.toml` to manage my dependencies. I have precise control over which commits I rely on. Also, I compile Lean much less often than nightlies are made, so I don't think I'm contributing much to climate change. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 12 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973707):
```
$ curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh

info: downloading installer
curl: (22) The requested URL returned error: 404 Not Found
elan: command failed: curl -sSfL https://github.com/Kha/elan/releases/download/v0.3.0/elan-x86_64-pc-windows-gnu.zip -o /tmp/tmp.xOB7DmPlna/elan-init.zip

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973815):
@**Kenny Lau** I'll take a look, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124973899):
@**Sean Leather** Just for completeness, elan should give you exactly the same amount of control. Well, you can't select commits between nightlies, but hopefully that should be granular enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 12 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124974006):
@**Sebastian Ullrich** Thanks. I'll wait and see how it goes. I do like being able to choose commits, but I grant you that is probably not an important requirement. At the moment, anyway, I don't feel the need to change my approach.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124975482):
There's also a certain argument that us "early adopters" hanging out here should dogfood elan, to make sure it's usable for the newcomers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 12 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124975863):
How widespread do you expect Lean to get :)? Can we go by how Coq's doing after 30 years?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 12 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124976887):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 12 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124976901):
I'm enormously encouraged by the fact that my undergrads can learn Lean, and do non-trivial stuff in it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124981519):
@**Sebastian Ullrich** I believe Elan is still using the wrong tool for unzipping on Mac

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 12 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124981608):
Well yes, I haven't touched it yet :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 12 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20nightly%20dependence/near/124982169):
I think that's the wrong approach to fixing it :stuck_out_tongue_closed_eyes:


{% endraw %}
