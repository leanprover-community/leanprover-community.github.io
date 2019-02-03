---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35647heqagain.html
---

## Stream: [general](index.html)
### Topic: [heq again](35647heqagain.html)

---


{% raw %}
#### [ Reid Barton (Sep 10 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673026):
<p>Hmm, I wasn't expecting this to work.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">types_eq_of_heq</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">==</span> <span class="n">b</span><span class="o">),</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">β</span>
<span class="bp">|</span> <span class="n">α</span> <span class="n">a</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">heq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Sep 10 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673064):
<p>why not?</p>

#### [ Kenny Lau (Sep 10 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673078):
<p>casing on <code>h</code> makes sure that the types are equal and the arguments are equal</p>

#### [ Reid Barton (Sep 10 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673143):
<p>Mostly because I haven't seen this fact in core or mathlib, so I guess I assumed it was not provable.</p>

#### [ Reid Barton (Sep 10 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673150):
<p>Now I have a followup question about <code>congr</code>.</p>

#### [ Reid Barton (Sep 10 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673156):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="kn">section</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">α&#39;</span> <span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">hα</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">F</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">hβ</span> <span class="o">:</span> <span class="n">F</span> <span class="n">β</span> <span class="bp">=</span> <span class="n">F</span> <span class="n">β&#39;</span><span class="o">)</span>
<span class="kn">parameters</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">==</span> <span class="n">f&#39;</span><span class="o">)</span>
<span class="n">include</span> <span class="n">hα</span> <span class="n">hβ</span> <span class="n">h</span>

<span class="n">def</span> <span class="n">fns</span> <span class="o">:=</span> <span class="err">Σ&#39;</span> <span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">F</span><span class="o">,</span> <span class="n">X</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">→</span> <span class="n">Y</span><span class="bp">.</span><span class="mi">1</span>
<span class="n">def</span> <span class="n">g</span> <span class="o">:</span> <span class="n">fns</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="n">F</span> <span class="n">α</span><span class="o">,</span> <span class="n">α</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">F</span> <span class="n">β</span><span class="o">,</span> <span class="n">β</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">f</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">g&#39;</span> <span class="o">:</span> <span class="n">fns</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="n">F</span> <span class="n">α&#39;</span><span class="o">,</span> <span class="n">α&#39;</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">F</span> <span class="n">β&#39;</span><span class="o">,</span> <span class="n">β&#39;</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">f&#39;</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">e</span> <span class="o">:</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">g</span><span class="o">,</span> <span class="n">g&#39;</span><span class="o">],</span>
  <span class="c">/-</span><span class="cm"> ⊢ ⟨⟨F α, _⟩, ⟨⟨F β, _⟩, f⟩⟩ = ⟨⟨F α&#39;, _⟩, ⟨⟨F β&#39;, _⟩, f&#39;⟩⟩ -/</span>
  <span class="c">/-</span><span class="cm"> How to proceed? My solution: -/</span>
  <span class="n">congr&#39;</span> <span class="mi">1</span><span class="o">,</span> <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">hα</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">congr&#39;</span> <span class="mi">1</span><span class="o">,</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">hα</span> <span class="o">},</span> <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">hβ</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">],</span>
<span class="kn">end</span>

<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673185):
<p>are you going to livestream?</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673186):
<p><code>type_eq_of_heq</code></p>

#### [ Reid Barton (Sep 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673196):
<p>I'm annoyed about this <code>{ rw hα }</code> thing. The goal there is</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">F</span><span class="o">}),</span> <span class="n">F</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Y</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">F</span><span class="o">}),</span> <span class="n">F</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">Y</span><span class="bp">.</span><span class="n">val</span>
</pre></div>


<p>which I think is trying to say that when I do the second <code>congr'</code>, the types of the two sides are equal.</p>

#### [ Reid Barton (Sep 10 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673243):
<p>Wow, my grep skills failed</p>

#### [ Reid Barton (Sep 10 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673266):
<p>If I put <code>{ admit }</code> there, the rest of the proof seems to go through fine. So couldn't <code>congr'</code> deduce that the types are equal after the fact, using <code>type_eq_of_heq</code>?</p>

#### [ Reid Barton (Sep 10 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673394):
<p>Here's a dumber example.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">a</span><span class="o">)</span> <span class="bp">==</span> <span class="o">(</span><span class="n">b</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">congr</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>There are four goals, <code>⊢ α = β</code> twice and <code>⊢ a == b</code> twice. But I can get the former from the latter.</p>

#### [ Reid Barton (Sep 10 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673520):
<p>Or a nicer presentation</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">α&#39;</span> <span class="n">β</span> <span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">a&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">b&#39;</span> <span class="o">:</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">==</span> <span class="o">(</span><span class="n">a&#39;</span><span class="o">,</span> <span class="n">b&#39;</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Sep 10 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673525):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="kn">section</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">α&#39;</span> <span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">hα</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">F</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">hβ</span> <span class="o">:</span> <span class="n">F</span> <span class="n">β</span> <span class="bp">=</span> <span class="n">F</span> <span class="n">β&#39;</span><span class="o">)</span>
<span class="kn">parameters</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">==</span> <span class="n">f&#39;</span><span class="o">)</span>
<span class="n">include</span> <span class="n">hα</span> <span class="n">hβ</span> <span class="n">h</span>

<span class="n">def</span> <span class="n">fns</span> <span class="o">:=</span> <span class="err">Σ&#39;</span> <span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">F</span><span class="o">,</span> <span class="n">X</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">→</span> <span class="n">Y</span><span class="bp">.</span><span class="mi">1</span>
<span class="n">def</span> <span class="n">g</span> <span class="o">:</span> <span class="n">fns</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="n">F</span> <span class="n">α</span><span class="o">,</span> <span class="n">α</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">F</span> <span class="n">β</span><span class="o">,</span> <span class="n">β</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">f</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">g&#39;</span> <span class="o">:</span> <span class="n">fns</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="n">F</span> <span class="n">α&#39;</span><span class="o">,</span> <span class="n">α&#39;</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">F</span> <span class="n">β&#39;</span><span class="o">,</span> <span class="n">β&#39;</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">f&#39;</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">e</span> <span class="o">:</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="n">only</span> <span class="o">[</span><span class="n">g</span><span class="o">,</span> <span class="n">g&#39;</span><span class="o">],</span>
  <span class="n">congr</span><span class="bp">;</span> <span class="n">try</span> <span class="o">{</span><span class="n">assumption</span><span class="o">},</span>
  <span class="n">ext</span> <span class="n">Y</span><span class="o">,</span> <span class="n">rw</span> <span class="n">hα</span>
<span class="kn">end</span>

<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (Sep 10 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673613):
<p>The <code>ext Y, rw hα</code> part is still there, though. That's the only part I care about because it seems unnecessary.<br>
In my real use case, I have three of them and they are bigger</p>

#### [ Reid Barton (Sep 10 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673768):
<p>Does <code>set_option trace.congr_lemma true</code> do anything?</p>

#### [ Reid Barton (Sep 10 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133673872):
<p>Kenny, I was thinking I would try this evening US eastern time today, maybe a bit late for you</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674237):
<p>That's a pretty messy goal. I would clean it up by hand as follows:</p>
<div class="codehilite"><pre><span></span>begin
  let G := λ A B (f : A → B) h h&#39;, (⟨⟨A, h⟩, ⟨B, h&#39;⟩, f⟩ : fns),
  suffices : ∀ {f f&#39; h₁ h₂ h₃ h₄}, f == f&#39; →
    G (F α) (F β) f h₁ h₂ = G (F α&#39;) (F β&#39;) f&#39; h₃ h₄, exact this h,
  rw [hα, hβ], intros, congr&#39;, apply eq_of_heq a
end
</pre></div>

#### [ Mario Carneiro (Sep 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674250):
<p>I would avoid having type equalities and heqs in the hypotheses to begin with</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674301):
<p><code>congr</code> is clearly dropping the ball here. There are lots of superfluous goals being generated</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674319):
<p>But usually you don't want to deduce a type equality from a heq; rather you want to assume the type equality and prove a regular equality dependent on it</p>

#### [ Kenny Lau (Sep 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674335):
<p>is there any way to prove this goal?</p>

#### [ Kenny Lau (Sep 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674338):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="kn">section</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">α&#39;</span> <span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">hα</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">F</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">hβ</span> <span class="o">:</span> <span class="n">F</span> <span class="n">β</span> <span class="bp">=</span> <span class="n">F</span> <span class="n">β&#39;</span><span class="o">)</span>
<span class="kn">parameters</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">F</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">==</span> <span class="n">f&#39;</span><span class="o">)</span>
<span class="n">include</span> <span class="n">hα</span> <span class="n">hβ</span> <span class="n">h</span>

<span class="n">def</span> <span class="n">fns</span> <span class="o">:=</span> <span class="err">Σ&#39;</span> <span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">F</span><span class="o">,</span> <span class="n">X</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">→</span> <span class="n">Y</span><span class="bp">.</span><span class="mi">1</span>
<span class="n">def</span> <span class="n">g</span> <span class="o">:</span> <span class="n">fns</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="n">F</span> <span class="n">α</span><span class="o">,</span> <span class="n">α</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">F</span> <span class="n">β</span><span class="o">,</span> <span class="n">β</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">f</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">g&#39;</span> <span class="o">:</span> <span class="n">fns</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="n">F</span> <span class="n">α&#39;</span><span class="o">,</span> <span class="n">α&#39;</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">F</span> <span class="n">β&#39;</span><span class="o">,</span> <span class="n">β&#39;</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">f&#39;</span><span class="bp">⟩</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">proofs</span> <span class="n">true</span>
<span class="kn">theorem</span> <span class="n">e</span> <span class="o">:</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g&#39;</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">fapply</span> <span class="n">psigma</span><span class="bp">.</span><span class="n">eq</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="n">hα</span> <span class="o">},</span>
  <span class="n">fapply</span> <span class="n">psigma</span><span class="bp">.</span><span class="n">eq</span><span class="o">,</span>
  <span class="o">{</span> <span class="c">/-</span><span class="cm"> (eq.rec_on (subtype.eq hα) (g.snd)).fst = (g&#39;.snd).fst -/</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (Sep 10 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674402):
<p>Well how about the following modification to <code>congr</code>. After each single layer of <code>congr</code>, try filling each of the new goals by applying <code>exact type_eq_of_heq ?m_i</code> where <code>?m_i</code> is the metavariable of each other goal.</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674429):
<p>That's not what you want though. You will have to deduce those type equalities anyway in order to prove the heq</p>

#### [ Reid Barton (Sep 10 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674434):
<p>But I didn't!</p>

#### [ Reid Barton (Sep 10 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674447):
<p>I happen to have the heq lying around, and where I proved it, the type equalities were obvious</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674498):
<p>You satisfied the type equality proof by <code>assumption</code></p>

#### [ Reid Barton (Sep 10 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674522):
<p>Which type equality proof?</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674533):
<p><code>hα</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674581):
<p>and <code>hβ</code> later in the proof</p>

#### [ Reid Barton (Sep 10 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674591):
<p>Right, but then there is an inner proof obligation I have to take care of, the one I solve using <code>{ rw hα }</code></p>

#### [ Reid Barton (Sep 10 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674615):
<p>Let me put up my real code</p>

#### [ Mario Carneiro (Sep 10 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674626):
<p>you have to solve that anyway</p>

#### [ Reid Barton (Sep 10 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674682):
<p>No, it follows from being able to solve the rest of the goals</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674706):
<p>how?</p>

#### [ Reid Barton (Sep 10 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674714):
<p>By <code>type_eq_of_heq</code>. Right?</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674717):
<p>applied to what?</p>

#### [ Reid Barton (Sep 10 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674730):
<p>Isn't it the same thing as this?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">α&#39;</span> <span class="n">β</span> <span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">a&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">b&#39;</span> <span class="o">:</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">==</span> <span class="n">a&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">==</span> <span class="n">b&#39;</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">==</span> <span class="o">(</span><span class="n">a&#39;</span><span class="o">,</span> <span class="n">b&#39;</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">congr</span><span class="o">,</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">type_eq_of_heq</span> <span class="n">ha</span> <span class="o">},</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">type_eq_of_heq</span> <span class="n">hb</span> <span class="o">},</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">ha</span> <span class="o">},</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">hb</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Sep 10 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674845):
<p>sure, but this is an unrealistic goal. Where are you going to get those heqs without a type equality?</p>

#### [ Reid Barton (Sep 10 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674859):
<p>so in my real code it happens here <a href="https://gist.github.com/rwbarton/dfb90b2552f09b51798bb52af9948d48#file-filtered-lean-L249" target="_blank" title="https://gist.github.com/rwbarton/dfb90b2552f09b51798bb52af9948d48#file-filtered-lean-L249">https://gist.github.com/rwbarton/dfb90b2552f09b51798bb52af9948d48#file-filtered-lean-L249</a></p>

#### [ Reid Barton (Sep 10 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133674928):
<p>S is the image of a functor F : I -&gt; C considered as a subgraph, defined here <a href="https://gist.github.com/rwbarton/dfb90b2552f09b51798bb52af9948d48#file-filtered-lean-L87" target="_blank" title="https://gist.github.com/rwbarton/dfb90b2552f09b51798bb52af9948d48#file-filtered-lean-L87">https://gist.github.com/rwbarton/dfb90b2552f09b51798bb52af9948d48#file-filtered-lean-L87</a></p>

#### [ Mario Carneiro (Sep 10 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675006):
<p>can you MWE the state just before the <code>rintro</code>?</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675033):
<p>or maybe just after</p>

#### [ Reid Barton (Sep 10 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675129):
<p>It should be more or less what I pasted originally.<br>
Note <code>hg : functor.map F ((⟨i', ⟨j', g⟩⟩.snd).snd) == f</code>, which came from the definition of <code>S</code></p>

#### [ Reid Barton (Sep 10 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675183):
<p>Corresponding to my original <code>(h : f == f')</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675193):
<p>I want to catch the state before the type equalities enter the context</p>

#### [ Reid Barton (Sep 10 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675269):
<p>Ah, so you mean <code>hi', hj'</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675288):
<p>ideally you should be able to match on <code>hi', hj', hg</code> and save all the mess</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675304):
<p>don't match on <code>⟨X, i, rfl⟩, ⟨Y, j, rfl⟩</code>, just do <code>⟨X, _⟩, ⟨Y, _⟩</code></p>

#### [ Reid Barton (Sep 10 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675399):
<p>Hmm, I will try that</p>

#### [ Reid Barton (Sep 10 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675614):
<p>Meanwhile I updated the gist with a version which is not M, but should be a WE</p>

#### [ Reid Barton (Sep 10 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675723):
<p>Oh, there is a trick in <code>F ijg.1 = X ∧ F ijg.2.1 = Y ∧ ...</code>. That is not just <code>X</code>, but <code>X.val</code></p>

#### [ Reid Barton (Sep 10 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675726):
<p>because of my representation of a subgraph, which I now infinitely regret</p>

#### [ Reid Barton (Sep 10 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675824):
<p>I have a subgraph as (1) a subset of the vertices, (2) for each pair of vertices in that set (as a subtype), a subset of the edges between them</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133675941):
<p>works for me:</p>
<div class="codehilite"><pre><span></span>    rintro ⟨⟨X, _⟩, ⟨Y, _⟩, ⟨f, ⟨i, j, g⟩, ⟨⟩, ⟨⟩, ⟨⟩⟩⟩,
    exact ⟨⟨i, j, g⟩, rfl⟩,
</pre></div>

#### [ Mario Carneiro (Sep 10 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676015):
<p>using <code>rfl</code> instead of <code>⟨⟩</code> calls <code>subst</code> instead of <code>cases</code>, and <code>subst</code> is not sufficiently aggressive wrt definitionally unfolding one side to a variable</p>

#### [ Reid Barton (Sep 10 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676023):
<p>Ahh</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676103):
<p>I would suggest, if you are okay with the added verbosity, that you use an inductive type to define your hom sets instead of ands of eqs and heqs</p>

#### [ Reid Barton (Sep 10 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676111):
<p>I see</p>
<div class="codehilite"><pre><span></span><span class="n">rfl</span> <span class="o">:</span> <span class="err">⇑</span><span class="n">F</span> <span class="o">(</span><span class="bp">⟨</span><span class="n">i&#39;</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">j&#39;</span><span class="o">,</span> <span class="n">g</span><span class="bp">⟩⟩.</span><span class="n">fst</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="bp">⟨</span><span class="n">X</span><span class="o">,</span> <span class="n">b_fst_property</span><span class="bp">⟩</span><span class="o">,</span>
</pre></div>

#### [ Mario Carneiro (Sep 10 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676128):
<p>it names the variable <code>rfl</code> before substing, I think</p>

#### [ Reid Barton (Sep 10 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676134):
<p>Looks that way.</p>

#### [ Reid Barton (Sep 10 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676219):
<p>that's a whole lot better, thanks!</p>

#### [ Reid Barton (Sep 10 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676236):
<p>You mean, in the definition of S?</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676240):
<p>yes</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676274):
<p>it's up to you, you can use tricks like this to match on it either way</p>

#### [ Reid Barton (Sep 10 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676290):
<p>oh, I could replace the whole <code>λ X Y, {f | ∃ (ijg : Σ (i j : I), i ⟶ j), F ijg.1 = X ∧ F ijg.2.1 = Y ∧ F.map ijg.2.2 == f}</code> with an inductive type I guess</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676299):
<p>right</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676371):
<p>it would give nicer equations, but if this is a one-off it's probably not worth it</p>

#### [ Reid Barton (Sep 10 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676380):
<p>and elsewhere I have similar constructions, like the union of a family of subgraphs</p>

#### [ Reid Barton (Sep 10 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676387):
<p>Yeah, I'm not sure I will need any of these constructions more than once, inside the associated proof</p>

#### [ Reid Barton (Sep 10 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676399):
<p>But a good technique to keep in mind</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676456):
<p>oh, looks like you don't even need to match on <code>ijg</code> in that proof</p>

#### [ Reid Barton (Sep 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676522):
<p>Yep</p>

#### [ Reid Barton (Sep 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676543):
<p>I think I know what happened here</p>

#### [ Reid Barton (Sep 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676558):
<p>I started without the <code>F ijg.1 = X ∧ F ijg.2.1 = Y ∧ </code> part</p>

#### [ Reid Barton (Sep 10 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676605):
<p>in the definition of S. And then I realized that wasn't going to work</p>

#### [ Reid Barton (Sep 10 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676623):
<p>but I think I had already written the <code>⟨X, i, rfl⟩, ⟨Y, j, rfl⟩</code> patterns</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676760):
<p>yeah, of course you can't deduce <code>X = X'</code> and <code>Y = Y'</code> from <code>X ⟶ Y = X' ⟶ Y'</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676778):
<p>not for function types and definitely not for homsets</p>

#### [ Reid Barton (Sep 10 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676917):
<p>Although it curiously would not even matter for the cardinality estimate I need to do here, because it would blow things up by a factor of less than <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span></p>

#### [ Reid Barton (Sep 10 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133676941):
<p>But anyways, that's when I started to wonder: would it be better to just define the edges as <code>(mors : set (Σ X Y, X ⟶ Y))</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677178):
<p>I'm inclined to say no, although possibly you might want <code>homs</code> to be defined on all objects, not just those in the subset</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677188):
<p>and just require that it be empty outside the subset</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677264):
<div class="codehilite"><pre><span></span>structure subgraph (C : Type u) [small_category C] : Type u :=
(objs : set C)
(homs : Π X Y : C, set (X ⟶ Y))
(dom_mem : Π X Y f, f ∈ homs X Y → X ∈ objs)
(cod_mem : Π X Y f, f ∈ homs X Y → Y ∈ objs)
</pre></div>

#### [ Reid Barton (Sep 10 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677305):
<p>Right, I would need those last two fields anyways. Just a difference between <code>set (Σ X Y, X ⟶ Y)</code> and <code>Π X Y : C, set (X ⟶ Y)</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677362):
<p>having a big sigma will make things more complicated with heqs and stuff as you've seen</p>

#### [ Reid Barton (Sep 10 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677367):
<p>Given that some of the things I do are look at the cardinality of the set of edges, and form the union of subgraphs</p>

#### [ Reid Barton (Sep 10 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677381):
<p>but I guess those are not significantly harder with the Pi approach</p>

#### [ Mario Carneiro (Sep 10 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20again/near/133677396):
<p>I think <code>arrows := Σ X Y, X ⟶ Y</code> is a useful definition in a category though</p>


{% endraw %}
