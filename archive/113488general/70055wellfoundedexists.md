---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70055wellfoundedexists.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [well-founded exists](https://leanprover-community.github.io/archive/113488general/70055wellfoundedexists.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Sep 12 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793419):
<p>Can I prove that a recursive definition <code>T → Prop</code> is well-founded if a clause wraps the recursive call with an exists (i.e. <code>f &lt;pattern&gt; := ∃ .., f &lt;subpattern&gt;</code>)? If so, how would I begin to do this?</p>

#### [ Sean Leather (Sep 12 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793458):
<p>Oh, actually, it's not a strict subpattern, it's a function that uses a subpattern. Maybe that's my issue, not the exists.</p>

#### [ Sean Leather (Sep 12 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793554):
<p>So, should I have something like <code>have sizeof (function-calling-subpattern) &lt; sizeof pattern</code> here?</p>

#### [ Sean Leather (Sep 12 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793805):
<p>Okay, never mind, I think I figured out what I need to solve.</p>

#### [ Sean Leather (Sep 12 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133793811):
<p>I always get confused with these well-founded proofs.</p>

#### [ Sean Leather (Sep 12 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133803135):
<p>So I finally figured out how to prove that my recursion is well-founded. But I think it could be better.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lc&#39;</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span> <span class="bp">→</span> <span class="kt">Prop</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">var</span> <span class="n">fb</span> <span class="bp">_</span><span class="o">)</span>     <span class="o">:=</span> <span class="n">fb</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span>    <span class="o">:=</span>
    <span class="k">have</span> <span class="n">depth</span> <span class="n">ef</span> <span class="bp">&lt;</span> <span class="n">depth</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">depth</span> <span class="n">ea</span> <span class="bp">&lt;</span> <span class="n">depth</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
    <span class="n">lc&#39;</span> <span class="n">ef</span> <span class="bp">∧</span> <span class="n">lc&#39;</span> <span class="n">ea</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">lam</span> <span class="n">v</span> <span class="n">eb</span><span class="o">)</span>     <span class="o">:=</span>
    <span class="bp">∃</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">tagged</span> <span class="n">V</span><span class="o">)),</span>
    <span class="k">have</span> <span class="n">depth</span> <span class="o">(</span><span class="n">open_fresh</span> <span class="n">v</span> <span class="n">L</span> <span class="n">eb</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">depth</span> <span class="o">(</span><span class="n">lam</span> <span class="n">v</span> <span class="n">eb</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">pos_iff_ne_zero&#39;</span><span class="o">],</span>
    <span class="n">lc&#39;</span> <span class="o">(</span><span class="n">open_fresh</span> <span class="n">v</span> <span class="n">L</span> <span class="n">eb</span><span class="o">)</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">let_</span> <span class="n">v</span> <span class="n">ed</span> <span class="n">eb</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">have</span> <span class="n">depth</span> <span class="n">ed</span> <span class="bp">&lt;</span> <span class="n">depth</span> <span class="o">(</span><span class="n">let_</span> <span class="n">v</span> <span class="n">ed</span> <span class="n">eb</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
    <span class="n">lc&#39;</span> <span class="n">ed</span> <span class="bp">∧</span>
    <span class="bp">∃</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">tagged</span> <span class="n">V</span><span class="o">)),</span>
    <span class="k">have</span> <span class="n">depth</span> <span class="o">(</span><span class="n">open_fresh</span> <span class="n">v</span> <span class="n">L</span> <span class="n">eb</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">depth</span> <span class="o">(</span><span class="n">let_</span> <span class="n">v</span> <span class="n">ed</span> <span class="n">eb</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
    <span class="n">lc&#39;</span> <span class="o">(</span><span class="n">open_fresh</span> <span class="n">v</span> <span class="n">L</span> <span class="n">eb</span><span class="o">)</span>
  <span class="n">using_well_founded</span> <span class="o">{</span>
    <span class="n">dec_tac</span> <span class="o">:=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span><span class="o">,</span>
    <span class="n">rel_tac</span> <span class="o">:=</span> <span class="bp">λ_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">measure_wf</span> <span class="n">depth</span><span class="bp">⟩</span><span class="o">]</span> <span class="o">}</span>
</pre></div>


<p>It would be nice if I could, say, use <code>simp</code> for the well-founded condition instead of all of those <code>have ... := simp</code>s. Also, I tried <code>instance : has_sizeof (exp V) := ⟨depth⟩</code> so that I wouldn't need to specify <code>rel_tac := λ_ _, `[exact ⟨_, measure_wf depth⟩]</code>, but that didn't seem to work. Any suggestions?</p>

#### [ Simon Hudon (Sep 12 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133803664):
<p>For the <code>have</code>, what if you had:</p>
<div class="codehilite"><pre><span></span> <span class="n">dec_tac</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="bp">&gt;&gt;</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span><span class="o">,</span>
</pre></div>


<p>in your <code>  using_well_founded</code> clause?</p>

#### [ Sean Leather (Sep 12 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133812958):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Good idea, but, unfortunately, that doesn't work.</p>

#### [ Sean Leather (Sep 12 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815702):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you have any thoughts on the above in this thread? Basically, I want to write <code>lc'</code> without <code>have</code>ing to redeclare all of these theorems locally. Ideally, I would like to avoid <code>using_well_founded</code> at all, but that's secondary.</p>

#### [ Mario Carneiro (Sep 12 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815806):
<p>did Simon's suggestion work?</p>

#### [ Sean Leather (Sep 12 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815820):
<p>No.</p>

#### [ Kenny Lau (Sep 12 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815841):
<p>what is <code>exp</code>?</p>

#### [ Mario Carneiro (Sep 12 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815845):
<p>Why not? If all your proofs are <code>by simp</code> then it should work as a discharger</p>

#### [ Sean Leather (Sep 12 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815909):
<div class="codehilite"><pre><span></span><span class="n">assumption</span> <span class="n">tactic</span> <span class="n">failed</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">V</span><span class="o">,</span>
<span class="n">lc&#39;</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="n">lc&#39;</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">),</span> <span class="o">(</span><span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">y</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">),</span> <span class="n">has_well_founded</span><span class="bp">.</span><span class="n">r</span> <span class="bp">_</span><span class="n">y</span> <span class="bp">_</span><span class="n">x</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="n">ef</span> <span class="n">ea</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">,</span>
<span class="bp">_</span><span class="n">F</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">y</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">),</span> <span class="n">has_well_founded</span><span class="bp">.</span><span class="n">r</span> <span class="bp">_</span><span class="n">y</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="err">⊢</span> <span class="n">measure</span> <span class="n">depth</span> <span class="n">ef</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Sep 12 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815914):
<p>actually you should just use <code> `[simp]</code> as the discharger</p>

#### [ Sean Leather (Sep 12 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815924):
<p>That was what I initially tried, too. No luck.</p>

#### [ Mario Carneiro (Sep 12 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815936):
<p>make that <code>simp [measure, inv_image]</code></p>

#### [ Sean Leather (Sep 12 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133815950):
<div class="codehilite"><pre><span></span><span class="n">assumption</span> <span class="n">tactic</span> <span class="n">failed</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">V</span><span class="o">,</span>
<span class="n">lc&#39;</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="n">lc&#39;</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">),</span> <span class="o">(</span><span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">y</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">),</span> <span class="n">has_well_founded</span><span class="bp">.</span><span class="n">r</span> <span class="bp">_</span><span class="n">y</span> <span class="bp">_</span><span class="n">x</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="n">ef</span> <span class="n">ea</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">,</span>
<span class="bp">_</span><span class="n">F</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">y</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">),</span> <span class="n">has_well_founded</span><span class="bp">.</span><span class="n">r</span> <span class="bp">_</span><span class="n">y</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="err">⊢</span> <span class="n">inv_image</span> <span class="n">has_lt</span><span class="bp">.</span><span class="n">lt</span> <span class="n">depth</span> <span class="n">ef</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Sep 12 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816009):
<p>I searched <code>inductive.*exp</code> but nothing came up</p>

#### [ Mario Carneiro (Sep 12 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816016):
<p>it's in sean's repo</p>

#### [ Sean Leather (Sep 12 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816032):
<div class="codehilite"><pre><span></span><span class="bp">`</span><span class="o">[</span><span class="n">simp</span> <span class="o">[</span><span class="n">measure</span><span class="o">,</span> <span class="n">inv_image</span><span class="o">]]</span> <span class="bp">&gt;&gt;</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span><span class="o">,</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">assumption</span> <span class="n">tactic</span> <span class="n">failed</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">no</span> <span class="n">goals</span>
</pre></div>

#### [ Mario Carneiro (Sep 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816043):
<p>and drop the <code>asssumption</code></p>

#### [ Sean Leather (Sep 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816047):
<p>Kenny, it's an inductive. But it's not relevant to the issue.</p>

#### [ Sean Leather (Sep 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816056):
<p>Ah ha!</p>

#### [ Sean Leather (Sep 12 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816138):
<p>That works. Thanks! Any way to simplify away the <code>using_well_founded</code>?</p>

#### [ Sean Leather (Sep 12 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816244):
<p>Can I define my own instance of...?</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">has_well_founded</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">wf</span> <span class="o">:</span> <span class="n">well_founded</span> <span class="n">r</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (Sep 12 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133816270):
<p>I mean, will defining an instance of <code>has_well_founded</code> allow me to remove <code>using_well_founded</code>?</p>

#### [ Simon Hudon (Sep 13 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133886977):
<p>I think so. You may also have to set the priority of <code>has_well_founded_of_has_sizeof</code> to 0</p>

#### [ Chris Hughes (Sep 13 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well-founded%20exists/near/133887243):
<p>I did this for polynomials. I had to write <code>dec_tac := tactic.assumption </code> everywhere, but other than that it worked.</p>


{% endraw %}
