---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66698opensetsareunionsofbasiselements.html
---

## Stream: [maths](index.html)
### Topic: [open sets are unions of basis elements](66698opensetsareunionsofbasiselements.html)

---


{% raw %}
#### [ Kevin Buzzard (May 13 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495112):
```lean
import analysis.topology.topological_space
open topological_space
universe u

lemma union_basis_elemnts_of_open {α : Type u} [topological_space α]
{B : set (set α)} (HB : is_topological_basis B) {U : set α} (HU : is_open U) :
∃ (β : Type u) (f : β → set α), U = set.Union f ∧ ∀ i : β, f i ∈ B := 
begin
  let β := {x : α // x ∈ U},
  existsi β,
  let f0 := λ i : β, (mem_basis_subset_of_mem_open HB U i.property HU),
  let f := λ i, classical.some (f0 i),
  let f1 : ∀ (i : β), ∃ (H : (f i) ∈ B), (i.val ∈ (f i) ∧ (f i) ⊆ U) := λ i, classical.some_spec (f0 i),
  let g := λ i, classical.some (f1 i),
  let g1 : ∀ (i : β), (i.val ∈ f i ∧ f i ⊆ U) := λ i, classical.some_spec (f1 i),
  existsi f,
  split,
  { rw set.subset.antisymm_iff,
    split,
    { intros y Hy,
      let i : β := ⟨y,Hy⟩,
      existsi (f ⟨y,Hy⟩),
      constructor,
        existsi i,
        refl,
      exact (g1 i).left,
    },
    { intros y Hy,
      cases Hy with V HV,cases HV with HV Hy,cases HV with i Hi,
      apply (g1 i).2,
      rwa ←Hi,
    },
  },
  { intro i,
    exact g i
  }
end
```

#### [ Kevin Buzzard (May 13 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495116):
That's the sort of proof I find very easy to write nowadays in tactic mode.

#### [ Kevin Buzzard (May 13 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495122):
At its heart though is a triviality.

#### [ Kevin Buzzard (May 13 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495124):
`mem_basis_subset_of_mem_open` says

#### [ Kenny Lau (May 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495167):
you shouldn't use `let` for propositions (`f0`, `f1`, `g1`)

#### [ Kevin Buzzard (May 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495169):
for every element `x` of an open set `U`, there's some basis element `V` with `x \in V` and `V \sub U`

#### [ Kevin Buzzard (May 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495172):
So it's one of those things which is in some sense completely trivial

#### [ Kevin Buzzard (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495177):
however because I have to use classical arguments I find writing a one-liner very hard

#### [ Kenny Lau (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495179):
also I don't think you need choice to do that, there's a trick I read somewhere

#### [ Kevin Buzzard (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495180):
So I just write it in tactic mode and I know I'll never get stuck

#### [ Kenny Lau (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495183):
instead of choosing one of them, choose all of them

#### [ Kevin Buzzard (May 13 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495184):
Kenny what I care about is whether I should be concerned that I am writing this sort of proof in 30 lines of tactic mode

#### [ Kenny Lau (May 13 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495223):
well I say that `classical.some` doesn't have a good interface

#### [ Kevin Buzzard (May 13 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495224):
and whether I should be striving to write a one-liner in term mode.

#### [ Kevin Buzzard (May 13 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495225):
Well I say that you are supposed to be sitting my exam at 10am tomorrow morning, so what are you doing chatting here? ;-)

#### [ Kenny Lau (May 13 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495227):
proving that determinant is multiplicative (not in Lean)

#### [ Kevin Buzzard (May 13 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495229):
I talked about interface to classical.some recently and Simon wrote `ccases` and Mario wrote `classical.rec_on`

#### [ Kevin Buzzard (May 13 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495269):
so there are some interfaces if you need them

#### [ Kenny Lau (May 13 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495274):
well you didn't use them

#### [ Kevin Buzzard (May 13 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495276):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/cases.20eliminating.20into.20type/near/125696468

#### [ Kevin Buzzard (May 13 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495282):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/cases.20eliminating.20into.20type/near/125695647

#### [ Kevin Buzzard (May 13 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495283):
I didn't use them because I have my own interface now -- see f,f1 and g,g1

#### [ Kevin Buzzard (May 13 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495284):
I don't really like it but it was easier to do it like that than find the thread

#### [ Kevin Buzzard (May 13 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495324):
that's not true

#### [ Kevin Buzzard (May 13 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495325):
I didn't use them because I didn't know how to use them in the middle of a function

#### [ Kevin Buzzard (May 13 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495327):
well, I didn't know how to use Simon's, and Mario's is in some sense just as complicated as what I did

#### [ Kevin Buzzard (May 13 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495334):
I was not in a situation where I had `exists x, p x` and I wanted `x` and `H : p x`

#### [ Kevin Buzzard (May 13 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495336):
I was in a situation where I wanted to construct a function

#### [ Kevin Buzzard (May 13 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495337):
so I had `forall i, exists x, p i x`

#### [ Kevin Buzzard (May 13 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495383):
and I wanted a map sending i to x

#### [ Kevin Buzzard (May 13 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495384):
hey, maybe I'm just saying that the interface for classical.some isn't great

#### [ Kevin Buzzard (May 13 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495393):
I guess I wanted a map sending i to x and a map sending i to a proof of p i x

#### [ Kevin Buzzard (May 13 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495394):
More precisely, I wanted a map `f` sending `i` to `x` and a map `f_proof` sending `i` to a proof of `p i (f i)`

#### [ Kevin Buzzard (May 13 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495433):
(rather than a proof of `p i (classical.some _)`

#### [ Kevin Buzzard (May 13 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495439):
and it still irks me a bit that I can't use a tactic which just builds these functions for me (with exactly those types, so no classical.some mentioned anywhere in the types, just in the definitions of the terms of these types)

#### [ Kevin Buzzard (May 13 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495441):
because my constructions of f f1 g and g1 involved building f, copying the type of the some_spec, editing it to replace classical.some _ with f i, then building f1, and this is a purely mechanical procedure.

#### [ Kevin Buzzard (May 13 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495489):
i.e. I started by writing

#### [ Kevin Buzzard (May 13 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495490):
```lean
  let f := λ i, classical.some (f0 i),
  let f1 := λ i, classical.some_spec (f0 i),
```

#### [ Kevin Buzzard (May 13 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495530):
and then I looked at the type of `f1` in the context, edited it to remove all trace of `classical.some` (replacing it with `f i`) and then inserted the explicit type of `f1`.

#### [ Kevin Buzzard (May 13 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495531):
It somehow all feels like both a waste of time and something which students would find confusing.

#### [ Kevin Buzzard (May 13 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126495536):
Kenny can you write a proof in term mode?

#### [ Mario Carneiro (May 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496195):
You shouldn't be using classical.some in the first place in this proof. It complicates things and there's no need. Before you start optimizing your use don't forget to see if another proof strategy works better by making canonical choices only

#### [ Kevin Buzzard (May 13 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496206):
I am a classical guy and have no feeling as to when I can get away with constructive maths

#### [ Kevin Buzzard (May 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496259):
I just wrote the first proof I thought of

#### [ Kevin Buzzard (May 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496298):
and I still find this sort of proof a joy to write

#### [ Mario Carneiro (May 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496746):
I would go for the version with a set first:
```
lemma sUnion_basis_elemnts_of_open {α : Type u} [topological_space α]
{B : set (set α)} (HB : is_topological_basis B) {U : set α} (HU : is_open U) :
∃ (S : set (set α)), U = ⋃₀ S ∧ S ⊆ B :=
⟨{b ∈ B | b ⊆ U}, set.ext (λ a,
   ⟨λ ha, let ⟨b, hb, ab, bu⟩ := mem_basis_subset_of_mem_open HB _ ha HU in
              ⟨b, ⟨hb, bu⟩, ab⟩,
    λ ⟨b, ⟨hb, bu⟩, ab⟩, bu ab⟩),
 λ b h, h.1⟩

lemma Union_basis_elemnts_of_open {α : Type u} [topological_space α]
{B : set (set α)} (HB : is_topological_basis B) {U : set α} (HU : is_open U) :
∃ (β : Type u) (f : β → set α), U = (⋃ i, f i) ∧ ∀ i : β, f i ∈ B :=
let ⟨S, su, sb⟩ := sUnion_basis_elemnts_of_open HB HU in
⟨S, subtype.val, su.trans set.sUnion_eq_Union', λ ⟨b, h⟩, sb h⟩
```
(I didn't start out planning to write a term proof, but there never really came a point where I needed a tactic)

#### [ Kevin Buzzard (May 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496845):
Right -- I generally switch to tactic mode when I want to do something like a rw which I'm too lazy to figure out with the funny triangle thing. But here I switched because it just felt easier with the classical.stuff and I felt I'd been beaten too early, that was the reason I asked.

#### [ Kevin Buzzard (May 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496886):
I see the constructivist's trick now -- thanks.

#### [ Kevin Buzzard (May 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496892):
That was the idea I was missing -- I feel confident that I could have generated a term proof now.

#### [ Kevin Buzzard (May 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496936):
PS the mis-spelling of `elements` in the name was not intentional :-)

#### [ Kevin Buzzard (May 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496941):
I wanted to write "Union_of_basis_elements_of_open" but then I had two different ofs with two different meanings

#### [ Kevin Buzzard (May 13 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126496982):
PS1 is this already in mathlib? I couldn't find it. It is the canonical thing you do with a basis!

#### [ Reid Barton (May 13 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126501829):
> I was in a situation where I wanted to construct a function
> so I had forall i, exists x, p i x
> and I wanted a map sending i to x

Use `classical.axiom_of_choice`

#### [ Reid Barton (May 13 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126501880):
```udiff
@@ -11,6 +11,3 @@
   let f0 := λ i : β, (mem_basis_subset_of_mem_open HB U i.property HU),
-  let f := λ i, classical.some (f0 i),
-  let f1 : ∀ (i : β), ∃ (H : (f i) ∈ B), (i.val ∈ (f i) ∧ (f i) ⊆ U) := λ i, classical.some_spec (f0 i),
-  let g := λ i, classical.some (f1 i),
-  let g1 : ∀ (i : β), (i.val ∈ f i ∧ f i ⊆ U) := λ i, classical.some_spec (f1 i),
+  cases classical.axiom_of_choice f0 with f hf,
   existsi f,
@@ -25,3 +22,3 @@
         refl,
-      exact (g1 i).left,
+      exact (hf i).snd.1
     },
@@ -29,3 +26,3 @@
       cases Hy with V HV,cases HV with HV Hy,cases HV with i Hi,
-      apply (g1 i).2,
+      apply (hf i).snd.2,
       rwa ←Hi,
@@ -34,3 +31,3 @@
   { intro i,
-    exact g i
+    exact (hf i).fst
   }
```

#### [ Mario Carneiro (May 13 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open%20sets%20are%20unions%20of%20basis%20elements/near/126501890):
Oh yes, sorry for not engaging with the original question, Reid is right that you should use `axiom_of_choice` here


{% endraw %}
