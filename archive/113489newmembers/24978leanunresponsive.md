---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/24978leanunresponsive.html
---

## Stream: [new members](index.html)
### Topic: [lean unresponsive](24978leanunresponsive.html)

---


{% raw %}
#### [ Sarah Mameche (Jan 07 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154576468):
<p>Hi, when I use 3.4.1, there are problems with displaying the goal if proofs get longer. In both Emacs and vscode, the goal is not displayed anymore and the message box just says 'updating'. If the proof is deleted and I restart it, it always happens again in some subcase as soon as the proof gets longer (it is not really that huge though, 20 lines maybe). Lean does not respond if something is typed  (if I type "end" I get the synthesize-placeholder error). Has anyone had this before?</p>

#### [ Bryan Gin-ge Chen (Jan 07 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154577042):
<p>In VS code, are you seeing any indications that lean is still working (e.g. orange bars on the sides)? It might help if you post a minimum example, since slowness could be caused by a variety of things...</p>

#### [ Uranus Testing (Jan 07 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154577401):
<p>There are orange bars on the sides and indicator in status bar (“Lean [indicator] (checking visible lines)”).</p>

#### [ Sarah Mameche (Jan 08 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154630892):
<p>The orange bars are there for a moment but disappear directly.</p>
<p>The proof uses two other files of definitions, here are the types if that helps: </p>
<div class="codehilite"><pre><span></span>variable Fin : nat -&gt; Type
variable tm : nat -&gt; Type
variable neutral {n} : tm n → Prop
variable eval : Π {n}, tm n → tm n → Prop
inductive type : Type
| tint : type
| tarrow : type → type → type
variable types : Π {m}, (Fin m → type) → tm m → type → Prop

variable R :  Π {n : nat}, (Fin n → type) → type → tm n → Prop

variable SNe : Π {n}, tm n → Prop

theorem CR₁₃x {n} (Γ) (A : type) (s:tm n) : (R Γ A s → SNe s) ∧
  (types Γ s A → neutral s → (∀ t, eval s t → R Γ A t)  → R Γ A s) :=   ...
</pre></div>


<p>I do an induction on the type A, but the proof always crashes somewhere in the tarrow-case ...</p>

#### [ Kenny Lau (Jan 08 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631244):
<p>more code would help</p>

#### [ Uranus Testing (Jan 08 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631733):
<p>What if run file from command line ($ lean /path/to/proof.lean)?</p>

#### [ Sarah Mameche (Jan 08 2019 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631799):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">nat</span>
<span class="kn">inductive</span> <span class="n">Fin</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">fz</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">Fin</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">fs</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">Fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Fin</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span>
<span class="kn">open</span> <span class="n">Fin</span>
<span class="n">attribute</span> <span class="kn">reducible</span> <span class="n">Fin</span>

<span class="kn">inductive</span> <span class="n">tm</span>  <span class="o">:</span> <span class="n">nat</span> <span class="bp">-&gt;</span> <span class="kt">Type</span>
  <span class="bp">|</span> <span class="n">var_tm</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">ntm</span> <span class="o">:</span> <span class="n">nat</span><span class="o">},</span> <span class="n">Fin</span> <span class="n">ntm</span> <span class="bp">-&gt;</span> <span class="n">tm</span> <span class="n">ntm</span>
  <span class="bp">|</span> <span class="n">app</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">ntm</span> <span class="o">:</span> <span class="n">nat</span><span class="o">},</span> <span class="n">tm</span> <span class="n">ntm</span> <span class="bp">-&gt;</span> <span class="n">tm</span> <span class="n">ntm</span> <span class="bp">-&gt;</span> <span class="n">tm</span> <span class="n">ntm</span>
  <span class="bp">|</span> <span class="n">lam</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">ntm</span> <span class="o">:</span> <span class="n">nat</span><span class="o">},</span> <span class="n">tm</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">ntm</span><span class="o">)</span> <span class="bp">-&gt;</span> <span class="n">tm</span> <span class="n">ntm</span>
  <span class="bp">|</span> <span class="n">const</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">ntm</span> <span class="o">:</span> <span class="n">nat</span><span class="o">},</span> <span class="n">nat</span>  <span class="bp">-&gt;</span> <span class="n">tm</span> <span class="n">ntm</span>
  <span class="bp">|</span> <span class="n">plus</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">ntm</span> <span class="o">:</span> <span class="n">nat</span><span class="o">},</span> <span class="n">tm</span> <span class="n">ntm</span> <span class="bp">-&gt;</span> <span class="n">tm</span> <span class="n">ntm</span> <span class="bp">-&gt;</span> <span class="n">tm</span> <span class="n">ntm</span>
<span class="kn">open</span> <span class="n">tm</span>

<span class="n">reserve</span> <span class="kn">infixl</span> <span class="bp">`</span><span class="err">≻</span><span class="bp">`</span><span class="o">:</span><span class="mi">40</span>
<span class="kn">inductive</span> <span class="kn">eval</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="n">tm</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">tm</span> <span class="n">n</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="kn">infixl</span> <span class="bp">`</span><span class="err">≻</span><span class="bp">`</span> <span class="o">:=</span> <span class="kn">eval</span>
<span class="bp">|</span> <span class="n">eappl</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">e₁</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">e₁&#39;</span> <span class="n">e₂</span><span class="o">}</span> <span class="o">:</span> <span class="n">e₁</span> <span class="err">≻</span> <span class="n">e₁&#39;</span> <span class="bp">→</span>  <span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span> <span class="err">≻</span> <span class="n">app</span> <span class="n">e₁&#39;</span> <span class="n">e₂</span>
<span class="bp">|</span> <span class="n">eappr</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">e₁</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">e₂</span> <span class="n">e₂&#39;</span><span class="o">}</span> <span class="o">:</span> <span class="n">e₂</span> <span class="err">≻</span> <span class="n">e₂&#39;</span> <span class="bp">→</span> <span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span> <span class="err">≻</span> <span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂&#39;</span>
<span class="bp">|</span> <span class="n">elam</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">e1</span> <span class="o">:</span> <span class="n">tm</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)}</span> <span class="o">{</span><span class="n">e2</span><span class="o">}</span> <span class="o">:</span> <span class="n">e1</span> <span class="err">≻</span> <span class="n">e2</span> <span class="bp">→</span> <span class="n">lam</span> <span class="n">e1</span> <span class="err">≻</span> <span class="n">lam</span> <span class="n">e2</span>
<span class="bp">|</span> <span class="n">eplusl</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">e₁</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">n</span><span class="o">}{</span><span class="n">e₁&#39;</span> <span class="n">e₂</span><span class="o">}</span> <span class="o">:</span> <span class="n">e₁</span> <span class="err">≻</span> <span class="n">e₁&#39;</span> <span class="bp">→</span> <span class="n">plus</span> <span class="n">e₁</span> <span class="n">e₂</span> <span class="err">≻</span> <span class="n">plus</span> <span class="n">e₁&#39;</span> <span class="n">e₂</span>
<span class="bp">|</span> <span class="n">eplusr</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">e₁</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">e₂</span> <span class="n">e₂&#39;</span><span class="o">}</span> <span class="o">:</span> <span class="n">e₂</span> <span class="err">≻</span> <span class="n">e₂&#39;</span> <span class="bp">→</span> <span class="n">plus</span> <span class="n">e₁</span> <span class="n">e₂</span> <span class="err">≻</span> <span class="n">plus</span> <span class="n">e₁</span> <span class="n">e₂&#39;</span>
<span class="bp">|</span> <span class="n">econst</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">n₁</span> <span class="n">n₂</span><span class="o">}</span> <span class="o">:</span> <span class="bp">@</span><span class="kn">eval</span> <span class="n">n</span> <span class="o">(</span><span class="n">plus</span> <span class="o">(</span><span class="n">const</span> <span class="n">n₁</span><span class="o">)</span> <span class="o">(</span><span class="n">const</span> <span class="n">n₂</span><span class="o">))</span> <span class="o">(</span><span class="n">const</span> <span class="o">(</span><span class="n">n₁</span><span class="bp">+</span><span class="n">n₂</span><span class="o">))</span>
<span class="c1">--| ebeta {n} {e₁ : tm (nat.succ n)} {e₂} : app (lam e₁) e₂ ≻ (subst_tm (scons e₂ var_tm ) (e₁))</span>
<span class="kn">infix</span> <span class="bp">`</span><span class="err">≻</span><span class="bp">`</span> <span class="o">:=</span> <span class="kn">eval</span>
<span class="kn">open</span> <span class="kn">eval</span>

<span class="kn">inductive</span> <span class="n">type</span> <span class="o">:</span> <span class="kt">Type</span>
  <span class="bp">|</span> <span class="n">tint</span> <span class="o">:</span> <span class="n">type</span>
  <span class="bp">|</span> <span class="n">tarrow</span> <span class="o">:</span> <span class="n">type</span> <span class="bp">→</span> <span class="n">type</span> <span class="bp">→</span> <span class="n">type</span>
<span class="kn">open</span> <span class="n">type</span>
<span class="kn">infixl</span> <span class="bp">`</span><span class="err">⤏</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">tarrow</span>

<span class="kn">definition</span> <span class="n">ctx</span> <span class="o">(</span><span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Fin</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">type</span>

<span class="kn">inductive</span> <span class="n">types</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">m</span><span class="o">},</span> <span class="o">(</span><span class="n">Fin</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">type</span><span class="o">)</span> <span class="bp">→</span> <span class="n">tm</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">type</span> <span class="bp">→</span> <span class="kt">Prop</span>
  <span class="bp">|</span> <span class="n">tvar</span> <span class="o">{</span><span class="n">m</span><span class="o">}</span> <span class="err">Γ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">Fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">types</span> <span class="err">Γ</span> <span class="o">(</span><span class="n">var_tm</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="err">Γ</span> <span class="n">x</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">tapp</span> <span class="o">{</span><span class="n">m</span><span class="o">}</span> <span class="err">Γ</span> <span class="o">(</span><span class="n">e₁</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">m</span><span class="o">)</span> <span class="n">e₂</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span><span class="o">)</span> <span class="o">:</span> <span class="n">types</span> <span class="err">Γ</span> <span class="n">e₁</span> <span class="o">(</span><span class="n">tarrow</span> <span class="n">A</span> <span class="n">B</span><span class="o">)</span> <span class="bp">→</span> <span class="n">types</span> <span class="err">Γ</span> <span class="n">e₂</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">types</span> <span class="err">Γ</span> <span class="o">(</span><span class="n">app</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="n">B</span>
  <span class="bp">|</span> <span class="n">tplus</span> <span class="o">{</span><span class="n">m</span><span class="o">}</span> <span class="err">Γ</span> <span class="o">(</span><span class="n">e₁</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">e₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">types</span> <span class="err">Γ</span> <span class="n">e₁</span> <span class="n">tint</span> <span class="bp">→</span> <span class="n">types</span> <span class="err">Γ</span> <span class="n">e₂</span> <span class="n">tint</span> <span class="bp">→</span> <span class="n">types</span> <span class="err">Γ</span> <span class="o">(</span><span class="n">plus</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="n">tint</span>
 <span class="c1">-- | tlam {m} Γ (e : tm (nat.succ m)) (A B) : types (@scons _ m  A Γ) e B → types Γ (lam e) (A ⤏ B)</span>
  <span class="bp">|</span> <span class="n">tconst</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span><span class="o">}</span> <span class="o">(</span><span class="err">Γ</span> <span class="o">:</span> <span class="n">ctx</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">types</span> <span class="err">Γ</span> <span class="o">(</span><span class="n">const</span> <span class="n">n</span><span class="o">)</span> <span class="n">tint</span>
<span class="kn">notation</span> <span class="err">Γ</span> <span class="bp">`</span> <span class="err">⊢</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="n">x</span> <span class="bp">`</span> <span class="o">:</span> <span class="bp">`</span> <span class="n">A</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">types</span> <span class="err">Γ</span> <span class="n">x</span> <span class="n">A</span><span class="bp">.</span>
<span class="kn">open</span> <span class="n">types</span>

<span class="kn">definition</span> <span class="n">agree_ren</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="err">Γ</span> <span class="o">:</span> <span class="n">ctx</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="err">Γ&#39;</span> <span class="o">:</span> <span class="n">ctx</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">ξ</span> <span class="o">:</span> <span class="n">Fin</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">Fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">forall</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="err">Γ</span> <span class="o">(</span><span class="n">ξ</span> <span class="n">x</span><span class="o">))</span> <span class="bp">=</span> <span class="err">Γ&#39;</span> <span class="n">x</span><span class="bp">.</span>

<span class="kn">notation</span> <span class="err">Γ</span> <span class="bp">`</span><span class="err">≼</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="err">Δ</span> <span class="bp">`</span><span class="o">:</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="n">ξ</span> <span class="o">:=</span> <span class="n">agree_ren</span> <span class="err">Δ</span> <span class="err">Γ</span> <span class="n">ξ</span><span class="bp">.</span>

<span class="kn">definition</span> <span class="n">neutral</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">n</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">lam</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">tt</span>


<span class="kn">inductive</span> <span class="n">SN</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">n</span> <span class="bp">-&gt;</span> <span class="n">tm</span> <span class="n">n</span> <span class="bp">-&gt;</span> <span class="kt">Prop</span> <span class="o">)</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">n</span> <span class="bp">-&gt;</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">sn_step</span> <span class="o">(</span><span class="n">e1</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="k">forall</span> <span class="n">e2</span><span class="o">,</span> <span class="n">R</span> <span class="n">e1</span> <span class="n">e2</span> <span class="bp">-&gt;</span> <span class="n">SN</span> <span class="n">e2</span><span class="o">)</span> <span class="bp">-&gt;</span> <span class="n">SN</span> <span class="n">e1</span><span class="bp">.</span>

<span class="kn">definition</span> <span class="n">SNe</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">SN</span> <span class="n">n</span> <span class="kn">eval</span><span class="bp">.</span>

<span class="kn">constant</span> <span class="n">ren_tm</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span> <span class="n">mtm</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">}</span> <span class="o">{</span> <span class="n">ntm</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">}</span> <span class="o">(</span><span class="n">xitm</span> <span class="o">:</span> <span class="n">Fin</span> <span class="n">mtm</span> <span class="bp">-&gt;</span> <span class="n">Fin</span> <span class="n">ntm</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">tm</span> <span class="n">mtm</span><span class="o">),</span> <span class="n">tm</span> <span class="n">ntm</span> <span class="c1">--...</span>

<span class="kn">definition</span> <span class="n">R</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="o">(</span><span class="n">ctx</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">type</span> <span class="bp">→</span> <span class="n">tm</span> <span class="n">n</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">n</span> <span class="err">Γ</span> <span class="n">tint</span> <span class="n">s</span> <span class="o">:=</span>  <span class="o">(</span><span class="err">Γ</span> <span class="err">⊢</span> <span class="n">s</span> <span class="o">:</span> <span class="n">tint</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">SNe</span> <span class="n">s</span>
<span class="bp">|</span> <span class="n">n</span> <span class="err">Γ</span> <span class="o">(</span><span class="n">tarrow</span> <span class="n">A</span> <span class="n">B</span><span class="o">)</span> <span class="n">s</span> <span class="o">:=</span> <span class="err">Γ</span> <span class="err">⊢</span> <span class="n">s</span> <span class="o">:</span> <span class="n">tarrow</span> <span class="n">A</span> <span class="n">B</span> <span class="bp">∧</span> <span class="k">forall</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="n">ξ</span> <span class="err">Δ</span> <span class="n">t</span><span class="o">,</span>
    <span class="o">(</span><span class="err">Γ</span> <span class="err">≼</span> <span class="err">Δ</span> <span class="o">:</span> <span class="n">ξ</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">@</span><span class="n">R</span> <span class="n">m</span> <span class="err">Δ</span> <span class="n">A</span> <span class="n">t</span> <span class="bp">-&gt;</span> <span class="n">R</span> <span class="err">Δ</span> <span class="n">B</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">ren_tm</span> <span class="n">ξ</span> <span class="n">s</span><span class="o">)</span> <span class="n">t</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">CR₁₃</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">(</span><span class="err">Γ</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span><span class="o">:</span> <span class="n">tm</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">R</span> <span class="err">Γ</span> <span class="n">A</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">SNe</span> <span class="n">s</span><span class="o">)</span> <span class="bp">∧</span>
  <span class="o">(</span><span class="err">Γ</span> <span class="err">⊢</span> <span class="n">s</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">neutral</span> <span class="n">s</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">t</span><span class="o">,</span> <span class="n">s</span> <span class="err">≻</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">R</span> <span class="err">Γ</span> <span class="n">A</span> <span class="n">t</span><span class="o">)</span> <span class="bp">→</span> <span class="n">R</span> <span class="err">Γ</span> <span class="n">A</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">revert</span> <span class="n">s</span> <span class="err">Γ</span> <span class="n">n</span><span class="o">,</span> <span class="n">induction</span> <span class="n">A</span><span class="bp">;</span> <span class="n">intros</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">apply</span> <span class="n">h</span><span class="bp">.</span><span class="n">right</span><span class="o">,},</span>
    <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span> <span class="n">admit</span><span class="o">,</span>
     <span class="n">constructor</span><span class="o">,</span> <span class="n">intros</span><span class="o">,</span>
    <span class="n">apply</span> <span class="o">(</span><span class="n">a_2</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">right</span><span class="o">,</span> <span class="n">admit</span><span class="o">,</span>
    <span class="o">},</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">apply</span> <span class="n">SN_appzero</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">p</span><span class="o">:=</span> <span class="o">(</span><span class="n">A_ih_a_1</span> <span class="o">(</span><span class="n">A_a</span><span class="bp">.;</span><span class="err">Γ</span><span class="o">)</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">ren_tm</span> <span class="n">shift</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">var_tm</span> <span class="n">var_zero</span><span class="o">))),</span>
    <span class="n">apply</span> <span class="n">p</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span> <span class="n">apply</span> <span class="n">h</span><span class="bp">.</span><span class="n">right</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>  <span class="n">refl</span><span class="o">,</span> <span class="o">},</span>
      <span class="o">{</span> <span class="n">apply</span> <span class="o">(</span><span class="n">A_ih_a</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">right</span><span class="o">,</span>
        <span class="o">{</span> <span class="n">constructor</span><span class="o">,</span> <span class="o">},</span>
        <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">neutral</span><span class="o">],</span> <span class="o">},</span>
        <span class="o">{</span> <span class="n">intros</span> <span class="n">t</span> <span class="n">q</span><span class="o">,</span> <span class="n">cases</span> <span class="n">q</span><span class="o">,</span> <span class="o">},</span>
      <span class="o">},</span>
    <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">h₃</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span> <span class="n">aauto</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">m</span> <span class="n">ξ</span> <span class="err">Δ</span> <span class="n">t</span> <span class="n">p₁</span> <span class="n">p₂</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">p₃</span> <span class="o">:</span> <span class="n">SNe</span> <span class="n">t</span><span class="o">,</span>
      <span class="k">from</span> <span class="k">begin</span>
        <span class="n">apply</span> <span class="o">(</span><span class="n">A_ih_a</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span> <span class="n">aauto</span>
      <span class="kn">end</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">p₃</span><span class="o">,</span>
</pre></div>


<p>There are some more definitions about properties of tm n, though</p>

#### [ Sarah Mameche (Jan 08 2019 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631854):
<p>It compiles if I run it from the command line but I can't finish the proof in interactive mode</p>

#### [ Kenny Lau (Jan 08 2019 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154631855):
<p>you still aren't showing us the exact part of your code that crashes</p>

#### [ Uranus Testing (Jan 08 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632041):
<p>Look at “Lean: Server Errors” log in Visual Studio Code, it may be useful.</p>

#### [ Sarah Mameche (Jan 08 2019 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632221):
<p>It added the induction where it crashed, but right now I can't even edit something at the beginning of the proof...</p>

#### [ Kenny Lau (Jan 08 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632274):
<p>you are advised to put <code>end</code> immediately after you put <code>begin</code> (and then add stuff between), etc</p>

#### [ Sarah Mameche (Jan 08 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632415):
<p>Oh that solved it! Thanks a lot</p>

#### [ Patrick Massot (Jan 08 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/lean%20unresponsive/near/154632772):
<p>This may be a good time to start using VScode code snippets. In menu File/Preferences/User code snippet (or slight variation on this, I'm making up translation from French) and select <code>lean.json</code>. Then put in:</p>
<div class="codehilite"><pre><span></span><span class="p">{</span>
    <span class="nt">&quot;Proof&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="nt">&quot;prefix&quot;</span><span class="p">:</span> <span class="s2">&quot;proof&quot;</span><span class="p">,</span>
        <span class="nt">&quot;body&quot;</span><span class="p">:</span> <span class="p">[</span>
          <span class="s2">&quot;begin&quot;</span><span class="p">,</span>
          <span class="s2">&quot;  $0&quot;</span><span class="p">,</span>
          <span class="s2">&quot;  sorry&quot;</span><span class="p">,</span>
          <span class="s2">&quot;end&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="nt">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;Proof tactic block&quot;</span>
    <span class="p">}</span>
</pre></div>


<p>Then you can (start to) type  proof and auto-completion will suggests using the snippet. After accepting that suggestion VScode will write "begin", "sorry", "end" and put the cursor at the right position</p>


{% endraw %}
