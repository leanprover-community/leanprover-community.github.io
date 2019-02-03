---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89192targetteddefinitionalreduction.html
---

## Stream: [general](index.html)
### Topic: [targetted definitional reduction](89192targetteddefinitionalreduction.html)

---


{% raw %}
#### [ Kevin Buzzard (May 29 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246965):
<p>The history of this question is the following: I had a complicated goal which could be reduced using a definitional unfolding which for some reason wasn't happening -- "unfold" wouldn't work</p>

#### [ Kevin Buzzard (May 29 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246970):
<p>I wanted to do the unfold manually with a rw so I asked the name of the theorem that <code>{a := x, b := y}.a = x</code></p>

#### [ Kevin Buzzard (May 29 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246972):
<p>and I was told that this theorem had no name</p>

#### [ Kevin Buzzard (May 29 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246978):
<p>because it was true by refl</p>

#### [ Kevin Buzzard (May 29 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127246982):
<p>On the other hand, browsing through the library I see a bunch of things with names whose proof is rfl</p>

#### [ Kevin Buzzard (May 29 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247027):
<p>All the other suggestions for what to do were not good for me.</p>

#### [ Kevin Buzzard (May 29 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247039):
<p>"Change it yourself with show" -- yeah but this is a PITA because my structure is a very complicated structure with a very long name and it is being constructed using very long terms</p>

#### [ Kevin Buzzard (May 29 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247045):
<p>and I know <em>precisely</em> how I want <em>this precise term</em> to unfold and I don't want to do anything else to the goal</p>

#### [ Kevin Buzzard (May 29 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247059):
<p>If I change it myself with show then I have to work out what I want the goal to be using pencil and paper! It's 2018!</p>

#### [ Kevin Buzzard (May 29 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247065):
<p>I _need_ to change it because rw is really fussy, it won't rw something defeq to what you want sometimes -- it sometimes needs help</p>

#### [ Kevin Buzzard (May 29 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247067):
<p>and the line after my show line was a complicated rw</p>

#### [ Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247110):
<p>Here's what I want to do</p>

#### [ Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247115):
<p>I want to zoom in to the area I am interested in using conv</p>

#### [ Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247120):
<p>and I want to run dsimp or some such thing just on that one term</p>

#### [ Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247121):
<p>Is this possible?</p>

#### [ Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247122):
<p>I don't think so.</p>

#### [ Kevin Buzzard (May 29 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247125):
<p>conv offers me exciting commands such as "to_lhs"</p>

#### [ Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247130):
<p>what about "to 3rd input of this function"?</p>

#### [ Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247136):
<p>Can conv do that?</p>

#### [ Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247142):
<p>Can I do dsimp in conv?</p>

#### [ Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247151):
<p>I use tactic mode precisely because I like the precise control I have over what is going on</p>

#### [ Kevin Buzzard (May 29 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247154):
<p>but as I get older and wiser and understand more about what is happening, I want more precise tools</p>

#### [ Kevin Buzzard (May 29 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247202):
<p>I can do dsimp in conv mode :-)</p>

#### [ Kevin Buzzard (May 29 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247203):
<p>so my question becomes how to access the 3rd input to a function</p>

#### [ Kevin Buzzard (May 29 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247207):
<p>goal is <code>f x y = g z</code></p>

#### [ Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247212):
<p>and I want to run dsimp on y only</p>

#### [ Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247213):
<p>how do I do that?</p>

#### [ Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247218):
<p>Ok I just thought of a solution which again will work in many cases</p>

#### [ Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247222):
<p>just define exactly the rewrite I want, call it H, and rw H</p>

#### [ Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247224):
<p>This gets me back to the original problem though</p>

#### [ Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247226):
<p>I do not want to run dsimp in my head</p>

#### [ Kevin Buzzard (May 29 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247229):
<p>I am too lazy</p>

#### [ Kevin Buzzard (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247271):
<p>I am a big boy now</p>

#### [ Mario Carneiro (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247273):
<p>what's wrong with <code>dsimp</code>?</p>

#### [ Kevin Buzzard (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247277):
<p>simplifies too much</p>

#### [ Kevin Buzzard (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247279):
<p>that's the wrong question</p>

#### [ Mario Carneiro (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247281):
<p>no, that's the standard solution</p>

#### [ Kevin Buzzard (May 29 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247284):
<p>unless you are genuinely convinced that I really never want to run dsimp on just a subterm</p>

#### [ Kevin Buzzard (May 29 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247288):
<p>Let me go back to my usage case</p>

#### [ Mario Carneiro (May 29 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127247296):
<p>you can use <code>dsimp only</code> or other such tricks to limit the unnecessary simping</p>

#### [ Chris Hughes (May 29 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127257747):
<p><code>unfold structure.a</code> sometimes works for me in these situations.</p>

#### [ Kevin Buzzard (May 29 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266078):
<p>In my usage case, dsimp doesn't do anything at all</p>

#### [ Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266492):
<p>the goal is (function x y z).F H -&gt; Z`</p>

#### [ Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266501):
<p>and <code>function x y z</code> creates a structure</p>

#### [ Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266505):
<p>by saying what all the bits and pieces are</p>

#### [ Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266508):
<p>including F</p>

#### [ Kevin Buzzard (May 29 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266511):
<p>dsimp does nothing</p>

#### [ Kevin Buzzard (May 29 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266515):
<p>I can't get conv to get to it</p>

#### [ Kevin Buzzard (May 29 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266577):
<p>is it because it's a pi type?</p>

#### [ Kevin Buzzard (May 29 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266622):
<p>In the end I copied the context, scrolled to the end of the proof, pasted it, changed <code>X : y,</code> to <code>(X : y)</code> about ten times and made them all variables, and then used <code>#reduce</code> and then cut and pasted the answer back in the proof and wrote "show" in front of it, and then farted around with some pp.proof on to get it to work and I was done</p>

#### [ Kevin Buzzard (May 29 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266624):
<p>That can't be the best way</p>

#### [ Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266676):
<p>that's not even true</p>

#### [ Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266680):
<p>#reduce didn't do it</p>

#### [ Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266684):
<p>no wait</p>

#### [ Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266686):
<p>it half did it</p>

#### [ Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266689):
<p>it did enough of it</p>

#### [ Kevin Buzzard (May 29 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266699):
<p>it unfolded (function x y z).F into (some function of x y and z)</p>

#### [ Kevin Buzzard (May 29 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127266711):
<p>Why did this cause me such pain? What did I miss?</p>

#### [ Kevin Buzzard (May 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267136):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span> <span class="n">scheme</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">proofs</span> <span class="n">true</span>

<span class="kn">theorem</span> <span class="n">presheaves_iso</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf_of_types</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="n">are_isomorphic_presheaves_of_types</span>
    <span class="o">(</span><span class="n">presheaf_of_types_pullback_under_open_immersion</span> <span class="n">F</span> <span class="n">id</span>
      <span class="o">(</span><span class="n">topological_space</span><span class="bp">.</span><span class="n">open_immersion_id</span> <span class="bp">_</span><span class="o">))</span>
    <span class="n">F</span>
<span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">constructor</span><span class="o">,</span><span class="n">tactic</span><span class="bp">.</span><span class="n">swap</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">constructor</span><span class="o">,</span><span class="n">tactic</span><span class="bp">.</span><span class="n">swap</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">U</span> <span class="n">HU</span><span class="o">,</span>
      <span class="k">have</span> <span class="n">Hid</span> <span class="o">:=</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">open_immersion_id</span> <span class="n">X</span><span class="o">,</span>
      <span class="c1">-- goal now</span>
      <span class="k">show</span> <span class="o">(</span><span class="n">presheaf_of_types_pullback_under_open_immersion</span> <span class="n">F</span> <span class="n">id</span> <span class="n">Hid</span><span class="o">)</span><span class="bp">.</span><span class="n">F</span> <span class="n">HU</span> <span class="bp">→</span> <span class="n">F</span><span class="bp">.</span><span class="n">F</span> <span class="n">HU</span><span class="o">,</span>
      <span class="c1">--unfold presheaf_of_types_pullback_under_open_immersion, -- fails</span>
      <span class="k">show</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">F</span> <span class="o">((</span><span class="n">Hid</span><span class="bp">.</span><span class="n">fopens</span> <span class="n">U</span><span class="o">)</span><span class="bp">.</span><span class="n">mp</span> <span class="n">HU</span><span class="o">))</span> <span class="bp">→</span> <span class="n">F</span><span class="bp">.</span><span class="n">F</span> <span class="n">HU</span><span class="o">,</span> <span class="c1">-- obtained by &quot;#reduce&quot; calculation below</span>
      <span class="k">show</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">F</span> <span class="o">(</span><span class="bp">_</span> <span class="o">:</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">))</span> <span class="bp">→</span> <span class="n">F</span><span class="bp">.</span><span class="n">F</span> <span class="n">HU</span><span class="o">),</span> <span class="c1">-- obtained by more out-of-proof unravelling</span>

      <span class="n">sorry</span>
    <span class="o">},</span><span class="n">sorry</span><span class="o">,</span>

  <span class="o">},</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
<span class="kn">variables</span>
<span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf_of_types</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">HU</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">H</span> <span class="n">U</span><span class="o">)</span>
<span class="o">(</span><span class="n">Hid</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">open_immersion</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">))</span>

<span class="bp">#</span><span class="n">reduce</span> <span class="o">(</span><span class="n">presheaf_of_types_pullback_under_open_immersion</span> <span class="n">F</span> <span class="n">id</span> <span class="n">Hid</span><span class="o">)</span><span class="bp">.</span><span class="n">F</span>
<span class="c1">-- λ (U : X → Prop) (HU : topological_space.is_open H U), F.F ((Hid.fopens U).mp HU)</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="n">Hid</span><span class="bp">.</span><span class="n">fopens</span> <span class="n">U</span><span class="o">)</span><span class="bp">.</span><span class="n">mp</span> <span class="c1">-- is_open U → is_open (id &#39;&#39; U)</span>


<span class="bp">#</span><span class="kn">exit</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267142):
<p>What my code looks like</p>

#### [ Kevin Buzzard (May 29 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267540):
<p>It doesn't run for people who don't have my repo because it needs scheme.lean but I hope it explicitly shows the problem. I don't know how to get Lean to unfold <code>(presheaf_of_types_pullback_under_open_immersion F id Hid).F</code>, possibily because it's in a lambda, but it is defeq to something much simpler which I work out outside the proof after some copying of context (IRL the context was huge and I just did the unravelling using cut and paste)</p>

#### [ Mario Carneiro (May 29 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267590):
<p>You should have a simp lemma for the value of <code>.F</code></p>

#### [ Mario Carneiro (May 29 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127267671):
<p>alternatively, you can <code>dsimp [function]</code> to unfold it</p>

#### [ Kevin Buzzard (May 30 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278172):
<blockquote>
<p>You should have a simp lemma for the value of <code>.F</code></p>
</blockquote>
<p>Talking through pnat was very instructional. I realise that I have a very poor feeling about what should be a simp lemma. I made that structure though -- these lemmas aren't automatically added when I make the structure? What is added to the simp machine?</p>

#### [ Kevin Buzzard (May 30 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278180):
<blockquote>
<p>alternatively, you can <code>dsimp [function]</code> to unfold it</p>
</blockquote>
<p>This is what I needed to know :-) Thanks!</p>

#### [ Kevin Buzzard (May 30 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278221):
<p>Even though my function isn't a simp lemma :-)</p>

#### [ Mario Carneiro (May 30 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278222):
<p><code>simp</code>  will reduce terms that look like <code>&lt;a, b, c&gt;.2</code></p>

#### [ Mario Carneiro (May 30 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278229):
<p>where <code>&lt;&gt;</code> is the builtin structure constructor and <code>.2</code> is a builtin projection</p>

#### [ Mario Carneiro (May 30 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278241):
<p>If there are any definitions shielding the redex from looking like that, simp won't find it</p>

#### [ Kevin Buzzard (May 30 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278246):
<p>like <code>(f x y z).F</code></p>

#### [ Mario Carneiro (May 30 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/targetted%20definitional%20reduction/near/127278247):
<p>right</p>


{% endraw %}
