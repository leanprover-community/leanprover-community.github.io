---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36129Sumsoverfinsets.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Sums over finsets](https://leanprover-community.github.io/archive/116395maths/36129Sumsoverfinsets.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 22 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126924811):
<p>I'm stuck on the following triviality</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sums</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">m</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="o">:</span> <span class="n">sum</span> <span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">sum</span> <span class="o">(</span><span class="n">univ</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">j</span><span class="o">))</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">univ</span> <span class="n">x</span>
<span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>It looks like I might want to use <code>finset.sum_sigma</code> but I don't see how to get all the sigma's in place. And the unification magic doesn't do the job either.</p>

#### [ Johan Commelin (May 22 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126924898):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="110044">@Chris Hughes</span>  I remember that you were also working on these kind of sum-rewritings about 2 months ago. Is this similar to what you did?</p>

#### [ Johannes Hölzl (May 22 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126925378):
<p>you can use <code>finset.sum_bind</code> to combine both sum to a single one and then use extensionality that the combination of the index sets on the right is <code>univ</code>. Or use <code>finset.sum_subset</code>  which also uses some sort of extensionality.</p>

#### [ Johan Commelin (May 22 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126925926):
<p>Ok, thanks!</p>

#### [ Johan Commelin (May 22 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126933905):
<p>Ok, I proved the lemma using <code>bind</code> and <code>ext.2</code>. Thanks a lot!</p>


{% endraw %}
