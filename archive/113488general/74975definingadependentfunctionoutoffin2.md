---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74975definingadependentfunctionoutoffin2.html
---

## Stream: [general](index.html)
### Topic: [defining a dependent function out of `fin 2`](74975definingadependentfunctionoutoffin2.html)

---


{% raw %}
#### [ Scott Morrison (Sep 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038733):
<p>I'm stuck on something basic to do with <code>fin n</code>.</p>

#### [ Scott Morrison (Sep 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038734):
<p>Suppose I have <code>T : fin 2 → Type</code>, and I happen to have <code>X : T ⟨ 0, by tidy ⟩</code> and a <code>Y : T ⟨ 1, by tidy ⟩</code>.</p>

#### [ Scott Morrison (Sep 16 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038736):
<p>How do I construct the dependent function <code>Π n : fin 2, T n</code> which sends 0 to <code>X</code> and 1 to <code>Y</code>?</p>

#### [ Simon Hudon (Sep 16 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038784):
<p>What about using an <code>if _ then _ else _</code>?</p>

#### [ Scott Morrison (Sep 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038797):
<p>How would that work?</p>

#### [ Scott Morrison (Sep 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038812):
<p>I remember someone showing me a trick to do <code>match</code> on <code>fin n</code>, but I can't find it anywhere now. :-(</p>

#### [ Simon Hudon (Sep 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038819):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">T</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="bp">|</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="n">X</span> <span class="k">else</span> <span class="n">Y</span>
</pre></div>

#### [ Simon Hudon (Sep 16 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038867):
<p>If you find it again, please show me.</p>

#### [ Scott Morrison (Sep 16 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038944):
<p>I don't see how your suggestion helps, <span class="user-mention" data-user-id="110026">@Simon Hudon</span>:</p>
<div class="codehilite"><pre><span></span>import tactic.tidy

def T : fin 2 → Type := sorry
def X : T ⟨ 0, by tidy ⟩ := sorry
def Y : T ⟨ 1, by tidy ⟩ := sorry

def S : Π n : fin 2, T n
| x := if x = 0 then X else Y
</pre></div>

#### [ Scott Morrison (Sep 16 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038950):
<p>errors with </p>
<div class="codehilite"><pre><span></span>type mismatch at application
  ite (x = 0) X
term
  X
has type
  T ⟨0, X._proof_1⟩
but is expected to have type
  T x
</pre></div>

#### [ Simon Hudon (Sep 16 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038961):
<p>Ah ok, I misunderstood your problem</p>

#### [ Scott Morrison (Sep 16 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039161):
<p>Here's a example of my problem:</p>
<div class="codehilite"><pre><span></span>import tactic.tidy

def T : fin 2 → Type := ([ℕ, ℤ].to_array).data
def X : T ⟨ 0, by tidy ⟩ := begin show ℕ, exact 1 end
def Y : T ⟨ 1, by tidy ⟩ := begin show ℤ, exact -1 end

def S : Π n : fin 2, T n
| ⟨ 0, _ ⟩ := X
| ⟨ 1, _ ⟩ := Y
| _ := sorry
</pre></div>

#### [ Scott Morrison (Sep 16 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039167):
<p>The question is to define <code>S</code>, following the intention shown, but without a <code>sorry</code>.</p>

#### [ Scott Morrison (Sep 16 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039171):
<p>(Side questions include better ways to write <code>T</code> in the first place.)</p>

#### [ Simon Hudon (Sep 16 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039173):
<p>One thing you can do is:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">S</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">n</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">,</span> <span class="n">T</span> <span class="n">n</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span><span class="bp">_⟩</span> <span class="o">:=</span> <span class="n">X</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span><span class="bp">_⟩</span> <span class="o">:=</span> <span class="n">Y</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">succ</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">),</span><span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="err">$</span> <span class="k">by</span> <span class="o">{</span> <span class="n">admit</span><span class="o">,</span> <span class="o">}</span>
</pre></div>

#### [ Scott Morrison (Sep 16 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039233):
<p>Excellent! That works, now the question becomes --- is my distant memory that there's an even better solution, correct? :-)</p>

#### [ Simon Hudon (Sep 16 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039281):
<p>My brain times out looking for one</p>

#### [ Scott Morrison (Sep 16 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039283):
<p>And what is the canonical way to fill in that admit, these days?</p>

#### [ Scott Morrison (Sep 16 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039291):
<p>I'd hoped that <code>linarith</code> was up to proving discharging <code>n+2 &lt; 2</code> implies <code>false</code>, but apparently not.</p>

#### [ Simon Hudon (Sep 16 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039293):
<p>There's a <code>linarith</code> tactic coming down the pipes. Maybe it can handle <code>nat</code> now? We'd have to check</p>

#### [ Simon Hudon (Sep 16 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039294):
<p>Oh, that's too bad</p>

#### [ Scott Morrison (Sep 16 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039334):
<p>There was a recent addition saying it could do nat.</p>

#### [ Scott Morrison (Sep 16 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039335):
<p>Oh, maybe I haven't pulled that one yet...</p>

#### [ Simon Hudon (Sep 16 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039342):
<p>It feels like the kind of proposition that you should be able to prove in two steps. All I can think of takes more</p>

#### [ Simon Hudon (Sep 16 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039389):
<div class="codehilite"><pre><span></span><span class="bp">|</span> <span class="bp">⟨</span><span class="n">succ</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">),</span><span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="err">$</span> <span class="k">by</span> <span class="o">{</span> <span class="n">apply</span> <span class="n">not_lt_of_ge</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">repeat</span> <span class="o">{</span> <span class="n">apply</span> <span class="n">succ_le_succ</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">zero_le</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>

#### [ Scott Morrison (Sep 16 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039444):
<p>(deleted)</p>

#### [ Simon Hudon (Sep 16 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039503):
<p>Ah! This is even shorter:</p>
<div class="codehilite"><pre><span></span>  <span class="k">by</span> <span class="o">{</span> <span class="n">repeat</span> <span class="o">{</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">lt_of_succ_lt_succ</span> <span class="n">h</span> <span class="o">},</span> <span class="n">cases</span> <span class="n">h</span> <span class="o">}</span>
</pre></div>

#### [ Mario Carneiro (Sep 16 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039568):
<p>that should be false by matching</p>

#### [ Scott Morrison (Sep 16 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039570):
<p>hmm, that doesn't work for me?</p>

#### [ Scott Morrison (Sep 16 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039575):
<p>but Kenny just showed me:</p>
<div class="codehilite"><pre><span></span>import tactic.tidy
-- import tactic.linarith

def T : fin 2 → Type := ([ℕ, ℤ].to_array).data
def X : T ⟨ 0, by tidy ⟩ := begin show ℕ, exact 1 end
def Y : T ⟨ 1, by tidy ⟩ := begin show ℤ, exact -1 end

def S : Π n : fin 2, T n
| ⟨ 0, _ ⟩ := X
| ⟨ 1, _ ⟩ := Y
| ⟨ nat.succ (nat.succ n), H ⟩ := false.elim $ by cases H with H H; cases H with H H; cases H
</pre></div>

#### [ Mario Carneiro (Sep 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039620):
<p>You can also use <code>fin.succ_rec_on</code> to get the right induction principle</p>

#### [ Scott Morrison (Sep 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039621):
<p>ah, and the new <code>linarith</code> really does it!</p>

#### [ Kenny Lau (Sep 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039622):
<p>how about</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="n">def</span> <span class="n">fin2</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span><span class="o">),</span> <span class="n">C</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">C</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">n</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="n">C0</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">C0</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="bp">_</span> <span class="n">C1</span> <span class="o">:=</span> <span class="n">C1</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="err">$</span> <span class="n">not_le_of_gt</span> <span class="n">H</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_add_left</span> <span class="bp">_</span> <span class="bp">_</span>
</pre></div>

#### [ Scott Morrison (Sep 16 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039668):
<div class="codehilite"><pre><span></span>import tactic.tidy
import tactic.linarith

def T : fin 2 → Type := ([ℕ, ℤ].to_array).data
def X : T ⟨ 0, by tidy ⟩ := begin show ℕ, exact 1 end
def Y : T ⟨ 1, by tidy ⟩ := begin show ℤ, exact -1 end

def S : Π n : fin 2, T n
| ⟨ 0, _ ⟩ := X
| ⟨ 1, _ ⟩ := Y
| ⟨ n + 2, H ⟩ := by exfalso; linarith
</pre></div>

#### [ Mario Carneiro (Sep 16 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039891):
<div class="codehilite"><pre><span></span>import data.fin data.list.basic

def T : fin 2 → Type := ([ℕ, ℤ].to_array).data
def X : T ⟨0, dec_trivial⟩ := (1 : ℕ)
def Y : T ⟨1, dec_trivial⟩ := (-1 : ℤ)

def S : Π n : fin 2, T n :=
fin.cases X (λ i, fin.cases Y (λ i, i.elim0) i)
</pre></div>

#### [ Scott Morrison (Sep 16 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134043762):
<p>Thanks, Mario. I think I might use the <code>match</code> version, even if it depends on linarith, for decipherability.</p>

#### [ Scott Morrison (Sep 16 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134043805):
<p>I think I'll also write a <code>fin_cases</code> tactic, that works with a <code>fin n</code> hypothesis with <code>n</code> a numeral.</p>

#### [ Scott Morrison (Sep 16 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134043808):
<p>(and actually gives you all the cases)</p>


{% endraw %}
