---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08179LeanassignmentfromKenny.html
---

## Stream: [general](index.html)
### Topic: [Lean assignment from Kenny](08179LeanassignmentfromKenny.html)

---


{% raw %}
#### [ Kenny Lau (Jul 30 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130567187):
<p>(optional) assignment for the people here who are too bored:<br>
Consider this inductive type:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">nested</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">nest</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nested</span> <span class="bp">→</span> <span class="n">nested</span>
</pre></div>


<p>Level 1: Write a definition <code>nested.cases_on'</code> and prove its equational lemmas.<br>
Level 2: Prove that this type has decidable equality (no, <code>@[derive decidable_eq]</code> won't work).<br>
Level 3: Write a definition <code>mem</code> such that <code>mem x (nest L)</code> iff <code>list.mem x L</code> and prove that <code>mem</code> is well-founded.<br>
Level 4: Prove that this type is <code>denumerable</code> (i.e. constructively countable).</p>

#### [ Kenny Lau (Jul 30 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130567191):
<p>(I've done levels 1-3 and will upload the code later)</p>

#### [ Kevin Buzzard (Jul 30 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130567208):
<p>Should this be a structure?</p>

#### [ Kenny Lau (Jul 30 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130567259):
<p>can you make it a structure?</p>

#### [ Kevin Buzzard (Jul 30 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130567272):
<p>I don't know. I only mention it because I am dimly aware that if you make something a structure then it does some of the work for you. And it only has one constructor...</p>

#### [ Kenny Lau (Jul 30 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130567285):
<p>I'm not sure whether <code>inductive</code> or <code>structure</code> comes with more tools, but I don't think you can make this a structure</p>

#### [ Kevin Buzzard (Jul 30 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130567296):
<p>I remember the days when I was bored. I have far too much to do nowadays to even contemplate being bored!</p>

#### [ Kenny Lau (Jul 30 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130569524):
<p>Answers: <a href="https://github.com/kckennylau/Lean/blob/master/nested.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/nested.lean">https://github.com/kckennylau/Lean/blob/master/nested.lean</a></p>

#### [ Kenny Lau (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130586341):
<p>here's a choice function:</p>

#### [ Kenny Lau (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130586343):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">choice</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">x</span> <span class="o">:</span> <span class="n">nested</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">nest</span> <span class="o">[]</span> <span class="bp">→</span> <span class="o">{</span> <span class="n">z</span> <span class="bp">//</span> <span class="n">z</span> <span class="err">∈</span> <span class="n">x</span> <span class="o">}</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nest</span> <span class="o">[])</span>       <span class="n">H</span> <span class="o">:=</span> <span class="n">absurd</span> <span class="n">rfl</span> <span class="n">H</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nest</span> <span class="o">(</span><span class="n">hd</span><span class="bp">::</span><span class="n">tl</span><span class="o">))</span> <span class="n">H</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">hd</span><span class="o">,</span> <span class="o">(</span><span class="n">mem_def</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Jul 31 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130626524):
<p>Somebody should collect up these puzzles which appear here occasionally and make a little challenge page somewhere.</p>

#### [ Kenny Lau (Jul 31 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130626588):
<p>such as in your blog?</p>

#### [ Kenny Lau (Jul 31 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627160):
<p>someone pointed out to me that my type is the type of all finite trees</p>

#### [ Kevin Buzzard (Jul 31 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627630):
<p>Do you want to write a guest post about this problem? I look at it and I think "I'd like to work on that, but I am too busy trying to deal with the questions my UROP students are asking me".</p>

#### [ Kenny Lau (Jul 31 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627637):
<p>I'm busy reading ANT and AM and all that :-)</p>

#### [ Kevin Buzzard (Jul 31 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627647):
<p>I saw Mario explicitly pointing out in a conference talk that there was not enough number theory in mathlib. I say that we begin to concentrate on fixing this.</p>

#### [ Kenny Lau (Jul 31 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627696):
<p>I'd say that among all things, the theory of fin.dim. vector spaces is a prerequisite</p>

#### [ Kevin Buzzard (Jul 31 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627699):
<p>What exactly do you need? I have several people working on this.</p>

#### [ Kenny Lau (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627702):
<p>determinant and trace, right</p>

#### [ Kevin Buzzard (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627709):
<p>I have several people working on det too</p>

#### [ Kenny Lau (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627712):
<p>Cayley-Hamilton would be great</p>

#### [ Kenny Lau (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627713):
<p>I mean, you know much more ANT than me</p>

#### [ Kevin Buzzard (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627715):
<p>right, indeed, that's precisely what I'm a world expert in :-)</p>

#### [ Kenny Lau (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627719):
<p>then why are you asking me lol</p>

#### [ Kevin Buzzard (Jul 31 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assignment%20from%20Kenny/near/130627720):
<p>I'm asking you to implement it ;-)</p>


{% endraw %}
