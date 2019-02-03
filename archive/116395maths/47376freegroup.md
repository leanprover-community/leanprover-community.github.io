---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/47376freegroup.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [free group](https://leanprover-community.github.io/archive/116395maths/47376freegroup.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 01 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494694):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  here's my old version of free group <a href="https://github.com/kckennylau/Lean/blob/c6eac863b23d58d40deaab62489f6069f860407e/free_group.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/c6eac863b23d58d40deaab62489f6069f860407e/free_group.lean">https://github.com/kckennylau/Lean/blob/c6eac863b23d58d40deaab62489f6069f860407e/free_group.lean</a></p>

#### [ Kenny Lau (Apr 01 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494732):
<p>is this what you wanted?</p>

#### [ Kenny Lau (Apr 01 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494739):
<p>you see, ambient has two universe parameters</p>

#### [ Kenny Lau (Apr 01 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494792):
<p>and this fucks up everything</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494806):
<p>Yes!</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494807):
<p>I thought Lean would somehow fix this, but the stupid issue is still there.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494846):
<p>Maybe you can get  a contradiction with a diagonal argument if you can get it to work all in the same universe :-)</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494847):
<p>I didn't read all of what Mario had to say about this.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494854):
<p>It's a bit annoying though</p>

#### [ Kenny Lau (Apr 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494860):
<p>it's maximally impredicative</p>

#### [ Kenny Lau (Apr 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494861):
<p>it's philosophically unsound</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494862):
<p>You could be even less constructive by replacing generate with span</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494903):
<p>I never know which is which</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494905):
<p>they are synonymous in my head</p>

#### [ Kenny Lau (Apr 01 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494906):
<p>you can't just quantify through every gorup and pretend that you have the UMP wrt every group</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494911):
<p>but the one where you say "if I am a subgroup of the big product containing S, then I contain span S"</p>

#### [ Kenny Lau (Apr 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494912):
<p>the point is</p>

#### [ Kenny Lau (Apr 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494913):
<p>you need to build the ambient group from S</p>

#### [ Kenny Lau (Apr 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494914):
<p>if you want things to work</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494954):
<p>I don't really understand why you can't just quantify through every group and pretend you have the UMP. Maybe I should read Mario's posts more carefully, wherever they've gone</p>

#### [ Kenny Lau (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494956):
<p>because it's cheating</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494958):
<p>I don't want to make the set of all sets</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494960):
<p>not because it's cheating</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494961):
<p>but because it leads to hell</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494962):
<p>whereas free groups won't take you to hell</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494963):
<p>because they really do exist</p>

#### [ Kenny Lau (Apr 01 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494967):
<p>right</p>

#### [ Kenny Lau (Apr 01 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494970):
<p>but that isn't the way to justify it</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495021):
<p>To build the free group in the ZFC approach, do you first build the abstract group (the subset of the product) and then say "aah it's generated by S so there's something isomorphic to it in V_kappa"?</p>

#### [ Kenny Lau (Apr 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495025):
<p>correct</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495026):
<p>Can one prove such a theorem in Lean?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495031):
<p>"If I am an object in some universe then sometimes you can build some object in some smaller universe which is isomorphic to me"</p>

#### [ Kenny Lau (Apr 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495075):
<p>actually</p>

#### [ Kenny Lau (Apr 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495077):
<p>what cardinality do you need?</p>

#### [ Kenny Lau (Apr 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495083):
<p>if you have n letters, to make a word of length k, you have at most k! n^k ways right</p>

#### [ Kenny Lau (Apr 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495084):
<p>no, just n^k</p>

#### [ Kenny Lau (Apr 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495086):
<p>so it's just n^omega</p>

#### [ Kenny Lau (Apr 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495126):
<p>hmm</p>

#### [ Kenny Lau (Apr 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495127):
<p>I mean</p>

#### [ Kenny Lau (Apr 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495128):
<p>now that I built it in the proper way, I don't see why we're beating a dead horse</p>

#### [ Kenny Lau (Apr 01 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495179):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> ves algum problema em o meu pull?</p>

#### [ Kenny Lau (Apr 01 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495277):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> "but that impredicative construction is not like constructing the set of all sets because it really exists" it is actually only correct iff you can justify its existence predicatively. that's the wrong justification for the right thing, and it doesn't tell you that it actually exists</p>

#### [ Kevin Buzzard (Apr 01 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496544):
<p><code>n^omega</code> is not at all the sum of <code>n^k</code> as I'm sure you know. Finitely-generated groups are all countable.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496589):
<p>The point is that if <code>S</code> has cardinality <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span> and if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>κ</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">\kappa'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">κ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> is the max of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="normal">ℵ</mi><mn>0</mn></msub></mrow><annotation encoding="application/x-tex">\aleph_0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.84444em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathrm">ℵ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> then any group generated by <code>S</code> has cardinality at most <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>κ</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">\kappa'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">κ</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Kevin Buzzard (Apr 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496590):
<p>eew what kind of a <code>\kappa</code> is that</p>

#### [ Kenny Lau (Apr 01 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496824):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> by n^omega I mean union n^k</p>

#### [ Kenny Lau (Apr 01 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496825):
<p>ordinal exponent</p>

#### [ Mario Carneiro (Apr 01 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497132):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> You can do such "arguments by cardinality" for universe resizing in lean as well. An example of this is:</p>
<div class="codehilite"><pre><span></span>theorem  lift_down {a : cardinal.{u}} {b : cardinal.{max u v}} : b ≤ lift a → ∃ a&#39;, lift a&#39; = b
</pre></div>


<p>which says that a cardinal that is smaller than a cardinal lifted from a small universe is also lifted from the small universe</p>

#### [ Kenny Lau (Apr 01 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497193):
<p>that epsilon-abstraction though <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Apr 01 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497199):
<p>say what?</p>

#### [ Kenny Lau (Apr 01 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497208):
<p>so you can't find that cardinal explicitly</p>

#### [ Mario Carneiro (Apr 01 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497215):
<p>which cardinal are you referring to? the exists in that theorem is unique</p>

#### [ Kenny Lau (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497255):
<p>axiom of unique choice?</p>

#### [ Mario Carneiro (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497259):
<p>cardinal theory uses choice everywhere, so meh</p>

#### [ Kenny Lau (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497261):
<p>i see</p>

#### [ Kenny Lau (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497262):
<p>fair enough</p>

#### [ Mario Carneiro (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497263):
<p>but it is explicitly constructed</p>

#### [ Kenny Lau (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497264):
<p>so do you see any problem with my pr</p>

#### [ Mario Carneiro (Apr 01 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497279):
<p>I don't think so. The only other thing I might want is a constructive reduced word function</p>

#### [ Kenny Lau (Apr 01 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497320):
<p>hmm</p>

#### [ Kenny Lau (Apr 01 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497529):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> linked list though</p>

#### [ Kenny Lau (Apr 01 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497631):
<p>you need decidable equality</p>

#### [ Kenny Lau (Apr 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124499790):
<p><a href="https://github.com/kckennylau/Lean/blob/master/free_group.lean#L266" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/free_group.lean#L266">https://github.com/kckennylau/Lean/blob/master/free_group.lean#L266</a></p>

#### [ Kenny Lau (Apr 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124499791):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> done!</p>

#### [ Kenny Lau (Apr 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512164):
<p><a href="https://github.com/kckennylau/category-theory/blob/master/src/free_group.lean" target="_blank" title="https://github.com/kckennylau/category-theory/blob/master/src/free_group.lean">https://github.com/kckennylau/category-theory/blob/master/src/free_group.lean</a></p>

#### [ Kenny Lau (Apr 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512166):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> could you help me prove <code>reduce.exact</code>?</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512261):
<p>do you know that the reduced word is minimal in length in the equivalence class?</p>

#### [ Kenny Lau (Apr 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512264):
<p>yes</p>

#### [ Kenny Lau (Apr 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512267):
<p>that's <code>reduce.min</code></p>

#### [ Mario Carneiro (Apr 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512272):
<p>that just says that the reduced word is smaller than the input</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512280):
<p>I mean if v ~~ w then length (reduce w) &lt;= length v</p>

#### [ Kenny Lau (Apr 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512283):
<p>oh, I don't know that then</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512336):
<p>You may find <a href="http://us.metamath.org/mpeuni/mmtheorems154.html" target="_blank" title="http://us.metamath.org/mpeuni/mmtheorems154.html">http://us.metamath.org/mpeuni/mmtheorems154.html</a> helpful; that's my construction of free groups in metamath by a similar method (it's more cumbersome in ZFC since it has to describe the whole reduction sequence, not just the result)</p>

#### [ Kenny Lau (Apr 02 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512381):
<p>...</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512522):
<p>I think I see the proof strategy. It goes by induction on the length of an extension sequence, proving that if two extension sequences (where one has length &lt;= n) end at the same point, then they start at the same point</p>

#### [ Kenny Lau (Apr 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512523):
<p>I thought you wrote it</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512524):
<p>I'm rereading the proof now</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512530):
<p>An extension sequence is a sequence that starts at a reduced word and inserts cancelling pairs one at a time</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512533):
<p>and the first step in the proof shows that every word has an extension sequence that terminates with it</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512626):
<p>Since the length of an extension sequence is also (half) the difference in length between the initial word and the reduced word, you could try induction on that</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513001):
<p>Okay, here's a suggestion in your language: can you prove the following?</p>
<div class="codehilite"><pre><span></span>inductive red (IT : Type u) [inv_type IT] :
  inv_type.to_inv_mon IT → inv_type.to_inv_mon IT → Prop
| cons : ∀ a x y, red x y → red (a :: x) (a :: y)
| cancel : ∀ a x, red (a :: a⁻¹ :: x) x

theorem eqv_gen_red (IT : Type u) [inv_type IT]
  {x y : inv_type.to_inv_mon IT} : x ≈ y ↔ eqv_gen (red IT) x y :=
sorry
</pre></div>

#### [ Mario Carneiro (Apr 02 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513020):
<p>this will considerably simplify your induction for the <code>reduce.exact</code> theorem</p>

#### [ Kenny Lau (Apr 02 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513023):
<p>but I don't need to simply <code>reduced.sound</code>, I need to prove <code>reduced.exact</code></p>

#### [ Mario Carneiro (Apr 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513068):
<p>yeah that</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513074):
<p>You could also fold in the eqv_gen constructors into the constructors of <code>red</code> if you prefer</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513077):
<p>although splitting it this way gives you the ability to talk about one step reduction</p>

#### [ Kenny Lau (Apr 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513180):
<p>proving multiplication amounts to the same amount of work</p>

#### [ Kenny Lau (Apr 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513182):
<div class="codehilite"><pre><span></span>case inv_mon.to_group.rel.mul
IT : Type u,
_inst_1 : inv_type IT,
x y c d p q : inv_type.to_inv_mon IT,
h1 : inv_mon.to_group.rel (inv_type.to_inv_mon IT) c p,
h2 : inv_mon.to_group.rel (inv_type.to_inv_mon IT) d q,
ih1 : eqv_gen (red IT) c p,
ih2 : eqv_gen (red IT) d q
⊢ eqv_gen (red IT) (c * d) (p * q)
</pre></div>

#### [ Kenny Lau (Apr 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513183):
<p>i.e. I can't prove it</p>

#### [ Mario Carneiro (Apr 02 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513231):
<p>Try proving <code>eqv_gen (red IT) x y -&gt;  eqv_gen (red IT) (a * x * b) (a * y * b)</code></p>

#### [ Mario Carneiro (Apr 02 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513281):
<p>which reduces to <code>red IT x y -&gt; red IT (a * x * b) (a * y * b)</code></p>

#### [ Mario Carneiro (Apr 02 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513325):
<p>(You could also do the left and right multiplications as separate lemmas)</p>


{% endraw %}
