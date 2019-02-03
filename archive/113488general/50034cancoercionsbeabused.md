---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50034cancoercionsbeabused.html
---

## Stream: [general](index.html)
### Topic: [can coercions be abused?](50034cancoercionsbeabused.html)

---


{% raw %}
#### [ Edward Ayers (Sep 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514643):
<p>I've added some questionable coercions to a lean file I am working on:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">le_of_eq</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">eq</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>
</pre></div>


<p>They work great in the file that I am working on because it means I can now do things like</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span><span class="o">:</span><span class="n">c</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span>  <span class="o">:=</span> <span class="n">le_trans</span> <span class="n">p</span> <span class="n">q</span>
</pre></div>


<p>Within a bigger proof and I don't have to use any tactics or faff around making sure equalities match up.<br>
Are there any pitfalls to this approach or is it good practice?</p>

#### [ Kenny Lau (Sep 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514725):
<p>wow</p>

#### [ Edward Ayers (Sep 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514812):
<p>In particular I am worried that stuff like <code>has_coe (a = b) (b = a)</code> will cause a loop of doom in the elaborator.</p>

#### [ Mario Carneiro (Sep 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514910):
<p>it will</p>

#### [ Mario Carneiro (Sep 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514920):
<p>you will probably get a timeout coercing <code>a = b</code> to <code>a = c</code></p>

#### [ Edward Ayers (Sep 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134514993):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">p</span>
</pre></div>


<p>doesn't loop forever with the above coercion. How can I get the bad behaviour?</p>

#### [ Mario Carneiro (Sep 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515063):
<p>hm, not sure in that case. I will downgrade from "bad" to "highly suspicious"</p>

#### [ Edward Ayers (Sep 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515081):
<p>I will leave it in and keep coding and see if it explodes anywhere.</p>

#### [ Mario Carneiro (Sep 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515084):
<p>seems reasonable</p>

#### [ Edward Ayers (Sep 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515127):
<p>It has saved me a lot of typing.</p>

#### [ Mario Carneiro (Sep 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515134):
<p>I can believe it</p>

#### [ Patrick Massot (Sep 24 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515368):
<p>Ed, have you tried Simon's mono tactic, from <a href="https://github.com/leanprover-community/mathlib-nursery/blob/master/src/tactic/monotonicity/interactive.lean" target="_blank" title="https://github.com/leanprover-community/mathlib-nursery/blob/master/src/tactic/monotonicity/interactive.lean">https://github.com/leanprover-community/mathlib-nursery/blob/master/src/tactic/monotonicity/interactive.lean</a> (see also <a href="https://github.com/leanprover-community/mathlib-nursery/blob/master/docs/monotonicity.md" target="_blank" title="https://github.com/leanprover-community/mathlib-nursery/blob/master/docs/monotonicity.md">https://github.com/leanprover-community/mathlib-nursery/blob/master/docs/monotonicity.md</a>)</p>

#### [ Edward Ayers (Sep 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515866):
<p>That's a nice tactic. I am now thinking that it is bad practice to use coercions to do reasoning because your code now depends directly on the minutiae of how the elaborator works, which is somewhat opaque and subject to change. Whereas the tactics have well-defined behaviour and can be tuned.<br>
However it is cool that the elaborator was able deal with my coercion abuse nicely. Are there any docs which specify precisely what the elaborator is doing when it looks for coercions?</p>

#### [ Patrick Massot (Sep 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20coercions%20be%20abused%3F/near/134515882):
<p>source code?</p>


{% endraw %}
