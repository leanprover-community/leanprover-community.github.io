---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51017notationstointroduceproofs.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [notations to introduce proofs](https://leanprover-community.github.io/archive/113488general/51017notationstointroduceproofs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastien Gouezel (Oct 15 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815299):
<p>In the following snippet,</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">foo</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span>        <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">B</span><span class="o">:=</span> <span class="k">calc</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="k">show</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span>          <span class="o">,</span> <span class="k">by</span> <span class="n">simp</span>
<span class="kn">end</span>
</pre></div>


<p>you can see that a proof after <code>have</code> is introduced by <code>:=</code>, after <code>calc</code> by <code>:</code> and after <code>show</code> by <code>,</code>. And they can essentially not be used one for the other (the only allowed change is to use <code>,</code> instead of <code>:=</code> on the first line). I am plainly used to it, but I would like to understand the rationale behind it. Is it to ease parsing? Or just for historical reasons? Would it make sense to use, say, <code>:=</code> everywhere, to avoid confusing newcomers for no reason?</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815435):
<p>Certainly <code>calc</code> would make sense with <code>:=</code></p>

#### [ Mario Carneiro (Oct 15 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815449):
<p>the commas in <code>show</code> and <code>have</code> are likely due to influence from Isar</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815458):
<p>Of course you should be looking at term proofs not tactic proofs, which are at best an approximation of the term equivalents</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815503):
<p>I'm not sure what notation Isar uses for <code>let</code>. Do you?</p>

#### [ Sebastien Gouezel (Oct 15 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815645):
<p>There are no commas in Isar. The formula to be proved is enclosed in quotes, and then you give the proof. Either it is a direct proof, and then you just write something like <code>using foo by auto</code>. Or it is a complex proof, and it is enclosed in <code>proof ... qed</code>. The <code>let</code> equivalent is called <code>define</code>, and used like <code>define foo where "foo = 0"</code>.</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815713):
<p>interesting. That's more different than I expected. Has it changed significantly in the past 10 years?</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815726):
<p>the base Isar syntax, I mean</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815737):
<p>Maybe it is Mizar influence then?</p>

#### [ Sebastien Gouezel (Oct 15 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815838):
<p>The <code>define</code>syntax is a recent change, it used to be <code>def "foo  = 0"</code>.</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815881):
<p>I was under the impression that the original term mode syntax of lean was basically lifted directly from the syntax of another language, probably Isar</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815886):
<p>and it has since been simplified a bit but is otherwise unchanged</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815898):
<p>like I think <code>and have</code> and <code>hence</code> used to exist and don't anymore</p>

#### [ Sebastien Gouezel (Oct 15 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135815958):
<p>Since formulas to be proved are enclosed in quotes in Isar, you don't a separator as in Lean. The comma makes sense, as would <code>:=</code>, but having two or three different separators depending on the context might be misleading to newcomers. Will it be uniformized in Lean 4, or is the syntax expected not to change?</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816033):
<p>I think syntax changes like that are on the table</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816039):
<p>I would be in support of using more <code>:=</code></p>

#### [ Sebastien Gouezel (Oct 15 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816055):
<p>I agree.</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816057):
<p>and drop the <code>from</code></p>

#### [ Mario Carneiro (Oct 15 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816116):
<p>i.e. <code>have A := proof in B</code> or <code>have A := by tac in B</code></p>

#### [ Mario Carneiro (Oct 15 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816119):
<p><code>show A := proof</code></p>

#### [ Mario Carneiro (Oct 15 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816182):
<p><code>calc A = B := proof ... = C := proof</code></p>

#### [ Mario Carneiro (Oct 15 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816239):
<p>although I guess <code>have in</code> has the problem that it won't look like the tactic version which is <code>have A := proof, tac</code></p>

#### [ Johannes Hölzl (Oct 15 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816298):
<p>I would prefer to get rid of the <code>in</code> in <code>let</code> and just write <code>let a := x, ...</code></p>

#### [ Rob Lewis (Oct 15 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816310):
<p>I don't mind the <code>from</code> so much, it makes things read slightly more naturally. Although I'm sure I wouldn't miss it for long if it disappeared. I get more annoyed with the difference between term and tactic <code>have</code>.</p>

#### [ Johannes Hölzl (Oct 15 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816311):
<p>and <code>have h : A, by tac, ...</code> or <code>have h : A := ..., ...</code></p>

#### [ Mario Carneiro (Oct 15 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816388):
<p>I think that <code>have h : A := by tac, ...</code> is more uniform. Putting a comma in there doesn't seem to win much</p>

#### [ Johannes Hölzl (Oct 15 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816389):
<p>it would also be nice to have parameters for <code>have</code> and <code>show</code>:<br>
<code>have h (a : A) (b : B) : T := ..., ...</code></p>

#### [ Mario Carneiro (Oct 15 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816412):
<p>short story: <code>let</code> and <code>have</code> should have the same parser</p>

#### [ Sebastien Gouezel (Oct 15 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816422):
<blockquote>
<p>and <code>have h : A, by tac, ...</code> or <code>have h : A := ..., ...</code></p>
</blockquote>
<p>So you would still use <code>,</code> to introduce a proof, and to separate a statement from the next. I think I would favor <code>:=</code> to introduce proofs, and <code>,</code> to go to the next statement (removing <code>in</code>, as you say).</p>

#### [ Johannes Hölzl (Oct 15 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816434):
<p>the comma would be just short form for tactic proofs.</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816502):
<p>right, but I don't think that needs to be a thing</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816509):
<p>like <code>have h : A := by tac, ...</code> and <code>have h : A := begin end, ...</code> are plenty short</p>

#### [ Johannes Hölzl (Oct 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816534):
<p>hm, yes its short enough. and nicely uniform</p>

#### [ Patrick Massot (Oct 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816538):
<p>what about <code>have h : A := { ... },</code>?</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816542):
<p>preposterous</p>

#### [ Johannes Hölzl (Oct 15 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816584):
<p>I guess it classes with set syntax</p>

#### [ Patrick Massot (Oct 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816602):
<p>Then we would still have inconsistency with the goal focussing {...}</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816617):
<p>just think of <code>begin end</code> as goal focussing brackets that work outside tactic mode</p>

#### [ Johannes Hölzl (Oct 15 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816618):
<p>another dream: not only unify <code>let</code> and <code>have</code> but unify it also with <code>def</code>, i.e. allow to use the equation compiler in proofs, ala</p>
<div class="codehilite"><pre><span></span><span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">\/</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">c</span>
<span class="bp">|</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">a</span> <span class="o">:=</span> <span class="bp">...</span>
<span class="bp">|</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">b</span> <span class="o">:=</span> <span class="bp">...</span><span class="o">,</span>
<span class="bp">...</span>
</pre></div>

#### [ Mario Carneiro (Oct 15 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816700):
<p><code>mutual have ... with ... </code>?</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135816754):
<p>yeah this makes a lot more sense than named <code>match</code></p>

#### [ Edward Ayers (Oct 15 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135819726):
<p>Is there a general notation wishlist thread?</p>

#### [ Mario Carneiro (Oct 15 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135851934):
<p>there is now</p>

#### [ Edward Ayers (Oct 15 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135852289):
<p>I would really like all of the bells and whistles you get with <code>{!...!}</code> to work with <code>_</code> when it fails to fill in the proof. But I guess that's more of an editor feature.</p>

#### [ Sebastian Ullrich (Oct 17 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/135960094):
<p>Lean 4 will most likely replace the hole syntax with <code>_</code>. Input to hole commands should be handled by the editor (which would've been basically impossible in Lean 3's infrastructure).</p>

#### [ Sebastien Gouezel (Dec 04 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/150872739):
<blockquote>
<p>Is there a general notation wishlist thread?</p>
</blockquote>
<p>Another notation wish: as for <code>rw</code> I would like <code>simp [←foo]</code> to add reversed <code>foo</code> to the simpset. And possibly to remove <code>foo</code> if it is in the simpset. Currently, if <code>foo</code> has say two variables, I achieve this with <code>simp[-foo, (foo _ _).symm]</code>.</p>

#### [ Patrick Massot (Dec 23 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152435172):
<p>New notation wishlist item: be able to replace, say in a parameter list, <code>(n : { n : ℕ // 0 &lt; n })</code> by <code>(n : ℕ // 0 &lt; n)</code> (or, even better,  <code>(n : ℕ | 0 &lt; n)</code>)</p>

#### [ Mario Carneiro (Dec 23 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152444089):
<p>is there a reason you aren't uskng two arguments?</p>

#### [ Mario Carneiro (Dec 24 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152445176):
<p>Also <code>(n &gt; 0)</code> already does almost exactly what you are saying</p>

#### [ Patrick Massot (Dec 24 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465051):
<p>It's not exactly the same. I can indeed modify my example to:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">euclid</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">),</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span> <span class="bp">//</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span><span class="bp">*</span><span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">∧</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">}</span>
<span class="bp">|</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n_pos</span><span class="o">,</span>
         <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="k">then</span>
           <span class="bp">⟨</span><span class="o">(</span><span class="mi">0</span><span class="o">,</span> <span class="n">m</span><span class="o">),</span> <span class="k">by</span> <span class="n">simp</span> <span class="bp">*⟩</span>
         <span class="k">else</span>
           <span class="k">have</span> <span class="n">m</span> <span class="bp">-</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_lt</span> <span class="bp">;</span> <span class="n">linarith</span><span class="o">,</span>
           <span class="k">let</span> <span class="bp">⟨⟨</span><span class="n">q</span><span class="o">,</span> <span class="n">r</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">H</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩⟩</span> <span class="o">:=</span> <span class="n">euclid</span> <span class="o">(</span><span class="n">m</span><span class="bp">-</span><span class="n">n</span><span class="o">)</span> <span class="n">n</span> <span class="n">n_pos</span> <span class="k">in</span>
             <span class="bp">⟨</span><span class="o">(</span><span class="n">q</span><span class="bp">+</span><span class="mi">1</span><span class="o">,</span> <span class="n">r</span><span class="o">),</span>
              <span class="bp">⟨</span><span class="k">begin</span>
                <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_eq_iff_eq_add</span> <span class="o">(</span><span class="n">le_of_not_lt</span> <span class="n">h</span><span class="o">)</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
                <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">],</span> <span class="n">ring</span><span class="o">,</span>
               <span class="kn">end</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩⟩</span>
</pre></div>


<p>but I still think the notation <code>(n : nat | n &gt; 0)</code> in a parameter list would be good to have (and they have it in Coq).</p>

#### [ Patrick Massot (Dec 24 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465176):
<p>By the way, the context is given by <a href="https://www.college-de-france.fr/site/xavier-leroy/seminar-2018-12-12-11h30.htm" target="_blank" title="https://www.college-de-france.fr/site/xavier-leroy/seminar-2018-12-12-11h30.htm">https://www.college-de-france.fr/site/xavier-leroy/seminar-2018-12-12-11h30.htm</a> which shows programming with recursion and dependent pattern matching in Coq. They have all sorts of cool tricks in this area, including deferring proof obligations after writing the program, you can have a look at minute 51 to see their version of the above function. And of course they also have <code>(q, r) : ℕ × ℕ</code> instead of our <code>p : ℕ × ℕ</code>, and a linear arithmetic tactic doing everything <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Mario Carneiro (Dec 24 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465235):
<p>You can defer proof obligations using <code>refine</code></p>

#### [ Mario Carneiro (Dec 24 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465353):
<p>Isn't this just the definition of <code>div</code>?</p>

#### [ Mario Carneiro (Dec 24 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465356):
<p>you can have a look at how it's defined in core</p>

#### [ Mario Carneiro (Dec 24 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465432):
<p>You can also write something with explicit binding for <code>q,r</code> but we try not to use it because it doesn't unfold as much</p>

#### [ Mario Carneiro (Dec 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152465552):
<p>you can do something like this (the notation isn't there, but you get the idea)</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">euclid</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">subtype</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">q</span><span class="o">,</span> <span class="n">r</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span><span class="bp">*</span><span class="n">q</span> <span class="bp">+</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Unfortunately I think lean has a bug with generating names for the auxiliary match and it clashes with the <code>let</code> statement in the body</p>

#### [ Patrick Massot (Dec 24 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152483363):
<blockquote>
<p>You can defer proof obligations using <code>refine</code></p>
</blockquote>
<p>It only defers a tiny bit. You need to close the goal before leaving the tactic block. DId you look at what <code>Program</code> does in this video? (you only have to look at the time I mentioned).</p>

#### [ Patrick Massot (Dec 24 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152483383):
<blockquote>
<p>you can have a look at how it's defined in core</p>
</blockquote>
<p>In core the output type does not assert correction. I'm not saying it should, I was doing an exercise.</p>

#### [ Patrick Massot (Dec 24 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notations%20to%20introduce%20proofs/near/152483401):
<blockquote>
<p>you can do something like this (the notation isn't there, but you get the idea)</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">euclid</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">subtype</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">q</span><span class="o">,</span> <span class="n">r</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span><span class="bp">*</span><span class="n">q</span> <span class="bp">+</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Unfortunately I think lean has a bug with generating names for the auxiliary match and it clashes with the <code>let</code> statement in the body</p>
</blockquote>
<p>Can you use well founded recursion if m and n are left of colon?</p>


{% endraw %}
