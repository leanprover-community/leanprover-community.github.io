---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/80075choosingfromdifferenceoffinsets.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [choosing from difference of finsets](https://leanprover-community.github.io/archive/113489newmembers/80075choosingfromdifferenceoffinsets.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Sep 09 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133619465):
<p>Here's my "Tactic State":</p>
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">,</span>
<span class="n">x</span> <span class="n">y</span> <span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">,</span>
<span class="n">hx</span> <span class="o">:</span> <span class="n">x</span> <span class="err">⊆</span> <span class="n">S</span><span class="o">,</span>
<span class="n">hy</span> <span class="o">:</span> <span class="n">y</span> <span class="err">⊆</span> <span class="n">S</span><span class="o">,</span>
<span class="n">hcard</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="n">y</span>
<span class="err">⊢</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">y</span> <span class="err">\</span> <span class="n">x</span>
</pre></div>


<p>I've been digging through <code>finset</code> and am not sure what I need to do to kill this goal. Any pointers? It looks like I need to invoke <code>classical.choice</code>, but does that mean I need to turn things into <code>fintype</code>s?</p>

#### [ Mario Carneiro (Sep 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133619814):
<p>You could prove that <code>finset.card (y \ x) != 0</code></p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133620757):
<p>Oops, I should have showed that <code>S</code> is nonempty before this point. But I'm still not seeing how to easily work with <code>finset.card</code>. Perhaps I should be working with <code>multiset.card</code> instead?</p>

#### [ Kevin Buzzard (Sep 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622733):
<p>The interface should all be there, although it might require reading <code>finset.lean</code>...</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622824):
<p>So my algorithm for doing questions like this is to type <code>import finset</code>, see what auto-complete suggests, find that <code>finset.lean</code> is in <code>data/</code>, then open finset.lean and search the file for <code>card</code> to see what's there.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622922):
<p><code>theorem eq_of_subset_of_card_le {s t : finset α} (h : s ⊆ t) (h₂ : card t ≤ card s) : s = t := ...</code>. Can I work classically?</p>

#### [ Patrick Massot (Sep 09 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622924):
<p>Yes!</p>

#### [ Patrick Massot (Sep 09 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622930):
<p>(didn't read the code part)</p>

#### [ Mario Carneiro (Sep 09 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133622931):
<p>You should have decidable whatever in this context</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623442):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>
<span class="kn">import</span> <span class="n">logic</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">0</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">hcard</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="n">y</span><span class="o">)</span>
<span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">y</span> <span class="err">\</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">hnsub</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">y</span> <span class="err">⊆</span> <span class="n">x</span><span class="o">),</span>
    <span class="n">intro</span> <span class="n">hsub</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">Heq</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">eq_of_subset_of_card_le</span> <span class="n">hsub</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="n">hcard</span><span class="o">),</span>
    <span class="n">rw</span> <span class="n">Heq</span> <span class="n">at</span> <span class="n">hcard</span><span class="o">,</span>
    <span class="n">revert</span> <span class="n">hcard</span><span class="o">,</span><span class="n">simp</span><span class="o">,</span>
  <span class="n">by_contra</span> <span class="n">hnotex</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h2</span> <span class="o">:=</span> <span class="n">forall_not_of_not_exists</span> <span class="n">hnotex</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">hnsub</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">b</span> <span class="n">Hb</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">h2</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">revert</span> <span class="n">Hb</span><span class="o">,</span>
  <span class="n">revert</span> <span class="n">h3</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Amateurish approach. I don't know if I need decidability.</p>

#### [ Mario Carneiro (Sep 09 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623456):
<p>does removing the local instance break the proof?</p>

#### [ Chris Hughes (Sep 09 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623508):
<p>I think the <code>by_contra</code> will break.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623509):
<p><code>by_contra hnotex</code> breaks</p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623511):
<p>I tried to do the following as a warmup for the above:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">chosen</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">S</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">))</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">ne</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
<span class="k">have</span> <span class="n">SS</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">(</span><span class="err">↑</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finset_coe</span><span class="bp">.</span><span class="n">fintype</span> <span class="n">S</span><span class="o">,</span>
<span class="k">have</span> <span class="n">hSS</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="o">(</span><span class="err">↑</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">nonempty_iff_univ_ne_empty</span><span class="bp">.</span><span class="n">mpr</span> <span class="bp">_</span><span class="o">,</span>
<span class="n">exact</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="n">hSS</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>


<p>I'm having trouble turning <code>h : S ≠ ∅</code> into <code>⊢ @set.univ ↥↑S ≠ ∅</code>. Probably I'm just scared by the <code>↥↑</code> since I'm not too comfortable with coercions. </p>
<p>I've also been following something like your algorithm <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> but I wanted to check in and make sure I wasn't missing some obscure lemma elsewhere. Thanks for your solution, I'll study it carefully now!</p>

#### [ Kenny Lau (Sep 09 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623556):
<p>if you make the statement bounded then by_contra will not break</p>

#### [ Mario Carneiro (Sep 09 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623557):
<p><code>chosen</code> is definitely noncomputable, but you can use <code>finset.exists_mem_of_ne_empty</code> to prove that easily</p>

#### [ Chris Hughes (Sep 09 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623565):
<p><code>classical.sone (exists_mem_of_ne_empty h)</code></p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623568):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> you should try and understand Kenny's golfed solution :-)</p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623615):
<p>Thanks Mario and Chris!</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623627):
<p>I'm having trouble getting your warm-up to compile. What are the imports and variables?</p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623705):
<p>Sorry about that, see the edit.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623756):
<p>My Lean has never heard of <code>set.nonempty_iff_univ_ne_empty.mpr</code></p>

#### [ Mario Carneiro (Sep 09 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623769):
<div class="codehilite"><pre><span></span>example (α) [decidable_eq α] (x y : finset α) (hcard : finset.card x &lt; finset.card y) : ∃ (e : α), e ∈ y \ x :=
classical.by_contradiction $ λ h,
not_le_of_lt hcard (finset.card_le_of_subset $ by simpa using h)
</pre></div>

#### [ Kevin Buzzard (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623814):
<p>Oh sorry, I meant Mario's golfed solution.</p>

#### [ Mario Carneiro (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623821):
<p>there is a way to prove it without classical stuff, but I will let kenny do that</p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623824):
<p>it's in data.set.basic; I guess it was added quite recently <a href="https://github.com/leanprover/mathlib/pull/295" target="_blank" title="https://github.com/leanprover/mathlib/pull/295">https://github.com/leanprover/mathlib/pull/295</a></p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133623831):
<p>Oh yes, I have an old project open. Thanks!</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624004):
<p>I guess <code>↥↑S</code> means the subtype corresponding to the set corresponding to <code>S</code>.</p>

#### [ Kenny Lau (Sep 09 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624012):
<blockquote>
<p>there is a way to prove it without classical stuff, but I will let kenny do that</p>
</blockquote>
<p>roger that</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">hcard</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">y</span> <span class="err">\</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">suffices</span> <span class="bp">∃</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">y</span><span class="o">,</span> <span class="n">e</span> <span class="err">∉</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simpa</span><span class="o">,</span>
<span class="n">by_contradiction</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">not_le_of_lt</span> <span class="n">hcard</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">card_le_of_subset</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">H</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Sep 09 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624124):
<p>lol, that was easy</p>

#### [ Kevin Buzzard (Sep 09 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624311):
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">chosen</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">S</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">))</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">ne</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">finset</span><span class="bp">.</span><span class="n">card_pos</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">change</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card</span> <span class="n">S</span><span class="bp">.</span><span class="n">val</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span> <span class="c1">-- switching to multisets</span>
  <span class="n">rw</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">card_pos_iff_exists_mem</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span> <span class="c1">-- there&#39;s now a one-liner that I forgot</span>
  <span class="k">have</span> <span class="n">hinhabited</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">inhabited_of_exists</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">hinhabited</span> <span class="k">with</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">a</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 09 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624321):
<blockquote>
<p>lol, that was easy</p>
</blockquote>
<p>oh come on, he just copied your answer ;-)</p>

#### [ Patrick Massot (Sep 09 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624505):
<p>the last three lines can be abbreviated to <code>exact (classical.inhabited_of_exists h).default</code></p>

#### [ Kenny Lau (Sep 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/choosing%20from%20difference%20of%20finsets/near/133624762):
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">chosen</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">S</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">))</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="err">$</span> <span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span>
<span class="n">mt</span> <span class="n">finset</span><span class="bp">.</span><span class="n">eq_empty_of_forall_not_mem</span> <span class="n">h</span>
</pre></div>


{% endraw %}
