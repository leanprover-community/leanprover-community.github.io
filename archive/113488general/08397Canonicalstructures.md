---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08397Canonicalstructures.html
---

## Stream: [general](index.html)
### Topic: [Canonical structures](08397Canonicalstructures.html)

---


{% raw %}
#### [ Kevin Sullivan (Oct 09 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Canonical%20structures/near/135481621):
<p>Will there be, or is there, an analog of Coq's "canonical structures", complementary to typeclasses, in Lean? </p>
<p>For information about canonical structures, see Canonical Structures for the working Coq user, <a href="https://hal.inria.fr/hal-00816703v2" target="_blank" title="https://hal.inria.fr/hal-00816703v2">https://hal.inria.fr/hal-00816703v2</a>, Sandrine Blazy and Christine Paulin and David Pichardie. ITP 2013, 4th Conference on Interactive Theorem Proving, Jul 2013, Rennes, France. Springer, 7998, pp.19-34, 2013, LNCS. 〈10.1007/978-3-642-39634-2_5.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Canonical%20structures/near/135481914):
<p>I've heard these things mentioned here in the past, and my impression is that at least some people seem to think that Lean's typeclasses are "better". Am I completely wrong about this?</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Canonical%20structures/near/135482042):
<p><a href="#narrow/stream/113488-general/subject/working.20with.20finite.20sequences/near/123573886" title="#narrow/stream/113488-general/subject/working.20with.20finite.20sequences/near/123573886">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/working.20with.20finite.20sequences/near/123573886</a></p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Canonical%20structures/near/135482064):
<p>Some old discussion on the same topic. If you have things to add I'm sure that people here would be interested.</p>

#### [ Kevin Sullivan (Oct 09 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Canonical%20structures/near/135485472):
<blockquote>
<p>Some old discussion on the same topic. If you have things to add I'm sure that people here would be interested.</p>
</blockquote>
<p>Ah, thanks for the link to this thread. I did a search before posting but didn't come up with this one.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Canonical%20structures/near/135531826):
<p>I found it using search -- searching for canonical structures gave me a bunch of posts by me banging on about canonical isomorphisms of structures; I then realised that searching for "canonical structure" was a better idea.</p>

#### [ Patrick Massot (Oct 10 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Canonical%20structures/near/135533733):
<p>About canonical structures, the only interesting thing I remember is that, in the Coq bigop paper, they insist a lot on the fact that canonical structures can be associated to terms and not only types, and this is meant to be a huge advantage over type classes. But this does not apply to Lean type classes. For instance the is_commutative type class in <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/algebra/classes.lean#L13" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/algebra/classes.lean#L13">https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/algebra/classes.lean#L13</a> is about a term.</p>


{% endraw %}
