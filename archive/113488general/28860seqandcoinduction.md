---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28860seqandcoinduction.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [seq and coinduction](https://leanprover-community.github.io/archive/113488general/28860seqandcoinduction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124283402):
<p>I see this comment in <code>data.seq.seq</code>:</p>
<div class="codehilite"><pre><span></span>/-
coinductive seq (α : Type u) : Type u
| nil : seq α
| cons : α → seq α → seq α
-/
 ```
Does this mean that `seq` is intended to be coinductive? Does that mean we can have co-fixed points?
</pre></div>

#### [ Mario Carneiro (Mar 27 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285523):
<p><code>seq</code> is intended to be coinductive, and it has co-fixed points. It has all the same properties you would expect of such a <code>coinductive</code> def, if it existed</p>

#### [ Mario Carneiro (Mar 27 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285526):
<p>except possibly the computation rules</p>

#### [ Kenny Lau (Mar 27 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285604):
<p>and what is the name of the fixed point function?</p>

#### [ Mario Carneiro (Mar 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285665):
<p><code>corec</code> I think, depending on what you mean by co-fixed point</p>

#### [ Kenny Lau (Mar 27 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285736):
<p>I mean the sequence (1,2,1,2,...) being defined as X := 1,2,X</p>

#### [ Mario Carneiro (Mar 27 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285760):
<p>We would need a better compiler to implement such a thing, but you can do it manually with a list storing the cycle</p>

#### [ Kenny Lau (Mar 27 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124285815):
<p>and then doing what?</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124287806):
<p>Here's an implementation of <code>cycle</code> for <code>stream</code>: <code>cycle 1 [2, 3] = [1, 2, 3, 1, 2, 3, ...]</code></p>
<div class="codehilite"><pre><span></span>def  cycle {α} (a : α) (l : list α) : stream α :=
stream.corec&#39; (λ al, match al with
| (b, []) := (b, a, l)
| (b, c::l&#39;) := (b, c, l&#39;)
end) (a, l)
</pre></div>

#### [ Kenny Lau (Mar 27 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124287865):
<p>no <code>cycle [1,2,3]</code>?</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288072):
<p>You could, but then what is <code>cycle []</code>?</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288086):
<p>this way that's syntactically impossible to give as input</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288092):
<p>if you did it in meta you wouldn't have to worry about this sort of thing, right?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288096):
<p>and then you could just promise not to put [] in</p>

#### [ Kenny Lau (Mar 27 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288142):
<p>I see</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/seq%20and%20coinduction/near/124288176):
<p>You can promise not to put <code>[]</code> in in cycle as well: you could have an assumption <code>l != []</code> which would be no fun to work with, or you could have <code>A</code> be inhabited so that it returns <code>[default, default, ...]</code> in that case, or you could return a <code>seq</code> so that this produces an empty seq</p>


{% endraw %}
