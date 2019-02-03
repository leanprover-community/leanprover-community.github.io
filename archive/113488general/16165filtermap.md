---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16165filtermap.html
---

## Stream: [general](index.html)
### Topic: [filter map](16165filtermap.html)

---


{% raw %}
#### [ Patrick Massot (May 10 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126378246):
<p>Is this already somewhere in core or mathlib?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">filter_map_comm</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">J</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="n">J</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">J</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span><span class="o">:</span> <span class="n">list</span> <span class="n">I</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">P</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">filter</span> <span class="n">P</span> <span class="o">(</span><span class="n">map</span> <span class="n">f</span> <span class="n">r</span><span class="o">)</span> <span class="bp">=</span> <span class="n">map</span> <span class="n">f</span> <span class="o">(</span><span class="n">filter</span> <span class="o">(</span><span class="n">P</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">r</span> <span class="k">with</span> <span class="n">h</span> <span class="bp">_</span> <span class="n">IH</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">simp</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">by_cases</span> <span class="n">H</span> <span class="o">:</span> <span class="n">P</span> <span class="o">(</span><span class="n">f</span> <span class="n">h</span><span class="o">)</span> <span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">filter_cons_of_pos</span><span class="o">,</span> <span class="n">filter_cons_of_neg</span><span class="o">,</span> <span class="n">H</span><span class="o">,</span> <span class="n">IH</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (May 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379540):
<p>try:</p>
<div class="codehilite"><pre><span></span>theorem filter_map_eq_map (f : α → β) : filter_map (some ∘ f) = map f :=
theorem filter_map_eq_filter (p : α → Prop) [decidable_pred p] :
  filter_map (option.guard p) = filter p :=
theorem filter_map_filter_map (f : α → option β) (g : β → option γ) (l : list α) :
  filter_map g (filter_map f l) = filter_map (λ x, (f x).bind g) l :=
</pre></div>


<p>from <code>data.list.basic</code></p>

#### [ Patrick Massot (May 10 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379629):
<p>What do you mean? The lemma is not there but there may be a shorter proof using those results?</p>

#### [ Simon Hudon (May 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379663):
<p>Yes exactly. Sorry, I was overly concise</p>

#### [ Patrick Massot (May 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379737):
<p>It looks at least as complicated as what I already have</p>

#### [ Patrick Massot (May 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379748):
<p>And I don't want to frustrate Kenny by stealing a golfing challenge from him</p>

#### [ Simon Hudon (May 10 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379819):
<p>That's very considerate :)</p>

#### [ Patrick Massot (May 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379852):
<p>Actually I'd rather use Kenny (or anyone else) to help me fighting nat substraction</p>

#### [ Patrick Massot (May 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379859):
<p>For instance:</p>

#### [ Simon Hudon (May 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379865):
<p>I like the resulting proof because it avoids induction</p>

#### [ Patrick Massot (May 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379880):
<p><code>example (a b k : ℕ) : b + k - (a + k) = b - a </code></p>

#### [ Patrick Massot (May 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379934):
<p>What do you mean avoid induction? <code>map</code> and <code>filter</code> are defined inductively</p>

#### [ Patrick Massot (May 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379939):
<p>You can at best hide induction</p>

#### [ Patrick Massot (May 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379947):
<p>Note that both sides are zero is b is larger than a</p>

#### [ Patrick Massot (May 10 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379959):
<p>So it looks like a "false" result but this one is actually true</p>

#### [ Patrick Massot (May 10 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126379962):
<p>I think</p>

#### [ Patrick Massot (May 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380041):
<p>Do you have a solution with <code>filter_map</code>? Actually it could be useful to learn what <code>filter_map</code> is good for</p>

#### [ Simon Hudon (May 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380170):
<blockquote>
<p>What do you mean avoid induction? <code>map</code> and <code>filter</code> are defined inductively</p>
</blockquote>
<p>They're recursively defined. But yeah, you can never get around using induction / recursion directly or indirectly but I feel hiding induction produces nicer interfaces. The laws about <code>filter_map</code> seem like you can prove a lot about <code>filter</code> and <code>map</code> without induction.</p>

#### [ Simon Hudon (May 10 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380179):
<p>It's a generalization of both <code>map</code> and <code>filter</code>.</p>

#### [ Patrick Massot (May 10 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380248):
<p>I still don't see how it could help me here</p>

#### [ Reid Barton (May 10 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380518):
<blockquote>
<p><code>example (a b k : ℕ) : b + k - (a + k) = b - a </code></p>
</blockquote>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">k</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_add_right</span> <span class="n">b</span> <span class="n">k</span> <span class="n">a</span>
</pre></div>

#### [ Patrick Massot (May 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380569):
<p><span class="emoji emoji-1f632" title="astonished">:astonished:</span></p>

#### [ Simon Hudon (May 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380590):
<p>I think I overlooked a detail. I thought just doing a <code>rw</code> would work but here is what I get:</p>
<div class="codehilite"><pre><span></span>  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">filter_map_eq_map</span>
     <span class="o">,</span><span class="err">←</span> <span class="n">filter_map_eq_filter</span>
     <span class="o">,</span><span class="err">←</span> <span class="n">filter_map_eq_filter</span>
     <span class="o">,</span><span class="n">filter_map_filter_map</span>
     <span class="o">,</span><span class="n">filter_map_filter_map</span><span class="o">],</span>
  <span class="n">congr</span><span class="o">,</span> <span class="n">funext</span><span class="o">,</span>
<span class="c1">-- ⊢ option.bind ((some ∘ f) x) (option.guard P) = option.bind (option.guard (P ∘ f) x) (some ∘ f)</span>
</pre></div>


<p>That should be hard either, but it makes the proof longer than expected</p>

#### [ Patrick Massot (May 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380594):
<p>That's crazy</p>

#### [ Patrick Massot (May 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380596):
<p>That's also crazy</p>

#### [ Patrick Massot (May 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380599):
<p>Thanks Reid</p>

#### [ Patrick Massot (May 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126380617):
<p>I wasn't hoping for this to be in Lean core...</p>

#### [ Patrick Massot (May 10 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381158):
<p>I'm becoming better and better at proof obfuscation. If I ever need to read those proofs, I'll hate myself.</p>

#### [ Reid Barton (May 10 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381226):
<p>it's too hard to resist the golf</p>

#### [ Patrick Massot (May 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381282):
<p>Right now I'm staring at line saying <code>congr_n 1 ; funext ; simp only [nat.add_sub_cancel, nat.add_sub_add_right]</code></p>

#### [ Patrick Massot (May 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381295):
<p>I wrote two minutes ago</p>

#### [ Patrick Massot (May 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381297):
<p>And I already have no clue what it does</p>

#### [ Patrick Massot (May 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381299):
<p>Mario and Johannes will be so proud</p>

#### [ Patrick Massot (May 10 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381363):
<p>Because it's half the proof of some trivial statement, and trivial statement must have obfuscated proof according to mathlib style guide</p>

#### [ Patrick Massot (May 10 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381371):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">big</span><span class="bp">.</span><span class="n">shift</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">P</span><span class="o">]</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">big</span><span class="o">[(</span><span class="err">◆</span><span class="o">)</span><span class="bp">/</span><span class="n">nil</span><span class="o">]</span><span class="bp">_</span><span class="o">(</span><span class="n">i</span><span class="bp">=</span><span class="n">a</span><span class="bp">..</span><span class="n">b</span> <span class="bp">|</span> <span class="o">(</span><span class="n">P</span> <span class="n">i</span><span class="o">))</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="n">big</span><span class="o">[(</span><span class="err">◆</span><span class="o">)</span><span class="bp">/</span><span class="n">nil</span><span class="o">]</span><span class="bp">_</span><span class="o">(</span><span class="n">i</span><span class="bp">=</span><span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">k</span><span class="o">)</span><span class="bp">..</span><span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="n">k</span><span class="o">)</span> <span class="bp">|</span> <span class="o">(</span><span class="n">P</span> <span class="o">(</span><span class="n">i</span><span class="bp">-</span><span class="n">k</span><span class="o">)))</span> <span class="o">(</span><span class="n">F</span> <span class="o">(</span><span class="n">i</span><span class="bp">-</span><span class="n">k</span><span class="o">)))</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">range&#39;_add_map</span><span class="o">,</span> <span class="n">big</span><span class="bp">.</span><span class="n">map</span><span class="o">],</span>
  <span class="n">congr_n</span> <span class="mi">1</span> <span class="bp">;</span> <span class="n">funext</span> <span class="bp">;</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_cancel</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_add_right</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (May 10 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381380):
<p>(for instance <code>big[(◆)/nil]</code> could be a <code>\Sum</code> operator</p>

#### [ Kevin Buzzard (May 10 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381460):
<p>This is just the sort of stuff which I really needed last November and wasn't there</p>

#### [ Kevin Buzzard (May 10 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381471):
<p>I remember having to give up on a 1st year problem sheet question because I couldn't prove that sum from 1 to n was equal to sum from n to 1 :-)</p>

#### [ Kevin Buzzard (May 10 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381475):
<p>[at the time]</p>

#### [ Reid Barton (May 10 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381521):
<p>imagine where we'd be if Gauss had had a computer</p>

#### [ Kevin Buzzard (May 10 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381527):
<p>I don't even want to think about that</p>

#### [ Kevin Buzzard (May 10 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381534):
<p>how much time did Gauss and Euler waste working out examples etc</p>

#### [ Patrick Massot (May 10 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381541):
<p>They would have had computer aided waste of time instead</p>

#### [ Kevin Buzzard (May 10 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381556):
<p>Maybe they would have just played minecraft all day</p>

#### [ Kevin Buzzard (May 10 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381559):
<p>and we'd be worse off</p>

#### [ Patrick Massot (May 10 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381562):
<p>yep</p>

#### [ Patrick Massot (May 10 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126381571):
<p>or watched lol cats on youtube</p>

#### [ Sean Leather (May 11 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126402529):
<p>If they were functional programmers (esp. in Haskell), I think they would have enjoyed <a href="https://spl.smugmug.com/Humor/Lambdacats/" target="_blank" title="https://spl.smugmug.com/Humor/Lambdacats/">Lambdacats</a>.</p>

#### [ Moses Schönfinkel (May 11 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126404033):
<p>Hehe, we're slowly eroding formality of this forum :).</p>

#### [ Patrick Massot (May 11 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126404169):
<p>I think it was already pretty badly eroded</p>

#### [ Moses Schönfinkel (May 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126404210):
<p>I believe cat pictures are new tho.</p>

#### [ Moses Schönfinkel (May 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126404214):
<p>Dank memes next.</p>

#### [ Sean Leather (May 11 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20map/near/126405008):
<blockquote>
<p>Hehe, we're slowly eroding formality of this forum <span class="emoji emoji-1f603" title="smiley">:smiley:</span>.</p>
</blockquote>
<p>Given that theorem proving is a formal method, what does an eroded formal method look like? <span class="emoji emoji-1f914" title="thinking face">:thinking_face:</span></p>
<p>Ah ha! <span class="emoji emoji-1f4a1" title="light bulb">:light_bulb:</span> This must be why the name “lean” was chosen: the methodological mountain was so eroded, it couldn't stand up straight.</p>


{% endraw %}
