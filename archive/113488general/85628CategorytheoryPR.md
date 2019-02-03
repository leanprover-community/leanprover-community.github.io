---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85628CategorytheoryPR.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Category theory PR](https://leanprover-community.github.io/archive/113488general/85628CategorytheoryPR.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 07 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131024775):
<p>Hi <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, I didn’t understand your suggestion to use “<code>functor.id</code> (protected)”. What is “protected”?</p>

#### [ Scott Morrison (Aug 07 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131025217):
<p>Worked it out.</p>

#### [ Mario Carneiro (Aug 07 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026124):
<p>Hm, I see that you renamed the identity functor to <code>category.identity</code> and the identity natural transformation to <code>functor.identity</code>. I assume you did that so that you can use projection notation, but I think it's more confusing than is worth it. What do the mathematicians here think?</p>

#### [ Scott Morrison (Aug 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026681):
<p>Oh, I'm not at all attached to projection notation here: I'd guessed that was what you'd tell me to do!</p>

#### [ Scott Morrison (Aug 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026746):
<p>As far as I'm concerned I would be happy with any of:<br>
<code>C.identity</code>, <code>Functor.id C</code>, <code>Functor.identity C</code>, or <code>1 : C ↝ C</code>.</p>

#### [ Scott Morrison (Aug 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026756):
<p>(I know how to arrange for any of those, just want to know what is preferred.)</p>

#### [ Johan Commelin (Aug 07 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026820):
<p>My order of preference would be 4,1,3,2</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026879):
<p>Johan, Would you prefer to see <code>1 X</code> or <code>functor.id C X</code> in a goal printout talking about the identity functor applied to an object <code>X</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026883):
<p>(this isn't a rhetorical question)</p>

#### [ Scott Morrison (Aug 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026887):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, I'm confused why we would want to put <code>protected</code> on the definition of the identity functor. What is the motivation there? It seems if we're going to hide that, we should also hide the lemmas about it.</p>

#### [ Scott Morrison (Aug 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026890):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, seeing that comparison, I really dislike <code>1 X</code>!</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026923):
<p>because <code>id</code> is already a global definition, and we don't want to interfere with that</p>

#### [ Scott Morrison (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026931):
<p>How about <code>functor.identity C</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026932):
<p>plus there are like 5 different <code>id</code>s going around and I'd like to know which is which</p>

#### [ Scott Morrison (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026933):
<p>No need to collide with the global <code>id</code></p>

#### [ Scott Morrison (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026935):
<p>or the <code>category.id</code></p>

#### [ Scott Morrison (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026936):
<p>... :-)</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026949):
<p>the name collision is deliberate though, it's a consistent naming scheme</p>

#### [ Scott Morrison (Aug 07 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026955):
<p>In fact, I now really dislike the <code>has_one</code> instances for both <code>C ↝ C</code> and <code>F ↝ F</code>, and want to remove both.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026995):
<p>I'm surprised this bothers you given that we already have <code>𝟙 X</code></p>

#### [ Scott Morrison (Aug 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027003):
<p>Okay... so <code>functor.id C</code>, <code>nat_trans.id F</code>, and the only use of the symbol 1 will be <code>𝟙 X</code>.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027012):
<p>I'm okay with that</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027021):
<p>the protection is not needed for the theorems since they usually have more specific names that don't collide with core</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027067):
<p>they are still namespaced in <code>functor</code> though so you will need to use the prefix unless you have opened it</p>

#### [ Johan Commelin (Aug 07 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027091):
<blockquote>
<p>Johan, Would you prefer to see <code>1 X</code> or <code>functor.id C X</code> in a goal printout talking about the identity functor applied to an object <code>X</code>?</p>
</blockquote>
<p>I think I would prefer something like that <code>id_ C</code> or <code>1_ C</code>.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027096):
<p>How about using local notations for that?</p>

#### [ Johan Commelin (Aug 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027100):
<p>That might work.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027141):
<p>You probably don't need the <code>C</code> most of the time either</p>

#### [ Johan Commelin (Aug 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027144):
<p>Yes, but it might help to remind you of which cat you're working with.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027148):
<p>Well if it shows up as <code>1_ X</code> then it's inferrable from context</p>

#### [ Johan Commelin (Aug 07 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027156):
<p>I might think that is the identity morphism of X</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027160):
<p>that's the <em>completely different</em> <code>𝟙 X</code> :P</p>

#### [ Scott Morrison (Aug 07 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027162):
<p>Yeah, I think we want to make expressions that look even vaguely like <code>1 X</code> unambiguous</p>

#### [ Scott Morrison (Aug 07 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027207):
<p>and my preference is that the only similar looking expressions are <code>𝟙 X</code>, the identity morphism on <code>X</code>.</p>

#### [ Scott Morrison (Aug 07 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027211):
<p>If only there was a triple struck 1</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027212):
<p>I keep being reminded of <code>equiv.refl</code> as the only notation for the identity equiv</p>

#### [ Johan Commelin (Aug 07 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027220):
<p>Hmm, I prefer <code>𝟙 C</code></p>

#### [ Johan Commelin (Aug 07 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027229):
<p>If we have <code>𝟙 X</code> already.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027232):
<p>I think that will be a thing too</p>

#### [ Johan Commelin (Aug 07 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027233):
<p>After all, it is the identity morphism on <code>C</code> in <code>Cat</code>.</p>

#### [ Johan Commelin (Aug 07 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027238):
<p>Aah, and they will be defeq, but we can't have only one definition?</p>

#### [ Scott Morrison (Aug 07 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027284):
<p>Yeah... that's a bit of a sore point. <code>Cat</code> is of course a 2-category, and thinking of it as a 1-category by just ignoring the top level invites trouble.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027304):
<p>so that means <code>𝟙 C</code> is not (or will be) defeq to <code>functor.id C</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027310):
<p>or does <code>𝟙 C</code> just not typecheck?</p>

#### [ Scott Morrison (Aug 07 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027356):
<p>At present it just doesn't typecheck</p>

#### [ Scott Morrison (Aug 07 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027360):
<p>Let me investigate this point for a few minutes.</p>

#### [ Scott Morrison (Aug 07 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028385):
<p>Arranging for <code>𝟙 C</code> to typecheck may not be impossible, but it will take quite a bit of work which hasn't otherwise been necessary, so I'd like to kick that back to some TODO list. :-)</p>

#### [ Johan Commelin (Aug 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028392):
<p>Sure, I'm completely fine with that (-;</p>

#### [ Scott Morrison (Aug 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028441):
<p>For now you just write <code>functor.id C</code> when you want the identity functor.</p>

#### [ Johan Commelin (Aug 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028442):
<p>Sounds like we might want <code>has_id</code> notation.</p>

#### [ Johan Commelin (Aug 07 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028454):
<p>And then all sorts of things can be instances of <code>has_id</code>, and you can write a doublestroke 1 in front of them.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028460):
<p>and what would the type of <code>generic.id</code> be?</p>

#### [ Johan Commelin (Aug 07 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028465):
<p>What's that?</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028471):
<p>if you have a typeclass, you have to decide in advance what the type of the thing is</p>

#### [ Johan Commelin (Aug 07 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028511):
<p>You are talking with a "cargo cult Leaner"</p>

#### [ Johan Commelin (Aug 07 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028520):
<p>So, you mean the type of <code>has_id</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028530):
<p>well, <code>has_id</code> will be a class that contains an identity operation, and that identity operation will have some type</p>

#### [ Johan Commelin (Aug 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028534):
<p>Aah, I see.</p>

#### [ Johan Commelin (Aug 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028538):
<p>Yeah... depends...</p>

#### [ Johan Commelin (Aug 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028546):
<p>And it depends a bit too much to be a dependent type.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028593):
<p>I suspect this will be a sticking point in any such plans</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028605):
<p>category theory just has too much overloading here to make sense of it</p>

#### [ Mario Carneiro (Aug 07 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131036160):
<p>Congratulations to Scott for his perseverance in improving this PR for mathlib and even going back to change his library, which could not have been an easy task.</p>

#### [ Scott Morrison (Aug 07 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131037342):
<p>Phew... I think I've rewritten everything about 4 times now. It does keep getting less bad as a result, whatever that signifies. :-)</p>

#### [ Mario Carneiro (Aug 07 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131037460):
<p>now that we've got the basic definitions, how about the less basic ones? :D</p>

#### [ Scott Morrison (Aug 07 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131037525):
<p>Don't worry, there's a <code>category_theory_2</code> branch ready to turn into a PR. :-)</p>

#### [ Scott Morrison (Aug 07 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131037530):
<p>I'm just having to google how rebasing works!</p>

#### [ Scott Morrison (Aug 07 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131038016):
<p>okay... rebasing is still confusing me, but there's a second PR now!</p>

#### [ Johan Commelin (Aug 07 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131038508):
<p>Cool! Awesome! Congratulations!</p>

#### [ Kevin Buzzard (Aug 07 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131040791):
<p>Oh the first PR has been merged! Fabulous!</p>

#### [ Scott Morrison (Aug 08 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131100523):
<p>Hi <span class="user-mention" data-user-id="110032">@Reid Barton</span> sometime soon we should  do some coordination to combine the category theory development you've been doing in your homotopy theory repo with mine.</p>

#### [ Patrick Massot (Aug 08 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131100538):
<p>This should definitely be one of our small groups in Orsay (although you can start online of course).</p>


{% endraw %}
