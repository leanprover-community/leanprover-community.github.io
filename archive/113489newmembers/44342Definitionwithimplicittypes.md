---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/44342Definitionwithimplicittypes.html
---

## Stream: [new members](index.html)
### Topic: [Definition with implicit types](44342Definitionwithimplicittypes.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 11 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437343):
Can someone correct the syntax for this definition:

def bind_option : {Π X : Type}, {Π Y : Type},
                option X → (X → option Y)
                      → option Y
| option.none f := @option.none Y
| (option.some x) f := f x

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437504):
What error do you get?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 11 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437545):
Also, can you enclose your code between three ticks: 

````
```lean
-- your code here
```
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437565):
```lean
def bind_option {X : Type} {Y : Type} :
option X → (X → option Y)
→ option Y
| option.none f := @option.none Y
| (option.some x) f := f x
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437580):
pattern matching is done on everything after the colon, which is why is moved the Types before the colon.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437585):
```lean
def bind_option {X : Type} {Y : Type} :
option X → (X → option Y)
→ option Y
| none f := none
| (some x) f := f x
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437635):
Also Pi should be out of the brackets like this ` Π {X Y : Type},`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437641):
If you were to put the Types after the colon.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 11 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437648):
Incidentally this function exists in the library and it's called `option.bind` I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 11 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438139):
Not quite--I get the following error on the "f x" term of the last line:

function expected at
  f x
term has type
  option Y

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438270):
perhaps you have something on the following line(s)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438273):
after the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 11 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438577):
This was the problem.  The error goes away if I add a period.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 11 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438647):
Usually we fix this by just having the next line start with some kind of command like `def`, `namespace`, or a comment. Presumably that line is giving you an error anyway otherwise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 11 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438654):
what can there be after that thing? I think all my lines start with keywords

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 11 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129456152):
Btw, we're thinking of not allowing function applications to stretch over empty lines in Lean 4 to fix such issues. I do hope that would not break anyone's weird code...?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129456661):
I see newbie errors like this all the time (I'm currently teaching Lean to a bunch of people)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129456667):
the function expects one or two more values so it just starts eating into the next command

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129456671):
resulting in errors which completely throw the user


{% endraw %}
