---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/63185cloneformalization.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [clone formalization](https://leanprover-community.github.io/archive/113489newmembers/63185cloneformalization.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Miroslav Olšák (Oct 23 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136329846):
<p>Hello everybody, we tried a testing formalization of a simple proposition about clones in several ITP's for comparison. LEAN seems pretty nice so far. However, I believe that there should be a better approach to certain parts the proof (if we just knew LEAN better).<br>
You can see the task description,  together with my complains (/ TODO) under the link.<br>
<a href="http://atrey.karlin.mff.cuni.cz/~mirecek/formal-math/clones.lean" target="_blank" title="http://atrey.karlin.mff.cuni.cz/~mirecek/formal-math/clones.lean">http://atrey.karlin.mff.cuni.cz/~mirecek/formal-math/clones.lean</a></p>

#### [ Johan Commelin (Oct 23 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136331045):
<p><span class="user-mention" data-user-id="133339">@Miroslav Olšák</span> I'm having trouble with certain symbols. I think unicode is being messed up or something. Could you post your code again with correct encoding? Maybe as a Github Gist, or something... (Don't know if you use github...)</p>

#### [ Bryan Gin-ge Chen (Oct 23 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136334848):
<p>In Firefox you can set the text encoding manually to unicode (View... Text Encoding...) and then the page displays properly. Apparently that feature no longer exists in Chrome.</p>

#### [ Miroslav Olšák (Oct 23 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136357974):
<p>All right, there it is on GitHub:<br>
<a href="https://github.com/mirefek/clones-lean/blob/master/clones.lean" target="_blank" title="https://github.com/mirefek/clones-lean/blob/master/clones.lean">https://github.com/mirefek/clones-lean/blob/master/clones.lean</a><br>
Any suggestions to the code? Is there a better way for case analysis through fin 3? Or a tactic that can do  all the rewrite at the end of the code?</p>

#### [ Mario Carneiro (Oct 23 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136358074):
<p>I think you should use ternary functions rather than arrays</p>

#### [ Mario Carneiro (Oct 23 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136358153):
<p>or products, but curried will be nicer</p>

#### [ Miroslav Olšák (Oct 23 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136360087):
<blockquote>
<p>I think you should use ternary functions rather than arrays</p>
</blockquote>
<p>Definitely not. Sure, it suffices for this simple example but it does not correspond to the definition of clone at all.</p>

#### [ Miroslav Olšák (Oct 23 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136360141):
<blockquote>
<p>or products, but curried will be nicer</p>
</blockquote>
<p>Show me.</p>

#### [ Miroslav Olšák (Oct 23 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136360748):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What do you mean by curried products?</p>

#### [ Johan Commelin (Oct 23 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136360856):
<p>You can write a function <code>X × Y → Z</code> as <code>X → Y → Z</code>.</p>

#### [ Johan Commelin (Oct 23 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136360866):
<p>This is known as "currying"</p>

#### [ Kenny Lau (Oct 23 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136360871):
<p>aka product is left-adjoint of hom</p>

#### [ Kenny Lau (Oct 23 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136360917):
<p>(sorry)</p>

#### [ Miroslav Olšák (Oct 23 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136361131):
<p>I see.<br>
But how to define the general composition for operations written like this?<br>
I really think it is better to interpret them as functions A^n -&gt; A, in the case of clones, as mathematicians usually do.</p>

#### [ Johan Commelin (Oct 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136361197):
<p>I tend to agree (I'm also a mathematician). But these CS people have really crazy operators that will do what you want.</p>

#### [ Johan Commelin (Oct 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136361225):
<p>And they can explain the benefits. (The disadvantage is that it no longer looks like what you are used to, although you can prove it is the same thing.)</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136361233):
<p>I guess the advantage of the CS approach is that you can just give a single input and get a function.</p>

#### [ Johan Commelin (Oct 23 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136361300):
<p>I don't know what a clone is exactly, but what I saw on wiki looks like it is related operads. <span class="user-mention" data-user-id="133339">@Miroslav Olšák</span> Is that right?</p>

#### [ Reid Barton (Oct 23 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136361938):
<p>nlab claims clones are analogous to operads but I think the relationship is less obvious than it looks at first glance</p>

#### [ Reid Barton (Oct 23 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136361968):
<p>The composition operation for operads takes a <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03148em;">k</span></span></span></span>-ary operation and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03148em;">k</span></span></span></span> operations of arity <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>n</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">n_1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">n</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, ..., <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>n</mi><mi>k</mi></msub></mrow><annotation encoding="application/x-tex">n_k</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">n</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> and gives you an operation of arity <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>n</mi><mn>1</mn></msub><mo>+</mo><mo>⋯</mo><mo>+</mo><msub><mi>n</mi><mi>k</mi></msub></mrow><annotation encoding="application/x-tex">n_1 + \cdots + n_k</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.58333em;"></span><span class="strut bottom" style="height:0.73333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">n</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mbin">+</span><span class="minner">⋯</span><span class="mbin">+</span><span class="mord"><span class="mord mathit">n</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span></p>

#### [ Reid Barton (Oct 23 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136362014):
<p>where the picture is that the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>k</mi></mrow><annotation encoding="application/x-tex">k</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03148em;">k</span></span></span></span> operations each have access to disjoint subsets of the input variables</p>

#### [ Reid Barton (Oct 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136362084):
<p>here, each of the composed operations has access to all the input variables. I guess maybe it is the same thing as saying that you have the power to duplicate variables.</p>

#### [ Miroslav Olšák (Oct 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136362172):
<p>I understand the advantages of functional programming, but not in this case. If anybody feels that defining a clone by curried functions would be better, it would be nice to see such an approach.</p>
<p>Concerning to operads, I don't know them very well. From what I see on Wiki right now, operads are more general than abstract clones since they does not have projections (and also, operads don't glue variables). I think Reid Barton is right, just faster than me :-)</p>

#### [ Mario Carneiro (Oct 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136384717):
<p>The fact that you can partially apply a curried function is not actually that important in this case, it's just the way lean naturally deals with n-ary functions</p>

#### [ Mario Carneiro (Oct 24 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136385067):
<p><span class="user-mention" data-user-id="133339">@Miroslav Olšák</span> Okay, I see now. I thought that you only had to deal with ternary functions, but now I see that the statement involves membership in a clone, which involves arbitrary arity functions</p>

#### [ Mario Carneiro (Oct 24 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136385128):
<p>In this case, I will point you to <a href="https://github.com/leanprover/mathlib/blob/master/computability/primrec.lean#L1132-L1141" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/computability/primrec.lean#L1132-L1141"><code>nat.primrec'</code></a>, which is somewhat similar in needing to deal with collections of n-ary functions and n-ary composition. I use functions of type <code>vector n A -&gt; A</code>, and n-ary composition is <code>λ a, f (of_fn (λ i, g i a))</code></p>

#### [ Miroslav Olšák (Oct 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/clone%20formalization/near/136396537):
<p>Interesting. Do you think that vectors behave in Lean better than arrays in general? (even though they are mathematically the same).</p>


{% endraw %}
