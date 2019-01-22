---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/00131Howtounpacknotation.html
---

## [new members](index.html)
### [How to "unpack" notation?](00131Howtounpacknotation.html)

#### [Abhimanyu Pallavi Sudhir (Oct 14 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135784139):
How can I "unpack" notation like `∉`, `∩`, etc.? I want to convert a proposition of the form `x ∉ S` to `x ∈ S → false`. Is this possible just definitionally or do I need to apply some lemma?

#### [Abhimanyu Pallavi Sudhir (Oct 14 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135784203):
You'd think just `change` should work, but it doesn't seem to do anything.

#### [Bryan Gin-ge Chen (Oct 14 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135784328):
This doesn't directly answer your question (which I think might be more a matter of how to get lean to avoid printing certain notation), but given `h : x ∉ S` and `H : x ∈ S`, the term `h H` is `false`. For this reason I don't think I've ever needed to change things like you're describing.

#### [Abhimanyu Pallavi Sudhir (Oct 14 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135784372):
But in that case, shouldn't `not_forall_not` work on something of the form `¬∀ (x : S), x ∉ T`? It gives me an error `invalid rewrite tactic, failed to synthesize type class instance`.

#### [Rob Lewis (Oct 14 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135784458):
`not_forall_not` requires the predicate to be decidable. Try putting `local attribute [instance] classical.prop_decidable` somewhere above your proof.

#### [Abhimanyu Pallavi Sudhir (Oct 14 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135784508):
That works, thanks. But what exactly does it do? Does it just tell Lean that all propositions are decidable or is there something more? (If so, is it really any different from classical.em?)

#### [Rob Lewis (Oct 14 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135784952):
Yes, it adds a (local) type class instance that tells Lean all propositions are decidable. It's derived from classical.em.

#### [Rob Lewis (Oct 14 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135785028):
A lot of things are written using decidability instances, like the `if p then _ else _` notation. If you're working classically and don't care about decidability, you need that line at the top of your file.

#### [Abhimanyu Pallavi Sudhir (Oct 14 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135785089):
Ah ok -- so both em and prop-decidable follow from the same mathematical law, but have different types.

#### [Rob Lewis (Oct 14 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135785202):
Exactly. `em` produces a proof, `prop_decidable` produces data.

#### [Kevin Buzzard (Oct 14 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135786589):
Abhi -- whenever you see a `failed to synthesize type class instance` error this means that the type class inference machine (the square bracket machine) has failed. The error often shows exactly what it has failed to construct (it was trying to fill in a variable you did not give it explicitly because it was in square brackets, and the goal in the error is the type of the term it failed to construct). 

```lean
import logic.basic

#check @not_forall_not
```

shows you that for this function to run in the usual way (i.e. without any messing around with `@`) Lean needs to get the type class machine to produce a proof of `decidable (∃ (x : α), p x)`. If `p` is random then Lean can't do this (because there are examples in computer science where this sort of this really is not decidable). But note that ` (∃ (x : α), p x)` is a proposition, so if you decide to be a mathematician and work in our wonderful world where every proposition is decidable (indeed, in classical mathematics there is no notion of decidability), then you can tell the type class inference machine that this is what you want to do by feeding  the relevant definition into the machine. 

Now if you were making the definition "all propositions are decidable" from scratch you could just use the `instance` keyword instead of the `definition` one, but in this case the relevant claim that all propositions are decidable is already a definition (`classical.prop_decidable`) and it's in core Lean. The issue is hence that this definition is not something which the machine knows about. Rob's trick `local attribute [instance] classical.prop_decidable` (and actually from experience I would recommend instead `local attribute [instance, priority 0] classical.prop_decidable`) tags the definition with the "instance" tag, which is exactly what you need to do to make the type class inference machine notice it.

You can learn more about type class inference in [chapter 10 of Theorem Proving In Lean](https://leanprover.github.io/theorem_proving_in_lean/type_classes.html)

#### [Kevin Buzzard (Oct 14 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135786805):
But back to the original question -- I remember well wanting to know exactly the same as what you want to know now. Here are some tips. 

1) Before the statement of whatever you are working on, you can switch notation off completely, by writing `set_option pp.notation false`. Example:

```lean
set_option pp.notation false 

#check 1 ∈ (@set.univ ℕ)
-- has_mem.mem 1 set.univ : Prop
```

If you want to unfold even further, there is a command for that: the `unfold` command. 

```lean
set_option pp.notation false 

example : 1 ∈ (@set.univ ℕ) → false :=
begin
  unfold has_mem.mem,
  unfold set.mem,
  unfold set.univ,
  sorry
end
```

When I was trying to figure out what the hell was going on, I wrote a lot of code which looked like this. You can write each line after you've seen the goal at the end of the line before. The `unfolds` do not change the goal at all (I think), they just change the way it is displayed. So once you've unfolded enough to figure out what's going on you can actually just delete all the `unfolds`. Also you can write them all in one line (`unfold X Y Z ...`) (no commas).

#### [Abhimanyu Pallavi Sudhir (Oct 14 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135787136):
@**Kevin Buzzard** "The unfolds do not change the goal at all" -- the same applies to `change`, doesn't it? Except you need to actually supply what you want to change things to. I've been using that to clarify things so far. `unfold` is nice, but with `change` I can actually figure out the answer without Lean telling me.

#### [Patrick Massot (Oct 14 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135787506):
`unfold` does change the goal, there are proofs where you cannot remove an `unfold`

#### [Kevin Buzzard (Oct 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135790655):
For goals you use `show`, for hypotheses you use `change`. I have no idea why different words are used for these.

#### [Abhimanyu Pallavi Sudhir (Oct 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135790724):
Wait, what? `change` works on goals too -- just don't put an `at` clause.

#### [Patrick Massot (Oct 14 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135790769):
Yes

#### [Patrick Massot (Oct 14 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135790782):
I never understood the difference between this use of `show` and `change`. I always use `change` since it's more descriptive

#### [Kevin Buzzard (Oct 14 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135791318):
```quote
Wait, what? `change` works on goals too -- just don't put an `at` clause.
```
o_O?

#### [Mario Carneiro (Oct 14 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135791450):
`change` and `show` are almost exactly the same. One difference is that `show` will also switch to another goal if it matches what you say when the first goal doesn't

#### [Mario Carneiro (Oct 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/How to "unpack" notation?/near/135791495):
`change` also has `change with` which is like definitional `rw`

