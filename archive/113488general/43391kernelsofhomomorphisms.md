---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43391kernelsofhomomorphisms.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [kernels of homomorphisms](https://leanprover-community.github.io/archive/113488general/43391kernelsofhomomorphisms.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Apr 23 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125580755):
<p>Ok, I'm making my feet wet with a first attempt at formalising something. I want to say write down the assumption im(f) = ker(g), where f and g are group homomorphisms. I guess im(f) will be something like <code>f ' A.univ</code>. I tried to find kernels in <code>algebra.group</code> but did not find anything. Are kernels somewhere else?</p>

#### [ Andrew Ashworth (Apr 23 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582195):
<p><a href="https://github.com/leanprover/mathlib/search?utf8=✓&amp;q=ker&amp;type=" target="_blank" title="https://github.com/leanprover/mathlib/search?utf8=✓&amp;q=ker&amp;type=">https://github.com/leanprover/mathlib/search?utf8=✓&amp;q=ker&amp;type=</a></p>

#### [ Andrew Ashworth (Apr 23 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582201):
<p>it's a little sparse</p>

#### [ Johan Commelin (Apr 23 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582221):
<p>Aah, ok. So I should use the github search for this. Thanks</p>

#### [ Johan Commelin (Apr 23 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582732):
<p>What am I doing wrong here?</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>
<span class="kn">variables</span>
<span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">A</span><span class="o">]</span>
<span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">B</span><span class="o">]</span>
<span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">}</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span>

<span class="kn">definition</span> <span class="n">ker</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">f</span>
<span class="kn">definition</span> <span class="n">im</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">univ</span> <span class="n">A</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Apr 23 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582735):
<p>Lean does not like my definition of <code>ker</code> and<code>im</code></p>

#### [ Johan Commelin (Apr 23 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582746):
<p>I get squiggles under the <code>f</code></p>

#### [ Johan Commelin (Apr 23 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125582759):
<p><code>invalid binder declaration, delimiter/bracket expected (i.e., '(', '{', '[', '{{')</code></p>

#### [ Reid Barton (Apr 23 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125584258):
<p>You can write</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">f</span><span class="o">)</span>
<span class="kn">definition</span> <span class="n">ker</span> <span class="o">:=</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">f</span>
<span class="kn">definition</span> <span class="n">im</span> <span class="o">:=</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">univ</span> <span class="n">A</span><span class="o">)</span>
</pre></div>


<p>though I'm not sure whether it is very good style</p>

#### [ Patrick Massot (Apr 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125586882):
<p>Could use <code>def im := set.range f</code></p>

#### [ Kevin Buzzard (Apr 23 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589015):
<p><code>definition ker f := ...</code> is no good because everything to the left of the <code>:=</code> has to either be a variable and skipped completely, or a term together with its type. Just <code>f</code> by itself doesn't work.</p>

#### [ Kevin Buzzard (Apr 23 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589020):
<p>As Reid Barton says, you can skip the <code>f</code> completely</p>

#### [ Kevin Buzzard (Apr 23 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589029):
<p>but you might want to write</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">subgroup</span>
<span class="n">universes</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">A</span><span class="o">]</span> <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">B</span><span class="o">]</span>

<span class="kn">definition</span> <span class="n">ker</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span><span class="o">)</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">:=</span> <span class="n">is_group_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="n">f</span>
</pre></div>

#### [ Patrick Massot (Apr 23 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589134):
<p>Why do you want to enforce the same universe?</p>

#### [ Kevin Buzzard (Apr 23 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589905):
<p>Patrick, although your comment is of course sensible, and probably Johan should write <code>universes u v</code> and then <code>{B : Type v}</code>, in ZFC we only have universe and it never bothered us before :-)</p>

#### [ Patrick Massot (Apr 23 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125589922):
<p>If you don't care (like I don't care) then use <code>Type*</code> until it bites you</p>

#### [ Mario Carneiro (Apr 24 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125592932):
<p>The lean syntax requires parentheses around arguments left of <code>:=</code>, so <code>def ker (f) := ...</code> would work. But it would be a different <code>f</code> than the one in the variable statement, so its type could be different (it will be inferred) and in particular it will not be assumed to be a group_hom</p>

#### [ Mario Carneiro (Apr 24 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/kernels%20of%20homomorphisms/near/125593086):
<p>By the way, the parentheses used to be optional, until we discovered that it enables the following evil example:</p>
<div class="codehilite"><pre><span></span>example inconsistent : false := trivial
</pre></div>


<p>(hint: it's not proving false)</p>


{% endraw %}
