---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36914howdoestacticringwork.html
---

## Stream: [general](index.html)
### Topic: [how does tactic.ring work?](36914howdoestacticringwork.html)

---


{% raw %}
#### [ Kevin Buzzard (Jun 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888870):
I have read through programming in Lean a couple of times and now wonder if it's time I started reading something else. I decided to read the ring tactic (not least because it failed to prove something relatively simple the last time I tried to use it and I'd rather fix it myself than pester Mario, not that I have any idea about how far I need to go before I am anywhere close to being able to fix it).

#### [ Kevin Buzzard (Jun 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888871):
Anyway, I started to read it:

#### [ Kevin Buzzard (Jun 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888874):
https://github.com/kbuzzard/mathlib/blob/tactic_doc/docs/ring_tactic.rst

#### [ Kevin Buzzard (Jun 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888882):
There are my comments on the first 30 or so lines, plus a long intro summarising programming in lean

#### [ Kevin Buzzard (Jun 11 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888901):
There's a link to programming in lean: https://leanprover.github.io/programming_in_lean/programming_in_lean.pdf

#### [ Kevin Buzzard (Jun 11 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888951):
Here's Patrick's secret gem: https://hanoifabs.files.wordpress.com/2018/05/slides.pdf (thanks Johannes)

#### [ Kevin Buzzard (Jun 11 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888964):
and that is pretty much every online resource for Lean tactics. Here's the file I want to understand:

#### [ Kevin Buzzard (Jun 11 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888974):
https://github.com/leanprover/mathlib/blob/master/tactic/ring.lean

#### [ Kevin Buzzard (Jun 11 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888989):
if anyone wants to help me understand it, they're welcome to edit the rst file. Note: I wrote `ring_ractic.rst` in sphinx not markdown. It's still human-readable and pretty easy to pick up.

#### [ Johan Commelin (Jun 11 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127893407):
Typo: "especially if one does it within Lean (thus gaining the ability to hover over or click on functions and see their type, definition and so on)." <-- you mean VScode instead of Lean, right?
Another typo: "Note that evem though" <-- s/evem/even/

#### [ Kevin Buzzard (Jun 11 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127896619):
Thanks. I had a look through all of tactic.ring and really it doesn't look too bad. I'm currently reading http://www.cs.ru.nl/~freek/courses/tt-2014/read/10.1.1.61.3041.pdf Assia's take on the matter (which I think was Mario's source for his code)

#### [ Kevin Buzzard (Jun 11 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127907285):
in fact I know it was Mario's source for the code because I've just noticed that it says this in the comments at the top.

#### [ Kevin Buzzard (Jun 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945351):
```lean
import tactic.ring 
variables (R : Type) [comm_ring R]

example (a b : R) : 
  a * (b * b) + (b * (a * a) + (b * (b * b) + (a * (2 * a * b) + b * (2 * a * b)))) =
  b * (b * b) + (3 * a * (b * b) + 3 * (a * a) * b) :=
begin
  ring,
  -- goal now (b * a + (2 * b * a + 3 * b ^ 2)) * a + b ^ 3 = (3 * b * a + 3 * b ^ 2) * a + b ^ 3
  simp,
  -- goal now (b * a + (2 * b * a + 3 * b ^ 2)) * a = (3 * b * a + 3 * b ^ 2) * a
  ring -- works
end 
```

#### [ Kevin Buzzard (Jun 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945353):
```
elaboration: tactic execution took 2.23s
num. allocated objects:  8522
num. allocated closures: 2163
 2229ms   100.0%   scope_trace
 2229ms   100.0%   tactic.istep._lambda_1
 2229ms   100.0%   tactic.istep
 2229ms   100.0%   tactic.step
 2229ms   100.0%   _interaction._lambda_2
 1987ms    89.1%   interaction_monad_orelse
 1929ms    86.5%   tactic.ring.eval
 1156ms    51.9%   tactic.interactive.ring1
 1156ms    51.9%   tactic.interactive.ring._lambda_1
 1156ms    51.9%   tactic.interactive.ring
 1057ms    47.4%   tactic.ring.eval_mul
```

#### [ Kevin Buzzard (Jun 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945354):
etc etc

#### [ Kevin Buzzard (Jun 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945358):
This tactic doesn't quite work yet as far as I can see.

#### [ Kevin Buzzard (Jun 12 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945366):
(noticable pause in `ring` whilst it's failing to prove it the first time)

#### [ Kevin Buzzard (Jun 12 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945407):
But I want to fix it.

#### [ Kevin Buzzard (Jun 12 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945415):
I re-read the "rings done right" paper and I understood _much_ more of it this time around.

#### [ Kevin Buzzard (Jun 12 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945427):
One insight which dawned on me is that there are two completely different issues involved with writing a ring tactic. Maybe everyone else is aware of this.

#### [ Kevin Buzzard (Jun 12 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945430):
Let me explain my understanding of what the ring tactic does.

#### [ Kevin Buzzard (Jun 12 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945444):
Let's say `d : int` and we want to prove `d^2 + 2*d + 1 = (d+1)^2`

#### [ Kevin Buzzard (Jun 12 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945497):
If we want to prove this using `ring` then we are saying "this is not true because of something specific to int, this is a general fact about rings"

#### [ Kevin Buzzard (Jun 12 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945501):
So what we actually want to do is to prove that $$X^2+2X+1=(X+1)^2$$ in $$\mathbb{Z}[X]$$

#### [ Kevin Buzzard (Jun 12 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945513):
and then deduce our goal by specialising to $$X=d$$

#### [ Kevin Buzzard (Jun 12 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945521):
This makes it clear what we have to do here.

#### [ Kevin Buzzard (Jun 12 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945565):
First we need to build a new type in Lean corresponding to polynomials in one variable

#### [ Kevin Buzzard (Jun 12 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945572):
or more generally, if we want to prove stuff like `(a+b)^2=a^2+2*a*b+b^2` for ints a,b

#### [ Kevin Buzzard (Jun 12 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945576):
we will need polynomials in a finite set of variables.

#### [ Kevin Buzzard (Jun 12 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945580):
Of course Lean has these.

#### [ Kevin Buzzard (Jun 12 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945588):
Once we have this new type, we need to prove an "evaluation theorem", saying that if $$f(X)=g(X)$$ in our polynomial ring

#### [ Kevin Buzzard (Jun 12 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945589):
then $$f(d)=g(d)$$ in int

#### [ Kevin Buzzard (Jun 12 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945634):
Along the way it would be natural to prove things like $$f(d)+g(d)=(f+g)(d)$$ and so on

#### [ Kevin Buzzard (Jun 12 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945646):
So we define our new polynomial type, define evaluation, prove nice properties about the evaluation map

#### [ Kevin Buzzard (Jun 12 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945648):
and now all that's left is the following problem:

#### [ Kevin Buzzard (Jun 12 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945650):
given `d^2+2*d+1` with `d : int`

#### [ Kevin Buzzard (Jun 12 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945653):
we need to manufacture `X^2+2*X+1` in our polynomial ring type.

#### [ Kevin Buzzard (Jun 12 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945714):
And for this we really need to take apart `d^2+2*d+1` and see how it is built from `d` and stuff that has analogues in the polynomial ring.

#### [ Kevin Buzzard (Jun 12 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945719):
(+,^,2,1)

#### [ Kevin Buzzard (Jun 12 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945734):
and I think that it's at this point that the non-tactic-user gets stuck.

#### [ Kevin Buzzard (Jun 12 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945904):
@**Simon Hudon** Assume Lean has a working polynomial ring type `ZX` (there are some kicking around, but perhaps none in mathlib) representing polynomials with integer coefficients in one variable `X`.  Am I right in thinking that it doesn't even make sense to ask for a function (in Lean's sense) which sends `d^2+2*d+1` to `X^2+2*X+1` where `d : int` is some variable? I can't even imagine what the domain of such a function would be. On the other hand, would I be able to write a tactic which took the expression `d^2+2*d+1` as an input and spat out `X^2+2*X+1`?

#### [ Kevin Buzzard (Jun 12 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945920):
Or is life not even that easy?

#### [ Scott Morrison (Jun 12 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127947136):
certainly given `d^2+2*d+1` as an `expr` (and let's say `d` is also given, as an `expr`), in meta land we can construct `X^2+2*X+1`.

#### [ Scott Morrison (Jun 12 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127947142):
(Mario's implementation does clever things, including a representation of sparse polynomials, but if you just want the stupid version I could probably manage that function.)

#### [ Simon Hudon (Jun 12 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127950108):
Is this simply renaming variables in the goal?

#### [ Scott Morrison (Jun 12 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127950557):
Sorry, the example wasn't very helpful: I just meant, determine if some expression is in fact a polynomial in some other expr, and if so, present it as such in some form (list of coefficients, map of coefficients, etc).

#### [ Kevin Buzzard (Jun 12 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951731):
```quote
Is this simply renaming variables in the goal?
```
@**Simon Hudon** No I think it's more. X is a genuine polynomial variable, we have a type `ZX` with an inclusion from int into ZX and also some element `X : ZX` which is not in the image of `int`, it's an abstract polynomial variable

#### [ Kevin Buzzard (Jun 12 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951740):
@**Scott Morrison** do we _have_ to do this in meta-land?

#### [ Simon Hudon (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951793):
ah! i see. So a kind of parser.

#### [ Kevin Buzzard (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951794):
I can see that Mario's implementation uses "Horner form" of a polynomial, so sparse polys are handled better.

#### [ Kevin Buzzard (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951798):
Yes, I was interested in building the stupid version of tactic.ring

#### [ Simon Hudon (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951805):
Yes, I think it has to be in meta because you need access to the `expr` syntax tree

#### [ Kevin Buzzard (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951812):
What I see in Mario's file seems to me to be a construction of an abstract polynomial ring but completely in meta-land

#### [ Kevin Buzzard (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951818):
Here is a concrete question.

#### [ Kevin Buzzard (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951823):
Would it be possible to just define the polynomial ring Z[X] in "normal" Lean

#### [ Kevin Buzzard (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951830):
e.g. in a non-efficient way, using lists for coefficients

#### [ Simon Hudon (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951837):
I believe so

#### [ Kevin Buzzard (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951841):
and then write a much simpler tactic than `tactic/ring.lean`

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951893):
which can prove statements of the form "forall d : int, (d+1)^3=d^3+3d^2+3d+1"

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951901):
by temporarily dipping into meta-land to construct the polynomials (X+1)^3 and X^3+3X^2+3X+1

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951904):
and then checking that they're equal in Z[X]

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951907):
and then evaluating at d

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951914):
and deducing the result?

#### [ Kevin Buzzard (Jun 12 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951927):
Or is it an essential part of the tactic.ring tactic that one builds some version of Z[X] in meta-land?

#### [ Kevin Buzzard (Jun 12 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951988):
It seems to me that Mario writes `horner` in normal-land and proves some lemmas about it in normal-land

#### [ Kevin Buzzard (Jun 12 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952002):
but the key facts are things like `eval_add`, which is meta

#### [ Kevin Buzzard (Jun 12 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952175):
`eval_add` seems to be some sort of theorem of the form "if this expr represents f and this expr represents g, then I will return an expr plus a proof that it is the evaluation of f plus the evaluation of g"

#### [ Kevin Buzzard (Jun 12 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952239):
I was wondering whether one could instead use a non-expr version

#### [ Simon Hudon (Jun 12 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952242):
Because `expr` is in meta land, you can't do any of that stuff in non-meta land

#### [ Kevin Buzzard (Jun 12 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952247):
right

#### [ Kevin Buzzard (Jun 12 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952253):
but if I had a tactic which took d^2+2*d+1

#### [ Kevin Buzzard (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952259):
and returned X^2+2*X+1

#### [ Simon Hudon (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952261):
I see ok yes that's possible

#### [ Simon Hudon (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952267):
That's called a proof by reflection

#### [ Kevin Buzzard (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952270):
plus a proof that X^2+X+1 evaluated at d was d^2+2*d+1

#### [ Kevin Buzzard (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952294):
then it seems to me that there's a chance that I can prove d^2+2*d+1=(d+1)^2 using this tactic

#### [ Kevin Buzzard (Jun 12 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952373):
because I feed in both sides to the tactic

#### [ Kevin Buzzard (Jun 12 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952376):
prove they're equal in `ZX`

#### [ Kevin Buzzard (Jun 12 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952382):
and deduce that their valuations are equal

#### [ Kevin Buzzard (Jun 12 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952390):
I am trying to get as much of the proof out of meta-land as I can

#### [ Reid Barton (Jun 12 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952404):
Regarding lands, have you looked at the slides on metaprogramming https://hanoifabs.files.wordpress.com/2018/05/slides.pdf?

#### [ Reid Barton (Jun 12 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952408):
In particular page 4

#### [ Kevin Buzzard (Jun 12 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952433):
This is part of the reason I'm thinking about this now

#### [ Kevin Buzzard (Jun 12 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952485):
I have looked through all of tactic/ring.lean and all of a sudden it doesn't look as intimidating as it used ti

#### [ Kevin Buzzard (Jun 12 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952486):
to

#### [ Kevin Buzzard (Jun 12 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952586):
https://github.com/kbuzzard/mathlib/blob/ring_tactic_comments/tactic/ring.lean

#### [ Reid Barton (Jun 12 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952590):
If you don't need access to meta-land features like general recursion or `expr` then you can stay in normal-land; and surely the theory of $$\mathbb{Z}[X]$$ doesn't need these things. On the other hand, you may want to avoid using noncomputable things if you want your tactic to, for example, be able to decide whether two polynomials in $$\mathbb{Z}[X]$$ are equal so that it can decide whether to succeed or fail.

#### [ Kevin Buzzard (Jun 12 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952593):
I am trying to write a comment about every definition and theorem in that link

#### [ Kevin Buzzard (Jun 12 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952613):
So one can certainly make Z[X], indeed it's been done several times although I don't think it's in mathlib yet

#### [ Kevin Buzzard (Jun 12 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952618):
The problem is the function sending d^2+2d+1 to X^2+2X+1

#### [ Reid Barton (Jun 12 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952671):
Right, so I guess the approach used here by `ring` is to represent a variable (which is basically something the tactic can't break down into further ring operations) by its `expr`

#### [ Kevin Buzzard (Jun 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952678):
right

#### [ Reid Barton (Jun 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952679):
Here the variable is simply `d`, but it could have been more complicated, e.g. `sin t`

#### [ Kevin Buzzard (Jun 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952681):
right

#### [ Kevin Buzzard (Jun 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952683):
or there could be several variables

#### [ Reid Barton (Jun 12 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952755):
So that must be why the `destruct_ty` thing is in `meta`, though if you wanted it to be in normal-land, you could probably just parameterize it on the expression type.

#### [ Reid Barton (Jun 12 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952758):
BTW, `_ty` probably just stands for "type"

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952829):
So completely independent of the ring tactic

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952830):
there is this horner thing

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952832):
and what seems to be going on there

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952834):
is that (and this is Assia's insight, or her joint insight with her co-author)

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952844):
storing polynomials as lists of coefficients might suck

#### [ Kevin Buzzard (Jun 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952888):
especially if you want to work out x^100 * x^100 without doing 10000 computations

#### [ Kevin Buzzard (Jun 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952898):
so they store e.g. x^100+3x^2+7 as (1*x^98+3)*x^2+7

#### [ Kevin Buzzard (Jun 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952903):
iterating the "x maps to a*x^n+b" map

#### [ Kevin Buzzard (Jun 12 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952918):
and so this is some sort of normal form for polynomials

#### [ Kevin Buzzard (Jun 12 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952922):
which we could call "horner normal form"

#### [ Kevin Buzzard (Jun 12 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952925):
and if you store polynomials in this way then it's a PITA to add or multiply them

#### [ Kevin Buzzard (Jun 12 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952929):
but this is OK because somehow this isn't the bottleneck

#### [ Reid Barton (Jun 12 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952978):
I see, and `eval_add` is basically implementing addition of polynomials in this form, it looks like?

#### [ Kevin Buzzard (Jun 12 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952979):
So one could envisage writing a second ring tactic which (a) was far less efficient and (b) worked in some situations where Mario's doesn't (because Mario's is currently buggy)

#### [ Kevin Buzzard (Jun 12 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952984):
where you just use lists for coefficients

#### [ Kevin Buzzard (Jun 12 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953003):
and then the resulting tactic file would have this extra obfuscating layer of difficulty removed

#### [ Kevin Buzzard (Jun 12 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953012):
and this was what got me into wondering whether I could even just use one of the already-existing polynomial ring Lean implementations

#### [ Kevin Buzzard (Jun 12 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953016):
instead of making Z[X] in meta-land

#### [ Kevin Buzzard (Jun 12 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953098):
```quote
I see, and `eval_add` is basically implementing addition of polynomials in this form, it looks like?
```
Yes, it's perhaps doing something clever like not just implementing addition, it's also collecting the proofs that addition commutes with evaluation, but the five lemmas before `eval_add` are precisely the five lemmas you need to add polynomials in "Horner form"

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953111):
You add `ax^n+b` and `a'x^n'+b'`

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953152):
where a and a' are allowed to be polynomials in horner form

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953158):
and you have to do the three cases n<n', n=n', n>n'

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953162):
and then also you have to add `ax^n+b` to c where c is a constant

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953163):
both ways around

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953168):
and there's some implicit inductive type horner_form

#### [ Kevin Buzzard (Jun 12 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953182):
which is defined by: a constant is in horner_form, and if a is in horner_form then so is a*x^n+b

#### [ Kevin Buzzard (Jun 12 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953187):
and then every polynomial has a canonical horner form

#### [ Kevin Buzzard (Jun 12 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953198):
and also perhaps some non-canonical ones

#### [ Kevin Buzzard (Jun 12 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953343):
I haven't got down as far as `normalize` but this might be the function which puts something in horner form into its normalised state (which you need because you need an algorithm for figuring out when two polynomials are equal)

#### [ Reid Barton (Jun 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953437):
```quote
and this was what got me into wondering whether I could even just use one of the already-existing polynomial ring Lean implementations
```
I don't see why not. Probably you can even use the one in `linear_algebra.multivariate_polynomial`

#### [ Kevin Buzzard (Jun 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953586):
You understand that I am not looking for some sort of uber-efficient ring tactic, like the one Mario wrote. I am trying to see in some sense what the minimal amount of work would be, if I wanted to write a more inefficient ring tactic of my own

#### [ Kevin Buzzard (Jun 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953590):
and the more I can get out of meta-land the better

#### [ Kevin Buzzard (Jun 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953599):
Even for just equations involving one unknown, I would be interested

#### [ Kevin Buzzard (Jun 12 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953672):
not least because `example (d : ℕ) : d^2+2*d+1=(d+1)^2 := by ring ` currently fails and rather than pestering Mario I thought it would be an interesting exercise to try and work out why.

#### [ Reid Barton (Jun 12 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953697):
Yes, I think a `ring` tactic optimized for simplicity would be valuable as a demonstration of how to write similar tactics, as well.

#### [ Kevin Buzzard (Jun 12 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954108):
Well maybe that's where this thread is going.

#### [ Mario Carneiro (Jun 12 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954256):
I'm not sure you can actually save that much work with a dumber `ring` tactic

#### [ Mario Carneiro (Jun 12 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954307):
Probably using dense polynomial representation is a bit easier, but I don't think proof by reflection is easier (although more of it can be verified)

#### [ Mario Carneiro (Jun 12 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954313):
but precisely because more of it is verified, there is more work to do

#### [ Mario Carneiro (Jun 12 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954331):
If `expr` was not meta, almost all of the ring tactic could be non-meta

#### [ Simon Hudon (Jun 12 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954389):
Do you know if there's any plan to make `expr` non-meta?

#### [ Mario Carneiro (Jun 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954397):
I have not investigated the `ring` bug, but one way to find out what is happening is to insert type checks in `eval_add` and such

#### [ Reid Barton (Jun 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954407):
By "simple", I really mean "easy to understand"

#### [ Reid Barton (Jun 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954409):
not necessarily short

#### [ Mario Carneiro (Jun 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954412):
There is no plan to make `expr` non-meta, and in fact I attempted such a plan and was rebuffed several months ago

#### [ Mario Carneiro (Jun 12 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954463):
The likely alternative is to have a mirror copy of `expr` that is non-meta

#### [ Mario Carneiro (Jun 12 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954469):
which would have to avoid certain meta things like macros

#### [ Kevin Buzzard (Jun 12 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954787):
```quote
I'm not sure you can actually save that much work with a dumber `ring` tactic
```
Yes, as Reid says, I'm not worried about work, I'm attempting to understand tactics in a way other than "read Programming In Lean again".

#### [ Kevin Buzzard (Jun 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954848):
The only other way I can think of is "read some tactic code and see if you can understand it, and see what questions arise because of it"

#### [ Kevin Buzzard (Jun 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954852):
and that's why I find myself in this thread

#### [ Kevin Buzzard (Jun 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954862):
One question: which is best? Documenting ring.lean like this https://github.com/kbuzzard/mathlib/blob/ring_tactic_comments/tactic/ring.lean

#### [ Kevin Buzzard (Jun 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954873):
or writing a stand-alone file with comments like this https://github.com/kbuzzard/mathlib/blob/tactic_doc/docs/ring_tactic.rst

#### [ Kevin Buzzard (Jun 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954883):
I currently find myself doing both

#### [ Kevin Buzzard (Jun 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954892):
As long as I get to the bottom using one method, I am sure I will have learnt a lot

#### [ Kevin Buzzard (Jun 12 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954939):
Currently the "adding comments to ring.lean" approach is winning

#### [ Kevin Buzzard (Jun 12 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954988):
but the waffle above about writing a simpler version -- which to be honest could I think turn into a great tutorial on how to write tactics, if we implement polynomials in one variable using some dumb list method or, even better, perhaps using some already-implemented method

#### [ Kevin Buzzard (Jun 12 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127955058):
Maybe that's the goal of this thread. To write an  as-stupid-as-possible ring tactic which attempts to have as little in meta-land as possible, and then stick it up on my blog as some sort of tactic tutorial as an alternative for people to read

#### [ Kevin Buzzard (Jun 12 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127955071):
Next term I'll be supervising a Masters project on how to write tactics so I'd better get my act together and learn it myself

#### [ Kevin Buzzard (Jun 12 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127955085):
The student in question is currently doing an internship at INRIA learning how to do it in Coq so I'm hoping that they will learn quickly and then teach me

#### [ Mario Carneiro (Jun 12 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127957753):
Maybe this will help: There is an implicit inductive type `horner_form_expr` with the following definition:
```
meta inductive horner_form_expr : Type
| const : expr → horner_form_expr
| horner (a : horner_form_expr) (x : expr) (n : nat) (b : horner_form_expr) : horner_form_expr
```
The job of `eval_add` and the other definitions is to rewrite any `expr` into a `horner_form_expr`. However, since `horner_form_expr` can be represented as an `expr`, the actual inductive type is omitted to avoid the overhead of converting back and forth. Furthermore, there is a normal form requirement, that says that the `x` expression must be lex_lt less than any other expressions in `x` slots of the `b` subtree.

#### [ Mario Carneiro (Jun 12 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127957847):
`destruct` is effectively the `cases_on` for this inductive type

#### [ Kevin Buzzard (Jun 12 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959658):
Right -- I had basically figured this out. But you see, in some educational blog post about this stuff you could put this type in, and furthermore make it work in a more stupid way using lists of coefficients. What I am still not clear about is whethet you can get away with making it not meta (and hence get away with not actually writing it at all, because it's already written)

#### [ Kevin Buzzard (Jun 12 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959693):
Because you're in meta-land you can just not even define the type, you can `destruct` it _assuming_ that it's in this form, and if it's not then big deal, things have gone wrong, just return `none`

#### [ Mario Carneiro (Jun 12 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959786):
You can't make it non-meta and still retain the `x` payloads, which have to be kept as is as exprs

#### [ Kevin Buzzard (Jun 12 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959808):
My idea was to have a meta function sending d^2+2d+1 to X^2+2X+1

#### [ Mario Carneiro (Jun 12 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959809):
unless maybe you write them down somewhere else and only keep pointers to them in your non-meta data structure (i.e. indexes into a list of exprs)

#### [ Mario Carneiro (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959864):
which I guess is similar to your Z[X] suggestion

#### [ Kevin Buzzard (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959867):
The tactic would only work for goals with one unknown

#### [ Mario Carneiro (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959874):
but you have to remember these are multivariate polynomials

#### [ Kevin Buzzard (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959877):
I know yours are

#### [ Kevin Buzzard (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959881):
but I am suggesting writing a simplified version

#### [ Kevin Buzzard (Jun 12 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959895):
I want to isolate the "now here we have to write some meta stuff" and make it as small as possible

#### [ Mario Carneiro (Jun 12 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959898):
If you take `d` as an input, then there are lots of bad exprs now

#### [ Mario Carneiro (Jun 12 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959906):
In my approach, there aren't any bad exprs because anything it doesn't understand becomes a new atom

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959948):
I know your approach is better at getting things done

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959956):
I am happy to let both d and Z be inputs

#### [ Mario Carneiro (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959964):
but you want to have only one atom

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959966):
right

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959969):
and I want to store polynomials as lists

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959974):
these facts are not unrelated

#### [ Mario Carneiro (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959987):
what happens if I pass `d^2+x` to your function?

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960000):
my function will fail

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960005):
because my function is there to teach people how to write tactics

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960006):
not to actually be used in the wild

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960013):
I am writing code for a completely different reason to probably any code you ever wrote

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960015):
I am writing code to teach my students that tactics are not scary

#### [ Kevin Buzzard (Jun 12 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960060):
which is not the impression you get when reading PIL

#### [ Mario Carneiro (Jun 12 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960068):
Okay, let me think about this

#### [ Mario Carneiro (Jun 12 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960076):
In the mean time, the `ring` bug has been fixed.

#### [ Kevin Buzzard (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960078):
:D

#### [ Kevin Buzzard (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960086):
OK so forget this thread, main goal achieved ;-)

#### [ Mario Carneiro (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960091):
The problem was in `horner_add_horner_lt` (and `gt`). Suppose we are adding `(a1 * x^n1 + b1) + (a2 * x^n2 + b2)` where `n1 > n2`

#### [ Kevin Buzzard (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960097):
dammit I even looked at that function!

#### [ Mario Carneiro (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960099):
It's funny, the theorem is not wrong

#### [ Mario Carneiro (Jun 12 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960146):
but it doesn't normalize like it should

#### [ Kevin Buzzard (Jun 12 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960148):
in fact that's exactly the point I'm up to

#### [ Kevin Buzzard (Jun 12 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960156):
`/-- This non-meta theorem just says a₁x^n₁+b₁+a₂x^(n₁+k)+b₂=(a₂x^k+a₁)x^n₁+(b₁+b₂) -/`

#### [ Andrew Ashworth (Jun 12 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960189):
I think this is a great idea. It took me some time to understand reflection in Lean. Unfortunately, translating Chlipala's section on it (in CPDT) from Coq to Lean is quite difficult. So a "Lean-first" tutorial would be great.

#### [ Mario Carneiro (Jun 12 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960192):
The current implementation normalizes `b1 + b2 = b'`, calculates `k` such that `n2 + k = n1`, and then outputs the normal form `(a1 * x^k + a2) * x^n2 + b'`

#### [ Kevin Buzzard (Jun 12 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960249):
yeah (modulo the fact that the (1,2) notation is switched in this thread from the conventions used in the actual code)

#### [ Mario Carneiro (Jun 12 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960250):
However, `a1 * x^k + a2` is not necessarily in normal form

#### [ Kevin Buzzard (Jun 12 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960258):
because x might not be lt the monomials showing up in a1?

#### [ Mario Carneiro (Jun 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960276):
Yes. In particular, `x` might appear in `a2`

#### [ Kevin Buzzard (Jun 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960282):
or a1

#### [ Kevin Buzzard (Jun 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960285):
;-)

#### [ Mario Carneiro (Jun 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960288):
that's okay

#### [ Kevin Buzzard (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960331):
not when you switch it so your algebra is correct ;-)

#### [ Kevin Buzzard (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960352):
[you only did half the editing job]

#### [ Mario Carneiro (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960365):
the whole point of factorizing `a1 * x^k + a2` is that `a2` has no `x`'s and `a1` has all the high order terms

#### [ Kevin Buzzard (Jun 12 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960372):
a2 * x^k + a1

#### [ Kevin Buzzard (Jun 12 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960388):
I think this part of the thread is now beyond saving

#### [ Kevin Buzzard (Jun 12 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960396):
but I think we both know what the other is saying :-)

#### [ Mario Carneiro (Jun 12 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960460):
fixed

#### [ Mario Carneiro (Jun 12 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960468):
I actually noticed the problem in `gt`, but I was translating to the symmetric version and got confused

#### [ Mario Carneiro (Jun 12 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960525):
(in this thread, that's not the bug)

#### [ Kevin Buzzard (Jun 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960552):
[I posted my docstring for `lt`, but you are talking about `gt`, so now all is right with the world]

#### [ Kevin Buzzard (Jun 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960559):
Right, so let's focus on `gt`

#### [ Mario Carneiro (Jun 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960560):
the bug is that since both `a1` and `a2` can contain `x`, we have a separate subproblem now, to normalize `(a1 * x^k + 0) + a2 = a'` and then output `a' * x^n2+ b'`

#### [ Kevin Buzzard (Jun 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960566):
`/-- This non-meta theorem just says a₁x^(n₂+k)+b₁+a₂x^n₂+b₂=(a₁x^k+a₂)x^n₂+(b₁+b₂) -/`

#### [ Mario Carneiro (Jun 12 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960611):
so I did that and now it works

#### [ Mario Carneiro (Jun 12 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960615):
I'm compiling now, I'll post it soon

#### [ Kevin Buzzard (Jun 12 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960626):
I would have liked to find this bug

#### [ Kevin Buzzard (Jun 12 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960636):
Because you're in meta mode you don't have to be super-anal about making sure everything is in canonical form

#### [ Kevin Buzzard (Jun 12 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960648):
you just write procedural code which is supposed to do it

#### [ Kevin Buzzard (Jun 12 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960715):
@**Andrew Ashworth** I did the introductory compiler exercise in CPDT, in Lean, over the weekend.

#### [ Mario Carneiro (Jun 12 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960717):
I'll help you with a tutorial ring tactic later

#### [ Mario Carneiro (Jun 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960732):
But one thing to be careful about is if you do too much non-meta, you might actually end up writing a tactic that does proof by reflection which is a completely different method

#### [ Kevin Buzzard (Jun 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960757):
reflection is _different_? I thought that it was somehow some fundamental principle which was used everywhere?

#### [ Mario Carneiro (Jun 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960760):
`ring` is an example of how to write tactics that build proofs by induction, but it's hard to do that non-meta

#### [ Mario Carneiro (Jun 12 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960901):
One way to see the difference is in the proof: A tactic that does proofs by meta-induction produces proofs that get longer as the theorem gets harder to prove, but a proof by reflection is relatively short, with the generated proof being proportional to the *statement* in length

#### [ Mario Carneiro (Jun 12 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960916):
Proofs by reflection are characterized by a "heavy" `rfl` proof somewhere in the middle

#### [ Mario Carneiro (Jun 12 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960934):
`ring` produces no heavy steps, every single theorem applied exactly matches the type it should have

#### [ Mario Carneiro (Jun 12 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960981):
so the kernel never has to do any definitional reduction

#### [ Kevin Buzzard (Jun 12 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127961459):
This is all very instructive and quite different from the PIL stuff which, inevitably,  is skewed towards CS applications

#### [ Mario Carneiro (Jun 12 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127964820):
@**Kevin Buzzard** Here's a toy version of `ring` that works using computational reflection:
```
import tactic.basic data.num.lemmas

namespace ring_tac
open tactic

@[derive has_reflect]
inductive ring_expr : Type
| add : ring_expr → ring_expr → ring_expr
| mul : ring_expr → ring_expr → ring_expr
| const : znum → ring_expr
| X : ring_expr

meta def reflect_expr (X : expr) : expr → option ring_expr
| `(%%e₁ + %%e₂) := do
  p₁ ← reflect_expr e₁,
  p₂ ← reflect_expr e₂,
  return (ring_expr.add p₁ p₂)
| `(%%e₁ * %%e₂) := do
  p₁ ← reflect_expr e₁,
  p₂ ← reflect_expr e₂,
  return (ring_expr.mul p₁ p₂)
| e := if e = X then return ring_expr.X else
  do n ← expr.to_int e,
     return (ring_expr.const (znum.of_int' n))

def poly := list znum

def poly.add : poly → poly → poly := λ _ _, []
def poly.mul : poly → poly → poly := λ _ _, []
def poly.const : znum → poly := sorry
def poly.X : poly := sorry

def to_poly : ring_expr → poly
| (ring_expr.add e₁ e₂) := (to_poly e₁).add (to_poly e₂)
| (ring_expr.mul e₁ e₂) := (to_poly e₁).mul (to_poly e₂)
| (ring_expr.const z) := poly.const z
| ring_expr.X := poly.X

def poly.eval {α} [comm_ring α] (X : α) : poly → α
| [] := 0
| (n::l) := n + X * poly.eval l

@[simp] theorem poly.eval_add {α} [comm_ring α] (X : α) : ∀ p₁ p₂ : poly,
  (p₁.add p₂).eval X = p₁.eval X + p₂.eval X := sorry

@[simp] theorem poly.eval_mul {α} [comm_ring α] (X : α) : ∀ p₁ p₂ : poly,
  (p₁.mul p₂).eval X = p₁.eval X * p₂.eval X := sorry

@[simp] theorem poly.eval_const {α} [comm_ring α] (X : α) : ∀ n : znum,
  (poly.const n).eval X = n := sorry

@[simp] theorem poly.eval_X {α} [comm_ring α] (X : α) : poly.X.eval X = X := sorry

def ring_expr.eval {α} [comm_ring α] (X : α) : ring_expr → α
| (ring_expr.add e₁ e₂) := e₁.eval + e₂.eval
| (ring_expr.mul e₁ e₂) := e₁.eval * e₂.eval
| (ring_expr.const z) := z
| ring_expr.X := X

theorem to_poly_eval {α} [comm_ring α] (X : α) (e) : (to_poly e).eval X = e.eval X :=
by induction e; simp [to_poly, ring_expr.eval, *]

theorem main_thm {α} [comm_ring α] (X : α) (e₁ e₂) {x₁ x₂}
  (H : to_poly e₁ = to_poly e₂) (R1 : e₁.eval X = x₁) (R2 : e₂.eval X = x₂) : x₁ = x₂ :=
by rw [← R1, ← R2, ← to_poly_eval, H, to_poly_eval]

meta def ring_tac (X : pexpr) : tactic unit := do
  X ← to_expr X,
  `(%%x₁ = %%x₂) ← target,
  r₁ ← reflect_expr X x₁,
  r₂ ← reflect_expr X x₂,
  let e₁ : expr := reflect r₁,
  let e₂ : expr := reflect r₂,
  `[refine main_thm %%X %%e₁ %%e₂ rfl _ _],
  all_goals `[simp only [ring_expr.eval,
    znum.cast_pos, znum.cast_neg, znum.cast_zero',
    pos_num.cast_bit0, pos_num.cast_bit1,
    pos_num.cast_one']]

example (x : ℤ) : (x + 1) * (x + 1) = x*x+2*x+1 :=
by do ring_tac ```(x)

end ring_tac
```

#### [ Mario Carneiro (Jun 12 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127964879):
I have left the exercise of defining `poly.add`, `poly.mul`, `poly.const` and `poly.X`, and proving correctness of the functions in the `eval_*` theorems (all non-meta), to you.

#### [ Mario Carneiro (Jun 12 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127964910):
Here the "heavy `rfl`" step is the `rfl` proof in `main_thm`

#### [ Mario Carneiro (Jun 12 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127964970):
you will need the mathlib update that just appeared

#### [ Kevin Buzzard (Jun 12 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127971021):
wooah many thanks Mario!

#### [ Kevin Buzzard (Jun 12 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127972171):
`example (a b : int) : (a+b)^11=a^11 + 11*b*a^10 + 55*b^2*a^9 + 165*b^3*a^8 + 330*b^4*a^7 + 462*b^5*a^6 + 462*b^6*a^5 + 330*b^7*a^4 + 165*b^8*a^3 + 55*b^9*a^2 + 11*b^10*a + b^11:= by ring`

#### [ Kevin Buzzard (Jun 12 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127972173):
but 12 times out :-)

#### [ Kevin Buzzard (Jun 12 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127972177):
[this is of course the official ring, not the one above]

#### [ Kevin Buzzard (Jun 12 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127972228):
`example (a b : int) : (a+b)^12=a^12 + 12*b*a^11 + 66*b^2*a^10 + 220*b^3*a^9 + 495*b^4*a^8 + 792*b^5*a^7 + 924*b^6*a^6 + 792*b^7*a^5 + 495*b^8*a^4 + 220*b^9*a^3 + 66*b^10*a^2 + 12*b^11*a + b^12:= by ring -- deterministic timeout`

#### [ Johan Commelin (Jun 12 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127973037):
@**Kevin Buzzard** So you need to teach `ring` about Chris's binomial theorem!

#### [ Kevin Buzzard (Jun 13 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127977028):
Well, I'm not sure I would use Lean to check the binomial theorem for n=12 :-)

#### [ Kevin Buzzard (Jun 13 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127977076):
Ironically I fired up pari-gp and computed (a+b)^12 in a gazillionth of a second and then cut and pasted the output into Lean in order to see if it could do something which I already had a much better tool for.

#### [ Kevin Buzzard (Jun 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979328):
```lean
import tactic.basic data.num.lemmas analysis.real

namespace ring_tac
open tactic

-- why this line?
@[derive has_reflect]
inductive ring_expr : Type
| add : ring_expr → ring_expr → ring_expr
| mul : ring_expr → ring_expr → ring_expr
| const : znum → ring_expr
| X : ring_expr

meta def reflect_expr (X : expr) : expr → option ring_expr
| `(%%e₁ + %%e₂) := do
  p₁ ← reflect_expr e₁,
  p₂ ← reflect_expr e₂,
  return (ring_expr.add p₁ p₂)
| `(%%e₁ * %%e₂) := do
  p₁ ← reflect_expr e₁,
  p₂ ← reflect_expr e₂,
  return (ring_expr.mul p₁ p₂)
| e := if e = X then return ring_expr.X else
  do n ← expr.to_int e,
     return (ring_expr.const (znum.of_int' n))

-- mathlib/data/num has znum and stuff like znum.of_int' (see above)
def poly := list znum
-- but why use it?

def poly.add : poly → poly → poly 
| [] g := g
| f [] := f 
| (a :: f') (b :: g') := (a + b) :: poly.add f' g' 

@[simp] lemma poly.zero_add (p : poly) : poly.add [] p = p := by induction p;refl 

def poly.smul : znum → poly → poly
| _ [] := []
| z (a :: f') := (z * a) :: poly.smul z f'

def poly.mul : poly → poly → poly 
| [] _ := []
| (a :: f') g := poly.add (poly.smul a g) (0 :: (poly.mul f' g))  

def poly.const : znum → poly := λ z, [z]

def poly.X : poly := [0,1]

def to_poly : ring_expr → poly
| (ring_expr.add e₁ e₂) := (to_poly e₁).add (to_poly e₂)
| (ring_expr.mul e₁ e₂) := (to_poly e₁).mul (to_poly e₂)
| (ring_expr.const z) := poly.const z
| ring_expr.X := poly.X

def poly.eval {α} [comm_ring α] (X : α) : poly → α
| [] := 0
| (n::l) := n + X * poly.eval l

@[simp] lemma poly.eval_zero {α} [comm_ring α] (X : α) : poly.eval X [] = 0 := rfl

@[simp] theorem poly.eval_add {α} [comm_ring α] (X : α) : ∀ p₁ p₂ : poly,
  (p₁.add p₂).eval X = p₁.eval X + p₂.eval X := 
begin
  intro p₁,
  induction p₁ with h₁ t₁ H,
    -- base case
    intros,simp [poly.eval],
  -- inductive step 
  intro p₂,
  cases p₂ with h₂ t₂,
    simp [poly.add],
  unfold poly.eval poly.add,
  rw (H t₂),
  simp [mul_add]
end 

@[simp] lemma poly.eval_mul_zero {α} [comm_ring α] (f : poly) (X : α) :
  poly.eval X (poly.mul f []) = 0 :=
begin
  induction f with h t H,
    refl,
  unfold poly.mul poly.smul poly.add poly.mul poly.eval,
  rw H,simp
end 

@[simp] lemma poly.eval_smul {α} [comm_ring α] (X : α) (z : znum) (f : poly) :
  poly.eval X (poly.smul z f) = z * poly.eval X f :=
begin
  induction f with h t H, simp [poly.smul,poly.eval,mul_zero],
  unfold poly.smul poly.eval,
  rw H,
  simp [mul_add,znum.cast_mul,mul_assoc,mul_comm]
end 

@[simp] theorem poly.eval_mul {α} [comm_ring α] (X : α) : ∀ p₁ p₂ : poly,
  (p₁.mul p₂).eval X = p₁.eval X * p₂.eval X := 
begin
  intro p₁,induction p₁ with h₁ t₁ H,
    simp [poly.mul],
  intro p₂,
  unfold poly.mul,
  rw poly.eval_add,
  unfold poly.eval,
  rw [H p₂,znum.cast_zero,zero_add,add_mul,poly.eval_smul,mul_assoc]
end 


@[simp] theorem poly.eval_const {α} [comm_ring α] (X : α) : ∀ n : znum,
  (poly.const n).eval X = n := 
begin
  intro n,
  unfold poly.const poly.eval,simp
end 

@[simp] theorem poly.eval_X {α} [comm_ring α] (X : α) : poly.X.eval X = X := 
begin
  unfold poly.X poly.eval,simp
end 


def ring_expr.eval {α} [comm_ring α] (X : α) : ring_expr → α
| (ring_expr.add e₁ e₂) := e₁.eval + e₂.eval
| (ring_expr.mul e₁ e₂) := e₁.eval * e₂.eval
| (ring_expr.const z) := z
| ring_expr.X := X

theorem to_poly_eval {α} [comm_ring α] (X : α) (e) : (to_poly e).eval X = e.eval X :=
by induction e; simp [to_poly, ring_expr.eval, *]

theorem main_thm {α} [comm_ring α] (X : α) (e₁ e₂) {x₁ x₂}
  (H : to_poly e₁ = to_poly e₂) (R1 : e₁.eval X = x₁) (R2 : e₂.eval X = x₂) : x₁ = x₂ :=
by rw [← R1, ← R2, ← to_poly_eval, H, to_poly_eval]

meta def ring_tac (X : pexpr) : tactic unit := do
  X ← to_expr X,
  `(%%x₁ = %%x₂) ← target,
  r₁ ← reflect_expr X x₁,
  r₂ ← reflect_expr X x₂,
  let e₁ : expr := reflect r₁,
  let e₂ : expr := reflect r₂,
  `[refine main_thm %%X %%e₁ %%e₂ rfl _ _],
  all_goals `[simp only [ring_expr.eval,
    znum.cast_pos, znum.cast_neg, znum.cast_zero',
    pos_num.cast_bit0, pos_num.cast_bit1,
    pos_num.cast_one']]

theorem X (x : ℝ) : (x + 1) * (x + 1) = x*x+2*x+1 :=
by do ring_tac ```(x)

#print axioms X 

end ring_tac
```

#### [ Kevin Buzzard (Jun 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979329):
Did my homework

#### [ Kevin Buzzard (Jun 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979333):
I feel like an UG again

#### [ Kevin Buzzard (Jun 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979394):
Notes: I had to introduce poly.smul (scalar multiplication of poly by znum) for definition of multiplication. I really tried to make simp do most of the work in general but I still had to do a lot of unfolding before I could get it going.

#### [ Kenny Lau (Jun 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979395):
did you just write a tactic?

#### [ Kevin Buzzard (Jun 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979401):
Not really

#### [ Kevin Buzzard (Jun 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979405):
in the sense that no code I wrote started with `meta`

#### [ Kevin Buzzard (Jun 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979408):
but check it out

#### [ Kevin Buzzard (Jun 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979412):
barely any code at all has `meta`

#### [ Kevin Buzzard (Jun 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979416):
Just `reflect_expr` at the very top, and `ring_tac` at the very bottom. Mario wrote both of those

#### [ Kevin Buzzard (Jun 13 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979480):
Kenny here's the strat: to prove that for d : int we have (d+1)^2=d^2+2*d+1 we first prove that in a polynomial ring we have (X+1)^2=X^2+2X+1 and then deduce

#### [ Kevin Buzzard (Jun 13 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979481):
The problem is that if Lean just sees (d+1)^2 it can't create (X+1)^2

#### [ Kevin Buzzard (Jun 13 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979489):
so this part you have to do in meta-land

#### [ Kevin Buzzard (Jun 13 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979491):
but it's only this part

#### [ Kevin Buzzard (Jun 13 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979496):
unsurprisingly, this is what `reflect_expr` does

#### [ Kevin Buzzard (Jun 13 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979537):
So there's a basic one-variable ring tactic with a very small amount of meta indeed, and the meta is really not hard to comprehend. I mean, it might be hard to write, but it's not at all hard to read.

#### [ Kevin Buzzard (Jun 13 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979539):
I'll write a blog post explaining it but now it's bed time. Once again many thanks Mario.

#### [ Kevin Buzzard (Jun 13 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979604):
Just to be clear @**Kenny Lau** the code I posted does seem to be a fully working baby `ring`

#### [ Kevin Buzzard (Jun 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000038):
Actually it doesn't work in all cases, because there is currently no "canonical form" lemma. The polynomials `[1]` and `[1,0]` (=0*x+1) are different.

#### [ Kevin Buzzard (Jun 13 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000106):
@**Mario Carneiro** Here are the three questions I have about this project, which basically came up when trying to write a blog post. The first two are trivial for you: what is `@[derive has_reflect]` and why `znum` rather than `int`?

#### [ Kevin Buzzard (Jun 13 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000111):
The third is a bit more annoying. Because there is no algorithm to put polynomials (= lists of znums) into "canonical form", `example (x : ℤ) : (x + 1) + ((-1)*x + 1) = 2 := by do ring_tac ```(x) ` fails

#### [ Kevin Buzzard (Jun 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000156):
I think this is because the polynomials `[2,0]` and `[2]` are considered distinct.

#### [ Kevin Buzzard (Jun 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000158):
Aah, I think I can fix this.

#### [ Kevin Buzzard (Jun 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000161):
I think I write some "canonical_form" function

#### [ Kevin Buzzard (Jun 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000162):
(not in meta land)

#### [ Kevin Buzzard (Jun 13 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000171):
and redefine add so that it puts the polynomial into canonical form afterwards.

#### [ Kevin Buzzard (Jun 13 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000180):
yeah yeah OK I think I can do this one.

#### [ Mario Carneiro (Jun 13 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001631):
> Why `@[derive has_reflect]`

This one is easy: otherwise you don't have a `reflect` instance for `ring_expr`. This function is used explicitly in `ring_tac`; the idea is that if `A` is a reflectable type then `reflect (a : A)` is an expr that denotes the same value as `a`

#### [ Mario Carneiro (Jun 13 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001637):
so for example `list` has a reflect that just turns each cons into a `expr.app ``list.cons a l`

#### [ Mario Carneiro (Jun 13 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001644):
and `nat` has a reflect that produces `bit0` and `bit1` expressions (which when printed appear as the number being denoted)

#### [ Mario Carneiro (Jun 13 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001686):
But not all types have a reflect; in particular quotients and other things that make different expressions equal according to lean don't have a reflect, since you would have to open up the quotient to get the element to print

#### [ Mario Carneiro (Jun 13 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001696):
In this case it is needed because `reflect_expr` produces a `ring_expr`, not an `expr` denoting a `ring_expr`

#### [ Mario Carneiro (Jun 13 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001746):
I think in this case you could skip the extra step and just produce an expr directly, but that would be less structured and more meta

#### [ Mario Carneiro (Jun 13 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001856):
> Why `znum`

This one is more subtle, and actually I knew you would ask this question and I used it in part to prompt the question. You can view this as an efficiency move, but when there is an exponential performance gap I think it is close enough to essential to teach directly. Whenever you use proof by reflection, it is absolutely essential that you do everything you can to make the computation simple and direct, because you will be working with a fairly heavy handicap. A big no-no is using `nat` and `int` anywhere in your computation, because (as Seul has discovered) this works in unary and there is nothing you can do to prevent this when computing in the kernel

#### [ Mario Carneiro (Jun 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001891):
This is in fact the raison d'etre for the `num` type - it allows for performing *kernel computations* on naturals and integers, with enough lemmas to relate them back to the more traditional `nat` type.

#### [ Mario Carneiro (Jun 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001947):
It's a bit of a delicate move, since `int` and `nat` are in fact the more efficient ones in VM computations, so you want to convert from `int` to `znum` when storing the numbers inside the kernel data structure (`ring_expr`), but not before

#### [ Mario Carneiro (Jun 13 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128002085):
> The third is a bit more annoying. Because there is no algorithm to put polynomials (= lists of znums) into "canonical form", example (x : ℤ) : (x + 1) + ((-1)*x + 1) = 2 := by do ring_tac ```(x) fails

I noticed this as well with your definition of `poly.add`. But there is actually another solution, which might be easier than applying a function that strips the high zeros after every operation. That is, define
```
def poly.is_eq : poly -> poly -> bool := sorry
```
so that trailing zeros are ignored in the equality test, and then replace `to_poly e1 = to_poly e2` with `poly.is_eq (to_poly e1) (to_poly e2)` in the `main_thm` and prove it with this (weaker) assumption

#### [ Andrew Ashworth (Jun 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128005278):
So, if I defined a new poly type quotiented with this equality relation, I'd have to explicitly define my denotation function? That doesn't sound so bad, I think... or would the kernel get stuck trying to reduce it?

#### [ Andrew Ashworth (Jun 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128005285):
maybe I should just try it out with the helpful reflection template that's just been posted :)

#### [ Kevin Buzzard (Jun 13 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128015942):
```lean
def poly.is_eq_aux : list znum -> list znum -> bool
| [] [] := tt 
| [] (h₂ :: t₂) := if (h₂ = 0) then poly.is_eq_aux [] t₂ else ff 
| (h₁ :: t₁) [] := if (h₁ = 0) then poly.is_eq_aux t₁ [] else ff
| (h₁ :: t₁) (h₂ :: t₂) := if (h₁ = h₂) then poly.is_eq_aux t₁ t₂ else ff

def poly.is_eq : poly → poly → bool := poly.is_eq_aux 
```

#### [ Kevin Buzzard (Jun 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128015985):
[recursion on poly doesn't seem to work]

#### [ Kevin Buzzard (Jun 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128015998):
```lean
theorem poly.eval_is_eq {α} [comm_ring α] (X : α) {p₁ p₂ : poly} : 
  poly.is_eq p₁ p₂ → p₁.eval X = p₂.eval X := 
begin
  revert p₂,
  induction p₁ with h₁ t₁ H₁,
  { intros p₂ H,
    induction p₂ with h₁ t₁ H₂,refl,
    unfold poly.eval,
    unfold poly.is_eq poly.is_eq_aux at H,
    split_ifs at H,swap,cases H,
    rw [h,←H₂ H],
    simp,
  },
  { intros p₂ H,
    induction p₂ with h₂ t₂ H₂,
    { unfold poly.eval,
      unfold poly.is_eq poly.is_eq_aux at H,
      split_ifs at H,swap,cases H,
      rw [h,H₁ H],
      simp
    },
    { unfold poly.eval,
      unfold poly.is_eq poly.is_eq_aux at H,
      split_ifs at H,swap,cases H,
      unfold poly.is_eq at H₂,
      rw [h,H₁ H]
    }
  } 
```

#### [ Kevin Buzzard (Jun 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128016003):
and then all we need is

#### [ Kevin Buzzard (Jun 13 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128016019):
```lean
theorem main_thm {α} [comm_ring α] (X : α) (e₁ e₂) {x₁ x₂}
  (H : poly.is_eq (to_poly e₁) (to_poly e₂)) (R1 : e₁.eval X = x₁) (R2 : e₂.eval X = x₂) : x₁ = x₂ :=
by rw [← R1, ← R2, ← to_poly_eval,poly.eval_is_eq X H, to_poly_eval]
```

#### [ Kevin Buzzard (Jun 13 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128016043):
```lean
example (x : ℤ) : (x + 1) * (x + 1) = x*x+2*x+1 := by do ring_tac ```(x)

example (x : ℤ) : (x + 1) + ((-1)*x + 1) = 2 := by do ring_tac ```(x) 
```

#### [ Kevin Buzzard (Jun 13 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128016051):
they both work :-)

#### [ Mario Carneiro (Jun 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034425):
I wouldn't recommend using a quotient, although it probably won't hurt

#### [ Mario Carneiro (Jun 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034426):
The VM can erase that stuff but the kernel has to deal with it all

#### [ Mario Carneiro (Jun 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034427):
if you keep all the functions simple and nondependent, the kernel doesn't have to carry around all the proof garbage

#### [ Mario Carneiro (Jun 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034428):
for the reason of "working with a handicap" I mentioned

#### [ Mario Carneiro (Jun 14 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034990):
Your definition didn't work on `poly` because it uses well founded recursion, which is another kernel no-no (it has to unfold the well foundedness proofs)

#### [ Mario Carneiro (Jun 14 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034994):
Try this instead:
```
def poly.is_zero : poly → bool
| [] := tt
| (h :: t) := (h = 0) && poly.is_zero t

def poly.is_eq : poly → poly → bool
| l₁ [] := poly.is_zero l₁
| [] l₂ := poly.is_zero l₂
| (h₁ :: t₁) (h₂ :: t₂) := if (h₁ = h₂) then poly.is_eq t₁ t₂ else ff
```
(sorry for all the proof obligations!)

#### [ Mario Carneiro (Jun 14 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128035061):
(Alternatively, if you defined subtraction or an equivalent you could use only `is_zero` and define `is_eq` by `(p1 - p2).is_zero`)

#### [ Kevin Buzzard (Jun 14 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128050689):
Why bool and not Prop?

#### [ Moses Schönfinkel (Jun 14 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128050810):
He did it on purpose to prompt this question! ;)

#### [ Kevin Buzzard (Jun 14 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128054279):
https://xenaproject.wordpress.com/2018/06/13/ab3/

#### [ Kevin Buzzard (Jun 14 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128054290):
Comments welcome. That's how some baby version of tactic.ring works, at least. And of course many thanks to Mario, without whom that little project would have taken far longer to complete.

#### [ Kevin Buzzard (Jun 14 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128054294):
I know the post is mega-long but I am not sure I care.

#### [ Johan Commelin (Jun 14 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128054577):
This is chapter 3 of your book?

#### [ Andrew Ashworth (Jun 14 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128059587):
I read and enjoyed your blog post! My only comment is perhaps you might have a further reading section. It would be a good place to link http://adam.chlipala.net/cpdt/html/Reflection.html and https://softwarefoundations.cis.upenn.edu/vfa-current/Decide.html#lab185 for people who are trying to seriously write a reflective tactic (although, unfortunately, you have to read Coq to understand what's going on... but I think at this stage of Lean's popularity, this is somewhat necessary regardless in the tactics game). Also, minor nitpick, but `znum` is only uber-efficient when it is used in `rfl` proofs, otherwise `int` has special fast support

#### [ Kevin Buzzard (Jun 14 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128067635):
Many thanks Andrew. I am not a computer scientist as I'm sure you know and I don't really know about references. I have looked, briefly, at both of the things you mention, but I have never really substantially engaged with them -- I tend to stop reading when things get "too CS" because they become less relevant to what I am trying to do in Lean. Thanks for the nitpick too.

#### [ Mario Carneiro (Jun 14 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128067751):
> Why bool and not Prop?

Because you can't compute with Props. You could get roughly the same behavior by using `decidable p` instead of `bool` (+ soundness proof), but since there are more dependency tricks there I suspect it's marginally slower than using bool (but not by any large margin).

#### [ Mario Carneiro (Jun 14 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128067896):
In this case, the bool definition functions both as the relation itself and its decidability proof. If you wanted to use decidable, then, it would be two definitions and a soundness proof

#### [ Kevin Buzzard (Jun 14 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128074464):
```quote
This is chapter 3 of your book?
```
I am not sure if this is book material.


{% endraw %}
