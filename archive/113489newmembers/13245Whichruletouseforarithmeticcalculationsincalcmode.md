---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13245Whichruletouseforarithmeticcalculationsincalcmode.html
---

## Stream: [new members](index.html)
### Topic: [Which rule to use for arithmetic calculations in calc mode?](13245Whichruletouseforarithmeticcalculationsincalcmode.html)

---


{% raw %}
#### [ Yufan Lou (Oct 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135641895):
<p>I am trying to prove for any odd number n, 3n + 5 is even as a practice. In the calc steps I have:<br>
3 * n + 5 = ...<br>
            ... = 3 * 2 * k + 3 + 5 : by rw mul_assoc<br>
            ... = 3 * 2 * k + 8        : by ?</p>
<p>What do I need to put in place of the question mark? I wrote the proof this way so as to closely track how I would write it manually, in hope I may introduce this to my classmates as a tool, so I don’t need to simplify it further.</p>

#### [ Kenny Lau (Oct 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135641906):
<p>by rw add_assoc</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642081):
<p><code>rfl</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642100):
<p><code>norm_num</code> is the correct answer though</p>

#### [ Yufan Lou (Oct 12 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642393):
<p>norm_num is unknown identifier tho</p>

#### [ Yufan Lou (Oct 12 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642396):
<p>I am using the online version</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642442):
<blockquote>
<p>norm_num is unknown identifier tho</p>
</blockquote>
<p>Just import tactic.norm_num</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642532):
<p>I'm not sure if the online version has <code>tactic.norm_num</code>, it's got a quite old version of mathlib</p>

#### [ Yufan Lou (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642552):
<p>import went through</p>

#### [ Yufan Lou (Oct 12 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642587):
<p>curiously it still doesn't work. rw add_assoc works btw</p>

#### [ Yufan Lou (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642644):
<p>Given by norm_num: <code>⊢ 3 + (5 + 6 * k) = 8 + 6 * k</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642649):
<p>You have to reassociate first</p>

#### [ Kenny Lau (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642651):
<blockquote>
<p><code>norm_num</code> is the correct answer though</p>
</blockquote>
<p>I would prefer <code>rfl</code> over <code>norm_num</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642664):
<p><code>norm_num</code> will evaluate closed term expressions but they have to all be gathered together</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642673):
<p><code>rfl</code> works in small cases, especially on <code>nat</code></p>

#### [ Yufan Lou (Oct 12 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642678):
<p>Problem I have with rfl is that the error is not helpful at all</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642734):
<p>But stuff like <code>3 + 5 = 8</code> on <code>real</code> needs <code>norm_num</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642744):
<blockquote>
<p>Problem I have with rfl is that the error is not helpful at all</p>
</blockquote>
<p>it just means they are not definitionally equal</p>

#### [ Yufan Lou (Oct 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642753):
<p>oh for my case I only work with int and nat</p>

#### [ Yufan Lou (Oct 12 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642759):
<p>no need for real here</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642768):
<p>Also stuff like <code>100 * 35 = 3500</code> should not be done by <code>rfl</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642770):
<p>sure</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642782):
<p>but for numbers less than 10 you should be fine</p>

#### [ Yufan Lou (Oct 12 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642836):
<p>cuz <code>rfl</code> does induction?</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642841):
<p>It calculates both sides to a normal form in unary</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642842):
<p>so it's exponentially slower than <code>norm_num</code> in large cases</p>

#### [ Yufan Lou (Oct 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135642851):
<p>gotcha</p>

#### [ Yufan Lou (Oct 12 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643128):
<blockquote>
<p>You have to reassociate first</p>
</blockquote>
<p>this kinda beats the purpose of replacing <code>rw add_assoc</code> tho</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643205):
<p>that's true</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643207):
<p><code>ring</code> will actually solve the whole goal in this case</p>

#### [ Yufan Lou (Oct 12 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643211):
<div class="codehilite"><pre><span></span>... = 3 * 2 * k + 8            : by rw add_assoc
 ... = 2 * 3 * k + 8            : by rw mul_comm
</pre></div>


<p>gives me <code>⊢ k * (3 * 2) + 8 = 2 * 3 * k + 8</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643221):
<p>you can do <code>mul_comm 2</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643229):
<p>to give lean a bit of a hint of which mul to comm</p>

#### [ Yufan Lou (Oct 12 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643233):
<p>gotcha</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643244):
<p>that's one that <code>norm_num</code> can solve btw... or <code>rfl</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643287):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>

<span class="kn">theorem</span> <span class="n">test</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">5</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">norm_num</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test</span>

<span class="kn">theorem</span> <span class="n">test1</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">5</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">bit1_add_bit1</span><span class="o">,</span> <span class="n">norm_num</span><span class="bp">.</span><span class="n">one_add_bit0</span><span class="o">,</span>
<span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_bit1</span><span class="o">,</span> <span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_one</span><span class="o">]</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test1</span>

<span class="kn">theorem</span> <span class="n">test2</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">5</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span>
<span class="k">calc</span>  <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">5</span>
    <span class="bp">=</span> <span class="n">bit0</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1</span> <span class="o">((</span><span class="mi">1</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">))</span> <span class="o">:</span> <span class="n">norm_num</span><span class="bp">.</span><span class="n">bit1_add_bit1</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">bit0</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1</span> <span class="o">(</span><span class="n">bit1</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)))</span> <span class="o">:</span> <span class="n">congr_arg</span> <span class="bp">_</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="bp">_</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">one_add_bit0</span> <span class="bp">_</span><span class="o">))</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">bit0</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)))</span> <span class="o">:</span> <span class="n">congr_arg</span> <span class="bp">_</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_bit1</span> <span class="bp">_</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">bit0</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)))</span> <span class="o">:</span> <span class="n">congr_arg</span> <span class="bp">_</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="bp">_</span> <span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_one</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">test2</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">+</span> <span class="mi">5</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span>
  <span class="o">(</span><span class="n">id</span>
     <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">trans</span>
        <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a</span> <span class="n">a_1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">e_1</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a_1</span><span class="o">)</span> <span class="o">(</span><span class="n">a_2</span> <span class="n">a_3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">e_2</span> <span class="o">:</span> <span class="n">a_2</span> <span class="bp">=</span> <span class="n">a_3</span><span class="o">),</span> <span class="n">congr</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">eq</span> <span class="n">e_1</span><span class="o">)</span> <span class="n">e_2</span><span class="o">)</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">+</span> <span class="mi">5</span><span class="o">)</span> <span class="mi">8</span>
           <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">subst_into_sum</span> <span class="mi">3</span> <span class="mi">5</span> <span class="mi">3</span> <span class="mi">5</span> <span class="mi">8</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="mi">3</span><span class="o">)</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="mi">5</span><span class="o">)</span>
              <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">bit1_add_bit1_helper</span> <span class="mi">1</span> <span class="mi">2</span> <span class="mi">3</span> <span class="mi">4</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">one_add_bit0</span> <span class="mi">1</span><span class="o">)</span>
                 <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_bit1_helper</span> <span class="mi">1</span> <span class="mi">2</span> <span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_one</span><span class="o">)))</span>
           <span class="mi">8</span>
           <span class="mi">8</span>
           <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="mi">8</span><span class="o">))</span>
        <span class="o">(</span><span class="n">eq_true_intro</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="mi">8</span><span class="o">))))</span>
  <span class="n">trivial</span>

<span class="kn">theorem</span> <span class="n">test1</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">+</span> <span class="mi">5</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span> <span class="o">(</span><span class="n">id</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">+</span> <span class="mi">5</span> <span class="bp">=</span> <span class="mi">8</span><span class="o">))</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">bit1_add_bit1</span> <span class="mi">1</span> <span class="mi">2</span><span class="o">)))</span>
  <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span> <span class="o">(</span><span class="n">id</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">))</span> <span class="bp">=</span> <span class="mi">8</span><span class="o">))</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">one_add_bit0</span> <span class="mi">1</span><span class="o">)))</span>
     <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span> <span class="o">(</span><span class="n">id</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1</span> <span class="mi">3</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">8</span><span class="o">))</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_bit1</span> <span class="mi">1</span><span class="o">)))</span>
        <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span> <span class="o">(</span><span class="n">id</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="n">bit0</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1</span> <span class="mi">1</span><span class="o">))</span> <span class="bp">=</span> <span class="mi">8</span><span class="o">))</span> <span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_one</span><span class="o">))</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="mi">8</span><span class="o">))))</span>

<span class="kn">theorem</span> <span class="n">test2</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">+</span> <span class="mi">5</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">trans</span>
  <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">bit1_add_bit1</span> <span class="mi">1</span> <span class="mi">2</span><span class="o">)</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">bit0</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">norm_num</span><span class="bp">.</span><span class="n">add1</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">one_add_bit0</span> <span class="mi">1</span><span class="o">))))</span>
     <span class="o">(</span><span class="n">congr_arg</span> <span class="n">bit0</span> <span class="o">(</span><span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_bit1</span> <span class="mi">1</span><span class="o">)))</span>
  <span class="o">(</span><span class="n">congr_arg</span> <span class="n">bit0</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">bit0</span> <span class="n">norm_num</span><span class="bp">.</span><span class="n">add1_one</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643290):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Can Lean be better at golfing?</p>

#### [ Kenny Lau (Oct 12 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643294):
<p>or is that actually pointless?</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643310):
<p>Lean doesn't make it easy to golf proofs in tactics</p>

#### [ Kenny Lau (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643315):
<p>I see</p>

#### [ Yufan Lou (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643321):
<p>nevermind... the import seems successful but norm_num is not actually imported</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643376):
<p>I would prefer that lean produced kind of short proofs (i.e. not obviously stupid things) but unfortunately <code>dsimp</code> ignores proof arguments</p>

#### [ Yufan Lou (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643444):
<p>btw <code>rfl</code> didn't work on the replacement of <code>rw mul_comm 2</code>either</p>

#### [ Yufan Lou (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643450):
<p><code>rfl</code> is less powerful than I thought</p>

#### [ Yufan Lou (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643457):
<p>or is it just in calc mode</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643458):
<p>that's surprising</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643471):
<p>this works for me in the web editor:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">+</span> <span class="mi">5</span> <span class="bp">=</span> <span class="mi">8</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span>
</pre></div>

#### [ Mario Carneiro (Oct 12 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643482):
<p>do you have a MWE with your unrflable proof?</p>

#### [ Yufan Lou (Oct 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643603):
<p>Maybe I had a typo... a minute</p>

#### [ Yufan Lou (Oct 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643691):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">is_odd</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_even</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h1</span> <span class="o">(</span><span class="k">assume</span> <span class="n">k</span><span class="o">,</span> <span class="k">assume</span> <span class="n">hw</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>
    <span class="o">(</span><span class="k">calc</span>
      <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">hw</span><span class="o">]</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">2</span>     <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">rfl</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rfl</span><span class="o">)</span>
</pre></div>

#### [ Yufan Lou (Oct 12 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643806):
<p><code>rfl</code> doesn't work anytime I need to adjust association right</p>

#### [ Yufan Lou (Oct 12 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643807):
<p>same as <code>norm_num</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643819):
<p><code>rfl</code> works iff the two expressions are definitionally equal</p>

#### [ Kenny Lau (Oct 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643823):
<p><code>2*(n+1)</code> for natural numbers is defined to be <code>2*n+2</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643826):
<p>that's unfolding definition of natural number multiplication</p>

#### [ Yufan Lou (Oct 12 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643888):
<p>it doesn't work tho</p>

#### [ Yufan Lou (Oct 12 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135643945):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">is_odd</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_even</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h1</span> <span class="o">(</span><span class="k">assume</span> <span class="n">k</span><span class="o">,</span> <span class="k">assume</span> <span class="n">hw</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>
    <span class="o">(</span><span class="k">calc</span>
      <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">hw</span><span class="o">]</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">2</span>     <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">add_assoc</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">*</span> <span class="mi">1</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">mul_one</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>   <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">mul_add</span>
        <span class="o">))</span>
</pre></div>


<p>without <code>rfl</code> this works, but I can't seem to replace any of them with <code>rw rfl</code>or <code>rfl</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644025):
<p><code>rfl</code> is a term not a tactic</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644031):
<p>so there is no <code>by</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644036):
<p>also <code>by rw rfl</code> is always redundant (does nothing)</p>

#### [ Yufan Lou (Oct 12 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644042):
<p>ah i see</p>

#### [ Yufan Lou (Oct 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644080):
<p>didn't think to replace by as well</p>

#### [ Yufan Lou (Oct 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644090):
<p>works now</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644091):
<p>there is a tactic version, called <code>refl</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644093):
<p>so <code>by refl</code> and <code>rfl</code> are usually interchangeable</p>

#### [ Yufan Lou (Oct 12 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644154):
<p>okay for simple calc proofs I can just put <code>: rfl</code> after each step nice</p>

#### [ Yufan Lou (Oct 12 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644160):
<p>thx y'all</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644176):
<p>actually a <code>: rfl</code> calc step can usually just be deleted entirely</p>

#### [ Yufan Lou (Oct 12 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644221):
<p>I know, writing out just for demonstration</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644224):
<p>right</p>

#### [ Yufan Lou (Oct 12 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644568):
<p>while we are at it is there a one-line proof of that theorem</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644653):
<p>what are the definitions?</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644664):
<p>MWE please</p>

#### [ Yufan Lou (Oct 12 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644674):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_even</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">b</span>
<span class="n">def</span> <span class="n">is_odd</span> <span class="o">(</span><span class="n">a</span><span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span>
<span class="kn">example</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">is_odd</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_even</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Oct 12 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644698):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">},</span> <span class="n">is_odd</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">is_even</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Oct 12 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644753):
<p>turns out the important part of the theorem is <code>2 * n + 1 + 1 = 2 * (n + 1)</code> which is true by definition</p>

#### [ Yufan Lou (Oct 12 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644768):
<p>cool</p>

#### [ Yufan Lou (Oct 12 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644777):
<p>what does <code>|</code> do and why <code>_</code> following it?</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644786):
<p>I'm using the equation compiler to pattern match on the exists</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644831):
<p>the <code>_</code> is the <code>n</code> from the statement</p>

#### [ Yufan Lou (Oct 12 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644838):
<p>ahh pattern matching thx</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644851):
<p>but it is matched against <code>2*n+1</code> because I matched on the equality too</p>

#### [ Yufan Lou (Oct 12 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135644929):
<p>using <code>rfl</code> in pattern matching is pretty eye opening</p>

#### [ Yufan Lou (Oct 12 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645149):
<p>Could you explain the pattern matching more thoroughly?</p>

#### [ Yufan Lou (Oct 12 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645163):
<div class="codehilite"><pre><span></span><span class="bp">|</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Oct 12 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645594):
<p>Since exists and eq are both inductive types, you can match on them, meaning you have to give a case for each constructor. Both only have one constructor, so there is only one case, where the exists is the <code>Exists.mk</code> function (which can also be written using the angle pair bracket) and the eq has the contstructor for equality which is <code>rfl</code>. If you put in both of those for the second argument, the first argument is forced to be <code>(2*n+1)</code> (Lean can figure this out, but if you want you can replace the <code>_</code> with <code>.(2*n+1)</code>, where the dot means that this argument's value is forced by later arguments.)</p>
<p>So in this case of the match, we have to prove the statement with <code>n</code> replaced with <code>2*n+1</code>, that is, <code>is_even (2 * n + 1 + 1)</code>. This is defeq to an exists, so I use the angle brackets to supply the witness, which is <code>n+1</code>, and the proof of equality, of type <code>2 * n + 1 + 1 = 2 * (n + 1)</code>, which as I said is true by reflexivity because both sides are defeq.</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645685):
<p>the defeq chain looks like this btw:</p>
<div class="codehilite"><pre><span></span>2 * (n + 1)
= 2 * succ n
= 2 * n + 2
= 2 * n + succ 1
= succ (2 * n + 1)
= succ (succ (2 * n))
</pre></div>


<div class="codehilite"><pre><span></span>2 * n + 1 + 1
= succ (2 * n + 1)
= succ (succ (2 * n))
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645733):
<div class="codehilite"><pre><span></span>2 * (n + 1)
= 2 * (succ (n + 0))
= 2 * (succ n)
= 2 * n + 2
= ...
</pre></div>

#### [ Mario Carneiro (Oct 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Which%20rule%20to%20use%20for%20arithmetic%20calculations%20in%20calc%20mode%3F/near/135645741):
<p>I'll omit the steps that unfold the definition of <code>+</code>. :)</p>


{% endraw %}
