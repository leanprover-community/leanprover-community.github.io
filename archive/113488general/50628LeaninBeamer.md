---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50628LeaninBeamer.html
---

## [general](index.html)
### [Lean in Beamer](50628LeaninBeamer.html)

#### [Patrick Massot (Jan 03 2019 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154244941):
How do people put Lean snippets inside LaTeX Beamer slides? Is there a `listings` syntax highlighting somewhere?

#### [Patrick Massot (Jan 03 2019 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245022):
Hum, google answered https://github.com/leanprover/lean/blob/master/extras/latex/lstlean.md

#### [Patrick Massot (Jan 03 2019 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245043):
I'd still be happy to read any comment of advice on this topic

#### [Sebastian Ullrich (Jan 03 2019 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245477):
I've switched to `minted` + luatex + https://bitbucket.org/leanprover/pygments-main for better Unicode support (and better highlighting, I think?). But setting it up isn't trivial, I wouldn't bother if you're happy with `listings`.

#### [Patrick Massot (Jan 03 2019 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245543):
I just discovered listings doesn't seem to like XeLaTeX so I'm not happy at all

#### [Patrick Massot (Jan 03 2019 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245565):
Sebastian, do you have setup instruction somewhere?

#### [Sebastian Ullrich (Jan 03 2019 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245594):
Not directly, no

#### [Patrick Massot (Jan 03 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245649):
if there any Lean-specific issue, or should general documentation apply?

#### [Patrick Massot (Jan 03 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245701):
appart from using the above fork of pygment I mean

#### [Sebastian Ullrich (Jan 03 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245720):
No, the `minted` documentation should work fine

#### [Patrick Massot (Jan 03 2019 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245771):
Thanks!

#### [Sebastian Ullrich (Jan 03 2019 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245774):
Just make sure you don't have the standard pygments installed, I think. It's been a while.

#### [Patrick Massot (Jan 03 2019 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248529):
I can't get any unicode character to work :sad:

#### [Sebastian Ullrich (Jan 03 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248702):
I don't know anything about Xelatex. Does your monospace font support them?

#### [Patrick Massot (Jan 03 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248714):
It's the same with LuaLaTeX, inside or outside Beamer

#### [Patrick Massot (Jan 03 2019 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248759):
Do you have any example of a working TeX file?

#### [Sebastian Ullrich (Jan 03 2019 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248769):
I.e. does it work in `\verb`?

#### [Sebastian Ullrich (Jan 03 2019 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248814):
This is what I do for unsupported characters:
```
\usepackage{newunicodechar}
\newfontfamily{\freeserif}{DejaVu Sans}
\newunicodechar{ℕ}{\freeserif{ℕ}}
\newunicodechar{ℝ}{\freeserif{ℝ}}
...
```

#### [Patrick Massot (Jan 03 2019 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248847):
It doesn't work with `\verb`

#### [Patrick Massot (Jan 03 2019 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248908):
But it works with your extra input

#### [Sebastian Ullrich (Jan 03 2019 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248916):
Great

#### [Johannes Hölzl (Jan 03 2019 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154249176):
@**Patrick Massot** how important is it to use xelatex or lualatex? I use something similar to the following setup with just pdflatex, and it works for me including unicode: https://gist.github.com/johoelzl/cf74935acdcc9f3133fe1aabaace68f0

#### [Patrick Massot (Jan 03 2019 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154249308):
I use them to be able to use [unicode-math](https://ctan.org/pkg/unicode-math)

#### [Patrick Massot (Jan 03 2019 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154249340):
I didn't know you could specify an aspect ratio to Beamer! Now I expect the organizers to tell me what is the aspect ratio of your video beamer!

#### [Johannes Hölzl (Jan 03 2019 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154249635):
Monday to Wednesday we are in a room called "Agora 1", I never was in this room, but "Agora 3" has 4:3. I can check tomorrow. @**Rob Lewis** do you know what kind of projection we will have?

#### [Rob Lewis (Jan 03 2019 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250098):
Uh, I assume the same as Agora 3. I was also going to check on the whiteboard and projector inputs tomorrow.

#### [Patrick Massot (Jan 03 2019 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250134):
Hum, I tried to sed-convert my unicode mapping list to Sebastian's trick, but the 80's fought back: `! TeX capacity exceeded, sorry [input stack size=5000].`

#### [Patrick Massot (Jan 03 2019 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250244):
Thanks Johannes and Rob! Don't worry too much about that aspect ratio thing, it's almost certainly traditional

#### [Patrick Massot (Jan 03 2019 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250256):
@**Sebastian Ullrich** do you have such a trick for calligraphic letters?

#### [Sebastian Ullrich (Jan 03 2019 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250322):
Something like this?
```
\newunicodechar{𝓞}{\ensuremath{\mathcal{O}}}
```

#### [Patrick Massot (Jan 03 2019 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250369):
I tried that, but then I get a red rectangle around the letter, as we somtimes see on Zulip. I guess this comes from Pygment though.

#### [Patrick Massot (Jan 03 2019 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250460):
Oh, I also have it on the left pointing arrow from backward rewrite. Could it mean I don't use the right version of pygment? Is there an easy test here?

#### [Patrick Massot (Jan 03 2019 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250884):
Maybe https://bitbucket.org/leanprover/pygments-main/src/50aee5370b53b5d05a2329d5e50ffdce83660d87/pygments/lexers/theorem.py?at=default&fileviewer=file-view-default#theorem.py-448 needs updating?

#### [Sebastian Ullrich (Jan 03 2019 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250964):
Riight. You'll want this repo instead... I think https://bitbucket.org/derkha/pygments-main

#### [Gabriel Ebner (Jan 03 2019 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250995):
Or this: https://bitbucket.org/gebner/pygments-main/

#### [Gabriel Ebner (Jan 03 2019 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251024):
@**Sebastian Ullrich** You might want to merge my last commit.

#### [Sebastian Ullrich (Jan 03 2019 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251097):
But then I'd have to figure out how to do that in hg again

#### [Patrick Massot (Jan 03 2019 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251140):
It looks like Gabriel could create a PR, as he would do on GitHub

#### [Gabriel Ebner (Jan 03 2019 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251279):
```quote
Access denied
Return to the previous page or go back to your dashboard.
```
:shrug:

#### [Patrick Massot (Jan 03 2019 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251364):
or not

#### [Sebastian Ullrich (Jan 03 2019 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251446):
Let's just set hg on fire instead

#### [Sebastian Ullrich (Jan 03 2019 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251473):
I see pygments development has actually resumed, I'm surprised. So maybe we can even upstream the changes.

#### [Patrick Massot (Jan 03 2019 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251542):
That would be soooo nice, especially for Zulip

#### [Patrick Massot (Jan 03 2019 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251662):
@**Gabriel Ebner** are you sure you fixed the caligraphic letter issue?

#### [Patrick Massot (Jan 03 2019 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251861):
Indeed it looks like activity resumed two weeks ago. They have only 83 PR to merge know, it's not even twice as many as mathlib!

#### [Gabriel Ebner (Jan 03 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154252775):
@**Patrick Massot**  No, I just fixed some highlighting issues (keywords, etc.).  And this was mainly for sphinx (which uses the html backend).  The calligraphic letters are only a problem with the latex backend (they work fine with html).

#### [Patrick Massot (Jan 03 2019 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154252937):
Would it be easy to fix?

#### [Gabriel Ebner (Jan 03 2019 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154253727):
{% raw %}
I think you just need to add enough `\DeclareUnicodeCharacter`:
```latex
\DeclareUnicodeCharacter{1D49E}{\ensuremath{\mathcal{C}}}
\DeclareUnicodeCharacter{1D4A5}{\ensuremath{\mathcal{J}}}
\DeclareUnicodeCharacter{1D49F}{\ensuremath{\mathcal{D}}}
\DeclareUnicodeCharacter{2964}{\ensuremath{\Rightarrow}} %FIXME
\DeclareUnicodeCharacter{3A0}{\ensuremath{\Pi}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{3C0}{\ensuremath{\pi}}
\DeclareUnicodeCharacter{226B}{>>} % FIXME
\DeclareUnicodeCharacter{22D9}{>>>} % FIXME
\DeclareUnicodeCharacter{226A}{<<} % FIXME
\DeclareUnicodeCharacter{27F6}{\ensuremath{\to}}
\DeclareUnicodeCharacter{27E8}{\ensuremath{\langle}}
\DeclareUnicodeCharacter{27E9}{\ensuremath{\rangle}}
\DeclareUnicodeCharacter{3BB}{\ensuremath{\lambda}}
\DeclareUnicodeCharacter{2245}{\ensuremath{\cong}}
\DeclareUnicodeCharacter{2190}{\ensuremath{\leftarrow}}
\DeclareUnicodeCharacter{27F9}{\ensuremath{\Rightarrow}}
\DeclareUnicodeCharacter{2192}{\ensuremath{\longrightarrow}} % FIXME
\DeclareUnicodeCharacter{3B9}{\ensuremath{\iota}}
\DeclareUnicodeCharacter{3B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{3B2}{\ensuremath{\beta}}
\DeclareUnicodeCharacter{2081}{\ensuremath{{}_1}}
\DeclareUnicodeCharacter{2082}{\ensuremath{{}_2}}
```
See https://gist.github.com/gebner/5f0026666e8758d00e87a2eb352f7a43  (This uses the `pygmentize -f latex` output directly).  The same trick probably works with minted as well.{% endraw %}

#### [Patrick Massot (Jan 03 2019 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154255475):
Sorry, I can't get anything to work with this method.

#### [Patrick Massot (Jan 03 2019 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154255646):
I think I'll use VScode instead :wink:

#### [Sebastian Ullrich (Jan 03 2019 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154265181):
It's pretty sad that not even luatex or xetex implement any kind of font fallback. It just works in our editors, damnit.

#### [matt rice (Jan 05 2019 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154475748):
```quote
if there any Lean-specific issue, or should general documentation apply?
```
 There actually is some lean specific doc here: https://github.com/leanprover/lean/blob/master/doc/syntax_highlight_in_latex.md which has worked well for me at least.

#### [Reid Barton (Jan 08 2019 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154666064):
```quote
I see pygments development has actually resumed, I'm surprised. So maybe we can even upstream the changes.
```
 Do we have a PR open currently? I thought there was one, but I don't see any.
Are there any other changes we should be making before submitting a PR?

#### [Patrick Massot (Jan 08 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676623):
There are changes we should be making, see the conversation in this thread

#### [Reid Barton (Jan 08 2019 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676685):
I meant changes relative to Gabriel's fork

#### [Patrick Massot (Jan 08 2019 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676694):
Yes

#### [Reid Barton (Jan 08 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676758):
Ah, I must have missed something then

#### [Patrick Massot (Jan 08 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676795):
I mentioned caligraphic letters, but also the right pointing arrow

#### [Reid Barton (Jan 08 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676826):
Ahh... I assumed those were due to using the upstream version

#### [Patrick Massot (Jan 08 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676837):
Look at the message where Gabriel pings me

