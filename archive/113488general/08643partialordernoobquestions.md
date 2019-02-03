---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08643partialordernoobquestions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [partial order noob questions](https://leanprover-community.github.io/archive/113488general/08643partialordernoobquestions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 04 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302203):
<p>OK so I appear to be engaging with orders for the first time in my Lean career.</p>
<p>1) Is this a good instance?</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">(</span><span class="n">X</span><span class="o">)</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">({</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">})</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>


<p>[I still feel very ill-equipped to answer such questions.]</p>
<p>2) Stupid class noob question: what am I doing wrong here:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">partial_order</span> <span class="o">(</span><span class="n">X</span><span class="o">)</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">({</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">})</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">le_refl</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="c1">-- error</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">invalid field notation, function &#39;partial_order.le_refl&#39;</span>
<span class="cm"> does not have explicit argument with type (partial_order ...)</span>
<span class="cm">-/</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="n">sorry</span>
  <span class="o">}</span>
</pre></div>


<p>This "invalid field notation" stuff is something I see a lot, because I don't understand fields very well (indeed in an earlier post today I managed to fail to even remember the word "field"). How am I supposed to prove <code>le_refl</code> like a boss?</p>
<p>3) Is it called <code>subtype.partial_order</code> or <code>partial_order.subtype</code> or something else? Is it already there?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302294):
<p><code>  le_refl := λ a, le_refl (a : X),</code> works. Why does what I did not work?</p>

#### [ Kenny Lau (Sep 04 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302298):
<p>2) don't use projection (the <code>x.y</code> notation) if <code>x</code> is an instance of a class<br>
3) subrel</p>

#### [ Kenny Lau (Sep 04 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302306):
<p>and in particular 2) don't name instances of classes</p>

#### [ Kenny Lau (Sep 04 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302344):
<p>i.e. <code>[h : partial_order X]</code> is wrong in the first place</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302433):
<p><code>subrel</code> just gives me the relation on the subtype, not that it is also a partial order.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302457):
<p>I wanted to use projection because I wanted to prove <code>le_refl</code> by "use X's le_refl"</p>

#### [ Kenny Lau (Sep 04 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302524):
<p>I don't think it's in mathlib</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302553):
<p>Kenny, I have a partial order structure on <code>submodule R M</code>, the type of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-submodules of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi></mrow><annotation encoding="application/x-tex">M</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span></span></span></span>. I want a partial order structure on the subtype of this consisting of submodules which are contained in a given submodule <code>N</code>. I was going to make this general subtype nonsense above and then use it to get an induced partial order on this subtype, and then prove that this was order isomorphic to <code>submodule R N</code>. Does this sound sensible?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302605):
<p>I'm currently trying to work out a way of doing this which won't make Mario's head hurt when he sees the PR.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302626):
<p>Then I get an order embedding <code>submodule R N -&gt; submodule R M</code> and I can deduce that <code>N</code> is Noetherian from the already-proved theoerem that Noetherian iff &gt; is well-founded.</p>

#### [ Kenny Lau (Sep 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302646):
<p>that sounds very sensible</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302845):
<p>?! <code>#print partial_order</code> gives <code>partial_order.le_antisymm : ∀ {α : Type u} [c : partial_order α] (a b : α), a ≤ b → b ≤ a → a = b</code> with <code>a</code> and <code>b</code> explicit, but hovering over <code>@le_antisymm</code> in the middle of the definition I'm writing gives me <code>le_antisymm : ∀ {α : Type u} [_inst_1 : partial_order α] {a b : α}, a ≤ b → b ≤ a → a = b</code> with <code>a</code> and <code>b</code> implicit. Who am I to believe?</p>

#### [ Kenny Lau (Sep 04 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302925):
<p>both</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302988):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">partial_order</span> <span class="o">(</span><span class="n">X</span><span class="o">)</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">({</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">})</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">le_refl</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">hab</span> <span class="n">hbc</span><span class="o">,</span> <span class="bp">@</span><span class="n">le_trans</span> <span class="n">X</span> <span class="bp">_</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">hab</span> <span class="n">hbc</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">hab</span> <span class="n">hba</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="bp">@</span><span class="n">le_antisymm</span> <span class="n">X</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">hab</span> <span class="n">hba</span>
<span class="o">}</span>
</pre></div>


<p>So I still don't know if this should be an instance. Should I just suck it and see?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133303450):
<p>and the presence of <code>@</code>s makes me feel like I'm missing a trick.</p>

#### [ Kenny Lau (Sep 04 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133303540):
<p>this is my code in the <code>temp</code> file in our stacks project:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">x</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="n">subrel</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">le_refl</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="n">le_trans</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hx</span> <span class="n">hy</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">le_antisymm</span> <span class="n">hx</span> <span class="n">hy</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Sep 04 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133304072):
<p>heh, so I switched to @ because I couldn't get <code>le_antisymm</code> working, and after the switch I still couldn't, and then I realised  <code>subtype.eq</code> was missing, and then I didn't switch back :-)</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133304099):
<p><code>le_refl := λ x, le_refl x</code> I am surprised this works. How does Lean know which <code>le_refl</code> to use?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133331784):
<p>This is kind of annoying. This <code>order_iso</code> stuff just seems to work with not an actual partial order or preorder or anything, but any binary relation at all. So I was expecting to see a lemma saying "if X and Y are equivalent partial orders, i.e. they have the same &lt;=, then they have the same &lt; too", but somehow this isn't covered by what <code>order_iso</code> does, despite its name.</p>


{% endraw %}
