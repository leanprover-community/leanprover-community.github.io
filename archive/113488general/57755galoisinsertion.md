---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57755galoisinsertion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [galois insertion](https://leanprover-community.github.io/archive/113488general/57755galoisinsertion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 25 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575752):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">archimedean</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">floor_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">galois_insertion</span> <span class="o">(</span><span class="n">ceil</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="n">coe</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">choice</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="bp">_</span><span class="o">,</span> <span class="err">⌈</span><span class="n">x</span><span class="err">⌉</span><span class="o">,</span>
  <span class="n">gc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">n</span><span class="o">,</span> <span class="n">ceil_le</span><span class="o">,</span>
  <span class="n">le_l_u</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">le_of_eq</span> <span class="o">(</span><span class="n">ceil_coe</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
  <span class="n">choice_eq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Sep 25 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575753):
<p>let's come up with more examples</p>

#### [ Mario Carneiro (Sep 25 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575821):
<p>nice observation. Of course <code>floor</code> is also in an adjoint pair, this time on the right side</p>

#### [ Mario Carneiro (Sep 25 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575944):
<p>also natural number subtraction is best understood in terms of the galois connection it forms with addition</p>

#### [ Mario Carneiro (Sep 25 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134575949):
<p>same with natural/integer division</p>

#### [ Kenny Lau (Sep 25 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134576084):
<blockquote>
<p>also natural number subtraction is best understood in terms of the galois connection it forms with addition</p>
</blockquote>
<p>previously unsaid sentence in human history <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Simon Hudon (Sep 25 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134576195):
<p>Sorry, I have to contradict you. I wrote those Galois connection and PRed them to the core library while I was interning at Galois. And I thought that was a beautiful coincidence and wouldn't shut up about it :P</p>

#### [ Mario Carneiro (Sep 25 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134576211):
<p>did you make any galois connections while you were there? :)</p>

#### [ Simon Hudon (Sep 25 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134576214):
<p>I certainly did :D</p>

#### [ Kevin Buzzard (Sep 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134578923):
<p>Kenny can you remind me what a Galois connection and Galois insertion is?</p>

#### [ Reid Barton (Sep 25 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134591243):
<p>If it helps, Galois connection ~ adjunction and Galois insertion ~ reflective subcategory, i.e. one of the adjoints is the inclusion of a full subcategory (or possibly coreflective, probably the other one is called a Galois coinsertion)</p>

#### [ Reid Barton (Sep 25 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134591256):
<p>where ~ means "is what you get by specializing to preorders = categories with at most one morphism in each hom set"</p>

#### [ Kevin Buzzard (Sep 25 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134592595):
<p>so a pair of adjoint functors and one is inclusion of a full subcategory. Aren't there lots of examples then? e.g. metric spaces &lt;-&gt; complete metric spaces and lots of other examples of when you drop a property of X and then find some adjoint?</p>

#### [ Reid Barton (Sep 25 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134592862):
<p>Yes except metric spaces don't form a preorder</p>

#### [ Reid Barton (Sep 25 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134592982):
<p>So the flavor of the examples tends to be a bit different, e.g., sub-R-modules inside all subsets or these floor/ceiling examples. But the theorems are largely the same--the left half of the connection preserves sups and so on</p>

#### [ Kevin Buzzard (Sep 25 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134593292):
<p>Aah! At most one morphism between two objects, and a pair of adjoint functors, and inclusion of a full subcategory. That's the question.</p>

#### [ Kenny Lau (Sep 29 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134878359):
<p>Is <code>nat.pred</code> and <code>nat.succ</code> a galois insertion?</p>

#### [ Kenny Lau (Sep 29 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134878360):
<p>I can't seem to prove it</p>

#### [ Kevin Buzzard (Sep 29 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879239):
<p>a&lt;= succ b iff pred a &lt;= b looks true to me</p>

#### [ Kevin Buzzard (Sep 29 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879241):
<p>succ is inclusion of a full subcategory</p>

#### [ Kevin Buzzard (Sep 29 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879290):
<p>succ a &lt;= b iff a &lt;= pred b is false though</p>

#### [ Kevin Buzzard (Sep 29 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879307):
<p>And pred is not an inclusion of a full subcategory</p>

#### [ Kevin Buzzard (Sep 29 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879423):
<p>So it's 50-50 from where I'm sitting as to whether it's an insertion or a coinsertion</p>

#### [ Kevin Buzzard (Sep 29 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879424):
<p>But it's not both</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879960):
<p>I was surprised to find that this wasn't already proven... more accurately there were some silly assumptions</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/galois%20insertion/near/134879976):
<p><code>a - b &lt;= c &lt;-&gt; a &lt;= b + c</code> is the galois connection, which is an insertion since <code>(a + b) - b = a</code>. Take <code>b = 1</code> and you have succ/pred</p>


{% endraw %}
