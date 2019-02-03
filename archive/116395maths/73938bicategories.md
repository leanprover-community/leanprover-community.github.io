---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/73938bicategories.html
---

## Stream: [maths](index.html)
### Topic: [bicategories](73938bicategories.html)

---


{% raw %}
#### [ Reid Barton (Oct 10 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502092):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> have you by any chance done or thought about formalizing bicategories?</p>

#### [ Reid Barton (Oct 10 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502151):
<p>I know you have monoidal categories somewhere which is in approximately the same direction</p>

#### [ Scott Morrison (Oct 10 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502652):
<p>Yes, I'd like to, but have done nothing.</p>

#### [ Scott Morrison (Oct 10 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502667):
<p>I've been meaning to rewrite the work on monoidal categories for a while now, as it's an excellent playground for my student Keeley Hoek's "rewrite_search" algorithms.</p>

#### [ Scott Morrison (Oct 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502740):
<p>I think the lesson I eventually learnt there is that defining a monoidal category as a category <code>C</code> equipped with a functor <code>C x C to C</code> is actually a bad idea, mostly for syntactic reasons! I think it will work much better if you have have operations tensor_obj and tensor_hom, and laws for them, etc, then have a theorem that packages these as a functor when needed.</p>

#### [ Scott Morrison (Oct 10 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502772):
<p>The basic problem is just that if you think of tensor as a functor out of C x C, then its argument is a pair, and you'd really really prefer the curried version of these for parsing, pattern matching, etc. Dealing with the pairs causes lots of pain.</p>

#### [ Reid Barton (Oct 10 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502818):
<p>Hmm, makes sense...</p>

#### [ Scott Morrison (Oct 10 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502824):
<p>It is a bit sad though that this is a significant consideration.</p>

#### [ Reid Barton (Oct 10 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502843):
<p><a href="https://ncatlab.org/nlab/show/bicategory#detailedDefn" target="_blank" title="https://ncatlab.org/nlab/show/bicategory#detailedDefn">https://ncatlab.org/nlab/show/bicategory#detailedDefn</a></p>

#### [ Scott Morrison (Oct 10 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502904):
<blockquote>
<p>The point is not that one would want to write out the definition in such elementary terms (although apparently I just did anyway) but rather that one can.</p>
</blockquote>

#### [ Scott Morrison (Oct 10 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502923):
<p>In a different direction, I would love to do (have someone do?) quasi-strict categories (according to Vicary), as a foundation for hooking up Lean and Globular.</p>

#### [ Reid Barton (Oct 10 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135503213):
<p>Right, I think we talked about this briefly in Orsay</p>

#### [ Reid Barton (Oct 10 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135507318):
<p>I suppose a possible alternative to <code>C x C -&gt; C</code> is a curried functor <code>C =&gt; (C =&gt; C)</code>, though I don't have a clear sense of the issues here yet</p>

#### [ Scott Morrison (Oct 10 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135508059):
<p>I suspect, although haven't actually checked, that this is just as bad. Because <code>F X</code> is handled via a coercion, rather than merely notation, I suspect we could never get <code>T X Y</code> to work for a curried functor.</p>

#### [ Mario Carneiro (Oct 10 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135510023):
<p>I think the curried functor should work fine</p>

#### [ David Michael Roberts (Oct 10 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135520001):
<p>Why not use the dependently-typed definition of bicategory a la an enriched category?</p>

#### [ David Michael Roberts (Oct 10 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135520083):
<p>As in, something like <code>obj1:Obj obj2:Obj |- Hom_obj1_obj2 : Cat</code> and then apply whatever solution makes the monoidal case work, modulo adapting to multiple objects?</p>

#### [ Reid Barton (Oct 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135530891):
<p>I think the issue is that we don't have a nice solution for monoidal categories, that doesn't require a structure with ~30 fields</p>


{% endraw %}
