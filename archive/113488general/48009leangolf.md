---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48009leangolf.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lean golf](https://leanprover-community.github.io/archive/113488general/48009leangolf.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Feb 28 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123089630):
<p>Shortest proof of this?</p>
<div class="codehilite"><pre><span></span><span class="n">a</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">c</span> <span class="bp">∧</span> <span class="n">d</span> <span class="bp">∧</span> <span class="n">e</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">c</span> <span class="bp">∧</span> <span class="n">c</span> <span class="bp">∧</span> <span class="n">d</span> <span class="bp">∧</span> <span class="n">e</span>
</pre></div>

#### [ Sebastian Ullrich (Feb 28 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123089805):
<p>Let's start with the basics</p>
<div class="codehilite"><pre><span></span><span class="k">by</span> <span class="n">split</span><span class="bp">;</span><span class="n">intro</span><span class="bp">;</span><span class="n">simp</span><span class="bp">*</span>
</pre></div>

#### [ Sean Leather (Feb 28 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123090043):
<p>That's like a sledgehammer using sledgehammers to hit small nails. For some reason, I never think to try <code>simp *</code>.</p>

#### [ Sebastian Ullrich (Feb 28 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123090128):
<p>Well, I don't really need <code>*</code> here, but naming the hypothesis obviously is a golf no-go :P</p>

#### [ Sean Leather (Feb 28 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123090420):
<p>Is it? If the proof is short, I don't see why. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Scott Morrison (Feb 28 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123090434):
<p>I was happy to see <code>by tidy</code> works too. Maybe one day I'll get up the courage to PR it.</p>

#### [ Kevin Buzzard (Feb 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123109866):
<p>I wondered whether <code>by cc</code> would work -- but it doesn't. I still don't really know what to expect with cc but I think I've seen it prove other goals of this nature.</p>

#### [ Sean Leather (Mar 01 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123129844):
<p>I'm slowly learning how to use <code>simp *</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">list</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span>

<span class="kn">theorem</span> <span class="n">nth_of_map</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">option</span><span class="bp">.</span><span class="n">get_or_else</span> <span class="o">(</span><span class="n">nth</span> <span class="o">(</span><span class="n">map</span> <span class="n">f</span> <span class="n">l</span><span class="o">)</span> <span class="n">n</span><span class="o">)</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">option</span><span class="bp">.</span><span class="n">get_or_else</span> <span class="o">(</span><span class="n">nth</span> <span class="n">l</span> <span class="n">n</span><span class="o">)</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">l</span> <span class="n">generalizing</span> <span class="n">n</span><span class="bp">;</span> <span class="o">[</span><span class="n">skip</span><span class="o">,</span> <span class="n">cases</span> <span class="n">n</span><span class="o">]</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">get_or_else</span><span class="o">]</span>

<span class="kn">end</span> <span class="n">list</span>
</pre></div>

#### [ Johannes Hölzl (Mar 02 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123179941):
<p>I guess <code>cc</code> doesn't work as it currently doesn't handle idempotent laws (i.e. <code>c ∧ c</code>).</p>

#### [ Kevin Buzzard (Mar 13 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123658195):
<p>Curry:</p>

#### [ Kevin Buzzard (Mar 13 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123658197):
<p><code>example (P Q R : Prop) : (P ∧ Q → R) ↔ (P → (Q → R)) := sorry</code></p>

#### [ Kevin Buzzard (Mar 13 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123658245):
<p>Doing this one taught me something, although it was arguably not very useful</p>

#### [ Kevin Buzzard (Mar 13 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123658252):
<p>Actually it taught me 2 things, one being that bash shell is not very good at counting unicode characters</p>

#### [ Sean Leather (May 24 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127015438):
<p>I'm sure I've asked this before, but I don't remember the answer. Better/shorter way to do this?</p>
<div class="codehilite"><pre><span></span><span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span>
</pre></div>


<p>Note that <code>simp</code> by itself doesn't work.</p>

#### [ Johannes Hölzl (May 24 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127016063):
<p><code>simp {contextual:=tt}</code> should do it.</p>

#### [ Sean Leather (May 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127016150):
<p>Yep, that did it. Thanks!</p>

#### [ Sean Leather (May 24 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017262):
<p><code>simp</code> doesn't solve this. Is there a theorem I can use with <code>simp</code> to solve it?</p>
<div class="codehilite"><pre><span></span><span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="bp">⟩</span> <span class="err">∈</span> <span class="n">l</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a₁</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">==</span> <span class="n">b₁</span> <span class="bp">∨</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="bp">⟩</span> <span class="err">∈</span> <span class="n">l</span>
</pre></div>

#### [ Johannes Hölzl (May 24 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017535):
<p>I guess you have <code>⟨a₁, b₁⟩ ∈ l</code>?</p>

#### [ Johannes Hölzl (May 24 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017583):
<p>But I also don't see how to solve it with the simplifier.</p>

#### [ Sean Leather (May 24 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017645):
<p>Oh wait, I'm stupid. Let me actually think. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Kevin Buzzard (May 24 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017653):
<p>Do you CS people know how to parse that sort of statement?</p>

#### [ Kevin Buzzard (May 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017685):
<p>I look at it (away from Lean) and have no idea about the relative priorities of and, or and iff. Is this just all some standard convention that you CS people know and we maths people just avoid by adding brackets?</p>

#### [ Kevin Buzzard (May 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017716):
<p>I mean -- I know I can go and check them -- my question is whether there are uniform standards or whether Lean made some random choice and you find different choices in other systems.</p>

#### [ Kevin Buzzard (May 24 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017741):
<p>obviously I can guess the answer in this situation from the context, but in the past I have written statements without brackets and then later on gone "oh crap, that doesn't mean what I wanted it to mean at all"</p>

#### [ Gabriel Ebner (May 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017785):
<p>The precedence is pretty standard.  In most (all?) programming languages as well as logic, and binds more tightly than or.  C doesn't have iff, so its hard to compare.</p>

#### [ Sean Leather (May 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017792):
<p>The “usual conventions:” <a href="https://groups.google.com/d/msg/lean-user/lbFwVL21Az4/1erXpLqBAwAJ" target="_blank" title="https://groups.google.com/d/msg/lean-user/lbFwVL21Az4/1erXpLqBAwAJ">https://groups.google.com/d/msg/lean-user/lbFwVL21Az4/1erXpLqBAwAJ</a></p>

#### [ Gabriel Ebner (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017838):
<p>Excerpt from a proof theory textbook lying around here (Troelstra &amp; Schwichtenberg):</p>
<blockquote>
<p>Notation (Saving on parentheses) In writing formulas we save on parentheses by assuming that ∀, ∃,  ¬ bind more strongly than ∧, ∨, and that in turn ∨, ∧ bind more strongly than →, ↔. [...]</p>
</blockquote>

#### [ Gabriel Ebner (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017848):
<p>I guess you will find similar boilerplate in most texts that deal with logical formulas.</p>

#### [ Sean Leather (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017854):
<p>One that I struggled with was <code>=</code> vs. <code>↔</code>, but now I'm used to it.</p>

#### [ Kevin Buzzard (May 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018118):
<blockquote>
<p>I guess you will find similar boilerplate in most texts that deal with logical formulas.</p>
</blockquote>
<p>I follow a text which deals with logical formulas in my introduction to proof class and I can find no mention of binding preferences anywhere!</p>

#### [ Kevin Buzzard (May 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018119):
<p>But I do see a lot of brackets :-)</p>

#### [ Kevin Buzzard (May 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018159):
<p>I conclude that the guy who wrote it (who is in the office a few doors down from me) was also a mathematician who had no idea of standard CS conventions :-)</p>

#### [ Gabriel Ebner (May 24 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018330):
<p>There is one confusing difference between proof theory and CS though: the precedence of ∀, ∃ is different.</p>
<div class="codehilite"><pre><span></span>  ∃x P(x) → Q     means:

  (∃x P(x)) → Q       for everyone in my research group
  ∃x (P(x) → Q)       in Lean, Coq, etc.
</pre></div>

#### [ Chris Hughes (May 24 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018489):
<p><code>(∃x P(x)) → Q</code> seems like really stupid precedence, since you would usually write <code>∀ x , P x → Q</code> instead of that.</p>

#### [ Sean Leather (May 24 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018550):
<p>Interesting. Pierce (Types and Programming Languages) uses explicit bracketing : <code>{∃x, P(x)}</code></p>

#### [ Gabriel Ebner (May 24 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018815):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> The same precedence is also used for ∀: <code>(∀x P(x)) → Q</code> vs. <code>∀x (P(x) → Q)</code>, which is just as confusing.</p>

#### [ Kevin Buzzard (May 24 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127019269):
<p>In fact it was exactly this forall point which I was referring to in my earlier "that doesn't mean what I wanted it to mean" comment</p>

#### [ Sean Leather (Aug 20 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132455368):
<p>Shortest proof of this?</p>
<div class="codehilite"><pre><span></span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="n">p</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span>
<span class="n">q</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span>
<span class="err">⊢</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span>
</pre></div>

#### [ Sean Leather (Aug 20 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132455921):
<p>This is what I came up with:</p>
<div class="codehilite"><pre><span></span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_of_le_and_ne</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_of_lt_succ</span> <span class="n">p</span><span class="o">)</span> <span class="n">q</span>
</pre></div>

#### [ Kenny Lau (Aug 20 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132456748):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cases</span> <span class="n">p</span><span class="bp">;</span> <span class="o">[</span><span class="n">cc</span><span class="o">,</span> <span class="n">assumption</span><span class="o">]</span>
</pre></div>

#### [ Johan Commelin (Aug 20 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132457185):
<p>I'm not on a Lean machine atm, but could <code>cooper</code> or <code>tidy</code> kill this one?</p>

#### [ Kenny Lau (Aug 21 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132529548):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="n">T</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">S</span> <span class="err">⊆</span> <span class="n">T</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">T</span><span class="bp">.</span><span class="n">card</span> <span class="bp">≤</span> <span class="n">S</span><span class="bp">.</span><span class="n">card</span><span class="o">)</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">=</span> <span class="n">T</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">disjoint</span> <span class="n">S</span> <span class="o">(</span><span class="n">T</span> <span class="err">\</span> <span class="n">S</span><span class="o">),</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">disjoint</span><span class="o">],</span>
<span class="k">have</span> <span class="n">H4</span> <span class="o">:</span> <span class="bp">_</span><span class="o">,</span> <span class="k">from</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card_disjoint_union</span> <span class="n">H3</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H5</span> <span class="o">:</span> <span class="n">S</span> <span class="err">∪</span> <span class="n">T</span> <span class="err">\</span> <span class="n">S</span> <span class="bp">=</span> <span class="n">T</span><span class="o">,</span> <span class="k">from</span> <span class="n">finset</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
  <span class="bp">⟨λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_union</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_of_subset</span> <span class="n">H1</span><span class="o">)</span> <span class="o">(</span><span class="n">and</span><span class="bp">.</span><span class="n">left</span> <span class="err">∘</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_sdiff</span><span class="bp">.</span><span class="mi">1</span><span class="o">),</span>
  <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_cases</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_union_left</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H&#39;</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_union_right</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_sdiff</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">H</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H6</span> <span class="o">:</span> <span class="n">S</span><span class="bp">.</span><span class="n">card</span> <span class="bp">=</span> <span class="n">T</span><span class="bp">.</span><span class="n">card</span><span class="o">,</span> <span class="k">from</span> <span class="n">le_antisymm</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">card_le_of_subset</span> <span class="n">H1</span><span class="o">)</span> <span class="n">H2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H7</span> <span class="o">:</span> <span class="n">T</span> <span class="err">\</span> <span class="n">S</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">,</span> <span class="k">from</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card_eq_zero</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span>
  <span class="n">nat</span><span class="bp">.</span><span class="n">add_left_cancel</span> <span class="err">$</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="n">H5</span><span class="o">,</span> <span class="n">H6</span><span class="o">]</span> <span class="n">at</span> <span class="n">H4</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H8</span> <span class="o">:</span> <span class="n">T</span> <span class="err">⊆</span> <span class="n">S</span><span class="o">,</span> <span class="k">from</span> <span class="n">finset</span><span class="bp">.</span><span class="n">subset_iff</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H&#39;</span><span class="o">,</span>
  <span class="n">finset</span><span class="bp">.</span><span class="n">ne_empty_of_mem</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_sdiff</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">H</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">H7</span><span class="o">,</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span> <span class="n">H1</span> <span class="n">H8</span>
</pre></div>

#### [ Kenny Lau (Aug 21 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132529552):
<p>is there a shorter proof?</p>

#### [ Mario Carneiro (Aug 21 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132531216):
<div class="codehilite"><pre><span></span>example (H1 : S ⊆ T) (H2 : T.card ≤ S.card) : S = T :=
finset.eq_of_veq $ multiset.eq_of_le_of_card_le (finset.val_le_iff.2 H1) H2
</pre></div>

#### [ Mario Carneiro (Aug 21 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132531244):
<p>this should be in mathlib though</p>

#### [ Kenny Lau (Aug 21 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132531591):
<p>ah it's in multiset lol</p>

#### [ Chris Hughes (Aug 21 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132531934):
<p>Pretty sure it's there for finsets. I remember seeing it.</p>

#### [ Chris Hughes (Aug 21 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132532050):
<p><code>finset.eq_of_subset_of_card_le</code></p>

#### [ Kenny Lau (Aug 21 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132532088):
<p>genius</p>

#### [ Kenny Lau (Aug 21 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132533414):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">surjective</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">eq_univ_iff_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">finset</span><span class="bp">.</span><span class="n">eq_of_subset_of_card_le</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">subset_univ</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="n">le_of_eq</span> <span class="err">$</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card_image_of_injective</span> <span class="bp">_</span> <span class="n">H</span><span class="o">),</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_image</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">H</span> <span class="n">y</span><span class="o">)</span> <span class="k">in</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Aug 21 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132533415):
<p>how about this?</p>

#### [ Chris Hughes (Aug 21 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132533791):
<p>Already in mathlib. <code>fintype.injective_iff_surjective</code> Your proof  is shorter though</p>

#### [ Kenny Lau (Aug 21 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534113):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">something</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">surjective</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">eq_univ_iff_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">finset</span><span class="bp">.</span><span class="n">eq_of_subset_of_card_le</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">subset_univ</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">(</span><span class="n">le_of_eq</span> <span class="err">$</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card_image_of_injective</span> <span class="bp">_</span> <span class="n">H</span><span class="o">),</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_image</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">H</span> <span class="n">y</span><span class="o">)</span> <span class="k">in</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">something2</span> <span class="o">[</span><span class="n">integral_domain</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">r</span> <span class="o">,</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">something</span> <span class="n">α</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">r</span><span class="o">,</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="o">(</span><span class="n">H&#39;</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">s</span> <span class="bp">*</span> <span class="n">x</span><span class="o">),</span> <span class="n">eq_of_sub_eq_zero</span> <span class="err">$</span> <span class="n">or</span><span class="bp">.</span><span class="n">resolve_right</span>
    <span class="o">(</span><span class="n">eq_zero_or_eq_zero_of_mul_eq_zero</span> <span class="err">$</span> <span class="k">show</span> <span class="o">(</span><span class="n">r</span> <span class="bp">-</span> <span class="n">s</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">sub_mul</span><span class="o">,</span> <span class="n">H&#39;</span><span class="o">,</span> <span class="n">sub_self</span><span class="o">])</span> <span class="n">H</span><span class="o">)</span> <span class="mi">1</span>

<span class="n">noncomputable</span> <span class="kn">instance</span> <span class="n">field_of_fintype_of_integral_domain</span> <span class="o">[</span><span class="n">integral_domain</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">field</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">if</span> <span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="mi">0</span> <span class="k">else</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="err">$</span> <span class="n">something2</span> <span class="n">α</span> <span class="n">x</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">mul_inv_cancel</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">H</span><span class="o">,</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">has_inv</span><span class="bp">.</span><span class="n">inv</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="n">dif_neg</span> <span class="n">H</span><span class="o">,</span> <span class="n">mul_comm</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">something2</span> <span class="n">α</span> <span class="n">x</span> <span class="n">H</span><span class="o">)],</span>
  <span class="n">inv_mul_cancel</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">H</span><span class="o">,</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">has_inv</span><span class="bp">.</span><span class="n">inv</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="n">dif_neg</span> <span class="n">H</span><span class="o">,</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">something2</span> <span class="n">α</span> <span class="n">x</span> <span class="n">H</span><span class="o">)],</span>
  <span class="bp">..</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span> <span class="o">:</span> <span class="n">integral_domain</span> <span class="n">α</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Aug 21 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534118):
<blockquote>
<p>Already in mathlib. <code>fintype.injective_iff_surjective</code> Your proof  is shorter though</p>
</blockquote>
<p>well I didn't prove the other direction</p>

#### [ Chris Hughes (Aug 21 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534147):
<p>Don't make that an instance or we have a cycle.</p>

#### [ Kenny Lau (Aug 21 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534161):
<p>also I can't find <code>injective_iff_surjective</code></p>

#### [ Chris Hughes (Aug 21 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534228):
<p>It's quite new. Last month or so.</p>

#### [ Kevin Buzzard (Aug 22 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601084):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">=</span> <span class="o">(</span><span class="n">b</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Too embarrassed to post my effort. <span class="user-mention" data-user-id="110044">@Chris Hughes</span> this came up with that countp v count thing. The proof isn't refl even though the predicates are whatever they call it -- eta equivalent or something.</p>

#### [ Patrick Massot (Aug 22 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601170):
<p><code>by cc</code></p>

#### [ Mario Carneiro (Aug 22 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601195):
<p><code>propext eq_comm</code></p>

#### [ Patrick Massot (Aug 22 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601255):
<p>Mine is shorter! <span class="emoji emoji-1f3c6" title="trophy">:trophy:</span></p>

#### [ Patrick Massot (Aug 22 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601261):
<p>I know, yours is probably faster</p>

#### [ Mario Carneiro (Aug 22 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601274):
<p>Mine is smaller with <code>pp.all</code> :)</p>

#### [ Kevin Buzzard (Aug 22 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132603490):
<p>Here's the context this came up in:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="kn">open</span> <span class="n">multiset</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">count</span> <span class="n">a</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">card</span> <span class="o">(</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">countp_eq_card_filter</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">count</span><span class="o">,</span>
  <span class="n">congr</span><span class="o">,</span>
  <span class="n">funext</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>I was surprised this wasn't there, but perhaps the issue is that you can filter on <code>λ b, b = a</code> or <code>λ b, a = b</code></p>

#### [ Kenny Lau (Aug 22 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132603835):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="kn">open</span> <span class="n">multiset</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">count</span> <span class="n">a</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">card</span> <span class="o">(</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">convert</span> <span class="n">countp_eq_card_filter</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">funext</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">cc</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Aug 22 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132603896):
<p><code>by simp [count, countp_eq_card_filter, eq_comm]; congr</code></p>

#### [ Kenny Lau (Aug 22 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132604013):
<p><code>by convert countp_eq_card_filter s; simp [eq_comm]</code></p>

#### [ Kevin Buzzard (Aug 23 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132604473):
<p>If I hover over <code>convert</code> in VS Code I get "convert &lt;- expr &lt;error while executing interactive.param_desc: don't know how to pretty print lean.parser.small_nat&gt;  Similar to <code>refine</code> but generates equality proof obligations for every discrepancy between the goal and the type of the rule"</p>

#### [ Mario Carneiro (Aug 23 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132604528):
<p>that's because <code>small_nat</code> doesn't have a description - compare with <code>congr'</code></p>

#### [ Sean Leather (Sep 12 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/133795530):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="mi">1</span> <span class="bp">+</span> <span class="n">max</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:=</span> <span class="bp">_</span>
</pre></div>

#### [ Reid Barton (Sep 12 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/133796099):
<p>not very creative, but <code>by rw [add_comm, nat.lt_succ_iff]; apply le_max_left</code></p>

#### [ Kenny Lau (Oct 18 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136055689):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">t1_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_open</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="bp">-</span><span class="n">s</span><span class="o">)</span><span class="bp">;</span> <span class="n">exact</span>
<span class="o">(</span><span class="n">is_closed_compl_iff</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">set</span><span class="bp">.</span><span class="n">bUnion_of_singleton</span> <span class="o">(</span><span class="bp">-</span><span class="n">s</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">is_closed_Union</span>
  <span class="bp">⟨</span><span class="n">set</span><span class="bp">.</span><span class="n">fintype_of_finset</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="bp">-</span><span class="n">s</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_filter</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_univ</span><span class="o">,</span> <span class="n">true_and</span><span class="o">])</span><span class="bp">⟩</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">is_closed_singleton</span><span class="o">))</span>
</pre></div>

#### [ Mario Carneiro (Oct 18 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136059466):
<p>I think this theorem could also be stated as <code>t = \top</code></p>

#### [ Mario Carneiro (Oct 18 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136060001):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">t2_space&#39;</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">t2</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">u</span> <span class="n">v</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">u</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">v</span> <span class="bp">→</span>
   <span class="n">x</span> <span class="err">∈</span> <span class="n">u</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">v</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span> <span class="err">∈</span> <span class="n">u</span> <span class="bp">∧</span> <span class="n">z</span> <span class="err">∈</span> <span class="n">v</span><span class="o">)</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>
<span class="n">include</span> <span class="n">t</span>

<span class="n">def</span> <span class="n">Hausdorffification</span><span class="bp">.</span><span class="n">setoid</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">t2_space&#39;</span> <span class="o">(</span><span class="n">quotient</span> <span class="n">s</span><span class="o">)],</span> <span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">r</span> <span class="n">α</span> <span class="n">s</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="bp">_</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">,</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="bp">@</span><span class="n">H</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H1</span> <span class="n">H2</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">,</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="bp">@</span><span class="n">H1</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">H2</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">)</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">Hausdorffification</span><span class="bp">.</span><span class="n">setoid</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">Hausdorffification</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="n">quotient</span> <span class="o">(</span><span class="n">Hausdorffification</span><span class="bp">.</span><span class="n">setoid</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">Hausdorffification</span><span class="bp">.</span><span class="n">t2_space&#39;</span> <span class="o">:</span>
  <span class="n">t2_space&#39;</span> <span class="o">(</span><span class="n">Hausdorffification</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">t2</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">x</span> <span class="n">y</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">quot</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">ht2</span><span class="o">,</span> <span class="k">begin</span>
      <span class="n">resetI</span><span class="o">,</span>
      <span class="k">let</span> <span class="n">f</span> <span class="o">:</span> <span class="n">Hausdorffification</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">quotient</span> <span class="n">r</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">refine</span> <span class="bp">λ</span> <span class="n">e</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on&#39;</span> <span class="n">e</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span><span class="o">,</span>
        <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">H</span><span class="o">,</span> <span class="n">apply</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span><span class="o">,</span> <span class="n">apply</span> <span class="n">H</span> <span class="o">},</span>
      <span class="k">have</span> <span class="n">hf</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">intros</span> <span class="n">s</span> <span class="n">hs</span><span class="o">,</span>
        <span class="n">change</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="bp">_</span><span class="o">),</span>
        <span class="n">rw</span> <span class="err">←</span> <span class="n">set</span><span class="bp">.</span><span class="n">preimage_comp</span><span class="o">,</span>
        <span class="n">exact</span> <span class="n">hs</span> <span class="o">},</span>
      <span class="n">refine</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">exact</span> <span class="o">(</span><span class="n">t2_space&#39;</span><span class="bp">.</span><span class="n">t2</span> <span class="bp">_</span> <span class="bp">_</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">u</span> <span class="n">v</span> <span class="n">h1</span> <span class="n">h2</span> <span class="n">h3</span> <span class="n">h4</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span>
      <span class="n">rcases</span> <span class="n">H</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">hf</span> <span class="bp">_</span> <span class="n">h1</span><span class="o">)</span> <span class="o">(</span><span class="n">hf</span> <span class="bp">_</span> <span class="n">h2</span><span class="o">)</span> <span class="n">h3</span> <span class="n">h4</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">z</span><span class="o">,</span> <span class="n">zu</span><span class="o">,</span> <span class="n">zv</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="n">exact</span> <span class="bp">⟨</span><span class="n">fz</span><span class="o">,</span> <span class="n">zu</span><span class="o">,</span> <span class="n">zv</span><span class="bp">⟩</span>
    <span class="kn">end</span> <span class="o">}</span>
</pre></div>

#### [ Johannes Hölzl (Oct 18 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136060806):
<p>By the way: this T2 space definition is equal to <code>not (disjoint (nhds x) (nhds y)) -&gt; x = y</code>.</p>

#### [ Mario Carneiro (Oct 18 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136061226):
<p>not constructively</p>

#### [ Mario Carneiro (Oct 18 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136061506):
<p>(oops, wrong thread, this should be in <a href="#narrow/stream/116395-maths/subject/Hausdorffification/near/136026443" title="#narrow/stream/116395-maths/subject/Hausdorffification/near/136026443">Hausdorffification</a>)</p>


{% endraw %}
