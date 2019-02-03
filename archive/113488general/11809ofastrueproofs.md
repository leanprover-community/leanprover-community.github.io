---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11809ofastrueproofs.html
---

## Stream: [general](index.html)
### Topic: [of_as_true proofs](11809ofastrueproofs.html)

---


{% raw %}
#### [ Joe Hendrix (Dec 28 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152632359):
<p>I'm trying to build up a mental model of the efficiency of using decidable predicates to construct proofs in tactics..<br>
Let's say I have a decidable predicate <code>P : nat -&gt; Prop</code> with an instance <code>h : decidable_pred P</code>, and a concrete value <code>x : nat</code> in a tactic.  <br>
I can match on <code>h x</code> within the tactic monad (which I think is using the VM), and see if the prop is true or false.<br>
However, I'd also like to have an expression for the proof of <code>P x</code>.  I seem to be able to do that via an expression like <code>@of_as_true _ (h x) trivial</code>, but I think this results in the elaborator needing to reduce <code>h x</code> to whnf.  I think of this as slower than the VM, since among other things nat will have a unary representation. <br>
Is the above correct, and is so is there some way like reflection to have the VM (or the compiler in Lean 4) run <code>h x</code> and efficiently construct the needed proof?</p>

#### [ Mario Carneiro (Dec 28 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152634914):
<p>No, you can't directly produce a "fast" kernel proof from a "fast" VM function. For many common operations on <code>nat</code>, <code>norm_num</code> will produce efficient kernel proofs using VM evaluation to guide the construction, but the method is generally completely different than what the decidable instance does</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638440):
<p>Good to know I'm not missing something.  I think it would be useful to have some way to write a verified decision procedure in logic mode, and then be able to use it to discharge proof obligations in tactic mode.<br>
For similar reasons, I started down the path of building up <code>has_reflect</code> instances for datatypes in proofs (e.g., <code>has_reflect (and P Q)</code>), but it's (1) a lot of work, and (2) still unclear how to support for some properties.  Specifically, I have <code>decidable (\forall (x : fin n), P x)</code>, but I'm struck on <code>has_reflect (\forall (x : fin n), P x)</code>.</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638542):
<p>hm, that's an interesting use of <code>has_reflect</code>. Usually we don't use <code>has_reflect</code> for propositions, what's the goal here?</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638564):
<p>I think what you want is actually <code>decidable</code>, or at least <code>semidecidable</code> (where <code>semidecidable p</code> is basically <code>option p</code>)</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638567):
<p>but you are limited by the same things as <code>decidable</code> proofs</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638568):
<p>The idea for that use was to get the VM to produce the proof object using the decidable instance, then call <code>has_reflect.reflect</code> to construct the appropriate expression.</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638610):
<p>decidable instances don't have proof objects</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638613):
<p>they put all the computation in the kernel</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638624):
<p>I'm referring to the proof object <code>p</code> that is the argument to <code>decidable.is_true p</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638671):
<p>You could infer <code>decidable p</code>, normalize it to <code>is_true h</code> and return <code>h</code>, but this is going to be almost as slow as kernel computing it</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152638673):
<p>you are "elaborator computing" it in this case</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639243):
<p>I think I haven't been clear.  I use the tactic <code>decidable_tac</code> below that uses uses the elaborator fairly often.  As a work around to get more use of the VM, I was hoping to be able to use both <code>decidable</code> and <code>has_reflect</code> instances to get something a bit more efficient in the <code>decidable_reflected</code> tactic below:</p>
<div class="codehilite"><pre><span></span>meta def decidable_tac : tactic unit := do
  tgt ← tactic.target,
  tactic.apply ((`(@of_as_true) : expr) tgt),
  tactic.exact `(trivial)

meta def decidable_reflected (P:Prop) [h:decidable P] [g:has_reflect P] : tactic unit := do
  match h with
  | decidable.is_true p := tactic.exact (g p)
  | decidable.is_false q := tactic.fail &quot;Prop false&quot;
  end
</pre></div>


<p>Unfortunately, I can't actually write the necessary <code>has_reflect</code> instances.  It seems like I would need some more support within Lean (perhaps constants that auto generated reflect instances for propositions).</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639535):
<p>You can't write <code>has_reflect</code> instances for many propositions</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639536):
<p>like <code>or</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639635):
<p>A <code>has_reflect</code> instance is a function that produces an expression that is a proof of <code>p</code>, provided <code>p</code> is in fact true</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639645):
<p>So <code>decidable p</code> implies <code>has_reflect p</code> because you can evaluate the decidable instance and take the proof out</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639695):
<p>Yep, I got <code>and</code> and <code>true</code>  and thought this would work, then got stuck with forall.  I tried <code>or</code> while writing up the example, and got the error about only being able to return a value of type <code>P</code>.</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639711):
<p>If you know one or the other of the propositions is decidable, you can reflect an <code>or</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639715):
<p>but really decidable is the one you want, it's closed under all the operations</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639761):
<p>Here was my attempt at <code>or</code>, but I can't match on the or value due to proof irrelevance:</p>
<div class="codehilite"><pre><span></span>meta instance or.reflect (P Q : Prop) [reflected P] [reflected Q] [hp:has_reflect P] [hq:reflected Q]
: has_reflect (P ∨ Q)
| (or.inl p) := `(or.inl).subst (hp p)
| (or.inr q) := `(or.inr).subst (hq q)
</pre></div>

#### [ Mario Carneiro (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639766):
<p>exactly</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639768):
<p>In a tactic, a proof value isn't very useful. It's only going to help avoid some code paths that weren't going to be exercised anyway</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639769):
<p>Interesting <code>and</code> did not complain even though it looks like it recurses:</p>
<div class="codehilite"><pre><span></span>meta instance and.reflect (P Q : Prop) [reflected P] [reflected Q] [hp:has_reflect P] [hq:has_reflect Q]
: has_reflect (P ∧ Q)
| ⟨p,q⟩ := (`(and.intro).subst (hp p)).subst (hq q)
</pre></div>

#### [ Mario Carneiro (Dec 28 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639770):
<p><code>and</code> has large elimination because it only has one constructor</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639815):
<p>The proof value is needed just so I can discharge theorems I'm proving.</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639823):
<p>so if you have a function <code>p -&gt; expr</code> coming from your has reflect instance, you could just as well have a function producing <code>option expr</code> with no proof preconditions</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639879):
<p>So when you are writing a has_reflect instance you are just constructing a proof from nothing. Sometimes that's easy, like <code>and</code>, sometimes that requires backtracking like <code>or</code>, and sometimes it's really hard</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639936):
<p>How are you supposed to use <code>decidable_reflected</code>?</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639938):
<p>nothing says what <code>P</code> is</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639949):
<p>it seems like it's mixing meta levels, and that's why you need <code>has_reflect</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639952):
<p><code>decidable_tac</code> is the same as <code>exact_dec_trivial</code> afaict</p>

#### [ Joe Hendrix (Dec 28 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152639997):
<p>Let me work on an example.  Is <code>exact_dec_trivial</code> in Lean standard library or mathlib?</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640005):
<p>It's in mathlib, but it's literally <code>exact dec_trivial</code> which is core only</p>

#### [ Joe Hendrix (Dec 28 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640062):
<p>I forget why I didn't just use <code>exact dec_trivial</code> -- I may not have known about it, I've used that tactic for a while now.</p>

#### [ Mario Carneiro (Dec 28 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640118):
<p>note that <code>dec_trivial</code> is notation for <code>of_as_true (by trivial)</code>; the tactic is there I think to stage the elaboration</p>

#### [ Mario Carneiro (Dec 28 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640234):
<p>Okay, so I think I understand now what you are trying to do. You need a combination of <code>decidable</code> and <code>has_reflect</code> that produces exprs rather than proof values. You can automatically construct one by reflecting a decidable instance, but you can also produce much smarter proofs for nats and such</p>

#### [ Joe Hendrix (Dec 28 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152640287):
<p>That's right.  I want proof search to run within the VM (or compiler in Lean 4), then either I can reflect on the generated proof, or maybe just have some magic constant that pretends to do it for me (say a safe version of <code>sorry</code>).<br>
(edit, apparently I can't spell)</p>

#### [ Mario Carneiro (Dec 28 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152641068):
<p><span class="user-mention" data-user-id="110994">@Joe Hendrix</span> Here's an example of what I mean. Unfortunately I had to fight lean somewhat to write the instance, possibly the ergonomics of instance writing needs work.</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">class</span><span class="o">]</span> <span class="n">meta</span> <span class="kn">inductive</span> <span class="n">reflect_decidable</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">is_true</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="c">/-</span><span class="cm">reflected h-/</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">reflect_decidable</span>
<span class="bp">|</span> <span class="n">is_false</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="c">/-</span><span class="cm">reflected h-/</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">reflect_decidable</span>
<span class="kn">open</span> <span class="n">reflect_decidable</span>

<span class="n">meta</span> <span class="kn">instance</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="n">reflected</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">reflected</span> <span class="n">q</span><span class="o">]</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">[</span><span class="n">reflect_decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">reflect_decidable</span> <span class="n">q</span><span class="o">],</span>
  <span class="n">reflect_decidable</span> <span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">is_true</span> <span class="n">h</span> <span class="n">e</span><span class="o">)</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">h</span><span class="o">)</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="bp">@</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="n">e</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">(</span><span class="n">is_true</span> <span class="n">h</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">h</span><span class="o">)</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="bp">@</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="n">e</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">is_false</span> <span class="n">h₁</span> <span class="n">e₁</span><span class="o">)</span> <span class="o">(</span><span class="n">is_false</span> <span class="n">h₂</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">is_false</span> <span class="o">(</span><span class="n">not_or</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">)</span> <span class="o">(</span><span class="n">expr</span><span class="bp">.</span><span class="n">mk_app</span> <span class="bp">`</span><span class="o">(</span><span class="bp">@</span><span class="n">not_or</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span> <span class="o">[</span><span class="n">e₁</span><span class="o">,</span> <span class="n">e₂</span><span class="o">])</span>

<span class="n">meta</span> <span class="kn">instance</span> <span class="o">:</span> <span class="n">reflect_decidable</span> <span class="n">true</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="n">trivial</span> <span class="bp">`</span><span class="o">(</span><span class="n">trivial</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">tactic</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">by_reflection</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">tgt</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">ty</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">(</span><span class="n">reflect_decidable</span> <span class="err">%%</span><span class="n">tgt</span><span class="o">),</span>
  <span class="n">inst</span> <span class="err">←</span> <span class="n">mk_instance</span> <span class="n">ty</span><span class="o">,</span>
  <span class="n">is_true</span> <span class="bp">_</span> <span class="n">e</span> <span class="err">←</span> <span class="bp">@</span><span class="n">tactic</span><span class="bp">.</span><span class="n">eval_expr</span> <span class="o">(</span><span class="n">reflect_decidable</span> <span class="n">true</span><span class="o">)</span>
    <span class="o">(</span><span class="k">by</span> <span class="n">delta</span> <span class="n">reflected</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">ty</span><span class="o">)</span> <span class="n">inst</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">e</span>

<span class="n">def</span> <span class="n">ex</span> <span class="o">:</span> <span class="n">true</span> <span class="bp">∨</span> <span class="n">true</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">by_reflection</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">ex</span> <span class="c1">-- or.inl trivial</span>
</pre></div>

#### [ Joe Hendrix (Dec 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152644194):
<p>That would kind of work.  One downside is that <code>reflect_decidable</code> is meta.  I'm interested in trying to write provably correct decision procedures, not just proof producing.  I'll try this approach in the short term though.</p>

#### [ Mario Carneiro (Dec 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152645158):
<p>it has to be meta, because it's creating <code>expr</code>s</p>

#### [ Mario Carneiro (Dec 28 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152645165):
<p>this is a limitation of lean 3 tactic framework</p>

#### [ Mario Carneiro (Dec 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/of_as_true%20proofs/near/152645210):
<p>You could create objects that are like <code>expr</code> but not meta, and then post process at the end, but that would add some extra overhead</p>


{% endraw %}
