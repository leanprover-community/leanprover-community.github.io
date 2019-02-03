---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/94506finset.html
---

## Stream: [general](index.html)
### Topic: [finset](94506finset.html)

---


{% raw %}
#### [ Floris van Doorn (Nov 20 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148072219):
<p>Is the following result somewhere in mathlib? If not, are there results which make it less painful than proving it from scratch using lists?</p>
<div class="codehilite"><pre><span></span>def exists_of_subset_image {α : Type u} {β : Type v} {f : α → β} {s : finset β} {t : set α}
  (h : ↑s ⊆ f &#39;&#39; t) : ∃s&#39; : finset α, ↑s&#39; ⊆ t ∧ s&#39;.image f = s
</pre></div>

#### [ Kenny Lau (Nov 20 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148074485):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">theorem</span> <span class="n">exists_of_subset_image</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="err">↑</span><span class="n">s</span> <span class="err">⊆</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">t</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∃</span><span class="n">s&#39;</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">,</span> <span class="err">↑</span><span class="n">s&#39;</span> <span class="err">⊆</span> <span class="n">t</span> <span class="bp">∧</span> <span class="n">s&#39;</span><span class="bp">.</span><span class="n">image</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">s</span> <span class="kn">using</span> <span class="n">finset</span><span class="bp">.</span><span class="n">induction</span> <span class="k">with</span> <span class="n">a</span> <span class="n">s</span> <span class="n">has</span> <span class="n">ih</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="err">∅</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">empty_subset</span> <span class="bp">_</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">image_empty</span> <span class="bp">_⟩</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">coe_insert</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">insert_subset</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">ih</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">s&#39;</span><span class="o">,</span> <span class="n">hst</span><span class="o">,</span> <span class="n">hsi</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">h</span><span class="bp">.</span><span class="mi">1</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hxt</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">refine</span> <span class="bp">⟨</span><span class="n">insert</span> <span class="n">x</span> <span class="n">s&#39;</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">coe_insert</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">insert_subset</span><span class="o">],</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">hxt</span><span class="o">,</span> <span class="n">hst</span><span class="bp">⟩</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">image_insert</span><span class="o">,</span> <span class="n">hsi</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 20 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148074490):
<p>a simple induction</p>

#### [ Floris van Doorn (Nov 20 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148074765):
<p>Thanks! <code>finset.induction</code> makes this indeed quite easy to prove.</p>

#### [ Kenny Lau (Nov 20 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148074832):
<p>can we call this finite_choice... &gt;?&lt;</p>

#### [ Floris van Doorn (Nov 21 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148078119):
<p>Different question: should <code>finset.singleton</code> be protected? There are two <code>singleton</code>s if you open <code>finset</code>.</p>
<div class="codehilite"><pre><span></span>import data.finset
open finset
#print singleton
</pre></div>

#### [ Kenny Lau (Nov 21 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148081655):
<p>so... don't open <code>finset</code>? /s</p>

#### [ Mario Carneiro (Nov 21 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148082475):
<p>or use <code>finset.singleton</code> anyway</p>

#### [ Mario Carneiro (Nov 21 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148082487):
<p>maybe it should be renamed to <code>single</code> or something, it's already far longer than it should be, namely <code>{x}</code></p>

#### [ Mario Carneiro (Nov 21 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148082509):
<p>in finset it has a prefix notation <code>ι</code>, you could use that</p>

#### [ Scott Morrison (Nov 22 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198016):
<p>Hi, possibly a range of <code>finset</code> questions coming up... :-)</p>

#### [ Scott Morrison (Nov 22 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198018):
<p>Why is <code>theorem insert.comm (a b : α) (s : finset α) : insert a (insert b s) = insert b (insert a s) := ...</code> marked as <code>@[simp]</code>?</p>

#### [ Scott Morrison (Nov 22 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198064):
<p>This seems like a terrible idea, and is responsible for bad simplifications like:<br>
<code>range (n + 1 + 1)</code> simplifying to <code>insert n (insert (n + 1) (range n))</code>.</p>

#### [ Reid Barton (Nov 22 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198073):
<p>how does that not loop?</p>

#### [ Scott Morrison (Nov 22 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198074):
<p>That too. :-)</p>

#### [ Scott Morrison (Nov 22 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198245):
<p>Does mathlib have something to the effect of <code>finset.iota n m</code>, giving the finset of natural numbers <code>n, n+1, ..., m-1</code>?</p>

#### [ Scott Morrison (Nov 23 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198417):
<p>Oops, <code>iota</code> is the wrong name. I guess <code>finset.interval n m</code>?</p>

#### [ Scott Morrison (Nov 23 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198511):
<p>Hmm.. <code>data.list.basic</code> has a peculiarly named <code>range' s n</code>, giving the list <code>[s, s+1, ..., s+n-1]</code>.</p>

#### [ Scott Morrison (Nov 23 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198612):
<p>Okay, removing <code>@[simp]</code> on <code>finset.insert.comm</code> doesn't break anything, so if there are no complaints I'll PR it later.</p>

#### [ Kevin Buzzard (Nov 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198721):
<p>IIRC Chris and Mario had a long discussion about the best way to do the bounds, when Chris was proving things about finite sums a while back</p>

#### [ Scott Morrison (Nov 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198726):
<p>So what happened to Chris's work on finite sums?</p>

#### [ Scott Morrison (Nov 23 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148198734):
<p>Faced with talking to students again, I really want to make <code>finset.sum</code> more fun. :-)</p>

#### [ Scott Morrison (Nov 23 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200245):
<p>I'm wondering how people would feel about removing the <code>@[simp]</code> from </p>
<div class="codehilite"><pre><span></span>theorem range_succ : range (succ n) = insert n (range n) := ...
</pre></div>


<p>I feel like this is often unhelpful. (In fact, in <code>quadratic_reciprocity.lean</code> Chris has to write <code>- range_succ</code> many times to avoid it firing. Similarly in <code>order_of_element.lean</code>.)</p>
<p>This would require either explicitly adding <code>range_succ</code> to the simp set in a few places, but not too many. (Three places across mathlib, and it saves many <code>simp [-range_succ]</code>s in <code>quadratic_reciprocity.lean</code>.)</p>

#### [ Scott Morrison (Nov 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200257):
<p>But in particular as soon as you have a sum of <code>range (n+1)</code>, this simp lemma may unhelpfully fire, which is confusing.</p>

#### [ Kenny Lau (Nov 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200291):
<p>Is Scott Morrison talking about <code>simp</code>? :P</p>

#### [ Scott Morrison (Nov 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200293):
<p>I love <code>simp</code>. I want to use it as much as possible.</p>

#### [ Scott Morrison (Nov 23 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200294):
<p>Hence I want to remove bad <code>@[simp]</code> lemmas that get the maths wrong.</p>

#### [ Kenny Lau (Nov 23 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200300):
<p>I see</p>

#### [ Chris Hughes (Nov 23 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148200457):
<p>I don't recall that conversation. I think it was Mario and Patrick. There's definitely a need to make finest.sum nicer, particularly with natural numbers. Also a need for a nice non commutative sum interface.</p>

#### [ Scott Morrison (Nov 23 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201138):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> , if we were going to introduce an <code>interval n m : finset nat</code>, and try to make doing sums over natural numbers work nicely with it, would you prefer <code>interval n m</code> includes <code>m</code>, or not?</p>

#### [ Scott Morrison (Nov 23 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201725):
<p>Does anyone know if</p>
<div class="codehilite"><pre><span></span>lemma finset_sum_split [add_comm_monoid β] (s : finset α) (f : α → β) (P : α → Prop) [decidable_pred P] :
s.sum f = (s.filter P).sum f + (s.filter (λ a, ¬ P a)).sum f := sorry
</pre></div>


<p>exists in mathlib?</p>

#### [ Kenny Lau (Nov 23 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201736):
<p>yes</p>

#### [ Kenny Lau (Nov 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201749):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>

<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">filter_pos_add_filter_neg</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">finsupp.filter_pos_add_filter_neg :</span>
<span class="cm">  ∀ {α : Type u_1} {β : Type u_2} [_inst_1 : decidable_eq α] [_inst_2 : decidable_eq β] [_inst_3 : add_monoid β]</span>
<span class="cm">  (f : α →₀ β) (p : α → Prop) [_inst_4 : decidable_pred p] [_inst_5 : decidable_pred (λ (a : α), ¬p a)],</span>
<span class="cm">    finsupp.filter p f + finsupp.filter (λ (a : α), ¬p a) f = f</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Nov 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201752):
<p>oh wait</p>

#### [ Kenny Lau (Nov 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201753):
<p>they are not exactly the same</p>

#### [ Scott Morrison (Nov 23 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201796):
<p>I see. They're clearly related, but it's not obvious you could even prove mine from this, because of the <code>decidable_eq</code> hypotheses.</p>

#### [ Scott Morrison (Nov 23 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201859):
<p>While on the subject, the <code>[_inst_5 : decidable_pred (λ (a : α), ¬p a)]</code> argument of <code>finsupp.filter_pos_add_filter_neg</code> is unnecessary.</p>

#### [ Kenny Lau (Nov 23 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148201968):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>

<span class="kn">lemma</span> <span class="n">finset_sum_split</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">P</span><span class="o">]</span> <span class="o">:</span>
<span class="n">s</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="bp">=</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="n">filter</span> <span class="n">P</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="bp">+</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">¬</span> <span class="n">P</span> <span class="n">a</span><span class="o">))</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_eq</span> <span class="n">α</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_union</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">filter_inter_filter_neg_eq</span> <span class="n">s</span><span class="o">),</span> <span class="n">finset</span><span class="bp">.</span><span class="n">filter_union_filter_neg_eq</span><span class="o">]</span>
</pre></div>

#### [ Scott Morrison (Nov 23 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202012):
<p>awesome, thank you!</p>

#### [ Reid Barton (Nov 23 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202015):
<p>in principle, it could be relevant at the use site... because decidability arguments are relevant</p>

#### [ Scott Morrison (Nov 23 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202017):
<p>oh, I see, you might want to give separate arguments that P and not P are decidable??</p>

#### [ Reid Barton (Nov 23 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202022):
<p>in principle...</p>

#### [ Reid Barton (Nov 23 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202070):
<p>though it's not very likely especially when the arguments are provided by type class inference and not looking at the expected type</p>

#### [ Reid Barton (Nov 23 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148202176):
<p>actually it might not be that unlikely, if both instances come from <code>prop_decidable</code></p>

#### [ Sebastien Gouezel (Nov 23 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148212877):
<blockquote>
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> , if we were going to introduce an <code>interval n m : finset nat</code>, and try to make doing sums over natural numbers work nicely with it, would you prefer <code>interval n m</code> includes <code>m</code>, or not?</p>
</blockquote>
<p>The notation for real intervals is Icc a b for intervals which are closed on both ends, and Ico for closed-open ones, and so on. All this is in <code>/data/set/intervals</code>. Ideally, you would use the same syntax prefixed with <code>finset.</code>, or something like that. And by the way, the only good convention to do sums is closed on the left and open on the right, i.e., $S_n f = \sum_{i=0}^{n-1}  f(i)$.</p>

#### [ Sebastien Gouezel (Nov 23 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148213145):
<p>Fancy Isabelle notation for these (I don't think this has been ported to Lean, or if there could be a parsing problem): <code>{a..b}</code> for the closed interval with endpoints <code>a</code> and <code>b</code>. And <code>{a&lt;..b}</code> for the open/closed version. And <code>{..&lt;b}</code> for the semiinfinite open one. And so on.</p>

#### [ Scott Morrison (Nov 23 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148213855):
<p>I wonder if we could do the actual maths notations for these... <code>[a,b)</code>, etc.</p>

#### [ Patrick Massot (Nov 23 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214028):
<p>Or the actual maths notations for these... <code>[a, b[,</code> etc.</p>

#### [ Mario Carneiro (Nov 23 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214030):
<p>nonono</p>

#### [ Mario Carneiro (Nov 23 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214031):
<p>that will kill your editor</p>

#### [ Mario Carneiro (Nov 23 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214075):
<p>trust me it's not worth it</p>

#### [ Patrick Massot (Nov 23 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214076):
<p>see also <a href="https://github.com/PatrickMassot/bigop/blob/master/src/tests.lean" target="_blank" title="https://github.com/PatrickMassot/bigop/blob/master/src/tests.lean">https://github.com/PatrickMassot/bigop/blob/master/src/tests.lean</a></p>

#### [ Patrick Massot (Nov 23 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214083):
<p>Although Cyril convinced me that Sébastien is right and I should exclude the upper bound from the sum</p>

#### [ Mario Carneiro (Nov 23 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214091):
<p>I'm okay with <code>{a..&lt;b}</code> and friends. In metamath we used <code>(a ..^ b)</code> which is slightly less mnemonic</p>

#### [ Mario Carneiro (Nov 23 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214133):
<p>there could be a parsing problem with <code>{a}</code>, but it might work as long as <code>...</code> doesn't mean anything else... oh</p>

#### [ Johan Commelin (Nov 23 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214140):
<p>There is also unicode <code>…</code></p>

#### [ Scott Morrison (Nov 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214207):
<p>In any case, it sounds like everyone is on board with the "default" being to not include the upper point.</p>

#### [ Kevin Buzzard (Nov 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214252):
<p>One million python users can't be wrong</p>

#### [ Patrick Massot (Nov 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214254):
<p>What convinced be is that is avoids some nat substractions. <em>That</em> is a killing argument</p>

#### [ Scott Morrison (Nov 23 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214257):
<p>I will try to fill in <code>interval n m</code> as a list/multiset/finset, and provide a good API for splitting these, into disjoint intervals or endpoint + other interval, for reindexing, etc.</p>

#### [ Johan Commelin (Nov 23 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148214346):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> How does this tie in to "I'll stop working on maths in Lean for a while, to work a bit on infrastructure..." (just curious)</p>

#### [ Scott Morrison (Nov 24 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148253177):
<p>:-)</p>

#### [ Scott Morrison (Nov 28 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148689585):
<p>Is there any reason why we don't have <code>sUnion</code> on <code>finset</code>? This seems like an obvious omission.</p>

#### [ Kenny Lau (Nov 28 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148689646):
<p><code>finset.bind _ id</code>?</p>

#### [ Scott Morrison (Nov 28 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148689656):
<p>Great, thank you!</p>

#### [ Scott Morrison (Nov 28 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148690310):
<p>Is there no <code>preimage</code> for <code>finset</code>?</p>

#### [ Kenny Lau (Nov 28 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset/near/148690350):
<p>you could use <code>finset.filter</code></p>


{% endraw %}
