---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99706Idealhasmem.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Ideal has_mem](https://leanprover-community.github.io/archive/113488general/99706Idealhasmem.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ AHan (Nov 30 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148853358):
<p>I don't get why <code>test₁</code> type checked but <code>test₂</code> will result in deterministic timeout...?</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">α</span><span class="o">)]</span>

<span class="kn">lemma</span> <span class="n">test₁</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">(</span><span class="n">ideal</span><span class="bp">.</span><span class="n">span</span> <span class="o">({</span><span class="n">a</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">test₂</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">(</span><span class="n">ideal</span><span class="bp">.</span><span class="n">span</span> <span class="o">({</span><span class="n">a</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">α</span><span class="o">)))</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johan Commelin (Nov 30 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148854580):
<p><span class="user-mention" data-user-id="133545">@AHan</span> What happens if you remove the <code>[comm_ring ...]</code> instance? It should derive it automatically, I hope.</p>

#### [ Patrick Massot (Nov 30 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148854942):
<p>And also the proof is only one <code>rw</code> long</p>

#### [ Patrick Massot (Nov 30 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855036):
<p>If order to find out the relevant lemma, you start by writing <code>ideal.mem_span</code> because you want something about ideals saying something belongs to a span, then you pause to inspect what autocompletions are suggested, and choose the relevant one.</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855180):
<p>@AHan if you pasted minimal _working_ examples (i.e. with all the imports needed to run the example) then my life would be slightly easier -- I'd just be able to cut and paste.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">multivariate_polynomial</span>
<span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">ideals</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span>
<span class="c1">--variables [comm_ring (mv_polynomial ℕ α)]</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- this works</span>

<span class="kn">lemma</span> <span class="n">test₁</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="o">(</span><span class="n">ideal</span><span class="bp">.</span><span class="n">span</span> <span class="o">({</span><span class="n">a</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">test₂</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">a</span> <span class="err">∈</span> <span class="o">(</span><span class="n">ideal</span><span class="bp">.</span><span class="n">span</span> <span class="o">({</span><span class="n">a</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">α</span><span class="o">)))</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- no timeout any more</span>
</pre></div>

#### [ Patrick Massot (Nov 30 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855293):
<p>you second import is probably unnecessary</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855406):
<p>So your problem is what Johan suggested. If alpha is a field then Lean <em>already knows</em> that the multivariate polynomial ring over alpha is a commutative ring. This fact is already in the "type class inference system" because Lean spotted that it was true, and put it there automatically. My <code>example</code> above shows that the fact that the polynomial ring is a commutative ring can be proved using the <code>apply_instance</code> tactic -- which means that Lean already internally has a term of type <code>comm_ring (mv_polynomial ℕ α)</code>. The line you wrote and I commented out makes a second term of that type. Now Lean's type class system works under the assumption that for typeclasses like <code>comm_ring</code>, there should be at most one term of each type, and if Lean has more than one term of a given typeclass then Lean can get confused. I don't know why this leads to a timeout in your case (some of the CS people here would be able to explain it I'm sure) but I can see the rule you broke, and breaking rules like this can lead to all sorts of random problems.</p>

#### [ Patrick Massot (Nov 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855565):
<p>What is slightly more mysterious is why <code>lemma test₂ (a : mv_polynomial ℕ α) : a ∈ (ideal.span ({a} : set (mv_polynomial ℕ α))) := 
by rw ideal.mem_span_singleton</code> works without any extra step</p>

#### [ Patrick Massot (Nov 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855576):
<p>The trick is <a href="https://github.com/leanprover/mathlib/blob/master/algebra/ring.lean#L73" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/algebra/ring.lean#L73">https://github.com/leanprover/mathlib/blob/master/algebra/ring.lean#L73</a></p>

#### [ Patrick Massot (Nov 30 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855635):
<p>Although <code>dvd_refl</code> is not definitionaly true, it is marked as <code>refl</code>, and it seems <code>rw</code> tries (all?) such lemmas to close goals</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855654):
<p>it calls <code>refl</code></p>

#### [ Patrick Massot (Nov 30 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855734):
<p>How do you ask lean whether a particular lemma has been marked as <code>refl</code> and, if yes, where? I found the above line using grep</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855777):
<p>if you print the lemma you can see any attributes</p>

#### [ Patrick Massot (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855782):
<p>good</p>

#### [ Patrick Massot (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855789):
<p>what about finding the line attaching the attribute?</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855798):
<p>no luck</p>

#### [ Patrick Massot (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855824):
<p>In <code>@[refl, simp, priority 100] theorem dvd_refl</code> what has priority 100?</p>

#### [ Patrick Massot (Nov 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855903):
<p>priority in which process? simp?</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855990):
<p>Oh +1 to that question! I thought priority was just for type classes.</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855993):
<p>I don't know why that's there. It's only for typeclasses</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148855997):
<p>oh cool, I'm going back to mathlib and I'm going to give all the lemmas I proved priority 20000</p>

#### [ Johan Commelin (Nov 30 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856047):
<p>You should give them priority 37. Just to make a point.</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856049):
<p>maybe <span class="user-mention" data-user-id="110111">@Keeley Hoek</span> can go code diving to ascertain if this is the case</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856057):
<p>is it explicitly set by some line?</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856059):
<p>or did lean do it</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856061):
<p>When Lean gets sponsored by Coca Cola and the user gets a little Coca Cola ad each time your lemma is used, every dev will want to make sure their lemmas are being used as much as possible.</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856126):
<p>"This factorization was brought to you by the refreshing taste of... Coca Cola"</p>

#### [ Johan Commelin (Nov 30 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856150):
<p>If (not when) that day arrives, I'll go back to pen and paper proofs.</p>

#### [ Edward Ayers (Nov 30 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856208):
<p>Just install adblock on vscode</p>

#### [ Johan Commelin (Nov 30 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856284):
<p>And waste precious CPU cycles. The real world is so debased. (And pure math is an ivory tower, yes I know.)</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856305):
<p>So if you write <code>#print dvd_refl</code> directly after the definition in core Lean in <code>init/algebra/ring.lean</code>, already the priority is 100. If you remove the <code>simp</code> tag then the priority also disappears.</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856318):
<p>Aah!</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856373):
<p><a href="https://github.com/leanprover/lean/blob/master/library/init/algebra/ring.lean#L11" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/algebra/ring.lean#L11">https://github.com/leanprover/lean/blob/master/library/init/algebra/ring.lean#L11</a></p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856392):
<div class="codehilite"><pre><span></span>/- Make sure instances defined in this file have lower priority than the ones
   defined for concrete structures -/
</pre></div>


<p>And simp lemmas too :-)</p>

#### [ Kevin Buzzard (Nov 30 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856457):
<p>Yeah that's it -- my <code>dvd_refl</code> now has priority 37.</p>

#### [ Patrick Massot (Nov 30 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856531):
<p>MWE</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">default_priority</span> <span class="mi">100</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span>
<span class="kn">lemma</span> <span class="n">pat</span> <span class="o">:</span> <span class="mi">1</span><span class="bp">+</span><span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">dec_trivial</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">pat</span>
</pre></div>

#### [ Patrick Massot (Nov 30 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856583):
<p>gives <code>@[simp, priority 100] theorem pat : 1 + 1 = 2 := of_as_true trivia</code></p>

#### [ Patrick Massot (Nov 30 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856586):
<p>Removing the <code>set_option</code> line remove any priority number</p>

#### [ Patrick Massot (Nov 30 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856595):
<p>Is this a bug in <code>set_option</code> <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> ?</p>

#### [ Mario Carneiro (Nov 30 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856596):
<p>so, does it affect simp?</p>

#### [ Patrick Massot (Nov 30 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856655):
<p>Yes!</p>

#### [ Patrick Massot (Nov 30 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856671):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">200</span><span class="o">]</span>
<span class="kn">lemma</span> <span class="n">pat</span> <span class="o">:</span> <span class="mi">1</span><span class="bp">+</span><span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">dec_trivial</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">37</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">kevin</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="n">of_as_true</span> <span class="n">trivial</span>

<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">simplify</span><span class="bp">.</span><span class="n">rewrite</span> <span class="n">true</span>
<span class="kn">example</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Patrick Massot (Nov 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856714):
<p>Changing priorities does change which lemma is used, so it's not a bug in <code>set_option</code>, it's an undocumented feature</p>

#### [ Reid Barton (Nov 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856727):
<p>whoa!</p>

#### [ Patrick Massot (Nov 30 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856729):
<p>Or maybe we didn't read the documentation seriously enough</p>

#### [ Patrick Massot (Nov 30 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856737):
<p>For instance, maybe we didn't read the source code...</p>

#### [ Sebastian Ullrich (Nov 30 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856747):
<p>Yeah, it's clearly spelled out in line 11386</p>

#### [ Patrick Massot (Nov 30 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148856927):
<p>The documentation file <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simp_lemmas.cpp" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simp_lemmas.cpp">https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simp_lemmas.cpp</a> mentions priority  all over the place</p>

#### [ AHan (Nov 30 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148857208):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  Thanks for the suggestion and explanation!!</p>

#### [ Patrick Massot (Nov 30 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148857259):
<p>I still wonder whether <code>set_option default_priority</code> setting both instance and simp priority is intended behavior. It would also be nice to know whether <code>simp</code> would be faster without this mechanism, which seems to be used nowhere</p>

#### [ Sebastian Ullrich (Nov 30 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148857918):
<blockquote>
<p>I still wonder whether <code>set_option default_priority</code> setting both instance and simp priority is intended behavior.</p>
</blockquote>
<p>The real problem is the <code>priority</code> attribute itself. It doesn't make any sense that it's <code>[simp, priority 1000]</code> instead of something like <code>[simp:1000]</code> in the first place (and when <code>priority</code> is gone, <code>default_priority</code> without any extra qualifier doesn't make much sense either). I doubt this will still be the case in Lean 4.</p>
<blockquote>
<p>It would also be nice to know whether <code>simp</code> would be faster without this mechanism, which seems to be used nowhere</p>
</blockquote>
<p>I don't think so, it's still using the head-symbol index.</p>

#### [ Patrick Massot (Nov 30 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148857993):
<p>The printing thing seems easy enough to correct at <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simp_lemmas.cpp#L175-L180" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simp_lemmas.cpp#L175-L180">https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simp_lemmas.cpp#L175-L180</a></p>

#### [ Patrick Massot (Nov 30 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ideal%20has_mem/near/148858035):
<p>but it's very probably not worth the trouble</p>


{% endraw %}
