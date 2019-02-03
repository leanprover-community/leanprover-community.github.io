---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85947ProgramminginLean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Programming in Lean](https://leanprover-community.github.io/archive/113488general/85947ProgramminginLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Jul 11 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129464604):
<p>The following code from Chapter 9 of Programming in Lean doesn't work in <code>lean-nightly-2018-04-20</code></p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">normalize_hyp</span> <span class="o">(</span><span class="n">lemmas</span> <span class="o">:</span> <span class="n">list</span> <span class="n">expr</span><span class="o">)</span> <span class="o">(</span><span class="n">hyp</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">try</span> <span class="o">(</span><span class="n">simp_at</span> <span class="n">hyp</span> <span class="n">lemmas</span><span class="o">)</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">normalize_hyps</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">hyps</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
<span class="n">lemmas</span> <span class="err">←</span> <span class="n">monad</span><span class="bp">.</span><span class="n">mapm</span> <span class="n">mk_const</span> <span class="o">[</span><span class="bp">``</span><span class="n">iff_iff_implies_and_implies</span><span class="o">,</span>
<span class="bp">``</span><span class="n">implies_iff_not_or</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_and_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_or_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_not_iff</span><span class="o">,</span>
<span class="bp">``</span><span class="n">not_true_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_false_iff</span><span class="o">],</span>
<span class="n">monad</span><span class="bp">.</span><span class="n">for&#39;</span> <span class="n">hyps</span> <span class="o">(</span><span class="n">normalize_hyp</span> <span class="n">lemmas</span><span class="o">)</span>
</pre></div>


<p>Can someone help me get it working??</p>

#### [ Simon Hudon (Jul 11 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465591):
<p>You can rewrite the first function as:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">normalize_hyp</span> <span class="o">(</span><span class="n">lemmas</span> <span class="o">:</span> <span class="n">list</span> <span class="n">expr</span><span class="o">)</span> <span class="o">(</span><span class="n">hyp</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">try</span> <span class="o">(</span><span class="n">simp_hyp</span> <span class="n">lemmas</span> <span class="o">[]</span> <span class="n">hyp</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Jul 11 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465655):
<p>For the second function, this should work:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">normalize_hyps</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">hyps</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
<span class="n">lemmas</span> <span class="err">←</span> <span class="n">list</span><span class="bp">.</span><span class="n">mmap</span> <span class="n">mk_const</span> <span class="o">[</span><span class="bp">``</span><span class="n">iff_iff_implies_and_implies</span><span class="o">,</span>
<span class="bp">``</span><span class="n">implies_iff_not_or</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_and_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_or_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_not_iff</span><span class="o">,</span>
<span class="bp">``</span><span class="n">not_true_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_false_iff</span><span class="o">],</span>
<span class="n">hyps</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="o">(</span><span class="n">normalize_hyp</span> <span class="n">lemmas</span><span class="o">)</span>
</pre></div>

#### [ Chris Hughes (Jul 11 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465732):
<p>It doesn't quite work. It complains lemmas has type <code>list expr</code> but needs to have type <code>simp_lemmas</code></p>

#### [ Chris Hughes (Jul 11 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465747):
<p>I'm a bit confused about the type <code>simp_lemmas</code>. It's defined as a constant, which seems a bit odd to me.</p>

#### [ Mario Carneiro (Jul 11 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465798):
<p>it's a special cached representation of a simp set</p>

#### [ Mario Carneiro (Jul 11 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465801):
<p>you should use the <code>simp_lemmas</code> functions to construct one</p>

#### [ Chris Hughes (Jul 11 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465810):
<p>So it looks almost like an inductive type, but they made all the constructors constants for some reason.</p>

#### [ Chris Hughes (Jul 11 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465815):
<p>I'll see if I can fix the list myself.</p>

#### [ Simon Hudon (Jul 11 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465842):
<p><code>simp_lemmas.append</code> and <code>simp_lemmas.mk</code> should be sufficient</p>

#### [ Simon Hudon (Jul 11 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465874):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">normalize_hyps</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">hyps</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
<span class="n">lemmas</span> <span class="err">←</span> <span class="n">list</span><span class="bp">.</span><span class="n">mmap</span> <span class="n">mk_const</span> <span class="o">[</span><span class="bp">``</span><span class="n">iff_iff_implies_and_implies</span><span class="o">,</span>
<span class="bp">``</span><span class="n">implies_iff_not_or</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_and_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_or_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_not_iff</span><span class="o">,</span>
<span class="bp">``</span><span class="n">not_true_iff</span><span class="o">,</span> <span class="bp">``</span><span class="n">not_false_iff</span><span class="o">],</span>
<span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">append</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">mk</span> <span class="n">lemmas</span><span class="o">,</span>
<span class="n">hyps</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="o">(</span><span class="n">normalize_hyp</span> <span class="n">lemmas</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Jul 11 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129465882):
<p>... and adjust <code>normalize_hyp</code> accordingly ;-)</p>

#### [ Kevin Buzzard (Jul 11 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129466489):
<p>Yesterday we found something else in PIL which didn't work any more (I think the first line was <code>open state</code> and already that failed IIRC). Maybe Chris and I should collect up some updates for Lean 3.4.1 and submit a PR. Would that sort of thing be welcome?</p>

#### [ Chris Hughes (Jul 11 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129466694):
<p>How does the notation with the backticks and brackets work? What's the difference between <code>'x</code>, <code>'''x</code>, <code>'''x</code>, <code>'(x)</code>, <code>''(x) and </code>'''(x)`?</p>

#### [ Mario Carneiro (Jul 11 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129467739):
<ul>
<li><code> `my.name</code> is the way to refer to a name. It is essentially a form of string quoting; no checks are done besides parsing dots into namespaced names</li>
<li><code> ``some </code> does name resolution at parse time, so it expands to <code> `option.some</code> and will error if the given name doesn't exist</li>
<li><code> `(my expr)</code> constructs an expression at parse time, resolving what it can in the current (of the tactic) namespace</li>
<li><code> ``(my pexpr)</code> constructs a pre-expression at parse time, resolving in the current (of the tactic) namespace</li>
<li><code> ```(my pexpr)</code> constructs a pexpr, but defers resolution to run time (of the tactic), meaning that any references will be resolved in the namespace of the begin end block of the user, rather than the tactic itself</li>
</ul>

#### [ Chris Hughes (Jul 11 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129468544):
<p>So can I give <code> ''(my pexpr)</code> when an <code>expr</code> is expected and it will elaborate it into an <code>expr</code> at parse time?</p>

#### [ Simon Hudon (Jul 11 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129468811):
<p>About back ticks and quoting them: you can include them <code> `` `(foo) `` </code> by using one more backtick to quote what's inside</p>

#### [ Simon Hudon (Jul 11 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129468833):
<p>And I produced the above by writing  <code> ``` `` `(foo) `` ``` </code></p>

#### [ Mario Carneiro (Jul 11 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129468922):
<p>If an <code>expr</code> is expected, then you should either use <code> `(my expr)</code> to construct one, or <code>to_expr ``(my pexpr)</code> or one of its variants to perform elaboration (but not name resolution) at run time</p>

#### [ Sebastien Gouezel (Jul 11 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471102):
<p>I see you are starting a very useful cheat sheet on backticks. Maybe you could add a word on <code> `[apply %%h]</code>? (as far as I can tell, it is not mentioned in Programming in Lean)</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471295):
<p><code> `[tac...] </code> is exactly the same as <code>begin tac... end</code> in the sense that it parses <code>tac...</code> using the interactive mode parser, but instead of evaluating the tactic to produce a term, it just wraps up the list of tactics as a single tactic of type <code>tactic unit</code>. This is useful for writing "macros" or light-weight tactic writing</p>

#### [ Chris Hughes (Jul 11 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471423):
<p>What is <code>%%</code>? I couldn't find it in programming in lean.</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471498):
<p>Re <code>%%</code>: This is called anti-quotation, and is supported in all the expr and pexpr quoting expressions <code> `(expr)</code>,  <code> ``(pexpr)</code>,  <code> ```(pexpr)</code>, as well as <code> `[tacs]</code>. Wherever an expression is expected inside one of these quoting constructs, you can use <code>%%e</code> instead, where <code>e</code> has type <code>expr</code> in the outer context of the tactic, and it will be spliced into the constructed expr/pexpr/etc.</p>

#### [ Chris Hughes (Jul 11 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471551):
<p>are <code> ` </code> and <code>%%</code> notation for some function or some deeper inbuilt thing?</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471568):
<p>a bit of both</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471589):
<p>It is difficult to completely replicate the behavior of the quoting expressions, but <code>%%</code> is supported through <code>pexpr.subst</code> if I recall correctly</p>

#### [ Chris Hughes (Jul 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471593):
<p>so <code>%%</code> turns an <code>expr</code> into the thing that the <code>expr</code> represents, like a <code>real</code> or a <code>nat</code> or something?</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471638):
<p>You can always just write it down and then inspect the resulting tactic with <code>#print</code> to find out how the sausage is made</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471654):
<p>No, <code>%%</code> inserts the <code>expr</code> into a hole in another <code>expr</code> you are creating</p>

#### [ Mario Carneiro (Jul 11 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471681):
<p>For example, if <code>a b : expr</code> then <code> `(%%a + %%b)</code> is of type <code>expr</code></p>

#### [ Mario Carneiro (Jul 11 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471748):
<p>Probably <code>a</code> and <code>b</code> are expressions for something of type <code>nat</code>, say, and then the resulting <code>expr</code> will also be a valid expression for a <code>nat</code></p>

#### [ Mario Carneiro (Jul 11 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129471969):
<p>Also worth mentioning are <code>expr</code> pattern matches, which have the same syntax like <code> `(%%a + %%b)</code>. These can be used in the pattern position of a <code>match</code> or on the left side of a <code>&lt;-</code> in do notation, and will destruct an expression and bind the antiquoted variables</p>

#### [ Mario Carneiro (Jul 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129472100):
<p>For example, if <code>e</code> is an expression then <code>do `(%%a = %%b) &lt;- return e, ...</code> will check that <code>e</code> is an equality, and bind the LHS and RHS to <code>a</code> and <code>b</code> (of type <code>expr</code>), and if it is not an equality the tactic will fail</p>

#### [ Chris Hughes (Jul 11 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129472732):
<p>so when you say <code> `(my expr)  </code>, <code>my expr</code> is not an object of type <code>expr</code> it's an actual expression like <code> `(2 + 2) </code></p>

#### [ Mario Carneiro (Jul 11 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129472907):
<p>right</p>

#### [ Chris Hughes (Jul 11 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129482162):
<p>How do tactics that take arguments work? I'm trying to write the easiest tactic I could think of, which basically does <code>apply quotient.induction_on, intros</code> I'm not sure what the type of the argument to the tactic should be, or even if it should be an argument. I couldn't find anything in <code>PIL</code> on this.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">qcases</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">pexpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="bp">`</span><span class="o">[</span><span class="n">apply</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="err">%%</span><span class="n">x</span><span class="o">,</span> <span class="n">intro</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">sorry</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">qcases</span> <span class="n">x</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Sebastian Ullrich (Jul 11 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129483237):
<p>See section 6 of <a href="https://leanprover.github.io/papers/tactic.pdf" target="_blank" title="https://leanprover.github.io/papers/tactic.pdf">https://leanprover.github.io/papers/tactic.pdf</a>; this is the best source for tactic writing, because it's the only one</p>

#### [ Chris Hughes (Jul 11 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129483792):
<p>Thanks.</p>

#### [ Chris Hughes (Jul 13 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129608241):
<p>One thing I've noticed is that putting tactics in the <code>tactic.interactive</code> namespace changes their behaviour. For example the following code.<br>
Should all tactics be in the <code>tactic.interactive</code> namespace? What difference does this namespace make to their behaviour?</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span> <span class="n">interactive</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">skip2</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">texpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="bp">`</span><span class="o">[</span><span class="n">skip</span><span class="o">]</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">skip3</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="bp">`</span><span class="o">[</span><span class="n">skip</span><span class="o">]</span>

<span class="kn">namespace</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">skip4</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">texpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="bp">`</span><span class="o">[</span><span class="n">skip</span><span class="o">]</span>

<span class="kn">end</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">sorry</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">skip4</span> <span class="n">s</span><span class="o">,</span> <span class="c1">--works</span>
  <span class="n">skip3</span><span class="o">,</span>   <span class="c1">--works</span>
  <span class="n">skip2</span> <span class="n">s</span><span class="o">,</span> <span class="c1">--fails</span>
<span class="kn">end</span>
</pre></div>

#### [ Sebastian Ullrich (Jul 13 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129608635):
<p>Also section 6 :)</p>

#### [ Kevin Buzzard (Jul 13 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129614422):
<p>The interactive namespace is where the tactics which you use in tactic mode live. Is there a difference between <code>by x</code> and <code>begin x end</code>?</p>

#### [ Simon Hudon (Jul 13 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129615276):
<p>I think officially, <code>begin x end</code> is shorthand for <code>by { x }</code></p>

#### [ Chris Hughes (Jul 14 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129654459):
<p>So if I look at the definition of <code>monad</code>, and some other definitions in <code>tactic.interactive</code>, there are <code>:=</code> in places I haven't seen them before. What does it mean to put a <code>:=</code> in a field of a structure like this? Same question for the <code>cfg</code> argument of <code>dunfold</code>.</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">monad</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">applicative</span> <span class="n">m</span><span class="o">,</span> <span class="n">has_bind</span> <span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="o">(</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">map</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&gt;&gt;=</span> <span class="n">pure</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span>
<span class="o">(</span><span class="n">seq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="bp">&gt;&gt;=</span> <span class="o">(</span><span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">x</span><span class="o">))</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">dunfold</span> <span class="o">(</span><span class="n">cs</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">ident</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">location</span><span class="o">)</span> <span class="o">(</span><span class="n">cfg</span> <span class="o">:</span> <span class="n">dunfold_config</span> <span class="o">:=</span> <span class="o">{})</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
</pre></div>

#### [ Patrick Massot (Jul 14 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129654705):
<p>Aren't they default values for these fields?</p>

#### [ Chris Hughes (Jul 14 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129655071):
<p>I thought that's what they probably were, but I wasn't sure.</p>

#### [ Patrick Massot (Jul 14 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129655083):
<p>see <a href="https://leanprover.github.io/reference/declarations.html#structures-and-records" target="_blank" title="https://leanprover.github.io/reference/declarations.html#structures-and-records">https://leanprover.github.io/reference/declarations.html#structures-and-records</a></p>

#### [ Patrick Massot (Jul 14 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129655118):
<blockquote>
<p>Lean also allows you to specify a default value for any field in a structure by writing (fieldᵢ : βᵢ := t).</p>
</blockquote>

#### [ Kevin Buzzard (Jul 14 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129657371):
<p>Here's an example from core lean (init/algebra/order):</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">preorder</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">has_le</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_lt</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">le_refl</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span>
<span class="o">(</span><span class="n">le_trans</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span>
<span class="o">(</span><span class="n">lt</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span>
<span class="o">(</span><span class="n">lt_iff_le_not_le</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="bp">.</span> <span class="n">order_laws_tac</span><span class="o">)</span>
</pre></div>


<p>I guess it means you can either skip the definition of <code>lt</code> or decide to over-write</p>

#### [ Chris Hughes (Jul 14 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659353):
<p>Another thing that's very odd about the <code>meta</code> code is the use of the <code>constant</code> keyword everywhere. If I look at the type <code>simp_lemmas</code> for example, it's almost like an inductive type, but all the constructors are constants. This just seems totally unworkable to me, because there aren't any eliminators. Is this because this stuff interfaces with C++ code? Or is this some weird case of the programming with expressions rather than data, where defeq terms can give different behaviour if they are syntactically different.</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">mk</span> <span class="o">:</span> <span class="n">simp_lemmas</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">join</span> <span class="o">:</span> <span class="n">simp_lemmas</span> <span class="bp">→</span> <span class="n">simp_lemmas</span> <span class="bp">→</span> <span class="n">simp_lemmas</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">erase</span> <span class="o">:</span> <span class="n">simp_lemmas</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">simp_lemmas</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">mk_default</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">simp_lemmas</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">simp_lemmas</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">simp_lemmas</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">add_simp</span> <span class="o">:</span> <span class="n">simp_lemmas</span> <span class="bp">→</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">simp_lemmas</span>
<span class="n">meta</span> <span class="kn">constant</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">add_congr</span> <span class="o">:</span> <span class="n">simp_lemmas</span> <span class="bp">→</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">simp_lemmas</span>
</pre></div>

#### [ Mario Carneiro (Jul 14 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659882):
<p>It's not an inductive type</p>

#### [ Mario Carneiro (Jul 14 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659925):
<p>that's why there are no eliminators</p>

#### [ Mario Carneiro (Jul 14 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659944):
<p>The reason it's all meta constants is, as you say, that it is interfacing with C++</p>

#### [ Mario Carneiro (Jul 14 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129659946):
<p>these are all just hooks to C++ functions</p>

#### [ Mario Carneiro (Jul 14 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Programming%20in%20Lean/near/129660104):
<p>If by "eliminator" you mean "a way to use this <code>simp_lemmas</code> thing once I've built one", that would be in tactics like <code>ext_simplify_core</code> and such that accept a <code>simp_lemmas</code> object to simp with</p>


{% endraw %}
