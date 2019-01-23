---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00248multiset.html
---

## Stream: [general](index.html)
### Topic: [multiset](00248multiset.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129522842):
@**Ellen Arlt** and I are putting `multiset.lean` through its paces.

Q1) This is perhaps a question about general lean/mathlib conventions disguised as a question about multisets. We have been working with multisets of size 0 and 1 and proving basic API lemmas. Initially I was using `∅` to denote the empty multiset (this is defined in mathlib, it's not my definition). I was surprised to find that `multiset.card (∅ : multiset α) = 0` was not a simp lemma (its proof is `rfl` but it can still be a simp lemma, right?) so I went to data.multiset to decide where to add it. And there I found that `multiset.card (0  : multiset α) = 0` *was* a simp lemma:

```lean
import data.multiset

variable {α : Type}

example  : (0 : multiset α) = (∅ : multiset α) := rfl 

example : multiset.card (0 : multiset α) = 0 := by simp 

example : multiset.card (∅ : multiset α) = 0 := by simp -- fails 
```

Is this an example of the "pecking order" CS thing? Does it say "yes, `∅` and `0` are the same multiset, but if you need to refer to this multiset then mathlib asks that you use `0`"? If I'm right, how is one supposed to figure this sort of thing out? The hard way, like I did?

Q2) `multiset.strong_induction_on` gives me a way of defining functions on multisets. But I am having trouble proving anything at all about such functions. I think I need some sensible eliminators for `multiset.strong_induction_on`, ideally the one that says that the function defined by `multiset.strong_induction_on` can be computed on a multiset if I can tell you its values on all proper subsets of the multiset. No doubt this eliminator is "there already" in some form -- but I don't know how to get to it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129522923):
This is a "pecking order" thing. I was remiss in not including a simp lemma `(∅ : multiset α) = 0` but it would have conveyed this intent well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129522982):
Alternatively, in hindsight perhaps it would have been better to make `∅` the primary one, since multisets have "set" in the name (as opposed to calling them `free_abelian_group` where `0` would be more natural)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 12 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523047):
Just idle speculation, I suppose in a future unbundled class hierarchy we would rather have an instance `is_zero ∅ (multiset a)` instead of `has_zero (multiset a)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 12 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523056):
So that there is no `(0  : multiset α)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523067):
I suppose that depends on whether we want to use `0` as notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523070):
like I said, it makes sense if you want to use `multiset` as a free group generator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523118):
A related question is what I should be using for `{c}` = `c :: 0` = `c :: ∅`. Who is top of the tree here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523122):
`c::0` is used exclusively for singleton on `multiset`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523196):
For Q2, you can use this theorem:
```
theorem strong_induction_eq {p : multiset α → Sort*}
  (s : multiset α) (H) : @strong_induction_on _ p s H =
    H s (λ t h, @strong_induction_on _ p t H) :=
by rw [strong_induction_on]
```
but the built in equation is also usable, as I did in the proof here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523214):
`c :: 0` -- Yes, I had spotted this. So I should always use this notation? I noticed in practice that if one sticks to the notation which is top of the tree, then random stuff just "worked better", e.g. I had a `split_ifs` nightmare scenario when all of a sudden I had four goals; I traced this back to "sometimes using 0 and sometimes emptyset" and when I started being consistent (initially with the wrong choice!) things got better.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523222):
yes, that's the name of the game

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523226):
These conventions are debatable, but the most important thing is to be consistent about them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523266):
As for built in equations for arbitrary definitions, I only noticed that they existed about 20 minutes ago ;-) Thanks @**Simon Hudon** !

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523271):
the built in equations are much more important for wf definitions, since they are often not by `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523288):
(they are by rfl in theory, but this is where lean breaks from the theory so it proves them automatically instead)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523333):
Conventions: I guess the second most important thing is to convey the conventions to your users. I am beginning to realise that these subtleties can actually be read off relatively easily by just reading the source. Presumably sometimes there is a genuine CS reason for choosing one over the other and sometimes it's just a fairly arbitrary choice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523337):
I currently spend three days a week surrounded by about 10 students most of whom know no Lean at all, and I am still amazed by how much their completely basic questions can teach me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 12 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129524684):
Does it give more momentum to your book writing effort?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129524832):
```lean
lemma v_empty : value_aux 0 0 = 0 :=
begin
  unfold value_aux, -- strong_induction hell
  rw strong_induction_eq, -- goal now one page long
  rw strong_induction_eq, -- goal now two pages long
  dsimp, -- goal now one line long and doesn't mention induction
  ...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129524833):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525185):
No -- in fact I spend all my time trying to answer their questions :-) What gives me momentum is that I give one Lean talk per week, and figuring out what to talk about seems to be the same as figuring out what I need to write about next. I am a terrible writer :-/ I am far too verbose. I need a good editor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525186):
The main function (`value_aux`) that I'm dealing with here is defined using two applications of `multiset.strong_induction_on`. The above lemma evaluates it on the empty set. To evaluate it on a singleton my code looks like
```lean
lemma v_one_chain (c : ℕ) : value_aux (c :: 0) 0 = c :=
begin
  unfold value_aux,
  rw strong_induction_eq,
  rw strong_induction_eq,
  simp,
  rw strong_induction_eq,
  simp,
  rw strong_induction_eq,
  simp,
  -- sanity prevails
```

I am just over the moon that I can actually do things now, although I'm not entirely sure I like my `simp` style and the intermediate goals are huge.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 12 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525210):
Do you know if `simp` always does the same thing here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525257):
`set_option trace.simplify.rewrite true` is your friend.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525281):
If it happens to do always the same thing you can either write a new lemma or a specialized tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525381):
I love the way that at 9:02am (UK time) I was *completely stuck* and now at 10:06am I have made huge progress in both my understanding of Lean and of the dots and boxes API. @**Sean Leather** and @**Patrick Massot** I'm sure you're right -- I should figure out exactly what `simp` is doing. But I am now too busy excitedly proving all the trivial lemmas that Ellen wanted :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525383):
You want to write an equation lemma for `value_aux`, similar to `strong_induction_eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525411):
How do I write an equation lemma? Is that just a useful lemma, possibly tagged simp, and called something like `value_aux.equation_37`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525459):
Nothing special, you don't get to write equation lemmas like lean does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525460):
you just give it a regular name and refer to it directly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525466):
I would probably call it `value_aux_eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 12 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525525):
As I understand it, an equation lemma would be what you get (or want) naturally for each constructor of an inductive data type. The equation lemma spells out the equation to reduce/simplify the constructor application. Of course, your type doesn't have to be inductive, nor does it need to have more than one constructor, for you to have an equation lemma. It's really just a name for a particular kind of equality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 12 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525911):
Well, more precisely, you get an equation lemma for each branch of a definition. If it's a straight definition X = Y then you get just one equation, but if it is defined by cases or induction on an inductive type then you get an equation for each constructor, as you say

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 12 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525924):
Right, forgot about about that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129566679):
So I had real trouble emulating `simp` and removing it from the middle of my proofs -- I think it was even rewriting things like `lam (h : a \in c :: 0)` to `lam (h : a = c)` and my conv-fu wasn't strong enough. Chris convinced me to try rolling my own inductive definition -- he said it was so that my equation lemmas would be nicer, but I was motivated because I'd never done this sort of thing before. But I'm using induction twice: I am defining a function `value : multiset nat -> multiset nat -> nat` with the idea being that if I input `C` and `L` then I should be able to assume I can evaluate `value` at `C.erase c L` and `C L.erase l` with c in C and l in L. I should say that Chris' docs in the mathlib docs dir were invaluable.

So I got it working, but here's the epilogue: I think the equation compiler might be performing a dangerous simp which I have no way of stopping. @**Mario Carneiro** am I right? (this was the theory Chris and I came up with). Here's something which doesn't work:

```lean
import data.multiset 

definition multiset.N_min : multiset ℕ → ℕ := sorry 

def value_aux' : multiset ℕ → multiset ℕ → ℕ
| C L := multiset.N_min (multiset.pmap 
      (λ a (h : a ∈ C), 
--        have multiset.card (C.erase a) < multiset.card C,
--          from multiset.card_lt_of_lt (multiset.erase_lt.2 h),
        have multiset.card (C.erase a) + multiset.card L < multiset.card C + multiset.card L, 
          from add_lt_add_right (multiset.card_lt_of_lt (multiset.erase_lt.2 h)) _,
        a - 2 + int.nat_abs (2 - value_aux' (C.erase a) L))
        C (λ _,id) + multiset.pmap 
      (λ a (h : a ∈ L), 
--        have multiset.card (L.erase a) < multiset.card L,
--          from multiset.card_lt_of_lt (multiset.erase_lt.2 h),
        have multiset.card C + multiset.card (multiset.erase L a) < multiset.card C + multiset.card L, 
          from add_lt_add_left (multiset.card_lt_of_lt (multiset.erase_lt.2 h)) _,
        a - 4 +int.nat_abs (4 - value_aux' C (L.erase a)))
        L (λ _,id))
using_well_founded {rel_tac := λ _ _, `[exact ⟨_, measure_wf 
  (λ CL, multiset.card CL.fst + multiset.card CL.snd)⟩]}
```

This is mostly noise -- the key thing to see is that I am taking as input two multisets, I am defining `value_aux` on the pair `C L` by a function which involves evaluating it on pairs `C' L` and `C L'` with `C'<C` and `L'<L` resp. The tactic I tell Lean to use to prove well-foundedness is, I think, the function sending `C L` to `card C + card L` (there's a `psigma` type involved, hopefully I got it right). The not-commented-out `have`s insert precisely what Lean needs to see a proof of, if I've understood things correctly. However the code above does not compile -- the equation compiler complains:

```
The nested exception contains the failure state for the decreasing tactic.
nested exception message:
failed
state:
value_aux' : (Σ' (a : multiset ℕ), multiset ℕ) → ℕ,
C L : multiset ℕ,
a : ℕ,
h : a ∈ C,
this : multiset.card (multiset.erase C a) + multiset.card L < multiset.card C + multiset.card L
⊢ multiset.card (multiset.erase C a) < multiset.card C
```

Now that looks strange to me, because if I've understood correctly, `this` is *precisely* what the equation compiler wanted to see a proof of. Chris conjectures that `simp` got applied before `assumption`.  If I comment out the `have/from` pairs and replace with the commented-out ones, the code compiles fine (and my equation lemmas don't mention `multiset.rec` :-) ). Chris points out that if the behaviour of `simp` changes in the future, then my code breaks in a really obscure way and there's little I can do about it. Have we understood what's going on correctly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129568895):
Here's a method that avoids the simplifier
```lean
def value_aux' (N_min : multiset ℕ → ℕ) : multiset ℕ → multiset ℕ → ℕ
| C L := N_min (multiset.pmap
      (λ a (h : a ∈ C),
--        have multiset.card (C.erase a) < multiset.card C,
--          from multiset.card_lt_of_lt (multiset.erase_lt.2 h),
        have multiset.card (C.erase a) + multiset.card L < multiset.card C + multiset.card L,
          from add_lt_add_right (multiset.card_lt_of_lt (multiset.erase_lt.2 h)) _,
        a - 2 + int.nat_abs (2 - value_aux' (C.erase a) L))
        C (λ _,id) + multiset.pmap
      (λ a (h : a ∈ L),
--        have multiset.card (L.erase a) < multiset.card L,
--          from multiset.card_lt_of_lt (multiset.erase_lt.2 h),
        have multiset.card C + multiset.card (multiset.erase L a) < multiset.card C + multiset.card L,
          from add_lt_add_left (multiset.card_lt_of_lt (multiset.erase_lt.2 h)) _,
        a - 4 +int.nat_abs (4 - value_aux' C (L.erase a)))
        L (λ _,id))
using_well_founded {dec_tac := tactic.assumption, rel_tac := λ _ _, `[exact ⟨_, measure_wf
  (λ CL, multiset.card CL.fst + multiset.card CL.snd)⟩]}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 13 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129568913):
I changed the `dec_tac` at the bottom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129575356):
Yes, the standard fix when the default dec_tac is being stupid is to replace it with `tactic.assumption` like chris did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129575360):
Actually the default dec_tac doesn't use simp, it is a custom tactic that does a few heuristic rules to do with nat.lt

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129575413):
it is `default_dec_tac` in `well_founded_tactics.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129575582):
But I'm confused what the issue was that caused you to move away from the original version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129585358):
Short answer: I wanted to get rid of the dangerous simps and this approach ("start again") would have the advantage that it (a) might solve this and (b) would also teach me something (slightly complicated use of equation compiler). 

Long technical answer: Your original fix was fine modulo these dangerous simps. I was just talking to Chris about it and he said "why did you even use `multiset.strong_induction_on` when you could use the equation compiler?" and because I couldn't get rid of my dangerous `simp` and because I'd never used `using_well_founded` before I thought I'd give it a go to teach myself something (which turns out to be pretty easy to understand modulo the `lam _ _, `[exact` bit, which I'm leaving as a black box). Chris pointed out that one only had to use the equation compiler once, whereas I was using strong induction twice, so I felt that rewriting this was somehow going in the right direction.

An example (two examples) of the dangerous simp in my original code looks like this: note that this is with `value_aux`, the version of my function which uses strong induction twice per application (as opposed to `value_aux'` above). 

```lean
lemma v_one_chain (c : ℕ) (h : c ≥ 3) : value_aux (c :: 0) 0 = c :=
begin
  unfold value_aux,
  rw strong_induction_eq,
  rw strong_induction_eq,
  simp,
  rw strong_induction_eq,
  rw strong_induction_eq,
  simp,
  show 2 + (c - 2) = c, -- irritating-to-Patrick goal (c is a nat)
  rw add_comm,refine nat.sub_add_cancel _,
  exact le_trans (show 2 ≤ 3, by exact dec_trivial) h,
end
```
This uses Mario's eliminator for `strong_induction_on` and compiles fine. The issue of course is with the simps in the middle. Replacing the first `simp` with `dsimp` breaks the code. Before the first simp is applied, the goal is https://gist.github.com/kbuzzard/d9f70ae02b5861bbce0f8d958e16619a and after it's applied, the goal becomes (the still quite long) https://gist.github.com/kbuzzard/07495e93ed94b3d4e5bfd4015a52914f . These goals are too big for my liking and the direct approach seemed like it would be likely to make them smaller. There are `strong_induction_on`s around in these goals but the rewrites won't work without the first `simp`. Sean suggested `set_option trace.simplify.rewrite true` and the output of that on the first dangerous `simp` is https://gist.github.com/kbuzzard/1a01ad2bc29aad1c257452c4d2d894d5 . I am certainly not a world expert in trace outputs, but I was interpreting the first line `0. [simplify.rewrite] [multiset.mem_singleton]: a ∈ c :: 0 ==> a = c` of that trace output as meaning "first we replace that `mem` term with an `eq` term" but as far as I could see the only occurrences of `a ∈ c :: 0` were in terms like `(λ (a : ℕ) (h : a ∈ c :: 0), ...` and I could not do that rewrite with my bare hands (maybe I am just lame at `conv` but OTOH rewriting the type of a term is probably a dangerous business). In short, I couldn't remove the dangerous simp so I thought I'd try another approach.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129585364):
```quote
Actually the default dec_tac doesn't use simp, it is a custom tactic that does a few heuristic rules to do with nat.lt
```
PS that's good to know. Thanks. @**Chris Hughes** it wasn't using `simp` after all. PPS I think https://nat.lt is in Lithuanian.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129586991):
I think you may not have understood my suggestion to write an equation lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587226):
Here is a version of `value_aux'` that uses `strong_induction_on` for its definition (presumably this looks like your original definition, although you didn't show it here):
```

def value_aux (N_min : multiset ℕ → ℕ) (C : multiset ℕ) : multiset ℕ → ℕ :=
multiset.strong_induction_on C $ λ C IH₁ L,
multiset.strong_induction_on L $ λ L IH₂,
N_min (
  multiset.pmap
    (λ a (h : a ∈ C),
      a - 2 + int.nat_abs (2 - IH₁ (C.erase a) (multiset.erase_lt.2 h) L))
    C (λ _, id) +
  multiset.pmap
    (λ a (h : a ∈ L),
      a - 4 + int.nat_abs (4 - IH₂ (L.erase a) (multiset.erase_lt.2 h)))
    L (λ _,id))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587227):
[equation lemma] For sure that is true. Probably my question immediately after your comment indicated this. Sometimes I do stuff to learn more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587233):
Yes, it looks pretty much like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587242):
except I used `C2` instead of `C` and `L2` instead of `L` because I am scared of free and bound variables having the same name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587260):
This is the equation lemma corresponding to that definition
```
theorem value_aux_eq (N_min : multiset ℕ → ℕ) (C L : multiset ℕ) :
  value_aux N_min C L = N_min (
    multiset.pmap
      (λ a (h : a ∈ C),
        a - 2 + int.nat_abs (2 - value_aux N_min (C.erase a) L))
      C (λ _, id) +
    multiset.pmap
      (λ a (h : a ∈ L),
        a - 4 + int.nat_abs (4 - value_aux N_min C (L.erase a)))
      L (λ _,id)) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587306):
I don't understand your application of the "equation lemma" function.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587310):
(Actually, you can simplify the `pmap` away the way it's been written here, since `h` is no longer used)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587311):
Is there an equation lemma corresponding to every definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587317):
What is "the equation lemma corresponding to nat"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587323):
or "the equation lemma corresponding to quotient.sound" etc etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587327):
Informally, an "equation lemma" says that a definition is what it was defined to be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587334):
`nat` and `quotient.sound` don't have equation lemmas because they are constants, not defs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587341):
`real`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587346):
`def f : nat -> nat := lam x, x + 3`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587347):
It has an equation lemma, although you would rarely use it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587388):
that definitely does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587394):
it's something like "forall x , f x = x + 3"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587398):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587400):
Maybe I don't understand the _point_ then.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587403):
Is it tagged as a simp lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587406):
Who is using these equation lemmas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587407):
sometimes it's a simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587410):
?!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587415):
Who makes the decision?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587416):
it gets used whenever you "unfold the definition"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587420):
Aah!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587425):
When I use unfold, sometimes it says that `simp` failed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587427):
some definitions are marked `@[simp]` meaning that their equation lemmas are simp lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587434):
You can tag a definition with simp? I am not sure I ever internalised that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587478):
like list.append
```
@[simp] protected def append : list α → list α → list α
| []       l := l
| (h :: s) t := h :: (append s t)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587481):
This marks this definition's two (!) equation lemmas as simp lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587493):
I can see all the equation lemmas with `#print prefix list.append` perhaps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587498):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587503):
So I must confess that I've never really understood the output of that sort of command.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587504):
We have `_main`, `_main._meta_aux` etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587506):
it's quite intimidating

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587508):
But sometimes lean doesn't generate equation lemmas the way you would like them, so you have to write your own, and that's my point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587596):
I am still missing a big issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587600):
OK so I wrote my function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587603):
and the equation lemmas are all wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587606):
so I need to write another one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587613):
For example, here's another way to write list.append
```
def list.append' {α} (l₁ l₂ : list α) : list α :=
list.rec_on l₁ l₂ (λ a l₁ IH, a :: IH)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587614):
OK so I wrote one: "`theorem X : f x = g x -- this is the equation lemma I want`"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587617):
that's a lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587618):
Is it an equation lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587620):
the equation lemmas are not what we would like
```
#print prefix list.append'
-- list.append' : Π {α : Type u_1}, list α → list α → list α
-- list.append'.equations._eqn_1 : ∀ {α : Type u_1} (l₁ l₂ : list α),
--   list.append' l₁ l₂ = list.rec_on l₁ l₂ (λ (a : α) (l₁ IH : list α), a :: IH)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587662):
why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587669):
What's wrong with them?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587672):
I don't understand several things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587680):
"equation lemmas are used in unfold"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587681):
"sometimes they're simp lemmas"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587684):
While it is true that append is equal to that rec_on mess, that's not what I want to see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587687):
"they're generated automatically"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587692):
that's about all I know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587693):
about equation lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587694):
I am missing some fundamental point about why they exist and why they're important

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587705):
"if you write a definition, Lean generates a bunch of lemmas with obscure names"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587706):
what I want to see are the things that the definition is trying to say, namely `list.append [] l = l` and `list.append (a::l) l' = a :: list.append l l'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587710):
This is really important for controlling the complexity of statements

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587714):
"if you write the definition differently, you might get different lemmas, and Mario can see that this might cause problems but Kevin still has no understanding of when equation lemmas are used so doesn't care what these auto-generated lemmas are"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587753):
if every time you used `nat.add` it unfolded to its definition it would be utterly unreadable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587756):
it can't unfold

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587760):
oh wit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587761):
oh wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587766):
is `nat.add` one of these things whose definition is not what I think it is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587771):
Is it not 0 -> x, succ y -> succ (x+y)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587783):
really making progress in this proof:
```
example (x : ℕ) : 0 + x = 0 :=
begin
  dsimp only [(+)], delta nat.add,
-- ⊢ nat.brec_on x
--       (λ (a : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a) (a_1 : ℕ),
--          (λ (a a_1 : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a_1),
--             nat.cases_on a_1 (λ (_F : nat.below (λ (a : ℕ), ℕ → ℕ) 0), id_rhs ℕ a)
--               (λ (a_1 : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) (nat.succ a_1)),
--                  id_rhs ℕ (nat.succ ((_F.fst).fst a)))
--               _F)
--            a_1
--            a
--            _F)
--       0 =
--     0
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587788):
I'm already lost, apparently it's `nat.add._main`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587790):
that does not look good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587794):
If `simp` did this Leo would be fired by now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587847):
The problem has occurred because `nat.add` is for some reason defined in a stupid way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587858):
I fixed this up in my blog IIRC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587861):
no, the problem has occurred because I unfolded the definition without folding it back up again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587877):
Does the equation compiler create that monstrosity?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587879):
Even if I defined `nat.add` the simple way, it would still not be pretty to look at

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587885):
oh holy moley

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587887):
I want to see `0 + x` not `nat.rec bla bla`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587893):
`nat.add` is defined sensibly in `core.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587913):
what has the equation compiler done??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587936):
The equation lemmas say things like `x + succ y = succ (x + y)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587941):
```lean
namespace nat
  protected def add : nat → nat → nat
  | a  zero     := a
  | a  (succ b) := succ (add a b)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587945):
That got turned into the monstrosity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587949):
this is true by rfl, but the really important thing is that the RHS does not have `nat.rec` in it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587960):
or `nat.brec_on` or its cousins

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587973):
Right -- Chris was stressing the importance of getting away from `multiset.rec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587994):
which I had in my initial equation lemmas for the value function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587998):
In fact, you could say that's the main purpose of equation lemmas, to hide recursors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588018):
actually it's even worse, my equation lemmas for value have strong induction in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588062):
```
value_aux.equations._eqn_1 : ∀ (C : multiset ℕ),
  value_aux C =
    multiset.strong_induction_on C
      (λ (C2 : multiset ℕ) (HC : Π (t : multiset ℕ), t < C2 → multiset ℕ → ℕ) (L : multiset ℕ),
         multiset.strong_induction_on L
           (λ (L2 : multiset ℕ) (HL : Π (t : multiset ℕ), t < L2 → ℕ),
              multiset.N_min
                (multiset.pmap
                     (λ (a : ℕ) (h : a ∈ C2), a - 2 + int.nat_abs (2 - ↑(HC (multiset.erase C2 a) _ L2)))
                     C2
                     _ +
                   multiset.pmap
                     (λ (a : ℕ) (h : a ∈ L2), a - 4 + int.nat_abs (4 - ↑(HL (multiset.erase L2 a) _)))
                     L2
                     _)))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588080):
Can you tell me a formal definition of which parts of the output of `#print prefix value_aux` are the equation lemmas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588084):
Is it precisely those which start `value_aux.equation...`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588095):
yes, those are the automatically generated equation lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588097):
because I have other things like the stunning observation `value_aux._proof_4 : ∀ (L2 : multiset ℕ) (_x : ℕ), _x ∈ L2 → _x ∈ L2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588103):
Is that an equation lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588109):
I don't know what I'd do without that lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588114):
those are extracting proof terms inside non-proof terms for performance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588166):
but not equation lemmas.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588167):
the extraction code isn't so bright

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588176):
equation lemmas are equations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588181):
OK so when I make a new definition, Lean makes some equation lemmas, and we've seen examples where these lemmas are in some sense unusable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588183):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588189):
so now all I need to know is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588193):
(1) what is actually using them and (2) how to write better ones

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588196):
When you write a definition you should already have in mind what its equation lemmas are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588202):
In this case, you knew you wanted `value_aux` to depend on itself at other values

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588203):
If we go back to `nat.add` I can see `x + succ y = succ (x + y)` would be the sort of thing that as an end user I would simply _assume_ was true by `rfl`, given the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588249):
which is where something like this comes from
```
theorem value_aux_eq (N_min : multiset ℕ → ℕ) (C L : multiset ℕ) :
  value_aux N_min C L = N_min (
    C.map (λ a, a - 2 + int.nat_abs (2 - value_aux N_min (C.erase a) L)) +
    C.map (λ a, a - 4 + int.nat_abs (4 - value_aux N_min C (L.erase a)))) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588256):
Right -- I feel like I want that theorem to be true by `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588258):
because in my non-CS mathematical mind that is "exactly how I defined the function"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588265):
that theorem is "true by definition"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588266):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588272):
but funnily enough I don't see it in my list of equation lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588277):
Half of the work is taking your "definition" and turning it into something lean will accept, and the other half is getting back to the original thing you wanted to call the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588318):
that latter step is the equation lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588327):
I had never remotely comprehended this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588329):
I thought that "Lean did the second part automatically"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588331):
it does, for the most part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588351):
but it's not perfect, it doesn't accept every definitionesque thing mathematicians dream up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588352):
OK so let's say I can prove the lemma which I thought should be `rfl` but which wasn't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588361):
Is it just a case of making sure that lemma is called `value_aux.equations._eqn_2`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588373):
Unfortunately, lean doesn't let you install your own equation lemmas like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588414):
OK so we're back to (1) I don't know how to make a lemma into an equation lemma and (2) I don't know exactly what is using the equation lemmas and when

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588416):
when you right your own equation lemma, it's just a theorem, an equality you can use in rewrite and simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588417):
and rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588420):
because equation lemmas are true by definition, right? :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588421):
If you prove it by `rfl` you can also use it in `dsimp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588424):
Sometimes it's `rfl` sometimes not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588425):
If it's not `rfl` then Lean made a mistake

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588430):
because the equation lemmas are the things which are true by definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588433):
for more elaborate definitional mechanisms, DTT doesn't recognize it as definitional but you can still prove it with some work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588436):
OK

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588478):
so now I proved a lemma, the proof unfortunately wasn't `rfl`, I want to use it everywhere because in my brain the lemma is "true by definition of the object".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588480):
Now what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588483):
In particular, I doubt `value_aux_eq` is true by `rfl`, particularly when I changed the `pmap` to `map`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588488):
Yes i can quite believe it's not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588493):
not least because `value_aux` uses `multiset.strong_induction_on` *twice*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588497):
but it is nevertheless "the way we want it to unfold" so we treat it as the equation lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588499):
"so we treat it as the equation lemma" is the bit I don't get

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588508):
Are you just saying "prove a lemma and then occasionally `rw` with it"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588512):
It just means we use that theorem when we would otherwise "unfold `value_aux`"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588521):
So 

```lean
lemma v_one_chain (c : ℕ) (h : c ≥ 3) : value_aux (c :: 0) 0 = c :=
begin
  unfold value_aux,
  rw strong_induction_eq,
  rw strong_induction_eq,
  simp,
  rw strong_induction_eq,
  rw strong_induction_eq,
  simp,
...
``` 

is not the right approach?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588566):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588568):
even though I have the right equation lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588570):
(I assume I do, I think you wrote it)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588588):
you want to use the equation lemma for `value_aux`, not the equation lemma for `strong_induction_on`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588593):
you will use the latter to prove the former

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588597):
aah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588613):
aah I was thinking "Mario said to use an equation lemma, I don't know what that is, I think Mario wrote it for me, I'll just use that"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588682):
So an equation lemma is just a lemma, with no magic properties, it doesn't have to have a weird name like `foo._equation_7_main_sunfold`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588688):
no, that's just the usual name for lean's autogenerated equation lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588691):
what makes it an equation lemma is that it represents a fact which the end user would like to think was "true by definition"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588696):
if they were a wooly thinker, like e.g. a pure mathematician

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588701):
those get some special magic, like being able to write `simp [f]` instead of `simp [f.equations_1]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588706):
Yes, I learnt that yesterday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588752):
OK so let me step back and try to wrap up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588761):
When I write a definition, I might want to consider what the fundamental properties of that definition are -- the things which *should* be "true by definition"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588768):
or "true because it's completely obvious"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588781):
and then I might want to look at the subset of the output of `#print prefix foo` consisting only of things which have the string "equation" in them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588789):
and I might want to just check that everything I want to be "true by definition" is there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588797):
The autogenerated equation lemmas are easy to predict without looking at them like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588801):
and if it's not then I might want to make a note of this, prove the remaining facts, and then spend the rest of my life rewriting with them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588845):
@**Kevin Buzzard** Perhaps “true by the definition you wished it had”? “True because it's obvious” is maybe too generous in what it allows.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588846):
```quote
The autogenerated equation lemmas are easy to predict without looking at them like that
```
says someone who has probably looked at the code which generates them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588847):
for each branch of the definition, each `:=`, you get a lemma saying your definition applied to those arguments gives the RHS

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588859):
@**Sean Leather** that's a better way of phrasing it. My definition of value by "induction on (induction on ...)" was never going to create the lemma I wanted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588880):
but on the other hand there was clearly a definition which in some sense I "wished I had written"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588887):
and that was precisely the definition I _did_ write yesterday, using the equation compiler

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588931):
So all this stinks. There are things which should be true by `rfl` but which I can't prove with `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588932):
One place where you might be surprised is in definitions with wildcards
```
def X {α} : list α → list α → list α
| [] _ := []
| _ [] := []
| x y := x
#print prefix X
-- X.equations._eqn_1 : ∀ {α : Type u_1}, X list.nil list.nil = list.nil
-- X.equations._eqn_2 : ∀ {α : Type u_1} (hd : α) (tl : list α), X list.nil (hd :: tl) = list.nil
-- X.equations._eqn_3 : ∀ {α : Type u_1} (hd : α) (tl : list α), X (hd :: tl) list.nil = list.nil
-- X.equations._eqn_4 : ∀ {α : Type u_1} (hd : α) (tl : list α) (hd_1 : α) (tl_1 : list α), X (hd :: tl) (hd_1 :: tl_1) = hd :: tl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588944):
notice that `X x y = x` is not an equation lemma since it has to do some case splits first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588952):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588953):
that all makes sense to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588957):
that's a lemma, that X x y = x

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588976):
actually it's perhaps not even true but I see your point whether or not this example is exactly right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589020):
So I prove this lemma by cases on x

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589033):
and then I decree in my head that this is an equation lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589045):
Maybe a better example of an equation lemma for this one is `X [] y = []` and `X x [] = []`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589054):
Neither of these is true by rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589055):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589063):
both proof by cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589069):
These look like simp lemmas to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589076):
They are that too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589080):
So an equation lemma seems to me to have no formal definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589082):
equation lemmas are often good simp lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589123):
it's "something which the user is clearly going to need again and again"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589129):
so should probably be proved immediately after the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589134):
but sometimes they would lead to infinite unfolding, like the equation lemma for `value_aux`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589143):
I think nat is well-founded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589148):
equation lemmas for wf definitions often have that problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589161):
`gcd x y` unfolds forever when given *variable* `x` and `y`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589173):
Oh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589177):
it doesn't matter that nat is well founded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589180):
Oh you're absolutely right!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589195):
because these are open terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589197):
We're not doing case splits on constructors for multiset or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589205):
oh so that lemma is actually quite dangerous!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589246):
Shall I make it a simp lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589257):
yes, you only want to use it with `rw` or `simp {single_pass := tt}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589266):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589273):
it should definitely not be a simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589278):
right!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589302):
I gave an entire lecture on functions last Monday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589305):
I feel like I could give another one now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589309):
:)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589315):
Many thanks as ever Mario.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589518):
What's nice about zulip rather than IRL meetings is that now I understand much better I can just read through the thread again with the benefit of hindsight and try to catch extra subtleties.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129590094):
```quote
Half of the work is taking your "definition" and turning it into something lean will accept, and the other half is getting back to the original thing you wanted to call the definition
```
This is somehow the key point. I have quite a flexible way of thinking about definitions and their basic properties, I guess because mathematicians are trained like that. Some properties of a definition are so completely basic that I think I've got into the habit of simply *assuming* that they will be (a) true and (b) `rfl`. For simple functions this might well be the case. For more complex definitions which need some bending to shove into Lean, life might not be so easy. I have a definition by induction on two variables, and Mario's equation lemma is exactly how I am thinking the definition "works". I shove the definition into Lean in perhaps an inelegant way ("Mario wrote `multiset.strong_induction_on` and I can apply it twice, that'll do") and now I need to be aware of the fact that Lean's understanding of the function is now quite far from my intuitive idea of how it works, and it should now be a top priority to sort this situation out by proving the lemmas which say that the definition behaves the way I expect it to. If I'm writing some API then I might want to consider proving these so-called "equation lemmas" -- this is an informal definition and it seems to mean "the lemmas which an end user might expect to be true by definition, whether or not they are true by `rfl`" -- immediately after the definition of the function. Some might already be there with exotic names with `_`s in, and the ones that are not should be written as a matter of priority or other mathematicians will not be able to use the function in the intuitive way which they would like to.

