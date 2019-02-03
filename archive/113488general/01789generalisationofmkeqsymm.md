---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01789generalisationofmkeqsymm.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [generalisation of mk_eq_symm](https://leanprover-community.github.io/archive/113488general/01789generalisationofmkeqsymm.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Mar 16 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123790494):
<p>I am really struggling to write a tactic that "does mk_eq_symm, but even inside binders". I would like to have something that given <code>h : \forall x : X, f x = g x</code>, spits back <code>\forall x : X, g x = f x</code>. Can anyone point me in the right direction?</p>

#### [ Scott Morrison (Mar 16 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123790545):
<p>(I need this to work its way through arbitrarily many binders, possibly zero.)</p>

#### [ Scott Morrison (Mar 16 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123790763):
<p>So far I have</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">mk_eq_symm_under_binders_aux</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
                             <span class="n">b&#39;</span> <span class="err">←</span> <span class="n">mk_eq_symm_under_binders_aux</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="n">e</span> <span class="n">b</span><span class="o">)</span> <span class="n">b</span><span class="o">,</span>
                             <span class="n">pure</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span> <span class="n">b&#39;</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">e</span> <span class="n">t</span> <span class="o">:=</span> <span class="n">mk_eq_symm</span> <span class="n">e</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">mk_eq_symm_under_binders</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">e</span><span class="o">,</span> <span class="n">mk_eq_symm_under_binders_aux</span> <span class="n">e</span> <span class="n">t</span>
</pre></div>

#### [ Kevin Buzzard (Mar 16 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123790818):
<p>Whilst of course I can't help, the recent thread here about using rw really opened my eyes to how this sort of thing wasn't "happening by default" as it were. I am still a little unclear about why <code>eq.symm</code> can't be used directly but this is probably just my poor understanding of the notion of equality in type theory. If I had write a tactic proof which did this I would just continually apply conv to everything.</p>

#### [ Scott Morrison (Mar 16 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791017):
<p>Yes! I know how to achieve this with <code>conv</code>. I need this tactic in service of my "rewrite searching" tactic, unfortunately, so a human isn't available to help direct the <code>conv</code>. I need to be able to determine if a rewrite is applying to the entire expression, or just a subexpression, but the only way to ask Lean to rewrite an entire expression seems to be via <code>simp_lemmas.rewrite</code>, which doesn't provide a facility for applying the rule in reverse, so I'm going to have to build the reverse rule myself.</p>

#### [ Scott Morrison (Mar 16 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791083):
<p>But what I have above is stupid. The <code>expr.app e b</code> is silly, it's not <code>b</code> that I'm meant to put in there, it's.... something. :-)</p>

#### [ Kevin Buzzard (Mar 16 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791084):
<p>I am a little disappointed that something like <code>repeat {by conv in (_ = _) {rw eq.symm}}</code> doesn't work in tactic mode :-)</p>

#### [ Kevin Buzzard (Mar 16 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791093):
<p>Or, more precisely, that I couldn't get it to work :-)</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791337):
<p>I wrote an extremely similar tactic for <code>alias</code></p>

#### [ Scott Morrison (Mar 16 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791338):
<p>I think my fundamental difficulty is I don't know how to construct an <code>expr.lam</code>.</p>

#### [ Scott Morrison (Mar 16 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791345):
<p>I will look at <code>alias</code>!</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791349):
<div class="codehilite"><pre><span></span>meta def mk_iff_mp_app (iffmp : name) : expr → (nat → expr) → tactic expr
| (expr.pi n bi e t) f := expr.lam n bi e &lt;$&gt; mk_iff_mp_app t (λ n, f (n+1) (expr.var n))
| `(%%a ↔ %%b) f := pure $ @expr.const tt iffmp [] a b (f 0)
| _ f := fail &quot;Target theorem must have the form `Π x y z, a ↔ b`&quot;
</pre></div>

#### [ Scott Morrison (Mar 16 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791350):
<p>e.g., if I have <code>f : \nat \to \nat</code>, how to I construct the <code>expr</code> for <code>\lambda n, f (n+1)</code>?</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791390):
<p>That tactic directly constructs a proof of <code>\forall x y z, a -&gt; b</code> from <code>\forall x y z, a &lt;-&gt; b</code></p>

#### [ Mario Carneiro (Mar 16 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791405):
<p>I don't think it even needs to be a tactic (I only used a tactic in that case so I could fail with a nice error message)</p>

#### [ Scott Morrison (Mar 16 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791446):
<p>So how does <code>expr.var</code> work?</p>

#### [ Scott Morrison (Mar 16 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791447):
<p>That has me confused.</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791450):
<p><code>expr.var</code> is a de bruijn variable</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791456):
<p>so <code>\forall x y z, x = y</code> becomes roughly <code>pi "x" (pi "y" (pi "z" (app (app (const "eq") (var 2)) (var 1)))</code></p>

#### [ Mario Carneiro (Mar 16 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791506):
<p>the number counts how many binders back the variable is</p>

#### [ Scott Morrison (Mar 16 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791513):
<p>I see. (Or, at least I can imagine writing voodoo code based on what I see. :-)</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791558):
<p>I have an aversion to writing code that has suboptimal asymptotics, so I may have been too clever in the definition there, what with the accumulation function and all</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791609):
<p>Also, I don't think you will be able to use <code>mk_eq_symm</code> in the function</p>

#### [ Kevin Buzzard (Mar 16 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791613):
<p>I guess one question for Scott then is whether he is likely to be applying his tactic to terms built from strings of length 10^10 :-)</p>

#### [ Scott Morrison (Mar 16 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791616):
<p>What will go wrong with <code>mk_eq_symm</code>?</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791617):
<p>because when you are working on an expr manually like this, you have to deal with open terms, and tactics don't like open terms</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791624):
<p>open meaning containing an unbound <code>var</code></p>

#### [ Scott Morrison (Mar 16 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791625):
<p>(Or you can let me find out for myself in a minute or two..)</p>

#### [ Scott Morrison (Mar 16 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791628):
<p>I see. But I can just build it directly myself?</p>

#### [ Scott Morrison (Mar 16 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791630):
<p>(as you did in your example)</p>

#### [ Mario Carneiro (Mar 16 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791670):
<p>yes</p>

#### [ Kevin Buzzard (Mar 16 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791690):
<p>Is it just a coincidence that Mario posted code with the line <code>lam n, f (n+1)</code> seconds before Scott asked about how to construct the <code>expr</code> for <code>lam n, f (n+1)</code>?</p>

#### [ Scott Morrison (Mar 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791736):
<p>apparently yes :-)</p>

#### [ Scott Morrison (Mar 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791740):
<p>They have nothing to do with each other. :-)</p>

#### [ Scott Morrison (Mar 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791741):
<p>(and wow, this looks like it may be working!)</p>

#### [ Kevin Buzzard (Mar 16 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791747):
<p>I thought so but I thought I'd ask as I am frantically cut-and-pasting into a text file and just wanted to check that zulip didn't have some "slightly re-order the messages" functionality</p>

#### [ Kevin Buzzard (Mar 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791810):
<p>It's about time I learnt something about tactics and one way of learning is to write some docs.</p>

#### [ Scott Morrison (Mar 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791850):
<p>Thank you all! Things are looking good here. :-) <code>all_rewrites</code> seems to be working, finding lots of rewrites that <code>rw</code> itself can't see.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791853):
<p>Can you post what you wrote?</p>

#### [ Kevin Buzzard (Mar 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791854):
<p>[if you're happy to do so of course!]</p>

#### [ Scott Morrison (Mar 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791855):
<p>It's probably slow as molasses ... but that's a different problem.</p>

#### [ Scott Morrison (Mar 16 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791902):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">mk_eq_symm_under_binders_aux</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="o">(</span><span class="n">nat</span> <span class="bp">→</span> <span class="n">expr</span><span class="o">)</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">pi</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span> <span class="n">b</span><span class="o">)</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">n</span> <span class="n">bi</span> <span class="n">d</span> <span class="bp">&lt;</span><span class="err">$</span><span class="bp">&gt;</span> <span class="n">mk_eq_symm_under_binders_aux</span> <span class="n">b</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">var</span> <span class="n">n</span><span class="o">))</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">a</span> <span class="bp">=</span> <span class="err">%%</span><span class="n">b</span><span class="o">)</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">mk_eq_symm</span> <span class="o">(</span><span class="n">e</span> <span class="mi">0</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">fail</span> <span class="s2">&quot;expression must have the form `Π x y z, a = b`&quot;</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">mk_eq_symm_under_binders</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">e</span><span class="o">,</span> <span class="n">mk_eq_symm_under_binders_aux</span> <span class="n">t</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">e</span><span class="o">)</span>
</pre></div>

#### [ Scott Morrison (Mar 16 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791903):
<p>That's just the <code>mk_eq_symm_under_binders</code> part.</p>

#### [ Scott Morrison (Mar 16 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791907):
<p>Then there's</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">rewrite_entire</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="o">(</span><span class="n">expr</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">))</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="o">(</span><span class="n">expr</span> <span class="bp">×</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">do</span> <span class="k">let</span> <span class="n">sl</span> <span class="o">:=</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">mk</span><span class="o">,</span>
   <span class="n">r&#39;</span> <span class="err">←</span> <span class="k">if</span> <span class="n">r</span><span class="bp">.</span><span class="mi">2</span> <span class="k">then</span> <span class="n">mk_eq_symm_under_binders</span> <span class="n">r</span><span class="bp">.</span><span class="mi">1</span> <span class="k">else</span> <span class="n">pure</span> <span class="n">r</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
   <span class="n">sl</span> <span class="err">←</span> <span class="n">sl</span><span class="bp">.</span><span class="n">add</span> <span class="n">r&#39;</span><span class="o">,</span>
   <span class="n">sl</span><span class="bp">.</span><span class="n">rewrite</span> <span class="n">e</span>
</pre></div>

#### [ Scott Morrison (Mar 16 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791924):
<p>which given <code>r</code>, a rule and a <code>bool</code> flag indicating whether to use the rule in reverse, and an expression <code>e</code>, either rewrite the entire expression <code>e</code> using the rule, returning the replacement and the proof, or fails.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791965):
<p>Now I will tell my students to alias rw to this and they will never have to worry about why it used to sometimes fail :-)</p>

#### [ Scott Morrison (Mar 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791971):
<p>And then there's <a href="https://gist.github.com/semorrison/9b3a0f42fbd697d562a8b6daa960f14e" target="_blank" title="https://gist.github.com/semorrison/9b3a0f42fbd697d562a8b6daa960f14e">https://gist.github.com/semorrison/9b3a0f42fbd697d562a8b6daa960f14e</a></p>

#### [ Scott Morrison (Mar 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791976):
<p>for the actual implementation of <code>all_rewrites</code></p>

#### [ Scott Morrison (Mar 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791977):
<p>which still needs a little more wrapper before you can use it in interactive mode...</p>

#### [ Kevin Buzzard (Mar 16 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123792018):
<p>Thanks for this. I know I could just try to learn tactics by reading the tactic code in core Lean etc but the problem with doing that is that it can often be pretty hard-core. It's like trying to learn Lean by reading core lean and instantly finding opt_params everywhere with no explanation as to what they are.</p>


{% endraw %}
