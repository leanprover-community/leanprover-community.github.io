---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29056negationofearliercasesofmatch.html
---

## Stream: [general](index.html)
### Topic: [negation of earlier cases of match](29056negationofearliercasesofmatch.html)

---


{% raw %}
#### [ Nima (Apr 24 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618723):
<p>(deleted)</p>

#### [ Nima (Apr 24 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618804):
<p>How should I change the following code, so in the second case I know <code>a</code> is not <code>aa</code>?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">ind</span> <span class="bp">|</span> <span class="n">aa</span> <span class="bp">|</span> <span class="n">bb</span>
<span class="kn">open</span> <span class="n">ind</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">ind</span> <span class="bp">→</span> <span class="n">ind</span> <span class="bp">→</span> <span class="n">ind</span> <span class="bp">→</span> <span class="n">ind</span> <span class="bp">→</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="n">aa</span> <span class="bp">_</span>  <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">a</span>  <span class="n">aa</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="bp">|</span> <span class="bp">_</span>  <span class="bp">_</span>  <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="mi">0</span>
</pre></div>

#### [ Kenny Lau (Apr 24 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618858):
<p>you can change the title next time</p>

#### [ Kenny Lau (Apr 24 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618863):
<p>type <code>bb</code> instead of <code>a</code></p>

#### [ Kenny Lau (Apr 24 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618872):
<p>(it can't know inside a match what conditions are not yet matched)</p>

#### [ Nima (Apr 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618929):
<p>How do I change the title?<br>
what if I have <br>
<code>inductive ind | aa | bb | cc | dd</code></p>

#### [ Kenny Lau (Apr 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618945):
<p>maybe could you give us the whole context? I sense some <a href="https://meta.stackexchange.com/questions/66377/what-is-the-xy-problem" target="_blank" title="https://meta.stackexchange.com/questions/66377/what-is-the-xy-problem">XY problem</a> going on here</p>

#### [ Kenny Lau (Apr 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618947):
<p>sorry</p>

#### [ Johan Commelin (Apr 24 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125618950):
<blockquote>
<p>How do I change the title?</p>
</blockquote>
<p>Just edit the post. There will be a field to edit the title as well.</p>

#### [ Simon Hudon (Apr 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619007):
<blockquote>
<p>what if I have <br>
<code>inductive ind | aa | bb | cc | dd</code></p>
</blockquote>
<p>I think you'd need an <code>if _ then _ else _</code> and a <code>match</code> inside one of the branches</p>

#### [ Kenny Lau (Apr 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619020):
<p>ite is hard to destruct. I don't recommend using it at all unless necessary</p>

#### [ Kenny Lau (Apr 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619022):
<p>I'm sure his situation has other ways out</p>

#### [ Simon Hudon (Apr 24 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619041):
<p>It would help if you derived <code>decidable_eq</code>:</p>
<div class="codehilite"><pre><span></span>@[derive decidable_eq]
inductive ind | aa | bb | cc | dd
</pre></div>

#### [ Simon Hudon (Apr 24 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619119):
<p>Kenny, the alternative would be to match on all branches.</p>

#### [ Kenny Lau (Apr 24 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619180):
<p>one can't be so sure</p>

#### [ Nima (Apr 24 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619276):
<p>So if I have a <strong>sparse</strong> match on many variables, and in each case I want to use the fact that previous cases were not a match, I would be better off with if-then-else. Right?</p>

#### [ Simon Hudon (Apr 24 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619323):
<p>Exactly</p>

#### [ Nima (Apr 24 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/negation%20of%20earlier%20cases%20of%20match/near/125619332):
<p>Thanks</p>


{% endraw %}
