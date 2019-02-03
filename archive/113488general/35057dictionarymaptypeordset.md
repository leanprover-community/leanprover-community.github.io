---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35057dictionarymaptypeordset.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [dictionary / map type: ordset](https://leanprover-community.github.io/archive/113488general/35057dictionarymaptypeordset.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Dec 11 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151471035):
<p>I've been playing around with conventional programming in lean lately (thank you Advent of Code), and it has made me realize that our capabilities with finite maps is quite limited. Currently, we have:</p>
<ul>
<li><code>native.rb_map</code>: meta interface to a C++ implementation of red black trees</li>
<li><code>rbmap</code>: lean implementation of red black trees in core</li>
<li><code>finmap</code>: maps via association lists (in mathlib)</li>
<li><code>finsupp</code>: finitely supported functions (non computational)</li>
</ul>
<p>The only one which is really suitable for computation is <code>rbmap</code> (<code>finmap</code> is too slow, since it is implemented with lists, although it is useful for specifications and verified computation), and it is implemented in core with basically only two operations: <code>insert</code> and <code>find</code>. And because the well-formedness condition is incorrect, you can't even implement more operations, like <code>erase</code>.</p>
<p>So I decided to start anew with weight balanced trees, as a direct port from Haskell's <code>Data.Set</code>. The result is the <a href="https://github.com/leanprover-community/mathlib/blob/ordmap/data/ordmap/ordnode.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/ordmap/data/ordmap/ordnode.lean"><code>ordnode A</code></a> type, which has a very complete set of operations for working with sets and maps. The library for <code>ordset A</code> is still under development but will incorporate the correct invariants on top of <code>ordnode A</code> so that the usual properties are provable.</p>
<p>PS: The names <code>ordnode</code>, <code>ordset</code>, <code>ordmap</code> are a bit inelegant, I'm open to suggestions.</p>

#### [ Gabriel Ebner (Dec 11 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472291):
<p><code>ordset α</code> does not seem to be isomorphic to <code>finset α</code>---is this intentional?</p>

#### [ Mario Carneiro (Dec 11 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472428):
<p>I added the equivalence relatively recently (<code>ordnode.equiv</code>). I will change <code>ordset</code> to be a quotient of the current subtype</p>

#### [ Mario Carneiro (Dec 11 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472565):
<p>Also it's not going to be isomorphic to <code>finset A</code> anyway, because of preorder stuff</p>

#### [ Mario Carneiro (Dec 11 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472607):
<p>I think the <code>ordset</code>s over a linear order should be isomorphic to <code>finset A</code></p>

#### [ Mario Carneiro (Dec 11 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472787):
<p>(more precisely, over a total preorder, a <code>ordset A</code> can only represent a comparability antichain, i.e. <code>x, y \in s</code> and <code>x &lt;= y</code> and <code>y &lt;= x</code> implies <code>x = y</code>)</p>

#### [ Gabriel Ebner (Dec 11 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151472863):
<p>Yeah, with the quotient they should be isomorphic for total orders.</p>

#### [ Joe Hendrix (Dec 11 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151473732):
<p>I had my own version of rb trees  while back (<a href="https://github.com/joehendrix/lean-containers/" target="_blank" title="https://github.com/joehendrix/lean-containers/">https://github.com/joehendrix/lean-containers/</a>).  It uses quotients so we can get a decidable equivalence relation.<br>
I had to put it on hold for other projects, and only got around to insert (so it's close to the existing rbmap capabilities).  I think it also probably doesn't work with the latest lean 3.  Maps are implemented on top of sets.</p>

#### [ Edward Ayers (Dec 11 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151480189):
<p>I ported Coq's implementation of RB trees (sans proofs).  I also didn't test it much so has bugs.<br>
<a href="https://github.com/EdAyers/edlib/blob/master/rb.lean" target="_blank" title="https://github.com/EdAyers/edlib/blob/master/rb.lean">https://github.com/EdAyers/edlib/blob/master/rb.lean</a></p>

#### [ Edward Ayers (Dec 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dictionary%20/%20map%20type%3A%20ordset/near/151481780):
<p>For naming, I vote <code>table</code></p>


{% endraw %}
