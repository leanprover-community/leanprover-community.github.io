---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64461unexpectedfunextreflbehaviour.html
---

## Stream: [general](index.html)
### Topic: [unexpected funext / refl behaviour](64461unexpectedfunextreflbehaviour.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 11 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946494):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">universes</span> <span class="n">true</span> <span class="c1">-- might help</span>
<span class="kn">example</span> <span class="o">:</span> <span class="c1">-- phenomenon won&#39;t occur if you replace this with theorem T!</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">,</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">),</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">funext</span><span class="o">,</span> <span class="c1">-- only pulls off X, possibly because of universe issues</span>
  <span class="c1">-- two failed attempts to pull off f now:</span>
  <span class="c1">-- funext, -- does nothing</span>
  <span class="c1">-- apply funext, -- fails to unify</span>
  <span class="n">refine</span> <span class="n">funext</span> <span class="bp">_</span><span class="o">,</span> <span class="c1">-- Type of X now Sort (imax ? ?) and a type mismatch error reported **but goal changes anyway**</span>
  <span class="n">intro</span> <span class="n">f</span><span class="o">,</span>
  <span class="c1">-- goal now f = f</span>
  <span class="c1">-- refl, -- doesn&#39;t work! Fails to unify.</span>
  <span class="n">exact</span> <span class="n">rfl</span><span class="o">,</span> <span class="c1">-- does work</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946536):
<p>I am pleased to have confused tactic mode so much that <code>refl</code> won't work but <code>exact rfl</code> will.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946548):
<p>I am not sure if my goal is true, as the sorts may or may not be in different universes initially. However the funext tactic seems to buy it, although after pulling off the X it gets confused and won't pull off the <code>f</code>.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946563):
<p><code>apply f</code> won't do it but I seem to be able to explicitly do it with <code>refine funext _</code> although now Lean is in a funny state -- the refine tactic does appear to do something, but reports an error anyway.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946610):
<p>replacing <code>example</code> with <code>theorem T</code> makes all the problems go away, which is to me very surprising behaviour.</p>

#### [ Patrick Massot (Apr 11 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946682):
<p>This Lean 3 is all broken. Let's have Lean 4.</p>

#### [ Patrick Massot (Apr 11 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946695):
<p>(and hope Kevin stops trying to break everything)</p>

#### [ Chris Hughes (Apr 11 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946760):
<p>Isn't it just because your X's are in different universes. And then if you put them in the same universe, it fails because the funext tactic gets rid of both lambdas.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946857):
<p>I agree that if you put them in the same universe, all is well.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946864):
<p>But if you leave them in different universes, Lean ends up in a weird state.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946940):
<p>After the intro f, you have a goal <code>f = f</code> which refl won't close</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946953):
<p>but <code>exact rfl</code> will. However we are now passed a red squiggly line and I am not too sure how seriously to take Lean.</p>

#### [ Chris Hughes (Apr 11 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946954):
<p>I'm beginning to see the problem. Is it something to do with, it let's you do funext the first time, so if you can prove their equal, it will deduce the universes are the same. So your proposition is a bit like an heq?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124946958):
<p>I was wondering if there was some implicit unification going on</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947005):
<p>Also it was very strange to see a line in tactic mode fail and yet see the goal change.</p>

#### [ Patrick Massot (Apr 11 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947019):
<p>Looks a bit in the same spirit as your most recent issue on Lean github</p>

#### [ Chris Hughes (Apr 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947028):
<p>And it automatically lifts the functions to a different universe to be able to state that they're equal.</p>

#### [ Patrick Massot (Apr 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947033):
<p>Lean somehow fails to notice it's failing</p>

#### [ Chris Hughes (Apr 11 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947109):
<p>Haven't ever done anything that really tests the universe system so I don't really know.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/124947173):
<p>I just started playing with it recently. I'm just trying to get the hang of it :-)</p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162334):
<p>I know there's something strange going on here but I've not explained it very well. How about this</p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162336):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">,</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">),</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">funext</span><span class="o">,</span> <span class="c1">-- it&#39;s not very effective</span>
  <span class="n">refine</span> <span class="bp">@</span><span class="n">funext</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="c1">-- back on track</span>
  <span class="n">intro</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">refl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 16 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162338):
<p>That works fine.</p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162340):
<p>But now let me change <code>example</code> to <code>theorem strange</code>:</p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162390):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">strange</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">,</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">),</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">funext</span><span class="o">,</span> <span class="c1">-- it&#39;s super effective!</span>
  <span class="n">refine</span> <span class="bp">@</span><span class="n">funext</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="c1">-- invalid type ascription</span>
  <span class="n">intro</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">refl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162393):
<p>The proof no longer typechecks if I name the theorem</p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162398):
<p>because the behaviour of <code>funext</code> changes now the theorem has a name</p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162401):
<p>That's not right, is it?</p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162462):
<p>I think this has something to do with screwy universes</p>

#### [ Johannes Hölzl (Apr 16 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162620):
<p>Yes, it could be related to the fact that <code>example</code> (compared to <code>theorem</code>) does allow meta (universe) variables in its statement. So the type is not fully elaborated, it gets fully elaborated together with the value like <code>def</code>. So maybe <code>funext</code> has a problem with instantiating them.</p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162747):
<p>Oh yes! If I set <code>pp.universes true</code> then I see that in the <code>theorem</code> the goal has <code>(X : Sort u_1)</code></p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125162780):
<p>but in the <code>example</code> it has <code>(X : Sort ?l_1)</code></p>

#### [ Kevin Buzzard (Apr 16 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125163009):
<p>I see, so <code>definition strange</code> fixes the problem :-)</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166006):
<p>here's some possibly related weird behaviour:</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166023):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="o">,</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">X</span><span class="o">),</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">funext</span><span class="o">,</span>
  <span class="n">refine</span> <span class="n">funext</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">f</span><span class="o">,</span>
  <span class="c1">-- this proof isn&#39;t finished yet</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166031):
<p>the goal now is <code>f = f</code></p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166037):
<p>(at the point where the proof is not finished)</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166041):
<p>or with <code>pp.all</code> on</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166054):
<p><code>⊢ @eq.{?l_2} (X → X) f f</code></p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166066):
<p>and the red squiggle is under <code>end</code></p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166073):
<p>because we wrote end before the proof was complete</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166079):
<p>However if we write <code>admit</code> to finish the proof</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166087):
<p>we get a new red squiggle</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166137):
<p>on the second funext :-)</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166149):
<p>Maybe the universe unification or whatever only takes place after the admit, and then Lean decides something was wrong all along</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166164):
<p>I guess this is the price I pay for the silly <code>Sort*</code> choices I made earlier</p>

#### [ Kevin Buzzard (Apr 16 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125166182):
<p>changing <code>example</code> to <code>theorem T</code> gives me the red squiggle on the second funext immediately</p>

#### [ Chris Hughes (Apr 16 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unexpected%20funext%20/%20refl%20behaviour/near/125168260):
<p>I think it might be because the proof could give a clue about universes, but not if the proof is admit.</p>


{% endraw %}
