---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63906Automaticvariablenames.html
---

## Stream: [general](index.html)
### Topic: [Automatic variable names](63906Automaticvariablenames.html)

---


{% raw %}
#### [ Patrick Stevens (May 29 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275253):
<p>Another noob question, sorry. I haven't found an answer out there because everyone always proves this theorem using <code>simp</code>.</p>
<p>I've defined <code>myNat</code> in the obvious inductive way (<code>zero : myNat</code>, and <code>succ : myNat -&gt; myNat</code>), and then defined <code>my_add</code> by cases as <code>| myNat.zero n := n</code> and <code>| (myNat.succ m) n := myNat.succ (my_add m n)</code>. To prove the theorem <code>addZero : (forall m : myNat, my_add m myNat.zero = m)</code> without using simp, I entered tactic mode and began with <code>assume m : myNat, induction m, refl</code> to take care of the base case. Now I have the goal to prove it for the successor case, and the Tactic State tells me that I have <code>m_a : myNat</code> and <code>m_ih : my_add m_a myNat.zero = m_a</code>. But when I try to reference these terms with <code>have (my_add (myNat.succ m_a) myNat.zero) = (myNat.succ (my_add m_a myNat.zero)), from sorry</code>, I get multiple syntax errors, one of which is "unknown identifier 'm_a'".</p>

#### [ Kenny Lau (May 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275311):
<p>post your code?</p>

#### [ Patrick Stevens (May 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275314):
<p>Have I got some syntax wrong, and if not, how do I reference variables that <code>induction</code> introduced?</p>

#### [ Andrew Ashworth (May 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275316):
<p>^ can you paste it in a formatted code block</p>

#### [ Patrick Stevens (May 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275360):
<p>Sorry - it really did come out pretty unreadable, hang on</p>

#### [ Patrick Stevens (May 29 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275438):
<div class="codehilite"><pre><span></span>inductive myNat : Type
| zero : myNat
| succ : myNat → myNat

axiom zeroIsNotASuccessor : (∀ n : myNat, ¬(myNat.succ n = myNat.zero))
axiom succPreservesInequality: (∀ n m : myNat, (¬(m = n)) → ¬(myNat.succ m = myNat.succ n))

definition my_add : myNat -&gt; myNat -&gt; myNat
| myNat.zero n := n
| (myNat.succ m) n := myNat.succ (my_add m n)

theorem addZero : (∀ m : myNat, my_add m myNat.zero = m) :=
begin
    assume m : myNat,
    induction m,
    refl,
    have (my_add (myNat.succ m_a) myNat.zero) = (myNat.succ (my_add m_a myNat.zero)), from
    begin
        sorry
    end
end
</pre></div>

#### [ Kenny Lau (May 29 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275455):
<p><code>have :</code></p>

#### [ Patrick Stevens (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275520):
<p>Ah, thanks - why was that colon not necessary in e.g.</p>
<div class="codehilite"><pre><span></span>example:p ∧ ¬q → ¬(p → q):=
begin
    intro h,
    assume hpq : p → q,
    cases h with hp hnq,
    have hq : q, from hpq hp,
    exact hnq hq
end
</pre></div>

#### [ Kenny Lau (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275532):
<p>it was</p>

#### [ Patrick Stevens (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275533):
<p>Oh, I get it - an anonymous member of the equality type</p>

#### [ Patrick Stevens (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275536):
<p>Sorry</p>

#### [ Kenny Lau (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275541):
<p><code>have :</code> sets the name to <code>this</code></p>

#### [ Kenny Lau (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275542):
<p><code>have hq :</code> sets the names to <code>hq</code></p>

#### [ Patrick Stevens (May 29 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275590):
<p>cheers</p>

#### [ Kevin Buzzard (May 30 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127277391):
<p>I never know whether using <code>have :...</code> (and thus making a variable called <code>this</code>) is bad style.</p>

#### [ Kevin Buzzard (May 30 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127277444):
<p>I tend to name all my have variables except for the ones I instantly use and throw away on the next line</p>


{% endraw %}
