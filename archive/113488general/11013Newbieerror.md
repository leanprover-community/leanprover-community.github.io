---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11013Newbieerror.html
---

## Stream: [general](index.html)
### Topic: [Newbie error](11013Newbieerror.html)

---


{% raw %}
#### [ Johan Commelin (May 08 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254021):
<p>I've got the following code</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ring</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>

<span class="kn">section</span> <span class="n">free_module</span>
<span class="kn">definition</span> <span class="n">free_module</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finsupp</span> <span class="n">S</span> <span class="n">R</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="o">(</span><span class="n">free_module</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">free_module</span>
</pre></div>

#### [ Johan Commelin (May 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254025):
<p>And this is the error</p>
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
R : Type u_1,
_inst_1 : ring R,
S : Type u_2
⊢ Type ?
</pre></div>

#### [ Johan Commelin (May 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254034):
<p>Aah, I should point out that the red squiggles are under <code>free_module</code> in the line with <code>sorry</code></p>

#### [ Mario Carneiro (May 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254076):
<p>Shouldn't <code>R</code> be explicit in <code>free_module</code>? It is not inferrable</p>

#### [ Johan Commelin (May 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254077):
<p>I think the error means that it can't figure out in which universe <code>free_module S</code> lives</p>

#### [ Johan Commelin (May 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254085):
<p>Aah, Ok, is that the problem. I thought it was automatically included, since I declared it a variable</p>

#### [ Johan Commelin (May 08 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254090):
<p>Or should I then use <code>()</code> instead of <code>{}</code></p>

#### [ Kenny Lau (May 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254096):
<p>it isn't a parameter</p>

#### [ Mario Carneiro (May 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254097):
<p>it is included, but the later use might refer to a different <code>R</code></p>

#### [ Johan Commelin (May 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254154):
<p>Ok... well, that fixed my problem. Thanks a lot!</p>

#### [ Kenny Lau (May 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254155):
<p>no, don't use parameter</p>

#### [ Kenny Lau (May 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254158):
<p>you won't be able to use it once you leave the section</p>

#### [ Johan Commelin (May 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254203):
<p>Hmm, what do you mean?</p>

#### [ Johan Commelin (May 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254205):
<p>I now have</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ring</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>

<span class="kn">section</span> <span class="n">free_module</span>
<span class="kn">definition</span> <span class="n">free_module</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finsupp</span> <span class="n">S</span> <span class="n">R</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="o">(</span><span class="n">free_module</span> <span class="n">R</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">split</span><span class="o">,</span> <span class="c1">-- tactic fails</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">free_module</span>
</pre></div>

#### [ Johan Commelin (May 08 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254209):
<p>Is that wrong?</p>

#### [ Kenny Lau (May 08 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254214):
<p>never mind</p>

#### [ Kenny Lau (May 08 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254216):
<p>that isn't wrong</p>

#### [ Johan Commelin (May 08 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254219):
<p>Ok, I don't mind learning a better way (-;</p>

#### [ Johan Commelin (May 08 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254265):
<p>So, why is <code>split</code> failing? I expected to get 4 goals, according to the 4 axioms of a module</p>

#### [ Kenny Lau (May 08 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254270):
<p>constructor</p>

#### [ Kenny Lau (May 08 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254273):
<p>but you don't want to use it since it <code>extends</code> something</p>

#### [ Kenny Lau (May 08 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254279):
<p>maybe if you really want to stay in tactic mode, do <code>refine {..}</code></p>

#### [ Johan Commelin (May 08 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254482):
<p>Well, I don't <em>want</em> to stay in tactic mode. It is just that I have no clue how to do things in term mode. And tactic mode helps me a bit (-;</p>

#### [ Johan Commelin (May 08 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254761):
<p>So what would be the proper way to prove this <code>instance</code>?</p>

#### [ Kenny Lau (May 08 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254774):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="o">(</span><span class="n">free_module</span> <span class="n">R</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">smul</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">smul_add</span> <span class="o">:=</span> <span class="bp">_</span> <span class="o">}</span>
</pre></div>


<p>etc</p>

#### [ Johan Commelin (May 08 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126254830):
<p>Ok, thanks! I'll try to do that.</p>

#### [ Johan Commelin (May 08 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126255445):
<p>Lol, this is already in <code>finsupp</code>: <code>to_module</code></p>

#### [ Kenny Lau (May 08 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126255448):
<p>lol</p>

#### [ Johan Commelin (May 08 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126256750):
<p>The errors continue:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ring</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>

<span class="kn">section</span> <span class="n">free_module</span>
<span class="kn">definition</span> <span class="n">free_module</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finsupp</span> <span class="n">S</span> <span class="n">R</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">S</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">add_comm_monoid</span> <span class="o">(</span><span class="n">free_module</span> <span class="n">R</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">add_comm_monoid</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="o">(</span><span class="n">free_module</span> <span class="n">R</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">to_module</span>
<span class="kn">end</span> <span class="n">free_module</span>

<span class="kn">section</span> <span class="n">generators</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span>

<span class="kn">definition</span> <span class="n">natural_map</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">M</span><span class="o">)</span> <span class="o">:</span> <span class="n">free_module</span> <span class="n">R</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">M</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">s</span> <span class="n">r</span><span class="o">,</span> <span class="n">r</span> <span class="err">•</span> <span class="n">s</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">generated_submodule</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">M</span><span class="o">)</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">natural_map</span> <span class="n">S</span><span class="o">)</span> <span class="c1">-- fails</span>

<span class="kn">definition</span> <span class="n">is_finitely_generated</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∃</span> <span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">M</span><span class="o">,</span> <span class="n">generated_submodule</span> <span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span><span class="o">}</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="n">M</span> <span class="c1">-- fails</span>

<span class="kn">end</span> <span class="n">generators</span>
</pre></div>

#### [ Johan Commelin (May 08 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126256792):
<p>Errors:</p>
<div class="codehilite"><pre><span></span>generators.lean:19:57: error

failed to synthesize type class instance for
M : Type u_2,
S : set M
⊢ module ?m_1 M
generators.lean:19:57: error

don&#39;t know how to synthesize placeholder
context:
M : Type u_2,
S : set M
⊢ Type ?
</pre></div>

#### [ Johan Commelin (May 08 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126256799):
<p>But I am telling it that M is a module over R, so why can't it unify <code>?m_1</code> with <code>R</code>?</p>

#### [ Kevin Buzzard (May 08 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258817):
<p>You started a new section so Lean has forgotten about the variable R</p>

#### [ Kevin Buzzard (May 08 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258821):
<p>wait</p>

#### [ Kevin Buzzard (May 08 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258825):
<p>that doesn't seem to be true</p>

#### [ Kevin Buzzard (May 08 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258898):
<p>It seems to be because you don't ever mention R so the type class inference doesn't kick in</p>

#### [ Kevin Buzzard (May 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258966):
<p><code>definition generated_submodule (S : set M) [module R M] := set.range (natural_map S) -- works</code></p>

#### [ Kevin Buzzard (May 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258971):
<p>Type class inference is a strange thing</p>

#### [ Kenny Lau (May 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258973):
<p>include R</p>

#### [ Kevin Buzzard (May 08 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258974):
<p>I would still not say I had completely got the hang of it</p>

#### [ Kevin Buzzard (May 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126258979):
<div class="codehilite"><pre><span></span><span class="n">include</span> <span class="n">R</span>
<span class="kn">definition</span> <span class="n">generated_submodule</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">M</span><span class="o">)</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">natural_map</span> <span class="n">S</span><span class="o">)</span> <span class="c1">-- works</span>
</pre></div>

#### [ Kevin Buzzard (May 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259016):
<p>Kenny's fix</p>

#### [ Kevin Buzzard (May 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259021):
<p>What does <code>include</code> do?</p>

#### [ Kevin Buzzard (May 08 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259026):
<p>I thought this was for including variable names in tactic proofs</p>

#### [ Kevin Buzzard (May 08 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259037):
<p>As for the equality failing</p>

#### [ Kevin Buzzard (May 08 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259038):
<p><code>set.univ : Π {α : Type u}, set α</code></p>

#### [ Kevin Buzzard (May 08 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259041):
<p><code>set.univ</code> doesn't take <code>M</code>, it guesses it.</p>

#### [ Kevin Buzzard (May 08 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259081):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">is_finitely_generated</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∃</span> <span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">M</span><span class="o">,</span> <span class="n">generated_submodule</span> <span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span><span class="o">}</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="c1">-- works</span>
</pre></div>

#### [ Kevin Buzzard (May 08 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259083):
<p>Recently I realised that I pretty fully understood most Lean errors</p>

#### [ Kevin Buzzard (May 08 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259086):
<p>i.e. I can look at the error and actually figure out what is wrong with my code, in many cases</p>

#### [ Kevin Buzzard (May 08 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259096):
<div class="codehilite"><pre><span></span>type mismatch at application
  generated_submodule {x : M | x ∈ S} = set.univ M
term
  set.univ M
has type
  Prop : Type
but is expected to have type
  set M : Type ?
</pre></div>

#### [ Kevin Buzzard (May 08 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259103):
<p>says "the right hand side is supposed to have type <code>set M</code> but it has type <code>Prop</code> so you have not written what you meant to write -- it doesn't typecheck."</p>

#### [ Kevin Buzzard (May 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259146):
<p>You are attempting to assert that two sets are equal</p>

#### [ Kevin Buzzard (May 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259147):
<p>so the correct type is <code>set M</code></p>

#### [ Kevin Buzzard (May 08 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259149):
<p>so the problem is that <code>set.univ M</code> has type Prop instead of type <code>set M</code></p>

#### [ Kevin Buzzard (May 08 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259156):
<p>and now you look at what <code>set.univ</code> actually does by hovering your mouse over <code>set.univ</code></p>

#### [ Kevin Buzzard (May 08 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259159):
<p>and you see your error</p>

#### [ Kevin Buzzard (May 08 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259207):
<p>I would urge you <span class="user-mention" data-user-id="112680">@Johan Commelin</span> to learn to read errors so you can find out the problem.</p>

#### [ Kevin Buzzard (May 08 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259211):
<p>Sometimes the problem is that type class inference has failed. Type class inference is just something you have to get the hang of and I had to ask and ask here about it -- see my typeclass inference woes thread</p>

#### [ Kevin Buzzard (May 08 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259224):
<p>But for other errors, try and make it so that there is exactly one error (i.e put sorry everywhere else) and then try and read the error.</p>

#### [ Kevin Buzzard (May 08 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259266):
<p>And then hope that you can fix it</p>

#### [ Johan Commelin (May 08 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126259847):
<p>Ok, thanks! I hope to get the hang of it as well...</p>

#### [ Chris Hughes (May 08 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126266575):
<p><code>set.univ : set M</code> should help</p>

#### [ Chris Hughes (May 08 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newbie%20error/near/126266785):
<p>Or perhaps <code>@set.univ M</code></p>


{% endraw %}
