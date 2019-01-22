---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/08397Usingaddrightinj.html
---

## [new members](index.html)
### [Using @add_right_inj](08397Usingaddrightinj.html)

#### [Abhimanyu Pallavi Sudhir (Oct 13 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135737105):
How many parameters do I need to specify to use `←@add_right_inj`? I'm trying to understand how to use tactics with implicit parameters, but can't seem to get it right. I keep getting `failed to synthesize type class instance`

#### [Chris Hughes (Oct 13 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135737389):
`rw ← add_right_inj x` should be good enough depending on the type that you're using. What type are the variables in your equality?

#### [Abhimanyu Pallavi Sudhir (Oct 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135737744):
```quote
`rw ← add_right_inj x` should be good enough depending on the type that you're using. What type are the variables in your equality?
```
Yeah, that works, but I'm trying to understand how exactly the `@` syntax works. Do we not need to use it for things in normal parantheses?

#### [Chris Hughes (Oct 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135737946):
No. `@` is for specifying the arguments in `{}` or `[]`, which are usually inferred, but sometimes Lean can't infer them so they have to be given explicitly. You can put underscores in place of arguments to you want to leave implicit, if you only want to give some of the implicit arguments explicitly.

#### [Kevin Buzzard (Oct 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135737951):
Can you post a MWE with the error?

#### [Kevin Buzzard (Oct 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135738009):
I gave a lecture on type class inference over the summer. Abhi if you log into Imperial's Panopto and search for Xena then you should be able to find all of them.

#### [Kevin Buzzard (Oct 13 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135738020):
The rule of thumb is that you should not be using @ in general

#### [Abhimanyu Pallavi Sudhir (Oct 13 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135738205):
```lean
import tactic.norm_num

example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) : 2 * r - 4 * s * s - 4 * s = 1 :=
begin
    rw ←@add_right_inj (4 * s + 4 * s * s) (2 * r - 4 * s * s - 4 * s) 1,
    sorry,
end
```

#### [Abhimanyu Pallavi Sudhir (Oct 13 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135738266):
(Something like that -- don't mind the sorry, I created the MWE from another project)

#### [Kenny Lau (Oct 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135738277):
```lean
import algebra.group

example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) : 2 * r - 4 * s * s - 4 * s = 1 :=
begin
    rw ←@add_right_inj ℕ _ (4 * s + 4 * s * s) (2 * r - 4 * s * s - 4 * s) 1,
    sorry,
end
```

#### [Kenny Lau (Oct 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135738280):
If you do `#check @add_right_inj`, then you get `∀ {α : Type u_1} [_inst_1 : add_right_cancel_semigroup α] (a : α) {b c : α}, b + a = c + a ↔ b = c`

#### [Kenny Lau (Oct 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135738281):
so the first argument is the type

#### [Kevin Buzzard (Oct 13 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135740723):
Here's a crash course in how it works. If you type `#check @add_right_inj` as Kenny says, you'll see the full definition of the function. Stuff in round brackets you are expected to supply (although if you are lazy you can write `_` which means "try to guess). Stuff in square brackets or curly brackets `{` `}` Lean is going to try to guess for you, so your first instinct should be to leave it out. If you leave that stuff out you just pretend it isn't there and don't use `@`

#### [Kevin Buzzard (Oct 13 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135740796):
Kenny wrote the output of the `#check` and you see that there's only one thing in round brackets, so it only wants the value of `a`

#### [Kevin Buzzard (Oct 13 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135740853):
So this works:
```lean
example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) : 2 * r - 4 * s * s - 4 * s = 1 :=
begin
    rw ←add_right_inj (4 * s + 4 * s * s),
    sorry,
end
```

#### [Kevin Buzzard (Oct 13 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135740891):
although I'm not sure it's what you want, because ` 2 * r - 4 * s * s - 4 * s` is parsed as ` (2 * r - 4 * s * s) - 4 * s` so you might want to worry about the `4 * s` first.

#### [Kevin Buzzard (Oct 13 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135740967):
But let's talk about this later. First let me show you how `@` works. With the `@` you need to supply _everything_, including the stuff which might not make much sense to you like the proof and all the data about the fact that the naturals are an additive right cancellative semigroup. Lean knows this already and without the @ it uses an algorithm called type class inference to find the proof in a database. That's what's going on with the square brackets.

#### [Kevin Buzzard (Oct 13 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135741043):
The squiggly brackets -- Lean is saying "I'll guess these from the context". For example your goal was `2 * r - 4 * s * s - 4 * s = 1` just before the rewrite, so Lean can guess `b` and `c` because they must be the left and right hand side.  And once it's guessed them, it can guess `α` as well, because that's the type of `b` and `c`

#### [Kevin Buzzard (Oct 13 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135741088):
If you want to go with the @ you can try this:

```lean
example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) : 2 * r - 4 * s * s - 4 * s = 1 :=
begin
    rw ←@add_right_inj _ _ (4 * s + 4 * s * s) _ _,
    sorry,
end
```

which says to Lean "OK I am using `@` so I am going to fill in everything myself...actually why don't you fill in those four things"

#### [Kevin Buzzard (Oct 13 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135741150):
This works too:

```lean
example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) : 2 * r - 4 * s * s - 4 * s = 1 :=
begin
    rw ←@add_right_inj ℕ _ (4 * s + 4 * s * s) (2 * r - 4 * s * s - 4 * s) 1,
    sorry,
end
```

and here I filled in the three squiggly bracket things but I didn't do the square bracket.

#### [Kevin Buzzard (Oct 13 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135741239):
Finally here is the example with everything filled in, including the term which Lean can generate automatically:

```lean
example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) : 2 * r - 4 * s * s - 4 * s = 1 :=
begin
    let abcde : add_right_cancel_semigroup ℕ, -- two goals now
      apply_instance, -- the new one just got closed
    rw ←@add_right_inj ℕ abcde (4 * s + 4 * s * s) (2 * r - 4 * s * s - 4 * s) 1,
    sorry,
end
```

The weird ` apply_instance` line means "explicitly apply the type class inference machine to solve this goal". It's the explicit tactic which means "run the square bracket machine to produce the term of this type"

#### [Kevin Buzzard (Oct 13 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135741500):
So that's the story of `@` in a nutshell. But what you might need advice on is how to solve your goal. If you let me cheat and work over the integers then here is the easiest way for a mathematician: 

```lean
import tactic.ring

example (r : ℤ) (s : ℤ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) : 2 * r - 4 * s * s - 4 * s = 1 :=
begin
    rw Hrs,
    ring,
end
```

However subtraction on the naturals is not so well-behaved (did anyone point out to you that `2-3=0`? ) and `ring` can't handle it (the naturals aren't a ring, and ring isn't always so clever in the naturals case)

#### [Kevin Buzzard (Oct 13 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135741550):
But something you have to learn about Lean is that almost every lemma you want is already there (e.g. `a+b=c -> a=c-b` and all the variants will be there).

#### [Kevin Buzzard (Oct 13 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135741806):
So here's a more low-level proof:

```lean
example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) :
2 * r - 4 * s * s - 4 * s = 1 :=
begin
  apply nat.sub_eq_of_eq_add,
  apply nat.sub_eq_of_eq_add,
  rw Hrs,
  simp,
end
```

#### [Kevin Buzzard (Oct 13 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135741863):
The strategy is to get rid of all the subtractions and then use simp, which is good at proving some equalities. Subtraction on naturals is a bit hairy though, that's why this was an effort. It would not surprise me if Kenny Chris or Mario could come up with a shorter proof.

#### [Chris Hughes (Oct 13 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135742263):
```lean
example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) :
  2 * r - 4 * s * s - 4 * s = 1 :=
by simp [nat.sub_sub, nat.add_sub_cancel, Hrs]
```

#### [Kevin Buzzard (Oct 13 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135742323):
How do you find a proof like that @**Chris Hughes** ?

#### [Kevin Buzzard (Oct 13 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135742325):
I was surprised `rw Hrs;ring` didn't work

#### [Chris Hughes (Oct 13 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135742640):
First try to substitute in Hrs as quickly as possible. Then `simp`, look at the goal and see what else needs to be done.

#### [Kevin Buzzard (Oct 13 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135742694):
I did that and got the horrible `1 + (4 * s + 4 * s * s) - 4 * s * s - 4 * s = 1`

#### [Kevin Buzzard (Oct 13 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135742718):
`((1 + (4 * s + 4 * s * s)) - 4 * s * s) - 4 * s = 1`

#### [Kenny Lau (Oct 13 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135744202):
@**Chris Hughes**
```lean
example (r : ℕ) (s : ℕ) (Hrs : 2 * r = 4 * s * s + 4 * s + 1) :
  2 * r - 4 * s * s - 4 * s = 1 :=
by rw [nat.sub_sub, Hrs, nat.add_sub_cancel_left]
```

#### [Kevin Buzzard (Oct 13 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135744571):
@**Abhimanyu Pallavi Sudhir** Kenny managed to do it in three rewrites; you can click around in the middle of his rewrite line to see what's going on.

#### [Abhimanyu Pallavi Sudhir (Oct 13 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135744726):
Oh, I know how to do the proof -- I just wanted to learn about @, __inst, etc. Your crash course is helpful, thanks!

#### [Kevin Buzzard (Oct 13 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135746827):
The weird `_inst_` variables are the ones which are generated by the type class inference machine

#### [Kevin Buzzard (Oct 13 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135747252):
If you ever see the word "instance" in Lean code it just means "definition, and add it to the type class inference machine too"

#### [Kevin Buzzard (Oct 13 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Using @add_right_inj/near/135747304):
So for example the construction of the ring structure on the integers will be defined as an instance rather than a definition, and then any lemmas about rings will automatically apply to the integers

