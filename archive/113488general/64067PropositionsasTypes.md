---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64067PropositionsasTypes.html
---

## Stream: [general](index.html)
### Topic: [Propositions as Types](64067PropositionsasTypes.html)

---


{% raw %}
#### [ Lyle Kopnicky (Apr 16 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125127870):
<p>I'm not clear why the definition of <code>p1</code> below is not a type error. What can it possibly mean for <code>p1</code> to be a proof of a proof of a proposition?</p>
<div class="codehilite"><pre><span></span>constant U : Type
constant u0 : U
constant u1 : u0 -- type error

constant p0 : Prop
constant p1 : p0 -- no type error!
constant p2 : p1 -- type error
</pre></div>


<p>I thought of <code>U</code> and <code>Prop</code> as being of the same "universe level", but apparently they're not.</p>

#### [ Simon Hudon (Apr 16 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125127979):
<p><span class="user-mention" data-user-id="113073">@Lyle Kopnicky</span> Before I answer, do you mind editing the topic to your post (and don't forget to select "Change later messages to this topic"). Maybe set it to "Propositions as Types"</p>

#### [ Simon Hudon (Apr 16 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128027):
<p>Let's have a look at what kind of beast <code>Prop</code> is. <code>Prop</code> is actually synonymous with <code>Sort 0</code>, that is, a sort in universe 0. <code>Sort 0</code> has type <code>Sort 1</code> and <code>Sort 1</code> has type <code>Sort 2</code>:</p>
<div class="codehilite"><pre><span></span>Prop : Sort 1
Sort 1 : Sort 2
Sort 2 : Sort 3
...
</pre></div>

#### [ Simon Hudon (Apr 16 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128076):
<p>For <code>e0 : e1</code> (a type judgement) to make sense, e1 must be a sort, i.e. there must be a universe <code>u</code> such that <code>e1 : Sort u</code>.</p>

#### [ Simon Hudon (Apr 16 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128126):
<p>Thanks!</p>
<p>We can see that <code>p1 : p0</code> satisfies this constraint because <code>p0 : Sort 0</code>. Similarly, <code>u0 : U</code> because there is a <code>u</code> (1), such that <code>U : Sort u</code>. Note that <code>Type u = Sort (u+1)</code></p>

#### [ Simon Hudon (Apr 16 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128133):
<p>We have the same problem for <code>u1 : u0</code> as for <code>p1 : p0</code></p>

#### [ Kenny Lau (Apr 16 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128230):
<blockquote>
<p>I'm not clear why the definition of <code>p1</code> below is not a type error. What can it possibly mean for <code>p1</code> to be a proof of a proof of a proposition?</p>
</blockquote>
<p>No, <code>p0</code> is the proposition and <code>p1</code> is the proof.</p>

#### [ Simon Hudon (Apr 16 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128238):
<p>If we omit universes for a moment, a type <code>t</code> is a term (or expression) such that <code>t : Sort</code> and that allows you to type expressions <code>e</code>: <code>e : t</code>.</p>
<p>That means that <code>Sort</code> must somehow be a type. This is where universes become important. If we still ignore them we have <code>Sort : Sort</code> but that invites paradoxes so we have to rank sorts: <code>Sort u : Sort (u+1)</code></p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128244):
<p>Ah, that makes sense, <span class="user-mention" data-user-id="110064">@Kenny Lau</span> , thanks.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128296):
<p>Thanks, <span class="user-mention" data-user-id="110026">@Simon Hudon</span> . If <code>Prop</code> is <code>Sort 0</code>,  what sort does <code>p0</code> have? Is it <code>Sort (-1)</code>?</p>

#### [ Kenny Lau (Apr 16 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128337):
<p><code>p0</code> is not a sort</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128345):
<p>Is <code>Type</code> a sort?</p>

#### [ Kenny Lau (Apr 16 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128383):
<p>Type = Sort 1</p>

#### [ Simon Hudon (Apr 16 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128384):
<p>I see why you would think that. <code>Sort u</code> is inhabited by sorts. They are not necessarily inhabited by sorts themselves.</p>
<blockquote>
<p>p0 is not a sort</p>
</blockquote>
<p>p0 is a sort but it is not equal to <code>Sort u</code> for any u.</p>

#### [ Kenny Lau (Apr 16 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128390):
<p>what <strong><em>sort</em></strong> of nonsense is this</p>

#### [ Simon Hudon (Apr 16 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128395):
<p>It is a sort, it can be on the right hand side of <code>:</code></p>

#### [ Simon Hudon (Apr 16 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128399):
<p>It is not a type of sorts though</p>

#### [ Kenny Lau (Apr 16 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128401):
<p>now I'm having jamais vu on sort</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128459):
<p>I guess I am thinking that everything has some "universe level", where <code>Sort 1</code> is level 1, <code>Sort 2</code> is level 2, etc.  Then if you can write <code>a : b</code>, <code>a</code> is one level lower than <code>b</code>. And you bottom out at some point, so that you can no longer write <code>a : b</code> if <code>b</code>'s level is too low.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128525):
<p>So, if <code>Type</code> is at level 1, <code>U</code> is at level 0 (though it's not synonymous with <code>Sort 0</code>), and <code>u0</code> is at level -1, and we can't write <code>u1 : u0</code> because <code>u0</code> has too low of a level. Does that make any sense?</p>

#### [ Simon Hudon (Apr 16 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128530):
<p>You could think of it that way, that's true. It's important to note that "too low a level" makes a term not a type. We normally reserve that universe terminology for types. There is a problem with thinking of level -1 though</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128574):
<p>I think of <code>u0</code> as the value level.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128578):
<p>Even though that can be confusing because types are values too.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128594):
<p>So, <code>Sort 0</code> is the lowest level of types, and just below that is the value level. Things that are not types.</p>

#### [ Simon Hudon (Apr 16 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128595):
<p>We can have some data <code>d</code> of type <code>t</code> with <code>t : Sort 3</code>. You would probably think of it as being in universe 2 but <code>d</code> is still not the type of any other terms.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128648):
<p>OK, yeah, I guess my analogy breaks down there.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128703):
<p>But what confuses me is, if <code>Prop : Sort 1</code>, then <code>Prop</code> would be at the same level as <code>U</code>... level 0. So you should be able to have <code>p0 : Prop</code>, but not <code>p1 : p0</code>.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128707):
<p>That would be going to "too low of a level".</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128719):
<p>So I guess my concept of "too low of a level" doesn't really work, either.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128736):
<p>So think of it this way: we're talking about a formal system focused on terms. Some terms <code>t</code> are types. Every term <code>t'</code> has a type such that <code>t' : t</code>. Every type has type <code>t : Sort u</code> for some universe <code>u</code></p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128828):
<p>Then in <code>p1 : p0</code>, <code>p0</code> must be a type. And <code>p0 : Prop</code>, but <code>Prop</code> is synonymous with <code>Sort 0</code>, so that works.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128841):
<p>Exactly</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128893):
<p>But is <code>Type</code> synonymous with some sort?</p>

#### [ Kenny Lau (Apr 16 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128895):
<p>sort 1</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128905):
<p>OK</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128945):
<p>And <code>Type 1 = Sort 2</code>, <code>Type 2 = Sort 3</code>, and so on?</p>

#### [ Simon Hudon (Apr 16 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128946):
<p>That's right</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125128997):
<p>So, <code>Prop</code> is just the universe below <code>Type</code>.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129003):
<p>Yep!</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129065):
<p>Coming from Haskell, where we have a value level, and a type level (which is like <code>Type</code>), and a kind level (which is like <code>Type 1</code>), and then... well, they've sort of unified the levels from <code>Type 1</code> up... I'm trying to figure out what the analogy is to <code>Prop</code> there.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129072):
<p>What does it mean to have another type level, <em>below</em> what I thought of as the lowest level?</p>

#### [ Simon Hudon (Apr 16 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129115):
<p>Haskell doesn't really have a type <code>Prop</code>. types in <code>Prop</code> are a bit like data type that are guaranteed to be erased at run time</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129131):
<p>Haskell erases all the types at runtime anyway. Well, except maybe if you use existential types.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129135):
<p>What I'm saying is that the values of a type in <code>Prop</code> are erased at run time, not just the type itself</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129175):
<p>Gotcha.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129179):
<p>Have you ever used the singleton library in Haskell?</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129183):
<p>No, but I've seen it demonstrated.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129251):
<p>Are you saying that the singletons are also values that are erased at runtime?</p>

#### [ Simon Hudon (Apr 16 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129267):
<p>Not quite no. So far as I know they haven't added erasure for those types. There's still an interesting comparison</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129270):
<p>I'll take a look at it sometime, thanks.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129361):
<p><code>singleton</code> hinges on the idea of having type level natural numbers (and other objects). If you have <code>n0</code> and <code>n1</code> are type level natural numbers, <code>n0 .&lt;= n1</code> is the type of a proof that shows that <code>n0 ≤ n1</code>. It is a data type and it is uninhabited (except for <code>undefined</code>) unless the value of <code>n0</code> is less or equal to that of <code>n1</code>. As types <code>n0</code> and <code>n1</code> have only one value (again, except for <code>undefined</code>): the number they represent.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129363):
<p><code>Prop</code>s are a bit like those <code>.&lt;=</code> types (I'm not sure of the exact syntax, sorry)</p>

#### [ Simon Hudon (Apr 16 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129369):
<p>Correction: the singleton operator is <code>%&lt;=</code>, not <code>.&lt;=</code></p>

#### [ Simon Hudon (Apr 16 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129370):
<p>Does it clarify things?</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129566):
<p>It seems analogous to Prop, yes. But I'm struggling to line it up with the universes.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129575):
<p>When you're getting started, you can mostly ignore universes. You can simply use <code>Type</code> and <code>Prop</code>. Higher universes become necessary when you bring in existential types.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129632):
<p>OK. I meant that I'm imagining what the universes are in Haskell, and trying to figure out which level these propositions defined with the singleton library live at.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129682):
<p>I think the analogy with Haskell's term, type and kind is somewhat wobbly.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129732):
<p>I was thinking that Haskell's "type" is like <code>Type</code>, and the lowest-level kind is like <code>Type 1</code>.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129746):
<p>Or... maybe <code>Type</code> is a kind, so instances of that are types.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129787):
<p>The need for universes in Lean comes from a requirement that the language be a consistent logic. Haskell doesn't have that requirement. I believe the requirement for Haskell to separate terms and types is historical. It started off with an ML style language and made a lot of changes over time including <code>RankNTypes</code> and higher kinded types.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129789):
<p>Right.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129797):
<p>If we forget about Haskell's existential types and GADTs, I think its types are <code>Type 0</code> and its kinds are <code>Type 1</code></p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129843):
<p>Yeah, makes sense. Except now they have unified <code>Type 1</code>, <code>Type 2</code>, and so forth...</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129894):
<p>So, these type-level naturals would have type <code>Type 1</code>?</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129941):
<p>Maybe this will all make more sense if I look at Idris. It should have similar power to Lean but be easier to compare to Haskell.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129987):
<p>So, translate concept from Lean to Idris, then from Idris to Haskell. Or vice versa.</p>

#### [ Simon Hudon (Apr 16 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129989):
<p>Let me give you an example where <code>Type 1</code> is needed in Lean.</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125129997):
<p>OK</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130000):
<p>Hi Lyle,<br>
There are three kinds of things in Haskell: terms, types, and kinds. The same trichotomy appears in Lean, but kinds have kinds too</p>

#### [ Simon Hudon (Apr 16 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130001):
<p><code>(Σ t : Type 0, list t) : Type 1</code>. This is basically an existential type. Because it "contains" a <code>Type 0</code>, it has to live in universe 1</p>

#### [ Simon Hudon (Apr 16 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130039):
<p>Mario to the rescue! Thanks!</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130043):
<p>Also kinds are types and types are terms so it forms a subset relation</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130049):
<p>A kind (or a sort) is a term of the form <code>Sort u</code> for some <code>u</code>. A type is a term whose type is a kind, and a term is anything which is well typed</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130051):
<p>Any term has a type which is a type, which means that if <code>e : t</code> then <code>t : Sort u</code> for some <code>u</code></p>

#### [ Mario Carneiro (Apr 16 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130098):
<p>Here <code>e</code> and <code>t</code> are both logically related to <code>u</code>, which you might call the level of the expression, but obviously their relation to <code>u</code> is slightly different. <code>t</code> is level 1 means that <code>t : Sort 1</code> while <code>e</code> has type in level 1 since <code>e : t : Sort 1</code></p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130101):
<p>Right, that was my understanding so far.</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130146):
<p>In Haskell, there are values, types, and kinds which correspond roughly to terms in types of level 1, types in level 1, and <code>Sort 1</code> with maybe some variations on it</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130153):
<p>The algebra of kinds in Haskell is not as rich as Lean's, they only have one universe</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130155):
<p>I think they call it <code>*</code></p>

#### [ Mario Carneiro (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130158):
<p>but it is closest to <code>Sort 1</code> aka <code>Type</code></p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130246):
<p>Yeah, they actually call it <code>Type</code> now, in newer versions</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130254):
<p>So, how do the type-level nats fit into this?</p>

#### [ Simon Hudon (Apr 16 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130255):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think it's closer to <code>Type*</code> because of existential types and GADTs</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130296):
<p>It's one universe, but it's system F so it is impredicative</p>

#### [ Mario Carneiro (Apr 16 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130297):
<p>and somehow contradiction is avoided by a hair</p>

#### [ Simon Hudon (Apr 16 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130342):
<p>I thought because of <code>undefined</code> you couldn't consider the whole thing a consistent logic</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130355):
<p>That's true too, but System F itself is consistent if you leave out bottom</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125130402):
<p>there are lots of extensions that break consistency because Haskell wants to be turing complete</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131020):
<p><a href="http://downloads.haskell.org/~ghc/latest/docs/html/users_guide/glasgow_exts.html#kind-polymorphism-and-type-in-type" target="_blank" title="http://downloads.haskell.org/~ghc/latest/docs/html/users_guide/glasgow_exts.html#kind-polymorphism-and-type-in-type">http://downloads.haskell.org/~ghc/latest/docs/html/users_guide/glasgow_exts.html#kind-polymorphism-and-type-in-type</a></p>
<p>The <code>TypeInType</code> extension allows kinds to be as intricate as types, allowing explicit quantification over kind variables, higher-rank kinds, and the use of type synonyms and families in kinds, among other features.</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131031):
<p>I am not a haskell expert, but from what I can tell, type level nats are a way to have nats as types, so that you can quantify over them without breaking the value/type distinction (and thus get dependent types over nats)</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131168):
<p>In lean this is not necessary because it's fully dependent anyway. Haskell is getting closer and closer to dependent type theory as time goes on, but it's not there yet</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131214):
<p>Yeah, since in Haskell you can't write a function from values to types, but you can write a function from types to types, these type-level nats stand in for values, but can be used in functions that produce types.</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131264):
<p><code>array A : nat -&gt; Type</code> is an example of a dependent type family in lean</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131313):
<p>I see what you're saying about the one universe in Haskell. Traditionally in Haskell, you have kind <code>*</code>, which is Lean's <code>Sort 1</code>, and you have types whose type is <code>*</code>, and you have values of those types. With the <code>TypeInType</code> extension, the kinds can be treated like types that now have their own types, but it's all still one universe.</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131354):
<p>Oh right, there was something else I wanted to say about your earlier example: <code>U : Type</code> and <code>Prop : Type</code>, so these can be equated (<code>U = Prop</code> is well formed), but they are nevertheless treated differently, since if <code>u : U</code> then <code>e : u</code> is malformed but if <code>p : Prop</code> then <code>h : p</code> is okay.</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131362):
<p>You can't prove that a type "is" a universe, it must be so syntactically</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131404):
<p>Hmm, OK. Well that's because <code>Prop</code> is also a sort.</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131405):
<p>exactly</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131410):
<p>It is possible to consider type in type in dependent type theory, this would be a relatively small change to a lean-like language, but it is inconsistent by Girard's paradox so it is not usually used in languages that aspire to a sound proof theory</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131444):
<p>In fact, forgetting the universes is the first step in compiling lean programs</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131499):
<p>Right</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131502):
<p>In Haskell you can have kind <code>* -&gt; *</code>, e.g. <code>List : * -&gt; *</code>. So in Lean would <code>List</code> have type <code>Type -&gt; Type</code>? Then what's the type of <code>Type -&gt; Type</code>? Is that <code>Type 1</code>?</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131512):
<p>Indeed, <code>list</code> has type <code>list : Type u -&gt; Type u</code>, which itself has type <code>Type (u+1)</code></p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131514):
<p>Ah, I see</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131556):
<p>Well, that helps. I have a lot more to learn about Lean. I've been working through <em>Logic &amp; Proof</em>.</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131558):
<p>Most type families are universe polymorphic like this, but if we restrict to <code>Type</code>, we have <code>list.{0} : Type -&gt; Type : Type 1</code></p>

#### [ Mario Carneiro (Apr 16 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131567):
<p>Most things that you think of as kinds will have type <code>Type 1</code> if you replace <code>*</code> with lean's <code>Type</code> everywhere</p>

#### [ Lyle Kopnicky (Apr 16 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125131614):
<p>Thanks!</p>

#### [ Kevin Buzzard (Apr 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Propositions%20as%20Types/near/125138177):
<blockquote>
<p>In lean this is not necessary because it's fully dependent anyway. Haskell is getting closer and closer to dependent type theory as time goes on, but it's not there yet</p>
</blockquote>
<p>I watched a talk by Edward Kmett on youtube recently -- "typeclasses against the world" (about Haskell and typeclasses) and, if I understood correctly, Kmett said at some point that a problem with typeclasses in DTT was that you get diamonds, and in Haskell these couldn't occur.</p>


{% endraw %}
