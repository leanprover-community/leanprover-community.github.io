---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53478naturalnumberhell.html
---

## Stream: [general](index.html)
### Topic: [natural number hell](53478naturalnumberhell.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580412):
I want to use `big.map` once I have the `map`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580421):
I should push something so that you can see the context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580423):
and then the `f` will be applied to the functions P and F... then what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580473):
https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L343

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580484):
wait, so you want the function `f` to be `i |-> a+b-i`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580489):
then why are you mapping with something else in the lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580551):
The problem is `reverse_range'` is about your `range'`, with start and length, and my goal is to have the maths range', with start and end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580614):
Think of the problem in reverse. You want the theorem to say `a+b-i` at the end, so you want `f` to be `\lam i, a+b-i` when you apply `big.map`; the reverse theorem just adds a `list.reverse` on the set. So you should be proving `reverse (range' a b) = map (λ i, a+b-i) (range' a b)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580663):
that is, without any algebraic rearrangement this is exactly what you need to fill the gap in the proof. Right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580668):
Maybe I did so many detours I forgot the goal on the road

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580776):
It seems I still need `a + (b + 1 - a) - i = a + b - i` (still assuming `i ∈ range' a (b + 1 - a)`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580783):
that's easy though, it is one of the `add_sub` theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580785):
I think we already saw that one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580824):
`nat.add_sub_cancel'`, which requires `a <= b + 1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580852):
Note that your assumption is sufficient to prove this, but only in a circuitous fashion, do you have any more direct evidence that `a <= b+1`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580897):
wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580898):
wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580899):
your theorem is nonsense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580904):
your theorem is nonsense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580905):
`reverse (range' a b) = map (λ i, a+b-i) (range' a b)` is not true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580910):
I changed all statements so many times...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580927):
I'm rather confused by the dual use of `range'` btw, could you give it another name? `range''` maybe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580953):
You mean in the name of `reverse_range'`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580963):
I mean `range' a b = [a, ..., b]` vs `range' a b = [a, ..., a+b]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580968):
pretty sure both functions are being called `range'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580970):
I don't redefine range'

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580973):
What is your definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126580974):
I use your range'

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581016):
oh I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581018):
But always in `range' a (b+1-a)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581019):
In that case I need to state the theorem above with your bounds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581022):
`reverse (range' a (b+1-a)) = map (λ i, a+b-i) (range' a (b+1-a))`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581026):
yes, this is correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581030):
(not that I can prove it, but I can check it on examples)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581093):
But I wanted to deduce it from a version involving only  `range' a b` in LHS

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581097):
hence the "arithmetic" trouble

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581150):
But indeed this is the statement which makes `big.range_anti_mph` trivial to prove from the previous results

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581152):
Well, there are a lot of free endpoints in the reverse theorem, maybe you need to generalize it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581159):
what reverse theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581276):
I'm thinking:
```
reverse (range' a (n + 1)) = map (λ i, c-i) (range' b (n + 1))
```
subject to an equation relating a,b,c

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581305):
Actually I think we need another generalization of `range'` that varies the step too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581346):
that would make this easy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581425):
I need to go to my office, but the situation improved a lot: https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L335-L341 Thank you very much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126581440):
I hope I'll be able to prove that last missing lemma later if you don't have time to do it properly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126582724):
I did it properly. Here are the lemmas I added:
```

theorem map_add_range' (a) : ∀ s n : ℕ, map ((+) a) (range' s n) = range' (a + s) n
| s 0     := rfl
| s (n+1) := congr_arg (cons _) (map_add_range' (s+1) n)

theorem range_succ_eq_map (n : ℕ) : range (n + 1) = 0 :: map succ (range n) :=
by rw [range_eq_range', range_eq_range', range',
       add_comm, ← map_add_range'];
   congr; exact funext one_add

theorem reverse_range' : ∀ s n : ℕ,
  reverse (range' s n) = map (λ i, s + n - 1 - i) (range n)
| s 0     := rfl
| s (n+1) := by rw [range'_concat, reverse_append, range_succ_eq_map];
  simpa [show s + (n + 1) - 1 = s + n, from rfl, (∘),
    λ a i, show a - 1 - i = a - succ i,
    by rw [nat.sub_sub, add_comm]; refl]
  using reverse_range' s n
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126584480):
Thank you Mario! I already had the first one at https://github.com/PatrickMassot/bigop/blob/master/src/bigop.lean#L126

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126584495):
Maybe I should learn to do induction using pattern matching

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126602871):
I read too quickly, I thought you proved the lemma I needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126602882):
But your RHS doesn't even contains `range'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126602935):
Proving the lemma I stated from what you proved seems to be as much work as a direct proof, no?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126610298):
You still have some algebra before you get to the exact version you need, but you can put `reverse_range'`, `range_eq_range'`, `map_add_range'` and `map_map` together and then do some algebra

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126610881):
```
theorem range'_eq_map_range (s n : ℕ) : range' s n = map ((+) s) (range n) :=
by rw [range_eq_range', map_add_range']; refl

example (a b : ℕ) : reverse (range' a (b+1-a)) = map (λ i, a+b-i) (range' a (b+1-a)) :=
begin
  rw [reverse_range', range'_eq_map_range, map_map],
  apply map_congr, intros i H,
  simp at *,
  rw [nat.add_sub_add_left, nat.add_sub_cancel'], {refl},
  refine (le_total _ _).resolve_left (λ h, _),
  rw sub_eq_zero_of_le h at H,
  exact not_lt_zero _ H
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613014):
Thank you very much Mario! I'm still not convinced this is simpler than a direct attack on this lemma, but I very much relieved to have it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613022):
What is this `resolve_left` thing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613109):
The state at the point where you write this, `a b i : ℕ,
H : i < b + 1 - a
⊢ b + 1 ≥ a` is typically something that could have led me to harm my computer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613166):
I also note that you used `simp at *` in the middle of a proof. Isn't this frowned upon according to mathlib's docs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613168):
That's actually a really subtle thing, it wouldn't work if it was `i <= b+1-a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613248):
What do you mean it wouldn't work? The statement would still be true, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613250):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613267):
This is crazy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613279):
if i is zero then b+1 could be less than a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613341):
Did I mentioned I hate this substraction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613362):
the argument is basically that when you subtract small minus large you get 0, so since i is less than the subtraction it isn't zero so it is in the proper domain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613460):
You could also have taken a <= b+1 as an assumption to the theorem if you like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613497):
I still don't know what `resolve_left` stands for

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613508):
`or.resolve_left`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613559):
@**Patrick Massot** The type of `le_total _ _` is `or _ _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613569):
So `(le_total _ _).resolve_left` means `or.resolve_left (le_total _ _)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613577):
Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613580):
to both of you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613601):
So the strategy here is some variation on a case disjunction, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613632):
Is it possible to use `by_cases` instead? (I only try to understand, I don't really want to use `by_cases`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613653):
`by_cases` uses `p or not p` instead of any arbitrary `p or q`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613672):
It's true that `le_total` is almost but not quite like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613749):
however I don't see the difference between `or.resolve_left (le_total _ _)` and `le_of_not_le`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613805):
I still don't understand why the goal after this `refine` is `false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613808):
`refine (le_total _ _).resolve_left (λ h, _)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613820):
the expected type of `(λ h, _)` is `not (le _ _)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613832):
so `h` has type `le _ _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613837):
so `_` has type `false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613899):
Indeed the mysterious line has the same effect as `apply le_of_not_le,
  by_contradiction h,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613905):
try `refine le_of_not_le (λ h, _)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613910):
`le_of_not_le` would also have worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613915):
@**Mario Carneiro** entao eu ganho?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613925):
vc ganhou

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126613971):
:D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614006):
The proof of `le_of_not_le` is exactly this `or.resolve_left le_total`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614057):
But indeed Kenny's solution will probably be easier to remember for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614194):
So, what should we do with all those lemmas we discussed in the last few days. Do you want me to prepare a PR? Are you doing it yourself?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614274):
I've got a pot brewing, you can hold onto them locally until then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614284):
No problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614634):
I extracted everything from my bigop file. It's now all in https://github.com/PatrickMassot/bigop/blob/master/src/pending_lemmas.lean if you want to make sure you have everything that was discussed here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126614653):
It's bedtime now. Thank you very much again!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636219):
I have three substractions now :fearful: `H : N ≥ 1, hyp : 0 ≤ i ∧ i < N ⊢ N - (N - 1 - i) = i + 1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636280):
Isn't it a way to first prove that we would get the same result in Z, because each substraction comes with its relevant inequality, and then `ring`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636450):
yes, of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636462):
just use `int.cast_sub`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636524):
how does that work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636528):
that is, use `int.cast_inj` to convert the natural number equality to a Z equality, and then use `int.cast_add`, `int.cast_sub` etc lemmas to move the arrows down to the bottom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636531):
Looking at the statement is pretty puzzling

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636540):
simp will do the latter part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636541):
```lean
example {i N : ℕ} (H : N ≥ 1) (hyp : 0 ≤ i ∧ i < N) : N - (N - 1 - i) = i + 1 :=
have 1 + i ≤ N, by rw add_comm; exact hyp.2,
by rw [nat.sub_sub, nat.sub_sub_self this, add_comm]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636544):
and the winner is...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636547):
^ or just prove it directly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636600):
Thanks Chris, but I'm really tired of those direct proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636603):
I want a systematic method

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636607):
```
example {i N : ℕ} (H : N ≥ 1) (hyp : 0 ≤ i ∧ i < N) : N - (N - 1 - i) = i + 1 :=
by rw [nat.sub_sub, add_comm, nat.sub_sub_self hyp.2]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636616):
and the winner is...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636619):
Is it poor form to use `exact hyp.2` instead of `exact nat.succ_le_of_lt hyp.2`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636625):
meh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636629):
maybe you should replace `exact hyp.2` with `cc`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 16 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636671):
I mean, it isn't like you can't prove `H` from `hyp`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636673):
in general you should minimize your implicit definitional unfolding, but some things are too foundational to change at this point and I assume it will stay that way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636676):
I don't know how to use `int.cast_inj`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636746):
oops, I mean `int.coe_nat_inj'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636832):
```
example {i N : ℕ} (H : N ≥ 1) (hyp : 0 ≤ i ∧ i < N) : N - (N - 1 - i) = i + 1 :=
by rw [← int.coe_nat_inj', int.coe_nat_sub, int.coe_nat_sub, int.coe_nat_sub]
```
produces a bunch of side conditions about less equal stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636880):
actually it's a bit messy since the side conditions themselves involve natural number subtraction, so you need to rewrite them too or else prove them directly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636937):
If you want to take this route I would suggest not writing natural number subtraction at all when you can help it, so that you don't need to deal with nested subtractions and the like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126636946):
that is, just use integer subtraction and convert back to natural numbers at the end with `int.to_nat` if necessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126637007):
"not writing natural number subtraction at all" is my greatest Lean dream

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126637069):
A simple way to actually do that is to replace `m - n` everywhere with `int.to_nat (m - n)` (where the subtraction there is actually integer subtraction now)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 16 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126637078):
I need to go, I'll try tonight. Thanks you!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 16 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126637080):
That way the funky zero saturation operator is explicit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643379):
```quote
I want a systematic method
```
How about this: replace every occurrence of `X <= Y` with `Y = X + c` and replace every occurrence of `X < Y ` with `Y = X + c + 1`, and then just use `add_sub_cancel` or whatever it's called -- `a + b - b = a`. It would not surprise me if this algorithm worked every time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643448):
Example: you know `i < N` and you want to prove `N - (N - 1 - i) = i + 1`, well, write `N = i + 1 + j` and -- oh -- you also need `X - (Y + Z) = X- Y - Z` -- you get `N - (j + 1 + i - (1 + i))` which is `N - j` which is `i + 1 + j - j` which is `i + 1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643465):
I am assuming that your mathematician's goals never actually rely on the fact that a - b = 0 if b>a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643674):
This should reduce everything to `nat.sub_sub` (if memory serves -- is it called that?) and `add_sub_cancel` or whatever it's called (not in front of Lean right now).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643689):
oh and associativity and commutativity of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643699):
Make them simp lemmas and see if simp can do it after you make the substitutions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643713):
(if they're not simp lemmas already)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643719):
Might not be the optimal approach but it looks pretty systematic to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643809):
```quote
replace every occurrence of `X <= Y` with `Y = X + c
```
This bit sounds hard to do with `simp`, since it involves casing on exists.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643817):
you just introduce another variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/natural%20number%20hell/near/126643823):
you do all that before you start the simp

