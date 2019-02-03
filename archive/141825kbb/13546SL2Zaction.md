---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/13546SL2Zaction.html
---

## Stream: [kbb](https://leanprover-community.github.io/archive/141825kbb/index.html)
### Topic: [SL2Z action](https://leanprover-community.github.io/archive/141825kbb/13546SL2Zaction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942386):
<p>I'm trying to continue Patrick's work on finiteness of the quotient <code>SL2Z \ (Mat m)</code>.<br>
This is one (approximate) step that would be useful:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">reps</span> <span class="o">:=</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span> <span class="bp">|</span> <span class="n">A</span><span class="bp">.</span><span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">A</span><span class="bp">.</span><span class="n">a</span> <span class="bp">∧</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">A</span><span class="bp">.</span><span class="n">b</span> <span class="bp">∧</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="n">A</span><span class="bp">.</span><span class="n">b</span> <span class="bp">≤</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="n">A</span><span class="bp">.</span><span class="n">d</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">ι</span> <span class="o">:</span> <span class="n">reps</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">fin</span> <span class="n">m</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">A</span><span class="o">,</span> <span class="bp">_</span>
</pre></div>

#### [ Johan Commelin (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942392):
<p>I get a deterministic timeout just for parsing the type of <code>ι</code></p>

#### [ Kenny Lau (Sep 14 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942399):
<p>is that MWE?</p>

#### [ Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942408):
<p>Proof strategy: we need to prove that <code>reps</code> is finite. Do this by injecting into <code>fin m × fin m × fin m</code>.</p>

#### [ Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942412):
<p>It is not exactly a MWE. You can find it by pulling the latest commits from <code>kbb</code></p>

#### [ Kenny Lau (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942413):
<p>I don't think that's a good strategy</p>

#### [ Johan Commelin (Sep 14 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942416):
<p>Ok, so how do you prove that <code>reps</code> is a finset?</p>

#### [ Kenny Lau (Sep 14 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942530):
<p>equiv it with <code>finset.filter (finset.univ : (finset (fin m × fin m × fin m))) sorry</code></p>

#### [ Kenny Lau (Sep 14 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942548):
<p>also why <code>int.nat_abs</code>?</p>

#### [ Johan Commelin (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942605):
<p>Because I don't know better?</p>

#### [ Kenny Lau (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942607):
<p>that's not what I mean</p>

#### [ Johan Commelin (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942608):
<p>That's what you were using in your inductive proof</p>

#### [ Kenny Lau (Sep 14 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942619):
<p>alright</p>

#### [ Kenny Lau (Sep 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942626):
<p>I think I'll prove that it's a fintype</p>

#### [ Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942779):
<p>ah</p>

#### [ Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942780):
<p>of course it times out</p>

#### [ Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942782):
<p><code>m</code> is an integer</p>

#### [ Kenny Lau (Sep 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942783):
<p><code>fin m</code> makes no sense</p>

#### [ Johan Commelin (Sep 14 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942860):
<p>Why did it time out? Why didn't it slap me in the face?</p>

#### [ Johan Commelin (Sep 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942904):
<p>It should just have errored immediately saying that <code>m</code> is not a nat.</p>

#### [ Kenny Lau (Sep 14 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133942928):
<p>I think it's searching for a coercion from int to nat</p>

#### [ Kenny Lau (Sep 14 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943083):
<p>also it still isn't a fintype</p>

#### [ Johan Commelin (Sep 14 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943209):
<p>What isn't?</p>

#### [ Kenny Lau (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943218):
<p>if m=0 I don't think it's a fintype</p>

#### [ Kenny Lau (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943220):
<p>the repr</p>

#### [ Johan Commelin (Sep 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943224):
<p>True. But you need <code>m ≠ 0</code></p>

#### [ Johan Commelin (Sep 14 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943277):
<p>Otherwise the orbits are parameterised by pairs <code>(a,b)</code> with <code>0 ≤ a</code> and <code>a,b</code> coprime.</p>

#### [ Johan Commelin (Sep 14 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943283):
<p>Inparticularinfinitelymanyorbits</p>

#### [ Johan Commelin (Sep 14 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133943379):
<p>Maybe we should have assumed <code>m : ℕ</code> from the beginning.</p>

#### [ Kenny Lau (Sep 14 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945384):
<p>why on earth is there classical.prop_decidable in the beginning of the file?</p>

#### [ Patrick Massot (Sep 14 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945453):
<p>Because it's a math file</p>

#### [ Kenny Lau (Sep 14 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945457):
<p>about integers</p>

#### [ Patrick Massot (Sep 14 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945508):
<p>The last lemma requires it</p>

#### [ Patrick Massot (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945515):
<p>it needs <code>decidable_eq (quotient (action_rel (SL2Z_M_ m)))</code></p>

#### [ Kenny Lau (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945520):
<p>I'll prove it</p>

#### [ Kenny Lau (Sep 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945523):
<p>after dinner</p>

#### [ Patrick Massot (Sep 14 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945571):
<p>I guess we can't really avoid that</p>

#### [ Kenny Lau (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945584):
<p>you're welcome to prove it if you want</p>

#### [ Johan Commelin (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945588):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Oo.ooo you released Kenny's inner wrath.</p>

#### [ Johan Commelin (Sep 14 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945593):
<p>I guess in this case you <em>can</em> prove that <code>decidable_eq</code> if you want to.</p>

#### [ Patrick Massot (Sep 14 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945606):
<p>I already proved it: <a href="https://github.com/semorrison/kbb/blob/757806ec7f9848a5eb405ca26f5a12d94932a197/src/SL2Z_generators.lean#L4" target="_blank" title="https://github.com/semorrison/kbb/blob/757806ec7f9848a5eb405ca26f5a12d94932a197/src/SL2Z_generators.lean#L4">https://github.com/semorrison/kbb/blob/757806ec7f9848a5eb405ca26f5a12d94932a197/src/SL2Z_generators.lean#L4</a></p>

#### [ Kenny Lau (Sep 14 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133945647):
<p>no you haven't</p>

#### [ Johan Commelin (Sep 14 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133964107):
<p>Cool! So now we have established finiteness of the orbit set!</p>

#### [ Patrick Massot (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971507):
<blockquote>
<p>Cool! So now we have established finiteness of the orbit set!</p>
</blockquote>
<p>Not quite, there has been some regression, let me fix that.</p>

#### [ Kenny Lau (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971536):
<p>eh... I'm editing SL2Z_generators.lean</p>

#### [ Patrick Massot (Sep 14 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971539):
<p>Done: no more sorry in SL2Z_generators.lean</p>

#### [ Kenny Lau (Sep 14 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133971561):
<p>ah I see what you did</p>

#### [ Kenny Lau (Sep 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979456):
<p>done</p>

#### [ Kenny Lau (Sep 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979472):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- correct if m ≠ 0 -/</span>
<span class="n">def</span> <span class="n">reduce</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span> <span class="o">:=</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_rec_on</span> <span class="n">n</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">ih</span> <span class="n">A</span> <span class="n">H</span><span class="o">,</span>
<span class="k">if</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span>
<span class="k">then</span> <span class="k">if</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">A</span><span class="bp">.</span><span class="n">a</span> <span class="bp">&gt;</span> <span class="mi">0</span>
  <span class="k">then</span> <span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="o">(</span><span class="n">T</span><span class="err">^</span><span class="o">(</span><span class="bp">-</span><span class="o">(</span><span class="n">A</span><span class="bp">.</span><span class="n">b</span><span class="bp">/</span><span class="n">A</span><span class="bp">.</span><span class="n">d</span><span class="o">)))</span> <span class="n">A</span>
  <span class="k">else</span> <span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="o">(</span><span class="n">T</span><span class="err">^</span><span class="o">(</span><span class="bp">-</span><span class="o">(</span><span class="bp">-</span><span class="n">A</span><span class="bp">.</span><span class="n">b</span><span class="bp">/</span> <span class="bp">-</span><span class="n">A</span><span class="bp">.</span><span class="n">d</span><span class="o">)))</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="n">A</span><span class="o">))</span>
<span class="k">else</span> <span class="n">ih</span> <span class="bp">_</span> <span class="o">(</span><span class="k">by</span> <span class="n">subst</span> <span class="n">H</span><span class="bp">;</span> <span class="k">from</span> <span class="n">reduce_aux</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H1</span><span class="o">)</span>
  <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="n">S</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span> <span class="o">(</span><span class="n">T</span><span class="err">^</span><span class="o">(</span><span class="bp">-</span><span class="o">(</span><span class="n">A</span><span class="bp">.</span><span class="n">a</span><span class="bp">/</span><span class="n">A</span><span class="bp">.</span><span class="n">c</span><span class="o">)))</span> <span class="n">A</span><span class="o">))</span> <span class="n">rfl</span>
<span class="o">:</span> <span class="bp">Π</span> <span class="n">n</span> <span class="o">(</span><span class="n">A</span><span class="o">:</span><span class="n">Mat</span> <span class="n">m</span><span class="o">),</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">int</span><span class="bp">.</span><span class="n">nat_abs</span> <span class="n">A</span><span class="bp">.</span><span class="n">c</span> <span class="bp">→</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">)</span> <span class="bp">_</span> <span class="n">A</span> <span class="n">rfl</span>

<span class="c1">--#reduce reduce (-1) ⟨1, 3, 1, 2, by norm_num⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979480):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">reps_equiv</span> <span class="o">(</span><span class="n">hm</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">quotient</span> <span class="o">(</span><span class="n">action_rel</span> <span class="o">(</span><span class="n">SL2Z_M_</span> <span class="n">m</span><span class="o">))</span> <span class="err">≃</span> <span class="n">reps</span> <span class="n">m</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Sep 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133979526):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> <span class="user-mention" data-user-id="112680">@Johan Commelin</span></p>

#### [ Johan Commelin (Sep 15 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995671):
<p>Ah, that looks like a smart way to approach this!</p>

#### [ Johan Commelin (Sep 15 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995907):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> The linecount in that file really exploded! You write Lean several orders of magnitude faster than I can read it.</p>

#### [ Kenny Lau (Sep 15 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133995980):
<p>lol</p>

#### [ Johan Commelin (Sep 15 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996045):
<p>Also you seem to like refactoring code, whereas for me there is some nasty psychological barrier...</p>

#### [ Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996052):
<p>Anyway, thanks a lot!</p>

#### [ Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996056):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Have you seen what happened?</p>

#### [ Mario Carneiro (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996060):
<p>what is this?</p>

#### [ Johan Commelin (Sep 15 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996062):
<p>We now have several hundreds of lines of code about a silly type called <code>SL2Z</code>, and it doesn't tie in to the <code>matrix</code> code at all.</p>

#### [ Johan Commelin (Sep 15 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996110):
<p>Well, that is not strictly true, Kenny proved that <code>SL2Z</code> is <code>equiv</code> to <code>SL 2 int</code>.</p>

#### [ Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996137):
<p>But now this <code>SL2Z</code> is acting on different sets, etc... and all this extra structure has not been tied to regular matrices.</p>

#### [ Mario Carneiro (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996143):
<p>This makes me vaguely uncomfortable</p>

#### [ Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996145):
<p>I think this was a great experiment, but I'm somewhat worried.</p>

#### [ Johan Commelin (Sep 15 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996150):
<p>Would you mind scrolling through the repo a bit?</p>

#### [ Mario Carneiro (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996190):
<p>unless the properties are not shared by other dimensions or rings?</p>

#### [ Kenny Lau (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996199):
<p>SL2Z is generated by two matrices</p>

#### [ Johan Commelin (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996203):
<p>Right.</p>

#### [ Mario Carneiro (Sep 15 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996212):
<p><code>induction_on</code> is frightening</p>

#### [ Johan Commelin (Sep 15 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996216):
<p>But the action of SL2Z on other 2x2-matrices is generic</p>

#### [ Johan Commelin (Sep 15 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996237):
<p>And the action of SL2Z on the upper-half plane is a restriction of the action of <code>(GL 2 real)_+</code> on the upper half plane</p>

#### [ Johan Commelin (Sep 15 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996267):
<p>So certain things are really specific, others are not.</p>

#### [ Kenny Lau (Sep 15 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996281):
<p>which is the restriction of GL2R acting on CP1</p>

#### [ Mario Carneiro (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996304):
<p>where should I be looking?</p>

#### [ Mario Carneiro (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996310):
<p>the frightening proof linked above appears to have been removed</p>

#### [ Kenny Lau (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996312):
<p>I made a function called reduce</p>

#### [ Johan Commelin (Sep 15 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996316):
<p>You could start with <code>modular_forms.lean</code> and then drill down.</p>

#### [ Mario Carneiro (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996364):
<p>on master?</p>

#### [ Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996366):
<p>Most of the hard stuff is happening in <code>SL2Z_generators</code> and some in <code>modular_group.lean</code></p>

#### [ Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996368):
<p>Yes</p>

#### [ Johan Commelin (Sep 15 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996371):
<p>We don't really use branches</p>

#### [ Johan Commelin (Sep 15 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996479):
<p>In the end, I would like <code>Hecke_operator</code> in <code>hecke_operators.lean</code> to have a somewhat readable definition.</p>

#### [ Johan Commelin (Sep 15 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/SL2Z%20action/near/133996541):
<p>It feels to me like all the ingredients are now there... but as you can see, my attempt at writing the definition is <span class="emoji emoji-1f4a9" title="poop">:poop:</span></p>


{% endraw %}
