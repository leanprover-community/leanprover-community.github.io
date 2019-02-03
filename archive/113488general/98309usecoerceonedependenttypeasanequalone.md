---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98309usecoerceonedependenttypeasanequalone.html
---

## Stream: [general](index.html)
### Topic: [use/coerce one dependent type as an equal one?](98309usecoerceonedependenttypeasanequalone.html)

---


{% raw %}
#### [ Andrew Tindall (Sep 23 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479228):
<p>I am trying to apply a function to a vector, and get the error message </p>
<div class="codehilite"><pre><span></span>type mismatch at application
  f (vector.take j v)
term
  vector.take j v
has type
  vector (S.A) (min j (max j k))
but is expected to have type
  vector (S.A) j
</pre></div>


<p><code>j</code> and <code>k</code> are <code>nat</code>s. I know that <code>j = min j (max j k)</code>, but I don't know how to use that equivalence to coerce <code>v</code> from one type to another. Should I just make a specific instance of <code>has_coe</code> and then use it to cast <code>v</code>?</p>

#### [ Keeley Hoek (Sep 23 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479329):
<p>If it was me I would explicitly turn <code>vector.take j v</code> into something of type <code>vector (S.A) j</code> before applying the coercion</p>

#### [ Reid Barton (Sep 23 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479736):
<p>Isn't <code>j = min j (max j k)</code> always true? Where is <code>vector.take</code> defined?</p>

#### [ Andrew Tindall (Sep 23 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479910):
<p>Yes, it's always true. <code>vector.take</code>is in <code>data.vector</code>.</p>

#### [ Kenny Lau (Sep 23 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479962):
<p>maybe you should change the type of <code>f</code> first</p>

#### [ Reid Barton (Sep 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479968):
<p>Oh, in the core library! Right</p>

#### [ Kenny Lau (Sep 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134479969):
<p>also, MWE</p>

#### [ Reid Barton (Sep 23 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/use/coerce%20one%20dependent%20type%20as%20an%20equal%20one%3F/near/134480135):
<p>If this is in a programming context, I would probably use the <code>convert</code> tactic or some <code>rw</code> and prove <code>j = min j (max j k)</code>.<br>
If this is in a theorem-proving context, where I need to prove some fact about the result of this expression, I would just define my own <code>take'</code> with a more useful type like</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">vec</span><span class="bp">.</span><span class="k">take</span><span class="err">&#39;</span> <span class="o">(</span><span class="n">i</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">&lt;=</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">vector</span> <span class="n">α</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">vector</span> <span class="n">α</span> <span class="n">i</span>
</pre></div>


<p>(the implementation can probably even be the same)</p>


{% endraw %}
