---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31387M1FP65syntacticentailmentexercise.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [(M1F/P65) syntactic entailment exercise](https://leanprover-community.github.io/archive/113488general/31387M1FP65syntacticentailmentexercise.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Oct 22 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136257251):
<p>At Imperial in the 3rd year logic course M3P65 they're doing first order propositional logic, soundness and completeness etc. In a guest M1F lecture (my course) John Britnell went through some of this stuff with the first years, and the last question on his problem sheet was a real stinker. <span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> <a href="https://math.stackexchange.com/questions/2962525/derive-simple-logical-laws-in-a-structure-with-not-and-implies" target="_blank" title="https://math.stackexchange.com/questions/2962525/derive-simple-logical-laws-in-a-structure-with-not-and-implies">asked about it on math SE</a> and got what looks like a couple of nice answers. I'd like the stufents to check those answers in Lean but I'd like to make it as easy as possible for them, by setting up the underlying infrastructure, so they have easy access to the axioms, and only the axioms. </p>
<p>I can think of several ways that one could try to do this (make a new inductive type for propositions-in-the-sense-of-this-question and then input the axioms as axioms, or make a structure somehow with the axioms inbuilt as part of the structure). It would be nice to get some views on the best way to set up this sort of puzzle. The idea would be for the students to formalise the answers posted on MO within the framework (a skeleton lean file or an import) which I provide them, with them not having to worry about setting up notation or whatever (I am assuming that we can't using inbuilt not and arrow for our two inbuilt constructors).</p>

#### [ Kevin Buzzard (Oct 22 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136257538):
<p>And here's a question which exposes my own ignorance on the subject: if we can check that <code>P → (¬ (¬ P))</code> using the "it's true if P is true and true if P is false so it's true" method (semantic entailment?) then does the completeness theorem actually construct a proof of this proposition from the three axioms in the question, or does the compactness argument render the entire thing necessarily nonconstructive (i.e. it only shows "there exists a term of this type" rather than "here is a term of this type")?</p>

#### [ Gabriel Ebner (Oct 22 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258425):
<p>The typical completeness proof is a proof by contradiction.  You can complete any set of (syntactically) consistent formulas into a maximally consistent set (for every formula <code>φ</code>, you iteratively add either <code>φ</code> or <code>¬ φ</code> so that the set stays consistent), which then gives you a model.  Your statement is then the contrapositive: there are no counterexamples, so the (singleton) set <code>{¬ (p → ¬ ¬ p)}</code> must be inconsistent.  I don't think that <em>this</em> proof gives you a proof.</p>

#### [ Gabriel Ebner (Oct 22 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258577):
<p>However it's not "necessarily" nonconstructive for a single propositional formula.  You can of course just produce a proof by case analysis (just do the "if p is true, then ..., if p is false, ...." in the proof).</p>

#### [ Kevin Buzzard (Oct 22 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258683):
<p>Thanks Gabriel! Now I realise that one can make it constructive by proving the proof exists and then just searching through all proofs to find it, knowing your search will terminate.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258693):
<p>So perhaps the interesting question is the best running time one can hope for, if I've understood all this correctly.</p>

#### [ Gabriel Ebner (Oct 22 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136258696):
<p>Propositional validity is coNP-complete.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259027):
<p>Math is hard</p>

#### [ Gabriel Ebner (Oct 22 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259350):
<p>Regarding the original question, I think inductive type for formulas and proofs is the way to go.  For inspiration, there are at least 2 logical formalizations in lean that I know of: <a href="https://github.com/skbaek/fol/blob/master/frm.lean" target="_blank" title="https://github.com/skbaek/fol/blob/master/frm.lean">https://github.com/skbaek/fol/blob/master/frm.lean</a> and <a href="https://github.com/avigad/formal_logic" target="_blank" title="https://github.com/avigad/formal_logic">https://github.com/avigad/formal_logic</a><br>
Personally I'm not a big fan of writing concrete Hilbert-style proofs as exercises.  I've found it to be much more instructive to show how to derive rules that allow you to simulate saner proof systems; e.g. the deduction theorem or even simple rules such as <code>p → q → r ⇒ q → p → r</code>.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259545):
<p>Gabriel I am a complete novice coming to this stuff. I guess I have no idea what is instructive -- because these questions are in the air in the maths department at Imperial I just decided it was time to get to the bottom of how it all worked.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259551):
<p>Here's an approach based on axioms, which I thought might be promising but got scary at the end:</p>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">prop</span> <span class="o">:</span> <span class="kt">Type</span>

<span class="kn">constant</span> <span class="n">impl</span> <span class="o">:</span> <span class="n">prop</span> <span class="bp">→</span> <span class="n">prop</span> <span class="bp">→</span> <span class="n">prop</span>

<span class="c1">-- I am assuming overwriting → is not recommended</span>
<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`~&gt;`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">impl</span>

<span class="kn">constant</span> <span class="n">pnot</span> <span class="o">:</span> <span class="n">prop</span> <span class="bp">→</span> <span class="n">prop</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">¬</span> <span class="o">:=</span> <span class="n">pnot</span>

<span class="kn">constant</span> <span class="n">entails</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">prop</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prop</span> <span class="bp">→</span> <span class="kt">Prop</span>

<span class="n">local</span> <span class="kn">infix</span> <span class="err">⊢</span> <span class="o">:=</span> <span class="n">entails</span>

<span class="kn">axiom</span> <span class="n">A1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="n">prop</span><span class="o">,</span> <span class="n">entails</span> <span class="o">{</span><span class="n">P</span><span class="o">,</span><span class="n">Q</span><span class="o">}</span> <span class="o">(</span><span class="n">P</span> <span class="bp">~&gt;</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">~&gt;</span> <span class="n">P</span><span class="o">))</span>

<span class="c1">-- plus two other axioms</span>

<span class="c1">-- and now I need modus ponens or something?</span>

<span class="c1">-- am I missing a trick?</span>
</pre></div>

#### [ Gabriel Ebner (Oct 22 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259786):
<p>You probably want <code>∅ ⊢ (P ~&gt; (Q ~&gt; P))</code>.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259808):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <span class="user-mention" data-user-id="110044">@Chris Hughes</span>  is it possible to make a simple framework in Lean where first years could work on <a href="https://math.stackexchange.com/questions/2962525/derive-simple-logical-laws-in-a-structure-with-not-and-implies" target="_blank" title="https://math.stackexchange.com/questions/2962525/derive-simple-logical-laws-in-a-structure-with-not-and-implies">the M1F question in the MSE post</a>? I find the files in Gabriel's links a bit daunting.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136259887):
<p>Or could I use those files without understanding them somehow?</p>

#### [ Gabriel Ebner (Oct 22 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136260159):
<p>If you just want a Hilbert calculus for propositional logic, then it's only two inductive types:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">fml</span>
<span class="bp">|</span> <span class="n">atom</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">imp</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span>
<span class="kn">open</span> <span class="n">fml</span>

<span class="kn">infixr</span> <span class="bp">`</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">imp</span>

<span class="kn">inductive</span> <span class="n">prf</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">axk</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axs</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">mp</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>
</pre></div>


<p>You can add negation if you want, but there should be enough examples in the implication-only fragment.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261299):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span>  I've got it up and running.</p>
<p><a href="https://gist.github.com/kbuzzard/15a40e59ce815b69a0dcc983935abc83" target="_blank" title="https://gist.github.com/kbuzzard/15a40e59ce815b69a0dcc983935abc83">https://gist.github.com/kbuzzard/15a40e59ce815b69a0dcc983935abc83</a></p>
<p>I've proved P implies P :-)</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261336):
<p>Thanks so much <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> , I think I can take it from here.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 22 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261394):
<blockquote>
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span>  I've got it up and running.</p>
<p><a href="https://gist.github.com/kbuzzard/15a40e59ce815b69a0dcc983935abc83" target="_blank" title="https://gist.github.com/kbuzzard/15a40e59ce815b69a0dcc983935abc83">https://gist.github.com/kbuzzard/15a40e59ce815b69a0dcc983935abc83</a></p>
<p>I've proved P implies P :-)</p>
</blockquote>
<p>Darn, I was trying to beat you to it.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 22 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261397):
<p>I'm almost done myself.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261420):
<p>:-)</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261429):
<p>Well there's still a race on for P implies not not P :-)</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261510):
<p>github being a bit unreliable at the minute -- I think they had a bit of a minor disaster earlier today. Here's the proof.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">fml</span>
<span class="bp">|</span> <span class="n">atom</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">imp</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">not</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">fml</span>

<span class="kn">infixr</span> <span class="bp">`</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">imp</span> <span class="c1">-- right associative</span>
<span class="n">local</span> <span class="kn">notation</span> <span class="bp">¬</span> <span class="o">:=</span> <span class="n">fml</span><span class="bp">.</span><span class="n">not</span>

<span class="kn">inductive</span> <span class="n">prf</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">axk</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axs</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axX</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="bp">¬</span><span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span>
<span class="bp">|</span> <span class="n">mp</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>

<span class="kn">open</span> <span class="n">prf</span>

<span class="kn">lemma</span> <span class="n">pqpp</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">mp</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">((</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">axk</span> <span class="n">p</span> <span class="n">q</span><span class="o">),</span>
  <span class="n">exact</span> <span class="n">axs</span> <span class="n">p</span> <span class="n">q</span> <span class="n">p</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">p_implies_p</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">exact</span> <span class="n">mp</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">axk</span> <span class="n">p</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">pqpp</span> <span class="n">p</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)),</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Oct 22 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261545):
<p>Gabriel called the axioms <code>axk</code> and <code>axs</code> but he left the negation one out (and indeed I never used it). I called it <code>axX</code> but I'm wondering where there is standard CS code for these axioms. <code>mp</code> I know is modus ponens.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 22 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136261975):
<p>Mine is essentially the same too but with <code>have</code>s instead of lemmas.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">reflex</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">P</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">begin</span>
        <span class="k">have</span> <span class="n">R</span> <span class="o">:</span> <span class="n">fml</span><span class="o">,</span> <span class="n">exact</span> <span class="n">P</span><span class="o">,</span>
        <span class="k">let</span> <span class="n">Q</span> <span class="o">:</span> <span class="n">fml</span> <span class="o">:=</span> <span class="n">R</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">P</span><span class="o">,</span>
        <span class="k">have</span> <span class="n">HPQ</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">Q</span><span class="o">),</span>
            <span class="n">change</span> <span class="n">prf</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">R</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">P</span><span class="o">)),</span>
            <span class="n">apply</span> <span class="n">prf</span><span class="bp">.</span><span class="n">axk</span><span class="o">,</span>
        <span class="k">have</span> <span class="n">HPQP</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">P</span><span class="o">)),</span>
            <span class="n">apply</span> <span class="n">prf</span><span class="bp">.</span><span class="n">axk</span><span class="o">,</span>
        <span class="k">have</span> <span class="n">HPQPP</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">((</span><span class="n">P</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">P</span><span class="o">)),</span>
            <span class="n">apply</span> <span class="n">prf</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">Q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">P</span><span class="o">),</span>
            <span class="n">exact</span> <span class="n">HPQP</span><span class="o">,</span>
            <span class="n">apply</span> <span class="n">prf</span><span class="bp">.</span><span class="n">axs</span><span class="o">,</span>
        <span class="n">apply</span> <span class="n">prf</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">Q</span><span class="o">),</span>
        <span class="n">exact</span> <span class="n">HPQ</span><span class="o">,</span>
        <span class="n">exact</span> <span class="n">HPQPP</span><span class="o">,</span>
    <span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 22 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262078):
<p>Btw is it a good idea to reuse <code>¬</code>? Shouldn't we use a variant like <code>¬'</code> as Gabriel Ebner did?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262110):
<p>So this is a weird thing about computer scientists -- they like to do proofs backwards. Almost all tactics operate on the goal. If you have proofs of <code>A</code>, <code>A -&gt; B</code>, <code>B -&gt; C</code> and <code>C -&gt; D</code> and your goal is <code>D</code>, a mathematician in a lecture might say "well first we can prove B, then we can deduce C, and then finally we can deduce D so done". If you write all of this in one theorem in Lean, in that order, you end up with a bunch of intermediate extra terms in your context which you only ever use once and then would really rather throw away because for big proofs all these extra junk terms just start getting in the way and making your goal scroll off the bottom of the screen.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262160):
<p>So there are two other ways of doing things. Either prove B and C as lemmas before you embark on a proof of D, or just write the entire proof backwards and change the goal from D to C to B to A with <code>apply</code> and then use <code>assumption</code> at the end.</p>

#### [ Johan Commelin (Oct 22 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262192):
<p>Well, there is <code>suffices</code>.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262196):
<p>Because going backwards is not always intuitive, the "lots of lemmas" approach becomes more appealing. And for other reasons too it's preferable to break your proofs up into as small chunks as you can.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262250):
<p><code>suffices</code> is still going backwards, right?</p>

#### [ Johan Commelin (Oct 22 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262258):
<p>Hmmm, yes, I guess it is.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262335):
<blockquote>
<p>Btw is it a good idea to reuse <code>¬</code>? Shouldn't we use a variant like <code>¬'</code> as Gabriel Ebner did?</p>
</blockquote>
<p>I have no idea if it's a good idea to reuse <code>¬</code>. I was 100% convinced that it was a bad idea to reuse <code>→</code> and I like Gabriel's idea of the apostrophe -- I think this is a CS meme or something.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262435):
<p>grr I wish github was working, I have everything locally in a git repo and am having trouble pushing.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262677):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> <a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/tree/master/src" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/tree/master/src">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/tree/master/src</a> you could just edit that file (as could anyone else who wants to work on this)</p>

#### [ Kevin Buzzard (Oct 22 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262684):
<p><span class="user-mention" data-user-id="131875">@Alexandru-Andrei Bosinta</span> There's my proof that P implies P</p>

#### [ Kevin Buzzard (Oct 22 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262985):
<p>Meh still GH problems (also having trouble with gists). Current version of framework, with example proof, is here (I took Abhi's advice and changed not to not'):</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">fml</span>
<span class="bp">|</span> <span class="n">atom</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">imp</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">not</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">fml</span>

<span class="kn">infixr</span> <span class="bp">`</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">imp</span> <span class="c1">-- right associative</span>

<span class="kn">notation</span> <span class="bp">`¬</span><span class="err">&#39;</span> <span class="bp">`</span> <span class="o">:=</span> <span class="n">fml</span><span class="bp">.</span><span class="n">not</span>


<span class="kn">inductive</span> <span class="n">prf</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">axk</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axs</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axX</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">((</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span>
<span class="bp">|</span> <span class="n">mp</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>

<span class="kn">open</span> <span class="n">prf</span>

<span class="kn">lemma</span> <span class="n">p_of_p_of_p_of_q</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">mp</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">((</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">axk</span> <span class="n">p</span> <span class="n">q</span><span class="o">),</span>
  <span class="n">exact</span> <span class="n">axs</span> <span class="n">p</span> <span class="n">q</span> <span class="n">p</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">p_of_p_of_p_of_q&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">mp</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">((</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">axk</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">(</span><span class="n">axs</span> <span class="n">p</span> <span class="n">q</span> <span class="n">p</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">p_of_p</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">exact</span> <span class="n">mp</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">axk</span> <span class="n">p</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">p_of_p_of_p_of_q</span> <span class="n">p</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)),</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Oct 22 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136262996):
<p>I also added a term proof for the first lemma</p>

#### [ Kevin Buzzard (Oct 22 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136263023):
<p>Note : <code>$</code> is a clever CS trick which can be used in place of brackets sometimes (it's a clever trick to do with BIDMAS / operator precedence)</p>

#### [ Gabriel Ebner (Oct 22 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136264746):
<p>I copied the apostrophe directly from Seul's formalization, but yeah indeed, apostrophe, tilde, hat, etc. are all common modifiers.</p>

#### [ Andrew Ashworth (Oct 22 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136265032):
<blockquote>
<p>So this is a weird thing about computer scientists -- they like to do proofs backwards. Almost all tactics operate on the goal. If you have proofs of <code>A</code>, <code>A -&gt; B</code>, <code>B -&gt; C</code> and <code>C -&gt; D</code> and your goal is <code>D</code>, a mathematician in a lecture might say "well first we can prove B, then we can deduce C, and then finally we can deduce D so done". If you write all of this in one theorem in Lean, in that order, you end up with a bunch of intermediate extra terms in your context which you only ever use once and then would really rather throw away because for big proofs all these extra junk terms just start getting in the way and making your goal scroll off the bottom of the screen.</p>
</blockquote>
<p>I know this isn't a good workaround, but you might try anonymous <code>have</code> statements.</p>

#### [ Gabriel Ebner (Oct 22 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136265228):
<blockquote>
<p>Gabriel called the axioms axk and axs but he left the negation one out (and indeed I never used it). I called it  axX but I'm wondering where there is standard CS code for these axioms. mp I know is modus ponens.</p>
</blockquote>
<p>This naming scheme is indeed rooted in a very fundamental observation in computer science, namely the Curry-Howard isomorphism.  This isomorphism maps formulas to types, and proofs to programs.  The Hilbert calculus for propositional logic that we consider here is mapped to the simply-typed <a href="https://en.wikipedia.org/wiki/SKI_combinator_calculus" target="_blank" title="https://en.wikipedia.org/wiki/SKI_combinator_calculus">combinator calculus</a>; and just as I hope that nobody is writing programs in combinator calculus, hopefully only hardcore freaks are writing proofs in Hilbert calculus.  To come back to the naming: as you might have noticed the propositions derived by these two axioms are exactly the types of the K and S combinators:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="n">combinator</span><span class="bp">.</span><span class="n">K</span>
<span class="c1">-- combinator.K : ?M_1 → ?M_2 → ?M_1</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">combinator</span><span class="bp">.</span><span class="n">S</span>
<span class="c1">-- combinator.S : (?M_1 → ?M_2 → ?M_3) → (?M_1 → ?M_2) → ?M_1 → ?M_3</span>
</pre></div>

#### [ Kevin Buzzard (Oct 22 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136265229):
<p>They still pile up. I guess what a mathematician would like is a tactic which actually deletes hypotheses <code>HA : A</code> and <code>HAB : A -&gt; B</code> from the context and adds a new hypothesis <code>HB : B</code>. That's very much how I'm thinking about these things. Of course there's the risk you'll need the hypotheses later but in my experience there are times you know for sure you won't.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136265369):
<p>This combinator business is so cool. Thanks Gabriel. They don't teach any of this stuff in maths departments usually -- just a couple of lectures on the completeness theorem and then let's get on to proper stuff like ZFC.</p>

#### [ Rob Lewis (Oct 22 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136268664):
<p>Kevin, are you aware of the <code>replace</code> tactic? It has some of the behavior you want.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">replace</span> <span class="n">ha</span> <span class="o">:=</span> <span class="n">hab</span> <span class="n">ha</span><span class="o">,</span> <span class="c1">-- now we have hab : B</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">hbc</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="n">C</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">A</span><span class="o">,</span> <span class="k">from</span> <span class="n">ha</span><span class="o">,</span> <span class="c1">-- this : A</span>
  <span class="n">replace</span> <span class="o">:=</span> <span class="n">hab</span> <span class="n">this</span><span class="o">,</span> <span class="c1">-- this : B</span>
  <span class="n">replace</span> <span class="o">:=</span> <span class="n">hbc</span> <span class="n">this</span><span class="o">,</span> <span class="c1">-- this : C</span>
  <span class="n">exact</span> <span class="n">this</span>
<span class="kn">end</span>
</pre></div>


<p>But in general, I think of forward reasoning as a term mode thing. Unless you're using tactics that search for things in the local context, there's nothing wrong with having lots of hypotheses around, other than that they clutter the goal view. If you're working in term mode, you don't need the goal view, and your hypotheses are all visible all the time because they're part of your proof script.</p>

#### [ Rob Lewis (Oct 22 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136268701):
<p>e.g. the proof that <span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> posted above is really a term mode proof until the very end.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136269931):
<p>That's an interesting point. I teach mathematicians tactic mode from the very start because I think it's much easier for them to grasp than term mode. I always forget about the <code>replace</code> tactic -- I always remember it starts <code>re</code>something and then it always autocompletes in my brain to <code>rewrite</code>.</p>

#### [ Johan Commelin (Oct 22 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136270252):
<p>Otoh in our minds we definitely don't think of it as <code>replace</code>ing an assumption.</p>

#### [ Johan Commelin (Oct 22 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136270296):
<p>In our minds what is really going on is <code>have b : B := hab a, clear a hab,</code></p>

#### [ Chris Hughes (Oct 22 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136271125):
<p>Is this a proof?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">imp</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">bool</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="n">bool</span><span class="o">)</span>
  <span class="o">(</span><span class="n">a1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p</span> <span class="n">q</span><span class="o">,</span> <span class="n">imp</span> <span class="n">p</span> <span class="o">(</span><span class="n">imp</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">)</span>
  <span class="o">(</span><span class="n">a2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p</span> <span class="n">q</span><span class="o">,</span> <span class="n">imp</span> <span class="o">(</span><span class="n">imp</span> <span class="o">(</span><span class="n">n</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="n">q</span><span class="o">))</span> <span class="o">(</span><span class="n">imp</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">)</span>
  <span class="o">(</span><span class="n">a3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span> <span class="n">imp</span> <span class="o">(</span><span class="n">imp</span> <span class="n">p</span> <span class="o">(</span><span class="n">imp</span> <span class="n">q</span> <span class="n">r</span><span class="o">))</span> <span class="o">(</span><span class="n">imp</span> <span class="o">(</span><span class="n">imp</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">(</span><span class="n">imp</span> <span class="n">q</span> <span class="n">r</span><span class="o">))</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">)</span>
<span class="n">include</span> <span class="n">a1</span> <span class="n">a2</span> <span class="n">a3</span>

<span class="kn">set_option</span> <span class="n">class</span><span class="bp">.</span><span class="n">instance_max_depth</span> <span class="mi">50</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p</span><span class="o">,</span> <span class="n">imp</span> <span class="n">p</span> <span class="o">(</span><span class="n">n</span> <span class="o">(</span><span class="n">n</span> <span class="n">p</span><span class="o">))</span> <span class="bp">=</span> <span class="n">tt</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">revert</span> <span class="n">imp</span> <span class="n">n</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Kevin Buzzard (Oct 22 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136271635):
<p>No, that doesn't count.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136272090):
<p><a href="/user_uploads/3121/RzZ8ETr6cUDU63MzUV9zWyXp/IMG_20181019_134013644.jpg" target="_blank" title="IMG_20181019_134013644.jpg">IMG_20181019_134013644.jpg</a> <a href="/user_uploads/3121/j9yYOt0hVLqosT3niylQup03/IMG_20181019_134020093.jpg" target="_blank" title="IMG_20181019_134020093.jpg">IMG_20181019_134020093.jpg</a> Chris -- you are assuming the completeness theorem, namely that the stuff which the axioms prove is exactly the stuff which is true. In 3rd year logic they're proving this sort of thing right now.</p>
<div class="message_inline_image"><a href="/user_uploads/3121/RzZ8ETr6cUDU63MzUV9zWyXp/IMG_20181019_134013644.jpg" target="_blank" title="IMG_20181019_134013644.jpg"><img src="/user_uploads/3121/RzZ8ETr6cUDU63MzUV9zWyXp/IMG_20181019_134013644.jpg"></a></div><div class="message_inline_image"><a href="/user_uploads/3121/j9yYOt0hVLqosT3niylQup03/IMG_20181019_134020093.jpg" target="_blank" title="IMG_20181019_134020093.jpg"><img src="/user_uploads/3121/j9yYOt0hVLqosT3niylQup03/IMG_20181019_134020093.jpg"></a></div>

#### [ Chris Hughes (Oct 22 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136272377):
<p>What's the definition of true?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136272981):
<p>Whilst there are many here who can explain all of this better than me, my memory of what I was taught in undergraduate logic was this. You can _prove_ statements by deducing them from the axioms using modus ponens. Note that the axioms aren't constructive logic because we have that extra one about not Q implies not P which is I believe is equivalent to LEM in the presence of the other two axioms. A statement is _true_ if whenever you evaluate all your variables as booleans and interpret -&gt; and not as following the truth tables, it evaluates to true. You have seen enough constructive mathematics to know that "always evaluates to true" a.k.a. "true in every model" is not the same as "being provable from a random set of axioms", especially if the axioms are those of constructive logic. The key thing here is that if we add that third axiom, then the true things and the provable things coincide. This is the completeness theorem.</p>

#### [ Chris Hughes (Oct 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136272996):
<p>I know what provable means. What does true mean?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273011):
<p>it means "always evaluates to true whenever we map the propositions to bools"</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273085):
<p>A _model_ of a bunch of statements involving propositions p q r etc is just an assignment of a boolean value to each of the variables p q retc so that all the statements become true.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273227):
<p>A bunch of propositions involving a set of variables _semantically entails_ another proposition X if, for every model where the bunch of propositions all evaluate to true, the proposition X also evaluates to true.</p>
<p>A bunch of propositions _syntactially entails_ another proposition X if you can use the axioms and modus ponens to deduce X from the bunch of propositions. This depends on your axioms of course.</p>
<p>The theorem is that for the axioms on the poor photos I sent you, the two notions are the same. If I've remembered everything correctly...</p>

#### [ Chris Hughes (Oct 22 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273242):
<p>By this definition, true + em -&gt; provable, though right?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273257):
<p>When you say "provable" you have to say which axioms we're using</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273320):
<p>"true" is an absolute thing, stuff like p -&gt; p is true because T -&gt; T and F -&gt; F</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273341):
<p>This is the same as "provable using the axioms of classical logic" (the completeness theorem) but not the same as "provable using the axioms of constructive logic" (the law of the excluded middle being a counterexample)</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273430):
<p>I only have the most tenuous understanding of this stuff now, so please someone butt in if I'm talking nonsense.</p>

#### [ Rob Lewis (Oct 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273434):
<blockquote>
<p>"true" is an absolute thing, stuff like p -&gt; p is true because T -&gt; T and F -&gt; F</p>
</blockquote>
<p>To nitpick: to say "true" you have to say what semantics we're using. Excluded middle isn't true in Kripke semantics for propositional logic.</p>

#### [ Simon Cruanes (Oct 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273435):
<p>When you move to higher-order logic and interpret function types as function spaces, then provability is always weaker than semantic truth, sadly.</p>

#### [ Rob Lewis (Oct 22 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273456):
<p>But Chris, feel free to ignore me complicating the story for now. :)</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273479):
<blockquote>
<p>To nitpick: to say "true" you have to say what semantics we're using.</p>
</blockquote>
<p>What semantics am I using?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273546):
<p>Are my semantics something like "bool is the set of values, and here's the truth table for -&gt;, and here's the truth table for not"?</p>

#### [ Rob Lewis (Oct 22 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273554):
<p>Boolean semantics? Truth table semantics? I'm blanking on a standard name.</p>

#### [ Rob Lewis (Oct 22 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273559):
<p>Exactly.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273575):
<p>I would have understood the logic course <em>much</em> better when I was an UG if I could have done the course in Lean.</p>

#### [ Rob Lewis (Oct 22 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273646):
<p>Intuitionistic logic is sound but not complete for those semantics. So you end up with Kripke semantics, a different way of interpreting true/false under which the true formulas coincide with the intuitionistically provable ones.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273691):
<p>I see. So you're saying there is a completeness theorem for constructive logic.</p>

#### [ Rob Lewis (Oct 22 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273888):
<p>Yeah, but it's not as intuitive (ha ha) as for classical logic. <a href="https://plato.stanford.edu/entries/logic-intuitionistic/#BasSem" target="_blank" title="https://plato.stanford.edu/entries/logic-intuitionistic/#BasSem">https://plato.stanford.edu/entries/logic-intuitionistic/#BasSem</a></p>

#### [ Simon Cruanes (Oct 22 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136273961):
<p>I don't know much about constructive semantics, but there are things like "reducibility candidates" in this area I believe?<br>
edit: ah neat, if there's an entry in the encyclopedia already, nevermind…</p>

#### [ Gabriel Ebner (Oct 22 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136275199):
<blockquote>
<p>To nitpick: to say "true" you have to say what semantics we're using. Excluded middle isn't true in Kripke semantics for propositional logic.</p>
</blockquote>
<p>To nitpick even harder: usually truth refers to a single model, the concept we need here is validity---truth in all models.  For example <code>p ∨ ¬ p</code> is true in some Kripke models (e.g. any model with only one world); but is not <em>valid</em>, it is not true at all worlds in all Kripke models.</p>

#### [ Gabriel Ebner (Oct 22 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136275469):
<blockquote>
<p>"true" is an absolute thing, stuff like p -&gt; p is true because T -&gt; T and F -&gt; F</p>
</blockquote>
<p>This should be "valid".  <code>p → p</code> is <em>valid</em> because <code>p → p</code> is <em>true</em> (alt. satisfied) in all models.</p>

#### [ Gabriel Ebner (Oct 22 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136275669):
<blockquote>
<p>[...] then the true things and the provable things coincide. This is the completeness theorem.</p>
</blockquote>
<p>Since we're already nitpicking, the completeness theorem only states one inclusion: namely that <code>valid ⊆ provable</code>.  The other direction, <code>provable ⊆ valid</code> is typically called soundness.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136278211):
<p>Thanks a lot for fixing up my inaccuracies. Some kids here at Imperial are asking me about these things so I'm very pleased to be able to get it all straight for the first time in my life.</p>

#### [ Kenny Lau (Oct 22 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136284552):
<p>there are quite some (equivalent) semantics for constructive logic</p>

#### [ Kevin Buzzard (Oct 22 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287058):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  are you going to rise to my challenge?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287089):
<p>or rather, Dr Britnell's challenge. <a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/c55d507918a8de1ec4c81953fe4dfcd696c46e82/src/gabriel_framework.lean#L33" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/c55d507918a8de1ec4c81953fe4dfcd696c46e82/src/gabriel_framework.lean#L33">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/c55d507918a8de1ec4c81953fe4dfcd696c46e82/src/gabriel_framework.lean#L33</a></p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287285):
<p><span class="user-mention" data-user-id="120559">@Rohan Mitta</span>  asked me why <code>prf</code> was taking values in Type and not Prop. Is there a reason for this? It gave Rohan some trouble (he couldn't use <code>or.elim</code>), so he made a new <code>Prop</code>-valued type to get around it. Does this mean that <code>or.elim</code> somehow should not be used? What's happening here?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287518):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> is making progress: <a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/c55d507918a8de1ec4c81953fe4dfcd696c46e82/src/abhimanyu.lean#L39" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/c55d507918a8de1ec4c81953fe4dfcd696c46e82/src/abhimanyu.lean#L39">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/c55d507918a8de1ec4c81953fe4dfcd696c46e82/src/abhimanyu.lean#L39</a></p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136287752):
<p><a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/rohan_enrico_success.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/rohan_enrico_success.lean">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/rohan_enrico_success.lean</a> <span class="user-mention" data-user-id="120559">@Rohan Mitta</span> says he's done it! But he changed the question a bit...</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288400):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I tidied up the question. Here it is:</p>
<p><a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/gabriel_framework.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/gabriel_framework.lean">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/gabriel_framework.lean</a></p>
<p>The proofs are really nice to write in term mode</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288447):
<p>That's what Britnell asked the first years.</p>

#### [ Kenny Lau (Oct 22 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288455):
<p>I'm revising for my test tomorrow</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288465):
<p>Probably a better use of your time, if you have a test tomorrow.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136288909):
<p><a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/question6.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/question6.lean">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/question6.lean</a> There's the final version of the challenge. I tinkered with <code>mp</code> a bit. If anyone can suggest any other improvements I'd be all ears. Rohan, I stubbornly left it as <code>Type</code> but only because I don't understand if changing it to <code>Prop</code> is cheating or not.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136289685):
<p><span class="user-mention" data-user-id="120559">@Rohan Mitta</span> what do you think of my changes to <code>mp</code>?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136289732):
<p>I put p and q in <code>{}</code> and I changed the order of the next two inputs (first the function, then the input).</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136289781):
<p>Would that have made your code easier or harder to write?</p>

#### [ Rohan Mitta (Oct 22 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136289917):
<p>Yeah your changes are great! In all my proofs I let lean infer what p and q were, and also often accidentally wrote the next two inputs in the order that you changed it to.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136290105):
<p>Oh, here's something I just realised I didn't know: Modus Ponens says <code>prf (q →' r) → (prf q → prf r)</code> but is the converse true? Is there a map <code>(prf q → prf r) → prf (q →' r)</code> ?</p>

#### [ Kevin Buzzard (Oct 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136290243):
<p>Regarding order of inputs for modus ponens, check out the analogy here:</p>
<div class="codehilite"><pre><span></span><span class="n">axs</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="n">mp</span> <span class="o">{</span><span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">r</span>
</pre></div>

#### [ Kevin Buzzard (Oct 22 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136290622):
<blockquote>
<p>Oh, here's something I just realised I didn't know: Modus Ponens says <code>prf (q →' r) → (prf q → prf r)</code> but is the converse true? Is there a map <code>(prf q → prf r) → prf (q →' r)</code> ?</p>
</blockquote>
<p>I see -- this is the deduction theorem.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 22 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292121):
<blockquote>
<p>Oh, here's something I just realised I didn't know: Modus Ponens says <code>prf (q →' r) → (prf q → prf r)</code> but is the converse true? Is there a map <code>(prf q → prf r) → prf (q →' r)</code> ?</p>
</blockquote>
<p>Is it okay to assume "internal modus ponens", i.e. <code>P →' (P →' Q) →' Q</code>? I can prove the other form, that <code>(P →' Q) →' P →' Q)</code> easily from <code>P →' P</code>, but not this form.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292278):
<p>Did you see what Rohan did? He set up a whole theory of what it means to be able to syntactically deduce a formula from a set of formulae</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 22 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292311):
<blockquote>
<p>Did you see what Rohan did?</p>
</blockquote>
<p>I tried to.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292322):
<p>I don't understand this stuff too well; I had never realised the subtleties of the internal / external stuff.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 22 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292397):
<p>It's just that the standard Hilbertian formulation contains modus ponens as an axiom, so it seems like it should be ok to assume it.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136292460):
<p>If you want to tinker with the framework then you'll need to talk to someone who knows what's going on better than me. I thought that it should be possible to prove what you want, because the term is valid.</p>

#### [ Kevin Buzzard (Oct 22 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136294136):
<p><span class="user-mention" data-user-id="120559">@Rohan Mitta</span> maybe the whole Prop / Type thing is the Curry-Howard thing. If you were writing computer programs, e.g. if you thought that <code>P -&gt;' P</code> was the identity function, then you should be using <code>Type</code>. But if you're regarding it as a theorem I guess you should be using <code>Prop</code>.  I don't know how well <code>Type</code> plays with the contrapositive axiom because that's precisely the axiom that the computer programmers don't have.</p>

#### [ Scott Morrison (Oct 23 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136303803):
<blockquote>
<p>In our minds what is really going on is <code>have b : B := hab a, clear a hab,</code></p>
</blockquote>
<p>There's no reason one couldn't write a tactic that does this; just parse the expression, looking for appearances and named hypotheses, and clear any that aren't used anymore. (e.g. just by attempting to clear them).</p>

#### [ Scott Morrison (Oct 23 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136303850):
<p>You could call this <code>then</code>, rather than <code>have</code>, perhaps.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 23 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136322889):
<p>I formalised the proof on MSE, but had to assume two additional axioms:<br>
<a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/abhimanyu.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/abhimanyu.lean">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/abhimanyu.lean</a></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136322908):
<p>It's not as comprehensive as Rohan &amp; Enrico's, of course.</p>

#### [ Gabriel Ebner (Oct 23 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136323186):
<blockquote>
<p>maybe the whole Prop / Type thing is the Curry-Howard thing. If you were writing computer programs, e.g. if you thought that P -&gt;' P was the identity function, then you should be using Type</p>
</blockquote>
<p>The choice of whether to use Type or Prop is not between programs and proofs, or between intuitionistic and classical logic, but between proofs and provability---each choice models <em>different objects</em> in mathematical logic.  A proof is traditionally a finite tree of inferences, and it should live in Type.  However if you use the exact same constructors and just change the universe to Prop then you get a completely different structure: namely the set of theorems, which is the same as the set of tautologies (= valid propositional formulas) and does not have any relationship to proofs.  There are lots of things you can do with proofs, but not with provability alone.  For example you can define the size of a proof as a function <code>size {p} : prf p → ℕ</code> (for Hilbert-style calculi you'd typically want to measure the size as a DAG though, i.e., not counting duplicate subproofs more than once), and ask the question whether there are formulas whose proofs are necessarily exponential in size (easy exercise: every tautology has a proof of exponential size).  (We don't know.)  Such questions about the sizes of proofs in various proof systems for propositional logic are considered in the field of proof complexity.<br>
Many proof systems also admit interpolation: from a proof of <code>p → q</code> you can compute an interpolant (= formula <code>r</code> such that <code>p → r</code> and <code>r → q</code> such that <code>r</code> only contains the symbols occurring in both <code>p</code> and <code>q</code>).  This interpolant depends on the proof; i.e., different proofs give different interpolants.  Since the computation of the interpolant is typically polynomial-time, we get a relationship to proof size as well.<br>
These are just two prominent examples from propositional logic, where you actually want to talk about proofs and not just provability.  Sure, I've seen workarounds: instead of defining a size function for proofs, you could define a predicate "provable in at most n steps".  But from my point of view this is an awkward workaround.  Fundamentally, proofs are <em>data</em> and should be modelled as such.</p>

#### [ Gabriel Ebner (Oct 23 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136323892):
<blockquote>
<p>Is there a map (prf q → prf r) → prf (q →' r) ?</p>
</blockquote>
<p>It almost looks like the deduction theorem, but no, there cannot be such a map.  This is because the function <code>prf q → prf r</code> can do a case analysis on the <code>prf q</code>.  Concretely, there is a function <code>prf (atom 0) → prf r</code> for any <code>r</code> (by contradiction, because <code>atom 0</code> is not a tautology).  Hence you'd be able to obtain e.g. <code>prf (atom 0 →' atom 1)</code>, which is clearly not a tautology.  (This problem is related to the so-called "exotic terms" in HOAS, if you're interested.)</p>

#### [ Gabriel Ebner (Oct 23 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136324163):
<p>If you want to prove the deduction theorem, my suggestion would be to add a parameter <code>Γ : set fml</code> so that <code>prf Γ p</code> are the proofs of <code>p</code> from assumptions <code>Γ</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">prf</span> <span class="o">(</span><span class="err">Γ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">ass</span> <span class="o">(</span><span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="err">∈</span> <span class="err">Γ</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">p</span>
<span class="bp">|</span> <span class="n">axk</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axs</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axX</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">((</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span>
<span class="bp">|</span> <span class="n">mp</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span> <span class="c1">-- bracket change</span>

<span class="kn">infix</span> <span class="bp">`</span> <span class="err">⊢</span> <span class="bp">`</span><span class="o">:</span><span class="mi">30</span> <span class="o">:=</span> <span class="n">prf</span>

<span class="n">def</span> <span class="n">deduction_thm</span> <span class="o">{</span><span class="err">Γ</span> <span class="n">p</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">q</span><span class="o">},</span> <span class="err">Γ</span> <span class="err">∪</span> <span class="o">{</span><span class="n">p</span><span class="o">}</span> <span class="err">⊢</span> <span class="n">q</span> <span class="bp">→</span> <span class="err">Γ</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Oct 23 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136353019):
<p><span class="user-mention" data-user-id="120559">@Rohan Mitta</span> (working with someone called Enrico) introduced a new <code>consequence</code> type <a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/8df51accce766b8e33cae026203f85a8f87eed7e/src/rohan_enrico_success.lean#L34" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/8df51accce766b8e33cae026203f85a8f87eed7e/src/rohan_enrico_success.lean#L34">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/8df51accce766b8e33cae026203f85a8f87eed7e/src/rohan_enrico_success.lean#L34</a> which probably has the same effect. Rohan -- you see the trick Gabriel is suggesting? Instead of introducing the new type, modify the definition of the old one.</p>

#### [ Kevin Buzzard (Oct 23 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136358650):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> examined Rohan's proof term and then came up with a really minimised answer <a href="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/Chris_Hughes.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/Chris_Hughes.lean">https://github.com/ImperialCollegeLondon/M1F_Problems_class_question/blob/master/src/Chris_Hughes.lean</a></p>

#### [ Kevin Buzzard (Oct 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136358920):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> was asking how Chris' term can work with so much information missing. I told him that Lean sees the missing <code>{ }</code> variables as a big logic puzzle and it must have proved that there was a unique solution.</p>

#### [ Kevin Buzzard (Oct 23 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136359692):
<p>Abhi you could change the definition of <code>prf</code> back so that the variables are explicit, and then you could fill in everything in Chris' proof with <code>_</code>'s as required and then start adding and deleting hints for the elaborator.</p>

#### [ Kevin Buzzard (Oct 23 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136360475):
<p>Here's something I don't understand.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">prf</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">axk</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axs</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axX</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">((</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span>
<span class="bp">|</span> <span class="n">mp</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>

<span class="kn">open</span> <span class="n">prf</span>

<span class="kn">theorem</span> <span class="n">not_not_p_of_p</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)))</span> <span class="o">:=</span>
<span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="n">axk</span><span class="o">)</span>
  <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axk</span> <span class="n">axs</span><span class="o">))</span>
  <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axk</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axX</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axX</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="n">axs</span><span class="o">))</span> <span class="n">axX</span>
</pre></div>


<p>I liked the analogy between <code>@mp q r</code> and <code>@axs p q r</code> when <code>mp</code> was written the other way around, however:</p>
<div class="codehilite"><pre><span></span><span class="bp">|</span> <span class="n">mp&#39;</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>
</pre></div>


<p>and I was in my mind using this to justify <code>mp'</code> over <code>mp</code>. I wondered what would happen to Chris' proof if I replaced <code>mp</code> with <code>mp'</code> though? He has all these rows of <code>mp (mp (mp (mp (...</code>. Is this an indication that he's doing it right, doing it wrong, or are these big strings just irrelevant? Is this even an important question, which way round these inputs go?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 23 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136360843):
<blockquote>
<p>Here's something I don't understand.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">prf</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">axk</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axs</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axX</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">((</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span>
<span class="bp">|</span> <span class="n">mp</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>

<span class="kn">open</span> <span class="n">prf</span>

<span class="kn">theorem</span> <span class="n">not_not_p_of_p</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)))</span> <span class="o">:=</span>
<span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="n">axk</span><span class="o">)</span>
  <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axk</span> <span class="n">axs</span><span class="o">))</span>
  <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axk</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axX</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axX</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="n">axs</span><span class="o">))</span> <span class="n">axX</span>
</pre></div>


<p>I liked the analogy between <code>@mp q r</code> and <code>@axs p q r</code> when <code>mp</code> was written the other way around, however:</p>
<div class="codehilite"><pre><span></span><span class="bp">|</span> <span class="n">mp&#39;</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>
</pre></div>


<p>and I was in my mind using this to justify <code>mp'</code> over <code>mp</code>. I wondered what would happen to Chris' proof if I replaced <code>mp</code> with <code>mp'</code> though? He has all these rows of <code>mp (mp (mp (mp (...</code>. Is this an indication that he's doing it right, doing it wrong, or are these big strings just irrelevant? Is this even an important question, which way round these inputs go?</p>
</blockquote>
<p>Something interesting to note is that the internal counterpart of <code>mp'</code> (i.e. <code>prf ((p →' q) →' p →' q)</code>) is much easier to prove in our system (follows from <code>P →' P</code>) than <code>mp</code> (i.e. <code>prf (p →' (p →' q) →' q)</code>) -- at least, I wasn't able to prove the latter. Which gives an indication that in this system, where stuff like <code>intro</code> are not formalised, it does make a difference how you define <code>mp</code>.</p>

#### [ Alexandru-Andrei Bosinta (Oct 23 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136361087):
<blockquote>
<p>Here's something I don't understand.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">prf</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">axk</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axs</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axX</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">((</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span>
<span class="bp">|</span> <span class="n">mp</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>

<span class="kn">open</span> <span class="n">prf</span>

<span class="kn">theorem</span> <span class="n">not_not_p_of_p</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)))</span> <span class="o">:=</span>
<span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="n">axk</span><span class="o">)</span>
  <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axk</span> <span class="n">axs</span><span class="o">))</span>
  <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axk</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axX</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="n">axX</span> <span class="n">axk</span><span class="o">)</span> <span class="n">axs</span><span class="o">))</span> <span class="n">axs</span><span class="o">))</span> <span class="n">axX</span>
</pre></div>


<p>I liked the analogy between <code>@mp q r</code> and <code>@axs p q r</code> when <code>mp</code> was written the other way around, however:</p>
<div class="codehilite"><pre><span></span><span class="bp">|</span> <span class="n">mp&#39;</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>
</pre></div>


<p>and I was in my mind using this to justify <code>mp'</code> over <code>mp</code>. I wondered what would happen to Chris' proof if I replaced <code>mp</code> with <code>mp'</code> though? He has all these rows of <code>mp (mp (mp (mp (...</code>. Is this an indication that he's doing it right, doing it wrong, or are these big strings just irrelevant? Is this even an important question, which way round these inputs go?</p>
</blockquote>
<p>If you replace mp with mp' you would probably only have to switch all the arguments, but I don't think anything else has to be changed.</p>

#### [ Kevin Buzzard (Oct 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136361161):
<p>Right -- but it would be really boring doing that by hand. I did all the other substitutions using emacs.</p>

#### [ Kevin Buzzard (Oct 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136361184):
<p>this one is a more serious tree operation</p>

#### [ Kevin Buzzard (Oct 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136361186):
<p>actually I think I can do it using emacs</p>

#### [ Kenny Lau (Oct 23 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136362986):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">fml</span><span class="bp">.</span><span class="kn">eval</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">atom</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">i</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">fml</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">fml</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">b</span>
<span class="bp">|</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">¬</span><span class="n">fml</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">a</span>

<span class="n">def</span> <span class="n">prf</span><span class="bp">.</span><span class="kn">eval</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">p</span><span class="o">:</span><span class="n">fml</span><span class="o">,</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">p</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">f</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hpq</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hpq</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">axs</span> <span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hpqr</span> <span class="n">hpq</span> <span class="n">hp</span><span class="o">,</span> <span class="n">hpqr</span> <span class="n">hp</span> <span class="o">(</span><span class="n">hpq</span> <span class="n">hp</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">axX</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hmt</span> <span class="n">hp</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hnq</span><span class="o">,</span> <span class="n">hmt</span> <span class="n">hnq</span> <span class="n">hp</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">mp</span> <span class="n">p</span> <span class="n">q</span> <span class="n">hp</span> <span class="n">hpq</span><span class="o">)</span> <span class="o">:=</span> <span class="n">prf</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">_</span> <span class="n">hpq</span> <span class="o">(</span><span class="n">prf</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">_</span> <span class="n">hp</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Oct 23 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136363138):
<p>I think Chris did something clever with decidability?</p>

#### [ Rob Lewis (Oct 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364666):
<p>Kenny, that's a soundness proof. Now do completeness!</p>

#### [ Kenny Lau (Oct 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364680):
<p>heh</p>

#### [ Rob Lewis (Oct 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364686):
<p>Kevin, I think the strings of <code>mp (mp (mp...</code> are really just a sign of how awkward Hilbert systems are to use.</p>

#### [ Rob Lewis (Oct 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364743):
<p>Like, that's just what a proof in this calculus looks like.</p>

#### [ Rob Lewis (Oct 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364757):
<p>If for some reason you wanted to keep making these proofs, you'd design tools to assemble them from something more readable.</p>

#### [ Rob Lewis (Oct 23 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364772):
<p>i.e. natural deduction, or a tactic language.</p>

#### [ Kenny Lau (Oct 23 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364796):
<p>i.e. prove the deduction theorem</p>

#### [ Rob Lewis (Oct 23 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136364828):
<p>Jeremy has a related example for the sequent calculus here: <a href="https://github.com/avigad/embed/blob/master/src/examples.lean" target="_blank" title="https://github.com/avigad/embed/blob/master/src/examples.lean">https://github.com/avigad/embed/blob/master/src/examples.lean</a></p>

#### [ Kevin Buzzard (Oct 23 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136365197):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">not_not_p_of_p</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)))</span> <span class="o">:=</span>
<span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span>
           <span class="o">(</span><span class="n">axk</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
       <span class="o">)</span>
       <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">))</span>
                           <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">axk</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                               <span class="o">(</span><span class="n">axs</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                           <span class="o">)</span>
                       <span class="o">)</span>
                       <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">axk</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                               <span class="o">(</span><span class="n">axk</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                           <span class="o">)</span>
                           <span class="o">(</span><span class="n">axs</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                       <span class="o">)</span>
                   <span class="o">)</span>
                   <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">axX</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                           <span class="o">(</span><span class="n">axk</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                       <span class="o">)</span>
                       <span class="o">(</span><span class="n">axs</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                   <span class="o">)</span>
               <span class="o">)</span>
               <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">mp</span> <span class="o">(</span><span class="n">axX</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                       <span class="o">(</span><span class="n">axk</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
                   <span class="o">)</span>
                   <span class="o">(</span><span class="n">axs</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
               <span class="o">)</span>
           <span class="o">)</span>
           <span class="o">(</span><span class="n">axs</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
       <span class="o">)</span>
   <span class="o">)</span>
   <span class="o">(</span><span class="n">axX</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>


<p>It's not very often I think about proof trees. I know it's all awful to you computer scientists, but I'm still on the basics :-)</p>

#### [ Mario Carneiro (Oct 24 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136381508):
<p>by the way, I think this is actually a really good application of metamath. The whole logic is set up from these exact axioms of propositional calculus, by lucasiewicz. (Unfortunately I don't have any better naming suggestions - in metamath they are literally called ax-1, ax-2, ax-3 since that's what lucasiewicz called them)</p>

#### [ Mario Carneiro (Oct 24 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136381553):
<p>You should look at the derivations of some basic theorems - this is where metamath is most readable. Your theorem is <a href="http://us.metamath.org/mpeuni/notnot1.html" target="_blank" title="http://us.metamath.org/mpeuni/notnot1.html">notnot1</a></p>

#### [ Mario Carneiro (Oct 24 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136383658):
<p>Here is a moderately inlined version of the metamath proof. The key to making this readable is to break it into bite sized pieces of no more than five steps. Almost all of the intermediate steps are independently useful, even more than I'm showing here. Hilbert style axiomatizations are not meant to be used directly; you should prove as lemmas all the basic facts and use them as scaffolding to manage the complexity.</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">fml</span>
<span class="bp">|</span> <span class="n">atom</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">imp</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">not</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">fml</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">fml</span>

<span class="kn">infixr</span> <span class="bp">`</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">imp</span> <span class="c1">-- right associative</span>

<span class="kn">prefix</span> <span class="bp">`¬</span><span class="err">&#39;</span> <span class="bp">`</span><span class="o">:</span><span class="n">max</span> <span class="o">:=</span> <span class="n">fml</span><span class="bp">.</span><span class="n">not</span>

<span class="kn">inductive</span> <span class="n">prf</span> <span class="o">:</span> <span class="n">fml</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">axk</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axs</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">axX</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="err">$</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span>
<span class="bp">|</span> <span class="n">mp</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="n">prf</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">prf</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="n">prf</span> <span class="n">q</span>

<span class="kn">namespace</span> <span class="n">prf</span>
<span class="kn">prefix</span> <span class="bp">`</span><span class="err">⊢</span> <span class="bp">`</span><span class="o">:</span><span class="mi">30</span> <span class="o">:=</span> <span class="n">prf</span>

<span class="n">def</span> <span class="n">mp&#39;</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">q</span> <span class="o">:=</span> <span class="n">mp</span> <span class="n">h2</span> <span class="n">h1</span>
<span class="n">def</span> <span class="n">a1i</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span> <span class="err">⊢</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">mp&#39;</span> <span class="n">axk</span>
<span class="n">def</span> <span class="n">a2i</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="bp">→</span> <span class="err">⊢</span> <span class="o">(</span><span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">mp&#39;</span> <span class="n">axs</span>
<span class="n">def</span> <span class="n">con4i</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="err">⊢</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span> <span class="err">⊢</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">mp&#39;</span> <span class="n">axX</span>
<span class="n">def</span> <span class="n">mpd</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">mp&#39;</span> <span class="o">(</span><span class="n">a2i</span> <span class="n">h</span><span class="o">)</span>
<span class="n">def</span> <span class="n">syl</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">mpd</span> <span class="o">(</span><span class="n">a1i</span> <span class="n">h2</span><span class="o">)</span> <span class="n">h1</span>
<span class="n">def</span> <span class="n">id</span> <span class="o">{</span><span class="n">p</span><span class="o">}</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">mpd</span> <span class="n">axk</span> <span class="o">(</span><span class="bp">@</span><span class="n">axk</span> <span class="n">p</span> <span class="n">p</span><span class="o">)</span>
<span class="n">def</span> <span class="n">a1d</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="o">:=</span> <span class="n">syl</span> <span class="n">h</span> <span class="n">axk</span>
<span class="n">def</span> <span class="n">com12</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">syl</span> <span class="o">(</span><span class="n">a1d</span> <span class="n">id</span><span class="o">)</span> <span class="o">(</span><span class="n">a2i</span> <span class="n">h</span><span class="o">)</span>
<span class="n">def</span> <span class="n">con4d</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="o">:=</span> <span class="n">syl</span> <span class="n">h</span> <span class="n">axX</span>
<span class="n">def</span> <span class="n">absurd</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="err">⊢</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="o">:=</span> <span class="n">con4d</span> <span class="n">axk</span>
<span class="n">def</span> <span class="n">imidm</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="o">:=</span> <span class="n">mpd</span> <span class="n">h</span> <span class="n">id</span>
<span class="n">def</span> <span class="n">contra</span> <span class="o">{</span><span class="n">p</span><span class="o">}</span> <span class="o">:</span> <span class="err">⊢</span> <span class="o">(</span><span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span><span class="o">)</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">imidm</span> <span class="o">(</span><span class="n">con4d</span> <span class="o">(</span><span class="n">a2i</span> <span class="n">absurd</span><span class="o">))</span>
<span class="n">def</span> <span class="n">notnot2</span> <span class="o">{</span><span class="n">p</span><span class="o">}</span> <span class="o">:</span> <span class="err">⊢</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">syl</span> <span class="n">absurd</span> <span class="n">contra</span>
<span class="n">def</span> <span class="n">mpdd</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span> <span class="n">s</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="bp">→</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">mpd</span> <span class="o">(</span><span class="n">syl</span> <span class="n">h</span> <span class="n">axs</span><span class="o">)</span>
<span class="n">def</span> <span class="n">syld</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span> <span class="n">s</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">mpdd</span> <span class="o">(</span><span class="n">a1d</span> <span class="n">h2</span><span class="o">)</span> <span class="n">h1</span>
<span class="n">def</span> <span class="n">con2d</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="n">r</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span> <span class="o">:=</span> <span class="n">con4d</span> <span class="o">(</span><span class="n">syld</span> <span class="o">(</span><span class="n">a1i</span> <span class="n">notnot2</span><span class="o">)</span> <span class="n">h1</span><span class="o">)</span>
<span class="n">def</span> <span class="n">con2i</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">q</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">con4i</span> <span class="o">(</span><span class="n">syl</span> <span class="n">notnot2</span> <span class="n">h1</span><span class="o">)</span>
<span class="n">def</span> <span class="n">notnot1</span> <span class="o">{</span><span class="n">p</span><span class="o">}</span> <span class="o">:</span> <span class="err">⊢</span> <span class="n">p</span> <span class="bp">→</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="bp">¬</span><span class="err">&#39;</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">con2i</span> <span class="n">id</span>

<span class="kn">end</span> <span class="n">prf</span>
</pre></div>

#### [ Mario Carneiro (Oct 24 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136383668):
<p>If you are going for a direct from axioms proof, there is probably a faster way, but all you get from that is a big hideous proof term and no useful subparts</p>

#### [ Mario Carneiro (Oct 24 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136384232):
<p>One of my first papers was a proof that Hilbert style axiomatizations result in an O(1) additive overhead over natural deduction proof rules (i.e. the bulk of the proof is 1-1 matched to lemmas), so I respectfully disagree that hilbert systems are innately harder to use - there is just a bit more "honest toil" in showing that and, or, implies all exist and have the appropriate theorems as in natural deduction</p>

#### [ Kevin Buzzard (Oct 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136391718):
<p>Well I am very unimpressed that metamath starts so high up. What's wrong with just having Chris Barker's iota combinator and building everything from that? Guess you guys were just lazy</p>

#### [ Kevin Buzzard (Oct 24 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136391779):
<p>I like the way everyone is calling that third axiom <code>axX</code>. That was supposed to be a placeholder until a computer scientist told us the proper name...</p>

#### [ Kevin Buzzard (Oct 24 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136391780):
<p>Xcluded middle</p>

#### [ Kevin Buzzard (Oct 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136392655):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> note proof of <code>syl</code>. Mario thanks a <em>lot</em> for this -- when I had time I was going to take Chris' proof apart and turn it into a bunch of lemmas like this, that's why I was unravelling all the brackets. I see you also have <code>mp</code> the "wrong way round"</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136429594):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> It also wasn't meant to be intentionally obtuse, it is following a mishmash of logic and set theory textbooks where possible (everything is referenced too, so you can read along)</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136429649):
<p>The Lucasiewicz axioms seem to be pretty popular for hilbert style axiomatizations</p>

#### [ Mario Carneiro (Oct 24 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28M1F/P65%29%20syntactic%20entailment%20exercise/near/136429705):
<p>Metamath has <code>mp</code> the way you stated it, but it also has no notion of partial application. You will notice I make use of partially applied <code>mp'</code> a few times</p>


{% endraw %}
