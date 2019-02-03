---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12051vectorspaces.html
---

## Stream: [general](index.html)
### Topic: [vector spaces](12051vectorspaces.html)

---


{% raw %}
#### [ Johan Commelin (Sep 14 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133922950):
<p>Before we go on a rampage proving things about vector spaces: there was some suggestion that we should just turn <code>vector_space</code> into notation/abbreviation for <code>module</code>. Maybe now is a good point to decide on this, since Kenny is already PR'ing stuff where he needs new instances of <code>vector_space</code>.</p>

#### [ Mario Carneiro (Sep 14 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133925427):
<p>this is also affected by my upcoming refactoring. Note that <code>semimodule</code> and <code>module</code> are also related in a similar way to <code>module</code> and <code>vector_space</code>, that is, there are no new axioms, just the parameters change.</p>

#### [ Johan Commelin (Sep 14 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133931912):
<p>Ok, so why don't we just call everything a <code>module</code>, and only require the base thingy to be a <code>semiring</code>?</p>

#### [ Mario Carneiro (Sep 14 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133931953):
<p>I'm on board with that if the rest of you are, but mathematicians seem to be picky about names</p>

#### [ Johan Commelin (Sep 14 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133931960):
<p>True, but usually we are ok with generalising a notion.</p>

#### [ Kenny Lau (Sep 14 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933360):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> why are 0 and 1 defined using ulift empty and ulift unit, instead of pempty and punit?</p>

#### [ Kenny Lau (Sep 14 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933361):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">cardinal</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="err">⟦</span><span class="n">ulift</span> <span class="n">empty</span><span class="err">⟧</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">cardinal</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="err">⟦</span><span class="n">ulift</span> <span class="n">unit</span><span class="err">⟧</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Sep 14 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933387):
<p>because they didn't exist at the time</p>

#### [ Kenny Lau (Sep 14 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933403):
<p>should I change it?</p>

#### [ Mario Carneiro (Sep 14 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933412):
<p>if you want</p>

#### [ Kenny Lau (Sep 14 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933417):
<p>it will certainly shorten my proofs:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_empty</span> <span class="o">:</span> <span class="n">mk</span> <span class="n">empty</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">fintype_card</span> <span class="n">empty</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_pempty</span> <span class="o">:</span> <span class="n">mk</span> <span class="n">pempty</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">fintype_card</span> <span class="n">pempty</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_empty&#39;</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">mk</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">empty</span> <span class="n">α</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ulift</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_plift_false</span> <span class="o">:</span> <span class="n">mk</span> <span class="o">(</span><span class="n">plift</span> <span class="n">false</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="n">equiv</span><span class="bp">.</span><span class="n">plift</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">false_equiv_empty</span><span class="bp">.</span><span class="n">trans</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ulift</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_unit</span> <span class="o">:</span> <span class="n">mk</span> <span class="n">unit</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fintype_card</span> <span class="n">unit</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_punit</span> <span class="o">:</span> <span class="n">mk</span> <span class="n">punit</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fintype_card</span> <span class="n">punit</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_singleton</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">mk</span> <span class="o">({</span><span class="n">x</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">singleton</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ulift</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_plift_true</span> <span class="o">:</span> <span class="n">mk</span> <span class="o">(</span><span class="n">plift</span> <span class="n">true</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="n">equiv</span><span class="bp">.</span><span class="n">plift</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">true_equiv_unit</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ulift</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_bool</span> <span class="o">:</span> <span class="n">mk</span> <span class="n">bool</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="n">equiv</span><span class="bp">.</span><span class="n">bool_equiv_unit_sum_unit</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">sum_congr</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ulift</span><span class="bp">.</span><span class="n">symm</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ulift</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_Prop</span> <span class="o">:</span> <span class="n">mk</span> <span class="kt">Prop</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="n">equiv</span><span class="bp">.</span><span class="n">Prop_equiv_bool</span><span class="bp">⟩</span> <span class="o">:</span> <span class="n">mk</span> <span class="kt">Prop</span> <span class="bp">=</span> <span class="n">mk</span> <span class="n">bool</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="n">mk_bool</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_option</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">:</span> <span class="n">mk</span> <span class="o">(</span><span class="n">option</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">mk</span> <span class="n">α</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">option_equiv_sum_unit</span> <span class="n">α</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">sum_congr</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="n">α</span><span class="o">)</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">ulift</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">mk_eq_of_injective</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">mk</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="bp">=</span> <span class="n">mk</span> <span class="n">s</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="n">f</span> <span class="n">s</span> <span class="n">hf</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933547):
<p>I think <code>empty</code> and <code>pempty</code> and <code>false</code> should be all definitionall equal</p>

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933548):
<p>but that's just me</p>

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933549):
<p>the same goes with <code>punit</code> and <code>true</code></p>

#### [ Mario Carneiro (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933551):
<p>I think that <code>punit</code> is defeq to <code>unit</code></p>

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933553):
<p>now I have to prove 6 equiv lemmas about the first one</p>

#### [ Kenny Lau (Sep 14 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933554):
<p>right, but not to <code>true</code></p>

#### [ Mario Carneiro (Sep 14 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933593):
<p>no, they can't be</p>

#### [ Mario Carneiro (Sep 14 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933599):
<p>they are in different universes</p>

#### [ Kenny Lau (Sep 14 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933603):
<p>then punit should be made to sort</p>

#### [ Kenny Lau (Sep 14 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933673):
<p>also, why can't <code>punit.star</code> be <code>()</code>?</p>

#### [ Kenny Lau (Sep 14 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933777):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">def</span> <span class="n">arrow_unit_equiv_unit</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">})</span> <span class="err">≃</span> <span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">w</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span> <span class="n">f</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="k">by</span> <span class="n">funext</span> <span class="n">x</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">f</span> <span class="n">x</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">u</span><span class="bp">;</span> <span class="n">reflexivity</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">def</span> <span class="n">unit_arrow_equiv</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="err">≃</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">u</span><span class="o">,</span> <span class="n">a</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="k">by</span> <span class="n">funext</span> <span class="n">x</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">def</span> <span class="n">empty_arrow_equiv_unit</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">empty</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="err">≃</span> <span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span> <span class="n">e</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">u</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">def</span> <span class="n">pempty_arrow_equiv_unit</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">pempty</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="err">≃</span> <span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span> <span class="n">e</span><span class="o">,</span> <span class="n">e</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">u</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">def</span> <span class="n">false_arrow_equiv_unit</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">false</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="err">≃</span> <span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="o">(</span><span class="n">false</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="err">≃</span> <span class="o">(</span><span class="n">empty</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">arrow_congr</span> <span class="n">false_equiv_empty</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">)</span>
             <span class="bp">...</span> <span class="err">≃</span> <span class="n">punit</span>       <span class="o">:</span> <span class="n">empty_arrow_equiv_unit</span> <span class="bp">_</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933781):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> should I change the name of these to <code>punit</code> etc?</p>

#### [ Mario Carneiro (Sep 14 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933820):
<p>yes, if it says punit it should be called punit</p>

#### [ Kenny Lau (Sep 14 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933831):
<p>the fact that it is tagged with <code>simp</code> makes it hard to trace</p>

#### [ Kenny Lau (Sep 14 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933832):
<p>let's hope for the best</p>

#### [ Kenny Lau (Sep 14 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933879):
<p>wow there's a lot more misnamed theorems</p>

#### [ Kenny Lau (Sep 14 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933891):
<p>also what is wrong with this proof</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">punit_equiv_punit</span> <span class="o">:</span> <span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}</span> <span class="err">≃</span> <span class="n">punit</span><span class="bp">.</span><span class="o">{</span><span class="n">w</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">punit</span><span class="bp">.</span><span class="n">star</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">u</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">u</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">u</span><span class="bp">;</span> <span class="n">reflexivity</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Sep 14 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933992):
<p>nothing</p>

#### [ Mario Carneiro (Sep 14 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133933999):
<p>although there are a lot more theorems where that came from</p>

#### [ Mario Carneiro (Sep 14 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934003):
<p>any universe polymorphic definition is going to have a theorem like that</p>

#### [ Kevin Buzzard (Sep 14 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934055):
<p>It seems weird to have to say that J is a submodule of R instead of an ideal of R.</p>

#### [ Kenny Lau (Sep 14 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934123):
<blockquote>
<p>nothing</p>
</blockquote>
<p>seriously, <code>reflexivity</code>?</p>

#### [ Mario Carneiro (Sep 14 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934419):
<p>the asymmetry is a bit odd</p>

#### [ Johan Commelin (Sep 14 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934731):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think the idea was that <code>ideal</code> could be notation for <code>submodule</code>. That way it is transparent to Lean, but we can still have our beloved terminology. Of course it means that you could start talking about ideals of a module, but you should just avoid that: Lean doesn't care, you will only confuse users.</p>

#### [ Kevin Buzzard (Sep 14 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934800):
<p>Then do we get is_ideal.add or ideal.add etc? And is_submodule.smul is different to is_ideal.smul because it's the ring multiplication in the second case. I found myself having to unfold things explicitly, it was a bit weird</p>

#### [ Kevin Buzzard (Sep 14 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934850):
<p>I was going to wait until all the semimodule stuff died down before making any explicit comments though. I'm using ideals a lot in the Hilbert basis proof course, but I have a lot of other stuff to worry about right now so it's slow progress</p>

#### [ Kevin Buzzard (Sep 14 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934867):
<p>For ideals you don't need to find the instance of module R R (and indeed yesterday I couldn't find it)</p>

#### [ Kevin Buzzard (Sep 14 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133934908):
<p>(but that might be because things are currently in a state of flux)</p>

#### [ Kenny Lau (Sep 14 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937436):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> so at the current moment, how should we know that a field is a vector space over itself?</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937444):
<p>there is an instance for this</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937488):
<p>but if it isn't working you can also introduce it locally</p>

#### [ Kenny Lau (Sep 14 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937518):
<p>oh ok</p>

#### [ Kenny Lau (Sep 14 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133937972):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">module_equiv_lc</span> <span class="o">(</span><span class="n">hs</span> <span class="o">:</span> <span class="n">is_basis</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="err">≃</span> <span class="o">(</span><span class="n">s</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938015):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> should I change this to the idiomatic <code>lc \a s</code>?</p>

#### [ Mario Carneiro (Sep 14 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938027):
<p>that theorem is the centerpiece of my current refactoring, so I recommend you leave it alone until I'm done</p>

#### [ Mario Carneiro (Sep 14 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938036):
<p>anyway <code>lc A s</code> doesn't work because <code>s</code> isn't a module</p>

#### [ Kenny Lau (Sep 14 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938049):
<p>ok...</p>

#### [ Kenny Lau (Sep 14 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938090):
<p>you see</p>

#### [ Kenny Lau (Sep 14 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938095):
<p>this would help my dimension stuff a lot</p>

#### [ Mario Carneiro (Sep 14 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938096):
<p>then wait</p>

#### [ Kenny Lau (Sep 14 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vector%20spaces/near/133938097):
<p>alright</p>


{% endraw %}
