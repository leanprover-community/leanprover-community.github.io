---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03459convexample.html
---

## [general](index.html)
### [conv example](03459convexample.html)

#### [Kevin Buzzard (Mar 13 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651407):
I was trying to write an example to illustrate the power of `conv`, by finding an example where the entire goal was difficult to work with because it contained implicit proofs. I realised that there were two things I didn't understand properly. Here's some code.

#### [Kevin Buzzard (Mar 13 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651409):
```
@[elab_simple] def subtypeadd {m : ℕ} {n : ℕ} (A : fin m) (B : fin n) : fin (m+n) :=
  ⟨A.val+B.val,add_lt_add A.is_lt B.is_lt⟩

definition phi {m n : ℕ} : fin (m + n) → fin (n + m) := λ ⟨i,Hi⟩, ⟨i,add_comm m n ▸ Hi⟩

example {m n : ℕ} (A : fin m) (B : fin n) : phi (subtypeadd A B) = subtypeadd B A :=
begin
  have H : A.val + B.val = B.val + A.val := add_comm _ _,
  -- unfold subtypeadd using show
  show phi ⟨A.val + B.val, _⟩ = ⟨B.val + A.val, _⟩,
  rw H -- fails
end 
```

#### [Kevin Buzzard (Mar 13 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651451):
I wanted to make the example hard for one reason, but it somehow turned out to be hard for another reason :-/

#### [Kevin Buzzard (Mar 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651460):
My first question is why does the `show` command succeed? I assumed that what `show X` did was that it first checked that `X` made sense, and then checked that it was defeq to the goal.

#### [Kevin Buzzard (Mar 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651464):
But I thought I had explicitly rigged it here so that `X` wouldn't be able to be elaborated, because of the missing proofs.

#### [Kevin Buzzard (Mar 13 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651506):
My second question is why does `rw` fail. I have heard rumours that `rw` will not work inside a lambda (although I don't really understand why -- why is this?) but this is not a lambda and I think the reason for failure is something else.

#### [Kevin Buzzard (Mar 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651512):
The error message is
```
rewrite tactic failed, motive is not type correct
nested exception message:
check failed, application type mismatch (use 'set_option trace.check true' for additional details)
state:
m n : ℕ,
A : fin m,
B : fin n,
H : A.val + B.val = B.val + A.val
⊢ phi ⟨A.val + B.val, _⟩ = ⟨B.val + A.val, _⟩
```

#### [Kevin Buzzard (Mar 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651515):
and if I `set_option trace.check true` then I get an exciting helpful extra hint:

#### [Kevin Buzzard (Mar 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651516):
```
[check] application type mismatch at
  ⟨_a, _⟩
argument type
  A.val + B.val < m + n
expected type
  _a < m + n
```

#### [Kevin Buzzard (Mar 13 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651557):
which makes no sense to me...oh! Is it rewriting too many A.val + B.val's?

#### [Kevin Buzzard (Mar 13 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651559):
I am still a bit bewildered about why this is a type mismatch I guess.

#### [Kevin Buzzard (Mar 13 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651565):
(deleted)

#### [Kevin Buzzard (Mar 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651618):
(deleted)

#### [Kevin Buzzard (Mar 13 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123651680):
For the first question I guess an underlying question is "which option do you switch on so you can see how Lean is filling in `_`s?"

#### [Mario Carneiro (Mar 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123652795):
> My first question is why does the show command succeed? I assumed that what show X did was that it first checked that X made sense, and then checked that it was defeq to the goal.

I was going to mention this before with your `X = Y` into `X' = Y` problem - you could have just written `show X' = _`. The reason this works is because the checking is done in a weak mode that tolerates metavariable generation, and the second defeq step is not just checking defeq, it is unifying with the target. This means that the first stage will create metavariables and the second stage will unfold stuff as needed to figure out the metavariables. If it can't completely solve the metavariables, you will get new goals instead of an error.
```
example : tt = tt :=
begin
  show (λ x, tt) _ = tt,
  -- ⊢ (λ (x : ?m_1), tt) ?m_2 = tt
end

example : tt = tt :=
begin
  change (λ x, tt) _ = tt,
  -- ⊢ (λ (x : ?m_1), tt) ?m_2 = tt
  -- ⊢ Sort ?
  -- ⊢ ?m_1
end
```
As you can see, `show` differs slightly in that it doesn't change the number of goals while `change` will add all those unsolved metavariables as new goals, just like `refine` would.

#### [Mario Carneiro (Mar 13 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123652855):
By the way, goals that look like your `phi ⟨A.val + B.val, _⟩ = ⟨B.val + A.val, _⟩` often don't work (they fail in the first stage of parsing), because the anonymous constructor can't be solved outright. In this case it works because `phi` is sufficient to deduce that both constructors are `fin`.

#### [Mario Carneiro (Mar 13 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653214):
> My second question is why does rw fail. I have heard rumours that rw will not work inside a lambda (although I don't really understand why -- why is this?) but this is not a lambda and I think the reason for failure is something else.

`rw` is very sensitive to dependencies. (Or more accurately, it is sufficiently *insensitive* to dependencies that it will generally fail in their presence.) Both `rw` and `generalize` are built on the same basic underlying internal tactic `kabstract`, which is supposed to take a term `P[T]` containing a subterm `T`, and replace it with a variable `x`. This is needed to construct the motive of the `eq.rec` application that goes in the proof term when using `rw`, and it's what you see directly if you use `generalize`.

The strategy is very simple: look through the term for any subterms that match `T` (up to some very light unfolding), and replace them with `x`. It should be obvious that this can get you into trouble when you have dependencies. For example, if `two_pos : 0 < 2` then `<2, two_pos>` is a well typed element of `fin 2`, but if you simply replace 2 with x you get `<x, two_pos>` which is not in either `fin x` or `fin 2`, it's just malformed. It is actually really difficult to do this correctly in general; in this case you would probably want to generalize the proof of `two_pos` first so that it will "ride the wave" of 2 -> x renaming rather than being stuck talking about the fixed number 2.

As it pertains to your example, the error message is fairly clear, although it would be more obvious with `set_option pp.proofs true`. The left argument to the `fin` constructor has been generalized from `A.val + B.val` to `_a`, but the right argument, the proof, is still a proof of `A.val + B.val < m + n` (namely `add_lt_add A.is_lt B.is_lt`, what you ended up with after the unfolding), and this is not a correct proof of `_a < m + n`.

The other major rewrite engine in lean is `simp`, which does not use `kabstract`. It operates by using congruence lemmas to recurse into subterms, and this strategy makes it much more reliably type-correct when it comes to rewriting under dependencies. If you try to use `simp` to rewrite here, it will work, and the proof argument will change to a cast of some sort to accommodate the new type.

#### [Kevin Buzzard (Mar 13 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653217):
Is it possible for me to watch all this unification taking place explicitly? i.e. some set_option?

#### [Kevin Buzzard (Mar 13 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653282):
[that was about the show / change stuff]

#### [Mario Carneiro (Mar 13 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653325):
I think `set_option trace.type_context.is_def_eq true` is what you want

#### [Kevin Buzzard (Mar 13 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653332):
Earlier on I realised that I didn't really know what rw did, so I've just spent 20 minutes doing edge cases and now I can understand the rw issue. I found that `rw` doesn't commute with `eq.symm` in general :-)

#### [Sebastian Ullrich (Mar 13 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653334):
Plus `...is_def_eq_detail`, probably

#### [Kevin Buzzard (Mar 13 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653381):
```
example (a b: ℕ) : b + a = b + a + a + b := begin
rw add_comm, -- a + b = a + b + a + b
end
```

#### [Kevin Buzzard (Mar 13 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653455):
Are the `set_option` options documented anywhere?

#### [Mario Carneiro (Mar 13 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123653753):
`#help options` seems to do the trick. (I had to search the code to find that gem. `#help` is such a rarely used command for me, I'm not even really sure what's there...)

#### [Kevin Buzzard (Mar 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123654932):
I am not even sure if I knew `#help` existed. I thought the help command in Lean was `#print`

#### [Mario Carneiro (Mar 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123654973):
it certainly does seem to be a large overlap of duties

#### [Kevin Buzzard (Mar 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123654990):
I can use conv to rewrite `A.val + B.val` in that earlier example.

#### [Kevin Buzzard (Mar 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123654994):
```
@[elab_simple] def subtypeadd {m : ℕ} {n : ℕ} (A : fin m) (B : fin n) : fin (m+n) :=
  ⟨A.val+B.val,add_lt_add A.is_lt B.is_lt⟩

definition phi {m n : ℕ} : fin (m + n) → fin (n + m) := λ ⟨i,Hi⟩, ⟨i,add_comm m n ▸ Hi⟩

example {m n : ℕ} (A : fin m) (B : fin n) : phi (subtypeadd A B) = subtypeadd B A :=
begin
  have H : A.val + B.val = B.val + A.val := add_comm _ _,
  -- unfold subtypeadd using show
  show phi ⟨A.val + B.val, _⟩ = ⟨B.val + A.val, _⟩,
  conv
  begin
  congr,
  congr,
  congr,
  rw H,
  end, -- is the term on the left OK??
  admit
end
```

#### [Kevin Buzzard (Mar 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123654999):
conv is doing all sorts of funny things here

#### [Kevin Buzzard (Mar 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655000):
It seems to forget some terms

#### [Kevin Buzzard (Mar 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655002):
and I managed to do a rewrite which earlier on was impossible for a good reason

#### [Kevin Buzzard (Mar 13 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655052):
or was it impossible for a bad reason?

#### [Kevin Buzzard (Mar 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655114):
Oh maybe conv doesn't care about the terms it forgets.

#### [Mario Carneiro (Mar 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655119):
I would be in support of moving all "auxiliary" `#print` stuff to `#help`; it is a little confusing to have namespace overlapping between `#print options` (which prints lean cmdline options), `#print option` (which prints the `option` type) and `#print pp.all` (which prints info on the `pp.all` option)

#### [Kevin Buzzard (Mar 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655120):
Does conv not bother with subsingletons?

#### [Kevin Buzzard (Mar 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655126):
I lost a proof

#### [Kevin Buzzard (Mar 13 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655197):
I see. So `fin` is a structure so I can build things of type `fin n` and they will be of the form `<value,proof that this value is less than n>`

#### [Kevin Buzzard (Mar 13 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655205):
but there's nothing stopping me from deviously changing the value without changing the proof

#### [Mario Carneiro (Mar 13 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655213):
By the way, if you are actually interested in this theorem, a short proof is `fin.eq_of_veq (add_comm _ _)`

#### [Kevin Buzzard (Mar 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655278):
I don't need the theorem, I was experimenting with trying to build goals which the prettyprinter wouldn't let me use show with ("show <what the pretty printer says the goal is>" failing)

#### [Mario Carneiro (Mar 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655280):
`conv` uses congrence lemmas, like `simp`, to traverse the term, certainly if you are using the `congr` tactic

#### [Mario Carneiro (Mar 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655286):
so it will succeed for the same reason that simp does

#### [Kevin Buzzard (Mar 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655290):
conv is really useful for a learner like me.

#### [Kevin Buzzard (Mar 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655342):
It enables to you really zoom in to parts of complicated things which beginners have trouble manipulating

#### [Mario Carneiro (Mar 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655343):
You should turn on `pp.proofs` while working with this

#### [Kevin Buzzard (Mar 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655346):
oh that's a cool option

#### [Mario Carneiro (Mar 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655358):
lol I remember the days when it was the only option. It's like 80% a good idea to hide proofs

#### [Kevin Buzzard (Mar 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655359):
is there a command which just changes the state of every option that is available?

#### [Kevin Buzzard (Mar 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655364):
then I could easily see all the other things I'm missing

#### [Mario Carneiro (Mar 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655365):
lol that would be bedlam

#### [Kevin Buzzard (Mar 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655368):
Imagine how much I'd learn

#### [Mario Carneiro (Mar 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655417):
If you care about printing, look at completions for `set_option pp.`

#### [Kevin Buzzard (Mar 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655428):
I remember getting really confused early on because of those `_`s in goals which I'd completely forgotten what they stood for

#### [Kevin Buzzard (Mar 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655438):
It would be even better if it said what they were a proof of

#### [Mario Carneiro (Mar 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655455):
That was proposed; but it would make things even harder for the copy-pasters

#### [Kevin Buzzard (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655497):
why not make it an option?

#### [Mario Carneiro (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655502):
I don't want to have to edit all those types out

#### [Mario Carneiro (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655505):
to make it compile

#### [Kevin Buzzard (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655512):
Oh wooah if I set proofs on, then does "show (goal)" always succeed?

#### [Mario Carneiro (Mar 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655514):
no, silly

#### [Kevin Buzzard (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655515):
:-)

#### [Kevin Buzzard (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655524):
does that solve the halting problem or something?

#### [Mario Carneiro (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655526):
there are a thousand and one edge cases that cause bad printing

#### [Kevin Buzzard (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655528):
Oh OK.

#### [Mario Carneiro (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655529):
even `pp.all` sometimes fails

#### [Kevin Buzzard (Mar 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655530):
o_O

#### [Mario Carneiro (Mar 13 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655728):
Here's an example:
```
theorem T : nat.zero = nat.zero :=
by have f := (λ {x}, eq.refl x); exact f

set_option pp.all true
#print T
theorem T' : @eq.{1} nat nat.zero nat.zero :=
@(λ {x : nat}, @eq.refl.{1} nat x) nat.zero --parse error
```

#### [Kevin Buzzard (Mar 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655807):
Oh maybe we're talking at cross purposes.

#### [Kevin Buzzard (Mar 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655814):
```
theorem T' : @eq.{1} nat nat.zero nat.zero :=
begin
show @eq.{1} nat nat.zero nat.zero -- succeeds
end
```

#### [Kevin Buzzard (Mar 13 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655864):
I was wondering if one could be in tactic mode in a situation where the goal is represented by some string S, and then `show S` fails

#### [Kevin Buzzard (Mar 13 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123655937):
I am pretty sure I've done that before, but I am less sure about having done it with pp.all true

#### [Mario Carneiro (Mar 13 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123656284):
It's easiest to demonstrate by using `#print` to view proof terms, but this affects all printing, and you can make it work with target printing as well by a similar mechanism.
```
--set_option pp.all true
theorem T : nat.le nat.zero (by have f := (λ {x:ℕ}, 0); exact @f nat.zero) :=
begin
  -- ⊢ nat.le 0 (λ {x : ℕ}, 0)
  change nat.le 0 (λ {x : ℕ}, 0), --fail
  change nat.le nat.zero (@(λ {x : nat}, @has_zero.zero.{0} nat nat.has_zero) nat.zero) -- parse error
end
```

#### [Kevin Buzzard (Mar 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123656605):
Are these bugs in the prettyprinter? Or just interesting features?

#### [Kevin Buzzard (Mar 13 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123656620):
Or should `@(lam {x},...)` actually work?

#### [Sebastian Ullrich (Mar 13 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123656672):
It's the pretty printer wishing for a feature the parser hasn't implemented yet

#### [Sebastian Ullrich (Mar 13 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123656731):
Slightly passive-agressive behavior

#### [Kevin Buzzard (Mar 13 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123657305):
I see. The pretty printer is somehow the anti-parser isn't it.

#### [Kevin Buzzard (Mar 13 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123657312):
in fact it's a one-sided inverse, in a perfect world.

#### [Patrick Massot (Mar 13 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123657314):
See #1900

#### [Kevin Buzzard (Mar 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123661013):
I am still unclear about one thing in this thread.

#### [Kevin Buzzard (Mar 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123661014):
```
example (a b c N : ℕ) (H1 : a = b) (H2 : a < N) (H3 : b < N) :
 (⟨a,H2⟩:fin N) = ⟨b,H3⟩ :=
begin
-- rw H1 fails
conv begin
  to_lhs,congr, -- goal now | a
  rw H1, -- succeeds
  end,
end
```

#### [Kevin Buzzard (Mar 13 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123661095):
The first rw fails and my understanding is that it fails because it gives rise to a term which is malformed (copying from Mario's comments above). However it seems to be only as malformed as the term I successfully construct using the conv trick.

#### [Kevin Buzzard (Mar 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123723050):
I am still none the wiser about this. One conclusion which I've not yet ruled out is simply that whoever wrote `rw` could have done better, and made that first `rw H1` above succeed, because there is nothing in type theory stopping it from succeeding, as we see from the conv approach. Is the reason that `rw H1` fails simply that the `rw` code just doesn't cover this use case?

#### [Mario Carneiro (Mar 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123723190):
I think you are missing that the `conv` version isn't using just `rw`, it's using `rw` + `congr`, and it is applying `congr` in the place where dependency matters. Once the goal is `| a`, there is no longer a dependency to worry about, and `rw` has no problems.

#### [Kevin Buzzard (Mar 14 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123723911):
But there is nothing stopping someone from beefing up rw so that it works without using conv? It's just some tactic, right?

#### [Kevin Buzzard (Mar 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724107):
Initially when I heard that rw couldn't rewrite in certain circumstances I thought that this was because of some theoretical type theory issue which was beyond me, but now I am more inclined to believe that it's just beyond rw.

#### [Kevin Buzzard (Mar 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724117):
This typechecks:
```
example (a b c N : ℕ) (H1 : a = b) (H2 : a < N) (H3 : b < N) :
 (⟨a,H2⟩:fin N) = ⟨b,H3⟩ := sorry 
```

#### [Kevin Buzzard (Mar 14 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724133):
but if I replace `sorry` with `eq.subst H1 _` then all of a sudden I get a type mismatch in the statement (not the proof) of the example.

#### [Mario Carneiro (Mar 14 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724136):
Yes and no. `rw` does exactly what we want it to, which is to produce an `eq.rec` term with a well chosen motive. `congr` applies an appropriate congruence lemma. There are theoretical limitations on what you can prove using `eq.rec`, and this is why one wouldn't want to change `rw` for this

#### [Mario Carneiro (Mar 14 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724181):
I opened an issue on dependent `rw` a while ago, I think it was closed by "use `simp` instead"

#### [Kevin Buzzard (Mar 14 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724194):
I now know from experience that this is not a satisfactory response

#### [Kevin Buzzard (Mar 14 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724201):
The reason I got interested in this use of conv was that I had a situation where simp simplified too much

#### [Kevin Buzzard (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724245):
so I had to be super-accurate with my rw

#### [Kevin Buzzard (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724246):
conv saved me

#### [Mario Carneiro (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724250):
I mean the `simp` engine, not necessarily `simp` on its own

#### [Kevin Buzzard (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724253):
How do you use the simp engine??

#### [Simon Hudon (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724256):
Did it simplify too much even when you called `simp only [your rules here]`?

#### [Mario Carneiro (Mar 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724259):
You know that `simp` has a bazillion options, right?

#### [Kevin Buzzard (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724265):
Oh that's a good point Simon, I didn't try this

#### [Mario Carneiro (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724279):
Remember when you discovered that `unfold` is really `simp`?

#### [Kevin Buzzard (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724280):
Are those bazillion options documented? If not, then no I don't know and I don't know how to find out.

#### [Kevin Buzzard (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724289):
other than random looking through changelogs and source code

#### [Kevin Buzzard (Mar 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724290):
which I find about as pleasant as looking through trash cans

#### [Simon Hudon (Mar 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724327):
That would deserve a good amount of documentation, that's true.

#### [Mario Carneiro (Mar 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724335):
`simp only [h] {single_pass := tt}` is pretty close to `rw`-like rewriting

#### [Kevin Buzzard (Mar 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724349):
I did know about simp only from TPIL but somehow it's one of those options which I would never use in practice because my initial reaction when I read TPIL was "whyever would you want to use simp only?"

#### [Simon Hudon (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724352):
And if you identify the lemmas that cause trouble you can disable it specifically with `simp [my_rule, - naughty]`

#### [Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724358):
and it's only more recently as I have become more experienced that I realise I need it, by which time I have forgotten about it

#### [Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724366):
and the simp docs which I PR'ed have explanations of how to find out which lemmas are causing trouble

#### [Mario Carneiro (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724367):
And to identify naughty lemmas you can use `set_option trace.simplify.rewrite true`

#### [Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724370):
yeah, I read that in the docs

#### [Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724371):
which I wrote

#### [Kevin Buzzard (Mar 14 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724376):
because I cannot manage without docs

#### [Kevin Buzzard (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724383):
because I am an old man

#### [Kevin Buzzard (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724420):
so no I don't know about the bazillion simp options

#### [Kevin Buzzard (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724424):
if you just rattled a few off now I might add them to the docs

#### [Kevin Buzzard (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724426):
I am in my late 40s :-)

#### [Mario Carneiro (Mar 14 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724430):
```

structure simp_config :=
(max_steps : nat           := simp.default_max_steps)
(contextual : bool         := ff)
(lift_eq : bool            := tt)
(canonize_instances : bool := tt)
(canonize_proofs : bool    := ff)
(use_axioms : bool         := tt)
(zeta : bool               := tt)
(beta : bool               := tt)
(eta  : bool               := tt)
(proj : bool               := tt) -- reduce projections
(iota : bool               := tt)
(iota_eqn : bool           := ff) -- reduce using all equation lemmas generated by equation/pattern-matching compiler
(constructor_eq : bool     := tt)
(single_pass : bool        := ff)
(fail_if_unchanged         := tt)
(memoize                   := tt)
```

#### [Mario Carneiro (Mar 14 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724441):
as you can see, leo is hard at work with those docstrings :)

#### [Kevin Buzzard (Mar 14 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724688):
two out of 16 ain't bad, as Meat Loaf once said

#### [Kevin Buzzard (Mar 14 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724692):
I am now going to have to rewrite some of my updated simp docs which I was editing as this post arrived.

#### [Kevin Buzzard (Mar 14 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724735):
About to be deleted: `It is well-known that there are a bazillion simp options, although most are known only to the Lean Inner Circle. Examples which mere mortals know about are those documented in the reference manual and Theorem Proving In Lean.`

#### [Mario Carneiro (Mar 14 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123724966):
That's not even all of it - there is also the underlying command `ext_simplify_core` with lots of space for configurability. And `dsimp` has its own variants on all of this.

#### [Kevin Buzzard (Mar 14 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123725306):
There are more options somehow:

#### [Kevin Buzzard (Mar 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123725311):
`simp tactics in interactive mode have a new configuration parameter (discharger : tactic unit) a tactic for discharging subgoals created by the simplifier. If the tactic fails, the simplifier tries to discharge the subgoal by reducing it to true. Example: simp {discharger := assumption}.`

#### [Kevin Buzzard (Mar 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123725317):
from the changelog

#### [Kevin Buzzard (Mar 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123725379):
I can't get this to work though

#### [Kevin Buzzard (Mar 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123725587):
OK I added some stuff about simp config options and added it to my PR

#### [Mario Carneiro (Mar 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123725662):
the `discharger`is a `tactic unit`, so you have to write it in non-interactive mode (or else have `tactic` open, which is I think what Leo did in that quote). ``simp {discharger := `[assumption]}`` should work

#### [Mario Carneiro (Mar 14 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv example/near/123725719):
but it's not that useful compared to `simp *`

