---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00248multiset.html
---

## Stream: [general](index.html)
### Topic: [multiset](00248multiset.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 12 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129522842):
<p><span class="user-mention" data-user-id="120469">@Ellen Arlt</span> and I are putting <code>multiset.lean</code> through its paces.</p>
<p>Q1) This is perhaps a question about general lean/mathlib conventions disguised as a question about multisets. We have been working with multisets of size 0 and 1 and proving basic API lemmas. Initially I was using <code>∅</code> to denote the empty multiset (this is defined in mathlib, it's not my definition). I was surprised to find that <code>multiset.card (∅ : multiset α) = 0</code> was not a simp lemma (its proof is <code>rfl</code> but it can still be a simp lemma, right?) so I went to data.multiset to decide where to add it. And there I found that <code>multiset.card (0  : multiset α) = 0</code> <em>was</em> a simp lemma:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>

<span class="kn">example</span>  <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- fails</span>
</pre></div>


<p>Is this an example of the "pecking order" CS thing? Does it say "yes, <code>∅</code> and <code>0</code> are the same multiset, but if you need to refer to this multiset then mathlib asks that you use <code>0</code>"? If I'm right, how is one supposed to figure this sort of thing out? The hard way, like I did?</p>
<p>Q2) <code>multiset.strong_induction_on</code> gives me a way of defining functions on multisets. But I am having trouble proving anything at all about such functions. I think I need some sensible eliminators for <code>multiset.strong_induction_on</code>, ideally the one that says that the function defined by <code>multiset.strong_induction_on</code> can be computed on a multiset if I can tell you its values on all proper subsets of the multiset. No doubt this eliminator is "there already" in some form -- but I don't know how to get to it.</p>

#### [ Mario Carneiro (Jul 12 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129522923):
<p>This is a "pecking order" thing. I was remiss in not including a simp lemma <code>(∅ : multiset α) = 0</code> but it would have conveyed this intent well</p>

#### [ Mario Carneiro (Jul 12 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129522982):
<p>Alternatively, in hindsight perhaps it would have been better to make <code>∅</code> the primary one, since multisets have "set" in the name (as opposed to calling them <code>free_abelian_group</code> where <code>0</code> would be more natural)</p>

#### [ Sebastian Ullrich (Jul 12 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523047):
<p>Just idle speculation, I suppose in a future unbundled class hierarchy we would rather have an instance <code>is_zero ∅ (multiset a)</code> instead of <code>has_zero (multiset a)</code>?</p>

#### [ Sebastian Ullrich (Jul 12 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523056):
<p>So that there is no <code>(0  : multiset α)</code></p>

#### [ Mario Carneiro (Jul 12 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523067):
<p>I suppose that depends on whether we want to use <code>0</code> as notation</p>

#### [ Mario Carneiro (Jul 12 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523070):
<p>like I said, it makes sense if you want to use <code>multiset</code> as a free group generator</p>

#### [ Kevin Buzzard (Jul 12 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523118):
<p>A related question is what I should be using for <code>{c}</code> = <code>c :: 0</code> = <code>c :: ∅</code>. Who is top of the tree here?</p>

#### [ Mario Carneiro (Jul 12 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523122):
<p><code>c::0</code> is used exclusively for singleton on <code>multiset</code></p>

#### [ Mario Carneiro (Jul 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523196):
<p>For Q2, you can use this theorem:</p>
<div class="codehilite"><pre><span></span>theorem strong_induction_eq {p : multiset α → Sort*}
  (s : multiset α) (H) : @strong_induction_on _ p s H =
    H s (λ t h, @strong_induction_on _ p t H) :=
by rw [strong_induction_on]
</pre></div>


<p>but the built in equation is also usable, as I did in the proof here</p>

#### [ Kevin Buzzard (Jul 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523214):
<p><code>c :: 0</code> -- Yes, I had spotted this. So I should always use this notation? I noticed in practice that if one sticks to the notation which is top of the tree, then random stuff just "worked better", e.g. I had a <code>split_ifs</code> nightmare scenario when all of a sudden I had four goals; I traced this back to "sometimes using 0 and sometimes emptyset" and when I started being consistent (initially with the wrong choice!) things got better.</p>

#### [ Mario Carneiro (Jul 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523222):
<p>yes, that's the name of the game</p>

#### [ Mario Carneiro (Jul 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523226):
<p>These conventions are debatable, but the most important thing is to be consistent about them</p>

#### [ Kevin Buzzard (Jul 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523266):
<p>As for built in equations for arbitrary definitions, I only noticed that they existed about 20 minutes ago ;-) Thanks <span class="user-mention" data-user-id="110026">@Simon Hudon</span> !</p>

#### [ Mario Carneiro (Jul 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523271):
<p>the built in equations are much more important for wf definitions, since they are often not by <code>rfl</code></p>

#### [ Mario Carneiro (Jul 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523288):
<p>(they are by rfl in theory, but this is where lean breaks from the theory so it proves them automatically instead)</p>

#### [ Kevin Buzzard (Jul 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523333):
<p>Conventions: I guess the second most important thing is to convey the conventions to your users. I am beginning to realise that these subtleties can actually be read off relatively easily by just reading the source. Presumably sometimes there is a genuine CS reason for choosing one over the other and sometimes it's just a fairly arbitrary choice.</p>

#### [ Kevin Buzzard (Jul 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129523337):
<p>I currently spend three days a week surrounded by about 10 students most of whom know no Lean at all, and I am still amazed by how much their completely basic questions can teach me.</p>

#### [ Patrick Massot (Jul 12 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129524684):
<p>Does it give more momentum to your book writing effort?</p>

#### [ Kevin Buzzard (Jul 12 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129524832):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">v_empty</span> <span class="o">:</span> <span class="n">value_aux</span> <span class="mi">0</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">value_aux</span><span class="o">,</span> <span class="c1">-- strong_induction hell</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span> <span class="c1">-- goal now one page long</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span> <span class="c1">-- goal now two pages long</span>
  <span class="n">dsimp</span><span class="o">,</span> <span class="c1">-- goal now one line long and doesn&#39;t mention induction</span>
  <span class="bp">...</span>
</pre></div>

#### [ Kevin Buzzard (Jul 12 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129524833):
<p>:-)</p>

#### [ Kevin Buzzard (Jul 12 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525185):
<p>No -- in fact I spend all my time trying to answer their questions :-) What gives me momentum is that I give one Lean talk per week, and figuring out what to talk about seems to be the same as figuring out what I need to write about next. I am a terrible writer :-/ I am far too verbose. I need a good editor.</p>

#### [ Kevin Buzzard (Jul 12 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525186):
<p>The main function (<code>value_aux</code>) that I'm dealing with here is defined using two applications of <code>multiset.strong_induction_on</code>. The above lemma evaluates it on the empty set. To evaluate it on a singleton my code looks like</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">v_one_chain</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">value_aux</span> <span class="o">(</span><span class="n">c</span> <span class="bp">::</span> <span class="mi">0</span><span class="o">)</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">value_aux</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="c1">-- sanity prevails</span>
</pre></div>


<p>I am just over the moon that I can actually do things now, although I'm not entirely sure I like my <code>simp</code> style and the intermediate goals are huge.</p>

#### [ Patrick Massot (Jul 12 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525210):
<p>Do you know if <code>simp</code> always does the same thing here?</p>

#### [ Sean Leather (Jul 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525257):
<p><code>set_option trace.simplify.rewrite true</code> is your friend.</p>

#### [ Patrick Massot (Jul 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525281):
<p>If it happens to do always the same thing you can either write a new lemma or a specialized tactic</p>

#### [ Kevin Buzzard (Jul 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525381):
<p>I love the way that at 9:02am (UK time) I was <em>completely stuck</em> and now at 10:06am I have made huge progress in both my understanding of Lean and of the dots and boxes API. <span class="user-mention" data-user-id="110045">@Sean Leather</span> and <span class="user-mention" data-user-id="110031">@Patrick Massot</span> I'm sure you're right -- I should figure out exactly what <code>simp</code> is doing. But I am now too busy excitedly proving all the trivial lemmas that Ellen wanted :-)</p>

#### [ Mario Carneiro (Jul 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525383):
<p>You want to write an equation lemma for <code>value_aux</code>, similar to <code>strong_induction_eq</code></p>

#### [ Kevin Buzzard (Jul 12 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525411):
<p>How do I write an equation lemma? Is that just a useful lemma, possibly tagged simp, and called something like <code>value_aux.equation_37</code>?</p>

#### [ Mario Carneiro (Jul 12 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525459):
<p>Nothing special, you don't get to write equation lemmas like lean does</p>

#### [ Mario Carneiro (Jul 12 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525460):
<p>you just give it a regular name and refer to it directly</p>

#### [ Mario Carneiro (Jul 12 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525466):
<p>I would probably call it <code>value_aux_eq</code></p>

#### [ Sean Leather (Jul 12 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525525):
<p>As I understand it, an equation lemma would be what you get (or want) naturally for each constructor of an inductive data type. The equation lemma spells out the equation to reduce/simplify the constructor application. Of course, your type doesn't have to be inductive, nor does it need to have more than one constructor, for you to have an equation lemma. It's really just a name for a particular kind of equality.</p>

#### [ Mario Carneiro (Jul 12 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525911):
<p>Well, more precisely, you get an equation lemma for each branch of a definition. If it's a straight definition X = Y then you get just one equation, but if it is defined by cases or induction on an inductive type then you get an equation for each constructor, as you say</p>

#### [ Sean Leather (Jul 12 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129525924):
<p>Right, forgot about about that.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129566679):
<p>So I had real trouble emulating <code>simp</code> and removing it from the middle of my proofs -- I think it was even rewriting things like <code>lam (h : a \in c :: 0)</code> to <code>lam (h : a = c)</code> and my conv-fu wasn't strong enough. Chris convinced me to try rolling my own inductive definition -- he said it was so that my equation lemmas would be nicer, but I was motivated because I'd never done this sort of thing before. But I'm using induction twice: I am defining a function <code>value : multiset nat -&gt; multiset nat -&gt; nat</code> with the idea being that if I input <code>C</code> and <code>L</code> then I should be able to assume I can evaluate <code>value</code> at <code>C.erase c L</code> and <code>C L.erase l</code> with c in C and l in L. I should say that Chris' docs in the mathlib docs dir were invaluable.</p>
<p>So I got it working, but here's the epilogue: I think the equation compiler might be performing a dangerous simp which I have no way of stopping. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> am I right? (this was the theory Chris and I came up with). Here's something which doesn't work:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="kn">definition</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">N_min</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">value_aux&#39;</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">C</span> <span class="n">L</span> <span class="o">:=</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">N_min</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">pmap</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">C</span><span class="o">),</span>
<span class="c1">--        have multiset.card (C.erase a) &lt; multiset.card C,</span>
<span class="c1">--          from multiset.card_lt_of_lt (multiset.erase_lt.2 h),</span>
        <span class="k">have</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">C</span><span class="bp">.</span><span class="n">erase</span> <span class="n">a</span><span class="o">)</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">L</span> <span class="bp">&lt;</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">C</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">L</span><span class="o">,</span>
          <span class="k">from</span> <span class="n">add_lt_add_right</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">card_lt_of_lt</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">erase_lt</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h</span><span class="o">))</span> <span class="bp">_</span><span class="o">,</span>
        <span class="n">a</span> <span class="bp">-</span> <span class="mi">2</span> <span class="bp">+</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">-</span> <span class="n">value_aux&#39;</span> <span class="o">(</span><span class="n">C</span><span class="bp">.</span><span class="n">erase</span> <span class="n">a</span><span class="o">)</span> <span class="n">L</span><span class="o">))</span>
        <span class="n">C</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">id</span><span class="o">)</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">pmap</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">L</span><span class="o">),</span>
<span class="c1">--        have multiset.card (L.erase a) &lt; multiset.card L,</span>
<span class="c1">--          from multiset.card_lt_of_lt (multiset.erase_lt.2 h),</span>
        <span class="k">have</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">C</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">erase</span> <span class="n">L</span> <span class="n">a</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">C</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">L</span><span class="o">,</span>
          <span class="k">from</span> <span class="n">add_lt_add_left</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">card_lt_of_lt</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">erase_lt</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h</span><span class="o">))</span> <span class="bp">_</span><span class="o">,</span>
        <span class="n">a</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">+</span><span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">-</span> <span class="n">value_aux&#39;</span> <span class="n">C</span> <span class="o">(</span><span class="n">L</span><span class="bp">.</span><span class="n">erase</span> <span class="n">a</span><span class="o">)))</span>
        <span class="n">L</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">id</span><span class="o">))</span>
<span class="n">using_well_founded</span> <span class="o">{</span><span class="n">rel_tac</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">measure_wf</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">CL</span><span class="o">,</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">CL</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">CL</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span><span class="bp">⟩</span><span class="o">]}</span>
</pre></div>


<p>This is mostly noise -- the key thing to see is that I am taking as input two multisets, I am defining <code>value_aux</code> on the pair <code>C L</code> by a function which involves evaluating it on pairs <code>C' L</code> and <code>C L'</code> with <code>C'&lt;C</code> and <code>L'&lt;L</code> resp. The tactic I tell Lean to use to prove well-foundedness is, I think, the function sending <code>C L</code> to <code>card C + card L</code> (there's a <code>psigma</code> type involved, hopefully I got it right). The not-commented-out <code>have</code>s insert precisely what Lean needs to see a proof of, if I've understood things correctly. However the code above does not compile -- the equation compiler complains:</p>
<div class="codehilite"><pre><span></span>The nested exception contains the failure state for the decreasing tactic.
nested exception message:
failed
state:
value_aux&#39; : (Σ&#39; (a : multiset ℕ), multiset ℕ) → ℕ,
C L : multiset ℕ,
a : ℕ,
h : a ∈ C,
this : multiset.card (multiset.erase C a) + multiset.card L &lt; multiset.card C + multiset.card L
⊢ multiset.card (multiset.erase C a) &lt; multiset.card C
</pre></div>


<p>Now that looks strange to me, because if I've understood correctly, <code>this</code> is <em>precisely</em> what the equation compiler wanted to see a proof of. Chris conjectures that <code>simp</code> got applied before <code>assumption</code>.  If I comment out the <code>have/from</code> pairs and replace with the commented-out ones, the code compiles fine (and my equation lemmas don't mention <code>multiset.rec</code> :-) ). Chris points out that if the behaviour of <code>simp</code> changes in the future, then my code breaks in a really obscure way and there's little I can do about it. Have we understood what's going on correctly?</p>

#### [ Chris Hughes (Jul 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129568895):
<p>Here's a method that avoids the simplifier</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">value_aux&#39;</span> <span class="o">(</span><span class="n">N_min</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">multiset</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">C</span> <span class="n">L</span> <span class="o">:=</span> <span class="n">N_min</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">pmap</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">C</span><span class="o">),</span>
<span class="c1">--        have multiset.card (C.erase a) &lt; multiset.card C,</span>
<span class="c1">--          from multiset.card_lt_of_lt (multiset.erase_lt.2 h),</span>
        <span class="k">have</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">C</span><span class="bp">.</span><span class="n">erase</span> <span class="n">a</span><span class="o">)</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">L</span> <span class="bp">&lt;</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">C</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">L</span><span class="o">,</span>
          <span class="k">from</span> <span class="n">add_lt_add_right</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">card_lt_of_lt</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">erase_lt</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h</span><span class="o">))</span> <span class="bp">_</span><span class="o">,</span>
        <span class="n">a</span> <span class="bp">-</span> <span class="mi">2</span> <span class="bp">+</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">-</span> <span class="n">value_aux&#39;</span> <span class="o">(</span><span class="n">C</span><span class="bp">.</span><span class="n">erase</span> <span class="n">a</span><span class="o">)</span> <span class="n">L</span><span class="o">))</span>
        <span class="n">C</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">id</span><span class="o">)</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">pmap</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">L</span><span class="o">),</span>
<span class="c1">--        have multiset.card (L.erase a) &lt; multiset.card L,</span>
<span class="c1">--          from multiset.card_lt_of_lt (multiset.erase_lt.2 h),</span>
        <span class="k">have</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">C</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">erase</span> <span class="n">L</span> <span class="n">a</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">C</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">L</span><span class="o">,</span>
          <span class="k">from</span> <span class="n">add_lt_add_left</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">card_lt_of_lt</span> <span class="o">(</span><span class="n">multiset</span><span class="bp">.</span><span class="n">erase_lt</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h</span><span class="o">))</span> <span class="bp">_</span><span class="o">,</span>
        <span class="n">a</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">+</span><span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">-</span> <span class="n">value_aux&#39;</span> <span class="n">C</span> <span class="o">(</span><span class="n">L</span><span class="bp">.</span><span class="n">erase</span> <span class="n">a</span><span class="o">)))</span>
        <span class="n">L</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span><span class="n">id</span><span class="o">))</span>
<span class="n">using_well_founded</span> <span class="o">{</span><span class="n">dec_tac</span> <span class="o">:=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span><span class="o">,</span> <span class="n">rel_tac</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">measure_wf</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">CL</span><span class="o">,</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">CL</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">+</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">CL</span><span class="bp">.</span><span class="n">snd</span><span class="o">)</span><span class="bp">⟩</span><span class="o">]}</span>
</pre></div>

#### [ Chris Hughes (Jul 13 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129568913):
<p>I changed the <code>dec_tac</code> at the bottom</p>

#### [ Mario Carneiro (Jul 13 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129575356):
<p>Yes, the standard fix when the default dec_tac is being stupid is to replace it with <code>tactic.assumption</code> like chris did</p>

#### [ Mario Carneiro (Jul 13 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129575360):
<p>Actually the default dec_tac doesn't use simp, it is a custom tactic that does a few heuristic rules to do with <a href="http://nat.lt" target="_blank" title="http://nat.lt">nat.lt</a></p>

#### [ Mario Carneiro (Jul 13 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129575413):
<p>it is <code>default_dec_tac</code> in <code>well_founded_tactics.lean</code></p>

#### [ Mario Carneiro (Jul 13 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129575582):
<p>But I'm confused what the issue was that caused you to move away from the original version</p>

#### [ Kevin Buzzard (Jul 13 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129585358):
<p>Short answer: I wanted to get rid of the dangerous simps and this approach ("start again") would have the advantage that it (a) might solve this and (b) would also teach me something (slightly complicated use of equation compiler). </p>
<p>Long technical answer: Your original fix was fine modulo these dangerous simps. I was just talking to Chris about it and he said "why did you even use <code>multiset.strong_induction_on</code> when you could use the equation compiler?" and because I couldn't get rid of my dangerous <code>simp</code> and because I'd never used <code>using_well_founded</code> before I thought I'd give it a go to teach myself something (which turns out to be pretty easy to understand modulo the <code>lam _ _, </code>[exact` bit, which I'm leaving as a black box). Chris pointed out that one only had to use the equation compiler once, whereas I was using strong induction twice, so I felt that rewriting this was somehow going in the right direction.</p>
<p>An example (two examples) of the dangerous simp in my original code looks like this: note that this is with <code>value_aux</code>, the version of my function which uses strong induction twice per application (as opposed to <code>value_aux'</code> above). </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">v_one_chain</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≥</span> <span class="mi">3</span><span class="o">)</span> <span class="o">:</span> <span class="n">value_aux</span> <span class="o">(</span><span class="n">c</span> <span class="bp">::</span> <span class="mi">0</span><span class="o">)</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">value_aux</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="k">show</span> <span class="mi">2</span> <span class="bp">+</span> <span class="o">(</span><span class="n">c</span> <span class="bp">-</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">=</span> <span class="n">c</span><span class="o">,</span> <span class="c1">-- irritating-to-Patrick goal (c is a nat)</span>
  <span class="n">rw</span> <span class="n">add_comm</span><span class="o">,</span><span class="n">refine</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_add_cancel</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">le_trans</span> <span class="o">(</span><span class="k">show</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">)</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>This uses Mario's eliminator for <code>strong_induction_on</code> and compiles fine. The issue of course is with the simps in the middle. Replacing the first <code>simp</code> with <code>dsimp</code> breaks the code. Before the first simp is applied, the goal is <a href="https://gist.github.com/kbuzzard/d9f70ae02b5861bbce0f8d958e16619a" target="_blank" title="https://gist.github.com/kbuzzard/d9f70ae02b5861bbce0f8d958e16619a">https://gist.github.com/kbuzzard/d9f70ae02b5861bbce0f8d958e16619a</a> and after it's applied, the goal becomes (the still quite long) <a href="https://gist.github.com/kbuzzard/07495e93ed94b3d4e5bfd4015a52914f" target="_blank" title="https://gist.github.com/kbuzzard/07495e93ed94b3d4e5bfd4015a52914f">https://gist.github.com/kbuzzard/07495e93ed94b3d4e5bfd4015a52914f</a> . These goals are too big for my liking and the direct approach seemed like it would be likely to make them smaller. There are <code>strong_induction_on</code>s around in these goals but the rewrites won't work without the first <code>simp</code>. Sean suggested <code>set_option trace.simplify.rewrite true</code> and the output of that on the first dangerous <code>simp</code> is <a href="https://gist.github.com/kbuzzard/1a01ad2bc29aad1c257452c4d2d894d5" target="_blank" title="https://gist.github.com/kbuzzard/1a01ad2bc29aad1c257452c4d2d894d5">https://gist.github.com/kbuzzard/1a01ad2bc29aad1c257452c4d2d894d5</a> . I am certainly not a world expert in trace outputs, but I was interpreting the first line <code>0. [simplify.rewrite] [multiset.mem_singleton]: a ∈ c :: 0 ==&gt; a = c</code> of that trace output as meaning "first we replace that <code>mem</code> term with an <code>eq</code> term" but as far as I could see the only occurrences of <code>a ∈ c :: 0</code> were in terms like <code>(λ (a : ℕ) (h : a ∈ c :: 0), ...</code> and I could not do that rewrite with my bare hands (maybe I am just lame at <code>conv</code> but OTOH rewriting the type of a term is probably a dangerous business). In short, I couldn't remove the dangerous simp so I thought I'd try another approach.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129585364):
<blockquote>
<p>Actually the default dec_tac doesn't use simp, it is a custom tactic that does a few heuristic rules to do with <a href="http://nat.lt" target="_blank" title="http://nat.lt">nat.lt</a></p>
</blockquote>
<p>PS that's good to know. Thanks. <span class="user-mention" data-user-id="110044">@Chris Hughes</span> it wasn't using <code>simp</code> after all. PPS I think <a href="https://nat.lt" target="_blank" title="https://nat.lt">https://nat.lt</a> is in Lithuanian.</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129586991):
<p>I think you may not have understood my suggestion to write an equation lemma</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587226):
<p>Here is a version of <code>value_aux'</code> that uses <code>strong_induction_on</code> for its definition (presumably this looks like your original definition, although you didn't show it here):</p>
<div class="codehilite"><pre><span></span>def value_aux (N_min : multiset ℕ → ℕ) (C : multiset ℕ) : multiset ℕ → ℕ :=
multiset.strong_induction_on C $ λ C IH₁ L,
multiset.strong_induction_on L $ λ L IH₂,
N_min (
  multiset.pmap
    (λ a (h : a ∈ C),
      a - 2 + int.nat_abs (2 - IH₁ (C.erase a) (multiset.erase_lt.2 h) L))
    C (λ _, id) +
  multiset.pmap
    (λ a (h : a ∈ L),
      a - 4 + int.nat_abs (4 - IH₂ (L.erase a) (multiset.erase_lt.2 h)))
    L (λ _,id))
</pre></div>

#### [ Kevin Buzzard (Jul 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587227):
<p>[equation lemma] For sure that is true. Probably my question immediately after your comment indicated this. Sometimes I do stuff to learn more</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587233):
<p>Yes, it looks pretty much like that</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587242):
<p>except I used <code>C2</code> instead of <code>C</code> and <code>L2</code> instead of <code>L</code> because I am scared of free and bound variables having the same name</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587260):
<p>This is the equation lemma corresponding to that definition</p>
<div class="codehilite"><pre><span></span>theorem value_aux_eq (N_min : multiset ℕ → ℕ) (C L : multiset ℕ) :
  value_aux N_min C L = N_min (
    multiset.pmap
      (λ a (h : a ∈ C),
        a - 2 + int.nat_abs (2 - value_aux N_min (C.erase a) L))
      C (λ _, id) +
    multiset.pmap
      (λ a (h : a ∈ L),
        a - 4 + int.nat_abs (4 - value_aux N_min C (L.erase a)))
      L (λ _,id)) := sorry
</pre></div>

#### [ Kevin Buzzard (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587306):
<p>I don't understand your application of the "equation lemma" function.</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587310):
<p>(Actually, you can simplify the <code>pmap</code> away the way it's been written here, since <code>h</code> is no longer used)</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587311):
<p>Is there an equation lemma corresponding to every definition?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587317):
<p>What is "the equation lemma corresponding to nat"?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587323):
<p>or "the equation lemma corresponding to quotient.sound" etc etc.</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587327):
<p>Informally, an "equation lemma" says that a definition is what it was defined to be</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587334):
<p><code>nat</code> and <code>quotient.sound</code> don't have equation lemmas because they are constants, not defs</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587341):
<p><code>real</code>?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587346):
<p><code>def f : nat -&gt; nat := lam x, x + 3</code>?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587347):
<p>It has an equation lemma, although you would rarely use it</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587388):
<p>that definitely does</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587394):
<p>it's something like "forall x , f x = x + 3"?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587398):
<p>yes</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587400):
<p>Maybe I don't understand the _point_ then.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587403):
<p>Is it tagged as a simp lemma?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587406):
<p>Who is using these equation lemmas?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587407):
<p>sometimes it's a simp lemma</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587410):
<p>?!</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587415):
<p>Who makes the decision?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587416):
<p>it gets used whenever you "unfold the definition"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587420):
<p>Aah!</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587425):
<p>When I use unfold, sometimes it says that <code>simp</code> failed</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587427):
<p>some definitions are marked <code>@[simp]</code> meaning that their equation lemmas are simp lemmas</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587434):
<p>You can tag a definition with simp? I am not sure I ever internalised that</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587478):
<p>like list.append</p>
<div class="codehilite"><pre><span></span>@[simp] protected def append : list α → list α → list α
| []       l := l
| (h :: s) t := h :: (append s t)
</pre></div>

#### [ Mario Carneiro (Jul 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587481):
<p>This marks this definition's two (!) equation lemmas as simp lemmas</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587493):
<p>I can see all the equation lemmas with <code>#print prefix list.append</code> perhaps</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587498):
<p>yes</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587503):
<p>So I must confess that I've never really understood the output of that sort of command.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587504):
<p>We have <code>_main</code>, <code>_main._meta_aux</code> etc</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587506):
<p>it's quite intimidating</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587508):
<p>But sometimes lean doesn't generate equation lemmas the way you would like them, so you have to write your own, and that's my point</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587596):
<p>I am still missing a big issue</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587600):
<p>OK so I wrote my function</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587603):
<p>and the equation lemmas are all wrong</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587606):
<p>so I need to write another one.</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587613):
<p>For example, here's another way to write list.append</p>
<div class="codehilite"><pre><span></span>def list.append&#39; {α} (l₁ l₂ : list α) : list α :=
list.rec_on l₁ l₂ (λ a l₁ IH, a :: IH)
</pre></div>

#### [ Kevin Buzzard (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587614):
<p>OK so I wrote one: "<code>theorem X : f x = g x -- this is the equation lemma I want</code>"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587617):
<p>that's a lemma</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587618):
<p>Is it an equation lemma?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587620):
<p>the equation lemmas are not what we would like</p>
<div class="codehilite"><pre><span></span>#print prefix list.append&#39;
-- list.append&#39; : Π {α : Type u_1}, list α → list α → list α
-- list.append&#39;.equations._eqn_1 : ∀ {α : Type u_1} (l₁ l₂ : list α),
--   list.append&#39; l₁ l₂ = list.rec_on l₁ l₂ (λ (a : α) (l₁ IH : list α), a :: IH)
</pre></div>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587662):
<p>why not?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587669):
<p>What's wrong with them?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587672):
<p>I don't understand several things</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587680):
<p>"equation lemmas are used in unfold"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587681):
<p>"sometimes they're simp lemmas"</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587684):
<p>While it is true that append is equal to that rec_on mess, that's not what I want to see</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587687):
<p>"they're generated automatically"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587692):
<p>that's about all I know</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587693):
<p>about equation lemmas</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587694):
<p>I am missing some fundamental point about why they exist and why they're important</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587705):
<p>"if you write a definition, Lean generates a bunch of lemmas with obscure names"</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587706):
<p>what I want to see are the things that the definition is trying to say, namely <code>list.append [] l = l</code> and <code>list.append (a::l) l' = a :: list.append l l'</code></p>

#### [ Mario Carneiro (Jul 13 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587710):
<p>This is really important for controlling the complexity of statements</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587714):
<p>"if you write the definition differently, you might get different lemmas, and Mario can see that this might cause problems but Kevin still has no understanding of when equation lemmas are used so doesn't care what these auto-generated lemmas are"</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587753):
<p>if every time you used <code>nat.add</code> it unfolded to its definition it would be utterly unreadable</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587756):
<p>it can't unfold</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587760):
<p>oh wit</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587761):
<p>oh wait</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587766):
<p>is <code>nat.add</code> one of these things whose definition is not what I think it is?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587771):
<p>Is it not 0 -&gt; x, succ y -&gt; succ (x+y)?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587783):
<p>really making progress in this proof:</p>
<div class="codehilite"><pre><span></span>example (x : ℕ) : 0 + x = 0 :=
begin
  dsimp only [(+)], delta nat.add,
-- ⊢ nat.brec_on x
--       (λ (a : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a) (a_1 : ℕ),
--          (λ (a a_1 : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) a_1),
--             nat.cases_on a_1 (λ (_F : nat.below (λ (a : ℕ), ℕ → ℕ) 0), id_rhs ℕ a)
--               (λ (a_1 : ℕ) (_F : nat.below (λ (a : ℕ), ℕ → ℕ) (nat.succ a_1)),
--                  id_rhs ℕ (nat.succ ((_F.fst).fst a)))
--               _F)
--            a_1
--            a
--            _F)
--       0 =
--     0
end
</pre></div>

#### [ Kevin Buzzard (Jul 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587788):
<p>I'm already lost, apparently it's <code>nat.add._main</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587790):
<p>that does not look good</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587794):
<p>If <code>simp</code> did this Leo would be fired by now</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587847):
<p>The problem has occurred because <code>nat.add</code> is for some reason defined in a stupid way</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587858):
<p>I fixed this up in my blog IIRC</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587861):
<p>no, the problem has occurred because I unfolded the definition without folding it back up again</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587877):
<p>Does the equation compiler create that monstrosity?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587879):
<p>Even if I defined <code>nat.add</code> the simple way, it would still not be pretty to look at</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587885):
<p>oh holy moley</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587887):
<p>I want to see <code>0 + x</code> not <code>nat.rec bla bla</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587893):
<p><code>nat.add</code> is defined sensibly in <code>core.lean</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587913):
<p>what has the equation compiler done??</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587936):
<p>The equation lemmas say things like <code>x + succ y = succ (x + y)</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587941):
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">nat</span>
  <span class="kn">protected</span> <span class="n">def</span> <span class="n">add</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span>
  <span class="bp">|</span> <span class="n">a</span>  <span class="n">zero</span>     <span class="o">:=</span> <span class="n">a</span>
  <span class="bp">|</span> <span class="n">a</span>  <span class="o">(</span><span class="n">succ</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">succ</span> <span class="o">(</span><span class="n">add</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587945):
<p>That got turned into the monstrosity</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587949):
<p>this is true by rfl, but the really important thing is that the RHS does not have <code>nat.rec</code> in it</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587960):
<p>or <code>nat.brec_on</code> or its cousins</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587973):
<p>Right -- Chris was stressing the importance of getting away from <code>multiset.rec</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587994):
<p>which I had in my initial equation lemmas for the value function</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129587998):
<p>In fact, you could say that's the main purpose of equation lemmas, to hide recursors</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588018):
<p>actually it's even worse, my equation lemmas for value have strong induction in</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588062):
<div class="codehilite"><pre><span></span>value_aux.equations._eqn_1 : ∀ (C : multiset ℕ),
  value_aux C =
    multiset.strong_induction_on C
      (λ (C2 : multiset ℕ) (HC : Π (t : multiset ℕ), t &lt; C2 → multiset ℕ → ℕ) (L : multiset ℕ),
         multiset.strong_induction_on L
           (λ (L2 : multiset ℕ) (HL : Π (t : multiset ℕ), t &lt; L2 → ℕ),
              multiset.N_min
                (multiset.pmap
                     (λ (a : ℕ) (h : a ∈ C2), a - 2 + int.nat_abs (2 - ↑(HC (multiset.erase C2 a) _ L2)))
                     C2
                     _ +
                   multiset.pmap
                     (λ (a : ℕ) (h : a ∈ L2), a - 4 + int.nat_abs (4 - ↑(HL (multiset.erase L2 a) _)))
                     L2
                     _)))
</pre></div>

#### [ Kevin Buzzard (Jul 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588080):
<p>Can you tell me a formal definition of which parts of the output of <code>#print prefix value_aux</code> are the equation lemmas?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588084):
<p>Is it precisely those which start <code>value_aux.equation...</code>?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588095):
<p>yes, those are the automatically generated equation lemmas</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588097):
<p>because I have other things like the stunning observation <code>value_aux._proof_4 : ∀ (L2 : multiset ℕ) (_x : ℕ), _x ∈ L2 → _x ∈ L2</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588103):
<p>Is that an equation lemma?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588109):
<p>I don't know what I'd do without that lemma</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588114):
<p>those are extracting proof terms inside non-proof terms for performance</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588166):
<p>but not equation lemmas.</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588167):
<p>the extraction code isn't so bright</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588176):
<p>equation lemmas are equations</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588181):
<p>OK so when I make a new definition, Lean makes some equation lemmas, and we've seen examples where these lemmas are in some sense unusable</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588183):
<p>right</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588189):
<p>so now all I need to know is</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588193):
<p>(1) what is actually using them and (2) how to write better ones</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588196):
<p>When you write a definition you should already have in mind what its equation lemmas are</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588202):
<p>In this case, you knew you wanted <code>value_aux</code> to depend on itself at other values</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588203):
<p>If we go back to <code>nat.add</code> I can see <code>x + succ y = succ (x + y)</code> would be the sort of thing that as an end user I would simply _assume_ was true by <code>rfl</code>, given the definition</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588249):
<p>which is where something like this comes from</p>
<div class="codehilite"><pre><span></span>theorem value_aux_eq (N_min : multiset ℕ → ℕ) (C L : multiset ℕ) :
  value_aux N_min C L = N_min (
    C.map (λ a, a - 2 + int.nat_abs (2 - value_aux N_min (C.erase a) L)) +
    C.map (λ a, a - 4 + int.nat_abs (4 - value_aux N_min C (L.erase a)))) := sorry
</pre></div>

#### [ Kevin Buzzard (Jul 13 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588256):
<p>Right -- I feel like I want that theorem to be true by <code>rfl</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588258):
<p>because in my non-CS mathematical mind that is "exactly how I defined the function"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588265):
<p>that theorem is "true by definition"</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588266):
<p>exactly</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588272):
<p>but funnily enough I don't see it in my list of equation lemmas</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588277):
<p>Half of the work is taking your "definition" and turning it into something lean will accept, and the other half is getting back to the original thing you wanted to call the definition</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588318):
<p>that latter step is the equation lemma</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588327):
<p>I had never remotely comprehended this.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588329):
<p>I thought that "Lean did the second part automatically"</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588331):
<p>it does, for the most part</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588351):
<p>but it's not perfect, it doesn't accept every definitionesque thing mathematicians dream up</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588352):
<p>OK so let's say I can prove the lemma which I thought should be <code>rfl</code> but which wasn't.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588361):
<p>Is it just a case of making sure that lemma is called <code>value_aux.equations._eqn_2</code>?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588373):
<p>Unfortunately, lean doesn't let you install your own equation lemmas like that</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588414):
<p>OK so we're back to (1) I don't know how to make a lemma into an equation lemma and (2) I don't know exactly what is using the equation lemmas and when</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588416):
<p>when you right your own equation lemma, it's just a theorem, an equality you can use in rewrite and simp</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588417):
<p>and rfl</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588420):
<p>because equation lemmas are true by definition, right? :-)</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588421):
<p>If you prove it by <code>rfl</code> you can also use it in <code>dsimp</code></p>

#### [ Mario Carneiro (Jul 13 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588424):
<p>Sometimes it's <code>rfl</code> sometimes not</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588425):
<p>If it's not <code>rfl</code> then Lean made a mistake</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588430):
<p>because the equation lemmas are the things which are true by definition</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588433):
<p>for more elaborate definitional mechanisms, DTT doesn't recognize it as definitional but you can still prove it with some work</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588436):
<p>OK</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588478):
<p>so now I proved a lemma, the proof unfortunately wasn't <code>rfl</code>, I want to use it everywhere because in my brain the lemma is "true by definition of the object".</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588480):
<p>Now what?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588483):
<p>In particular, I doubt <code>value_aux_eq</code> is true by <code>rfl</code>, particularly when I changed the <code>pmap</code> to <code>map</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588488):
<p>Yes i can quite believe it's not</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588493):
<p>not least because <code>value_aux</code> uses <code>multiset.strong_induction_on</code> <em>twice</em></p>

#### [ Mario Carneiro (Jul 13 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588497):
<p>but it is nevertheless "the way we want it to unfold" so we treat it as the equation lemma</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588499):
<p>"so we treat it as the equation lemma" is the bit I don't get</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588508):
<p>Are you just saying "prove a lemma and then occasionally <code>rw</code> with it"?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588512):
<p>It just means we use that theorem when we would otherwise "unfold <code>value_aux</code>"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588521):
<p>So </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">v_one_chain</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≥</span> <span class="mi">3</span><span class="o">)</span> <span class="o">:</span> <span class="n">value_aux</span> <span class="o">(</span><span class="n">c</span> <span class="bp">::</span> <span class="mi">0</span><span class="o">)</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">value_aux</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">strong_induction_eq</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
<span class="bp">...</span>
</pre></div>


<p>is not the right approach?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588566):
<p>no</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588568):
<p>even though I have the right equation lemma?</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588570):
<p>(I assume I do, I think you wrote it)</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588588):
<p>you want to use the equation lemma for <code>value_aux</code>, not the equation lemma for <code>strong_induction_on</code></p>

#### [ Mario Carneiro (Jul 13 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588593):
<p>you will use the latter to prove the former</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588597):
<p>aah</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588613):
<p>aah I was thinking "Mario said to use an equation lemma, I don't know what that is, I think Mario wrote it for me, I'll just use that"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588682):
<p>So an equation lemma is just a lemma, with no magic properties, it doesn't have to have a weird name like <code>foo._equation_7_main_sunfold</code></p>

#### [ Mario Carneiro (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588688):
<p>no, that's just the usual name for lean's autogenerated equation lemmas</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588691):
<p>what makes it an equation lemma is that it represents a fact which the end user would like to think was "true by definition"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588696):
<p>if they were a wooly thinker, like e.g. a pure mathematician</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588701):
<p>those get some special magic, like being able to write <code>simp [f]</code> instead of <code>simp [f.equations_1]</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588706):
<p>Yes, I learnt that yesterday</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588752):
<p>OK so let me step back and try to wrap up</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588761):
<p>When I write a definition, I might want to consider what the fundamental properties of that definition are -- the things which <em>should</em> be "true by definition"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588768):
<p>or "true because it's completely obvious"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588781):
<p>and then I might want to look at the subset of the output of <code>#print prefix foo</code> consisting only of things which have the string "equation" in them</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588789):
<p>and I might want to just check that everything I want to be "true by definition" is there</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588797):
<p>The autogenerated equation lemmas are easy to predict without looking at them like that</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588801):
<p>and if it's not then I might want to make a note of this, prove the remaining facts, and then spend the rest of my life rewriting with them</p>

#### [ Sean Leather (Jul 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588845):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Perhaps “true by the definition you wished it had”? “True because it's obvious” is maybe too generous in what it allows.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588846):
<blockquote>
<p>The autogenerated equation lemmas are easy to predict without looking at them like that</p>
</blockquote>
<p>says someone who has probably looked at the code which generates them</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588847):
<p>for each branch of the definition, each <code>:=</code>, you get a lemma saying your definition applied to those arguments gives the RHS</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588859):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> that's a better way of phrasing it. My definition of value by "induction on (induction on ...)" was never going to create the lemma I wanted</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588880):
<p>but on the other hand there was clearly a definition which in some sense I "wished I had written"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588887):
<p>and that was precisely the definition I _did_ write yesterday, using the equation compiler</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588931):
<p>So all this stinks. There are things which should be true by <code>rfl</code> but which I can't prove with <code>rfl</code></p>

#### [ Mario Carneiro (Jul 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588932):
<p>One place where you might be surprised is in definitions with wildcards</p>
<div class="codehilite"><pre><span></span>def X {α} : list α → list α → list α
| [] _ := []
| _ [] := []
| x y := x
#print prefix X
-- X.equations._eqn_1 : ∀ {α : Type u_1}, X list.nil list.nil = list.nil
-- X.equations._eqn_2 : ∀ {α : Type u_1} (hd : α) (tl : list α), X list.nil (hd :: tl) = list.nil
-- X.equations._eqn_3 : ∀ {α : Type u_1} (hd : α) (tl : list α), X (hd :: tl) list.nil = list.nil
-- X.equations._eqn_4 : ∀ {α : Type u_1} (hd : α) (tl : list α) (hd_1 : α) (tl_1 : list α), X (hd :: tl) (hd_1 :: tl_1) = hd :: tl
</pre></div>

#### [ Mario Carneiro (Jul 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588944):
<p>notice that <code>X x y = x</code> is not an equation lemma since it has to do some case splits first</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588952):
<p>right</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588953):
<p>that all makes sense to me</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588957):
<p>that's a lemma, that X x y = x</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129588976):
<p>actually it's perhaps not even true but I see your point whether or not this example is exactly right</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589020):
<p>So I prove this lemma by cases on x</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589033):
<p>and then I decree in my head that this is an equation lemma</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589045):
<p>Maybe a better example of an equation lemma for this one is <code>X [] y = []</code> and <code>X x [] = []</code></p>

#### [ Mario Carneiro (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589054):
<p>Neither of these is true by rfl</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589055):
<p>yes</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589063):
<p>both proof by cases</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589069):
<p>These look like simp lemmas to me</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589076):
<p>They are that too</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589080):
<p>So an equation lemma seems to me to have no formal definition</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589082):
<p>equation lemmas are often good simp lemmas</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589123):
<p>it's "something which the user is clearly going to need again and again"</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589129):
<p>so should probably be proved immediately after the definition</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589134):
<p>but sometimes they would lead to infinite unfolding, like the equation lemma for <code>value_aux</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589143):
<p>I think nat is well-founded</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589148):
<p>equation lemmas for wf definitions often have that problem</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589161):
<p><code>gcd x y</code> unfolds forever when given <em>variable</em> <code>x</code> and <code>y</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589173):
<p>Oh!</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589177):
<p>it doesn't matter that nat is well founded</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589180):
<p>Oh you're absolutely right!</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589195):
<p>because these are open terms</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589197):
<p>We're not doing case splits on constructors for multiset or whatever</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589205):
<p>oh so that lemma is actually quite dangerous!</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589246):
<p>Shall I make it a simp lemma?</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589257):
<p>yes, you only want to use it with <code>rw</code> or <code>simp {single_pass := tt}</code></p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589266):
<p>right</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589273):
<p>it should definitely not be a simp lemma</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589278):
<p>right!</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589302):
<p>I gave an entire lecture on functions last Monday</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589305):
<p>I feel like I could give another one now</p>

#### [ Mario Carneiro (Jul 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589309):
<p>:)</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589315):
<p>Many thanks as ever Mario.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129589518):
<p>What's nice about zulip rather than IRL meetings is that now I understand much better I can just read through the thread again with the benefit of hindsight and try to catch extra subtleties.</p>

#### [ Kevin Buzzard (Jul 13 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset/near/129590094):
<blockquote>
<p>Half of the work is taking your "definition" and turning it into something lean will accept, and the other half is getting back to the original thing you wanted to call the definition</p>
</blockquote>
<p>This is somehow the key point. I have quite a flexible way of thinking about definitions and their basic properties, I guess because mathematicians are trained like that. Some properties of a definition are so completely basic that I think I've got into the habit of simply <em>assuming</em> that they will be (a) true and (b) <code>rfl</code>. For simple functions this might well be the case. For more complex definitions which need some bending to shove into Lean, life might not be so easy. I have a definition by induction on two variables, and Mario's equation lemma is exactly how I am thinking the definition "works". I shove the definition into Lean in perhaps an inelegant way ("Mario wrote <code>multiset.strong_induction_on</code> and I can apply it twice, that'll do") and now I need to be aware of the fact that Lean's understanding of the function is now quite far from my intuitive idea of how it works, and it should now be a top priority to sort this situation out by proving the lemmas which say that the definition behaves the way I expect it to. If I'm writing some API then I might want to consider proving these so-called "equation lemmas" -- this is an informal definition and it seems to mean "the lemmas which an end user might expect to be true by definition, whether or not they are true by <code>rfl</code>" -- immediately after the definition of the function. Some might already be there with exotic names with <code>_</code>s in, and the ones that are not should be written as a matter of priority or other mathematicians will not be able to use the function in the intuitive way which they would like to.</p>


{% endraw %}
