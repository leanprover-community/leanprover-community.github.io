---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/96236Wellfoundednessdeclarations.html
---

## Stream: [new members](index.html)
### Topic: [Well foundedness declarations](96236Wellfoundednessdeclarations.html)

---


{% raw %}
#### [ Ken Roe (Jul 11 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Well%20foundedness%20declarations/near/129479543):
It seems for the mutually recursive function below, Lean cannot find the well founded relation.  How can I specify the relation?

inductive Value : Type
| NatValue : ℕ -> Value
| ListValue : list Value -> Value
| NoValue : Value

mutual def findRecord, findRecordHelper
with findRecord : ℕ → Value → (list Value)
| l (Value.ListValue ((Value.NatValue x)::r)) :=
                 if beq_nat x l then
                     ((Value.NatValue x)::r)
                 else findRecordHelper x r
| _ _ := list.nil
with findRecordHelper : ℕ → (list Value) → (list Value)
| _ list.nil := list.nil
| v (f::r) := match findRecord v f with
              | list.nil := findRecordHelper v r
              | x        := x
              end.

#### [ Kevin Buzzard (Jul 11 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Well%20foundedness%20declarations/near/129479933):
Do you know about the triple back tick thing? It makes code much easier to read

#### [ Kevin Buzzard (Jul 11 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Well%20foundedness%20declarations/near/129479954):
` ```lean ` at the beginning and ` ``` ` at the end

#### [ Ken Roe (Jul 11 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Well%20foundedness%20declarations/near/129480038):
Here it is with the triple back thing.
```lean
inductive Value : Type
| NatValue : ℕ -> Value
| ListValue : list Value -> Value
| NoValue : Value

mutual def findRecord, findRecordHelper
with findRecord : ℕ → Value → (list Value)
| l (Value.ListValue ((Value.NatValue x)::r)) :=
if beq_nat x l then
((Value.NatValue x)::r)
else findRecordHelper x r
| _ _ := list.nil
with findRecordHelper : ℕ → (list Value) → (list Value)
| _ list.nil := list.nil
| v (f::r) := match findRecord v f with
| list.nil := findRecordHelper v r
| x := x
end.
```


{% endraw %}
