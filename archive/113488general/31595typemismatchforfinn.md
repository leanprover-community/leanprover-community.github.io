---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31595typemismatchforfinn.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [type mismatch for fin n](https://leanprover-community.github.io/archive/113488general/31595typemismatchforfinn.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 11 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579325):
<p>I am surprised that this doesn't typecheck:</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579326):
<div class="codehilite"><pre><span></span>def subtypeadd {m : ℕ} {n : ℕ} (A : fin m) (B : fin n) : fin (m+n) :=
  ⟨A.val+B.val,add_lt_add A.is_lt B.is_lt⟩

example (A : fin 3) (B : fin 4) (C : fin 7)
  : A = ⟨2,dec_trivial⟩ → B = ⟨0,dec_trivial⟩ → C = subtypeadd A B → C = ⟨2,dec_trivial⟩ := sorry
</pre></div>

#### [ Kevin Buzzard (Mar 11 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579333):
<p>It complains at <code>subtypeadd</code> that <code>A</code> has type <code>fin 3</code> and it expects it to have type <code>fin 6</code>??</p>

#### [ Mario Carneiro (Mar 11 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579423):
<p>I think this is the default elaboration strategy's fault</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579425):
<p>It's hard for me to see what's going on because it doesn't typecheck so I don't have any term to work with</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579430):
<p>Obviously I can fix it with @</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579431):
<p>but here -- hey -- can you be the elaborator like you sometimes do?</p>

#### [ Mario Carneiro (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579432):
<p>You can make it typecheck by writing <code>@subtypeadd _ _ A B</code> or adding <code>@[elab_simple]</code> to the definition of subtypeadd</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579433):
<p>You have to figure out what m and n are</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579434):
<p>and the only clues you have are that A : fin m and A : fin 3</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579435):
<p>what do you think</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579472):
<p>mr elaborator</p>

#### [ Mario Carneiro (Mar 11 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579497):
<p>It sees that the goal is <code>fin 7</code> and so has to solve <code>7 =?= ?m1 + ?m2</code>. I think if you unfold 7 enough (<code>bit1 (bit1 one)</code>) you get <code>bit0 (bit1 one) + 1</code>, i.e. <code>6+1</code>. So it's the most obvious split and lean takes it</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579501):
<p>Aah excellent!</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579541):
<p>so in fact this is a fun game</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579542):
<p>guess the error</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579543):
<div class="codehilite"><pre><span></span>example (A : fin 3) (B : fin 5) (C : fin 8)
  : A = ⟨2,dec_trivial⟩ → B = ⟨0,dec_trivial⟩ → C = subtypeadd A B → C = ⟨2,dec_trivial⟩ := sorry
</pre></div>

#### [ Kevin Buzzard (Mar 11 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579544):
<p>you have to guess the spurious complaint that Lean makes</p>

#### [ Kevin Buzzard (Mar 11 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20mismatch%20for%20fin%20n/near/123579594):
<p>for <code>fin 2n</code> it wants <code>A : fin n</code> and for <code>fin (2n+1)</code> it wants <code>A : fin (2n)</code></p>


{% endraw %}
