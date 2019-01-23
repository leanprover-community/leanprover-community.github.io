---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61646Unfoldingcarefully.html
---

## Stream: [general](index.html)
### Topic: [Unfolding carefully](61646Unfoldingcarefully.html)

---

#### [Moses Schönfinkel (Apr 11 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124924517):
Suppose I have the following goal `f a = c (f (d a))`. What I am looking to do is to `unfold1 f` but only on the left hand side. Currently I do `generalize hack : f (d a) = x, unfold1 f, rw <- hack`. Apart from the fact that it's a hack, the `generalize` takes a couple of seconds to execute. I tried using `conv { to_lhs ... }` but `unfold1` is not an option in conv (and simp fails with deterministic timeout). a) Why on Earth is `generalize` so slow in this case - is it because `c` is some horrible dependently typed function with explicit well founded termination proofs? b) Is there a nicer trick to invoke `unfold1` on left hand side only?

#### [Kenny Lau (Apr 11 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124924577):
use `change`?

#### [Moses Schönfinkel (Apr 11 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124924634):
that would involve me having to explicitly state the effect of unfolding if I understand your suggestion; right?

#### [Simon Hudon (Apr 11 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124932179):
What about using transitivity instead of generalize?

#### [Moses Schönfinkel (Apr 11 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933566):
ooh that is actually brilliant! what I ended up doing is something I'm ashamed of but it saves me 15 seconds on each recompile - I reformulated the lemma such that it contains a pre-generalized expression and an equality (which I will, of course, change now :P)

#### [Simon Hudon (Apr 11 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933627):
Great! Glad to be of help! So, the way I use `transitivity` to protect parts of my formulas is to do `transitivity, blah, blah, refl`

#### [Moses Schönfinkel (Apr 11 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933640):
Yeah I have never thought of that. Thanks a lot. I wish `conv` was a bit less constrained.

#### [Moses Schönfinkel (Apr 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933693):
if this worked, then `conv { to_lhs, dsimp1 f }` would be just fine for me - but `interactive.conv.*` only has a bunch of tactics for reasons I'm not sure I want to know about :P

#### [Simon Hudon (Apr 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933694):
If you have something more specific that you want to use, let's say `g` instead of `=`, you can also make your own protection lemmas:

```
lemma protect (x y : α) (z : β) 
  (h : x = y)
  (h : g y z)
: g x z := ...
```

This allows you to select exactly what part of the formula you want to rewrite when you expect something very specific. And `z` is protected.

#### [Moses Schönfinkel (Apr 11 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933756):
ah, right; this is basically the general version that I ended up doing, but I think the transitivity is such a neat hack :P

#### [Simon Hudon (Apr 11 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933767):
```quote
if this worked, then `conv { to_lhs, dsimp1 f }` would be just fine for me - but `interactive.conv.*` only has a bunch of tactics for reasons I'm not sure I want to know about :P
```
I think Coq is more targeted like that `rewrite h at 1,3`. I found I missed that at first but I'm not sure it makes for stable proofs

#### [Moses Schönfinkel (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933776):
yes, in Coq I can rewrite where I want

#### [Moses Schönfinkel (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933779):
I can also rewrite under binders

#### [Moses Schönfinkel (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933780):
(with setoid rewrites)

#### [Moses Schönfinkel (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933785):
in Lean I've only used `simp` to rewrite under binders, not sure how else it can be even done

#### [Simon Hudon (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933788):
`simp` helps there with binders and congruence lemmas but it's a bit less controlled

#### [Simon Hudon (Apr 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933835):
... yeah, exactly

#### [Moses Schönfinkel (Apr 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933842):
stability of proofs has never been an issue for me, because, I, urm... write them once and then I... forget about them...

#### [Moses Schönfinkel (Apr 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933846):
I may need to try to write Coq in "industrial" settings :P

#### [Simon Hudon (Apr 11 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933853):
Question: I've only used Coq as a noob so I never experienced scaling up proofs that uses the `at 1,3` notation. Do you find that your proofs breaks a lot when you do that?

#### [Moses Schönfinkel (Apr 11 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933855):
yes, they do

#### [Moses Schönfinkel (Apr 11 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933858):
it's the absolute worst thing one can do

#### [Simon Hudon (Apr 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933923):
In my temporal logic tactics language, I have played with a tactic you call as `rw_using : f x = g x, { /- proof -/ }`. For some reason, I liked not clearing a temporary assumption.

#### [Simon Hudon (Apr 11 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933971):
In temporal logic, that was doubly useful because the proof of equality was typically done in normal Lean logic

#### [Simon Hudon (Apr 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933979):
Otherwise, I really haven't found a drop in replacement for that Coq notation

#### [Moses Schönfinkel (Apr 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933983):
I wish I understood exactly how `simp` works but I have never had the willpower to look at it

#### [Moses Schönfinkel (Apr 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934025):
I believe it's been modeled to resemble the Isabelle heuristics you get when you're within a single `theory` section thing

#### [Moses Schönfinkel (Apr 11 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934037):
where `theory` just aggregates a set of related constants, definitions, proofs, etc. and you abuse this implicit relation in automation

#### [Simon Hudon (Apr 11 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934038):
I feel like I really don't understand what Isabelle does with any given proof. It's hard for me to understand that comparison

#### [Moses Schönfinkel (Apr 11 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934081):
you basically help guide automation in Isabelle by aggregating related stuff together in "theories", which is something like making a hint database in Coq

#### [Moses Schönfinkel (Apr 11 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934160):
(so like a beefy namespace that implicitly provides hints for automation)

#### [Simon Hudon (Apr 11 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934166):
Ah I see. Does it make things clearer to use the theories or the databases?

#### [Moses Schönfinkel (Apr 11 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934172):
databases are less implicit so you have to go over the trouble of creating them

#### [Moses Schönfinkel (Apr 11 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934174):
so in Isabelle you get nice behaviour by default but it's less controlled because it's just "whatever you put in this theory"

#### [Moses Schönfinkel (Apr 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934230):
I think people with purely math background would have easier time using Isabelle, simply because you get nice implicit heuristic-guided behaviour out of the box (+ the Sledgehammer)

#### [Moses Schönfinkel (Apr 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934236):
if I understand Kevin correctly, he uses Lean because he wants dependent types

#### [Moses Schönfinkel (Apr 11 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934246):
(or I should say, he's not using Isabelle because he wants dependent types)

#### [Moses Schönfinkel (Apr 11 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934254):
and `simp` in Lean takes after Isabelle default simplifier, I believe

#### [Simon Hudon (Apr 11 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934307):
Any chance that something like sledgehammer would work with dependent types? Or is it more of a matter of structuring databases like Isabelle?

#### [Moses Schönfinkel (Apr 11 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934321):
it would work, Sledgehammer is almost like an outside tool that ships proof obligations to SMT solvers and ATPs

#### [Moses Schönfinkel (Apr 11 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934329):
Sledgehammer is really the most unimpressive piece of Isabelle; it just tries to invoke every automating algorithm it can get its grabby mittens on

#### [Sebastian Ullrich (Apr 11 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934605):
That may be the understatement of the century

#### [Moses Schönfinkel (Apr 11 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934614):
:D

#### [Sebastian Ullrich (Apr 11 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934637):
Sledgehammer is the result of a multi-year research project that produced a good amount of papers http://www.cl.cam.ac.uk/~lp15/papers/Automation/

#### [Sebastian Ullrich (Apr 11 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934693):
The hard parts are relevance filtering of lemmas to pass to the external solver, and of course translating between HOL and FOL

#### [Moses Schönfinkel (Apr 11 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124936062):
ok ok I will change it to 2 out of 10 on the scale of impressiveness, making it the second least impressive Isabelle feature right after its bundled development IDE :grinning:

#### [Kevin Buzzard (Apr 11 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947660):
I use Lean because when I had never heard of any theorem provers apart from Coq, and never used any at all, I watched a live stream of Tom Hales in Cambridge talking about (amongst other things) FAbstracts, and someone asked him which language he would be using, and he said "...Lean?" and I thought "OK that'll do for me"

#### [Kevin Buzzard (Apr 11 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947669):
and I certainly didn't know what a dependent type was at that point

#### [Kevin Buzzard (Apr 11 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947672):
I just decided to jump in

#### [Kevin Buzzard (Apr 11 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947753):
```quote
I wish I understood exactly how `simp` works but I have never had the willpower to look at it
```
I wish I understood more about how `simp` works but I learnt a couple of `set_option` options and wrote https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md

#### [Kevin Buzzard (Apr 11 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947824):
Looking at the output of `set_option trace.simplify true` gave me some sort of idea about the absolute inanity of what simp was doing

#### [Chris Hughes (Apr 11 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948004):
```quote
```quote
I wish I understood exactly how `simp` works but I have never had the willpower to look at it
```
I wish I understood more about how `simp` works but I learnt a couple of `set_option` options and wrote https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md
```
That bit at the end sounds interesting. Does that mean if I had `a + b ≡ c [MOD n]` and `h : a ≡ d [MOD n]` I could rewrite to get `a + d ≡ c [MOD n]`? How would that work with complicated examples, with lots of addition and multiplication?

#### [Kevin Buzzard (Apr 11 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948228):
I have never used that MOD business so I'm not sure

#### [Kevin Buzzard (Apr 11 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948232):
Oh, Gabriel said that

#### [Kevin Buzzard (Apr 11 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948276):
I didn't understand it so I didn't use it

#### [Kevin Buzzard (Apr 11 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948281):
[and you mean d + b = c of course]

#### [Kevin Buzzard (Apr 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948297):
Aah but I do remember that this might work in calc mode.

#### [Kevin Buzzard (Apr 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948305):
If your relation is tagged with trans then I think calc supports it

#### [Chris Hughes (Apr 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948370):
Can I mix equality and an congruences in calc?

#### [Kevin Buzzard (Apr 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948374):
I haven't ever seen this done

#### [Kevin Buzzard (Apr 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948382):
I think that either in the reference manual or in TPIL they are pretty formal about what you can do with calc

#### [Kevin Buzzard (Apr 11 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948467):
https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html#calculational-proofs

#### [Kevin Buzzard (Apr 11 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948471):
searching TPIL for calc doesn't find that

#### [Kevin Buzzard (Apr 11 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948475):
so I always look at https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/calc.md

#### [Kevin Buzzard (Apr 11 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948494):
and indeed there is an example with different operators, = and < and <=

#### [Patrick Massot (Apr 11 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948495):
```quote
searching TPIL for calc doesn't find that
```
It does actually, but you don't recognize it

#### [Patrick Massot (Apr 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948549):
3rd result

#### [Patrick Massot (Apr 11 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948575):
I know this because I filled  a Sphinx bug report before understanding this :flushed:

#### [Kevin Buzzard (Apr 11 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948619):
Oh! So "It's somewhere in Chapter 4" is the best I get?

#### [Patrick Massot (Apr 11 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948622):
yes

#### [Kevin Buzzard (Apr 11 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948624):
"PS here's the first occurrence of the string Calc"

#### [Kevin Buzzard (Apr 11 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948630):
"feel free to look and see if there are any others"

#### [Patrick Massot (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948643):
Web pages of TPIL are too big

#### [Patrick Massot (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948645):
from this point of view

#### [Kevin Buzzard (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948653):
That's one interpretation

#### [Kevin Buzzard (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948657):
Another is "search is crap"

#### [Kevin Buzzard (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948662):
I know we've all been spoilt by Google...

#### [Patrick Massot (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948720):
google would show you the same

#### [Kevin Buzzard (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948722):
or maybe section 4.3 should be tagged calc

#### [Kevin Buzzard (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948723):
and the search should prioritise tags

#### [Patrick Massot (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948726):
one hit for this page, and not all occurences on the search result page

#### [Kevin Buzzard (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948728):
is that possible in Sphinx?

#### [Kevin Buzzard (Apr 11 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948737):
Google might have a better idea about moving the "right" answer to #1 in the list...

#### [Chris Hughes (Apr 11 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948751):
```quote
Can I mix equality and an congruences in calc?
```
I tried it and you can.

#### [Patrick Massot (Apr 11 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948888):
Go to google and typein search bar: `site:https://leanprover.github.io/theorem_proving_in_lean/ calc`

#### [Patrick Massot (Apr 11 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948904):
Google is smarter than Sphynx

#### [Kevin Buzzard (Apr 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948916):
```quote
Can I mix equality and an congruences in calc?
```
`@[trans] protected theorem trans : a ≡ b [MOD n] → b ≡ c [MOD n] → a ≡ c [MOD n] := eq.trans
`

#### [Kevin Buzzard (Apr 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948919):
and lo and behold

#### [Kevin Buzzard (Apr 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948923):
```lean
import data.nat.modeq
variables (a b c d m : ℕ)

example (H1 : a ≡ b [MOD m]) (H2 : b = c) (H3 : c ≡ d [MOD m]) : a ≡ d [MOD m] :=
calc a ≡ b [MOD m] : H1
... = c : H2
... ≡ d [MOD m] : H3 
```

#### [Kevin Buzzard (Apr 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948977):
Google is smarter than everything :-/

#### [Chris Hughes (Apr 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948981):
what if I have two relations that are "co transitive" in the same sense that `le` and `lt` are. Can I make them work with calc?

#### [Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948986):
Right, e.g. a congruence mod 8 might imply a congruence mod 4

#### [Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949001):
I have no idea how Lean is doing the < and <= thing

#### [Patrick Massot (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949002):
calc knowing about that would be pretty cool

#### [Chris Hughes (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949003):
I thought that was a useless question, but obviously not.

#### [Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949008):
I know from experience that it will let you prove `a < d` by writing `a <= b < c <= d`

#### [Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949012):
so it knows `lt_of_le_of_lt`

#### [Patrick Massot (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949014):
yes, this is already really cool

#### [Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949018):
but it wouldn't surprise me if this were hard wired in somehow

#### [Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949020):
as a common use case

#### [Patrick Massot (Apr 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949055):
but I suspect this special case is hard-wired

#### [Chris Hughes (Apr 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949064):
`lt_of_lt_of_le` is tagged with trans. So it might just be a case of doing that.

#### [Kevin Buzzard (Apr 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949138):
Oh well spotted!

#### [Patrick Massot (Apr 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949150):
indeed

#### [Chris Hughes (Apr 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949181):
```lean
def r : ℕ → ℕ → Prop := sorry
def s : ℕ → ℕ → Prop := sorry

local infix `r'`:50 := r
local infix `s'`:50 := s

@[trans] lemma r.trans {a b c : ℕ} : r a b → r b c → r a c := sorry
@[trans] lemma rs.trans {a b c : ℕ} : r a b → s b c → r a c := sorry

@[trans] lemma rs.trans1 {a b c : ℕ} (h₁ : r a b) (h₂ : s b c) : r a c := calc
  a r' b : h₁ 
  ... s' c : h₂ 
```

#### [Chris Hughes (Apr 11 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949227):
That pasted from VScode without any extra spaces.

#### [Patrick Massot (Apr 11 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949231):
:hushed:

#### [Kevin Buzzard (Apr 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949234):
```lean
import data.nat.modeq
variables (a b c d m : ℕ)

@[trans] theorem helpful (a b c : ℕ) : a ≡ b [MOD 8] → b ≡ c [MOD 16] → a ≡ c [MOD 4] := sorry
example (H1 : a ≡ b [MOD 8]) (H2 : b = c) (H3 : c ≡ d [MOD 16]) : a ≡ d [MOD 4] :=
calc a ≡ b [MOD 8] : H1
... = c : H2
... ≡ d [MOD 16] : H3 

```

#### [Kevin Buzzard (Apr 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949241):
(deleted)

#### [Kevin Buzzard (Apr 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949244):
so did that

#### [Kevin Buzzard (Apr 11 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949257):
So it's really not hard coded in, there is some dark art with trans tags

#### [Patrick Massot (Apr 11 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949301):
Let's keep that in Lean 4

#### [Kevin Buzzard (Apr 11 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949304):
Conclusion in my example must be a = c mod 8 after second line

#### [Kevin Buzzard (Apr 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949314):
it uses this:

#### [Kevin Buzzard (Apr 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949316):
`#check trans_rel_left -- ∀ (r : ?M_1 → ?M_1 → Prop), r ?M_2 ?M_3 → ?M_3 = ?M_4 → r ?M_2 ?M_4
`

#### [Kevin Buzzard (Apr 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949323):
(I know because some messing around gave me some explicit error messages)

#### [Kevin Buzzard (Apr 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949327):
and then it uses my trans-tagged theorem for 3rd line

#### [Patrick Massot (Apr 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949380):
To the `docs/extras/calc`!

#### [Kevin Buzzard (Apr 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949384):
Yes, this deserves to be better known

#### [Kevin Buzzard (Apr 11 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949399):
I mean it's mentioned in TPIL but somehow it hadn't dawned on me how far you could push this

#### [Chris Hughes (Apr 11 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949401):
So now I know the point of `@[trans]` and `@[refl]` but I'm still not sure why you would tag something `@[symm]`

#### [Kevin Buzzard (Apr 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949503):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp.20is.20amazing

#### [Kevin Buzzard (Apr 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949509):
Gabriel's comment is in that thread

#### [Kevin Buzzard (Apr 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949511):
but I don't know any longer if it was about simp

#### [Kevin Buzzard (Apr 11 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949557):
If you tag something symm then there's some tactic called symmetry which will work ;-)

#### [Patrick Massot (Apr 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949669):
We need to formalize something using this calc power

#### [Patrick Massot (Apr 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949671):
What about some version of Hensel's lemma?

#### [Patrick Massot (Apr 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949678):
There should be chains of congruence modulo different stuff there

#### [Patrick Massot (Apr 11 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949719):
And it may even be useful for perfectoids, who knows?

#### [Kevin Buzzard (Apr 11 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949725):
`theorem X (a b m : ℕ) (H : a ≡ b [MOD m]) : b ≡ a [MOD m] := by symmetry;assumption`

#### [Chris Hughes (Apr 11 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949738):
`theorem X (a b m : ℕ) (H : a ≡ b [MOD m]) : b ≡ a [MOD m] := H.symm`

#### [Kevin Buzzard (Apr 11 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949739):
symmetry tactic replaces a hypothesis with another one if the fact that one implies the other is marked with symm

#### [Chris Hughes (Apr 11 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949789):
I know what it does, but it seems fairly useless.

#### [Kevin Buzzard (Apr 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949806):
Simon's cool use of transivity is above, and refl is used everywhere, but who knows what symmetry is for :-)

#### [Chris Hughes (Apr 11 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949874):
```quote
Simon's cool use of transivity is above, and refl is used everywhere, but who knows what symmetry is for :-)
```
What's Simon's cool use of transitivity?

#### [Kevin Buzzard (Apr 11 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124950966):
At the start of this thread

#### [Kevin Buzzard (Apr 12 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953029):
```quote
To the `docs/extras/calc`!
```
https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/calc.md

#### [Chris Hughes (Apr 12 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953112):
Can I use calc if I haven't defined an infix for my relation?

#### [Kevin Buzzard (Apr 12 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953180):
I don't know!

#### [Kevin Buzzard (Apr 12 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953181):
As you can see I defined infixes for mine.

#### [Kevin Buzzard (Apr 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953284):
@**Mario Carneiro** I wrote some calc docs (see link above) extending what is written in TPIL, together with some notes for things I struggled with myself after reading TPIL (e.g. I would sometimes get into a real mess with some syntax error or proof error manifesting itself as a red squiggle under a random `...`). Three questions:

#### [Kevin Buzzard (Apr 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953288):
1) Shall I PR to mathlib?

#### [Kevin Buzzard (Apr 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953293):
2) Chris asks if `calc` can be used with operators that aren't infix

#### [Kevin Buzzard (Apr 12 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953362):
3) I made some guesses as to how calc works. In particular I note that `trans_rel_right` and `trans_rel_left` are not tagged `[trans]`. Are these special cases which are tried first?

#### [Kevin Buzzard (Apr 12 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953417):
And an idle question -- would it be possible to break `calc` by proving e.g. `a < b -> b < c -> a <= c` and tagging with `[trans]`?

#### [Kevin Buzzard (Apr 12 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953555):
And @**Patrick Massot** After Mario accepted my last mathlib PRs I just nuked the entire repo and forked it again (do you remember I had a bad commit history because I never branched?). Now I have a branch with my WIPs. I know I can google for how to do this but I'm sure you will know instantly -- what is the best way to just PR the calc.md file? Sorry to bother you.

#### [Patrick Massot (Apr 12 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971220):
Since you have only one file to PR and don't care about keeping the history of this file, here the simplest route: copy that calc.md somewhere else (say /home/kevin/), then, inside mathlib,
```
git checkout master
git checkout -b docs-calc
cp /home/kevin/calc.md docs/extras/
```
then edit `docs/extras.md` to add a link to `docs/extra/calc.md`
```
git add docs/extras.md docs/extra/calc.md
git commit
git push 
```
The last command will complain you should explicitly say to create an upstream branch. Copy-paste the suggested command (I never remember the syntax since git always helps me here).

#### [Patrick Massot (Apr 12 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971277):
I forgot: don't forget to make sure your master is in sync with Mario's before `git check-out -b docs-calc`

#### [Patrick Massot (Apr 12 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971317):
assuming you followed conventional names, that would mean `git pull upstream master` after `git checkout master`

#### [Mario Carneiro (Apr 12 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971318):
It's not a big problem if you PR off an old version of mathlib, since I usually rebase it on the current head when I merge the PR anyway

#### [Mario Carneiro (Apr 12 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971319):
unless there's a conflict of course

#### [Mario Carneiro (Apr 12 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971320):
but docs don't usually cause conflicts if they are new

#### [Patrick Massot (Apr 12 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971369):
sure

#### [Patrick Massot (Apr 12 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971371):
I'm only trying to explain good practice

#### [Mario Carneiro (Apr 12 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971558):
I agree with everything you said.

I would add that if you intend to PR some addition, you should write it "in place", i.e. with the file located in mathlib where you want it to be, by first checking out `master` then checking out a new branch (i.e. the first two lines of Patrick's script), then making any modifications there.  Then any commits you make will branch from master nicely. If you need to set the work aside, you can just commit what you have to the branch and move to the current master or somewhere else, and come back to your PR when you are ready to resume work with `git checkout my-pr`.

#### [Patrick Massot (Apr 12 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124972034):
No -b in your last sentence

#### [Patrick Massot (Apr 12 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124972076):
Otherwise of course this is the correct way. I was explaining how to fix the mess.

#### [Mario Carneiro (Apr 12 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124972188):
oops, typo (copy-o?)

#### [Kevin Buzzard (Apr 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124990989):
OK done. Thanks both for the advice. Mario -- it's a bit of a WIP because I guessed how the transitivity worked in calc mode. First I guessed that Lean went from `A op1 B op2 C op3 D` to `A op4 D` via "reading from left to right", i.e. first attempting to figure out how `A op1 B op2 C` can become `A op5 C` and then merging this with `C op3 D` (i.e. I don't know if it does anything clever like trying to merge two random consecutive theorems in the middle), and secondly I guessed that when trying to merge two ops to become another one it first uses rw if one is `=` and then tries lemmas tagged `trans` if neither op is `=`. These are just plain guesses.

#### [Chris Hughes (Apr 12 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124992197):
I did some testing and I don't think it tries to do anything clever with changing the order. `L2` doesn't work below, but the rest do. You can also state that three relations are transitive together.
```lean
def r : ℕ → ℕ → Prop := sorry
def s : ℕ → ℕ → Prop := sorry
def t : ℕ → ℕ → Prop := sorry

local infix `r'`:50 := r
local infix `s'`:50 := s
local infix `t'`:50 := t
variables {a b c d : ℕ}

@[trans] lemma rrr.trans {a b c : ℕ} : r a b → r b c → r a c := sorry
@[trans] lemma srr.trans {a b c : ℕ} : s a b → r b c → r a c := sorry
@[trans] lemma sts.trans {a b c : ℕ} : s a b → t b c → s a c := sorry
@[trans] lemma rss.trans {a b c : ℕ} : r a b → s b c → r a c := sorry
@[trans] lemma trs.trans {a b c : ℕ} : t a b → r b c → s a c := sorry

lemma L1 (h₁ : s a b) (h₂ : t b c) (h₃ : r c d) : r a d :=
calc a s' b : h₁
   ... t' c : h₂
   ... r' d : h₃ 

lemma L2 (h₁ : r a b) (h₂ : s b c) (h₃ : t c d) : r a d :=
calc a r' b : h₁
   ... s' c : h₂
   ... t' d : h₃ 

lemma L2' (h₁ : r a b) (h₂ : s b c) (h₃ : t c d) : r a d := 
rss.trans h₁ (sts.trans h₂ h₃)

lemma L3 {a b c : ℕ} (h₁ : t a b) (h₂ : r b c) : s a c :=
calc a t' b : h₁
   ... r' c : h₂
```

#### [Kevin Buzzard (Apr 12 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124993108):
Thanks for checking. That was one way of doing it. The other way is to read the source code, but I sort-of suspect (perhaps incorrectly) that it will be in C++ not Lean.

