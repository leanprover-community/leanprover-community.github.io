---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36954singletonunique.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [singleton / unique](https://leanprover-community.github.io/archive/113488general/36954singletonunique.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jan 18 2019 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156348116):
<p>It has been remarked before that we need a class that is <code>nonempty</code> + <code>subsingleton</code>. I guess the canonical name would be <code>singleton</code>. How would people want to define it?</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">singleton</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">elem</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">uniq</span> <span class="o">:</span> <span class="err">\</span><span class="k">Pi</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span><span class="n">y</span> <span class="o">:</span> <span class="n">X</span><span class="o">),</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span>
</pre></div>

#### [ Nicholas Scheel (Jan 18 2019 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156348829):
<p>why not just take nonempty and subsingleton as assumptions together?</p>

#### [ Johan Commelin (Jan 18 2019 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349297):
<p>I guess there are two options: either we make an inductive <code>Prop</code>, or we make a thing that lives in <code>Type*</code> but has an easy projector to the element.</p>

#### [ Johan Commelin (Jan 18 2019 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349300):
<p>I'm not sure what is best.</p>

#### [ Johan Commelin (Jan 18 2019 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349909):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> There is probably common wisdom on this in the wider community. What would you suggest?</p>

#### [ Johannes Hölzl (Jan 18 2019 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349975):
<p>Hm, this is a case which is not often used. But I would guess the <code>Type*</code> variant could be more helpful.</p>

#### [ Johan Commelin (Jan 18 2019 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349979):
<p>It is not? Ooh, that surprises me.</p>

#### [ Johannes Hölzl (Jan 18 2019 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156349989):
<p>Up to now we didn't need it in mathlib...</p>

#### [ Johan Commelin (Jan 18 2019 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350044):
<p>Where would you put it?</p>

#### [ Johan Commelin (Jan 18 2019 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350048):
<p>Somewhere in <code>data/</code>?</p>

#### [ Johannes Hölzl (Jan 18 2019 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350123):
<p>Maybe even in <code>logic/basic.lean</code>? Plus the <code>unit</code> instance.</p>

#### [ Johan Commelin (Jan 18 2019 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350136):
<p>Is it ok to extend <code>inhabited</code>?</p>

#### [ Johan Commelin (Jan 18 2019 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350138):
<p>Or is that wrong for semantic reasons?</p>

#### [ Johan Commelin (Jan 18 2019 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350189):
<p>I still don't know the semantics of all those types like <code>inhabited</code>, <code>default</code>, etc...</p>

#### [ Johannes Hölzl (Jan 18 2019 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156350275):
<p>Yes, extend <code>inhabited</code> and derive <code>subsingleton</code></p>

#### [ Johan Commelin (Jan 18 2019 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351117):
<p>Ooop <span class="emoji emoji-1f648" title="see no evil">:see_no_evil:</span> the name <code>singleton</code> is of course already taken by singleton sets...</p>

#### [ Johan Commelin (Jan 18 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351184):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Do you have a good suggestion for a name?</p>

#### [ Kenny Lau (Jan 18 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351186):
<p>nope</p>

#### [ Johan Commelin (Jan 18 2019 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351566):
<p>Aahrg, <code>punit.inhabited</code> is only for <code>Type</code>, not <code>Type u</code>.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351834):
<p>I guess the name <code>contractible</code> is to HoTT, right?</p>

#### [ Reid Barton (Jan 18 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351888):
<p>Maybe <code>unique</code>?</p>

#### [ Johan Commelin (Jan 18 2019 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351908):
<p>Yes, that might work. But I'dd like to also emphasise the existence.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156351921):
<p>People might think that <code>unique</code> is a variant on <code>subsingleton</code>.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352558):
<p><a href="https://github.com/leanprover/mathlib/issues/605" target="_blank" title="https://github.com/leanprover/mathlib/issues/605">#605</a> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span></p>

#### [ Mario Carneiro (Jan 18 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352717):
<p>what's wrong with just <code>inhabited</code> + <code>subsingleton</code> or <code>nonempty</code> + <code>subsingleton</code>?</p>

#### [ Johan Commelin (Jan 18 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352733):
<p>That it's longer to write?</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352740):
<p>not good enough, definitions are worth more than that</p>

#### [ Johan Commelin (Jan 18 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352747):
<p>When I'm pulling a limit cone through and adjoint functor I want to spend as little time with these stupid classes...</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352802):
<p>aha, okay sure I've seen this. Are you perhaps saying this about a subtype?</p>

#### [ Johan Commelin (Jan 18 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352805):
<p>No...</p>

#### [ Johan Commelin (Jan 18 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352807):
<p>Why do you think that?</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352821):
<p>That's the way it usually goes with universal properties</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352831):
<p>there exists a unique map satisfying such and such property</p>

#### [ Johan Commelin (Jan 18 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352835):
<p>Ok, maybe. I haven't thought of it like that. But there are no subtypes in sight with what I'm doing right now.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352839):
<p>Aah, but that's all packaged into <code>cone_morphism</code></p>

#### [ Johan Commelin (Jan 18 2019 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352901):
<p>I want to say that <code>c</code> is a limit cone if <code>\Pi t, unique (cone_morphism c t)</code></p>

#### [ Mario Carneiro (Jan 18 2019 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352910):
<p>why not say that in two conditions?</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352916):
<p>you have a morphism and a proof of uniqueness</p>

#### [ Johan Commelin (Jan 18 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352918):
<p>And then adjunctions give me <code>equiv</code>s, and <code>equiv.unique_of_equiv</code> will let me easily manipulate it.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352929):
<p>It's too unbundled.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352935):
<p>I agree that that is also useful. And it is what we have right now in the library.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352937):
<p>It's good when you are applying these things in concrete cases.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156352990):
<p>But for abstract category theory, I think it becomes a lot easier to manipulate these things when they are bundled.</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353025):
<p>I take it you don't want to use this like a typeclass then?</p>

#### [ Johan Commelin (Jan 18 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353084):
<p>Uuuh, I don't know?</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353100):
<p>what does <code>equiv.unique_of_equiv</code> say?</p>

#### [ Johan Commelin (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353116):
<p>If <code>X \equiv Y</code> and you know <code>unique Y</code> then you get <code>unique X</code>.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353117):
<p>But you knew that.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353119):
<p>You want code.</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353124):
<p>and that's all you intend to do with <code>unique</code>, besides using the projections directly?</p>

#### [ Johan Commelin (Jan 18 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353126):
<p><a href="https://github.com/leanprover/mathlib/pull/605/files#diff-a714d761eac2ec5a2e4b0ed4592f9c46R474" target="_blank" title="https://github.com/leanprover/mathlib/pull/605/files#diff-a714d761eac2ec5a2e4b0ed4592f9c46R474">https://github.com/leanprover/mathlib/pull/605/files#diff-a714d761eac2ec5a2e4b0ed4592f9c46R474</a></p>

#### [ Johan Commelin (Jan 18 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353185):
<p>Eehm, yes, for the time being.</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353191):
<p>By the way, you can define <code>unique</code> in a simpler way, with only one quantifier</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353197):
<p>there is <code>x : A</code> and <code>\forall y, x = y</code></p>

#### [ Johan Commelin (Jan 18 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353208):
<p>Yes, I've derived those versions. But I wanted to be as symmetric as possible.</p>

#### [ Johan Commelin (Jan 18 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353214):
<p>Or is that not useful?</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353269):
<p>For the structure you want the axiom to be easy to prove. Probably when one picks a default it will be easy to work with</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353286):
<p>like how one shows a zero ring is <code>unique</code>, you show every element is 0, and hence every element is equal</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353291):
<p>saves you a step</p>

#### [ Johan Commelin (Jan 18 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353310):
<p>Ok, fine. I'll rewrite that.</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353313):
<p>besides, the two quantifier version is available as <code>subsingleton.eq</code></p>

#### [ Johan Commelin (Jan 18 2019 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353468):
<p>Ok, sure.</p>

#### [ Mario Carneiro (Jan 18 2019 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353487):
<p>I don't have any better suggestions for the name than <code>unique</code></p>

#### [ Mario Carneiro (Jan 18 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353504):
<p>but I think it might be usable as a regular type</p>

#### [ Johan Commelin (Jan 18 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353638):
<p>Ok, so <code>structure</code> instead of <code>class</code>?</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353676):
<p>maybe a <code>class</code> on some days? If you use <code>attribute [class] unique</code> after the definition you can use it as a class when you feel like it but the projections won't have inst implicit</p>

#### [ Johan Commelin (Jan 18 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353700):
<p>Aah, maybe that helps.</p>

#### [ Johan Commelin (Jan 18 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353753):
<p>I guess I should make some simp-lemmas. And then hopefully <code>tidy</code> can work with this nicely.</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353770):
<p>Here are some interesting facts: <code>subsingleton (unique A)</code>, and <code>unique (unique A) &lt;-&gt; unique A</code>, <code>unique A -&gt; unique B</code> if <code>f : A -&gt; B</code> is a surjection (not required to be a bijection)</p>

#### [ Johan Commelin (Jan 18 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353798):
<p>Yep... would you like all of those?</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353802):
<p>if you are going to define a thing you should prove all the basic theorems</p>

#### [ Johan Commelin (Jan 18 2019 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353873):
<p>Where should those go?</p>

#### [ Johan Commelin (Jan 18 2019 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353875):
<p><code>logic/basic</code>?</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353945):
<p>how about <code>logic/unique</code> unless there is a reason to merge it</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353950):
<p>I don't think there are currently any new definitions in <code>logic/basic</code></p>

#### [ Mario Carneiro (Jan 18 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353964):
<p>but <code>logic/basic</code> probably needs a refactor, it's a bit of a grab bag</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156353971):
<p>it literally has a <code>miscellaneous</code> section, that's never a good sign</p>

#### [ Johan Commelin (Jan 18 2019 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354031):
<p>Ok, I can start <code>logic/unique</code></p>

#### [ Johan Commelin (Jan 18 2019 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354050):
<p>If I do the <code>attribute [class]</code> thing, and I assume <code>[unique X]</code> then it still doesn't infer <code>inhabited X</code>. So I have to state those inferences by hand?</p>

#### [ Johan Commelin (Jan 18 2019 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354355):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Should I include simp-lemmas like this?</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">to_inhabited</span> <span class="err">‹</span><span class="n">unique</span> <span class="n">α</span><span class="err">›</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">eq_default</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">default</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">uniq</span> <span class="bp">_</span> <span class="n">a</span>
</pre></div>

#### [ Mario Carneiro (Jan 18 2019 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354405):
<p>you have to mark <code>unique.to_inhabited</code> as <code>instance</code></p>

#### [ Mario Carneiro (Jan 18 2019 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354416):
<p><code>eq_default</code> won't work</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354429):
<p>neither will <code>default_eq</code></p>

#### [ Johan Commelin (Jan 18 2019 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354443):
<p>Why not?</p>

#### [ Johan Commelin (Jan 18 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354515):
<p>It would be cool if <code>simp</code> would just simplify every element to the default.</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354520):
<p>simp lemmas with a variable on the left trigger on anything</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354529):
<p>at least that's what lean says; I don't see why that's a problem but it's explicitly rejected by <code>simp</code></p>

#### [ Johan Commelin (Jan 18 2019 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354548):
<p>Aah, and simp doesn't know yet if the <code>unique X</code> instance will be found or not.</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354584):
<p>well, it could just try to apply it on every term... you know I think this is a bad idea</p>

#### [ Johan Commelin (Jan 18 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354647):
<blockquote>
<p>you have to mark <code>unique.to_inhabited</code> as <code>instance</code></p>
</blockquote>
<p>Like so: <code>attribute [instance] unique.to_inhabited</code>?</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354650):
<p>yes</p>

#### [ Johan Commelin (Jan 18 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156354671):
<p>But then</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">unique</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">α</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>


<p>still fails.</p>

#### [ Mario Carneiro (Jan 18 2019 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156355179):
<p>oh, I guess that's because the <code>unique</code> is explicit in <code>unique.to_inhabited</code>. So you will have to make an instance like you did</p>

#### [ Johan Commelin (Jan 18 2019 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156356937):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Should the following be done with instances or not?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">of_surjective</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">surjective</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">default</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">h</span><span class="bp">.</span><span class="n">default</span> <span class="o">}</span>
</pre></div>

#### [ Johannes Hölzl (Jan 18 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156357666):
<p><code>hf</code> is not required...</p>

#### [ Johan Commelin (Jan 18 2019 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156357745):
<p>Lol... I've been thinking too much about <code>unique</code> <span class="emoji emoji-1f600" title="grinning">:grinning:</span></p>

#### [ Johan Commelin (Jan 18 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156357779):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I pushed an update to <a href="https://github.com/leanprover/mathlib/issues/605" target="_blank" title="https://github.com/leanprover/mathlib/issues/605">#605</a></p>

#### [ Johan Commelin (Jan 18 2019 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/singleton%20/%20unique/near/156358134):
<p>Woops, forgot to <code>git add</code> the new file.</p>


{% endraw %}
