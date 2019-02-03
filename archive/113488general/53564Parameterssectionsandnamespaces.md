---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53564Parameterssectionsandnamespaces.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Parameters, sections and namespaces](https://leanprover-community.github.io/archive/113488general/53564Parameterssectionsandnamespaces.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mark Dickinson (Dec 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152645325):
<p>I've just encountered the fact that parameters behave differently inside and outside namespaces, and was wondering whether anyone has either an explanation or a pointer to documentation. Here's a toy example (cut down from a real one):</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">anon</span>

<span class="kn">parameters</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">a_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span>
<span class="n">include</span> <span class="n">a_pos</span>

<span class="kn">lemma</span> <span class="n">a2_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="n">mul_pos</span> <span class="n">a_pos</span> <span class="n">a_pos</span>
<span class="kn">lemma</span> <span class="n">a3_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="n">mul_pos</span> <span class="n">a2_pos</span> <span class="n">a_pos</span>
<span class="kn">lemma</span> <span class="n">a3_pos_bis</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exact</span> <span class="n">mul_pos</span> <span class="n">a2_pos</span> <span class="n">a_pos</span>

<span class="kn">end</span> <span class="n">anon</span>
</pre></div>


<p>Here, as expected from the documentation, <code>a2_pos</code> has <code>a_pos</code> as a premise outside the section, but within the section it's supplied implicitly. My problem arose when I moved the real code that the above was adapted from to within a namespace:</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">bob</span>
<span class="kn">section</span> <span class="n">anon</span>

<span class="kn">parameters</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">a_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span>
<span class="n">include</span> <span class="n">a_pos</span>

<span class="kn">lemma</span> <span class="n">a2_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="n">mul_pos</span> <span class="n">a_pos</span> <span class="n">a_pos</span>
<span class="kn">lemma</span> <span class="n">a3_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="n">mul_pos</span> <span class="n">a2_pos</span> <span class="n">a_pos</span>
<span class="kn">lemma</span> <span class="n">a3_pos_bis</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exact</span> <span class="n">mul_pos</span> <span class="n">a2_pos</span> <span class="n">a_pos</span>  <span class="c1">-- Lean unhappy here</span>

<span class="kn">end</span> <span class="n">anon</span>
<span class="kn">end</span> <span class="n">bob</span>
</pre></div>


<p>Now I've got the dreaded red squigglies under <code>mul_pos</code> on the <code>a3_pos_bis</code> line, and to banish them I have to replace <code>a2_pos</code> with <code>(a2_pos a_pos)</code>, but _only_ for the tactic proof. In the direct proof of <code>a3_pos</code>, I have to use <code>a2_pos</code> rather than <code>(a2_pos a_pos)</code>.</p>
<p>What are the rules here, and are they documented anywhere?</p>

#### [ Mario Carneiro (Dec 28 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646780):
<p>Inside tactics, parameters don't work</p>

#### [ Mario Carneiro (Dec 28 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646785):
<p>all theorems look like they would outside the section</p>

#### [ Mario Carneiro (Dec 28 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646794):
<p>you can work around this by using local notations instead, as in <code>local notation `a2_pos` := a2_pos a_pos</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646862):
<p>also using the explicit name seems to help, as in <code>mul_pos bob.a2_pos a_pos</code></p>

#### [ Mark Dickinson (Dec 28 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646873):
<p>Thanks! But I'm confused: in the top example (which does work), isn't this exactly an example of parameters working inside a tactic?</p>

#### [ Mario Carneiro (Dec 28 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646928):
<p>I think the fact that the real name of <code>a2_pos</code> is <code>bob.a2_pos</code> has something to do with it in the second example</p>

#### [ Mario Carneiro (Dec 28 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646943):
<p>I generally avoid parameters because they are kind of flaky when you use tactics</p>

#### [ Mario Carneiro (Dec 28 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646951):
<p>it's really just a notation, and lean doesn't hide this very well</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152646996):
<p>Okay, thanks.</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647058):
<p>So I get the sense I'm abusing Lean here; I probably need to change my approach. I have a train of lemmas leading up to a main theorem, with a whole bunch of definitions, hypotheses, etc. common to all. As a mathematician, I'd declare the variables and assumptions at the start of a section, then make use of them within the section; parameters seemed like the right fit for this.</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647075):
<p>I don't really want to have to explicitly include the necessary hypotheses in each lemma; that would be repetitive and painful. The alternative seems to be to embed everything within the proof of the main theorem; maybe that's the way to go.</p>

#### [ Kenny Lau (Dec 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647120):
<p>... or you can use <code>variables</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647121):
<p>You can package up all the hypotheses into a definition</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647125):
<p>Hmm; that could work.</p>

#### [ Mario Carneiro (Dec 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647132):
<p>in theory parameters are the way to go, but they just don't work very well</p>

#### [ Kenny Lau (Dec 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647135):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">bob</span>
<span class="kn">section</span> <span class="n">anon</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">a_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">)</span>
<span class="n">include</span> <span class="n">a_pos</span>

<span class="kn">lemma</span> <span class="n">a2_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="n">mul_pos</span> <span class="n">a_pos</span> <span class="n">a_pos</span>
<span class="kn">lemma</span> <span class="n">a3_pos</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="n">mul_pos</span> <span class="o">(</span><span class="n">a2_pos</span> <span class="n">a_pos</span><span class="o">)</span> <span class="n">a_pos</span>
<span class="kn">lemma</span> <span class="n">a3_pos_bis</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">*</span><span class="n">a</span><span class="bp">*</span><span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exact</span> <span class="n">mul_pos</span> <span class="o">(</span><span class="n">a2_pos</span> <span class="n">a_pos</span><span class="o">)</span> <span class="n">a_pos</span>  <span class="c1">-- Lean unhappy here</span>

<span class="kn">end</span> <span class="n">anon</span>
<span class="kn">end</span> <span class="n">bob</span>
</pre></div>

#### [ Mario Carneiro (Dec 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647184):
<p>If the lemmas all represent major parts of the main theorem, it's not a bad idea to explicitly <code>have</code> each of them in the main theorem, passing in all the assumptions</p>

#### [ Kenny Lau (Dec 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647193):
<p>anyway it would be better if you have some practical examples</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647205):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I do, but they're long. :-)</p>

#### [ Mario Carneiro (Dec 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647206):
<p>for an example like the above that approach would be a bit too "heavyweight", but presumably your real example is larger and might warrant it</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647255):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Yes, moving things into the main theorem sounds like the right approach.</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647721):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> FWIW, here's the real example code that I was attempting to put into a namespace (mostly because I want to be able to make local definitions): <a href="https://github.com/mdickinson/snippets/blob/master/proofs/isqrt/src/isqrt.lean#L380-L500" target="_blank" title="https://github.com/mdickinson/snippets/blob/master/proofs/isqrt/src/isqrt.lean#L380-L500">https://github.com/mdickinson/snippets/blob/master/proofs/isqrt/src/isqrt.lean#L380-L500</a></p>

#### [ Kenny Lau (Dec 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647727):
<p>we already have isqrt though</p>

#### [ Kenny Lau (Dec 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647734):
<p>oh it's a different purpose</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647809):
<p>Yes, I know. :-)  I'm not trying to define isqrt. I'm proving that a particular algorithm for computing integer sqrt that I care about (because it's useful in another language) is valid.</p>

#### [ Mark Dickinson (Dec 28 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152647916):
<p>I was trying to tidy this section of the proof up by fixing all the repetition of <code>let a := M*d + n / (4*M*d) in ...</code>. Making <code>a</code> a definition in the section seems like the obvious way to do this, but has the issue that then I can't use <code>a</code> later on because it's already taken for that definition; I only really want a local definition. So I tried to use namespaces to contain the definition, and that's when things started to go wrong. :-(</p>

#### [ Mark Dickinson (Dec 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152649070):
<p>Quick followup: the specific issue I was running into was already reported here: <a href="https://github.com/leanprover/lean/issues/1773" target="_blank" title="https://github.com/leanprover/lean/issues/1773">https://github.com/leanprover/lean/issues/1773</a>. (I _did_ search the GitHub issues before posting; honest!)</p>

#### [ Mario Carneiro (Dec 28 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152653413):
<p>Do you know how this algorithm compares to the algorithm for <code>nat.sqrt</code>, which is also a binary algorithm? That one has a proof already</p>

#### [ Mark Dickinson (Dec 28 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152653940):
<p>Well, for Python (which is what I actually care about in this case), it's hundreds of times faster for (for example) crypto-size integers (by which I mean a few hundred to a few thousand digits).</p>

#### [ Mark Dickinson (Dec 28 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654012):
<p>It's basically Newton–Raphson with steadily increasing working precision, so takes many fewer steps than the bit-by-bit approach that <code>nat.sqrt</code> uses (at least if I'm understanding it correctly).</p>

#### [ Mark Dickinson (Dec 28 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654170):
<p>It's not a world away from the GMP integer square root algorithm, which has been verified in Coq (in a paper by Yves Bertot, Nicolas Magaud, and Paul Zimmermann), except that their algorithm needs a possible correction at every step, and this one only needs a single possible correction at the end.</p>

#### [ Kevin Buzzard (Dec 28 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654340):
<p>Hi Mark! How do running times in Lean and python compare?</p>

#### [ Mario Carneiro (Dec 28 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654346):
<p>python certainly wins hands down</p>

#### [ Mario Carneiro (Dec 28 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152654469):
<p>For the main recursion in <code>isqrt_aux</code>, you should use <code>binary_rec_on</code> which is implemented with bit shifts</p>

#### [ Reid Barton (Dec 28 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152655105):
<blockquote>
<p>So I get the sense I'm abusing Lean here; I probably need to change my approach. I have a train of lemmas leading up to a main theorem, with a whole bunch of definitions, hypotheses, etc. common to all. As a mathematician, I'd declare the variables and assumptions at the start of a section, then make use of them within the section; parameters seemed like the right fit for this.</p>
</blockquote>
<p>I like this style a lot (for example see <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/topological_spaces/pushout_lemmas.lean#L163" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/topological_spaces/pushout_lemmas.lean#L163">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/topological_spaces/pushout_lemmas.lean#L163</a>), and so I have a small bag of tricks for working around the issue with tactics, including "avoid tactics" and a trick with <code>let</code> I described here: <a href="#narrow/stream/113488-general/subject/parameters.20and.20tactics/near/148863078" title="#narrow/stream/113488-general/subject/parameters.20and.20tactics/near/148863078">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/parameters.20and.20tactics/near/148863078</a></p>

#### [ Reid Barton (Dec 28 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152655288):
<p>Or sometimes the path of least resistance is just to supply the parameters manually when you use one of your lemmas from within a tactic.</p>

#### [ Mark Dickinson (Dec 28 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152662761):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Re: running times; I'm afraid I have little idea. I know a bit about the Python side, but very little about the Lean side, so don't have much basis for comparison. CPython's bigint implementation is basic and simple (nothing like GMP), but it's well written and  does pretty well in practice provided you don't try to use hundred-thousand digit integers (which isn't really the target anyway). With one exception, complexities are the ones you'd expect from the usual school-taught algorithms: linear time for addition, subtraction, left and right shifts and other bitwise operations, quadratic time for division. Multiplication uses Karatsuba's algorithm when the number of bits gets large enough, so is subquadratic. (Disclaimer: I've done a bit of hacking on Python's bigint implementation over the years, so I'm biased.)</p>

#### [ Mark Dickinson (Dec 28 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152662811):
<p>I think SAGE uses GMP-based integers instead of Python bigints, which makes sense given the target audience.</p>

#### [ Mark Dickinson (Dec 28 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152662918):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks; I'll give <code>binary_rec_on</code> a try. Though part of my aim here is to keep the <code>isqrt</code> and <code>isqrt_aux</code> code as close as possible to the Python equivalents, so that it's evident that there are no errors in translation.</p>

#### [ Mark Dickinson (Dec 28 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Parameters%2C%20sections%20and%20namespaces/near/152663078):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Thanks for the tips and links! I'll take a look shortly. At this point I'm finding other people's code to be by far the best resource for learning how to use Lean better.</p>


{% endraw %}
