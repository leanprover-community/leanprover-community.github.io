---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93453nonexhaustiveformeta.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [non-exhaustive for meta](https://leanprover-community.github.io/archive/113488general/93453nonexhaustiveformeta.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Zesen Qian (Jul 09 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129371844):
<p>If we allow non-termination at meta level, shouldn't we also allow non-exhaustive match?</p>

#### [ Simon Hudon (Jul 09 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129372015):
<p>There are a lot of possibilities. While mandatory termination is very restrictive, exhaustiveness is not and it has great benefits. It allows Lean to tell you when you're messing up</p>

#### [ Simon Hudon (Jul 09 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129372069):
<p>Whenever you would leave some cases out, it is a good practice to write an error message instead</p>

#### [ Simon Hudon (Jul 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129372151):
<p>You're making clear to any reader that you don't accept every input</p>

#### [ Zesen Qian (Jul 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373623):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> by error message you mean type level error? or is there some backdoor at meta-level that I can just halt the program in case of non-exhaustion?</p>

#### [ Zesen Qian (Jul 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373691):
<p>because I'm pretty sure the rest case is not going to happen(and if it happens, that means problem in my meta-code).</p>

#### [ Simon Hudon (Jul 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373788):
<p>If you're in <code>tactic</code>, you can use <code>fail my_error_message</code> to report the error ... it might actually a good enough reason to write code in <code>tactic</code></p>

#### [ Simon Hudon (Jul 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373814):
<p>But that's not a backdoor, you can write trusted code in a similar way (but with different monads than <code>tactic</code> because <code>tactic</code> is <code>meta</code>)</p>

#### [ Zesen Qian (Jul 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373829):
<p>hmm, what about a meta-program that simply returns a proof? </p>
<div class="codehilite"><pre><span></span>prog : hint -&gt; pexpr
</pre></div>

#### [ Zesen Qian (Jul 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373904):
<p>because the generation of the proof doesn't depends on inspection of the prover's environment, but only on the hint.</p>

#### [ Simon Hudon (Jul 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129373988):
<p>You can return a default value like <code> ``(Type) </code></p>

#### [ Gabriel Ebner (Jul 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129374000):
<p>There is also <code>undefined_core "my error message"</code></p>

#### [ Zesen Qian (Jul 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/non-exhaustive%20for%20meta/near/129374011):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> I think that's what I wanted.</p>


{% endraw %}
