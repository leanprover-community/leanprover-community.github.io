---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03072hidingwhenimport.html
---

## Stream: [general](index.html)
### Topic: [hiding when import?](03072hidingwhenimport.html)

---


{% raw %}
#### [ Zesen Qian (Jun 27 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737287):
<p>Hi, is there some way to hiding a name when importing a module?</p>

#### [ Simon Hudon (Jun 27 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737350):
<p>You can do that on a namespace scale: <code>open my_namespace hiding (clashing_def)</code></p>

#### [ Simon Hudon (Jun 27 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737357):
<p>You can also do selective opening of namespaces</p>

#### [ Zesen Qian (Jun 27 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737377):
<p>thank you, I'm still new to the name space space. But what if a name is at the top level of a module?</p>

#### [ Zesen Qian (Jun 27 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737390):
<p>or module itself is a namespace?</p>

#### [ Simon Hudon (Jun 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737479):
<p>The top most namespace is called <code>_root_</code>. Anything in that namespace can be hard to deal with. I'm not sure what the best approach is for dealing with name clashes in the root namespace. The best advice I have is: avoid</p>

#### [ Simon Hudon (Jun 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737536):
<p>A module itself is not a namespace. It would be interesting if it was though. Maybe we can request that feature</p>

#### [ Zesen Qian (Jun 27 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737637):
<p>OK, maybe I'm wrong, but it seems that parser in  data.buffer.parser is at top level.</p>

#### [ Zesen Qian (Jun 27 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737654):
<p>I guess that means this name will be there for all modules recursively importing it,</p>

#### [ Zesen Qian (Jun 27 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737665):
<p>and there is no way to hide it?</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737681):
<p>hide in what sense?</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737689):
<p>do you want to name something else <code>parser</code> at the top level?</p>

#### [ Zesen Qian (Jun 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737736):
<p>A import B, B has a top level name which clashes with a name A wants to use.</p>

#### [ Zesen Qian (Jun 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737750):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> exactly.</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737759):
<p>that's bad, avoid it</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737772):
<p><code>hide</code> does not change actual names, this will cause a name conflict</p>

#### [ Zesen Qian (Jun 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737795):
<p>maybe we should ask the author of standard library to avoid it first.</p>

#### [ Zesen Qian (Jun 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737797):
<p>then we can ask the users to avoid it too.</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737804):
<p>sadly the core lib is frozen</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737829):
<p>so you will have to work around it</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737888):
<p>but it's a global coordination problem, it's not a problem until someone else wants the name</p>

#### [ Simon Hudon (Jun 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737890):
<p>If you define your own <code>parser</code> in your local namespace, doesn't that make it the default definition that will be used as <code>parser</code>?</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737901):
<p>yes, that will work fine</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737918):
<p>but it means you can never define <code>_root_.parser</code></p>

#### [ Mario Carneiro (Jun 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737922):
<p>since it's been defined already</p>

#### [ Simon Hudon (Jun 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737931):
<p>Right</p>

#### [ Zesen Qian (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737985):
<p>to solve it once and for all, we need qualified import, like in haskell.</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737988):
<p>The moral of the story is that you should define most of your stuff in your own namespace</p>

#### [ Zesen Qian (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737989):
<p>so you can rename a namespace/module</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737998):
<p>that way core or mathlib can't get in your way</p>

#### [ Zesen Qian (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128737999):
<p>well again, I don't see the std lib doing it,  so I don't feel obligated to do it either.</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738004):
<p>you aren't stdlib</p>

#### [ Zesen Qian (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738009):
<p>why his parser is more fundenmental than mine?</p>

#### [ Simon Hudon (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738014):
<p>I think if we could have a qualification to a module like <code>import data.buffer.parser within buffer</code> as a way of putting all the definitions directly in the <code>parser</code> module in a new <code>buffer</code> namespace, that might help manage this situation</p>

#### [ Mario Carneiro (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738031):
<p>To be fair, I agree that that parser definition should be in the <code>buffer</code> namespace, but in general corelib will take lots of top level names</p>

#### [ Reid Barton (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738032):
<p>Unlike in Haskell, though, modules and namespaces are orthogonal in Lean. A module might define names in many namespaces and many modules might define names in the same namespace. So renaming a module doesn't make a lot of sense, in general.</p>

#### [ Zesen Qian (Jun 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738034):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> that's the "qualified import" I was talking about.</p>

#### [ Simon Hudon (Jun 27 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738102):
<p>That would be a bit different from Haskell though. In Haskell, <code>qualified</code> is a form of renaming</p>

#### [ Zesen Qian (Jun 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738107):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> how about this: import A as B. then the top-level def. foo in A becomes B.foo, ns.foo becomes B.ns.foo.</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738137):
<p>and then you define a top level def?</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738150):
<p>because then what happens to files C importing A?</p>

#### [ Zesen Qian (Jun 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738152):
<p>yes, I'm the king.</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738204):
<p>Or worse, a file C that imports A and B?</p>

#### [ Zesen Qian (Jun 27 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738238):
<p>it might conflict with the current semantics of import in lean.</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738244):
<p>it sure does</p>

#### [ Zesen Qian (Jun 27 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738261):
<p>but since lean always break old stuffs, I see that as a good thing.</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738271):
<p>I mean, what's your solution?</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738319):
<p>if A has foo, B imports A as A and also defines foo, and C imports A and B, what happens?</p>

#### [ Reid Barton (Jun 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738321):
<p>there's also the type-directed <code>.</code> notation to worry about</p>

#### [ Simon Hudon (Jun 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738386):
<p>I think like in Haskell, the qualification must only be local</p>

#### [ Zesen Qian (Jun 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738389):
<p>a practical solution would need thorough consideration of all factors, esp. the ability of .olean format.</p>

#### [ Zesen Qian (Jun 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738439):
<p>but I would naively believe there must be a better way.</p>

#### [ Reid Barton (Jun 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738534):
<p>A bigger annoyance IMO is that after you have given up and put your own <code>parser</code> name inside your own namespace, Lean will still consider <code>_root_.parser</code> to be a possible overload for <code>parser</code> (as far as I know?)</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738576):
<p>Not inside your namespace</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738629):
<p>and if it gives you trouble you can always make <code>parser</code> a local notation</p>

#### [ Mario Carneiro (Jun 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738639):
<p>that will clobber any overloads</p>

#### [ Reid Barton (Jun 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738643):
<p>hmm I feel like I've had trouble with this before... but can't recall the details. Maybe inside tactic mode?</p>

#### [ Reid Barton (Jun 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hiding%20when%20import%3F/near/128738650):
<p>And yeah, I used local notation to work around it</p>


{% endraw %}
