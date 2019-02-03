---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01960nthmap.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [nth_map](https://leanprover-community.github.io/archive/113488general/01960nthmap.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (May 13 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509555):
<p>Do we have something like</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">nth_le_map</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span><span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">length</span> <span class="n">l</span><span class="o">)</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">nth_le</span> <span class="o">(</span><span class="n">map</span> <span class="n">f</span> <span class="n">l</span><span class="o">)</span> <span class="n">n</span> <span class="o">((</span><span class="n">length_map</span> <span class="n">f</span> <span class="n">l</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">H</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">nth_le</span> <span class="n">l</span> <span class="n">n</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>

#### [ Patrick Massot (May 13 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509560):
<p>It feels a bit weird to stick a proof in the middle of the statement</p>

#### [ Patrick Massot (May 13 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509561):
<p>Am I doing something wrong?</p>

#### [ Mario Carneiro (May 13 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509612):
<p>One approach I have used in the past is to have two proof arguments, but this makes rewriting produce proof obligations that look superfluous</p>

#### [ Patrick Massot (May 13 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509615):
<p>And I don't know how to prove it</p>

#### [ Mario Carneiro (May 13 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509620):
<p>i.e. you would prove <code>nth_le (map f l) n H1 = f (nth_le l n H2) </code></p>

#### [ Patrick Massot (May 13 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509621):
<p>You you mean adding <code>(H' : n &lt; length (map f l))</code>?</p>

#### [ Patrick Massot (May 13 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509651):
<p>ok</p>

#### [ Patrick Massot (May 13 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509663):
<p>I still don't know how to prove it though</p>

#### [ Patrick Massot (May 13 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509671):
<p>Why is this not in mathlib? It looks like it would be useful for many proofs</p>

#### [ Mario Carneiro (May 13 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509672):
<p>I'm asking the same question</p>

#### [ Mario Carneiro (May 13 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509674):
<p>I would start with <code>nth</code></p>

#### [ Mario Carneiro (May 13 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509675):
<p>since that avoids the proof argument stuff</p>

#### [ Patrick Massot (May 13 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509676):
<p>I also thought that</p>

#### [ Patrick Massot (May 13 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509677):
<p>But I couldn't even state it <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span></p>

#### [ Patrick Massot (May 13 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509716):
<p>Because <code>f</code> doesn't want an <code>option α</code></p>

#### [ Mario Carneiro (May 13 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509823):
<div class="codehilite"><pre><span></span>theorem nth_map (f : α → β) : ∀ l n, nth (map f l) n = (nth l n).map f
| []       n     := rfl
| (a :: l) 0     := rfl
| (a :: l) (n+1) := nth_map l n

theorem nth_le_map (f : α → β) {l n} (H1 H2) : nth_le (map f l) n H1 = f (nth_le l n H2) :=
option.some.inj $ by rw [← nth_le_nth, nth_map, nth_le_nth]; refl
</pre></div>

#### [ Mario Carneiro (May 13 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509824):
<p><code>option.map</code> takes <code>f : A -&gt; B</code> to <code>map f : option A -&gt; option B</code></p>

#### [ Patrick Massot (May 13 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509827):
<p><span class="emoji emoji-1f62e" title="open mouth">:open_mouth:</span></p>

#### [ Patrick Massot (May 13 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509881):
<p>I was clearly missing that <code>option.map</code> piece</p>

#### [ Patrick Massot (May 13 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509886):
<p>but probably not only that</p>

#### [ Mario Carneiro (May 13 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509887):
<p><code>option</code> is a functor</p>

#### [ Kenny Lau (May 13 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509889):
<p>is this proven in mathlib / Lean?</p>

#### [ Mario Carneiro (May 13 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509891):
<p>yes, because every monad is a functor</p>

#### [ Mario Carneiro (May 13 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509898):
<p>and <code>option</code> is like the very first monad you write</p>

#### [ Kenny Lau (May 13 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509900):
<p>you mean sentence</p>

#### [ Mario Carneiro (May 13 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509942):
<p>like when learning what monads are and examples, <code>option</code> is always the example</p>

#### [ Patrick Massot (May 13 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509946):
<p>Thank you very much Mario. I hope this will also be a good reference next time I'll hit this <code>option</code> stuff</p>

#### [ Patrick Massot (May 13 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509947):
<p>I still think you could put those two lemmas in mathlib</p>

#### [ Mario Carneiro (May 13 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126509993):
<p>I'm doing that now</p>

#### [ Mario Carneiro (May 13 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126510003):
<p>I definitely want more <code>nth</code> and <code>index_of</code> theorems, to make it easier to think of <code>list</code> as finitely supported functions on nat</p>

#### [ Patrick Massot (May 13 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126510056):
<p>Great</p>

#### [ Patrick Massot (May 13 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126510097):
<p>I was going after something like <code>reverse (range' a b) = map (lam x, ...) (range' a b)</code> and stuff like that</p>

#### [ Patrick Massot (May 13 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126510108):
<p>And was also thinking about defining <code>int_range k n</code> same as <code>range'</code> but <code>k</code> is an integer</p>

#### [ Patrick Massot (May 13 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126510154):
<p>and generalizing all the <code>range'</code> lemmas to this case</p>

#### [ Mario Carneiro (May 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nth_map/near/126512722):
<p>That makes sense. I guess you could define <code>range'</code> generalized to any semiring, although it doesn't have the "consecutivity" property except in <code>nat</code> and <code>int</code></p>


{% endraw %}
