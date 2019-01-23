---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63417ccissopowerful.html
---

## Stream: [general](index.html)
### Topic: [cc is so powerful](63417ccissopowerful.html)

---


{% raw %}
#### [ Kenny Lau (Apr 21 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125493933):
`cc` resolved the following:
```lean
x1 : α,
b1 : bool,
x2 : α,
b2 : bool,
H2 : (x1, b1) ≠ (x2, b2),
L : list (α × bool),
H3 : L = (x1, b1) :: L₃,
H4 : L = (x2, b2) :: L₄
⊢ red L₃ ((x1, bnot b1) :: L)
```
which makes me wonder how `cc` works

#### [ Kenny Lau (Apr 21 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125493934):
The docs say that it attempts to synthesize an empty inductive type

#### [ Kenny Lau (Apr 21 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125493939):
but it doesn't say how it achieves it

#### [ Kenny Lau (Apr 21 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125493940):
the printed theorem says:
```lean
false.elim
         (false_of_true_eq_false
            (eq.trans
               (eq.symm
                  (eq_true_intro
                     (and.elim_left
                        (list.no_confusion (eq.trans (eq.symm H3) H4)
                           (λ (hd_eq : (x1, b1) = (x2, b2)) (tl_eq : L₃ = L₄), ⟨hd_eq, tl_eq⟩)))))
               (eq_false_intro H2))))
```

#### [ Simon Hudon (Apr 21 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494189):
I think it does so by building an equality matching graph. It's a graph where the vertices are terms and they are linked by edges if they  are known to be equal. Once you've added all the equalities in your context, you take the transitive closure of the graph and, for each connected component (i.e. equivalence class) you can elect a term that will represent the whole class and replace every occurrence of every member of that class by that one representative.

#### [ Simon Hudon (Apr 21 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494190):
It's a very algorithmic proof technique

#### [ Kenny Lau (Apr 21 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494191):
very interesting

#### [ Kenny Lau (Apr 21 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494193):
but the transitive closure isn't necessarily decidable?

#### [ Simon Hudon (Apr 21 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494235):
It is because you're only considering the finite set of terms that are visible in your context (and some variation on each)

#### [ Kenny Lau (Apr 21 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494236):
hmm

#### [ Gabriel Ebner (Apr 21 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494530):
@**Simon Hudon** Congruence closure does one more thing: it closes these equivalences under congruence.  For example if you know `a=b` and have two subterms `f a` and `f b`, then it will deduce `f a = f b`.

#### [ Kenny Lau (Apr 21 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494532):
is there any paper regarding this?

#### [ Simon Hudon (Apr 21 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494580):
Thanks for adding this detail! I could only think of it in algorithmic terms and that didn't seem enlightening. But your explanation is nice

#### [ Gabriel Ebner (Apr 21 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494581):
I don't know a canonical citation off the top of my head, it's pretty standard stuff.  Give me a sec.

#### [ Kenny Lau (Apr 21 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494590):
thanks

#### [ Gabriel Ebner (Apr 21 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494591):
Nelson, Oppen, Fast decision procedures based on congruence closure, Journal of the ACM (1980) http://www.cs.colorado.edu/~bec/courses/csci5535-s09/reading/nelson-oppen-congruence.pdf

#### [ Gabriel Ebner (Apr 21 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494634):
The congruence lemmas for dependent type theory as used in Lean are described in this paper (de Moura, Selsam IJCAR 2016): https://leanprover.github.io/papers/congr.pdf

#### [ Patrick Massot (Apr 21 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494642):
I'm always hesitant to try to read Lean papers because I always fear they will be outdated (say Lean 2 era or worse) and only confuse me

#### [ Gabriel Ebner (Apr 21 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494643):
The `cc` implementation in Lean does a few more tricks: for example it derives `a=b` from `nat.succ a = nat.succ b`, and `nat.succ a != nat.zero` for any `a`.

#### [ Patrick Massot (Apr 21 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494644):
Do you have something like a list of still relevant Lean papers?

#### [ Kenny Lau (Apr 21 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494684):
```lean
theorem test (α : Type*) (f : α → α) (x : α)
  (H1 : f (f (f x)) = x) (H2 : f (f (f (f (f x)))) = x) :
  f x = x :=
by cc

#print test
/-of_eq_true
    (eq_true_intro
       (eq.trans
          (eq_of_heq
             ((λ (a a' : α) (e_0 : a = a'), eq.rec (heq.refl (f a)) e_0) x (f (f x))
                (eq.trans (eq.symm H2)
                   (eq_of_heq
                      ((λ (a a' : α) (e_0 : a = a'), eq.rec (heq.refl (f a)) e_0) (f (f (f (f x)))) (f x)
                         (eq_of_heq
                            ((λ (a a' : α) (e_0 : a = a'), eq.rec (heq.refl (f a)) e_0) (f (f (f x))) x H1)))))))
          H1))-/
```

#### [ Patrick Massot (Apr 21 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494713):
Wow

#### [ Kenny Lau (Apr 21 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494739):
(taken from P.1 of the first linked paper)

#### [ Gabriel Ebner (Apr 21 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494856):
@**Patrick Massot**   Let me look through the publication list at https://leanprover.github.io/publications/.  The system description is pretty high-level and only obsolete in details.  The metaprogramming paper is new and describes Lean 3.2.  The machine learning paper doesn't seem to talk much about Lean. The congruence closure paper seems to be still relevant.  The elaboration paper is completely obsolete as it describes Lean 2.

#### [ Kenny Lau (Apr 21 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494858):
```quote
The congruence lemmas for dependent type theory as used in Lean are described in this paper (de Moura, Selsam IJCAR 2016): https://leanprover.github.io/papers/congr.pdf
```
of *course* it is de moura :P

#### [ Patrick Massot (Apr 21 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125494992):
Thanks

#### [ Patrick Massot (Apr 21 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495002):
So actually the obsolete one is clearly flagged Lean 2 on  https://leanprover.github.io/publications/

#### [ Patrick Massot (Apr 21 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495043):
It reminds me a question: what is the status of `super` today?

#### [ Patrick Massot (Apr 21 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495101):
And these `crush` things mentioned in the metaprogramming paper and some slides?

#### [ Gabriel Ebner (Apr 21 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495203):
`super` never progressed beyond a proof of concept.  From my point of view, the main thing holding it back is performance.  Some APIs that would be very nice to do e.g. resolution with unification (such as temporary metavariables) are simply not available from the metaprogramming side.  And I have enough other things to do.  Maybe I will revisit `super` when Lean 4 arrives.

#### [ Gabriel Ebner (Apr 21 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495211):
`crush` is available as a package: https://github.com/leanprover/mini_crush

#### [ Gabriel Ebner (Apr 21 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495213):
`rsimp` is in the core library

#### [ Simon Hudon (Apr 21 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495253):
What does `rsimp` do?

#### [ Gabriel Ebner (Apr 21 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495262):
Re: `super`.  This was the first thing I did with Lean, and at the time I did not know about typeclasses, simp lemmas, the equation compiler, etc.  It did not help that the Lean 3 library at the time did not even have more than a few theorems about natural numbers.

#### [ Gabriel Ebner (Apr 21 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495316):
@**Simon Hudon**: `rsimp` is Leo's idea on how to do simplification with congruence closure.  As you've observed, `cc` stores the equivalence classes of subterms.  Roughly, `rsimp` then applies simp lemmas on the subterms, and traverses the equivalence classes to pick the smallest subterm as a result.

#### [ Gabriel Ebner (Apr 21 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495366):
The main advantage compared to `simp` is that it doesn't loop (so easily).  For example, `simp*` would loop on `a=b, b=a :- f a = f b` but `rsimp` would not.

#### [ Kenny Lau (Apr 21 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495368):
why would it not loop on a=b b=a?

#### [ Simon Hudon (Apr 21 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495371):
That is so cool :) Is there a downside to using `rsimp` instead of `simp`?

#### [ Gabriel Ebner (Apr 21 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495461):
Just looked back at the paper and apparently I remembered it incorrectly, `rsimp` uses E-matching to instantiate lemmas instead of `simp`.  So in the example above, `rsimp` is essentially `cc`.

#### [ Patrick Massot (Apr 21 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495466):
Thanks. Indeed it sounds like `super` needs to wait for Lean 4.

#### [ Gabriel Ebner (Apr 21 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495501):
Maybe more interestingly: if you call rsimp on `a=b, a=f a :- p (f (f a))` then rsimp would simplify the goal to `p a` (or `p b`, randomly).

#### [ Kenny Lau (Apr 21 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495512):
I found that `cc` automatically does `intros`

#### [ Kenny Lau (Apr 21 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495513):
I was wondering if it rewrote the conditions like `simp` does

#### [ Kenny Lau (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495514):
I think that's less efficient so I don't prefer it rewriting the conditions

#### [ Kenny Lau (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495553):
so I like `cc` more :P

#### [ Gabriel Ebner (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495554):
```quote
I was wondering if it rewrote the conditions like `simp` does
```
What do mean by "rewriting conditions"?

#### [ Kenny Lau (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495555):
so the goal is `A -> B`

#### [ Kenny Lau (Apr 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495557):
simp would rewrite `A` to `C` without intro right

#### [ Gabriel Ebner (Apr 21 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495661):
I'm not sure if there is a meaningful difference in efficiency here.  The reason why `simp` does not do `intros` is because `simp` may not close the goal and you don't want `simp` to intro stuff randomly.  On the other hand, `cc` is an end-game tactic and can do whatever it wants.

#### [ Kenny Lau (Apr 21 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20so%20powerful/near/125495707):
I see


{% endraw %}
