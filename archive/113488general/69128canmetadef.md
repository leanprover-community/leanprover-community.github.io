---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69128canmetadef.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [can meta `def`?](https://leanprover-community.github.io/archive/113488general/69128canmetadef.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394258):
<p>Can you have meta code that writes definitions and lemmas for you? Probably yes, and this is how things like <code>to_additive</code> work. Is that right?</p>

#### [ Johan Commelin (Sep 05 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394409):
<p>Is this somehow what <code>add_decl</code> is for?</p>

#### [ Simon Hudon (Sep 05 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394637):
<p>Yes it is</p>

#### [ Johan Commelin (Sep 05 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394664):
<p>Ok cool! I could imagine some uses for it.</p>

#### [ Johan Commelin (Sep 05 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394687):
<p>For example, you define multiplication of matrices, and immediately afterwards, there is a simp-lemma <code>mul_val</code>. This happens a lot. Couldn't we auto-generate those?</p>

#### [ Johan Commelin (Sep 05 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394756):
<p>I feel like at least half of the simp lemmas after definitions could be auto-generated.</p>

#### [ Johan Commelin (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394817):
<p>Here is a claim: every lemma that is proved by <code>rfl</code> is a good candidate for being auto-generated.</p>

#### [ Simon Hudon (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394857):
<p>Yes, they can be generated. But could it be that you could get rid of the lemmas altogether by tagging your definition as <code>simp</code>?</p>

#### [ Johan Commelin (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133394898):
<p>Hmm, I think usually there is notation introduced in between.</p>

#### [ Simon Hudon (Sep 05 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395156):
<p>But the notation doesn't affect rewriting.</p>

#### [ Johan Commelin (Sep 05 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395204):
<p>Hmm... then I'm just really confused.</p>

#### [ Johan Commelin (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395224):
<p>Take <a href="https://github.com/leanprover-community/mathlib/blob/noetherian/ring_theory/ideals.lean#L176" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/noetherian/ring_theory/ideals.lean#L176">https://github.com/leanprover-community/mathlib/blob/noetherian/ring_theory/ideals.lean#L176</a> for example.</p>

#### [ Johan Commelin (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395268):
<p>Those lines have completely predictable names (even to me), and are completely boring statements.</p>

#### [ Johan Commelin (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395286):
<p>I would definitely forget to write them, until I need the after 50 other lines, and then only write half of them.</p>

#### [ Johan Commelin (Sep 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395396):
<p>Do you think stuff like this could be automated?</p>

#### [ Johan Commelin (Sep 05 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395464):
<p>Maybe the question is to general...</p>

#### [ Simon Hudon (Sep 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395514):
<p>I think the issue there is the combination of <code>coe</code> (which comes from a type class) and its underlying definition.</p>

#### [ Johan Commelin (Sep 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395533):
<p>At least I got an answer to the original question. And I am glad that it was positive. I'll keep it in mind, because I'm sure it will come in handy at some point.</p>

#### [ Simon Hudon (Sep 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395540):
<p>It is not as trivial as I thought but there might be something to do with it.</p>

#### [ Simon Hudon (Sep 05 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395641):
<p>In general, maybe the question is to do <code>simp</code> lemmas from a type class instance which is just built on top of stand alone definitions</p>

#### [ Simon Hudon (Sep 05 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395779):
<p>If you have </p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">my_class</span> <span class="n">my_type</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">op</span> <span class="o">:=</span> <span class="n">my_type</span><span class="bp">.</span><span class="n">op</span> <span class="o">}</span>
</pre></div>


<p>we can take all the equations of <code>my_type.op</code>, replace the occurrences of <code>my_type.op</code> with <code>my_class.op</code> and label the result as <code>simp</code></p>

#### [ Johan Commelin (Sep 05 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395833):
<p>Right. That sounds useful. But I don't know what the experts think (-;</p>

#### [ Simon Hudon (Sep 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133395896):
<p>More import still: does it seem like a generalization of the problem you were asking about?</p>

#### [ Johan Commelin (Sep 05 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396014):
<p>Yes, I think so... although there might also be other cases. For example <a href="https://github.com/leanprover/mathlib/pull/316/files#diff-dcac36203421953a8cefa07fecd35a79R71" target="_blank" title="https://github.com/leanprover/mathlib/pull/316/files#diff-dcac36203421953a8cefa07fecd35a79R71">https://github.com/leanprover/mathlib/pull/316/files#diff-dcac36203421953a8cefa07fecd35a79R71</a> might be enhanced to also define a functor along the way.</p>

#### [ Johan Commelin (Sep 05 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396029):
<p>But I'm not suggesting that these are special cases of one sort of automation.</p>

#### [ Johan Commelin (Sep 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396047):
<p>It is just that they could both benefit from some <code>add_decl</code> if I'm not mistaken.</p>

#### [ Simon Hudon (Sep 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396183):
<p>If you want, I can walk you through the construction of the solution I suggested and then we can see if something similar can be done for your second example</p>

#### [ Johan Commelin (Sep 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396356):
<p>Ok, would definitely like to do that. But maybe not tonight (-; I need to catch up with some sleep, so I'll be gone in a couple of minutes.</p>

#### [ Simon Hudon (Sep 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133396393):
<p>Sure, let me know when you're ready and I'll give you a hand</p>

#### [ Johannes Hölzl (Sep 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20meta%20%60def%60%3F/near/133397167):
<p>Just for your information: Isabelle has a tool called <code>lift_definition</code> which lifts a term along subtypes / quotients / other relations etc.<br>
If one wants to define a function <code>lift f : {a : A // p a} -&gt; {b : B // q b}</code>, it provides one with the following two goals:<br>
the function itself: <code>f : A -&gt; B</code> and a proof <code>forall a : A, p a -&gt; q (f b)</code>. The nice thing is that this also works for quotients, but in Isabelle this is done by assuming that there is a canonical projection (i.e. <code>quot.out</code>) which we may want to avoid, and instead use a more generic lifting constant.</p>
<p>My idea for a lift function would be: get typing information (which includes the information for which types the representation should change) and the term to lift. Then it puts <code>lift</code> or <code>cases</code> around the term to translate into the other type. All further proofs are left as subgoals to the user. Finally it produces the constant itself, and a rewrite rule which adds coercions etc at all places necessary to remove all lift constants.</p>


{% endraw %}
