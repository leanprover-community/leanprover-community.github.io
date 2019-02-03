---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52683unexpectedlylong.html
---

## Stream: [general](index.html)
### Topic: [unexpectedly long](52683unexpectedlylong.html)

---


{% raw %}
#### [ Kenny Lau (Sep 28 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134828020):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>

<span class="kn">open</span> <span class="n">finset</span> <span class="n">lattice</span>

<span class="kn">set_option</span> <span class="n">profiler</span> <span class="n">true</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">sup_le</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span><span class="n">b</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="bp">→</span> <span class="n">s</span><span class="bp">.</span><span class="n">sup</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_eq</span> <span class="n">β</span><span class="bp">;</span> <span class="k">from</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">bot_le</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">})</span>
<span class="c1">-- why so long?</span>
</pre></div>

#### [ Kenny Lau (Sep 28 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134828031):
<p>takes somewhere between 5s and 30s to compile</p>

#### [ Simon Hudon (Sep 28 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134829320):
<p>Is the time spent on <code>simp</code>?</p>

#### [ Kenny Lau (Sep 28 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134829840):
<p>I think so</p>

#### [ Kenny Lau (Sep 28 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134829940):
<p>btw that's <code>finset.sup_le</code></p>

#### [ Kenny Lau (Sep 28 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134829952):
<p>that's right, a 10s-lemma is inside mathlib</p>

#### [ Simon Hudon (Sep 28 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134839187):
<p>I'm planning on writing a tactic today <code>squeeze_simp</code> that will call <code>simp</code> and print a minimized <code>simp only</code> version. That might help in your endeavor</p>

#### [ Simon Hudon (Sep 28 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134839219):
<p>I can automate the application of the suggestion in emacs but I don't know how to do the same with VS code</p>

#### [ Johan Commelin (Sep 28 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134839421):
<p>Register it as a hole command, like <code>tidy</code> does.</p>

#### [ Simon Hudon (Sep 28 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134839603):
<p>Is that a mechanism of VS Code?</p>

#### [ Johan Commelin (Sep 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840062):
<p>No, it's a Lean thing</p>

#### [ Johan Commelin (Sep 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840104):
<p>I think it is a type class</p>

#### [ Johan Commelin (Sep 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840132):
<p>But I guess IDE's also have to hook into it. But this is a one time thing that has been done already</p>

#### [ Simon Hudon (Sep 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840140):
<p>Thanks! I'm looking at the <code>tidy</code> code, it's actually an attribute</p>

#### [ Simon Hudon (Sep 28 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840156):
<p>Cool</p>

#### [ Reid Barton (Sep 28 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840173):
<p>Simon have you determined yet whether the emacs mode already supports hole commands? I haven't looked</p>

#### [ Johan Commelin (Sep 28 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840284):
<p>I thought emacs always supported the supremum of the features of all other IDE's<br>
By definition</p>

#### [ Simon Hudon (Sep 28 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840326):
<p>It is indeed emacs definition</p>

#### [ Simon Hudon (Sep 28 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840382):
<p>It does support hole commands, at least three that I have seen</p>

#### [ Johan Commelin (Sep 28 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840401):
<p>Since <code>tidy</code> there should be 4</p>

#### [ Simon Hudon (Sep 28 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840430):
<p>I confirm that I can now see tidy in that list too</p>

#### [ Simon Hudon (Sep 28 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840456):
<p>I like the idea of the type hole but it has a down side: if you're replacing <code>simp</code> in a file, you have to do it one at a time.</p>

#### [ Reid Barton (Sep 28 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840547):
<p>Aha I see, I have to be inside the hole and then invoke <code>lean-hole</code>.</p>

#### [ Reid Barton (Sep 28 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840568):
<p>I misunderstood the docstring "Ask Lean for a list of holes, then ask the user which to use."</p>

#### [ Johan Commelin (Sep 28 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840701):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Agreed. Still it could be nice for the future. Because then one can use it during the golfing phase of a proof that one just finished.</p>

#### [ Johan Commelin (Sep 28 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840725):
<p>For squeezing entire files you might not even want to focus on editor integration.</p>

#### [ Simon Hudon (Sep 28 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134840941):
<p>I agree with your first point Johan. For the second point, the reason I'm thinking about editor integration is out of laziness. The slow files are really big and applications of <code>simp</code> vary a lot so search and replace alone doesn't cut it</p>

#### [ Johan Commelin (Sep 28 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134841018):
<p>Ok, fair enough</p>

#### [ Simon Hudon (Sep 28 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134841064):
<p>What I want to do is search and replace <code>simp</code> (not preceded by a square bracket) with <code>squeeze_simp</code> which will output all the required substitutions with line numbers and then emacs can do a very targeted replacement of all the <code>squeeze_simp</code></p>

#### [ Simon Hudon (Sep 28 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpectedly%20long/near/134841212):
<p>But now that I know about <code>hole_command</code> attributes, I think I might start with that to test out my idea</p>


{% endraw %}
