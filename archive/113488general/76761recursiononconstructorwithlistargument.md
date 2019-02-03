---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76761recursiononconstructorwithlistargument.html
---

## Stream: [general](index.html)
### Topic: [recursion on constructor with list argument](76761recursiononconstructorwithlistargument.html)

---


{% raw %}
#### [ Seul Baek (Jun 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursion%20on%20constructor%20with%20list%20argument/near/127832469):
<p>I'm experimenting with embedding first-order logic in Lean, and I'm using the following definition of terms : </p>
<div class="codehilite"><pre><span></span>inductive trm : Type
| var : nat → trm
| const : string → trm
| fn : string → list trm → trm
</pre></div>


<p>And I'd like to write some functions by recursion on terms. E.g., a function that replaces all occurrences of a variable in a term with a term : </p>
<div class="codehilite"><pre><span></span>def inst_trm (n : nat) (t : trm) : trm → trm
| (trm.var m) := if n = m then t else trm.var m
| (trm.fn s ts) := trm.fn s (list.map inst_trm ts)
| t&#39; := t&#39;
</pre></div>


<p>But it doesn't work, presumably because Lean can't automatically show argument decrease for the recursive calls to elements of <code>ts</code> in the second match case.</p>
<p>Now, it is possible to get around this problem by recursion on lists of terms...</p>
<div class="codehilite"><pre><span></span>def inst_trm_core (n t) : list trm → list trm
| [] := []
| (trm.var m :: ts) := ((if n = m then t else trm.var m) :: inst_trm_core ts)
| (trm.const s :: ts) := (trm.const s :: inst_trm_core ts)
| (trm.fn s ts1 :: ts2) := (trm.fn s (inst_trm_core ts1) :: inst_trm_core ts2)

instance : decidable_eq trm :=
by tactic.mk_dec_eq_instance

def list.head_nonempty {α : Type} : Π (l : list α), l ≠ [] → α
| [] h := by {exfalso, exact (h rfl)}
| (a::as) h := a

lemma inst_trm_core_nonempty (n t1 t2) : inst_trm_core n t1 [t2] ≠ [] :=
by {cases t2; intro h; exfalso;
    try {unfold inst_trm_core at h}; cases h}

def inst_trm (n : nat) (t1 t2 : trm) : trm :=
list.head_nonempty
  (inst_trm_core n t1 [t2])
  (inst_trm_core_nonempty _ _ _)
</pre></div>


<p>...but this does not feel quite right. I wonder if there's a better solution?</p>

#### [ Simon Hudon (Jun 09 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursion%20on%20constructor%20with%20list%20argument/near/127832568):
<p>I haven't tried it recently but you may be able to get an improvement by writing two mutually recursive functions: one on the list of terms and one on individual terms. This is the kind of feature that has improved quickly in the last year so I'm not sure at what point it is now.</p>

#### [ Mario Carneiro (Jun 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursion%20on%20constructor%20with%20list%20argument/near/127850700):
<p>This is a known issue with nested inductives. Like Simon suggests, you should use mutual recursion to define functions on the type.</p>

#### [ Seul Baek (Jun 10 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursion%20on%20constructor%20with%20list%20argument/near/127867644):
<p>Thank you. It looks a lot better with mutual recursion now.</p>


{% endraw %}
