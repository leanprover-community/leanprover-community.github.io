---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84306undead.html
---

## [general](index.html)
### [undead](84306undead.html)

#### [Kevin Buzzard (Aug 23 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132629895):
"Undead" is a game from [Simon Tatham's portable puzzle collection] (https://www.chiark.greenend.org.uk/~sgtatham/puzzles/). These games are perfect information one player puzzle games, and often solving a level completely (for me at least, in most of these games) involves finding a constructive proof that there is precisely one solution to the level. I'm probably going to supervise a masters project this coming academic year on games like this, so I thought it was about time I understood what I could do with them in Lean.

Here's a [pic of an undead level] (http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead_initial.png). The diagonal lines in some squares are (two-sided) mirrors. The vacant squares need to be each filled with exactly one of a vampire, ghost or zombie. There are 9 vacant squares and we're told at the top that we need to fill them with three ghosts, three vampires and three zombies. The numbers around the outside of the board are the number of monsters you can see if you look into the board from where the number is, with the caveat that you can't see a ghost directly and you can't see a vampire through a mirror. So for example, the zero on the top row, second from the left, indicates that you can't see the monster in the top left hand corner through a mirror, so it must be a vampire, and the 3 at the left of the top row indicates that exactly one of the monsters in the first column is a ghost (because you can only see three of the four monsters in that column).

This sort of game is really easy to model in Lean; like mathematics, it seems to fit very gracefully into the language of dependent type theory. The nine empty squares can be thought of as 9 variables of type `square` (or type `monster` or whatever), the 16 numbers and three totals give 19 equations involving these variables, and the two main claims here are (1) that there's a solution to the equations and (2) it's unique.

Here is a formalisation of the level in Lean, plus some preliminary lemmas.

https://gist.github.com/kbuzzard/53712d672a894d7b158a512f7aa5f836

The lemmas reduce the problem to the following position:

http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead.png

(and actually a little further because I worked out something about a7 after taking that screenshot). The search space initially has size 3^9, which is a bit big perhaps for Lean, but the lemmas I prove about the solution reduce the space to something like 2^7 * 3, which sounds a bit more reasonable. I think I'd now like to brute force it and get a proof that there's a unique solution, plus a description of the solution, but I'm not sure how to do that in Lean. I have these random facts like "variable a6 isn't a vampire" but I am not sure how to write the procedural code in Lean which will save me from generating a gazillion cases with a6 being a vampire. The issue is that I want to do cases on all 8 remaining variables at once, but for the variables where I've proved something I want to immediately eliminate all cases which contradict what I've proved. Am I making sense? I just want to solve the level now, in Lean, without running out of memory, and ideally I'd like to output the solution. I feel like I've done the lion's share of the work now but I've not quite finished.

#### [Sean Leather (Aug 23 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132630343):
`@[derive decidable_eq]`

#### [Kevin Buzzard (Aug 23 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132630393):
Oh yeah that was it :-) I derived it myself :-) I think I'd find it easier to remember that if I understood what was going on there. Is this the same as `@[simp]`? It doesn't look like it.

#### [Sean Leather (Aug 23 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132630465):
`init/meta/derive.lean` says: “Attribute that can automatically derive typeclass instances.”

#### [Sean Leather (Aug 23 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132630478):
Maybe that note will also help me remember the syntax. I don't use it very often, so I have to keep looking for it. But if I know that it's an attribute, I know it must be in `@[...]`.

#### [Kevin Buzzard (Aug 23 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132655747):
I'm working on square 7. After the line `  cases a₂;cases a₃;cases a₅;cases h₇;cases h₁₅,` in tactic mode, it's difficult for me to see what happened. Each of the a's has three possibilities, so after the three cases tactics there are now 27 goals. But for most of them (I think) there is a contradiction with assumptions h7 and h15, so after that entire line is processed we are back to one goal (unless I have misunderstood Lean's output). However I don't seem to be able to read off which of the cases we are in. Is there a trick for me to track which of the 27 branches survived?

#### [Chris Hughes (Aug 23 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132656912):
Prove it's equivalent to proving `∃! (a₁ ∈ [vampire, ghost]) (a₂ ∈ [ghost, zmobie]) ...` and use dec_trivial. You might have to guide simp a bit, and prove lemmas like `a ! = zombie iff a = vampire or a = ghost`

#### [Kevin Buzzard (Aug 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657067):
Actually I am now confused about whether I have even done what I think I've done. Is this a bug? What happens if you type this into a Lean file:

```lean
inductive square
| vampire : square
| ghost : square
| zombie : square 

theorem test (a b c d : square) : false :=
begin
  cases a;cases b,
  cases c;cases d,
  repeat {sorry}
end

```

and then put your cursor just after the end comma in the `cases a;cases b,` line? I expect to see 9 goals but I only see one. Typing "sorry" makes the next one appear :-) Typing a few sorries eventually sorts things out and then it's back to 9 goals.

#### [Kevin Buzzard (Aug 23 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657172):
Even weirder:

```lean
inductive square
| vampire : square
| ghost : square
| zombie : square

theorem test (a b c d : square) : false :=
begin
  cases a;cases b,
  sorry,
  sorry,
  cases c;cases d,
  repeat {sorry}
end
```

After the `b,` there are 9 cases, after the next sorry there are 8, and after the next one it drops to one. The others are still there, they're just not being displayed for some reason.
```

#### [Chris Hughes (Aug 23 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657277):
It seems to be being parsed as this
```lean
theorem test (a b c d : square) : false :=
begin
  cases a; {cases b,
  cases c; cases d, 
  repeat {sorry}},
end
```

#### [Chris Hughes (Aug 23 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657330):
Actually not quite.

#### [Gabriel Ebner (Aug 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657422):
I think the `;` just messes up the information on the current line.  If you put `skip,` on another line it shows the expected number of goals.

#### [Gabriel Ebner (Aug 23 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657546):
Information about the goal is stored in a very unstructured form at the moment: essentially there is a function `tactic.save_info` which stores the corresponding string at a user-specified position (= line/column pair, and yes this can be almost anywhere..).

#### [Kevin Buzzard (Aug 23 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657821):
If you put `skip` then on the line *before* the `skip` it displays correctly. So perhaps it's the second semicolon which is causing the confusion.

#### [Gabriel Ebner (Aug 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657983):
Yes, the semicolon seems to break the goal output between the surrounding commas.  If you add a `skip,` then you add a comma which keeps the breakage away.

#### [Patrick Massot (Aug 23 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132660215):
I've noticed repeatedly that using semi-colon is very confusing in this way

#### [Patrick Massot (Aug 23 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132660271):
About the general problem, isn't something that could be handled entirely by the type class system? It looks like problem designed for solving using prolog.

#### [Andrew Ashworth (Aug 23 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132660854):
i believe sebastian solved the n-queens problem using type classes

#### [Andrew Ashworth (Aug 23 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132660967):
this is really an abuse of inference I think :)

#### [Kevin Buzzard (Aug 23 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661039):
```quote
Prove it's equivalent to proving `∃! (a₁ ∈ [vampire, ghost]) (a₂ ∈ [ghost, zmobie]) ...` and use dec_trivial. You might have to guide simp a bit, and prove lemmas like `a ! = zombie iff a = vampire or a = ghost`
```
So how does `dec_trivial` work? Does it look at hypotheses? Why doesn't this work:

```lean
@[derive decidable_eq]
inductive square
| vampire : square
| ghost : square
| zombie : square

open square

lemma thing : ∀ a : square, a = vampire ∨ a = ghost ∨ a = zombie := dec_trivial -- fails

```

It looks pretty decidably trivial to me. How can I make this work?

#### [Chris Hughes (Aug 23 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661087):
Prove fintype square

#### [Kevin Buzzard (Aug 23 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661203):
`@[derive fintype]`?

#### [Kenny Lau (Aug 23 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661276):
look at my `three` elsewhere lol

#### [Patrick Massot (Aug 23 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661277):
What is this derive? I see this from time to time but never know what it means

#### [Kevin Buzzard (Aug 23 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661358):
What I wrote doesn't work.

#### [Kevin Buzzard (Aug 23 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661371):
`failed to find a derive handler for 'fintype'`

#### [Andrew Ashworth (Aug 23 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661688):
I believe the derive stuff is user-written extensions that add functionality to a type. like `@[derive decidable_eq]` adds an automatically generated instance saying that the type is decidable

#### [Kevin Buzzard (Aug 23 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661874):
```lean
definition finset_square : finset square :=
{ val := [vampire,ghost,zombie],
  nodup := begin
    repeat {constructor,intro a,cases a,repeat {exact dec_trivial}},
    constructor,
  end
}

instance : fintype square := {
  elems := finset_square,
  complete := λ x,by cases x;exact dec_trivial
}
```

:-)

#### [Kevin Buzzard (Aug 23 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661922):
I reckon that could be automated...

#### [Kevin Buzzard (Aug 23 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661973):
```lean

instance : fintype three :=
{ elems := {A, B, C},
  complete := λ x, by cases x; simp }
```

Kenny's `three`

#### [Kevin Buzzard (Aug 23 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662313):
```lean
import data.fintype

@[derive decidable_eq]
inductive square
| vampire : square
| ghost : square
| zombie : square

open square

instance : fintype square := {
  elems := {vampire,ghost,zombie},
  complete := λ x,by cases x;exact dec_trivial
}

open square

lemma thing2 : ∃! a : square, a = vampire := dec_trivial -- fails
```

That looks pretty trivial too. Error is

```
failed to synthesize type class instance for
⊢ decidable (∃! (a : square), a = vampire)
```

#### [Kenny Lau (Aug 23 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662380):
you need to import something iirc

#### [Chris Hughes (Aug 23 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662383):
`unfold exists_unique` first

#### [Kevin Buzzard (Aug 23 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662611):
rofl I just tried it for the actual problem and I got this error: https://gist.github.com/kbuzzard/84dbdf0fab4b96148099f49ac4f1770e . I think I've seen this before when you do exists_unique with multiple variables, it unfolds to something quite unwieldy.

#### [Patrick Massot (Aug 23 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662675):
nice goal!

#### [Kevin Buzzard (Aug 23 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662688):
```lean
example : ∃! (a b c : ℕ), a + b + c = 0 :=
begin
  unfold exists_unique,
/-
∃ (x : ℕ),
    (∃ (x_1 : ℕ),
         (∃ (x_2 : ℕ), x + x_1 + x_2 = 0 ∧ ∀ (y : ℕ), x + x_1 + y = 0 → y = x_2) ∧
           ∀ (y : ℕ),
             (∃ (x_1 : ℕ), x + y + x_1 = 0 ∧ ∀ (y_1 : ℕ), x + y + y_1 = 0 → y_1 = x_1) → y = x_1) ∧
      ∀ (y : ℕ),
        (∃ (x : ℕ),
           (∃ (x_1 : ℕ), y + x + x_1 = 0 ∧ ∀ (y_1 : ℕ), y + x + y_1 = 0 → y_1 = x_1) ∧
             ∀ (y_1 : ℕ),
               (∃ (x : ℕ), y + y_1 + x = 0 ∧ ∀ (y_2 : ℕ), y + y_1 + y_2 = 0 → y_2 = x) → y_1 = x) →
        y = x
-/
  sorry
end
```

#### [Kevin Buzzard (Aug 23 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662703):
Does it have to do that? Why not just "exists a b c, a + b + c = 0 and forall a' b' c', a' + b' + c' = 0 implies a=a' and b=b' and c=c'"?

#### [Chris Hughes (Aug 23 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662959):
It's parsed as a load of nested `exists_uniques`. I imagine your definition is quite hard to write

#### [Reid Barton (Aug 23 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663069):
Wait, does it even mean the right thing then?

#### [Reid Barton (Aug 23 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663141):
Isn't this "there exists a unique a such that there exists a unique b such that ...", but maybe for some other a there's multiple b's which would work, and so there isn't actually a unique (a,b,c)

#### [Reid Barton (Aug 24 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663480):
Say `P x y` holds if and only if (x, y) is (1, 2) or (3, 4) or (3, 5). Then `∃! x y, P x y = ∃! x, ∃! y, P x y` is true because `∃! y, P x y` holds only for x = 1.

#### [Reid Barton (Aug 24 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663491):
But I'm sure what you really wanted is `∃! p, P p.1 p.2`.

#### [Patrick Massot (Aug 24 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663542):
That's a pretty nasty trap

#### [Sebastian Ullrich (Aug 24 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663616):
*makes note to remove this "feature" as soon as possible*

#### [Kevin Buzzard (Aug 24 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663779):
I think I once tried to prove exactly the goal above and decided at the end of it that it seemed to be an extremely roundabout way of saying the correct thing.

#### [Kevin Buzzard (Aug 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663910):
I think it unfolds to something more complicated than what Reid is suggesting.

#### [Kevin Buzzard (Aug 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663916):
In particular I'm suggesting that Chris' comment is oversimplifying the matter.

#### [Kevin Buzzard (Aug 24 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663971):
Here's an example of an intermediate goal that you have to prove when proving the exists_unique statement above:

```
y : ℕ,
h : ∃ (x : ℕ), 0 + y + x = 0 ∧ ∀ (y_1 : ℕ), 0 + y + y_1 = 0 → y_1 = x
⊢ y = 0
```

#### [Reid Barton (Aug 24 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664036):
This is after you set a and b to 0, right?

#### [Reid Barton (Aug 24 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664041):
You shouldn't be given the `∀ (y_1 : ℕ), 0 + y + y_1 = 0 → y_1 = x` part of the hypothesis

#### [Reid Barton (Aug 24 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664053):
I think. Actually staring at this is making me confused.

#### [Reid Barton (Aug 24 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664101):
But in general, the way that Lean interprets `∃! x y, ...` is as `∃! x, ∃! y, ...`, right?

#### [Mario Carneiro (Aug 24 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664341):
> Description: An alternate definition of double existential uniqueness (see 2eu4 2371). A mistake sometimes made in the literature is to use ∃!𝑥∃!𝑦 to mean "exactly one 𝑥 and exactly one 𝑦." (For example, see Proposition 7.53 of [TakeutiZaring] p. 53.) It turns out that this is actually a weaker assertion, as can be seen by expanding out the formal definitions. This theorem shows that the erroneous definition can be repaired by conjoining ∀𝑥∃* 𝑦𝜑 as an additional condition. The correct definition apparently has never been published. (∃* means "exists at most one.")

http://us.metamath.org/mpeuni/2eu5.html

#### [Reid Barton (Aug 24 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664344):
You want to prove (0, 0, 0) is the unique solution (let's say). Then you ought to be able to prove
```lean
y : ℕ,
h : ∃ (x : ℕ), 0 + y + x = 0
⊢ y = 0
```

#### [Mario Carneiro (Aug 24 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664437):
the simplest way to assert multiple existential uniqueness is to claim unique existence of a triple

#### [Mario Carneiro (Aug 24 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664553):
also: why are you using lean as a sat solver? It's not particularly smart for this

#### [Kevin Buzzard (Aug 24 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132665771):
@**Kenny Lau** you might like this challenge:

```lean
example (p : ℕ → ℕ → Prop) :
(∃ m n, p m n ∧ (∀ b c : ℕ, p b c → b = m ∧ c = n)) ↔ ∃! m n : ℕ, p m n := sorry
```

Mario -- did I get this right? I just spent 15 minutes on it and failed to do one way; I don't want to waste Kenny's time. 

I'm using Lean as a whatever-you-said because I'm trying to figure out what can and can't and should be done using Lean when it comes to puzzles like this.

#### [Mario Carneiro (Aug 24 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132665962):
as Reid points out, as well as the quote I gave, that theorem is false

#### [Reid Barton (Aug 24 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666080):
There are other tools out there which are a better fit for these kinds of constraint satisfaction problems. One of which even shares an author with Lean.

#### [Kevin Buzzard (Aug 24 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666081):
right, I just went back to it and figured that it couldn't possibly be provable.

#### [Reid Barton (Aug 24 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666088):
However, you can't beat the convenience of already knowing the input language.

#### [Kevin Buzzard (Aug 24 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666093):
In which case I don't understand what this exists_unique even means.

#### [Kevin Buzzard (Aug 24 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666142):
I could solve this undead puzzle in python just with some dull loop. I was trying to work out what Lean could offer me that python couldn't.

#### [Kevin Buzzard (Aug 24 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666168):
So Lean really does do what Chris says? "There exists a unique x such that there exists a unique y such that..."? That's not what I would have guessed from the notation.

#### [Mario Carneiro (Aug 24 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666375):
```
example : ¬ ∀ (p : ℕ → ℕ → Prop),
  (∃ m n, p m n ∧ (∀ b c : ℕ, p b c → b = m ∧ c = n)) ↔ ∃! m n : ℕ, p m n :=
λ H, begin
  let p := λ m n, m = 0 → n = 0,
  have : ∃! m n : ℕ, p m n,
  { refine ⟨0, ⟨0, λ _, rfl, λ n h, h rfl⟩, λ m h, _⟩,
    rcases h with ⟨m', h₁, h₂⟩,
    by_contra h,
    have := h₂ 1 h.elim,
    rw ← h₂ 0 (λ _, rfl) at this,
    cases this },
  rcases (H _).2 this with ⟨m, n, h₁, h₂⟩,
  simpa [(h₂ 0 0 id).1.symm] using h₂ 1 1 id
end
```

#### [Mario Carneiro (Aug 24 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666391):
this is what all nested binders are unfolded to in lean

#### [Mario Carneiro (Aug 24 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666452):
in most cases it works brilliantly - forall, exists, indexed union, supremum, infinite sum... it is only exists unique which doesn't have a nice interpretation

#### [Kevin Buzzard (Aug 24 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666531):
rofl

```lean
definition p (a b : ℕ) := (a = 1 ∧ b = 1) ∨ (a = 2 ∧ b = 3) ∨ (a = 2 ∧ b = 4)

theorem silly : ∃! a b, p a b :=
begin
  existsi 1,
  split,
  existsi 1,
  split,
  left,exact dec_trivial,
  intros y,
  unfold p,
  simp,intro H,
  cases H,exact H,cases H,cases H,cases H_left,cases H,cases H_left,
  intros y Hy,
  unfold p at Hy,
  cases Hy with x Hx,
  cases Hx with H H1,
  cases H,exact H.left,
  cases H,cases H with Hy Hx,
  dsimp at H1,rw Hx at *,
  have H := H1 4,
  suffices : 4 = 3,
    revert this,exact dec_trivial,
  apply H,rw Hy,simp,
  cases H with Hy Hx,
  dsimp at H1,rw Hx at *,
  have H := H1 3,
  suffices : 3 = 4,
    revert this,exact dec_trivial,
  apply H,rw Hy,simp
end
```

#### [Kevin Buzzard (Aug 24 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666593):
I had no idea `∃!` meant that in Lean. That is for me a very surprising design decision. `∃! a b` doesn't even mean the same as `∃! b a`, right?

#### [Mario Carneiro (Aug 24 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666599):
no, they are not logically equivalent

#### [Mario Carneiro (Aug 24 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666608):
frankly the problem is that `∃!` is a shitty binder notation

#### [Kevin Buzzard (Aug 24 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666610):
wo

#### [Kevin Buzzard (Aug 24 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666611):
w

#### [Mario Carneiro (Aug 24 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666618):
it's not monotone

#### [Kevin Buzzard (Aug 24 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666626):
So in fact the thing I'm trying to prove with this undead thing is not even formulated correctly.

#### [Mario Carneiro (Aug 24 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666669):
like I said, the easy way to say this without having to think much is to use exists unique in a pair type

#### [Kevin Buzzard (Aug 24 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666698):
I don't care what Lean thinks `∃!` means. All I want to say is that there exists a unique 9-tuple with some property, and I've just realised that I'd better spell it out rather than using this terrifying notation.

#### [Kevin Buzzard (Aug 24 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666757):
I wonder if any of the mathematicians here can find a mathematician who thinks `∃! a b, p a b` means anything other than what I suggested it meant above with that false lemma.

#### [Kevin Buzzard (Aug 24 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666837):
I see. The reason this has happened is that Lean has one inbuilt system for dealing with multiple variables with one binder, and to put it bluntly it doesn't work with this one, so really perhaps a different system should be used for this one binder and that might be what Sebastian was saying. Maybe I've caught up at last.

#### [Mario Carneiro (Aug 24 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666999):
> I wonder if any of the mathematicians here can find a mathematician who thinks ∃! a b, p a b means anything other than what I suggested it meant above with that false lemma.

Most mathematicians think ∃! a b, p a b means what you wrote. They also think that ∃! a, ∃! b, p a b encodes this statement, and they are wrong

#### [Mario Carneiro (Aug 24 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132667051):
it is obvious once you give it more than a cursory examination, but it's one of those things that often escapes notice

#### [Kevin Buzzard (Aug 24 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132667177):
```quote
Most mathematicians think ∃! a b, p a b means what you wrote. They also think that ∃! a, ∃! b, p a b encodes this statement, and they are wrong
```
I don't think I'd ever even considered the concept `∃! a, ∃! b, p a b` until this evening and I suspect that many mathematicians would also not have come across it. It looks very weird to me. Of course, hindsight is a wonderful thing...

