---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51637typeclassinferenceaftercolon.html
---

## Stream: [general](index.html)
### Topic: [type class inference after colon](51637typeclassinferenceaftercolon.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 11 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123577754):
<p>In <code>example (α : Type) [comm_ring α] : ∀ x y z : α, x*(y+z)=x*y+x*z := mul_add</code>, type class inference enables us to use <code>mul_add</code>. Is it possible to move the colon to the left of the alpha though? Not that  I need to, it's just an idle question. If I try <code>example : ∀ (α : Type) [comm_ring α], ∀ x y z : α, x*(y+z)=x*y+x*z := mul_add</code> then Lean complains about not being able to find <code>has_add alpha</code> etc.</p>

#### [ Kevin Buzzard (Mar 11 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123577804):
<p>A related question: is there ever a difference between <code>[comm_ring alpha]</code> and <code>[H : comm_ring alpha]</code> in terms of the type class inference system? Or between <code>[comm_ring alpha]</code> and <code>[_inst_1 : comm_ring alpha]</code>?</p>

#### [ Kevin Buzzard (Mar 11 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123578051):
<p>And another type class subtlety. With</p>
<div class="codehilite"><pre><span></span>structure foo (α : Type) :=
(bar : α)
(baz : α → α)

#check @foo.bar
#check @foo.baz
</pre></div>


<p>both <code>foo.bar</code> and <code>foo.baz</code> are <code>Π {α : Type},...</code>. But if I change the structure to a class, <code>foo.bar</code> (but not <code>foo.baz</code>) magically changes to <code>Π (α : Type)...</code> (no longer implicit). It didn't have to be that way, right? That is presumably some design decision?</p>

#### [ Mario Carneiro (Mar 11 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123579280):
<p>The first issue is <a href="https://github.com/leanprover/lean/issues/1920" target="_blank" title="https://github.com/leanprover/lean/issues/1920">#1920</a>. You have to write <code>example : ∀ (α : Type) [comm_ring α], ∀ x y z : α, by exactI x*(y+z)=x*y+x*z</code> if you want to use any typeclass args right of the colon</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123579286):
<p>Aah -- this is exactly the change that caused you so much trouble!</p>

#### [ Mario Carneiro (Mar 11 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123579327):
<p>The second issue is just the usual analysis of when to make arguments implicit. It's a design decision, of course, but it is reasonably predictable and well motivated</p>


{% endraw %}
