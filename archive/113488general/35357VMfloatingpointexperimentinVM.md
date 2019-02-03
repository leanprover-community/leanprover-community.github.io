---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35357VMfloatingpointexperimentinVM.html
---

## Stream: [general](index.html)
### Topic: [VM floating point experiment in VM](35357VMfloatingpointexperimentinVM.html)

---


{% raw %}
#### [ Edward Ayers (Dec 07 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151113509):
<p>Hi all, as an experiment I made some changes to the Lean VM sourcecode so that it can do basic floating point arithmetic in the VM. It was just an experiment so I do not have the intention of working on it for PR. Overall I found working with the C++ codebase easy to figure out so I would like to thank the Lean team for that.</p>
<p><a href="https://github.com/EdAyers/lean/commit/f839ef617d896d216abe4712abc7caf9d031d3a3" target="_blank" title="https://github.com/EdAyers/lean/commit/f839ef617d896d216abe4712abc7caf9d031d3a3">https://github.com/EdAyers/lean/commit/f839ef617d896d216abe4712abc7caf9d031d3a3</a></p>
<p>The idea is that one would eventually write a Lean file that follows IEEE floating points specification, then prove stuff about <code>float</code>s (not from scratch. Use John Harrison's work or eg: <a href="https://www.isa-afp.org/entries/IEEE_Floating_Point.html" target="_blank" title="https://www.isa-afp.org/entries/IEEE_Floating_Point.html">https://www.isa-afp.org/entries/IEEE_Floating_Point.html</a>) , but also these floats are backed by the VM. I guess that the Lean team already have something like this in mind, since it has clear analogies to the other proof -&gt; VM entities in Lean, perhaps for Lean 4? I know how horrific the IEEE spec for floating points is so I completely acknowledge that it a hard problem to have verified floats in Lean.</p>
<p>I would really appreciate any feedback on whether I am using the Lean C++ correctly: in particular:</p>
<ul>
<li><code>meta instance : has_add float := ⟨add⟩</code> doesn't work because it says that it "failed to generate bytecode for 'has_add' code generation failed, VM does not have code for 'native.float.add'". This seems to happen because the "does it have a VM builtin?" check only happens if the declaration is a definition rather than a constant. What is the workaround for this? One possibility is to make it a <code>definition</code> and include a bogus definition. But that seems really dirty.</li>
<li>I'm just stuffing the bits of the float into <code>mk_vm_simple</code> which I don't claim to understand. This also seems dirty but it worked. Is there a canonical way of doing this?</li>
</ul>

#### [ Edward Ayers (Dec 07 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151113652):
<p>Example usage (I got this to work on my machine, no guarantees of reproducibility):</p>
<div class="codehilite"><pre><span></span>    <span class="kn">open</span> <span class="n">native</span>
    <span class="n">meta</span> <span class="n">def</span> <span class="n">x</span> <span class="o">:</span> <span class="n">float</span> <span class="o">:=</span> <span class="n">native</span><span class="bp">.</span><span class="n">float</span><span class="bp">.</span><span class="n">of_nat</span> <span class="mi">199</span>
    <span class="bp">#</span><span class="kn">eval</span> <span class="n">x</span> <span class="c1">-- outputs 199</span>
    <span class="n">meta</span> <span class="n">def</span> <span class="n">y</span> <span class="o">:</span> <span class="n">float</span> <span class="o">:=</span> <span class="n">native</span><span class="bp">.</span><span class="n">float</span><span class="bp">.</span><span class="n">of_nat</span> <span class="mi">400</span>
    <span class="n">meta</span> <span class="n">def</span> <span class="n">z</span> <span class="o">:</span> <span class="n">float</span> <span class="o">:=</span> <span class="n">native</span><span class="bp">.</span><span class="n">float</span><span class="bp">.</span><span class="n">div</span> <span class="n">x</span> <span class="n">y</span>
    <span class="bp">#</span><span class="kn">eval</span> <span class="n">z</span> <span class="c1">-- outputs 0.4975</span>
</pre></div>

#### [ Rob Lewis (Dec 07 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151114638):
<p>I actually did exactly this for some experiments, ages ago. It was just some hacking, no guarantees that any of it is correct or safe. But I didn't have a problem instantiating <code>has_add</code>. You can try to find the difference if you want: <a href="https://github.com/robertylewis/lean/tree/floats" target="_blank" title="https://github.com/robertylewis/lean/tree/floats">https://github.com/robertylewis/lean/tree/floats</a> <a href="https://github.com/robertylewis/relevance_filter/blob/master/float.lean" target="_blank" title="https://github.com/robertylewis/relevance_filter/blob/master/float.lean">https://github.com/robertylewis/relevance_filter/blob/master/float.lean</a></p>

#### [ Edward Ayers (Dec 07 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151116036):
<p>Fabulous!<br>
It looks like we did basically the same things. You used <code>vm_external</code> as a new struct which is much better than how I did it.<br>
I can't figure out why you can implement <code>has_add</code> but mine fails. Maybe because I tried to put <code>float.lean</code> in the core library?</p>

#### [ Rob Lewis (Dec 07 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151116412):
<p>Afraid I have no clue, and no time right now to switch Lean versions to check. I don't see why putting it in core would make a difference. Mine is also based on 3.3, but again, I don't remember any relevant changes.</p>

#### [ Edward Ayers (Dec 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151117360):
<p>np thanks for the help!</p>

#### [ Edward Ayers (Dec 07 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151117588):
<p>Bytecode error has gone away now mysteriously. I now suspect it's because my editor was looking at the wrong build of lean.</p>

#### [ Edward Ayers (Dec 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151119436):
<p>Mind blown: <code> #eval (23.45 : float)</code> works! How can decimals work out of the box!?!</p>

#### [ Sebastian Ullrich (Dec 07 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151119723):
<p><a href="https://github.com/leanprover/lean/blob/1229f9b2d7f0a1eff10bb33f1cab220f4f6f06ab/src/frontends/lean/parser.cpp#L2133" target="_blank" title="https://github.com/leanprover/lean/blob/1229f9b2d7f0a1eff10bb33f1cab220f4f6f06ab/src/frontends/lean/parser.cpp#L2133">https://github.com/leanprover/lean/blob/1229f9b2d7f0a1eff10bb33f1cab220f4f6f06ab/src/frontends/lean/parser.cpp#L2133</a></p>

#### [ Mario Carneiro (Dec 07 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151119966):
<p>See <code>data.fp.basic</code> for some initial steps in verified floats in lean</p>

#### [ Mario Carneiro (Dec 07 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151120085):
<p>The hard part is supporting nondeterminism, since different architectures do different things with NaN payload bits and stuff</p>

#### [ Edward Ayers (Dec 07 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151121199):
<p>Are there any design notes on how Lean does memory management, thread management?</p>

#### [ Joe Hendrix (Dec 08 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151155621):
<p>How deep are your floating point needs?  I am working with a couple others at Galois on x86_64 semantics, and it would be nice to have support for floating point.  The question in my mind is how flexible to be though, e.g. how significant are the mantissa bits in a nan (do we just care about signaling bit), do we care about rounding mode, denormal support, exception masks, etc.</p>

#### [ Johan Commelin (Dec 08 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151166110):
<p>Are there also people at Galois working on Galois theory? <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span> <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>

#### [ Kevin Buzzard (Dec 08 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151167993):
<blockquote>
<p>Are there also people at Galois working on Galois theory? <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span> <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>
</blockquote>
<p>Joe it's nice to see you back! There will be people at Imperial working on Galois theory soon Johan.</p>

#### [ Edward Ayers (Dec 08 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/151183404):
<p>I personally want floats merely for tactic writing and perhaps one day being able to write UI in Lean. So I'm not overly worried if it doesn't do the right/consistent thing if I multiply some weird corner cases together. <br>
It would be a huge triumph for Lean to formalise floating point though. Who doesn't want to write numerical analysis programs where you have a guarantee that your output float value is within epsilon of the true value all within the same programming language?</p>

#### [ Keeley Hoek (Dec 21 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VM%20floating%20point%20experiment%20in%20VM/near/152323115):
<p>Yeah, it'd be super great if a there was a (meta?) float which was a C float</p>


{% endraw %}
