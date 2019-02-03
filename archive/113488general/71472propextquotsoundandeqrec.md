---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71472propextquotsoundandeqrec.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [propext, quot.sound and eq.rec](https://leanprover-community.github.io/archive/113488general/71472propextquotsoundandeqrec.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Oct 09 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135462261):
<p>Is every <code>nat</code> defined using <code>propext</code>, <code>quot.sound</code> and <code>eq.rec</code> but without choice guaranteed to reduce to <code>succ $ succ $ succ ... zero</code>?</p>

#### [ Gabriel Ebner (Oct 09 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135481037):
<p>You don't even need <code>quot.sound</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_refl</span> <span class="o">:</span> <span class="n">true</span> <span class="bp">=</span> <span class="o">(</span><span class="n">true</span> <span class="bp">∨</span> <span class="n">false</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">propext</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span>

<span class="n">def</span> <span class="n">does_not_reduce_to_zero</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">_</span> <span class="n">not_refl</span> <span class="err">$</span>
<span class="mi">0</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">does_not_reduce_to_zero</span>
<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">proofs</span> <span class="n">true</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="n">does_not_reduce_to_zero</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="n">does_not_reduce_to_zero</span>
</pre></div>

#### [ Gabriel Ebner (Oct 09 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135481110):
<p>I'm pretty sure <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> has an example lying around that doesn't even need <code>propext</code>; I think you can do this even with a counterexample to the transitivity of definitional equality.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135481440):
<p>An excellent question and an excellent answer!</p>

#### [ Scott Olson (Oct 09 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135481619):
<p>Here's an example with quotients:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">s₁</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="o">[</span><span class="mi">1</span><span class="o">,</span> <span class="mi">2</span><span class="o">,</span> <span class="mi">3</span><span class="o">]</span>
<span class="n">def</span> <span class="n">s₂</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="o">[</span><span class="mi">2</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span> <span class="mi">3</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">s₁_eq_s₂</span> <span class="o">:</span> <span class="n">s₁</span> <span class="bp">=</span> <span class="n">s₂</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">perm</span><span class="bp">.</span><span class="n">swap</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
<span class="n">def</span> <span class="n">s₃</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">s₁_eq_s₂</span> <span class="n">s₁</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">s₂</span><span class="bp">.</span><span class="n">card</span> <span class="c1">-- 3</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="n">s₃</span><span class="bp">.</span><span class="n">card</span> <span class="c1">-- 3</span>

<span class="bp">#</span><span class="n">reduce</span> <span class="n">s₂</span><span class="bp">.</span><span class="n">card</span> <span class="c1">-- 3</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="n">s₃</span><span class="bp">.</span><span class="n">card</span> <span class="c1">-- quot.lift list.length _ (eq.rec (quot.mk list.perm [1, 2, 3]) _)</span>
</pre></div>


<p>AIUI, the kernel reduction rules for quotients only know how to reduce terms in the form <code> quot.lift _ _ (quot.mk _ _)</code>, but <code>quot.sound</code> introduces an irreducible <code>eq</code>.</p>
<p>EDIT: simplified example</p>

#### [ Chris Hughes (Oct 09 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482021):
<p>I did manage to prove <code>does_not_reduce_to_zero = 0</code>, after quite a bit of fiddling around. Next question, is there an example where it's not provably equal to something of the form <code>succ $ succ $ ... 0</code></p>

#### [ Chris Hughes (Oct 09 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482155):
<p>This basically means that a lot of computable functions aren't really computable. That is surprising.</p>

#### [ Scott Olson (Oct 09 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482382):
<p>There's a section about the implications of axioms in Lean here <a href="https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html">https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html</a></p>

#### [ Scott Olson (Oct 09 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482525):
<p>In particular Lean makes a distinction between canonicity (being able to evaluate any closed term of type ℕ to <code>succ $ succ $ ... 0</code>) and computability</p>

#### [ Gabriel Ebner (Oct 09 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482544):
<blockquote>
<p>This basically means that a lot of computable functions aren't really computable.</p>
</blockquote>
<p>No, they're perfectly computable.  Just not using the reduction relation of the type theory.  (The easiest way to compute them is using type erasure, i.e., VM execution.)</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135494239):
<p>The extra magic sauce that the VM has and the kernel reduction doesn't is the reduction <code>eq.rec h e ~&gt; e</code>, regardless of the type of <code>h</code>. This is not type correct unless <code>h : A = A</code>, in which case the kernel knows about it as well, but the VM just plows ahead anyway</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135494367):
<p>This means that the VM deals with terms that are not type correct, and this is resolved by saying that types are "erased" so that now the terms have no meaning except for their reduction behavior. Concretely, this means that any term of type <code>Sort u</code> is replaced with <code>*</code>, as well as any proofs (terms of type <code>p : Prop</code>). When you see me talk about "data" vs non-data, this is what I am talking about. Anything which is a type has no runtime representation except as a neutral object that does nothing</p>

#### [ Chris Hughes (Oct 13 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135706032):
<blockquote>
<p>I'm pretty sure <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> has an example lying around that doesn't even need <code>propext</code>; I think you can do this even with a counterexample to the transitivity of definitional equality.</p>
</blockquote>
<p>I had a go at this. Most of the non transitivities contain free variables, but I after a little while I found an example with bound variables instead that was provable without <code>funext</code>. The trouble was that even though the <code>rfl</code> didn't work as a proof, the proof I wrote instead still reduced to <code>eq.refl _</code>, so my <code>nat</code> did reduce.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">h</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">P</span> <span class="n">b</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">b</span><span class="o">,</span> <span class="n">C</span> <span class="n">h</span><span class="o">)</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">P</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">f</span> <span class="n">h</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">f</span> <span class="n">h₁</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">lemma</span> <span class="n">acc_rec_lemma</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">acc</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">false</span> <span class="bp">→</span> <span class="n">acc</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="n">y</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">y</span><span class="o">,</span> <span class="n">false</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">y</span><span class="o">)</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">false</span> <span class="bp">→</span> <span class="n">acc</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="n">y</span><span class="o">),</span>
  <span class="bp">@</span><span class="n">acc</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">ℕ</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="n">C</span> <span class="n">f</span> <span class="mi">0</span> <span class="n">h₁</span><span class="o">)</span> <span class="bp">=</span>
<span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">acc</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="mi">0</span><span class="o">)</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">false</span> <span class="bp">→</span> <span class="n">acc</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="n">y</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">y</span><span class="o">,</span> <span class="n">false</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">y</span><span class="o">)</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">x</span><span class="o">)</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">false</span> <span class="bp">→</span> <span class="n">acc</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="n">y</span><span class="o">),</span>
  <span class="bp">@</span><span class="n">acc</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">ℕ</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="n">C</span> <span class="n">f</span> <span class="mi">0</span> <span class="o">(</span><span class="n">acc</span><span class="bp">.</span><span class="n">intro</span> <span class="mi">0</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span><span class="o">)))</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">h</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="k">show</span> <span class="n">acc</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="o">)</span> <span class="mi">0</span><span class="o">,</span> <span class="k">from</span> <span class="n">acc</span><span class="bp">.</span><span class="n">intro</span> <span class="mi">0</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span><span class="o">))</span>
<span class="c1">-- rfl didn&#39;t work</span>

<span class="n">def</span> <span class="n">does_reduce</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="mi">0</span> <span class="bp">_</span> <span class="n">acc_rec_lemma</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">does_reduce</span>

<span class="bp">#</span><span class="n">reduce</span> <span class="n">does_reduce</span>
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is it possible?</p>

#### [ Kenny Lau (Oct 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135706590):
<p>not sure how relevant this is, but maybe one can produce some examples using this:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">bad</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">bad</span> <span class="o">:</span> <span class="n">list</span> <span class="n">bad</span> <span class="bp">→</span> <span class="n">bad</span>

<span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="n">bad</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">bad : Type</span>
<span class="cm">bad.bad : list bad → bad</span>
<span class="cm">bad.bad.inj : ∀ {a a_1 : list bad}, bad.bad a = bad.bad a_1 → a = a_1</span>
<span class="cm">bad.bad.inj_arrow : Π {a a_1 : list bad}, bad.bad a = bad.bad a_1 → Π ⦃P : Sort l⦄, (a = a_1 → P) → P</span>
<span class="cm">bad.bad.inj_eq : ∀ {a a_1 : list bad}, bad.bad a = bad.bad a_1 = (a = a_1)</span>
<span class="cm">bad.bad.sizeof_spec : ∀ (a : list bad), bad.sizeof (bad.bad a) = 1 + sizeof a</span>
<span class="cm">bad.cases_on : Π (C : bad → Sort l) (x : bad), (Π (a : list bad), C (bad.bad a)) → C x</span>
<span class="cm">bad.has_sizeof_inst : has_sizeof bad</span>
<span class="cm">bad.pack_0_0 : list bad → _nest_1_1.list.bad</span>
<span class="cm">bad.pack_0_0.inj : ∀ (a a_1 : list bad), bad.pack_0_0 a = bad.pack_0_0 a_1 ↔ a = a_1</span>
<span class="cm">bad.pack_unpack_0_0 : ∀ (x_packed : _nest_1_1.list.bad), bad.pack_0_0 (bad.unpack_0_0 x_packed) = x_packed</span>
<span class="cm">bad.primitive.pack : list bad → _nest_1_1.list.bad</span>
<span class="cm">bad.primitive.pack.inj : ∀ (a a_1 : list bad), bad.primitive.pack a = bad.primitive.pack a_1 ↔ a = a_1</span>
<span class="cm">bad.primitive.pack.list.cons.spec : ∀ (hd : bad) (tl : list bad), bad.primitive.pack (hd :: tl) = _nest_1_1.list.bad.cons hd (bad.primitive.pack tl)</span>
<span class="cm">bad.primitive.pack.list.nil.spec : bad.primitive.pack list.nil = _nest_1_1.list.bad.nil</span>
<span class="cm">bad.primitive.pack_unpack : ∀ (x_packed : _nest_1_1.list.bad), bad.primitive.pack (bad.primitive.unpack x_packed) = x_packed</span>
<span class="cm">bad.primitive.sizeof_pack : ∀ (x_unpacked : list bad), _nest_1_1.list.bad.sizeof (bad.primitive.pack x_unpacked) = sizeof x_unpacked</span>
<span class="cm">bad.primitive.unpack : _nest_1_1.list.bad → list bad</span>
<span class="cm">bad.primitive.unpack._nest_1_1.list.bad.cons.spec : ∀ (hd : bad) (tl : _nest_1_1.list.bad),</span>
<span class="cm">  bad.primitive.unpack (_nest_1_1.list.bad.cons hd tl) = hd :: bad.primitive.unpack tl</span>
<span class="cm">bad.primitive.unpack._nest_1_1.list.bad.nil.spec : bad.primitive.unpack _nest_1_1.list.bad.nil = list.nil</span>
<span class="cm">bad.primitive.unpack_pack : ∀ (x_unpacked : list bad), bad.primitive.unpack (bad.primitive.pack x_unpacked) = x_unpacked</span>
<span class="cm">bad.rec : Π (C : bad → Sort l), (Π (a : list bad), C (bad.bad a)) → Π (x : bad), C x</span>
<span class="cm">bad.sizeof : bad → ℕ</span>
<span class="cm">bad.sizeof_pack_0_0 : ∀ (x_unpacked : list bad), _nest_1_1.list.bad.sizeof (bad.pack_0_0 x_unpacked) = sizeof x_unpacked</span>
<span class="cm">bad.unpack_0_0 : _nest_1_1.list.bad → list bad</span>
<span class="cm">bad.unpack_pack_0_0 : ∀ (x_unpacked : list bad), bad.unpack_0_0 (bad.pack_0_0 x_unpacked) = x_unpacked</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Oct 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135706602):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what is <code>pack</code> and <code>unpack</code> and <code>primitive</code> and are there any more hidden constructors like this?</p>

#### [ Mario Carneiro (Oct 13 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135712980):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Actually I think Gabriel's recollection of me is incorrect, that is, I think that canonicity actually holds for closed terms of Lean's DTT with no axioms. I don't have a full proof yet (this is likely a future project), but it's not that hard to show that at least a term can't get stuck, from which the theorem follows assuming strong normalization. Basically, there is a coherent notion of "head position" for a term that determines where to look in a closed term to find a redex, and if there is no redex there then it's a stuck term.</p>
<p>If you look at the left-most part of an application (i.e. follow all apps up the left part), you may find:</p>
<ul>
<li>if you find a lambda then it is a redex or already in whnf (because the whole term is a lambda)</li>
<li>if you find a definition then you can reduce it</li>
<li>if you find an inductive recursor then you can try to reduce the major premise to a constructor (inductively by canonicity), and then it is a redex</li>
<li>if you find an inductive constructor then it is in whnf</li>
<li>if you find a universe or pi or inductive type constructor then it is in whnf</li>
<li>you can't find a variable because it is in the empty context</li>
</ul>
<p>The part where this proof breaks down if you add axioms is in, well, the case analysis. If we have another constant we have another case, and it is not the case that i.e. <code>propext iff.rfl</code> reduces to <code>rfl</code>, which can spoil the inductive recursor case later. The same happens with any of the other axioms - they can be used to inhabit inductive types without giving any hint at what they should reduce to.</p>
<blockquote>
<p>Next question, is there an example where it's not provably equal to something of the form <code>succ $ succ $ ... 0</code></p>
</blockquote>
<p>This is a more interesting question. For the first two axioms I am inclined to say "yes"; the claim for <code>propext</code> seems to be some kind of univalence conservativity statement which is at least intuitively plausible (i.e. any ground terms you prove using <code>propext</code> can be proven without it). For <code>quot.sound</code> this is again a conservativity result - quotients are unnecessary because you can use setoids instead, as in Coq.</p>
<p>For <code>choice</code> it's clearly false; <code>@classical.choice nat &lt;0&gt;</code> is a term of type <code>nat</code> which is not provably equal to any numeral.</p>

#### [ Mario Carneiro (Oct 13 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135713102):
<p>In fact, I think conservativity of <code>propext</code> should follow from conservativity of <code>A ~= B -&gt; A = B</code>, that is, any two types with the same cardinality are consistently equal</p>

#### [ Mario Carneiro (Oct 13 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135713753):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Luckily (for me), nested and mutual inductives are compiled down to regular inductives by lean when you write them, so the kernel knows nothing of them and they don't affect any metatheoretic properties like canonicity. I'm not sure why it's a prefix instead of a suffix (<span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> bug?), but the real inductive type is <code>_nest_1_1._nest_1_1.bad._mut_</code>, and there are a bunch more theorems in that namespace:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="bp">_</span><span class="n">nest_1_1</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">_nest_1_1._nest_1_1.bad._mut_ : psum unit unit → Type</span>
<span class="cm">_nest_1_1._nest_1_1.bad._mut_.bad_0 : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ()) →</span>
<span class="cm">_nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inl idx) ())</span>
<span class="cm">_nest_1_1._nest_1_1.bad._mut_.cons_1 : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inl idx) ()) →</span>
<span class="cm">  _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ()) →</span>
<span class="cm">  _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ())</span>
<span class="cm">_nest_1_1._nest_1_1.bad._mut_.nil_1 : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ())</span>
<span class="cm">_nest_1_1._nest_1_1.bad._mut_.rec : Π {C : Π (a : psum unit unit), _nest_1_1._nest_1_1.bad._mut_ a → Sort l},</span>
<span class="cm">  (Π (a : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ())),</span>
<span class="cm">     C ((λ (idx : unit), psum.inr idx) ()) a →</span>
<span class="cm">     C ((λ (idx : unit), psum.inl idx) ()) (_nest_1_1._nest_1_1.bad._mut_.bad_0 a)) →</span>
<span class="cm">  C ((λ (idx : unit), psum.inr idx) ()) _nest_1_1._nest_1_1.bad._mut_.nil_1 →</span>
<span class="cm">  (Π (hd : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inl idx) ()))</span>
<span class="cm">   (tl : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ())),</span>
<span class="cm">     C ((λ (idx : unit), psum.inl idx) ()) hd →</span>
<span class="cm">     C ((λ (idx : unit), psum.inr idx) ()) tl →</span>
<span class="cm">     C ((λ (idx : unit), psum.inr idx) ()) (_nest_1_1._nest_1_1.bad._mut_.cons_1 hd tl)) →</span>
<span class="cm">  Π {a : psum unit unit} (n : _nest_1_1._nest_1_1.bad._mut_ a), C a n</span>
<span class="cm">_nest_1_1.bad : Type</span>
<span class="cm">_nest_1_1.bad.bad : _nest_1_1.list.bad → _nest_1_1.bad</span>
<span class="cm">_nest_1_1.bad.rec : Π (C : _nest_1_1.bad → Sort l),</span>
<span class="cm">  (Π (a : _nest_1_1.list.bad), C (_nest_1_1.bad.bad a)) → Π (x : _nest_1_1.bad), C x</span>
<span class="cm">_nest_1_1.list.bad : Type</span>
<span class="cm">_nest_1_1.list.bad.cons : _nest_1_1.bad → _nest_1_1.list.bad → _nest_1_1.list.bad</span>
<span class="cm">_nest_1_1.list.bad.nil : _nest_1_1.list.bad</span>
<span class="cm">_nest_1_1.list.bad.rec : Π (C : _nest_1_1.list.bad → Sort l),</span>
<span class="cm">  C _nest_1_1.list.bad.nil →</span>
<span class="cm">  (Π (hd : _nest_1_1.bad) (tl : _nest_1_1.list.bad), C tl → C (_nest_1_1.list.bad.cons hd tl)) →</span>
<span class="cm">  Π (x : _nest_1_1.list.bad), C x</span>
<span class="cm">...</span>
<span class="cm">-/</span>
</pre></div>

#### [ Mario Carneiro (Oct 13 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135713821):
<p>When Lean 4 comes around, though, I will have to add another chapter on this mess because nested inductives are coming to a kernel near you</p>

#### [ Kevin Buzzard (Oct 13 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135720885):
<blockquote>
<p>but the real inductive type is <code>_nest_1_1._nest_1_1.bad._mut_</code>, and there are a bunch more theorems in that namespace:</p>
</blockquote>
<p>o_O so many consequences of one definition! I had no idea that these ones were there.</p>

#### [ Mario Carneiro (Oct 13 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135721078):
<p>that's not even all of them, I removed the usual theorems about <code>cases_on</code> and <code>rec_on</code> and <code>brec_on</code> and <code>ibelow</code> and <code>no_confusion</code> and <code>has_sizeof</code>. . .</p>

#### [ Mario Carneiro (Oct 13 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135721090):
<p>nested inductive translation seems kind of overcomplicated</p>

#### [ Kenny Lau (Oct 13 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722421):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">bad</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">bad</span> <span class="o">:</span> <span class="n">list</span> <span class="n">bad</span> <span class="bp">→</span> <span class="n">bad</span>

<span class="n">def</span> <span class="n">bad</span><span class="bp">.</span><span class="n">to_list</span> <span class="o">:</span> <span class="n">bad</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">bad</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">bad</span><span class="bp">.</span><span class="n">bad</span> <span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="n">L</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">bad</span> <span class="o">):</span> <span class="n">bad</span><span class="bp">.</span><span class="n">to_list</span> <span class="o">(</span><span class="n">bad</span><span class="bp">.</span><span class="n">bad</span> <span class="n">L</span><span class="o">)</span> <span class="bp">=</span> <span class="n">L</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">type mismatch, term</span>
<span class="cm">  rfl</span>
<span class="cm">has type</span>
<span class="cm">  ?m_2 = ?m_2</span>
<span class="cm">but is expected to have type</span>
<span class="cm">  bad.to_list (bad.bad L) = L</span>
<span class="cm">-/</span>
</pre></div>

#### [ Mario Carneiro (Oct 13 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722527):
<p>I don't think I need to say it since you've already found out: equation compiler on nested inductives doesn't produce defeq equation lemmas</p>

#### [ Mario Carneiro (Oct 13 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722530):
<p>this is one of the reasons equation lemmas are a thing</p>

#### [ Kenny Lau (Oct 13 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722531):
<p>what does canonicity mean?</p>

#### [ Mario Carneiro (Oct 13 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722577):
<p>the exact statement is a bit tricky, but basically every closed term reduces to a normal form which can be described explicitly by the type</p>

#### [ Mario Carneiro (Oct 13 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722580):
<p>i.e. for nat this means <code>succ $ ... $ 0</code></p>

#### [ Kenny Lau (Oct 13 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722584):
<p>but this error I found, it doesn't affect canonicity?</p>

#### [ Mario Carneiro (Oct 13 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722596):
<p>no because nothing there is an axiomatic constant</p>

#### [ Mario Carneiro (Oct 13 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722603):
<p>it's all a layer over the real inductive type</p>

#### [ Mario Carneiro (Oct 13 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722605):
<p>That theorem has to be proven by cases or induction or something internally so it's not defeq</p>

#### [ Kevin Buzzard (Oct 13 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722841):
<p>(warning: amateur alert). So this is exactly the situation where you can't prove your example by <code>rfl</code> (even though to naive eyes it looks like it should be <code>rfl</code>) so you prove it by hand (possibly using some weird theorems with weird names with <code>_</code> at the beginning), give it a good name, mark it as a simp lemma, and move on.</p>

#### [ Mario Carneiro (Oct 13 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722854):
<p>yes</p>

#### [ Mario Carneiro (Oct 13 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722855):
<p>except in this case lean did it all for you and slapped a nice API over the whole thing</p>

#### [ Mario Carneiro (Oct 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722865):
<p>In this case you can write <code>by rw bad.to_list</code> and it will use the equation lemmas for <code>bad.to_list</code>, which in this case are actually nontrivial theorems</p>

#### [ Kenny Lau (Oct 13 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722965):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">bad</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">bad</span> <span class="o">:</span> <span class="n">list</span> <span class="n">bad</span> <span class="bp">→</span> <span class="n">bad</span>

<span class="n">def</span> <span class="n">bad</span><span class="bp">.</span><span class="n">to_list</span> <span class="o">:</span> <span class="n">bad</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">bad</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">bad</span><span class="bp">.</span><span class="n">bad</span> <span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="n">L</span>

<span class="kn">theorem</span> <span class="n">bad</span><span class="bp">.</span><span class="n">very_bad</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="n">bad</span> <span class="o">):</span> <span class="n">bad</span><span class="bp">.</span><span class="n">to_list</span> <span class="o">(</span><span class="n">bad</span><span class="bp">.</span><span class="n">bad</span> <span class="n">L</span><span class="o">)</span> <span class="bp">=</span> <span class="n">L</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">bad</span><span class="bp">.</span><span class="n">to_list</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">bad</span><span class="bp">.</span><span class="n">very_bad</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem bad.very_bad : ∀ (L : list bad), bad.to_list (bad.bad L) = L :=</span>
<span class="cm">λ (L : list bad),</span>
<span class="cm">  eq.mpr (id (eq.rec (eq.refl (bad.to_list (bad.bad L) = L)) (bad.to_list.equations._eqn_1 L))) (eq.refl L)</span>
<span class="cm">-/</span>
</pre></div>

#### [ Mario Carneiro (Oct 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135723063):
<p>this is just a funny way of writing <code>bad.to_list.equations._eqn_1 L</code> of course</p>

#### [ Gabriel Ebner (Oct 13 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135725329):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks for the explanation, I'm looking forward to the canonicity result.  Tiny nitpick:</p>
<blockquote>
<p>it is not the case that i.e. <code>propext iff.rfl</code> reduces to <code>rfl</code>, which can spoil the inductive recursor case later. </p>
</blockquote>
<p>In this particular case it actually works out since <code>propext iff.rfl</code> has type <code>a = a</code> for some <code>a</code>, and then <code>eq.rec</code> reduces by axiom K.</p>


{% endraw %}
