---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36244islinearmap.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [is_linear_map](https://leanprover-community.github.io/archive/116395maths/36244islinearmap.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 22 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148162896):
<p>Is there a reason why <code>is_linear_map</code> does not extend <code>is_add_group_hom</code>?</p>

#### [ Johan Commelin (Nov 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163165):
<p>Here is what I'm trying to do:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group</span>
<span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">namespace</span> <span class="n">finsupp</span>
<span class="n">noncomputable</span> <span class="n">theory</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span>

<span class="n">def</span> <span class="n">linear_extension</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">M</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">M</span> <span class="bp">→</span> <span class="n">Y</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">M</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">M</span><span class="o">)</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">M</span> <span class="o">:=</span>
<span class="n">s</span><span class="bp">.</span><span class="n">sum</span> <span class="err">$</span> <span class="n">f</span>

<span class="kn">namespace</span> <span class="n">linear_extension</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">M</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">M</span> <span class="bp">→</span> <span class="n">Y</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">M</span><span class="o">}</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="n">f</span> <span class="n">x</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">m₁</span> <span class="n">m₂</span> <span class="o">:</span> <span class="n">M</span><span class="o">),</span> <span class="n">f</span> <span class="n">x</span> <span class="o">(</span><span class="n">m₁</span> <span class="bp">+</span> <span class="n">m₂</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="n">m₁</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">x</span> <span class="n">m₂</span><span class="o">)</span> <span class="o">:</span>
<span class="n">is_add_monoid_hom</span> <span class="err">$</span> <span class="n">linear_extension</span> <span class="n">f</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_zero</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">map_add</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s₁</span> <span class="n">s₂</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">sum_add_index</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">M</span> <span class="bp">→</span> <span class="n">Y</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">M</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="n">is_add_group_hom</span> <span class="err">$</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span>
<span class="n">is_add_group_hom</span> <span class="err">$</span> <span class="n">linear_extension</span> <span class="n">f</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="o">(</span><span class="n">linear_extension</span><span class="bp">.</span><span class="n">is_add_monoid_hom</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">zero</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">h</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">add</span><span class="o">))</span><span class="bp">.</span><span class="n">map_add</span> <span class="o">}</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span>
<span class="n">include</span> <span class="n">R</span>

<span class="kn">instance</span> <span class="n">is_linear_map</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">M</span> <span class="bp">→</span> <span class="n">Y</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">M</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="bp">@</span><span class="n">is_linear_map</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">to_module</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="err">$</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">@</span><span class="n">is_linear_map</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">to_module</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">to_module</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="err">$</span> <span class="n">linear_extension</span> <span class="n">f</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="o">(</span><span class="n">linear_extension</span><span class="bp">.</span><span class="n">is_add_group_hom</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">h</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">add</span><span class="bp">⟩</span><span class="o">))</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span> <span class="c1">-- gives stupid error</span>
  <span class="n">smul</span> <span class="o">:=</span> <span class="bp">_</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">linear_extension</span>

<span class="kn">end</span> <span class="n">finsupp</span>
</pre></div>

#### [ Johan Commelin (Nov 22 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163178):
<p>The error is:</p>
<div class="codehilite"><pre><span></span>synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  ⁇
inferred
  to_module Y M
</pre></div>

#### [ Johan Commelin (Nov 22 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163749):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Somehow the <code>@is_linear_map _ _ _ _ _ _ _</code> all over the place give me the feeling that I don't quite understand how to use modules.</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163772):
<p>you shouldn't be using <code>is_linear_map</code> at all</p>

#### [ Johan Commelin (Nov 22 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163907):
<p>So what should I use?</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163914):
<p><code>linear_map</code></p>

#### [ Johan Commelin (Nov 22 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163971):
<p>Ok, is there value in the other two instances? for add monoids/groups?</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163981):
<p>but I understand that the reason you are getting these errors is because <code>finsupp.to_module</code> is not an instance</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148163986):
<p>you should try declaring it locally</p>

#### [ Johan Commelin (Nov 22 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164159):
<p>Ok, that helps.</p>

#### [ Johan Commelin (Nov 22 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164169):
<p>But I would like to use <code>linear_extension</code> in a context with and without modules.</p>

#### [ Johan Commelin (Nov 22 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164172):
<p>Am I trying to be  too flexible?</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164328):
<p>no that's fine, you should just declare a wrapper for <code>linear_extension</code> making it into a linear map</p>

#### [ Johan Commelin (Nov 22 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164410):
<p>But that is already there, right. You made <code>is_linear_map.mk'</code>. Or do you mean something else?</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164519):
<p>I mean <code>linear_extension : linear_map A B</code></p>

#### [ Johan Commelin (Nov 22 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164724):
<p>But then it is no longer a function that can be a group hom if I'm not working with modules...</p>

#### [ Mario Carneiro (Nov 22 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148164936):
<p>you have another function for that; the function parts will be equal (even defeq)</p>

#### [ Johan Commelin (Nov 22 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148166197):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Ok, I finally completed the proof. So what is your suggestion? I should have two different names? One for the unbundled, and one for the bundled linear map? Are there naming conventions for this?</p>

#### [ Kenny Lau (Nov 22 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148182128):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> add <code>l</code> (that's a small <code>L</code>) in front of the name for the bundled version</p>

#### [ Kenny Lau (Nov 22 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_linear_map/near/148182132):
<p>so e.g. the map is <code>mul</code> and the linear_map is <code>lmul</code></p>


{% endraw %}
