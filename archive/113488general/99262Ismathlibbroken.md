---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99262Ismathlibbroken.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Is mathlib broken?](https://leanprover-community.github.io/archive/113488general/99262Ismathlibbroken.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 05 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292498):
<p>I do not expect mathlib to be working 24/7 but I am wondering if it currently broken for everyone or just me. I have problems in prod.lean with <code>prod.mk.eta</code> on line 21 -- <code>invalid definition, a declaration named 'prod.mk.eta' has already been declared</code></p>

#### [ Kevin Buzzard (Mar 05 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292504):
<p>The reason I ask is that I have a file which reaches unreachable code</p>

#### [ Kevin Buzzard (Mar 05 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292507):
<p>and it probably it would be better if this were the only error rather than all the sorrys which currently come with it</p>

#### [ Kevin Buzzard (Mar 05 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292510):
<p>which may or may not be part of the problem</p>

#### [ Kevin Buzzard (Mar 05 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292573):
<p>current version is here : <a href="https://gist.github.com/kbuzzard/50a650e6df7e712138456facb5a81f22" target="_blank" title="https://gist.github.com/kbuzzard/50a650e6df7e712138456facb5a81f22">https://gist.github.com/kbuzzard/50a650e6df7e712138456facb5a81f22</a> but I also have 4 sorrys from mathlib so I'll try to remove mathlib</p>

#### [ Moses Schönfinkel (Mar 05 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123292628):
<p>Broken for me as well.</p>

#### [ Johannes Hölzl (Mar 05 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305123):
<p>It should work again.</p>

#### [ Johannes Hölzl (Mar 05 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305506):
<p><span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> the generalization of the <code>do</code>-notation resulted in the following work around:  <a href="https://github.com/leanprover/mathlib/commit/ec9dac3ada9aa2107d5f3fceb3d28eee113278b8#diff-d49a7b7cdfea7e016e137ab7be5dc597L65" target="_blank" title="https://github.com/leanprover/mathlib/commit/ec9dac3ada9aa2107d5f3fceb3d28eee113278b8#diff-d49a7b7cdfea7e016e137ab7be5dc597L65">https://github.com/leanprover/mathlib/commit/ec9dac3ada9aa2107d5f3fceb3d28eee113278b8#diff-d49a7b7cdfea7e016e137ab7be5dc597L65</a><br>
I don't know what exactly is happening, it claims to expect a <code>name</code>, but gets a <code>tactic _</code>. Is there a way to see what overloaded <code>bind</code> is used in the error message? <code>pp.full_names</code> etc didn't work for me.</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305570):
<p>Urgh, pretty sure it's trying to do a recursive call</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305576):
<p>Could you post the error?</p>

#### [ Johannes Hölzl (Mar 05 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305709):
<p>Ah yes, looks like this (now I also added <code>pp.locals_full_name</code>:</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  &lt;bind.0._fresh.31.20685&gt; (&lt;c₁.0._fresh.31.20672&gt; &lt;r.0._fresh.31.20695&gt; &lt;e.0._fresh.31.20699&gt;)
term
  &lt;c₁.0._fresh.31.20672&gt; &lt;r.0._fresh.31.20695&gt; &lt;e.0._fresh.31.20699&gt;
has type
  tactic (old_conv_result &lt;α.0._fresh.31.20670&gt;)
but is expected to have type
  name
</pre></div>

#### [ Johannes Hölzl (Mar 05 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305785):
<p>Would it make sense to force the namespace of <code>bind</code>, like the <code>begin [m]</code> notation does? But it gets a ambiguous with <code>do [c] &lt;- l, ...</code></p>

#### [ Sebastian Ullrich (Mar 05 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305831):
<p>The real issue is that the local for recursive calls ignores the <code>protected</code> specifier, imo</p>

#### [ Johannes Hölzl (Mar 05 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Is%20mathlib%20broken%3F/near/123305899):
<p>Or this!</p>


{% endraw %}
