---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/28918vectorspacesvsmodulesoverafield.html
---

## Stream: [maths](index.html)
### Topic: [vector spaces vs modules over a field](28918vectorspacesvsmodulesoverafield.html)

---


{% raw %}
#### [ Johan Commelin (Jun 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128233939):
<p>I have a module over a field. How do I upgrade it to a vector_space? We can't have a generic instance, because we would immediately get loops (every vector_space is already a module).</p>

#### [ Johan Commelin (Jun 18 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128233981):
<p>I really wish this would be transparent, because there is no content at all.</p>

#### [ Chris Hughes (Jun 18 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237488):
<p>Something like this?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">field</span> <span class="n">F</span><span class="o">]</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">m</span> <span class="o">:</span> <span class="n">module</span> <span class="n">F</span> <span class="n">M</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">Mvector_space</span> <span class="o">:</span> <span class="n">vector_space</span> <span class="n">F</span> <span class="n">M</span> <span class="o">:=</span> <span class="o">{</span><span class="bp">..</span><span class="n">m</span><span class="o">}</span>
</pre></div>

#### [ Gabriel Ebner (Jun 18 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237549):
<p>Maybe make vector_space a reducible definition for module?</p>

#### [ Johan Commelin (Jun 18 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237680):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> That is tricky right? Because then we get cycles in the type class system.</p>

#### [ Johan Commelin (Jun 18 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237682):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> How do I make a class reducible?</p>

#### [ Chris Hughes (Jun 18 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237786):
<p>I agree it does seem a little silly. I'm not sure we'd get cycles any more than we would by any other use of extends. This is a little weird because there aren't any extra axioms, but extends is used all the time without any problems.</p>

#### [ Chris Hughes (Jun 18 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237806):
<p>In fact just making what I just wrote a global instance is probably a good idea.</p>

#### [ Gabriel Ebner (Jun 18 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237812):
<p>Not class, just <code>@[reducible] def vector_space (α : Type u) (β : Type v) [field α] := module α β</code></p>

#### [ Johan Commelin (Jun 18 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237871):
<p>But then we can't use the type class instance anymore...</p>

#### [ Johan Commelin (Jun 18 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237896):
<p>Chris, Hmmm, I thought introducing cycles was a bad idea. I think we try to avoid them.</p>

#### [ Johan Commelin (Jun 18 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128237910):
<p><code>extends</code> does not introduce cycles. So I don't understand your point.</p>

#### [ Chris Hughes (Jun 18 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238026):
<p>The definition of <code>vector_space</code> just <code>extends</code> <code>module</code> with no extra axioms. So it won't introduce cycles.</p>

#### [ Chris Hughes (Jun 18 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238028):
<p>If <code>extends</code> doesn't introduce cycles.</p>

#### [ Gabriel Ebner (Jun 18 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238029):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> There is the cycle module -&gt; vector_space -&gt; module.</p>

#### [ Gabriel Ebner (Jun 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238033):
<p>(If you add the instance.)</p>

#### [ Chris Hughes (Jun 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238038):
<p>Oh I see.</p>

#### [ Gabriel Ebner (Jun 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238046):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I just tried replacing the vector_space class by a definition and everything seems to work.  Why do you think it would break type class instances?</p>

#### [ Johan Commelin (Jun 18 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238097):
<p>I mean, then I can't any longer write <code>{V : Type} [vector_space real V]</code> in my theorems. Right?</p>

#### [ Johan Commelin (Jun 18 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238103):
<p>Because the <code>[]</code> only work for classes.</p>

#### [ Chris Hughes (Jun 18 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238156):
<p>Maybe it will just interpret it as <code>module real V</code></p>

#### [ Johan Commelin (Jun 18 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238167):
<p>The reason that nothing breaks after your change, is because mathlib has not <em>really used</em> vector spaces yet. It only defines them...</p>

#### [ Johan Commelin (Jun 18 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238185):
<p>Chris, hmm, that might be true! Then it might work!</p>

#### [ Johan Commelin (Jun 18 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128238264):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Ok, I see that in fact on the line below there is already <code>[vector_space ...]</code> and it seems to work. You are right. Thanks!</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242421):
<p>IIRC I set this up before (<code>vector_space</code> as reducible def) and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> reverted it to the current wrapper class style, so there was probably a reason although I forget what it is.</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242443):
<p>I think the preferred solution is just to have instances of <code>vector_space</code> for all your vector spaces</p>

#### [ Johan Commelin (Jun 18 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242581):
<p>Ok, but aren't you scared that this creates cycles?</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242598):
<p>Chris's instance will create cycles. I'm not suggesting that</p>

#### [ Johan Commelin (Jun 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242640):
<p>Or, you mean, explicitly saying</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">foobar</span> <span class="o">:</span> <span class="n">vector_space</span> <span class="n">real</span> <span class="n">V</span> <span class="o">:=</span> <span class="o">{}</span>
</pre></div>

#### [ Johan Commelin (Jun 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242648):
<p>whenever <code>V</code> is a module over the reals.</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242649):
<p>depends on what <code>V</code> is there</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242659):
<p>if <code>V</code> is an arbitrary module over the reals, then no</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242677):
<p>if you replace <code>V</code> with <code>my_R_vec</code> then yes</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242737):
<p>If you want to deal with an arbitrary real vector space, the assumption should say <code>vector_space</code> not <code>module</code></p>

#### [ Chris Hughes (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242744):
<p>What happens if you have something like a vector space instance for polynomials over a field, but also a module instance for polynomials over a ring. Then you have cycles.</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242750):
<p>no</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242752):
<p>that's perfectly okay</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242755):
<p>that's a diamond not a cycle</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242763):
<p>and the defeq constraint will be easy to satisfy here</p>

#### [ Johan Commelin (Jun 18 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128242909):
<p>Mario, I am defining Lie algebras. They are modules over a ring with extra data and properties. But if my ring happens to be a field, then I want to prove extra things about my Lie algebras (using things like <code>dimension</code> etc...). How should I explain to Lean that if I have <code>[field R]</code> I want to upgrade my <code>[lie_algebra L]</code> to a <code>[vector_space R L]</code> instead of just the <code>module R L</code> that it extends?</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128243070):
<p>you can have an instance for that</p>

#### [ Mario Carneiro (Jun 18 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128243075):
<p><code>instance [field R] [lie_algebra L] : vector_space R L</code></p>

#### [ Johan Commelin (Jun 18 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128243174):
<p>ok, I see</p>

#### [ Johan Commelin (Jun 18 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128243182):
<p>That's a good solution, I guess (-;</p>

#### [ Johannes Hölzl (Jun 18 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/vector%20spaces%20vs%20modules%20over%20a%20field/near/128263024):
<p>I don't remember why I changed it to a <code>class</code> maybe I had a problem in combination with the <code>inout</code> parameter. We can change it back and see what happens.</p>


{% endraw %}
