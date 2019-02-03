---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05564chainrule.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [chain rule](https://leanprover-community.github.io/archive/113488general/05564chainrule.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Feb 28 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123090490):
<p>I have this chain rule proof in <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean</a> which 100 lines long. And <span class="user-mention" data-user-email="assia.mahboubi@inria.fr" data-user-id="110172">@Assia Mahboubi</span> tells me <a href="https://github.com/math-comp/analysis/blob/6b36593f4a6a612212163b25c6bad3522c7fa679/derive.v#L494" target="_blank" title="https://github.com/math-comp/analysis/blob/6b36593f4a6a612212163b25c6bad3522c7fa679/derive.v#L494">https://github.com/math-comp/analysis/blob/6b36593f4a6a612212163b25c6bad3522c7fa679/derive.v#L494</a></p>

#### [ Patrick Massot (Feb 28 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123090492):
<p>What is the miracle here? Is it proving stuff about o and O notations?</p>

#### [ Chris Hughes (Feb 28 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123102048):
<p>I don't know anything about that proof in particular, but what I have noticed is that it's good practice to never prove too much in one go, and extract as many lemmas as possible. <br>
Stuff like <code>add_halves</code>, and <code>exists_forall_ge_and</code> are the sorts of things Mario has extracted, when a pattern comes up very often<br>
Some of it is just style to make things shorter, for example, if <code>D</code> and <code>D'</code> were moved after the <code>:</code>, the first seven lines of the proof could be shortened to</p>
<div class="codehilite"><pre><span></span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">cont_lin_l</span><span class="o">,</span> <span class="n">ε</span><span class="o">,</span> <span class="n">TEf</span><span class="o">,</span> <span class="n">lim_ε</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">cont_lin_P</span><span class="o">,</span> <span class="n">η</span><span class="o">,</span> <span class="n">TEg</span><span class="o">,</span> <span class="n">lim_η</span><span class="bp">⟩</span><span class="o">,</span>
<span class="k">let</span> <span class="n">cont_linPL</span> <span class="o">:=</span> <span class="n">is_bounded_linear_map</span><span class="bp">.</span><span class="n">comp</span> <span class="n">cont_lin_L</span> <span class="n">cont_lin_P</span> <span class="k">in</span>
<span class="bp">⟨</span><span class="n">cont_linPL</span><span class="o">,</span> <span class="k">begin</span> <span class="bp">...</span>
</pre></div>


<p><code>unfold is_differential</code> is probably unnecessary as <code>split</code> does that for you<br>
lines 78 to 85 could be moved into a couple of lines in term mode, possibly even without the <code>simp</code>s at the start, if all they do is unfold definitional equalities<br>
<code>simp [δ], simp [H]</code>, can probably be shortened to <code>simp [δ, H]</code><br>
Also the lines of calc could possibly be shortened to one line of rw or simp, when it's just equality that needs to be proved.</p>
<p>My experience is that you really have to pay attention to matters of style like this if you make a mathlib PR</p>

#### [ Mario Carneiro (Feb 28 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123102296):
<p>The reason Assia's proof is so short is because almost all the work is in the previous lemma <code>dcomp</code> (and possibly also <code>compOo_eqo</code>)</p>

#### [ Patrick Massot (Feb 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123106492):
<p>I understand that some stuff is split into several lemmas, but it still doesn't seem to be 100 lines long</p>

#### [ Simon Hudon (Feb 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123106699):
<p>It might be one of those "the whole is more than the sum of its parts" situation. It's surprising sometimes how much you shrink your code by choosing abstract interfaces between components.</p>

#### [ Patrick Massot (Feb 28 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123106851):
<p><span class="user-mention" data-user-email="chrishughes24@gmail.com" data-user-id="110044">@Chris Hughes</span>  thank you for your comments. I agree about the first seven lines, although I'm not sure it improves readability. I thought about simplifying <code>simp [δ], simp [H]</code> to <code>simp [δ, H]</code> but it doesn't work. The calc lines are compressed as much as I could: I could get it to worked when skipping any step.</p>

#### [ Damien Rouhling (Mar 01 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129650):
<p>Hello everyone.<br>
I am the author of the proof Assia told you about. All in all, my proof is also 100 lines long if you take into account the lemmas I had to prove for this:<br>
-  <code>linear_lipschitz</code> and its consequence <code>linear_eqO</code> to state that a continuous linear function is a O(id) at 0<br>
- the two composition rules for O(id) and o(id) at 0: <code>compOo_eqo</code>and <code>compoO_eqo</code>.<br>
The remaining is just manipulation of asymptotic expansions. No miracle in here :-)</p>

#### [ Patrick Massot (Mar 01 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129709):
<p><code>linear_lipschitz</code> is not included in my version, it is in <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L116" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L116">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L116</a></p>

#### [ Patrick Massot (Mar 01 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129724):
<p>I don't know if Assia gave you the context though: I'm not a all an expert in Lean or any other proof assistant, I'm a regular mathematician would fancies trying proof assistants and started three months ago</p>

#### [ Patrick Massot (Mar 01 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129773):
<p>I was interested in understanding what kind of support for o and O you managed to setup. But it's very hard for me to read Coq, especially SSReflect style</p>

#### [ Patrick Massot (Mar 01 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129778):
<p>Can you do computations with o and O floating around in the middle of formulas?</p>

#### [ Patrick Massot (Mar 01 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129781):
<p>Or only state as an hypothesis or conclusion that f = o(g)?</p>

#### [ Damien Rouhling (Mar 01 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129845):
<p>We have rewriting rules for o and O so we can indeed manipulate such expressions.</p>

#### [ Patrick Massot (Mar 01 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123129853):
<p>Arggg, I'm required for more serious stuff. I'm on vacations and it's time to go skiing with my daughters (I can no longer follow my 10 years old son but I'm still a God skier to my 4 and 7 years old daughters). I will very carefully read whatever you'll write when I'll come back</p>

#### [ Damien Rouhling (Mar 01 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123130268):
<p>In order to prove that f = o(g) we have two possibilities:<br>
- go back to the definition of o(g), that's what I do for <code>compOo_eqo</code> for instance<br>
- use rewriting rules to change the goal into o(g) = o(g).<br>
Our notation for o(g) hides a function, which has the property to be a o(g). So the goal f = o(g) is an equality between two functions and after using rewriting rules the goal o(g) = o(g) is an equality between functions too. These can be different so we have a mean to replace the hidden function in f = o(g) with an existential variable so that unification will close the goal o(g) = o(g).</p>

#### [ Cyril Cohen (Mar 01 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123130338):
<p>We have a draft paper here about this: <a href="https://hal.inria.fr/hal-01719918" target="_blank" title="https://hal.inria.fr/hal-01719918">https://hal.inria.fr/hal-01719918</a></p>

#### [ Patrick Massot (Mar 01 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138004):
<p>Nice! <span class="emoji emoji-1f60d" title="heart eyes">:heart_eyes:</span> <span class="user-mention" data-user-email="di.gama@gmail.com" data-user-id="110049">@Mario Carneiro</span> please, please, please, can we have this little-o and big-O magic in mathlib?</p>

#### [ Patrick Massot (Mar 01 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138057):
<p><span class="user-mention" data-user-email="cyril.cohen@inria.fr" data-user-id="110193">@Cyril Cohen</span> <span class="user-mention" data-user-email="damien.rouhling@ens-lyon.org" data-user-id="110231">@Damien Rouhling</span> I would be a very nice way to learn Lean to translate this to Lean. I'm sure you understand that your goal of having asymptotic reasoning that looks natural to mathematicians is completely blocked by shortcomings of Coq notations. With Lean you could have much more natural notations</p>

#### [ Patrick Massot (Mar 01 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138123):
<p>Where is Johannes? It seems he didn't come from Gitter to here. He should see this.</p>

#### [ Cyril Cohen (Mar 01 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138178):
<p><span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span> in this case Coq notations are not "blocking" because we hack around the shortcommings.</p>

#### [ Cyril Cohen (Mar 01 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138281):
<p>Most of the "magic" of our little-o and big-O notation happen in the use of existential variables to delay their instantiation until a stage where they appear in the goal. And of course in splitting the proof into the parts that depend only in little-o/big-O arithmetic and parts that depend only on linearity.</p>

#### [ Patrick Massot (Mar 01 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138282):
<p>I think you are so much used to SSReflect notations that can't see how weird they look</p>

#### [ Patrick Massot (Mar 01 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138287):
<p>Have you seen the <code>calc</code> blocks in my proof? This looks like mathematics to a mathematician eyes</p>

#### [ Patrick Massot (Mar 01 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138299):
<p>I agree about delayed existential. The definition of delta very early in my proof is clearly the weirdest aspect for a mathematician</p>

#### [ Patrick Massot (Mar 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138357):
<p><a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L41" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L41">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L41</a> and <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L129" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L129">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L129</a> completely kill the illusion of being doing maths</p>

#### [ Cyril Cohen (Mar 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138439):
<p>I see your <code>calc</code>, that's what the mathematician should see, but do you like to explain line by line the new members of your equalities? Personally I prefer giving fewer explicit terms, and more unambiguous instructions... and letting the proof assistant show me where I am,... is it not a matter of taste?<br>
How the notation f = g + o (e) looks exactly is another debate IMHO, and I think you are right, Coq gets in the way to get the most readable notation possible...</p>

#### [ Patrick Massot (Mar 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138479):
<p>But <code>@^~_ @ F</code> from line 38 of your paper...</p>

#### [ Cyril Cohen (Mar 01 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138515):
<blockquote>
<p><a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L41" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L41">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L41</a> and <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L129" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L129">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/continuous_linear_maps.lean#L129</a> completely kill the illusion of being doing maths</p>
</blockquote>
<p>I am happy to hear you say this, and this is exactly the point of the above mentioned code and paper.</p>

#### [ Patrick Massot (Mar 01 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138565):
<p>Yes I understand, here my <span class="emoji emoji-1f60d" title="heart eyes">:heart_eyes:</span> reaction</p>

#### [ Cyril Cohen (Mar 01 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138657):
<blockquote>
<p>But <code>@^~_ @ F</code> from line 38 of your paper...</p>
</blockquote>
<p>...looks cryptic... I realize that now. Is it that bad?</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138704):
<p>I didn't know you could embed Perl into Coq!</p>

#### [ Cyril Cohen (Mar 01 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138707):
<p>bad -&gt; difficult to read</p>

#### [ Moses Schönfinkel (Mar 01 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138717):
<p>Be careful what you say around Coq people. Next thing you know there's "Cerl" or "Peroq".</p>

#### [ Patrick Massot (Mar 01 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138728):
<p>In Lean you could write "bad → difficult to read". Unicode symbols is the default option</p>

#### [ Patrick Massot (Mar 01 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138734):
<p>No ascii art notation</p>

#### [ Patrick Massot (Mar 01 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138806):
<blockquote>
<p>...looks cryptic... I realize that now. Is it that bad?</p>
</blockquote>
<p>It's not much worse than <code>g =&gt; /=.</code></p>

#### [ Patrick Massot (Mar 01 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138952):
<p>But even removing SSReflect from the discussion,  in Lean you could replace <code>\forall k \near +oo, \forall x \near F, ‘|[f x]| &lt;= k * ‘|[g x]|.</code> by <br>
<code>∀ k near +∞, ∀ x near F, |f x| ≤ k*|g x|</code>. I'm sorry I'm totally incompetent at discussing anything deep in dependent type theory, I only tell you what an average mathematician sees when starting using a proof assistant.</p>

#### [ Patrick Massot (Mar 01 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138979):
<p>And my kids need me again (nap time ended), sorry</p>

#### [ Cyril Cohen (Mar 01 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123138982):
<p>I can totally agree with your last remark.</p>

#### [ Patrick Massot (Mar 01 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139061):
<p>Maybe mathematicians will never use proof assistants, I don't know. But I'm 100% sure they will never use a proof assistant using alien notations</p>

#### [ Cyril Cohen (Mar 01 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139065):
<p>Coq notation system makes us take solutions that are not satisfactory.<br>
(the debate about <code>=&gt; /=</code> and <code>@~_</code> and "Cerl" and "Peroq" is totally different)</p>

#### [ Patrick Massot (Mar 01 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139131):
<p>I don't know if Coq can be "fixed" or if you should switch to Lean to get nice notations (and I have <em>no idea</em> about deeper reasons to choose one or the other). But I can tell you that notations (and the awesomeness of <em>Theorem proving in Lean</em>) is what made me start using Lean instead of Coq (remember I have no CS training at all)</p>

#### [ Patrick Massot (Mar 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139140):
<p>And now I really have to go. See you!</p>

#### [ Cyril Cohen (Mar 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139142):
<p>(the difference is in your last example the symbols correspond to usual mathematical practice, and in the "Cerl" criticism symbols that are introduced by programs or proof scripts, and both suffer from the lack of expressivness of Coq notation system)</p>

#### [ Cyril Cohen (Mar 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139144):
<p><span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span> see you later</p>

#### [ Moses Schönfinkel (Mar 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123139145):
<p>I love SSreflect notation! I think ever since APL they've been building resistance in CS people to horrible notation (to the point where conciseness looks strangely appealing).</p>

#### [ Johannes Hölzl (Mar 02 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123180953):
<p>Cyril showed me the <code>near</code> tactics at the TYPES meeting in Nijmegen a month ago. And indeed, they looks very nice! Modulo ssreflect which I still can't read :)</p>

#### [ Patrick Massot (Mar 02 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123180990):
<p>Would it be an awful lot of work to adapt this to Lean and have them in mathlib?</p>

#### [ Johannes Hölzl (Mar 02 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123181067):
<p>I'm not sure what's the best way to do it in Lean. One way would be to introduce a new tactic mode (like the <code>smt</code> or <code>conv</code> modes). But all we want is to add data and hide metavariables, so that we can take care of them later.</p>

#### [ Cyril Cohen (Mar 02 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123182527):
<blockquote>
<p>Cyril showed me the <code>near</code> tactics at the TYPES meeting in Nijmegen a month ago. And indeed, they looks very nice! Modulo ssreflect which I still can't read :)</p>
</blockquote>
<p>Hi <span class="user-mention" data-user-email="johannes.hoelzl@gmx.de" data-user-id="110294">@Johannes Hölzl</span> ! How are you? In Nijmegen I did show you near tactics but I did not have the time to show you the little-o and big-O notations and arithmetic. I might want to take a look at that too.</p>

#### [ Johannes Hölzl (Mar 02 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123182544):
<p>Oh yes, it's on my list!</p>

#### [ Patrick Massot (Mar 02 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123182545):
<p>Great!</p>

#### [ Patrick Massot (Mar 05 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123317833):
<p><span class="user-mention" data-user-email="johannes.hoelzl@gmx.de" data-user-id="110294">@Johannes Hölzl</span> is today's filter commit related to the discussion in this topic?</p>

#### [ Johannes Hölzl (Mar 05 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123318060):
<p>not directly . This was a change I had flying around since a couple of month. But I implemented <code>filter_upwards</code> when <span class="user-mention" data-user-email="cyril.cohen@inria.fr" data-user-id="110193">@Cyril Cohen</span>  showed me his filter-tactics. It is a much simpler implementation, its what is available in Isabelle.<br>
For a goal of the form <code>s \in f.sets</code> and terms for <code>h1 : t1 \in f.sets</code> ...  <code>hn : tn \in f.sets</code> one gets the new goal:<br>
<code>\forall x, x \in t1 -&gt; .. -&gt; x \in tn -&gt; x \in s</code><br>
(I will add this as docstring)</p>

#### [ Patrick Massot (Mar 05 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/chain%20rule/near/123318874):
<p>Ok, thanks. Do you think you'll try to adapt the full thing at some point? Or is it too much work for something which wouldn't be new (hence not publishable)?</p>


{% endraw %}
