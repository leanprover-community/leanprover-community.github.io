---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34376hascoetofunquestions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [has_coe_to_fun questions](https://leanprover-community.github.io/archive/113488general/34376hascoetofunquestions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Oct 31 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136859792):
<p>1) What's going on here?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">definition</span> <span class="n">ABC</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">theorem</span> <span class="n">CBA</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="kn">definition</span> <span class="n">XYZ</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">has_coe_to_fun</span> <span class="o">(</span><span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="c1">-- theorem ZYX (α β : Type) : has_coe_to_fun (α ≃ β) := by apply_instance -- fails??</span>
</pre></div>


<p>2) Does <code>has_coe_to_fun</code> work by magic? I hadn't really appreciated this before. I understand how vanilla type class inference works, i.e. how <code>has_add.add x y</code> uses unification to figure out the type of x and y and then uses type class inference to figure out what addition I meant, but the reason this works is that the definition of <code>has_add.add</code> has some <code>[]</code> brackets in. I realise now that in this code</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">H</span>
</pre></div>


<p>nothing I wrote contains a <code>[]</code>. So some extra magic is happening. Is this something to do with some C++ type unification algorithm going "oh-oh, <code>H</code> doesn't have the right type, but the user is looking for a function, why don't I see if <code>has_coe_to_fun</code> can help?" Or is there some more  down-to-earth explanation which I've missed?</p>

#### [ Johannes Hölzl (Oct 31 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860331):
<p>For 1) you see the difference when you activate <code>set_option pp.all true</code> in the <code>definition</code> case, the inferred function is into an type universe which is still a meta variable (which is important as it will be fixed to 1). In the <code>theorem</code> case it is fixed to a universe variable, and hence fails</p>

#### [ Johannes Hölzl (Oct 31 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860427):
<p><code>definition</code> does not require that the type is fully elaborated, quiet the opposite, that's why one can write a definition without a result type. The result type is inferred from the right-hand side.</p>

#### [ Johannes Hölzl (Oct 31 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860469):
<p><code>theorem</code> works different, it fully elaborates the statement, and any universe hole is filled in with a fresh variable.</p>

#### [ Floris van Doorn (Oct 31 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860492):
<p>2) Yes, there is some extra magic happening. If Lean knows that the type of some term <code>t</code> is <code>T</code>, and knows that the expected type is a function type, then it will automatically fire type-class inference to find an instance of <code>has_coe_to_fun T</code>.</p>

#### [ Johannes Hölzl (Oct 31 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860704):
<p>One might wonder why the universe parameters are not filled in by stating <code>has_coe_to_fun (α ≃ β)</code> for <code>α</code> and <code>β</code> in <code>Type 0</code> (which is the case in the examples):<br>
<code>has_coe_to_fun</code> actually allows to map to a different type universe!</p>

#### [ Kevin Buzzard (Oct 31 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860778):
<p>Thanks to both of you. I remember it taking me a very long time to understand type class inference, and I had always assumed I understood it until I started thinking about it more carefully just the other day. For (1) I remember running into these subtleties with the difference between <code>definition</code> and <code>theorem</code> before, but maybe I have just never fully understood them. Usually they only show up (for me) when I foolishly use the wrong one :-) I think we should have a little VS Code paperclip that pops up saying "I see you're writing a theorem. Do you want some help with that, specifically because you seem to be constructing a term whose type is not a proposition?".</p>


{% endraw %}
