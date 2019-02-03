---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78590namespacefieldnotation.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [namespace field notation](https://leanprover-community.github.io/archive/113488general/78590namespacefieldnotation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Apr 11 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921576):
<p>Before I disappeared for a month to handle a visiting-family exception, I was experimenting with using more “namespace field notation.” That is, instead of using <code>list.map f l</code>, I would use <code>l.map f</code>. I like the conciseness gained by removing the namespace <code>list</code>.</p>
<p>However, I had started to sour on it then, and, after returning to my code and trying to refresh my working cache, I find that I no longer like it. Since the field notation differs from the definition notation and from the pretty-printed <code>lean</code> output in errors, going back and forth between notations requires repeatedly reorienting on the positions of arguments. (While <code>list.map</code> is a nice example for advocating use of the notation, when a definition has more than 2 parameters or typically needs bracketed arguments, the notation does not help.)</p>
<p>If we could write definitions using namespace field notation and if the notation were used by <code>lean</code> to pretty-print, I believe the benefit would become clear. Otherwise, I don't think I'll be using it much.</p>
<p>What do you think?</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921708):
<p>It doesn't really make sense to use projection notation in definitions, since it requires that the variable already be declared and have known type. You certainly won't get this before you've even stated the theorem name</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921747):
<p>projection in pretty printing would be nice, but I don't know how hard it is</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921757):
<p>also it's one more thing that can break in inconvenient ways if the pretty printed expression doesn't quite typecheck due to too many implicit things</p>

#### [ Sean Leather (Apr 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921758):
<blockquote>
<p>It doesn't really make sense to use projection notation in definitions, since it requires that the variable already be declared and have known type. You certainly won't get this before you've even stated the theorem name</p>
</blockquote>
<p>Perhaps there could be some alternative <code>notation</code>-like operation to allow being explicit about the projection instead of using the built-in rule that now exists.</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921798):
<p>I don't follow</p>

#### [ Sean Leather (Apr 11 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921806):
<p>In other words, perhaps the implicit projection rule could be replaced with an explicit projection declaration.</p>

#### [ Sean Leather (Apr 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921853):
<p>It would (a) be more flexible and (b) add documentation of the projection notation for a particular definition.</p>

#### [ Sean Leather (Apr 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921862):
<blockquote>
<p>also it's one more thing that can break in inconvenient ways if the pretty printed expression doesn't quite typecheck due to too many implicit things</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What is “it” referring to here?</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921863):
<p>What kind of flexibility are you thinking? Also I don't relish the idea of adding thousands of annotations for what is essentially redundant information, and having to keep it up to date. The current projection algorithm is easy to learn and completely uniform</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921948):
<p>"it" is pp projection notation. The elaborator has less to go on with projection notation, so if it can't solve for the type of a variable immediately projections just halt the whole type inference process. I'm saying that this situation may occur with pp expressions, assuming you aren't using some <code>pp.all</code> type option</p>

#### [ Sean Leather (Apr 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124921998):
<blockquote>
<p>What kind of flexibility are you thinking?</p>
</blockquote>
<p>Declaring which parameter should be used for projection is the main one that comes to mind. I recall running into an issue where projection didn't work, but I think it would if I could explicitly declare how to do it. (I don't remember the exact issue, unfortunately.)</p>

#### [ Sean Leather (Apr 11 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922012):
<blockquote>
<p>"it" is pp projection notation. The elaborator has less to go on with projection notation, so if it can't solve for the type of a variable immediately projections just halt the whole type inference process. I'm saying that this situation may occur with pp expressions, assuming you aren't using some <code>pp.all</code> type option</p>
</blockquote>
<p>Yes, I could see how that could be a problem if pretty-printing involves inferring the projection notation. But, given the above idea of an explicit projection notation, it would not need to infer anything.</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922016):
<p>Projection was less powerful early in its history, because you could only project with the first explicit argument. That restriction has since been dropped, so make sure that isn't the issue you are thinking of</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922063):
<p>it would still need to infer stuff even with projection annotations, since <code>x.bar</code> could mean either <code>list.bar x</code> if <code>x : list a</code> or <code>multiset.bar x</code> if <code>x : multiset a</code>, or even <code>x.bar</code> if <code>x</code> is a namespace</p>

#### [ Sean Leather (Apr 11 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922078):
<blockquote>
<p>Projection was less powerful early in its history, because you could only project with the first explicit argument. That restriction has since been dropped, so make sure that isn't the issue you are thinking of</p>
</blockquote>
<p>No, I don't think that's relevant. My issue is with going back and forth between two different notations.</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922080):
<p>That just sounds like a pp problem</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922130):
<p>I just always use projections in the code, and replace anything I copy after pp with projections</p>

#### [ Sean Leather (Apr 11 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922135):
<blockquote>
<p>That just sounds like a pp problem</p>
</blockquote>
<p>A bit too simplistic of a view, I think. I'm pretty sure we don't want to pretty-print everything in projection notation.</p>

#### [ Mario Carneiro (Apr 11 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922141):
<p>so there's no back and forth unless I'm doing a lot of copy paste from pp anyway, which produces non-human output for several reasons, that's not the only thing I want to change in general</p>

#### [ Sean Leather (Apr 11 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922435):
<p>Here's a simple example:</p>
<p>1. Projection:</p>
<div class="codehilite"><pre><span></span><span class="n">t</span><span class="bp">.</span><span class="kn">open</span> <span class="n">ts</span> <span class="bp">=</span> <span class="n">subst_list</span> <span class="n">xs</span> <span class="n">ts</span> <span class="o">(</span><span class="n">t</span><span class="bp">.</span><span class="kn">open</span> <span class="o">(</span><span class="n">xs</span><span class="bp">.</span><span class="n">map</span> <span class="n">varf</span><span class="o">))</span>
</pre></div>


<p>2. No projection:</p>
<div class="codehilite"><pre><span></span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="n">ts</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">subst_list</span> <span class="n">xs</span> <span class="n">ts</span> <span class="o">(</span><span class="n">typ</span><span class="bp">.</span><span class="kn">open</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">map</span> <span class="n">varf</span> <span class="n">xs</span><span class="o">)</span> <span class="n">t</span><span class="o">)</span>
</pre></div>


<p>The first option is less verbose, but I only ever see it in code I write. The second is what the pretty-printer shows.</p>

#### [ Sean Leather (Apr 11 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922436):
<p>Here are some questions and thoughts prompted by the discussion above:</p>
<p>Why shouldn't I be able to tell Lean to pretty-print the projection notation as in 1? I can already tell it to use some other <code>notation</code> or <code>infix</code>. I don't see how the inference problem is different.</p>
<p>Once I am allowed to say I want definition <code>d</code> to be pretty-printed with projection notation, why shouldn't I be able to declare which parameter is the projection target? Consequently, the declaration to “use projection notation” becomes another <code>notation</code> or <code>infix</code> but specialized to projection.</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922714):
<blockquote>
<p>The first option is less verbose, but I only ever see it in code I write. The second is what the pretty-printer shows.<br>
Why shouldn't I be able to tell Lean to pretty-print the projection notation as in 1? </p>
</blockquote>
<p>Like I said, a pp problem. There's nothing wrong with this in principle, except this is a core lean issue so it's not going to happen until lean 4, and that only if Leo thinks of this himself</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922804):
<blockquote>
<p>Once I am allowed to say I want definition d to be pretty-printed with projection notation, why shouldn't I be able to declare which parameter is the projection target? Consequently, the declaration to “use projection notation” becomes another notation or infix but specialized to projection.</p>
</blockquote>
<p>There isn't really any choice in what argument can be the projection argument, except in definitions which, say, take in more than one <code>list</code> parameter. If you think the second argument is a better projection target than the first, then I suggest you reorder the parameters</p>

#### [ Sean Leather (Apr 11 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922826):
<blockquote>
<p>Like I said, a pp problem. There's nothing wrong with this in principle, except this is a core lean issue so it's not going to happen until lean 4, and that only if Leo thinks of this himself</p>
</blockquote>
<p>Right, but I don't think that means that I can't bring it up here and discuss it, does it? <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (Apr 11 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922879):
<blockquote>
<p>There isn't really any choice in what argument can be the projection argument, except in definitions which, say, take in more than one <code>list</code> parameter. If you think the second argument is a better projection target than the first, then I suggest you reorder the parameters</p>
</blockquote>
<p>I disagree. You could expand projection to include things outside the namespace of the definition.</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922930):
<p>No, that doesn't really work with the way projections are resolved. It gets the type of the argument, and uses that as a namespace to look up projections. If you want a projection to work on a certain argument, make sure the namespace lines up</p>

#### [ Sean Leather (Apr 11 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922944):
<p>But it <em>could</em> work that way with explicit projection notation. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Mario Carneiro (Apr 11 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124922946):
<p>It obviously has to key on <em>something</em>, since otherwise it has to go through all the definitions, and the only available information at that point is the type of the variable</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923047):
<p>I don't see the difference between an explicit projection notation and naming the definition appropriately so the automatic method picks out the desired argument. Do you have a concrete example where you think it would be difficult to do otherwise?</p>

#### [ Sean Leather (Apr 11 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923160):
<p>I did at one point. It had to do with a list parameter, I think, but I don't remember it now.</p>

#### [ Sean Leather (Apr 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923432):
<p>Generally, though, suppose you have a definition that is not for general <code>list</code>s but has a <code>list</code> parameter and you want projection on an <code>list</code> argument, you would need to put the definition in the <code>list</code> namespace. Slightly more concretely, suppose you have something like <code>def n.d : list n → Prop</code>. So, to get projection notation, you would need to rename <code>n.d</code> to <code>list.d</code>. That seems wrong.</p>

#### [ Patrick Massot (Apr 11 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923698):
<p>Sean, since you seem to care about this projection notation, have you seen <a href="https://github.com/leanprover/mathlib/pull/96" target="_blank" title="https://github.com/leanprover/mathlib/pull/96">https://github.com/leanprover/mathlib/pull/96</a> ? Don't hesitate to propose any further clarification or new tricks in <a href="https://github.com/PatrickMassot/mathlib/blob/8bf2648418549d605a18fe5d38a67eb725e66317/docs/extras/structures.md#about-the-namespace-shortcut" target="_blank" title="https://github.com/PatrickMassot/mathlib/blob/8bf2648418549d605a18fe5d38a67eb725e66317/docs/extras/structures.md#about-the-namespace-shortcut">the relevant section</a></p>

#### [ Sean Leather (Apr 11 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923908):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I saw it. It was part of the reason, other than that I've been thinking about it for a while, that I brought up the subject.</p>
<p>I think the only change I would make is that “first explicit argument” is not correct. As <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> said, the argument (or what I prefer to call “parameter”) need not be explicit. In other words, you could have this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sum</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">point</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">p</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="n">x</span> <span class="bp">+</span> <span class="n">p</span><span class="bp">.</span><span class="n">y</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="n">p</span><span class="bp">.</span><span class="n">sum</span> <span class="n">α</span>
</pre></div>

#### [ Patrick Massot (Apr 11 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124923954):
<p>What would you write then?</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924022):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> </p>
<blockquote>
<p>So, to get projection notation, you would need to rename n.d to list.d. That seems wrong.</p>
</blockquote>
<p>But this is how it works in OOP languages the notation was borrowed from, if you interpret classes as introducing namespaces. How would we know to look in the namespace <code>n</code> for <code>d</code>?</p>

#### [ Sean Leather (Apr 11 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924026):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> The simplest change would be to remove “explicit” and to give an example in which the argument is not explicit. You could use the one above, though you should check it first to make sure I didn't make a mistake.</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924080):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Btw, have we ever discussed a notation like <code>xs.(map f).(filter g)</code> to solve the chaining issue? I might have to experiment with a macro for that in Lean 4 <span class="emoji emoji-1f606" title="laughing">:laughing:</span> .</p>

#### [ Patrick Massot (Apr 11 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924122):
<p>Actually I don't know how to call that kind of argument that lingers right of the colon. My explicit was rather referring to <code>(x : X)</code> vs <code>{x : X}</code>.</p>

#### [ Patrick Massot (Apr 11 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924127):
<blockquote>
<p>But this is how it works in OOP languages the notation was borrowed from, if you interpret classes as introducing namespaces. How would we know to look in the namespace <code>n</code> for <code>d</code>?</p>
</blockquote>
<p>At last, someone confess FP is trying to mimic OOP greatness</p>

#### [ Sean Leather (Apr 11 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924136):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Ah, okay. I may have misinterpreted it then. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Sean Leather (Apr 11 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924137):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>:</p>
<blockquote>
<p>But this is how it works in OOP languages the notation was borrowed from, if you interpret classes as introducing namespaces. How would we know to look in the namespace <code>n</code> for <code>d</code>?</p>
</blockquote>
<p>I don't follow. In OOP, you wouldn't find a method with the type <code>list n</code> in a <code>list</code> class.</p>

#### [ Patrick Massot (Apr 11 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924183):
<p>But I'm interested in explaining how far that projection notation extends. So I'll definitely try that <code>def sum (α : Type) [has_add α] : point α → α := λ p, p.x + p.y
</code></p>

#### [ Patrick Massot (Apr 11 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924188):
<p>But right now I'm typing notes on the Nash-Kuiper embedding theorem, not playing with Lean or chatting on Zulip</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924193):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> In Java, <code>x.f</code> will look up <code>f</code> in the class of <code>x</code> and pass <code>x</code> as the <code>this</code> argument. Basically what happens in Lean.</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924311):
<p>The whole point of field notation is to hide the namespace. I don't see the benefit of <code>p.sum</code> over <code>sum p</code>.</p>

#### [ Sean Leather (Apr 11 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924433):
<blockquote>
<p>In Java, <code>x.f</code> will look up <code>f</code> in the class of <code>x</code> and pass <code>x</code> as the <code>this</code> argument. Basically what happens in Lean.</p>
</blockquote>
<p>Right. It also extends the lookup to superclasses. But still, that's rather limiting, I think.</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924449):
<blockquote>
<p>It also extends the lookup to superclasses.</p>
</blockquote>
<p>As we do</p>

#### [ Sean Leather (Apr 11 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924452):
<p>What's a superclass in Lean?</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924502):
<p>The thing after <code>extends</code> :)</p>

#### [ Sean Leather (Apr 11 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924513):
<p>Are you talking about <code>class</code> or <code>namespace</code>? I wasn't aware a <code>namespace</code> could <code>extends</code> something.</p>

#### [ Gabriel Ebner (Apr 11 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924570):
<blockquote>
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Btw, have we ever discussed a notation like <code>xs.(map f).(filter g)</code> to solve the chaining issue? I might have to experiment with a macro for that in Lean 4 <span class="emoji emoji-1f606" title="laughing">:laughing:</span> .</p>
</blockquote>
<p>No I don't think so.  I think the only proposal that aimed to simplify chaining was my Agda-like <code>xs .map f .filter g</code>, which many people apparently found abhorrent.</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/namespace%20field%20notation/near/124924578):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> Ah sorry, I was thinking of the basic field notation, which will pick up fields from super structures as well. But it doesn't work with functions in the namespace... yet</p>


{% endraw %}
