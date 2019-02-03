---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71476structureturnedintoclass.html
---

## Stream: [general](index.html)
### Topic: [structure turned into class](71476structureturnedintoclass.html)

---


{% raw %}
#### [ Patrick Massot (Apr 08 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809321):
<p>In <code>topological_space.lean</code>, I see:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">is_open</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="o">(</span><span class="n">is_open_univ</span> <span class="o">:</span> <span class="n">is_open</span> <span class="n">univ</span><span class="o">)</span>
<span class="o">(</span><span class="n">is_open_inter</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">s</span> <span class="n">t</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">s</span> <span class="err">∩</span> <span class="n">t</span><span class="o">))</span>
<span class="o">(</span><span class="n">is_open_sUnion</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">s</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span><span class="n">t</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">t</span><span class="o">)</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="o">(</span><span class="err">⋃₀</span> <span class="n">s</span><span class="o">))</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">class</span><span class="o">]</span> <span class="n">topological_space</span>
</pre></div>

#### [ Patrick Massot (Apr 08 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809361):
<p>Why not directly replacing <code>structure</code> with <code>class</code>?</p>

#### [ Patrick Massot (Apr 08 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809362):
<p>What would be the difference?</p>

#### [ Johannes Hölzl (Apr 08 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809726):
<p>Currently the operations <code>topological_space.is_open</code> has an <strong>explicit</strong> <code>topological_space</code> argument, when using <code>class</code> this would be a <strong>instance</strong> argument. So when working with multiple topologies on the same type the current way is a little bit simpler as one can just write <code>t.is_open s</code>, instead of <code>@is_open _ t s</code>.</p>

#### [ Patrick Massot (Apr 08 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809769):
<p>Thanks. What does this last line do then?</p>

#### [ Johannes Hölzl (Apr 08 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809778):
<p>we still want to use <code>topological_space</code> as a type class, for this we need to add this attribute. Later we add <code>is_open</code> etc as names in the root namespace with the corresponding <strong>instance</strong> arguments.</p>

#### [ Patrick Massot (Apr 08 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809868):
<p>I sort of see. Do you have an example of a lemma involving two topological structures on the same type? I guess in this case you don't use square brackets arguments?</p>

#### [ Johannes Hölzl (Apr 08 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810140):
<p>I should be more precise, it is not about structures on the same type, but a way to refer explicitly to the structure and not be force to only refer to it  over the type. For example see: <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L712" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L712">https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L712</a> and following.</p>

#### [ Patrick Massot (Apr 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810253):
<p>You mean the same definition with <code>class topological_space</code> would not give you a type <code>topological_space α</code>?</p>

#### [ Patrick Massot (Apr 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810355):
<p>But I can still do</p>

#### [ Patrick Massot (Apr 08 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810395):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">toto</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">}:</span> <span class="n">group</span> <span class="o">(</span><span class="n">toto</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Patrick Massot (Apr 08 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810397):
<p>So I don't understand what you mean</p>

#### [ Patrick Massot (Apr 08 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810407):
<p>In my search for minimal example I noticed a class doesn't need to have any field <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span></p>

#### [ Johannes Hölzl (Apr 08 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124811318):
<p>No, <code>class topological_space</code> is nearly the same as <code>structure topological_space</code>. The main difference is the attribute added to <code>topological_space</code> and the binder information on the generated projections, i.e. that <code>is_open</code> has a explicit argument or that it has a type class instance argument.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124812952):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">class</span><span class="o">]</span> <span class="n">foo</span>

<span class="n">class</span> <span class="n">foo&#39;</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar&#39;</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">foo</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">foo</span><span class="bp">.</span><span class="n">bar</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- this doesn&#39;t work</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">foo&#39;</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">foo&#39;</span><span class="bp">.</span><span class="n">bar&#39;</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- this works</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="n">foo</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">H</span><span class="bp">.</span><span class="n">bar</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- this works</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H&#39;</span> <span class="o">:</span> <span class="n">foo&#39;</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">H&#39;</span><span class="bp">.</span><span class="n">bar&#39;</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- this doesn&#39;t work</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124812957):
<p>Projections work differently.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124812998):
<p>I am not saying I understand why we want topological space to be this way, but I think this is what Johannes is saying.</p>

#### [ Kevin Buzzard (Apr 09 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124813133):
<p>Johannes' link is to a construction partially ordering all topologies on a fixed type, so he likes <code>foo</code> better here because <code>H.bar</code> works nicely if we have <code>H1, H2...</code></p>


{% endraw %}
