---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49724Retrievinginteractivelyconstructedterms.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Retrieving interactively constructed terms](https://leanprover-community.github.io/archive/113488general/49724Retrievinginteractivelyconstructedterms.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Seul Baek (Jun 15 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Retrieving%20interactively%20constructed%20terms/near/128095723):
<p>Suppose I'd like to construct a term of type <code>τ</code> interactively, so I use <code>e ← assert n '(τ)</code> and apply some further tactics to close off the goal. Now <code>e</code> is bound to a local constant, which is the expr of a term that has type <code>τ</code>.</p>
<p>Later in the proof, I need to call a tactic <code>foo : τ → tactic unit</code>. I think I should be able to use <code>e</code> in some way to extract a term <code>t : τ </code> to be used as an argument for <code>foo</code>. But <code>t ← eval_expr τ e</code> doesn't work, because <code>eval_expr</code> only works on closed expressions. Is there something else I can do to retrieve the constructed term?</p>
<p>It seems that <code>define</code> retains more information than <code>assert</code>, but I'm not sure whether that helps.</p>

#### [ Sebastian Ullrich (Jun 15 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Retrieving%20interactively%20constructed%20terms/near/128110543):
<p>You should probably use <code>tactic.solve_aux</code> in favor of <code>assert</code></p>

#### [ Seul Baek (Jun 15 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Retrieving%20interactively%20constructed%20terms/near/128125818):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I think this is closer to what I need, but it requires that you provide upfront a specific tactic which will solve the newly created goal. If there is a need to go interactive because it can't be predicted beforehand which tactic will do the job, I wonder if there are alternatives?</p>
<p>I'm currently experimenting with combinations of <code>assert</code> and <code>mk_meta_var</code>, but it seems that anything I do will only add a local constant to the context, instead of the actual term. Perhaps I'm trying to do something that you're not supposed to do <span class="emoji emoji-1f615" title="confused">:confused:</span></p>

#### [ Sebastian Ullrich (Jun 15 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Retrieving%20interactively%20constructed%20terms/near/128125953):
<blockquote>
<p>If there is a need to go interactive because it can't be predicted beforehand which tactic will do the job, I wonder if there are alternatives?</p>
</blockquote>
<p>I'm not sure I understand, what does your use case look like that you don't know when the goal will be solved? Anyway, if you copy and adapt <code>solve_aux</code>'s implementation, you should be able to do something like that.</p>


{% endraw %}
