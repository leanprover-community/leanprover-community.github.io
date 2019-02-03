---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59410exposeclassfunctotoplevel.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [expose class func to top-level](https://leanprover-community.github.io/archive/113488general/59410exposeclassfunctotoplevel.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Zesen Qian (Jun 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674397):
<p>Hi, how can I expose a function defined in type class to the top-level? i.e., the way to_string is exposed.</p>

#### [ Simon Hudon (Jun 06 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674462):
<p>You can do <code>export has_to_string (to_string)</code></p>

#### [ Zesen Qian (Jun 06 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674583):
<p>the function it exposes doesn't seem to the one I want. I have to provide the type parameter.</p>

#### [ Zesen Qian (Jun 06 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674595):
<p>I hope I can write <code>to_string 5</code> instead of <code>to_string nat 5</code></p>

#### [ Zesen Qian (Jun 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674650):
<p>ahh sorry, seem in my case, the type inference doesn't work; in other case it works well.</p>

#### [ Simon Hudon (Jun 06 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674679):
<p>I think there are two ways of doing that. Either you write a definition in the global namespace where you have fine control over implicit / explicit parameters or you use the following:</p>
<div class="codehilite"><pre><span></span>class my_algebra (a : Type) :=
  (zero {} : a)
</pre></div>


<p>I haven't used it myself but I think it should work.</p>

#### [ Simon Hudon (Jun 06 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674742):
<p>(I just tried it. It works)</p>

#### [ Zesen Qian (Jun 06 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674747):
<p>thanks! now it works.</p>

#### [ Zesen Qian (Jun 06 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674821):
<p>question: how to give the checker a hint for synthesis?</p>

#### [ Simon Hudon (Jun 06 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674837):
<p>Do you mean elaboration, i.e. inferring the type that are not explicitly required?</p>

#### [ Zesen Qian (Jun 06 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674850):
<p>yes. But in my case it can't be inferred, so I want to give it a hint of the type.</p>

#### [ Simon Hudon (Jun 06 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674922):
<p>If your function is <code>foo</code>, <code>@foo</code> makes every implicit parameters (types, type class instances and others) explicit. It's a bit of all or nothing but there are ways to simplify if that comes up too often.</p>

#### [ Simon Hudon (Jun 06 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127675004):
<p>Sorry, my brain is currently working in Haskell. In Lean, if that comes up too often, you may have to make the parameter explicit. Before you get there, can give some type annotations in the form of <code>(expr : type)</code></p>

#### [ Simon Hudon (Jun 06 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127675084):
<p>For example if your function infers a type from its list argument but you provide an empty list, you can write <code>foo ([] : list a)</code> or <code>foo (@nil a)</code></p>

#### [ Zesen Qian (Jun 06 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127675179):
<p>yep! I just used annotation and it works well.</p>


{% endraw %}
