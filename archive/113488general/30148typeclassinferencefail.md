---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30148typeclassinferencefail.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [type class inference fail](https://leanprover-community.github.io/archive/113488general/30148typeclassinferencefail.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jun 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760290):
<div class="codehilite"><pre><span></span><span class="n">don&#39;t</span> <span class="n">know</span> <span class="n">how</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">placeholder</span>
<span class="kn">context</span><span class="o">:</span>
<span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">comm_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="bp">@</span><span class="n">topological_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="bp">_</span><span class="n">inst_2</span> <span class="o">(</span><span class="bp">@</span><span class="n">comm_ring</span><span class="bp">.</span><span class="n">to_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">),</span>
<span class="n">R₀</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_4</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_subring</span> <span class="n">R</span> <span class="o">(</span><span class="bp">@</span><span class="n">comm_ring</span><span class="bp">.</span><span class="n">to_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="n">R₀</span><span class="o">,</span>
<span class="n">I</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">coe_sort</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span> <span class="mi">2</span><span class="o">}</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">set</span><span class="bp">.</span><span class="n">has_coe_to_sort</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">)</span> <span class="n">R₀</span><span class="o">),</span>
<span class="bp">_</span><span class="n">inst_5</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">is_ideal</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">coe_sort</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span> <span class="mi">2</span><span class="o">}</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">set</span><span class="bp">.</span><span class="n">has_coe_to_sort</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span><span class="o">)</span> <span class="n">R₀</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">subtype</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="bp">@</span><span class="n">comm_ring</span><span class="bp">.</span><span class="n">to_ring</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span> <span class="bp">_</span><span class="n">inst_1</span><span class="o">)</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="n">R₀</span> <span class="bp">_</span><span class="n">inst_4</span><span class="o">)</span>
    <span class="n">I</span>
<span class="err">⊢</span> <span class="n">topological_space</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">R</span>
</pre></div>


<p>Why can this even fail?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760358):
<p>Because type class inference is not looking at your context, maybe?</p>

#### [ Johan Commelin (Jun 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760423):
<p>Right... so how is it ever supposed to figure things out if it doesn't look at my context?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760424):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">comm_group</span> <span class="n">G</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">G</span><span class="o">,</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760425):
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
G : Type,
a : comm_group G,
a b : G
⊢ has_mul G
</pre></div>

#### [ Kevin Buzzard (Jun 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760427):
<p>The system doesn't look there</p>

#### [ Johan Commelin (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760433):
<p>Shouldn't it?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760435):
<p>That's not a question I'm qualified to answer</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760437):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_group</span> <span class="n">G</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">G</span><span class="o">,</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760441):
<p>That works</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760445):
<p>the square brackets mean "add me to the type class inference system"</p>

#### [ Johan Commelin (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760488):
<p>This feels extremely counterintuitive to me... after all, we go through pains to make sure there is only one instance of a class... so if there is <em>one</em> instance in my context there won't be any others. (I promise!)</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760489):
<p>However there are commands which explicitly add stuff to the type class inference system</p>

#### [ Sean Leather (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760490):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> What does <code>set_option pp.all true</code> before that tell you?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760491):
<p>Do you know about <code>letI</code>?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760493):
<p>Maybe search for that in the type class inference thread</p>

#### [ Johan Commelin (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760497):
<p>Aha, I don't know about <code>letI</code>.</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760498):
<p>I half-understand it</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760504):
<p>the main gotcha is that this is defined in mathlib</p>

#### [ Johan Commelin (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760505):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> I already have that set to true. You see it in the output.</p>

#### [ Kevin Buzzard (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760506):
<p>so you have to import _some_ mathlib file before it works</p>

#### [ Johan Commelin (Jun 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760507):
<p>Is this one of our mathematical promises playing up again?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760552):
<p>stream:general topic:more+type+class+inference+issues leti</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760631):
<p><a href="#narrow/search/i.20would.20rather.20just.20make.20type.20class.20inference.20work.2E" title="#narrow/search/i.20would.20rather.20just.20make.20type.20class.20inference.20work.2E">https://leanprover.zulipchat.com/#narrow/search/i.20would.20rather.20just.20make.20type.20class.20inference.20work.2E</a></p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760632):
<p>Kenny teaching me about letI in pretty much the same situation</p>

#### [ Johan Commelin (Jun 08 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760634):
<p>Right, so I insert</p>
<div class="codehilite"><pre><span></span><span class="k">by</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">topological_space</span> <span class="n">R</span><span class="bp">;</span> <span class="n">exact</span>
</pre></div>


<p>in the middle of my definition, and it works. Ugly!</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760659):
<p>I totally agree that it is ugly</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760677):
<p>And they have no plans to change it in Lean 4</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760686):
<p>Mario wrote all this letI and exactI and haveI when Leo made some non-trivial changes which broke a lot of stuff</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760688):
<p>For some reason, liberal type class inference was making Lean slow</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760690):
<p>for his application</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760691):
<p>so he made it stricter</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760694):
<p>and then a whole bunch of mathlib broke</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760713):
<p>and if this letI hack hadn't worked</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760737):
<p>then it would not surprise me if mathlib would still be broken</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760751):
<p>On the other hand</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760753):
<p>I'm not sure you can have "mathematician inference"</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760757):
<p>I think we're too clever</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760799):
<p>If you can formalise some nice MWE of something which you feel would be nice if it worked but doesn't work</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760800):
<p>then you could ask Sebastian or Mario why it doesn't work</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760803):
<p>but I fear the answer might be</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760804):
<p>something like "if that worked, then this important file would take 100 years to compile"</p>

#### [ Kevin Buzzard (Jun 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20fail/near/127760811):
<p>But I'm not sure, what happened with the changes to type class inference is beyond my pay grade</p>


{% endraw %}
