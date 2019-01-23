---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59576leanstypetheory.html
---

## Stream: [general](index.html)
### Topic: [lean's type theory](59576leanstypetheory.html)

---


{% raw %}
#### [ Mario Carneiro (Mar 17 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123826805):
Okay, I'm a bit embarrassed to release this in this very early form, but there's enough meat in it that it can be useful to others even before it's done. This will probably become a major part of my master's thesis. What you will find:

* A definition of the axioms of lean
  * The basic DTT stuff
  * let binders and definitions
  * inductive types (in full gory detail)
  * the computation rules (beta, eta, zeta, delta, iota)
  * Quotient types
  * propext and choice
* Algorithmic equality (aka lean's defeq)
  * proof that algorithmic equality is not transitive and defeq is not decidable
* Unique typing
  * A long and complicated proof, involving a hierarchy of church-rosser theorems. I'm really glad it worked out, but the complexity shows, and I need to trim it down and make it more accessible
* Soundness (unfinished)
  * It is exactly as simple as it sounds like, but the language is huge and there are a lot of cases.

https://github.com/digama0/lean-type-theory/releases/download/v0.1/main.pdf

#### [ Kevin Buzzard (Mar 17 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123835473):
Oh many thanks for this -- as you saw, I made some sort of effort to engage with this kind of material without reading the source code (i.e. restricting to the docs) and it was tough. I am relieved to see that iota reduction applies to things defined by recursion rather than just cases!

#### [ Kevin Buzzard (Mar 17 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123836058):
I spent some time yesterday trying to get to the bottom of this `accrec` example and it would have been a darn sight easier if I'd had access to this paper then.

#### [ Gabriel Ebner (Mar 17 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837211):
I think it's great that we finally have a written description of the type theory implemented in Lean.  Ideally it should also be included in the reference manual, and/or published somewhere.

#### [ Gabriel Ebner (Mar 17 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837329):
section 2.3: I don't think it is a good idea to require full whnf in the algorithmic equivalence since we don't do it any of the implementations.  We do lazy delta-reduction, that is, do full beta/iota/quotient/zeta and only unfold the constant with the larger definitional height, once.  I think you should just replace ↓ by ⇝* here.

#### [ Gabriel Ebner (Mar 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837381):
section 2.4: "Lean takes a simpler approach and simply zeta expands these binders when necessary for checking.":  I don't think you've defined "Lean" anywhere.  Not all of the implementations follow this approach.  The C++ `type_checker`, the Haskell `tc`, and `trepplein` all eagerly unfold lets.  However, the `type_context` doesn't.  I believe the term ζ-reduction typically refers to x ⇝ e'.

#### [ Mario Carneiro (Mar 17 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837575):
There are a few white lies in algorithmic equivalence, and I'd be happy to give a more honest account but I'm not quite sure how. (One thing I have noticed is that sometimes pure congruence proofs don't check, because one side is eagerly iota reduced to something that is not recognizably equivalent anymore.)

#### [ Gabriel Ebner (Mar 17 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837576):
section 2.6.2: "Here we have K-like elimination": do you mean large elimination?  K-like reduction for acc would not be strongly normalizing, right?

#### [ Mario Carneiro (Mar 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837581):
I don't use the term "subsingleton elimination" anywhere in the paper, I may have mixed up my terms. I use K-like elimination to refer to large eliminating props

#### [ Mario Carneiro (Mar 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837625):
When I talk about "lean does X", I am usually referring to lean.exe's kernel. I didn't want to get into checking expressions with lets in the context, like `type_context` does, which is why I omitted that approach.

#### [ Gabriel Ebner (Mar 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837626):
> but there is a second reduction rule used for K-like eliminators. It can be thought of as a combination of proof irrelevance to change the major
premise into a constructor followed by the iota rule.

Yes, you might want to clean up the definitions (and actually define them). ^^

#### [ Mario Carneiro (Mar 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837628):
which part?

#### [ Mario Carneiro (Mar 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837668):
Also: I just finished the proof of soundness. Celebrate! Lean can't prove false

#### [ Gabriel Ebner (Mar 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837669):
K-like elimination refers to K-like reduction here, and subsingleton elimination on the page before, afaict.

#### [ Gabriel Ebner (Mar 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837670):
That's not using algorithmic defeq, right?

#### [ Mario Carneiro (Mar 17 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837680):
Soundness for both algorithmic and ideal typechecking

#### [ Mario Carneiro (Mar 17 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837721):
I proved it for the ideal version, and the algorithmic check implies ideal check

#### [ Gabriel Ebner (Mar 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837765):
> algorithmic check implies ideal check

That's not proven yet, right?

#### [ Mario Carneiro (Mar 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837766):
It's pretty trivial

#### [ Mario Carneiro (Mar 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837767):
the algorithmic rules are a subset of the ideal ones

#### [ Mario Carneiro (Mar 17 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837772):
the ideal check is basically what lean would do if it was nondeterministic and tried all the tricks at once

#### [ Gabriel Ebner (Mar 17 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837816):
Except that the ideal ones have extra side conditions that require the well-typedness of all terms that occur.  The implication requires at the very least subject reduction for ⇝, which is not completely obvious to me.

#### [ Gabriel Ebner (Mar 17 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837861):
Ok, I see subjection reduction is Lemma 3.10.

#### [ Mario Carneiro (Mar 17 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837866):
Note that ->_kappa is a bit different from ->, it has slightly different rules for iota stuff

#### [ Mario Carneiro (Mar 17 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837869):
I never explicitly stated subject reduction for -> (using the ideal check), but maybe I should be more precise about it

#### [ Gabriel Ebner (Mar 17 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838082):
I think the general approach for the algorithmic defeq is good.  It's better to have an over-approximation than to precisely model the actual (current implementation of the) type-checker.  If you can show this defeq proof system to be sound, then all "reasonable" type-checkers should be correct.

#### [ Gabriel Ebner (Mar 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838128):
section 2.3:  you're also missing η-expansion, see https://github.com/leanprover/lean/blob/07bb7d809b6be49f38ce4e427c54a82708ae281f/src/kernel/type_checker.cpp#L517-L529

#### [ Mario Carneiro (Mar 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838372):
Would it suffice to replace the eta rule with extensionality "e x <-> e' x => e <-> e'"?

#### [ Mario Carneiro (Mar 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838415):
or is this only used when solving lam x:a. e <-> e'

#### [ Gabriel Ebner (Mar 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838416):
Yes, you can then recover η via the conversion rule.

#### [ Gabriel Ebner (Mar 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838417):
Yes, in practice it is only used when one side is a lambda.

#### [ Mario Carneiro (Mar 17 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838454):
I know some typecheckers prefer extensionality over eta, since it's pretty easy to figure out when to use it

#### [ Mario Carneiro (Mar 17 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838801):
> > but there is a second reduction rule used for K-like eliminators. It can be thought of as a combination of proof irrelevance to change the major
premise into a constructor followed by the iota rule.
>
> Yes, you might want to clean up the definitions (and actually define them). ^^

I don't follow. That passage looks alright, is something missing?

#### [ Gabriel Ebner (Mar 17 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838901):
K-like elimination refers to multiple concepts in the paper: 1) subsingleton elimination, and 2) K-like reduction.  For example, `and` has 1) but not 2).

#### [ Mario Carneiro (Mar 17 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838941):
I use it essentially only for (1), (2) is more of a remark that comes up once as a sort of historical note "why K?"

#### [ Gabriel Ebner (Mar 17 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838949):
You use it for 2) in section 2.6.4.  Although it is not clear how you obtain the `b` there.

#### [ Mario Carneiro (Mar 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838988):
I need a name for inductive types that eliminate to Type but live in Prop. "Large elimination" seems to also suggest when the type itself is large, so it's not a great name. Will subsingleton elimination cover exactly this usage?

#### [ Mario Carneiro (Mar 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838989):
the b is obtained from the LHS as described in the paragraph after

#### [ Mario Carneiro (Mar 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838990):
and it only applies if you can obtain all of b that way

#### [ Gabriel Ebner (Mar 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838991):
I've only seen "subsingleton elimination" in this usage.

#### [ Mario Carneiro (Mar 17 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838996):
cool, I'll stop saying K-like then

#### [ Gabriel Ebner (Mar 17 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838997):
Ah, next page, ok.

#### [ Mario Carneiro (Mar 17 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123840473):
Huh, I've been telling myself that defeq is only undecidable in inconsistent contexts, but this is not true, almost trivially: if `x : 0 |- A = B` is some undecidable defeq problem, then `|- \lam x : 0. A = \lam x : 0. B` is also an undecidable defeq problem

#### [ Patrick Massot (Mar 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843167):
I swear one day I'll have time to actually read this paper (or maybe a version with a bit higher word/symbol ratio). In the mean time I'm surprised by the source code. It' funny to see Lean consistently use unicode to be more readable than Coq but you still write `\Gamma\vdash \alpha:\U_\ell\quad \Gamma\vdash e:\beta` in your LaTeX source like it's still 1990.

#### [ Patrick Massot (Mar 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843211):
You even use `$$`!

#### [ Patrick Massot (Mar 17 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843221):
And a non-semantic use of `\frac`

#### [ Patrick Massot (Mar 17 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843223):
Ok, I go back to work

#### [ Simon Hudon (Mar 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843262):
Yeah LaTeX is pretty horrible. Nothing seems to measure up though. And people have tried a lot

#### [ Patrick Massot (Mar 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843270):
Mario's LaTeX is horrible

#### [ Patrick Massot (Mar 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843272):
Nothing keeps him in 1990

#### [ Patrick Massot (Mar 17 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843279):
He could use `xeLaTeX` (or `LuaLaTeX`) and `unicode-math`

#### [ Simon Hudon (Mar 17 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843280):
Maybe that and underwater basket weaving are the things he doesn't rock at. But seriously, what does 2018 LaTeX look like?

#### [ Patrick Massot (Mar 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843324):
At least https://gitlab.com/PatrickMassot/h-principle/blob/master/src/hol_approx.tex

#### [ Patrick Massot (Mar 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843336):
(some unicode is not used in this example because this source code is also meant for MathJax consumption)

#### [ Simon Hudon (Mar 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843337):
I have not actually tried those. You actually enter your formulas with unicode and don't need spacing commands?

#### [ Patrick Massot (Mar 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843341):
You still need spacing commands

#### [ Patrick Massot (Mar 17 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843343):
but no `\Gamma`

#### [ Simon Hudon (Mar 17 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843383):
That is pretty nice

#### [ Mario Carneiro (Mar 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843396):
I'm never sure if unicode is going to get mangled somewhere

#### [ Simon Hudon (Mar 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843397):
I've been trying org-mode for my dissertation. Maybe I should add one of those too

#### [ Mario Carneiro (Mar 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843441):
I remember Floris sent in a tex file with lean snippets, and the journal typesetter complained about the unicode

#### [ Patrick Massot (Mar 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843444):
Oh yes, you could have trouble with the journal

#### [ Patrick Massot (Mar 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843450):
Today you still need to fight arXiv if you want to use 21th century LaTeX

#### [ Simon Hudon (Mar 17 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843452):
can you use those tools as preprocessors?

#### [ Patrick Massot (Mar 17 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843459):
That's the reason why you see more and more papers on arxiv where only the pdf is available and not the TeX source

#### [ Mario Carneiro (Mar 17 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843504):
No one has ever convincingly explained to me why `$$` is worse than `\[` (or something else?)

#### [ Gabriel Ebner (Mar 17 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843560):
section 3.4: why do you consider η-reduction?  I don't think any Lean typechecker has that.

#### [ Patrick Massot (Mar 17 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843567):
$$ has spacing issues (beyond being harder to parsers)

#### [ Patrick Massot (Mar 17 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843569):
https://tex.stackexchange.com/questions/503/why-is-preferable-to/69854 probably contains useful links

#### [ Mario Carneiro (Mar 17 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843622):
How else are you going to get eta reduction unless you put it in? Also: the constraints on the kappa reduction relation are very tight. I went through no less than 10 variations on it before I was able to get the church rosser theorem to go through

#### [ Simon Hudon (Mar 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843662):
```quote
That's the reason why you see more and more papers on arxiv where only the pdf is available and not the TeX source
```
Do you mean that it is not used as a preprocessor and therefore people only submit pdfs?

#### [ Gabriel Ebner (Mar 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843665):
Not at all?  None of the typecheckers uses it, AFAIK.  Trepplein definitely doesn't.  We only do η for defeq.

#### [ Gabriel Ebner (Mar 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843671):
I just got the feeling that η is a serious complication here, and the main reason you need a new and different reduction relation and defeq relation.

#### [ Mario Carneiro (Mar 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843679):
the whole point of the kappa reduction is so that the statement of Theorem 3.15 holds

#### [ Mario Carneiro (Mar 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843724):
The alternative would be to try to put eta or extensionality in the =p relation

#### [ Gabriel Ebner (Mar 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843729):
I thought it is included in the ... in the definition of =p.

#### [ Mario Carneiro (Mar 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843730):
the ... only includes compatibility rules

#### [ Gabriel Ebner (Mar 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843772):
I don't think it says that anywhere. (at least not above and below the definition)

#### [ Mario Carneiro (Mar 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843778):
It's a very spartan relation, it's just replacing proofs and nothing else (except for that lambda thing)

#### [ Mario Carneiro (Mar 17 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843925):
I will investigate whether it suffices to have one-sided extensionality e =p e' x => lam x:a. e =p e' and remove eta from the kappa reduction. If so that would allow me to remove the context from ->k, which would be nice

#### [ Mario Carneiro (Mar 17 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844178):
I think the biggest departure from the usual reduction relation is the K reduction (which I have renamed K+), because it is super aggressive unfolding of a proof, which guarantees nontermination when it sees an acc.rec

#### [ Kevin Buzzard (Mar 17 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844779):
so is this paper about what Lean does, or what it should do in your opinion :-)

#### [ Kevin Buzzard (Mar 17 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844830):
And do the devs have any comments about whether Lean 4 will do the same thing when it comes to definitional equality?

#### [ Gabriel Ebner (Mar 17 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844835):
Not sure if I count as a dev anymore, but I seriously doubt there will be any foundational changes in Lean 4.

#### [ Kevin Buzzard (Mar 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844845):
That's good to know -- I guess there were foundational changes from Lean 2 to Lean 3 so I suppose it wasn't something one could definitely assume...

#### [ Gabriel Ebner (Mar 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844931):
There were exactly two foundational changes from Lean 2 to Lean 3: 1) let-expressions in the kernel (completely harmless), 2) mutually inductive types are no longer supported by the kernel (these are now simulated).  Also the axioms for choice and quotients got some mostly cosmetic changes.

#### [ Kevin Buzzard (Mar 17 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844940):
Oh I thought there was some change to the underlying type theory -- HoTT in Lean 2?

#### [ Gabriel Ebner (Mar 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845033):
Oh yes, HoTT got removed from the kernel (you had to pass an extra command-line flag to use it, and there was a separate library).  Completely forgot about that.  But we now have a reasonably way to do it without kernel changes: https://github.com/gebner/hott3

#### [ Mario Carneiro (Mar 17 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845396):
> so is this paper about what Lean does, or what it should do in your opinion :-)

The motivation is of course what lean does, but this is badly behaved in a number of ways which make it completely unsuitable for theoretical treatment, so I replace it with a better version, show soundness of the original version with respect to that, and then forget about the original thing

#### [ Mario Carneiro (Mar 17 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845485):
As Gabriel mentions, there are multiple "leans", and they don't all agree on the foundational stuff. This is in part what I wanted to address with this paper, to get down a single system that we can talk about as the ideal lean, and look at how close we can get to that. One thing which should be true, however, is that all existing lean kernels are underestimates of the typing judgment in this paper. That means that anything you can't prove with the ideal judgment can't be verified in these kernels either, which is the soundness result I want

#### [ Gabriel Ebner (Mar 17 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845593):
AFAICT all existing kernels even fit within the *algorithmic* definitional equality check.

#### [ Gabriel Ebner (Mar 17 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845655):
NB: I think the algorithmic definitional equality is not just an ugly approximation of the ideal one, but also important as a practical *optimization*: using the algorithmic definitional equality, we can elide almost all type-inference calls during type-checking.

#### [ Gabriel Ebner (Mar 17 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845731):
Compare also the various variants of the typing rules proved equivalent in [1].
[1] A.Bauer, P. Haselwarter, T. Wintertaler, A modular formalization of type theory in Coq, TYPES (2017). http://math.andrej.com/2017/05/29/a-modular-formalization-of-type-theory-in-coq/

#### [ Mario Carneiro (Mar 17 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845987):
I'm also having difficulty with stating strong normalization because of my struggles here, I think. What is the reduction relation of interest here? Is it just head reduction? I think it is supposed to include reduction under binders, but then once we decide "arbitrarily" not to reduce some things that should be reducible, in what sense are we talking about the "right" relation? I.e. what does strong normalization have to do with consistency?

#### [ Gabriel Ebner (Mar 17 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846304):
Weak head reduction is enough for consistency.  But strong normalization for the full reduction relation is definitely interesting as well.

#### [ Gabriel Ebner (Mar 17 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846367):
Since we've talked about η today, I think I've found a novel way to break transitivity with just K-like reduction for `eq`:
```lean
def foo : 0 = 0 → ℕ :=
@eq.rec ℕ 0 (λ _, ℕ) 42 0
def bar : 0 = 0 → ℕ :=
@eq.rec ℕ 0 (λ n, if n = 0 then ℕ else empty) (42 : ℕ) 0

example : foo = (λ _, 42) := rfl
example : bar = (λ _, 42) := rfl
example : foo = bar := rfl -- fails
```

#### [ Mario Carneiro (Mar 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846714):
I found an interesting potential computational rule for `quot.sound`:
```
variables (α : Sort*) (r : α → α → Prop) (a : α)
  (f : α → Sort*) (H : ∀ (a b : α), r a b → f a = f b)
  (e : f a) (b : α) (h : r a b)

example : @eq.rec (quot r) (quot.mk r a) (quot.lift f H) e
            (quot.mk r b) (quot.sound h) = cast (H a b h) e :=
by change H a b h with (congr_arg (quot.lift f H) (quot.sound h):_);
   induction quot.sound h; refl
```

#### [ Mario Carneiro (Mar 17 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846769):
@**Gabriel Ebner** That was a big pain during the proof of church rosser. It's actually not a theoretical problem, but rather a side effect of K reductions without accounting for eta reduction

#### [ Mario Carneiro (Mar 17 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846775):
I fixed it by making sure that all recursors have the right number of arguments at all times

#### [ Mario Carneiro (Mar 17 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846824):
Alternatively, any K-like inductive should be eta expanded before normalization

#### [ Mario Carneiro (Mar 17 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123847134):
The problem is that unapplied K recursors are stuck terms when they shouldn't be
```
variables (α : Sort*) (a : α) (C : α → Sort*) (e : C a)
#reduce λ h, @eq.rec α a C e a h -- λ (h : a = a), e   <- good
#reduce @eq.rec α a C e a -- eq.rec e                  <- bad
```

#### [ Mario Carneiro (Mar 17 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123847259):
I originally had the recursors evaluating to lambdas like this, but it was a notational nightmare since the number of unapplications depends on how many variables there are (the only one you have "control" over is the major premise, once that one is allowed to be a variable you have to deal with the parameters and such, and any of those could be variables or things equivalent to variables...), so I opted instead for an up-front eta expansion, since during reduction a recursor never loses its major premise


{% endraw %}
