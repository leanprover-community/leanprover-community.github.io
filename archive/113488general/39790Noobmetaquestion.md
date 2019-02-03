---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39790Noobmetaquestion.html
---

## Stream: [general](index.html)
### Topic: [Noob meta question](39790Noobmetaquestion.html)

---


{% raw %}
#### [ Chris Hughes (Sep 11 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133727546):
<p>What's the "correct" way to efficiently implement finitely supported functions in Lean meta. Currently I'm using <code>list (α × β)</code> as <code>α →₀ β</code>, but this seems totally wrong. By finitely supported, I mean functions for which I only care about the result for finitely many <code>α</code></p>

#### [ Reid Barton (Sep 11 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133727560):
<p><code>data.rbmap</code>?</p>

#### [ Reid Barton (Sep 11 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133727620):
<p>that's the best way I know of</p>

#### [ Sean Leather (Sep 11 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133727662):
<p><a href="https://github.com/spl/lean-finmap" target="_blank" title="https://github.com/spl/lean-finmap">https://github.com/spl/lean-finmap</a> ?</p>

#### [ Chris Hughes (Sep 11 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133728841):
<p><code>rbmap</code> looks about right. Thanks.</p>

#### [ Chris Hughes (Sep 11 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133730984):
<p>Is there a <code>decidable</code> instance for <code>mem</code> in <code>rbmap</code> anywhere. This seems like something so fundamental that I feel like I must be doing something wrong by trying to use it.</p>

#### [ Sean Leather (Sep 11 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133731062):
<p>I don't think the <code>rbmap</code> theorem collection is very extensive.</p>

#### [ Chris Hughes (Sep 11 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133734773):
<p>I see there's <code>contains</code>, which I assume is the same thing.</p>

#### [ Chris Hughes (Sep 11 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133735259):
<p>There doesn't seem to be an <code>erase</code> either.</p>

#### [ Chris Hughes (Sep 11 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Noob%20meta%20question/near/133737802):
<p>Is <code>rbtree α</code> isomorphic to <code>finset α</code>, and is <code>rbmap α β</code> isomorphic to <code>Σ s : finset α, Π x, x ∈ s → β</code></p>


{% endraw %}
