---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/02913yoneda.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [yoneda](https://leanprover-community.github.io/archive/116395maths/02913yoneda.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 18 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136033284):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Is there a reason why <code>yoneda</code> takes the category as explicit argument? Now we have to write <code>yoneda C X</code> instead of just <code>yoneda X</code>.</p>

#### [ Scott Morrison (Oct 18 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047539):
<p>Try it: you still wouldn't be able to write <code>yoneda X</code>. The problem is that <code>yoneda C X</code> has a coercion, converting it to <code>(yoneda C).obj X</code>, and the coercion mechanism isn't clever enough to handle <code>yoneda X</code> by filling in <code>C</code> as an implicit argument before using the coercion.</p>

#### [ Reid Barton (Oct 18 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047790):
<p>I guess <code>yoneda.obj X</code> would work then, if the category argument was implicit?</p>

#### [ Reid Barton (Oct 18 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047957):
<p>This coercion stuff has turned out to be a lot more frustrating than expected--it's lovely when it works but Lean's reluctance to use coercions in the presence of metavariables means that they're often a lot more awkward than just writing <code>F.obj X</code>, but then you have the burden of supporting both <code>F X</code> and <code>F.obj X</code> which are different expressions.</p>

#### [ Johan Commelin (Oct 18 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047972):
<p><em>"and the coercion mechanism isn't clever enough"</em> <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Johan Commelin (Oct 18 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136047999):
<p>I guess this is why Scott didn't use any coercions a couple of months ago...</p>

#### [ Reid Barton (Oct 18 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048072):
<p>If <code>F X</code> and <code>F.obj X</code> were the same expression, one could forgive the elaborator for being picky about where it is willing to insert a coercion</p>

#### [ Reid Barton (Oct 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048215):
<p>I think this thing with <code>yoneda C</code> is the same issue I ran into whenever I had to deal with cylinders in my homotopy theory library. There I had a functor <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>I</mi><mo>:</mo><mi>C</mi><mo>→</mo><mi>C</mi></mrow><annotation encoding="application/x-tex">I : C \to C</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">I</span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.07153em;">C</span></span></span></span> which was attached to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">C</span></span></span></span> by a type class, but I think that detail doesn't matter.</p>

#### [ Johan Commelin (Oct 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048220):
<p>Could we choose a fancy bracket that looks like <code>(</code> and <code>)</code>, and turn that into notation for <code>has_apply</code>?</p>

#### [ Reid Barton (Oct 18 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048261):
<p>And then I also had natural transformations <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>i</mi><mn>0</mn></msub></mrow><annotation encoding="application/x-tex">i_0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.65952em;"></span><span class="strut bottom" style="height:0.80952em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">i</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>i</mi><mn>1</mn></msub><mo>:</mo><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">d</mi></mrow><mo>→</mo><mi>I</mi></mrow><annotation encoding="application/x-tex">i_1 : \mathrm{id} \to I</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.84444em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">i</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">:</span><span class="mord"><span class="mord mathrm">i</span><span class="mord mathrm">d</span></span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.07847em;">I</span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>p</mi><mo>:</mo><mi>I</mi><mo>→</mo><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">d</mi></mrow></mrow><annotation encoding="application/x-tex">p : I \to \mathrm{id}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">p</span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.07847em;">I</span><span class="mrel">→</span><span class="mord"><span class="mord mathrm">i</span><span class="mord mathrm">d</span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>v</mi><mo>:</mo><mi>I</mi><mo>→</mo><mi>I</mi></mrow><annotation encoding="application/x-tex">v : I \to I</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.07847em;">I</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.07847em;">I</span></span></span></span>, all of which had the same issue...</p>

#### [ Johan Commelin (Oct 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048366):
<p>I think wouldn't mind write <code>F(X)</code> with some fancy <code>()</code>. But maybe this is abusing notation and type classes too much.</p>

#### [ Johan Commelin (Oct 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048387):
<p>I think this could then replace <code>coe_to_fun</code>.</p>

#### [ Reid Barton (Oct 18 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048509):
<p>It's not clear to me that we would not just end up back in the same situation</p>

#### [ Reid Barton (Oct 18 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048567):
<p>We would still have two things, <code>F.obj X</code> and <code>apply F X</code>. I guess the question is whether we could avoid ever having to write <code>F.obj X</code>. But it would be so much simpler if there was just one thing in the first place.</p>

#### [ Johan Commelin (Oct 18 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048684):
<p><code>apply F X</code> would be <code>F.obj X</code> by definition.</p>

#### [ Reid Barton (Oct 18 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048696):
<p>It's possible if I had built my homotopy theory library on top of a category theory version with coercions from the start, I could have found a more convenient way to set things up</p>

#### [ Reid Barton (Oct 18 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048781):
<p>But "by definition" is not good enough for <code>simp</code>, <code>rw</code> etc.</p>

#### [ Reid Barton (Oct 18 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048801):
<p>I had a hard time porting a lot of proofs over the transition to use coercions in category theory</p>

#### [ Reid Barton (Oct 18 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048815):
<p>because I had to be careful about the difference between <code>F X</code> and <code>F.obj X</code></p>

#### [ Reid Barton (Oct 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048831):
<p>If I could actually write <code>F X</code> consistently then that might be okay, but I couldn't because of the issues with coercions and metavariables</p>

#### [ Reid Barton (Oct 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048875):
<p>In the end I think I wrote some explicit type ascriptions in the statements of the simp lemmas I had defined, so that they could work on the <code>F X</code> version</p>

#### [ Scott Morrison (Oct 18 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048943):
<p>If we can agree that the coercion mechanism is broken, I would very happily rip them back out of the <code>category_theory/</code>.</p>

#### [ Reid Barton (Oct 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048952):
<p>For example <a href="https://github.com/rwbarton/lean-homotopy-theory/commit/e98dd6f51cd46653bf30c610e60573318443466c#diff-6931c0d6d9d8dda133a6b3ed34b290d5L548" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/commit/e98dd6f51cd46653bf30c610e60573318443466c#diff-6931c0d6d9d8dda133a6b3ed34b290d5L548">https://github.com/rwbarton/lean-homotopy-theory/commit/e98dd6f51cd46653bf30c610e60573318443466c#diff-6931c0d6d9d8dda133a6b3ed34b290d5L548</a></p>

#### [ Scott Morrison (Oct 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136048993):
<p>The saving of not having to write <code>.obj</code> most of the time is far outweighed by the confusion of sometimes mysteriously having to do so.</p>

#### [ Reid Barton (Oct 18 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049015):
<p><a href="https://github.com/rwbarton/lean-homotopy-theory/commit/e98dd6f51cd46653bf30c610e60573318443466c#diff-f49cdebfeaf5ac27e5bea99a12ad4ca9L129" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/commit/e98dd6f51cd46653bf30c610e60573318443466c#diff-f49cdebfeaf5ac27e5bea99a12ad4ca9L129">https://github.com/rwbarton/lean-homotopy-theory/commit/e98dd6f51cd46653bf30c610e60573318443466c#diff-f49cdebfeaf5ac27e5bea99a12ad4ca9L129</a> -- sometimes I needed to help Lean out with the types and other times I didn't; it was hard to predict</p>

#### [ Scott Morrison (Oct 18 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049175):
<p>There's also the issue of why <code>category_theory/</code> requires so much use of <code>erw</code> rather than <code>rw</code>. This stinks, and I don't have a clear idea of why it happens, but fear that coercions are sometimes to blame.</p>

#### [ Reid Barton (Oct 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049245):
<p>I changed a bunch of <code>rw</code> to <code>erw</code> in that commit too, precisely because of the coercion thing. But there are some other situations where you need <code>erw</code> as well.</p>

#### [ Scott Morrison (Oct 18 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049299):
<p>Do you think you can explain any of the others? I unfortunately just try <code>erw</code> and get on with it, and haven't invested the time in seeing what was going wrong.</p>

#### [ Reid Barton (Oct 18 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049412):
<p>I suspect that most of my cases are because I still use the explicit version (<code>nat_trans.app</code> in this case) in my definitions: <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/formal/cylinder/homotopy.lean#L17" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/formal/cylinder/homotopy.lean#L17">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/formal/cylinder/homotopy.lean#L17</a><br>
and I frequently want to rewrite using the conditions Hi\0, Hi\1</p>

#### [ Reid Barton (Oct 18 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049503):
<p>It was quite unclear to me at first whether the easiest way forward was to use coercions everywhere or to use coercions nowhere or something in between</p>

#### [ Reid Barton (Oct 18 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049546):
<p>Oh you mean the other situations, not related to coercions.</p>

#### [ Reid Barton (Oct 18 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049640):
<p>I think for me they come from things like: <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>i</mi><mn>0</mn></msub></mrow><annotation encoding="application/x-tex">i_0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.65952em;"></span><span class="strut bottom" style="height:0.80952em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">i</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> is a natural transformation <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="normal">i</mi><mi mathvariant="normal">d</mi></mrow><mo>→</mo><mi>I</mi></mrow><annotation encoding="application/x-tex">\mathrm{id} \to I</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathrm">i</span><span class="mord mathrm">d</span></span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.07847em;">I</span></span></span></span>. So the naturality law for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>i</mi><mn>0</mn></msub></mrow><annotation encoding="application/x-tex">i_0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.65952em;"></span><span class="strut bottom" style="height:0.80952em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">i</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> contains stuff like <code>(functor.id C) X</code> in the types and I need it to be <code>X</code> to continue with a subsequent rewrite, and that's why I need <code>erw</code>.</p>

#### [ Reid Barton (Oct 18 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049645):
<p>I don't remember more details off-hand, sorry</p>

#### [ Reid Barton (Oct 18 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049665):
<p>But I know that at least some cases had to do with this specific issue of applying the identity functor</p>

#### [ Reid Barton (Oct 18 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049757):
<p>Like I might want to rewrite using associativity where I have three maps <code>A -&gt; B</code>, <code>B -&gt; X</code>, <code>(functor.id C) X -&gt; (functor.id C) Y</code></p>

#### [ Reid Barton (Oct 18 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049770):
<p>and then <code>rw</code> says "nope"</p>

#### [ Reid Barton (Oct 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049818):
<p>I guess my suggestion might be to rip out coercions for now and then suggest as a wishlist item for <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span> to replace <code>has_coe_to_fun</code> by what I was calling in Orsay "type-indexed notation"</p>

#### [ Mario Carneiro (Oct 18 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049869):
<p>what is that?</p>

#### [ Reid Barton (Oct 18 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049899):
<p>The idea is if <code>F X</code> was actually <strong>notation</strong> for <code>F.obj X</code> then coercion and non-coercion syntax could all live happily forever.</p>

#### [ Reid Barton (Oct 18 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049909):
<p>Currently, when Lean tries to elaborate <code>F X</code> it sees that the type of <code>F</code> is not a Pi type and then it maybe inserts a coercion</p>

#### [ Reid Barton (Oct 18 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049921):
<p>So I presume this involves reducing the type of <code>F</code> to WHNF at least?</p>

#### [ Reid Barton (Oct 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136049969):
<p>Then the idea is, allow the user to specify another interpretation of <code>F X</code> as <em>notation</em> which depends on the head of the type of <code>F</code>, or something like that.</p>

#### [ Reid Barton (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050000):
<p>rather than the rule being "if the type of <code>F</code> is a Pi type then produce an application <code>F X</code>, otherwise produce <code>coe_fun_t F X</code>" or whatever it is today</p>

#### [ Reid Barton (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050010):
<p>give the user the chance to add additional rules "if the type of <code>F</code> looks like [...], then produce [...]"</p>

#### [ Reid Barton (Oct 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050092):
<p>In this case, <code>functor.obj F X</code></p>

#### [ Reid Barton (Oct 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050430):
<p>By the way, the <code>equiv</code> coercion to fun is another one which has given me a lot of problems, which again is annoying because there are simp rules written in terms of the coercion like <code>e.symm (e x) = x</code></p>

#### [ Reid Barton (Oct 18 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050577):
<p>I guess the usability of these coercions depends upon the usage patterns. Once the <code>equiv</code>s you are working with are not ones which were passed as arguments to your lemma, but things like the equivalence Hom(FX, Y) = Hom(X, GY) induced by an adjunction, then I guess more of these metavariables crop up</p>

#### [ Mario Carneiro (Oct 18 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050684):
<p>I think this can be solved by a simp lemma like <code>e.to_fun = \u e</code> and <code>e.inv_fun = \u e.symm</code></p>

#### [ Reid Barton (Oct 18 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050894):
<p>Yes, probably; then the next problem is that I might want to define my own simp lemmas whose statements involve applying equivs as functions</p>

#### [ Reid Barton (Oct 18 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050915):
<p>and then I don't know how to write the statement of the lemma in simp normal form except by writing some bulky type ascriptions</p>

#### [ Mario Carneiro (Oct 18 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136050937):
<p>I have found that coercions between different function(like) types is a bad idea for this reason</p>

#### [ Reid Barton (Oct 18 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136051838):
<p>By the way, when bumping dependencies of your project across a substantial change, I can highly recommend having a separate checkout of the project built against the old version of the deps so that you can figure out how the heck any of your proofs used to work <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Mario Carneiro (Oct 18 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136052379):
<p>ah, that brings me back to metamath days</p>

#### [ Johan Commelin (Oct 19 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136105758):
<p>On the topic of coercions in category theory: would it make sense to use coercions to turn specialised shapes (like <code>fork</code> and <code>square</code> and <code>fan</code>) into the general shape <code>cone</code>? Of course we should also prove that have limits means having equalizers, pullbacks, products, etc... Then we might be able to prove a lot of stuff about general limits and use those results on specialised shapes. Or is this wishful thinking?</p>

#### [ Johan Commelin (Oct 19 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136106147):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I really like your idea about type indexed notation! Because then we could also have very clean notation for applying a functor to a morphism.</p>

#### [ Reid Barton (Oct 19 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136108963):
<p>Yes, I was just thinking of that as well--it would be nice to have both <code>F X</code> for <code>F.obj X</code> and <code>F f</code> for <code>F.map f</code>. I'm not sure that comes for free with the exact setup I had in mind, where the interpretation of juxtaposition depends only on the type of <code>F</code>, but maybe some slightly different design could handle it.</p>

#### [ Reid Barton (Oct 19 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136109281):
<p>I think we may indeed want to arrange things so that equalizers and so on are actually defined as special cases of limits, and then wrap that in a nicer interface (which doesn't involve manually constructing a diagram/functor). The body of facts we have about limits is just going to keep increasing, and duplicating the results for each special shape of limit doesn't make sense.</p>

#### [ Johan Commelin (Oct 19 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136110360):
<p>You say "actually defined as". Do you mean defeq? I was suggesting a coercion. But maybe that is not good enough.</p>

#### [ Johan Commelin (Oct 19 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136110402):
<p>I do think that these are issues that should be sorted out soon. Because otherwise the refactoring will become a big pain if there is already too much code depending on the current setup.</p>

#### [ Johan Commelin (Oct 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136112654):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I suppose the parser could also look at the "token" just following <code>F</code> to see whether it is an object or a hom. (And I assume the parser is smart enough to guess the right "token".)</p>

#### [ Reid Barton (Oct 19 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136112698):
<p>I meant defeq but I haven't thought that much about what exact condition we would want.<br>
Here is an example statement: if I have a limit cone in a diagram category then evaluation on any object yields a limit cone. Now we want the same statement for equalizers. If equalizers are defeq to a special case of limits, then we just apply the original statement. If equalizers are only <code>equiv</code> to a special shape of limit, then we need to transport across the equiv on both sides.</p>

#### [ Johan Commelin (Oct 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136112828):
<p>So all the current machinery should be replaced by constructors yielding a nice API?</p>

#### [ Johan Commelin (Oct 19 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136112977):
<p>It's really weird that these definitions are so non-trivial. Why are we so good at unifying concepts, and why can't we teach that trick to a computer?</p>

#### [ Scott Morrison (Oct 19 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136120823):
<p>I’d love to be able to do something like this, but at the moment I really don’t see a good option. We can work on constructing diagrams (with some help from tactics) more easily. As an example, if <code>X Y : C</code>, and <code>f g : X \hom Y</code>, there’s no reason why <code>construct_diagram [f,g]</code> couldn’t return a <code>\Sigma (J : Type) [category J], J \func C</code>, automatically deciding the index category J should be the walking parallel pair.</p>

#### [ Scott Morrison (Oct 19 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136120919):
<p>If this becomes easy enough, it becomes plausible to start defining “special” limits in terms of general ones. But without a huge improvement in this direction, it’s way too painful to expect a user to talk about equalizers as (defeq) special cases of limits. Just see the hoops I had to jump through to prove that having limits implies having equalizers...</p>

#### [ Scott Morrison (Oct 19 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136121056):
<p>Also, <span class="user-mention" data-user-id="112680">@Johan Commelin</span>, I’m not sure if you saw it already, but there’s a second pull request (from the <code>limits-constructions</code> branch) that constructs products and equalizers from limits, etc.</p>

#### [ Johan Commelin (Oct 19 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136121069):
<p>I haven't yet looked in detail.</p>

#### [ Johan Commelin (Oct 19 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136121484):
<p>I really hope that I will be able to write down a definition of <code>sieve</code> without <code>@</code>s. I must say that my experience with your library has been very positive. Writing things down is really pain-free and automation takes care of a lot of troubles.<br>
Do you have a general guideline for when to add an auto_param in a definition?</p>

#### [ Reid Barton (Oct 19 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136122297):
<p>Couldn't we have a function <code>construct_equalizer_diagram {a b} (f g : a \hom b) : walking_fork \func C</code>, and then define <code>equalizer f g := limit (construct_equalizer_diagram f g)</code>?</p>

#### [ Johan Commelin (Oct 19 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136126239):
<p>I like this idea. <span class="user-mention" data-user-id="110087">@Scott Morrison</span> , did you try something like this before you settled on the current approach? Do you see problems with it?</p>

#### [ Reid Barton (Oct 19 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136126789):
<blockquote>
<p>But without a huge improvement in this direction, it’s way too painful to expect a user to talk about equalizers as (defeq) special cases of limits. Just see the hoops I had to jump through to prove that having limits implies having equalizers...</p>
</blockquote>
<p>I agree that it is more work starting from scratch to set up the basic definitions of things like equalizers as special cases of limits, but now that <em>you</em> have already jumped through those particular hoops, why would a user also need to?</p>

#### [ Scott Morrison (Oct 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127042):
<p>I guess the problem with <code>equalizer f g := limit (construct_equalizer_diagram f g)</code> is that then the user of equalizers has to know the names of the objects and morphisms in the <code>walking_fork</code>. (Separately, I think <code>walking_fork</code> is the wrong name here; the "handle" of the fork is missing at this point.)</p>

#### [ Scott Morrison (Oct 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127048):
<p>Maybe this is a small cost.</p>

#### [ Scott Morrison (Oct 19 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127083):
<p>What should the objects and morphisms be?</p>

#### [ Scott Morrison (Oct 19 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127202):
<p>I guess I'm really not seeing where there would be a simplification of the code, however.</p>

#### [ Johan Commelin (Oct 19 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127279):
<p>The simplification would come later, right? For example you have a massive file about deriving products and equalizers from limits. That would simplify.</p>

#### [ Johan Commelin (Oct 19 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127290):
<p>And functors preserving limits and such.</p>

#### [ Scott Morrison (Oct 19 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127302):
<p>Still for any theorem about limits, you need to restate a special version of it for equalizers/products/etc. None of these things require humans to write the proofs at this point.</p>

#### [ Johan Commelin (Oct 19 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127348):
<p>Sorry, maybe I'm dense, but what exactly do you mean?</p>

#### [ Scott Morrison (Oct 19 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127349):
<p>Okay, I agree the files that construct equalizers, products, etc from limits would essentially disappear.</p>

#### [ Scott Morrison (Oct 19 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127444):
<p>Let's think about the construction <br>
<code>def pi.post (f : β → C) (G : C ⥤ D) : G (limits.pi f) ⟶ (limits.pi (G.obj ∘ f)) := ...</code></p>

#### [ Reid Barton (Oct 19 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127488):
<p><code>pi</code> = product of an arbitrary family?</p>

#### [ Scott Morrison (Oct 19 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127490):
<p>if <code>limits.pi f</code> is defined as <code>limit (functor.of_function f)</code></p>

#### [ Scott Morrison (Oct 19 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127493):
<p>Yes.</p>

#### [ Scott Morrison (Oct 19 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127589):
<p>hmm... okay, maybe you guys are right here. :-)</p>

#### [ Johan Commelin (Oct 19 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127591):
<p>Wouldn't you just prove this by <code>limit.post</code>...?</p>

#### [ Johan Commelin (Oct 19 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127656):
<p>Oohh, I really don't know. You guys have written orders of magnitude more code then I have. I'm just a user...</p>

#### [ Scott Morrison (Oct 19 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127698):
<p>So... for now I agree that this is worth exploring.</p>

#### [ Scott Morrison (Oct 19 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127744):
<p>However, I'm hoping to pause for a while on Lean, in not too long, as I have a lot of maths I want to work on.</p>

#### [ Scott Morrison (Oct 19 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127754):
<p>So I'm not sure what to do with this PR in the meantime.</p>

#### [ Scott Morrison (Oct 19 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127755):
<p>Options:</p>

#### [ Scott Morrison (Oct 19 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127764):
<p>1. leave it open for others to modify</p>

#### [ Scott Morrison (Oct 19 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127801):
<p>2. close it for now</p>

#### [ Reid Barton (Oct 19 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127811):
<p>I'm not sure exactly where that "..." was going, but another example to keep in mind is "if D is a complete category then a cone in D^J is a limit cone iff each the value at each j in J is a limit cone"</p>

#### [ Scott Morrison (Oct 19 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127820):
<p>3. strip it down to just limits, not the special cases, and leave those for later</p>

#### [ Reid Barton (Oct 19 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127834):
<p>I have been meaning to suggest that 3 is a good idea anyways</p>

#### [ Reid Barton (Oct 19 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127923):
<p>Because the PR involves a lot of relatively untested design, and I think it's worth it to go and try to prove loads of things about general limits to "kick the tires" and make sure we settle on a design that we want</p>

#### [ Scott Morrison (Oct 19 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136127930):
<p>Okay. I will strip it down. Maybe someone else can explore if the special cases defined as suggested above are usable.</p>

#### [ Johan Commelin (Oct 19 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136128038):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> How hard would it be to test that on your homotopy lib?</p>

#### [ Johan Commelin (Oct 19 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136128100):
<p>Or should we try this on a fork of Scott's lib?</p>

#### [ Reid Barton (Oct 19 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136129012):
<p>Probably not that easy since I have some setup of my own to prove a bunch of lemmas about pushouts. Though maybe I could sorry all those proofs and just see how usable it is in the actual homotopy theory part.</p>

#### [ Johan Commelin (Oct 19 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136129599):
<p>Yeah, I meant that you just create a branch, and maybe break a couple files, but test this idea on the other files.</p>

#### [ Johan Commelin (Oct 19 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136129608):
<p>I'm not suggesting you uproot your <code>master</code> branch (-;</p>

#### [ Scott Morrison (Oct 20 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136142166):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, do you have  ideas about how to define all the "walking" categories for limits of special shapes?</p>

#### [ Scott Morrison (Oct 20 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136142173):
<p>I have reduced my PR to just the plain limits.</p>

#### [ David Michael Roberts (Oct 20 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146298):
<p>Just as we have finite sets, why not have a collection of finite categories of the usual special shapes?</p>

#### [ Scott Morrison (Oct 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146369):
<p>Yes. The point is just to decide the names of the objects and morphisms, because these names will then be fixed forever, and part of the API.</p>

#### [ Scott Morrison (Oct 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146418):
<blockquote>
<p>Wouldn't you just prove this by <code>limit.post</code>...?</p>
</blockquote>
<p>I've just been trying this, and quickly discovered the reason: <code>limit.post</code> assumes that you're in a complete category. However <code>pi.post</code> only assumes you have all products. Therefore you can't call <code>limit.post</code> from <code>pi.post</code>, and we're stuck proving it again.</p>

#### [ Scott Morrison (Oct 20 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146426):
<p>Maybe this is a sign that <code>pi.post</code> is not what we want to provide people anyway.</p>

#### [ Scott Morrison (Oct 20 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146470):
<p>Except ... that it is...</p>

#### [ Scott Morrison (Oct 20 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146475):
<p>Maybe I will finish off "porting" products to the new setup, and then you guys can have a look to see what can be reduced.</p>

#### [ Scott Morrison (Oct 20 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146479):
<p>I'll do products because there no walking categories are required, we just use <code>functor.of_function</code>.</p>

#### [ Reid Barton (Oct 20 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146551):
<p>We probably need things like <code>[has_limits_of_shape J]</code> for other purposes anyways</p>

#### [ Reid Barton (Oct 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146593):
<p>e.g. <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-accessible categories have all <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-filtered colimits</p>

#### [ Reid Barton (Oct 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146599):
<p>("We" = "I", perhaps)</p>

#### [ Reid Barton (Oct 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146608):
<p>Similarly we want to talk about functors which preserve finite products or whatever</p>

#### [ Reid Barton (Oct 20 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146677):
<p>or filtered colimits, etc. This seems to me like more evidence that we need to be able to represent special shapes of (co)limits as special cases of general (co)limits so that we can flexibly mix all these notions, though certainly I have not yet tried to construct a specific design for any of this</p>

#### [ Scott Morrison (Oct 20 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146882):
<p>Could we try something like... <code>has_limits_of {A : Type} (Q : A \to \Sigma (J : Type), J \func C)</code></p>

#### [ Scott Morrison (Oct 20 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146949):
<p><code>has_limits</code> itself could be defined as <code>has_limits_of id</code></p>

#### [ Scott Morrison (Oct 20 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146965):
<p><code>has_products</code> could be defined as <code>has_limits_of A Q</code> with <code>A = \Sigma (b : Type), b \to C</code>, and <code>Q = \lambda p, p.1, functor.of_function p.2</code>.</p>

#### [ Reid Barton (Oct 20 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136146967):
<p>That's super general but I think even that level of generality could be useful in specific circumstances.</p>

#### [ Scott Morrison (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147009):
<p>Maybe there's no need to specify the allowed functors?</p>

#### [ Scott Morrison (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147015):
<p>Just the allowed diagrams?</p>

#### [ Reid Barton (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147016):
<p>For example cofibration categories or Waldhausen categories have an axiom which says that you can form a pushout if one of the legs is a cofibration (one of the bits of structure)</p>

#### [ Scott Morrison (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147021):
<p>I see.</p>

#### [ Reid Barton (Oct 20 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147033):
<p>I just hand-crafted this axiom in my project: <a href="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/formal/cofibrations/precofibration_category.lean#L41" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/formal/cofibrations/precofibration_category.lean#L41">https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/formal/cofibrations/precofibration_category.lean#L41</a></p>

#### [ Reid Barton (Oct 20 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147080):
<p>So I know this example off-hand because I already implemented it in Lean. I think this is a pretty rare scenario, but if doesn't make things too much more complicated...? Certainly the common case would be A = (J \func C), or Sigma of that over all J of some form (e.g., J filtered)</p>

#### [ Reid Barton (Oct 20 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147151):
<p>i.e., stick <code>has_limits_of_shape J</code> as a specialization of <code>has_limits_of</code> and a generalization of <code>has_products</code></p>

#### [ Scott Morrison (Oct 20 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147519):
<p>well, maybe even one more step: <code>has_limits_of</code>, allowing you to specify arbitrary diagrams and arbitrary functors out of those, then <code>has_limits_of_shapes</code> allowing you to specify a class of diagrams, but all functors out of them, then <code>has_limits_of_shape</code> for a single diagram, and then <code>has_binary_products</code> would be a specialisation of that.</p>

#### [ Scott Morrison (Oct 20 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147522):
<p>in any case, I'll give this a go, I guess.</p>

#### [ Reid Barton (Oct 20 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147525):
<p>Sounds great!</p>

#### [ Reid Barton (Oct 20 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136147610):
<p>I should really finish up that Grand Plan for formalizing model categories that I started writing a while ago...</p>

#### [ Johan Commelin (Oct 20 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136153288):
<p>While we are at it: Do people have strong opinions on whether the homs of a category live in <code>Type v</code> or <code>Sort v</code>? I think if we start doing all sorts of diagrams over preorders (or using preorders as categories in other places) it might help in manipulating the homs if they are just in <code>Prop</code> instead of the whole <code>ulift plift</code> dance.<br>
<span class="user-mention" data-user-id="110087">@Scott Morrison</span> Let me stress that I really love what you've done so far <span class="emoji emoji-1f64f" title="thank you">:thank_you:</span>. The only reason that I have these questions is because your code is so good <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span>  that I can't resist using it <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>

#### [ Scott Morrison (Oct 20 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136155058):
<p>I've tried this before, but it's not possible to use <code>Sort v</code>. Unfortunately at the moment I can't remember why... From memory if you just start at the top and switch it over you run into difficulties quite quickly, if you want to try it yourself. :-)</p>

#### [ David Michael Roberts (Oct 20 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136157606):
<blockquote>
<p>For example cofibration categories or Waldhausen categories have an axiom which says that you can form a pushout if one of the legs is a cofibration (one of the bits of structure)</p>
</blockquote>
<p>Dually, there are many cases where one has a class of morphisms of which pullbacks along arbitrary maps exist (eg submersions, in smooth manifolds)</p>

#### [ Johan Commelin (Oct 20 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136158656):
<p>Right. At some point we want to formalise this list: <a href="https://stacks.math.columbia.edu/tag/02WE" target="_blank" title="https://stacks.math.columbia.edu/tag/02WE">https://stacks.math.columbia.edu/tag/02WE</a></p>

#### [ David Michael Roberts (Oct 20 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136159177):
<p>Well, <code>span</code> and <code>cospan</code> are obvious choices, as is <code>parallel_pair</code>. Then also for each finite set one should have the corresponding discrete category, so as to form products/coproduct. The empty category should be there too, to get terminal/initial objects.</p>

#### [ Scott Morrison (Oct 20 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173465):
<p>No, I want to know what the _objects_ and _morphisms_ inside, for example <code>parallel_pair</code> should be called.</p>

#### [ Scott Morrison (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173471):
<p>Should the objects be <code>source</code> and <code>target</code>, and the morphisms <code>left</code> and <code>right</code>?</p>

#### [ Reid Barton (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173472):
<p>Yeah that's a tough one. <code>top_arrow</code>?</p>

#### [ Scott Morrison (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173473):
<p>Or should <code>parallel_pair := bool</code>??</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173480):
<p>I like 0 and 1 for the objects</p>

#### [ Scott Morrison (Oct 20 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173484):
<p>As in <code>def parallel_pair := fin 2</code>?</p>

#### [ Scott Morrison (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173531):
<p>Or</p>
<div class="codehilite"><pre><span></span>inductive parallel_pair | _0 | _1
</pre></div>


<p>??</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173532):
<p>probably not literally</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173535):
<p>like the second</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173541):
<p>I just mean as names</p>

#### [ Scott Morrison (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173543):
<p>okay, that's what I've done previously. Is there something better that <code>_0</code> and <code>_1</code> for the names?</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173551):
<p><code>0</code> and <code>1</code> are achievable</p>

#### [ Scott Morrison (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173555):
<p>Oh, how?</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173557):
<p>add an instance</p>

#### [ Reid Barton (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173560):
<p><code>has_zero</code> <code>has_one</code></p>

#### [ Scott Morrison (Oct 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173613):
<p>ah, I see.</p>

#### [ Scott Morrison (Oct 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173617):
<p>Isn't it just more confusing to have an inductive type with terms <code>_0</code>, <code>_1</code>, but then give them second names via instances?</p>

#### [ Reid Barton (Oct 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173619):
<p>Probably</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173627):
<p>I would call them <code>zero</code> and <code>one</code></p>

#### [ Mario Carneiro (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173635):
<p>and then use <code>0</code> and <code>1</code> as notation</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173640):
<p>we do that for <code>nat</code>, it's not that confusing</p>

#### [ Scott Morrison (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173643):
<p>okay... And using <code>0</code> and <code>1</code> as notation via <code>has_zero</code> and <code>has_one</code> will work in pattern matching, etc, just like for nat.</p>

#### [ Scott Morrison (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173644):
<p>Sounds reasonable.</p>

#### [ Scott Morrison (Oct 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173648):
<p>On to the morphisms, then. :-)</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173667):
<p>yeah...</p>

#### [ Scott Morrison (Oct 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173692):
<p>And the names of objects in pullbacks and pushouts...</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173694):
<p>no bright ideas there. <code>left</code> and <code>right</code> seem reasonable?</p>

#### [ Scott Morrison (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173706):
<p>Except that there's no sense in which the two are actually different...</p>

#### [ Reid Barton (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173721):
<p>surely they're <code>top</code> and <code>bottom</code>?</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173723):
<p>I don't think <code>left</code> and <code>right</code> imply any other difference</p>

#### [ Reid Barton (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173724):
<p>Which way do you draw your equalizers??</p>

#### [ Scott Morrison (Oct 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173768):
<p>Yeah, there's that too. <code>top</code> and <code>bottom</code> are probably better.</p>

#### [ Reid Barton (Oct 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173769):
<p>(but maybe <code>top</code> and <code>bottom</code> have too many other connotations, with ordering?)</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173772):
<p>I know, it's bugging me that the walking pair is always drawn with the arrows above each other</p>

#### [ Scott Morrison (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173788):
<p>oh -- and if <code>walking_pair</code> is the diagram for an equalizer, what is the diagram for a binary product?</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173789):
<p>but I think that the analogy to posets is important, that's why 0 and 1 are useful</p>

#### [ Reid Barton (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173790):
<p>I was going to bring up binary things next.</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173796):
<p>which one is that?</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173799):
<p>A &gt; B &lt; C?</p>

#### [ Scott Morrison (Oct 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173844):
<p>binary product is just the diagram with two objects, no arrows at all</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173849):
<p>left and right, definitely</p>

#### [ Reid Barton (Oct 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173851):
<p>In my homotopy theory library I used the convention of naming things like the inclusions of a coproduct with <code>\_0</code> and <code>\_1</code>, and eventually I got annoyed that I hadn't chosen <code>\_1</code> and <code>\_2</code>, but it would be a lot of things to change.</p>

#### [ Scott Morrison (Oct 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173852):
<p>... I'd been tempted to call that the <code>walking_pair</code>, and the diagram for an equalizer the <code>walking_parallel_pair</code>, but that is contrary to usual usage, I think.</p>

#### [ Reid Barton (Oct 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173861):
<p>I assume you're going to define it as <code>discrete</code> of some type?</p>

#### [ Reid Barton (Oct 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173870):
<p>The reason is that <code>\_1</code> and <code>\_2</code> aligns better with Lean's builtin <code>p.1</code> and <code>p.2</code></p>

#### [ Scott Morrison (Oct 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173877):
<p>Okay, yeah, I guess that is best, so it's defeq a special case of arbitrarily indexed products.</p>

#### [ Reid Barton (Oct 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173922):
<p>Yes, and it should also just be less work overall</p>

#### [ Scott Morrison (Oct 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173923):
<p>So is the indexing category for <code>binary_product</code> <code>discrete (fin 2)</code>, <code>discrete bool</code> or <code>discrete side</code>, where <code>side</code> is an inductive type with terms <code>left</code> and <code>right</code>?</p>

#### [ Scott Morrison (Oct 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173927):
<p>I maybe prefer the last?</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173931):
<p>I think I do too</p>

#### [ Scott Morrison (Oct 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173937):
<p>or something with terms <code>fst</code> and <code>snd</code>?</p>

#### [ Scott Morrison (Oct 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173942):
<p>That fits better with the naming of projection maps in Lean itself.</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173947):
<p>the problem with that is they aren't maps</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173992):
<p>I would get the two confused</p>

#### [ Scott Morrison (Oct 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136173994):
<p>yes, but we'll be able to write things like <code>c.\pi fst</code> for the first projection</p>

#### [ Reid Barton (Oct 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174001):
<p><code>left</code> and <code>right</code> are nice for <code>inl</code> and <code>inr</code> though</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174009):
<p>is it the same category being reused?</p>

#### [ Scott Morrison (Oct 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174021):
<p>I don't see why not.</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174023):
<p>ok, then I agree with Reid</p>

#### [ Reid Barton (Oct 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174025):
<p>Probably it should be... so that we can relate coproducts in C to products in C^op eventually</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174029):
<p>although I guess technically one is the op of the other</p>

#### [ Reid Barton (Oct 20 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174069):
<p>Yes, technically it should be the op</p>

#### [ Scott Morrison (Oct 20 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174072):
<p>Great, I will use <code>side</code> with <code>left</code> and <code>right</code>.</p>

#### [ Reid Barton (Oct 20 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174074):
<p>but we're already writing the category as <code>discrete T</code> where <code>T</code> is the type of its objects</p>

#### [ Scott Morrison (Oct 20 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174075):
<p>Finally, pullbacks and pushouts</p>

#### [ Mario Carneiro (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174087):
<p>Can we steal the same names?</p>

#### [ Scott Morrison (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174088):
<p>it would be nice here if everything is consistent...</p>

#### [ Reid Barton (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174092):
<p><code>middle</code>??</p>

#### [ Reid Barton (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174095):
<p>Is anyone going to actually see these names?</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174152):
<p><code>left - inl &gt; 1 &lt; inr - right</code></p>

#### [ Mario Carneiro (Oct 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174158):
<p><code>left &lt; fst - 0 - snd &gt; right</code></p>

#### [ Scott Morrison (Oct 20 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174262):
<p>okay, sounds good to me</p>

#### [ Scott Morrison (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174278):
<p>except...</p>

#### [ Reid Barton (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174281):
<p>I guess those names are technically accurate in some sense, though I find them really confusing</p>

#### [ Reid Barton (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174289):
<p>like, you have <code>fst</code> and <code>snd</code> involved in the diagram for pushouts and vice versa</p>

#### [ Scott Morrison (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174292):
<p>remember the morphisms there are terms of one-element types</p>

#### [ Scott Morrison (Oct 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174303):
<p>maybe we should just make all those morphisms types <code>punit</code>.</p>

#### [ Scott Morrison (Oct 20 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174308):
<p>and not have names at all</p>

#### [ Scott Morrison (Oct 20 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174365):
<p>we just have to name the objects here, so we'd have <code>inductive walking_pullback | left | right | one</code></p>

#### [ Mario Carneiro (Oct 20 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174368):
<p>I don't think so... the type is a inductive family with two elements</p>

#### [ Reid Barton (Oct 20 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174370):
<p>As they say, no names is good names</p>

#### [ Scott Morrison (Oct 20 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174396):
<p>why? we need to have a type of morphisms from <code>left</code> to <code>one</code>, and it contains only <code>inl</code>.</p>

#### [ Scott Morrison (Oct 20 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174400):
<p>etc</p>

#### [ Reid Barton (Oct 20 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174403):
<p>It depends on whether you want to define <code>hom</code> as a single inductive family, or a type defined by case analysis</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174418):
<p>I think types by case analysis is a bad idea</p>

#### [ Scott Morrison (Oct 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174462):
<p>remember <code>hom : obj -&gt; obj -&gt; Type</code></p>

#### [ Reid Barton (Oct 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174474):
<p>I agree it probably makes the finite amount of work it takes to set up these categories and describe functors from them larger</p>

#### [ Scott Morrison (Oct 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174475):
<p>maybe I'm confused here</p>

#### [ Reid Barton (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174478):
<p>I don't know if it has any longer term consequences though</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174484):
<p><code>inductive hom | inl : hom left 1 | inr : hom right 1</code></p>

#### [ Scott Morrison (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174486):
<p>I see</p>

#### [ Scott Morrison (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174487):
<p>okay, that does sound good</p>

#### [ Scott Morrison (Oct 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174489):
<p>but makes it harder to name things. :-)</p>

#### [ Reid Barton (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174527):
<p>what about identities though? I think the truly correct way to do this is to go through the free graph construction</p>

#### [ Reid Barton (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174531):
<p>Er, free category on a graph construction</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174533):
<p>I was just about to say the same</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174534):
<p>this is a graph, not a cat</p>

#### [ Reid Barton (Oct 20 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174536):
<p>which I do have written down somewhere</p>

#### [ Scott Morrison (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174539):
<p>yes... I have this as well. It is extraordinarily painful to use, and this is why I hadn't previously pursued this approach.</p>

#### [ Reid Barton (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174542):
<p>but I'm still not sure whether it makes any difference once we're done defining all these little categories</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174547):
<p>really? I wouldn't have expected that</p>

#### [ Scott Morrison (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174549):
<p>but Reid, isn't your point that "all these little categories" is not a fixed set?</p>

#### [ Reid Barton (Oct 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174552):
<p>Specifically, it should be easy enough to change our mind about the definitions of these categories later, right?<br>
As long as we have a usable interface for building functors out of them</p>

#### [ Reid Barton (Oct 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174619):
<p>for example: there is some category called <code>parallel_pair</code>, and to define a functor <code>parallel_pair \func C</code> I have to give you two objects (a b : C) and two maps (f g : a \hom b)</p>

#### [ Scott Morrison (Oct 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174627):
<p>yes</p>

#### [ Scott Morrison (Oct 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174633):
<p>my preference would be on the first cut to define the slightly larger  indexed inductive types for morphisms that include identity morphisms.</p>

#### [ Reid Barton (Oct 20 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174634):
<p>and then... there is some extensionality rule or something... and then it doesn't matter what goes inside. Right?<br>
And nobody really needs to care about the choices of names, since I just renamed everything <code>a b f g</code> anyways</p>

#### [ Scott Morrison (Oct 20 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174676):
<p>and only later to pursue defining these as path categories on graphs (because I don't know how to do this well)</p>

#### [ Reid Barton (Oct 20 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174678):
<p>As long as we can maintain this interface, it shouldn't matter whether we use the free category on a graph, or define hom as an indexed inductive type, or define hom by case analysis</p>

#### [ Reid Barton (Oct 20 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174683):
<p>or define the category as a poset if it happens to be one</p>

#### [ Scott Morrison (Oct 20 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174688):
<p>I can't see to find my previous attempt to construct equalizers, based on a free category, out of limits, which was so unpleasant...</p>

#### [ Reid Barton (Oct 20 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174736):
<p>I admit I never actually used my free category construction to do anything. I was going to use it to prove that Cat has coequalizers... but I didn't.</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174758):
<p>Oh hey, are graphs an example of <code>has_hom</code>?</p>

#### [ Reid Barton (Oct 20 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174780):
<p>That depends on what <code>has_hom</code> means exactly--this example was in the back of my mind when commenting on that aspect of Simon's PR</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174823):
<p>assuming categories extend it, it must mean the notation, with hom and objects</p>

#### [ Reid Barton (Oct 20 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174824):
<p>I think Scott convinced me at one point that it was better to not build <code>category</code> on top of <code>graph</code>, but I don't remember why exactly... maybe if we rename <code>graph</code> to <code>has_hom</code> it is more palatable, haha</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174883):
<p>I kind of want to reserve the name <code>graph</code> for <em>small</em> <code>has_hom</code>s</p>

#### [ Reid Barton (Oct 20 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174893):
<p>Mario I'm glad you agree--there's this discussion about what to rename <code>has_hom</code> to in Simon's PR, which is really "the data of a category without the laws"</p>

#### [ Reid Barton (Oct 20 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174900):
<p>That would just be specializing the universe parameters of <code>has_hom</code> to be equal right?</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174949):
<p>I think so? I'm not sure that's small enough. Maybe it doesn't make sense</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174956):
<p>I want <code>graph A : Type u</code> when <code>A : Type u</code></p>

#### [ Mario Carneiro (Oct 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174960):
<p>but there's no way I'm going to get that</p>

#### [ Reid Barton (Oct 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174961):
<p>A graph is a set of vertices, together with a set of edges from a to b for each a and b</p>

#### [ Reid Barton (Oct 20 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136174964):
<p>Well, if graph isn't allowed to have multiple edges...</p>

#### [ Mario Carneiro (Oct 20 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175003):
<p>yeah, simple graphs solve the problem</p>

#### [ Reid Barton (Oct 20 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175008):
<p>I guess actual graph theorists would call this a multigraph</p>

#### [ Reid Barton (Oct 20 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175074):
<p>Anyways <code>graph</code>s would also be examples of <code>has_hom</code> in any case</p>

#### [ Reid Barton (Oct 20 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175113):
<p>Anyways anyways, my overall claim is that these names don't really matter either, because people should only be using the interface like <code>parallel_pair_functor f g</code>.</p>

#### [ Reid Barton (Oct 20 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175312):
<p>Maybe that means the things to do is to pick the variable names which appear in the interface (like <code>f</code> and <code>g</code>?) and then choose the names of generating morphisms based on them in some systematic way (like <code>F</code> and <code>G</code>?)</p>

#### [ Reid Barton (Oct 20 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136175325):
<p>or whatever naming convention seems least likely to collide with other relevant things, maybe <code>F</code> is a bad name</p>

#### [ Kevin Buzzard (Oct 20 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136178333):
<blockquote>
<p>The reason is that <code>\_1</code> and <code>\_2</code> aligns better with Lean's builtin <code>p.1</code> and <code>p.2</code></p>
</blockquote>
<p>I was surprised once when I realised that the builtin notation was not <code>p.0</code> and <code>p.1</code> but presumably could have been, given that Lean was written by CS people.</p>

#### [ Scott Morrison (Oct 21 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136199413):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, <span class="user-mention" data-user-id="112680">@Johan Commelin</span>, I experimented with a new design for "special" shape limits. Now they are all defined as special cases of limits. If you want to have a quick look, see <a href="https://github.com/leanprover-community/mathlib/tree/limits-others-new/category_theory/limits" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/limits-others-new/category_theory/limits">https://github.com/leanprover-community/mathlib/tree/limits-others-new/category_theory/limits</a>.</p>

#### [ Scott Morrison (Oct 21 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136199421):
<p>I think it looks reasonable. I would like to try proving some things about limits in functor categories, and make sure they immediately imply the corresponding results about pullbacks/products/etc.</p>

#### [ Scott Morrison (Oct 23 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136302717):
<p>I'm going to make other fundamental changes, I think.</p>

#### [ Scott Morrison (Oct 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136302755):
<p>(deleted)</p>

#### [ Scott Morrison (Oct 23 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136302808):
<p>I'm going to change <code>cone F</code> at least so that it is an object, bundled with a natural transformation from the constant functor (with value that object) to <code>F</code>. I may go all the way and just define <code>cone F</code> as a special case of a comma category. That had, long ago, been my initial version of limits, but I was having too much trouble with it. Having learnt a few things, I think it's viable again, so will try again. :-)</p>

#### [ Reid Barton (Oct 23 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136303069):
<p>I wanted exactly this description in order to prove that right adjoints preserve limits</p>

#### [ Johan Commelin (Oct 23 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136319006):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Cool! That sounds like a good generalisation.<br>
Concretely, you had a definition of sheaves, and I have almost generalised it to arbitrary sites. The real test case is probably going to be sheafification, and more generally pushforward and pullbacks of sheaves (and the fact that those are adjoint).</p>

#### [ Johan Commelin (Oct 23 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/yoneda/near/136324809):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> How general are you planning to set up comma categories? Only slices over an object, or the general thing where you start with two functors?</p>


{% endraw %}
