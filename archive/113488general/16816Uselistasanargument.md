---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16816Uselistasanargument.html
---

## Stream: [general](index.html)
### Topic: [Use list as an argument](16816Uselistasanargument.html)

---


{% raw %}
#### [ Blair Shi (Jul 11 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458509):
I define a function which takes a list as a argument but I do not know why it always break when I use it in my other theorem or function.
my function no error:
```
def f_span (l : list V) : set V :=
span {vc : V | vc ∈ l}
```
use it later in
```
def are_basis_equal (l₀ : list V) (l₁ : list V) : Prop := 
∀vc : V, vc ∈ (f_span l₀) ∧ vc ∈ (f_span l₁) 
```
it reports error :
```
[Lean]
type mismatch at application
  f_span l₀
term
  l₀
has type
  list V : Type v
but is expected to have type
  Type ? : Type (?+1)
```

#### [ Kevin Buzzard (Jul 11 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458841):
You have some variable `V` somewhere, I guess?

#### [ Kevin Buzzard (Jul 11 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458858):
If you look at what you wrote as the definition of `f_span` then it *looks* like it is expecting one input, namely `l` of type `list V`

#### [ Kevin Buzzard (Jul 11 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458871):
But after the definition of `f_span`, if you write `#check f_span` you will probably see a different story!

#### [ Kevin Buzzard (Jul 11 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458902):
Probably `f_span` is also expecting you to input `V` itself. So that's my guess as to what your error is caused by -- you need `f_span V l_0`

#### [ Kevin Buzzard (Jul 11 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129458955):
The trick is to make `V` a `{}` variable; then `f_span` won't ask for it. I've got to run but that's the idea

#### [ Sean Leather (Jul 11 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129459298):
```quote
But after the definition of `f_span`, if you write `#check f_span` you will probably see a different story!
```
Even better would be to write `#check @f_span`. That fills in those pesky metavariables with something readable.

#### [ Blair Shi (Jul 11 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129459870):
I added more argument using `[]` and it works now. thank you !

#### [ Sean Leather (Jul 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129460007):
@**Blair Shi** Can you show us what it looks like now?

#### [ Blair Shi (Jul 11 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129460651):
```
def f_span (l : list V) : set V :=
span {vc : V | vc ∈ l}
def are_basis_equal (l₀ : list V) (l₁ : list V) : Prop := 
∀vc : V, vc ∈ (f_span k V l₀) ∧ vc ∈ (f_span k V l₁) 
```
I just added k V everywhere when I using the function `f_span` without any change of `f_span` 

Because if you check my `f_span`, the type is
```
f_span :
  Π (k : Type u_1) (V : Type u_2) [_inst_1 : field k] [_inst_2 : ring k] [_inst_3 : module k V], list V → set V
```

I also tried like added `(k : Type u_1) (V : Type u_2) [_inst_1 : field k] [_inst_2 : ring k] [_inst_3 : module k V]` all of them as arguments to my `f_span` but I realized I don't need to do so. But adding arguments also works for me.

#### [ Patrick Massot (Jul 11 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129460809):
Are you sure you're not duplicating stuff around https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L122?

#### [ Blair Shi (Jul 11 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129461143):
@**Patrick Massot**  because the vector space in mathlib does not support finite dimensional vector space. I am currently working on finite dimensional vector space and in the definition of finite dimensional vector space, the basis is a list.

#### [ Blair Shi (Jul 11 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129461329):
@**Sean Leather** 
I realized I have wrote the global variables and if I delete them the code does not work
```
variables (k : Type u) (V : Type v)
variable [field k]
variables [ring k] [module k V]
variables (a : k) (b : V)
include k 
```

#### [ Patrick Massot (Jul 11 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129461449):
Ok. I remember we had this discussion about ordering basis elements here.

#### [ Mario Carneiro (Jul 11 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129461828):
You want `variables {k : Type u} {V : Type v}` in the first line

#### [ Blair Shi (Jul 11 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129462340):
I change it to be `{k : Type u} {V : Type v}`as you said. Now I delete all `k V` when I use the function:)

#### [ Kevin Buzzard (Jul 11 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129462359):
ordering basis elements -- it's a funny situation! In the general case you seem to want a basis to be a set. But to prove the standard undergraduate theorems about linear maps = matrices you seem to want the basis to be a finite totally ordered set.

#### [ Kevin Buzzard (Jul 11 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Use%20list%20as%20an%20argument/near/129462488):
@**Blair Shi** yes -- if you are doing vector spaces over a field field `k` then you don't want to have to keep mentioning `k`. If you're doing `k`-linear maps between vector spaces `V` and `W` then you probably want to mention `V` but if you're doing things with a fixed `V` like showing that sets of size less than dim(V) can't span then you might not even want to mention `V`. This is how those `{}` and `()` brackets that I talked about in my lecture on Monday work in practice. There are tricks to change the variable from `()` to `{}`and back in the middle of a file which I can tell you about later if you need them.


{% endraw %}
