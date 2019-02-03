---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78790typeclassresolutionorunification.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [type class resolution or unification?](https://leanprover-community.github.io/archive/113488general/78790typeclassresolutionorunification.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265237):
<p>This question might be too vague to answer. I have a fixed type <code>X</code> and I am doing a lot of work with functions from <code>{U : set X // P U}</code> to <code>Type*</code> (for example, <code>X</code> might be a topological space and the functions might assign a type to each open set in <code>X</code>, but I also consider more general possibilities for <code>P</code>, e.g. <code>P</code> might say "<code>U</code> is in a fixed basis for the topological space"). I seem to have three different ways to set up such functions.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265251):
<p>1) I could look at functions on subtypes, as I wrote above. I don't do this. I think subtypes are messy and would be forever taking them apart.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265280):
<p>2) I could define my functions as <code>lam {U} (H : P U), ...</code></p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265322):
<p>3) I could define my functions as <code>lam U [H : P U], ...</code></p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265336):
<p>I don't like (3) because it relies on the type class inference system and for my own types P it would rely on my getting the system to work.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265360):
<p>I used to be using (4) <code>lam U (H : P U)</code> but I just got sick of constantly writing U when it could be inferred from HU, so I just switched to (2).</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265371):
<p>I am now looking at (2) thinking "ugh, my functions are supposed to be eating open sets and they're now eating proofs, that looks a bit weird"</p>

#### [ Chris Hughes (Apr 18 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265469):
<p>I like (2). Same number of arguments, but you don't have to rely on type classes. So long as you always have a proof of <code>P U</code> to hand.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265532):
<p>Are there any arguments for or against any of (1) to (4)? I am 99.9% convinced that I could get any of (1), (2) or (4) working. I simply don't know whether I could get (3) working; in my mind it would be by far the "riskiest" approach. These functions are everywhere in my code and I am constantly coming up with proofs that various sets have property <code>P</code>; in the case <code>P</code> is "I am an open set" then some of these are in mathlib. I would probably have to go around making a whole bunch of things instances, and even then I'm not convinced that I would be able to cover everything (e.g. these functions might show up as part of structures, where the proof of <code>P U</code> is somewhere else in the structure and I am not 100 percent convinced that type class inference can get me to it).</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265593):
<p>I used (4) for open sets and (2) for bases of open sets, and both worked fine, so I switched to (2) because it made my code shorter.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265703):
<p>...and possibly slightly less readable -- e.g. open sets like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>f</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>V</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">f^{-1}(V)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.22222em;">V</span><span class="mclose">)</span></span></span></span> (which was easy to read) have now been removed and replaced by hypotheses like "I am a lemma in mathlib saying the pre-image of an open set under a continuous function is open".</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265721):
<p>On the other hand I am using type class inference for rings (the functions map open sets to rings) and sometimes it just doesn't work and it's easier to do the <code>@</code> dance than try to figure out why it didn't work.</p>

#### [ Chris Hughes (Apr 18 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265734):
<p>(1) has no advantages other than proving things like injectivity where the function has to be <code>α → β</code>, but I don't think you want to do that. (4) does have the advantage of readability. <code>some _</code> is a nightmare in this regard.</p>

#### [ Kenny Lau (Apr 18 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265779):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> it's amazing how we went from knowing nothing about type theory to having an opinion on them</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265780):
<p>yes.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265784):
<p>I've learnt so much this year.</p>

#### [ Kenny Lau (Apr 18 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265795):
<p>the best way to learn maths is indeed to play with them</p>

#### [ Kenny Lau (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265805):
<p>people just learn symbols without the meanings</p>

#### [ Kenny Lau (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265810):
<p>(x+y)^2 = x^2+2xy+y^2</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265811):
<p>I am very much in two minds about whether I want my code to be readable though.</p>

#### [ Kenny Lau (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265812):
<p>means nothing</p>

#### [ Kenny Lau (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265819):
<p>but whenever you are told to expand it, you go from left to right</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265829):
<p>here it means "about 6 invocations of the axioms of a ring" :-)</p>

#### [ Andrew Ashworth (Apr 18 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265831):
<p>i think you should not worry too much about your code being readable in tactic mode</p>

#### [ Andrew Ashworth (Apr 18 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265888):
<p>i don't think there's any way to understand tactic mode without going through the proofs line by line</p>

#### [ Moses Schönfinkel (Apr 18 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265901):
<p>Technically Coq is all tactic mode and you can write readable proofs just fine :).</p>

#### [ Andrew Ashworth (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265962):
<p>chlipala disagrees :)</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265965):
<p>I think I read some quote by Paulson arguing that readability was super-important</p>

#### [ Andrew Ashworth (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265968):
<p>and that's the biggest difference between the isabelle style and the coq style</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265970):
<p>I see.</p>

#### [ Moses Schönfinkel (Apr 18 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125265972):
<p>Adam Disagrees and then writes CPDT, which has yet to be deciphered :).</p>

#### [ Andrew Ashworth (Apr 18 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266045):
<p>well, readability is definitely important, but do you want to make a second pass over all your proofs?</p>

#### [ Andrew Ashworth (Apr 18 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266060):
<p>you can write out many of the intermediate steps with show, have, and give many comments, and that is certainly great</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266138):
<p>The last big proof I wrote (compactness of a certain topological space), every few lines I wrote down what the goal was (in mathematical language) and what I was going to do next.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266142):
<p>So "unreadable" proof but readable comments</p>

#### [ Andrew Ashworth (Apr 18 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266222):
<p>in isabelle some authors go so far as to write a latex proof in the comments next to the formal derivation</p>

#### [ Kenny Lau (Apr 18 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266226):
<p>in isabelle one forgets computability</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266580):
<p>In the future there will be files which humans read which will look like beautifully typeset mathematics and which will unfold into computer-checked proofs.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266586):
<p>I hope to see it before I die.</p>

#### [ Andrew Ashworth (Apr 18 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266609):
<p>perhaps... you have to wonder why coq and isabelle never took off. well, maybe people just need to be exposed to it more</p>

#### [ Sebastien Gouezel (Apr 18 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266776):
<p>Speaking of readability, I just wrote a proof like that:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">eventually_bdd_above_iff_exists_eventually_le</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">u</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span>
<span class="o">(</span><span class="n">eventually_bdd_above</span> <span class="n">F</span> <span class="n">u</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∃</span><span class="n">t</span><span class="o">,</span> <span class="n">eventually</span> <span class="o">(</span><span class="bp">λ</span><span class="n">n</span><span class="o">,</span> <span class="n">u</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">t</span><span class="o">)</span> <span class="n">F</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">A</span><span class="o">:</span> <span class="n">eventually_bdd_above</span> <span class="n">F</span> <span class="n">u</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span><span class="n">t</span><span class="o">,</span> <span class="n">eventually</span> <span class="o">(</span><span class="bp">λ</span><span class="n">n</span><span class="o">,</span> <span class="n">u</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">t</span><span class="o">)</span> <span class="n">F</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">assume</span> <span class="bp">⟨</span><span class="n">su</span><span class="o">,</span> <span class="n">suF</span><span class="o">,</span> <span class="n">tu</span><span class="o">,</span> <span class="n">tuH</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">eventually</span> <span class="o">(</span><span class="bp">λ</span><span class="n">n</span><span class="o">,</span> <span class="n">u</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">tu</span><span class="o">)</span> <span class="n">F</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">apply</span> <span class="n">filter</span><span class="bp">.</span><span class="n">upwards_sets</span> <span class="n">F</span> <span class="n">suF</span><span class="o">,</span>
    <span class="k">assume</span> <span class="o">(</span><span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">Hy</span><span class="o">),</span>
    <span class="n">apply</span> <span class="n">tuH</span> <span class="bp">_</span> <span class="o">(</span><span class="n">mem_image_of_mem</span> <span class="bp">_</span> <span class="n">Hy</span><span class="o">)</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="bp">⟨</span><span class="n">tu</span><span class="o">,</span> <span class="k">by</span> <span class="n">assumption</span><span class="bp">⟩</span><span class="o">,</span>
<span class="k">have</span> <span class="n">B</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span><span class="n">t</span><span class="o">,</span> <span class="n">eventually</span> <span class="o">(</span><span class="bp">λ</span><span class="n">n</span><span class="o">,</span> <span class="n">u</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">t</span><span class="o">)</span> <span class="n">F</span><span class="o">)</span> <span class="bp">→</span> <span class="n">eventually_bdd_above</span> <span class="n">F</span> <span class="n">u</span> <span class="o">:=</span>
  <span class="k">assume</span> <span class="bp">⟨</span><span class="n">t</span><span class="o">,</span> <span class="n">Ht</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">bdd_above</span> <span class="o">(</span><span class="n">u</span> <span class="err">&#39;&#39;</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">u</span> <span class="n">y</span> <span class="bp">≤</span> <span class="n">t</span><span class="o">})</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">apply</span> <span class="n">bdd_above</span><span class="bp">.</span><span class="n">mk</span> <span class="n">t</span><span class="o">,</span>
    <span class="k">assume</span> <span class="o">(</span><span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">Hy</span><span class="o">),</span>
    <span class="n">induction</span> <span class="n">Hy</span> <span class="k">with</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
    <span class="n">simpa</span> <span class="o">[</span><span class="n">Hx</span><span class="bp">.</span><span class="mi">2</span><span class="o">]</span> <span class="kn">using</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="bp">⟨</span><span class="o">{</span><span class="n">y</span> <span class="bp">|</span> <span class="n">u</span> <span class="n">y</span> <span class="bp">≤</span> <span class="n">t</span><span class="o">},</span> <span class="k">by</span> <span class="n">assumption</span><span class="o">,</span> <span class="k">by</span> <span class="n">assumption</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">⟨</span><span class="n">A</span><span class="o">,</span> <span class="n">B</span><span class="bp">⟩</span>
</pre></div>


<p>and then I compacted it to</p>
<div class="codehilite"><pre><span></span><span class="bp">⟨λ</span> <span class="bp">⟨</span><span class="n">su</span><span class="o">,</span> <span class="n">suF</span><span class="o">,</span> <span class="n">tu</span><span class="o">,</span> <span class="n">tuH</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">tu</span><span class="o">,</span> <span class="n">filter</span><span class="bp">.</span><span class="n">upwards_sets</span> <span class="n">F</span> <span class="n">suF</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="n">Hy</span><span class="o">,</span> <span class="n">tuH</span> <span class="bp">_</span> <span class="o">(</span><span class="n">mem_image_of_mem</span> <span class="bp">_</span> <span class="n">Hy</span><span class="o">))</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">t</span><span class="o">,</span> <span class="n">Ht</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="o">{</span><span class="n">y</span> <span class="bp">|</span> <span class="n">u</span> <span class="n">y</span> <span class="bp">≤</span> <span class="n">t</span><span class="o">},</span> <span class="n">Ht</span><span class="o">,</span> <span class="n">t</span><span class="o">,</span> <span class="o">(</span><span class="bp">λ</span><span class="n">y</span> <span class="n">Hy</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">Hx</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">Hy</span> <span class="k">in</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">Hx</span><span class="bp">.</span><span class="mi">2</span><span class="o">]</span> <span class="kn">using</span> <span class="n">Hx</span><span class="o">)</span><span class="bp">⟩⟩</span>
</pre></div>


<p>Do you have an opinion on the readability of both, and which one I should keep?</p>

#### [ Moses Schönfinkel (Apr 18 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125266974):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> They're reasonably well established in a few specific areas, almost exclusively related to software verification. Are you talking widespread adoption by mathematicians and in general, people who use formal apparatus of any kind?</p>

#### [ Andrew Ashworth (Apr 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267209):
<p>i like non-compacted proofs, although the mathlib developers disagree with me <span class="emoji emoji-1f600" title="grinning">:grinning:</span></p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267224):
<p>I think it depends on your audience.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267229):
<p>If you want to get it into mathlib then if you wrote the long one they would squish it down to the short one themselves</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267240):
<p>If you want to explain to a bunch of undergraduates how Lean works then I would definitely not recommend the short one</p>

#### [ Mario Carneiro (Apr 18 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267303):
<p>there is plenty of space for big proofs in TPIL and similar works</p>

#### [ Andrew Ashworth (Apr 18 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267345):
<p><span class="user-mention" data-user-id="110027">@Moses Schönfinkel</span> yes. it doesn't even have that many inroads into high-assurance software, which is all written in things like MISRA C</p>

#### [ Johannes Hölzl (Apr 18 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267350):
<p>For simple statements like this I prefer the later proof (btw: you can even reduce it more: <code>λy Hy, let ⟨x, Hx⟩ := Hy in  ~&gt; λy ⟨x, Hx⟩,</code>). But the more complicated the proof itself is, especially when the proof goes over a couple of lines, I prefer the more elaborate one.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267433):
<p>In fact Johannes taught me a valuable lesson regarding this sort of thing (which you already know Sebastian) -- it's a very good exercise, at some point in your Lean career, to start trying to write the shortest proofs you possibly can.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267442):
<p>because this game just teaches you stuff, or perhaps teaches you to appreciate certain things</p>

#### [ Kevin Buzzard (Apr 18 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267448):
<p>which you might otherwise miss.</p>

#### [ Sebastien Gouezel (Apr 18 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267549):
<p>Agreed. To be able to compactify the proof, I needed to understand much more of what is going on.</p>

#### [ Johannes Hölzl (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267682):
<p>The problem with compact proofs is of course, that it is hard to ever change the definition of constants. As the often rely on definitional equality. There using automation has a big advantage, as it is often configurable like the simplifier.</p>

#### [ Andrew Ashworth (Apr 18 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267683):
<p>compact proofs / programs are painful to me. as someone who was tasked with fixing an old scientific c program from the 80s for several months, terseness is the great enemy</p>

#### [ Patrick Massot (Apr 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267849):
<p>What about having the goal that people could learn stuff from reading proofs?</p>

#### [ Patrick Massot (Apr 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267852):
<p>In ordinary maths this is a pretty important idea</p>

#### [ Patrick Massot (Apr 18 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125267932):
<p>Of course we could completely separate the explanation of a theorem from its proof using Lean. But that wouldn't help people learning how to convince Lean that something is true</p>

#### [ Kevin Buzzard (Apr 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269848):
<p>What about having the goal that in between the incomprehensible lines of Lean code there are comments explaining what is going on, so people can learn from the comments?</p>

#### [ Johan Commelin (Apr 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269853):
<p>I think readability is extremely important for people to have confidence in formalisations. I am sure you all know the paper by Pollack, "How to believe a machine-checked proof": <a href="http://www.brics.dk/RS/97/18/BRICS-RS-97-18.pdf" target="_blank" title="http://www.brics.dk/RS/97/18/BRICS-RS-97-18.pdf">http://www.brics.dk/RS/97/18/BRICS-RS-97-18.pdf</a></p>

#### [ Johan Commelin (Apr 18 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269859):
<p>I think he has very good points</p>

#### [ Johan Commelin (Apr 18 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269962):
<p>For example, if the statement of Ramanujan's conjecture uses modular forms, then I need to understand the formalisation of the definition of modular forms as well. And if they are defined as sections of some line bundle on a modular curve, then I need to understand those as well...</p>

#### [ Johan Commelin (Apr 18 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125269972):
<p>If there is one typo in those definitions... then the proof of Ramanujan's conjecture might not actually be a proof.</p>

#### [ Johan Commelin (Apr 18 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125270026):
<p>That is why theorems with simple statements should have extremely readable and simple formalisations</p>

#### [ Johan Commelin (Apr 18 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125270044):
<p>And afterwards, there might be theorems that say the statement is equivalent to some other statement using involved definitions, which you then go on to prove...</p>

#### [ Johan Commelin (Apr 18 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20resolution%20or%20unification%3F/near/125270068):
<p>On the other hand, maybe my rant does not have much bearing on readability of <em>proofs</em>...</p>


{% endraw %}
