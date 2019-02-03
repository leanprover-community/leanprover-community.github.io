---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17208pygments.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [pygments](https://leanprover-community.github.io/archive/113488general/17208pygments.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andrew Ashworth (Feb 26 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002866):
<p>my understanding was zulip uses an old version of pygments, and that the lean pygments update was never merged to begin with</p>

#### [ Patrick Massot (Feb 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002921):
<p>we can still do </p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">f</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">sorry</span>
</pre></div>

#### [ Patrick Massot (Feb 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002930):
<p>which is a bit disappointing</p>

#### [ Patrick Massot (Feb 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002938):
<p>I had better luck with earlier tests</p>

#### [ Sebastian Ullrich (Feb 26 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002948):
<p>I don't think there is such an option</p>

#### [ Patrick Massot (Feb 26 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123002966):
<p>let me try again:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span>
</pre></div>

#### [ Patrick Massot (Feb 26 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003003):
<p>that one is nicer</p>

#### [ Patrick Massot (Feb 26 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003010):
<p>pygments doesn't like meta...</p>

#### [ Andrew Ashworth (Feb 26 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003170):
<p>i think pygments for lean is still on highlighting based on lean 2's syntax, iirc</p>

#### [ Patrick Massot (Feb 26 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003200):
<p>I guess that could explain a lot</p>

#### [ Andrew Ashworth (Feb 26 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003261):
<p>yeah, first i think we'll need to submit a support ticket to zulip and see if they will fork pygments for us, and then we can update the pygment's lexer file for lean</p>

#### [ Patrick Massot (Feb 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003279):
<p>Yes, I guess <span class="user-mention" data-user-email="rwbarton@gmail.com" data-user-id="110032">@Reid Barton</span> will do that for us</p>

#### [ Reid Barton (Feb 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003285):
<p>I've already checked with the Zulip devs and they would be happy to fork pygments if there is a request to do so.</p>

#### [ Reid Barton (Feb 26 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003336):
<p>If someone here can produce a patch then I can take care of getting it upstreamed</p>

#### [ Patrick Massot (Feb 26 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003356):
<p>Great, <span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> already has everything we need</p>

#### [ Patrick Massot (Feb 26 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003400):
<p>I'm requested elsewhere. See you</p>

#### [ Sebastian Ullrich (Feb 26 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/123003826):
<p>Our pygments fork is at <a href="https://bitbucket.org/gebner/pygments-main" target="_blank" title="https://bitbucket.org/gebner/pygments-main">https://bitbucket.org/gebner/pygments-main</a></p>

#### [ Reid Barton (Jan 15 2019 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163511):
<p>I ran all of mathlib and a couple of my projects through Gabriel's pygments fork, using the following command:</p>
<div class="codehilite"><pre><span></span>find . -name &#39;*.lean&#39; \( -exec ~/.local/bin/pygmentize -l lean -F raiseonerror &#39;{}&#39; &#39;;&#39; -o -exec echo $&#39;\npygmentize failed:&#39; &#39;{}&#39; &#39;;&#39; -quit \)
</pre></div>


<p>There was just one lexer error, it doesn't know about the escape sequence <code>"\t"</code>. <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> should I submit a PR, or would it be easier for you to just fix it yourself?</p>

#### [ Reid Barton (Jan 15 2019 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163531):
<p>(Minimum failing example: <code>example : string := "\t"</code>)</p>

#### [ Reid Barton (Jan 15 2019 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163672):
<p>It also doesn't know about <code>"\x12"</code>, <code>"\u1234"</code>, or <code>"\'"</code> (I checked the Lean source to see what escape sequences exist)</p>

#### [ Gabriel Ebner (Jan 15 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163795):
<p>Please file a PR.</p>

#### [ Reid Barton (Jan 15 2019 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155163875):
<p>OK</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155164033):
<p>I think you can get pwned with <code>-exec</code> if someone writes a malicious mathlib PR, although I've never understood the details (I read this in the find man page)</p>

#### [ Reid Barton (Jan 15 2019 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155167115):
<blockquote>
<p>Please file a PR.</p>
</blockquote>
<p>I think I managed to do this.</p>

#### [ Gabriel Ebner (Jan 15 2019 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155167460):
<p>Merged.  I've also given you write access if you want.</p>

#### [ Reid Barton (Jan 15 2019 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155168459):
<p>I know <span class="user-mention" data-user-id="110031">@Patrick Massot</span> was also having LaTeX problems with some specific characters but I don't know whether that's something that would be fixed within pygments or outside it</p>

#### [ Patrick Massot (Jan 15 2019 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155168553):
<p>Reid, you only need to try using pygment with LaTeX to see it's all broken, and needs fixing from pygment</p>

#### [ Patrick Massot (Jan 15 2019 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155169307):
<p>Now I'm confused: I can't reproduce the problem</p>

#### [ Patrick Massot (Jan 15 2019 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155169837):
<p>The following works:</p>
<div class="codehilite"><pre><span></span>\documentclass{article}

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
example  {f : α → β} (hf : uniform_continuous&#39; f) : continuous f :=
suffices ∀ a, ∀ V ∈ 𝓝 (f a), f ⁻¹&#39; V ∈ 𝓝 a,
  from continuous_iff_nhds_sets.2 this,
assume a V Vin,
suffices ∃ U ∈ 𝓤 α, f ⁻¹&#39; V = ι a ⁻¹&#39; U,  by rwa mem_nhds_uniformity&#39;,
have exW : ∃ W ∈ 𝓤 β, V = ι (f a) ⁻¹&#39; W, by rwa mem_nhds_uniformity&#39; at Vin,
let ⟨W, W_in, hWV⟩ := exW in
⟨(f ⨯ f) ⁻¹&#39; W, hf W W_in,  -- let&#39;s use U = (f ⨯ f) ⁻¹&#39; W
  calc
    f ⁻¹&#39; V = f ⁻¹&#39; (ι (f a) ⁻¹&#39; W) : by rw hWV
        ... = (ι (f a) ∘ f) ⁻¹&#39; W   : rfl
        ... = (f⨯f ∘ ι a) ⁻¹&#39; W     : by rw show ι (f a) ∘ f = (f ⨯ f) ∘ ι a,
                                            by ext ; refl
        ... = ι a ⁻¹&#39; (f⨯f ⁻¹&#39; W)   : rfl⟩
\end{minted}
\end{document}
</pre></div>


<p>compiled using <code> xelatex -shell-escape test.tex</code> after installing Gabriel's pygment fork</p>

#### [ Patrick Massot (Jan 15 2019 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155169965):
<p>of course the <code>newunicodechar</code> lines are ugly, and you can't even do it once and for all because of TeX super small memory capacity. But this is not related to pygment</p>

#### [ Sebastian Ullrich (Jan 15 2019 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155170760):
<p>AFAIR, we at some point declared a "fallback" token class in the Lean pygments tokenizer so that it should never fail on an unknown notation now</p>

#### [ Sebastien Gouezel (Jan 15 2019 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155171886):
<p>If you use a font with enough symbols (such as the Isabelle fonts I sent you the other day), everything works out of the box without any need for <code>\newunicodechar</code>.<br>
Unrelated (and out of topic): should I PR <a href="https://github.com/sgouezel/mathlib/tree/essai6" target="_blank" title="https://github.com/sgouezel/mathlib/tree/essai6">https://github.com/sgouezel/mathlib/tree/essai6</a> at once, or split it in smaller bits (and maybe wait for the refactoring)? :)</p>

#### [ Patrick Massot (Jan 15 2019 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172615):
<p>Oh, I forgot this email! I'll try to find it back</p>

#### [ Patrick Massot (Jan 15 2019 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172655):
<p>About the PR, here is a rule of thumb: each time GitHub says "Large diffs are not rendered by default" you may consider splitting in smaller bits</p>

#### [ Johan Commelin (Jan 15 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172807):
<p>I think if you want reasonably fast merging you should aim for &lt;200 lines per PR. If you are adding a new file, I guess you can make them a bit larger. But everything &gt;500 lines seems to just rot away in the queue.</p>

#### [ Patrick Massot (Jan 15 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172875):
<p>We are talking about " 3,734 additions and 264 deletions. " in one commit here</p>

#### [ Johan Commelin (Jan 15 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172881):
<p>I do understand that this means you will have to create 10-20 PRs...</p>

#### [ Patrick Massot (Jan 15 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155172895):
<p>Let's wait for the reorganization maybe</p>

#### [ Sebastien Gouezel (Jan 15 2019 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155173389):
<p>My question was mainly a joke, of course I won't PR it in one go. And yes, I will wait for the refactoring before I submit anything. By the way, I am really happy to have done something in Lean (define the space of all nonempty compact metric spaces, with the Gromov-Hausdorff distance) that does not even make sense in Isabelle.</p>

#### [ Patrick Massot (Jan 15 2019 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155173468):
<p>Does it directly make sense in DTT, or did you still have to cheat a bit?</p>

#### [ Sebastien Gouezel (Jan 15 2019 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155184044):
<p>It makes sense to consider all compact subsets of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="normal">ℓ</mi><mi mathvariant="normal">∞</mi></msup><mo>(</mo><mrow><mi mathvariant="double-struck">N</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">\ell^\infty(\mathbb{N})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">ℓ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">∞</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathbb">N</span></span><span class="mclose">)</span></span></span></span> modulo isometry (and it also makes sense in Isabelle). Call the quotient <code>GH_space</code>. It is easy to check that any compact metric space can be isometrically embedded in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="normal">ℓ</mi><mi mathvariant="normal">∞</mi></msup><mo>(</mo><mrow><mi mathvariant="double-struck">N</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">\ell^\infty(\mathbb{N})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">ℓ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">∞</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathbb">N</span></span><span class="mclose">)</span></span></span></span>, which gives a canonical map associating to any compact metric type a <code>GH_space</code> element. This is the part that does not make sense in Isabelle: you can not define a map that will take a type (with some additional typeclass properties) and yield an element of another type.</p>

#### [ Patrick Massot (Jan 15 2019 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155184670):
<p>I understand that. But my distant memory of GH distance between X and Y  involve sending X and Y into any other metric space. Is such a definition already problematic (and only heuristic) in set theory?</p>

#### [ Sebastien Gouezel (Jan 15 2019 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187105):
<blockquote>
<p>But my distant memory of GH distance between X and Y  involve sending X and Y into any other metric space. Is such a definition already problematic (and only heuristic) in set theory?</p>
</blockquote>
<p>Textbooks do not really go to such details, but they should: if you say "all compact metric spaces up to isometry", this is not well defined (but if you notice that the cardinal of such a space is bounded, then everything is easy to solve). In the same way, if you say "send X and Y to all metric spaces", this is not well defined, but in fact all that matters is the union of the images of X and Y, which is compact and therefore has bounded cardinal. This is essentially what I do, saying that it is enough to consider embeddings in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="normal">ℓ</mi><mi mathvariant="normal">∞</mi></msup><mo>(</mo><mrow><mi mathvariant="double-struck">N</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">\ell^\infty(\mathbb{N})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">ℓ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">∞</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathbb">N</span></span><span class="mclose">)</span></span></span></span> to say something about all metric spaces.</p>

#### [ Patrick Massot (Jan 15 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187371):
<p>Still, do you think everybody working with GH distance will be happy with your definition?</p>

#### [ Patrick Massot (Jan 15 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187414):
<p>Should we ask Gromov? <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sebastien Gouezel (Jan 15 2019 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187510):
<p>Yes, because I prove that it gives what you expect: for any embeddings of X and Y in metric spaces, the Gromov-Hausdorff distance between X and Y is bounded above by the Hausdorff distance of the images. And there is one such embedding that realizes the Gromov-Hausdorff distance.</p>

#### [ Sebastien Gouezel (Jan 15 2019 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pygments/near/155187605):
<p>In fact, the API is designed so that, in the end, you should completely forget that it was defined using <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="normal">ℓ</mi><mi mathvariant="normal">∞</mi></msup><mo>(</mo><mrow><mi mathvariant="double-struck">N</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">\ell^\infty(\mathbb{N})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">ℓ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">∞</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathbb">N</span></span><span class="mclose">)</span></span></span></span>: this is just a handy technical tool in the construction.</p>


{% endraw %}
