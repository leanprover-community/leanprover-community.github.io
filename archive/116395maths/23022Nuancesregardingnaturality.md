---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/23022Nuancesregardingnaturality.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Nuances regarding naturality](https://leanprover-community.github.io/archive/116395maths/23022Nuancesregardingnaturality.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Oct 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135266364):
<p><a href="https://mathoverflow.net/questions/244131/nuances-regarding-naturality?noredirect=1&amp;lq=1" target="_blank" title="https://mathoverflow.net/questions/244131/nuances-regarding-naturality?noredirect=1&amp;lq=1">https://mathoverflow.net/questions/244131/nuances-regarding-naturality?noredirect=1&amp;lq=1</a></p>
<p>Does Lean have a good answer to this question? My understanding is that the OP is trying to define data which involves an uncomputable choice of some other data (and it's a theorem that such a choice can always be made in at least one way) and then a proof that the data we care about is independent of this uncomputable choice.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135266773):
<p>Is the function that sends a vector space to the cardinal corresponding to its dimension any "better" in any way than the function that sends a vector space to a basis which was chosen using the axiom of choice?</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135271784):
<p>Perhaps I'm missing something, but the dimension function is defined using the "choose-a-basis" function, right?</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135271867):
<p>I ran into this when I was working on the rank function for matroids (which is a generalization of dimension for f.d. vector spaces); even with unique existence, you still have to apply some form of choice to define the actual nat.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272437):
<p>Yes. The question is whether the added nuance of the proof that the output is independent of the choice can be expressed in Lean. A mathematician might argue that they hadn't "seriously" used choice, or something. I was wondering if there was anything in this.</p>

#### [ Chris Hughes (Oct 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272490):
<p>It could still be done computably, using <code>trunc</code>, instead of<code> exists</code>, and <code>quot.lift</code> instead of choice.</p>

#### [ Reid Barton (Oct 05 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272523):
<p>The dimension function can be defined using only "unique choice" <code>nonempty a -&gt; (\all x y : a, x = y) -&gt; a</code>. This is just as noncomputable as full choice but philosophically less problematic (at least to me) because the type of the "unique choice" constant is a subsingleton.</p>

#### [ Reid Barton (Oct 05 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272533):
<p>Another formulation is <code>nonempty a -&gt; trunc a</code>, yes</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272596):
<p>At the time I ended up throwing in an <code>encodable</code> instance. I'll have to look into <code>trunc</code> now that I know a little more about it though.</p>

#### [ Reid Barton (Oct 05 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272696):
<p>The "pick a basis" function is different because its value depends on the interpretation of the <code>choice</code> constant</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135273811):
<p>What's <code>nonempty a -&gt; trunc a</code>? I see <code>nonempty_of_trunc</code> in mathlib but not the other way around. Is this because in lean's foundations there's no unique choice? To define the dimension function in lean, am I right that you could only do it by returning the cardinality of "pick a basis"? Well-definedness would be proven and used separately I suppose.</p>

#### [ Reid Barton (Oct 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135273995):
<p><code>choice</code>, then <code>trunc.mk</code></p>

#### [ Reid Barton (Oct 05 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274205):
<p>Lean's core library only has the axiom <code>choice</code>, and derives all the other classical principles from it. So in this setup you can't make fine distinctions between things like using choice and only using unique choice. However, you could imagine adding unique choice (and LEM) as separate axioms.</p>

#### [ Reid Barton (Oct 05 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274280):
<p>You could also add the "axiom of choice" (which is a Prop) as a separate axiom.</p>

#### [ Reid Barton (Oct 05 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274327):
<p>Then you could define the dimension function using only the "axiom of choice" (to prove <code>nonempty (basis V)</code>) and "unique choice" (to extract the dimension)--in order to do this you <em>have</em> to prove that every basis has the same cardinality</p>

#### [ Reid Barton (Oct 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274384):
<p>Both of these axioms are subsingletons, so you can conclude that the dimension of a vector space doesn't depend on the interpretation of <code>choice</code> or on any other "arbitrary choices".</p>

#### [ Reid Barton (Oct 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274415):
<p>You cannot define the "pick a basis" function this way</p>

#### [ Kenny Lau (Oct 05 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274693):
<p>is it possible to define <code>trunc (basis V)</code> computably?</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274730):
<p>How are you given <code>V</code>?</p>

#### [ Kenny Lau (Oct 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274795):
<div class="codehilite"><pre><span></span>k : Type u
V : Type v
_inst_1 : field k
_inst_2 : vector_space k V
</pre></div>

#### [ Chris Hughes (Oct 05 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274888):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> providing a truncated basis could be part of the definition of finite dimensional vector space.</p>

#### [ Chris Hughes (Oct 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274976):
<p>For the infinite case you can't do it, but who cares when cardinals don't have decidable equality.</p>

#### [ Kenny Lau (Oct 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274977):
<p>so essentially I'm asking for a term of the type <code>\Pi (k : Type u) (V : Type v) [field k] [vector_space k V], trunc (basis k V)</code></p>


{% endraw %}
