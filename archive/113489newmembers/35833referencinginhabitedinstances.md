---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/35833referencinginhabitedinstances.html
---

## Stream: [new members](index.html)
### Topic: [referencing inhabited instances](35833referencinginhabitedinstances.html)

---


{% raw %}
#### [ Ken Roe (Aug 11 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/referencing%20inhabited%20instances/near/131964186):
If I declare values as inhabited instances, how do I reference the instances?
```lean
def cell := option ℕ
def heap := ℕ → option ℕ
def env := ident → ℕ

instance : inhabited env := ⟨λ x, 0⟩
instance : inhabited heap := ⟨λ h, none⟩
instance : inhabited cell := ⟨none⟩

def empty_env env :=  env.inhabited

def empty_heap : heap  := heap.inhabited

def empty_cell : option ℕ := cell.inhabited
```
The last three "def" constructs don't seem to work.

#### [ Simon Hudon (Aug 11 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/referencing%20inhabited%20instances/near/131964248):
If you write `#print inhabited` you should see the following appear:

```lean
@[class]
structure inhabited : Sort u → Sort (max 1 u)
fields:
inhabited.default : Π (α : Sort u) [c : inhabited α], α
```

This tells you that `default env` is what you want.


{% endraw %}
