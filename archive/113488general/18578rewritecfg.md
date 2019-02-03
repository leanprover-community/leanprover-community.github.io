---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18578rewritecfg.html
---

## Stream: [general](index.html)
### Topic: [rewrite_cfg](18578rewritecfg.html)

---


{% raw %}
#### [ Patrick Massot (Sep 21 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134366830):
<p>Recently Johannes wrote <code>rwa [htop] {occs := occurrences.pos [2]}</code> and I suddenly became aware of the rewrite tactic configuration options. Is it only me who missed this? I don't see anything about this in TPIL or the reference manual. I searched a bit and found: <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/rewrite_tactic.lean#L11" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/rewrite_tactic.lean#L11">https://github.com/leanprover/lean/blob/master/library/init/meta/rewrite_tactic.lean#L11</a> and <a href="https://github.com/leanprover/lean/blob/master/library/init/meta/occurrences.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/occurrences.lean">https://github.com/leanprover/lean/blob/master/library/init/meta/occurrences.lean</a>. So in case some terms appear several times, you can tell <code>rw</code> where you want to rewrite: everywhere (this is the default), only at a list of positions, everywhere except at a list of positions. There are two other parameters. <code>symm</code> presumably has to do with backward rewriting. Does it mean everything backward? Or try backward if forward doesn't work? We can experiment if nobody knows. And the last parameter is <code>md</code> which seem related to reducibility stuff.</p>

#### [ Patrick Massot (Sep 21 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134366841):
<p>Previously I was using <code>conv</code> whenever I should have been using the <code>occs</code> parameter</p>

#### [ Geoffrey Yeung (Sep 21 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134372914):
<p>I'm still learning basic lean atm, and I've come across this recently: <a href="https://leanprover.github.io/tutorial/tutorial.pdf" target="_blank" title="https://leanprover.github.io/tutorial/tutorial.pdf">https://leanprover.github.io/tutorial/tutorial.pdf</a><br>
This is an outdated Theorem Proving in Lean pdf for lean 2. However, there is an appendix in this version, which doesn't exist in the newer version.</p>

#### [ Geoffrey Yeung (Sep 21 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134373418):
<p>Even though quite a lot of the tactics have been renamed, changed, or removed, it's still pretty useful as a quick reference, especially for new learners like me. Should someone who's more familiar and knowledgeable about lean tactics update the appendix?</p>

#### [ Patrick Massot (Sep 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134375895):
<p>Good question! <span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> what happened to this appendix?</p>

#### [ Johannes Hölzl (Sep 21 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134377970):
<p>Tactics in Lean 2 worked completely different from Lean 3 tactics. Also the syntax very much changes. So I guess the appendix needed to be scrapped :(</p>

#### [ Rob Lewis (Sep 21 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134378895):
<p>I think the closest thing is the reference manual. <a href="https://leanprover.github.io/reference/lean_reference.pdf" target="_blank" title="https://leanprover.github.io/reference/lean_reference.pdf">https://leanprover.github.io/reference/lean_reference.pdf</a></p>

#### [ Rob Lewis (Sep 21 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134378904):
<p>This may not be completely up to date, and doesn't cover the mathlib-specific tactics.</p>

#### [ Rob Lewis (Sep 21 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134378921):
<p>But it's certainly more accurate than the Lean 2 tutorial.</p>

#### [ Kevin Buzzard (Sep 21 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134379488):
<p>It's also worth mentioning the more informal docs on e.g. <code>simp</code> and <code>cc</code> at <a href="https://github.com/leanprover/mathlib/tree/master/docs/extras" target="_blank" title="https://github.com/leanprover/mathlib/tree/master/docs/extras">https://github.com/leanprover/mathlib/tree/master/docs/extras</a></p>

#### [ Jeremy Avigad (Sep 21 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134382321):
<p>Yes, documentation for tactics in the core lib is in the reference manual, which should match the docstrings closely. The documentation for the mathlib tactics is also really helpful: <a href="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md">https://github.com/leanprover/mathlib/blob/master/docs/tactics.md</a></p>

#### [ Scott Morrison (Sep 22 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134413575):
<p>The <code>occs</code> parameter for <code>rewrite</code> is a bit unreliable (or at least its behaviour is somewhat unintuitive).</p>


{% endraw %}
