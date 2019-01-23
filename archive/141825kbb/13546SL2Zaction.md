---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/13546SL2Zaction.html
---

## Stream: [kbb](index.html)
### Topic: [SL2Z action](13546SL2Zaction.html)

---

#### [Johan Commelin (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942386):
I'm trying to continue Patrick's work on finiteness of the quotient `SL2Z \ (Mat m)`.
This is one (approximate) step that would be useful:
```lean
def reps := {A : Mat m | A.c = 0 ∧ 0 ≤ A.a ∧ 0 ≤ A.b ∧ int.nat_abs A.b ≤ int.nat_abs A.d }

def ι : reps m → fin m :=
λ A, _
```

#### [Johan Commelin (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942392):
I get a deterministic timeout just for parsing the type of `ι`

#### [Kenny Lau (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942399):
is that MWE?

#### [Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942408):
Proof strategy: we need to prove that `reps` is finite. Do this by injecting into `fin m × fin m × fin m`.

#### [Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942412):
It is not exactly a MWE. You can find it by pulling the latest commits from `kbb`

#### [Kenny Lau (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942413):
I don't think that's a good strategy

#### [Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942416):
Ok, so how do you prove that `reps` is a finset?

#### [Kenny Lau (Sep 14 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942530):
equiv it with `finset.filter (finset.univ : (finset (fin m × fin m × fin m))) sorry`

#### [Kenny Lau (Sep 14 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942548):
also why `int.nat_abs`?

#### [Johan Commelin (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942605):
Because I don't know better?

#### [Kenny Lau (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942607):
that's not what I mean

#### [Johan Commelin (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942608):
That's what you were using in your inductive proof

#### [Kenny Lau (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942619):
alright

#### [Kenny Lau (Sep 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942626):
I think I'll prove that it's a fintype

#### [Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942779):
ah

#### [Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942780):
of course it times out

#### [Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942782):
`m` is an integer

#### [Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942783):
`fin m` makes no sense

#### [Johan Commelin (Sep 14 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942860):
Why did it time out? Why didn't it slap me in the face?

#### [Johan Commelin (Sep 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942904):
It should just have errored immediately saying that `m` is not a nat.

#### [Kenny Lau (Sep 14 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942928):
I think it's searching for a coercion from int to nat

#### [Kenny Lau (Sep 14 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943083):
also it still isn't a fintype

#### [Johan Commelin (Sep 14 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943209):
What isn't?

#### [Kenny Lau (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943218):
if m=0 I don't think it's a fintype

#### [Kenny Lau (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943220):
the repr

#### [Johan Commelin (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943224):
True. But you need `m ≠ 0`

#### [Johan Commelin (Sep 14 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943277):
Otherwise the orbits are parameterised by pairs `(a,b)` with `0 ≤ a` and `a,b` coprime.

#### [Johan Commelin (Sep 14 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943283):
Inparticularinfinitelymanyorbits

#### [Johan Commelin (Sep 14 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943379):
Maybe we should have assumed `m : ℕ` from the beginning.

#### [Kenny Lau (Sep 14 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945384):
why on earth is there classical.prop_decidable in the beginning of the file?

#### [Patrick Massot (Sep 14 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945453):
Because it's a math file

#### [Kenny Lau (Sep 14 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945457):
about integers

#### [Patrick Massot (Sep 14 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945508):
The last lemma requires it

#### [Patrick Massot (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945515):
it needs `decidable_eq (quotient (action_rel (SL2Z_M_ m)))`

#### [Kenny Lau (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945520):
I'll prove it

#### [Kenny Lau (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945523):
after dinner

#### [Patrick Massot (Sep 14 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945571):
I guess we can't really avoid that

#### [Kenny Lau (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945584):
you're welcome to prove it if you want

#### [Johan Commelin (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945588):
@**Patrick Massot** Oo.ooo you released Kenny's inner wrath.

#### [Johan Commelin (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945593):
I guess in this case you *can* prove that `decidable_eq` if you want to.

#### [Patrick Massot (Sep 14 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945606):
I already proved it: https://github.com/semorrison/kbb/blob/757806ec7f9848a5eb405ca26f5a12d94932a197/src/SL2Z_generators.lean#L4

#### [Kenny Lau (Sep 14 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945647):
no you haven't

#### [Johan Commelin (Sep 14 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133964107):
Cool! So now we have established finiteness of the orbit set!

#### [Patrick Massot (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971507):
```quote
Cool! So now we have established finiteness of the orbit set!
```
Not quite, there has been some regression, let me fix that.

#### [Kenny Lau (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971536):
eh... I'm editing SL2Z_generators.lean

#### [Patrick Massot (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971539):
Done: no more sorry in SL2Z_generators.lean

#### [Kenny Lau (Sep 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971561):
ah I see what you did

#### [Kenny Lau (Sep 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979456):
done

#### [Kenny Lau (Sep 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979472):
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

#### [Kenny Lau (Sep 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979480):
```lean
def reps_equiv (hm : m ≠ 0) : quotient (action_rel (SL2Z_M_ m)) ≃ reps m :=
```

#### [Kenny Lau (Sep 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979526):
@**Patrick Massot** @**Johan Commelin**

#### [Johan Commelin (Sep 15 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995671):
Ah, that looks like a smart way to approach this!

#### [Johan Commelin (Sep 15 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995907):
@**Kenny Lau** The linecount in that file really exploded! You write Lean several orders of magnitude faster than I can read it.

#### [Kenny Lau (Sep 15 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995980):
lol

#### [Johan Commelin (Sep 15 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996045):
Also you seem to like refactoring code, whereas for me there is some nasty psychological barrier...

#### [Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996052):
Anyway, thanks a lot!

#### [Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996056):
@**Mario Carneiro** Have you seen what happened?

#### [Mario Carneiro (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996060):
what is this?

#### [Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996062):
We now have several hundreds of lines of code about a silly type called `SL2Z`, and it doesn't tie in to the `matrix` code at all.

#### [Johan Commelin (Sep 15 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996110):
Well, that is not strictly true, Kenny proved that `SL2Z` is `equiv` to `SL 2 int`.

#### [Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996137):
But now this `SL2Z` is acting on different sets, etc... and all this extra structure has not been tied to regular matrices.

#### [Mario Carneiro (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996143):
This makes me vaguely uncomfortable

#### [Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996145):
I think this was a great experiment, but I'm somewhat worried.

#### [Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996150):
Would you mind scrolling through the repo a bit?

#### [Mario Carneiro (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996190):
unless the properties are not shared by other dimensions or rings?

#### [Kenny Lau (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996199):
SL2Z is generated by two matrices

#### [Johan Commelin (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996203):
Right.

#### [Mario Carneiro (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996212):
`induction_on` is frightening

#### [Johan Commelin (Sep 15 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996216):
But the action of SL2Z on other 2x2-matrices is generic

#### [Johan Commelin (Sep 15 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996237):
And the action of SL2Z on the upper-half plane is a restriction of the action of `(GL 2 real)_+` on the upper half plane

#### [Johan Commelin (Sep 15 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996267):
So certain things are really specific, others are not.

#### [Kenny Lau (Sep 15 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996281):
which is the restriction of GL2R acting on CP1

#### [Mario Carneiro (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996304):
where should I be looking?

#### [Mario Carneiro (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996310):
the frightening proof linked above appears to have been removed

#### [Kenny Lau (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996312):
I made a function called reduce

#### [Johan Commelin (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996316):
You could start with `modular_forms.lean` and then drill down.

#### [Mario Carneiro (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996364):
on master?

#### [Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996366):
Most of the hard stuff is happening in `SL2Z_generators` and some in `modular_group.lean`

#### [Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996368):
Yes

#### [Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996371):
We don't really use branches

#### [Johan Commelin (Sep 15 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996479):
In the end, I would like `Hecke_operator` in `hecke_operators.lean` to have a somewhat readable definition.

#### [Johan Commelin (Sep 15 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996541):
It feels to me like all the ingredients are now there... but as you can see, my attempt at writing the definition is :poop:

