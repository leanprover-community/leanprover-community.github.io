---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19500elaborator.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [elaborator](https://leanprover-community.github.io/archive/113488general/19500elaborator.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 01 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491100):
<p>Over the last few months I have been idly writing something called "from unicode to bytecode", which is some (still extremely incomplete) documentation as to how Lean turns a string of unicode characters (the input file) into bytecode. One reason it's incomplete currently is that I have no real idea what bytecode is. But when I started this project I had no idea what a scanner / parser / token / etc was either, so I'm definitely moving forwards.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491140):
<p>I am now trying to understand the elaborator better. Here is a very basic question.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491183):
<p>This works (by which I think I mean "Lean's kernel manages to fully parse and elaborate the string of characters and add a new term <code>easy</code> to the environment"):</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491186):
<p><code>theorem  easy {i : ℕ} {n : ℕ} : i &lt; n → i &lt; nat.succ n :=  λ H, lt.trans H $ nat.lt_succ_self n</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491187):
<p>If I replace the <code>n</code> with an underscore, it still works</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491188):
<p><code>theorem  easy {i : ℕ} {n : ℕ} : i &lt; n → i &lt; nat.succ n :=  λ H, lt.trans H $ nat.lt_succ_self _</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491196):
<p>Somehow Lean knows from the type of everything that it wants <code>nat.lt_succ_self _</code> to have type <code>n  &lt; nat.succ n</code> and hence it knows <code>_</code> should be <code>n</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491197):
<p>But this doesn't work:</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491238):
<p><code>theorem  easy {i : ℕ} {n : ℕ} : i &lt; n → i &lt; nat.succ n :=  λ H, lt.trans _ $ nat.lt_succ_self n</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491239):
<p>Here Lean knows from type theory that it wants <code>_</code> to be a proof of <code>i &lt; n</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491245):
<p>and even though <code>H : i &lt; n</code> is in the local context, it won't take it and insert it.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491246):
<p>We get an error which, if you don't understand magic, looks silly:</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491248):
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
i n : ℕ,
H : i &lt; n
⊢ i &lt; n
</pre></div>

#### [ Kevin Buzzard (Apr 01 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491289):
<p>"Well, you knew how to synthesize <code>n</code> when that was in the local context..."</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491296):
<p>I think that as a learner (as I still am, but I am thinking more about people who are like I was last October, i.e. complete beginners), you have to just trust some stuff to magic.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491297):
<p>You type "simp" and sometimes it works and sometimes it doesn't, but if it does, then you'll take it.</p>

#### [ Gabriel Ebner (Apr 01 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491338):
<p>Maybe your confusion comes from the fact that the two situations are in fact very different.  In the first one, Lean doesn't just guess and take a natural number from the local context.  The reason that the placeholder gets filled in is because <code>n</code> is <em>the only possible choice</em> if you want the theorem to type-check.</p>

#### [ Gabriel Ebner (Apr 01 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491339):
<p>In the second case, <em>any value</em> of type <code>i &lt; n</code> would work.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491340):
<p>I think that whilst initially this way of thinking -- "sometimes it just works by magic" -- is initially the only way to proceed.  But now I want to start understanding Lean properly and in particular I want to know exactly what I can expect the elaborator to do.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491345):
<p>Thanks Gabriel, I could see that the situations somehow felt different but you have very quickly got to the heart of the matter.</p>

#### [ Sebastian Ullrich (Apr 01 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491396):
<p>In other words, the first placeholder can be solved by unification while type checking the right-hand side. The second one cannot.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491445):
<p>I think that the <code>_</code> (when it is representing <code>n</code>) gets filled in initially as something like <code>?m_1</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491451):
<p>Oh it perhaps even initially gets filled in as <code>(?m_1 : nat)</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491492):
<p>and then we have to solve <code>nat.lt_succ_self (?m_1 : nat) : n &lt; nat.succ n</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491499):
<p>and we know the type of <code>nat.lt.succ_self</code> is <code>?m_1 &lt; nat.succ ?m_1</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491541):
<p>and those two types really now have to be _equal_. I realise now I am slightly unsure what it means for two types to be equal. For example if <code>?m_1</code> was equal to <code>m</code> and it was a theorem that <code>m = n</code>, would these two types be equal?</p>

#### [ Gabriel Ebner (Apr 01 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491542):
<p>Pretty much in this order.  You essentially start with <code>?m_1: ?m_2</code> and <code>?m_2: Sort ?u_3</code> for the underscore. Then the elaborator wants to construct the application <code>nat.lt_succ_self ?m_1</code>, so it needs to make sure that the type of <code>?m_1</code> is <code>nat</code>, and you get the unification constraint <code>?m_2 =?= nat</code>.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491547):
<p>I have seen Mario writing these <code>=?=</code>s</p>

#### [ Gabriel Ebner (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491548):
<blockquote>
<p>it was a theorem that m = n, would these two types be equal?</p>
</blockquote>
<p>No, only definitional equality is used in unification.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491549):
<p>And these types would be equal because of some theorem</p>

#### [ Gabriel Ebner (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491551):
<p><code>=?=</code> is just the notation for "should unify with"</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491552):
<p>I could probably answer these questions myself now</p>

#### [ Gabriel Ebner (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491587):
<p>unification = assign the ?m_1, ..., ?m_n in such a way that the two sides are definitionally equal</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491593):
<p>if I could get Lean to print out these <code>=?=</code> constraints myself.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491595):
<p>Is there some set_option I can turn on</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491596):
<p>so I can just watch it all happening?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491597):
<p>I remember when I discovered set_option pp.all true and very quickly developed a much better understanding of what a term was</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491605):
<p>and when I discovered various set_option things for simp and very quickly got a much better understanding of what simp di.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491606):
<p>did</p>

#### [ Gabriel Ebner (Apr 01 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491607):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">type_context</span><span class="bp">.</span><span class="n">is_def_eq</span> <span class="n">true</span>
</pre></div>

#### [ Kevin Buzzard (Apr 01 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491660):
<p>oh gosh</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491661):
<p>even when I fill in all the <code>_</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491662):
<p>I still get outputs</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491702):
<p>This must be because of <code>@</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491709):
<p><code>theorem  easy {i : ℕ} {n : ℕ} : i &lt; n → i &lt; nat.succ n :=  λ H, lt.trans H $ nat.lt_succ_self n</code></p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491712):
<p>The output also includes all the unification you get for type-checking, even if there are no underscores.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491713):
<p>produces two bursts of excitement:</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491714):
<div class="codehilite"><pre><span></span>[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= n ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ?m_1 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= nat.has_lt ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= nat.has_lt ... success  (approximate mode)
</pre></div>

#### [ Kevin Buzzard (Apr 01 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491755):
<p>and</p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491757):
<p>Yes, I'm not sure how much you can learn from the output.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491758):
<div class="codehilite"><pre><span></span>[type_context.is_def_eq] ?m_1 =?= i &lt; n ... success  (approximate mode)
[type_context.is_def_eq] i &lt; nat.succ n =?= ?m_3 &lt; ?m_4 ... success  (approximate mode)
[type_context.is_def_eq] partial_order.to_preorder ℕ =?= partial_order.to_preorder ℕ ... success  (approximate mode)
[type_context.is_def_eq] i &lt; n =?= ?m_3 &lt; ?m_4 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= ?m_4 &lt; ?m_5 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= H ... success  (approximate mode)
[type_context.is_def_eq] ?m_3 &lt; ?m_4 =?= ?m_5 &lt; nat.succ ?m_5 ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ℕ =?= ℕ ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= n ... success  (approximate mode)
[type_context.is_def_eq] n &lt; nat.succ n =?= ?m_3 &lt; ?m_4 ... success  (approximate mode)
[type_context.is_def_eq] ?m_1 =?= nat.lt_succ_self n ... success  (approximate mode)
[type_context.is_def_eq] i &lt; n → i &lt; nat.succ n =?= i &lt; n → i &lt; nat.succ n ... success  (approximate mode)
</pre></div>

#### [ Kevin Buzzard (Apr 01 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491760):
<p>In my current state I can probably learn quite a bit</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491810):
<p>I think the guilty party is <code>lt.trans</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491811):
<p>or, as it should really be known</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491813):
<p>[rips mask off in Scooby-doo like manner]</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491815):
<p><code>@lt_trans _ _ _ _ _</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491865):
<p>Hmm</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491866):
<div class="codehilite"><pre><span></span>definition  Npreorder : preorder ℕ :=  by apply_instance

theorem  easy&#39; {i : ℕ} {n : ℕ} : i &lt; n → i &lt; nat.succ n :=
λ H, @lt.trans ℕ Npreorder i n (nat.succ n) H $ nat.lt_succ_self n
</pre></div>

#### [ Kevin Buzzard (Apr 01 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491911):
<p>I still get a bunch of output from <code> set_option trace.type_context.is_def_eq true </code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491913):
<p>aargh it's the notation</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491958):
<p><code> [type_context.is_def_eq] ?m_1 =?= n ... success  (approximate mode)</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491959):
<p>Nice to see we're in "approximate mode"</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491960):
<p>Doesn't fill me with confidence</p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124491965):
<p>Checking the equality of two terms without metavariables is a special case of unification.  That's also why it's called <code>is_def_eq</code>.  So whenever the elaborator makes sure that a term type-checks, it will produce unification constraints.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492018):
<p>Am I "being the elaborator" at the minute? So far I am up to</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492020):
<div class="codehilite"><pre><span></span>definition  Npreorder : preorder ℕ :=  by apply_instance
definition  Nhas_lt : has_lt ℕ :=  by apply_instance

theorem  easy&#39; {i : ℕ} {n : ℕ} : @has_lt.lt ℕ Nhas_lt i n →  @has_lt.lt ℕ Nhas_lt i (nat.succ n) :=
λ H, @lt.trans ℕ Npreorder i n (nat.succ n) H $ nat.lt_succ_self n
</pre></div>

#### [ Kevin Buzzard (Apr 01 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492021):
<p>I am having real trouble elaborating this any more.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492068):
<p>In fact I would go so far to say that this term can't be elaborated any more.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492070):
<p>although of course things could be unfolded.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492081):
<p>What does the unfolding? Is that still the elaborator? Does the elaborator have to think about the actual definition of the term <code>@has_lt.lt</code> or does it just check its type?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492125):
<p>I am not sure I care at all about the definition of <code>@has_lt.lt nat Nhas_lt</code>, all I need to know is that N is a preorder.</p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492126):
<p>If you need to unify <code>has_lt.lt a b c d</code> and <code>nat.lt c d</code>, then yes, the elaborator will unfold <code>has_lt.lt</code>.</p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492128):
<p>In this case, I don't think we unfold <code>has_lt.lt</code> anywhere.  (At least we don't need to.)</p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492180):
<p>The <code>easy'</code> theorem is still missing the domain of the lambda, if you want to write down a "fully elaborated" term.</p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492235):
<p>BTW, I believe it's a mistake to think of elaboration as "filling things in" (even though that may be literal meaning of the word).  From a big picture point of view elaboration is the translation of pre-expressions (which are close to what you write down) to type-correct terms in the core type theory.  Personally I think of a pre-expression more like a recipe that tells the elaborator to do what you want.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492240):
<p>Oh! Yes, I forgot about the lambda.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492245):
<p>So am I changing a <code>pexpr</code> to an <code>expr</code>?</p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492248):
<p>No, you're changing one <code>pexpr</code> into another <code>pexpr</code>.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492254):
<p>dammit I want an expr</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492259):
<p>I read about them in the manual</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492267):
<p>I am concerned that I might have more than one <code>&lt;=</code> on my <code>nat</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492279):
<p><code>Npreorder</code> says that <code>nat</code> has the structure of a <code>preorder</code></p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492310):
<p>I guess as an exercise you could write down the proof of <code>easy</code> using the <code>expr</code> constructors:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="kn">theorem</span> <span class="n">easy</span> <span class="o">{</span><span class="n">i</span> <span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">-&gt;</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">do</span> <span class="n">exact</span> <span class="err">$</span> <span class="n">lam</span> <span class="c">/-</span><span class="cm"> fill in here -/</span>
</pre></div>

#### [ Kevin Buzzard (Apr 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492323):
<p>and the <code>&lt;</code> on it is I think called something like <code>Npreorder.lt</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492331):
<p>but the <code>&lt;</code> I want is called <code>has_lt.lt</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492373):
<p>Actually I don't even know what it's called</p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492379):
<p>Yes, they are many <code>lt</code>s on <code>nat</code> and they all mean the same in the end.  AFAICT you have <code>has_lt.lt</code> everywhere though, as you should.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492380):
<p>it's called <code>Nhas_lt</code> I guess</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492383):
<p>I am not so sure about the <code>lt</code> coming from the preorder</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492391):
<p>I used type class inference to define the preorder on <code>nat</code></p>

#### [ Gabriel Ebner (Apr 01 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492433):
<p>Ah, I understand now.  The question is about the relation between <code>Npreorder</code> and <code>Nhas_lt</code>: the terms <code>@preorder.to_has_lt nat Npreorder</code> and <code>Nhas_lt</code> are definitionally equal.  (And type-checking actually needs to verify this equality.)</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492439):
<p>The more I elaborate, the greater the output of <code> set_option trace.type_context.is_def_eq true</code> becomes!</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124492993):
<blockquote>
<p>I guess as an exercise you could write down the proof of <code>easy</code> using the <code>expr</code> constructors:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="kn">theorem</span> <span class="n">easy</span> <span class="o">{</span><span class="n">i</span> <span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">-&gt;</span> <span class="n">i</span> <span class="bp">&lt;</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">do</span> <span class="n">exact</span> <span class="err">$</span> <span class="n">lam</span> <span class="c">/-</span><span class="cm"> fill in here -/</span>
</pre></div>


</blockquote>
<p>Oh I like this comment. Thanks! I might start with something easier than <code>easy</code> but this looks like a fun game :-)</p>

#### [ Kevin Buzzard (Apr 01 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493033):
<p>I might well find it a challenge to prove <code>1 + 1 = 2</code> in this mode</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493239):
<p>woo I made Prop</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493240):
<p><code>meta  definition  prop : expr (ff) := expr.sort level.zero</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493279):
<p>That's the proof that <code>expr</code> is inhabited</p>

#### [ Sebastian Ullrich (Apr 01 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493342):
<p>Note that <code>expr ff = pexpr</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493495):
<p>I just noticed that expr was demanding a bool so I gave it one</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493541):
<p>Hmm, that's funny. <code>pexpr.lean</code> says <code> @[reducible]  meta  def  pexpr  := expr ff</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493545):
<p>but <code>#print pexpr</code> says that it's <code> id_rhs Type (expr ff) </code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493584):
<p>rofl and <code>id_rhs</code> is an abbreviation. <span class="user-mention" data-user-id="110064">@Kenny Lau</span> here's when you should use reducible, apparently, and abbreviations too.</p>

#### [ Kenny Lau (Apr 01 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124493591):
<p>so when exactly?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494493):
<p>Oh this is all much too hard. I don't know how to turn anything at all into an expr. How do I turn a nat into an expr? How do I turn a Prop into an expr? How do I turn a proof into an expr? How do I turn a Type into an expr? Oh -- are these questions too general?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494496):
<p>How do I turn a constructor into an expr? Is that a sensible question?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494501):
<p>How do I turn<code> nat.zero</code> into an expr?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494542):
<p>If <code>f : X -&gt; Y</code> and I have an expr <code>ex</code> representing the...name? <code>x : X</code> , how do I create an expr corresponding to <code>f x</code>?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494550):
<p>How do I turn <code>eq.refl</code> into an expr?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494589):
<p>This sort of exercise might be a really good bridge to the Programming In Lean book.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494590):
<p>All this expr stuff is introduced at the same time as everything else somehow</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494592):
<p>Perhaps one can abstract it away first</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494598):
<p>and think about making exprs from usual Lean terms rather than letting the elaborator do it</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494647):
<p>Does the elaborator take a list of tokens and return an expr?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494686):
<p>I am still at the stage where I don't know if I have the words right</p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494741):
<p>I feel like this could be a cute blog post, explaining how to get from a string of unicode characters to an expr, even a really stupid string like <code>theorem  X : unit = unit := eq.refl unit</code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124494748):
<p>I don't know how to turn this into an expr</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124498667):
<div class="codehilite"><pre><span></span>theorem  very_easy : unit = unit :=
by  do to_expr ```(eq.refl unit) &gt;&gt;= exact
</pre></div>

#### [ Kevin Buzzard (Apr 01 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124498669):
<p>that's kind of a cheat because I didn't start <code> by do exact $ </code></p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124498712):
<p>but all this stuff like <code>get_local</code> and <code>to_expr</code>, all these functions return <code>tactic</code> something.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elaborator/near/124498724):
<p>Do I have to use the tactic monad?</p>


{% endraw %}
