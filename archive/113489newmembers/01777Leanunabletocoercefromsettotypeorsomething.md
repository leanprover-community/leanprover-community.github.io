---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01777Leanunabletocoercefromsettotypeorsomething.html
---

## Stream: [new members](index.html)
### Topic: [Lean unable to coerce from set to type (or something)](01777Leanunabletocoercefromsettotypeorsomething.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 01 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136915550):
(approximately M)WE:

```lean
import data.set.basic
import data.set.lattice
universe u

variable {X : Type u}
variable {Y : Type u}
variable {f : X → Y}

def G (f : X → Y) : set (X × Y) := { g | g.2 = f (g.1) }
def p1 (g : G f) : X := g.1.1
def injectivity' {X' Y' : Type} (g : X' → Y') := ∀ x1 x2 : X', g x1 = g x2 → x1 = x2
def surjectivity' {X' Y' : Type} (g : X' → Y') := ∀ y : Y', ∃ x : X', g x = y
def bijectivity' {X' Y' : Type} (g : X' → Y') := injectivity' g ∧ surjectivity' g

theorem bij_p1 : @bijectivity' (↥(set (X × Y))) (↥(G f)) (p1) :=
    begin
        sorry,
    end

#check p1
#check bijectivity'
```

But Lean doesn't seem to understand that `↥(set (X × Y)` is a Type -- it gives me the error `failed to synthesise type class instance for: has_coe_to_sort (Type u)`. What's going on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 01 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136918282):
```lean
import data.set.basic
import data.set.lattice
universe u

variable {X : Type u}
variable {Y : Type u}
variable {f : X → Y}

def G (f : X → Y) : set (X × Y) := { g | g.2 = f (g.1) }
def p1 (g : G f) : X := g.1.1
def injectivity' {X' Y' : Type u} (g : X' → Y') := ∀ x1 x2 : X', g x1 = g x2 → x1 = x2
def surjectivity' {X' Y' : Type u} (g : X' → Y') := ∀ y : Y', ∃ x : X', g x = y
def bijectivity' {X' Y' : Type u} (g : X' → Y') := injectivity' g ∧ surjectivity' g

theorem bij_p1 : @bijectivity' (↥(G f)) X (p1) :=
    begin
        sorry,
    end

#check p1
#check bijectivity'
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 01 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136918283):
universe issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 01 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136918689):
Oh -- of course. Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 01 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136918860):
And I have no clue why I was putting in the domain and range of `f` instead of `p1`.


{% endraw %}
