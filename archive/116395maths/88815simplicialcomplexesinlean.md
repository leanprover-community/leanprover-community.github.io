---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/88815simplicialcomplexesinlean.html
---

## Stream: [maths](index.html)
### Topic: [simplicial complexes in lean](88815simplicialcomplexesinlean.html)

---


{% raw %}
#### [ Johan Commelin (May 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203178):
<p>Now we have simplicial complexes!</p>

#### [ Johan Commelin (May 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203179):
<p>And also the singular complex</p>

#### [ Johan Commelin (May 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203191):
<p>With coefficients in arbitrary <code>\Z</code>-modules</p>

#### [ Johan Commelin (May 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203237):
<p>See <a href="https://github.com/jcommelin/mathlib/tree/simplicial" target="_blank" title="https://github.com/jcommelin/mathlib/tree/simplicial">https://github.com/jcommelin/mathlib/tree/simplicial</a></p>

#### [ Patrick Massot (May 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203238):
<p>A less magical solution:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">simplicial_identity₁</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">simplicial_set</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">])</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">@</span><span class="n">δ</span> <span class="n">X</span> <span class="n">n</span><span class="o">)</span> <span class="n">i</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">j</span><span class="bp">.</span><span class="n">succ</span> <span class="bp">=</span> <span class="n">δ</span> <span class="n">j</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">i</span><span class="bp">.</span><span class="n">raise</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">δ</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">comp</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">comp</span><span class="o">,</span>
  <span class="n">congr&#39;</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">simplex_category</span><span class="bp">.</span><span class="n">simplicial_identity₁</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (May 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203241):
<p>Aaah, so <code>congr'</code> is what I was waiting for...</p>

#### [ Johan Commelin (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203244):
<p>I have no idea what that does...</p>

#### [ Patrick Massot (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203250):
<p>Uses congruence exactly once</p>

#### [ Patrick Massot (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203254):
<p>congruence is something we wouldn't bother to state</p>

#### [ Johan Commelin (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203256):
<p>Alas, we don't have singular homology yet. Because there are no quotient groups... only quotient modules...</p>

#### [ Patrick Massot (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203257):
<p>x = y implies f(x) = f(y)</p>

#### [ Johan Commelin (May 28 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203301):
<p>And although we take coeffients in <code>\Z</code>-modules, we get a complex of <code>add_comm_group</code>s</p>

#### [ Johan Commelin (May 28 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203311):
<p>Because <code>finsupp</code> gives me <code>add_comm_group</code>, and because <code>is_linear_map</code> drove me crazy...</p>

#### [ Patrick Massot (May 28 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203317):
<p>Small tip: <code>i</code> and <code>j</code> should be implicit arguments because they can be inferred from <code>H</code></p>

#### [ Johan Commelin (May 28 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203320):
<p>Ok, fair enough</p>

#### [ Patrick Massot (May 28 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203321):
<p>And this is what I did in my <code>simplex_category.simplicial_identity₁ _ _ H</code></p>

#### [ Johan Commelin (May 28 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203364):
<p>So, now begins the ugly part...</p>

#### [ Johan Commelin (May 28 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203365):
<p>cleaning up the proof</p>

#### [ Patrick Massot (May 28 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203429):
<p><a href="https://github.com/jcommelin/mathlib/blob/06469f0cd7c502ec64b31ba5e6211e937a00b0e1/algebraic_topology/simplicial_set.lean#L49" target="_blank" title="https://github.com/jcommelin/mathlib/blob/06469f0cd7c502ec64b31ba5e6211e937a00b0e1/algebraic_topology/simplicial_set.lean#L49">https://github.com/jcommelin/mathlib/blob/06469f0cd7c502ec64b31ba5e6211e937a00b0e1/algebraic_topology/simplicial_set.lean#L49</a> certainly looks like it could use some cleaning</p>

#### [ Johan Commelin (May 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127204820):
<p>I cleaned up that line</p>

#### [ Johan Commelin (May 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127204821):
<p>I also added some user comments to the definitions</p>

#### [ Johan Commelin (May 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127204822):
<p><a href="https://github.com/leanprover/mathlib/pull/144" target="_blank" title="https://github.com/leanprover/mathlib/pull/144">https://github.com/leanprover/mathlib/pull/144</a></p>

#### [ Patrick Massot (May 28 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209260):
<p><a href="https://gist.github.com/PatrickMassot/ef4d356b2c42e469a94f392d61cf173b" target="_blank" title="https://gist.github.com/PatrickMassot/ef4d356b2c42e469a94f392d61cf173b">https://gist.github.com/PatrickMassot/ef4d356b2c42e469a94f392d61cf173b</a></p>

#### [ Patrick Massot (May 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209274):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  I went through your file, with random local edits</p>

#### [ Patrick Massot (May 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209277):
<p>I stopped when I went below 150 lines</p>

#### [ Patrick Massot (May 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209281):
<p>I hope you can learn stuff from the diff</p>

#### [ Patrick Massot (May 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209285):
<p>But keep in mind these are only local edits</p>

#### [ Johan Commelin (May 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209326):
<p>Thanks! I'm looking at it!</p>

#### [ Patrick Massot (May 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209332):
<p>You certainly need some global thinking to get useful lemmas replacing parts of this gigantic proof</p>

#### [ Patrick Massot (May 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209344):
<p>and using <code>calc</code> would almost certainly make a more readable proof</p>

#### [ Patrick Massot (May 28 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209719):
<p>One last edit spotted because VScode showed me a large area without blue marking: after line 75 of my version <code>simpa using nat.succ_le_succ (mem_filter.mp hp).2</code> closes the goal</p>

#### [ Johan Commelin (May 28 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213378):
<p>So what is the best way to get some intuition for when to try the <code>finish</code> magic? Or should I just always try it?</p>

#### [ Kenny Lau (May 28 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213387):
<p>don't use it :P</p>

#### [ Patrick Massot (May 28 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213438):
<p>Reading the doc is a good start</p>

#### [ Johan Commelin (May 28 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213549):
<p>Oooh, and thanks a lot for shaving of 80 lines!</p>

#### [ Patrick Massot (May 28 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213663):
<p>Again, you can certainly shave much more, but I hope you can still learn something from this diff</p>

#### [ Kevin Buzzard (May 28 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127222299):
<p>Johan I have had my mind on other things today and have only just noticed this -- well done! Want to try perfectoid spaces now? :-)</p>

#### [ Johan Commelin (May 29 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127237060):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Well, I'm not so sure what the best way forward is. (1) I need to do some paper writing on non-formal maths. (2) I would love to formalise something cool (like perfectoid spaces), but I will need a lot of help. (3) There is still a lot of scaffolding missing. <code>module.lean</code> needs some love, I would like to do finitely generated groups/modules/algebras/fields. Then we can do number fields, rings of integers. Define etale morphisms of schemes. Galois theory... the list goes on and on.</p>

#### [ Johan Commelin (May 29 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127237062):
<p>So, concerning (3). Your plan is to train an army of students  to do this for us.</p>

#### [ Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241755):
<p>Yes, I also do not know what the best way forward is. Here are some things that need doing.</p>

#### [ Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241788):
<p>1) I should look at your code and review it</p>

#### [ Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241793):
<p>2) Someone should look at my schemes code and review it</p>

#### [ Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241798):
<p>3) A group of people should define a perfectoid space before 1st August</p>

#### [ Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241800):
<p>I am unclear about how important it is to put those things in an appropriate order</p>

#### [ Johan Commelin (May 29 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241826):
<blockquote>
<p>2) Someone should look at my schemes code and review it</p>
</blockquote>
<p>I could try to be that someone. But I guess that doesn't help. I can't give much feedback on the Lean... and I'm quite sure that the maths is fine (-; After all, Lean thinks its fine. So I definitely want to review it. But I guess the only one gaining something from that is myself.</p>

#### [ Johan Commelin (May 29 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241875):
<p>1) is not very important. That can wait.</p>

#### [ Johan Commelin (May 29 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241902):
<p>Sounds like Assia wants to look at your scheme code as well.</p>

#### [ Johan Commelin (May 29 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242065):
<p>Ok, Kevin, I've attended a seminar on perfectoid spaces. And I have seen some talks on them (including one by you). Do you think the complexity of the definition is much beyond that of schemes? To me it seems like you need to prove some stuff on power-bounded elements and such, and otherwise you just run the "sheaf of rings on a space" machinery, with a different model of affines.</p>

#### [ Johan Commelin (May 29 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242071):
<p>But of course that is hopelessly naive. Both math-wise and lean-wise, I guess.</p>

#### [ Kevin Buzzard (May 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242099):
<p>No, I think defining a perfectoid space will be easy</p>

#### [ Kevin Buzzard (May 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242102):
<p>that's why I'm so keen to do it</p>

#### [ Kevin Buzzard (May 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242104):
<p>I can see no obstruction</p>

#### [ Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242110):
<p>and if we find an obstruction</p>

#### [ Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242145):
<p>then we learn more about whether Lean is an appropriate place to do interesting mathematics</p>

#### [ Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242148):
<p>but if we find an obstruction</p>

#### [ Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242153):
<p>I am optimistic the CS guys will fix it</p>

#### [ Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242155):
<p>because look at my horrible pre_semi_sheaf question</p>

#### [ Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242156):
<p>those goals looked awful</p>

#### [ Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242157):
<p>and they fixed it</p>

#### [ Johan Commelin (May 29 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242177):
<p>Ok... do you want to do it in a separate project? Or in a feature branch of mathlib?</p>

#### [ Johan Commelin (May 29 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242302):
<blockquote>
<p>because look at my horrible pre_semi_sheaf question<br>
those goals looked awful<br>
and they fixed it</p>
</blockquote>
<p>Yes, that was fantastic.</p>

#### [ Sean Leather (May 29 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242305):
<blockquote>
<p>Ok... do you want to do it in a separate project? Or in a feature branch of mathlib?</p>
</blockquote>
<p>I recommend not starting from a fork of mathlib. Your compile times will generally be faster. You can always add it to mathlib later.</p>

#### [ Johan Commelin (May 29 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242353):
<p>Ok, I developed simplicial sets in a feature branch. And I was quite happy.</p>

#### [ Johan Commelin (May 29 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242365):
<p>The positive side is that it is very easy to make small improvements to mathlib when you need them.</p>

#### [ Johan Commelin (May 29 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242369):
<p>For example, I made small changes to <code>fin</code> and later added <code>nnreal</code>, and I got those merged before my current PR.</p>

#### [ Sean Leather (May 29 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242416):
<p>I've done both, and I was happier not starting from mathlib. <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Sean Leather (May 29 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242432):
<p>I just add files to the same directory as mathlib that I intend to place them. It's just as easy.</p>

#### [ Kevin Buzzard (May 29 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127264180):
<p>Oh that's a nice idea</p>

#### [ Kevin Buzzard (May 29 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127264181):
<p>I was just mulling over this sort of thing myself.</p>

#### [ Scott Morrison (May 30 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279311):
<p>I think an advantage of working in a feature branch of mathlib is that it keeps at the front of your mind that it's important that new work is eventually merged into mathlib.</p>

#### [ Scott Morrison (May 30 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279353):
<p>(Otherwise, the work is lost. Of course, indirect consequences of the work, such as inspiring people to think about interactive theorem proving through talks, may survive.)</p>

#### [ Scott Morrison (May 30 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279366):
<p>Not that I am doing this myself. But as soon as I have satisfactory resolution of handling universes in category theory (getting there?), next up should be a PR. :-)</p>

#### [ Kevin Buzzard (May 30 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279720):
<p>Johan Commelin suggests that I wait for you before defining more sheaves of things</p>

#### [ Kevin Buzzard (May 30 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279722):
<p>and perfectoid spaces have sheaves of topological rings...</p>

#### [ Johan Commelin (May 30 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127286907):
<p>But Johan Commelin is a layman, who doesn't know anything about proper writing of structures and interfaces. I guess he thinks you just use some abstract category theory imported from Scott's library, and then definitions become 1-liners. But he forgets that you will still need a lot of interface writing. And this interface writing may or may not become more complicated with the overhead of the category lib. Johan has no clue whether this is a good idea or not.</p>

#### [ Scott Morrison (May 30 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287077):
<p>I'm really sorry about being slow. I am feeling lame about not finishing real papers recently, and trying to get some non-Lean work done. Given the perfectoid spaces project is not immediately planning on contributing to mathlib (tsk) perhaps I could give you a relatively stable version of my category theory library to use as a dependency, and once (I mustn't say "if") I get it PR'd into mathlib it should be relatively easy to replumb.</p>

#### [ Johan Commelin (May 30 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287092):
<p>No worries. We all have other obligations as well (-;</p>

#### [ Johan Commelin (May 30 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287147):
<p>The thing is: I really am a layman. I have no clue whether you lib will allow us to write shorter code. Or whether we still need to write lots of plumbing stuff. I just don't have enough experience with formalisations to have good intuition about this.</p>

#### [ Johan Commelin (May 30 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287164):
<p>In maths you would say: "Look, Scott has written a book on category theory! Let's just refer to that, instead of writing a 50 page appendix ourselves. That will save us 50 pages!"</p>

#### [ Johan Commelin (May 30 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287166):
<p>But it seems like it might not work that way in Lean.</p>

#### [ Patrick Massot (May 30 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127293960):
<blockquote>
<p>Of course, indirect consequences of the work, such as inspiring people to think about interactive theorem proving through talks, may survive.</p>
</blockquote>
<p>Did you already gave talks about interactive theorem proving?</p>

#### [ Johan Commelin (Nov 22 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148191703):
<p>I tried to update my <code>simplicial</code> branch today: <a href="https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplicial_set.lean#L188" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplicial_set.lean#L188">https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplicial_set.lean#L188</a> is the proof that <code>boundary (boundary x) = 0</code>.</p>

#### [ Johan Commelin (Nov 22 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148191759):
<p>I do have some issues with <code>pmf.map f</code> where <code>f</code> is a function between two fintypes. This should be continuous for the subspace topology. And I had a working proof. But in the last months, the topology on <code>nnreal</code> has changed, using uniform spaces. Now my proof seems pretty broken.</p>

#### [ Johan Commelin (Nov 22 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148191764):
<p>If any of the uniform spaces wizards want to help me out there, that would be cool.</p>

#### [ Johan Commelin (Nov 22 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148192272):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I think that I would like to make use of all the machinery that you have developed in you homotopy repo. So I won't push this much further. At least now the files are somewhat up to date with mathlib again.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193784):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> So now I have a proof that</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">lboundary_lboundary</span> <span class="o">:</span> <span class="o">(</span><span class="n">lboundary</span> <span class="n">R</span> <span class="n">M</span> <span class="n">X</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">comp</span> <span class="o">(</span><span class="n">lboundary</span> <span class="n">R</span> <span class="n">M</span> <span class="n">X</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">boundary_boundary</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
</pre></div>


<p>Is there now an easy way to take homology? What is the <em>correct</em> way to do that?</p>

#### [ Reid Barton (Nov 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193785):
<p>Which machinery did you have in mind?</p>

#### [ Johan Commelin (Nov 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193787):
<p>Aah, the stuff about cylinders etc</p>

#### [ Reid Barton (Nov 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193788):
<p>Can we do a version for simplicial modules now?</p>

#### [ Johan Commelin (Nov 22 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193798):
<p>I do not have a working functor <code>Top</code> to <code>simplicial_set</code> yet. It is a bit annoying.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193800):
<p>But the other pieces are now becoming quite nice.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193859):
<p>Also, I guess I should call them simplicial types? And the category should be <code>sType</code>?</p>

#### [ Reid Barton (Nov 22 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193863):
<p>That is--this argument also works to show that the (unnormalized) chain complex associated to any simplicial module is in fact a chain complex. The original simplicial module doesn't have to be free.</p>

#### [ Reid Barton (Nov 22 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193867):
<p>I don't know whether that will make the proof any easier</p>

#### [ Reid Barton (Nov 22 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193881):
<p><a href="https://ncatlab.org/nlab/show/Moore+complex#ForSimplicialAbelianGroups" target="_blank" title="https://ncatlab.org/nlab/show/Moore+complex#ForSimplicialAbelianGroups">https://ncatlab.org/nlab/show/Moore+complex#ForSimplicialAbelianGroups</a></p>

#### [ Johan Commelin (Nov 22 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193886):
<p>Aaah, I don't know anything about this.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193928):
<p>Are you planning to PR parts of your project into mathlib in the near future?</p>

#### [ Reid Barton (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193942):
<p>Probably not the near future. It's more likely that I will do a "version 2.0" of some parts in the less near future.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193944):
<p>Aha</p>

#### [ Reid Barton (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193947):
<p>But, it depends on the part. Some stuff about Top could probably be PRed relatively soon without many changes</p>

#### [ Reid Barton (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193954):
<p>Let me see if I can read your proof</p>

#### [ Johan Commelin (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193955):
<p>It would be nice to have singular homology</p>

#### [ Reid Barton (Nov 22 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194000):
<p>I wrote out a plan for it in a comment on one of your earlier PRs</p>

#### [ Reid Barton (Nov 22 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194014):
<p>what's the story with the topological simplices functor?</p>

#### [ Reid Barton (Nov 22 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194017):
<p>Delta -&gt; Top</p>

#### [ Reid Barton (Nov 22 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194021):
<p>Something broke with it?</p>

#### [ Johan Commelin (Nov 22 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194023):
<p><a href="https://github.com/leanprover/mathlib/pull/144#issuecomment-425715546" target="_blank" title="https://github.com/leanprover/mathlib/pull/144#issuecomment-425715546">https://github.com/leanprover/mathlib/pull/144#issuecomment-425715546</a></p>

#### [ Johan Commelin (Nov 22 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194028):
<p>Yes, that's broken...</p>

#### [ Johan Commelin (Nov 22 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194081):
<p>And I didn't see an obvious fix. The topology on <code>pmf [n]</code> is now no longer a subspace topology of a Pi-topology. But a subspace of some uniform thing.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194086):
<p>And my uniform-fu is nil.</p>

#### [ Reid Barton (Nov 22 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194092):
<p>Technically we can do all this right now I think, without even waiting for limits or adjunctions</p>

#### [ Johan Commelin (Nov 22 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194140):
<p>Yes, apart from this stupid brokenness, all the other parts are mostly there.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194145):
<p>I didn't abstract complexes yet.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194275):
<p>Did you do complexes somewhere?</p>

#### [ Johan Commelin (Nov 22 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194277):
<p>I know that we had some discussion here on zulip a long time ago.</p>

#### [ Reid Barton (Nov 22 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194280):
<p>Not yet</p>

#### [ Johan Commelin (Nov 22 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194348):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Are you interested in exercising your mastery of uniform spaces again?</p>

#### [ Patrick Massot (Nov 22 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194403):
<p>I can try</p>

#### [ Patrick Massot (Nov 22 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194411):
<p>Did you already precisely described the problem? I didn't read carefully</p>

#### [ Patrick Massot (Nov 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194455):
<p>Is there something I could clone?</p>

#### [ Johan Commelin (Nov 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194458):
<p>Nope, there is a broken proof. It used to work, long ago. But then uniform spaces came along, and now it is broken.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194460):
<p><code>simplicial</code> branch on community mathlib</p>

#### [ Patrick Massot (Nov 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194462):
<p>did you push everything relevant to that branch?</p>

#### [ Johan Commelin (Nov 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194471):
<p><a href="https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/standard_topological_simplex.lean#L31" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/standard_topological_simplex.lean#L31">https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/standard_topological_simplex.lean#L31</a></p>

#### [ Johan Commelin (Nov 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194473):
<p>That might not be the exact statement that you want to prove...</p>

#### [ Johan Commelin (Nov 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194475):
<p>You could generalise to any <code>f : X → Y</code> where <code>X</code> and <code>Y</code> are fintypes.</p>

#### [ Johan Commelin (Nov 22 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194512):
<p>you get an induced map <code>pmf.map f</code></p>

#### [ Johan Commelin (Nov 22 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194519):
<p>And that should be continuous</p>

#### [ Johan Commelin (Nov 22 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194530):
<p>We will then apply this to monotone maps between <code>[n]</code> and <code>[m]</code></p>

#### [ Patrick Massot (Nov 22 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196152):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I investigate a bit. There isn't much uniform space here, only metric space. The seemingly missing lemma is:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">metric_pi_topology</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">π</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">metric_space</span> <span class="o">(</span><span class="n">π</span> <span class="n">a</span><span class="o">)]:</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">metric_space_pi</span> <span class="bp">_</span> <span class="n">π</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">to_uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="bp">=</span> <span class="bp">@</span><span class="k">Pi</span><span class="bp">.</span><span class="n">topological_space</span> <span class="bp">_</span> <span class="n">π</span> <span class="bp">_</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Patrick Massot (Nov 22 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196155):
<p>Which says the topology on a finite product of metric spaces is the product topology. It probably used to be rfl but isn't.</p>

#### [ Patrick Massot (Nov 22 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196167):
<p>After proving that lemma, typing:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">β</span><span class="o">]</span>

<span class="n">def</span> <span class="n">pmf_top</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">pmf</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">pmf_top</span>
<span class="kn">lemma</span> <span class="n">map</span><span class="bp">.</span><span class="n">cont</span>  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">continuous</span> <span class="o">(</span><span class="n">pmf</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">continuous_subtype_mk</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">metric_pi_topology</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">continuous_pi</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">j</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>should put you back on track</p>

#### [ Patrick Massot (Nov 22 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196212):
<p>because then <code>theorem map.continuous (f : [m] → [n]) : continuous (map f) := map.cont f</code></p>

#### [ Patrick Massot (Nov 22 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196266):
<p>It may be better to state a <code>continuous_metric_pi</code> with proof containing the <code>rw metric_pi_topology</code> which we'd rather keep hidden</p>

#### [ Patrick Massot (Nov 22 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196287):
<p>Clearly the definition <code>metric_space_pi</code> currently lacks proper API. <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> do you have opinons about that (you don't need to read anything before this monologue)?</p>

#### [ Reid Barton (Nov 23 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148201901):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I pushed an "exercise" for you, in <a href="https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplicial_module.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplicial_module.lean">https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplicial_module.lean</a></p>

#### [ Reid Barton (Nov 23 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148201905):
<p>It should be a proper subset of your existing <code>boundary_boundary</code> proof, I hope.</p>

#### [ Johan Commelin (Nov 23 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148209235):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Thanks a lot for investigating. I'll connect the pieces together now.</p>

#### [ Johan Commelin (Nov 23 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148209238):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Thanks! I'll take a look.</p>

#### [ Patrick Massot (Nov 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214146):
<p>Johan, are you working on this product topology vs product metric? Or do you need help?</p>

#### [ Johan Commelin (Nov 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214147):
<p>I just finished some bureaucracy. I'll look at it now</p>

#### [ Patrick Massot (Nov 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214150):
<p>It probably requires quite a bit of preparation if you want to do it right</p>

#### [ Patrick Massot (Nov 23 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214190):
<p>including figuring out what is already in mathlib</p>

#### [ Patrick Massot (Nov 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214196):
<p>stuff like the base of the product topology in terms of open subsets in the factors, maybe some congr lemma for topologies, balls in the product metric space is products of balls etc.</p>

#### [ Patrick Massot (Nov 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214208):
<p>maybe also things like projection on factors is an open map</p>

#### [ Johan Commelin (Nov 23 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214276):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Why do your fintypes have such strange names? Did you give up on <code>X</code> and <code>Y</code>?</p>

#### [ Patrick Massot (Nov 23 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214345):
<p>I copied and pasted too much. The idea of using π in <code>{π : α → Type*} [fintype α] [∀ a, metric_space (π a)]</code> is also a nightmare, since there are Pi-type mixed with π map everywhere then</p>

#### [ Johan Commelin (Nov 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215270):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Ok, my proof works again, modulo the lemma. It is a bit scary (in the sense of <em>unmathematical</em>) to do rewrites that don't change the pretty printed goal. But I guess it is fine.</p>

#### [ Patrick Massot (Nov 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215286):
<p>Which lemma? <code>metric_pi_topology</code>?</p>

#### [ Johan Commelin (Nov 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215369):
<p>Right, that one.</p>

#### [ Johan Commelin (Nov 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215412):
<p>I need to dive into mathlib to figure out how to prove that...</p>

#### [ Patrick Massot (Nov 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215415):
<p>Do you want me to try proving it?</p>

#### [ Patrick Massot (Nov 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215426):
<p>I'd rather have you work on sheaves or that localization API hole</p>

#### [ Johan Commelin (Nov 23 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215517):
<p>Yeah, I should stop again with this project. I needed to do something else than sheaves for a day. But now I should return.</p>

#### [ Johan Commelin (Nov 23 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215526):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> How did Lean figure out that your definition of <code>boundary</code> is a linear map?! That's really slick!</p>

#### [ Johan Commelin (Nov 23 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215533):
<p>Kudos to <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Johan Commelin (Nov 23 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215581):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">simplicial_module</span> <span class="o">:=</span> <span class="n">simplicial_object</span> <span class="o">(</span><span class="n">RMod</span> <span class="n">R</span><span class="o">)</span>

<span class="kn">section</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">simplicial_module</span> <span class="n">R</span><span class="o">)</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span> <span class="o">[</span><span class="bp">`</span><span class="n">n</span><span class="bp">`</span><span class="o">]</span> <span class="bp">`</span> <span class="o">:=</span> <span class="n">simplex_category</span><span class="bp">.</span><span class="n">from_nat</span> <span class="n">n</span>

<span class="n">def</span> <span class="n">boundary</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span><span class="bp">.</span><span class="n">obj</span> <span class="o">[</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">]</span> <span class="err">⟶</span> <span class="n">X</span><span class="bp">.</span><span class="n">obj</span> <span class="o">[</span><span class="n">n</span><span class="o">]</span> <span class="o">:=</span>
<span class="n">sum</span> <span class="n">univ</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">],</span> <span class="n">gsmul</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span><span class="err">^</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">(</span><span class="n">X</span><span class="bp">.</span><span class="n">δ</span> <span class="n">i</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Nov 23 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215584):
<p>I don't know what you are talking about but I'm happy to take credit</p>

#### [ Johan Commelin (Nov 23 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215585):
<p>That's so concise! You'dd almost call it normal math.</p>

#### [ Johan Commelin (Nov 23 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215595):
<p><code>boundary</code> is a map between to modules. And there you have it.</p>

#### [ Johan Commelin (Nov 23 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215603):
<p>The only difference from regular math is pretty printing</p>

#### [ Johan Commelin (Nov 23 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215665):
<p>It's using the fact that <code>linear_map</code> is a group. It is really nice that this <em>Just Works™</em></p>

#### [ Johan Commelin (Nov 23 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215829):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Did you also prove that composition of linear maps is bilinear?</p>

#### [ Mario Carneiro (Nov 23 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215832):
<p>yeah, that's <code>lcomp</code> or <code>llcomp</code></p>

#### [ Johan Commelin (Nov 23 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215833):
<p>Otherwise that would be a natural step in <span class="user-mention" data-user-id="110032">@Reid Barton</span>s challenge.</p>

#### [ Johan Commelin (Nov 23 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215838):
<p>Ok, cool.</p>

#### [ Mario Carneiro (Nov 23 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215879):
<p>llcomp is linear in all the ways</p>

#### [ Reid Barton (Nov 23 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148232028):
<p>btw, <code> : ℤ</code> isn't necessary there</p>

#### [ Reid Barton (Nov 23 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148232113):
<p>And yes, I was pretty happy about how easy it was to write down this statement. Now let's see how the proof turns out :)</p>

#### [ Johan Commelin (Nov 23 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148233797):
<p>Yes, I think that we need to change the definition of composition to <code>llcomp g f</code>. After that, there is <code>map_sum</code> for <code>linear_map</code>s. If that works, I think we are good to go. I'll try it when I'm home.</p>

#### [ Johan Commelin (Nov 23 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148236827):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Sadly, this gives a failure</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">RMod_category</span> <span class="o">:</span> <span class="n">category</span> <span class="o">(</span><span class="n">RMod</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">M</span> <span class="n">N</span><span class="o">,</span> <span class="n">M</span> <span class="bp">→</span><span class="err">ₗ</span> <span class="n">N</span><span class="o">,</span>
  <span class="n">id</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">M</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">id</span><span class="o">,</span>
  <span class="n">comp</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">M</span> <span class="n">N</span> <span class="n">P</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="n">linear_map</span><span class="bp">.</span><span class="n">llcomp</span> <span class="n">M</span> <span class="n">N</span> <span class="n">P</span> <span class="n">g</span> <span class="n">f</span> <span class="o">}</span>
</pre></div>


<p>Once again, Lean can not find the ring over which <code>M</code> is a module...</p>

#### [ Reid Barton (Nov 23 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148236903):
<p>I'm confused, why are you trying to use <code>llcomp</code>?</p>

#### [ Johan Commelin (Nov 23 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237005):
<p>Because then I can pull <code>sum</code> through the linear map that is composition.</p>

#### [ Reid Barton (Nov 23 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237097):
<p>I see. So in the level of generality that I picked (RMod for a not necessarily commutative ring), the homs are only abelian groups, not modules. Of course, this is still enough but we have to use this additivity somehow</p>

#### [ Johan Commelin (Nov 23 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237106):
<p>Aah, yes, I changed <code>R</code> to <code>comm_ring</code>, but that is not the problem I think.</p>

#### [ Johan Commelin (Nov 23 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237115):
<p>It is still maxing out on some typeclass search</p>

#### [ Reid Barton (Nov 23 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237119):
<p>Well, there is no reason it should not work for <code>ring</code> as well, or any additive category even</p>

#### [ Johan Commelin (Nov 23 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237192):
<p>Sure, but we don't have enriched categories etc</p>

#### [ Reid Barton (Nov 23 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237198):
<p>what about just proving the equality element-wise?</p>

#### [ Reid Barton (Nov 23 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237205):
<p>Well, in any case, <code>comp</code> cannot be <code>llcomp</code>, because it has the wrong type. Right?</p>

#### [ Johan Commelin (Nov 23 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237219):
<p><code>llcomp g f</code> should be an element of <code>linear_map M P</code></p>

#### [ Reid Barton (Nov 23 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237276):
<p>Or, sorry</p>

#### [ Johan Commelin (Nov 23 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237279):
<p>because <code>llcomp</code> is cast to a function that eats <code>g</code>, etc...</p>

#### [ Reid Barton (Nov 23 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237284):
<p>So how can <code>llcomp</code> help</p>

#### [ Johan Commelin (Nov 23 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237297):
<p><code>llcomp boundary</code> is a linear map</p>

#### [ Reid Barton (Nov 23 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237322):
<p>is the idea to get an expression containing a coercion of <code>llcomp</code>, so that some lemma can see it's linear?</p>

#### [ Reid Barton (Nov 23 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237392):
<p>This sounds kind of fragile to me</p>

#### [ Johan Commelin (Nov 23 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237410):
<p>why?</p>

#### [ Reid Barton (Nov 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237429):
<p>It just does?</p>

#### [ Reid Barton (Nov 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237431):
<p>Easy to imagine the simplifier deciding to rewrite <code>llcomp f g</code> to <code>lcomp f g</code> or whatever</p>

#### [ Reid Barton (Nov 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237433):
<p>and then you're stuck</p>

#### [ Johan Commelin (Nov 23 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237488):
<p>That would be <code>lcomp g f</code> because of [see above]</p>

#### [ Johan Commelin (Nov 23 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237490):
<p>Anyway, I'm sidetracking.</p>

#### [ Johan Commelin (Nov 23 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237499):
<p>Ok, I'll just <code>change</code> to the <code>llcomp</code> expression inside my proof.</p>

#### [ Reid Barton (Nov 23 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237843):
<p>What lemma are you using to pull the sum through the composition?</p>

#### [ Johan Commelin (Nov 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237918):
<p><code>algebra/module.lean:@[simp] lemma map_sum</code></p>

#### [ Johan Commelin (Nov 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237921):
<p>That was my plan, at least.</p>

#### [ Reid Barton (Nov 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237987):
<p>I see</p>

#### [ Reid Barton (Nov 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237989):
<p>hmm</p>

#### [ Reid Barton (Nov 23 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148238375):
<p>Maybe it's better to make lemmas like <code>sum_comp</code>/<code>comp_sum</code> phrased in terms of the category composition and then write the proof in terms of those</p>

#### [ Johan Commelin (Nov 23 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148243762):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">class</span><span class="bp">.</span><span class="n">instance_max_depth</span> <span class="mi">100</span>
</pre></div>


<p>I found this at the top of the <code>tensor_product</code> file. That was why the <code>llcomp</code> stuff wasn't working (<span class="user-mention" data-user-id="110032">@Reid Barton</span>)<br>
Seems a bit fragile indeed...</p>

#### [ Johan Commelin (Nov 23 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148244765):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I just pushed some stuff. I can indeed copy most of my previous proof. I need one more little simp-lemma near the end. But I now need to do some other stuff first...</p>

#### [ Johan Commelin (Nov 23 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248147):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Done.</p>

#### [ Reid Barton (Nov 23 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248153):
<p>I just did it too :)</p>

#### [ Johan Commelin (Nov 23 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248159):
<p>Ooh, sorry...</p>

#### [ Johan Commelin (Nov 23 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248162):
<p>Are our proofs homotopic?</p>

#### [ Johan Commelin (Nov 23 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248163):
<p>Oooh, wait... this isn't HoTT</p>

#### [ Reid Barton (Nov 23 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248232):
<p>They're pretty similar</p>

#### [ Reid Barton (Nov 23 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248350):
<p>I added a bunch of lemmas for bilinearity of composition (without proofs)<br>
<a href="https://github.com/leanprover-community/mathlib/blob/simplicial2/category_theory/examples/modules.lean#L35" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/simplicial2/category_theory/examples/modules.lean#L35">https://github.com/leanprover-community/mathlib/blob/simplicial2/category_theory/examples/modules.lean#L35</a></p>

#### [ Johan Commelin (Nov 23 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248469):
<p>Ok, now I should really get back to sheaves</p>

#### [ Johan Commelin (Nov 23 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248476):
<p>But I'm a bit stuck there...</p>


{% endraw %}
