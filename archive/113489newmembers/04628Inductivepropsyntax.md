---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/04628Inductivepropsyntax.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Inductive prop syntax](https://leanprover-community.github.io/archive/113489newmembers/04628Inductivepropsyntax.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ cbailey (Aug 29 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20prop%20syntax/near/133006097):
<p>Hi, I was wondering if anyone can explain the inductive prop syntax in Lean a little bit; the definition of less_than_or_equal in basic.lean is written in a way that returns a partially applied function for the base case (|refl: less_than_or_equal a), but it doesn't visibly define behavior for that curried return function that would actually say when the prop is true. I noticed that if I #print less_than_or_equal, it comes back as the more familiar Coq style of |refl: forall (a: nat), less_than_or_equal a a, where you explicitly say this prop is true if the two elements are a and a, and the prop has the signature nat -&gt; nat -&gt; Prop without the named (a: nat) parameter. Does Lean default to using reflexivity as the truth condition for an inductively defined prop's base case, or is there something more important about the partially applied function that I'm missing?<br>
Thanks!</p>

#### [ Kevin Buzzard (Aug 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20prop%20syntax/near/133012820):
<p>These aren't partially applied -- there's a trick. The definition is</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">less_than_or_equal</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">:</span> <span class="n">less_than_or_equal</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">step</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">b</span><span class="o">},</span> <span class="n">less_than_or_equal</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">less_than_or_equal</span> <span class="o">(</span><span class="n">succ</span> <span class="n">b</span><span class="o">)</span>
</pre></div>


<p>but you see the <code>a</code> in the first line is left of the colon, so when you see <code>less_than_or_equal</code> on the second or third line you should read <code>less_than_or_equal a</code>. Now it all makes sense :-)</p>

#### [ cbailey (Aug 30 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20prop%20syntax/near/133062381):
<p>Thank you! That makes sense.</p>


{% endraw %}
