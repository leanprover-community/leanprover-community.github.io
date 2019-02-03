---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55694namespace.html
---

## Stream: [general](index.html)
### Topic: [namespace](55694namespace.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 21 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130048945):
<p>I thought it was about time I read through theorem proving in Lean again, to make sure I understand it 100% now. I don't. </p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">foo</span>

<span class="n">def</span> <span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="mi">5</span>
<span class="n">def</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">7</span>
<span class="n">def</span> <span class="n">fa</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">a</span>
<span class="n">def</span> <span class="n">ffa</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">print</span> <span class="s2">&quot;inside foo&quot;</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">a</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">f</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">fa</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">ffa</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">foo</span><span class="bp">.</span><span class="n">fa</span>

<span class="kn">end</span> <span class="n">foo</span>
</pre></div>

#### [ Kevin Buzzard (Jul 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130048997):
<p>Why does that last <code>#check</code> work? What if there had been a <code>foo.foo.fa</code>? Who wins? Can I control who wins?</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130048998):
<p>you have a misplaced <code>#</code></p>

#### [ Kevin Buzzard (Jul 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049000):
<p>I'm on my phone, sorry</p>

#### [ Kenny Lau (Jul 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049002):
<p>I think the definition closest to your "#check" wins</p>

#### [ Kenny Lau (Jul 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049014):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">foo</span>

<span class="n">def</span> <span class="n">fa</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="mi">5</span>
<span class="n">def</span> <span class="n">foo</span><span class="bp">.</span><span class="n">fa</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="mi">5</span>

<span class="bp">#</span><span class="kn">print</span> <span class="s2">&quot;inside foo&quot;</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">fa</span>      <span class="c1">-- fa : ℕ</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">foo</span><span class="bp">.</span><span class="n">fa</span>  <span class="c1">-- foo.fa : ℤ</span>

<span class="kn">end</span> <span class="n">foo</span>
</pre></div>

#### [ Kevin Buzzard (Jul 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049020):
<p>In a nested namespace situation what are the rules?</p>

#### [ Kevin Buzzard (Jul 21 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049065):
<p>And can I bend them with extra annotations? Is this to do with <code>private</code>?</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049068):
<p>Kenny, interchanging the definition order there doesn't change the result</p>

#### [ Kenny Lau (Jul 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049071):
<p>hmm</p>

#### [ Kenny Lau (Jul 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049072):
<p>surely Mario knows why</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049076):
<p>well, it's not to hard to come up with a post hoc rule given this data</p>

#### [ Kevin Buzzard (Jul 21 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049119):
<p>I don't have access to lean right now</p>

#### [ Kevin Buzzard (Jul 21 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049121):
<p>That's why I'm reading TPIL :-)</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049179):
<p>Okay, here's the rule, I think: If you are in <code>namespace foo</code>, ignoring <code>open</code>s, you can refer to things in the root namespace, and in the <code>foo</code> namespace. You can also refer to things in namespaces below that by adding prefixes relative to one of these roots. If there is a conflict, then the stuff in namespace <code>foo</code> wins over the root namespace</p>

#### [ Mario Carneiro (Jul 21 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049230):
<p>So <code>#check foo.fa</code> inside namespace <code>foo</code> refers to <code>foo.fa</code> relative to the root namespace. If there was a <code>foo.foo.fa</code> it would take precedence over this</p>

#### [ Kevin Buzzard (Jul 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049807):
<p>I think I meant <code>protected</code> not <code>private</code></p>

#### [ Kevin Buzzard (Jul 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049808):
<p>Difficult to check right now</p>

#### [ Mario Carneiro (Jul 21 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130049967):
<p>Something with <code>protected</code> marking cannot be referred to without its last namespace. So if <code>A.B.C</code> was declared <code>protected</code> then it could be referred to as <code>A.B.C</code> or <code>B.C</code> but not <code>C</code></p>

#### [ Mario Carneiro (Jul 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130050030):
<p>Something with <code>private</code> marking has a name which is rather obscured, usually something like <code>_private.12345.name</code>. Inside the section/namespace it is declared, you can use <code>name</code> as its short name, but after that it is essentially inaccessible. I don't think it participates in namespacing</p>

#### [ Mario Carneiro (Jul 21 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130050319):
<p>after some testing, it looks like you can't actually type <code>_private.12345.name</code> and refer to the private value since the <code>12345</code> is a numeric name part, which you can't type using the usual lean parser. You can refer to it using tactics though. Here's a silly example:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">quot</span>

<span class="kn">section</span> <span class="n">foo</span>
<span class="kn">private</span> <span class="n">def</span> <span class="n">my_password</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="mi">57</span>

<span class="n">def</span> <span class="n">I_haz_pass</span> <span class="o">:</span> <span class="n">trunc</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">trunc</span><span class="bp">.</span><span class="n">mk</span> <span class="n">my_password</span>
<span class="kn">end</span> <span class="n">foo</span>

<span class="kn">open</span> <span class="n">tactic</span>
<span class="n">def</span> <span class="n">evil</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">do</span>
  <span class="n">env</span> <span class="err">←</span> <span class="n">get_env</span><span class="o">,</span>
  <span class="n">d</span> <span class="err">←</span> <span class="n">env</span><span class="bp">.</span><span class="n">get</span> <span class="bp">``</span><span class="n">I_haz_pass</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">(</span><span class="n">trunc</span><span class="bp">.</span><span class="n">mk</span> <span class="err">%%</span><span class="n">e</span><span class="o">)</span> <span class="err">←</span> <span class="n">return</span> <span class="n">d</span><span class="bp">.</span><span class="n">value</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">e</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="n">evil</span> <span class="c1">-- 57</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">evil</span> <span class="bp">=</span> <span class="mi">57</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Mario Carneiro (Jul 21 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130050377):
<p>the lesson here is that <code>private</code> definitions are not an impermeable abstraction layer, if you want to use them to hide the details of a construction. If consistency depends on this (e.g. Dan Licata's trick) then it's not a good plan</p>

#### [ Kevin Buzzard (Jul 21 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace/near/130052500):
<p>Thanks for the detective work!</p>
<p>I'm 1/3 of the way through my 100% playthrough of TPIL.</p>


{% endraw %}
