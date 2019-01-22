---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55694namespace.html
---

## [general](index.html)
### [namespace](55694namespace.html)

#### [Kevin Buzzard (Jul 21 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130048945):
I thought it was about time I read through theorem proving in Lean again, to make sure I understand it 100% now. I don't. 

```lean
namespace foo 

def a : ℕ := 5 
def f (x : ℕ) : ℕ := x + 7 
def fa : ℕ := f a 
def ffa : ℕ := f (f a) 

#print "inside foo" 

#check a 
#check f 
#check fa 
#check ffa 
#check foo.fa 

end foo 
```

#### [Kevin Buzzard (Jul 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130048997):
Why does that last `#check` work? What if there had been a `foo.foo.fa`? Who wins? Can I control who wins?

#### [Mario Carneiro (Jul 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130048998):
you have a misplaced `#`

#### [Kevin Buzzard (Jul 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049000):
I'm on my phone, sorry

#### [Kenny Lau (Jul 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049002):
I think the definition closest to your "#check" wins

#### [Kenny Lau (Jul 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049014):
```lean
namespace foo

def fa : ℕ := 5
def foo.fa : ℤ := 5

#print "inside foo"

#check fa      -- fa : ℕ
#check foo.fa  -- foo.fa : ℤ

end foo
```

#### [Kevin Buzzard (Jul 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049020):
In a nested namespace situation what are the rules?

#### [Kevin Buzzard (Jul 21 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049065):
And can I bend them with extra annotations? Is this to do with `private`?

#### [Mario Carneiro (Jul 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049068):
Kenny, interchanging the definition order there doesn't change the result

#### [Kenny Lau (Jul 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049071):
hmm

#### [Kenny Lau (Jul 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049072):
surely Mario knows why

#### [Mario Carneiro (Jul 21 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049076):
well, it's not to hard to come up with a post hoc rule given this data

#### [Kevin Buzzard (Jul 21 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049119):
I don't have access to lean right now

#### [Kevin Buzzard (Jul 21 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049121):
That's why I'm reading TPIL :-)

#### [Mario Carneiro (Jul 21 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049179):
Okay, here's the rule, I think: If you are in `namespace foo`, ignoring `open`s, you can refer to things in the root namespace, and in the `foo` namespace. You can also refer to things in namespaces below that by adding prefixes relative to one of these roots. If there is a conflict, then the stuff in namespace `foo` wins over the root namespace

#### [Mario Carneiro (Jul 21 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049230):
So `#check foo.fa` inside namespace `foo` refers to `foo.fa` relative to the root namespace. If there was a `foo.foo.fa` it would take precedence over this

#### [Kevin Buzzard (Jul 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049807):
I think I meant `protected` not `private`

#### [Kevin Buzzard (Jul 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049808):
Difficult to check right now

#### [Mario Carneiro (Jul 21 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049967):
Something with `protected` marking cannot be referred to without its last namespace. So if `A.B.C` was declared `protected` then it could be referred to as `A.B.C` or `B.C` but not `C`

#### [Mario Carneiro (Jul 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130050030):
Something with `private` marking has a name which is rather obscured, usually something like `_private.12345.name`. Inside the section/namespace it is declared, you can use `name` as its short name, but after that it is essentially inaccessible. I don't think it participates in namespacing

#### [Mario Carneiro (Jul 21 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130050319):
after some testing, it looks like you can't actually type `_private.12345.name` and refer to the private value since the `12345` is a numeric name part, which you can't type using the usual lean parser. You can refer to it using tactics though. Here's a silly example:
```lean
import data.quot

section foo
private def my_password : ℕ := 57

def I_haz_pass : trunc ℕ := trunc.mk my_password
end foo

open tactic
def evil : ℕ := by do
  env ← get_env,
  d ← env.get ``I_haz_pass,
  `(trunc.mk %%e) ← return d.value,
  exact e
#eval evil -- 57
example : evil = 57 := rfl
```

#### [Mario Carneiro (Jul 21 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130050377):
the lesson here is that `private` definitions are not an impermeable abstraction layer, if you want to use them to hide the details of a construction. If consistency depends on this (e.g. Dan Licata's trick) then it's not a good plan

#### [Kevin Buzzard (Jul 21 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130052500):
Thanks for the detective work!

I'm 1/3 of the way through my 100% playthrough of TPIL.

