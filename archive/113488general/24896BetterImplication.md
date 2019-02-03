---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24896BetterImplication.html
---

## Stream: [general](index.html)
### Topic: [Better Implication](24896BetterImplication.html)

---


{% raw %}
#### [ Nima (Apr 19 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287484):
<p>I can write <code>if h:cnd then aa else bb</code>.<br>
Inside each breach, I have access to <code>h</code>.<br>
Suppose I only want to write something like <code>h:cnd → aa</code> (<code>else</code> branch is <code>true</code>).<br>
Is there anyway to do this without writing <code>if h:cnd then aa else true</code>?<br>
The similar question is for <code>h:cnd ∧ aa</code>.<br>
I rather not use <code>∀h:cnd, aa</code>, since if I have <code>cnd</code> or its complement in local hypotheses, <code>simp</code> does not simplify.</p>

#### [ Kenny Lau (Apr 19 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287490):
<p>just write <code>cnd -&gt; aa</code>?</p>

#### [ Nima (Apr 19 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287549):
<p>I want to use <code>h</code> in RHS</p>

#### [ Nima (Apr 19 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287801):
<p>Here is an example (please ignore the actual definitions, just the usage),</p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="n">def</span> <span class="n">exp</span> <span class="o">(</span><span class="n">a</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span><span class="n">a</span><span class="bp">≠</span><span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- some function that takes an input and requires something to be true about that input</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">:</span><span class="n">α</span><span class="o">,</span> <span class="n">h</span><span class="o">:</span><span class="n">a</span><span class="bp">≠</span><span class="mi">0</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">exp</span> <span class="n">a</span> <span class="n">h</span> <span class="c1">-- for any `a` in the domain of `exp`, we have some property</span>
</pre></div>

#### [ Kenny Lau (Apr 19 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287816):
<p>the "standard" approach in mathlib is to define the function without assuming the condition, and prove the theorems assuming the condition</p>

#### [ Kenny Lau (Apr 19 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287820):
<p>i.e. don't make the condition one of the arguments to the function</p>

#### [ Nima (Apr 19 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287938):
<p>Not sure that is what I wanted. For example, I can always use <code>if then else</code>, but then one branch is always useless. I was looking for a solution to this problem, not erasing it. ;)</p>

#### [ Kenny Lau (Apr 19 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125287961):
<p>I don't recommend using <code>if then else</code> at all</p>

#### [ Mario Carneiro (Apr 19 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288045):
<p>You should use <code>∀h:cnd, aa</code> in this case</p>

#### [ Nima (Apr 19 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288152):
<p>Well, <code>simp</code> does not handle <code>∀h:cnd, aa</code> when I have <code>h:cnd</code> in local hypotheses. Right? Any other way, to automatically simplify <code>∀h:cnd, aa</code> (this will be more serious when the quantification is part of a bigger condition)</p>

#### [ Kenny Lau (Apr 19 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288268):
<p><code>specialize</code></p>

#### [ Mario Carneiro (Apr 19 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288534):
<p>I see. Tell me whether these simp lemmas work in your use-case:</p>
<div class="codehilite"><pre><span></span>@[simp] theorem forall_prop_of_true {p : Prop} {q : p → Prop} (h : p) : (∀ h&#39; : p, q h&#39;) ↔ q h :=
@forall_const (q h) p ⟨h⟩

@[simp] theorem exists_prop_of_true {p : Prop} {q : p → Prop} (h : p) : (∃ h&#39; : p, q h&#39;) ↔ q h :=
@exists_const (q h) p ⟨h⟩

@[simp] theorem forall_prop_of_false {p : Prop} {q : p → Prop} (hn : ¬ p) : (∀ h&#39; : p, q h&#39;) ↔ true :=
iff_true_intro $ λ h, hn.elim h

@[simp] theorem exists_prop_of_false {p : Prop} {q : p → Prop} : ¬ p → ¬ (∃ h&#39; : p, q h&#39;) :=
mt Exists.fst
</pre></div>

#### [ Mario Carneiro (Apr 19 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288622):
<p>But I will remark that this situation is rather rare in mathlib, because we try to avoid partial functions, which tend to make rewriting difficult. From the code you've shown here before, you seem to prefer partial functions</p>

#### [ Nima (Apr 19 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125288748):
<p>Thank you, they help.<br>
Did you just wrote them?<br>
Also, the last one does not type check.</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289030):
<p>Yes I did. For the last one you should have <code>logic.basic</code> imported</p>

#### [ Nima (Apr 19 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289044):
<p>I haven't done anything about code generation. But what I have in mind is a type that take parameters and has different fields based on values of those parameters. In C++, I can easily use template to have those fields defined based on the input template arguments. In Lean, I am trying to have the same effect, by making sure that every time I am reading a field, it is defined.</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">constraint</span>
          <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
          <span class="o">(</span><span class="n">trvk</span> <span class="o">:</span> <span class="n">triviality_kind</span><span class="o">)</span>
          <span class="o">(</span><span class="n">dirk</span> <span class="o">:</span> <span class="n">direction_kind</span> <span class="o">)</span>
          <span class="o">(</span><span class="n">strk</span> <span class="o">:</span> <span class="n">strictness_kind</span><span class="o">)</span>
          <span class="o">:=</span>
<span class="n">cnstr</span> <span class="bp">::</span>
  <span class="o">(</span><span class="n">tri</span> <span class="o">:</span> <span class="n">trvk</span> <span class="bp">=</span> <span class="n">triviality_kind</span><span class="bp">.</span><span class="n">kdyn</span> <span class="bp">→</span> <span class="n">triviality</span><span class="o">)</span>
  <span class="o">(</span><span class="n">str</span> <span class="o">:</span> <span class="n">strk</span> <span class="bp">=</span> <span class="n">strictness_kind</span><span class="bp">.</span><span class="n">kdyn</span> <span class="bp">→</span> <span class="n">strictness</span><span class="o">)</span>
  <span class="o">(</span><span class="n">bnd</span> <span class="o">:</span> <span class="n">trvk</span> <span class="bp">≠</span> <span class="n">triviality_kind</span><span class="bp">.</span><span class="n">ktrv</span> <span class="bp">→</span> <span class="n">α</span>         <span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Apr 19 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289117):
<p>(I'm assuming the reason it doesn't typecheck is because it says <code>Exists.fst</code> can't be found; that's a hint.)</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289180):
<p>I would suggest using an inductive type to encode these constraints</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289239):
<p>I think it will be easier for you to return a default value when you can, and an option when there is no reasonable default, to totalize your functions. If you are going for efficiency, this won't achieve it anyway due to thunk generation</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289284):
<p>Could you link to your files where you define these <code>triviality_kind</code> etc? Let me make a mockup</p>

#### [ Nima (Apr 19 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289353):
<p>I used that first, but it has its own problem.<br>
For example, suppose I have two constraints and I want to add them.<br>
But not only I want to define addition for constraints with the same type parameters, but also in case the result cannot be represented by a constraint, I want to return a smallest representable constraint that is of the right type. If I push everything inside one inductive type, then I have to put extra condition on the signature of addition (or I don't know how else I can do it).<br>
<a href="https://github.com/nima-roohi/lets-learn-some-lean" target="_blank" title="https://github.com/nima-roohi/lets-learn-some-lean">https://github.com/nima-roohi/lets-learn-some-lean</a></p>

#### [ Mario Carneiro (Apr 19 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289504):
<p>What does adding constraints mean here? If I understand your model correctly, you want to be able to represent the sets <code>true</code>, <code>{x | x R a}</code>, and <code>{x | a R x}</code> where <code>R</code> is <code>&lt;=</code> or <code>&lt;</code>. Does adding the sets mean all pointwise additions, i.e. <code>{x + y | x \in c1, y \in c2}</code>, or the intersection / union of constraints or something else?</p>

#### [ Nima (Apr 19 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289557):
<p><code>addition</code> is just an example. You can assume pointwise addition as you defined.<br>
If <code>α</code> is, for example, <code>float</code> then even addition of two constraints cannot always be represented by a constraint.</p>

#### [ Nima (Apr 19 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289665):
<p>Is there anyway I can change this <code>notation</code> so the example will work?</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span>  <span class="n">c</span><span class="bp">`</span><span class="o">:</span><span class="bp">`</span><span class="n">h</span> <span class="bp">`→`</span> <span class="n">hh</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">c</span><span class="o">:</span><span class="n">h</span> <span class="k">then</span> <span class="n">hh</span> <span class="k">else</span> <span class="n">true</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="mi">1</span><span class="bp">&gt;</span><span class="mi">2</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">1</span><span class="bp">&gt;</span><span class="mi">2</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Apr 19 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289768):
<p>Here's more or less what I'm thinking:</p>
<div class="codehilite"><pre><span></span>import algebra.ordered_group

inductive constraint (α : Type*)
| triv {} : constraint
| le : α → constraint
| lt : α → constraint
| ge : α → constraint
| gt : α → constraint

namespace constraint

def is_trivial {α} : constraint α → bool
| constraint.triv := tt
| _ := ff

def get_bound {α} : constraint α → option α
| constraint.triv := none
| (constraint.le a) := some a
| (constraint.lt a) := some a
| (constraint.ge a) := some a
| (constraint.gt a) := some a
--add others to taste, but you shouldn&#39;t need them

protected def mem {α} [preorder α] (x : α) : constraint α → Prop
| constraint.triv := true
| (constraint.le a) := a ≤ x
| (constraint.lt a) := a &lt; x
| (constraint.ge a) := x ≤ a
| (constraint.gt a) := x &lt; a

instance {α} [preorder α] : has_mem α (constraint α) := ⟨constraint.mem⟩

protected def add {α} [ordered_comm_group α] : constraint α → constraint α → constraint α
| constraint.triv c2 := c2
| c1 constraint.triv := c1
| (constraint.le a) (constraint.le b) := constraint.le (a + b)
| (constraint.le a) (constraint.lt b) := constraint.lt (a + b)
| (constraint.lt a) (constraint.le b) := constraint.lt (a + b)
| (constraint.lt a) (constraint.lt b) := constraint.lt (a + b)
| (constraint.ge a) (constraint.ge b) := constraint.ge (a + b)
| (constraint.ge a) (constraint.gt b) := constraint.gt (a + b)
| (constraint.gt a) (constraint.ge b) := constraint.gt (a + b)
| (constraint.gt a) (constraint.gt b) := constraint.gt (a + b)
| _ _ := constraint.triv

instance {α} [ordered_comm_group α] : has_add (constraint α) := ⟨constraint.add⟩

end constraint
</pre></div>

#### [ Mario Carneiro (Apr 19 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125289820):
<p>You can't define the arrow and colon as notations; they are reserved for function types</p>

#### [ Nima (Apr 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125290011):
<p>I see what you mean by making a function total.<br>
May be that makes things easier.<br>
But I am not sure about performance of the result code.<br>
Also, in your definition you only have one <code>le</code>, but I have two of them (dynamic vs static). So if every time I have to write all the cases, that might be a problem itself.</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125290452):
<p>Okay, version 2:</p>
<div class="codehilite"><pre><span></span>import algebra.ordered_group

inductive direction | lower | upper

inductive constraint (α : Type*)
| triv {} : constraint
| mk (dir : direction) (strict : bool) (dynamic : bool) (bound : α) : constraint

namespace constraint
open direction

def is_trivial {α} : constraint α → bool
| triv := tt
| _ := ff

def get_bound {α} : constraint α → option α
| triv := none
| (mk a s d b) := some b

protected def mem {α} [preorder α] (x : α) : constraint α → Prop
| triv := true
| (mk lower ff d a) := a ≤ x
| (mk lower tt d a) := a &lt; x
| (mk upper ff d a) := x ≤ a
| (mk upper tt d a) := x &lt; a

instance {α} [preorder α] : has_mem α (constraint α) := ⟨constraint.mem⟩

protected def add {α} [ordered_comm_group α] : constraint α → constraint α → constraint α
| (mk lower s1 d1 a) (mk lower s2 d2 b) := mk lower (s1 || s2) (d1 || d2) (a + b)
| (mk upper s1 d1 a) (mk upper s2 d2 b) := mk upper (s1 || s2) (d1 || d2) (a + b)
| _ _ := constraint.triv

instance {α} [ordered_comm_group α] : has_add (constraint α) := ⟨constraint.add⟩

end constraint
</pre></div>

#### [ Nima (Apr 19 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125290742):
<p>Thank you.<br>
I guess the biggest difference between what you wrote and what I have is that, assuming we are defining the same concept, in my definition when <code>dynamic</code> is <code>ff</code> then there is no field named <code>strict</code> (at least intuitively). If I preserve that restriction throughout my definition, (I hope) that transforming these into a code would be easier, at least when I do it manually!!</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Better%20Implication/near/125291309):
<p>I'm making up stuff as I go along re: the actual semantics, but I assume it looks something like this:</p>
<div class="codehilite"><pre><span></span>import algebra.ordered_group

inductive direction | lower | upper
inductive strictness | stt | nst | dyn

namespace strictness

def is_strict : strictness → bool
| stt := tt
| _ := ff

def join : strictness → strictness → strictness
| dyn _ := dyn
| _ dyn := dyn
| stt _ := stt
| _ stt := stt
| _ _ := nst

end strictness

inductive constraint (α : Type*)
| triv {} : constraint
| mk (dir : direction) (strict : strictness) (bound : α) : constraint

namespace constraint
open direction

def is_trivial {α} : constraint α → bool
| triv := tt
| _ := ff

def get_bound {α} : constraint α → option α
| triv := none
| (mk a s b) := some b

protected def mem {α} [preorder α] (x : α) : constraint α → Prop
| triv := true
| (mk lower s a) := if s.is_strict then a &lt; x else a ≤ x
| (mk upper s a) := if s.is_strict then x &lt; a else x ≤ a

instance {α} [preorder α] : has_mem α (constraint α) := ⟨constraint.mem⟩

protected def add {α} [ordered_comm_group α] : constraint α → constraint α → constraint α
| (mk lower s1 a) (mk lower s2 b) := mk lower (s1.join s2) (a + b)
| (mk upper s1 a) (mk upper s2 b) := mk upper (s1.join s2) (a + b)
| _ _ := constraint.triv

instance {α} [ordered_comm_group α] : has_add (constraint α) := ⟨constraint.add⟩

end constraint
</pre></div>


{% endraw %}
