---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16371modifiedinductiononnat.html
---

## Stream: [general](index.html)
### Topic: ["modified" induction on nat](16371modifiedinductiononnat.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 18 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147917777):
<p>I am doing the homework I set my students. I seem to often want "induction on n &gt;= 1" and in this question I even want "induction starting at n = 2". I have a family of propositions <code>P n</code> for <code>n : nat</code>, which are true for n &gt;= 2 (and this can be proved by induction on n&gt;=2), and I also have the hypothesis <code>Hn2 : n &gt;= 2</code>. Currently (in tactic mode) I write</p>
<div class="codehilite"><pre><span></span>  <span class="c1">-- hypotheses    n : ℕ</span>
  <span class="c1">--             Hn2 : n ≥ 2</span>
  <span class="c1">-- now replace n with m + 2 and then do induction on m &gt;= 0</span>
  <span class="n">cases</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span><span class="o">,</span> <span class="n">cases</span> <span class="n">Hn2</span><span class="o">,</span> <span class="c1">-- Hn2 : 0 ≥ 2 and cases kills it.</span>
  <span class="n">cases</span> <span class="n">n</span> <span class="k">with</span> <span class="n">m</span><span class="o">,</span> <span class="n">revert</span> <span class="n">Hn2</span><span class="o">,</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span> <span class="c1">-- here Hn2 : 1 ≥ 2 and cases doesn&#39;t kill it</span>
  <span class="n">clear</span> <span class="n">Hn2</span><span class="o">,</span> <span class="c1">-- and we&#39;re finally ready to go</span>
  <span class="c1">-- it would be nice to have</span>
  <span class="n">induction</span> <span class="n">m</span> <span class="k">with</span> <span class="n">d</span> <span class="n">Hd</span><span class="o">,</span>
</pre></div>


<p>and off I go. But even then it's pretty meh because n is replaced by <code>nat.succ (nat.succ m)</code>. </p>
<p>I don't think it would be too hard to knock up some kind of "modified principle of induction" which takes as input a hypothesis n&gt;=2 and spits out two goals, one the case n = 2 and the other the goal <code>P (n + 1)</code> assuming both <code>P n</code> and <code>n &gt;= 2</code> still. </p>
<p>I might try to get a minion to do this. How would this work exactly?  I've just looked at the source code for meta induction and it looks intimidating, but I guess that's because it works on a general inductive type. Is this a feasible project for a student? What should it be called? What should the syntax be? <code>modified_induction n Hn2 with d Hd</code>?  It's just something that seems to come up a lot in my class, that's why I'm interested.</p>

#### [ Reid Barton (Nov 18 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918117):
<p>No need for a custom tactic, you can define that as a lemma, and maybe invoke it with <code>inducting ... using</code>.</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918290):
<p>Hmm. What is this <code>using</code> of which you speak? Is that some keyword I don't know?</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918299):
<p>it comes out blue in VS code so I guess it means something...</p>

#### [ Reid Barton (Nov 18 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918336):
<p>It's one of the keywords that can be used by interactive tactics I guess</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918435):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">Q0502&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≥</span> <span class="mi">2</span> <span class="bp">→</span> <span class="mi">4</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">3</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">d</span> <span class="n">Hd</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="c1">-- now pick up the pieces for modified induction</span>
  <span class="n">intro</span> <span class="n">Hs</span><span class="o">,</span> <span class="n">cases</span> <span class="n">Hs</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span> <span class="c1">-- base case n = 2,</span>
  <span class="n">replace</span> <span class="n">Hd</span> <span class="o">:=</span> <span class="n">Hd</span> <span class="n">Hs_a</span><span class="o">,</span> <span class="n">clear</span> <span class="n">Hs_a</span><span class="o">,</span>
  <span class="c">/-</span><span class="cm"></span>
<span class="cm">  d : ℕ,</span>
<span class="cm">  Hd : 4 ^ d &gt; 3 ^ d + 2 ^ d</span>
<span class="cm">  ⊢ 4 ^ nat.succ d &gt; 3 ^ nat.succ d + 2 ^ nat.succ d</span>
<span class="cm">  -/</span>
  <span class="c1">-- exact calc blah</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>This isn't so bad, although using induction twice does look weird. I think I still want it to be better though. I need to learn about <code>using</code> apparently...</p>

#### [ Reid Barton (Nov 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918438):
<p>Check out the docstring for <code>induction</code> (it's quite long)</p>

#### [ Mario Carneiro (Nov 18 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918796):
<p>this is not the easiest way to prove it</p>

#### [ Mario Carneiro (Nov 18 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918968):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">h0</span> <span class="o">:</span> <span class="n">P</span> <span class="mi">37</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="mi">37</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="mi">37</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">introv</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">IH</span><span class="o">,</span> <span class="o">{</span><span class="n">cases</span> <span class="n">h</span><span class="o">},</span>
  <span class="n">cases</span> <span class="n">lt_or_eq_of_le</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_of_succ_le_succ</span> <span class="n">h</span><span class="o">)</span> <span class="k">with</span> <span class="n">lt</span> <span class="n">eq</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">h1</span> <span class="bp">_</span> <span class="n">lt</span> <span class="o">(</span><span class="n">IH</span> <span class="n">lt</span><span class="o">)</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">eq</span><span class="o">,</span> <span class="n">exact</span> <span class="n">h0</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Nov 18 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147918969):
<p>this is what I usually do when I have an induction with a weird base case</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919062):
<p>But it makes it harder to see what's going on</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919065):
<p>It's still better than both my ways though :-)</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919070):
<p>but that doesn't mean that I'm happy with it.</p>

#### [ Mario Carneiro (Nov 18 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919113):
<p>this is a bit more flexible with weird induction steps:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">{</span><span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="n">h0</span> <span class="o">:</span> <span class="n">P</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_induction_on</span> <span class="n">n</span><span class="o">,</span> <span class="n">intros</span> <span class="n">n</span> <span class="n">IH</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">lt_or_eq_of_le</span> <span class="n">h</span> <span class="k">with</span> <span class="n">lt</span> <span class="n">eq</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span><span class="o">,</span> <span class="o">{</span><span class="n">cases</span> <span class="n">lt</span><span class="o">},</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_of_lt_succ</span> <span class="n">lt</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">h1</span> <span class="bp">_</span> <span class="n">this</span> <span class="o">(</span><span class="n">IH</span> <span class="bp">_</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="bp">_</span><span class="o">)</span> <span class="n">this</span><span class="o">)</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">n</span><span class="o">,</span> <span class="n">exact</span> <span class="n">h0</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 18 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919124):
<p>That's the optimal set-up I guess. So now I can do "induction n using ^^^" somehow?</p>

#### [ Mario Carneiro (Nov 18 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919125):
<p>eh, it's not that great</p>

#### [ Mario Carneiro (Nov 18 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919164):
<p><code>induction using</code> has little to offer over <code>refine</code> and it is much pickier</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919174):
<p>I just want to make it a one-liner for my students to go from goal <code>P n</code> and hypothesis <code>Hn : n &gt;= 2</code> to goals <code>P 2</code> and <code>P (d + 1)</code>, the latter with hypotheses <code>P d</code> and <code>d &gt;= 2</code></p>

#### [ Mario Carneiro (Nov 18 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919216):
<p>sure, just use this lemma</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919218):
<p>indeed!</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919454):
<p>Yes, this is better than anything I had. I've added modified induction to <code>xenalib</code> :-)</p>

#### [ Kevin Buzzard (Nov 18 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147919455):
<p>Thanks!</p>

#### [ Patrick Massot (Nov 18 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/147925201):
<blockquote>
<p><code>induction using</code> has little to offer over <code>refine</code> and it is much pickier</p>
</blockquote>
<p>It may require Lean 4 but I hope we'll have something as powerfull as SSReflect <code>elim</code> instead</p>

#### [ Sebastien Gouezel (Dec 01 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/150688665):
<blockquote>
<p>this is a bit more flexible with weird induction steps:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">{</span><span class="n">m</span><span class="o">}</span> <span class="o">(</span><span class="n">h0</span> <span class="o">:</span> <span class="n">P</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_induction_on</span> <span class="n">n</span><span class="o">,</span> <span class="n">intros</span> <span class="n">n</span> <span class="n">IH</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">lt_or_eq_of_le</span> <span class="n">h</span> <span class="k">with</span> <span class="n">lt</span> <span class="n">eq</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span><span class="o">,</span> <span class="o">{</span><span class="n">cases</span> <span class="n">lt</span><span class="o">},</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_of_lt_succ</span> <span class="n">lt</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">h1</span> <span class="bp">_</span> <span class="n">this</span> <span class="o">(</span><span class="n">IH</span> <span class="bp">_</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="bp">_</span><span class="o">)</span> <span class="n">this</span><span class="o">)</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">n</span><span class="o">,</span> <span class="n">exact</span> <span class="n">h0</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


</blockquote>
<p>Has this been incorporated in mathlib? It turns out that I just need this lemma right now :)</p>

#### [ Sebastien Gouezel (Dec 01 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/150689029):
<p>In the middle of a proof, I need to define by induction a function from ℕ to some type α. I know how to do this with a top-level definition, but I could not figure out the syntax inside a proof. Is this possible?</p>

#### [ Reid Barton (Dec 01 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/150689418):
<p>I don't think you can do it using the equation compiler</p>

#### [ Sebastien Gouezel (Dec 01 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22modified%22%20induction%20on%20nat/near/150689522):
<p>Yes, I have probably to use <code>nat.rec_on</code>, but this looks really arcane.</p>


{% endraw %}
