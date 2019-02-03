---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/69812Ismathlibbrokencurrentlyno.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Is mathlib broken currently? (no)](https://leanprover-community.github.io/archive/116395maths/69812Ismathlibbrokencurrentlyno.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 06 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133406331):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">ideals</span>

<span class="n">def</span> <span class="n">is_fg</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_submodule</span> <span class="n">s</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∃</span> <span class="n">t</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">β</span><span class="o">,</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">span</span> <span class="err">↑</span><span class="n">t</span> <span class="bp">=</span> <span class="n">s</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">maximum class-instance resolution depth has been reached</span>
<span class="cm"> (the limit can be increased by setting option &#39;class.instance_max_depth&#39;)</span>
<span class="cm">  (the class-instance resolution trace can be visualized by setting option</span>
<span class="cm">   &#39;trace.class_instances&#39;)</span>
<span class="cm">-/</span>
</pre></div>


<p>I think I'm up to date. This is from the Noetherian branch of community mathlib but it doesn't seem to work with (non-community) mathlib master either.</p>

#### [ Kevin Buzzard (Sep 06 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133406390):
<p>hmm on the other hand I just managed to compile mathlib master so I don't know what's going on.</p>

#### [ Kevin Buzzard (Sep 06 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133406443):
<p>It's the coercion from finset beta to set beta which seems to cause the loop</p>

#### [ Johannes Hölzl (Sep 06 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133408030):
<p><code>(2) ?x_7 : has_coe (finset β) ?x_5 := @quotient_ring.has_coe ?x_9 ?x_10 ?x_11 ?x_12</code><br>
ouch, doesn't seam to be a good coercion rule...</p>

#### [ Johannes Hölzl (Sep 06 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133408329):
<p>not this one but the <code>quotient_module</code> one</p>

#### [ Johannes Hölzl (Sep 06 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133408472):
<p>it should work now</p>

#### [ Mario Carneiro (Sep 06 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133409247):
<p>This is the same kind of problem as in <code>option.has_coe</code>. You can't coerce out of an arbitrary type in <code>has_coe</code>, you have to use <code>has_coe_t</code> directly</p>

#### [ Johannes Hölzl (Sep 06 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133409438):
<p>hm, then it needs to be changed further. I just fixed the implicit instead of instance for the out_param problem.</p>

#### [ Kevin Buzzard (Sep 06 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133425189):
<p>I'm sick of not being able to understand and debug this stuff. What happened in practice is that I wanted to do a bit more work on the noetherian branch yesterday evening but instead spent 30 minutes pulling, rebasing and compiling mathlib because I could see the error and I could not see how to fix it, I could only see how to try and get up to date and hope the error would go away. I would like to learn how to diagnose and fix what just happened and I still find these traces intimidating. Because I don't understand the traces I spent some time looking through recent mathlib commits to try and spot some suspicious looking instances but I couldn't find any. My next step would have been to go through each commit in mathlib, because I know the code worked last week and it didn't work yesterday, to try and find the offending one, but I suspect that neither of you did this.</p>
<p>OK so I still have a borked noetherian branch [because I didn't update yet]. Presumably I start with <code>set_option trace.class_instances true</code>. I now get 100+ lines of output. Here is a random snippet:</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">13</span><span class="o">)</span> <span class="err">?</span><span class="n">x_94</span> <span class="o">:</span> <span class="n">ring</span> <span class="err">?</span><span class="n">x_93</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">ring</span> <span class="err">?</span><span class="n">x_97</span> <span class="err">?</span><span class="n">x_98</span> <span class="err">?</span><span class="n">x_99</span> <span class="err">?</span><span class="n">x_100</span> <span class="err">?</span><span class="n">x_101</span> <span class="err">?</span><span class="n">x_102</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">14</span><span class="o">)</span> <span class="err">?</span><span class="n">x_98</span> <span class="o">:</span> <span class="n">discrete_linear_ordered_field</span> <span class="err">?</span><span class="n">x_97</span> <span class="o">:=</span> <span class="n">rat</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">14</span><span class="o">)</span> <span class="err">?</span><span class="n">x_100</span> <span class="o">:</span> <span class="n">ring</span> <span class="err">?</span><span class="n">x_99</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_1</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">14</span><span class="o">)</span> <span class="err">?</span><span class="n">x_102</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_absolute_value</span> <span class="n">ℚ</span> <span class="n">rat</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="err">?</span><span class="n">x_101</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">abs_is_absolute_value</span> <span class="err">?</span><span class="n">x_103</span> <span class="err">?</span><span class="n">x_104</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">14</span><span class="o">)</span> <span class="err">?</span><span class="n">x_100</span> <span class="o">:</span> <span class="n">ring</span> <span class="err">?</span><span class="n">x_99</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">ring</span> <span class="err">?</span><span class="n">x_103</span> <span class="err">?</span><span class="n">x_104</span> <span class="err">?</span><span class="n">x_105</span> <span class="err">?</span><span class="n">x_106</span> <span class="err">?</span><span class="n">x_107</span> <span class="err">?</span><span class="n">x_108</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">15</span><span class="o">)</span> <span class="err">?</span><span class="n">x_104</span> <span class="o">:</span> <span class="n">discrete_linear_ordered_field</span> <span class="err">?</span><span class="n">x_103</span> <span class="o">:=</span> <span class="n">rat</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">15</span><span class="o">)</span> <span class="err">?</span><span class="n">x_106</span> <span class="o">:</span> <span class="n">ring</span> <span class="err">?</span><span class="n">x_105</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">inst_1</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">15</span><span class="o">)</span> <span class="err">?</span><span class="n">x_108</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_absolute_value</span> <span class="n">ℚ</span> <span class="n">rat</span><span class="bp">.</span><span class="n">discrete_linear_ordered_field</span> <span class="n">α</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="err">?</span><span class="n">x_107</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">abs_is_absolute_value</span> <span class="err">?</span><span class="n">x_109</span> <span class="err">?</span><span class="n">x_110</span>
<span class="n">failed</span> <span class="n">is_def_eq</span>
</pre></div>


<p>That's not the relevant part, because I have no idea how to read this in detail or what the relevant part is. Let me instead say what I see when I look at this output. Firstly the numbers in brackets near the beginning of each line ((13),(14),(15)) are slowly increasing, which probably means there's a loop. Looking more carefully it seems that other than these numbers and the names of metavariables, the output is periodic with period 4, which means there really is a loop. Looking at the output in more detail, I see <code>?x_100 : ring ?x_99</code> and I know from the experience that this is the line which makes Mario say "aah, something is wrong, because that should never happen". I still don't understand why, because I don't understand what the output represents. What does it represent? Lean is trying to prove that something is a ring -- that doesn't sound too bad to me; sometimes it is supposed to do that. So far I have managed to diagnose that something is wrong and I need to ask for help. </p>
<p>The full 200+ line output is here:</p>
<p><a href="https://gist.github.com/kbuzzard/e113b65c54e35bff839fb88365811ef5" target="_blank" title="https://gist.github.com/kbuzzard/e113b65c54e35bff839fb88365811ef5">https://gist.github.com/kbuzzard/e113b65c54e35bff839fb88365811ef5</a></p>
<p>There is now no hurry on this (hopefully) but if at some point someone could explain how to get from it to the diagnosis above (which I must admit I do not fully understand -- but I see the words "it should work now" which I am very grateful for -- thanks Johannes!), I'd be much obliged.</p>

#### [ Kevin Buzzard (Sep 06 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Is%20mathlib%20broken%20currently%3F%20%28no%29/near/133430208):
<p>PS I can confirm that the noetherian branch is now building again (and also that I am unsure whether I should be merging or rebasing when I update mathlib-community from mathlib master and then update the noetherian branch, or indeed whether it even matters).</p>


{% endraw %}
