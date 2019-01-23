---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27671optionrecelim.html
---

## Stream: [general](index.html)
### Topic: [option.rec.elim](27671optionrecelim.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053317):
I don't want to prove the goal here, I want to prove an intermediate lemma: `∀ x : γ, option.map f (k x) = j x`. 

So what's going on is `f : α → β` and `g : β → α` with `f ∘ g = id`. Given a function `j : γ → option β` I want to lift it to `k :  γ → option α` using `g` and then prove that applying `f` (or more precisely `option.map f`) to `k` gets you back to `j`. All this is happening in the middle of a tactic proof:

```lean
example (α β γ : Type) (f : α → β) (g : β → α) (H : ∀ b : β, f (g b) = b)
 (j : γ → option β) : 1 = 1 :=
begin
  let k : γ → option α := λ x,
--    match (j x) with
--    | none := none 
--    | some b := some (g b)
--    end,
-- here written out in term mode
    option.rec_on (j x) (none : option α) (λ b, some (g b)), 
  have : ∀ x : γ, option.map f (k x) = j x, -- what I actually want
    -- this should be trivial by casing on j x
    -- if j x is none then by definition k x is none  so f (k x) is none
    -- if j x is some b then map f (k x) = some (f (g b)) = some b
    intro x,
    cases (j x), 
    -- first goal now option.map f (k x) = none
    -- but assumption that j x = none nowhere to be seen
    repeat {sorry}
end 
```

I want to do a `cases` on `j x` but I can't seem to do it directly. How do I eliminate `j`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 21 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053396):
```lean
example (α β γ : Type) (f : α → β) (g : β → α) (H : ∀ b : β, f (g b) = b)
  (j : γ → option β) :
  let k : γ → option α := λ x,
    option.rec_on (j x) (none : option α) (λ b, some (g b)) in
  ∀ x : γ, option.map f (k x) = j x :=
begin
  
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053404):
thanks -- had not occurred to me to use let in the statement. This is a rather more elegant way of asking the question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 21 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053488):
```lean
example (α β γ : Type) (f : α → β) (g : β → α) (H : ∀ b : β, f (g b) = b)
  (j : γ → option β) :
  let k : γ → option α := λ x,
    option.rec_on (j x) (none : option α) (λ b, some (g b)) in
  ∀ x : γ, option.map f (k x) = j x :=
begin
  intros k x,
  dsimp [k],
  cases j x,
  refl,
  simp [option.map, option.bind, H],
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053550):
`dsimp [k]` does the substitution. That's what I was missing. Thanks a lot Kenny!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053683):
In my actual use case I end up with a term involving `id_rhs`. I'd never heard of this! It's defined in core lean as `abbreviation id_rhs (α : Sort u) (a : α) : α := a`. I've never heard of `abbreviation` either!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 21 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053701):
```quote
In my actual use case I end up with a term involving `id_rhs`.
```
consequence of using too many tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 21 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053703):
don't use any tactic in the definition of anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 21 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053712):
You could even do this
```lean
example (α β γ : Type) (f : α → β) (g : β → α) (H : ∀ b : β, f (g b) = b)
  (j : γ → option β) :
  let k : γ → option α := λ x, do y ← (j x), return (g y) in
  ∀ x : γ, option.map f (k x) = j x :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 21 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053725):
says the tacticmaster

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 21 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053909):
```lean
example (α β γ : Type) (f : α → β) (g : β → α) (H : ∀ b : β, f (g b) = b)
  (j : γ → option β) :
  ∀ x : γ, (do y ← (j x), return (f (g y))) = j x := 
 by simp [H]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 21 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053958):
```quote
In my actual use case I end up with a term involving `id_rhs`. I'd never heard of this! It's defined in core lean as `abbreviation id_rhs (α : Sort u) (a : α) : α := a`. I've never heard of `abbreviation` either!
```
I think abbreviation is more or less the same as reducible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130054096):
*boggle* `option.map.none'` is what I want to use to finish my base case, but alpha and beta have to be in the same universe and this is exactly the situation I'm not in :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130054156):
First few lines of `data/option.lean` in mathlib: 

```lean
namespace option
universe u
variables {α β : Type u}
```

and then things like `@[simp] theorem map_none' {f : α → β} : option.map f none = none := rfl`. Why are alpha and beta in the same universe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130054283):
I will have to use the non-API `refl` :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059145):
This is still no good in my use case -- I want to do `cases (j x)` and in the case `some val` I would like to keep track of the fact that `j x = some val` because I will need to know this later. Am I somehow doing the wrong thing entirely, or is there a trick I'm missing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059416):
Maybe I can refactor exactly what I want out as some awful ugly auxiliary lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059477):
I am supposed to be spending the weekend doing continuous valuations, and all I am doing is slowly proving that some definition doesn't depend on which universe I use :-/ I am just trusting that Mario is right when he says I need to make the type of Gamma the same as the type of R. My fear is that if I don't go through this pain now then I'll go through worse pain later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 21 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059671):
```quote
This is still no good in my use case -- I want to do `cases (j x)` and in the case `some val` I would like to keep track of the fact that `j x = some val` because I will need to know this later. Am I somehow doing the wrong thing entirely, or is there a trick I'm missing?
```
try `destruct (j x)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059771):
> and then things like @[simp] theorem map_none' {f : α → β} : option.map f none = none := rfl. Why are alpha and beta in the same universe?

OMG! No wonder that thing never works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059824):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059846):
This is why I make a habit of avoiding explicit universes whenever possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059975):
`destruct (j x)` @**Chris Hughes** this is *exactly* what I needed! This just saved me a huge refactoring pain! Thanks a lot! Even though I could see my lemma was unprovable I kept going, because I could see I could reduce it to exactly the hypothesis which wasn't in the context :-) I was worried I was wasting my time but using destruct instead gave me exactly what I needed. Wow, who needs `cases`!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059998):
```quote
OMG! No wonder that thing never works
```
If you hadn't told me to be universe polymorphic I'd never have spotted this :-) Thanks also to @**Johan Commelin** -- your "come on, it's just a glorified axiom of infinity" was what persuaded me to go back to `Type u` -- that and Mario saying that sticking to `Type` was futile anyway.

I am still kind-of fearing the discussion I'll one day have with a serious ZFC-ist who will be horrified that I am assuming the existence of universes when teaching my students undergraduate level maths. This is perfectoid spaces stuff but still -- Scholze's section 4 implies it can all be done in ZFC, and I'm not doing it in ZFC. Perhaps I should try and understand better what Mario was saying about all this a week or two ago.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 21 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060201):
how do you do category without universes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060667):
You aren't *using* universes so much as playing fast and loose with them. It *can* all be made precise and ZFC like, you just aren't bothering

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060668):
that's what you should tell the ZFC-ist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060710):
you would certainly be in good company in doing so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060854):
If you want an equality proof in your `cases`, you can use `cases h : e` instead of just `cases e`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060862):
I think `destruct` is just a longer way to say `cases`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061105):
```quote
If you want an equality proof in your `cases`, you can use `cases h : e` instead of just `cases e`
```
Yes it sounds like this would have done as well. I've seen `cases e with ...` but I hadn't realised how to name the hypothesis (or I had seen it before and forgotten).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061153):
and if that doesn't work you can also split the generalization and cases steps by using `generalize h : e = x` first and then `cases x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061355):
```quote
how do you do category without universes?
```
So you don't prove general theorems about categories, you prove results about the categories which you care about. For example I'm a number theorist so I might have a representation $$\rho : G\to GL(n,k)$$ and I might want to take its universal deformation. I might *say* "now consider the category whose objects are local rings $$R$$ with an identification of the residue field with $$k$$, such that these rings are projective limits of Artin local rings, and consider the functor from this category to the category of sets sending $$R$$ to the set of lifts of $$\rho$$ to $$\tilde{\rho} : G \to GL(n,R)$$ which lift $$\rho$$; then under certain finiteness assumptions on $$G$$ this functor is representable by some pair $$R^{univ},\rho^{univ}$$. Now consider the following elements of $$R^{univ}$$... . But when the ZFCist challenges me I say "aah there's a trick. I can prove that given any object $$R$$ of this category I can replace it with a subring $$R'$$ with cardinality at most $$\kappa(R,k)$$ for some explicit cardinal $$\kappa$$ such that anything interesting happening happens already in $$R'$$ (all this can be made rigorous but this is not the place to do it), so we can just consider the category of rings $$R'$$ with cardinality at most $$\kappa$$ and this is equivalent to a *small* category which is a set, and I can reformulate the statement I want purely as a statement about this latter set, so I didn't use universes after all".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061400):
And in the past I have linked to explicit places in the stacks project and in work of Scholze, where explicit arguments of this nature are given, always of this form ("we only need to consider things of size 2^2^2^(max(stuff we're looking at right now)), so we're all OK").

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061401):
So that's how an actual working mathematician does categories without universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061450):
I have no idea what the category theorist do and I'm not sure I care. Probably some work in ZFC and some don't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061453):
All I know is that the universes showing up in the category theory stuff which me and my number theory colleagues use can all be dealt with in this way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130062024):
```quote
If you want an equality proof in your `cases`, you can use `cases h : e` instead of just `cases e`
```
`e` is a term here. `cases (h : e)` doesn't typecheck (and indeed makes no sense). `cases h : e` does work but now I look at it it looks pretty weird.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130062147):
it's meant to be suggestive of the `h : e = x` hypothesis you get

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130062155):
it looks better in `generalize`, but in `cases` it doesn't make sense to have a `= x` there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130062208):
By the way, in tactic documentation `e` is often used as a placeholder for a term or `e`xpression, while `x` is a variable


{% endraw %}
