---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22985rwunderlambda.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rw under lambda](https://leanprover-community.github.io/archive/113488general/22985rwunderlambda.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (May 04 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126107890):
<p><code>rw</code> refuses to perform rewrites inside a lambda, as far as I can tell. Is there a convenient way to do so?<br>
For example, frequently my goal is of the form <code>∃ x, P x ∧ Q x</code> and I would like to rewrite it to <code>∃ x, P x ∧ Q' x</code> (where I know <code>Q x ↔ Q' x</code>).</p>

#### [ Simon Hudon (May 04 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126107975):
<p>use <code>simp</code> instead of <code>rw</code> if you want to rewrite under lambda. If you don't want <code>simp</code> to use default <code>simp</code> rules, you can do <code>simp only [my_rule]</code></p>

#### [ Reid Barton (May 04 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126108133):
<p>Oops, I tried <code>simp only</code>, but I mixed up <code>.symm</code> and <code>.mpr</code> so it didn't appear to work. Thanks!</p>

#### [ Patrick Massot (May 04 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126109753):
<p>See also <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md</a></p>

#### [ Reid Barton (May 04 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126111096):
<p>I couldn't work out how to do this with <code>conv</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">conv</span> <span class="k">begin</span>
    <span class="c1">-- use rw add_comm somehow</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">h</span>
<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (May 04 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126111175):
<p>I tried <code>congr, funext, congr</code> but I got an error that I didn't understand on the second <code>congr</code></p>

#### [ Simon Hudon (May 04 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126111358):
<p>try:</p>
<div class="codehilite"><pre><span></span>example : (∃ a b, a + b = 0) ↔ ∃ a b, b + a = 0 :=
by conv in (_ + _) begin
  rw add_comm,
end
</pre></div>

#### [ Reid Barton (May 04 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126111674):
<p>ah, interesting</p>

#### [ Simon Hudon (May 04 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126112393):
<p>This would also work, btw:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">))</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">conv</span> <span class="k">in</span> <span class="o">(</span><span class="bp">_</span> <span class="bp">+</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="n">add_comm</span> <span class="o">},</span>
  <span class="n">exact</span> <span class="n">h</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (May 04 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20lambda/near/126115523):
<p><code>conv in ( _ = _)</code> would also work, but I would be interested in seeing a solution without pattern matching. It seems we lack some navigation tactic (like <code>to_lhs</code>/<code>to_rhs</code>,  <code>congr</code>). <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> any idea?</p>


{% endraw %}
