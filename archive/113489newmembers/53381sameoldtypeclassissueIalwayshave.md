---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/53381sameoldtypeclassissueIalwayshave.html
---

## Stream: [new members](index.html)
### Topic: [same old typeclass issue I always have](53381sameoldtypeclassissueIalwayshave.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 08 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401453):
<p>I really should write these down at some point; I'm always having to ask. I still can't quite control <code>haveI</code> <code>exactI</code> etc.</p>
<p>I saw in the code of one of my first year students the comment <code>what's with rw mul_self_iff_eq_one? can't it be used to prove 0 = 1?</code>. I thought this was a great comment. I encouraged the student to formalise their question in Lean. And then I tried to knock this off myself.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">mul_self_iff_eq_one</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">mul_self_iff_eq_one : ∀ {α : Type u_1} [_inst_1 : group α] {a : α}, a * a = a ↔ a = 1</span>
<span class="cm">-/</span>
<span class="kn">lemma</span> <span class="n">lean_is_broken</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span>
                          <span class="bp">→</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- fails to synthesize has_mul and has_one</span>
</pre></div>


<p>damnit is there a trick to get past type class inference issues? It would be nice if students could be taught to answer their own questions like this.</p>

#### [ Mario Carneiro (Oct 08 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401601):
<p>put <code>by exactI</code> between the group instance and the point of use</p>

#### [ Gabriel Ebner (Oct 08 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401606):
<p>The only typeclass instances that are used by the elaborator are the ones before the colon:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">l_i_b</span> <span class="o">[</span><span class="n">this_gets_used</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">[</span><span class="n">this_not</span><span class="o">],</span> <span class="n">foo</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Oct 08 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401729):
<blockquote>
<p>put <code>by exactI</code> between the group instance and the point of use</p>
</blockquote>
<p>I tried that and I got a second error :-/</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">group</span> <span class="n">α</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="n">has_one</span> <span class="n">α</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">group</span> <span class="n">α</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="n">Sort</span> <span class="err">?</span>
</pre></div>

#### [ Kevin Buzzard (Oct 08 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401774):
<p>I know they can just create the term with <code>let X := mul_self_iff_eq_one</code> in a tactic mode proof -- I was just trying to explictly put it into the question.</p>

#### [ Mario Carneiro (Oct 08 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401896):
<p>this works fine for me:</p>
<div class="codehilite"><pre><span></span>lemma lean_is_broken : (∀ {α : Type*} [_inst_1 : group α] {a : α}, by exactI a * a = a ↔ a = 1)
                          → (0 : ℕ) = 1 := sorry
</pre></div>

#### [ Kevin Buzzard (Oct 08 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401899):
<p>Maybe that's actually a better answer because then they can see the term and not the type.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135401903):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">lean_is_broken</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">X</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">mul_self_iff_eq_one</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Oct 08 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135402028):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">lean_is_broken&#39;</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="k">by</span> <span class="n">exactI</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span>
                          <span class="bp">→</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Yup you're right, I don't know what I did :-/</p>

#### [ Kevin Buzzard (Oct 08 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135402105):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> There are some ideas about how to formalise your question.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135402292):
<p>The best questions on this forum are ones where people actually post MWEs -- completely working Lean code which people can just cut and paste -- and then ask a question about it. But when I began to learn to formulate my basic questions in this way, I realised that I was starting to be able to answer them myself without having to ask at all.</p>

#### [ Kevin Buzzard (Oct 08 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/same%20old%20typeclass%20issue%20I%20always%20have/near/135402362):
<p>The biggest wins are when, in the process of formalising it, you remember that what you're stuck on is actually something you already asked about earlier :-) Then you go and search the forums and read what was said at the time.</p>


{% endraw %}
