---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98316haveIbug.html
---

## Stream: [general](index.html)
### Topic: [haveI bug](98316haveIbug.html)

---

#### [Chris Hughes (Sep 12 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/haveI%20bug/near/133810460):
There's a bug in `haveI` when the type is not given, but can be inferred, and the user has more than one goal.
Here's an MWE
```lean
inductive T : Type
| t : T

lemma subsingleton_T : subsingleton T := ⟨λ x y, by cases x; cases y; refl⟩

lemma foo (x y : T) : x = y ∧ x = y :=
begin
  split,
  haveI := subsingleton_T,
  exact subsingleton.elim _ _, -- failed to synthesize type class instance
end


lemma bar (x y : T) : x = y :=
begin
  haveI := subsingleton_T,
  exact subsingleton.elim _ _, -- no errors
end

lemma baz (x y : T) : x = y ∧ x = y :=
begin
  have := subsingleton_T,
  split,
  haveI := subsingleton_T,
  admit,
  exact subsingleton.elim _ _, -- works, instance cache has been reset for second goal
end
```
I think it's something to do with the line `swap >> reset_instance_cache >> swap` in the definition of `haveI`, if it inferred the type successfully, but you have another goal anyway, it resets the instance cache for your second goal, but not the first.

