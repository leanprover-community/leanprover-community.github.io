---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02862Proofofargumentdecreasefornumgcd.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Proof of argument decrease for num.gcd](https://leanprover-community.github.io/archive/113488general/02862Proofofargumentdecreasefornumgcd.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Seul Baek (Jun 07 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127717897):
<p>I'm trying to define <code>gcd</code> for <code>num</code>. I've already defined <code>num.mod</code> and proved related lemmas (which you can check at <a href="https://github.com/skbaek/qelim/blob/master/src/common/num.lean" target="_blank" title="https://github.com/skbaek/qelim/blob/master/src/common/num.lean">https://github.com/skbaek/qelim/blob/master/src/common/num.lean</a>), and here's my first attempt using those preliminary definitions :</p>
<div class="codehilite"><pre><span></span>def gcd : num → num → num
| 0       y := y
| (pos x) y :=
  have y % pos x &lt; pos x, from mod_lt _ $ pos_pos _,
  gcd (y % pos x) (pos x)
</pre></div>


<p>I get an error message saying that Lean failed to prove recursive application is decreasing. Apparently Lean is not using the proof of argument decrease provided by <code>have</code>. I'm not sure why this happens, since the definition of <code>nat.gcd</code> is almost identical. Any ideas?</p>

#### [ Gabriel Ebner (Jun 07 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127718228):
<p>The error message shows what you need to prove: in this case, it's <code>num.sizeof (y % pos x) &lt; pos_num.sizeof x + 1</code> (didn't clone the repo).</p>

#### [ Gabriel Ebner (Jun 07 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127718320):
<p>The default termination measure for well-founded recursion in the equation compiler is lexicographic ordering of the <code>sizeof</code> values of the arguments.  You should probably define <code>has_sizeof</code> for <code>num</code> in a sensible way (i.e. the nat value).  Check out <code>#eval sizeof (1000:num)</code></p>

#### [ Gabriel Ebner (Jun 07 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127718425):
<p>Note that <code>#eval sizeof</code> is broken for nested and mutual inductives.  <a href="https://github.com/leanprover/lean/issues/1518" target="_blank" title="https://github.com/leanprover/lean/issues/1518">https://github.com/leanprover/lean/issues/1518</a></p>

#### [ Seul Baek (Jun 07 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127720042):
<p>That worked. Thank you!</p>

#### [ Mario Carneiro (Jun 12 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/127961269):
<p><span class="user-mention" data-user-id="116585">@Seul Baek</span> The latest mathlib update includes <code>div</code> and <code>gcd</code> for <code>num</code> and <code>znum</code>. It is implemented in binary, rather than by repeated subtraction, so it should be exponentially faster than the transcribed <code>nat</code> definition, which is what it looks like you did. I think <code>gcd</code> should have something like <code>O((log n)^2)</code> performance in the kernel now</p>

#### [ Seul Baek (Jun 15 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20of%20argument%20decrease%20for%20num.gcd/near/128092239):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thank you for the notice. This is very good news - I was only thinking about faster subtraction using binary representations.</p>


{% endraw %}
