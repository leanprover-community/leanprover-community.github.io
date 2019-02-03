---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60832listprod.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [list.prod](https://leanprover-community.github.io/archive/113488general/60832listprod.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jun 20 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128334739):
<p>Was there any point in time where <code>list.prod [t]</code> was definitionally equivalent to <code>t * 1</code>?</p>

#### [ Kenny Lau (Jun 20 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335761):
<p>and was there any point in time where <code>list.prod (x :: L) = x * list.prod L</code> was <code>rfl</code>?</p>

#### [ Simon Hudon (Jun 20 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335831):
<p>I think not. The foldl implementation is faster and Leo has been pretty aggressive with optimization from the start</p>

#### [ Kenny Lau (Jun 20 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335838):
<p>interesting. my category repo seems to answer yes to my questions</p>

#### [ Kenny Lau (Jun 20 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335887):
<p>i.e. a code worked some time ago, and now it doesn't</p>

#### [ Simon Hudon (Jun 20 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335915):
<p>You can have an even clearer answer and use <code>git blame</code> on the definition of <code>list.product</code></p>

#### [ Kenny Lau (Jun 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335924):
<p>how do I do that?</p>

#### [ Simon Hudon (Jun 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335941):
<p>Do you use emacs and magit?</p>

#### [ Kenny Lau (Jun 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128335996):
<p>eh... not really</p>

#### [ Simon Hudon (Jun 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128336002):
<p>You can get the instructions on using <code>git blame</code> by typing <code>man git-blame</code> in a terminal</p>

#### [ Johan Commelin (Jun 20 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128347985):
<p>Alternatively, you go to GitHub, and lookup the relevant line: <a href="https://github.com/leanprover/mathlib/blob/e1f795d0d929fa6b5458a04bd6bb5889e503b0bf/data/list/basic.lean#L1054" target="_blank" title="https://github.com/leanprover/mathlib/blob/e1f795d0d929fa6b5458a04bd6bb5889e503b0bf/data/list/basic.lean#L1054">https://github.com/leanprover/mathlib/blob/e1f795d0d929fa6b5458a04bd6bb5889e503b0bf/data/list/basic.lean#L1054</a><br>
Then you click on the <code>...</code> to the left of that line, and choose <code>git blame</code>. That gives you <a href="https://github.com/leanprover/mathlib/blob/e1f795d0d929fa6b5458a04bd6bb5889e503b0bf/data/list/basic.lean#L1054" target="_blank" title="https://github.com/leanprover/mathlib/blob/e1f795d0d929fa6b5458a04bd6bb5889e503b0bf/data/list/basic.lean#L1054">https://github.com/leanprover/mathlib/blob/e1f795d0d929fa6b5458a04bd6bb5889e503b0bf/data/list/basic.lean#L1054</a></p>

#### [ Johan Commelin (Jun 20 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128348026):
<p>But I don't see an easy option to walk through the history of that line. On the command line you <em>can</em> do that, with <code>git log</code> and some options. See also <a href="https://flummox-engineering.blogspot.com/2016/05/view-specific-lines-of-source-code-in-git-history.html" target="_blank" title="https://flummox-engineering.blogspot.com/2016/05/view-specific-lines-of-source-code-in-git-history.html">https://flummox-engineering.blogspot.com/2016/05/view-specific-lines-of-source-code-in-git-history.html</a></p>

#### [ Johannes Hölzl (Jun 20 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128362377):
<p>I traced it back, it was always <code>foldl</code>. I ported the definition from Lean2's library. I think we should change it to <code>foldr</code> then we get the expected equalities.</p>

#### [ Simon Hudon (Jun 20 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128362751):
<p>Is there a way to use <code>foldr</code> as the definition but run <code>foldl</code> implementation in the VM?</p>

#### [ Gabriel Ebner (Jun 20 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128362770):
<p>If you want to patch Lean, then yes.</p>

#### [ Simon Hudon (Jun 20 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128362903):
<p>That sounds less trivial than the "yes" suggests <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Reid Barton (Jun 20 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128364747):
<p><code>{-# RULES #-}</code>with a proof obligation would be neat...</p>

#### [ Simon Hudon (Jun 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128364931):
<p>you could probably write it <code>@[rule]</code> before a lemma</p>

#### [ Chris Hughes (Jun 20 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list.prod/near/128368155):
<blockquote>
<p>and was there any point in time where <code>list.prod (x :: L) = x * list.prod L</code> was <code>rfl</code>?</p>
</blockquote>
<p>I don't think it was even equal to that with non commutative multiplication, <code>list.prod (x :: L) = list.prod L * x</code>at the moment.</p>


{% endraw %}
