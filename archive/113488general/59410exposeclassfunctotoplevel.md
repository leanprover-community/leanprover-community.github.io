---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59410exposeclassfunctotoplevel.html
---

## Stream: [general](index.html)
### Topic: [expose class func to top-level](59410exposeclassfunctotoplevel.html)

---


{% raw %}
#### [ Zesen Qian (Jun 06 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674397):
Hi, how can I expose a function defined in type class to the top-level? i.e., the way to_string is exposed.

#### [ Simon Hudon (Jun 06 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674462):
You can do `export has_to_string (to_string)`

#### [ Zesen Qian (Jun 06 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674583):
the function it exposes doesn't seem to the one I want. I have to provide the type parameter.

#### [ Zesen Qian (Jun 06 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674595):
I hope I can write `to_string 5` instead of `to_string nat 5`

#### [ Zesen Qian (Jun 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674650):
ahh sorry, seem in my case, the type inference doesn't work; in other case it works well.

#### [ Simon Hudon (Jun 06 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674679):
I think there are two ways of doing that. Either you write a definition in the global namespace where you have fine control over implicit / explicit parameters or you use the following:

```
class my_algebra (a : Type) :=
  (zero {} : a)
```

I haven't used it myself but I think it should work.

#### [ Simon Hudon (Jun 06 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674742):
(I just tried it. It works)

#### [ Zesen Qian (Jun 06 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674747):
thanks! now it works.

#### [ Zesen Qian (Jun 06 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674821):
question: how to give the checker a hint for synthesis?

#### [ Simon Hudon (Jun 06 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674837):
Do you mean elaboration, i.e. inferring the type that are not explicitly required?

#### [ Zesen Qian (Jun 06 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674850):
yes. But in my case it can't be inferred, so I want to give it a hint of the type.

#### [ Simon Hudon (Jun 06 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127674922):
If your function is `foo`, `@foo` makes every implicit parameters (types, type class instances and others) explicit. It's a bit of all or nothing but there are ways to simplify if that comes up too often.

#### [ Simon Hudon (Jun 06 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127675004):
Sorry, my brain is currently working in Haskell. In Lean, if that comes up too often, you may have to make the parameter explicit. Before you get there, can give some type annotations in the form of `(expr : type)`

#### [ Simon Hudon (Jun 06 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127675084):
For example if your function infers a type from its list argument but you provide an empty list, you can write `foo ([] : list a)` or `foo (@nil a)`

#### [ Zesen Qian (Jun 06 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expose%20class%20func%20to%20top-level/near/127675179):
yep! I just used annotation and it works well.


{% endraw %}
