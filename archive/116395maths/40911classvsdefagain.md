---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/40911classvsdefagain.html
---

## Stream: [maths](index.html)
### Topic: [class vs def again](40911classvsdefagain.html)

---


{% raw %}
#### [ Patrick Massot (Jul 16 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129776099):
<p>Variation on a well-known theme: should uniform continuity of a map <code>f</code> between uniform spaces <code>a</code> and <code>b</code> be a <code>def</code> or a <code>class</code>? Or should we bundle <code>f</code> and its uniform continuity?  Currently we have a <code>def</code> and no bundling. As usual, this is all convenient to prove properties of individual maps, or compositions of two such maps. Now let's get functorial. I want to promote each such <code>f</code> to a map between the respective Hausdorff completions of <code>a</code> and <code>b</code>.  Of course in math this would be called <code>completion_lift f</code>. This currently doesn't make sense in mathlib, we need a term <code>h : uniform_continuous f</code>. So we could write <code>completion_lift f h</code>. But <code>f</code> can be inferred from <code>h</code>, so common sense dictates it should be an implicit argument, and we end up with <code>completion_lift h</code>. And it looks <em>weird</em>. And it gets worse when stating and proving properties of <code>completion_lift</code>, especially functoriality that should read <code>completion_lift f' ∘ f = (completion_lift f') ∘ completion_lift f </code> but actually reads <code>completion_lift (uniform_continuous.comp h h') = (completion_lift h') ∘ completion_lift h</code>.</p>

#### [ Patrick Massot (Jul 16 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129776108):
<p>What should we do?</p>

#### [ Patrick Massot (Jul 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129776783):
<p>See <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean</a> for the concrete situation</p>

#### [ Patrick Massot (Jul 16 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129776974):
<p>I had a lot of fun doing all this after proving the universal mapping property for completions. It was fun because it was really very close to a paper and pencil proof. But I wouldn't find it fun to do this ten times. I can't wait until we get nice abstract non-sense in mathlib. How far are we from merging <span class="user-mention" data-user-id="110087">@Scott Morrison</span> PR? Has anyone heard from Scott recently?</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778526):
<p>The last few times I've been asked this I advocated the bundled function approach and it's worked well thus far</p>

#### [ Patrick Massot (Jul 17 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778652):
<p>Question is then how to handle the existing code base? How to avoid duplicating too much stuff. I guess we still want to keep the current Prop</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778896):
<p>Hm, good point. Is it possible to define <code>completion_lift f</code> without the continuity assumption?</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778901):
<p>i.e. take a default value</p>

#### [ Patrick Massot (Jul 17 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778911):
<p>It depends on <code>dense_embedding.extend</code> we were discussing earlier today</p>

#### [ Patrick Massot (Jul 17 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778935):
<p>see <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean#L95-L96" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean#L95-L96">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean#L95-L96</a></p>

#### [ Mario Carneiro (Jul 17 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778936):
<p><code>dense_embedding.extend</code> doesn't require continuity</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778979):
<p>oh, weird, a unique exists</p>

#### [ Patrick Massot (Jul 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778993):
<p>well, it doesn't require it until <code>ext_e_eq</code></p>

#### [ Patrick Massot (Jul 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129778999):
<p>unique exitsts are everywhere in this abstract nonsense business</p>

#### [ Patrick Massot (Jul 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779005):
<p>That's an important part of the universal property</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779008):
<p>oh sure, but mathlib basically never uses it</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779056):
<p>it always defines the unique thing with a concrete term</p>

#### [ Patrick Massot (Jul 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779058):
<p>that's because it lacks basic category theory support</p>

#### [ Patrick Massot (Jul 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779066):
<p>I don't want a definition with a concrete term, I want the abstract interface, as in my file</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779069):
<p>no, there are plenty of places where math dictates a unique existence, it's just easier to work with terms</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779079):
<p>If you look at scott's development I think he's done the same</p>

#### [ Patrick Massot (Jul 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779121):
<p>even the explicit construction of <code>completion</code> and <code>to_completion</code> will need to be complemented by a uniqueness up to unique iso result. This is my plan for tomorrow, as well as deducing that completion of a product is isomorphic to product of completions</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779122):
<p>I'm sure Kevin can discuss his experiences with <code>sqrt_exists</code></p>

#### [ Patrick Massot (Jul 17 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779137):
<p>Probably the best is to have an explicit term <em>and</em> a uniqueness lemma</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779148):
<p>right</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779152):
<p>the uniqueness lemma says something like <code>x = my_thing &lt;-&gt; property</code></p>

#### [ Patrick Massot (Jul 17 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779198):
<p>I still don't know how to do that in this case. Because that <code>de.ext</code> is only half the construction. Then it must still descend to a quotient (lift to a quotient in Lean-speak)</p>

#### [ Patrick Massot (Jul 17 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779201):
<p><a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean#L99" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean#L99">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/1e1fb6f6e6b03eb2e5d436851aaaa8e8fc3f1582/src/for_mathlib/completion.lean#L99</a></p>

#### [ Mario Carneiro (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779202):
<p>Still, you've constructed the term</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779208):
<p><code>g</code> in the proof</p>

#### [ Patrick Massot (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779210):
<p>this uses uniform continuity</p>

#### [ Patrick Massot (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779214):
<p>no, <code>g</code> needs <code>compat</code></p>

#### [ Mario Carneiro (Jul 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779220):
<p>right, it's defined by lift on the quotient</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779283):
<p>I'm not asking you to prove the theorem without the assumption, or even do the construction without uniform continuity</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779292):
<p>I want to see if you can do a similar thing to what I did for <code>extend</code></p>

#### [ Patrick Massot (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779295):
<p>Then I don't understand what you suggest</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779297):
<p>If <code>A</code> is empty, is <code>completion A</code> also empty?</p>

#### [ Patrick Massot (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779300):
<p>yes</p>

#### [ Patrick Massot (Jul 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779303):
<p>(I hope)</p>

#### [ Patrick Massot (Jul 17 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779342):
<p>In my mind it is certainly empty</p>

#### [ Patrick Massot (Jul 17 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779346):
<p>but I'm not an expert in zerology</p>

#### [ Mario Carneiro (Jul 17 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779426):
<p>Then you can follow a similar proof to what I did. Define <code>completion.extend f</code> by cases on <code>uniform_continuous f</code>. If it is, do the regular thing. Otherwise, we can pick an arbitrary element of <code>B</code> by <code>choice</code>. We know it is nonempty because we are given an element of <code>completion A</code> so we can prove <code>A</code> is nonempty, so <code>a : A</code> means <code>f a : B</code></p>

#### [ Patrick Massot (Jul 17 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779662):
<p>Oh. This is twisted</p>

#### [ Patrick Massot (Jul 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779781):
<p>I'll try that tomorrow, before moving on to products. It seems we don't have an instance for completion of a product of complete spaces, so there will be preparation work.</p>

#### [ Patrick Massot (Jul 17 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779858):
<p>If I'm lucky I'll even get a <code>dense_embedding.extend</code> without inhabitants in mathlib when I'll wake up <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (Jul 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129779882):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> don't hesitate to have a look at the current state of <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean</a> and comment. It's all for the perfectoid project.</p>

#### [ Kevin Buzzard (Jul 17 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129798324):
<p>Patrick I'm really grateful for all of this. The perfectoid project shouldn't be too hard to do. The hard part with schemes was proving that the structure presheaf on Spec(R) was a sheaf because this had all sorts of unexpected pitfalls. The analogous statement for adic spaces isn't true -- an affinoid adic space is <em>defined</em> to be an affinoid pre-adic space Spa(R) for which the structure presheaf happens to be a sheaf, so that is a huge hurdle that we don't have to deal with. Completions are, I think, the main technical issue left, and you are dealing with them. I will try and focus on continuous valuations.</p>

#### [ Johan Commelin (Jul 19 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129917105):
<blockquote>
<p>Has anyone heard from Scott recently?</p>
</blockquote>
<p>I haven't seen Scott here for a while. Maybe it's time for (winter?) holidays down under?</p>

#### [ Patrick Massot (Jul 19 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129921084):
<p>Maybe. He also doesn't answer emails.</p>

#### [ Patrick Massot (Jul 19 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129931031):
<p>His webpage revealed <a href="https://tqft.net/calendar/" target="_blank" title="https://tqft.net/calendar/">https://tqft.net/calendar/</a> which pretty clearly indicates winter vacations.</p>

#### [ Johan Commelin (Jul 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/class%20vs%20def%20again/near/129935705):
<p>It also means he should be back next week (-;</p>


{% endraw %}
