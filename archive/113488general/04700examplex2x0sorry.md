---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04700examplex2x0sorry.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [example (x : ℕ) : ¬ (2 + x = 0) := sorry](https://leanprover-community.github.io/archive/113488general/04700examplex2x0sorry.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 04 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124642055):
<p>It is forever taking me 3 lines to prove stuff like this. What's a slick way of doing this quickly?</p>

#### [ Mario Carneiro (Apr 04 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124642141):
<p><code>rw add_comm; apply succ_ne_zero</code></p>

#### [ Kenny Lau (Apr 05 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644443):
<div class="codehilite"><pre><span></span>example (x : ℕ) : ¬ (2 + x = 0) :=
by cases x; apply nat.no_confusion
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644446):
<p>So you (Mario) decided to do it in tactic mode. Looking at this example I realise I didn't really understand what <code>apply</code> actually does.</p>

#### [ Kenny Lau (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644490):
<p>oh hey our solutions have exactly the same length</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644493):
<p>he opened nat!</p>

#### [ Kenny Lau (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644496):
<p>oh right</p>

#### [ Kenny Lau (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644498):
<p>so i win</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644500):
<p>in some sense</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644502):
<p>He answered first</p>

#### [ Kenny Lau (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644504):
<p>well i was sleeping</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644512):
<p>solutions aren't totally ordered</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644519):
<p>you always win if you get to choose the ordering</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644528):
<p>Let me think about Mario's solution.</p>

#### [ Kenny Lau (Apr 05 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644542):
<p><code>apply [xxx]</code>, where <code>[xxx] : A -&gt; B -&gt; C -&gt; D</code> attempts to match <code>D</code> with the goal, and set <code>A</code>, <code>B</code>, <code>C</code> as three new goals if necessary</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644544):
<p><code>x + 2</code> unfolds to <code>x + bit0 1</code> which unfolds to <code>x + (1 + 1)</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644550):
<p>and I can't match this with nat.succ anything</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644596):
<p>oh I have to unfold more</p>

#### [ Kenny Lau (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644602):
<div class="codehilite"><pre><span></span>example (x : ℕ) : x + 2 = nat.succ (x + 1) := rfl
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644603):
<p><code>x + succ 1, succ (x + 1)</code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644605):
<p>right</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644617):
<p>but there's still more to do</p>

#### [ Kenny Lau (Apr 05 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644618):
<p>how so</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644624):
<p>because apply is not exact</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644625):
<p>and this is not exact</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644670):
<p>the goal is <code>f(succ x)</code> and we solve it with <code>forall n, f(n)</code></p>

#### [ Kenny Lau (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644675):
<div class="codehilite"><pre><span></span>example (x : ℕ) : ¬ (2 + x = 0) :=
by rw add_comm; exact nat.succ_ne_zero (x+1)
</pre></div>

#### [ Kenny Lau (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644676):
<p><code>apply</code> automatically fills out the arguments for you</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644678):
<p>I've seen it not automatically fill out the arguments for me</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644681):
<p>and I've had to use refine instead</p>

#### [ Kenny Lau (Apr 05 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644693):
<p>well I can't say anything if you don't have an example</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644698):
<p>yeah and I can't read the definition of apply because it's in meta land</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644739):
<p>I guess I've sometimes tried to apply to partially close a goal and it's failed</p>

#### [ Kevin Buzzard (Apr 05 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644750):
<p>I guess I just have to read the docstring more carefully.</p>

#### [ Kenny Lau (Apr 05 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124644764):
<div class="codehilite"><pre><span></span>/--
The `apply` tactic tries to match the current goal against the conclusion of the type of term. The argument term should be a term well-formed in the local context of the main goal. If it succeeds, then the tactic returns as many subgoals as the number of premises that have not been fixed by type inference or type class resolution. Non-dependent premises are added before dependent ones.

The `apply` tactic uses higher-order pattern matching, type class resolution, and first-order unification with dependent types.
-/
</pre></div>

#### [ Mario Carneiro (Apr 05 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124650332):
<p>I used <code>apply</code> in that example simply as a shorthand for <code>exact</code> (or <code>refine</code> nonterminally), it saves me a few underscores at the end. It doesn't always work, but I think it works here.</p>

#### [ Nicholas Scheel (Apr 05 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653601):
<p>what about <code>rw add_comm; from dec_trivial</code>?</p>

#### [ Kenny Lau (Apr 05 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653603):
<p>does it work?</p>

#### [ Nicholas Scheel (Apr 05 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653644):
<p><a href="https://leanprover.github.io/live/latest/#code=variable%20x%20:%20nat%0A%0Aexample%20:%20%C2%AC%20(2%20+%20x%20=%200)%20:=%20by%20rw%20add_comm;%20from%20dec_trivial" target="_blank" title="https://leanprover.github.io/live/latest/#code=variable%20x%20:%20nat%0A%0Aexample%20:%20%C2%AC%20(2%20+%20x%20=%200)%20:=%20by%20rw%20add_comm;%20from%20dec_trivial">https://leanprover.github.io/live/latest/#code=variable%20x%20:%20nat%0A%0Aexample%20:%20%C2%AC%20(2%20+%20x%20=%200)%20:=%20by%20rw%20add_comm;%20from%20dec_trivial</a></p>

#### [ Kenny Lau (Apr 05 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653651):
<p>you win</p>

#### [ Scott Morrison (Apr 05 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653845):
<p><code>simp; from dec_trivial</code></p>

#### [ Kenny Lau (Apr 05 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653851):
<p>ok you win</p>

#### [ Scott Morrison (Apr 05 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/example%20%28x%20%3A%20%E2%84%95%29%20%3A%20%C2%AC%20%282%20%2B%20x%20%3D%200%29%20%3A%3D%20sorry/near/124653852):
<p>Or import lean-tidy and: <code>obviously</code>.</p>


{% endraw %}
