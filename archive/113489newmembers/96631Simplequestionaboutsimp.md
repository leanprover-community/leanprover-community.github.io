---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/96631Simplequestionaboutsimp.html
---

## Stream: [new members](index.html)
### Topic: [Simple question about simp](96631Simplequestionaboutsimp.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Dec 11 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simple%20question%20about%20simp/near/151460730):
The behavior of simp depends on how the rules for computing function values are presented, in a way I don't quite understand. What follows are two ways of writing a list append function. The first case is verbose, as it lists rules for all four combinations of nil and non-nil values. The second is more concise and is the usual way one would see this function defined. Following the alternative implementations is part of a proof that a length function distributes over append. When the first definition of append is used, the simp in the last line of the proof fails, while if the second, simp succeeds. The expressions to be simplified are the same in both cases. Thanks for enlightening me as to why this is so. I know this is an easy one. --ks

``` lean
inductive nlist : Type 
| nil : nlist
| cons : ℕ → nlist → nlist

``` lean
def len : nlist → ℕ
| nlist.nil := 0
| (nlist.cons h t) := 1 + len t

``` lean
def app : nlist → nlist → nlist
| nlist.nil nlist.nil  := nlist.nil 
| nlist.nil l2 := l2
| l1 nlist.nil := l1
| (nlist.cons h t) l2 := nlist.cons h (app t l2)
```

``` lean
def app  : nlist → nlist → nlist
| nlist.nil l2  := l2
| (nlist.cons h t) l2 := nlist.cons h (app t l2)
```

``` lean
example : 
    ∀ l1 l2 : nlist, 
        len (app l1 l2) = (len l1) + (len l2) :=
begin
intros l1 l2,
induction l1,
simp [len],
-- len (app nlist.nil l2) = len l2
simp [app], 
_
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Dec 11 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simple%20question%20about%20simp/near/151461827):
@**Kevin Sullivan** It's easier to answer these questions if you can post a full example -- we can't try that out without definitions for `nlist` and `len`. But you can see the difference between the two by comparing the outputs of `#print prefix app`. The simp lemmas that are generated for the first definition will only fire when argument 2 is either `nil` or `cons` because you've defined those cases differently. You'd need to do something like `cases l2; simp [app]` to use that definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Sullivan (Dec 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simple%20question%20about%20simp/near/151462030):
```quote
@**Kevin Sullivan** It's easier to answer these questions if you can post a full example -- we can't try that out without definitions for `nlist` and `len`. But you can see the difference between the two by comparing the outputs of `#print prefix app`. The simp lemmas that are generated for the first definition will only fire when argument 2 is either `nil` or `cons` because you've defined those cases differently. You'd need to do something like `cases l2; simp [app]` to use that definition.
```
 
Yes, just added previous defs to message above. Will evaluate your answer. Thank you, Rob.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 12 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simple%20question%20about%20simp/near/151510730):
```quote
Yes, just added previous defs to message above. Will evaluate your answer. Thank you, Rob.
```
Logically equivalent definitions can sometimes create different equation lemmas which would affect the behaviour of `simp`. I am not a computer scientist, but I *think* that what `simp [len]`actually does it that it tells Lean to use the so-called equation lemmas for `len`, which you can see yourself by typing `#print prefix len.equations`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 12 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simple%20question%20about%20simp/near/151511099):
OK so this is the question, I think:

```lean
inductive nlist : Type
| nil : nlist
| cons : ℕ → nlist → nlist

def len : nlist → ℕ
| nlist.nil := 0
| (nlist.cons h t) := 1 + len t

def app1 : nlist → nlist → nlist
| nlist.nil nlist.nil  := nlist.nil
| nlist.nil l2 := l2
| l1 nlist.nil := l1
| (nlist.cons h t) l2 := nlist.cons h (app1 t l2)

def app2  : nlist → nlist → nlist
| nlist.nil l2  := l2
| (nlist.cons h t) l2 := nlist.cons h (app2 t l2)

example :
  ∀ l1 l2 : nlist,
    len (app1 l1 l2) = (len l1) + (len l2) :=
begin
  intros l1 l2,
  induction l1,
  { simp only [len],
    simp [app1],
    -- goal len (app1 nlist.nil l2) = len l2
    sorry
  },
  sorry
end

example :
  ∀ l1 l2 : nlist,
    len (app2 l1 l2) = (len l1) + (len l2) :=
begin
  intros l1 l2,
  induction l1,
  { simp only [len],
    simp [app2],
    -- no goals this time
  },
  sorry
end
```

Trying to prove the same thing with the two equivalent definitions, but a technique succeeds with `app2` and fails with `app1`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 12 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simple%20question%20about%20simp/near/151511168):
I changed your `simp [len]` to `simp only [len]` because you are not supposed to use `simp` in the middle of a proof -- people can add and remove simp lemmas whenever they like, which makes the behaviour unpredictable, so the general rule is to only use it to close a goal or else you are writing code which is hard to maintain.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 12 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simple%20question%20about%20simp/near/151511471):
So the problem is exactly what Rob says: at the crucial moment where the stories diverge you are faced with a goal containing `app nlist.nil l2` and if you want to use `simp` then you are going to be hoping that the equation lemmas for `app` can deal with this. Now the equation lemmas aren't a big secret here -- they are the things you used to define `app`. So if you use `app1` then there are four equation lemmas, saying what to do in the nil/nil, nil/cons, cons/nil and cons/cons case, as you can see with `#print prefix app1.equations`. But none of these are any use to you if your goal is `app1 nlist.nil l2` because we don't know whether `l2` is a nil or a cons, so none of the lemmas apply! You can guess the rest. The equation lemmas for `app2` explicitly mention this nil/l2 case, so `simp` works. And as Rob also said, the way to fix this in the app1 situation is to branch on whether `l2` is a nil or a cons using induction or cases.

