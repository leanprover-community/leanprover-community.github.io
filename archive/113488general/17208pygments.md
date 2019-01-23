---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17208pygments.html
---

## Stream: [general](index.html)
### Topic: [pygments](17208pygments.html)

---

#### [Andrew Ashworth (Feb 26 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002866):
my understanding was zulip uses an old version of pygments, and that the lean pygments update was never merged to begin with

#### [Patrick Massot (Feb 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002921):
we can still do 
```lean
meta def f := by sorry
```

#### [Patrick Massot (Feb 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002930):
which is a bit disappointing

#### [Patrick Massot (Feb 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002938):
I had better luck with earlier tests

#### [Sebastian Ullrich (Feb 26 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002948):
I don't think there is such an option

#### [Patrick Massot (Feb 26 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002966):
let me try again:
```lean
example : 1 + 1 = 2 := by norm_num
```

#### [Patrick Massot (Feb 26 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003003):
that one is nicer

#### [Patrick Massot (Feb 26 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003010):
pygments doesn't like meta...

#### [Andrew Ashworth (Feb 26 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003170):
i think pygments for lean is still on highlighting based on lean 2's syntax, iirc

#### [Patrick Massot (Feb 26 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003200):
I guess that could explain a lot

#### [Andrew Ashworth (Feb 26 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003261):
yeah, first i think we'll need to submit a support ticket to zulip and see if they will fork pygments for us, and then we can update the pygment's lexer file for lean

#### [Patrick Massot (Feb 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003279):
Yes, I guess @**Reid Barton** will do that for us

#### [Reid Barton (Feb 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003285):
I've already checked with the Zulip devs and they would be happy to fork pygments if there is a request to do so.

#### [Reid Barton (Feb 26 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003336):
If someone here can produce a patch then I can take care of getting it upstreamed

#### [Patrick Massot (Feb 26 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003356):
Great, @**Sebastian Ullrich** already has everything we need

#### [Patrick Massot (Feb 26 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003400):
I'm requested elsewhere. See you

#### [Sebastian Ullrich (Feb 26 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003826):
Our pygments fork is at https://bitbucket.org/gebner/pygments-main

#### [Reid Barton (Jan 15 2019 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163511):
I ran all of mathlib and a couple of my projects through Gabriel's pygments fork, using the following command:
```
find . -name '*.lean' \( -exec ~/.local/bin/pygmentize -l lean -F raiseonerror '{}' ';' -o -exec echo $'\npygmentize failed:' '{}' ';' -quit \)
```
There was just one lexer error, it doesn't know about the escape sequence `"\t"`. @**Gabriel Ebner** should I submit a PR, or would it be easier for you to just fix it yourself?

#### [Reid Barton (Jan 15 2019 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163531):
(Minimum failing example: `example : string := "\t"`)

#### [Reid Barton (Jan 15 2019 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163672):
It also doesn't know about `"\x12"`, `"\u1234"`, or `"\'"` (I checked the Lean source to see what escape sequences exist)

#### [Gabriel Ebner (Jan 15 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163795):
Please file a PR.

#### [Reid Barton (Jan 15 2019 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163875):
OK

#### [Kevin Buzzard (Jan 15 2019 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155164033):
I think you can get pwned with `-exec` if someone writes a malicious mathlib PR, although I've never understood the details (I read this in the find man page)

#### [Reid Barton (Jan 15 2019 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155167115):
```quote
Please file a PR.
```
 I think I managed to do this.

#### [Gabriel Ebner (Jan 15 2019 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155167460):
Merged.  I've also given you write access if you want.

#### [Reid Barton (Jan 15 2019 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155168459):
I know @**Patrick Massot** was also having LaTeX problems with some specific characters but I don't know whether that's something that would be fixed within pygments or outside it

#### [Patrick Massot (Jan 15 2019 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155168553):
Reid, you only need to try using pygment with LaTeX to see it's all broken, and needs fixing from pygment

#### [Patrick Massot (Jan 15 2019 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155169307):
Now I'm confused: I can't reproduce the problem

#### [Patrick Massot (Jan 15 2019 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155169837):
The following works:
```
\documentclass{article}

\usepackage{newunicodechar}

\newunicodechar{α}{\ensuremath{\alpha}}
\newunicodechar{β}{\ensuremath{\beta}}
\newunicodechar{ι}{\ensuremath{\iota}}
\newunicodechar{𝓤}{\ensuremath{\mathcal{U}}}
\newunicodechar{⁻}{\ensuremath{^-}}
\newunicodechar{¹}{\ensuremath{^1}}
\newunicodechar{∈}{\ensuremath{\in}}
\newunicodechar{∘}{\ensuremath{\circ}}
\newunicodechar{∀}{\ensuremath{\forall}}
\newunicodechar{∃}{\ensuremath{\exists}}
\newunicodechar{𝓝}{\ensuremath{\mathcal{N}}}
\newunicodechar{⨯}{\ensuremath{\mathcal{\times}}}
\newunicodechar{⟨}{\ensuremath{\langle}}
\newunicodechar{⟩}{\ensuremath{\rangle}}

\usepackage{minted}
\begin{document}
\begin{minted}{lean}
example  {f : α → β} (hf : uniform_continuous' f) : continuous f :=
suffices ∀ a, ∀ V ∈ 𝓝 (f a), f ⁻¹' V ∈ 𝓝 a, 
  from continuous_iff_nhds_sets.2 this,
assume a V Vin,
suffices ∃ U ∈ 𝓤 α, f ⁻¹' V = ι a ⁻¹' U,  by rwa mem_nhds_uniformity',
have exW : ∃ W ∈ 𝓤 β, V = ι (f a) ⁻¹' W, by rwa mem_nhds_uniformity' at Vin,
let ⟨W, W_in, hWV⟩ := exW in
⟨(f ⨯ f) ⁻¹' W, hf W W_in,  -- let's use U = (f ⨯ f) ⁻¹' W
  calc
    f ⁻¹' V = f ⁻¹' (ι (f a) ⁻¹' W) : by rw hWV
        ... = (ι (f a) ∘ f) ⁻¹' W   : rfl
        ... = (f⨯f ∘ ι a) ⁻¹' W     : by rw show ι (f a) ∘ f = (f ⨯ f) ∘ ι a, 
                                            by ext ; refl
        ... = ι a ⁻¹' (f⨯f ⁻¹' W)   : rfl⟩
\end{minted}
\end{document}
```
compiled using ` xelatex -shell-escape test.tex` after installing Gabriel's pygment fork

#### [Patrick Massot (Jan 15 2019 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155169965):
of course the `newunicodechar` lines are ugly, and you can't even do it once and for all because of TeX super small memory capacity. But this is not related to pygment

#### [Sebastian Ullrich (Jan 15 2019 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155170760):
AFAIR, we at some point declared a "fallback" token class in the Lean pygments tokenizer so that it should never fail on an unknown notation now

#### [Sebastien Gouezel (Jan 15 2019 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155171886):
If you use a font with enough symbols (such as the Isabelle fonts I sent you the other day), everything works out of the box without any need for `\newunicodechar`.
Unrelated (and out of topic): should I PR https://github.com/sgouezel/mathlib/tree/essai6 at once, or split it in smaller bits (and maybe wait for the refactoring)? :)

#### [Patrick Massot (Jan 15 2019 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172615):
Oh, I forgot this email! I'll try to find it back

#### [Patrick Massot (Jan 15 2019 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172655):
About the PR, here is a rule of thumb: each time GitHub says "Large diffs are not rendered by default" you may consider splitting in smaller bits

#### [Johan Commelin (Jan 15 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172807):
I think if you want reasonably fast merging you should aim for <200 lines per PR. If you are adding a new file, I guess you can make them a bit larger. But everything >500 lines seems to just rot away in the queue.

#### [Patrick Massot (Jan 15 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172875):
We are talking about " 3,734 additions and 264 deletions. " in one commit here

#### [Johan Commelin (Jan 15 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172881):
I do understand that this means you will have to create 10-20 PRs...

#### [Patrick Massot (Jan 15 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172895):
Let's wait for the reorganization maybe

#### [Sebastien Gouezel (Jan 15 2019 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155173389):
My question was mainly a joke, of course I won't PR it in one go. And yes, I will wait for the refactoring before I submit anything. By the way, I am really happy to have done something in Lean (define the space of all nonempty compact metric spaces, with the Gromov-Hausdorff distance) that does not even make sense in Isabelle.

#### [Patrick Massot (Jan 15 2019 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155173468):
Does it directly make sense in DTT, or did you still have to cheat a bit?

#### [Sebastien Gouezel (Jan 15 2019 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155184044):
It makes sense to consider all compact subsets of $$\ell^\infty(\mathbb{N})$$ modulo isometry (and it also makes sense in Isabelle). Call the quotient `GH_space`. It is easy to check that any compact metric space can be isometrically embedded in $$\ell^\infty(\mathbb{N})$$, which gives a canonical map associating to any compact metric type a `GH_space` element. This is the part that does not make sense in Isabelle: you can not define a map that will take a type (with some additional typeclass properties) and yield an element of another type.

#### [Patrick Massot (Jan 15 2019 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155184670):
I understand that. But my distant memory of GH distance between X and Y  involve sending X and Y into any other metric space. Is such a definition already problematic (and only heuristic) in set theory?

#### [Sebastien Gouezel (Jan 15 2019 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187105):
```quote
But my distant memory of GH distance between X and Y  involve sending X and Y into any other metric space. Is such a definition already problematic (and only heuristic) in set theory?
```
 Textbooks do not really go to such details, but they should: if you say "all compact metric spaces up to isometry", this is not well defined (but if you notice that the cardinal of such a space is bounded, then everything is easy to solve). In the same way, if you say "send X and Y to all metric spaces", this is not well defined, but in fact all that matters is the union of the images of X and Y, which is compact and therefore has bounded cardinal. This is essentially what I do, saying that it is enough to consider embeddings in $$\ell^\infty(\mathbb{N})$$ to say something about all metric spaces.

#### [Patrick Massot (Jan 15 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187371):
Still, do you think everybody working with GH distance will be happy with your definition?

#### [Patrick Massot (Jan 15 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187414):
Should we ask Gromov? :wink:

#### [Sebastien Gouezel (Jan 15 2019 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187510):
Yes, because I prove that it gives what you expect: for any embeddings of X and Y in metric spaces, the Gromov-Hausdorff distance between X and Y is bounded above by the Hausdorff distance of the images. And there is one such embedding that realizes the Gromov-Hausdorff distance.

#### [Sebastien Gouezel (Jan 15 2019 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187605):
In fact, the API is designed so that, in the end, you should completely forget that it was defined using $$\ell^\infty(\mathbb{N})$$: this is just a handy technical tool in the construction.

