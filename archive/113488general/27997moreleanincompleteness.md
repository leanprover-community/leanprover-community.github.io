---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27997moreleanincompleteness.html
---

## Stream: [general](index.html)
### Topic: [more lean incompleteness](27997moreleanincompleteness.html)

---


{% raw %}
#### [ Mario Carneiro (Apr 04 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20lean%20incompleteness/near/124609074):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> I found another place where I lie in the paper compared to lean's actual behavior:</p>
<div class="codehilite"><pre><span></span>universe u
inductive fooProp : Prop | mk : ℕ → fooProp --ok
inductive fooType : Type u | mk : ℕ → fooType --ok
inductive fooSort : Sort u | mk : ℕ → fooSort
-- universe level of type_of(arg #1) of &#39;foo.mk&#39; is too big for the corresponding inductive datatype
</pre></div>


<p>I assumed the last definition should work, writing the universe constraint as <code>imax v u &lt;= u</code> where <code>u</code> is the sort of the inductive type itself (here <code>u</code>) and <code>v</code> is the sort of the constructor argument (here <code>1</code>). Is this just because lean doesn't know how to prove <code>imax 1 u &lt;= u</code>?</p>


{% endraw %}
