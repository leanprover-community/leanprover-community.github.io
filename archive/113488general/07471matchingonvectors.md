---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07471matchingonvectors.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [matching on vectors](https://leanprover-community.github.io/archive/113488general/07471matchingonvectors.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Floris van Doorn (Oct 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136140175):
<p>Is there a library of vectors, defined inductively?</p>
<div class="codehilite"><pre><span></span>inductive dvector (α : Type u) : ℕ → Type u
| nil {} : dvector 0
| cons : ∀{n}, α → dvector n → dvector (n+1)
</pre></div>


<p>Alternatively, can I use the equation compiler to pattern match on <code>vector</code> in the library in a nice way? I want something resembling the definitions in the following code:</p>
<div class="codehilite"><pre><span></span>universe variables u v w
inductive dvector (α : Type u) : ℕ → Type u
| nil {} : dvector 0
| cons : ∀{n}, α → dvector n → dvector (n+1)

local notation h :: t  := dvector.cons h t
local notation `[` l:(foldr `, ` (h t, dvector.cons h t) dvector.nil `]`) := l

namespace dvector
variables {α : Type u} {β : Type v} {γ : Type w} {n : ℕ}

@[simp] protected def map (f : α → β) : ∀{n : ℕ}, dvector α n → dvector β n
| _ []      := []
| _ (x::xs) := f x :: map xs

@[simp] protected def map_id : ∀{n : ℕ} (xs : dvector α n), xs.map (λx, x) = xs
| _ []      := rfl
| _ (x::xs) := by dsimp; simp*

@[simp] protected def map_congr {f g : α → β} (h : ∀x, f x = g x) :
  ∀{n : ℕ} (xs : dvector α n), xs.map f = xs.map g
| _ []      := rfl
| _ (x::xs) := by dsimp; simp*

@[simp] protected def map_map (g : β → γ) (f : α → β): ∀{n : ℕ} (xs : dvector α n),
  (xs.map f).map g = xs.map (λx, g (f x))
  | _ []      := rfl
  | _ (x::xs) := by dsimp; simp*

end dvector
</pre></div>

#### [ Floris van Doorn (Oct 19 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136140303):
<p>(and yes, <em>these</em> operations are probably already defined for <code>vector</code>, but I want to define new operations on vectors using pattern matching, and I kind-of don't want to do it on lists first)</p>

#### [ Reid Barton (Oct 19 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136140731):
<p><code>vector.cons</code> already has the <code>pattern</code> attribute; have you tried using it in the equation compiler?</p>

#### [ Floris van Doorn (Oct 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136141401):
<p>What does the <code>pattern</code> attribute do?<br>
Yes, I tried matching on vectors using <code>vector.nil</code> and <code>vector.cons</code>, but something like this doesn't work:</p>
<div class="codehilite"><pre><span></span>protected def vector.my_map {α : Type u} {β : Type v} {γ : Type w} (f : α → β) :
 ∀{n : ℕ}, vector α n → vector β n
| _ vector.nil         := vector.nil
| _ (vector.cons x xs) := vector.cons (f x) (vector.my_map xs)
</pre></div>

#### [ Reid Barton (Oct 20 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136141888):
<p>It lets you use the definition in a pattern context, I'm not too sure of the details of how it works</p>

#### [ Reid Barton (Oct 20 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136142036):
<p>Yeah, it seems not to work, unfortunate...</p>

#### [ Reid Barton (Oct 20 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136142212):
<p>It seems like maybe the problem is the way that Lean moved the proof field of <code>vector.nil</code> into a <code>theorem</code></p>

#### [ Reid Barton (Oct 20 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136142217):
<p>I wonder whether there is some option to disable that?</p>

#### [ Reid Barton (Oct 20 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136142222):
<p>though one would like it to not matter, since it is a Prop anyways</p>

#### [ Mario Carneiro (Oct 20 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136143993):
<p><span class="user-mention" data-user-id="111080">@Floris van Doorn</span> There should be a custom recursor for this</p>

#### [ Mario Carneiro (Oct 20 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136143995):
<p>that's usually the way we show alternate inductive patterns for types</p>

#### [ Reid Barton (Oct 20 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136145108):
<p>But can you use that with the equation compiler?</p>

#### [ Johan Commelin (Oct 20 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136152692):
<p><span class="user-mention" data-user-id="111080">@Floris van Doorn</span> In <code>kbb</code> we experimented with code like this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">vector</span><span class="bp">.</span><span class="n">mk</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">pr</span> <span class="o">:</span> <span class="n">l</span><span class="bp">.</span><span class="n">length</span> <span class="bp">=</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">vector</span> <span class="n">α</span> <span class="n">n</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">l</span><span class="o">,</span> <span class="n">pr</span><span class="bp">⟩</span>

<span class="kn">notation</span> <span class="bp">`!</span><span class="o">[</span><span class="bp">`</span> <span class="n">l</span><span class="o">:(</span><span class="n">foldr</span> <span class="bp">`</span><span class="o">,</span> <span class="bp">`</span> <span class="o">(</span><span class="n">h</span> <span class="n">t</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">h</span> <span class="n">t</span><span class="o">)</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="bp">`</span><span class="o">]</span><span class="bp">`</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">vector</span><span class="bp">.</span><span class="n">mk</span> <span class="n">l</span> <span class="n">rfl</span>

<span class="n">def</span> <span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">fast_matrix</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span> <span class="n">vector</span> <span class="o">(</span><span class="n">vector</span> <span class="n">α</span> <span class="n">n</span><span class="o">)</span> <span class="n">m</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">fast_matrix</span> <span class="mi">2</span> <span class="mi">3</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="bp">!</span><span class="o">[</span><span class="bp">!</span><span class="o">[</span> <span class="mi">1</span> <span class="o">,</span> <span class="mi">1</span><span class="o">,</span>  <span class="mi">5</span> <span class="o">],</span>
  <span class="bp">!</span><span class="o">[</span> <span class="mi">0</span> <span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="bp">-</span><span class="mi">2</span> <span class="o">]]</span>
</pre></div>


<p>It is not exactly what you want, but maybe a bit related.</p>

#### [ Floris van Doorn (Oct 21 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187187):
<p>Yes, a custom recursor for <code>vector</code> would be nice. That doesn't affect pattern matching though, right?</p>

#### [ Floris van Doorn (Oct 21 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187264):
<p>What is the reason to define vectors (and fin) this way, instead of the inductive family with the nicer pattern matching? Is it because the virtual machine can then use its representation of lists (and nat) for efficient computation?</p>

#### [ Floris van Doorn (Oct 21 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187318):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> that is indeed nice notation. You can get the same effect if you define the notation using <code>vector.nil</code> and <code>vector.cons</code>, right?</p>

#### [ Mario Carneiro (Oct 21 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187497):
<p>Yes, both of these types are implemented this way for efficient computation</p>

#### [ Mario Carneiro (Oct 21 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187550):
<p>The downside of custom recursors is of course that they don't hook in to the equation compiler, so you don't get the nice pattern matching</p>

#### [ Mario Carneiro (Oct 21 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187558):
<p>An alternative is to define the alternate inductive structure as <code>vector2</code> or something, and prove an equiv</p>

#### [ Mario Carneiro (Oct 21 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187561):
<p>If you want these, <code>fin2</code> and <code>vector2</code> are defined in <code>dioph.lean</code></p>

#### [ Floris van Doorn (Oct 21 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187742):
<p>Oh, so they do exist, just not in the <code>data</code> folder. In <code>dioph</code> I only find <code>vector3</code> though. Where is <code>vector2</code>?</p>

#### [ Mario Carneiro (Oct 21 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136190101):
<p>oh,  I thought I renamed it</p>

#### [ Mario Carneiro (Oct 21 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136190144):
<p><code>vector2</code> used to be just <code>fin n -&gt; A</code></p>

#### [ Mario Carneiro (Oct 21 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136190149):
<p>or maybe it was <code>fin2 n -&gt; A</code></p>


{% endraw %}
