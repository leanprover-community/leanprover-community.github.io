---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54886functorialitytactic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [functoriality tactic](https://leanprover-community.github.io/archive/113488general/54886functorialitytactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Sep 08 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133540754):
<p>I wonder how hard it would be to write a tactic which takes an expression which is supposed to be the object mapping part of a functor, and tries to guess the morphism mapping part.</p>

#### [ Reid Barton (Sep 08 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133540817):
<p>If the language for writing the object mapping part is sufficiently restricted, it should be doable, I think. Concretely I'm thinking of stuff like lambdas and applications of known functors and bifunctors</p>

#### [ Reid Barton (Sep 08 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133540878):
<p>Something like a little type checker for a "directed type theory" language I guess</p>

#### [ Reid Barton (Sep 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133540900):
<p>I'm imagining it would work by induction on the structure of the object-mapping expression.<br>
GHC has a built-in feature which is kind of like this, incidentally (<code>deriving Functor</code>)</p>

#### [ Kevin Buzzard (Sep 08 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133541004):
<p>It's an interesting question, because this tactic must be somehow inbuilt into mathematicians -- for the kinds of categories they talk about (even ones where the objects are filtered vector spaces with a nilpotent endomorphism or whatever) it is often the case that the morphisms in the category are defined when introducing the category but the morphisms are barely ever mentioned when defining functors.</p>

#### [ Reid Barton (Sep 08 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133541093):
<p>And we say things like "the functor <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mo>↦</mo><mrow><mi mathvariant="normal">H</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">m</mi></mrow><mo>(</mo><mi>F</mi><mi>A</mi><mo separator="true">,</mo><mi>Z</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">A \mapsto \mathrm{Hom}(FA, Z)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">A</span><span class="mrel">↦</span><span class="mord"><span class="mord mathrm">H</span><span class="mord mathrm">o</span><span class="mord mathrm">m</span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mord mathit">A</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.07153em;">Z</span><span class="mclose">)</span></span></span></span>" (for some functor F and object Z) without bothering to spell out the action on morphisms all the time</p>

#### [ Reid Barton (Sep 08 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133541110):
<p>So, I'd like to be able to infer the functor-ness of <code>λ A, F A ⟶ Z</code>, for example.</p>

#### [ Reid Barton (Sep 08 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133541177):
<p>Currently I can express it as <code>F.comp (yoneda Z)</code> or something opaque like that</p>

#### [ Reid Barton (Sep 08 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133541292):
<p>I'm pretty sure the way we do this is just type checking except we also have to keep track of whether variables appear in a positive or negative (= covariant or contravariant) position.</p>

#### [ Reid Barton (Sep 08 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133541429):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mrow><mi mathvariant="normal">c</mi><mi mathvariant="normal">o</mi><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>j</mi><mo>∈</mo><mi>J</mi></mrow></msub><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>i</mi><mo>∈</mo><mi>I</mi></mrow></msub><mi>F</mi><mo>(</mo><mi>i</mi><mo separator="true">,</mo><mi>j</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathrm{colim}_{j \in J} \mathrm{lim}_{i \in I} F(i, j)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathrm">c</span><span class="mord mathrm">o</span><span class="mord mathrm">l</span><span class="mord mathrm">i</span><span class="mord mathrm">m</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.328331em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.05724em;">j</span><span class="mrel mtight">∈</span><span class="mord mathit mtight" style="margin-right:0.09618em;">J</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mord"><span class="mord"><span class="mord mathrm">l</span><span class="mord mathrm">i</span><span class="mord mathrm">m</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">∈</span><span class="mord mathit mtight" style="margin-right:0.07847em;">I</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.17737em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit">i</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.05724em;">j</span><span class="mclose">)</span></span></span></span> was a real-world example of this. To even make sense of this we need to know that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mrow><mi mathvariant="normal">l</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">m</mi></mrow><mrow><mi>i</mi><mo>∈</mo><mi>I</mi></mrow></msub><mi>F</mi><mo>(</mo><mi>i</mi><mo separator="true">,</mo><mi>j</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathrm{lim}_{i \in I} F(i, j)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathrm">l</span><span class="mord mathrm">i</span><span class="mord mathrm">m</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">∈</span><span class="mord mathit mtight" style="margin-right:0.07847em;">I</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.17737em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit">i</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.05724em;">j</span><span class="mclose">)</span></span></span></span> is functorial in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>j</mi></mrow><annotation encoding="application/x-tex">j</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.65952em;"></span><span class="strut bottom" style="height:0.85396em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05724em;">j</span></span></span></span>.</p>

#### [ Reid Barton (Sep 08 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133541474):
<p>If you had a binder notation for (co)limits which also could infer the functoriality then you could literally write <code>colim (j : J), lim (i : I), F (i, j)</code></p>

#### [ Mario Carneiro (Sep 08 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542353):
<p>You could do this via a custom pexpr parser</p>

#### [ Reid Barton (Sep 08 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542416):
<p>In <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span> or today?</p>

#### [ Mario Carneiro (Sep 08 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542425):
<p>today, I think</p>

#### [ Mario Carneiro (Sep 08 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542431):
<p>e.g. <code>def my_hom := by ccc \lam x:C, \&lt;x, x\&gt;</code></p>

#### [ Reid Barton (Sep 08 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542437):
<p>Oh, like as an argument to a tactic. Yes</p>

#### [ Mario Carneiro (Sep 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542449):
<p>It has to be valid leanish syntax, but I don't think the names have to resolve or anything, you can just inspect the syntax</p>

#### [ Reid Barton (Sep 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542476):
<p>So to clarify, by "parser" you mean I get an actual already-parsed <code>pexpr</code>, then I do whatever processing I want with it to produce something else</p>

#### [ Reid Barton (Sep 08 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542570):
<p>that is, the tactic will receive <code>expr.lam .....</code></p>

#### [ Reid Barton (Sep 08 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542673):
<p>Can I write notation like <code>notation `fun` e := by ccc e</code>, or is it too late by then?</p>

#### [ Reid Barton (Sep 08 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542734):
<p>Or I guess there are things called macros?</p>

#### [ Reid Barton (Sep 08 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542902):
<p>Another idea is to use an auto param like</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">small_category</span> <span class="n">C</span><span class="o">]</span> <span class="o">[</span><span class="n">small_category</span> <span class="n">D</span><span class="o">]</span>
<span class="n">def</span> <span class="n">mk_fun</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">C</span> <span class="bp">→</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">map</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">C</span><span class="o">),</span> <span class="o">(</span><span class="n">a</span> <span class="err">⟶</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span> <span class="err">⟶</span> <span class="n">f</span> <span class="n">b</span><span class="o">)</span> <span class="bp">.</span> <span class="n">guess_functor</span><span class="o">)</span> <span class="o">:</span> <span class="n">functor</span> <span class="n">C</span> <span class="n">D</span> <span class="o">:=</span>
</pre></div>


<p>and then have the tactic process the goal, but then I guess it can only get an elaborated expr?</p>

#### [ Reid Barton (Sep 08 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133542984):
<p>It would probably be least confusing if the action on objects was exactly the provided expression, anyways.</p>

#### [ Reid Barton (Sep 08 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133543123):
<p><code>ccc</code> is a bit different but also an interesting idea. You could imagine many variants (cartesian categories, monoidal categories, symmetric monoidal categories etc.)</p>

#### [ Reid Barton (Sep 08 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133543323):
<p>Like in a monoidal (only) category you would be allowed to write <code>\lam &lt;&lt;a, b&gt;, c&gt;, &lt;a, &lt;b, c&gt;&gt;</code> but not <code>\lam &lt;a, b&gt;, &lt;b, a&gt;</code>.</p>

#### [ Reid Barton (Sep 08 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133543337):
<p>With a cartesian category you can also duplicate and discard variables.</p>

#### [ Reid Barton (Sep 08 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133544989):
<p>I want to write something like this but it doesn't work. How can I get an <code>expr</code> representing <code>f</code> to pass into <code>go</code>?</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">go</span> <span class="o">:</span> <span class="n">pexpr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">pexpr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">var</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:=</span> <span class="n">return</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">var</span> <span class="mi">0</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">return</span> <span class="n">e</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">guess_functor_core</span> <span class="o">:</span> <span class="n">pexpr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">pexpr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">lam</span> <span class="n">var</span> <span class="bp">_</span> <span class="n">t</span> <span class="n">body</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
    <span class="n">map_body</span> <span class="err">←</span> <span class="n">go</span> <span class="n">body</span><span class="o">,</span>
    <span class="n">return</span> <span class="bp">``</span><span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span><span class="o">,</span> <span class="err">%%</span><span class="n">body</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">:=</span> <span class="n">return</span> <span class="n">e</span>
</pre></div>

#### [ Reid Barton (Sep 08 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133545122):
<p>I guess this was already asked at <a href="#narrow/stream/113488-general/topic/creating.20lambda.20without.20tactic" title="#narrow/stream/113488-general/topic/creating.20lambda.20without.20tactic">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating.20lambda.20without.20tactic</a></p>

#### [ Reid Barton (Sep 08 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133546868):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">myfun</span> <span class="o">:</span> <span class="n">C</span> <span class="err">↝</span> <span class="n">C</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">guess_functor</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">F</span> <span class="o">(</span><span class="n">F</span> <span class="n">x</span><span class="o">))</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">myfun</span>
<span class="err">│</span> <span class="n">def</span> <span class="n">myfun</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">small_category</span> <span class="n">C</span><span class="o">]</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">},</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">C</span> <span class="o">:=</span>
<span class="err">│</span> <span class="bp">λ</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">small_category</span> <span class="n">C</span><span class="o">]</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">C</span> <span class="err">⥤</span> <span class="n">C</span><span class="o">},</span>
<span class="err">│</span>   <span class="o">{</span><span class="n">obj</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">C</span><span class="o">),</span> <span class="err">⇑</span><span class="n">F</span> <span class="o">(</span><span class="err">⇑</span><span class="n">F</span> <span class="n">x</span><span class="o">),</span>
<span class="err">│</span>    <span class="n">map&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">),</span> <span class="n">functor</span><span class="bp">.</span><span class="n">map</span> <span class="n">F</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">map</span> <span class="n">F</span> <span class="n">f</span><span class="o">),</span>
<span class="err">│</span>    <span class="n">map_id&#39;</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
<span class="err">│</span>    <span class="n">map_comp&#39;</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">}</span>
</pre></div>

#### [ Mario Carneiro (Sep 08 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133552385):
<p>that works?</p>

#### [ Mario Carneiro (Sep 08 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133552432):
<p>I was expecting the output to be more like <code>F &gt;&gt; F</code></p>

#### [ Scott Morrison (Sep 08 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133557295):
<p>That's pretty cool! Can we play with it?</p>

#### [ Scott Morrison (Sep 08 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133557301):
<p>Inspired by that, I wrote a pretty dumb <code>fyn</code> (short for "follow your nose") tactic, that tries to build morphisms out of what it has at hand.</p>

#### [ Scott Morrison (Sep 08 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133557342):
<p>It is just <code>solve_by_elim</code> also using:</p>
<div class="codehilite"><pre><span></span>[ `category_theory.category.id,
  `category_theory.functor.map,
  `category_theory.nat_trans.app,
  `category_theory.category.comp ]
</pre></div>

#### [ Scott Morrison (Sep 08 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133557348):
<p>With that I can get the construction of the yoneda functor down to:</p>
<div class="codehilite"><pre><span></span>def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) :=
{ obj := λ X, { obj := λ Y : C, Y ⟶ X } }
</pre></div>

#### [ Scott Morrison (Sep 08 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133557355):
<p>down from</p>
<div class="codehilite"><pre><span></span>def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) :=
{ obj := λ X, { obj := λ Y : C, Y ⟶ X,
                map&#39; := λ Y Y&#39; f g, f ≫ g },
  map&#39; := λ X X&#39; f, { app := λ Y g, g ≫ f } }
</pre></div>

#### [ Scott Morrison (Sep 08 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133557489):
<p>which is itself down from</p>
<div class="codehilite"><pre><span></span>def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) :=
{ obj := λ X, { obj := λ Y : C, Y ⟶ X,
                map&#39; := λ Y Y&#39; f g, f ≫ g,
                map_comp&#39; := begin intros X_1 Y Z f g, ext1, dsimp at *, erw [category.assoc] end,
                map_id&#39; := begin intros X_1, ext1, dsimp at *, erw [category.id_comp] end },
  map&#39; := λ X X&#39; f, { app := λ Y g, g ≫ f,
                      naturality&#39; := begin intros X_1 Y f_1, ext1, dsimp at *, simp at * end },
  map_comp&#39; := begin intros X Y Z f g, ext1, ext1, dsimp at *, simp at * end,
  map_id&#39;   := begin intros X, ext1, ext1, dsimp at *, simp at * end }
</pre></div>


<p>before <code>obviously</code>. :-)</p>

#### [ Johan Commelin (Sep 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133557712):
<p>That's really awesome. I like!</p>

#### [ Reid Barton (Sep 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133560247):
<p>Sure, here it is: <a href="https://gist.github.com/rwbarton/46f3352f7a4b84bd75c7c335efd74bb9" target="_blank" title="https://gist.github.com/rwbarton/46f3352f7a4b84bd75c7c335efd74bb9">https://gist.github.com/rwbarton/46f3352f7a4b84bd75c7c335efd74bb9</a><br>
I'm sure that almost everything about this is wrong, and it fails on almost any more complicated example.<br>
Currently it only supports one outer layer of lambda, so it wouldn't work for <code>yoneda</code> yet. I did add products though which sometimes work.</p>

#### [ Reid Barton (Sep 08 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133560344):
<p>One concern I had with a tactic like this is that because it produces data, not a proof, it's important that the exact form of the output be predictable. That's why I thought some kind of induction on the expression might be preferable to a tactic which just tries to repeatedly apply things. It's possible you could get the same predictability from the latter approach too, though.</p>

#### [ Reid Barton (Sep 08 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133561161):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span>, then also consider</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="bp">`</span><span class="err">ƛ</span><span class="bp">`</span> <span class="n">binders</span> <span class="bp">`</span><span class="o">,</span> <span class="bp">`</span> <span class="n">r</span><span class="o">:(</span><span class="n">scoped</span> <span class="n">f</span><span class="o">,</span> <span class="o">{</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">functor</span> <span class="bp">.</span> <span class="n">obj</span> <span class="o">:=</span> <span class="n">f</span> <span class="o">})</span> <span class="o">:=</span> <span class="n">r</span>
</pre></div>

#### [ Scott Morrison (Sep 08 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562061):
<p><code>def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) := ƛ X, ƛ Y : C, Y ⟶ X</code></p>

#### [ Scott Morrison (Sep 08 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562063):
<p>This is getting a little silly. :-)</p>

#### [ Reid Barton (Sep 08 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562079):
<p>is that <code>: C</code> needed because the variable comes from <code>Cᵒᵖ</code>?</p>

#### [ Scott Morrison (Sep 08 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562081):
<p>I can't omit the <code>: C</code> after the <code>Y</code>, or my <code>construct_morphism</code> gets confuseds.</p>

#### [ Reid Barton (Sep 08 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562084):
<p>how about <code>ƛ X, ƛ Y, (X, Y)</code>?</p>

#### [ Scott Morrison (Sep 08 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562086):
<p>What do you mean?</p>

#### [ Reid Barton (Sep 08 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562141):
<p>I mean it's a functor C -&gt; D -&gt; C x D, can your tactic support it? If so is the type annotation on Y required?</p>

#### [ Reid Barton (Sep 08 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562190):
<p>Also, I'm curious what happens if you try <code>ƛ x, x ⟶ x</code></p>

#### [ Reid Barton (Sep 08 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133562248):
<p>Slightly less silly notation idea is <code>\lam'</code></p>

#### [ Scott Morrison (Sep 08 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133563447):
<p><code>def foo : C ⥤ (D ⥤ (C × D)) := ƛ X, ƛ Y, (X, Y)</code></p>

#### [ Kevin Buzzard (Sep 08 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality%20tactic/near/133565802):
<p>The fact that the Yoneda definition now looks like that is in some sense indicative of how little content is involved in any of the checks -- the content is in the idea that the functor exists rather than the verification that it does. I don't think it's silly at all really, I think that in some sense all that is left in the code is the idea, and a machine is doing the rest -- which is what machines are supposed to do. There are plenty of "follow your nose" definitions and theorems in mathematics. I started noticing this when I introduced the following technique into my teaching: I would state a theorem (e.g. "if a_n tends to a and b_n tends to b then (a_n + b_n) tends to a+b") and during the proof I would highlight the <em>idea</em> in the proof, which in this case is "epsilon / 2 not epsilon". I would encourage students not to learn the proof but to learn the idea, and to let the rest of the proof flow naturally. That's what's happening here -- it turns out that there are no ideas in the checks, the idea is the map on objects, and that is now all that's left.</p>


{% endraw %}
