---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58237haveinmathlib.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [have in mathlib](https://leanprover-community.github.io/archive/113488general/58237haveinmathlib.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastien Gouezel (Jan 05 2019 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154469705):
<p>I am definitely very grateful to Mario for everything he does, but there is one question I want to raise on mathlib style. In general programming practice, comments are considered good, and even necessary. In lean, you can have lean-checked comments, in the form of <code>have</code>or <code>show</code>statements which, while unncessary to the compiler, increase a lot maintainability, readability, reusability (I mean, if you want to adapt a proof to suit your needs and you see what the proof is doing, then this is much easier), and make the learning curve less steep (by browsing through understandable code, one understands better what is going on). But this is at the price of compactness, or golfedness, which is very much valued in mathlib. </p>
<p>Let me take a simple example, for the sake of the discussion. Suppose one wants to prove a statement by applying lemma <code>foo</code>, which gives rise to two subgoals <code>subgoal 1</code> and <code>subgoal 2</code>, whose proofs are both nontrivial. The mathlib canonical version (M) would be:</p>
<div class="codehilite"><pre><span></span>  <span class="n">refine</span> <span class="n">foo</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rather</span> <span class="n">lengthy</span>
    <span class="k">proof</span> <span class="n">of</span> <span class="n">subgoal</span> <span class="mi">1</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">rather</span> <span class="n">lengthy</span> <span class="k">proof</span>
    <span class="n">of</span> <span class="n">subgoal</span> <span class="mi">2</span> <span class="o">}</span>
</pre></div>


<p>(or if you could even put some part of the proof in the first line, maybe go for it, for instance if the proof of <code>subgoal 1</code> starts with the introduction of variables <code>x</code> and <code>y</code> maybe write <code>refine foo (λ x y, _) _</code> in the first line)</p>
<p>But you could imagine more verbose versions such as (V1):</p>
<div class="codehilite"><pre><span></span>  <span class="n">refine</span> <span class="n">foo</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="k">show</span> <span class="n">subgoal</span> <span class="mi">1</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rather</span> <span class="n">lengthy</span>
    <span class="k">proof</span> <span class="n">of</span> <span class="n">subgoal</span> <span class="mi">1</span> <span class="o">},</span>
  <span class="k">show</span> <span class="n">subgoal</span> <span class="mi">2</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rather</span> <span class="n">lengthy</span> <span class="k">proof</span>
    <span class="n">of</span> <span class="n">subgoal</span> <span class="mi">2</span> <span class="o">}</span>
</pre></div>


<p>where the <code>show</code>lines are meant as completely unncessary comments. Or even (V2):</p>
<div class="codehilite"><pre><span></span>  <span class="k">have</span> <span class="n">A</span> <span class="o">:</span> <span class="n">subgoal</span> <span class="mi">1</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rather</span> <span class="n">lengthy</span>
    <span class="k">proof</span> <span class="n">of</span> <span class="n">subgoal</span> <span class="mi">1</span> <span class="o">},</span>
  <span class="k">have</span> <span class="n">B</span> <span class="o">:</span> <span class="n">subgoal</span> <span class="mi">2</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rather</span> <span class="n">lengthy</span> <span class="k">proof</span>
    <span class="n">of</span> <span class="n">subgoal</span> <span class="mi">2</span> <span class="o">},</span>
  <span class="n">exact</span> <span class="n">foo</span> <span class="n">A</span> <span class="n">B</span>
</pre></div>


<p>(M) is definitely more compact, but in my opinion (V1) or (V2) are preferable. And using (V1) or (V2) can depend on the intent: if the punchline is that one should use the lemma <code>foo</code>, I would put it at the beginning of the argument as in (V1), but if it is obvious that one should use <code>foo</code> and the hard part is checking the subgoals then I would rather go for (V2). Pros: more readable, maintainable, reusable. Cons: more verbose, slightly slower compilation time (?)</p>
<p>Anyway, I understand that the mathlib-ready version for now is (M), but I would really much like this to change. I am just starting the discussion, let me know what you think of it.</p>
<p>TLDR; I like code with a lot of <code>have</code> and <code>show</code> (at least one every sixth or seventh line?), and I would like to see more of them in mathlib. What do you think?</p>

#### [ Mario Carneiro (Jan 05 2019 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470063):
<p>My impression of these <code>show</code> lines is that they are mostly superfluous (there are ways to make a <code>show</code> do some work but I think we can agree that the question here is about the ones that are unnecessary for lean). Lean proofs (or at least mathlib proofs) aren't really intended to be read without the aid of lean in the background to give you side information. If we wanted to change that, a <code>show</code> line here and there wouldn't be nearly enough anyway. But assuming that the user has access to a lean server, comments about the current goal and the types of variables is quite redundant. It reminds me of the classic "bad C comment":</p>
<div class="codehilite"><pre><span></span>int i = 1; // set i to 1
</pre></div>


<p>There are much better uses for comments, like explaining <em>why</em> you are proving what you are. The Arzela-Ascoli theorem has several comments along these lines, and I think they are useful. But saying information that is already present seems like a waste of space.</p>

#### [ Patrick Massot (Jan 05 2019 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470079):
<p>I like Sébastien's <code>show</code></p>

#### [ Mario Carneiro (Jan 05 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470250):
<p>For very large proofs, it is helpful to mark the major landmarks with a <code>show</code>. But for sufficiently large proofs it is still better to just call these out as their own lemmas. Very long proofs don't work so great in lean; I would try to keep it to a page or less and break out lemmas if it gets longer than that (especially if the theorem takes a long time to compile).</p>

#### [ Sebastien Gouezel (Jan 05 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470420):
<blockquote>
<p>Lean proofs (or at least mathlib proofs) aren't really intended to be read without the aid of lean in the background to give you side information.</p>
</blockquote>
<p>Being able to read nontrivial proofs without starting a lean server looks important to me (I do it often in Isabelle). Maybe not all the tiny details of the proof, but the global structure, and what one is doing currently.</p>

#### [ Mario Carneiro (Jan 05 2019 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470540):
<p>also I much prefer (V1) style to (V2). When a proof breaks into a small piece and a large piece, the small piece should come first</p>

#### [ Mario Carneiro (Jan 05 2019 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470589):
<p>this produces a more even distribution of complexity and minimizes nesting</p>

#### [ Kevin Buzzard (Jan 05 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154470960):
<p>The question is whether one should be reading them at all. At the minute if you want to understand a lemma in mathlib you can usually just read a proof in an undergraduate textbook if it's "high level" and if it's a foundational lemma about multisets then who cares about the proof anyway, right? ;-)</p>

#### [ Kevin Buzzard (Jan 05 2019 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154471059):
<p>My personal opinion is that mathlib is extremely hard to read for beginners and hence extremely intimidating. However the decisions about what it should like are entirely up to the maintainers who I'm sure have their reasons. I personally think that any reason of the form "makes compile time shorter" is spurious because we should be compiling every commit and dumping the olean files online so users don't have to compile ever and we should concentrate on solving this really</p>

#### [ Patrick Massot (Jan 05 2019 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154471356):
<p>I think the compilation time thing is currently crucial, and shouldn't be. Today I'm trying to bring Sébastien's metric namespace PR up to date with mathlib. I merged master, fix conflicts and pushed without building because it takes forever. And of course it failed to build. So I've tried to fix it, and now it takes forever to try to build. And this is not even touching basic files imported everywhere. But I needed to switch branch and everything is rebuilding. I think this is a major pain for maintainers, except if you can maintain without ever editing code...</p>

#### [ Sebastien Gouezel (Jan 05 2019 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/have%20in%20mathlib/near/154471838):
<p>I have a separate copy of mathlib for each branch I am working on. So, I don't ever switch branches, as it is too painful otherwise. Clearly suboptimal, but efficient enough.</p>


{% endraw %}
