---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/44924physicsattack.html
---

## Stream: [maths](index.html)
### Topic: [physics attack](44924physicsattack.html)

---


{% raw %}
#### [ Patrick Massot (Sep 19 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134230265):
<p>Argg, mathlib is under attack from the physics department!</p>

#### [ Patrick Massot (Sep 19 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134230288):
<p>I wasn't expecting that</p>

#### [ Patrick Massot (Sep 19 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134230387):
<p>I know Mario doesn't want to have folders <code>cs</code> and <code>math</code> as the first level of the mathlib file hierarchy, but maybe we could have a <code>physics</code> folder</p>

#### [ Johan Commelin (Sep 19 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134230503):
<p>Is this referring to the <code>tensor</code> PR <span class="emoji emoji-1f606" title="lol">:lol:</span> ?</p>

#### [ Patrick Massot (Sep 19 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134230509):
<p>Sure</p>

#### [ Patrick Massot (Sep 19 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134230517):
<p>it's <code>physics_tensor</code>, there is a typo</p>

#### [ Patrick Massot (Sep 19 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134230596):
<p>It's very interesting however that someone outside CS seemed to have been able to learn Lean without coming here on Zulip</p>

#### [ Johan Commelin (Sep 19 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134230939):
<p>And it is using <code>tidy</code>! Is this a student of Scott, maybe?</p>

#### [ Patrick Massot (Sep 19 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231019):
<p>The plot thickens</p>

#### [ Kevin Buzzard (Sep 19 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231277):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> How much of the tensor PR can be done using <code>pi_instances</code>?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231512):
<p>Alex Bentkamp (benti @ github) is a CS PhD student here at the VU. So this is not related to physics. And he got help from me and Rob (his office mate)</p>

#### [ Patrick Massot (Sep 19 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231521):
<p>What about acting stupid and answering we already have tensor products of modules by Kenny?</p>

#### [ Johannes Hölzl (Sep 19 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231530):
<p>why do we need matrices if we have modules?</p>

#### [ Patrick Massot (Sep 19 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231533):
<p>Wow</p>

#### [ Johannes Hölzl (Sep 19 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231754):
<p>its based on the Deep_Learning entry in the AFP: <a href="https://www.isa-afp.org/browser_info/current/AFP/Deep_Learning/Tensor.html" target="_blank" title="https://www.isa-afp.org/browser_info/current/AFP/Deep_Learning/Tensor.html">https://www.isa-afp.org/browser_info/current/AFP/Deep_Learning/Tensor.html</a></p>

#### [ Patrick Massot (Sep 19 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231834):
<p>So today I learned CS people use the word tensor in the same way physicists do</p>

#### [ Patrick Massot (Sep 19 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231851):
<p>Too bad, I was impressed by the story of a physicist learning Lean alone</p>

#### [ Patrick Massot (Sep 19 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231868):
<p>Still, we have matrices but we don't call them linear maps, we call them matrices</p>

#### [ Patrick Massot (Sep 19 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134231928):
<p>So we need a different name for tensors and this physics/IA stuff</p>

#### [ Johannes Hölzl (Sep 19 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134232125):
<p>IA? is this french for artificial intelligence?</p>

#### [ Patrick Massot (Sep 19 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134232136):
<p>sorry, I probably meant AI</p>

#### [ Patrick Massot (Sep 19 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134232155):
<p>Yes, wikipedia says AI</p>

#### [ Johan Commelin (Sep 19 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134232158):
<p>IA = irtificial antelligence</p>

#### [ Johannes Hölzl (Sep 19 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134232172):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  can you mention the renaming concern on the PR? Alex is usually not here on Zulip</p>

#### [ Patrick Massot (Sep 19 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134232174):
<p>yes, it's computer imitating ants who are stupid but exhibit collective intelligence</p>

#### [ Patrick Massot (Sep 19 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/physics%20attack/near/134232462):
<p>done</p>


{% endraw %}
