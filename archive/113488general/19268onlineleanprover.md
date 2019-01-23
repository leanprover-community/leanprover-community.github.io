---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19268onlineleanprover.html
---

## Stream: [general](index.html)
### Topic: [online leanprover](19268onlineleanprover.html)

---

#### [Kenny Lau (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701238):
just how outdated is this thing? I posted some code somewhere public and then one guy complained they can't run it in the online lean prover

#### [Kenny Lau (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701252):
and I verified it

#### [Kenny Lau (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701271):
and it's because the online lean prover doesn't have topological groups

#### [Kenny Lau (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701275):
this is very concerning

#### [Kevin Buzzard (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701276):
It's 3.4.1

#### [Kevin Buzzard (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701281):
as far as I know

#### [Kevin Buzzard (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701285):
or maybe even 3.4.0

#### [Kenny Lau (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701287):
what would people think about lean if we keep spreading codes that can't run

#### [Kevin Buzzard (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701295):
and mathlib from the time 3.4.0 was invented

#### [Kenny Lau (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701296):
unless you spend 2 hours installing everything

#### [Mario Carneiro (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701303):
it gets updated when lean core does, I think

#### [Kenny Lau (Nov 14 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701470):
when will lean quit its beta status

#### [Mario Carneiro (Nov 14 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147701693):
when it's not an academic playground app

#### [Kenny Lau (Nov 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702245):
on the one hand me and kevin want to promote it

#### [Kenny Lau (Nov 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702249):
and on the other hand the big devs don't want it to be promoted

#### [Kenny Lau (Nov 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702271):
also it's quite ironic that the project is microsoft-funded and can't deal with windows paths

#### [Reid Barton (Nov 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702300):
Lean or the online Lean thing?

#### [Kenny Lau (Nov 14 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702337):
lean

#### [Kenny Lau (Nov 14 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702354):
aha I misremembered the original quote

#### [Kenny Lau (Nov 14 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702356):
I mean

#### [Kenny Lau (Nov 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702361):
it's quite ironic that the project is microsoft-funded and requires a linux emulator to be installed

#### [Chris Hughes (Nov 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702586):
Out of interest, why are Microsoft funding it. How do they make money on this free software?

#### [Kevin Buzzard (Nov 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702605):
they are secretly using it to check windows 10 has no bugs

#### [Kevin Buzzard (Nov 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702632):
and the NSA gets them to use it to find bugs in the Android kernel

#### [Kevin Buzzard (Nov 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147702640):
maybe

#### [Abhimanyu Pallavi Sudhir (Nov 15 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147759375):
```quote
and it's because the online lean prover doesn't have topological groups
```
 I recall it didn't have p-adic valuations either.

#### [Leonardo de Moura (Nov 16 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147796514):
@**Kenny Lau** 
> when will lean quit its beta status

Lean is a research project. I have no interest in building a product at this point.

> it's quite ironic that the project is microsoft-funded and requires a linux emulator to be installed

MSYS2 is not a linux emulator, but a POSIX compatibility layer. It makes sure we can write build and test scripts that run in all platforms.

#### [Leonardo de Moura (Nov 16 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147796577):
@**Chris Hughes** 
>  Out of interest, why are Microsoft funding it. How do they make money on this free software?

Lean is not a product. I work for Microsoft Research, and I can pick my own research projects. Nobody at Microsoft is expecting to make money with Lean.

#### [Leonardo de Moura (Nov 16 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147796742):
@**Kenny Lau** 
> on the one hand me and kevin want to promote it
> and on the other hand the big devs don't want it to be promoted

I know Lean has serious performance and usability problems. I tried to make this clear in the FAQ document https://github.com/leanprover/lean/blob/master/doc/faq.md. I told the CMU guys many times it was a bad idea to develop mathlib at this point, and that they were going to hit performance problems and bugs. There is no point in promoting the system at this point. It is useful as a playground for trying ideas, but it is not ready for serious use.

#### [Kevin Buzzard (Nov 16 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147804573):
Kenny -- the ideas we are currently trying include "is dependent type theory actually robust enough in practice to deal with definitions and basic properties of the complex objects which serious research level mathematicians use in their daily work" and "is it possible to integrate formal proof verification systems into teaching of undergraduate mathematics". I'm having quite a lot of fun investigating these things. I think it's pretty clear at this point that there are no optimal choices for the underlying software. There are problems with Coq, problems with Lean, problems with Isabelle HOL, problems with univalent foundations -- there seems to me to be currently no good answer to "which system should we use".  I am a mathematician and I cannot really help with these problems, which view as firmly living in the domain of computer science -- deciding whether it's this kind of type theory or that kind of type theory, and how the type class system should work, are not really things I can help with. This still seems to me to be a fairly young research area and what you are seeing is simply the consequences of the nature of cutting edge research. One thing I am convinced of is that to make progress with these questions we absolutely need to have mathematicians using this kind of software, so that is what I am promoting. Without mathematicians we're just going going to get more pieces of software and more proofs of Godel's incompleteness theorem. There is still a long journey ahead though. Maybe the software that mathematicians as a community end up using is some new piece of software that hasn't even been written yet. 

One thing I've always been adamant about though is that Lean 3.4.1 is perfectly adequate as a tool for working with undergraduate level mathematics; I see evidence of this time and time again. I have to figure out how to really use it to help more people to actually learn and do undergraduate level mathematics, and this is something I am actively working on, and for which the CS problems are now solved -- Lean 3.4.1 will do fine.

#### [Kenny Lau (Nov 16 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147804890):
how about adding the elaborator attributes back to `nat.strong_rec_on` and `int.induction_on`...

#### [Bryan Gin-ge Chen (Nov 16 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147806828):
How hard is it to build a custom version of the lean web editor? Are the instructions at [the "lean-web-editor" repo](https://github.com/leanprover/lean-web-editor) still up to date?

#### [Patrick Massot (Nov 16 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147807616):
There was a lot of discussions about this at https://gitter.im/leanprover_public/lean_js?source=orgpage

#### [Bryan Gin-ge Chen (Nov 16 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147808794):
I'm having trouble with [the live version of the lean-web-editor](https://leanprover.github.io/live/latest/) in firefox (63.0.3) currently. The editor seems to work fine in Chrome though. In firefox, I'm not getting any messages when I type things like `#eval 2+2` in the window. If I refresh the window with some `#eval` code in the URL, then I get multiple `eval result` messages, but when I start typing it seems to break again. I didn't have these issues a few months ago when I last seriously tried using the editor so maybe some recent changes to firefox has messed things up somehow.

#### [Patrick Massot (Nov 16 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147808895):
I've always had trouble with the web editor in Firefox.

#### [Bryan Gin-ge Chen (Nov 16 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147809069):
Also, I just tried following the instructions on the lean-web-editor repo and things seem to work (in chrome), except that when I tried to create an up-to-date version of `library.zip` by editing `leanpkg.toml` and running `leanpkg upgrade` and then `mk_library.py`, I get `file '/library/init/default.lean' not found` in the web-editor (served locally by webpack-dev-server).  Chrome says that `library.zip` is loading, and when I unzip `library.zip` I do find `init/default.olean`.

#### [Bryan Gin-ge Chen (Nov 16 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147809134):
(Everything works fine if I just use the `library.zip` downloaded using `fetch_lean_js.sh`)

#### [Bryan Gin-ge Chen (Nov 17 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147878223):
OK, I managed to build a working `library.zip`. I had changed the `lean_version` in `combined_lib/leanpkg.toml` to `nightly`, so that `leanpkg upgrade` would put in an up-to-date commit of `mathlib`. But the instructions say "Make sure you run the same Lean version locally as the javascript version you target", so I changed it back to `3.4.1` and then running `mk_library.py` worked.

Still no idea how to solve the firefox issues, but outside of that I support what @**Scott Morrison|110087** said in the `lean_js` gitter:
>We might consider adding the lean-web-editor to a travis build, so that there is an online version that is always tracking mathlib (and we get notifications as soon as something breaks).
My guess is that this would be more appropriate at part of the mathlib travis build than the lean build.

Perhaps we could set up github pages for `leanprover-community` with a copy of `lean-web-editor` including an automatically compiled version of `mathlib`?

#### [Bryan Gin-ge Chen (Nov 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/online%20leanprover/near/147928323):
More on firefox issues: After playing around more with `lean-web-editor` and `lean-client-js-browser`, I think the issue is with the 3.4.1 wasm builds of lean. In particular, [the 3.3.0 version](https://leanprover.github.io/live/3.3.0) works fine for me in firefox. Was something changed between 3.3.0 and 3.4.1  that could have broken firefox compatibility? @**Gabriel Ebner** @**Sebastian Ullrich** 

Unfortunately, [per earlier discussion here](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/lean-web-editor.20not.20compiling.3F/near/124566399), compiling a wasm build with emscripten requires linux, so it will be hard for me to investigate this further on my own.

