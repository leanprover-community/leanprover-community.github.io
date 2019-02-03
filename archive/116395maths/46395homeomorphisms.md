---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/46395homeomorphisms.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [homeomorphisms](https://leanprover-community.github.io/archive/116395maths/46395homeomorphisms.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jun 01 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127431536):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>, did you have a definition of homeomorphisms somewhere?</p>

#### [ Patrick Massot (Jun 01 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127431596):
<p><a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean</a></p>

#### [ Reid Barton (Jun 01 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127432191):
<p>thanks! I like this <code>extends equiv</code> idea</p>

#### [ Patrick Massot (Jun 01 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127435414):
<p>This was Mario's idea. At that time I had no idea <code>equiv</code> existed</p>

#### [ Kenny Lau (Jun 01 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127435457):
<p>just do it in a category man</p>

#### [ Kevin Buzzard (Jun 01 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437006):
<p>won't there be universe issues?</p>

#### [ Kenny Lau (Jun 01 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437010):
<p>just build a category theory without universe issue, man</p>

#### [ Kevin Buzzard (Jun 01 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437112):
<p>I think Russell had something to say about that</p>

#### [ Kenny Lau (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437168):
<p>the category itself as an object has universe issues</p>

#### [ Kenny Lau (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437170):
<p>if you use the things within, you should be fine</p>

#### [ Kevin Buzzard (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437171):
<p>I never really understood the issues that Scott had with universes but my impression is that things are harder than you might think</p>

#### [ Kenny Lau (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437173):
<p>(there's a different category for each universe)</p>

#### [ Kenny Lau (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437175):
<p>(but it doesn't matter)</p>

#### [ Kevin Buzzard (Jun 01 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437712):
<p>my understanding is that sometimes it does matter</p>

#### [ Kevin Buzzard (Jun 01 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437718):
<p>because maybe you end up with the right object but in the wrong universe</p>

#### [ Scott Morrison (Jun 02 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127440872):
<p>The problem with universes (which is the sole reason I didn't have a PR ready months ago) is that there are genuinely two different sorts of categories one needs in mathematics: "small categories", in which objects and morphisms live in the same fixed universe, and "large categories", in which objects get to live in one higher universe than the morphisms.</p>

#### [ Scott Morrison (Jun 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127440923):
<p>For a very long time in my pre-Lean mathematical career, I thought this wasn't such a big deal, but I've learnt better. :-)</p>

#### [ Scott Morrison (Jun 02 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441044):
<p>(Briefly: we need large categories because all the basic algebra examples like <code>Types</code>, <code>Groups</code>, <code>PL</code>, etc are large. We need small categories because if you try thinking about any of the basic machinery in category theory, particularly taking limits, when you index over objects in a large category you find yourself having to move up the universe hierarchy over and over again, while when you index over objects in a small category you can stay at one level. Happily, one can get away with doing most of mathematics only having to index over a small category --- but not quite all, so eventually you need to admit that the universe parameter can vary across a development.)</p>

#### [ Scott Morrison (Jun 02 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441103):
<p>So, how to implement this? We don't want to have parallel developments of small and large categories, because then we'd have at least 3 different types of functors (small to small, small to large, large to large -- large to small is just silly, of course :-), and lifts between these, and then more mess at the level of transformations, and it will all end badly.</p>

#### [ Scott Morrison (Jun 02 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441107):
<p>The two options I considered were:</p>

#### [ Scott Morrison (Jun 02 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441133):
<p>1) "categories" by default have objects in <code>Type (u+1)</code> and morphisms in <code>Type u</code>, and a small category is a category along with the additional evidence that the objects are equivalent in something in <code>Type u</code> after all.</p>

#### [ Scott Morrison (Jun 02 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441186):
<p>2) We define "categories" to have two universe parameters, so objects live in <code>Type u</code> and morphisms in <code>Type v</code>, and define "small_category" and "large_category" as subclasses (with <code>u=v</code> and <code>u=v+1</code> respectively).</p>

#### [ Scott Morrison (Jun 02 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441203):
<p>In the end, it seems that 1) just doesn't work; I found that I was having to implement multiple sorts of functors and natural transformations anyway.</p>

#### [ Scott Morrison (Jun 02 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441301):
<p>2) mostly works. You develop as much as you need at the level of "independent universe" categories, but then when it makes sense restrict to either <code>small_category</code> or <code>large_category</code>. Working entirely with independent universe categories becomes problematic, because Lean usually can't infer the morphism universe level. Mostly you can get around this just by specifying that level explicitly, but it also starts to break typeclass inference and so eventually becomes a serious problem.</p>


{% endraw %}
