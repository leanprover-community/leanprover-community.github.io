---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59614VMdoesnothavecodeformultisetstronginductionon.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [VM does not have code for 'multiset.strong_induction_on'](https://leanprover-community.github.io/archive/113488general/59614VMdoesnothavecodeformultisetstronginductionon.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 08 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20does%20not%20have%20code%20for%20%27multiset.strong_induction_on%27/near/129309672):
<p>What's happening here? I'm defining a map from <code>multiset nat</code> to <code>nat</code> :</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">multiset</span><span class="bp">.</span><span class="n">strong_induction_on</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">multiset.strong_induction_on :</span>
<span class="cm">  Π {α : Type u_1} {p : multiset α → Sort u_2} (s : multiset α),</span>
<span class="cm">    (Π (s : multiset α), (Π (t : multiset α), t &lt; s → p t) → p s) → p s</span>
<span class="cm">-/</span>

<span class="kn">definition</span> <span class="n">f</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
  <span class="n">multiset</span><span class="bp">.</span><span class="n">strong_induction_on</span> <span class="n">s</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">s&#39;</span> <span class="n">H</span><span class="o">,</span><span class="mi">0</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">f</span> <span class="o">{</span><span class="mi">1</span><span class="o">,</span><span class="mi">2</span><span class="o">,</span><span class="mi">3</span><span class="o">}</span>
</pre></div>


<p>but the <code>#eval</code> fails with </p>
<div class="codehilite"><pre><span></span>code generation failed, VM does not have code for &#39;multiset.strong_induction_on&#39;
</pre></div>


<p>I must be honest, I don't really know what a virtual machine is. I don't really see an obstruction to evaluating the function, however I can see that there might be issues with dealing with the quotient type. Can't the VM just assume everything is well-defined on equivalence classes and have a punt? Or is the issue elsewhere?</p>

#### [ Andrew Ashworth (Jul 08 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20does%20not%20have%20code%20for%20%27multiset.strong_induction_on%27/near/129309806):
<p>does <code>#reduce</code> produce the same error message?</p>

#### [ Mario Carneiro (Jul 08 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20does%20not%20have%20code%20for%20%27multiset.strong_induction_on%27/near/129309871):
<p><code>multiset.strong_induction_on</code> should not have been marked a <code>lemma</code> instead of a <code>def</code></p>

#### [ Mario Carneiro (Jul 08 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20does%20not%20have%20code%20for%20%27multiset.strong_induction_on%27/near/129309913):
<p>because it produces elements of type <code>p s : Sort*</code></p>

#### [ Kevin Buzzard (Jul 08 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20does%20not%20have%20code%20for%20%27multiset.strong_induction_on%27/near/129309917):
<p>Oh! :-)</p>

#### [ Kevin Buzzard (Jul 08 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20does%20not%20have%20code%20for%20%27multiset.strong_induction_on%27/near/129309929):
<p>I should really add this to my list of "basic checks when something isn't working". I've been caught out in the past myself writing <code>have</code> instead of <code>let</code> and then wondering why something won't unfold.</p>

#### [ Mario Carneiro (Jul 08 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20does%20not%20have%20code%20for%20%27multiset.strong_induction_on%27/near/129310102):
<p>This is a different issue. The VM constructs code for all definitions that are not <code>noncomputable</code>; this is what enables the use of <code>#eval</code> to run functions. But <code>lemma</code> and <code>theorem</code> definitions do not have code generated, which is usually okay since these are usually propositions which do not have any computational content anyway, but it causes problems if data is marked like this</p>

#### [ Mario Carneiro (Jul 08 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20does%20not%20have%20code%20for%20%27multiset.strong_induction_on%27/near/129310119):
<p>This can cause issues even if you don't use <code>#eval</code> at all:</p>
<div class="codehilite"><pre><span></span>lemma A : nat := 42
def B : nat := A
-- failed to generate bytecode for &#39;B&#39;
-- code generation failed, VM does not have code for &#39;A&#39;
</pre></div>


{% endraw %}
