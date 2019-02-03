---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/39678LIVECHATStructuresformathematicians.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [LIVE CHAT: Structures for mathematicians](https://leanprover-community.github.io/archive/116395maths/39678LIVECHATStructuresformathematicians.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 29 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127264270):
<p>At 8pm UK time (2000 BST, so 1900 GMT) I am going to a live Lean explanation, in this thread, of a very simple mathlib file which defines a (non-inductive) structure. Mathematicians need to learn how to make structures, it's something we do very differently in mathematics. Here we need a far more formal kind of interface. I will hopefully do a few of these. It's like "talking people through mathlib files".</p>

#### [ Kenny Lau (May 29 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127264325):
<p>youtube live?</p>

#### [ Johan Commelin (May 29 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127264635):
<p>No, it seems "Zulip live"</p>

#### [ Kevin Buzzard (May 29 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127265656):
<p>Johan, I was inspired to do it after looking at the structure you constructed, which reminded me of the terrible first structure I constructed.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267673):
<p>Hello, this is just me talking through <code>pnat.lean</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267674):
<p>It should be easy</p>

#### [ Kevin Buzzard (May 29 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267678):
<p>and maybe people will find it later.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267695):
<p>Ok so mathematicians use a lot of structures, and one structure I was brought up on is "the UK mathematician's nat", namely {1,2,3,...}</p>

#### [ Kevin Buzzard (May 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267698):
<p>Ok so how do we define the UK mathematician's nat?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267701):
<p>Well pretty clearly we could define it like the computer scientist's nat := {0,1,2,3,...}</p>

#### [ Kevin Buzzard (May 29 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267702):
<p>we could just make a structure</p>

#### [ Kevin Buzzard (May 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267742):
<p>hmm</p>

#### [ Kevin Buzzard (May 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267745):
<p>let me fire up lean</p>

#### [ Kevin Buzzard (May 29 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267771):
<p>that's better</p>

#### [ Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267796):
<p>I am so rubbish at structures</p>

#### [ Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267810):
<p>aah bingo</p>

#### [ Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267813):
<p>it's not a structure</p>

#### [ Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267817):
<p>it's an inductive type</p>

#### [ Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267819):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">pnat</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:</span> <span class="n">pnat</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="n">pnat</span> <span class="bp">→</span> <span class="n">pnat</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267820):
<p>So there's pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267825):
<p>and that would work</p>

#### [ Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267870):
<p>and we could define addition and multiplication and prove addition is commutative</p>

#### [ Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267873):
<p>and do all that stuff again</p>

#### [ Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267877):
<p>and that's stuff we already did with nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267879):
<p>and that's kind of a waste</p>

#### [ Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267889):
<p>it would be nice to inherit all those theorems about nat and get them to pnat immediately</p>

#### [ Kevin Buzzard (May 29 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267896):
<p>so let's take a look at what they did in Lean or mathlib, wherever they defined pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267932):
<p>Ok so it's in mathlib</p>

#### [ Kevin Buzzard (May 29 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267936):
<p>which means that computer scientists are not interested in this structure</p>

#### [ Kevin Buzzard (May 29 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267939):
<p>You can get to it with "import data.pnat"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267943):
<p>let's find it on github</p>

#### [ Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267993):
<p><a href="https://github.com/leanprover/mathlib/blob/master/data/pnat.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/pnat.lean">https://github.com/leanprover/mathlib/blob/master/data/pnat.lean</a></p>

#### [ Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267996):
<p>There it is.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127267999):
<p>Last modified two days ago!</p>

#### [ Kevin Buzzard (May 29 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268002):
<p>Things never stand still around here</p>

#### [ Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268022):
<p>OK so I'm going to talk through this file, or at least what I understand of this file, which is pretty much all of it I hope</p>

#### [ Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268029):
<p>and the first thing we notice</p>

#### [ Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268034):
<p>is that on line 1</p>

#### [ Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268037):
<p>they don't define it using an inductive structure like nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268039):
<p>they define it as a _subtype_</p>

#### [ Kevin Buzzard (May 29 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268041):
<p>which is a bit more annoying to use in practice</p>

#### [ Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268066):
<p>oh wait I skipped a line</p>

#### [ Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268093):
<p><code>import tactic.basic</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268099):
<p>let's come back to that line when I have figured out why it's there</p>

#### [ Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268104):
<p><code>def pnat := {n : ℕ // n &gt; 0}</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268105):
<p>And there it is.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268107):
<p>There are sets <code>{x | blah}</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268110):
<p>and there are subtypes <code>{x // blah}</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268112):
<p>this one is a subtype</p>

#### [ Kevin Buzzard (May 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268135):
<p>don't mind me I'm just editing mathlib</p>

#### [ Kevin Buzzard (May 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268138):
<p>Ok so I was trying to work out what a subtype was</p>

#### [ Kevin Buzzard (May 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268140):
<p>but I know the answer</p>

#### [ Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268197):
<p>to make a pnat you have to give two pieces of data</p>

#### [ Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268200):
<p>1) a nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268204):
<p>2) a proof that it's positive</p>

#### [ Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268209):
<p>(that's &gt; 0 for you French speakers)</p>

#### [ Kevin Buzzard (May 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268220):
<p>so here's an example</p>

#### [ Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268230):
<p><code>definition x : pnat := ⟨59,oh crap⟩</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268232):
<p>that didn't go well</p>

#### [ Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268235):
<p>I was in the middle of defining 59</p>

#### [ Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268238):
<p>and all of a sudden I needed a proof.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268240):
<p>OK so let's try again but this time be prepared</p>

#### [ Kevin Buzzard (May 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268288):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">H</span> <span class="o">:</span> <span class="mi">59</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">definition</span> <span class="n">x</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">59</span><span class="o">,</span><span class="n">H</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268289):
<p>Ok that went better</p>

#### [ Kevin Buzzard (May 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268295):
<p>I cheated with my proof that 59 &gt; 0 by saying the proof was sorry (which means "just assume it")</p>

#### [ Kevin Buzzard (May 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268298):
<p>and now I can finally make my pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268311):
<p>This is going to be pretty inconvenient having to prove that things are positive</p>

#### [ Kevin Buzzard (May 29 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268316):
<p>but actually in a couple of lines we're going to see a really good way of doing it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268324):
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="bp">`ℕ+`</span> <span class="o">:=</span> <span class="n">pnat</span>

<span class="kn">instance</span> <span class="n">coe_pnat_nat</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="bp">ℕ+</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">subtype</span><span class="bp">.</span><span class="n">val</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268325):
<p>Those are the next couple of lines</p>

#### [ Kevin Buzzard (May 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268373):
<p>The first one is easy: it sets up notation, and we're going to use the completely non-standard notation <code>ℕ+</code> for pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268376):
<p>as opposed to a little plus or a little star or whatever the French use, maybe some sub zero or super zero</p>

#### [ Kevin Buzzard (May 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268383):
<p>this sort of thing is a minefield</p>

#### [ Kevin Buzzard (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268387):
<p><code>ℕ+</code> will do</p>

#### [ Kevin Buzzard (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268413):
<p>and now this incomprehensible coe line is where we start making the interface for our structure</p>

#### [ Patrick Massot (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268417):
<p>ℕ^*</p>

#### [ Kevin Buzzard (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268418):
<p>because we are already finished with the structure</p>

#### [ Kevin Buzzard (May 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268425):
<p>Submit a PR Patrick</p>

#### [ Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268486):
<p>The thing that mathematicians don't realise</p>

#### [ Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268490):
<p>or at least that I didn't realise at all</p>

#### [ Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268492):
<p>(I suspect Patrick knew full well)</p>

#### [ Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268493):
<p>was that it's not just about making the structure</p>

#### [ Kevin Buzzard (May 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268494):
<p>the next thing you have to do is to say to yourself</p>

#### [ Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268502):
<p>"what is every single basic thing that my users might want to do with this structure?"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268515):
<p>And the first basic thing is that given a positive natural, a mathematician might also want to think of it as a natural.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268519):
<p>And in fact it's such a natural (no pun intended) to move from pnat to nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268520):
<p>that not only did they design a function for it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268529):
<p>but they made it into a coercion</p>

#### [ Kevin Buzzard (May 29 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268532):
<p>which means "it happens magically"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268580):
<p>Aah I see what to do</p>

#### [ Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268582):
<p>I have mathlib pnat open</p>

#### [ Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268584):
<p>and a copy of it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268586):
<p>and I edit the copy</p>

#### [ Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268587):
<p>great</p>

#### [ Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268598):
<p>so let's see if we can understand this coercion</p>

#### [ Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268602):
<p>and then let's see it happen</p>

#### [ Kevin Buzzard (May 29 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268616):
<p><code>instance coe_pnat_nat : has_coe ℕ+ ℕ := ⟨subtype.val⟩</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268617):
<p>instances are something I never understood</p>

#### [ Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268622):
<p>coercions not really either</p>

#### [ Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268629):
<p>and then those dreaded pointy brackets</p>

#### [ Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268633):
<p>and then an incomprehensible <code>subtype.val</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268636):
<p>That's what I thought of that line in about January.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268646):
<p>But as Kenny once told me, Lean does not do magic</p>

#### [ Kevin Buzzard (May 29 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268652):
<p>so we can work out what this line does</p>

#### [ Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268719):
<p>and I work it out by having this pnat file open in Lean and just right clicking on subtype.val</p>

#### [ Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268723):
<p>and then selecting "go to definition"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268728):
<p>and then we find ourselves right in the heart of core lean</p>

#### [ Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268731):
<p>and we see</p>

#### [ Kevin Buzzard (May 29 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268733):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">subtype</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">property</span> <span class="o">:</span> <span class="n">p</span> <span class="n">val</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268742):
<p>and pnat, the positive naturals, was a subtype</p>

#### [ Kevin Buzzard (May 29 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268750):
<p>in fact if we switch notation off and look at pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268765):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="kn">notation</span> <span class="n">false</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">pnat</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268803):
<p>we see</p>

#### [ Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268808):
<p><code>def pnat : Type :=
subtype (λ (n : nat), gt n 0)</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268814):
<p>eew</p>

#### [ Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268816):
<p><code>gt</code> is <code>&gt;</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268824):
<p>so indeed we see a function nat to Prop</p>

#### [ Kevin Buzzard (May 29 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268827):
<p>sending n to "n &gt; 0"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268833):
<p>and we get a subtype, consisting of the n such that we have a proof that n &gt; 0</p>

#### [ Kevin Buzzard (May 29 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268846):
<p>and we see from the definition of the subtype structure that the <code>n</code> is the <code>val</code> and the proof is the <code>property</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268904):
<p>so subtype.val sends the pnat <code>⟨59,H⟩</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268905):
<p>to its value</p>

#### [ Kevin Buzzard (May 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268906):
<p>which is 59</p>

#### [ Kevin Buzzard (May 29 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268913):
<p>and we made it a coercion using coercion instance magic</p>

#### [ Kevin Buzzard (May 29 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268920):
<p>so that means it should happen naturally</p>

#### [ Kevin Buzzard (May 29 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268930):
<p>Ok it works!</p>

#### [ Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268987):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">H</span> <span class="o">:</span> <span class="mi">59</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">definition</span> <span class="n">x</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">59</span><span class="o">,</span><span class="n">H</span><span class="bp">⟩</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">pnat</span><span class="o">)</span> <span class="c1">-- x : pnat</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268991):
<p>it would be better if you could see me typing</p>

#### [ Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268992):
<p>that would save me having to cut and paste</p>

#### [ Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268993):
<p>how do I do that?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268994):
<p>Did someone say youtube ?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268996):
<p>Does twitch take this sort of stuff?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127268997):
<p>I have done all manner of weird things on twitch</p>

#### [ Patrick Massot (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269004):
<p>Yes, I don't understand why you don't record that and put it on youtube</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269008):
<p>because I'm just squeezing this in before I put the kids to bed</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269009):
<p>so back to the point</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269011):
<p>a miracle occurred!</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269012):
<p>A contradiction in type theory!</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269015):
<p>x had type pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269016):
<p>and type nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269019):
<p>as well</p>

#### [ Kevin Buzzard (May 29 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269021):
<p>but actually what happened was that coercion kicked in</p>

#### [ Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269062):
<p>The output of the second check was <code>↑x : ℕ</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269074):
<p>and that arrow (which you get with <code>\u</code>)</p>

#### [ Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269077):
<p>means "I got coerced!"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269084):
<p>so that has solved our first fundamental problem</p>

#### [ Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269086):
<p>which is that for a mathematician, pnat is a subset of nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269088):
<p>and hence every pnat _is_ a nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269092):
<p>They don't have it so easy in DTT</p>

#### [ Kevin Buzzard (May 29 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269100):
<p>so we are stuck with the cute little arrows</p>

#### [ Kevin Buzzard (May 29 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269107):
<p>let's press on</p>

#### [ Kevin Buzzard (May 29 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269120):
<p>The next line is clever</p>

#### [ Kevin Buzzard (May 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269146):
<p><code>def to_pnat (n : ℕ) (h : n &gt; 0 . tactic.exact_dec_trivial) : ℕ+ := ⟨n, h⟩</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269177):
<p>That's using a really cool piece of Lean functionality</p>

#### [ Kevin Buzzard (May 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269191):
<p>...which breaks if I remove that <code>import</code> line</p>

#### [ Kevin Buzzard (May 29 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269193):
<p>so that's why the import is there</p>

#### [ Kevin Buzzard (May 29 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269213):
<p>This is pretty much the rarest of ways to make a function input for Lean</p>

#### [ Patrick Massot (May 29 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269215):
<p>you could still hide the  cute little arrows from pp display though</p>

#### [ Kevin Buzzard (May 29 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269225):
<p>there's something in the manual about this</p>

#### [ Kevin Buzzard (May 29 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269228):
<p>you can do pp.no_cute_arrows Patrick?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269280):
<p>here we are</p>

#### [ Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269281):
<p><a href="https://leanprover.github.io/reference/expressions.html#implicit-arguments" target="_blank" title="https://leanprover.github.io/reference/expressions.html#implicit-arguments">https://leanprover.github.io/reference/expressions.html#implicit-arguments</a></p>

#### [ Patrick Massot (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269282):
<p><code>set_option pp.coercions false</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269286):
<p>does that mean Lean doesn't do them?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269290):
<p>or just doesn't print the arrows?</p>

#### [ Patrick Massot (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269291):
<p>doesn't print</p>

#### [ Kevin Buzzard (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269293):
<p>thought so :-)</p>

#### [ Patrick Massot (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269297):
<p>hence the pp</p>

#### [ Johan Commelin (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269299):
<p><code>pp</code> means "pretty print"</p>

#### [ Patrick Massot (May 29 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269300):
<p>meaning pretty print</p>

#### [ Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269305):
<p>presumably no setting of options can change Lean's behaviour?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269320):
<p>in pnat we have the last of the ways that Lean can make an implicit argument</p>

#### [ Patrick Massot (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269324):
<p><code>class.instance_max_depth</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269331):
<p>"run a tactic to make the argument for you"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269333):
<p>Patrick: touch\'e</p>

#### [ Kevin Buzzard (May 29 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269339):
<p><code>def to_pnat (n : ℕ) (h : n &gt; 0 . tactic.exact_dec_trivial) : ℕ+ := ⟨n, h⟩</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269389):
<p>means "take an input n, and then see if you can prove n &gt; 0 by using the tactic <code>tactic.exact_dec_trivial</code>"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269394):
<p>Let's see this tactic in action</p>

#### [ Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269414):
<p><code>theorem H : 59 &gt; 0 := by tactic.exact_dec_trivial</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269416):
<p>It works!</p>

#### [ Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269420):
<p>To find out what it does you can right click on it and it will be all tacticy stuff</p>

#### [ Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269422):
<p>so I'm not going to do that</p>

#### [ Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269424):
<p>but I know what is going on</p>

#### [ Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269425):
<p>in fact there's a shorter way of doing it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269430):
<p><code>theorem H : 59 &gt; 0 := dec_trivial</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269432):
<p>(not a tactic, so no <code>by</code> this time)</p>

#### [ Kevin Buzzard (May 29 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269485):
<p><code>dec_trivial</code> just means "&gt; is decidable on nat so just please decide this for me by proving it's true"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269505):
<p>apparently you can't use it to prove things are false though</p>

#### [ Kevin Buzzard (May 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269512):
<p><code>theorem H1 : 0 &gt; 0 := dec_trivial</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269514):
<p>doesn't work</p>

#### [ Kevin Buzzard (May 29 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269527):
<p>so let's see <code>to_pnat</code> in action!</p>

#### [ Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269542):
<p><code>definition y : pnat := to_pnat 12 </code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269579):
<p>that's much better than what we had before</p>

#### [ Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269595):
<p><code>definition z : pnat := to_pnat 0</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269600):
<p>you get some weird error</p>

#### [ Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269610):
<p>OK so let's press on</p>

#### [ Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269612):
<p><code>def succ_pnat (n : ℕ) : ℕ+ := ⟨succ n, succ_pos n⟩</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269616):
<p>this one looks easy.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269626):
<p>Given n a nat, we are building a pnat called <code>succ_pnat n</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269633):
<p>and you can guess from the name that it will be n + 1</p>

#### [ Kevin Buzzard (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269638):
<p>so I reckon that succ_pos n is going to be the theorem that n + 1 &gt; 0</p>

#### [ Kevin Buzzard (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269644):
<p>we can check that easily</p>

#### [ Mario Carneiro (May 29 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269659):
<p>Obviously you can't prove false things using <code>dec_trivial</code>, they're false</p>

#### [ Mario Carneiro (May 29 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269708):
<p>but you can prove the negation using <code>dec_trivial</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269733):
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">succ_pos</span> <span class="n">n</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269739):
<p><code>succ_pos n : 0 &lt; succ n</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269750):
<p>we could have right clicked and wandered back in to core lean or so, but this is another way</p>

#### [ Kevin Buzzard (May 29 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269767):
<p>So that's two maps from nat to pnat and a map from pnat to nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269774):
<p>It's certainly the case that we could imagine using both those maps</p>

#### [ Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269818):
<p>but what do we need to do next?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269824):
<p>This is the question that I as a mathematician find hard</p>

#### [ Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269825):
<p>and I think that people like Mario just somehow know</p>

#### [ Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269828):
<p>I'm just going to cheat and look at the code</p>

#### [ Kevin Buzzard (May 29 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269831):
<p><code>@[simp] theorem succ_pnat_coe (n : ℕ) : (succ_pnat n : ℕ) = succ n := rfl</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269845):
<p>OK so this says that given a nat, if we compute its successor as a pnat then it equals its successor as a nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269852):
<p>Notice the secret coercion! That equality is between a pnat and a nat</p>

#### [ Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269854):
<p>and Lean coerces the left hand side</p>

#### [ Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269855):
<p>so if you think about it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269857):
<p>when you unravel it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269860):
<p>that theorem just says <code>succ n = succ n</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269865):
<p>so the proof is <code>rfl</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269928):
<p>Ok now <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> told me that theorems whose proofs were rfl sometimes don't get names</p>

#### [ Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269932):
<p>but this one got lucky</p>

#### [ Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269934):
<p>it got a name</p>

#### [ Mario Carneiro (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269936):
<p>it's a simp lemma, those need names</p>

#### [ Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269940):
<p>and presumably that's because someone somewhere realised that this was a good simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269944):
<p>NOTE FOR BEGINNERS</p>

#### [ Mario Carneiro (May 29 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269946):
<p>also I'm not sure that's a good rule of thumb</p>

#### [ Mario Carneiro (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269960):
<p>rfl proofs are very common</p>

#### [ Kevin Buzzard (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269963):
<p>It's important that you get your simp lemma the right way round</p>

#### [ Kevin Buzzard (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269971):
<p>you don't want to prove that <code>succ n</code> equals <code>succ_pnat n</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269975):
<p>because that would be a comp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127269984):
<p>in maths it doesn't matter which order you put the things that are equal</p>

#### [ Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270022):
<p><code>x = y</code> and <code>y = x</code> mean the same thing</p>

#### [ Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270034):
<p>but in Lean you might want to consider putting the more complicated thing on the left</p>

#### [ Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270042):
<p>and then simp will simplify it to the right if it uses your lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270046):
<p>and even if simp does not use your lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270053):
<p>imagine when you're doing a rewrite</p>

#### [ Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270060):
<p>you are trying to prove something</p>

#### [ Kevin Buzzard (May 29 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270065):
<p>so you're usally trying to make stuff easier</p>

#### [ Kevin Buzzard (May 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270075):
<p>and you don't want to have to put left arrows everywhere because they look weird</p>

#### [ Kevin Buzzard (May 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270085):
<p>so, mathematicians everywhere, remember that THIS WEIRD CS WORLD IS ASYMMETRIC</p>

#### [ Kevin Buzzard (May 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270092):
<p>and if you've proved x = y, make sure x takes more characters to type</p>

#### [ Kevin Buzzard (May 29 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270097):
<p>or else you should have proved y = x</p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270142):
<p>Next line</p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270143):
<p><code>@[simp] theorem pos (n : ℕ+) : (n : ℕ) &gt; 0 := n.2</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270150):
<p>that looks like really poor Lean to me</p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270153):
<p>who wrote this file anyway</p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270156):
<p>oh I heard of that guy</p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270165):
<p>Now everyone knows that simp is used to prove _equalities_</p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270170):
<p>so all your simp lemmas should be _equalities_</p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270171):
<p>or _iff_s</p>

#### [ Kevin Buzzard (May 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270175):
<p>and anything which is a random thing like &gt;</p>

#### [ Kevin Buzzard (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270180):
<p>obviously should not be a simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270196):
<p>because simp, it turns out, does <em>not</em> stand for "this lemma is pretty simple"</p>

#### [ Mario Carneiro (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270200):
<p>This is useful for fulfulling side conditions in algebraic rules, which sometimes need that things are nonzero or positive</p>

#### [ Kevin Buzzard (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270203):
<p>it stands for "this lemma is appropriate for the simplifier"</p>

#### [ Kevin Buzzard (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270215):
<p>and 9 times out of 10 it's because it's an equality</p>

#### [ Patrick Massot (May 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270221):
<p>I disagree our equality is symmetric. Would you write some cohomological vanishing theorem as <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>0</mn><mo>=</mo><msup><mi>H</mi><mi>i</mi></msup><mo>(</mo><mi>X</mi><mo separator="true">,</mo><mi>F</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">0 = H^i(X, F)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.824664em;"></span><span class="strut bottom" style="height:1.0746639999999998em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">0</span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.08125em;">H</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.824664em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mclose">)</span></span></span></span>?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270268):
<p>but apparently there are other times when it's not</p>

#### [ Kevin Buzzard (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270285):
<p>Interesting point Patrick I guess you're right</p>

#### [ Kevin Buzzard (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270288):
<p>Maybe 0 is a special case</p>

#### [ Kevin Buzzard (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270303):
<p>The conclusion of this is that working out if something is a simp lemma is still something which I haven't got the hang of</p>

#### [ Mario Carneiro (May 29 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270309):
<p>most "let x = value" type statements have the variable on the left in math</p>

#### [ Patrick Massot (May 29 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270343):
<p>What about <span class="tex-error">$$\int_{-\infty}^\infty e^{-x^2} dx = \srqt\pi$$</span>?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270345):
<p>Now look at these</p>

#### [ Kevin Buzzard (May 29 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270348):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">pnat</span>

<span class="kn">open</span> <span class="n">nat</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">pos</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span>

<span class="kn">theorem</span> <span class="n">eq</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mk_coe</span> <span class="o">(</span><span class="n">n</span> <span class="n">h</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_add</span> <span class="bp">ℕ+</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">,</span> <span class="n">add_pos</span> <span class="n">m</span><span class="bp">.</span><span class="mi">2</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">add_coe</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">ne_zero</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">ne_of_gt</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270404):
<p>The last thing we want to do is to define random theorems like <code>ne_zero</code> (the last one) and have its actual name be <code>ne_zero</code> in the root namespace</p>

#### [ Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270408):
<p>I did that a lot when I started</p>

#### [ Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270416):
<p>The statement that if n is a pnat then n isn't zero -- clearly ne_zero is a good name for it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270417):
<p>but its full name is <code>pnat.ne_zero</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270423):
<p>like all the other pnat things we're going to do now</p>

#### [ Johan Commelin (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270429):
<p>So, why is <code>theorem eq</code> not a simp theorem?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270430):
<p>so that's why we opened the pnat namespace</p>

#### [ Kevin Buzzard (May 29 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270435):
<p>we namespaced</p>

#### [ Kevin Buzzard (May 29 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270438):
<p>and we opened nat for good measure</p>

#### [ Mario Carneiro (May 29 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270443):
<p>because the RHS has a variable not on the LHS</p>

#### [ Kevin Buzzard (May 29 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270452):
<p>So theorem <code>eq</code> says a fundamental thing about subtypes.</p>

#### [ Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270507):
<p>Remember -- a subtype is a term and then a proof of something that depends only on the term</p>

#### [ Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270516):
<p>so if we have two subtype things with the same term and different proofs, are they the same?</p>

#### [ Patrick Massot (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270520):
<p>What RHS variable?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270523):
<p>And yes they are, because all proofs are the same</p>

#### [ Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270526):
<p>so that's why pnat.eq is true</p>

#### [ Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270530):
<p>and indeed the proof is subtype.eq and you can guess what that says</p>

#### [ Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270532):
<p>or right click on ir</p>

#### [ Kevin Buzzard (May 29 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270534):
<p>it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270536):
<p>or #check it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270549):
<p>Oh I know why eq isn't a simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270550):
<p>it's not an equality</p>

#### [ Mario Carneiro (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270552):
<p><code>m = n</code> is not a simplification</p>

#### [ Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270555):
<p>it's an implication</p>

#### [ Mario Carneiro (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270559):
<p>and where is <code>n</code> coming from?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270567):
<p>aah</p>

#### [ Mario Carneiro (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270570):
<p>that's what I mean, <code>n</code> doesn't show up on the LHS</p>

#### [ Kevin Buzzard (May 29 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270575):
<p>There's another simp rule of thumb</p>

#### [ Kevin Buzzard (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270620):
<p>all the variables on the RHS should be in the LHS too</p>

#### [ Johan Commelin (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270625):
<p>Whenever I have to subtype thingies in my goal, and I need to prove that they are equal, Lean should always apply <code>subtype.eq</code>. I can't think of any reason why you wouldn't want to do that.</p>

#### [ Patrick Massot (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270626):
<p>why this rule?</p>

#### [ Kevin Buzzard (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270627):
<p>I should mention that to the guy who wrote the simp docs</p>

#### [ Mario Carneiro (May 29 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270637):
<p>It's an extensionality theorem</p>

#### [ Mario Carneiro (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270644):
<p>you don't always want it applied, because it complicates the goal</p>

#### [ Patrick Massot (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270651):
<p>should it be tagged as such?</p>

#### [ Mario Carneiro (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270655):
<p>probably</p>

#### [ Kevin Buzzard (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270657):
<p>More generally Johan, if you have two structures that are equal, you might want Lean to just decompose them and demand that you prove that all the bits you used to make them are equal</p>

#### [ Kevin Buzzard (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270666):
<p>but I think it would be a bit confusing if you were just motoring along and all of a sudden you have 10 goals</p>

#### [ Johan Commelin (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270670):
<blockquote>
<p>you don't always want it applied, because it complicates the goal</p>
</blockquote>
<p>Huh, the goal becomes easier, right? I just got rid of some irrelevant proofs...</p>

#### [ Kevin Buzzard (May 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270672):
<p>because you wanted to prove complicated structures were equal</p>

#### [ Kevin Buzzard (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270717):
<p>I think this sort of thing is an art</p>

#### [ Kevin Buzzard (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270731):
<p>I'm not sure what the best answer is but clearly Mario will speak from experience</p>

#### [ Mario Carneiro (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270732):
<p>you were trying to prove <code>m = n</code>, now you are proving <code>\u m = \u n</code></p>

#### [ Mario Carneiro (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270740):
<p>the goal got more complicated</p>

#### [ Mario Carneiro (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270744):
<p>sometimes that's what you want, but it needs to be an explicit choice</p>

#### [ Kevin Buzzard (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270745):
<p>Aah -- Johan -- if you actually had variables m and n which were pnats</p>

#### [ Kevin Buzzard (May 29 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270749):
<p>then you might well not want it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270756):
<p>but if m was explicitly <code>&lt;nat,proof&gt;</code></p>

#### [ Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270760):
<p>and so was n</p>

#### [ Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270766):
<p>then you might want it</p>

#### [ Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270767):
<p>(but you might not)</p>

#### [ Johan Commelin (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270774):
<p>Hmm, fair enough</p>

#### [ Mario Carneiro (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270775):
<p>and that version is a simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270789):
<p>ooh my son's gone</p>

#### [ Kevin Buzzard (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270791):
<p>I just inherited a second screen</p>

#### [ Johan Commelin (May 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270796):
<p>Ok, I have met subtypes where it was not a simp lemma, I think</p>

#### [ Kevin Buzzard (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270801):
<p>Ok so mk_coe</p>

#### [ Johan Commelin (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270811):
<p>Or is it a simp lemma for general subtypes?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270861):
<p>that says "make the subtype and then coerce back to nat and you're back where you started"</p>

#### [ Johan Commelin (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270864):
<p>Hmm, yes, let's move on with this chat</p>

#### [ Mario Carneiro (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270870):
<p><code>subtype.mk_eq_mk</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270885):
<p><code>@[simp] theorem mk_coe (n h) : ((⟨n, h⟩ : ℕ+) : ℕ) = n := rfl</code></p>

#### [ Mario Carneiro (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270888):
<p>it's a general simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270901):
<p>Actually there are several cool things about <code>mk_coe</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270918):
<p>first, it's something which I wanted for my structure and Mario said it didn't have a name</p>

#### [ Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270922):
<p>hmm</p>

#### [ Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270924):
<p>maybe that's not entirely true</p>

#### [ Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270933):
<p>Mario -- why does this lemma use coercion instead of val?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270937):
<p>They're definitionally equal, right?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270972):
<p>Does it matter which one you choose when making your structure?</p>

#### [ Mario Carneiro (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270986):
<p>it's a simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270995):
<p>But what about <code>(⟨n, h⟩ : ℕ+).val = n</code></p>

#### [ Mario Carneiro (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127270999):
<p>The val version is automatic, because simp knows about structures</p>

#### [ Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271006):
<p>or <code>subtype.val (⟨n, h⟩ : ℕ+) = n</code></p>

#### [ Mario Carneiro (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271010):
<p>but when the val is hidden in a coercion simp misses it</p>

#### [ Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271014):
<p>oh so simp doesn't need to be told that</p>

#### [ Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271017):
<p>the thing I wrote</p>

#### [ Kevin Buzzard (May 29 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271021):
<p>but does need to be told the thing you put in the file</p>

#### [ Mario Carneiro (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271030):
<p>right</p>

#### [ Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271036):
<p>You see -- there is so much subtlety in this stuff</p>

#### [ Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271045):
<p>I saw the definition of pnat in a maths lecture</p>

#### [ Mario Carneiro (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271048):
<p>I mean you could have it as a simp lemma if you want</p>

#### [ Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271050):
<p>it was "take nat and remove 0"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271054):
<p>and that was it</p>

#### [ Mario Carneiro (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271056):
<p>but it probably won't trigger</p>

#### [ Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271059):
<p>There is all this extra stuff here</p>

#### [ Kevin Buzzard (May 29 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271068):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_add</span> <span class="bp">ℕ+</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">,</span> <span class="n">add_pos</span> <span class="n">m</span><span class="bp">.</span><span class="mi">2</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">add_coe</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271073):
<p>We want add on pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271116):
<p>and here's something I only learnt recently</p>

#### [ Kevin Buzzard (May 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271134):
<p>the only purpose of <code>has_add</code> and the 20 or so other <code>has_notation</code> things</p>

#### [ Kevin Buzzard (May 29 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271138):
<p>is notation</p>

#### [ Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271143):
<p>The instance is so unimportant that it doesn't even deserve a name</p>

#### [ Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271155):
<p>although probably one could have called it <code>pnat.add</code></p>

#### [ Mario Carneiro (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271162):
<p>it gets an automatic name if you don't specify, in this case <code>pnat.has_add</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271167):
<p>The definition of add on pnat clearly needs a theorem -- it needs the theorem that if a&gt;0 and b&gt;0 then a+b&gt;0</p>

#### [ Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271170):
<p>Oh I didn't know that -- thanks</p>

#### [ Mario Carneiro (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271173):
<p><code>pnat.add</code> would be the name of the function itself</p>

#### [ Mario Carneiro (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271179):
<p>if it had a name</p>

#### [ Kevin Buzzard (May 29 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271181):
<p>Oh of course</p>

#### [ Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271222):
<p>The function is add</p>

#### [ Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271233):
<p>and the proof that it has an add is something else</p>

#### [ Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271243):
<p>actually it's not a proof</p>

#### [ Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271245):
<p>it's data</p>

#### [ Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271253):
<p>OK so we need to proev that if a&gt;0 and b&gt;0 then a+b&gt;0</p>

#### [ Kevin Buzzard (May 29 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271258):
<p>and we cheat and look at what Mario did</p>

#### [ Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271277):
<p>and why is the output from #check so ugly?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271284):
<p><code>#check add_pos </code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271291):
<p><code>add_pos : 0 &lt; ?M_3 → 0 &lt; ?M_4 → 0 &lt; ?M_3 + ?M_4</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271293):
<p>thanks Lean</p>

#### [ Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271299):
<p><code>#check @add_pos </code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271304):
<p><code>add_pos : ∀ {α : Type u_1} [_inst_1 : ordered_cancel_comm_monoid α] {a b : α}, 0 &lt; a → 0 &lt; b → 0 &lt; a + b</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271339):
<p>not ideal either</p>

#### [ Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271358):
<p>I would have preferred</p>

#### [ Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271364):
<p><code>0 &lt; a → 0 &lt; b → 0 &lt; a + b</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271371):
<p>but unsurprisingly</p>

#### [ Kevin Buzzard (May 29 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271376):
<p>it's the lemma we need</p>

#### [ Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271395):
<p>Now these should be straightforward</p>

#### [ Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271401):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">add_coe</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">ne_zero</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">ne_of_gt</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">nat_coe_coe</span>  <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="o">((</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">succ_pred_eq_of_pos</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">to_pnat&#39;_coe</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="n">n</span><span class="bp">.</span><span class="n">to_pnat&#39;</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">succ_pred_eq_of_pos</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">coe_nat_coe</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">eq</span> <span class="o">(</span><span class="n">nat_coe_coe</span> <span class="n">n</span><span class="bp">.</span><span class="n">pos</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271414):
<p>you see -- this is the advantage of making it a subtype</p>

#### [ Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271420):
<p>we have to carry around all these proofs</p>

#### [ Kevin Buzzard (May 29 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271425):
<p>but <code>add_coe</code> says "adding the pnats is the same as adding the nats, by definition"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271485):
<p>and indeed if you look at the coercion you can see that this is just a statement of the form X = X</p>

#### [ Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271500):
<p>ne_zero : we will need to prove n &gt; 0 -&gt; n ne 0</p>

#### [ Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271514):
<p>and it would not surprise me if that were called ne_of_gt</p>

#### [ Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271517):
<p>and note that</p>

#### [ Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271528):
<p><code>n.2</code> is the proof</p>

#### [ Kevin Buzzard (May 29 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271531):
<p>that n &gt; 0</p>

#### [ Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271536):
<p>it's <code>n.property</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271546):
<p>for kids who are too cool to write such a long thing</p>

#### [ Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271563):
<p><code>nat_coe_coe</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271565):
<p>I have no idea why this is a simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271571):
<p>I guess I do know</p>

#### [ Kevin Buzzard (May 29 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271573):
<p>it's kind of "well there's only a minor precondition"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271614):
<p>"and then we get some serious simplification"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271619):
<p>I am kind of surprised this works</p>

#### [ Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271626):
<p>we coerce a nat to a pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271632):
<p>that doesn't even make sense</p>

#### [ Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271635):
<p>oh crap</p>

#### [ Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271642):
<p>I am looking at an old version of pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271645):
<p>rofl</p>

#### [ Kevin Buzzard (May 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271669):
<p>I'm now looking at the up to date version</p>

#### [ Kevin Buzzard (May 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271672):
<p>and that line is gone :-)</p>

#### [ Kevin Buzzard (May 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271680):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">add_coe</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">ne_zero</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">ne_of_gt</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">to_pnat&#39;_coe</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="n">n</span><span class="bp">.</span><span class="n">to_pnat&#39;</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">succ_pred_eq_of_pos</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">coe_to_pnat&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span><span class="bp">.</span><span class="n">to_pnat&#39;</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">eq</span> <span class="o">(</span><span class="n">to_pnat&#39;_coe</span> <span class="n">n</span><span class="bp">.</span><span class="n">pos</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (May 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271682):
<blockquote>
<p>Last modified two days ago!<br>
Things never stand still around here</p>
</blockquote>

#### [ Kevin Buzzard (May 29 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271734):
<p>Things stand still with my mathlib install I can assure you :-)</p>

#### [ Kevin Buzzard (May 29 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271747):
<p>Ok great</p>

#### [ Kevin Buzzard (May 29 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271750):
<p><code>@[simp] theorem to_pnat'_coe {n : ℕ} : n &gt; 0 → (n.to_pnat' : ℕ) = n := succ_pred_eq_of_pos</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271766):
<p>that starts with a nat, uses <code>to_pnat'</code> to get to a pnat and then coerces back to a nat and the claim is we're back where we started</p>

#### [ Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271777):
<p><code>def to_pnat' (n : ℕ) : ℕ+ := succ_pnat (pred n)</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271778):
<p>Ok so this looks good</p>

#### [ Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271785):
<p>if you unravel then we're claiming that succ (pred n) = n</p>

#### [ Kevin Buzzard (May 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271786):
<p>and this is not rfl</p>

#### [ Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271789):
<p>indeed it's not even true</p>

#### [ Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271816):
<p>it's false for n=0</p>

#### [ Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271835):
<p>but we have the hypo n &gt; 0</p>

#### [ Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271843):
<p>so we need a lemma that says n &gt; 0 implies succ pred n = n</p>

#### [ Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271849):
<p>and that would be called something like <code>succ_pred_eq_of_pos</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271850):
<p>which it indeed is</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271869):
<p>Ok nearly there</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271876):
<p>oh one more simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271882):
<p>you see this is exactly what I don't get</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271885):
<p>who decides (a) what to prove (b) what to make a simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271889):
<p>We have just proved 10 trivial things</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271892):
<p><code>@[simp] theorem coe_to_pnat' (n : ℕ+) : (n : ℕ).to_pnat' = n := eq (to_pnat'_coe n.pos)</code></p>

#### [ Mario Carneiro (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271896):
<p>This is a very basic file, so it has almost nothing but simp lemmas</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271897):
<p>look!</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271899):
<p>We just proved <code>n = n</code> again</p>

#### [ Kevin Buzzard (May 29 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271902):
<p>let's make it a simp lemma!</p>

#### [ Kevin Buzzard (May 29 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271950):
<p>to_pnat' is a bit funny isn't it</p>

#### [ Kevin Buzzard (May 29 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271959):
<p><code>def to_pnat' (n : ℕ) : ℕ+ := succ_pnat (pred n)</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271964):
<p>sends n to n if n is positive</p>

#### [ Kevin Buzzard (May 29 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271967):
<p>and 0 to 1</p>

#### [ Kevin Buzzard (May 29 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271974):
<p>because nobody listens to me when I say it should be 37</p>

#### [ Mario Carneiro (May 29 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271991):
<p>hey, the succ pred thing wouldn't work with 37</p>

#### [ Kevin Buzzard (May 29 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127271992):
<p>and perhaps in this particular case they're right</p>

#### [ Kevin Buzzard (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272066):
<p>Ok so we basically think of every possible way we can move between nats and pnats and then figure out what is true and make every simplification a simp lemma</p>

#### [ Mario Carneiro (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272079):
<p>exactly</p>

#### [ Kevin Buzzard (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272088):
<p>Now here's a meaty bit of file</p>

#### [ Kevin Buzzard (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272092):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="bp">ℕ+</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">m</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">n</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">mul_pos</span> <span class="n">m</span><span class="bp">.</span><span class="mi">2</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">one</span>       <span class="o">:=</span> <span class="n">succ_pnat</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">one_mul</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">one_mul</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_one</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_one</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_comm</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_comm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272101):
<p>it's a commutative monoid!</p>

#### [ Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272109):
<p>You can see what Lean thinks the axioms for a commutative monoid are, right there</p>

#### [ Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272133):
<p>Now if I had been doing this I would have done <code>instance : has_mul pnat := &lt;...&gt;</code> first</p>

#### [ Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272135):
<p>outside the monoid</p>

#### [ Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272142):
<p>and I would have done <code>has_one pnat</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272147):
<p>Mario -- does your pnat have a mul?</p>

#### [ Mario Carneiro (May 29 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272150):
<p>yes, it's right there</p>

#### [ Mario Carneiro (May 29 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272203):
<p><code>comm_monoid</code> implies <code>has_mul</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272232):
<p>If I type <code>#print comm_monoid</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272243):
<p>I can't see this</p>

#### [ Kevin Buzzard (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272252):
<p>Do I have to look at the source code to see that comm_monoid extends has_mul?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272254):
<p>Or have I misunderstood?</p>

#### [ Mario Carneiro (May 29 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272264):
<p><code>comm_monoid</code> extends <code>monoid</code> which extends <code>semigroup</code> which extends <code>has_mul</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272268):
<p><code>class comm_monoid (α : Type u) extends monoid α, comm_semigroup α</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272331):
<p>but you had to know that</p>

#### [ Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272336):
<p>I could have written comm_monoid in a different way</p>

#### [ Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272338):
<p>and it would have _looked_ like there was a mul</p>

#### [ Kevin Buzzard (May 29 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272339):
<p>but you wouldn't have got the notation</p>

#### [ Kevin Buzzard (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272343):
<p>so I have to look in the source code to check my mul is a mul?</p>

#### [ Mario Carneiro (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272353):
<div class="codehilite"><pre><span></span>set_option pp.implicit true
#check (by apply_instance : has_mul ℕ+)
-- @semigroup.to_has_mul ℕ+ (@monoid.to_semigroup ℕ+ (@comm_monoid.to_monoid ℕ+ pnat.comm_monoid)) : has_mul ℕ+
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272357):
<p>The technical point here, for those wondering, is how I can get Lean to use the notation <code>*</code> for multiplication of pnats</p>

#### [ Mario Carneiro (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272369):
<p>you already have the notation</p>

#### [ Mario Carneiro (May 29 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272370):
<p>after that instance</p>

#### [ Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272409):
<p>after making it a commutative monoid</p>

#### [ Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272416):
<p>but you didn't know for sure that was going to happen</p>

#### [ Mario Carneiro (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272419):
<p>proving it's a comm monoid a fortiori implies it's a monoid and a has_mul and all that</p>

#### [ Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272425):
<p>you could only work it out by doing it and then checking that the multiplication notation stuck</p>

#### [ Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272430):
<p>with your #check</p>

#### [ Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272434):
<p>if you had wanted to know before writing the code</p>

#### [ Kevin Buzzard (May 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272436):
<p>you would have had to read Lean source code</p>

#### [ Mario Carneiro (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272444):
<p>If you define something with a <code>mul := </code> field it's in all likelihood extending <code>has_mul</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272451):
<p>you can't just work it out by querying the system</p>

#### [ Kevin Buzzard (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272458):
<p>exactly</p>

#### [ Kevin Buzzard (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272469):
<p>You had to rely on someone else being sensible</p>

#### [ Kevin Buzzard (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272471):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="bp">ℕ+</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">m</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">n</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">mul_pos</span> <span class="n">m</span><span class="bp">.</span><span class="mi">2</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">one</span>       <span class="o">:=</span> <span class="n">succ_pnat</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">one_mul</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">one_mul</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_one</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_one</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_comm</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_comm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Mario Carneiro (May 29 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272473):
<p>you can either read the code, the inheritance hierarchy, or get lean to tell you</p>

#### [ Kevin Buzzard (May 29 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272512):
<p>But you didn't get Lean to tell you</p>

#### [ Mario Carneiro (May 29 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272523):
<p>no because I knew that <code>comm_monoid</code> extends <code>has_mul</code> (and it wouldn't make sense any other way)</p>

#### [ Kevin Buzzard (May 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272538):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">tricky1</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">mul</span> <span class="o">:</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">G</span> <span class="bp">→</span> <span class="n">G</span><span class="o">)</span>
<span class="o">(</span><span class="n">tricky_bit</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (May 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272539):
<p>It is important that <code>has_mul</code> be declared only once though</p>

#### [ Kevin Buzzard (May 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272546):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">tricky2</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">has_mul</span> <span class="n">G</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">tricky_bit</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (May 29 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272555):
<p>only <code>tricky2</code> gets the notation, yes</p>

#### [ Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272596):
<p>but your method for checking this fails</p>

#### [ Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272607):
<p>because you can't make any instances</p>

#### [ Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272614):
<p><code>#check (by apply_instance : has_mul ℕ+)</code></p>

#### [ Kenny Lau (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272615):
<p>sorry, you can</p>

#### [ Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272620):
<p>your method relied on pnat existing</p>

#### [ Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272625):
<p>show me Kenny :-)</p>

#### [ Kenny Lau (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272628):
<p>just <code>sorry</code> everything</p>

#### [ Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272630):
<p>Fair enough</p>

#### [ Kevin Buzzard (May 29 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272634):
<p>even mul?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272638):
<p>(deleted)</p>

#### [ Kevin Buzzard (May 29 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272649):
<p>I seem to have wandered a bit</p>

#### [ Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272700):
<p>OK so what do we need for mul -- clearly we need a proof that if a &gt; 0 and b &gt; 0 then a * b &gt; 0, and we think of what a good name for this lemma would be, and we think "oh maybe <code>mul_pos_of_pos_of_pos</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272706):
<p>and then we think "wait a minute that's too long"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272707):
<p>why don't we just go with mul_pos</p>

#### [ Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272709):
<p>and indeed that's what it is</p>

#### [ Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272710):
<p>naming is an art</p>

#### [ Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272712):
<p>and it's another thing mathematicians are bad at</p>

#### [ Kevin Buzzard (May 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272713):
<p>The only training we get</p>

#### [ Kevin Buzzard (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272719):
<p>is "Now by lemma 3.1 and 3.2 we see that Theorem A is proved!"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272724):
<p>from our teachers</p>

#### [ Mario Carneiro (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272729):
<div class="codehilite"><pre><span></span>class tricky1 (G : Type) :=
(mul : G → G → G)
(tricky_bit : 0 = 1)

class tricky2 (G : Type) extends has_mul G :=
(tricky_bit : 0 = 1)

section
variables (G : Type) [tricky1 G]
#check (by apply_instance : has_mul G) --fail

instance tricky1.has_mul : has_mul G := ⟨tricky1.mul⟩

#check (by apply_instance : has_mul G) --fixed
end

section
variables (G : Type) [tricky2 G]
#check (by apply_instance : has_mul G) --success
end
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272739):
<p>There you go</p>

#### [ Kevin Buzzard (May 29 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272741):
<p>couldn't be easier</p>

#### [ Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272779):
<p>Now</p>

#### [ Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272783):
<p>how are we going to prove all these stupid axioms?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272786):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="bp">ℕ+</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">m</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">n</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">mul_pos</span> <span class="n">m</span><span class="bp">.</span><span class="mi">2</span> <span class="n">n</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">one</span>       <span class="o">:=</span> <span class="n">succ_pnat</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">one_mul</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">one_mul</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_one</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_one</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_comm</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">mul_comm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272787):
<p>mul_assoc -- that's already proved for nats</p>

#### [ Kevin Buzzard (May 29 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272789):
<p>as is mul_comm</p>

#### [ Kevin Buzzard (May 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272795):
<p>and the full proof of mul_comm is quite long if you have defined pnat as an inductive type with one and succ</p>

#### [ Kevin Buzzard (May 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272804):
<p>so here we see the benefits</p>

#### [ Kevin Buzzard (May 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272821):
<p>the proof of mul_comm is "to check a * b = b * a, all we have to do is to check the underlying nats are the same, which is true because that's mul_comm for nat"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272827):
<p>was subtype.eq a simp lemma?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272867):
<p>oh no</p>

#### [ Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272869):
<p>of course not</p>

#### [ Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272871):
<p>it has an implies</p>

#### [ Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272875):
<p>so we can't hope to prove that with simp I guess</p>

#### [ Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272878):
<p>all the proofs are the same</p>

#### [ Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272885):
<p>on the other hand it still feels like a machine could have written those four proofs</p>

#### [ Kevin Buzzard (May 29 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272888):
<p>whereas I suspect Mario wrote them</p>

#### [ Kevin Buzzard (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272905):
<p>Mario, why isn't there some weird tactic which deduces a bunch of lemmas for subtypes from the corresponding lemmas for the types?</p>

#### [ Patrick Massot (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272907):
<p>We still have no conclusive proof that Mario is not a machine</p>

#### [ Kevin Buzzard (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272910):
<p>true</p>

#### [ Patrick Massot (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272916):
<p>This situation looks like what Simon solve for pi instances</p>

#### [ Kevin Buzzard (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272917):
<p>People like Simon Hudon are good at writing that sort of thing</p>

#### [ Patrick Massot (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272921):
<p>Where is Simon by the way?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272956):
<p>he's cool -- don't underestimate him</p>

#### [ Patrick Massot (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272960):
<p>Haven't we lost him?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272965):
<p>All that's left is <code>one</code></p>

#### [ Mario Carneiro (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272967):
<p>because the proof is so short it's not worth automating</p>

#### [ Mario Carneiro (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272970):
<p>there is a balance point there</p>

#### [ Kevin Buzzard (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272976):
<p>and Mario used succ_pnat, there were 5 other ways he could have done it, I am pretty sure that 1 &gt; 0 is a named theorem, he could have used that</p>

#### [ Kevin Buzzard (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272981):
<p>I don't think it matters</p>

#### [ Mario Carneiro (May 29 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272982):
<p>If I had to define a hundred more like that, sure</p>

#### [ Kevin Buzzard (May 29 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272985):
<p>I think every method will produce basically the same term</p>

#### [ Kevin Buzzard (May 29 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272994):
<p>All that's left is this:</p>

#### [ Kevin Buzzard (May 29 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127272996):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">one_coe</span> <span class="o">:</span> <span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mul_coe</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">m</span> <span class="bp">*</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="c">/-</span><span class="cm">- The power of a pnat and a nat is a pnat. -/</span>
<span class="n">def</span> <span class="n">pow</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ+</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">m</span> <span class="err">^</span> <span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pos_pow_of_pos</span> <span class="bp">_</span> <span class="n">m</span><span class="bp">.</span><span class="n">pos</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_pow</span> <span class="bp">ℕ+</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">pow</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">pow_coe</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">m</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">m</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">end</span> <span class="n">pnat</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273053):
<p>one_coe -- who knows why this is a simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273057):
<p>Where does it end</p>

#### [ Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273060):
<p>two_coe? Why is that not a simp lemma?</p>

#### [ Mario Carneiro (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273064):
<p>because that's not an atomic term</p>

#### [ Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273068):
<p>mul_coe -- proof is refl</p>

#### [ Kevin Buzzard (May 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273072):
<p>Oh I see</p>

#### [ Kevin Buzzard (May 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273075):
<p>one just _became_ an atomic term</p>

#### [ Mario Carneiro (May 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273076):
<p>the simp lemma would be about <code>\u bit0 n = bit0 \u n</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273084):
<p>when you decided that the fact that it was a monoid was worth proving</p>

#### [ Kevin Buzzard (May 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273097):
<p>and finally power</p>

#### [ Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273144):
<p>There's a has_pow thing instance. That presumably is tied to the <code>^</code> notation</p>

#### [ Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273146):
<p>how new-fangled and fancy</p>

#### [ Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273149):
<p>it wasn't like this when I learnt it</p>

#### [ Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273154):
<p><code>#print notation ^</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273157):
<p><code>_ </code>^<code>:80 _:79 := has_pow.pow #1 #0</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273169):
<p>Ok so the definition of pow is "work out pow in nats"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273180):
<p>but you now need to prove that if m&gt;0 and n&gt;=0 then m^n&gt;0</p>

#### [ Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273182):
<p>and if this was me 6 months ago</p>

#### [ Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273186):
<p>I would think "oh I quite fancy this one"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273188):
<p>"induction on n should do it"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273190):
<p>and I'd prove it</p>

#### [ Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273229):
<p>but that's not the way to think about Lean</p>

#### [ Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273230):
<p>the way to think about it is</p>

#### [ Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273239):
<p>"this looks pretty standard -- m &gt; 0 implies m^n &gt; 0"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273245):
<p>maybe the person who was implementing pow on nat thought of this</p>

#### [ Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273248):
<p>and even if they didn't</p>

#### [ Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273253):
<p>maybe some obsessive mathlib guy thought of it</p>

#### [ Kevin Buzzard (May 29 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273259):
<p>and maybe they gave it a name</p>

#### [ Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273273):
<p>and maybe it's someething like <code>pos_pow_of_pos</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273279):
<p>This is the way to write Lean</p>

#### [ Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273282):
<p>don't write the code because you can</p>

#### [ Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273287):
<p>try and find the code someone else wrote already that does it</p>

#### [ Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273291):
<p>write <code>nat.pos_pow</code> and hit ctrl-space</p>

#### [ Kevin Buzzard (May 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273292):
<p>and see if you get lucky</p>

#### [ Kevin Buzzard (May 29 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273351):
<p>note that Mario used <code>m.pos</code> not <code>m.2</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273355):
<p>That might just be for readability</p>

#### [ Kevin Buzzard (May 29 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273359):
<p>The philosophy is that <code>m.2</code> is something Lean will always offer you</p>

#### [ Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273364):
<p>but <code>m.pos</code> is basically better</p>

#### [ Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273371):
<p>because it's more readable</p>

#### [ Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273375):
<p><code>@[simp] theorem pos (n : ℕ+) : (n : ℕ) &gt; 0 := n.2</code></p>

#### [ Mario Carneiro (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273376):
<p>I'm sure it's just inconsistency</p>

#### [ Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273380):
<p>But you are making an interface for pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273388):
<p>and that interface should involve a nice name for the assertion that a positive nat is positive</p>

#### [ Mario Carneiro (May 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273390):
<p>of course it doesn't matter at all what gets used in the proof</p>

#### [ Kevin Buzzard (May 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273425):
<p>which you should encourage the users to use</p>

#### [ Kevin Buzzard (May 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273442):
<p>It literally makes no difference to anything?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273449):
<p>Doesn't it increase compile time by a zillisecond?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273456):
<p>you had to look up <code>pos</code> in some table</p>

#### [ Mario Carneiro (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273464):
<p>It's not literally the same proof term, and who knows how compile time is affected, but whatever difference is extremely minimal</p>

#### [ Kevin Buzzard (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273472):
<p>Let me think epsilon more about poe</p>

#### [ Kevin Buzzard (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273474):
<p>pow</p>

#### [ Kevin Buzzard (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273481):
<p>What is going through the writer's mind when they write this</p>

#### [ Kevin Buzzard (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273492):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- The power of a pnat and a nat is a pnat. -/</span>
<span class="n">def</span> <span class="n">pow</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ+</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">m</span> <span class="err">^</span> <span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pos_pow_of_pos</span> <span class="bp">_</span> <span class="n">m</span><span class="bp">.</span><span class="n">pos</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (May 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273493):
<p>note that projection notation in both cases only works if <code>n</code> has visible type pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273503):
<p>They are thinking "yay we now have pow"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273548):
<p>but then <em>immediately after</em></p>

#### [ Kevin Buzzard (May 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273555):
<p>they think "OK I now have some obligations"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273562):
<p>There's the obvious one -- make an instance of has_pow, which is just an elaborate way of saying "let's enable <code>^</code> notation"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273568):
<p>but then there's the less obvious (to me) fact:</p>

#### [ Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273571):
<p>which we've seen lots of times before</p>

#### [ Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273576):
<p>we want to check that powers in pnat agree with powers in nat</p>

#### [ Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273578):
<p>and even though the proof is refl</p>

#### [ Kevin Buzzard (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273580):
<p>this looks like it should be a simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273634):
<p>It says "if we coerce m ^ n to nat we get what we expect"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273641):
<p>That is a way of thinking which is not normally taught to the mathematician</p>

#### [ Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273650):
<p>to define pow : pnat -&gt; nat -&gt; nat we just use induction</p>

#### [ Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273652):
<p>to prove it lands in pnat we prove a lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273653):
<p>and that's the end</p>

#### [ Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273654):
<p>We stop here:</p>

#### [ Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273655):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">pow</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ+</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">m</span> <span class="err">^</span> <span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pos_pow_of_pos</span> <span class="bp">_</span> <span class="n">m</span><span class="bp">.</span><span class="n">pos</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_pow</span> <span class="bp">ℕ+</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">pow</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273657):
<p>We don't do this bit</p>

#### [ Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273659):
<p><code>@[simp] theorem pow_coe (m : ℕ+) (n : ℕ) : (↑(m ^ n) : ℕ) = m ^ n := rfl</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273662):
<p>but in CS if you don't do this</p>

#### [ Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273704):
<p>then your users moan that they used a pnat 50 lines ago and it won't disappear</p>

#### [ Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273705):
<p>even though we only care about nats now</p>

#### [ Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273710):
<p>in fact did we prove all the coercions?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273711):
<p><code>@[simp] theorem mul_coe (m n : ℕ+) : ((m * n : ℕ+) : ℕ) = m * n := rfl</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273716):
<p><code>@[simp] theorem one_coe : ((1 : ℕ+) : ℕ) = 1 := rfl</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273723):
<p><code>@[simp] theorem add_coe (m n : ℕ+) : ((m + n : ℕ+) : ℕ) = m + n := rfl</code></p>

#### [ Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273733):
<p>They all got proved</p>

#### [ Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273744):
<p>Does that mean that if I have some complicated number made using lots of pnats and addition and multiplication etc</p>

#### [ Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273745):
<p>and then I made it a nat</p>

#### [ Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273747):
<p>then simp would remove all the pnats for me?</p>

#### [ Kevin Buzzard (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273748):
<p>I think it might!</p>

#### [ Kevin Buzzard (May 29 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273796):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">hc</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273811):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">A</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">ha</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">B</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="n">hb</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">C</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span><span class="n">hc</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273818):
<p>One thing I learnt a while ago was that instead of asking "can Lean do this"</p>

#### [ Kevin Buzzard (May 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273822):
<p>it's not hard to just make Lean try to do it yourself</p>

#### [ Kevin Buzzard (May 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273827):
<p>you just use variables to make stuff</p>

#### [ Kevin Buzzard (May 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273890):
<p>rofl</p>

#### [ Kevin Buzzard (May 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273906):
<p>I need to work harder</p>

#### [ Kevin Buzzard (May 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273925):
<p>dammit</p>

#### [ Kevin Buzzard (May 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273937):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">hb</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">hc</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span>
<span class="n">def</span> <span class="n">A</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">ha</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">B</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="n">hb</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">C</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span><span class="n">hc</span><span class="bp">⟩</span>


<span class="kn">example</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">*</span> <span class="o">(</span><span class="n">A</span> <span class="bp">+</span> <span class="n">B</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">C</span> <span class="bp">+</span> <span class="o">(</span><span class="n">A</span> <span class="bp">+</span> <span class="n">B</span><span class="o">))</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">c</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273974):
<p>doesn't typecheck yet</p>

#### [ Mario Carneiro (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127273996):
<p>Note that <code>A</code> and <code>B</code> are the same</p>

#### [ Mario Carneiro (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274000):
<p>You should use <code>parameters</code> instead</p>

#### [ Kevin Buzzard (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274008):
<p>for a b c</p>

#### [ Kevin Buzzard (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274009):
<p>what about the proofs?</p>

#### [ Mario Carneiro (May 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274010):
<p>all six</p>

#### [ Kevin Buzzard (May 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274039):
<p>Parameters can only be used in a section</p>

#### [ Kevin Buzzard (May 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274043):
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">hb</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">hc</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span>
<span class="n">def</span> <span class="n">A</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">ha</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">B</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="n">hb</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">C</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span><span class="n">hc</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="n">A</span> <span class="bp">*</span> <span class="o">(</span><span class="n">A</span> <span class="bp">+</span> <span class="n">B</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">C</span> <span class="bp">+</span> <span class="o">(</span><span class="n">A</span> <span class="bp">+</span> <span class="n">B</span><span class="o">))</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">c</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="kn">section</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274085):
<p>and this typechecks</p>

#### [ Kevin Buzzard (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274092):
<p>now let's remove the sorry (which I put there for typechecky reasons)</p>

#### [ Kevin Buzzard (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274093):
<p>maybe that's something I could mention</p>

#### [ Kevin Buzzard (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274098):
<p>I like my lean files to have no red squiggly underlines ever</p>

#### [ Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274102):
<p>but I am happy with plenty of sorrys</p>

#### [ Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274108):
<p>green squiggly underlines ftw</p>

#### [ Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274111):
<p>the reason for this</p>

#### [ Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274113):
<p>is that if you make an error</p>

#### [ Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274116):
<p>then sometimes your new red squiggly underline appears in a weird place</p>

#### [ Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274118):
<p>and you might not notice it if they're everywhere</p>

#### [ Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274121):
<p>so every time I split in tactic mode</p>

#### [ Kevin Buzzard (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274123):
<p>I always put in two sorrys</p>

#### [ Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274162):
<p>etc etc</p>

#### [ Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274174):
<p><code>example : (A * (A + B) * (C + (A + B)) : ℕ) = a * (a + b) * (c + (a + b)) := rfl </code></p>

#### [ Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274181):
<p>that's not surprising</p>

#### [ Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274188):
<p><code>example : ↑(A * (A + B) * (C + (A + B))) = a * (a + b) * (c + (a + b)) := rfl </code></p>

#### [ Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274193):
<p>that's not surprising</p>

#### [ Kevin Buzzard (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274201):
<p>why did he make all these rfl things simp lemmas?</p>

#### [ Kevin Buzzard (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274217):
<p><code>example : ↑(A * (A + B) * (C + (A + B))) = a * (a + b) * (c + (a + b)) := by simp  </code></p>

#### [ Kevin Buzzard (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274218):
<p>fails :-)</p>

#### [ Kevin Buzzard (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274222):
<p><em>doh</em></p>

#### [ Kevin Buzzard (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274232):
<p>aah well so it was probably for another reason</p>

#### [ Kevin Buzzard (May 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274284):
<p>but at least we made it to the end, even if I'm still not 100% sure what makes a good simp lemma. Maybe I'm beginning to get the hang of it.</p>

#### [ Mario Carneiro (May 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274294):
<p>You have to unfold your new definitions</p>

#### [ Kevin Buzzard (May 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274295):
<p>But it's interesting to see the way of thinking -- put new structure on pnat, now immediately ask yourself if we need some lemmas</p>

#### [ Mario Carneiro (May 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274299):
<p>try <code>by simp [A, B, C]</code></p>

#### [ Kevin Buzzard (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274314):
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">hb</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">hc</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span>
<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">A</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">ha</span><span class="bp">⟩</span>
<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">B</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="n">hb</span><span class="bp">⟩</span>
<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">C</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span><span class="n">hc</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="n">A</span> <span class="bp">*</span> <span class="o">(</span><span class="n">A</span> <span class="bp">+</span> <span class="n">B</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">C</span> <span class="bp">+</span> <span class="o">(</span><span class="n">A</span> <span class="bp">+</span> <span class="n">B</span><span class="o">))</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">c</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">))</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>

<span class="kn">end</span> <span class="kn">section</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274321):
<p>That works because I told Lean to unfold A B and C eagerly</p>

#### [ Kevin Buzzard (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274333):
<p><code>simp [A,B,C]</code>?</p>

#### [ Kevin Buzzard (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274336):
<p>Is <code>A</code> a good simp lemma??</p>

#### [ Kevin Buzzard (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274383):
<p>Normally when you start putting <code>simp [random thing]</code> it complains that the random thing isn't a good simp lemma</p>

#### [ Kevin Buzzard (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274392):
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span>
<span class="kn">parameters</span> <span class="o">{</span><span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">hb</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">hc</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span>
<span class="n">def</span> <span class="n">A</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span><span class="n">ha</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">B</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span><span class="n">hb</span><span class="bp">⟩</span>
<span class="n">def</span> <span class="n">C</span> <span class="o">:</span> <span class="n">pnat</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span><span class="n">hc</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="n">A</span> <span class="bp">*</span> <span class="o">(</span><span class="n">A</span> <span class="bp">+</span> <span class="n">B</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">C</span> <span class="bp">+</span> <span class="o">(</span><span class="n">A</span> <span class="bp">+</span> <span class="n">B</span><span class="o">))</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">c</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">))</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">A</span><span class="o">,</span><span class="n">B</span><span class="o">,</span><span class="n">C</span><span class="o">]</span>


<span class="kn">end</span> <span class="kn">section</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274396):
<p>well blow me down it works</p>

#### [ Mario Carneiro (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274400):
<p><code>simp [my_def]</code> where <code>my_def</code> is a <code>def</code> means <code>simp [my_def.&lt;equation lemmas&gt;]</code></p>

#### [ Kevin Buzzard (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274405):
<p>ooh</p>

#### [ Kevin Buzzard (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274411):
<p>How do I see A's equation lemmas?</p>

#### [ Kevin Buzzard (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274420):
<p><code>#print prefix A </code></p>

#### [ Kevin Buzzard (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274428):
<div class="codehilite"><pre><span></span><span class="n">A</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">{</span><span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">},</span> <span class="bp">ℕ+</span>
<span class="n">A</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">{</span><span class="n">ha</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">},</span> <span class="n">A</span> <span class="bp">=</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">ha</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274479):
<p>That doesn't look like a good simp lemma to me</p>

#### [ Mario Carneiro (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274482):
<p>not by default, no</p>

#### [ Kevin Buzzard (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274486):
<p>there are variables on the RHS which don't appear on the LHS</p>

#### [ Mario Carneiro (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274492):
<p>Actually they appear on the left too</p>

#### [ Kevin Buzzard (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274498):
<p>and a wise person once told me not to put these into simp</p>

#### [ Mario Carneiro (May 29 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274501):
<p>they are hidden because of the parameter thing</p>

#### [ Mario Carneiro (May 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274521):
<p>or possibly because you have <code>{a} {ha}</code></p>

#### [ Kevin Buzzard (May 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274523):
<p>heh</p>

#### [ Kevin Buzzard (May 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274524):
<p>I think the latter</p>

#### [ Kevin Buzzard (May 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274531):
<p>Ok so we got there</p>

#### [ Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274569):
<p>and that's pnat.</p>

#### [ Mario Carneiro (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274572):
<p>if they didn't appear on the left, you could use this theorem to prove 1 = 2</p>

#### [ Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274578):
<p>Oh that would be a cool application of pnat</p>

#### [ Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274586):
<p>I need to go to tend to the family</p>

#### [ Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274589):
<p>but there's a random thing</p>

#### [ Kevin Buzzard (May 29 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274593):
<p>which people will be able to link to and look at later on</p>

#### [ Kevin Buzzard (May 29 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274605):
<p>and in particular in a couple of weeks when I am supposed to be teaching a bunch of mathematicians Lean and they don't know how to make structures</p>

#### [ Kevin Buzzard (May 29 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274610):
<p>and it was much easier to write than a proper document</p>

#### [ Kevin Buzzard (May 29 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/LIVE%20CHAT%3A%20Structures%20for%20mathematicians/near/127274613):
<p>Thanks for the help Mario and Patrick and Johan and others</p>


{% endraw %}
