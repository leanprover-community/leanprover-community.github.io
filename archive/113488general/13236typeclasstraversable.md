---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13236typeclasstraversable.html
---

## Stream: [general](index.html)
### Topic: [type class traversable](13236typeclasstraversable.html)

---


{% raw %}
#### [ Simon Hudon (Mar 08 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123421044):
<p>I have written a type class <code>traversable</code> similar to that of Haskell. Universe polymorphism has made the task challenging but I think I have reached a reasonable compromise. I'd love to hear what the community thinks of it: </p>
<p><a href="https://github.com/cipher1024/mathlib/commit/2f4aa9ed9c0e83d26ea3ae876b801851db6fb8ec" target="_blank" title="https://github.com/cipher1024/mathlib/commit/2f4aa9ed9c0e83d26ea3ae876b801851db6fb8ec">https://github.com/cipher1024/mathlib/commit/2f4aa9ed9c0e83d26ea3ae876b801851db6fb8ec</a></p>

#### [ Simon Hudon (Mar 08 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123421354):
<p>To the non-haskellers: <code>traversable</code> is a way of generalizing Lean's <code>mmap : (α → m β) → list α → m (list β)</code> so that it works with more collections than just <code>list</code>.</p>

#### [ Andrew Ashworth (Mar 08 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426715):
<p>heh, i haven't used mmap either, unfortunately</p>

#### [ Andrew Ashworth (Mar 08 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426731):
<p>is this similar to <code>Iterable</code> or <code>Sequence</code> in other languages?</p>

#### [ Simon Hudon (Mar 08 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426744):
<p>It is similar. The big difference is that is has a nice specification</p>

#### [ Simon Hudon (Mar 08 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426797):
<p>If you compare to <code>map</code>, <code>map</code> allows you to replace any element of a list but does not allow you to perform any effect (updating state, performing, I/O, raising exceptions, etc) in the process. Having a monad <code>m</code> (actually, we only need <code>m</code> to be an applicative) allows you to perform arbitrary effects in the process of replacing the elements of the collection.</p>

#### [ Andrew Ashworth (Mar 08 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426843):
<p>so for example, how might I traverse the rb-tree implementation in lean core?</p>

#### [ Andrew Ashworth (Mar 08 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426847):
<p>is it easy to adapt an arbitrary data structure to fit the interface?</p>

#### [ Simon Hudon (Mar 08 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426854):
<p>If you have <code>ask_age : string -&gt; io nat</code> which prompts the user for their age using stdin and stdout, <code>mmap ask_age user_list</code> creates the list of the age of all users</p>

#### [ Simon Hudon (Mar 08 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123426998):
<blockquote>
<p>is it easy to adapt an arbitrary data structure to fit the interface?</p>
</blockquote>
<p>It would be tricky for <code>rbtree</code> because we have an assumption, the ordering, on the type parameter. <code>functor</code>, <code>foldable</code>, <code>traversable</code>, <code>applicative</code> and <code>monad</code> requires that any type can be substituted for the type variable. But if you have <code>rbmap</code>, you can traverse the value and you can extend the interface to <code>indexed_traversable</code> so that when you traverse the value, you can read the key as well.</p>

#### [ Andrew Ashworth (Mar 08 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427054):
<p>interesting, i wish i could provide feedback, but I think I'd need to sit down with haskell for awhile first and learn how these all work</p>

#### [ Andrew Ashworth (Mar 08 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427109):
<p>but i can see how useful it would be to have a uniform interface for any data-structure, and traverse it in some deterministic order</p>

#### [ Simon Hudon (Mar 08 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427167):
<p>I find it very useful in Haskell and easier to reason about than the iterable patterns that I have encountered. I'm hoping having access to traversable laws will make them awesomer</p>

#### [ Mario Carneiro (Mar 08 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427268):
<p>What is the difference between a traversable and something that coerces to a list?</p>

#### [ Mario Carneiro (Mar 08 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427279):
<p>I'm not so sure about how you dealt with the universe stuff</p>

#### [ Simon Hudon (Mar 08 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427328):
<p>If you're looking at <code>my_collection</code>, <code>traverse : (α → m β) → my_collection α → m (my_collection β)</code>. You're getting a <code>my_collection</code> back afterwards. Coercible to <code>list</code> would be the weaker <code>foldable</code>.</p>

#### [ Simon Hudon (Mar 08 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427392):
<p>And it is still better than coercible from list because structures like vectors, matrices and even pairs cannot be made from arbitrary lists</p>

#### [ Mario Carneiro (Mar 08 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427567):
<p>Although it is a little limiting, I think you should make all the universes the same in <code>traversable</code>, similar to how <code>monad</code> works</p>

#### [ Simon Hudon (Mar 08 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427725):
<p>I have considered that. With monad, we have <code>Type u -&gt; Type v</code> (two universes) which constrains the type variable to be of type <code>Type u</code> and not to change. If I take a similar approach, the collection has to be of type <code>Type u -&gt; Type u</code> (only one universe) and also limits the type of applicative used. I thought of separating  <code>has_traverse</code> and <code>traversable</code> to limit the polymorphism in <code>traversable</code> but not in <code>has_traverse</code></p>

#### [ Simon Hudon (Mar 08 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123427734):
<p>Another option is to limit the polymorphism in both but provide type classes like <code>can_traverse my_appl my_collection</code> to provide more flexible traversals and laws</p>

#### [ Mario Carneiro (Mar 08 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123428079):
<p>Right, I think the monad/applicative also has to be <code>Type u -&gt; Type u</code> for the statement of <code>has_traverse</code> to make sense. The way this has been done in things like <code>list.bind</code> is to have the definition itself be fully polymorphic, but the definition that gets used in the instance is universe monomorphic. So the polymorphic functions are still available, you just don't get the typeclass niceties in this case</p>

#### [ Mario Carneiro (Mar 08 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123428085):
<p>Luckily, almost all programming stuff fits in <code>Type 0</code></p>

#### [ Mario Carneiro (Mar 08 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123428126):
<p>except existential types, but these have their own issues</p>

#### [ Simon Hudon (Mar 08 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123428246):
<p>That makes sense. Thinking back, the reason I was obstinate about making <code>traversable</code> as polymorphic as possible is that I was trying to mimic the <code>bound</code> Haskell library which encodes de Bruijn indices in type parameters. That gave me something of type <code>Type 0 -&gt; Type 1</code> but luckily, on the google group, someone proposed a nicer encoding. I think I will survive making <code>traversable</code> universe monomorphic</p>

#### [ Simon Hudon (Mar 08 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123458480):
<p><span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> Would this be more at home in the core library?</p>

#### [ Sebastian Ullrich (Mar 08 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123464546):
<p><span class="user-mention" data-user-email="simon.hudon@gmail.com" data-user-id="110026">@Simon Hudon</span> Not sure. Almost all recent additions to core lib are things we actually need there, but I wouldn't mind having access to <code>sequence</code>.</p>

#### [ Simon Hudon (Mar 08 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123464625):
<p>My thinking was that <code>traversable</code> is such an organizing principle in the Haskell base library that supporting right from the start might generalize a good portion of the machinery there. There was a recent version of the base library (I think 4.9) that made that step and de facto reduced some of the redundancy</p>

#### [ Simon Hudon (Mar 08 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123464676):
<p>And <code>sequence</code> is a fun thing to have when you need <code>f</code> and <code>g</code> to commute in any <code>f (g a)</code> type.</p>

#### [ Scott Morrison (Mar 09 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20traversable/near/123468370):
<p>(deleted)</p>


{% endraw %}
