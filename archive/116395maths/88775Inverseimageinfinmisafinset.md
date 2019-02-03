---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/88775Inverseimageinfinmisafinset.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Inverse image in `fin m` is a `finset`](https://leanprover-community.github.io/archive/116395maths/88775Inverseimageinfinmisafinset.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 16 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126647766):
<p>The following code is (obviously) not typechecking. How do I make this work?</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">finvj</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">exact</span> <span class="o">{</span><span class="n">i</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">j</span><span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 16 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648041):
<p>Well, I guess <code>{i // f i = j}</code> has type <code>Type</code></p>

#### [ Kevin Buzzard (May 16 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648075):
<p>and you want something of type <code>finset (fin m)</code></p>

#### [ Kevin Buzzard (May 16 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648124):
<p>so I guess you'd better find a way of constructing something of type <code>finset (fin m)</code></p>

#### [ Kevin Buzzard (May 16 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648132):
<p>I don't know the first thing about finsets so I guess I start with <code>#print finset</code></p>

#### [ Kevin Buzzard (May 16 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648144):
<p>oh and that doesn't look too good</p>

#### [ Kevin Buzzard (May 16 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648158):
<p>you seem to have to supply a multiset and a proof that this multiset has no duplicates</p>

#### [ Kevin Buzzard (May 16 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648215):
<p>but fortunately finset is in mathlib so there will probably exist a good interface</p>

#### [ Kevin Buzzard (May 16 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648230):
<p>which in this case will mean "other constructors"</p>

#### [ Kevin Buzzard (May 16 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648235):
<p>so next I guess I'd have a look at <code>finset.lean</code></p>

#### [ Kevin Buzzard (May 16 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648257):
<p>or maybe I could look for other constructors by typing <code>finset.</code> in VS code and then hitting ctrl-space a while</p>

#### [ Kevin Buzzard (May 16 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648415):
<p>oh -- <code>finset.filter</code> exists</p>

#### [ Chris Hughes (May 16 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648416):
<p><code>univ.filter (\la i, f i = j)</code></p>
<p>I think you might need the finset  namespace open.</p>

#### [ Kevin Buzzard (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648422):
<p>aah, here's a finset expert</p>

#### [ Johan Commelin (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648430):
<p>Aah, cool.</p>

#### [ Kevin Buzzard (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648432):
<p>but I was seconds ahead of him ;-)</p>

#### [ Johan Commelin (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648437):
<p>Yeah, congrats (-;</p>

#### [ Johan Commelin (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648438):
<p>I'll look at filter!</p>

#### [ Kevin Buzzard (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648456):
<p>I was just showing you how I think about these things of course</p>

#### [ Kevin Buzzard (May 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648489):
<p>but actually in retrospect I missed a trick</p>

#### [ Kevin Buzzard (May 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648503):
<p>Instead of saying "I wonder what's there -- let's take a look at everything"</p>

#### [ Kevin Buzzard (May 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648510):
<p>I should have said "let's assume everything is there -- what do I actually want?"</p>

#### [ Kevin Buzzard (May 16 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648523):
<p>and what I want is (1) fin n is a finset and (2) a subset of a finset defined by a predicate being true is a finset</p>

#### [ Kevin Buzzard (May 16 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648532):
<p>and I should by now know that (2) is called <code>filter</code></p>

#### [ Johan Commelin (May 16 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648537):
<p>And I learned that today (-;</p>

#### [ Johan Commelin (May 16 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648541):
<p>I did not yet find out (1)...</p>

#### [ Johan Commelin (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648587):
<p>Chris's answer isn't working flawlessly here</p>

#### [ Kevin Buzzard (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648591):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> How does one prove fin n is a finset?</p>

#### [ Johan Commelin (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648600):
<p>My search continues</p>

#### [ Kevin Buzzard (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648614):
<p>it'll be there somewhere</p>

#### [ Kevin Buzzard (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648618):
<p>hmm</p>

#### [ Kevin Buzzard (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648620):
<p>it's somehow not strictly speaking meaningful</p>

#### [ Kevin Buzzard (May 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648635):
<p>fin n is not a finset -- fin n and something of type finset are different things</p>

#### [ Chris Hughes (May 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648637):
<p>fin n is not a finset. It is a fintype, and that should be automatically deduced as an instance</p>

#### [ Kevin Buzzard (May 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648639):
<p>right</p>

#### [ Chris Hughes (May 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648646):
<p>sometimes (univ : finset (fin n)) helps</p>

#### [ Kevin Buzzard (May 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648698):
<p>Johan -- why do you want to use finset?</p>

#### [ Chris Hughes (May 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648699):
<p>because otherwise it doesn't know the intended type. Also import data.fintype</p>

#### [ Kevin Buzzard (May 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648736):
<p>"set" doesn't mean what mathematicians think it means</p>

#### [ Kevin Buzzard (May 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648742):
<p>"set" in Lean means "subset of a set"</p>

#### [ Kevin Buzzard (May 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648749):
<p>"subset of a given type"</p>

#### [ Kevin Buzzard (May 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648751):
<p>rather than "arbitrary set of anything"</p>

#### [ Kevin Buzzard (May 16 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648797):
<p>This took me a while to get my head around</p>

#### [ Kevin Buzzard (May 16 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648813):
<p>"X : set N" doesn't mean "X is a proof that N is a set", it means "X is a subset of N". I sometimes read "set" as "subset_of".</p>

#### [ Kevin Buzzard (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648912):
<p>Because fin n is a type, and you have a predicate on that type, the natural thing to make is either a subtype or a <code>set (fin m)</code></p>

#### [ Johan Commelin (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648916):
<p>Kevin, I want to use finset, because I want to sum a function over it.</p>

#### [ Johan Commelin (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648928):
<p>And finset's have all sorts of stuff for that</p>

#### [ Kevin Buzzard (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648930):
<p>My guess is that any type with a reasonable finiteness property will have sums</p>

#### [ Kevin Buzzard (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648934):
<p>with all sorts of stuff</p>

#### [ Kevin Buzzard (May 16 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648945):
<p>but on the other hand maybe finsets have the stuff you need</p>

#### [ Johan Commelin (May 16 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648965):
<p>I couldn't find it for fin</p>

#### [ Kevin Buzzard (May 16 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126648968):
<p>In which case I think Chris' answer sounds best. Why not do the dirty work with fintype (which presumably also has filter) and then turn it into a finset</p>

#### [ Kevin Buzzard (May 16 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649037):
<p>hmm I don't know what a fintype is either</p>

#### [ Kevin Buzzard (May 16 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649039):
<p>well, I just looked</p>

#### [ Kevin Buzzard (May 16 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649042):
<p>I know nothing about these finite gadgets</p>

#### [ Chris Hughes (May 16 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649043):
<p>It's only finsets that have sums.</p>

#### [ Kevin Buzzard (May 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649089):
<p>but there's a coercion from fintype to finset?</p>

#### [ Chris Hughes (May 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649103):
<p>There is a function from fintype to finset. It's not a coercion.</p>

#### [ Chris Hughes (May 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649106):
<p>It's called univ</p>

#### [ Kevin Buzzard (May 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649109):
<p><code>example (m : ℕ) : fintype (fin m) := by apply_instance</code></p>

#### [ Kevin Buzzard (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649110):
<p>that's a good start</p>

#### [ Kevin Buzzard (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649123):
<p>type class inference will tell you that (fin m) is a fintype</p>

#### [ Johan Commelin (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649138):
<p>Yes, it's working now</p>

#### [ Kevin Buzzard (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649139):
<p>OK great</p>

#### [ Johan Commelin (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649143):
<p>So now I can start mangling around with my sums</p>

#### [ Johan Commelin (May 16 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649144):
<p>(-;</p>

#### [ Kevin Buzzard (May 16 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649185):
<p>Now it's Patrick you want to talk to :-)</p>

#### [ Johan Commelin (May 16 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649186):
<p>But first I need to catch a train</p>

#### [ Johan Commelin (May 16 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649187):
<p>Yes, I am using big_ops</p>

#### [ Patrick Massot (May 16 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649343):
<p>Actually I currently focused on non-commutative operations. That's why I can't work with finite sets. I'm summing (or multiplying or composing or whatever) elements of (ordered!) lists</p>

#### [ Patrick Massot (May 16 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649408):
<p>That's why I can't use <code>algebra.big_operators</code></p>

#### [ Chris Hughes (May 16 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20in%20%60fin%20m%60%20is%20a%20%60finset%60/near/126649647):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> <code>algebra.big_operators</code> is probably better than Patrick's big operators in this case.</p>


{% endraw %}
