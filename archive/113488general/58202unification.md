---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58202unification.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [unification](https://leanprover-community.github.io/archive/113488general/58202unification.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jan 25 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838225):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="bp">_</span> <span class="c1">-- fails</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="n">a</span> <span class="c1">-- works</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="bp">_</span> <span class="c1">-- works</span>
</pre></div>


<p>How does unification work? I was in the middle of something else and I wrote the first line, confident that Lean should be able to figure it out, but it didn't: I got</p>
<div class="codehilite"><pre><span></span>type mismatch, term
  le_refl ?m_3
has type
  ?m_3 ≤ ?m_3
but is expected to have type
  a ∈ {x : ℕ | x ≤ a}
</pre></div>


<p>What is Lean's algorithm for attempting to solve for these metavariables, and how does adding the extra <code>a</code> actually help it? The moment Lean unfolds the definitions of <code>has_mem.mem</code> and <code>set.mem</code> it can see what's going on -- but why does adding <code>a</code> push it towards doing this? Is the algorithm easy to explain or is it some arcane thing which I should never be thinking about?</p>

#### [ Kenny Lau (Jan 25 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838324):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">le_refl</span> <span class="bp">ℕ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="c1">--works</span>
</pre></div>

#### [ Kenny Lau (Jan 25 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838326):
<p>Lean can't even figure out that we're talking about the natural numbers</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838374):
<p>Aah! I remember now. The <code>@</code> changes Lean's strategy doesn't it.</p>

#### [ Kenny Lau (Jan 25 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838376):
<p>but once we tell Lean that, Lean can figure it out by itself</p>

#### [ Kenny Lau (Jan 25 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838379):
<p>does it?</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838380):
<p>I am not sure it's as simple as what you say</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838384):
<p>I <em>think</em> the <code>@</code> changes Lean's elaboration procedure.</p>

#### [ Kenny Lau (Jan 25 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838385):
<p>well Lean sees the head term being "has_mem.mem" and is like "what? where is has_le.le?"</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838395):
<p>Hey, look at us, mathematicians talking about head terms and elaboration procedures. This is progress, as far as I am concerned.</p>

#### [ Kenny Lau (Jan 25 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838401):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">le_refl&#39;</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="bp">_</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl&#39;</span> <span class="bp">ℕ</span> <span class="bp">_</span> <span class="c1">--works</span>
</pre></div>

#### [ Kenny Lau (Jan 25 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838402):
<p>no <code>@</code></p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838403):
<p>Right, but when I use <code>a</code> explicitly, it must say "OK! I can't see <code>has_le.le</code> -- let's go for the unfold option.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838447):
<p>Oh so you are right.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838451):
<p>It's not using <code>a</code>, it's using its type. How does this help things I wonder?</p>

#### [ Kenny Lau (Jan 25 2019 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838468):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> might we plebs be honoured by your explanation?</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838476):
<p>ha ha, he logs on and within seconds he's being pestered by mathematicians :-)</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838482):
<p>aka plebs</p>

#### [ Kevin Buzzard (Jan 25 2019 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838544):
<p>I should re-read the bit in TPIL where it talks about <code>elab_as_eliminator</code> etc.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838634):
<p>"Lean has to rely on heuristics to determine what to unfold or reduce, and when."</p>

#### [ Sebastian Ullrich (Jan 25 2019 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838699):
<p><em>arrives at university</em></p>
<blockquote>
<p>How does unification work?</p>
</blockquote>
<p><em>turns around and leaves</em></p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838749):
<p>maybe it's hard?</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838755):
<p>"using the @ symbol in front of an identifier in an expression<br>
instructs the elaborator to use the [elab_simple] strategy" -- that was what I was remembering</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838765):
<p>But </p>
<div class="codehilite"><pre><span></span><span class="n">attribute</span> <span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">has_mem</span><span class="bp">.</span><span class="n">mem</span>
<span class="n">attribute</span> <span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem</span>
<span class="n">attribute</span> <span class="o">[</span><span class="n">elab_simple</span><span class="o">]</span> <span class="n">le_refl</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="bp">_</span> <span class="c1">-- fails</span>
</pre></div>


<p>so it's not the <code>@</code>, as Kenny suspected.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838850):
<p><code>example (a : ℕ) : a ∈ {x : ℕ | x ≤ a} := @@le_refl _ _ -- fails</code></p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838865):
<p>not something you see very often, the <code>@@</code></p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156838961):
<p>The first <code>_</code> in the above is expecting <code>preorder ?m_1</code> so again it seems to be a case of "I will unfold <code>has_mem.mem</code> iff you tell me we're talking about nats"</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839117):
<p>Computers are so stupid. Why are we even here? Maybe I should go back to writing references.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839144):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> do you know if this is "higher order unification" or something else?</p>

#### [ Kenny Lau (Jan 25 2019 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839158):
<p>perhaps</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839201):
<p>I realise I am a bit unclear about what that term even means.</p>

#### [ Kenny Lau (Jan 25 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839205):
<p>has_le.le is a function with &gt; 0 inputs</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839212):
<p>i.e. what a mathematician would call "a function"</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839316):
<p>It has taken me a year to be proficient enough at Lean to be able to start formalising basic questions about what I don't understand, and because I have learnt type theory in some weird way (by trying to use it in a random context, i.e. mathematics) there are still, I'm sure, several important things which I don't understand yet.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839335):
<p>It took me a year to understand what equality was, basically, and now I'm pressing on from there.</p>

#### [ Kenny Lau (Jan 25 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839392):
<p>global sections of affine schemes are dependent functions</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156839691):
<p>This I know. As is Fermat's Last Theorem.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156840744):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">has_mem</span><span class="bp">.</span><span class="n">mem</span> <span class="n">a</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="bp">_</span> <span class="c1">-- fails</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem</span> <span class="n">a</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="bp">_</span> <span class="c1">-- works</span>
</pre></div>

#### [ Kenny Lau (Jan 25 2019 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156840862):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">le_refl&#39;</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">preorder</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="bp">_</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@@</span><span class="n">has_mem</span><span class="bp">.</span><span class="n">mem</span> <span class="o">(</span><span class="bp">@</span><span class="n">set</span><span class="bp">.</span><span class="n">has_mem</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="n">a</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl&#39;</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="c1">--fails</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem</span> <span class="n">a</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl&#39;</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="c1">--works</span>
</pre></div>

#### [ Kevin Buzzard (Jan 25 2019 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156840979):
<p>I think this must be a bug in <code>has_mem.mem</code> ;-)</p>

#### [ Kevin Buzzard (Jan 25 2019 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841033):
<p>but unfortunately I've now made it to work so need to do something serious.</p>

#### [ Sebastian Ullrich (Jan 25 2019 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841375):
<p>Yeah, this one is a bit involved. In your first example, you're asking Lean to figure out all parameters of <code>le_refl</code> by unifying its type with the expected type (the goal).</p>
<div class="codehilite"><pre><span></span>8:7: [type_context.is_def_eq_detail] [1]: @has_mem.mem nat (set nat) (@set.has_mem nat) a (@set_of nat (λ (x : nat), @has_le.le nat nat.has_le x a)) =?= @has_le.le ?m_1 (@preorder.to_has_le ?m_1 ?m_2) ?m_3 ?m_3
[type_context.is_def_eq_detail] [2]: @set.mem nat a (@set_of nat (λ (x : nat), @has_le.le nat nat.has_le x a)) =?= @preorder.le ?m_1 ?m_2 ?m_3 ?m_3
[type_context.is_def_eq_detail] unfold left: set.mem
[type_context.is_def_eq_detail] [3]: @set_of nat (λ (x : nat), @has_le.le nat nat.has_le x a) a =?= @preorder.le ?m_1 ?m_2 ?m_3 ?m_3
[type_context.is_def_eq_detail] unfold left: set_of
[type_context.is_def_eq_detail] [4]: (λ (x : nat), @has_le.le nat nat.has_le x a) a =?= @preorder.le ?m_1 ?m_2 ?m_3 ?m_3
[type_context.is_def_eq_detail] after whnf_core: @has_le.le nat nat.has_le a a =?= @preorder.le ?m_1 ?m_2 ?m_3 ?m_3
[type_context.is_def_eq_detail] [5]: nat.less_than_or_equal a a =?= @preorder.le ?m_1 ?m_2 ?m_3 ?m_3
[type_context.is_def_eq_detail] [6]: nat.less_than_or_equal =?= preorder.le
[type_context.is_def_eq_detail] on failure: nat.less_than_or_equal =?= preorder.le
[type_context.is_def_eq_detail] on failure: nat.less_than_or_equal a a =?= @preorder.le ?m_1 ?m_2 ?m_3 ?m_3
</pre></div>


<p>At different points during unification, Lean has unfolded the LHS <code>has_le.le</code> to <code>nat.less_than_or_equal</code> and the RHS's to <code>preorder.le</code>, but in the end fails to unify these two, because it doesn't know the RHS preorder yet and so can't unfold <code>preorder.le</code>.<br>
If Lean can otherwise figure out the preorder (by specifying one of the arguments), it works. If you use <code>set.mem</code>, it works more or less coincidentally because Lean prefers unfolding the definition <code>set.mem</code> over the projection <code>has_le.le</code>.</p>

#### [ Patrick Massot (Jan 25 2019 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841546):
<p>Will this be easier with the Lean 4 non-monotonic elaboration?</p>

#### [ Kenny Lau (Jan 25 2019 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841634):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> how did you get that output?</p>

#### [ Sebastian Ullrich (Jan 25 2019 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841690):
<div class="codehilite"><pre><span></span>set_option pp.implicit true
set_option pp.notation false
set_option trace.type_context.is_def_eq true
set_option trace.type_context.is_def_eq_detail true
</pre></div>

#### [ Kenny Lau (Jan 25 2019 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841741):
<p>thanks</p>

#### [ Sebastian Ullrich (Jan 25 2019 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841918):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> No. The only thing the elaborator can do to figure out <code>le_refl _</code>'s arguments is to unify it with the expected type. Elaboration order doesn't matter if there's only a single way to proceed.</p>

#### [ Patrick Massot (Jan 25 2019 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841984):
<p>ok, thanks</p>

#### [ Kevin Buzzard (Jan 25 2019 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156841988):
<p>I love it when those trace outputs turn from "incomprehensible debugging messages which I can't make any sense of and hence just ignore" to "something I can actually understand". Thanks Sebastian.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156842132):
<blockquote>
<p>If you use <code>set.mem</code>, it works more or less coincidentally because Lean prefers unfolding the definition <code>set.mem</code> over the projection <code>has_le.le</code>.</p>
</blockquote>
<p>One could imagine that rewriting Lean from scratch might change the coincidences that happen now to a completely different set of coincidences which may or may not happen. I wonder to what extent mathlib depends on such coincidences.</p>

#### [ Kevin Buzzard (Jan 25 2019 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156842295):
<p>So the bug in <code>has_mem.mem</code> is that is that it is unfolded after <code>has_le.le</code>. Maybe someone should make a PR. How does one control unfolding power?</p>

#### [ Sebastian Ullrich (Jan 25 2019 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156842367):
<p>No, they're both unfolded in the same step. You can't customize this.</p>

#### [ Sebastian Ullrich (Jan 25 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156842486):
<p>Unification isn't likely to change much, but heuristics in other parts of the elaborator may behave differently, yes.<br>
I'm not an expert on unification, but I suppose one could argue that maybe Lean shouldn't unfold projections of stuck parent projections like <code>@has_le.le ?m_1 (@preorder.to_has_le ?m_1 ?m_2)</code>. Not sure how other systems handle that.</p>

#### [ Sebastian Ullrich (Jan 25 2019 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156842926):
<p>Uh... which is exactly what it would do when using new-style structures. If you copy the relevant code to a context where <code>old_structure_cmd</code> is not set, it just works.</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">foo</span>
<span class="n">class</span> <span class="n">preorder</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">has_le</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_lt</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">le_refl</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span>
<span class="o">(</span><span class="n">le_trans</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span>
<span class="o">(</span><span class="n">lt</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span>
<span class="o">(</span><span class="n">lt_iff_le_not_le</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="bp">.</span> <span class="n">order_laws_tac</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="n">refl</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">le_refl</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">preorder</span><span class="bp">.</span><span class="n">le_refl</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">preorder</span> <span class="n">nat</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">}</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="bp">_</span>
<span class="kn">end</span> <span class="n">foo</span>
</pre></div>

#### [ Sebastian Ullrich (Jan 25 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unification/near/156843094):
<p>So depending on what <code>preorder</code> looks like in Lean 4 (where it may not be a part of core), this may just work. If it gets bundled, the unfication problems will look completely different anyway.</p>


{% endraw %}
