---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90420sortvstype.html
---

## Stream: [general](index.html)
### Topic: [sort vs type](90420sortvstype.html)

---


{% raw %}
#### [ Johan Commelin (Jul 03 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129031745):
<p>I realise that I don't actually quite understand what the distinction is between sort and type. Somehow I treat them as interchangeable, but of course that is not a very solid strategy. So, what exactly is a sort, and when should I use it?</p>

#### [ Reid Barton (Jul 03 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129032001):
<p>Basically, <code>Sort*</code> = <code>Prop</code> union <code>Type*</code>. <code>Sort 0 = Prop</code>, and <code>Sort (u+1) = Type u</code>.</p>

#### [ Johan Commelin (Jul 03 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129032574):
<p>Hmm, so that kind explains my thinking that I could equate <code>Sort*</code> and <code>Type*</code>. But it doesn't explain why we have these two notions that are almost the same. Lean seems to prefer to have only 1 concept when 1 suffices...</p>

#### [ Sean Leather (Jul 04 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129068181):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Here's some of the <a href="https://github.com/leanprover/lean/issues/1341" target="_blank" title="https://github.com/leanprover/lean/issues/1341">design discussion</a>.</p>

#### [ Johan Commelin (Jul 04 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sort%20vs%20type/near/129068681):
<p>Thanks!</p>


{% endraw %}
