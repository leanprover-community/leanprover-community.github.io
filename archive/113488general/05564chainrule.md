---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05564chainrule.html
---

## [general](index.html)
### [chain rule](05564chainrule.html)

#### [Patrick Massot (Feb 28 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123090490):
I have this chain rule proof in https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean which 100 lines long. And @**Assia Mahboubi** tells me https://github.com/math-comp/analysis/blob/6b36593f4a6a612212163b25c6bad3522c7fa679/derive.v#L494

#### [Patrick Massot (Feb 28 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123090492):
What is the miracle here? Is it proving stuff about o and O notations?

#### [Chris Hughes (Feb 28 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123102048):
I don't know anything about that proof in particular, but what I have noticed is that it's good practice to never prove too much in one go, and extract as many lemmas as possible. 
Stuff like `add_halves`, and `exists_forall_ge_and` are the sorts of things Mario has extracted, when a pattern comes up very often
Some of it is just style to make things shorter, for example, if `D` and `D'` were moved after the `:`, the first seven lines of the proof could be shortened to
```lean
λ ⟨cont_lin_l, ε, TEf, lim_ε⟩ ⟨cont_lin_P, η, TEg, lim_η⟩,
let cont_linPL := is_bounded_linear_map.comp cont_lin_L cont_lin_P in
⟨cont_linPL, begin ...
```
`unfold is_differential` is probably unnecessary as `split` does that for you
lines 78 to 85 could be moved into a couple of lines in term mode, possibly even without the `simp`s at the start, if all they do is unfold definitional equalities
 `simp [δ], simp [H]`, can probably be shortened to `simp [δ, H]`
Also the lines of calc could possibly be shortened to one line of rw or simp, when it's just equality that needs to be proved.

My experience is that you really have to pay attention to matters of style like this if you make a mathlib PR

#### [Mario Carneiro (Feb 28 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123102296):
The reason Assia's proof is so short is because almost all the work is in the previous lemma `dcomp` (and possibly also `compOo_eqo`)

#### [Patrick Massot (Feb 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123106492):
I understand that some stuff is split into several lemmas, but it still doesn't seem to be 100 lines long

#### [Simon Hudon (Feb 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123106699):
It might be one of those "the whole is more than the sum of its parts" situation. It's surprising sometimes how much you shrink your code by choosing abstract interfaces between components.

#### [Patrick Massot (Feb 28 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123106851):
@**Chris Hughes**  thank you for your comments. I agree about the first seven lines, although I'm not sure it improves readability. I thought about simplifying `simp [δ], simp [H]` to `simp [δ, H]` but it doesn't work. The calc lines are compressed as much as I could: I could get it to worked when skipping any step.

#### [Damien Rouhling (Mar 01 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129650):
Hello everyone.
I am the author of the proof Assia told you about. All in all, my proof is also 100 lines long if you take into account the lemmas I had to prove for this:
-  `linear_lipschitz` and its consequence `linear_eqO` to state that a continuous linear function is a O(id) at 0
- the two composition rules for O(id) and o(id) at 0: `compOo_eqo`and `compoO_eqo`.
The remaining is just manipulation of asymptotic expansions. No miracle in here :-)

#### [Patrick Massot (Mar 01 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129709):
`linear_lipschitz` is not included in my version, it is in https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L116

#### [Patrick Massot (Mar 01 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129724):
I don't know if Assia gave you the context though: I'm not a all an expert in Lean or any other proof assistant, I'm a regular mathematician would fancies trying proof assistants and started three months ago

#### [Patrick Massot (Mar 01 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129773):
I was interested in understanding what kind of support for o and O you managed to setup. But it's very hard for me to read Coq, especially SSReflect style

#### [Patrick Massot (Mar 01 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129778):
Can you do computations with o and O floating around in the middle of formulas?

#### [Patrick Massot (Mar 01 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129781):
Or only state as an hypothesis or conclusion that f = o(g)?

#### [Damien Rouhling (Mar 01 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129845):
We have rewriting rules for o and O so we can indeed manipulate such expressions.

#### [Patrick Massot (Mar 01 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129853):
Arggg, I'm required for more serious stuff. I'm on vacations and it's time to go skiing with my daughters (I can no longer follow my 10 years old son but I'm still a God skier to my 4 and 7 years old daughters). I will very carefully read whatever you'll write when I'll come back

#### [Damien Rouhling (Mar 01 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123130268):
In order to prove that f = o(g) we have two possibilities:
- go back to the definition of o(g), that's what I do for `compOo_eqo` for instance
- use rewriting rules to change the goal into o(g) = o(g).
Our notation for o(g) hides a function, which has the property to be a o(g). So the goal f = o(g) is an equality between two functions and after using rewriting rules the goal o(g) = o(g) is an equality between functions too. These can be different so we have a mean to replace the hidden function in f = o(g) with an existential variable so that unification will close the goal o(g) = o(g).

#### [Cyril Cohen (Mar 01 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123130338):
We have a draft paper here about this: https://hal.inria.fr/hal-01719918

#### [Patrick Massot (Mar 01 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138004):
Nice! :heart_eyes: @**Mario Carneiro** please, please, please, can we have this little-o and big-O magic in mathlib?

#### [Patrick Massot (Mar 01 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138057):
@**Cyril Cohen** @**Damien Rouhling** I would be a very nice way to learn Lean to translate this to Lean. I'm sure you understand that your goal of having asymptotic reasoning that looks natural to mathematicians is completely blocked by shortcomings of Coq notations. With Lean you could have much more natural notations

#### [Patrick Massot (Mar 01 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138123):
Where is Johannes? It seems he didn't come from Gitter to here. He should see this.

#### [Cyril Cohen (Mar 01 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138178):
@**Patrick Massot** in this case Coq notations are not "blocking" because we hack around the shortcommings.

#### [Cyril Cohen (Mar 01 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138281):
Most of the "magic" of our little-o and big-O notation happen in the use of existential variables to delay their instantiation until a stage where they appear in the goal. And of course in splitting the proof into the parts that depend only in little-o/big-O arithmetic and parts that depend only on linearity.

#### [Patrick Massot (Mar 01 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138282):
I think you are so much used to SSReflect notations that can't see how weird they look

#### [Patrick Massot (Mar 01 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138287):
Have you seen the `calc` blocks in my proof? This looks like mathematics to a mathematician eyes

#### [Patrick Massot (Mar 01 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138299):
I agree about delayed existential. The definition of delta very early in my proof is clearly the weirdest aspect for a mathematician

#### [Patrick Massot (Mar 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138357):
https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L41 and https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L129 completely kill the illusion of being doing maths

#### [Cyril Cohen (Mar 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138439):
I see your `calc`, that's what the mathematician should see, but do you like to explain line by line the new members of your equalities? Personally I prefer giving fewer explicit terms, and more unambiguous instructions... and letting the proof assistant show me where I am,... is it not a matter of taste?
How the notation f = g + o (e) looks exactly is another debate IMHO, and I think you are right, Coq gets in the way to get the most readable notation possible...

#### [Patrick Massot (Mar 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138479):
But `@^~_ @ F` from line 38 of your paper...

#### [Cyril Cohen (Mar 01 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138515):
```quote
https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L41 and https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L129 completely kill the illusion of being doing maths
```
I am happy to hear you say this, and this is exactly the point of the above mentioned code and paper.

#### [Patrick Massot (Mar 01 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138565):
Yes I understand, here my :heart_eyes: reaction

#### [Cyril Cohen (Mar 01 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138657):
```quote
But `@^~_ @ F` from line 38 of your paper...
```
...looks cryptic... I realize that now. Is it that bad?

#### [Sebastian Ullrich (Mar 01 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138704):
I didn't know you could embed Perl into Coq!

#### [Cyril Cohen (Mar 01 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138707):
bad -> difficult to read

#### [Moses Schönfinkel (Mar 01 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138717):
Be careful what you say around Coq people. Next thing you know there's "Cerl" or "Peroq".

#### [Patrick Massot (Mar 01 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138728):
In Lean you could write "bad → difficult to read". Unicode symbols is the default option

#### [Patrick Massot (Mar 01 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138734):
No ascii art notation

#### [Patrick Massot (Mar 01 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138806):
```quote
...looks cryptic... I realize that now. Is it that bad?
```
It's not much worse than `g => /=.`

#### [Patrick Massot (Mar 01 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138952):
But even removing SSReflect from the discussion,  in Lean you could replace `\forall k \near +oo, \forall x \near F, ‘|[f x]| <= k * ‘|[g x]|.` by 
`∀ k near +∞, ∀ x near F, |f x| ≤ k*|g x|`. I'm sorry I'm totally incompetent at discussing anything deep in dependent type theory, I only tell you what an average mathematician sees when starting using a proof assistant.

#### [Patrick Massot (Mar 01 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138979):
And my kids need me again (nap time ended), sorry

#### [Cyril Cohen (Mar 01 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138982):
I can totally agree with your last remark.

#### [Patrick Massot (Mar 01 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139061):
Maybe mathematicians will never use proof assistants, I don't know. But I'm 100% sure they will never use a proof assistant using alien notations

#### [Cyril Cohen (Mar 01 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139065):
Coq notation system makes us take solutions that are not satisfactory.
(the debate about `=> /=` and `@~_` and "Cerl" and "Peroq" is totally different)

#### [Patrick Massot (Mar 01 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139131):
I don't know if Coq can be "fixed" or if you should switch to Lean to get nice notations (and I have *no idea* about deeper reasons to choose one or the other). But I can tell you that notations (and the awesomeness of *Theorem proving in Lean*) is what made me start using Lean instead of Coq (remember I have no CS training at all)

#### [Patrick Massot (Mar 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139140):
And now I really have to go. See you!

#### [Cyril Cohen (Mar 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139142):
(the difference is in your last example the symbols correspond to usual mathematical practice, and in the "Cerl" criticism symbols that are introduced by programs or proof scripts, and both suffer from the lack of expressivness of Coq notation system)

#### [Cyril Cohen (Mar 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139144):
@**Patrick Massot** see you later

#### [Moses Schönfinkel (Mar 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139145):
I love SSreflect notation! I think ever since APL they've been building resistance in CS people to horrible notation (to the point where conciseness looks strangely appealing).

#### [Johannes Hölzl (Mar 02 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123180953):
Cyril showed me the `near` tactics at the TYPES meeting in Nijmegen a month ago. And indeed, they looks very nice! Modulo ssreflect which I still can't read :)

#### [Patrick Massot (Mar 02 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123180990):
Would it be an awful lot of work to adapt this to Lean and have them in mathlib?

#### [Johannes Hölzl (Mar 02 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123181067):
I'm not sure what's the best way to do it in Lean. One way would be to introduce a new tactic mode (like the `smt` or `conv` modes). But all we want is to add data and hide metavariables, so that we can take care of them later.

#### [Cyril Cohen (Mar 02 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123182527):
```quote
Cyril showed me the `near` tactics at the TYPES meeting in Nijmegen a month ago. And indeed, they looks very nice! Modulo ssreflect which I still can't read :)
```
Hi @**Johannes Hölzl** ! How are you? In Nijmegen I did show you near tactics but I did not have the time to show you the little-o and big-O notations and arithmetic. I might want to take a look at that too.

#### [Johannes Hölzl (Mar 02 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123182544):
Oh yes, it's on my list!

#### [Patrick Massot (Mar 02 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123182545):
Great!

#### [Patrick Massot (Mar 05 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123317833):
@**Johannes Hölzl** is today's filter commit related to the discussion in this topic?

#### [Johannes Hölzl (Mar 05 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123318060):
not directly . This was a change I had flying around since a couple of month. But I implemented `filter_upwards` when @**Cyril Cohen**  showed me his filter-tactics. It is a much simpler implementation, its what is available in Isabelle.
For a goal of the form `s \in f.sets` and terms for `h1 : t1 \in f.sets` ...  `hn : tn \in f.sets` one gets the new goal:
`\forall x, x \in t1 -> .. -> x \in tn -> x \in s`
(I will add this as docstring)

#### [Patrick Massot (Mar 05 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123318874):
Ok, thanks. Do you think you'll try to adapt the full thing at some point? Or is it too much work for something which wouldn't be new (hence not publishable)?

