---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/81673extractingtacticsandproofterms.html
---

## Stream: [new members](index.html)
### Topic: [extracting tactics and proof terms](81673extractingtacticsandproofterms.html)

---

#### [Michael Jendrusch (Nov 12 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/extracting%20tactics%20and%20proof%20terms/near/147516992):
This is probably a question with a simple answer, but I'll ask it either way. Is there a way to programmatically extract the sequence of tactics used to prove a given lemma? I can get the proof term pretty easily by doing something like this:

```lean
import tactic
open tactic.interactive

namespace my_namespace

lemma my_lemma : Π n : ℕ, n + 1 > n :=
begin
  intros,
  rw gt,
  simp,
  comp_val,
end

#eval do
  env ← tactic.get_env,
  ml  ← env.get(mk_str_name "my_namespace" "my_lemma"),
  fmt ← tactic_format_expr ml.value,
  trace $ "type  : " ++ (to_string $ expr.to_raw_fmt ml.type) ++ "\n",
  trace $ "value : " ++ (to_string $ expr.to_raw_fmt ml.value) ++ "\n",
  return unit.star

end my_namespace
```

but I haven't had any luck extracting tactics yet. On another note, is there some function other than `expr.to_raw_fmt` for serializing expressions?

#### [Mario Carneiro (Nov 12 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/extracting%20tactics%20and%20proof%20terms/near/147517509):
No. It's not stored

#### [Keeley Hoek (Nov 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/extracting%20tactics%20and%20proof%20terms/near/147517700):
What do you mean "serializing"?

#### [Michael Jendrusch (Nov 12 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/extracting%20tactics%20and%20proof%20terms/near/147519876):
Serializing, as in generating some text (s-expression, JSON) or binary representation of expressions which can be read from another program. But I suppose `expr.to_raw_fmt`should be enough for my purposes.

