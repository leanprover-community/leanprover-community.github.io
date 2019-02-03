---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04284linarith.html
---

## Stream: [general](index.html)
### Topic: [linarith](04284linarith.html)

---


{% raw %}
#### [ Johan Commelin (Nov 21 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148096612):
<p>Shouldn't <code>linarith</code> be able to take care of this?</p>
<div class="codehilite"><pre><span></span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">),</span>
<span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">),</span>
<span class="n">ha</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">b</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="n">b</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
<span class="n">a_1</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">&gt;</span> <span class="n">b</span><span class="bp">.</span><span class="n">val</span>
<span class="err">⊢</span> <span class="n">false</span>
</pre></div>

#### [ Kenny Lau (Nov 21 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148096896):
<p>I thought it has been made clear that <code>linarith</code> doesn't deal with <code>nat</code></p>

#### [ Patrick Massot (Nov 21 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097084):
<p>After <code>apply ha</code> it should be an easy target for <code>mono</code> but it doesn't work <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Patrick Massot (Nov 21 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097138):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> </p>
<div class="codehilite"><pre><span></span>import tactic.monotonicity

example (n : ℕ)
(i : fin (n + 1 + 1))
(a b : fin (n + 1))
(ha : ¬a.val &lt; i.val)
(h : b.val &lt; i.val)
(H : a.val ≤ b.val)
(a_1 : nat.succ (a.val) &gt; b.val) : false :=
begin
  apply ha,
  mono*,  -- does nothing :-(
  exact calc a.val ≤ _ : H
  ... &lt; _ : h,
end
</pre></div>

#### [ Rob Lewis (Nov 21 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097160):
<p>Change <code>nat.succ (a.val)</code> to <code>a.val + 1</code>.</p>

#### [ Patrick Massot (Nov 21 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097178):
<p>This is the first thing I tried, but it changes nothing</p>

#### [ Kenny Lau (Nov 21 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097262):
<p>maybe stop (over)relying on tactics</p>

#### [ Rob Lewis (Nov 21 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097310):
<p>Oh, change <code>ha</code> to <code>a.val ≥ i.val</code>.</p>

#### [ Patrick Massot (Nov 21 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097329):
<p>that works</p>

#### [ Patrick Massot (Nov 21 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097395):
<p>Kenny, the discussion is not really about how to prove that particular goal. It's about having a toolset which gets rid of hundred of stupid goals like this, that would otherwise break our proof flow and concentration</p>

#### [ Rob Lewis (Nov 21 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097485):
<p>There's something wrong with the routine that makes <code>linarith</code> work for <code>nat</code> and the part that deals with negated hypotheses, I'll look into it when I have a minute.</p>

#### [ Patrick Massot (Nov 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097660):
<p>Nice! In the mean time, Johan can use <code>replace ha := le_of_not_lt ha ; linarith</code> to close that goal</p>

#### [ Rob Lewis (Nov 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097675):
<p>Or <code>apply ha; linarith</code>.</p>

#### [ Patrick Massot (Nov 21 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148097682):
<p>indeed</p>

#### [ Sebastien Gouezel (Nov 21 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148099129):
<p>Another <code>linarith</code>wishlist entry: if there is an assumption <code>abs x ≤ c</code>, convert it to <code>x ≤ c</code> and <code>-x ≤ c</code>.</p>

#### [ Rob Lewis (Nov 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148101337):
<p>There are various unfolding/preprocessing things like that, that <code>linarith</code> could do. Writing a separate tactic that unfolds <code>abs</code> would be very easy, and you could even add <code>meta def linarith' := unfold_abs; linarith</code> if you wanted. But I'm not sure that bundling all these things into the main tactic is a good idea.</p>

#### [ Rob Lewis (Nov 21 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148101362):
<p>There's now a PR open to fix Johan's problem, btw.</p>

#### [ Sebastien Gouezel (Nov 21 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148101659):
<p>OK, I understand. I can definitely unfold it by hand when needed. I am just motivated by the principle of maximal laziness.</p>

#### [ Johan Commelin (Nov 21 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104169):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> Cool! Thanks a lot.</p>

#### [ Johan Commelin (Nov 21 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104182):
<p>Now there is still the problem with <code>nat.succ _</code> vs <code>_ + 1</code>. Could that be fixed as well?</p>

#### [ Johan Commelin (Nov 21 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104248):
<p>Because then I could run <code>split_ifs with foo bar; {ext, simp, linarith}</code> and be done with it. Otherwise I need to explicitly <code>change</code> my goal for each goal. Or should I write a custom simp-lemma for this, that I use locally?</p>

#### [ Johan Commelin (Nov 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104284):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">δ_monotone</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">])</span> <span class="o">:</span> <span class="n">monotone</span> <span class="o">(</span><span class="n">δ</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">change</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="n">b</span><span class="bp">.</span><span class="n">val</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ_above</span><span class="o">],</span>
  <span class="n">split_ifs</span> <span class="k">with</span> <span class="n">ha</span> <span class="n">hb</span><span class="bp">;</span>
  <span class="n">try</span> <span class="o">{</span> <span class="n">ext1</span><span class="o">,</span> <span class="n">simp</span><span class="o">,</span> <span class="n">linarith</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">ext1</span><span class="o">,</span> <span class="n">simp</span><span class="o">,</span> <span class="n">change</span> <span class="bp">_</span> <span class="bp">≤</span> <span class="bp">_</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span> <span class="n">linarith</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">ext1</span><span class="o">,</span> <span class="n">simp</span><span class="o">,</span> <span class="n">change</span> <span class="bp">_</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="bp">_</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span> <span class="n">linarith</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Rob Lewis (Nov 21 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104414):
<p><span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> If you don't want to do it by hand, you can finish this and use it (or modify it to fit your purposes). Just use <code>unfold_abs; linarith</code> in place of <code>linarith</code>, or define an alias for that.</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>
<span class="kn">lemma</span> <span class="n">le_and_le_of_abs_le</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_linear_ordered_comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">∧</span> <span class="bp">-</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">unfold_abs</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">local_context</span> <span class="bp">&gt;&gt;=</span> <span class="n">list</span><span class="bp">.</span><span class="n">mmap&#39;</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">e</span><span class="o">,</span> <span class="n">try</span> <span class="o">(</span><span class="n">mk_app</span> <span class="bp">`</span><span class="n">le_and_le_of_abs_le</span> <span class="o">[</span><span class="n">e</span><span class="o">]</span> <span class="bp">&gt;&gt;=</span> <span class="n">cases</span><span class="o">))</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">abs</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold_abs</span>
<span class="kn">end</span>
</pre></div>

#### [ Rob Lewis (Nov 21 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104502):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> This falls into the same basket as Sebastien's request. There are lots of constants that can be unfolded or rewritten into a form that <code>linarith</code> will handle. I don't want to build them all in. You can just add <code>nat.succ_eq_add_one</code> to the <code>simp</code> call.</p>

#### [ Johan Commelin (Nov 21 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104578):
<p>Ok, thanks, will do.</p>

#### [ Johan Commelin (Nov 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148104774):
<blockquote>
<p>maybe stop (over)relying on tactics</p>
</blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Can you golf this?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">δ_monotone</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">])</span> <span class="o">:</span> <span class="n">monotone</span> <span class="o">(</span><span class="n">δ</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="n">b</span><span class="bp">.</span><span class="n">val</span><span class="o">),</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ_above</span><span class="o">]</span><span class="bp">;</span> <span class="n">split_ifs</span> <span class="k">with</span> <span class="n">ha</span> <span class="n">hb</span><span class="bp">;</span> <span class="o">{</span> <span class="n">ext1</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_eq_add_one</span><span class="o">],</span> <span class="n">linarith</span> <span class="o">}</span>
</pre></div>


<p>You can find it here: <a href="https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplex_category.lean#L33-L35" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplex_category.lean#L33-L35">https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplex_category.lean#L33-L35</a></p>

#### [ Johan Commelin (Nov 21 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105362):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> So presumably goals of this form are also outside the scope of <code>linarith</code>?</p>
<div class="codehilite"><pre><span></span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">),</span>
<span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">),</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
<span class="n">h_1</span> <span class="o">:</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">cast_succ</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="n">j</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
<span class="n">h_2</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
<span class="n">h_3</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span>
<span class="err">⊢</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span>
</pre></div>


<p>I have 7 goals that are all of this form or another... I would like to kill them all in one go.</p>

#### [ Johan Commelin (Nov 21 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105382):
<p>Sorry, I should paste context...</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105384):
<p>So these are nats?</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105470):
<p>What is the argument in maths?</p>

#### [ Rob Lewis (Nov 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105480):
<p>Um, <code>linarith</code> doesn't know anything about the relation between <code>fin</code> and <code>fin.val</code>, or anything about <code>fin.succ</code> or <code>fin.cast_succ</code>.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105484):
<p>I am not sure you can ask <code>linarith</code> to start unfolding <code>fin.succ</code> or stuff like that</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105487):
<p>There will be a never-ending list of things you want it to unfold.</p>

#### [ Rob Lewis (Nov 21 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105530):
<p>Basically, those are a bunch of random inequalities between distinct variables, not even all of the same type.</p>

#### [ Rob Lewis (Nov 21 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105541):
<p>The only thing <code>linarith</code> will learn is that <code>j.val &lt; i.val</code>.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105559):
<p>What about <code>x ∈ {a : ℕ | a &gt; 5}</code> ? That unfolds to an inequality, but it's surely not <code>linarith</code>'s job to figure that out.</p>

#### [ Kenny Lau (Nov 21 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105571):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> there must be such a function in mathlib</p>

#### [ Kenny Lau (Nov 21 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105575):
<p>(or not)</p>

#### [ Kenny Lau (Nov 21 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105617):
<p>(yes it’s decidable)</p>

#### [ Rob Lewis (Nov 21 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105647):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> right, see my last few comments. <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span> Infinitely many things can unfold to linear inequalities. If <code>linarith</code> tries everything possible it will be unpredictable and slow.</p>

#### [ Johan Commelin (Nov 21 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148105717):
<p>Cool, I'm getting the hang of this! <span class="user-mention" data-user-id="110596">@Rob Lewis</span> Thanks for your help. I'm starting to understand how to play with <code>linarith</code>.<br>
After:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">simplicial_identity₁</span> <span class="o">{</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">]}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span><span class="o">)</span> <span class="o">:</span> <span class="n">δ</span> <span class="n">j</span><span class="bp">.</span><span class="n">succ</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">δ</span> <span class="n">i</span><span class="bp">.</span><span class="n">cast_succ</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">j</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">change</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">funext</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ_above</span><span class="o">],</span>
  <span class="n">split_ifs</span><span class="bp">;</span> <span class="o">{</span> <span class="n">try</span> <span class="o">{</span><span class="n">ext1</span><span class="o">},</span> <span class="n">try</span> <span class="o">{</span><span class="n">simp</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_eq_add_one</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*</span><span class="o">},</span> <span class="n">try</span> <span class="o">{</span><span class="n">linarith</span><span class="o">}</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>


<p>Before:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">simplicial_identity₁</span> <span class="o">{</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">]}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span><span class="o">)</span> <span class="o">:</span> <span class="n">δ</span> <span class="n">j</span><span class="bp">.</span><span class="n">succ</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">δ</span> <span class="n">i</span><span class="bp">.</span><span class="n">cast_succ</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">j</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">funext</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ_above</span><span class="o">],</span>
  <span class="n">by_cases</span> <span class="n">hja</span> <span class="o">:</span> <span class="o">(</span><span class="n">j</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="o">),</span>
  <span class="o">{</span> <span class="k">have</span> <span class="n">hja&#39;</span> <span class="o">:</span> <span class="o">((</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="n">j</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">begin</span>
      <span class="n">simp</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_le_succ</span> <span class="n">hja</span><span class="o">,</span>
    <span class="kn">end</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hia</span> <span class="o">:</span> <span class="o">((</span><span class="n">i</span><span class="bp">.</span><span class="n">cast_succ</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">begin</span>
      <span class="n">simp</span><span class="o">,</span>
      <span class="n">refine</span> <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="n">H</span> <span class="bp">_</span><span class="o">),</span>
      <span class="n">exact</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_trans</span> <span class="n">hja</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_succ</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="o">))</span>
    <span class="kn">end</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">if_pos</span> <span class="n">hja</span><span class="o">,</span> <span class="n">if_pos</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_trans</span> <span class="n">H</span> <span class="n">hja</span><span class="o">),</span> <span class="n">if_pos</span> <span class="n">hja&#39;</span><span class="o">,</span> <span class="n">if_pos</span> <span class="n">hia</span><span class="o">]},</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">dif_neg</span> <span class="n">hja</span><span class="o">],</span>
    <span class="n">by_cases</span> <span class="n">hia</span> <span class="o">:</span> <span class="o">(</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="o">),</span>
    <span class="o">{</span> <span class="k">have</span> <span class="n">hia&#39;</span> <span class="o">:</span> <span class="o">((</span><span class="n">fin</span><span class="bp">.</span><span class="n">raise</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">raise</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">:=</span> <span class="n">hia</span><span class="o">,</span>

      <span class="k">have</span> <span class="n">hja&#39;</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">j</span><span class="bp">.</span><span class="n">succ</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="n">a</span><span class="bp">.</span><span class="n">succ</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">:=</span>
      <span class="k">begin</span>
        <span class="n">simp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
        <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_le_succ</span> <span class="n">hja</span>
      <span class="kn">end</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">dif_pos</span> <span class="n">hia</span><span class="o">,</span> <span class="n">dif_pos</span> <span class="n">hia&#39;</span><span class="o">,</span> <span class="n">dif_neg</span> <span class="n">hja&#39;</span><span class="o">],</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">fin</span><span class="bp">.</span><span class="n">raise</span><span class="o">],</span>
      <span class="n">apply</span> <span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span><span class="o">,</span>
      <span class="n">simp</span><span class="o">},</span>
    <span class="o">{</span> <span class="k">have</span> <span class="n">hja&#39;</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">j</span><span class="bp">.</span><span class="n">succ</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="n">a</span><span class="bp">.</span><span class="n">raise</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">:=</span>
      <span class="k">begin</span>
        <span class="n">simp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
        <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_trans</span> <span class="n">hja</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_succ</span> <span class="n">j</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span>
      <span class="kn">end</span><span class="o">,</span>
      <span class="k">have</span> <span class="n">hia&#39;</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">((</span><span class="n">fin</span><span class="bp">.</span><span class="n">raise</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">raise</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">:=</span>
      <span class="k">begin</span>
        <span class="n">unfold</span> <span class="n">fin</span><span class="bp">.</span><span class="n">raise</span><span class="o">,</span> <span class="n">exact</span> <span class="n">hia</span>
      <span class="kn">end</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">dif_neg</span> <span class="n">hia</span><span class="o">,</span> <span class="n">dif_neg</span> <span class="n">hja&#39;</span><span class="o">,</span> <span class="n">dif_neg</span> <span class="n">hia&#39;</span><span class="o">]}}</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Nov 21 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148106009):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Do you mean it should be provable by <code>dec_trivial</code>?</p>

#### [ Simon Hudon (Nov 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148122480):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> <span class="user-mention" data-user-id="110596">@Rob Lewis</span> Did the problem turn out to be <code>mono</code>?</p>

#### [ Patrick Massot (Nov 21 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148122892):
<p><code>linarith</code> doesn't use <code>mono</code> so the bug in <code>linarith</code> had nothing to do with <code>mono</code> (and is now fixed). But I'm still disappointed I can't get <code>mono</code> to help here</p>

#### [ Patrick Massot (Nov 21 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148123052):
<p>You can try, what I posted right after pinging you is a MWE</p>

#### [ Patrick Massot (Nov 21 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148123091):
<p>search for "does nothing" in this thread</p>

#### [ Simon Hudon (Nov 21 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148124879):
<p>I wouldn't expect it to do anything in that case. What would you expect it to do?</p>

#### [ Patrick Massot (Nov 21 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148125029):
<p>I would expect it to close the goal</p>

#### [ Simon Hudon (Nov 21 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148128435):
<p>You mean using mixed transitivity? It doesn’t do that. What it does is identify a monotonic function on either side of a relation. &lt; is that relation in your case but it doesn’t have a monotonic function on both sides.</p>

#### [ Simon Hudon (Nov 21 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148128458):
<p>If you want, you can treat &lt; as the monotonic function and -&gt; as the relation.</p>

#### [ Simon Hudon (Nov 21 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148128569):
<p>To do that, you need to do <code>revert h</code> before mono.</p>

#### [ Patrick Massot (Nov 21 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131648):
<p>This is sad. We need something like <code>cc</code> for inequality, working together with <code>mono</code></p>

#### [ Simon Hudon (Nov 21 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131680):
<p>Maybe something like what I did for tfae would work for that</p>

#### [ Patrick Massot (Nov 21 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131689):
<p>Except <code>tfae</code> doesn't work <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Patrick Massot (Nov 21 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131747):
<p>The following is ridiculous but gives hope:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">≤</span> <span class="n">q</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;</span> <span class="o">:</span> <span class="n">q</span> <span class="bp">≤</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">≤</span> <span class="n">r</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">le_trans</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">swap</span><span class="o">,</span>
  <span class="n">tauto</span><span class="o">,</span>
  <span class="n">tauto</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Nov 21 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131762):
<p>This is the kind goal I hope some "<code>cc</code> for inequalities" would solve</p>

#### [ Simon Hudon (Nov 21 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131878):
<p>What is tricky for this kind of tactic is that one would expect it to work in the case of mixed transitivity which makes selecting a relation a bit more difficult. I could do it specifically for <code>&lt;</code> and <code>≤</code> to simplify things but it's a bit disappointing in terms of generality</p>

#### [ Simon Hudon (Nov 21 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148131995):
<p>But in the situations that you're showing, it seems like the kind of stuff <code>linarith</code> should handle</p>

#### [ Rob Lewis (Nov 21 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148135817):
<p>Patrick, can you elaborate on what you mean by "cc for inequalities"?</p>

#### [ Chris Hughes (Nov 21 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148135937):
<p>I think he more or less means solvable using linear order axioms, without any algebra.</p>

#### [ Chris Hughes (Nov 21 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148135954):
<p>But I think linarith does those.</p>

#### [ Rob Lewis (Nov 21 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148136093):
<p>Ah. Yeah, linarith does those. But I guess it requires some extra algebraic structure on the type that isn't always necessary.</p>

#### [ Chris Hughes (Nov 21 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148136290):
<p>And maybe preorder axioms and partial order axioms would be nice as well.</p>

#### [ Rob Lewis (Nov 21 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148136993):
<p>Indeed. A tactic for this kind of transitivity reasoning would be a nice project for someone who wants to learn about writing tactics. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Rob Lewis (Nov 21 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148136997):
<p>Note, I haven't really looked into <code>mono</code> yet, so I'm not sure how much overlap there is.</p>

#### [ Simon Hudon (Nov 21 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148137165):
<p>There isn't much overlap actually. To implement this tactic, tfae would be more helpful. It calculates the transitive closure of implication on the local assumptions.</p>

#### [ Simon Hudon (Nov 21 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148137182):
<p>You replace implication by a preorder and you'd get what Patrick is talking about with the additional difficulty of handling <code>&lt;</code> properly</p>

#### [ Rob Lewis (Nov 21 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148137301):
<p>Ah, sure. Sounds reasonable enough.</p>

#### [ Patrick Massot (Nov 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148140643):
<p>I'd love to try to understand how to adapt <code>tfae</code> here, but again I don't think this would be reasonable before we get a deterministic behavior from <code>tfae</code></p>

#### [ Kenny Lau (Nov 22 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148181673):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I see someone has figured out the function in mathlib</p>

#### [ Johan Commelin (Nov 22 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148187179):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Wait, which function in mathlib are you referring to?</p>

#### [ Kenny Lau (Nov 22 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148190141):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> <code>fin.succ_above</code></p>

#### [ Johan Commelin (Nov 22 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148191135):
<p>Aah, yes, I'm using that one. Was that answering a question of mine?</p>

#### [ Johan Commelin (Nov 22 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148191179):
<p>Or maybe you just think it is confusing notation? It probably is...</p>

#### [ Kenny Lau (Nov 22 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148191834):
<p>never mind, ignore me</p>

#### [ Scott Morrison (Nov 24 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148254707):
<p>More requests: are these reasonable to expect from <code>linarith</code>?</p>
<div class="codehilite"><pre><span></span>n m : ℕ,
h₁ : n &lt; m,
⊢ n + 1 ≤ m
</pre></div>


<p>and</p>
<div class="codehilite"><pre><span></span>n m l : ℕ,
a_left : n ≤ l,
a_right : l &lt; n + (m - n)
⊢ l &lt; m
</pre></div>


<p>and</p>
<div class="codehilite"><pre><span></span>a_left : n ≤ l,
a_right : l &lt; m
⊢ l &lt; n + (m - n)
</pre></div>

#### [ Kenny Lau (Nov 24 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148256879):
<blockquote>
<p>The following is ridiculous but gives hope:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">≤</span> <span class="n">q</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;</span> <span class="o">:</span> <span class="n">q</span> <span class="bp">≤</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">≤</span> <span class="n">r</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">le_trans</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">swap</span><span class="o">,</span>
  <span class="n">tauto</span><span class="o">,</span>
  <span class="n">tauto</span>
<span class="kn">end</span>
</pre></div>


<p>This is the kind of goal I hope some "<code>cc</code> for inequalities" would solve</p>
</blockquote>
<p>So like this?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">cc_inequality</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="bp">`</span><span class="o">[</span><span class="n">transitivity</span><span class="bp">;</span> <span class="n">tauto</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">≤</span> <span class="n">q</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;</span> <span class="o">:</span> <span class="n">q</span> <span class="bp">≤</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">≤</span> <span class="n">r</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cc_inequality</span>
</pre></div>

#### [ Johan Commelin (Nov 24 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148263754):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Your first question is <code>exact h1</code>, so I would hope that <code>linarith</code> could do it.  The second and third are nasty because they use nat-subtraction. I think we still need a <code>num_cast</code> tactic that would lift it to <code>int</code>, and then <code>linarith</code> could do the job.</p>

#### [ Andrew Ashworth (Nov 24 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148265222):
<p>Cooper will kill these, if you're willing to use another dependency</p>

#### [ Scott Morrison (Nov 24 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148265691):
<p>Am I allowed to import <code>cooper</code> into <code>data.nat.basic</code>? :-)</p>

#### [ Scott Morrison (Nov 24 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148265692):
<p>Thanks for the suggestion, I will try out cooper!</p>

#### [ Rob Lewis (Nov 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148270921):
<p><code>linarith</code> will not prove any of those. Think of it as a tactic for linear rational inequalities.  If a goal over <code>int</code> is still provable when you replace <code>int</code> with <code>rat</code>, it will still work. Inequalities over <code>nat</code> are cast to inequalities over <code>int</code>, with extra assumptions that all atoms are nonnegative. Applications of nat subtraction are treated as atoms.</p>

#### [ Rob Lewis (Nov 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148270931):
<p>The first one isn't true in a dense order. The second ones involve properties of nat subtraction beyond nonnegativity.</p>

#### [ Rob Lewis (Nov 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148270979):
<p><code>cooper</code> isn't in mathlib, it's in Seul's repository. Use it, of course, but incorporating it into mathlib is a bigger discussion.</p>

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148271514):
<p>Would it be possible to edit <code>linarith</code> so that it automatically knows that variables coerced from nat are nonnegative? Compare:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span><span class="n">a</span><span class="bp">≥</span><span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℚ</span><span class="o">)</span><span class="bp">/</span><span class="mi">4</span> <span class="bp">≤</span> <span class="o">(</span><span class="mi">4</span><span class="o">:</span><span class="n">ℚ</span><span class="o">)</span> <span class="bp">+</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">linarith</span> <span class="c1">--works</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℚ</span><span class="o">)</span><span class="bp">/</span><span class="mi">4</span> <span class="bp">≤</span> <span class="o">(</span><span class="mi">4</span><span class="o">:</span><span class="n">ℚ</span><span class="o">)</span> <span class="bp">+</span> <span class="err">↑</span><span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">linarith</span> <span class="c1">-- fails</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span><span class="n">a</span><span class="bp">≥</span><span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℚ</span><span class="o">)</span><span class="bp">/</span><span class="mi">4</span> <span class="bp">≤</span> <span class="o">(</span><span class="mi">4</span><span class="o">:</span><span class="n">ℚ</span><span class="o">)</span> <span class="bp">+</span> <span class="err">↑</span><span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">linarith</span> <span class="c1">-- even this fails</span>
</pre></div>

#### [ Rob Lewis (Nov 24 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148273249):
<p><code>linarith</code> isn't a smart tactic. It does one thing (linear rational arithmetic) very well, and by coincidence, sometimes it can do things with <code>nat</code> and <code>int</code>. In your second example, it doesn't know any connection between <code>a</code> and <code>↑a</code>, and why should it? Instead of a cast, that could be <code>abs</code>, or <code>square</code>, or any nonnegative function. In the very special case when it sees an inequality over <code>nat</code>, it will cast it to <code>int</code> and add the nonnegativity hypotheses. But it won't go digging through the input looking for things it can learn are nonnegative. That's a kind of preprocessing that can be done separately.</p>

#### [ Rob Lewis (Nov 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148273254):
<p>The third example is a little different. It sees the <code>a &gt;= 0</code> hypothesis, and casts it to <code>int</code>. But the overall problem is in <code>rat</code>.</p>

#### [ Rob Lewis (Nov 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148273298):
<p>In general, there's no well-defined type of the "overall problem," since you could have hypotheses over many different types.</p>

#### [ Rob Lewis (Nov 24 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148273305):
<p>It could try to guess what type to cast to, or it could cast to every type that appears. This wouldn't be so unreasonable.</p>

#### [ Bryan Gin-ge Chen (Nov 24 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith/near/148283001):
<p>Thanks for explaining! As always, there was a lot of complexity lurking here that I didn't appreciate.</p>


{% endraw %}
