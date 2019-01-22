---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87350Stilldontunderstandsimp.html
---

## [general](index.html)
### [Still don't understand simp](87350Stilldontunderstandsimp.html)

#### [Kevin Buzzard (Jul 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435282):
I still don't understand simp. I tried

```lean
example (c : ℕ) (H : 0 + 0 + c = 0) : c = 0 := by simp [H]
```

fully expecting it to work, and it didn't. So I switched to `by simp at H;assumption` which works fine -- but I feel like I'm missing a trick. What is the correct way to solve this goal? I know I could prove it using `zero_add` a couple of times -- is best practice to spell out the proof in full or use automation?

#### [Kevin Buzzard (Jul 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435357):
The moment I try `zero_add` in term mode I find myself in triangle hell.

#### [Chris Hughes (Jul 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435434):
`simpa using h`

#### [Chris Hughes (Jul 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435456):
`simp * at *`

#### [Kevin Buzzard (Jul 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130435851):
```quote
`simpa using h`
```

Do I need an import for this?

#### [Mario Carneiro (Jul 27 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130436468):
just the usual

#### [Kevin Buzzard (Jul 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437084):
That's happening to me more and more. Is there any way I can import every mathlib tactic automatically?

#### [Mario Carneiro (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437123):
`import tactic.interactive` gets the main tactics, but advanced tactics have their own imports, in particular `ring` and `finish`

#### [Kevin Buzzard (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437133):
Is there any reason I shouldn't import `ring` always?

#### [Mario Carneiro (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437138):
if you don't need it, don't import it

#### [Mario Carneiro (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437143):
and you shouldn't overuse it anyway, it's slow

#### [Kevin Buzzard (Jul 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437145):
```quote
if you don't need it, don't import it
```
Why not? If I don't use it, it doesn't even matter

#### [Mario Carneiro (Jul 27 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437200):
it adds a spurious dependency, which is probably a bigger problem for me than for you

#### [Mario Carneiro (Jul 27 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437223):
Of course, adding additional dependencies also slows down startup and recompile times

#### [Kevin Buzzard (Jul 27 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437228):
Even if I never use them?

#### [Kevin Buzzard (Jul 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437273):
They're compiled on sight?

#### [Mario Carneiro (Jul 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437281):
of course, how would it know if you have used the file unless it compiles the dependency?

#### [Mario Carneiro (Jul 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437292):
the way you are supposed to signal what you depend on is in your import list

#### [Kevin Buzzard (Jul 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437304):
How about I don't import it, and every time I use it a little pop-up appears saying "I see you're using `ring`. Do you want to import `tactic.ring`?"

#### [Mario Carneiro (Jul 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437309):
how would it know that `ring` exists?

#### [Kevin Buzzard (Jul 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437312):
and same for `simpa` and `tactic.interactive`

#### [Kevin Buzzard (Jul 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437322):
```quote
how would it know that `ring` exists?
```
Because I just tell it, using a "snippet" or something?

#### [Kevin Buzzard (Jul 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437377):
"I see that you just deleted the last occurrence of `simpa`. Do you want me to unimport it again?"

#### [Kevin Buzzard (Jul 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437387):
"I see that you used `simp`. Do you want me to replace that argument with what Lean actually did?"

#### [Mario Carneiro (Jul 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437389):
hm, I suppose one option is to somehow generate an "index" of all definitions in mathlib and their locations, and then store this info in some file with no dependencies and use it for hints

#### [Mario Carneiro (Jul 27 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437409):
Import analysis like that is very expensive

#### [Kevin Buzzard (Jul 27 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437410):
I'm basically asking for some sort of tactic manager I think.

#### [Kevin Buzzard (Jul 27 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437411):
I just have no idea about what is possible.

#### [Kevin Buzzard (Jul 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437471):
Does `simpa !? only? (* | [(* | (- id | expr)), ...]?) (with id*)? (using expr)? tactic.simp_config_ext?` actually mean something? Where can I learn about what it means?

#### [Mario Carneiro (Jul 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437472):
It is hard to get the analysis exactly right without just recompiling the current file, and if it's not exactly right then there is the possibility of incorrect hints, which will get old fast

#### [Mario Carneiro (Jul 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437486):
yes, it's a description of the parsing of arguments following `simpa`

#### [Kevin Buzzard (Jul 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437537):
I want it to be a regex but I can't make sense of it

#### [Mario Carneiro (Jul 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437544):
Basically `?` means that the previous thing may or may not be present, and `*` means zero or more of the previous thing

#### [Sebastian Ullrich (Jul 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437546):
It's a pseudorex

#### [Kevin Buzzard (Jul 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437547):
oh is it just a regex but using stuff I don't know?

#### [Kevin Buzzard (Jul 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437548):
Aah thanks!

#### [Mario Carneiro (Jul 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437559):
`|` means alternatives

#### [Mario Carneiro (Jul 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437563):
i.e. `a | b` means parse `a` or parse `b`

#### [Kevin Buzzard (Jul 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437618):
and `expr` is some kind of variable? Or you want something of type `expr`?

#### [Mario Carneiro (Jul 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437621):
`expr` means parse an expression

#### [Mario Carneiro (Jul 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437622):
and `id` means parse an identifier

#### [Kevin Buzzard (Jul 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437625):
I thought that `h` was a name in `simpa using h`, not an `expr`

#### [Mario Carneiro (Jul 27 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437637):
nope, look for `simpa using show` in mathlib and you will find several larger examples

#### [Mario Carneiro (Jul 27 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437644):
it's a nice way to say "use this term, but clean it up first"

#### [Kevin Buzzard (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437689):
so what's `with`?

#### [Kevin Buzzard (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437693):
I just apply these things at random usually.

#### [Mario Carneiro (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437699):
most of the args are just passed to `simp` as is

#### [Kevin Buzzard (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437700):
I have a list of "incantations formed with `simp` or `simpa` which have worked for me in the past"

#### [Mario Carneiro (Jul 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437704):
that includes `!` and `with`

#### [Mario Carneiro (Jul 27 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437719):
the `with` arg of `simp` allows you to simplify with custom simp sets, like `functor_norm`

#### [Mario Carneiro (Jul 27 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437726):
I don't use it much at all

#### [Kevin Buzzard (Jul 27 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437773):
What does `simpa [this]` do? Does that not even parse?

#### [Chris Hughes (Jul 27 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437781):
The same as `simp [this], assumption`

#### [Kevin Buzzard (Jul 27 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437859):
```lean
example (c : ℕ) (H : 0 + 0 + c = 0) : c = 0 := by simpa -- fails
example (c : ℕ) : 0 + 0 + c = 0 → c = 0 := by simpa -- works 
```
If you'd told me one works and one failed I would have guessed the other way around.

#### [Chris Hughes (Jul 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437929):
The second one is simplified to `c=0 -> c=0`. The first one doesn't simplify `H`

#### [Kevin Buzzard (Jul 27 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437940):
`example : ∀ (y : ℕ), (λ (c : ℕ), 0 + 0 + c = 0) y → y = 0 := by simp `

#### [Kevin Buzzard (Jul 27 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437982):
I wouldn't have dreamed of applying `simp` to that because it's not an equality. Am I using `simp` completely wrong?

#### [Mario Carneiro (Jul 27 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130437984):
Actually `simpa [this]` is a bit funny - it's more like `have this' := this, simp [this] at this', simp [this], exact this'`

#### [Mario Carneiro (Jul 27 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438007):
for the first example you want `by simpa using H`

#### [Mario Carneiro (Jul 27 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438050):
The `using` argument of `simpa` is pretty important. It's not really optional, it just has a default value of `this`

#### [Mario Carneiro (Jul 27 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438054):
so `by simpa` where there is no `this` in the context is kind of pointless

#### [Chris Hughes (Jul 27 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438060):
One nice feature of `simp` I discovered today, is it doesn't let you make horrible simp lemma. I tried to prove `forall x : zmod 2, x = -x` and it didn't let me make it `simp`

#### [Kevin Buzzard (Jul 27 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438080):
If you try it again you might get banned

#### [Kevin Buzzard (Jul 27 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438084):
"no more simp for you for a week"

#### [Mario Carneiro (Jul 27 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438146):
your use of `simp` to prove that is valid but a bit funny and doesn't generalize well

#### [Mario Carneiro (Jul 27 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438155):
I would do `intros y H; simpa using H`

#### [Mario Carneiro (Jul 27 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Still%20don%27t%20understand%20simp/near/130438163):
`simp {contextual := tt}` often works in these situations, but I don't think it simplifies the assumptions first

