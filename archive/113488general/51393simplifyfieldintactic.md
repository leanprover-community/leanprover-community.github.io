---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51393simplifyfieldintactic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simplify field in tactic](https://leanprover-community.github.io/archive/113488general/51393simplifyfieldintactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Sep 10 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639356):
<p>Trivial question: I've got an instance <code>s</code> of some structure which has a <code>nat</code>-valued field <code>f</code>. In tactic mode I have as a hypothesis <code>v : nat := s.f</code>. What can I do to replace v with with its actual <code>nat</code> value? Sorry for the noise</p>

#### [ Mario Carneiro (Sep 10 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639619):
<p>what do you mean? If you are in tactic mode, you aren't proving anything so it doesn't matter</p>

#### [ Mario Carneiro (Sep 10 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639634):
<p>or do you mean that <code>v : nat := s.f</code> is in the local context of the proof state?</p>

#### [ Mario Carneiro (Sep 10 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639640):
<p>You can use <code>dsimp only [v] {zeta := tt}</code> to zeta expand <code>v</code></p>

#### [ Keeley Hoek (Sep 10 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639833):
<p>Hi Mario, I think that's what I mean. If I understand you right, are you saying something like this:</p>
<div class="codehilite"><pre><span></span>structure my_struct :=
(f : ℕ)

example : false := begin
  let s : my_struct := ⟨42⟩,
  let v := s.f,
  dsimp only [v] {zeta := tt},
  admit
end
</pre></div>


<p>should work? Weirdly, the <code>dsimp</code> line fails with</p>
<div class="codehilite"><pre><span></span>dsimplify tactic failed to simplify
state:
s : my_struct := {f := 42},
v : ℕ := s.f
⊢ false
</pre></div>


<p>:'(</p>

#### [ Simon Hudon (Sep 10 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133639884):
<p>Does <code>v</code> occur in the goal?</p>

#### [ Keeley Hoek (Sep 10 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640190):
<p>No, well secretly I'm trying to write a function which I can pass an <code>expr</code> and get back a "simplified" <code>expr</code>; in this case hopefully <code>s.f</code> will become <code>42</code>.</p>

#### [ Keeley Hoek (Sep 10 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640248):
<p>Is there anything which does something like this? Maybe even just like <code>1 + 1</code> -&gt; <code>2</code></p>

#### [ Kenny Lau (Sep 10 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640374):
<p>from my experience, not many tactics know about definitions (i.e. <code>:=</code>)</p>

#### [ Kenny Lau (Sep 10 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640378):
<p>which is quite annoying</p>

#### [ Simon Hudon (Sep 10 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640385):
<p>You can have a look at <code>tactic.dsimp_target</code> in <code>init/meta/simp_tactic.lean</code> to do that. But if your variable <code>v</code> does not occur in the expression, it will fail. You may have to enclose it in <code>try</code></p>

#### [ Kenny Lau (Sep 10 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640455):
<p>oh and you'll never change the definition of <code>v</code> using any tactic.</p>

#### [ Kenny Lau (Sep 10 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640463):
<p>just literally no tactic can rewrite definition (things to the right of <code>:=</code>) in hypothesis, in my experience</p>

#### [ Kenny Lau (Sep 10 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640468):
<p>my workaround:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">my_struct</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="k">let</span> <span class="n">s</span> <span class="o">:</span> <span class="n">my_struct</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">42</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">s</span><span class="bp">.</span><span class="n">f</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">hv</span> <span class="o">:</span> <span class="n">v</span> <span class="bp">=</span> <span class="mi">42</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Sep 10 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640484):
<p>No, you can do some manipulation</p>

#### [ Simon Hudon (Sep 10 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640526):
<p>in <code>tactic.basic</code>, in <code>mathlib</code>, you can use <code>local_def_value</code> to get the value of a definition. Then you can rewrite that experience, create a new definition and clear the old one</p>

#### [ Keeley Hoek (Sep 10 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640746):
<p>Thanks, yeah I was poking around in <code>simp_target</code> and <code>simplify</code> before and was wondering why it was failing. I note that</p>
<div class="codehilite"><pre><span></span>structure my_struct :=
(f : ℕ)

def s : my_struct := ⟨42⟩

#reduce s.f
</pre></div>


<p>(obviously) prints <code>42</code>. Is there any way to capture the result like this? I see that in the kernel reduce calls <code>normalize(...)</code> which returns an <code>expr</code>, is there away to get it to do that and capture the result myself?</p>

#### [ Simon Hudon (Sep 10 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640862):
<p>Are you trying to evaluate the expression? If it's an arithmetic expression, you can use norm_num. Otherwise, whnf should take you part of the way there</p>

#### [ Simon Hudon (Sep 10 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133640973):
<p>Also, do you mean <code>normalize</code> from <code>ring.lean</code>?</p>

#### [ Keeley Hoek (Sep 10 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133641053):
<p>Thanks I'll dig in and read about <code>whnf</code> for a bit. I don't think so, there's this file <code>src/library/normalize.cpp</code> which <code>normalize</code>s <code>expr</code>s you give it.</p>

#### [ Keeley Hoek (Sep 10 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20field%20in%20tactic/near/133641194):
<p>Actually, I think:</p>
<div class="codehilite"><pre><span></span>meta def dme : tactic unit := do
  let no_dflt := ff,
  let attr_names : list name := [],
  let hs : list simp_arg_type := [],
  (s, to_unfold) ← mk_simp_set no_dflt attr_names hs,
  e ← s.dsimplify to_unfold `({ my_struct . f := 42 }.f),
  trace e

#eval dme
</pre></div>


<p>might do what I want!</p>


{% endraw %}
