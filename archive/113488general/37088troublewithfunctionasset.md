---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37088troublewithfunctionasset.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [trouble with function as set](https://leanprover-community.github.io/archive/113488general/37088troublewithfunctionasset.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Marcus Klaas (Dec 02 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700590):
<p>Hi! Is this a proper channel for asking (elementary) questions?</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700592):
<p>I'm stuck trying to prove the following trivial statement:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">func_as_set</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">f</span><span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">}</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="err">∈</span> <span class="n">func_as_set</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Marcus Klaas (Dec 02 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700597):
<p>Refl and Simp tactics don't seem to work, unfortunately</p>

#### [ Chris Hughes (Dec 02 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700700):
<p>Did you try <code>rfl</code>?</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700743):
<p>I don't think so. I will do it now.</p>

#### [ Chris Hughes (Dec 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700744):
<p><code>refl</code> works for any reflexive relation, and I guess the elaborator looks for a proof that <code>∈</code> is reflexive. <code>rfl</code> is only for equality.</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700750):
<p>omg that worked. Thanks for the elaboration too. Very useful to know!!</p>

#### [ Kevin Buzzard (Dec 02 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701125):
<p>PS</p>
<blockquote>
<p>Hi! Is this a proper channel for asking (elementary) questions?</p>
</blockquote>
<p>Here is fine, although most of the elementary questions get asked in <a class="stream" data-stream-id="113489" href="/#narrow/stream/113489-new-members">#new members</a> . There are no hard and fast rules though.</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701289):
<p>Cool, thanks</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701337):
<p>In that case, I have another trivial follow up ;-) How does one go from a hypothesis in this form</p>
<div class="codehilite"><pre><span></span><span class="n">x</span> <span class="err">∈</span><span class="o">{</span> <span class="n">y</span> <span class="bp">|</span> <span class="n">P</span> <span class="n">y</span> <span class="o">}</span>
</pre></div>


<p>to</p>
<div class="codehilite"><pre><span></span><span class="n">P</span> <span class="n">x</span>
</pre></div>


<p>?</p>

#### [ Kevin Buzzard (Dec 02 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701352):
<p>Again isn't that <code>rfl</code>?</p>

#### [ Chris Hughes (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701400):
<p><code>rw set.mem_set_of_eq</code> also works. That lemma does not have a good name.</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701402):
<p>but you can't use that when it's a hypothesis, right?</p>

#### [ Chris Hughes (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701405):
<p><code>rw _ at h</code></p>

#### [ Marcus Klaas (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701406):
<p>right - trying now</p>

#### [ Kevin Buzzard (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701407):
<p>Are you in tactic mode or term mode?</p>

#### [ Chris Hughes (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701409):
<p>if <code>h</code> is your hypothesis.</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701412):
<p>tactic mode</p>

#### [ Kenny Lau (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701420):
<p>you can just change it</p>

#### [ Kenny Lau (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701422):
<p>or pretend that it's already in that form</p>

#### [ Kenny Lau (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701424):
<p>depending on what you're trying to do</p>

#### [ Kevin Buzzard (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701425):
<p>You could do <code>change P x at h</code> as well</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701431):
<p>oooh, that's useful<br>
thanks folks!</p>

#### [ Kevin Buzzard (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701435):
<p>Because the two terms are definitionally equal you might not even need to change it</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701602):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> my proposition is an equality in this case. i need it for a rewrite. doesnt seem to work without an explicit change</p>

#### [ Marcus Klaas (Dec 02 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701605):
<p>with the change, it does! :-)</p>

#### [ Kevin Buzzard (Dec 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701611):
<p>Post some working code?</p>

#### [ Kevin Buzzard (Dec 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701615):
<p>But yes, <code>rw</code> needs things to be unravelled explicitly.</p>


{% endraw %}
