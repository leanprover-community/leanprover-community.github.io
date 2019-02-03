---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90140inductiveoccurrenceunderatypeconstructor.html
---

## Stream: [general](index.html)
### Topic: [inductive occurrence under a type constructor](90140inductiveoccurrenceunderatypeconstructor.html)

---


{% raw %}
#### [ Arseniy Alekseyev (Jul 18 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838639):
<p>I've got a rose tree definition:</p>
<div class="codehilite"><pre><span></span>inductive tree : Type
| branch : list tree -&gt; tree
</pre></div>


<p>The interesting/unusual part here is that the recursive occurrence of "tree" is inside a list, so this can only work if <code>list</code> is strictly positive, which makes elaboration perhaps tricky, but it does get accepted.<br>
On this type I defined a function:</p>
<div class="codehilite"><pre><span></span>open tree
def f : tree → string
| (branch _) := &quot;hello&quot;
</pre></div>


<p>which works</p>
<div class="codehilite"><pre><span></span>#eval (f (branch []))
-- ^ &quot;hello&quot;
</pre></div>


<p>but refuses to compute during typechecking:</p>
<div class="codehilite"><pre><span></span>example : f (branch []) = &quot;hello&quot; :=
  eq.refl &quot;hello&quot;
-- type mismatch, term
--   eq.refl &quot;hello&quot;
-- has type
--   &quot;hello&quot; = &quot;hello&quot;
-- but is expected to have type
--   f (branch list.nil) = &quot;hello&quot;
</pre></div>


<p>I poked around the <code>_mut_</code> and found that the thing gets elaborates to something roughly like this:</p>
<div class="codehilite"><pre><span></span>mutual inductive tree, lst
with tree : Type
| branch : lst -&gt; tree
with lst : Type
| nil : lst
| cons : tree → lst → lst
</pre></div>


<p>And if I do this encoding manually then the function suddenly computes fine.</p>
<p>Basically my question is: what's going wrong in the original example?</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838763):
<blockquote>
<p>The interesting/unusual part here is that the recursive occurrence of "tree" is inside a list, so this can only work if list is strictly positive, which makes elaboration perhaps tricky, but it does get accepted.</p>
</blockquote>
<p>Lean compiles nested inductive types like these to plain inductive types by unfolding the inductive definitions under the hood. This usually doesn't matter so much but you should be aware that this isn't the kernel being lenient, it is the equation compiler doing extra work</p>

#### [ Arseniy Alekseyev (Jul 18 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838764):
<p>Having formulated the question now I can find a relevant wiki page too: <a href="https://github.com/leanprover/lean/wiki/Inductive-datatypes" target="_blank" title="https://github.com/leanprover/lean/wiki/Inductive-datatypes">https://github.com/leanprover/lean/wiki/Inductive-datatypes</a>. I guess the answer is making it compute is hard.</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838837):
<blockquote>
<p>but refuses to compute during typechecking:</p>
</blockquote>
<p>The equation compiler defaults to well founded recursion for definitions on mutual and nested inductives. These have the side effect that the definition's equalities are not by rfl, so you have to use the provided equalities instead of definitional equality</p>

#### [ Arseniy Alekseyev (Jul 18 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838862):
<p>do those have predictable names?</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838923):
<p>they are called <code>f.equations.stuff</code> but <code>rw</code>, <code>simp</code> and <code>unfold</code> will use them by direct reference to the definition:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">branch</span> <span class="o">[])</span> <span class="bp">=</span> <span class="s2">&quot;hello&quot;</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">f</span>
</pre></div>

#### [ Mario Carneiro (Jul 18 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838932):
<p><code>rw f</code> and <code>simp [f]</code> also work</p>

#### [ Arseniy Alekseyev (Jul 18 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838984):
<p>oh!</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129838985):
<div class="codehilite"><pre><span></span>#print prefix f
</pre></div>


<div class="codehilite"><pre><span></span>f : tree → string
f._main : tree → string
f._main.equations._eqn_1 : ∀ (_x : list tree), f._main (branch _x) = &quot;hello&quot;
f._sunfold : tree → string
f.equations._eqn_1 : ∀ (_x : list tree), f (branch _x) = &quot;hello&quot;
</pre></div>


<p>the operative lemma is <code>f.equations._eqn_1</code></p>

#### [ Arseniy Alekseyev (Jul 18 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839065):
<p>Do #eval/#reduce also use these equations then? (they are both able to reduce this)</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839079):
<p><code>#reduce</code> does not, it unfolds everything by rfl but it also unfolds theorems and stuff as well which is what makes this work</p>

#### [ Arseniy Alekseyev (Jul 18 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839147):
<p>Those f.equations are pretty cool, thank you!</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839192):
<p><code>#eval</code> does not use equations at all, it does unbounded recursion using the original match equations and ignores all the encoding stuff</p>

#### [ Mario Carneiro (Jul 18 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20occurrence%20under%20a%20type%20constructor/near/129839226):
<p>(Your example doesn't show too much of this since it is nonrecursive, but recursive definitions use a completely different meta implementation in <code>#eval</code>)</p>


{% endraw %}
