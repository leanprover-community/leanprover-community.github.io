---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04369unfoldrefusestounfold.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [`unfold` refuses to unfold](https://leanprover-community.github.io/archive/113488general/04369unfoldrefusestounfold.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Arseniy Alekseyev (May 12 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471033):
<p>Here <code>t2_to_t1</code> is fully applied to a constructor, but lean still refuses to unfold/reduce. How so?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">t1</span>
<span class="bp">|</span> <span class="n">c1</span> <span class="o">:</span> <span class="n">t1</span>

<span class="kn">inductive</span> <span class="n">t2</span>
<span class="bp">|</span> <span class="n">c2</span> <span class="o">:</span> <span class="n">t2</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">def</span> <span class="n">t2_to_t1</span> <span class="o">:</span> <span class="n">t2</span> <span class="bp">→</span> <span class="n">t1</span>
<span class="bp">|</span> <span class="n">t2</span><span class="bp">.</span><span class="n">c2</span> <span class="o">:=</span> <span class="n">t1</span><span class="bp">.</span><span class="n">c1</span>

<span class="kn">theorem</span> <span class="n">hmm</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">t2</span><span class="o">),</span> <span class="o">(</span><span class="n">t1</span><span class="bp">.</span><span class="n">rec</span> <span class="mi">5</span> <span class="o">(</span><span class="n">t2_to_t1</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">5</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">unfold</span> <span class="n">t2_to_t1</span><span class="o">,</span>
    <span class="c1">-- simplify tactic failed to simplify</span>
    <span class="c1">--state:</span>
    <span class="c1">-- ⊢ t1.rec 5 (t2_to_t1 t2.c2) = 5</span>
</pre></div>

#### [ Mario Carneiro (May 12 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471093):
<p><code>rw</code> works</p>

#### [ Sebastian Ullrich (May 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471136):
<p><code>dunfold</code> too, probably?</p>

#### [ Mario Carneiro (May 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471137):
<p>and <code>dsimp</code></p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471138):
<p>yep, they all work</p>

#### [ Mario Carneiro (May 12 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471145):
<p>The problem is that it is a dependent function, so non-definitional rewrites don't necessarily work</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471188):
<p>you mean t1.rec is dependent so those tactics don't even try to rewrite it?</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471189):
<p>rewrite its argument*</p>

#### [ Mario Carneiro (May 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471191):
<p>it will only rewrite in certain locations, depending on the generated congr lemma</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471197):
<p>interesting</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471237):
<p>thanks!</p>

#### [ Mario Carneiro (May 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471242):
<div class="codehilite"><pre><span></span>open tactic
run_cmd do
  c ← mk_const `t1.rec &gt;&gt;= mk_congr_lemma,
  trace c.type

-- ∀ {C : t1 → Sort ?} (e_1 e_1_1 : C t1.c1), e_1 = e_1_1 →
--   ∀ (n : t1), t1.rec e_1 n = t1.rec e_1_1 n
``
</pre></div>

#### [ Mario Carneiro (May 12 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471249):
<p>as you can see from the type, it only rewrites the first argument, the <code>n</code> is fixed on both sides</p>

#### [ Mario Carneiro (May 12 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471294):
<p>here's what you would get with a less dependent function:</p>
<div class="codehilite"><pre><span></span>run_cmd do
  c ← mk_const `has_add.add &gt;&gt;= mk_congr_lemma,
  trace c.type
-- ∀ {α : Type ?} [c : has_add α] (a a_1 : α), a = a_1 →
--   ∀ (a_2 a_3 : α), a_2 = a_3 → a + a_2 = a_1 + a_3
</pre></div>

#### [ Arseniy Alekseyev (May 12 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471295):
<p>is it based purely on the type of the function?</p>

#### [ Mario Carneiro (May 12 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471306):
<p>There is a general procedure for generating "congruence" theorems such as these. The only input is the type of the function, and as you can see it doesn't really try to rewrite in dependent argument positions</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471349):
<p>right</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471353):
<p>because it doesn't even work in general for higher-than-Prop sorts, is that right?</p>

#### [ Mario Carneiro (May 12 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471360):
<p>The cool part is that it will automatically use known <code>subsingleton</code> arguments to change values without any equality hypothesis. In particular, that means that proof arguments can be freely rewritten</p>

#### [ Mario Carneiro (May 12 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471400):
<p>even if they are dependent on some earlier argument</p>

#### [ Mario Carneiro (May 12 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471401):
<p>This is where the <code>simp</code> approach to rewriting wins over <code>rw</code></p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471463):
<p>I didn't get that (I don't know where <code>subsingleton</code> instances would come from).</p>

#### [ Mario Carneiro (May 12 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471464):
<div class="codehilite"><pre><span></span>example (f : ∀ n : ℕ, n &gt; 0 → ℕ) (x : ℕ) (x0 : 0 + x &gt; 0) : f (0 + x) x0 = 1 :=
by simp; admit

example (f : ∀ n : ℕ, n &gt; 0 → ℕ) (x : ℕ) (x0 : 0 + x &gt; 0) : f (0 + x) x0 = 1 :=
by rw zero_add; admit --error: motive is not type correct
</pre></div>

#### [ Mario Carneiro (May 12 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471505):
<p>after the <code>simp</code>, the goal looks like <code>f x _ = 1</code> where <code>_</code> is some proof depending on the equality that was used to rewrite</p>

#### [ Mario Carneiro (May 12 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471513):
<p>whereas <code>rw</code> attempts to rewrite to <code>f x x0</code> and then gives up when it finds out this is not type correct</p>

#### [ Mario Carneiro (May 12 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471517):
<p><code>subsingleton</code> is a typeclass, it is inferred by typeclass inference</p>

#### [ Mario Carneiro (May 12 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471567):
<p>For example, <code>decidable p</code> is a subsingleton, because any two instances of <code>decidable p</code> must either both be <code>of_true</code> or both <code>of_false</code></p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471569):
<p>oh, "proof arguments" as in arguments that are themselves proofs rather than arguments of proofs. I guess all <code>Prop</code>s are subsingletons then?</p>

#### [ Mario Carneiro (May 12 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471574):
<p>All elements of Prop are subsingletons</p>

#### [ Mario Carneiro (May 12 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471575):
<p>if <code>p : Prop</code> and <code>h1 h2 : p</code> then <code>h1 = h2</code></p>

#### [ Mario Carneiro (May 12 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471616):
<p>that equality is definitional, but <code>simp</code> will use it even if it is not definitional like in the <code>decidable p</code> example</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471621):
<p>right, cool</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471626):
<p>what's "sub" about this notion of singleton?</p>

#### [ Mario Carneiro (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471627):
<p><code>empty</code> is a subsingleton too</p>

#### [ Mario Carneiro (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471628):
<p><code>subsingleton A</code> is defined to mean that if <code>a b : A</code> then <code>a = b</code>; classically that means <code>A</code> is a singleton or empty</p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471629):
<p>ah, of course!</p>

#### [ Mario Carneiro (May 12 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471673):
<p>"singleton" is usually stated as <code>\ex a, \all b, a = b</code></p>

#### [ Arseniy Alekseyev (May 12 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471774):
<p>subsingleton is what they call proposition in hott land, isn't it? Interestingly, it's one truncation hierarchy level <em>higher</em> than singleton there.</p>

#### [ Mario Carneiro (May 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471835):
<p>Yes, if you are familiar with HoTT terminology then "singleton" is "contractible" is -2 truncated, and "subsingleton" is "proposition" is -1 truncated. "set" or 0 truncated is true of all types in lean, because equality is a proposition.</p>

#### [ Mario Carneiro (May 12 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60unfold%60%20refuses%20to%20unfold/near/126471879):
<p>I also find it a bit funny that -2 truncated types have elements while -1 truncated types may not, but the ordering there makes sense: every -2 truncated type is -1 truncated but not the other way around.</p>


{% endraw %}
