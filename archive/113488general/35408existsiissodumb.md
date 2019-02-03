---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35408existsiissodumb.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [`existsi` is so dumb](https://leanprover-community.github.io/archive/113488general/35408existsiissodumb.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 19 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962582):
<p>I often really feel like the <code>existsi</code> tactic is slacking off. It is always moaning that it doesn't know the type of what I suggest, even though it knows exactly the type it is expecting to get. And now this!</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>


<span class="kn">theorem</span> <span class="n">existsi_is_so_dumb</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">S</span> <span class="bp">=</span> <span class="n">S</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">this</span> <span class="o">:</span> <span class="n">has_emptyc</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="err">∅</span><span class="o">,</span>
  <span class="c1">-- new goal `⊢ has_emptyc (set α)` appears</span>
  <span class="c1">-- I mean -- what did you even try??</span>
  <span class="o">{</span> <span class="n">refl</span><span class="o">},</span>
  <span class="o">{</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Nov 19 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962659):
<p>It's not my favorite tactic</p>

#### [ Mario Carneiro (Nov 19 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962674):
<p>it's more or less completely superceded by <code>refine</code></p>

#### [ Mario Carneiro (Nov 19 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962760):
<p>I can see why:</p>
<div class="codehilite"><pre><span></span>meta def existsi : parse pexpr_list_or_texpr → tactic unit
| []      := return ()
| (p::ps) := i_to_expr p &gt;&gt;= tactic.existsi &gt;&gt; existsi ps
</pre></div>


<p>The type of <code>p</code> is elaborated with no other information from the target type</p>

#### [ Mario Carneiro (Nov 19 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962824):
<p>The underlying <code>existsi</code> tactic is a bit more sophisticated, and it could have elaborated in the appropriate context</p>

#### [ Johan Commelin (Nov 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962852):
<p>Is this in core?</p>

#### [ Mario Carneiro (Nov 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962854):
<p>yes</p>

#### [ Mario Carneiro (Nov 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962858):
<p>still it's all just a long winded way of doing the same thing as <code>refine &lt;e1, e2, _&gt;</code></p>

#### [ Johan Commelin (Nov 19 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962914):
<p>Hmm, we could define a tactic <code>use e1 e2 ...</code> that is a wrapper around <code>refine</code>.</p>

#### [ Johan Commelin (Nov 19 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962919):
<p>It is both shorter and more readable than <code>existsi</code>.</p>

#### [ Mario Carneiro (Nov 19 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962928):
<p>the point is that the extra flexibility in where to put the underscores is actually useful</p>

#### [ Johan Commelin (Nov 19 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147962953):
<p>Of course, so <code>use</code> is for when you don't need that flexibility and you want some sort of beginner-friendly readable proof.</p>

#### [ Kevin Buzzard (Nov 19 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147963409):
<p><code>existsi</code> is a rubbish name anyway. No mathematician knows what it means, it's not even a word. How about <code>use x := refine x _ _ _ _ ... _</code>. Can we do that? Beginner mathematicans would like it.</p>

#### [ Kevin Buzzard (Nov 19 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147963515):
<p>or however it would work, is it just <code>use x := refine \&lt; x,_\&gt;</code>?, I don't know exactly how to make it work, all I know is that it would be better than existsi</p>

#### [ Kevin Buzzard (Nov 19 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/147963708):
<p>I don't know how to define <code>use x := refine \&lt;x, _\&gt;</code> in Lean. This involves making a tactic that takes an input, and I only ever write tactics by just writing them in tactic mode and then sticking a load of backticks and square brackets everywhere.</p>

#### [ Patrick Massot (Nov 20 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148044440):
<p>So, what's the conclusion of that thread? Who is writing that <code>use</code> tactic?</p>

#### [ Johan Commelin (Nov 20 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148044510):
<p>How about <code>meta def use := refine</code>?</p>

#### [ Rob Lewis (Nov 20 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148045273):
<p>I think this is approximately right.</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">use</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">parse</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span><span class="bp">.</span><span class="n">pexpr_list_or_texpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">tactic</span><span class="bp">.</span><span class="n">refine</span> <span class="err">$</span> <span class="n">l</span><span class="bp">.</span><span class="n">foldr</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span> <span class="n">p</span><span class="o">,</span> <span class="bp">``</span><span class="o">(</span><span class="bp">⟨</span><span class="err">%%</span><span class="n">t</span><span class="o">,</span> <span class="err">%%</span><span class="n">p</span><span class="bp">⟩</span><span class="o">))</span> <span class="n">pexpr</span><span class="bp">.</span><span class="n">mk_placeholder</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">6</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">use</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">],</span> <span class="n">refl</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">existsi_is_so_dumb</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">S</span> <span class="bp">=</span> <span class="n">S</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">use</span> <span class="err">∅</span><span class="o">,</span> <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 20 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148048724):
<p>how about we PR core</p>

#### [ Patrick Massot (Nov 21 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110505):
<p>How about PRing </p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">use</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">parse</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span><span class="bp">.</span><span class="n">pexpr_list_or_texpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">refine</span> <span class="err">$</span> <span class="n">l</span><span class="bp">.</span><span class="n">foldr</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span> <span class="n">p</span><span class="o">,</span> <span class="bp">``</span><span class="o">(</span><span class="bp">⟨</span><span class="err">%%</span><span class="n">t</span><span class="o">,</span> <span class="err">%%</span><span class="n">p</span><span class="bp">⟩</span><span class="o">))</span> <span class="n">pexpr</span><span class="bp">.</span><span class="n">mk_placeholder</span><span class="o">,</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">try</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">refl</span>
</pre></div>


<p>to mathlib? I only added trying refl, just in case (I hope it's not too time consuming)</p>

#### [ Chris Hughes (Nov 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110636):
<p>Does it also solve the issue where <code>existsi</code> does not know the expected type. So if I type <code>existsi ⟨x, y⟩</code>, it fails because it doesn't know what type <code>⟨x, y⟩</code> is even though this should be inferrable from the goal.</p>

#### [ Patrick Massot (Nov 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110648):
<p>It's meant to solve this issue, yes</p>

#### [ Patrick Massot (Nov 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110650):
<p>And it does on Kevin's examples</p>

#### [ Patrick Massot (Nov 21 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110655):
<p>Could you provide more examples?</p>

#### [ Chris Hughes (Nov 21 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148110725):
<p>I never use it.</p>

#### [ Patrick Massot (Nov 21 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111034):
<p>Here are my test cases so far:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">use</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">parse</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span><span class="bp">.</span><span class="n">pexpr_list_or_texpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">refine</span> <span class="err">$</span> <span class="n">l</span><span class="bp">.</span><span class="n">foldr</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span> <span class="n">p</span><span class="o">,</span> <span class="bp">``</span><span class="o">(</span><span class="bp">⟨</span><span class="err">%%</span><span class="n">t</span><span class="o">,</span> <span class="err">%%</span><span class="n">p</span><span class="bp">⟩</span><span class="o">))</span> <span class="n">pexpr</span><span class="bp">.</span><span class="n">mk_placeholder</span><span class="o">,</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">try</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">refl</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">6</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">use</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">S</span> <span class="bp">=</span> <span class="n">S</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">use</span> <span class="err">∅</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">use</span> <span class="mi">42</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">×</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">use</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="mi">42</span><span class="bp">⟩</span>
</pre></div>

#### [ Rob Lewis (Nov 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111139):
<p>The first example is more interesting with <code>int</code> instead of <code>nat</code> since <code>existsi</code> fails in that case.</p>

#### [ Patrick Massot (Nov 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111142):
<p>Only the first one works with <code>existsi</code>, even if you end the line with <code>; refl</code></p>

#### [ Patrick Massot (Nov 21 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111157):
<p>Right, replace nat by int in the first example</p>

#### [ Patrick Massot (Nov 21 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111210):
<p>Rob, would you mind PRing this? I can do it of course, but I don't want to claim any credit</p>

#### [ Rob Lewis (Nov 21 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111239):
<p>Yeah, I'll do it. It's a little hackish, but I couldn't think of a nicer one line solution off the top of my head. So, good enough!</p>

#### [ Patrick Massot (Nov 21 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148111607):
<p>Of course the real test would be to replace every use of <code>existsi</code> in mathlib, but that's more work, and probably not worth the trouble</p>

#### [ Rob Lewis (Nov 21 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148112078):
<p>PRed. That's definitely not worth the trouble.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148112151):
<p>Thanks Rob! This looks much much better pedagogically</p>

#### [ Kevin Buzzard (Nov 21 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148112259):
<p>And thanks Patrick too for helping to make it happen</p>

#### [ Rob Lewis (Nov 21 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148114826):
<p><a href="/user_uploads/3121/lVNrNYy6wJQaiT7sCVQo4wsi/if-you-give-a-mouse-a-cookie-HarperCollins.jpeg" target="_blank" title="if-you-give-a-mouse-a-cookie-HarperCollins.jpeg">if-you-give-a-mouse-a-cookie-HarperCollins.jpeg</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/lVNrNYy6wJQaiT7sCVQo4wsi/if-you-give-a-mouse-a-cookie-HarperCollins.jpeg" target="_blank" title="if-you-give-a-mouse-a-cookie-HarperCollins.jpeg"><img src="/user_uploads/3121/lVNrNYy6wJQaiT7sCVQo4wsi/if-you-give-a-mouse-a-cookie-HarperCollins.jpeg"></a></div>

#### [ Rob Lewis (Nov 21 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148114844):
<p>(<a href="https://github.com/leanprover/mathlib/pull/486" target="_blank" title="https://github.com/leanprover/mathlib/pull/486">https://github.com/leanprover/mathlib/pull/486</a>)</p>

#### [ Jeremy Avigad (Nov 21 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148117611):
<p>I don't see a big win over <code>exists</code> and <code>refine</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">6</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">S</span> <span class="bp">=</span> <span class="n">S</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="err">∅</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">×</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">exact</span> <span class="bp">⟨⟨</span><span class="mi">1</span><span class="o">,</span> <span class="mi">42</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
</pre></div>


<p><code>exists</code> and <code>refine</code> with the corner brackets is more flexible, since the corner brackets can handle structures with multiple arguments and nested structures. If you use <code>exact</code> with placeholders, squiggly lines well tell you what you need to fill in. You can use whatever tactics you want to discharge the final goal. Are there any advantages to <code>use</code>? Doesn't it just clutter the language?</p>

#### [ Rob Lewis (Nov 21 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148119422):
<p>When you're proving <code>∃ x, P x</code> in tactic mode, and the proof of <code>P a</code> is long, you don't want to write <code>exact &lt;a, begin end&gt;</code>. You can write <code>refine &lt;a, _&gt;</code> and keep going. This tactic is exactly an abbreviation for that, that looks more natural. <code>use</code> is really a replacement for <code>existsi</code>,  except we can't change that.</p>

#### [ Patrick Massot (Nov 21 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60existsi%60%20is%20so%20dumb/near/148119507):
<p>Jeremy, the comparison is not with <code>exact</code> and <code>refine</code>. <code>use</code> is meant as a better behaved drop-in replacement of <code>existsi</code></p>


{% endraw %}
