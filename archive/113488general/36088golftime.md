---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36088golftime.html
---

## Stream: [general](index.html)
### Topic: [golf time](36088golftime.html)

---


{% raw %}
#### [ Reid Barton (May 11 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126431532):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">finset</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">range</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="err">\</span> <span class="n">range</span> <span class="n">n</span> <span class="bp">=</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:=</span>
</pre></div>

#### [ Chris Hughes (May 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126433149):
<p>Not very pleased with my effort. I certainly lose points for stability</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">range</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="err">\</span> <span class="n">range</span> <span class="n">n</span> <span class="bp">=</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:=</span>
<span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">mem_sdiff</span><span class="o">,</span> <span class="n">mem_range</span><span class="o">,</span> <span class="n">le_iff_eq_or_lt</span><span class="bp">.</span><span class="n">symm</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">le_antisymm_iff</span><span class="o">]</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span>
    <span class="k">by</span> <span class="n">simp</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}</span><span class="bp">⟩</span>
</pre></div>

#### [ Chris Hughes (May 11 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126433411):
<p>More stable version</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">range</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="err">\</span> <span class="n">range</span> <span class="n">n</span> <span class="bp">=</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:=</span>
<span class="n">ext</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mem_sdiff</span><span class="o">,</span> <span class="n">mem_range</span><span class="o">,</span> <span class="n">mem_range</span><span class="o">,</span> <span class="n">singleton_eq_singleton</span><span class="o">,</span> <span class="n">mem_singleton</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">le_antisymm</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_of_lt_succ</span> <span class="n">h</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">le_of_not_gt</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
  <span class="k">by</span> <span class="n">simp</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126435105):
<p>It's this sort of question that gives Lean a bad name amongst mathematicians.</p>

#### [ Kevin Buzzard (May 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126435106):
<p>"it's obvious"? ;-)</p>

#### [ Mario Carneiro (May 12 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126440450):
<div class="codehilite"><pre><span></span>example {n : ℕ} : range (n+1) \ range n = {n} :=
ext.2 $ by simp [-range_succ, nat.lt_succ_iff, le_antisymm_iff]
</pre></div>

#### [ Mario Carneiro (May 12 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126440496):
<p>i.e. "it's obvious"</p>

#### [ Kevin Buzzard (May 12 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126455763):
<p>:-)</p>

#### [ Kevin Buzzard (May 12 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126455765):
<p>I'm not so sure that one of my first year undergraduates would find that proof obvious to spot :-)</p>

#### [ Reid Barton (May 12 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126465086):
<p>When do we get <code>omega</code> or a Presburger arithmetic solver?</p>

#### [ Andrew Ashworth (May 14 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126521067):
<blockquote>
<p>When do we get <code>omega</code> or a Presburger arithmetic solver?</p>
</blockquote>
<p>You're not the first person to ask this in the chat, hah. The answer is: whenever a motivated contributer decides to port the Coq implementation to Lean. Leo and the other developers are not interested in doing this work as it is non-trivial and not academically interesting, so it can't lead to something publishable.</p>

#### [ Mario Carneiro (May 14 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126521751):
<p>I think it also has dubious merit, I'm not sure that we actually have goals that fit the pattern very often to begin with</p>

#### [ Mario Carneiro (May 14 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126521812):
<p>That said, I know that Seul Baek (my fellow CMU PhD) has implemented Cooper's algorithm for linear arithmetic over integers, and maybe he will pop in here someday to show it off</p>

#### [ Andrew Ashworth (May 14 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126523011):
<p>Well, in defense of the people who really want omega, it's not so much that many goals may need a Presburger arith solver. However, when you do have a problem of that type, a tactic that solves them in one tactic invocation is convenient. It has a well-defined scope and application, and is not heuristics-based, so it will always succeed if the problem is appropriate.</p>

#### [ Andrew Ashworth (May 14 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126523100):
<p>In Software Foundations Vol 3, which discusses verified data structures, the author uses omega quite frequently</p>

#### [ Kevin Buzzard (May 14 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126534010):
<p>As <span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> points out, this question (porting omega) does come up again from time to time. Can someone give me an idea of how much work this would actually be? Obviously I am in no position to do it because I only know epsilon about tactics and have no time anyway, and perhaps one should at least wait until Lean 4 before embarking on such a project, but in the long term is it the sort of thing one can get a Masters student to do for a project, for example? I just have no  idea.</p>

#### [ Andrew Ashworth (May 14 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126546657):
<p>Well, looking at the Coq source, it seems omega is around ~3500 lines of mixed ML and Ltac. For new work, you can probably estimate ~30 lines of finished, complete code / day, leading to a time estimate of ~120 days of full-time work. However, this isn't a completely new rewrite, but a translation of existing code, so maybe handwave and cut the time required in half... so about two months of work.</p>

#### [ Johan Commelin (May 15 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126582480):
<p>I would be interested in feedback on the definition of <code>\sigma</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fin</span> <span class="n">order</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">linear_order</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span><span class="n">le</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">less_than_or_equal</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span> <span class="n">b</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_refl</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_trans</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span> <span class="n">b</span><span class="bp">.</span><span class="mi">1</span> <span class="n">c</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">eq_of_veq</span> <span class="err">$</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_antisymm</span> <span class="n">a</span> <span class="n">b</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">le_total</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_total</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">lt</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span> <span class="n">b</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">lt_iff_le_not_le</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_iff_le_not_le</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span> <span class="n">b</span><span class="bp">.</span><span class="mi">1</span><span class="o">}</span>

<span class="n">def</span> <span class="n">σ</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="k">if</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">raise_fin</span> <span class="n">i</span> <span class="k">then</span> <span class="n">a</span> <span class="k">else</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pred</span> <span class="n">a</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="n">by_cases</span> <span class="o">(</span><span class="n">a</span> <span class="bp">≤</span> <span class="n">raise_fin</span> <span class="n">i</span><span class="o">),</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">if_pos</span> <span class="n">h</span><span class="o">],</span> <span class="n">exact</span> <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="n">h</span> <span class="n">i</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">if_neg</span> <span class="n">h</span><span class="o">],</span> <span class="n">simp</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">apos</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">begin</span>
        <span class="k">show</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span><span class="o">,</span>
        <span class="n">apply</span> <span class="n">lt_of_le_of_lt</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">zero_le</span> <span class="bp">_</span><span class="o">)</span> <span class="n">h</span><span class="o">,</span>
    <span class="kn">end</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">pred</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">n</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_pred_eq_of_pos</span> <span class="n">apos</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pred_le_pred</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span> <span class="o">}</span>
  <span class="kn">end</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (May 15 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126582865):
<p>You could skip the whole <code>linear_order</code> business by writing the if condition as <code>a.1 &lt;= i.1</code></p>

#### [ Johan Commelin (May 15 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126582980):
<p>Yes, that is true... but I want to prove stuff about monotone functions <code>fin n \to fin m</code></p>

#### [ Johan Commelin (May 15 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126582982):
<p>So I need it when I start using <code>\sigma</code></p>

#### [ Mario Carneiro (May 15 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126583130):
<p>golfed:</p>
<div class="codehilite"><pre><span></span>def σ {n : ℕ} (i : fin n) (a : fin (n+1)) : fin n :=
⟨if a.1 ≤ i.1 then a else nat.pred a,
  begin
    by_cases a.1 ≤ i.1; simp [h],
    { exact lt_of_le_of_lt h i.2 },
    { exact (nat.sub_lt_right_iff_lt_add
        (lt_of_le_of_lt (nat.zero_le i.1) (not_le.1 h))).2 a.2 },
  end⟩
</pre></div>


<p>what's with the mysterious name?</p>

#### [ Johan Commelin (May 15 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126583282):
<p>Well, <a href="https://en.wikipedia.org/wiki/Simplicial_set#Face_and_degeneracy_maps" target="_blank" title="https://en.wikipedia.org/wiki/Simplicial_set#Face_and_degeneracy_maps">https://en.wikipedia.org/wiki/Simplicial_set#Face_and_degeneracy_maps</a></p>

#### [ Johan Commelin (May 15 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126583289):
<p>And thanks for golfing!!</p>

#### [ Patrick Massot (May 15 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126584504):
<p>Nice idea to do simplicial sets!</p>

#### [ Sean Leather (May 15 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126586836):
<p>(deleted)</p>

#### [ Sean Leather (May 15 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126586921):
<p>Oh, never mind.</p>

#### [ Sean Leather (May 15 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587382):
<p>Here's my adaptation of Mario's version:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">σ</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">a</span><span class="bp">.</span><span class="n">val</span> <span class="bp">≤</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="k">then</span>
  <span class="bp">⟨</span><span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span> <span class="n">lt_of_le_of_lt</span> <span class="n">h</span> <span class="n">i</span><span class="bp">.</span><span class="n">is_lt</span><span class="bp">⟩</span>
<span class="k">else</span>
  <span class="bp">⟨</span><span class="n">a</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">pred</span><span class="o">,</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">sub_lt_right_iff_lt_add</span> <span class="o">(</span><span class="n">lt_of_le_of_lt</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">zero_le</span> <span class="o">(</span><span class="n">not_le</span><span class="bp">.</span><span class="n">mp</span> <span class="n">h</span><span class="o">)))</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">a</span><span class="bp">.</span><span class="n">is_lt</span><span class="bp">⟩</span>
</pre></div>

#### [ Johan Commelin (May 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587558):
<p>That doesn't parse, right? The <code>h</code> in the <code>then</code>-part is undefined.</p>

#### [ Sean Leather (May 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587563):
<p>1. I find using the structure field names (<code>val</code>, <code>is_lt</code>) and <code>mpr</code> to be better documentation than <code>.1</code> and <code>.2</code>; I usually reserve the latter for “obvious” uses such as <code>and</code>,  <code>sigma</code>, etc.<br>
2. The use of tactics in a definition momentarily confused me into thinking it was a theorem.<br>
3. The duplicate casing with both <code>if</code> and <code>by_cases</code> seems redundant to me.</p>

#### [ Sean Leather (May 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587572):
<blockquote>
<p>That doesn't parse, right? The <code>h</code> in the <code>then</code>-part is undefined.</p>
</blockquote>
<p>It does parse in my Lean. I don't think it's been changed.</p>

#### [ Johan Commelin (May 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587617):
<p>Aah, sorry, I didn't copy your <code>h</code> from the line above...</p>

#### [ Sean Leather (May 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587624):
<p><code>if then else</code> is notation for <code>ite</code> and <code>if h : p then else</code> is notation for <code>dite</code>.</p>

#### [ Sean Leather (May 15 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587806):
<p>Also, I could be wrong, but I think you might find it easier to work with the definition without tactics in it. At the very least, you know more clearly what you have to prove if you unfold it.</p>

#### [ Sean Leather (May 15 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587819):
<p>Along the same lines, having just <code>if</code> instead of <code>if</code> and <code>by_cases</code> should make it easier to work with.</p>

#### [ Johan Commelin (May 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587929):
<p>Well... until you try to prove anything about the composition of two such maps...</p>

#### [ Johan Commelin (May 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587930):
<p>Like I am trying now</p>

#### [ Johan Commelin (May 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587934):
<p>If you unfold, you suddenly have a page-filling goal (-;</p>

#### [ Kevin Buzzard (May 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587975):
<blockquote>
<p>Also, I could be wrong, but I think you might find it easier to work with the definition without tactics in it. At the very least, you know more clearly what you have to prove if you unfold it.</p>
</blockquote>
<p>It's only the proof part of the def that involves tactics, so maybe this is OK?</p>

#### [ Sean Leather (May 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126587984):
<p>That may be true.</p>

#### [ Kevin Buzzard (May 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588029):
<p>OTOH I am a bit wary of Johan's unfolding comment above...</p>

#### [ Sean Leather (May 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588087):
<blockquote>
<p>If you unfold, you suddenly have a page-filling goal (-;</p>
</blockquote>
<p>Is there a difference between the goals using the different definitions of <code>σ</code>?</p>

#### [ Johan Commelin (May 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588091):
<p>Not too much</p>

#### [ Johan Commelin (May 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588102):
<p>But you get stuff of the form <code>(\lambda h, ...)</code> where you first didn't have the <code>\lambda</code>. I think this has to do with <code>ite</code> vs <code>dite</code></p>

#### [ Kevin Buzzard (May 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588107):
<p>Johan, let me echo other people's comments that it's a great idea to do whatever it is that you're doing, which might be simplicial homology of a topological space as far as I can see. I definitely learnt the most about how Lean works at times when I was engaged in actually writing non-trivial amounts of non-trivial code, and even if I look back at my schemes work and perhaps regret some earlier design decisions (e.g. a cheap definition of the structure presheaf on an affine scheme which now has to be seriously reworked) I still learnt masses of stuff. You might well end up with a canonical "bad lecture" -- some definition of cohomology, plus not one single example worked out :-)</p>

#### [ Johan Commelin (May 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588149):
<p>Hehe</p>

#### [ Kevin Buzzard (May 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588151):
<p>But this raises the question of whether lean code is supposed to be used to teach people mathematics, and I have pretty much decided that the answer should be "no, at least for the code I write".</p>

#### [ Kevin Buzzard (May 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588153):
<p>I'm going to see Larry Paulson on Tuesday who I think has very different ideas about this.</p>

#### [ Johan Commelin (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588160):
<p>At some point in the future we need readable code, I think</p>

#### [ Kevin Buzzard (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588166):
<p>Why?</p>

#### [ Kevin Buzzard (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588170):
<p>Why can't we have unreadable code with readable documentation and comments instead?</p>

#### [ Johan Commelin (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588173):
<p>Ok, sure</p>

#### [ Kevin Buzzard (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588174):
<p>"This is what is going on here"</p>

#### [ Johan Commelin (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588177):
<p>But so far I haven't seen much comments in Lean code</p>

#### [ Kevin Buzzard (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588181):
<p><code>simp;cc;finish</code></p>

#### [ Johan Commelin (May 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588183):
<p>I know you have some comments,...</p>

#### [ Johan Commelin (May 15 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588233):
<p>but the ratio of comments/code in mathlib is pretty low</p>

#### [ Kevin Buzzard (May 15 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588234):
<p>But that's because most code you've seen has probably been written by Mario, and he's not a big commenter</p>

#### [ Johan Commelin (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588243):
<p>That's what you get when you speak Lean faster then anyone else (-;</p>

#### [ Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588247):
<p>OTOH one might argue that much of the mathlib code is "elementary" in the sense that it is proving lemmas which are trivial to a mathematician</p>

#### [ Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588250):
<p>so one might argue that this code does not need comments.</p>

#### [ Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588253):
<p>"I am proving this by induction"</p>

#### [ Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588254):
<p>"as any mathematician would"</p>

#### [ Johan Commelin (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588258):
<p>Well, I often have quite a hard time figuring out <em>which</em> lemma is being proven</p>

#### [ Kevin Buzzard (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588259):
<p>"it's just that mathematicians can't read the argument without training"</p>

#### [ Johan Commelin (May 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588262):
<p>Because the type signatures can be pretty unreadable as well</p>

#### [ Johan Commelin (May 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588306):
<p>And I think that we should at least make sure that type signatures are readable</p>

#### [ Johan Commelin (May 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588315):
<p>That's why I really loved Reid's improvement of my statement of the five lemma... He just put everything into a diagram!</p>

#### [ Kevin Buzzard (May 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588320):
<p>Yeah that was great :-)</p>

#### [ Patrick Massot (May 15 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588394):
<p>At some point Mario added a lot of comments on top of unreadable definitions and statements</p>

#### [ Patrick Massot (May 15 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126588398):
<p>But I don't know if this was continued with new stuff in mathlib</p>

#### [ Mario Carneiro (May 15 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20time/near/126609677):
<p>More precisely, I added comments on every <code>def</code> and <code>class</code> and <code>structure</code> and <code>inductive</code>. I think that is still mostly the case, I can do another pass to make sure</p>


{% endraw %}
