---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21725codeextraction.html
---

## [general](index.html)
### [code extraction](21725codeextraction.html)

#### [jacke (Apr 17 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171529):
I would like to extract c++ programs from my lean code, but the question is how to do it! Page 6 of Programming in Lean says that " Programs
written in the language can be evaluated efficiently by Lean’s virtual-machine interpreter or translated automatically to C++ and compiled"

#### [jacke (Apr 17 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171587):
I can see that there is a PR here that promises such functionality: https://github.com/leanprover/lean/pull/1241, but it was never integrated into the codebase (the PR was rejected). 

Is there a way to extract C++ programs using Lean 3.3.0?

Thanks for helping, and sorry for my formatting!

#### [Simon Hudon (Apr 17 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171694):
So far, there is no facility for code extraction in any language. The only way to execute a Lean program is with the Lean virtual machine. The developers plan to add native code generation (like a compiler) in the next version (Lean 4) which is already under construction.

#### [jacke (Apr 17 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171818):
Got it, thanks! 

I've been using Lean to prove out certain algorithms, and code extraction to C++ would be a wonderful way to generate an immediate efficiency dividend.

#### [jacke (Apr 17 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171824):
Looking forward to version 4!

#### [Simon Hudon (Apr 17 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171883):
You and me both! If this is something you have time for / skills for, (source) code generation in various languages would be pretty useful. My own todo list has code generation in Haskell and Rust on it but I don't know in which decade I'll get around to it :stuck_out_tongue_closed_eyes:

#### [Mario Carneiro (Apr 17 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171887):
This is on my todo list as well, I was working on this just today

#### [Simon Hudon (Apr 17 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171928):
You were? Which language?

#### [Mario Carneiro (Apr 17 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125171938):
Lean to C, or maybe ML

#### [jacke (Apr 17 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125172006):
It's super easy to interface from C/C++ to pretty much anywhere else. 
Extracting to C  would be great.

#### [Simon Hudon (Apr 17 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125172052):
Nice! What's your approach?

#### [Mario Carneiro (Apr 17 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125172100):
I'm still looking at large scale infrastructure, but the idea is to have a type translation for the objects, and then closure conversion and translate the rest as directly as possible

#### [Mario Carneiro (Apr 17 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125172127):
There is a question of whether to use "advanced" features of C++ or treat it like assembly language with nicer syntax and get rid of all the complicated control flow

#### [Simon Hudon (Apr 17 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125172203):
Any thoughts on proving the correctness of the translation?

#### [Mario Carneiro (Apr 17 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125172318):
I'm toying with the idea of doing this as a dissertation project, but probably code extraction should come first

#### [Simon Hudon (Apr 17 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code extraction/near/125172374):
That would be awesome! I'm thinking of doing that myself because I need such a feature but it's a bit of a distraction for me. One the examples in my dissertation is a non-blocking double ended queue. It would be fun if I could refine it down to executable code.

