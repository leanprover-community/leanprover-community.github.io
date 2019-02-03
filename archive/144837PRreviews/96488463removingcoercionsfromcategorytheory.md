---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/96488463removingcoercionsfromcategorytheory.html
---

## Stream: [PR reviews](index.html)
### Topic: [#463 removing coercions from category_theory/](96488463removingcoercionsfromcategorytheory.html)

---


{% raw %}
#### [ Scott Morrison (Nov 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929906):
<p>For your consideration, <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>, <span class="user-mention" data-user-id="112680">@Johan Commelin</span>, <span class="user-mention" data-user-id="110032">@Reid Barton</span>, <span class="user-mention" data-user-id="128547">@Michael Jendrusch</span>.</p>
<p>I propose removing all the coercions. It only took about 20 minutes to take them out, and I think overall it already simplifies the mathlib code, and will simplify lots of other things going forward.</p>

#### [ Scott Morrison (Nov 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929916):
<p>The cost is having to write <code>F.obj X</code> instead of <code>F X</code>, and having to write <code>t.app X</code> instead of <code>t X</code>.</p>

#### [ Scott Morrison (Nov 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929959):
<p>The benefit is not having to work out why <code>F X</code> doesn't work some fraction of the time.</p>

#### [ Scott Morrison (Nov 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929965):
<p>and not having to jump through hoops with extra variations of structure fields, to introduce coercions.</p>

#### [ Scott Morrison (Nov 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929970):
<p>and ... various other things as discussed in recent threads.</p>

#### [ Scott Morrison (Nov 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929985):
<p><a href="https://github.com/leanprover/mathlib/pull/463/files" target="_blank" title="https://github.com/leanprover/mathlib/pull/463/files">https://github.com/leanprover/mathlib/pull/463/files</a></p>

#### [ Scott Morrison (Nov 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929990):
<p>Notice that overall it reduces the codebase: +247 −317</p>

#### [ Kevin Buzzard (Nov 07 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146930066):
<p>I don't really see this as a cost. It's sort-of how I think of functors anyway :-)</p>

#### [ Kenny Lau (Nov 07 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146930864):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> do you think this will also benefit modules?</p>

#### [ Johan Commelin (Nov 07 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931051):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I think this is totally fine. In the sheaf stuff I've already avoided coercions; it wasn't too painful.</p>

#### [ Mario Carneiro (Nov 07 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931064):
<p>you know, I'm not sure how to take the lines reduction when you are reformatting at the same time :P</p>

#### [ Mario Carneiro (Nov 07 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931112):
<p><a href="https://github.com/leanprover/mathlib/pull/463/files#diff-d821da3f10c3bc4b40e7718069576210R81" target="_blank" title="https://github.com/leanprover/mathlib/pull/463/files#diff-d821da3f10c3bc4b40e7718069576210R81">https://github.com/leanprover/mathlib/pull/463/files#diff-d821da3f10c3bc4b40e7718069576210R81</a></p>

#### [ Mario Carneiro (Nov 07 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931252):
<p>there are also almost no actual proofs involved. Is it all just definitions?</p>

#### [ Kevin Buzzard (Nov 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931583):
<p>This night be a silly question because I don't know the previous setup -- could you just have the coercion on objects and only explicitly have to write F.app for the morphisms?</p>

#### [ Kevin Buzzard (Nov 07 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931654):
<p>Oh I see, this is exactly what was causing problems</p>

#### [ Kevin Buzzard (Nov 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931665):
<p>I now realise t is not a functor but probably a natural transformation</p>

#### [ Scott Morrison (Nov 07 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146932793):
<blockquote>
<p>there are also almost no actual proofs involved. Is it all just definitions?</p>
</blockquote>
<p>Yeah, nothing in <code>category_theory/</code> so far counts as a "theorem" except perhaps yoneda.</p>

#### [ Kevin Buzzard (Nov 07 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146933605):
<p>I am reminded of <a href="https://mathoverflow.net/a/10899/1384" target="_blank" title="https://mathoverflow.net/a/10899/1384">https://mathoverflow.net/a/10899/1384</a></p>

#### [ Scott Morrison (Nov 07 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146933680):
<p>Hmm... Does sounds like Lang. :-)</p>

#### [ Scott Morrison (Nov 08 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147273670):
<p>Hi @Mario, I'd be interested to hear your thoughts on this. I'm hesitant to continue working on later parts of the category theory development, because in several spots my current issues are connected to coercions. If I know whether or not it's likely this will be merged, I can decide whether or not to continue fighting those issues. :-)</p>

#### [ Mario Carneiro (Nov 08 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147273876):
<p>I want to hear what <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> has to say. You've been fighting these demons more than me, so I'll go with it if you think it helps, but I think it is a stylistic loss</p>

#### [ Johan Commelin (Nov 08 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147276465):
<p>I would be happy with merging this. I think <span class="user-mention" data-user-id="110032">@Reid Barton</span> expressed a similar opinion.</p>

#### [ Johannes Hölzl (Nov 08 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285804):
<p>I agree that it is a stylisitic loss, but its not too bad. Also we get rid of a lot of boilerplate code.<br>
So I'm okay with removing the coercions</p>

#### [ Scott Morrison (Nov 08 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285900):
<p>Whee... :-) After <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span>, I will see if we can do better.</p>

#### [ Scott Morrison (Nov 08 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285913):
<p>Would it be better with a symbol in between, instead of just field notation?</p>

#### [ Johan Commelin (Nov 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285958):
<p>Naahh, I would find it less readable with a symbol</p>

#### [ Mario Carneiro (Nov 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285959):
<p>I'm a bit worried that you can't do the same thing with notations</p>

#### [ Mario Carneiro (Nov 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285967):
<p>in particular that example with monoidal functor application</p>

#### [ Scott Morrison (Nov 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285994):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, could you clarify that? I'm not sure what you mean yet.</p>

#### [ Mario Carneiro (Nov 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147286041):
<p>if <code>F</code> is a monoidal functor, then <code>F.app X</code> is magically parsed to <code>F.to_functor.app X</code></p>

#### [ Mario Carneiro (Nov 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147286048):
<p>You don't get the same magic if you write <code>F +&gt; X</code> or whatever</p>

#### [ Johannes Hölzl (Nov 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147286639):
<p>is it ready to be merged?</p>

#### [ Mario Carneiro (Nov 08 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147286899):
<p>go for launch</p>

#### [ Johannes Hölzl (Nov 08 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147287069):
<p>merged</p>


{% endraw %}
