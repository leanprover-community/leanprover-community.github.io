---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96702anatisjustanonnegativeint.html
---

## [general](index.html)
### [a nat is just a non-negative int](96702anatisjustanonnegativeint.html)

#### [Kevin Buzzard (Sep 18 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134155954):
Over the summer I watched students struggling with easy number theory for the wrong reasons. They were asked questions about `nat` but their solutions involve dabbling with `int`. First they had to realise that subtraction was broken in `nat`. Then they had to coerce everything. And then they ended up with random goals like `of_nat x < \u y` where they knew `x < y` but didn't know how to finish. Any attempt to use induction in tactic mode produced goals mentioning terms of the form `-[1+ succ e]` or some such thing, and again they didn't by default know what to do with such terms. The fact that `-[1+ e]` is not defeq to the coercion of `-(1+e)` did not help either (it turns out to be defeq to `-(e+1)`, which in some sense indicates that the notation is not great, but I don't know if there are technical problems with changing it). 

I talked about this with Chris. He said that number theory was much harder than one might naively think, for beginners, because of these issues. I suggested that I just told them all to work with `int` at all times, because at least then the basic ring operations `+ - *` all do what the students think they will do, but Chris was not convinced that this was a good approach, because then you lose access to all the structure built on `nat`, for example primes. I did note that after a few weeks someone had defined `int.prime` and the students were using that. But I am asking if we can have more.

The structures `nat` and `{z : int // z >= 0}` are canonically isomorphic, if you forget the subtraction on `nat` which no end user should be touching anyway if they're doing mathematics. Hence every definition or construction or theorem about nat should have a corresponding definition or construction or theorem if you have an int `z` in your list of hypotheses and also a proof that `z>=0`. What I want the students to be able to do is to seamlessly get at all these definitions and constructions and theorems by perhaps using a tactic or perhaps using some clever tagging machinery (results about nat which transfer to int correctly because they don't mention subtraction, should be transferrable. For example one should be able to talk about `z` being prime, and it should realise that we just mean `nat.prime` for the corresponding `nat`). 

How feasible is this?

#### [Johan Commelin (Sep 18 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134156545):
I agree that we need better tooling here.
Any solution to this should preferably also allow to show that every int is just a rat with denominator 1, and every real is just a complex with imaginary part 0, etc... etc...

#### [Kevin Buzzard (Sep 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158536):
Actually we also ran into problems with dividing integers because we weren't in rat. In the division case I told the student to bite the bullet and stick with rat and use division and remainder and just pretend the rational was there. But I think you're right really -- to let mathematicians use the software naturally something like the following should happen: whenever someone in "mathematician mode" (a mode which people like Mario would always have switched off) attempts to divide a nat by another nat a little paperclip should pop up and say "I see you're trying to divide naturals. Would you like to coerce every single thing into rat? That way you'll get the right answer!" and then every nat is replaced by a rat plus proof that the denominator is 1 and the numerator is non-negative. Why not! To the mathematician all that has happened is that a structure has been replaced with a canonically isomorphic structure -- or, in other words, nothing has happened at all, but their division now works correctly. I don't see any disadvantages in this. At the end of it we were supposed to prove that n = 3, and we've actually proved n_rat = 3 : Q, but Lean is smart enough to figure out that we're done because n_rat := (n : Q) and simp knows about the lemma which the mathematician is too blind to see that they need.

#### [Kevin Buzzard (Sep 18 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158586):
I really think that is how it should work. That's how maths packages work, and that's what we're used to.

#### [Johan Commelin (Sep 18 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158669):
@**Kevin Buzzard** You might be interested in the last chapter of Mohan's thesis. It deals with this concept of "unification". I think it is one of the main gaps that lies between mathematicians and theorem provers.

#### [Kevin Buzzard (Sep 18 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158676):
pari-gp:

```
$ gp
Reading GPRC: /etc/gprc ...Done.

                  GP/PARI CALCULATOR Version 2.7.5 (released)
          amd64 running linux (x86-64/GMP-6.0.0 kernel) 64-bit version
  compiled: Nov 10 2015, gcc version 5.2.1 20151028 (Ubuntu 5.2.1-23ubuntu1) 
                           threading engine: pthread
                 (readline v6.3 enabled, extended help enabled)

                     Copyright (C) 2000-2015 The PARI Group

PARI/GP is free software, covered by the GNU General Public License, and comes 
WITHOUT ANY WARRANTY WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 8000000, primelimit = 500000
? x=4
%1 = 4
? type(x)
%2 = "t_INT"
? x
%3 = 4
? y=6/2
%4 = 3
? type(y)
%5 = "t_INT"
? z=x/y
%6 = 4/3
? type(z)
%7 = "t_FRAC"
? w=z*y
%8 = 4
? type(w)
%9 = "t_INT"
? 
```

All happening seamlessly behind the user's back.

#### [Patrick Massot (Sep 18 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158749):
Of course I agree. We have fun with perfectoid spaces, but the sad truth is that Lean is not usable because you cannot manipulate school numbers.

#### [Johan Commelin (Sep 18 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158776):
Mohan discusses several solutions, including coercions etc. And he makes fair points about them. I'm not sure if his solution will ever be adaptable to computers, because he ends up using an extremely weak type system.

#### [Johan Commelin (Sep 18 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158779):
But it is a good read anyway.

#### [Johan Commelin (Sep 18 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134158845):
Right, manipulating "numbers" should be trivial. By now I've learned to just avoid them. Seems like a bad solution.

#### [Kevin Buzzard (Sep 18 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134159314):
Here's an example of the problem. Say we take the standard undergraduate proof that if p is prime and p divides ab then it divides a or b. Here p, a, b are all positive nats say (because the person setting the question is sloppy, which is fine, there is no drive in mathematics to make the absolute most general statement here, we're not adding to mathlib). So the student chooses nat for p,a,b, which is a reasonable-looking choice, and then we assume p does not divide a, and we have to use this somehow, and the way we use it is some lemma saying that if p doesn't divide a then the gcd of p and a is 1. Now we use the standard fact that the gcd is a linear combination of the numbers in question, write `1=l*p+m*a` with `l` and `m` now ints, all these random up-arrows start appearing, we multiply both sides by b, prove that p divides both factors and try to deduce that p divides b but we've only deduced \u p divides \u b. What happened? What would be really nice is that when `gcd = l p + m a` is invoked *everything* becomes and int, and a tactic changes our goal to the corresponding statement about ints, and the user barely notices.

#### [Kevin Buzzard (Sep 18 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134159412):
Kicking around in the background is a proof that the new int-valued a and b and p are >= 0, so if the user ever wants to switch back and it's safe to, they can.

#### [Kevin Buzzard (Sep 18 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134159421):
@**Simon Hudon** Is this sort of thing feasible or am I asking for magic? Someone once told me that Lean does not do magic.

#### [Simon Hudon (Sep 18 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161382):
I taught you well, young man :) I think there are a few things we could try. We could have a tactic `to_int` to find all the local constants of type `nat` and replace them with a constant of the same name but of type `int` with an added assumption saying that it's non-negative.

#### [Simon Hudon (Sep 18 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161403):
The remaining problem would be to rewrite the assumptions to remove `\u` occurrences and use integer related functions / operators

#### [Simon Hudon (Sep 18 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161468):
The short answer is yes if the above is satisfactory to you

#### [Simon Hudon (Sep 18 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161508):
We could have a more elaborate tactic language to solve that problem but I'm thinking it might be overkill

#### [Kevin Buzzard (Sep 18 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134161837):
It could fail if the int version of the goal didn't imply the nat version.

#### [Simon Hudon (Sep 18 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134162045):
The way I'm thinking of it, if that was the case, you'd be left with some `\u`. But we can also make it fail if you prefer that.

#### [Simon Hudon (Sep 18 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134162484):
The easiest way to implement it would be to use `simp` to rewrite all the propositions into equivalent ones. This is stronger than required but it has the benefit of being simple to do.

#### [Simon Hudon (Sep 18 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134170146):
I just wrote a tactic to see if it could be done. I used it in the following example:

```lean
example (a b c d : ℕ)
  (h : a + b ≥ c)
  (h₀ : a ∣ c)
  (h' : a + c + 17 ≥ d) :
  a * c ≤ b + d * c :=
begin
  to_int,
    -- a : ℤ,
    -- a_nneg : a ≥ 0,
    -- b : ℤ,
    -- b_nneg : b ≥ 0,
    -- c : ℤ,
    -- c_nneg : c ≥ 0,
    -- d : ℤ,
    -- d_nneg : d ≥ 0,
    -- h : a + b ≥ c,
    -- h₀ : a ∣ c,
    -- h' : a + c + 17 ≥ d
    -- ⊢ a * c ≤ b + d * c
end
```

Does that look like what you're looking for?

#### [Simon Hudon (Sep 18 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134171190):
I just pushed it to `mathlib-nursery`. To use it, `import tactic.to_int`

#### [Simon Hudon (Sep 18 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134171215):
I'm hopeful that any oversight of the current version can be fixed by tagging lemmas with `@[to_int]`

#### [Mario Carneiro (Sep 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134171547):
The version I'm thinking of here would be a tactic like `cast ℤ at h1 h2`, which would try to convert any equalities or inequalities in the given target(s) to the specified type using cast theorems

#### [Mario Carneiro (Sep 18 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134171631):
Applied to `h'` above it would produce `(↑a + ↑c + 17 : ℤ) ≥ ↑d`

#### [Simon Hudon (Sep 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172005):
I decided to go one step further and eliminate all arrows if possible just so Kevin's student don't have to think about them.

#### [Chris Hughes (Sep 18 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172093):
I think hiding too much information might cause more problems than it solves.

#### [Mario Carneiro (Sep 18 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172119):
I'm also worried about losing the link to the original variables, which may be involved in other things that can't be cast

#### [Simon Hudon (Sep 18 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172222):
I agree that it can be the case but in this situation, removing the arrows can take a number of lines that aren't too enlightening with regards to what you're trying to prove

#### [Mario Carneiro (Sep 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172299):
that's the part that a `cast` tactic would solve

#### [Simon Hudon (Sep 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172301):
The other thing is that, if we keep the arrows, you end up working with two kinds of addition, two kinds of multiplication ... etc. I thought I'd try to remove that hurdle

#### [Mario Carneiro (Sep 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172432):
`cast` would also solve that

#### [Simon Hudon (Sep 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172456):
What part of `to_int` would you not put in `cast`?

#### [Mario Carneiro (Sep 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172534):
the part about eliminating the original variables in favor of arbitrary nonnegative integers

#### [Mario Carneiro (Sep 18 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172548):
and also allowing for more targeting to particular hypotheses

#### [Simon Hudon (Sep 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134172746):
I can see the point of that. Actually, I can see a case for both removing the original variables and keeping them.

#### [Mario Carneiro (Sep 18 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134174523):
besides the mental load of having arrows in your goal, I don't see any harm in keeping them, meaning that unless you are being specifically pedagogical and you are before the chapter on coercion or whatever it seems like a bad idea to remove them

#### [Mario Carneiro (Sep 18 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134174601):
That is, they shouldn't get in your way for the rest of the proof once they have been moved down to the atoms

#### [Simon Hudon (Sep 18 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134176929):
I agree that it's useful for pedagogical reasons and to lift a mental burden but I wouldn't say that those are mere goodies. I think that limiting the size of the relevant vocabulary (int vs nat) can make solutions more obvious both for a human prover and for an automated prover. If every natural number in your goal occurs with `\u` right next to it, most likely, natural numbers are not relevant for that part of the proof so let's not look for `nat.` lemmas.

#### [Mario Carneiro (Sep 18 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134179372):
It is true that if a natural number `n` only ever appears in the form `\u n` in hypotheses and the goal, then it is "safe" to replace it with a nonnegative integer variable. But this only works in certain cases; I don't see an analogous argument for `Q -> R` coercion for example.

#### [Simon Hudon (Sep 18 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134179785):
That can be optional behavior. It can a useful thing to do in other cases too. But in the case of nat / int, the knowledge we have of the situation allows us to assume `i ≥ 0`

#### [Nicholas Scheel (Sep 20 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326214):
I was playing around with a tactic that I think does similar things: https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/naturally.lean

#### [Nicholas Scheel (Sep 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326321):
some usages: https://github.com/MonoidMusician/MATH361/blob/lean-3.4.1/src/hw/hw2.lean#L520

#### [Nicholas Scheel (Sep 20 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326426):
at the end I use it to squash all of these at once, after applying `div_nonneg` as appropriate:
```lean
9 goals
⊢ 0 ≤ 81
⊢ 0 < 64
⊢ 0 ≤ 2
⊢ 0 ≤ 9
⊢ 0 < 8
⊢ 0 ≤ 9
⊢ 0 < 4
⊢ 0 ≤ 3
⊢ 0 < 2
```

#### [Nicholas Scheel (Sep 20 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326444):
(those statements are all in ℝ)

#### [Mario Carneiro (Sep 20 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20nat%20is%20just%20a%20non-negative%20int/near/134326914):
`norm_num`?

