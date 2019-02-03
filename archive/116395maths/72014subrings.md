---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/72014subrings.html
---

## Stream: [maths](index.html)
### Topic: [subrings](72014subrings.html)

---


{% raw %}
#### [ Johan Commelin (Jun 07 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127699034):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- `S` is a subgroup: a set containing 1 and closed under multiplication, addition and and additive inverse. -/</span>
<span class="n">class</span> <span class="n">is_subring</span>  <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="c1">-- would like `extends is_add_subgroup`, but that class doesn&#39;t exist</span>
<span class="o">(</span><span class="n">one_mem</span>       <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span>
<span class="o">(</span><span class="n">mul_mem</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">}</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span>
<span class="o">(</span><span class="n">add_mem</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">}</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span>
<span class="o">(</span><span class="n">inv_mem</span> <span class="o">{</span><span class="n">x</span><span class="o">}</span>   <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="bp">-</span><span class="n">x</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">ring</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">}</span> <span class="o">[</span><span class="n">is_subring</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">S</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johan Commelin (Jun 07 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127699067):
<p>I think the route of defining <code>is_add_subgroup</code> will pay off in the end. Is this again one of those things where <code>[to_additive]</code> should help? The last time I tried that, it didn't work.</p>

#### [ Johan Commelin (Jun 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127699721):
<p>Ok, the easy way out: I'll extend <code>is_submonoid</code>. Even though it feels "unmathematical" to me.</p>

#### [ Kevin Buzzard (Jun 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127703755):
<p>A minimalist definition of subgroup is : non-empty and closed under lam x y,xy^{-1}. Is there any point using this minimalist definition? You could do the same with add_mem and inv_mem here. Does this save time or obfuscate? Or both?</p>

#### [ Johan Commelin (Jun 07 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127706197):
<p>I think it would be best if we could extend both <code>is_submonoid</code> and <code>is_add_subgroup</code>.</p>

#### [ Scott Morrison (Jun 07 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127711064):
<p>Regarding minimalist definitions (<code>x * y^{-1}</code>), I think it is best if the official definition is the bog standard definition, with no clever tricks or surprises. It's fine to then provide an alternative constructor which allows you to take advantage of shortcuts like this if you want them.</p>

#### [ Scott Morrison (Jun 07 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127711149):
<p>Until the constructions become seriously dire, I think it's best to optimise definitions to be usable (after you've constructed instances), rather than easy to satisfy.</p>

#### [ Scott Morrison (Jun 07 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127711160):
<p>(Of course actually redundant things should be lemmas.)</p>

#### [ Johan Commelin (Jun 07 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127723434):
<p><a href="https://github.com/jcommelin/lean-perfectoid-spaces/tree/subring/src/for_mathlib" target="_blank" title="https://github.com/jcommelin/lean-perfectoid-spaces/tree/subring/src/for_mathlib">https://github.com/jcommelin/lean-perfectoid-spaces/tree/subring/src/for_mathlib</a></p>

#### [ Johan Commelin (Jun 07 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127723435):
<p>Here is a small start on subrings</p>

#### [ Johan Commelin (Jun 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758357):
<p>Update: <a href="https://github.com/jcommelin/lean-perfectoid-spaces/blob/subring/src/for_mathlib/subring.lean" target="_blank" title="https://github.com/jcommelin/lean-perfectoid-spaces/blob/subring/src/for_mathlib/subring.lean">https://github.com/jcommelin/lean-perfectoid-spaces/blob/subring/src/for_mathlib/subring.lean</a></p>

#### [ Johan Commelin (Jun 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758368):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> what do you think is the best strategy for integral elements?</p>

#### [ Johan Commelin (Jun 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758422):
<p>Were univariate polynomials already there? Somewhere? Did Chris or Nicholas do this?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758494):
<p>I think lots of people did univariate polynomials</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758500):
<p>but I don't know if anyone submitted a PR</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758507):
<p>I think Kenny proved a universal property</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758520):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> <span class="user-mention" data-user-id="110064">@Kenny Lau</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Did any of you PR a definition of a polynomial in 1 variable into mathlib?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758567):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Note that for the definition of a perfectoid space it might be the case that one only has to formalise the definition, i.e. "I am a root of a monic poly with coefficients in the smaller ring"</p>

#### [ Johan Commelin (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758569):
<p>Yes, that is what I am currently trying to do</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758571):
<p>To prove integral closure is a ring will involve some Noetherian arguments</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758572):
<p>but I am not sure this result is needed</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758573):
<p>We need "I am a subring of R^o"</p>

#### [ Kevin Buzzard (Jun 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758574):
<p>but I am not sure we need "...and by the way R^o is a ring"</p>

#### [ Johan Commelin (Jun 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758614):
<p>Right, we never take the closure (-; We only have stuff that already is a subring, and then prove it is closed</p>

#### [ Johan Commelin (Jun 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127758621):
<p>Oooh, what you are saying is different from what I was saying...</p>

#### [ Johannes Hölzl (Jun 08 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127762328):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  There are no univariate polynomials in mathlib or in a PR. I want to move the polynomials from Mason-Stother proof in July / August.</p>

#### [ Chris Hughes (Jun 08 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127766040):
<p>I will do that once I've done my project.</p>

#### [ Johan Commelin (Jun 08 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127766743):
<p>What is the best way to define the n-th power of an ideal?</p>

#### [ Johan Commelin (Jun 08 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127767182):
<p>Current proposal:</p>
<div class="codehilite"><pre><span></span><span class="n">span</span> <span class="o">{</span><span class="n">i</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">I</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">card</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">∧</span> <span class="n">i</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="n">map</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="bp">.</span><span class="n">prod</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Jun 08 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772173):
<p>I think Kenny did product of ideals so you could just define them recursively</p>

#### [ Johannes Hölzl (Jun 08 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772572):
<p>Are Kenny's ideals a subtype parameterised by the ring? I guess they form a monoid? Then you could just write <code>I ^ n</code>?</p>

#### [ Johan Commelin (Jun 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772627):
<p>But <code>I</code> has type <code>set R</code>. And there is some instance hanging around telling you that it is an ideal. So now Lean wants <code>have_pow (set R) nat</code>.</p>

#### [ Johan Commelin (Jun 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772630):
<p>And that doesn't make sense.</p>

#### [ Johan Commelin (Jun 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127772637):
<p>But maybe I'm missing something.</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773371):
<p>It doesn't make sense to a mathematician -- that's what you're missing.</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773379):
<p>I think the idea in CS is that you just define I*J for I and J sets to be the ideal generated by the ij</p>

#### [ Mario Carneiro (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773380):
<p>why not?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773388):
<p>it's the same math/CS thing</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773391):
<p>it's just like dividing by zero</p>

#### [ Mario Carneiro (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773393):
<p>Is that even a CS thing?</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773396):
<p>yes</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773400):
<p>nobody divides by zero except CS people</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773404):
<p>oh</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773405):
<p>maybe applied mathematicians do</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773407):
<p>no not even them</p>

#### [ Mario Carneiro (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773408):
<p>where's the division by zero</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773409):
<p>they only do 0 / 0</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773413):
<p>the "division by zero" is when you multiply two sets that are not ideals together</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773414):
<p>when nobody in their right mind would do this</p>

#### [ Mario Carneiro (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773415):
<p>presumably this is exactly what is meant by I^n</p>

#### [ Kevin Buzzard (Jun 08 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773416):
<p>Exactly</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773470):
<p>The notion A*B for A,B sets is well defined even if they are not ideals</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773472):
<p>It's just a different way of thinking about things. I know exactly why Johan is confused.</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773485):
<p>Yes, well-defined and kind-of pointless</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773486):
<p>but if you want to restrict to ideals, it makes no difference</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773487):
<p>so we don't think of it</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773488):
<p>exactly</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773491):
<p>and then whenever you apply it, you are probably carrying around a proof that things are ideals</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773495):
<p>not at all pointless, the notation is not limited to ring theory</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773497):
<p>This is just another instance of this canonical disconnect</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773503):
<p>we only define things where we need them</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773513):
<p>you over-define and sift later</p>

#### [ Kevin Buzzard (Jun 08 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773516):
<p>it's just cultural</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773523):
<p>I'm certain I've seen A - B and A + B and other things as well with weirder sets than ideals</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773576):
<p>i.e. "prove C + C = [0, 2] where C is the cantor set"</p>

#### [ Johan Commelin (Jun 08 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773599):
<p>0/0 is also well-defined. It is 57.</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773615):
<p>but I'm not even stressing this domain of definition, define it on ideals if you want</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773623):
<p>you can still define I^n that way</p>

#### [ Johan Commelin (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773630):
<p>And <code>A * B</code> for <code>A B : set R</code> has two definitions that make sense. (1) <code>{ a*b | a \in A, b \in B}</code> or (2) <del><code>span { a*b | a \in A, b \in B}</code></del> sorry, I meant <code>span { a*b | a \in span A, b \in span B}</code></p>

#### [ Mario Carneiro (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773673):
<p>since I^(n+1) = I^n * I and I^0 = B and these are both ideals</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773680):
<p>in ring theory you obviously need the second definition</p>

#### [ Johan Commelin (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773685):
<p>I would say that (1) is more natural. But for ideals you want (2)</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773722):
<p>A question: using the set definition, is <code>span (I*I*I) = span (span (I*I) * I)</code>?</p>

#### [ Kenny Lau (Jun 08 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773729):
<p>yes</p>

#### [ Johan Commelin (Jun 08 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773771):
<p>Anyway, Kevin, here is <a href="https://github.com/jcommelin/lean-perfectoid-spaces/tree/subring" target="_blank" title="https://github.com/jcommelin/lean-perfectoid-spaces/tree/subring">https://github.com/jcommelin/lean-perfectoid-spaces/tree/subring</a> with <code>is_integrally_closed</code> up to some sorrys in mason-stother.</p>

#### [ Kenny Lau (Jun 08 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773788):
<p>A subset B is trivial, to see that B subset A, suffices to show that <code>span(I*I)*I subset I*I*I</code>, and then it follows from distributivity</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773808):
<p>Here's another CS-ism: instead of dealing with ideals, generalize to all sets by implicitly taking the span when you need to</p>

#### [ Johan Commelin (Jun 08 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773872):
<p>Ok, so we put a semiring structure on <code>set R</code>...</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773903):
<p>One problem with doing this generally is that <code>-A</code> is taken in sets</p>

#### [ Johan Commelin (Jun 08 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773973):
<p>Hmm, there is no semiring structure actually. Because <code>neg A</code> is <code>span (-A)</code>, and so <code>neg neg A \ne A</code>.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127773984):
<p>Unless <code>A</code> is an ideal... but that is a very crazy assumption. (-;</p>

#### [ Johan Commelin (Jun 08 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774029):
<p>I think the nice thing to do is to define a class <code>ideals R</code>, just as with <code>opens X</code>.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774043):
<p>And then put the nice structure on <code>ideals R</code>.</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774051):
<p>actually if you only want a semiring you don't need neg</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774056):
<p>I don't think you have to worry about any cancellation</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774067):
<p>but the distributive law fails I think</p>

#### [ Johan Commelin (Jun 08 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774069):
<p>Aah, you are right of course</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774147):
<p><code>{1, 2}*({1} + {1}) = {2, 4}</code>, <code>{1, 2}*{1} + {1,2}*{1} = {2,3,4}</code></p>

#### [ Johan Commelin (Jun 08 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774188):
<p>No, your counterexample fails. Both sides are <code>R</code>.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774235):
<p>And in fact, I think you get a semiring.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774259):
<p>The output of <code>+</code> and <code>*</code> is always an ideal.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774283):
<p><code>A + B</code> is defined as <code>span (span A +' span B)</code>, where <code>+'</code> is the stupid element-wise addition.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774288):
<p>Analogously for <code>*</code>.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774346):
<p>(I agree that my initial definition was wrong. But I had not learnt your CS-ism back then. So I didn't put in enough <code>span</code>s.)</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774416):
<p>I think <code>span (A +' B)</code> should suffice?</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774476):
<p>My observation is that elementwise addition is non-distributive (although it is associative and commutative if the underlying op is)</p>

#### [ Johan Commelin (Jun 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774499):
<p>Right, but you want that multiplication and addition of ideals is distributive.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774504):
<p>That is a fact that will someday be in mathlib, I hope.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774514):
<p>So we tweak our definition, and throw in some extra <code>span</code>s.</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774669):
<p>You don't need the extra spans though, the span in the upgraded addition is sufficient to fix the issues</p>

#### [ Mario Carneiro (Jun 08 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774696):
<p><code>span (A *' span (B +' C)) = span (span (A *' B) +' span (A *' C))</code></p>

#### [ Johan Commelin (Jun 08 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127774957):
<p>Take <code>A = R</code>, <code>B = {1}</code> and <code>C = {-1}</code>. Then LHS = 0 while RHS = R.</p>

#### [ Reid Barton (Jun 08 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127780905):
<p>The main point here is that you should be writing <code>(I : ideal R)</code>, not <code>(I : set R) (h : is_ideal I)</code> or whatever.</p>

#### [ Johan Commelin (Jun 08 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781504):
<p>So why do we still write <code>(R : Type) [ring R]</code>? Shouldn't we write <code>R : Ring</code> and <code>G : Group</code> or something like that?</p>

#### [ Johan Commelin (Jun 08 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781586):
<p>Or does the difference have to do with whether your class is a <code>Prop</code>?</p>

#### [ Johan Commelin (Jun 08 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781612):
<p>So all the <code>is_open</code>s, <code>is_ideal</code>s and <code>is_subring</code>s get gathered into classes <code>opens</code>, <code>ideals</code>, and <code>subrings</code>. But things like rings and groups shouldn't...</p>

#### [ Reid Barton (Jun 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781677):
<p>I think in many cases you should also be writing <code>R : Ring</code> etc. Particularly in settings where the only thing you know about <code>R</code> is that it is a ring.</p>

#### [ Reid Barton (Jun 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781694):
<p><code>R : Ring</code> might be less convenient when dealing with specific objects. For examples, the real numbers are a ring but they are also a topological space, etc.</p>

#### [ Johan Commelin (Jun 08 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781772):
<p>Right</p>

#### [ Johan Commelin (Jun 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781873):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I think Mario said something along the lines that type inference and coercions don't work together.</p>

#### [ Johan Commelin (Jun 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127781959):
<p>So, suppose you have the following statement <code>instance {R : Type} [ring R] (S: subrings R) : ring S</code>. If you then want to prove <code>instance {R : Type} [comm_ring R] (S: subrings R) : comm_ring S</code> I think you run in to trouble, because now Lean needs to turn <code>S</code> into a <code>Type</code> and also infer that it is a <code>ring</code>.</p>

#### [ Johan Commelin (Jun 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127782008):
<p>And I couldn't just easily prove stuff.</p>

#### [ Johan Commelin (Jun 08 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subrings/near/127782026):
<p>(I don't have Lean here atm... so I can't reproduce the exact problem I ran into.</p>


{% endraw %}
