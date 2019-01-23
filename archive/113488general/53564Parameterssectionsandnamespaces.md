---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53564Parameterssectionsandnamespaces.html
---

## Stream: [general](index.html)
### Topic: [Parameters, sections and namespaces](53564Parameterssectionsandnamespaces.html)

---


{% raw %}
#### [ Mark Dickinson (Dec 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152645325):
I've just encountered the fact that parameters behave differently inside and outside namespaces, and was wondering whether anyone has either an explanation or a pointer to documentation. Here's a toy example (cut down from a real one):

```lean
section anon

parameters {a : ℕ} (a_pos : 0 < a)
include a_pos

lemma a2_pos : 0 < a*a := mul_pos a_pos a_pos
lemma a3_pos : 0 < a*a*a := mul_pos a2_pos a_pos
lemma a3_pos_bis : 0 < a*a*a := by exact mul_pos a2_pos a_pos

end anon
```

Here, as expected from the documentation, `a2_pos` has `a_pos` as a premise outside the section, but within the section it's supplied implicitly. My problem arose when I moved the real code that the above was adapted from to within a namespace:
```lean
namespace bob
section anon

parameters {a : ℕ} (a_pos : 0 < a)
include a_pos

lemma a2_pos : 0 < a*a := mul_pos a_pos a_pos
lemma a3_pos : 0 < a*a*a := mul_pos a2_pos a_pos
lemma a3_pos_bis : 0 < a*a*a := by exact mul_pos a2_pos a_pos  -- Lean unhappy here

end anon
end bob
```
Now I've got the dreaded red squigglies under `mul_pos` on the `a3_pos_bis` line, and to banish them I have to replace `a2_pos` with `(a2_pos a_pos)`, but _only_ for the tactic proof. In the direct proof of `a3_pos`, I have to use `a2_pos` rather than `(a2_pos a_pos)`.

What are the rules here, and are they documented anywhere?

#### [ Mario Carneiro (Dec 28 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646780):
Inside tactics, parameters don't work

#### [ Mario Carneiro (Dec 28 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646785):
all theorems look like they would outside the section

#### [ Mario Carneiro (Dec 28 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646794):
you can work around this by using local notations instead, as in ``local notation `a2_pos` := a2_pos a_pos``

#### [ Mario Carneiro (Dec 28 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646862):
also using the explicit name seems to help, as in `mul_pos bob.a2_pos a_pos`

#### [ Mark Dickinson (Dec 28 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646873):
Thanks! But I'm confused: in the top example (which does work), isn't this exactly an example of parameters working inside a tactic?

#### [ Mario Carneiro (Dec 28 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646928):
I think the fact that the real name of `a2_pos` is `bob.a2_pos` has something to do with it in the second example

#### [ Mario Carneiro (Dec 28 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646943):
I generally avoid parameters because they are kind of flaky when you use tactics

#### [ Mario Carneiro (Dec 28 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646951):
it's really just a notation, and lean doesn't hide this very well

#### [ Mark Dickinson (Dec 28 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646996):
Okay, thanks.

#### [ Mark Dickinson (Dec 28 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647058):
So I get the sense I'm abusing Lean here; I probably need to change my approach. I have a train of lemmas leading up to a main theorem, with a whole bunch of definitions, hypotheses, etc. common to all. As a mathematician, I'd declare the variables and assumptions at the start of a section, then make use of them within the section; parameters seemed like the right fit for this.

#### [ Mark Dickinson (Dec 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647075):
I don't really want to have to explicitly include the necessary hypotheses in each lemma; that would be repetitive and painful. The alternative seems to be to embed everything within the proof of the main theorem; maybe that's the way to go.

#### [ Kenny Lau (Dec 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647120):
... or you can use `variables`

#### [ Mario Carneiro (Dec 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647121):
You can package up all the hypotheses into a definition

#### [ Mark Dickinson (Dec 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647125):
Hmm; that could work.

#### [ Mario Carneiro (Dec 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647132):
in theory parameters are the way to go, but they just don't work very well

#### [ Kenny Lau (Dec 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647135):
```lean
namespace bob
section anon

variables {a : ℕ} (a_pos : 0 < a)
include a_pos

lemma a2_pos : 0 < a*a := mul_pos a_pos a_pos
lemma a3_pos : 0 < a*a*a := mul_pos (a2_pos a_pos) a_pos
lemma a3_pos_bis : 0 < a*a*a := by exact mul_pos (a2_pos a_pos) a_pos  -- Lean unhappy here

end anon
end bob
```

#### [ Mario Carneiro (Dec 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647184):
If the lemmas all represent major parts of the main theorem, it's not a bad idea to explicitly `have` each of them in the main theorem, passing in all the assumptions

#### [ Kenny Lau (Dec 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647193):
anyway it would be better if you have some practical examples

#### [ Mark Dickinson (Dec 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647205):
@**Kenny Lau** I do, but they're long. :-)

#### [ Mario Carneiro (Dec 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647206):
for an example like the above that approach would be a bit too "heavyweight", but presumably your real example is larger and might warrant it

#### [ Mark Dickinson (Dec 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647255):
@**Mario Carneiro** Yes, moving things into the main theorem sounds like the right approach.

#### [ Mark Dickinson (Dec 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647721):
@**Kenny Lau** FWIW, here's the real example code that I was attempting to put into a namespace (mostly because I want to be able to make local definitions): https://github.com/mdickinson/snippets/blob/master/proofs/isqrt/src/isqrt.lean#L380-L500

#### [ Kenny Lau (Dec 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647727):
we already have isqrt though

#### [ Kenny Lau (Dec 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647734):
oh it's a different purpose

#### [ Mark Dickinson (Dec 28 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647809):
Yes, I know. :-)  I'm not trying to define isqrt. I'm proving that a particular algorithm for computing integer sqrt that I care about (because it's useful in another language) is valid.

#### [ Mark Dickinson (Dec 28 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647916):
I was trying to tidy this section of the proof up by fixing all the repetition of `let a := M*d + n / (4*M*d) in ...`. Making `a` a definition in the section seems like the obvious way to do this, but has the issue that then I can't use `a` later on because it's already taken for that definition; I only really want a local definition. So I tried to use namespaces to contain the definition, and that's when things started to go wrong. :-(

#### [ Mark Dickinson (Dec 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152649070):
Quick followup: the specific issue I was running into was already reported here: https://github.com/leanprover/lean/issues/1773. (I _did_ search the GitHub issues before posting; honest!)

#### [ Mario Carneiro (Dec 28 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152653413):
Do you know how this algorithm compares to the algorithm for `nat.sqrt`, which is also a binary algorithm? That one has a proof already

#### [ Mark Dickinson (Dec 28 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152653940):
Well, for Python (which is what I actually care about in this case), it's hundreds of times faster for (for example) crypto-size integers (by which I mean a few hundred to a few thousand digits).

#### [ Mark Dickinson (Dec 28 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654012):
It's basically Newton–Raphson with steadily increasing working precision, so takes many fewer steps than the bit-by-bit approach that `nat.sqrt` uses (at least if I'm understanding it correctly).

#### [ Mark Dickinson (Dec 28 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654170):
It's not a world away from the GMP integer square root algorithm, which has been verified in Coq (in a paper by Yves Bertot, Nicolas Magaud, and Paul Zimmermann), except that their algorithm needs a possible correction at every step, and this one only needs a single possible correction at the end.

#### [ Kevin Buzzard (Dec 28 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654340):
Hi Mark! How do running times in Lean and python compare?

#### [ Mario Carneiro (Dec 28 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654346):
python certainly wins hands down

#### [ Mario Carneiro (Dec 28 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654469):
For the main recursion in `isqrt_aux`, you should use `binary_rec_on` which is implemented with bit shifts

#### [ Reid Barton (Dec 28 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152655105):
```quote
So I get the sense I'm abusing Lean here; I probably need to change my approach. I have a train of lemmas leading up to a main theorem, with a whole bunch of definitions, hypotheses, etc. common to all. As a mathematician, I'd declare the variables and assumptions at the start of a section, then make use of them within the section; parameters seemed like the right fit for this.
```
 I like this style a lot (for example see https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/topological_spaces/pushout_lemmas.lean#L163), and so I have a small bag of tricks for working around the issue with tactics, including "avoid tactics" and a trick with `let` I described here: https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/parameters.20and.20tactics/near/148863078

#### [ Reid Barton (Dec 28 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152655288):
Or sometimes the path of least resistance is just to supply the parameters manually when you use one of your lemmas from within a tactic.

#### [ Mark Dickinson (Dec 28 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152662761):
@**Kevin Buzzard** Re: running times; I'm afraid I have little idea. I know a bit about the Python side, but very little about the Lean side, so don't have much basis for comparison. CPython's bigint implementation is basic and simple (nothing like GMP), but it's well written and  does pretty well in practice provided you don't try to use hundred-thousand digit integers (which isn't really the target anyway). With one exception, complexities are the ones you'd expect from the usual school-taught algorithms: linear time for addition, subtraction, left and right shifts and other bitwise operations, quadratic time for division. Multiplication uses Karatsuba's algorithm when the number of bits gets large enough, so is subquadratic. (Disclaimer: I've done a bit of hacking on Python's bigint implementation over the years, so I'm biased.)

#### [ Mark Dickinson (Dec 28 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152662811):
I think SAGE uses GMP-based integers instead of Python bigints, which makes sense given the target audience.

#### [ Mark Dickinson (Dec 28 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152662918):
@**Mario Carneiro** Thanks; I'll give `binary_rec_on` a try. Though part of my aim here is to keep the `isqrt` and `isqrt_aux` code as close as possible to the Python equivalents, so that it's evident that there are no errors in translation.

#### [ Mark Dickinson (Dec 28 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152663078):
@**Reid Barton** Thanks for the tips and links! I'll take a look shortly. At this point I'm finding other people's code to be by far the best resource for learning how to use Lean better.


{% endraw %}
