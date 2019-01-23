---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67584automaticsimplemmas.html
---

## Stream: [general](index.html)
### Topic: [automatic simp lemmas](67584automaticsimplemmas.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 15 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151823722):
We have a lot of simp lemmas in category theory that describe the action of functors, natural isomorphisms, etc. on various things. Johan has a few open PRs adding more of these lemmas (eg #503, #505) and they prompted me to try to understand how to describe these lemmas systematically.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 15 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151823896):
I think we can build these rfl lemmas by applying the following algorithm.
* Start with the result type `LHS = RHS`, where LHS is the thing being defined and RHS is its definition (this is what just putting `@[simp]` on the definition would do).
* If the RHS is a Prop, then just throw away the equation (do nothing).
* Otherwise, if the RHS is a record constructor `{ f1 := R1, f2 := R2 }`, recursively produce lemmas of the form `LHS.f1 = R1`, `LHS.f2 = R2`.
* Otherwise, if the RHS is a lambda `\lam x, R x`, recursively produce a lemma `LHS x = R x`.
* Otherwise, output a simp lemma stating `LHS = RHS` by rfl.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 15 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151823958):
@**Simon Hudon**, I guess we discussed something along these lines at some point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 15 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151824107):
But now I have a pseudo-spec

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 15 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151825251):
See also https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/sheaves.20and.20sites/near/148770849 for something that might qualify as pre-semi-pseudo-spec.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 15 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151825291):
My PR's are the result of following Mario's creed "just go for it". But I definitely wouldn't mind if this was automated away.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Dec 15 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151842594):
I remember this conversation. In my mind, that kind of feature might be about translating lemmas about specific definitions into lemmas referring to a type class instance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 15 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151844113):
@**Simon Hudon** I'm not sure I understand what you mean. Is it close to what Reid wrote down, or do you want something (slightly) different?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151844463):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Dec 15 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151846909):
Actually, I have a hard time remembering the details of that idea. I'll try to find the conversation again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 15 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151851104):
@**Simon Hudon** If you want a good showcase of what Reid and I mean, I think you should look at the file on comma categories: https://github.com/leanprover-community/mathlib/blob/over_under/category_theory/comma.lean
I just started adding over categories to the mix (a special case of comma categories), and I'm restating all the simp lemmas. The signal-to-noise ratio is increasing rapidly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Dec 15 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151851170):
Ah yes! That's also what I was going for I think. The way I was generalizing it is that we want to unfold specific projections. I think I had an idea of which ones to unfold but I'd have to get back into that mindset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Dec 15 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/151851331):
The good news is that soon, I won't have to take care of finding an apartment and I will have only Lean and my dissertation to take care of.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319775):
I'm sorry if I annoyingly keep coming on about this, but I have a command which does the constructor-half of this thing and has been tested on at least one (:D) category theory structure definition. It's called `rfl_lemma` (you use it on its own line like `rfl_lemma inverse_equivalence map`---which would tell you that an inverse equivalence of an equivalence has functor going the "forward way" equal to the functor going the "backward way" in the original equivalence), and is here:
https://github.com/semorrison/lean-tidy/blob/master/src/tidy/command/rfl_lemma.lean

It took multiple iterations because it turned out that getting the types right for the lemma I needed to generate turned out to be really quite hard (at least for me). I can give some examples to elabourate this point if anyone is interested. Making it do this for every projection of a structure instead of just the specified one is trivial.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319830):
`rfl_lemma?` is meant to tell you what the code generated was, and `private rfl_lemma ...` makes a private definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 21 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319847):
How much does this depend on the `lean-tidy` repo?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 21 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319851):
Sounds cool btw!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319864):
it depends on a few pieces of the `lib` folder in there, let me take a look

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 21 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319870):
```
tk "private rfl_lemma"
```
omg

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 21 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319928):
Is that pushing the definition of "token" a bit far or something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 21 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319930):
If it doesn't depend too much on `lean-tidy`, I'dd say: push it to a branch on the community repo. Then we can experiment with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 21 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152319955):
@**Kevin Buzzard** It is, but I guess it actually works. Though, @**Keeley Hoek**, have you taken a look at the `decl_meta_info` parameter?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320028):
No I haven't Sebastian, and thanks, now I have an idea about what it's for :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 21 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320044):
Yeah, I don't think your current code would have worked anyway. There is no such registered token.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320059):
The thing is, I'm pretty sure it did work! I'll try...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320066):
also it was before I knew I could do stuff like parse a question mark after a token, so please forgive me... :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320116):
It will be parsed successfully, but it will still call the regular definition with `private := tt` in the meta info

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320210):
Unless you've run it and can prove I'm crazy, I just did and I'm quiiite confident a different one of those `user_command`s is being called depending on private or not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320258):
Does it have something to do with the fact that for `user_command`s, unlike `user_notation`s, you don't need to reserve tokens for them to work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 21 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320261):
Right... oops

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320305):
:D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320330):
But no reason not to fix it up so it works properly... cheers! (and I only need a single definition now, not `2^2`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320363):
BTW, here's a "live demo"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320369):
(RE: the original post)
````lean
structure my_str :=
(a : ℕ)

def a_cnstr (b : ℕ) : my_str := ⟨b⟩
def a_cnstr' (b : ℕ) : my_str := ⟨b + 1⟩

rfl_lemma? a_cnstr a
private rfl_lemma? a_cnstr' a
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 21 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320457):
Nice. Any reason it's not an attribute?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320555):
That's cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320641):
@**Johan Commelin** Based on the pieces of `lib` which have ended up in mathlib now, I just need the `lib.expr` support file. My only reluctance comes from the fact that I will have to check whether a few of the functions at the bottom of that file are already in mathlib---at the time it was less effort just to write them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 21 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152320981):
One more thing if anyone doing maths actually uses it: it adds a prime to the projection name you supply, seeing if that works, before trying without. Hopefully that's convenient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 21 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20simp%20lemmas/near/152351507):
The interface I had in mind was that you'd write something like `@[simp_fields] def a_cnstr ... := ...`, and it would automatically generate all of the appropriate lemmas.

