---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21725codeextraction.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [code extraction](https://leanprover-community.github.io/archive/113488general/21725codeextraction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ jacke (Apr 17 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171529):
<p>I would like to extract c++ programs from my lean code, but the question is how to do it! Page 6 of Programming in Lean says that " Programs<br>
written in the language can be evaluated efficiently by Lean’s virtual-machine interpreter or translated automatically to C++ and compiled"</p>

#### [ jacke (Apr 17 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171587):
<p>I can see that there is a PR here that promises such functionality: <a href="https://github.com/leanprover/lean/pull/1241" target="_blank" title="https://github.com/leanprover/lean/pull/1241">https://github.com/leanprover/lean/pull/1241</a>, but it was never integrated into the codebase (the PR was rejected). </p>
<p>Is there a way to extract C++ programs using Lean 3.3.0?</p>
<p>Thanks for helping, and sorry for my formatting!</p>

#### [ Simon Hudon (Apr 17 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171694):
<p>So far, there is no facility for code extraction in any language. The only way to execute a Lean program is with the Lean virtual machine. The developers plan to add native code generation (like a compiler) in the next version (Lean 4) which is already under construction.</p>

#### [ jacke (Apr 17 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171818):
<p>Got it, thanks! </p>
<p>I've been using Lean to prove out certain algorithms, and code extraction to C++ would be a wonderful way to generate an immediate efficiency dividend.</p>

#### [ jacke (Apr 17 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171824):
<p>Looking forward to version 4!</p>

#### [ Simon Hudon (Apr 17 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171883):
<p>You and me both! If this is something you have time for / skills for, (source) code generation in various languages would be pretty useful. My own todo list has code generation in Haskell and Rust on it but I don't know in which decade I'll get around to it <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Mario Carneiro (Apr 17 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171887):
<p>This is on my todo list as well, I was working on this just today</p>

#### [ Simon Hudon (Apr 17 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171928):
<p>You were? Which language?</p>

#### [ Mario Carneiro (Apr 17 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125171938):
<p>Lean to C, or maybe ML</p>

#### [ jacke (Apr 17 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125172006):
<p>It's super easy to interface from C/C++ to pretty much anywhere else. <br>
Extracting to C  would be great.</p>

#### [ Simon Hudon (Apr 17 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125172052):
<p>Nice! What's your approach?</p>

#### [ Mario Carneiro (Apr 17 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125172100):
<p>I'm still looking at large scale infrastructure, but the idea is to have a type translation for the objects, and then closure conversion and translate the rest as directly as possible</p>

#### [ Mario Carneiro (Apr 17 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125172127):
<p>There is a question of whether to use "advanced" features of C++ or treat it like assembly language with nicer syntax and get rid of all the complicated control flow</p>

#### [ Simon Hudon (Apr 17 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125172203):
<p>Any thoughts on proving the correctness of the translation?</p>

#### [ Mario Carneiro (Apr 17 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125172318):
<p>I'm toying with the idea of doing this as a dissertation project, but probably code extraction should come first</p>

#### [ Simon Hudon (Apr 17 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/code%20extraction/near/125172374):
<p>That would be awesome! I'm thinking of doing that myself because I need such a feature but it's a bit of a distraction for me. One the examples in my dissertation is a non-blocking double ended queue. It would be fun if I could refine it down to executable code.</p>


{% endraw %}
