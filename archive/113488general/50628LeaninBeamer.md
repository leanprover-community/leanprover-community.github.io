---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50628LeaninBeamer.html
---

## Stream: [general](index.html)
### Topic: [Lean in Beamer](50628LeaninBeamer.html)

---


{% raw %}
#### [ Patrick Massot (Jan 03 2019 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154244941):
<p>How do people put Lean snippets inside LaTeX Beamer slides? Is there a <code>listings</code> syntax highlighting somewhere?</p>

#### [ Patrick Massot (Jan 03 2019 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245022):
<p>Hum, google answered <a href="https://github.com/leanprover/lean/blob/master/extras/latex/lstlean.md" target="_blank" title="https://github.com/leanprover/lean/blob/master/extras/latex/lstlean.md">https://github.com/leanprover/lean/blob/master/extras/latex/lstlean.md</a></p>

#### [ Patrick Massot (Jan 03 2019 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245043):
<p>I'd still be happy to read any comment of advice on this topic</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245477):
<p>I've switched to <code>minted</code> + luatex + <a href="https://bitbucket.org/leanprover/pygments-main" target="_blank" title="https://bitbucket.org/leanprover/pygments-main">https://bitbucket.org/leanprover/pygments-main</a> for better Unicode support (and better highlighting, I think?). But setting it up isn't trivial, I wouldn't bother if you're happy with <code>listings</code>.</p>

#### [ Patrick Massot (Jan 03 2019 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245543):
<p>I just discovered listings doesn't seem to like XeLaTeX so I'm not happy at all</p>

#### [ Patrick Massot (Jan 03 2019 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245565):
<p>Sebastian, do you have setup instruction somewhere?</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245594):
<p>Not directly, no</p>

#### [ Patrick Massot (Jan 03 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245649):
<p>if there any Lean-specific issue, or should general documentation apply?</p>

#### [ Patrick Massot (Jan 03 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245701):
<p>appart from using the above fork of pygment I mean</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245720):
<p>No, the <code>minted</code> documentation should work fine</p>

#### [ Patrick Massot (Jan 03 2019 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245771):
<p>Thanks!</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154245774):
<p>Just make sure you don't have the standard pygments installed, I think. It's been a while.</p>

#### [ Patrick Massot (Jan 03 2019 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248529):
<p>I can't get any unicode character to work <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248702):
<p>I don't know anything about Xelatex. Does your monospace font support them?</p>

#### [ Patrick Massot (Jan 03 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248714):
<p>It's the same with LuaLaTeX, inside or outside Beamer</p>

#### [ Patrick Massot (Jan 03 2019 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248759):
<p>Do you have any example of a working TeX file?</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248769):
<p>I.e. does it work in <code>\verb</code>?</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248814):
<p>This is what I do for unsupported characters:</p>
<div class="codehilite"><pre><span></span>\usepackage{newunicodechar}
\newfontfamily{\freeserif}{DejaVu Sans}
\newunicodechar{ℕ}{\freeserif{ℕ}}
\newunicodechar{ℝ}{\freeserif{ℝ}}
...
</pre></div>

#### [ Patrick Massot (Jan 03 2019 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248847):
<p>It doesn't work with <code>\verb</code></p>

#### [ Patrick Massot (Jan 03 2019 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248908):
<p>But it works with your extra input</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154248916):
<p>Great</p>

#### [ Johannes Hölzl (Jan 03 2019 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154249176):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> how important is it to use xelatex or lualatex? I use something similar to the following setup with just pdflatex, and it works for me including unicode: <a href="https://gist.github.com/johoelzl/cf74935acdcc9f3133fe1aabaace68f0" target="_blank" title="https://gist.github.com/johoelzl/cf74935acdcc9f3133fe1aabaace68f0">https://gist.github.com/johoelzl/cf74935acdcc9f3133fe1aabaace68f0</a></p>

#### [ Patrick Massot (Jan 03 2019 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154249308):
<p>I use them to be able to use <a href="https://ctan.org/pkg/unicode-math" target="_blank" title="https://ctan.org/pkg/unicode-math">unicode-math</a></p>

#### [ Patrick Massot (Jan 03 2019 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154249340):
<p>I didn't know you could specify an aspect ratio to Beamer! Now I expect the organizers to tell me what is the aspect ratio of your video beamer!</p>

#### [ Johannes Hölzl (Jan 03 2019 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154249635):
<p>Monday to Wednesday we are in a room called "Agora 1", I never was in this room, but "Agora 3" has 4:3. I can check tomorrow. <span class="user-mention" data-user-id="110596">@Rob Lewis</span> do you know what kind of projection we will have?</p>

#### [ Rob Lewis (Jan 03 2019 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250098):
<p>Uh, I assume the same as Agora 3. I was also going to check on the whiteboard and projector inputs tomorrow.</p>

#### [ Patrick Massot (Jan 03 2019 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250134):
<p>Hum, I tried to sed-convert my unicode mapping list to Sebastian's trick, but the 80's fought back: <code>! TeX capacity exceeded, sorry [input stack size=5000].</code></p>

#### [ Patrick Massot (Jan 03 2019 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250244):
<p>Thanks Johannes and Rob! Don't worry too much about that aspect ratio thing, it's almost certainly traditional</p>

#### [ Patrick Massot (Jan 03 2019 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250256):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> do you have such a trick for calligraphic letters?</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250322):
<p>Something like this?</p>
<div class="codehilite"><pre><span></span>\newunicodechar{𝓞}{\ensuremath{\mathcal{O}}}
</pre></div>

#### [ Patrick Massot (Jan 03 2019 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250369):
<p>I tried that, but then I get a red rectangle around the letter, as we somtimes see on Zulip. I guess this comes from Pygment though.</p>

#### [ Patrick Massot (Jan 03 2019 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250460):
<p>Oh, I also have it on the left pointing arrow from backward rewrite. Could it mean I don't use the right version of pygment? Is there an easy test here?</p>

#### [ Patrick Massot (Jan 03 2019 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250884):
<p>Maybe <a href="https://bitbucket.org/leanprover/pygments-main/src/50aee5370b53b5d05a2329d5e50ffdce83660d87/pygments/lexers/theorem.py?at=default&amp;fileviewer=file-view-default#theorem.py-448" target="_blank" title="https://bitbucket.org/leanprover/pygments-main/src/50aee5370b53b5d05a2329d5e50ffdce83660d87/pygments/lexers/theorem.py?at=default&amp;fileviewer=file-view-default#theorem.py-448">https://bitbucket.org/leanprover/pygments-main/src/50aee5370b53b5d05a2329d5e50ffdce83660d87/pygments/lexers/theorem.py?at=default&amp;fileviewer=file-view-default#theorem.py-448</a> needs updating?</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250964):
<p>Riight. You'll want this repo instead... I think <a href="https://bitbucket.org/derkha/pygments-main" target="_blank" title="https://bitbucket.org/derkha/pygments-main">https://bitbucket.org/derkha/pygments-main</a></p>

#### [ Gabriel Ebner (Jan 03 2019 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154250995):
<p>Or this: <a href="https://bitbucket.org/gebner/pygments-main/" target="_blank" title="https://bitbucket.org/gebner/pygments-main/">https://bitbucket.org/gebner/pygments-main/</a></p>

#### [ Gabriel Ebner (Jan 03 2019 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251024):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> You might want to merge my last commit.</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251097):
<p>But then I'd have to figure out how to do that in hg again</p>

#### [ Patrick Massot (Jan 03 2019 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251140):
<p>It looks like Gabriel could create a PR, as he would do on GitHub</p>

#### [ Gabriel Ebner (Jan 03 2019 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251279):
<blockquote>
<p>Access denied<br>
Return to the previous page or go back to your dashboard.</p>
</blockquote>
<p><span class="emoji emoji-1f937" title="shrug">:shrug:</span></p>

#### [ Patrick Massot (Jan 03 2019 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251364):
<p>or not</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251446):
<p>Let's just set hg on fire instead</p>

#### [ Sebastian Ullrich (Jan 03 2019 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251473):
<p>I see pygments development has actually resumed, I'm surprised. So maybe we can even upstream the changes.</p>

#### [ Patrick Massot (Jan 03 2019 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251542):
<p>That would be soooo nice, especially for Zulip</p>

#### [ Patrick Massot (Jan 03 2019 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251662):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> are you sure you fixed the caligraphic letter issue?</p>

#### [ Patrick Massot (Jan 03 2019 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154251861):
<p>Indeed it looks like activity resumed two weeks ago. They have only 83 PR to merge know, it's not even twice as many as mathlib!</p>

#### [ Gabriel Ebner (Jan 03 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154252775):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  No, I just fixed some highlighting issues (keywords, etc.).  And this was mainly for sphinx (which uses the html backend).  The calligraphic letters are only a problem with the latex backend (they work fine with html).</p>

#### [ Patrick Massot (Jan 03 2019 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154252937):
<p>Would it be easy to fix?</p>

#### [ Gabriel Ebner (Jan 03 2019 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154253727):
<p>I think you just need to add enough <code>\DeclareUnicodeCharacter</code>:</p>
<p><span class="tex-error">\DeclareUnicodeCharacter{1D49E}{\ensuremath{\mathcal{C}}}
\DeclareUnicodeCharacter{1D4A5}{\ensuremath{\mathcal{J}}}
\DeclareUnicodeCharacter{1D49F}{\ensuremath{\mathcal{D}}}
\DeclareUnicodeCharacter{2964}{\ensuremath{\Rightarrow}} %FIXME
\DeclareUnicodeCharacter{3A0}{\ensuremath{\Pi}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{3C0}{\ensuremath{\pi}}
\DeclareUnicodeCharacter{226B}{&gt;&gt;} % FIXME
\DeclareUnicodeCharacter{22D9}{&gt;&gt;&gt;} % FIXME
\DeclareUnicodeCharacter{226A}{&lt;&lt;} % FIXME
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
\DeclareUnicodeCharacter{2082}{\ensuremath{{}_2}}</span></p>
<p>See <a href="https://gist.github.com/gebner/5f0026666e8758d00e87a2eb352f7a43" target="_blank" title="https://gist.github.com/gebner/5f0026666e8758d00e87a2eb352f7a43">https://gist.github.com/gebner/5f0026666e8758d00e87a2eb352f7a43</a>  (This uses the <code>pygmentize -f latex</code> output directly).  The same trick probably works with minted as well.</p>

#### [ Patrick Massot (Jan 03 2019 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154255475):
<p>Sorry, I can't get anything to work with this method.</p>

#### [ Patrick Massot (Jan 03 2019 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154255646):
<p>I think I'll use VScode instead <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sebastian Ullrich (Jan 03 2019 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154265181):
<p>It's pretty sad that not even luatex or xetex implement any kind of font fallback. It just works in our editors, damnit.</p>

#### [ matt rice (Jan 05 2019 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154475748):
<blockquote>
<p>if there any Lean-specific issue, or should general documentation apply?</p>
</blockquote>
<p>There actually is some lean specific doc here: <a href="https://github.com/leanprover/lean/blob/master/doc/syntax_highlight_in_latex.md" target="_blank" title="https://github.com/leanprover/lean/blob/master/doc/syntax_highlight_in_latex.md">https://github.com/leanprover/lean/blob/master/doc/syntax_highlight_in_latex.md</a> which has worked well for me at least.</p>

#### [ Reid Barton (Jan 08 2019 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154666064):
<blockquote>
<p>I see pygments development has actually resumed, I'm surprised. So maybe we can even upstream the changes.</p>
</blockquote>
<p>Do we have a PR open currently? I thought there was one, but I don't see any.<br>
Are there any other changes we should be making before submitting a PR?</p>

#### [ Patrick Massot (Jan 08 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676623):
<p>There are changes we should be making, see the conversation in this thread</p>

#### [ Reid Barton (Jan 08 2019 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676685):
<p>I meant changes relative to Gabriel's fork</p>

#### [ Patrick Massot (Jan 08 2019 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676694):
<p>Yes</p>

#### [ Reid Barton (Jan 08 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676758):
<p>Ah, I must have missed something then</p>

#### [ Patrick Massot (Jan 08 2019 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676795):
<p>I mentioned caligraphic letters, but also the right pointing arrow</p>

#### [ Reid Barton (Jan 08 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676826):
<p>Ahh... I assumed those were due to using the upstream version</p>

#### [ Patrick Massot (Jan 08 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20in%20Beamer/near/154676837):
<p>Look at the message where Gabriel pings me</p>


{% endraw %}
