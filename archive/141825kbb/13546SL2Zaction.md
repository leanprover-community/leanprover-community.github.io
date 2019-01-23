---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/13546SL2Zaction.html
---

## Stream: [kbb](index.html)
### Topic: [SL2Z action](13546SL2Zaction.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942386):
I'm trying to continue Patrick's work on finiteness of the quotient `SL2Z \ (Mat m)`.
This is one (approximate) step that would be useful:
```lean
def reps := {A : Mat m | A.c = 0 ∧ 0 ≤ A.a ∧ 0 ≤ A.b ∧ int.nat_abs A.b ≤ int.nat_abs A.d }

def ι : reps m → fin m :=
λ A, _
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942392):
I get a deterministic timeout just for parsing the type of `ι`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942399):
is that MWE?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942408):
Proof strategy: we need to prove that `reps` is finite. Do this by injecting into `fin m × fin m × fin m`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942412):
It is not exactly a MWE. You can find it by pulling the latest commits from `kbb`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942413):
I don't think that's a good strategy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942416):
Ok, so how do you prove that `reps` is a finset?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942530):
equiv it with `finset.filter (finset.univ : (finset (fin m × fin m × fin m))) sorry`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942548):
also why `int.nat_abs`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942605):
Because I don't know better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942607):
that's not what I mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942608):
That's what you were using in your inductive proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942619):
alright

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942626):
I think I'll prove that it's a fintype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942779):
ah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942780):
of course it times out

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942782):
`m` is an integer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942783):
`fin m` makes no sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942860):
Why did it time out? Why didn't it slap me in the face?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942904):
It should just have errored immediately saying that `m` is not a nat.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942928):
I think it's searching for a coercion from int to nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943083):
also it still isn't a fintype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943209):
What isn't?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943218):
if m=0 I don't think it's a fintype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943220):
the repr

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943224):
True. But you need `m ≠ 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943277):
Otherwise the orbits are parameterised by pairs `(a,b)` with `0 ≤ a` and `a,b` coprime.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943283):
Inparticularinfinitelymanyorbits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943379):
Maybe we should have assumed `m : ℕ` from the beginning.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945384):
why on earth is there classical.prop_decidable in the beginning of the file?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945453):
Because it's a math file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945457):
about integers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945508):
The last lemma requires it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945515):
it needs `decidable_eq (quotient (action_rel (SL2Z_M_ m)))`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945520):
I'll prove it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945523):
after dinner

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945571):
I guess we can't really avoid that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945584):
you're welcome to prove it if you want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945588):
@**Patrick Massot** Oo.ooo you released Kenny's inner wrath.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945593):
I guess in this case you *can* prove that `decidable_eq` if you want to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945606):
I already proved it: https://github.com/semorrison/kbb/blob/757806ec7f9848a5eb405ca26f5a12d94932a197/src/SL2Z_generators.lean#L4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945647):
no you haven't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133964107):
Cool! So now we have established finiteness of the orbit set!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971507):
```quote
Cool! So now we have established finiteness of the orbit set!
```
Not quite, there has been some regression, let me fix that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971536):
eh... I'm editing SL2Z_generators.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971539):
Done: no more sorry in SL2Z_generators.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971561):
ah I see what you did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979456):
done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979472):
```lean
/-- correct if m ≠ 0 -/
def reduce (m : ℤ) (A : Mat m) : Mat m :=
(λ n, nat.strong_rec_on n $ λ n ih A H,
if H1 : n = 0
then if H2 : A.a > 0
  then SL2Z_M_ m (T^(-(A.b/A.d))) A
  else SL2Z_M_ m (T^(-(-A.b/ -A.d))) (SL2Z_M_ m S (SL2Z_M_ m S A))
else ih _ (by subst H; from reduce_aux _ _ H1)
  (SL2Z_M_ m S (SL2Z_M_ m (T^(-(A.a/A.c))) A)) rfl
: Π n (A:Mat m), n = int.nat_abs A.c → Mat m) _ A rfl

--#reduce reduce (-1) ⟨1, 3, 1, 2, by norm_num⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979480):
```lean
def reps_equiv (hm : m ≠ 0) : quotient (action_rel (SL2Z_M_ m)) ≃ reps m :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979526):
@**Patrick Massot** @**Johan Commelin**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995671):
Ah, that looks like a smart way to approach this!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995907):
@**Kenny Lau** The linecount in that file really exploded! You write Lean several orders of magnitude faster than I can read it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995980):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996045):
Also you seem to like refactoring code, whereas for me there is some nasty psychological barrier...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996052):
Anyway, thanks a lot!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996056):
@**Mario Carneiro** Have you seen what happened?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996060):
what is this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996062):
We now have several hundreds of lines of code about a silly type called `SL2Z`, and it doesn't tie in to the `matrix` code at all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996110):
Well, that is not strictly true, Kenny proved that `SL2Z` is `equiv` to `SL 2 int`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996137):
But now this `SL2Z` is acting on different sets, etc... and all this extra structure has not been tied to regular matrices.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996143):
This makes me vaguely uncomfortable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996145):
I think this was a great experiment, but I'm somewhat worried.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996150):
Would you mind scrolling through the repo a bit?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996190):
unless the properties are not shared by other dimensions or rings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996199):
SL2Z is generated by two matrices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996203):
Right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996212):
`induction_on` is frightening

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996216):
But the action of SL2Z on other 2x2-matrices is generic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996237):
And the action of SL2Z on the upper-half plane is a restriction of the action of `(GL 2 real)_+` on the upper half plane

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996267):
So certain things are really specific, others are not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996281):
which is the restriction of GL2R acting on CP1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996304):
where should I be looking?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996310):
the frightening proof linked above appears to have been removed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996312):
I made a function called reduce

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996316):
You could start with `modular_forms.lean` and then drill down.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996364):
on master?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996366):
Most of the hard stuff is happening in `SL2Z_generators` and some in `modular_group.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996368):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996371):
We don't really use branches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996479):
In the end, I would like `Hecke_operator` in `hecke_operators.lean` to have a somewhat readable definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 15 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996541):
It feels to me like all the ingredients are now there... but as you can see, my attempt at writing the definition is :poop:


{% endraw %}
