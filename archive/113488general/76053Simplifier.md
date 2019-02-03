---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76053Simplifier.html
---

## Stream: [general](index.html)
### Topic: [Simplifier](76053Simplifier.html)

---


{% raw %}
#### [ Sebastien Gouezel (Oct 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326024):
<p>I'm realizing I don't understand how the simplifier works. I have a complicated goal involving product spaces, and in the middle of this goal there is the expression <code>(f, x).fst</code>. When I apply <code>simp</code> to my goal, it does not reduce to <code>f</code>. To help simp, I wrote down an auxiliary statement exactly with the good types and elements <code>f</code> and <code>x</code>, but still it does not help <code>simp</code>. Even when I turn on <code>set_option pp.all true</code> I can't see what is wrong.<br>
My helper lemma is <code>should_help : (prod.mk f x).fst = f</code>. Fully expanded, it reads</p>
<div class="codehilite"><pre><span></span><span class="n">should_help</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span><span class="bp">+</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">bounded_continuous_function</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="bp">_</span><span class="n">inst_2</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">prod</span><span class="bp">.</span><span class="n">fst</span><span class="bp">.</span><span class="o">{(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">bounded_continuous_function</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="bp">_</span><span class="n">inst_2</span><span class="o">)</span> <span class="n">α</span>
       <span class="o">(</span><span class="bp">@</span><span class="n">prod</span><span class="bp">.</span><span class="n">mk</span><span class="bp">.</span><span class="o">{(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">bounded_continuous_function</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="bp">_</span><span class="n">inst_2</span><span class="o">)</span> <span class="n">α</span> <span class="n">f</span> <span class="n">x</span><span class="o">))</span>
    <span class="n">f</span>
</pre></div>


<p>And in my goal I have the lines</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="bp">@</span><span class="n">prod</span><span class="bp">.</span><span class="n">fst</span><span class="bp">.</span><span class="o">{(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">bounded_continuous_function</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="bp">_</span><span class="n">inst_2</span><span class="o">)</span> <span class="n">α</span>
                         <span class="o">(</span><span class="bp">@</span><span class="n">prod</span><span class="bp">.</span><span class="n">mk</span><span class="bp">.</span><span class="o">{(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">bounded_continuous_function</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">α</span> <span class="n">β</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="bp">_</span><span class="n">inst_2</span><span class="o">)</span> <span class="n">α</span> <span class="n">f</span> <span class="n">x</span><span class="o">))</span>
</pre></div>


<p>Can someone explain why <code>simp [should_help]</code> does not reduce this term to <code>f</code>? (I can certainly work it around, but still I would be very happy to understand what is going on here...)</p>

#### [ Gabriel Ebner (Oct 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326122):
<p>Does <code>dsimp</code> work?</p>

#### [ Sebastien Gouezel (Oct 23 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326263):
<p>Yes it does.</p>

#### [ Gabriel Ebner (Oct 23 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326513):
<p>Then welcome to dependent type theory!  Basically <code>simp</code> can only rewrite at non-dependent arguments.  The automatically generated congruence lemmas only have hypotheses for the non-dependent arguments.  We could also rewrite at dependent arguments, but then you'd get casts all over the place.</p>

#### [ Sebastien Gouezel (Oct 23 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136326860):
<p>OK. Not sure I really understand: is the problem the fact that my type is <code>@bounded_continuous_function.{u v} α β _inst_1 _inst_2</code>, so depending on other types and instances? In any case, thanks a lot, I will add <code>dsimp</code> to my toolbox and try to apply it when <code>simp</code> does not work, even if I don't know why. (And this is a perfectly well-defined and efficient algorithm!)</p>

#### [ Gabriel Ebner (Oct 23 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136327235):
<p>No, I think the problem is that <code>prod.fst ...</code> <em>occurs</em> as a subterm of some dependent argument, and hence simp cannot reach it.</p>

#### [ Floris van Doorn (Oct 23 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136351767):
<p>Consider the following example: suppose <code>h</code> has type <code>is_prime (1+n)</code> and somewhere in the goal I have <code>⟨1+n, h⟩</code> as a subterm. Suppose I want to rewrite <code>1+n</code> to <code>n+1</code> using (using <code>rw [add.comm 1 n]</code> or <code>simp</code>) then I get the subterm <code>⟨1+n, h⟩</code>, but this is not type correct: <code>h</code> has type <code>is_prime (1+n)</code>, not type <code>is_prime (n+1)</code>. Therefore, <code>rw</code> and <code>simp</code> will fail if you do this.</p>
<p>Now we modify the example, and <code>h</code> has type <code>is_prime (1+4)</code>. <code>1+4</code> and <code>5</code> are definitionally equal, which implies that <code>h</code> <em>also</em> has type <code>is_prime 5</code>. Therefore, if your goal contains <code>⟨2+3, h⟩</code> you are allowed to rewrite this to <code>⟨5, h⟩</code>. However, <code>simp</code> and <code>rw</code> will not do this for you, but <code>dsimp</code> (which only rewrites with definitional equalities) happily will.</p>

#### [ Mario Carneiro (Oct 23 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136352123):
<p>simp should handle this</p>

#### [ Mario Carneiro (Oct 23 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136353224):
<p>simp will produce a term like <code>⟨1+n, cast (add_comm 1 n) h⟩</code></p>

#### [ Floris van Doorn (Oct 23 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136356668):
<p>Oh yeah, my example is wrong, <code>simp</code> does handly my case correctly.</p>

#### [ Floris van Doorn (Oct 23 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136356985):
<p>but only because <code>is_prime</code> is a proposition. If you replace <code>is_prime</code> by <code>vector bool</code> or anything else living in <code>Type*</code>, then what I described is correct.</p>

#### [ Mario Carneiro (Oct 23 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simplifier/near/136357623):
<p>Actually it will work as long as the second argument is a subsingleton. This is because this cast thing is being inserted by the congr lemma, that automatically discharges subsingleton arguments (even if they are in Type)</p>


{% endraw %}
