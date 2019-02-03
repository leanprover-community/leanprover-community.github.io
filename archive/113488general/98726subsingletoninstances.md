---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98726subsingletoninstances.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [subsingleton instances](https://leanprover-community.github.io/archive/113488general/98726subsingletoninstances.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Mar 03 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123231023):
<p>I'm struggling with the following proof</p>
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">fintype</span> <span class="err">↥</span><span class="n">s</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span>
<span class="err">⊢</span> <span class="n">card</span> <span class="err">↥</span><span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span>
</pre></div>


<p>the trouble is that rw h` does not work because it has to rewrite the fintype instance at the same time. I'm having trouble in general with lean not recognizing two terms as equal because the fintype instances are different. Is there a nice way of dealing with this. I can use congr to prove that two terms with different fintype instances are equal, but this seems quite messy.</p>

#### [ Gabriel Ebner (Mar 03 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123231503):
<p>Does <code>simp [h]</code> work by chance?</p>

#### [ Chris Hughes (Mar 03 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123232077):
<p>no</p>

#### [ Kevin Buzzard (Mar 03 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123234939):
<div class="codehilite"><pre><span></span>import data.fintype
universe u


example (α : Type u) (s : set α) [fintype s] (h : s = ∅) : fintype.card ↥s = 0 := begin
rw ←fintype.card_empty,
rw fintype.card_eq,
rw h,
show nonempty ({x : α // false} ≃ empty),
refine ⟨_⟩,
refine ⟨_,_,_,_⟩,
exact λ x, false.elim x.property,
intro x,cases x,
intro x,exact false.elim x.property,
intro x,cases x,
end
</pre></div>

#### [ Kevin Buzzard (Mar 03 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123234993):
<p>kind of a comical proof because I never used these types before, so most of it is me experimenting with what is there. Obviously this can be shortened a lot.</p>

#### [ Chris Hughes (Mar 03 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123235101):
<p><code>rw ← set.empty_card; congr; assumption</code> is also a slightly shorter proof, but I was hoping there was an easy way.</p>

#### [ Patrick Massot (Mar 03 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123235357):
<p>Are students allowed to be that insolent in England?</p>

#### [ Gabriel Ebner (Mar 03 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123235716):
<p>I think this is a more idiomatic solution:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>
<span class="kn">universe</span> <span class="n">u</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card_emptyset</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)]</span> <span class="o">:</span>
    <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">fintype</span><span class="bp">.</span><span class="n">card</span><span class="o">],</span> <span class="n">apply</span> <span class="n">finset</span><span class="bp">.</span><span class="n">ext</span><span class="bp">.</span><span class="n">mpr</span><span class="o">,</span> <span class="n">intros</span><span class="o">,</span> <span class="n">cases</span> <span class="n">a</span><span class="o">,</span> <span class="n">cases</span> <span class="n">a_property</span>
<span class="kn">end</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="bp">-</span><span class="n">simp</span><span class="o">]</span> <span class="n">set</span><span class="bp">.</span><span class="n">set_coe_eq_subtype</span> <span class="c1">-- bad simp lemma</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">s</span><span class="o">]</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span>
    <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="err">↥</span><span class="n">s</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span>
</pre></div>

#### [ Chris Hughes (Mar 03 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123237242):
<p>the lemma <code>fintype.card_emptyset</code> already exists, it's called <code>set.empty_card</code> in data/set/finite. However it doesn't require a fintype instance as an argument, because it uses a different proof that the empty set is finite.</p>

#### [ Gabriel Ebner (Mar 03 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123237868):
<p>That's the core of the misunderstanding: <code>fintype</code> is not a proof, it is data.  So you need to write all lemmas with generic <code>fintype</code> arguments, otherwise they won't match.  We have a very similar problem with decidability instances actually.</p>

#### [ Gabriel Ebner (Mar 03 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123237912):
<p>One solution is to use E-matching in the SMT mode.  This would transparently ignore the different subsingleton instances.  However the SMT mode is abandoned and does not have a clear future.</p>

#### [ Gabriel Ebner (Mar 03 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123238082):
<p>I'm not sure if I see a good and general solution.  The same issue applies not just to simp, but pretty much all tactics and also term-mode proof construction.  A somewhat clean approach that works in all those cases would be to post-process the types of lemmas, and generalize non-dependent subsingleton subterms.  Maybe we could do this automatically with more powerful user attributes, or user commands once the new parser lands.</p>

#### [ Kevin Buzzard (Mar 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123239544):
<blockquote>
<p>Are students allowed to be that insolent in England?</p>
</blockquote>
<p>Ha ha :-) Chris knows a lot more about these finite types than I do. He's been doing stuff with finite groups -- I've never used them at all. Chris -- why not PR some stuff to xena? Or just email it me if you can't be bothered? I'd be interested to see what you've been doing.</p>

#### [ Chris Hughes (Mar 03 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123240179):
<p>Just made a PR to xena. It's quite an incomplete file with a few sorries, but there's lagrange in there, which is good.</p>

#### [ Patrick Massot (Mar 04 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123256948):
<p>What's the point of proving Lagrange without developing group actions? If you want to do more group theory you won't be able to bypass them much longer.</p>

#### [ Patrick Massot (Mar 04 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123256953):
<p><span class="user-mention" data-user-email="scott@tqft.net" data-user-id="110087">@Scott Morrison</span> what happened to your student who was doing group theory?</p>

#### [ Patrick Massot (Mar 04 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123256993):
<p><span class="user-mention" data-user-email="chrishughes24@gmail.com" data-user-id="110044">@Chris Hughes</span> what happened to your analysis PRs?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123261173):
<blockquote>
<p>What's the point of proving Lagrange without developing group actions? If you want to do more group theory you won't be able to bypass them much longer.</p>
</blockquote>
<p>There's a danger here that you can argue that there's no point doing anything because someone did something more general. Chris is a first year undergraduate who just learnt Lagrange's theorem and we don't teach group actions until the 3rd year, so his view of the subject is very different to yours. I completely appreciate your point of view but the answer is that Chris is using Lean to teach himself the material that he's going to be examined on in the summer.</p>

#### [ Chris Hughes (Mar 04 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123261269):
<p><span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span> I'm waiting for a PR on Cauchy Sequence limits to be merged, and then I'll merge some more stuff. There was a bit of discussion about the best way to implement the exponential function, about whether to do it using Johannes definition of a limit, or Mario's simpler definition of a limit. I'm not going to work on making it mathlib ready until that discussion is resolved.</p>
<p>The answer to your other question was pretty much the same as <span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span> 's answer. I've no idea if my group theory stuff is useful, given that I've formalised most of what I know, it's unlikely I'll have defined things in the most useful manner.</p>

#### [ Patrick Massot (Mar 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268844):
<p>I agree that aiming for the greatest generality is not a good idea. My point is that, if you continue finite group theory, then you will encounter group actions really soon (for instance if you go for Sylow).</p>

#### [ Patrick Massot (Mar 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268852):
<p>Maybe I'm confused about what you know because Kevin teaches the concept of rigorous proofs, schemes, and perfectoid spaces in the same year.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268901):
<p>I teach several different courses/classes I guess</p>

#### [ Patrick Massot (Mar 04 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268913):
<p>No, you teach schemes to Kenny and you mentioned teaching perfectoid spaces to first years on March 11th or something</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268915):
<p>That's right but these are different things</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268916):
<p>There's my normal course for 220 first years</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268917):
<p>there is xena</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268919):
<p>there is an undergraduate conference</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268958):
<p>I am also teaching a graduate course</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268966):
<p>oh golly</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123268967):
<p>he pushed them to mine</p>

#### [ Patrick Massot (Mar 04 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269006):
<p>yes</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269009):
<p>OK I merged.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269010):
<p>Should I just push to mathlib?</p>

#### [ Patrick Massot (Mar 04 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269067):
<p>Nah</p>

#### [ Patrick Massot (Mar 04 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269072):
<p>You should do something to my pending review</p>

#### [ Patrick Massot (Mar 04 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269079):
<p>Otherwise Chris cannot see it</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269135):
<p>I can't figure out how to do that</p>

#### [ Patrick Massot (Mar 04 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269140):
<p>Hum, maybe the fact that you merged is not helping here</p>

#### [ Patrick Massot (Mar 04 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269189):
<p>Or maybe it's my fault</p>

#### [ Patrick Massot (Mar 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269192):
<p>yes it was</p>

#### [ Patrick Massot (Mar 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269198):
<p>I forgot to hit some button to submit my review</p>

#### [ Patrick Massot (Mar 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269199):
<p>It should be visible now</p>

#### [ Patrick Massot (Mar 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269200):
<p><span class="user-mention" data-user-email="chrishughes24@gmail.com" data-user-id="110044">@Chris Hughes</span> could you have a look at <a href="https://github.com/kbuzzard/mathlib/pull/1/" target="_blank" title="https://github.com/kbuzzard/mathlib/pull/1/">https://github.com/kbuzzard/mathlib/pull/1/</a> ?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123269241):
<p>OK I can now see it</p>

#### [ Scott Morrison (Mar 04 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton%20instances/near/123271415):
<p><span class="user-mention" data-user-email="patrickmassot@free.fr" data-user-id="110031">@Patrick Massot</span> they are getting a PR ready. We met on Friday to discuss, and I'm now travelling all this week (actually doing some maths...), so I'm not sure when it will happen.</p>
<p>I think his plan is to send an initial PR covering subgroups, normal subgroups, centers, and kernels, and then a second PR with quotient groups and the first isomorphism theorem.</p>


{% endraw %}
