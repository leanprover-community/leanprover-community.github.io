---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56418Tactichelp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Tactic help](https://leanprover-community.github.io/archive/113488general/56418Tactichelp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Koundinya Vajjha (Jan 02 2019 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20help/near/154186308):
<p>Hi, in order to get familiar with writing tactics, I am trying to write a simple tactic to count the number of occurrences of <code>∅</code> in a goal. Here is what I have so far:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">is_empty&#39;</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">has_emptyc</span><span class="bp">.</span><span class="n">emptyc</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">ff</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">list_emptys&#39;</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">expr</span> <span class="o">:=</span>
<span class="n">e</span><span class="bp">.</span><span class="n">fold</span> <span class="o">[]</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">e&#39;</span> <span class="bp">_</span> <span class="n">es</span><span class="o">,</span> <span class="k">if</span> <span class="o">(</span><span class="n">is_empty&#39;</span> <span class="n">e&#39;</span><span class="o">)</span> <span class="k">then</span> <span class="n">insert</span> <span class="n">e&#39;</span> <span class="n">es</span> <span class="k">else</span> <span class="n">es</span><span class="o">)</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">find_empty</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">e</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">target</span><span class="o">,</span>
<span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span> <span class="err">$</span> <span class="o">(</span><span class="n">list_emptys&#39;</span> <span class="n">e</span><span class="o">)</span>
</pre></div>


<p>But if I run this tactic</p>
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">set</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span> <span class="err">∅</span> <span class="err">∩</span> <span class="err">∅</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">find_empty</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>I only get <code>[∅]</code>. Can someone help me figure out what I am doing wrong? I'm guessing it's me not understanding how <code>fold</code> works for <code>expr</code>...</p>

#### [ Mario Carneiro (Jan 02 2019 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20help/near/154187855):
<p>you used <code>insert</code> to accumulate the list, this removes duplicates</p>

#### [ Mario Carneiro (Jan 02 2019 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20help/near/154187873):
<p>and the only thing you ever put in the list is <code>∅</code> (twice)</p>

#### [ Mario Carneiro (Jan 02 2019 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20help/near/154187929):
<p>use <code>::</code> instead</p>

#### [ Koundinya Vajjha (Jan 02 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20help/near/154187975):
<p>Aha! that worked. Thanks <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Jan 02 2019 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20help/near/154188502):
<p>anticlimax...</p>

#### [ Johan Commelin (Jan 02 2019 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20help/near/154191437):
<p><span class="user-mention" data-user-id="116448">@Koundinya Vajjha</span> Have you seen <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/tactic_writing.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/tactic_writing.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/tactic_writing.md</a>? I have no idea about your level of experience with Lean or other programming languages. But for mathematicians who have never written anything in a functional programming language before, I think this is a very good introduction.</p>


{% endraw %}
