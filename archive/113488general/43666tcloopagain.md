---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43666tcloopagain.html
---

## Stream: [general](index.html)
### Topic: [tc loop again](43666tcloopagain.html)

---


{% raw %}
#### [ Patrick Massot (May 28 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127213712):
<p>I tried to define norms on indexed product, but it seems I have a type class loop again. It's dinner time here, but if someone wants to have a look at why <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean#L319" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean#L319">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean#L319</a> fails I'd be very grateful</p>

#### [ Nicholas Scheel (May 28 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127213727):
<p>does <code>begin admit end</code> act any differently?</p>

#### [ Patrick Massot (May 28 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127220182):
<p>No. I can replace the infinite loop by weirder error messages using <code>refine</code> but that's all I can get</p>

#### [ Patrick Massot (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127271172):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> could you have a look at this issue if you have some time please? This only other it depends on is Johannes' <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/metric_space_fintype_pi.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/metric_space_fintype_pi.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/metric_space_fintype_pi.lean</a></p>

#### [ Kevin Buzzard (May 30 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277524):
<p>This would be so much easier to do if you could minimise</p>

#### [ Kevin Buzzard (May 30 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277533):
<p>cutting and pasting one file works</p>

#### [ Kevin Buzzard (May 30 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277569):
<p>even cutting and pasting the file you import would be better than this</p>

#### [ Kevin Buzzard (May 30 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277583):
<p>I don't want to dump Johannes' file into the project I have open</p>

#### [ Kevin Buzzard (May 30 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277586):
<p>if I put it in scratch then I don't know how to import it</p>

#### [ Kevin Buzzard (May 30 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127277604):
<p>I mean -- even if it's a huge gist -- for <em>me</em> at least, one file is a whole lot easier than two</p>

#### [ Kevin Buzzard (May 30 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279386):
<p><a href="https://gist.github.com/kbuzzard/e8c1b1ac3d50795b1bdf3094bc823de6" target="_blank" title="https://gist.github.com/kbuzzard/e8c1b1ac3d50795b1bdf3094bc823de6">https://gist.github.com/kbuzzard/e8c1b1ac3d50795b1bdf3094bc823de6</a></p>

#### [ Kevin Buzzard (May 30 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279387):
<p>there's the error</p>

#### [ Kevin Buzzard (May 30 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279694):
<p>so you made all these instances in this file and they are all those terrifying things like normed space to normed group, and then product of normed spaces is a normed space and product of normed groups is a normed group. Are all these safe? Is this unrelated to your problem?</p>

#### [ Kevin Buzzard (May 30 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279851):
<p>Patrick I wrote the error to a file, and then deleted all the lines with failed is_def_eq underneath and now it looks like this:</p>

#### [ Mario Carneiro (May 30 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279854):
<p>The problem is in the very first few lines. </p>
<div class="codehilite"><pre><span></span>[class_instances] (0) ?x_2 : @module ?x_0 (Π (i : ι), E i) ?x_1 := @pi.module ?x_3 ?x_4 ?x_5 ?x_6 ?x_7
[class_instances] (1) ?x_6 : ring ?x_5 := @prod.ring ?x_8 ?x_9 ?x_10 ?x_11
failed is_def_eq
</pre></div>


<p>After matching <code>pi.module</code> for the typeclass, it immediately attempts to resolve <code>?x_6</code>, which is the <code>[ring A]</code> argument</p>

#### [ Kevin Buzzard (May 30 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279863):
<div class="codehilite"><pre><span></span>[class_instances] (8) ?x_70 : @is_absolute_value ℝ real.discrete_linear_ordered_field α
  (@normed_ring.to_ring α (@normed_field.to_normed_ring α _inst_1))
[class_instances] (8) ?x_68 : ring ?x_67 := @cau_seq.ring ?x_74 ?x_75 ?x_76 ?x_77 ?x_78 ?x_79
[class_instances] (9) ?x_75 : discrete_linear_ordered_field ?x_74 := real.discrete_linear_ordered_field
[class_instances] (9) ?x_77 : ring ?x_76 := @normed_ring.to_ring ?x_84 ?x_85
[class_instances] (10) ?x_85 : normed_ring ?x_84 := @normed_field.to_normed_ring ?x_86 ?x_87
[class_instances] (11) ?x_87 : normed_field ?x_86 := _inst_1
[class_instances] (9) ?x_79 : @is_absolute_value ℝ real.discrete_linear_ordered_field α
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279864):
<p>that's the period</p>

#### [ Kevin Buzzard (May 30 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279867):
<p>with the number going up each time</p>

#### [ Mario Carneiro (May 30 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279909):
<p>but since it hasn't figured out <code>?x_5</code> yet, it's on a wild goose chase to come up with a ring, any ring, and it gets caught up in a loop somewhere with some iterating ring construction</p>

#### [ Kevin Buzzard (May 30 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279918):
<p>So the red flag for you is the attempt to prove <code>ring ?x_5</code></p>

#### [ Mario Carneiro (May 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279923):
<p>right</p>

#### [ Mario Carneiro (May 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279936):
<p>you can see that also in the period; the number is the stack depth, so you can see it's recursing each time on a <code>ring ?</code> goal</p>

#### [ Kevin Buzzard (May 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279984):
<div class="codehilite"><pre><span></span>[class_instances] (1) ?x_6 : ring ?x_5 := @prod.ring ?x_8 ?x_9 ?x_10 ?x_11
failed is_def_eq
[class_instances] (1) ?x_6 : ring ?x_5 := @normed_ring.to_ring ?x_12 ?x_13
[class_instances] (2) ?x_13 : normed_ring ?x_12 := @normed_field.to_normed_ring ?x_14 ?x_15
[class_instances] (3) ?x_15 : normed_field ?x_14 := _inst_1
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279988):
<p>It looks like it solves it there</p>

#### [ Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279992):
<p>it can prove it's a ring if it proves it's a normed ring</p>

#### [ Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279993):
<p>or a normed field</p>

#### [ Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279994):
<p>and something was a normed field at the time</p>

#### [ Mario Carneiro (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279996):
<p>it solves a subgoal, but it hasn't solved the main goal</p>

#### [ Kevin Buzzard (May 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127279997):
<p>has it solved ring ?x_5?</p>

#### [ Mario Carneiro (May 30 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280041):
<p>no, the last (1) line is line 27 which is a <code>ring ?x_5</code> goal</p>

#### [ Kevin Buzzard (May 30 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280053):
<p>the line after I quoted</p>

#### [ Kevin Buzzard (May 30 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280104):
<p><code>[class_instances] (1) ?x_6 : ring ?x_5 := @cau_seq.ring ?x_11 ?x_12 ?x_13 ?x_14 ?x_15 ?x_16</code><br>
`</p>

#### [ Mario Carneiro (May 30 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280109):
<p>The role of <code>cau_seq.ring</code> here is that it produces a ring from a ring</p>

#### [ Kevin Buzzard (May 30 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280110):
<p>I thought I'd seen the last of it</p>

#### [ Mario Carneiro (May 30 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280117):
<p>so it's building a ring of the form <code>(cau_seq (cau_seq (cau_seq ? ?) ?) ?)</code></p>

#### [ Mario Carneiro (May 30 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280136):
<p>the fault isn't <code>cau_seq</code> though, that was just the first recursing construction it fell upon</p>

#### [ Kevin Buzzard (May 30 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280137):
<p><code>[class_instances] (9) ?x_77 : ring ?x_76 := @cau_seq.ring ?x_83 ?x_84 ?x_85 ?x_86 ?x_87 ?x_88</code></p>

#### [ Kevin Buzzard (May 30 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280139):
<p>There's the last <code>(9)</code></p>

#### [ Mario Carneiro (May 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280184):
<p>The real problem is that it's solving <code>ring ?</code></p>

#### [ Kevin Buzzard (May 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280192):
<p><code>cau_seq.ring :
  Π {α : Type u_3} [_inst_1 : discrete_linear_ordered_field α] {β : Type u_4} [_inst_2 : ring β] {abv : β → α}
  [_inst_3 : is_absolute_value abv], ring (cau_seq β abv)</code></p>

#### [ Kevin Buzzard (May 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280198):
<p>"you give me a ring, I'll give you another ring"</p>

#### [ Mario Carneiro (May 30 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280268):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Why don't out_params work here? Adding <code>out_param</code> to <code>pi.module</code> does not change the order of inference for the arguments</p>

#### [ Mario Carneiro (May 30 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280339):
<p>maybe it has to do with the fact that the <code>module</code> argument is in a pi?</p>

#### [ Kevin Buzzard (May 30 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280417):
<p>It's funny that <code>instance product_normed_space : normed_space α (E × F) </code> works</p>

#### [ Kevin Buzzard (May 30 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280422):
<p>but then <code>instance fintype.normed_space {ι : Type*} {E : ι → Type*} [fintype ι] [∀i, normed_space α (E i)]</code> gives him trouble</p>

#### [ Mario Carneiro (May 30 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280915):
<p>Here's a minimized version:</p>
<div class="codehilite"><pre><span></span>class ring&#39; (α : Type*).

class module&#39; (α : out_param $ Type*) (β : Type*) [out_param $ ring&#39; α].

class normed_field&#39; (α : Type*) extends ring&#39; α.

class normed_space&#39; (α : out_param $ Type*) (β : Type*) [out_param $ normed_field&#39; α] extends module&#39; α β.

instance pi.module&#39; {I : Type*} {f : I → Type*}
 {α : out_param Type*} [out_param $ ring&#39; α] [∀ i, module&#39; α $ f i] : module&#39; α (Π i : I, f i) :=
sorry

instance loop (α) [ring&#39; α] : ring&#39; (option α) := sorry

set_option trace.class_instances true

instance fintype.normed_space&#39; {α} [normed_field&#39; α]
  {ι : Type*} {E : ι → Type*} [∀i, normed_space&#39; α (E i)] :
  normed_space&#39; α (Πi, E i) :=
⟨_, _⟩
</pre></div>

#### [ Mario Carneiro (May 30 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127280979):
<div class="codehilite"><pre><span></span>[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_2 : @module&#39; ?x_0 (Π (i : ι), E i) ?x_1 := @pi.module&#39; ?x_3 ?x_4 ?x_5 ?x_6 ?x_7
[class_instances] (1) ?x_6 : out_param (ring&#39; ?x_5) := @loop ?x_8 ?x_9
[class_instances] (2) ?x_9 : ring&#39; ?x_8 := @loop ?x_10 ?x_11
[class_instances] (3) ?x_11 : ring&#39; ?x_10 := @loop ?x_12 ?x_13
[class_instances] (4) ?x_13 : ring&#39; ?x_12 := @loop ?x_14 ?x_15
...
</pre></div>

#### [ Mario Carneiro (May 30 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127286141):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I think we should just abandon the <code>out_param</code> in module and live with having to give the type explicitly in scalar multiplication. It's too brittle and there is very little I can do about these issues without modifying lean.</p>

#### [ Patrick Massot (May 30 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293689):
<p>Thank you very much Mario and Kevin. I understood what was happening, the question is how to solve this (and I also wanted to point out to Sebastian that out_param stuff maybe requires more thinking in Lean 4, I don't know).</p>

#### [ Patrick Massot (May 30 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293699):
<p>What confuses me is:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">ι</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">E</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">ι</span><span class="o">]</span> <span class="o">[</span><span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">vector_space</span> <span class="n">α</span> <span class="o">(</span><span class="n">E</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
  <span class="n">vector_space</span> <span class="n">α</span> <span class="o">(</span><span class="bp">Π</span><span class="n">i</span><span class="o">,</span> <span class="n">E</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>


<p>works fine</p>

#### [ Patrick Massot (May 30 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293706):
<p>But the type class mechanism doesn't search for this. Why?</p>

#### [ Patrick Massot (May 30 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293750):
<p>Is there any way I could help the type class search here?</p>

#### [ Patrick Massot (May 30 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293764):
<p><code>vector_space</code> is very closely related to <code>module</code>, the full definition is simply <code>class vector_space (α : out_param $ Type u) (β : Type v) [field α] extends module α β</code></p>

#### [ Patrick Massot (May 30 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293839):
<p>but I would still naively expect the search that is currently failing to start by looking for some <code>vector_space α (Πi, E i)</code> rather than <code>@module ?x_0 (Π (i : ι), E i) ?x_1</code></p>

#### [ Patrick Massot (May 30 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127293945):
<p>Note that the working instance here is <code>pi.vector_space</code> whose definition is literally: <code>instance vector_space (α : Type*) [field α] [∀ i, vector_space α $ f i] : vector_space α (Π i : I, f i) :=
{ ..pi.module }</code></p>

#### [ Sebastian Ullrich (May 30 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127294838):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you want</p>
<div class="codehilite"><pre><span></span>instance pi.module&#39; {I : Type*} {f : I → Type*}
 {α : Type*} {r : ring&#39; α} [∀ i, module&#39; α (f i)] : module&#39; α (Π i : I, f i) :=
</pre></div>


<p>?</p>

#### [ Johannes Hölzl (May 30 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298089):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> this still loops. One problem is that it looks for <code>@module' ?x_0 (Π (i : ι), E i) ?x_1</code> instead of<code>@module' α (Π (i : ι), E i) ?x_1</code> . Then the type class inference loops by making <code>loop</code> steps.</p>

#### [ Sebastian Ullrich (May 30 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298146):
<p>It doesn't loop in Mario's example</p>

#### [ Johannes Hölzl (May 30 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298202):
<p>Ah, sorry, I didn't see that you also changed <code>[ring' α]</code> to <code>{r : ring' α}</code>.</p>

#### [ Sebastian Ullrich (May 30 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298212):
<p>Yes, that's the important part :) . <code>instance</code> doesn't do anything special with <code>out_param</code>.</p>

#### [ Sebastian Ullrich (May 30 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298320):
<p>The intended meaning behind making it implicit is "don't try to infer an instance at this point, we don't even know α yet".</p>

#### [ Johannes Hölzl (May 30 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127298985):
<p>Thanks, this is a good explanation. It doesn't work now, but it seams to be a problem that the pi instance can not be applied.</p>

#### [ Patrick Massot (May 31 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc%20loop%20again/near/127349063):
<p>So, do we have a solution?</p>


{% endraw %}
