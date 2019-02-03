---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28385changingtype.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [`@` changing type?](https://leanprover-community.github.io/archive/113488general/28385changingtype.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 06 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193790):
<p>What's going on here?</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">Nat</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">},</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span>

<span class="kn">definition</span> <span class="n">Zero</span> <span class="o">:</span> <span class="n">Nat</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="n">i</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="n">Zero</span> <span class="o">:</span> <span class="n">Nat</span><span class="o">)</span> <span class="c1">-- fails</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="bp">@</span><span class="n">Zero</span> <span class="o">:</span> <span class="n">Nat</span><span class="o">)</span> <span class="c1">-- works</span>
</pre></div>

#### [ Kenny Lau (Jul 06 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193835):
<p>change λ (X : Type) to λ {X : Type}?</p>

#### [ Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193846):
<p>What does that change mean?</p>

#### [ Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193849):
<p>It doesn't fix the problem</p>

#### [ Kenny Lau (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193852):
<p>never mind then</p>

#### [ Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193853):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">Nat</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">},</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span>

<span class="kn">definition</span> <span class="n">Zero</span> <span class="o">:</span> <span class="n">Nat</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="n">i</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="n">Zero</span> <span class="o">:</span> <span class="n">Nat</span><span class="o">)</span> <span class="c1">-- fails</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="bp">@</span><span class="n">Zero</span> <span class="o">:</span> <span class="n">Nat</span><span class="o">)</span> <span class="c1">-- works</span>
</pre></div>

#### [ Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193856):
<div class="codehilite"><pre><span></span>invalid type ascription, term has type
  (?m_1 → ?m_1) → ?m_1 → ?m_1 : Type
but is expected to have type
  Nat : Type 1
</pre></div>

#### [ Kevin Buzzard (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193858):
<p>It's a universe issue?</p>

#### [ Chris Hughes (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193861):
<p>change the pi</p>

#### [ Chris Hughes (Jul 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193864):
<p>brackets</p>

#### [ Chris Hughes (Jul 06 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193918):
<p>Zero has type <code>(? -&gt; ?) -&gt; ? -&gt; ?</code> or something</p>

#### [ Chris Hughes (Jul 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193934):
<p>or use <code>⦃</code></p>

#### [ Chris Hughes (Jul 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129193940):
<p>for weakly implicit</p>

#### [ Kevin Buzzard (Jul 06 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194314):
<blockquote>
<p>change λ (X : Type) to λ {X : Type}?</p>
</blockquote>
<p>This is syntactically valid but does it change anything?</p>

#### [ Chris Hughes (Jul 06 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194378):
<p>my guess is that if you don't state the type the inferred type will be <code>Pi {X}, ...</code> for one of them and <code>Pi (X), ...</code> for the other one.</p>

#### [ Mario Carneiro (Jul 06 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194534):
<p>In this case the binder on the lambda doesn't matter, since it is explicitly given the type <code>Nat</code></p>

#### [ Mario Carneiro (Jul 06 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194551):
<p>All that matters for elaboration purposes is whether <code>Nat</code> is defined as <code>Pi {X : Type}, ...</code> or <code>Pi (X : Type), ...</code></p>

#### [ Johan Commelin (Jul 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194690):
<p>Do I correctly infer from Kevin's example that Lean does not remember that <code>Zero</code> has type <code>Nat</code>, even if it is explicitly told so during the <code>definition</code>? So it uses that fact while type checking the definition, but afterwards throws it away and only stores the term (or something)?</p>

#### [ Kevin Buzzard (Jul 06 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194746):
<p>I think the problem is that when Lean sees <code>Zero</code> with <code>{}</code> it immediately tries to fill in the <code>{}</code> variable, so <code>Zero</code> is the same as <code>@Zero _</code> which is not the same as <code>@Zero</code></p>

#### [ Kevin Buzzard (Jul 06 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194750):
<p>If you use <code>{{}}</code> then Lean decides to wait until later before guessing what goes in the brackets</p>

#### [ Kevin Buzzard (Jul 06 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194801):
<p>The easiest fix is just to use <code>(X : Type)</code> I guess</p>

#### [ Mario Carneiro (Jul 06 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194807):
<p>When defining a type as a pi like this, you almost never want to use <code>Pi {X}</code> because of "surprises" like this</p>

#### [ Mario Carneiro (Jul 06 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194818):
<p>This is one of the main use cases for <code>Pi {{X}}</code></p>

#### [ Mario Carneiro (Jul 06 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60%40%60%20changing%20type%3F/near/129194820):
<p>like in the definition of <code>set.subset</code></p>


{% endraw %}
