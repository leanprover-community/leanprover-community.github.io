---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84549idlytryingsoftwarefoundations.html
---

## Stream: [general](index.html)
### Topic: [idly trying software foundations](84549idlytryingsoftwarefoundations.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 27 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286568):
<p>I am working through software foundations. I'm finding the first book relatively straightforward, which is a relief. I was trying to do the exercises in a golf-like way. Why doesn't this work:</p>

#### [ Kevin Buzzard (Mar 27 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286609):
<div class="codehilite"><pre><span></span>inductive  ev : nat →  Prop
| ev_0 : ev 0
| ev_SS : ∀ n : nat, ev n → ev (n+2)
open ev
</pre></div>

#### [ Kevin Buzzard (Mar 27 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286615):
<p><code>theorem  ev_plus4 : ∀ n, ev n → ev (n +  4) :=  λ _ _,ev_SS _ (ev_SS _ _)</code></p>

#### [ Kevin Buzzard (Mar 27 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286618):
<p>I thought there was every chance :-)</p>

#### [ Kevin Buzzard (Mar 27 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286636):
<p>but I get</p>

#### [ Kevin Buzzard (Mar 27 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286637):
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
_x : ℕ,
_x : ev _x
⊢ ev _x
</pre></div>

#### [ Kenny Lau (Mar 27 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124286973):
<p>what is software foundations?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287015):
<p>a book on the web</p>

#### [ Kevin Buzzard (Mar 27 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287019):
<p><a href="https://softwarefoundations.cis.upenn.edu/" target="_blank" title="https://softwarefoundations.cis.upenn.edu/">https://softwarefoundations.cis.upenn.edu/</a></p>

#### [ Kevin Buzzard (Mar 27 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287026):
<p>They have exercises like this:</p>

#### [ Gabriel Ebner (Mar 27 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287030):
<p>You need to plug in the assumption for <code>ev n</code> somewhere.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287035):
<div class="codehilite"><pre><span></span>definition  double (n : ℕ) := n + n
theorem  ev_double (n : ℕ) : ev (double n) := nat.rec_on n ev_0
(λ n H, have (n+1)+(n+1)=n+n+2,by simp,show ev((n+1)+(n+1)),by {rw this;exact ev_SS _ H})
</pre></div>

#### [ Kevin Buzzard (Mar 27 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287047):
<p>I wanted the elaborator to guess where. I have it as an underscore</p>

#### [ Gabriel Ebner (Mar 27 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287102):
<p>The underscores won't find it because it is not determined by unification.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287111):
<p>I know that <code>theorem  ev_plus4 : ∀ n, ev n → ev (n +  4) :=  λ _ H,ev_SS _ (ev_SS _ H)</code> works but I...basically I am trying to get a feeling for what I can get away with with underscores</p>

#### [ Kenny Lau (Mar 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287122):
<p>it's the same reason <code> #check  λ n : nat, (rfl : _ +  4  = (_ +  2) +  2) </code> fails, I think</p>

#### [ Kenny Lau (Mar 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287124):
<p>(obviously it's <code>n</code>!!)</p>

#### [ Gabriel Ebner (Mar 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287129):
<p>It could also be 0, or 1, or...</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287133):
<p>Or <code>n!!</code> <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287178):
<p>but <code>#check  λ n : nat, (rfl : _ +  4  = (_ +  4))</code> works...</p>

#### [ Gabriel Ebner (Mar 27 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287191):
<p>But I hope you get a metavariable and not n, right?</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287199):
<p>Yes, because check allows unsolved metavars. Otherwise <code>#check f</code> where f takes implicit parameters would be pretty useless.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287278):
<p>ha ha</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287283):
<p><code>#check (rfl : _ = _ +  0)</code></p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287290):
<p>didn't give what I expected</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287304):
<p>but probably did give what everyone else expected.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287415):
<blockquote>
<p>The underscores won't find it because it is not determined by unification.</p>
</blockquote>
<p>unification says "this should be a proof of ev _x", and there is something in the local context which is a proof of ev _x</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287449):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> my proof of ev_double is lame. Can you do better?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287472):
<p>This one surely qualifies for the "this is mathematically obvious so it doesn't matter how obscure the proof is, just make it short"</p>

#### [ Patrick Massot (Mar 27 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287521):
<blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> my proof of ev_double is lame. Can you do better?</p>
</blockquote>
<p>I should do that with my PhD student, and see what comes out of it.</p>

#### [ Kenny Lau (Mar 27 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287523):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  "of course it's even, you just doubled it!"</p>

#### [ Patrick Massot (Mar 27 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287533):
<p>I mean asking about real proofs</p>

#### [ Kenny Lau (Mar 27 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287541):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> are you aiming for length?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287589):
<p>brevity</p>

#### [ Patrick Massot (Mar 27 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287618):
<p>By the way, we have a new nice example of a real world theorem built purely on trusting the big guys in the field: <a href="https://arxiv.org/abs/1803.07997" target="_blank" title="https://arxiv.org/abs/1803.07997">https://arxiv.org/abs/1803.07997</a> There are three ingredients: one was announced in 2001 and never written. One has a draft written in 2012 but the author doesn't want to make it into a publishable paper. The third one is published but none of the experts except the author understand the proof.</p>

#### [ Patrick Massot (Mar 27 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287682):
<p>One day, proof assistants will change all that</p>

#### [ Kenny Lau (Mar 27 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287685):
<div class="codehilite"><pre><span></span>theorem  ev_double : ∀ (n : ℕ), ev (double n)
| 0  := ev_0
| (n+1) := (by simp [double] : double n +  2  = double (n+1)) ▸ ev_SS _ (ev_double n)
</pre></div>

#### [ Kenny Lau (Mar 27 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287687):
<p>how is this?</p>

#### [ Kenny Lau (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287704):
<p>we all know there's so many things we need to do</p>

#### [ Kenny Lau (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287705):
<p>we need to prove the equality somehow</p>

#### [ Kenny Lau (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287707):
<p>and we need to use recursion</p>

#### [ Chris Hughes (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287713):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span>  <span class="n">ev_double</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ev</span> <span class="o">(</span><span class="mi">2</span>  <span class="bp">*</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="n">ev</span><span class="bp">.</span><span class="n">ev_0</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="n">hi</span><span class="o">,</span> <span class="n">ev_SS</span> <span class="bp">_</span> <span class="n">hi</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Mar 27 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287719):
<p>well</p>

#### [ Patrick Massot (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287764):
<p>Johannes has a bad influence on Chris</p>

#### [ Kenny Lau (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287771):
<p>changing the definition of <code>double</code> is called cheating :P</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287774):
<p>I see an unused eta contraction</p>

#### [ Chris Hughes (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287779):
<p>What's the definition of double?</p>

#### [ Kenny Lau (Mar 27 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287783):
<p><code> definition  double (n : ℕ) := n + n</code></p>

#### [ Kenny Lau (Mar 27 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124287804):
<p>and by eta contraction he means</p>
<div class="codehilite"><pre><span></span>lemma ev_double (n : ℕ) : ev (2  * n) :=
nat.rec_on n ev.ev_0 (λ n, ev_SS _)
</pre></div>

#### [ Chris Hughes (Mar 27 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288271):
<p>My best attempt for double. I saved three characters by using <code>rec</code> instead of <code>rec_on</code></p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span>  <span class="n">ev_double</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ev</span> <span class="o">(</span><span class="n">double</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec</span> <span class="n">ev_0</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="n">h</span><span class="o">,</span> <span class="k">show</span> <span class="n">ev</span> <span class="o">(</span><span class="bp">_</span> <span class="bp">+</span> <span class="bp">_</span><span class="o">),</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">succ_add</span><span class="bp">;</span> <span class="k">from</span> <span class="n">ev_SS</span> <span class="bp">_</span> <span class="n">h</span><span class="o">)</span> <span class="n">n</span>
</pre></div>

#### [ Kenny Lau (Mar 27 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288275):
<p>do we count brevity by characters?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288283):
<p>or by tokens</p>

#### [ Kenny Lau (Mar 27 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288286):
<p>this is ridiculous</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288319):
<p>or by file size</p>

#### [ Kenny Lau (Mar 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288333):
<p>if your goal is to save time, you should stick with what you have</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288334):
<p>(so then probably fancy unicode characters cost more)</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288353):
<p>and he opened nat! Is that allowed? you have to put <code>nat.succ_add</code></p>

#### [ Chris Hughes (Mar 27 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288408):
<p>I think there should be bonus points for term style. I would have used eq.subst but it was longer.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288508):
<p>I don't understand the syntax of Chris' answer! What is this ; from business? I've only ever seen ; in tactic mode.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288520):
<p>oh we are in tactic mode?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288525):
<p>Then my question is "what is this from in tactic mode?"</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288572):
<p>and now I hover over it and find out.</p>

#### [ Chris Hughes (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288575):
<p>You can use from instead of exact, if you want to save one character.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288581):
<p>I think that's the main reason they put it in.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288590):
<p>Chris do you know about pyth? (as in "pithy")</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288591):
<p><a href="https://esolangs.org/wiki/Pyth" target="_blank" title="https://esolangs.org/wiki/Pyth">https://esolangs.org/wiki/Pyth</a></p>

#### [ Kenny Lau (Mar 27 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288595):
<p>you bunch are ridiculous</p>

#### [ Kenny Lau (Mar 27 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288603):
<p>ok to be fair I use pyth when I need to compute something quickly</p>

#### [ Kenny Lau (Mar 27 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288610):
<p>and it's far more convenient than other programming languages</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288663):
<p>ha ha "you bunch are ridiculous" "actually I use it IRL"</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288670):
<p>The <code>;</code> there is actually in tactic mode</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288676):
<p>yes it all dawned on me later</p>

#### [ Kenny Lau (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288680):
<p>wait what?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288681):
<p>I hadn't seen from in tactic mode before</p>

#### [ Kenny Lau (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288695):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> he's saying that <code>;</code> itself is in tactic mode</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288697):
<p>it's just so you can write <code>have x, from y</code> in tactic mode</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288700):
<p>I think we need "coz"</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288702):
<p>which is from but one fewer letter</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288709):
<p>I'll file an issue</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288726):
<p>I prefer <code>exact</code> over <code>from</code> when it's not used after <code>show</code>, <code>have</code>, <code>suffices</code> or <code>let</code> tactics</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288778):
<p>As for the golfing, I won't enter the ring. I'd emphasize good lemmas in this instance so you can write each individual theorem very concisely</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288843):
<p>Aah I see. Perhaps double n = n * 2 or 2 * n would be worth proving before we launch into trying to prove stuff like this</p>

#### [ Patrick Massot (Mar 27 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288849):
<p>I hope the new parser will allow Kevin to define <code>coz</code> by adding one line near the top of his file</p>

#### [ Patrick Massot (Mar 27 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288871):
<p>Do code-golf belong to the target of "domain specific language handling"?</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288932):
<p>You can define <code>coz</code> in one line today</p>

#### [ Kenny Lau (Mar 27 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288935):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I've been a member of PPCG for 3 years</p>

#### [ Kenny Lau (Mar 27 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288936):
<p>the people in the chat know me</p>

#### [ Mario Carneiro (Mar 27 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288953):
<div class="codehilite"><pre><span></span>meta def tactic.interactive.coz := tactic.interactive.from
</pre></div>

#### [ Patrick Massot (Mar 27 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288975):
<p><em>message stared</em></p>

#### [ Kenny Lau (Mar 27 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124288983):
<p>lol</p>

#### [ Kenny Lau (Mar 27 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289032):
<p>and a solution a la Mario:</p>
<div class="codehilite"><pre><span></span>lemma  double.aux (n : ℕ) : double (n+1) = double n +  2  :=
nat.succ_add _ _

lemma ev_double (n : ℕ) : ev (double n) :=
nat.rec ev_0 (λ n h, (double.aux n).symm ▸ ev_SS _ h) n
</pre></div>

#### [ Kevin Buzzard (Mar 27 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289273):
<blockquote>
<p>By the way, we have a new nice example of a real world theorem built purely on trusting the big guys in the field: <a href="https://arxiv.org/abs/1803.07997" target="_blank" title="https://arxiv.org/abs/1803.07997">https://arxiv.org/abs/1803.07997</a> There are three ingredients: one was announced in 2001 and never written. One has a draft written in 2012 but the author doesn't want to make it into a publishable paper. The third one is published but none of the experts except the author understand the proof.</p>
</blockquote>
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> as long as the experts are happy, we're all happy, right?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289337):
<p>I would be most concerned about the third assumption I guess.</p>

#### [ Patrick Massot (Mar 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289340):
<p>Right. But there are not all happy about the third ingredient.</p>

#### [ Patrick Massot (Mar 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289351):
<p>Because the third ingredient was proved by an obscure polish mathematician</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289357):
<p>so you'll have to hope that the referees are either optimists or lazy</p>

#### [ Patrick Massot (Mar 27 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289375):
<p>Who didn't even get the Crafoord prize.</p>

#### [ Patrick Massot (Mar 27 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289447):
<p>We have two more elaborate plans actually. First we'd like to try to read the Polish proof. And we have a backup plan which is to use an earlier weaker result (about <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>C</mi><mi>r</mi></msup></mrow><annotation encoding="application/x-tex">C^r</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.02778em;">r</span></span></span></span></span></span></span></span></span></span></span> diffeomorphisms, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>r</mi><mo>≤</mo><mn>1</mn><mo>+</mo><mi>dim</mi><mo>(</mo><mi>V</mi><mo>)</mo><mi mathvariant="normal">/</mi><mn>2</mn></mrow><annotation encoding="application/x-tex">r \leq 1+\dim(V)/2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="mrel">≤</span><span class="mord mathrm">1</span><span class="mbin">+</span><span class="mop">dim</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.22222em;">V</span><span class="mclose">)</span><span class="mord mathrm">/</span><span class="mord mathrm">2</span></span></span></span>) to get a correspondingly weaker (but still new) result</p>

#### [ Patrick Massot (Mar 27 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289474):
<p>How do you get LaTeX rendering on this website?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289523):
<p>two $s</p>

#### [ Patrick Massot (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289529):
<p>weird</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289531):
<p>ooh Coq has an inversion tactic</p>

#### [ Patrick Massot (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289535):
<p>inverting what?</p>

#### [ Kenny Lau (Mar 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289536):
<p>is there a subversion tactic?</p>

#### [ Patrick Massot (Mar 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289545):
<p>nooo subversion is dead</p>

#### [ Patrick Massot (Mar 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289553):
<p>all cool kids use git nowadays</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289557):
<div class="codehilite"><pre><span></span>Theorem evSS_ev : ∀ n,
  ev (S (S n)) → ev n.
Proof.
  intros n E.
  inversion E as [| n&#39; E&#39;].
  (* We are in the E = ev_SS n&#39; E&#39; case now. *)
  apply E&#39;.
Qed.
</pre></div>

#### [ Kevin Buzzard (Mar 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289618):
<p>induction n would not go down well here</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289625):
<p>Coq knows that the only way to prove ev (S S n) is to prove ev n and deduce ev (S S n)</p>

#### [ Kenny Lau (Mar 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289721):
<p>is this the same as coinduction?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289727):
<p>The question in full:</p>

#### [ Kevin Buzzard (Mar 27 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289736):
<div class="codehilite"><pre><span></span>inductive  ev : nat →  Prop
| ev_0 : ev 0
| ev_SS : ∀ n : nat, ev n → ev (n+2)

open ev

example : ∀ n, ev (n+2) → ev n :=  sorry
</pre></div>

#### [ Kevin Buzzard (Mar 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289957):
<p>oh no way, intros n H, cases H works!</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289966):
<p>Yay, we have an inversion tactic!</p>

#### [ Patrick Massot (Mar 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289980):
<p>I still don't understand what this inversion tactic is meant to do.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289984):
<div class="codehilite"><pre><span></span>example : ¬ (ev 1) :=  begin
intro H,
cases H,
end
</pre></div>

#### [ Patrick Massot (Mar 27 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124289987):
<p>(but I'm writing lecture notes on convex integration without integration in parallel of reading Zulip)</p>

#### [ Kenny Lau (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290030):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I have a solution: do you want to see it?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290031):
<p>inversion says "You are assuming ev (n+2) and the only way to prove this would be by proving ev(n) and tehen applying ev_SS</p>

#### [ Kenny Lau (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290037):
<p>btw what you call "inversion" is just induction on the inductive predicate "ev"</p>

#### [ Kenny Lau (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290045):
<p>(it's called <code>inductive</code> because you can do <code>induction</code>)</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290047):
<p>it's what software foundations calls inversion</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290129):
<p>"rule inversion" is what computer scientists say when they mean "case analysis"</p>

#### [ Kenny Lau (Mar 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290139):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> for a second I thought this is something Lean doesn't have</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290140):
<p>(well, it's specific to inductive definitions usually)</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290152):
<p>So did I, that's why I mentioned it here</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290244):
<p>case (hah) in point</p>
<div class="codehilite"><pre><span></span>example : ∀ n, ev (n+2) → ev n
| n (ev_SS _ h) := h
</pre></div>

#### [ Patrick Massot (Mar 27 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290266):
<p>Kevin and Kenny, have you managed to prove an affine scheme is a scheme?</p>

#### [ Kenny Lau (Mar 27 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290273):
<p>if we're allowed to assume <code>false</code>, then we've proved it</p>

#### [ Kenny Lau (Mar 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290323):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> hmm, I still have much to learn</p>

#### [ Kenny Lau (Mar 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290326):
<p>you gave a 2-line solution</p>

#### [ Kenny Lau (Mar 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290328):
<p>mine had 10 lines</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290333):
<p>I considered formatting it as one line</p>

#### [ Kenny Lau (Mar 27 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290711):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> do you have a link?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290779):
<p>For schemes? I think we're in the wrong topic. We are plenty of lemmas short of proving that an affine scheme is a scheme.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290787):
<p>Tom Hales told me he was going to mention it in his talk at AITP today</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290788):
<p>so Kenny and I and Chris were hard at work trying to get it done</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290796):
<p>and then Tom broke his toe and couldn't go to the conference :-/</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290799):
<p>so I decided to leave the undergraduates alone so they can revise for their exams!</p>

#### [ Kenny Lau (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290804):
<p>as if they would really do so</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290806):
<p>Are you not revising mechanics?</p>

#### [ Kenny Lau (Mar 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290850):
<p>I'm building the function X -&gt; T</p>

#### [ Patrick Massot (Mar 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290851):
<p>There are not revising and you are code golfing...</p>

#### [ Patrick Massot (Mar 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290852):
<p>Go back to schemes!</p>

#### [ Patrick Massot (Mar 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290853):
<p><span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290874):
<blockquote>
<p>Are you not revising mechanics</p>
</blockquote>

#### [ Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290876):
<p>Let's look at my latest test scores</p>

#### [ Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290882):
<p>M1M2 100%</p>

#### [ Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290885):
<p>M1P2 100%</p>

#### [ Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290886):
<p>M1A1 100%</p>

#### [ Kenny Lau (Mar 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290891):
<p>conclusion: continue building the map</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290934):
<p>are you arguing by induction?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290936):
<p>This is a dangerous technique :-)</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290941):
<p>The final exam is worth 18 times more than the tests so you need to work 18 times as hard, right?</p>

#### [ Patrick Massot (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290944):
<p>This AITP looks interesting</p>

#### [ Kenny Lau (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290948):
<p>what is AITP?</p>

#### [ Patrick Massot (Mar 27 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290949):
<p>why did nobody mentioned that when we discussed ITP?</p>

#### [ Patrick Massot (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290959):
<p><a href="http://aitp-conference.org/2017/" target="_blank" title="http://aitp-conference.org/2017/">http://aitp-conference.org/2017/</a></p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290960):
<p>a conference on the top of a mountain</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290964):
<p>That link might be last year's...</p>

#### [ Patrick Massot (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290968):
<p>That where <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> must be then!</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290969):
<p>just at a guess</p>

#### [ Andrew Ashworth (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290970):
<p>conferences are always best when they are in a desireable location</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290972):
<p>I never think that</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290973):
<p>My favourite conferences are in big cities</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124290975):
<p>that way I don't miss home so much</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291024):
<p>I have been asked to go to exotic conferences in exotic places like Hawaii and have declined</p>

#### [ Andrew Ashworth (Mar 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291028):
<p>think of your graduate students who attend who can't afford holidays abroad without work kicking in a bit :)</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291029):
<p>because I was not sure I could handle a week there</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291039):
<p>Last three conferences I went to were in Boston, Berkeley and LA</p>

#### [ Patrick Massot (Mar 27 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291041):
<p>Indeed I was probably looking for <a href="http://aitp-conference.org/2018/" target="_blank" title="http://aitp-conference.org/2018/">http://aitp-conference.org/2018/</a></p>

#### [ Sebastian Ullrich (Mar 27 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291057):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> wait what</p>

#### [ Patrick Massot (Mar 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291119):
<p>Oh, it's in Aussois!</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291122):
<p>I try to avoid going skiing in March, February is way better</p>

#### [ Patrick Massot (Mar 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291146):
<p>I could have gone there easily (except that I'm teaching this week)</p>

#### [ Patrick Massot (Mar 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291153):
<p>I read "Robert Lewis: Toward AI for Lean, via metaprogramming"</p>

#### [ Patrick Massot (Mar 27 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291197):
<p>Looks like some people got proper training in grant proposal writing</p>

#### [ Patrick Massot (Mar 27 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291199):
<p>I would fund that one</p>

#### [ Matt Wilson (Mar 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291269):
<p>is that paper available publicly?</p>

#### [ Patrick Massot (Mar 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291282):
<p>I also like the spirit of the schedule:</p>
<blockquote>
<p><strong>March 25</strong><br>
19:30 dinner<br>
<strong>March 26</strong><br>
...</p>
</blockquote>

#### [ Sebastian Ullrich (Mar 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291443):
<p>Oh, I didn't know Rob had a new paper</p>

#### [ Sebastian Ullrich (Mar 27 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291449):
<p>I love that the conference page concludes with ski rental prices</p>

#### [ Patrick Massot (Mar 27 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291509):
<p>Does talking in this conference imply new paper?</p>

#### [ Patrick Massot (Mar 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291514):
<p>(I'm trying to learn CS academic life)</p>

#### [ Andrew Ashworth (Mar 27 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291520):
<p>you have to hope that your labmates ski though; not one of mine in graduate school did</p>

#### [ Patrick Massot (Mar 27 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291626):
<p>There is <a href="http://aitp-conference.org/2018/aitp18-proceedings.pdf" target="_blank" title="http://aitp-conference.org/2018/aitp18-proceedings.pdf">http://aitp-conference.org/2018/aitp18-proceedings.pdf</a> but it contains only one page by Rob</p>

#### [ Patrick Massot (Mar 27 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291637):
<p>But it contains question relevant to Lean 4 (stuff about the VM)</p>

#### [ Patrick Massot (Mar 27 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291904):
<p>I'd be curious to know what Hales intended to say</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291922):
<p>He was probably going to let out the secret.</p>

#### [ Patrick Massot (Mar 27 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291938):
<p>Which one? There are so many secrets</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291942):
<p>He just got a big grant to fund formal abstracts</p>

#### [ Patrick Massot (Mar 27 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291952):
<p>Oooh</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124291997):
<p>and talking of secrets</p>

#### [ Patrick Massot (Mar 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292004):
<p>Fund what exactly?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292007):
<p>today I heard i'd been awarded a rather smaller grant to find my 13 undergraduates this summer</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292017):
<p>I think Hales is going to pay people to type in statements of theorems in the Annals or whatever.</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292023):
<p>into Lean</p>

#### [ Patrick Massot (Mar 27 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292034):
<p>Where will he find those people?</p>

#### [ Kevin Buzzard (Mar 27 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292043):
<p>If he's sitting at home with a broken toe he should come here and tell us the details :-)</p>

#### [ Rob Lewis (Mar 28 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292550):
<p>Hah, I guessed from the email I just got that I was mentioned here. There's no new paper, just a talk about some experiments that Minchao and I have been doing in our free time. Nothing very deep.</p>

#### [ Rob Lewis (Mar 28 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292584):
<p>The slides will eventually be online. The wifi here barely works, it took me ten minutes to email a picture of the scenery so I'm not gonna try to upload them now.</p>

#### [ Patrick Massot (Mar 28 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292586):
<p>Is this hammer thing the same as the stuff Isabelle users always talk  about?</p>

#### [ Rob Lewis (Mar 28 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292639):
<p>Yeah. There's a recent paper that translates the idea to Coq.</p>

#### [ Patrick Massot (Mar 28 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292663):
<p>Great!</p>

#### [ Patrick Massot (Mar 28 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292716):
<p>Do you have a public demo?</p>

#### [ Patrick Massot (Mar 28 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292728):
<p>And, while you're here: are you considering have your Mathematica stuff turned into a Sage stuff?</p>

#### [ Rob Lewis (Mar 28 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292865):
<p>We've only worked out the relevance filter component, and it isn't quite fast enough for practical use yet. This is really just experimenting right now. There's some messy jumble of code on github but nothing you want to look at. Johannes and I have been talking to a masters student who is interested in this kind of automation though, so with some luck, the three of us will make some progress soon.</p>

#### [ Rob Lewis (Mar 28 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292868):
<p>The ideas behind the link will transfer easily enough. The engineering is another story, and I've never actually used Sage.</p>

#### [ Rob Lewis (Mar 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292906):
<p>It could happen, particularly with an application in mind, but it isn't at the top of my to-do list.</p>

#### [ Patrick Massot (Mar 28 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124292975):
<p>I don't have any specific application in mind. But I was surprised by your paper because I know no Mathematica user, everybody uses Sage around me, and teaches Sage to students</p>

#### [ Patrick Massot (Mar 28 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293020):
<p>And Lean is open source software so it looks strange to choose Mathematica as a partner</p>

#### [ Patrick Massot (Mar 28 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293023):
<p>(well Lean 4 development is not yet open source, but let's hope for the best)</p>

#### [ Patrick Massot (Mar 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293079):
<p>But I should be sleeping. Tomorrow I need to teach old fashioned algebraic geometry in Sage (computing projections of algebraic sets using resultants).</p>

#### [ Patrick Massot (Mar 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293084):
<p>Bye</p>

#### [ Rob Lewis (Mar 28 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293097):
<p>I had the opposite experience as an undergrad, they taught us Mathematica and nothing else. Most of the people I asked said similar, but it was definitely a biased sample. And there were people at Wolfram who were already interested in Lean, so it made sense at the time, heh.</p>

#### [ Rob Lewis (Mar 28 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293105):
<p>I should also call it a night!</p>

#### [ Kevin Buzzard (Mar 28 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293282):
<p>I'm still sitting here idly trying software foundations.</p>

#### [ Kevin Buzzard (Mar 28 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293292):
<div class="codehilite"><pre><span></span>namespace hidden

inductive  le : nat → nat →  Prop
| le_n : ∀ n, le n n
| le_S : ∀ n m, (le n m) → (le n (nat.succ m))

local  infix ` lq ` :50  :=  λ m n, le m n

open le

lemma n_le_m__Sn_le_Sm : ∀ n m,
  n lq m → nat.succ n lq nat.succ m :=
begin
  intros n m H,
  cases H with NOT_USED NOT_USED_EITHER q Hnq,
  repeat {admit},
end
</pre></div>

#### [ Kevin Buzzard (Mar 28 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293348):
<p>cases is throwing away my variable names</p>

#### [ Kevin Buzzard (Mar 28 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124293359):
<p>(I called it lq to avoid confusion with already-defined-things)</p>

#### [ Kevin Buzzard (Mar 28 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295500):
<p>I proved 2+2 isn't 6</p>

#### [ Kevin Buzzard (Mar 28 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295506):
<div class="codehilite"><pre><span></span>definition  S (n : ℕ) := nat.succ n

inductive  R : nat → nat → nat →  Prop
| c1 : R 0  0  0
| c2 : ∀ m n o, R m n o → R (S m) n (S o)
| c3 : ∀ m n o, R m n o → R m (S n) (S o)

open R

example : R 1  1  2  := c3 _ _ _ (c2 _ _ _ c1)

example : ¬ (R 2  2  6) :=  begin
intro H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
cases H with H H H H H H H H,
end
</pre></div>

#### [ Kevin Buzzard (Mar 28 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295555):
<p>Cases eats far too many variables which makes the proof look even more ridiculous</p>

#### [ Kevin Buzzard (Mar 28 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295607):
<p>Cut and paste from VS Code into zulipchat (ubuntu, firefox) isn't great. I get extra spaces, extra carriage returns</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295722):
<p>I'm not sure what's up with zulip paste. I don't think it was doing that when we first moved</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295724):
<p>Here's a shorter way to write that proof:</p>
<div class="codehilite"><pre><span></span>example : ¬ (R 2 2 6) | H := by casesm * [R _ _ _]
</pre></div>

#### [ Mario Carneiro (Mar 28 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295739):
<p>but if you look at the resulting proof, it's rather involved</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295788):
<p>You can simplify the proof if you define <code>R</code> to avoid having both <code>c2</code> and <code>c3</code>; the proof length here increases exponentially</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124295898):
<blockquote>
<p>cases is throwing away my variable names</p>
</blockquote>
<p>I tried once to make a version of cases that doesn't throw away names, but it's tough. What happens is that the names are allotted first, in the case splits, and then some cases are eliminated outright by inversion so you never see those names. I just put <code>_</code> for those</p>

#### [ Kenny Lau (Mar 29 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359326):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> did you do the 4-star exercise proving that the two notions of evenness are equivalent?</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359329):
<p>Three notions :-)</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359330):
<p>I must be ahead of you ;-)</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359338):
<p>Link?</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359397):
<p>Use cases or induction on the inductive prop, if that's the issue. This blew my mind.</p>

#### [ Kenny Lau (Mar 29 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359405):
<p><a href="https://softwarefoundations.cis.upenn.edu/lf-current/IndProp.html#lab206" target="_blank" title="https://softwarefoundations.cis.upenn.edu/lf-current/IndProp.html#lab206">https://softwarefoundations.cis.upenn.edu/lf-current/IndProp.html#lab206</a></p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359407):
<p>Yes I did that one</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359416):
<p>I did the exercise before that one as well, which IIRC I used.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359594):
<p>Here's what I think Kenny is asking:</p>

#### [ Kenny Lau (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359603):
<p>All I'm asking is " did you do the 4-star exercise proving that the two notions of evenness are equivalent? "</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359604):
<div class="codehilite"><pre><span></span>def  S  := nat.succ

inductive  ev : nat →  Prop
| ev_0 : ev 0
| ev_SS : ∀ n : nat, ev n → ev (S (S n))

inductive  ev&#39; : nat →  Prop
| ev&#39;_0 : ev&#39; 0
| ev&#39;_2 : ev&#39; 2
| ev&#39;_sum : ∀ n m, ev&#39; n → ev&#39; m → ev&#39; (n + m)

theorem  ev&#39;_ev : ∀ n, ev&#39; n ↔ ev n :=  sorry
</pre></div>

#### [ Kenny Lau (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359607):
<p>right</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359609):
<p>and the answer is "yes, I did it whilst watching the football on Tuesday"</p>

#### [ Kenny Lau (Mar 29 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359650):
<p>did you use term mode or tactic mode?</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359652):
<p>tactic</p>

#### [ Kenny Lau (Mar 29 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359656):
<p>why am i not surprised</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359657):
<p>I really like Software Foundations, because I can do the exercises no matter how many stars they have, which is a good confidence boost :-)</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359665):
<p>The first time I saw a 5-star one I thought "oh gosh", and then I just sat down and did it, and thought "maybe I already know what they're trying to teach me here"</p>

#### [ Kenny Lau (Mar 29 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359670):
<p>maybe they're teaching you to quit using tactic mode</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359672):
<p>rofl</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359722):
<p>Coq is big on tactic mode</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359727):
<p>Term mode is favored by mathematicians who work in isabelle</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359734):
<p>Ish. Obviously there are exceptions</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359737):
<p>Lean docs seem to push term mode a lot at the start.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359740):
<p>I did notice that Software foundations instantly starts with "OK so here are some easy things, let's prove them in tactic mode".</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359742):
<p>You mean Jeremy pushes term mode in TIPL <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359743):
<p>As did a Coq tutorial I did before I came to Lean.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359782):
<p>I think that mathematicians should start with tactic mode</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359785):
<p>because they typically have no idea what a functional language is or what a lambda is</p>

#### [ Kenny Lau (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359787):
<p>mathematicians should start with formal proofs...</p>

#### [ Kenny Lau (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359790):
<p>fitch, hilbert, whatever</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359791):
<p>right</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359792):
<p>via tactic mode</p>

#### [ Kenny Lau (Mar 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359793):
<p>via writing it down on pen and paper</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359841):
<p>You can get pretty far writing everything out with assume, show, and calc in lean</p>

#### [ Kenny Lau (Mar 29 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359857):
<p>as far as Zeno got?</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359906):
<p>whenever I do a tactic proof I don't indent the line after <code>begin</code> and I can hear Johannes' voice in my head telling me that I can't get it PR'ed to mathlib that way</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359907):
<p>Not familiar with his proofs, unfortunately</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359915):
<p>Haha, best fix your style or else you'll get another nasty email asking you to teach your students the mathlib style</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359917):
<p>It's the voices in my head I have to deal with</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359966):
<p>be the compiler, be the journal editor... these voices are quite talented</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124359971):
<p>yeah I have some pretty high-class voices in my head.</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360082):
<p>Did you skip over the 5 star pumping lemma? That was quite an exercise</p>

#### [ Andrew Ashworth (Mar 29 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360115):
<p>Actually even the one on palindromes in the same chapter was involved</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360123):
<p>I looked at that when I didn't have access to a computer</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360126):
<p>and decided that mathematicians didn't care about pumping lemmas.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360128):
<p>I did do the 5 star constructive mathematics exercise even though the first time I saw it I figured mathematicians didn't care about that either.</p>

#### [ Kenny Lau (Mar 29 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360137):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> try doing regex :P</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360138):
<p>I did the 4 star even question again just now, because I couldnt' find my original solution and Kenny asking it made me concerned I'd missed something.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360139):
<p>I saw that regex stuff. I am not convinced I need to learn this sort of skill. I'm sure I'd find it a lot of fun</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360140):
<p>but I need to focus on other things.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360189):
<p>Kenny, my evenness proof is just <code>repeat {induction *, exact *}</code></p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124360191):
<p>well, perhaps not quite that</p>

#### [ Kenny Lau (Mar 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124381653):
<p>I have a 4-line 223-character solution</p>

#### [ Kenny Lau (Mar 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124381654):
<div class="codehilite"><pre><span></span>inductive ev : nat → Prop
| ev_0 : ev 0
| ev_SS : ∀ n, ev n → ev (n + 2)

inductive ev&#39; : nat → Prop
| ev&#39;_0 : ev&#39; 0
| ev&#39;_2 : ev&#39; 2
| ev&#39;_sum : ∀ n m, ev&#39; n → ev&#39; m → ev&#39; (n + m)

open ev
open ev&#39;

theorem ev&#39;_ev.standalone : ∀ n, ev&#39; n ↔ ev n :=
Line 1
Line 2
Line 3
Line 4
</pre></div>

#### [ Kenny Lau (Mar 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124381656):
<p>Let's see who can beat me</p>

#### [ Kenny Lau (Mar 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124381658):
<p>(I used appropriate spacings and I counted them in)</p>

#### [ Andrew Ashworth (Mar 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382012):
<p>i'm surprised there's so much interest in the "three different definitions of even" exercise</p>

#### [ Kenny Lau (Mar 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382023):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> beat me :P</p>

#### [ Andrew Ashworth (Mar 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382029):
<p>i thought the most interesting ones in that chapter were the subseq and palindrome problems</p>

#### [ Andrew Ashworth (Mar 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382078):
<p>i would give it a shot except i'm currently supposedly doing work at the moment</p>

#### [ Andrew Ashworth (Mar 29 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124382173):
<p>and i think the nodup and nostutter predicates are interesting since they are related to how finite sets are implemented in lean</p>

#### [ Ching-Tsun Chou (Mar 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idly%20trying%20software%20foundations/near/124383111):
<p>I would be interested to know if anyone can prove the pigeonhole principle (last exercise of the IndProp chapter) without excluded_middle.</p>


{% endraw %}
