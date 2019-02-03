---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79076Mathematicianslearningtactics.html
---

## Stream: [general](index.html)
### Topic: [Mathematicians learning tactics](79076Mathematicianslearningtactics.html)

---


{% raw %}
#### [ Kevin Buzzard (May 30 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318046):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="bp">ℕ+</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">m</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">n</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">mul_pos</span> <span class="n">m</span><span class="bp">.</span><span class="mi">2</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">one</span>       <span class="o">:=</span> <span class="n">succ_pnat</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">one_mul</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">one_mul</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_one</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_one</span> <span class="bp">_</span><span class="o">),</span>
<span class="n">mul_comm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_comm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318057):
<p><a href="https://github.com/leanprover/mathlib/blob/00a2eb4119d27761c8a6ee38eb1eae532cd3ac19/data/pnat.lean#L52" target="_blank" title="https://github.com/leanprover/mathlib/blob/00a2eb4119d27761c8a6ee38eb1eae532cd3ac19/data/pnat.lean#L52">https://github.com/leanprover/mathlib/blob/00a2eb4119d27761c8a6ee38eb1eae532cd3ac19/data/pnat.lean#L52</a></p>

#### [ Kevin Buzzard (May 30 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318061):
<p>All of the proofs of the axioms are the same</p>

#### [ Kevin Buzzard (May 30 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318070):
<p>"it's true for <code>nat</code> so done by <code>subtype.eq</code>"</p>

#### [ Kevin Buzzard (May 30 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318075):
<p>Could I write that sentence as a tactic?</p>

#### [ Kevin Buzzard (May 30 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318082):
<p>I don't even know if that's possible because I don't know what tactics know about names</p>

#### [ Kevin Buzzard (May 30 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318143):
<p>I'm looking for a proof that defines <code>mul</code> and <code>one</code> and then says <code>done by tactic</code></p>

#### [ Kevin Buzzard (May 30 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318210):
<p>If I can do the above with a tactic then I think I can start to work on the tactic I actually want.</p>

#### [ Kevin Buzzard (May 30 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318216):
<p>and maybe other mathematicians might like the same sort of tactics</p>

#### [ Kevin Buzzard (May 30 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318230):
<p>Remember when we noticed that proving that if A and B were equiv and A was a ring then B was a ring, was actually quite annoying?</p>

#### [ Kevin Buzzard (May 30 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318243):
<p>And Kenny would just knock off a proof and he'd just check all ten axioms</p>

#### [ Kevin Buzzard (May 30 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318254):
<p>and every proof would be <code>funext, simp [name of thing I'm proving]</code></p>

#### [ Kevin Buzzard (May 30 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318296):
<p>I think it's about time Kenny learnt how to write this tactic too</p>

#### [ Mario Carneiro (May 30 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318312):
<p>This is somewhat similar to Simon's pi instance tactic</p>

#### [ Kevin Buzzard (May 30 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318314):
<p>Can you give me a link?</p>

#### [ Mario Carneiro (May 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318327):
<p><a href="https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean">https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean</a></p>

#### [ Kevin Buzzard (May 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318339):
<p>It's just the same underlying question Mario. It's some concept that is natural to us -- you exchange something with something that's equiv and then an algorithm goes off in our heads which just transfers a whole bunch of structure from one thing to the other effortlessly</p>

#### [ Mario Carneiro (May 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318345):
<p>but to be perfectly honest, the "Kenny method", which I used also in metamath days, actually gets things done</p>

#### [ Mario Carneiro (May 30 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318406):
<p>It's only after you find yourself doing exactly the same thing ~20 times that you should start considering the tactic approach</p>

#### [ Kevin Buzzard (May 30 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318420):
<p>That's the point. I wonder if this is what I'm staring at.</p>

#### [ Mario Carneiro (May 30 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318426):
<p>with less than that, the time it takes to figure out how to write a tactic <em>eclipses</em> the time it would have taken to just copy paste get it over with</p>

#### [ Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318428):
<p>I'm running into it again and again, constantly proving trivial things</p>

#### [ Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318437):
<p>and the reason I'm interested</p>

#### [ Mario Carneiro (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318439):
<p>That's not the same</p>

#### [ Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318444):
<p>is that the tactic formalises something which I do naturally in my brain</p>

#### [ Mario Carneiro (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318445):
<p>if it's <em>different</em> trivial things, the tactic won't help</p>

#### [ Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318447):
<p>and I like formalizing stuff</p>

#### [ Mario Carneiro (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318451):
<p>it will handle one kind of trivial and leave untouched 60 others</p>

#### [ Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318452):
<p>This is the point at which I stop understanding</p>

#### [ Kevin Buzzard (May 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318455):
<p>and the only way I will understand</p>

#### [ Kevin Buzzard (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318473):
<p>is by trying to do it and failing</p>

#### [ Mario Carneiro (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318499):
<p>How many other proofs look like the proof of <code>comm_monoid pnat</code>?</p>

#### [ Kevin Buzzard (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318500):
<p>so I want to finally understand how difficult it is to write schoolkid.</p>

#### [ Kevin Buzzard (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318504):
<p>I don't know Mario. That's what I want to find out.</p>

#### [ Kevin Buzzard (May 30 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318514):
<p>Instead of saying "Mario go write schoolkid like I told you, it should be there"</p>

#### [ Mario Carneiro (May 30 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318521):
<p>it should already be in your file staring back at you before you want to consider writing a tactic automating it</p>

#### [ Kevin Buzzard (May 30 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318523):
<p>I should just try to write it myself</p>

#### [ Mario Carneiro (May 30 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318592):
<p>Another way to put it: Tactics are a <em>refactoring technique</em>. You should already have a repetitive proof, and now you want to get the same thing done but easier</p>

#### [ Reid Barton (May 30 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318616):
<p>I also wonder whether you really need a tactic, or just a lemma/instance "a subtype of a monoid is a monoid if it's closed under multiplication and contains the identity"</p>

#### [ Mario Carneiro (May 30 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127318684):
<p>^ this. In this world of automation, lemmas are unsung heroes</p>

#### [ Andrew Ashworth (May 30 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320354):
<p>that might be true in this case, but i think knowing how to write a tactic is a useful and core lean skill. Even if you don't write tactics, you should understand how they work so you can understand why they fail</p>

#### [ Andrew Ashworth (May 30 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320393):
<p>obviously there is chapter 8 in programming in lean. now if you don't want to write anything complicated, the way forward is to browse through how the tactics are written in core lean, starting with the most basic ones like intro.</p>

#### [ Andrew Ashworth (May 30 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320399):
<p>(this is all on my to-do list as well, haha)</p>

#### [ Andrew Ashworth (May 30 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320469):
<p>for references there is John Harrison's "Practical Logic and Automated Reasoning", Chlipala's "Certified Programming with Dependent Types", although in Coq, is handy</p>

#### [ Andrew Ashworth (May 30 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320585):
<p>for some applications I have "Term Rewriting and All That", "Decision Procedures: An Algorithmic Point of View", "Modern Computer Algebra"</p>

#### [ Andrew Ashworth (May 30 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320794):
<p>All the way at the bottom of my very sad to-do list is: "learn Isabelle and study sledgehammer and nitpick" (some other popular and useful tactics...)</p>

#### [ Andrew Ashworth (May 30 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127320822):
<p>since i only make progress with Lean on the weekends, I'll see you guys in a few years :)</p>

#### [ Johan Commelin (May 30 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321007):
<p>But the <code>intro</code> tactic is written in C++, right? At least I found <a href="https://github.com/leanprover/lean/tree/dac6eec55661d3a2dab56859ffc05aef1aabb185/src/library/tactic" target="_blank" title="https://github.com/leanprover/lean/tree/dac6eec55661d3a2dab56859ffc05aef1aabb185/src/library/tactic">https://github.com/leanprover/lean/tree/dac6eec55661d3a2dab56859ffc05aef1aabb185/src/library/tactic</a>, and it contains a lot of <code>cpp</code> files.</p>

#### [ Andrew Ashworth (May 30 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321123):
<p>try <code>library/init/meta/interactive.lean</code></p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">intro</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">ident_</span><span class="err">?</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">unit</span>
<span class="bp">|</span> <span class="n">none</span>     <span class="o">:=</span> <span class="n">intro1</span> <span class="bp">&gt;&gt;</span> <span class="n">skip</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">h</span><span class="o">)</span> <span class="o">:=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">intro</span> <span class="n">h</span> <span class="bp">&gt;&gt;</span> <span class="n">skip</span>
</pre></div>

#### [ Johan Commelin (May 30 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321207):
<p>So what is the relation between this <code>lean</code>-file and the <code>cpp</code>-files that I found?</p>

#### [ Simon Hudon (May 30 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321289):
<p>The tactics that you found are declared in Lean as constants:</p>
<div class="codehilite"><pre><span></span>meta constant intro_core    : name → tactic expr
meta constant intron        : nat → tactic unit
</pre></div>


<p>That is, they do not have Lean definitions and Lean simply executes the C++ implementation when they are called.</p>

#### [ Kevin Buzzard (May 30 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321647):
<p>Dumb question:</p>

#### [ Kevin Buzzard (May 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321708):
<p>what's the quickest way to generate a complete "blank" construction of a <code>comm_ring</code></p>

#### [ Kevin Buzzard (May 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321712):
<p>I want</p>

#### [ Kevin Buzzard (May 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321718):
<div class="codehilite"><pre><span></span>{mul := _,
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321725):
<p><code>mul_assoc := _,</code></p>

#### [ Kevin Buzzard (May 30 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321731):
<p>etc etc</p>

#### [ Sebastian Ullrich (May 30 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321765):
<p><code>{..}</code></p>

#### [ Simon Hudon (May 30 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127321819):
<p>You should look into <code>pexpr.mk_structure_instance</code></p>

#### [ Kevin Buzzard (May 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322553):
<p>Possibly first stupid question of many</p>

#### [ Kevin Buzzard (May 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322561):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">semigroup</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">semigroup</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">intros</span><span class="o">,</span> <span class="n">sorry</span> <span class="kn">end</span><span class="o">,</span>
<span class="n">mul_assoc</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322575):
<p>I am just trying to play with structures to see how far I can get in tactic mode</p>

#### [ Kevin Buzzard (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322588):
<p>but Lean doesn't like that instance</p>

#### [ Kevin Buzzard (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322628):
<div class="codehilite"><pre><span></span>type mismatch at field &#39;mul_assoc&#39;
  sorry
has type
  ∀ (a b c : Π (i : I), f i), ?m_1 (?m_1 a b) c = ?m_1 a (?m_1 b c)
but is expected to have type
  ∀ (a b c : Π (i : I), f i), a * b * c = a * (b * c)
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322630):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> thanks -- that comment helped!</p>

#### [ Kevin Buzzard (May 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322634):
<p>I'm still stuck though</p>

#### [ Kevin Buzzard (May 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322666):
<p>fixed it</p>

#### [ Kevin Buzzard (May 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322669):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">semigroup</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">semigroup</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span>
<span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span><span class="n">sorry</span><span class="o">,</span>
<span class="n">mul</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">intros</span><span class="o">,</span> <span class="n">sorry</span> <span class="kn">end</span><span class="o">,</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127322676):
<p>I think Mario once explained to me what was going on there but I still find it confusing</p>

#### [ Kevin Buzzard (May 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323292):
<p>I am experimenting with algebra.pi_instances</p>

#### [ Kevin Buzzard (May 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323297):
<p>I kind of suspect that Kenny will know all the answers to my questions</p>

#### [ Kevin Buzzard (May 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323332):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> what's your golf proof of <code>instance comm_ring [∀ i, comm_ring $ f i] : comm_ring (Π i : I, f i)</code>?</p>

#### [ Kevin Buzzard (May 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323365):
<p>Product of commutative rings is a ring.</p>

#### [ Kevin Buzzard (May 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323385):
<p>Do you have to write as many lines as there are axioms (plus a few more lines on top)?</p>

#### [ Kevin Buzzard (May 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323397):
<p>Or can you do tricks -- but you can't use Simon's tactic, just stuff like simp</p>

#### [ Kevin Buzzard (May 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323402):
<p>you can write tools</p>

#### [ Kevin Buzzard (May 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127323406):
<p>but in tactic mode, not new tactics</p>

#### [ Kenny Lau (May 30 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127324580):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">comm_ring</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span> <span class="n">x</span> <span class="n">i</span> <span class="bp">+</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">neg</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="bp">-</span><span class="n">x</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span> <span class="n">x</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span>
  <span class="bp">..</span> <span class="o">}</span><span class="bp">;</span>
<span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">funext</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">add_assoc</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">add_zero</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">zero_add</span>
    <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">add_left_neg</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">add_comm</span>
    <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">mul_assoc</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">mul_one</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">one_mul</span>
    <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">left_distrib</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">right_distrib</span>
    <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">mul_comm</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325167):
<p>Kenny I want to play with the add/zero/neg etc part of your code</p>

#### [ Kevin Buzzard (May 30 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325169):
<p>but if I try this</p>

#### [ Kevin Buzzard (May 30 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325171):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">comm_ring</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span>
<span class="o">{</span> <span class="n">add</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">intros</span><span class="o">,</span><span class="n">sorry</span><span class="o">,</span><span class="kn">end</span><span class="o">,</span><span class="c1">-- λ x y i, x i + y i,</span>
  <span class="n">zero</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">neg</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="bp">-</span><span class="n">x</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span> <span class="n">x</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">y</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="mi">1</span><span class="o">,</span>
  <span class="bp">..</span> <span class="o">}</span><span class="bp">;</span>
<span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">funext</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">add_assoc</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">add_zero</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">zero_add</span>
    <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">add_left_neg</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">add_comm</span>
    <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">mul_assoc</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">mul_one</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">one_mul</span>
    <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">left_distrib</span> <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">right_distrib</span>
    <span class="bp">&lt;|&gt;</span> <span class="n">apply</span> <span class="n">mul_comm</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (May 30 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325176):
<p>how do you want to play with them?</p>

#### [ Kevin Buzzard (May 30 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325185):
<p>then there's no definition of add so your tactic doesn't finish the job and the errors from this for some reason stop Lean from processing <code>add</code></p>

#### [ Kenny Lau (May 30 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325192):
<p>what do you want to change it to?</p>

#### [ Kevin Buzzard (May 30 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325201):
<p>I want to change it into a begin end tactic</p>

#### [ Kevin Buzzard (May 30 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325248):
<p>of the form "intros,funext,apply has_add.add end"</p>

#### [ Kenny Lau (May 30 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325254):
<p>trust the force, Luke</p>

#### [ Kevin Buzzard (May 30 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325285):
<p>Can you write a tactic which does add,zero,neg,mul and one?</p>

#### [ Kenny Lau (May 30 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325301):
<p>not really</p>

#### [ Kevin Buzzard (May 30 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127325306):
<p>In every case it's "deduce it from the factors"</p>

#### [ Mario Carneiro (May 30 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127327884):
<p>I'm not clear on why we're rehashing this. You are rediscovering Simon's tactic</p>

#### [ Kevin Buzzard (May 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328137):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">pi</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>     <span class="c1">-- The indexing type</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span> <span class="c1">-- The family of types already equiped with instances</span>

<span class="n">class</span> <span class="n">notation_crazy_structure_that_someone_else_wrote</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">has_add</span> <span class="n">α</span><span class="o">,</span>
<span class="n">has_mul</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_zero</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_one</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_neg</span> <span class="n">α</span><span class="o">,</span> <span class="n">has_le</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">*</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="bp">-</span><span class="mi">1</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">can_a_tactic_prove_me</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">notation_crazy_structure_that_someone_else_wrote</span> <span class="err">$</span> <span class="n">f</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span>
<span class="n">notation_crazy_structure_that_someone_else_wrote</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span> <span class="o">:</span> <span class="n">I</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (May 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328145):
<p>I'm trying to learn it</p>

#### [ Kevin Buzzard (May 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328238):
<p>I can't prove that with pi_instance</p>

#### [ Kevin Buzzard (May 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328254):
<p>I am hoping I can just have a proof of the form "by canonical"</p>

#### [ Kevin Buzzard (May 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328266):
<p>I have to learn it because I can't keep pestering Simon every time I want it to do a bit more</p>

#### [ Kevin Buzzard (May 30 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328440):
<p>no extra inputs or anything</p>

#### [ Kevin Buzzard (May 30 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328458):
<p>because isn't it true that all that structure just transfers over completely canonically?</p>

#### [ Kevin Buzzard (May 30 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328540):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> can <code>pi_instance</code> do this without being fed any extra information whatsoever?</p>

#### [ Kevin Buzzard (May 30 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328563):
<p>Lean needs to get better at doing stuff which mathematicians find trivial</p>

#### [ Simon Hudon (May 30 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328635):
<p>Do what specifically?</p>

#### [ Simon Hudon (May 30 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328636):
<p>(deleted)</p>

#### [ Kevin Buzzard (May 30 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328683):
<p>construct the instance above called <code>can_a_tactic_prove_me</code></p>

#### [ Kevin Buzzard (May 30 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328725):
<p>Is it possible to write a tactic which proves a goal like that without any extra prodding?</p>

#### [ Simon Hudon (May 30 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328730):
<p>I think so.</p>

#### [ Kevin Buzzard (May 30 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328740):
<p>By generalising your pi_instance tactic?</p>

#### [ Simon Hudon (May 30 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328857):
<p>I'm working on a set of tactics to replace <code>pi_instance</code>. It would be the dual of <code>cases</code> / <code>case</code> which I call <code>refine_struct</code>/ <code>field</code> / <code>apply_field</code>. Basically, you write <code>refine_struct { .. } ; intro ; apply_field</code>. Maybe you'd need a bit more but you would have a generic way of referring to the field that you're looking into</p>

#### [ Kevin Buzzard (May 30 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328918):
<p>oh wow!</p>

#### [ Simon Hudon (May 30 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328953):
<p>I've been procrastinating with writing my dissertation and working but I should get back to it</p>

#### [ Kevin Buzzard (May 30 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328962):
<p>Yes that's exactly the sort of conclusion I was coming to (that's why I was asking about <code>..</code>). I wanted to do <code>begin refine { .. },...</code> but was having trouble with it</p>

#### [ Kevin Buzzard (May 30 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328969):
<p>Well can I write these tactics somehow?</p>

#### [ Kevin Buzzard (May 30 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127328976):
<p>Or Kenny when he's finished doing my project?</p>

#### [ Simon Hudon (May 30 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329067):
<p>It is actually some pretty tricky stuff so it would be easier for me to just do it than to explain how to do it. Although, I'd like to also write a tutorial about it</p>

#### [ Kevin Buzzard (May 30 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329164):
<p>Darn it I need a route into this stuff</p>

#### [ Simon Hudon (May 30 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329194):
<p>In the mean time, I have a goodie coming up: a tactic that asserts that subtractions have non-negative results (they don't hit the floor of natural numbers) and a tactic that assert that all divisors are non-null</p>

#### [ Kevin Buzzard (May 30 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329201):
<p>I need to find a tactic which I can write and is somehow distantly related to what I want to be able to do with tactics</p>

#### [ Kevin Buzzard (May 30 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329253):
<p>subtractions -- Patrick will be over the moon!</p>

#### [ Simon Hudon (May 30 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329342):
<p>If you want, I can show you my subtraction tactic and let you figure out the version for division</p>

#### [ Kevin Buzzard (May 30 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329369):
<p>I could have a look!</p>

#### [ Kevin Buzzard (May 30 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329374):
<p>Somehow it's the canonical stuff that I'm interested in though</p>

#### [ Simon Hudon (May 30 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127329426):
<p>What do you mean by canonical?</p>

#### [ Simon Hudon (May 30 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127330210):
<p>Feel free to try your hand on <a href="https://gist.github.com/cipher1024/72af1694ce395d7162bab1a72c1f9c56" target="_blank" title="https://gist.github.com/cipher1024/72af1694ce395d7162bab1a72c1f9c56">https://gist.github.com/cipher1024/72af1694ce395d7162bab1a72c1f9c56</a></p>

#### [ Patrick Massot (May 31 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathematicians%20learning%20tactics/near/127349075):
<p>Thanks Simon! I'll have a very close look at that (but probably not today <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span> )</p>


{% endraw %}
