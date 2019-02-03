---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/52642wellfoundedrecursionlexicographicordering.html
---

## Stream: [maths](index.html)
### Topic: [well-founded recursion & lexicographic ordering ?](52642wellfoundedrecursionlexicographicordering.html)

---


{% raw %}
#### [ Jack Crawford (Sep 14 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941390):
<p>Hi, I have a pleb question about how Lean infers whether recursion is well-founded or not.<br>
I'm writing a recursive function whose first two arguments are of type <code>fin m</code> and <code>fin n</code>,  and my algorithm:<br>
 1) always decreases the size of my <code>fin n</code><br>
 2) sometimes decreases the size of my <code>fin m</code><br>
I would think that Lean should be able to work out that my recursion is well-founded from the first fact alone, but it does not seem able.<br>
However, when I simply change the order that my arguments appear from <code>fin m -&gt; fin n -&gt; ...</code> to <code>fin n -&gt; fin m -&gt; ...</code> and nothing else (nontrivial), suddenly Lean recognises well-foundedness!</p>
<p>It seems that Lean is only trying to show well-foundedness from my first argument and can't work out that there should be well-foundedness on the lexicographic order of my <code>fin m</code> and <code>fin n</code>, or that just my <code>fin n</code> alone should suffice. Everything's sort of "doing what I want it to" except that I have to write the arguments to my function in an unconventional way. How can I tell Lean to just look for well-foundedness on my second argument (the <code>fin n</code>), or on the lexicographic pair of <code>fin m</code> and <code>fin n</code>, and not just purely on my <code>fin m</code>? Thanks!</p>

#### [ Kenny Lau (Sep 14 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941463):
<p>MWE</p>

#### [ Kevin Buzzard (Sep 14 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941803):
<p>By default Lean uses lexicographic ordering when trying to prove recursive functions are well-defined, so definitely the input order matters. The notes at <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md</a> probably tell you all you need to know</p>

#### [ Jack Crawford (Sep 14 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941855):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <br>
here's an MWE, compare the pair:</p>
<div class="codehilite"><pre><span></span>def mwe_aux {m n : ℕ} : Π (i : fin m) (j : fin n), bool
| ⟨0, h₁⟩ ⟨k₂, h₂⟩ := ff
| ⟨k₁+1, h₁⟩ ⟨0, h₂⟩ := ff
| ⟨k₁+1, h₁⟩ ⟨k₂+1, h₂⟩ :=
begin
    apply mwe_aux,
    from if k₂%2 = 0 then ⟨k₁, nat.lt_of_succ_lt h₁⟩ else ⟨k₁+1, h₁⟩,
    from ⟨k₂, nat.lt_of_succ_lt h₂⟩
end

def mwe_aux2 {m n : ℕ} : Π (j : fin n) (i : fin m), bool
| ⟨k₂, h₂⟩ ⟨0, h₁⟩ := ff
| ⟨0, h₂⟩ ⟨k₁+1, h₁⟩ := ff
| ⟨k₂+1, h₂⟩ ⟨k₁+1, h₁⟩ :=
begin
    apply mwe_aux2,
    from ⟨k₂, nat.lt_of_succ_lt h₂⟩,
    from if k₂%2 = 0 then ⟨k₁, nat.lt_of_succ_lt h₁⟩ else ⟨k₁+1, h₁⟩,
end
</pre></div>

#### [ Kevin Buzzard (Sep 14 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941878):
<p>the linked notes explain how to change the well-order on your input.</p>

#### [ Jack Crawford (Sep 14 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941927):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  ah oops I didn't see that before I responded to Kenny, thanks, I'll have a look!</p>

#### [ Kenny Lau (Sep 14 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941991):
<p>well I mean, what are you trying to do, instead of MWE of the error</p>


{% endraw %}
