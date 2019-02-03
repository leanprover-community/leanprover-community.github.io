---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27671optionrecelim.html
---

## Stream: [general](index.html)
### Topic: [option.rec.elim](27671optionrecelim.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 21 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053317):
<p>I don't want to prove the goal here, I want to prove an intermediate lemma: <code>∀ x : γ, option.map f (k x) = j x</code>. </p>
<p>So what's going on is <code>f : α → β</code> and <code>g : β → α</code> with <code>f ∘ g = id</code>. Given a function <code>j : γ → option β</code> I want to lift it to <code>k :  γ → option α</code> using <code>g</code> and then prove that applying <code>f</code> (or more precisely <code>option.map f</code>) to <code>k</code> gets you back to <code>j</code>. All this is happening in the middle of a tactic proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span>
 <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">k</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
<span class="c1">--    match (j x) with</span>
<span class="c1">--    | none := none</span>
<span class="c1">--    | some b := some (g b)</span>
<span class="c1">--    end,</span>
<span class="c1">-- here written out in term mode</span>
    <span class="n">option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">j</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">none</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">some</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span><span class="o">)),</span>
  <span class="k">have</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="o">(</span><span class="n">k</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">j</span> <span class="n">x</span><span class="o">,</span> <span class="c1">-- what I actually want</span>
    <span class="c1">-- this should be trivial by casing on j x</span>
    <span class="c1">-- if j x is none then by definition k x is none  so f (k x) is none</span>
    <span class="c1">-- if j x is some b then map f (k x) = some (f (g b)) = some b</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">cases</span> <span class="o">(</span><span class="n">j</span> <span class="n">x</span><span class="o">),</span>
    <span class="c1">-- first goal now option.map f (k x) = none</span>
    <span class="c1">-- but assumption that j x = none nowhere to be seen</span>
    <span class="n">repeat</span> <span class="o">{</span><span class="n">sorry</span><span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>I want to do a <code>cases</code> on <code>j x</code> but I can't seem to do it directly. How do I eliminate <code>j</code>?</p>

#### [ Kenny Lau (Jul 21 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053396):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span>
  <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
  <span class="k">let</span> <span class="n">k</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">j</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">none</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">some</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span><span class="o">))</span> <span class="k">in</span>
  <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="o">(</span><span class="n">k</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">j</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>

<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jul 21 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053404):
<p>thanks -- had not occurred to me to use let in the statement. This is a rather more elegant way of asking the question.</p>

#### [ Kenny Lau (Jul 21 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053488):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span>
  <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
  <span class="k">let</span> <span class="n">k</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">j</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">none</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">some</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span><span class="o">))</span> <span class="k">in</span>
  <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="o">(</span><span class="n">k</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">j</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">k</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">k</span><span class="o">],</span>
  <span class="n">cases</span> <span class="n">j</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">refl</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">option</span><span class="bp">.</span><span class="n">map</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">bind</span><span class="o">,</span> <span class="n">H</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jul 21 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053550):
<p><code>dsimp [k]</code> does the substitution. That's what I was missing. Thanks a lot Kenny!</p>

#### [ Kevin Buzzard (Jul 21 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053683):
<p>In my actual use case I end up with a term involving <code>id_rhs</code>. I'd never heard of this! It's defined in core lean as <code>abbreviation id_rhs (α : Sort u) (a : α) : α := a</code>. I've never heard of <code>abbreviation</code> either!</p>

#### [ Kenny Lau (Jul 21 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053701):
<blockquote>
<p>In my actual use case I end up with a term involving <code>id_rhs</code>.</p>
</blockquote>
<p>consequence of using too many tactics</p>

#### [ Kenny Lau (Jul 21 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053703):
<p>don't use any tactic in the definition of anything</p>

#### [ Chris Hughes (Jul 21 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053712):
<p>You could even do this</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span>
  <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
  <span class="k">let</span> <span class="n">k</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">do</span> <span class="n">y</span> <span class="err">←</span> <span class="o">(</span><span class="n">j</span> <span class="n">x</span><span class="o">),</span> <span class="n">return</span> <span class="o">(</span><span class="n">g</span> <span class="n">y</span><span class="o">)</span> <span class="k">in</span>
  <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="o">(</span><span class="n">k</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">j</span> <span class="n">x</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Jul 21 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053725):
<p>says the tacticmaster</p>

#### [ Chris Hughes (Jul 21 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053909):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span>
  <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="o">(</span><span class="n">do</span> <span class="n">y</span> <span class="err">←</span> <span class="o">(</span><span class="n">j</span> <span class="n">x</span><span class="o">),</span> <span class="n">return</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">y</span><span class="o">)))</span> <span class="bp">=</span> <span class="n">j</span> <span class="n">x</span> <span class="o">:=</span>
 <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">]</span>
</pre></div>

#### [ Chris Hughes (Jul 21 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130053958):
<blockquote>
<p>In my actual use case I end up with a term involving <code>id_rhs</code>. I'd never heard of this! It's defined in core lean as <code>abbreviation id_rhs (α : Sort u) (a : α) : α := a</code>. I've never heard of <code>abbreviation</code> either!</p>
</blockquote>
<p>I think abbreviation is more or less the same as reducible</p>

#### [ Kevin Buzzard (Jul 21 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130054096):
<p><em>boggle</em> <code>option.map.none'</code> is what I want to use to finish my base case, but alpha and beta have to be in the same universe and this is exactly the situation I'm not in :-)</p>

#### [ Kevin Buzzard (Jul 21 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130054156):
<p>First few lines of <code>data/option.lean</code> in mathlib: </p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">option</span>
<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
</pre></div>


<p>and then things like <code>@[simp] theorem map_none' {f : α → β} : option.map f none = none := rfl</code>. Why are alpha and beta in the same universe?</p>

#### [ Kevin Buzzard (Jul 21 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130054283):
<p>I will have to use the non-API <code>refl</code> :-)</p>

#### [ Kevin Buzzard (Jul 21 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059145):
<p>This is still no good in my use case -- I want to do <code>cases (j x)</code> and in the case <code>some val</code> I would like to keep track of the fact that <code>j x = some val</code> because I will need to know this later. Am I somehow doing the wrong thing entirely, or is there a trick I'm missing?</p>

#### [ Kevin Buzzard (Jul 21 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059416):
<p>Maybe I can refactor exactly what I want out as some awful ugly auxiliary lemma</p>

#### [ Kevin Buzzard (Jul 21 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059477):
<p>I am supposed to be spending the weekend doing continuous valuations, and all I am doing is slowly proving that some definition doesn't depend on which universe I use :-/ I am just trusting that Mario is right when he says I need to make the type of Gamma the same as the type of R. My fear is that if I don't go through this pain now then I'll go through worse pain later.</p>

#### [ Chris Hughes (Jul 21 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059671):
<blockquote>
<p>This is still no good in my use case -- I want to do <code>cases (j x)</code> and in the case <code>some val</code> I would like to keep track of the fact that <code>j x = some val</code> because I will need to know this later. Am I somehow doing the wrong thing entirely, or is there a trick I'm missing?</p>
</blockquote>
<p>try <code>destruct (j x)</code></p>

#### [ Mario Carneiro (Jul 21 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059771):
<blockquote>
<p>and then things like @[simp] theorem map_none' {f : α → β} : option.map f none = none := rfl. Why are alpha and beta in the same universe?</p>
</blockquote>
<p>OMG! No wonder that thing never works</p>

#### [ Kenny Lau (Jul 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059824):
<p>lol</p>

#### [ Mario Carneiro (Jul 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059846):
<p>This is why I make a habit of avoiding explicit universes whenever possible</p>

#### [ Kevin Buzzard (Jul 21 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059975):
<p><code>destruct (j x)</code> <span class="user-mention" data-user-id="110044">@Chris Hughes</span> this is <em>exactly</em> what I needed! This just saved me a huge refactoring pain! Thanks a lot! Even though I could see my lemma was unprovable I kept going, because I could see I could reduce it to exactly the hypothesis which wasn't in the context :-) I was worried I was wasting my time but using destruct instead gave me exactly what I needed. Wow, who needs <code>cases</code>!</p>

#### [ Kevin Buzzard (Jul 21 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130059998):
<blockquote>
<p>OMG! No wonder that thing never works</p>
</blockquote>
<p>If you hadn't told me to be universe polymorphic I'd never have spotted this :-) Thanks also to <span class="user-mention" data-user-id="112680">@Johan Commelin</span> -- your "come on, it's just a glorified axiom of infinity" was what persuaded me to go back to <code>Type u</code> -- that and Mario saying that sticking to <code>Type</code> was futile anyway.</p>
<p>I am still kind-of fearing the discussion I'll one day have with a serious ZFC-ist who will be horrified that I am assuming the existence of universes when teaching my students undergraduate level maths. This is perfectoid spaces stuff but still -- Scholze's section 4 implies it can all be done in ZFC, and I'm not doing it in ZFC. Perhaps I should try and understand better what Mario was saying about all this a week or two ago.</p>

#### [ Kenny Lau (Jul 21 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060201):
<p>how do you do category without universes?</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060667):
<p>You aren't <em>using</em> universes so much as playing fast and loose with them. It <em>can</em> all be made precise and ZFC like, you just aren't bothering</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060668):
<p>that's what you should tell the ZFC-ist</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060710):
<p>you would certainly be in good company in doing so</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060854):
<p>If you want an equality proof in your <code>cases</code>, you can use <code>cases h : e</code> instead of just <code>cases e</code></p>

#### [ Mario Carneiro (Jul 21 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130060862):
<p>I think <code>destruct</code> is just a longer way to say <code>cases</code></p>

#### [ Kevin Buzzard (Jul 21 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061105):
<blockquote>
<p>If you want an equality proof in your <code>cases</code>, you can use <code>cases h : e</code> instead of just <code>cases e</code></p>
</blockquote>
<p>Yes it sounds like this would have done as well. I've seen <code>cases e with ...</code> but I hadn't realised how to name the hypothesis (or I had seen it before and forgotten).</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061153):
<p>and if that doesn't work you can also split the generalization and cases steps by using <code>generalize h : e = x</code> first and then <code>cases x</code></p>

#### [ Kevin Buzzard (Jul 21 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061355):
<blockquote>
<p>how do you do category without universes?</p>
</blockquote>
<p>So you don't prove general theorems about categories, you prove results about the categories which you care about. For example I'm a number theorist so I might have a representation <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>ρ</mi><mo>:</mo><mi>G</mi><mo>→</mo><mi>G</mi><mi>L</mi><mo>(</mo><mi>n</mi><mo separator="true">,</mo><mi>k</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\rho : G\to GL(n,k)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">ρ</span><span class="mrel">:</span><span class="mord mathit">G</span><span class="mrel">→</span><span class="mord mathit">G</span><span class="mord mathit">L</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03148em;">k</span><span class="mclose">)</span></span></span></span> and I might want to take its universal deformation. I might <em>say</em> "now consider the category whose objects are local rings <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> with an identification of the residue field with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03148em;">k</span></span></span></span>, such that these rings are projective limits of Artin local rings, and consider the functor from this category to the category of sets sending <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> to the set of lifts of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>ρ</mi></mrow><annotation encoding="application/x-tex">\rho</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">ρ</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mover accent="true"><mrow><mi>ρ</mi></mrow><mo>~</mo></mover><mo>:</mo><mi>G</mi><mo>→</mo><mi>G</mi><mi>L</mi><mo>(</mo><mi>n</mi><mo separator="true">,</mo><mi>R</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\tilde{\rho} : G \to GL(n,R)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord accent"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.6678599999999999em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord"><span class="mord mathit">ρ</span></span></span><span style="top:-3.35em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.16668em;"><span>~</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.19444em;"></span></span></span></span><span class="mrel">:</span><span class="mord mathit">G</span><span class="mrel">→</span><span class="mord mathit">G</span><span class="mord mathit">L</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mclose">)</span></span></span></span> which lift <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>ρ</mi></mrow><annotation encoding="application/x-tex">\rho</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">ρ</span></span></span></span>; then under certain finiteness assumptions on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi></mrow><annotation encoding="application/x-tex">G</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">G</span></span></span></span> this functor is representable by some pair <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mrow><mi>u</mi><mi>n</mi><mi>i</mi><mi>v</mi></mrow></msup><mo separator="true">,</mo><msup><mi>ρ</mi><mrow><mi>u</mi><mi>n</mi><mi>i</mi><mi>v</mi></mrow></msup></mrow><annotation encoding="application/x-tex">R^{univ},\rho^{univ}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.824664em;"></span><span class="strut bottom" style="height:1.019104em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.824664em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">u</span><span class="mord mathit mtight">n</span><span class="mord mathit mtight">i</span><span class="mord mathit mtight" style="margin-right:0.03588em;">v</span></span></span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit">ρ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.824664em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">u</span><span class="mord mathit mtight">n</span><span class="mord mathit mtight">i</span><span class="mord mathit mtight" style="margin-right:0.03588em;">v</span></span></span></span></span></span></span></span></span></span></span></span>. Now consider the following elements of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mrow><mi>u</mi><mi>n</mi><mi>i</mi><mi>v</mi></mrow></msup></mrow><annotation encoding="application/x-tex">R^{univ}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.824664em;"></span><span class="strut bottom" style="height:0.824664em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.824664em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">u</span><span class="mord mathit mtight">n</span><span class="mord mathit mtight">i</span><span class="mord mathit mtight" style="margin-right:0.03588em;">v</span></span></span></span></span></span></span></span></span></span></span></span>... . But when the ZFCist challenges me I say "aah there's a trick. I can prove that given any object <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> of this category I can replace it with a subring <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> with cardinality at most <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi><mo>(</mo><mi>R</mi><mo separator="true">,</mo><mi>k</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\kappa(R,k)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">κ</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03148em;">k</span><span class="mclose">)</span></span></span></span> for some explicit cardinal <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span> such that anything interesting happening happens already in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> (all this can be made rigorous but this is not the place to do it), so we can just consider the category of rings <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>R</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">R'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> with cardinality at most <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span> and this is equivalent to a <em>small</em> category which is a set, and I can reformulate the statement I want purely as a statement about this latter set, so I didn't use universes after all".</p>

#### [ Kevin Buzzard (Jul 21 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061400):
<p>And in the past I have linked to explicit places in the stacks project and in work of Scholze, where explicit arguments of this nature are given, always of this form ("we only need to consider things of size 2^2^2^(max(stuff we're looking at right now)), so we're all OK").</p>

#### [ Kevin Buzzard (Jul 21 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061401):
<p>So that's how an actual working mathematician does categories without universes</p>

#### [ Kevin Buzzard (Jul 21 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061450):
<p>I have no idea what the category theorist do and I'm not sure I care. Probably some work in ZFC and some don't.</p>

#### [ Kevin Buzzard (Jul 21 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130061453):
<p>All I know is that the universes showing up in the category theory stuff which me and my number theory colleagues use can all be dealt with in this way.</p>

#### [ Kevin Buzzard (Jul 21 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130062024):
<blockquote>
<p>If you want an equality proof in your <code>cases</code>, you can use <code>cases h : e</code> instead of just <code>cases e</code></p>
</blockquote>
<p><code>e</code> is a term here. <code>cases (h : e)</code> doesn't typecheck (and indeed makes no sense). <code>cases h : e</code> does work but now I look at it it looks pretty weird.</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130062147):
<p>it's meant to be suggestive of the <code>h : e = x</code> hypothesis you get</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130062155):
<p>it looks better in <code>generalize</code>, but in <code>cases</code> it doesn't make sense to have a <code>= x</code> there</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option.rec.elim/near/130062208):
<p>By the way, in tactic documentation <code>e</code> is often used as a placeholder for a term or <code>e</code>xpression, while <code>x</code> is a variable</p>


{% endraw %}
