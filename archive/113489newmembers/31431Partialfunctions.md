---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31431Partialfunctions.html
---

## Stream: [new members](index.html)
### Topic: [Partial functions](31431Partialfunctions.html)

---


{% raw %}
#### [ zaa (Oct 02 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005256):
<p>Are there cases where partial functions are actually necessary? [Should probably make a new topic.]</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005726):
<p>Necessary for lean, or for mathematics?</p>

#### [ zaa (Oct 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005767):
<p>I can imagine that high school math (or some university math) definitely contains exercises with, for example, functions not defined for all real numbers.<br>
"Find the domain of definition of blah-blah function, and it's range of values, etc."<br>
"Find the solutions and don't forget about domain of definition."</p>
<p>Programming should have use for them too, imo (they could throws exceptions, errors or NaNs)</p>
<p>...</p>

#### [ zaa (Oct 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005768):
<blockquote>
<p>Necessary for lean, or for mathematics?</p>
</blockquote>
<p>For math.</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005836):
<p>There are plenty of places where partial functions in all their guises are useful</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005877):
<p>But there are many ways to interpret what "partial function" even means</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005878):
<p>There are definitely lots of circumstances when the domain of a function is only a subset of some initial set that we are interested in; I guess you might call that a partial function, though I think most of the time people prefer just to talk about functions with different domains.</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005889):
<p>In dependent type theory, you have the ability to specify such precise domains that it is not really necessary to have a partial function in the truest sense</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005934):
<p>Usually when I talk about a partial function in lean I mean a function with an argument that is a proof</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005943):
<p>Every partial function is isomorphic to a total function, over the subtype</p>

#### [ zaa (Oct 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005954):
<blockquote>
<p>Usually when I talk about a partial function in lean I mean a function with an argument that is a proof</p>
</blockquote>
<p>Like <code>F: forall x, P x -&gt; A</code>?</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135005957):
<p>Right</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006020):
<p>Actually there are two ways to losslessly totalize the function. One is to "push the argument left" to form the subtype <code>{x // P x} -&gt; A</code>, and the other is to push the argument right, into the output, as <code>X -&gt; \Sigma p, p -&gt; A</code></p>

#### [ Mario Carneiro (Oct 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006025):
<p>also known as <code>X -&gt; roption A</code> or <code>X -&gt;. A</code> which is the mathlib type of partial functions</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006076):
<p>When working in a programming context, it is often reasonable to upgrade this to <code>X -&gt; option A</code>. Here the function will "tell you" if you have gone out of domain, and will return a result if not</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006085):
<p>whereas <code>X -&gt; roption A</code> will not "tell you" if you have got the domain right; you have to pass in a proof that you are allowed to call the function before you get a result</p>

#### [ zaa (Oct 02 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006134):
<p><code>X -&gt; option A</code> is what people have at school. :D</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006139):
<p>It looks like <code>roption</code> is only used in the computability stuff in mathlib, whereas <code>option</code> appears much more frequently.</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006187):
<p>That's mostly because we don't use partial functions that much</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006189):
<p>Most of the time you can avoid it one way or another</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006205):
<p>Notice that with either approach, you get a plain nondependent function. This is important for stuff like rewriting to work smoothly</p>

#### [ Mario Carneiro (Oct 02 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006216):
<p>with the proof exposed version, you have a dependent function, and then <code>rw</code> will often fail and <code>simp</code> will produce huge goals</p>

#### [ zaa (Oct 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006411):
<p>How are square root or logarithms (staying with real numbers) done in lean?</p>

#### [ zaa (Oct 02 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006601):
<p>Coq has that <code>positive := { x | x &gt;= 0 }</code> approach and than square root works on them, if I remember correctly.<br>
No idea about logarithms, should check if they're even in the Standard Library. It seems they're not.</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006655):
<p><a href="http://﻿﻿﻿﻿https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L508" target="_blank" title="http://﻿﻿﻿﻿https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L508">Here's sqrt</a> and <a href="https://github.com/leanprover-community/mathlib/blob/exp/analysis/exponential.lean#L119" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/exp/analysis/exponential.lean#L119">here's the in-progress fork with ln</a>.</p>

#### [ Mario Carneiro (Oct 02 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006734):
<p>Most mathematical functions in mathlib are totalized, meaning that rather than preserving the proof part we just do something random when it's not true</p>

#### [ Mario Carneiro (Oct 02 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135006750):
<p>e.g. a sqrt function might be defined to be the usual thing for nonnegative x and 0 for negative x</p>

#### [ Kenny Lau (Oct 02 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135013778):
<p>unfortunately sqrt(-1) is not 37</p>

#### [ zaa (Oct 02 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135016849):
<p>And 1/0 isn't too.</p>

#### [ zaa (Oct 02 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135016912):
<p>Ok, then partial functions are used only if really necessary. We should do that at school math too :D.</p>

#### [ Kevin Buzzard (Oct 02 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Partial%20functions/near/135018459):
<p>I am a mathematician and was very uncomfortable initially with the fact that sqrt(-1) was not <code>NaN</code>. But now I interpret it exactly as Mario says -- I have a mental note not to use the square root function on negative numbers in the statements of my theorems because I use it like a partial function even though it's total. Of course in the proofs I can do what I like. The fact that the square root function "should" only be used on non-negative integers is somehow something which a human uses for guidelines, but Lean doesn't need to be told this.</p>


{% endraw %}
