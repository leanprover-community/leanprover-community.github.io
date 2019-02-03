---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56940piinstancewoes.html
---

## Stream: [general](index.html)
### Topic: [pi_instance woes](56940piinstancewoes.html)

---


{% raw %}
#### [ Kevin Buzzard (Jun 14 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076746):
<p>A product of topological groups is a topological group.</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076751):
<p>That doesn't sound too hard!</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076814):
<p>Attempt 1:</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076840):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span> <span class="bp">...</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076846):
<p>unknown identifier: topological_group!</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076852):
<p>We have topological monoids, topological rings...</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076856):
<p>but no topological groups :-)</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076863):
<p>After some digging, I find that we have <code>topological_add_group</code></p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076866):
<p>and given that we also have the insane convention that addition isn't commutative</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076869):
<p>this will do</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076883):
<p>Attempt 2:</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076925):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span> <span class="bp">...</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076937):
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
γ : Type,
F : γ → Type,
i : γ
⊢ add_group (F i)
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076940):
<p>(and topological_space too)</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076941):
<p><em>sigh</em></p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076965):
<p>Attempt 3:</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076968):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
<span class="n">topological_add_group</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076979):
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
γ : Type,
F : γ → Type,
_inst_1 : Π (i : γ), topological_space (F i),
_inst_2 : Π (i : γ), add_group (F i),
_inst_3 : ∀ (i : γ), topological_add_group (F i)
⊢ add_group (Π (i : γ), F i)
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076981):
<p>gaargh</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076994):
<p>Oh but this is done in pi_instances, right?</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128076996):
<p>Attempt 4</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077047):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">pi_instances</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
<span class="n">topological_add_group</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{}</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077058):
<div class="codehilite"><pre><span></span>maximum class-instance resolution depth has been reached (the limit can be increased by setting option &#39;class.instance_max_depth&#39;) (the class-instance resolution trace can be visualized by setting option &#39;trace.class_instances&#39;)
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077062):
<p><em>bangs head on table</em></p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077199):
<p>Here's how far I have got:</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077205):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_structures</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">pi_instances</span>

<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">class_instances</span> <span class="n">true</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
<span class="n">topological_add_group</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
<span class="n">continuous_neg</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077213):
<p>and the trace looks like this:</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128077316):
<p><a href="https://gist.github.com/kbuzzard/762adae68d4cbe240f4098968b14fe2e" target="_blank" title="https://gist.github.com/kbuzzard/762adae68d4cbe240f4098968b14fe2e">https://gist.github.com/kbuzzard/762adae68d4cbe240f4098968b14fe2e</a></p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078022):
<p>Oh!</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078031):
<p>That trace is just tracing along not looking like anything too serious is happening in terms of loops</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078038):
<p>and then right at the end it randomly explodes</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078061):
<div class="codehilite"><pre><span></span>[class_instances] (4) ?x_28 : ring ?x_27 := @pi.ring ?x_30 ?x_31 ?x_32
[class_instances] (5) ?x_32 i : ring (?x_31 i) := @pi.ring (?x_33 i) (?x_34 i) (?x_35 i)
[class_instances] (6) ?x_35 i i_1 : ring (?x_34 i i_1) := @pi.ring (?x_36 i i_1) (?x_37 i i_1) (?x_38 i i_1)
[class_instances] (7) ?x_38 i i_1 i_2 : ring (?x_37 i i_1 i_2) := @pi.ring (?x_39 i i_1 i_2) (?x_40 i i_1 i_2) (?x_41 i i_1 i_2)
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078080):
<p>and it just keeps getting bigger and bigger</p>

#### [ Simon Hudon (Jun 14 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078153):
<p>What instance are you expecting will resolve this?</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078207):
<p>you are that instance</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078218):
<p>my question certainly seems to have nothing to do with rings</p>

#### [ Simon Hudon (Jun 14 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078250):
<p><code>apply_instance</code> doesn't have my phone number ;-)</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078253):
<p>I want to prove that the product of top groups is a top group</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078256):
<p>The instance isn't there yet</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078261):
<p>but I haven't even got to defining the instance</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078303):
<p>because of some random type class explosion</p>

#### [ Simon Hudon (Jun 14 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078305):
<p>You can try <code>by pi_instance</code></p>

#### [ Simon Hudon (Jun 14 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078339):
<p>You will need more arguments, we'll see what errors we get</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078402):
<p>I'm on it</p>

#### [ Simon Hudon (Jun 14 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078425):
<p>If you use my <code>refine_struct</code> branch, that should be all you need.</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078439):
<p>ooh</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078442):
<p>so you mean don't use algebra.pi_instances?</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078486):
<p>Apparently I should prove pi.topological_add_monoid first</p>

#### [ Simon Hudon (Jun 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078495):
<p>No I mean you write <code>by pi_instance</code> and it figures it all out on its own without you having to give more information</p>

#### [ Simon Hudon (Jun 14 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078506):
<p>(if you use <code>refine_struct</code>)</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078695):
<p>so can you give me more clues about exactly what to type, so I can "use <code>refine_struct</code>"?</p>

#### [ Simon Hudon (Jun 14 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078748):
<p>certainly</p>

#### [ Simon Hudon (Jun 14 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078852):
<p>1. delete your <code>_target</code> directory<br>
2. go in your <code>leanpkg.toml</code> file<br>
3. replace the <code>mathlib</code> entry with<br>
<code>mathlib = {git = "https://github.com/cipher1024/mathlib", rev = "e1c15f02a62a0343e5497ae380355e966be9b3e4"}</code><br>
4. in a terminal, call <code>leanpkg build</code> on your project</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078880):
<p>You know what</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078881):
<p>I think the problem might be</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078883):
<p>that pi_instances doesn't do any topology</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078887):
<p>and I rather think that putting a topological space structure on a product of types</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078926):
<p>is actually something which requires an idea</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078933):
<p>at least if you want to put the correct top space structure on it</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078941):
<p>Aah sorry</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078950):
<p>By "don't use algebra.pi_instances"</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078959):
<p>I mean "don't use official mathlib's algebra.pi_instances"?</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078966):
<p>OK I will switch.</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128078972):
<p>It will be interesting to see what happens!</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079136):
<p>building</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079149):
<p>But I don't think your pi_instances tactic is going to put a topological space structure on a product of topological spaces</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079154):
<p>This isn't formal, like a ring structure on a product of rings</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079165):
<p>I think this needs to be written by hand.</p>

#### [ Simon Hudon (Jun 14 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079374):
<p>Yes, that's right. If the instance relies on any kind of insight that is not already present in the more basic instance, my tactic won't do.</p>

#### [ Simon Hudon (Jun 14 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128079509):
<p><code>refine_struct</code> might still be helpful, especially if many of the proofs are of the same shape</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080056):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">topological_space</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">topological_space</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">topological_space</span><span class="bp">.</span><span class="n">generate_from</span> <span class="o">{</span> <span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">u</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">set</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">),</span>
<span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="o">{</span><span class="n">i</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">|</span> <span class="n">u</span> <span class="n">i</span> <span class="bp">≠</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span><span class="o">}</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">g</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">,</span> <span class="n">U</span> <span class="n">g</span> <span class="bp">=</span> <span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">g</span> <span class="n">i</span> <span class="err">∈</span> <span class="n">u</span> <span class="n">i</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080077):
<p>But now I have this -- assuming I got it right (and I am not entirely sure that introducing both U and u was necessary) -- I wonder if I can persuade pi_instances to go further.</p>

#### [ Simon Hudon (Jun 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080143):
<p>Now I think there's a chance</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080147):
<p>Actually this might just be hard. Now I can prove that a product of topological groups is a topological space and a group</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080150):
<p>but a topological group is more than this</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080163):
<p>you want the group structure maps like product and inverse to be continuous</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080174):
<p>and these might be lemmas rather than stuff which is formally true</p>

#### [ Reid Barton (Jun 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080184):
<p>That Pi type topological space instance is already in <code>topological_space.lean</code> isn't it?</p>

#### [ Reid Barton (Jun 14 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080241):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="k">Pi</span><span class="bp">.</span><span class="n">topological_space</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">t₂</span> <span class="o">:</span> <span class="bp">Π</span><span class="n">a</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">β</span> <span class="n">a</span><span class="o">)]</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="bp">Π</span><span class="n">a</span><span class="o">,</span> <span class="n">β</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="err">⨆</span><span class="n">a</span><span class="o">,</span> <span class="n">induced</span> <span class="o">(</span><span class="bp">λ</span><span class="n">f</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">t₂</span> <span class="n">a</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080249):
<p>Oh did I miss it?</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080258):
<p>Oh it's not in pi_instances!</p>

#### [ Reid Barton (Jun 14 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080261):
<p>But it's in the same module that defines <code>topological_space</code></p>

#### [ Reid Barton (Jun 14 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080275):
<p>Oh okay, it looks like Lean never actually claimed it was missing?</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080318):
<p>No it just gave me terrifying errors</p>

#### [ Kevin Buzzard (Jun 14 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080358):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi_topological_monoid</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">add_monoid</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_monoid</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
<span class="n">topological_add_monoid</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080370):
<p>I get these <code>maximum class-instance resolution depth has been reached </code> errors</p>

#### [ Reid Barton (Jun 14 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080442):
<p>I see</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080848):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi_topological_add_monoid</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">add_monoid</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_monoid</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
<span class="n">topological_add_monoid</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">pi_instance</span> <span class="o">[</span><span class="n">pi</span><span class="bp">.</span><span class="n">add_monoid</span><span class="o">,</span><span class="k">Pi</span><span class="bp">.</span><span class="n">topological_space</span><span class="o">]</span>
</pre></div>

#### [ Reid Barton (Jun 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080900):
<p>I don't know what is to be done about that instance resolution loop (I'm pretty sure it has been discussed here before), but as a workaround you can specify the instance you want:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi_topological_monoid</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
<span class="bp">@</span><span class="n">topological_add_group</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">_</span> <span class="o">(</span><span class="n">pi</span><span class="bp">.</span><span class="n">add_group</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080902):
<p>my suggestion doesn't work</p>

#### [ Reid Barton (Jun 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080925):
<p><code>pi.add_monoid</code> doesn't actually exist, that's why I switched back to <code>add_group</code></p>

#### [ Reid Barton (Jun 14 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128080931):
<p>Of course, you could probably add it</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081015):
<p>If you replace your sorry with <code>{}</code> do you get the runaway typeclass?</p>

#### [ Reid Barton (Jun 14 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081038):
<p>Yes</p>

#### [ Reid Barton (Jun 14 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081074):
<p>I guess that's because it tried to look up a <code>topological_add_monoid</code> "parent" instance to extend, and then that fell into the same loop</p>

#### [ Reid Barton (Jun 14 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081137):
<p>If I specify both <code>continuous_add</code> and <code>continuous_neg</code> (as <code>sorry</code>) then I don't get a loop.</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081299):
<p>you're right :-)</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081300):
<p>I love living life on the edge</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081302):
<p>one false move</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081303):
<p>runaway typeclass</p>

#### [ Reid Barton (Jun 14 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081317):
<p>actually, that was apparently the original issue, too.</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi_topological_monoid</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
<span class="n">topological_add_group</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">continuous_add</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">continuous_neg</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
<span class="o">}</span>
</pre></div>


<p>also works</p>

#### [ Kenny Lau (Jun 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081464):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous_pi</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">π</span> <span class="n">i</span><span class="o">)]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">Π</span><span class="n">i</span><span class="o">:</span><span class="n">ι</span><span class="o">,</span> <span class="n">π</span> <span class="n">i</span><span class="o">}</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span><span class="n">a</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="n">i</span><span class="o">))</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span> <span class="o">:=</span>
<span class="n">continuous_supr_rng</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">i</span><span class="o">,</span> <span class="n">continuous_induced_rng</span> <span class="err">$</span> <span class="n">h</span> <span class="n">i</span>
</pre></div>

#### [ Kenny Lau (Jun 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081466):
<p>might be useful</p>

#### [ Reid Barton (Jun 14 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081723):
<p>I tried writing the actual instance but the loop came back :(</p>

#### [ Reid Barton (Jun 14 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081810):
<p>It should just be <code>continuous_add := continuous_pi $ λ i, continuous.comp continuous_add' (continuous_apply i)</code></p>

#### [ Reid Barton (Jun 14 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081827):
<p>Er wait, no</p>

#### [ Reid Barton (Jun 14 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128081851):
<p>that's totally wrong</p>

#### [ Reid Barton (Jun 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082090):
<p>OK</p>

#### [ Reid Barton (Jun 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082107):
<p><code>continuous_apply</code> has a totally extraneous argument <code>α</code> which makes it unusable. It should be</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">pi</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">ι</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">π</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="kn">lemma</span> <span class="n">continuous_apply&#39;</span> <span class="o">[</span><span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">π</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">ι</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">continuous</span> <span class="o">(</span><span class="bp">λ</span><span class="n">p</span><span class="o">:</span><span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">π</span> <span class="n">i</span><span class="o">,</span> <span class="n">p</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">continuous_supr_dom</span> <span class="n">continuous_induced_dom</span>
<span class="kn">end</span> <span class="n">pi</span>
</pre></div>

#### [ Reid Barton (Jun 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082114):
<div class="codehilite"><pre><span></span>  <span class="n">continuous_add</span> <span class="o">:=</span> <span class="n">continuous_pi</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">continuous_add</span>
      <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span> <span class="n">continuous_fst</span> <span class="o">(</span><span class="n">continuous_apply&#39;</span> <span class="n">i</span><span class="o">))</span>
      <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span> <span class="n">continuous_snd</span> <span class="o">(</span><span class="n">continuous_apply&#39;</span> <span class="n">i</span><span class="o">))</span>
</pre></div>

#### [ Reid Barton (Jun 14 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082327):
<p>Alternatively,</p>
<div class="codehilite"><pre><span></span>  <span class="n">continuous_add</span> <span class="o">:=</span> <span class="n">continuous_pi</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span>
      <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">prod_mk</span>
        <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span> <span class="n">continuous_fst</span> <span class="o">(</span><span class="n">continuous_apply&#39;</span> <span class="n">i</span><span class="o">))</span>
        <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span> <span class="n">continuous_snd</span> <span class="o">(</span><span class="n">continuous_apply&#39;</span> <span class="n">i</span><span class="o">)))</span>
      <span class="n">continuous_add&#39;</span>
</pre></div>


<p>shows the formal structure a little better, because <code>continuous_add'</code> is the actual class method <code>topological_add_monoid.continuous_add</code></p>

#### [ Reid Barton (Jun 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082403):
<p><code>continuous.comp</code> reads from left to right. First you build a pair by (first taking the first component, and then the <code>i</code>th component of that; first taking the second component, and then the <code>i</code>th component of that), and then you add them.</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082567):
<p><code>continuous_neg := continuous_pi (λ i, continuous.comp _ (continuous_neg continuous_id)</code></p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082573):
<p>but I need to fill in the <code>_</code></p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082585):
<p><code>continuous (λ (x : Π (i : γ), F i), x i)</code></p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082586):
<p>Projection is continuous</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082588):
<p>is what I need</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082764):
<p>and then we're either done</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082771):
<p>or we have a runaway instance</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128082791):
<p>The topological structure on the product is defined as the coarsest topology which makes all the projection maps continuous</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083035):
<p>aah I see this is exactly this apply'</p>

#### [ Kevin Buzzard (Jun 14 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083037):
<p>what is going on with apply? :-)</p>

#### [ Kevin Buzzard (Jun 14 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083126):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi_topological_group</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">topological_add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
<span class="bp">@</span><span class="n">topological_add_group</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="k">Pi</span><span class="bp">.</span><span class="n">topological_space</span><span class="o">)</span> <span class="o">(</span><span class="n">pi</span><span class="bp">.</span><span class="n">add_group</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
<span class="n">continuous_add</span> <span class="o">:=</span> <span class="n">continuous_pi</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">continuous_add</span>
      <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span> <span class="n">continuous_fst</span> <span class="o">(</span><span class="n">continuous_apply&#39;</span> <span class="n">i</span><span class="o">))</span>
      <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span> <span class="n">continuous_snd</span> <span class="o">(</span><span class="n">continuous_apply&#39;</span> <span class="n">i</span><span class="o">)),</span>
<span class="n">continuous_neg</span> <span class="o">:=</span> <span class="n">continuous_pi</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span> <span class="o">(</span><span class="n">continuous_apply&#39;</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">continuous_neg</span> <span class="n">continuous_id</span><span class="o">)</span>
<span class="o">)</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083155):
<p>rofl</p>

#### [ Kevin Buzzard (Jun 14 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083197):
<div class="codehilite"><pre><span></span>continuous_apply :
  ∀ {α : Type u_1} {ι : Type u_2} {π : ι → Type u_3} [_inst_1 : topological_space α]
  [_inst_2 : Π (i : ι), topological_space (π i)] (i : ι), continuous (λ (p : Π (i : ι), π i), p i)
</pre></div>

#### [ Kevin Buzzard (Jun 14 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083198):
<p>I see what Reid means</p>

#### [ Kevin Buzzard (Jun 14 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128083202):
<p>It's going to be pretty tough inferring what alpha is given that it's never mentioned :-)</p>

#### [ Johan Commelin (Jun 15 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pi_instance%20woes/near/128106193):
<blockquote>
<p>It's going to be pretty tough inferring what alpha is given that it's never mentioned :-)</p>
</blockquote>
<p>I fixed this in my simplicial branch. But it hasn't made it into mathlib yet.</p>


{% endraw %}
