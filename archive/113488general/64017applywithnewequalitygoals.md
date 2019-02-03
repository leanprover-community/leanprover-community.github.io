---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64017applywithnewequalitygoals.html
---

## Stream: [general](index.html)
### Topic: [apply with new equality goals](64017applywithnewequalitygoals.html)

---


{% raw %}
#### [ Reid Barton (Apr 23 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558382):
<p>Is there a tactic which works like <code>apply f</code> except that, if unifying the goal with the result type of <code>f</code> fails, it introduces new goals stating that the terms which don't unify are equal?<br>
Example: I want to prove a statement like <code>f ⁻¹' (u ∩ v) = ∅</code>. Suppose I know I want to use <code>preimage_empty : f ⁻¹' ∅ = ∅</code>. I would like to obtain <code>u ∩ v = ∅</code> as a new goal without spelling it out explicitly (in a <code>have</code> or similar).</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558494):
<p>An interesting idea. You can effectively get the result by <code>refine cast _ f</code> and then <code>congr</code></p>

#### [ Patrick Massot (Apr 23 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558636):
<p>I'm interested in this question but I don't understand the answer at all. <span class="user-mention" data-user-id="110032">@Reid Barton</span> do your have a MWE so that Mario (or you) could be more explicit about to do this?</p>

#### [ Reid Barton (Apr 23 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558645):
<p>Let me try to cook one up and try out Mario's suggestion</p>

#### [ Reid Barton (Apr 23 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558848):
<p>OK, here's an example:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>
<span class="kn">open</span> <span class="n">set</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">singleton_inter_singleton_eq_empty</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
  <span class="o">({</span><span class="n">x</span><span class="o">}</span> <span class="err">∩</span> <span class="o">{</span><span class="n">y</span><span class="o">}</span> <span class="bp">=</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">))</span> <span class="bp">↔</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">singleton_inter_eq_empty</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="o">{</span><span class="n">x</span><span class="o">}</span> <span class="err">∩</span> <span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="o">{</span><span class="n">y</span><span class="o">}</span> <span class="bp">=</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">preimage_inter</span><span class="o">,</span>
<span class="c1">-- ⊢ f ⁻¹&#39; ({x} ∩ {y}) = ∅</span>
  <span class="k">have</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">}</span> <span class="err">∩</span> <span class="o">{</span><span class="n">y</span><span class="o">}</span> <span class="bp">=</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">this</span><span class="o">,</span> <span class="n">exact</span> <span class="n">preimage_empty</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 23 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558894):
<p>If <code>p</code> has type <code>f ⁻¹' ∅ = ∅</code> and the goal is <code>f ⁻¹' (u ∩ v) = ∅</code>, then <code>refine cast _ p</code> will give the goal <code>(f ⁻¹' (u ∩ v) = ∅) = (f ⁻¹' ∅ = ∅)</code> and <code>congr</code> will skip all the same stuff to get to <code>u ∩ v = ∅</code>. Of course this has the usual <code>congr</code> caveats about going too far, but it seems like the right idea for Reid's problem</p>

#### [ Reid Barton (Apr 23 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125558946):
<p><code>refine cast _ preimage_empty</code> guessed to replace the wrong part, though, leaving <code>⊢ ?m_3 ⁻¹' ∅ = ∅ = (f ⁻¹' ({x} ∩ {y}) = ∅)</code></p>

#### [ Mario Carneiro (Apr 23 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559023):
<p>no that's correct</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559026):
<p>what happens after <code>congr</code>?</p>

#### [ Reid Barton (Apr 23 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559043):
<p><code>congr</code> errors with "tactic failed, there are no goals to be solved" (even though there were 4 goals)</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559090):
<p>what is the first goal?</p>

#### [ Reid Barton (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559104):
<p>the goals are <code>⊢ Type ?</code>, <code>⊢ Type ?</code>, <code>⊢ ?m_1 → ?m_2</code>, and what I wrote above</p>

#### [ Reid Barton (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559106):
<p>I assume they are describing the type of <code>?m_3</code></p>

#### [ Mario Carneiro (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559107):
<p>yes</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559109):
<p>You don't want to run <code>congr</code> on those goals</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559159):
<p>you have to cycle through them or set up the refine right, I guess</p>

#### [ Reid Barton (Apr 23 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559169):
<p>I'm confused though because I thought it was the <code>{x} ∩ {y}</code> part I wanted to replace</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559218):
<p>The goal is to do it in two stages. The first stage replaces your goal with an equality between the "apply" theorem and the goal, and the second stage simplifies the equality by congruence until you just have the part(s) that aren't defeq</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559225):
<p><code>cast</code> has the type <code>A = B -&gt; A -&gt; B</code>, so <code>cast _ p</code> where <code>p : A</code> yields the goal <code>A = B</code></p>

#### [ Reid Barton (Apr 23 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559234):
<p>Oh I see</p>

#### [ Reid Barton (Apr 23 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559235):
<p>I need to tell it to solve the third goal with <code>f</code></p>

#### [ Mario Carneiro (Apr 23 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559236):
<p>You could also try specifying <code>f</code> for the sake of the example</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559276):
<p>i.e. <code>refine cast _ (@preimage_empty _ _ f)</code></p>

#### [ Reid Barton (Apr 23 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559289):
<p>I just did <code>exact β, exact α, exact f, congr,</code>, and that also works, and leaves me with <code>⊢ ∅ = {x} ∩ {y}</code> like I wanted</p>

#### [ Reid Barton (Apr 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559306):
<p>Well, I would have preferred <code>⊢ {x} ∩ {y} = ∅</code> <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Mario Carneiro (Apr 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559349):
<p>I'm not sure if congr will automatically unify when it can, but that would fix these metavars without your intervention</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559353):
<p>I think <code>eq.mp</code> and <code>eq.mpr</code> are the same as <code>cast</code> and allow you to get the orientation right</p>

#### [ Reid Barton (Apr 23 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559421):
<p>Yes, <code>refine cast _ preimage_empty, swap 4, congr</code> also worked</p>

#### [ Reid Barton (Apr 23 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559424):
<p>and <code>eq.mpr</code> eliminates the need for <code>symmetry</code></p>

#### [ Reid Barton (Apr 23 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559473):
<p>Final version is to replace the last two lines with</p>
<div class="codehilite"><pre><span></span>  <span class="n">refine</span> <span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span> <span class="bp">_</span> <span class="n">preimage_empty</span><span class="o">,</span> <span class="n">swap</span> <span class="mi">4</span><span class="o">,</span> <span class="n">congr</span><span class="o">,</span>
<span class="c1">-- ⊢ {x} ∩ {y} = ∅</span>
  <span class="n">simpa</span> <span class="kn">using</span> <span class="n">h</span>
</pre></div>

#### [ Reid Barton (Apr 23 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559482):
<p>This is helpful, I haven't used congr before</p>

#### [ Reid Barton (Apr 23 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559542):
<p>The <code>swap</code> business reminds me of those pairs of tactics which differ only in how the resulting goals get ordered; I guess <code>refine</code> has no such companion?</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559594):
<p>no, it just creates all metavars in the order it finds them</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559606):
<p>There is enough going on here that it would not be unreasonable to have a tactic for it. Keep in mind though that it's not like apply in that it can't guess how many args to apply</p>

#### [ Patrick Massot (Apr 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559612):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> we need you!</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559657):
<p>if you don't get the args right your equality will be some statement like (\forall x. ...) = (f 0 = 0) and congr will not do anything useful</p>

#### [ Reid Barton (Apr 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559662):
<p>Right, I realized as I was asking the question that I don't really know how <code>apply</code> figures out how many args to insert</p>

#### [ Mario Carneiro (Apr 23 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125559679):
<p>I think it just applies as many as it can, or maybe counts how many nested pi are in the theorem type vs the target type and applies the difference</p>

#### [ Simon Hudon (Apr 23 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125568801):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> What would you imagine a tactic doing?</p>

#### [ Patrick Massot (Apr 23 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125568812):
<p>Ideally, the first message of this thread</p>

#### [ Simon Hudon (Apr 23 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125572764):
<p>Something like this?</p>
<div class="codehilite"><pre><span></span>meta def bridge_gap (r : parse texpr) : parse (&quot;using&quot; *&gt; smallnat)? -&gt; tactic unit
| none := refine ``(cast _ %%r) &gt;&gt; congr
| (some n) := refine ``(cast _ %%r) &gt;&gt; congr_n n
</pre></div>


<p>This way you can do <code>bridge_gap rule using n</code> to limit the depth of <code>congr</code> or just <code>bridge_gap rule</code></p>

#### [ Simon Hudon (Apr 23 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125572815):
<p>I'm not sure of the name though. Maybe something like <code>fit</code> or <code>adapt_to</code> would be better</p>

#### [ Simon Hudon (Apr 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125572849):
<p>I don't get why you need <code>swap</code> though</p>

#### [ Patrick Massot (Apr 23 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125573226):
<p>Can you do the example with it?</p>

#### [ Simon Hudon (Apr 23 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125573428):
<p>I'm giving it a try. My computer is not helping today</p>

#### [ Simon Hudon (Apr 23 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125575245):
<p>Ok I think I see why <code>swap</code> was necessary. Here's a proof and a tactic that work:</p>

#### [ Simon Hudon (Apr 23 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125575289):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="o">{</span><span class="n">x</span><span class="o">}</span> <span class="err">∩</span> <span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="o">{</span><span class="n">y</span><span class="o">}</span> <span class="bp">=</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">}</span> <span class="err">∩</span> <span class="o">{</span><span class="n">y</span><span class="o">}</span> <span class="bp">=</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">bridge_gap</span> <span class="n">preimage_empty</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">preimage_inter</span><span class="o">,</span><span class="n">this</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">tactic</span>
<span class="kn">namespace</span> <span class="n">interactive</span>

<span class="kn">open</span> <span class="n">interactive</span> <span class="n">interactive</span><span class="bp">.</span><span class="n">types</span> <span class="n">lean</span><span class="bp">.</span><span class="n">parser</span>
<span class="n">local</span> <span class="kn">postfix</span> <span class="bp">`</span><span class="err">?</span><span class="bp">`</span><span class="o">:</span><span class="mi">9001</span> <span class="o">:=</span> <span class="n">optional</span>
<span class="n">local</span> <span class="kn">postfix</span> <span class="bp">*</span><span class="o">:</span><span class="mi">9001</span> <span class="o">:=</span> <span class="n">many</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">bridge_gap</span> <span class="o">(</span><span class="n">sym</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(</span><span class="n">tk</span> <span class="s2">&quot;←&quot;</span><span class="o">)</span><span class="err">?</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">texpr</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">parse</span> <span class="o">(</span><span class="n">tk</span> <span class="s2">&quot;using&quot;</span> <span class="bp">*&gt;</span> <span class="n">small_nat</span><span class="o">)</span><span class="err">?</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">v</span> <span class="err">←</span> <span class="n">mk_mvar</span><span class="o">,</span>
   <span class="k">if</span> <span class="n">sym</span><span class="bp">.</span><span class="n">is_none</span>
     <span class="k">then</span> <span class="n">refine</span> <span class="bp">``</span><span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mp</span> <span class="err">%%</span><span class="n">v</span> <span class="err">%%</span><span class="n">r</span><span class="o">)</span>
     <span class="k">else</span> <span class="n">refine</span> <span class="bp">``</span><span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span> <span class="err">%%</span><span class="n">v</span> <span class="err">%%</span><span class="n">r</span><span class="o">),</span>
   <span class="n">gs</span> <span class="err">←</span> <span class="n">get_goals</span><span class="o">,</span>
   <span class="n">set_goals</span> <span class="o">[</span><span class="n">v</span><span class="o">],</span>
   <span class="o">(</span><span class="n">option</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">n</span> <span class="n">congr</span> <span class="n">congr_n</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span><span class="o">),</span>
   <span class="n">gs&#39;</span> <span class="err">←</span> <span class="n">get_goals</span><span class="o">,</span>
   <span class="n">set_goals</span> <span class="err">$</span> <span class="n">gs&#39;</span> <span class="bp">++</span> <span class="n">gs</span>

<span class="kn">end</span> <span class="n">interactive</span>
<span class="kn">end</span> <span class="n">tactic</span>
</pre></div>

#### [ Simon Hudon (Apr 23 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125575597):
<p>I added an option to allow <code>bridge_gap ← preimage_empty</code> but the parser doesn't seem to like it</p>

#### [ Simon Hudon (Apr 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576655):
<p>Ok, it's now working. I put it here <a href="https://gist.github.com/cipher1024/0d3328135367269cc35f74f43ecbb302" target="_blank" title="https://gist.github.com/cipher1024/0d3328135367269cc35f74f43ecbb302">https://gist.github.com/cipher1024/0d3328135367269cc35f74f43ecbb302</a> if you want to use it.</p>

#### [ Patrick Massot (Apr 23 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576871):
<p>Let's get to 20! (I mean 20, not 20!)</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576890):
<p>noooo</p>

#### [ Mario Carneiro (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576902):
<p>my backlog is so long...</p>

#### [ Patrick Massot (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576905):
<p>(deleted)</p>

#### [ Kevin Buzzard (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125576908):
<p>He'll go hermit</p>

#### [ Patrick Massot (Apr 23 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125577105):
<p>(deleted)</p>

#### [ Simon Hudon (Apr 23 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125577350):
<blockquote>
<p>Let's get to 20! (I mean 20, not 20!)</p>
</blockquote>
<p>20 what?</p>

#### [ Patrick Massot (Apr 23 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125577366):
<p>20 opened PR to mathlib</p>

#### [ Simon Hudon (Apr 23 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125578498):
<p>Ah! I didn't open a PR. I don't know if it's generally useful</p>

#### [ Simon Hudon (Apr 23 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125578578):
<p>Or rather, I don't know if there's interest for this tactic to be in mathlib rather than in one particular project</p>

#### [ Sebastien Gouezel (Apr 23 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125586345):
<p>20 :)</p>

#### [ Patrick Massot (Apr 24 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125595892):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>  Is this really a problem to have too many tactics in mathlib?</p>

#### [ Simon Hudon (Apr 24 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596043):
<p>I think it's good to prioritize the tactics that will have the most positive impact for the users of <code>mathlib</code>. On one hand, that makes better use of Mario's time and on the other hand, it minimizes the effort required to understand <code>mathlib</code>'s features</p>

#### [ Patrick Massot (Apr 24 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596052):
<p>I have a new idea for you (which would simplify my current work). Assume <code>(*) : R → R → R</code> and <code>[is_associative (*))]</code>. I have an expression like <code>(a₁*(a₂*a₃)*a₄)*((a₅*a₆)*a₇)</code> (maybe I'm in conv mode so I only see this expression). I'd like to write <code>simon_new_magic_trick 4 5</code> and get an expression where parentheses are rearranged so that I see <code>(a₄*a₅)</code> in the middle.</p>

#### [ Patrick Massot (Apr 24 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596095):
<p>And I'm going to sleep (2:33 am here)</p>

#### [ Simon Hudon (Apr 24 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596180):
<p>We can talk about it some more tomorrow. Do you want it as a preparation for something in particular (e.g. <code>rw</code>) or do you foresee using it in combination with multiple other tactics?</p>

#### [ Simon Hudon (Apr 24 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596233):
<p>As for syntax, I could think of calling it <code>ac_zoom a₄*a₅</code> (in case we want to consider commutativity too) in <code>conv</code> mode.</p>

#### [ Andrew Ashworth (Apr 24 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596308):
<p>that does seem useful. I guess the algebraic normalization functionality got put by the wayside for lean 4</p>

#### [ Mario Carneiro (Apr 24 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596313):
<p>how about <code>ac_focus</code>? that sounds pretty neat</p>

#### [ Andrew Ashworth (Apr 24 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596321):
<p>more generally being able to rewrite declaratively with wildcards like <code>_</code> would be sweet</p>

#### [ Simon Hudon (Apr 24 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596330):
<blockquote>
<p>I guess the algebraic normalization functionality got put by the wayside for lean 4</p>
</blockquote>
<p>What are you referring to?</p>

#### [ Simon Hudon (Apr 24 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596372):
<blockquote>
<p>more generally being able to rewrite declaratively with wildcards like <code>_</code> would be sweet</p>
</blockquote>
<p>Can you elaborate a bit on what that would look like?</p>

#### [ Mario Carneiro (Apr 24 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596379):
<p>Alternatively, the syntax could be an expression like <code>ac_zoom _*a₄*a₅</code> and this is ac-unified with the goal</p>

#### [ Andrew Ashworth (Apr 24 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596441):
<p>you have <code>(a1 * (a2 * (a3 * (a4 * (a5 * a6)))))</code>, you want <code>a1 * a2 * (a3 * a4) * a5 * a6</code>, hmm, maybe something like <code>mytactic _ * _ * (a3 * a4) * _ * _</code></p>

#### [ Andrew Ashworth (Apr 24 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596444):
<p>perhaps you could allow less <code>_</code> than variables and that would make the constraint search easier</p>

#### [ Andrew Ashworth (Apr 24 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596455):
<p>I remember hearing awhile back that there was going to be a lot of algebra machinery going in</p>

#### [ Mario Carneiro (Apr 24 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596459):
<p>you could get by with only one <code>_</code> on left and right with assoc only, and just one <code>_</code> on left or right with ac</p>

#### [ Mario Carneiro (Apr 24 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596503):
<p>if there are too many holes you can just fill them eagerly</p>

#### [ Mario Carneiro (Apr 24 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596506):
<p>and fail if there aren't enough terms</p>

#### [ Mario Carneiro (Apr 24 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596511):
<p>commutativity only reasoning seems trickier</p>

#### [ Simon Hudon (Apr 24 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596583):
<p>You mean without associativity? Why is it trickier?</p>

#### [ Andrew Ashworth (Apr 24 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596671):
<p>:( too bad floating point math is non-associative</p>

#### [ Reid Barton (Apr 24 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596776):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Thanks, this <code>bridge_gap</code> worked in my real project too.<br>
Only I can't seem to get the ← feature to actually work (I tried <code>bridge_gap ←preimage_empty</code> with all combinations of space or no space around the arrow). But it works fine if I change ← to - for some reason.</p>

#### [ Reid Barton (Apr 24 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596793):
<p>With ←, I get a parse error</p>

#### [ Reid Barton (Apr 24 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596811):
<p>"error: expression expected", and then it continues in a confused state</p>

#### [ Simon Hudon (Apr 24 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596814):
<p>I had a hard time too with that notation. I don't understand why. It works fine with <code>rw</code>. Have you tried <code>&lt;-</code>? That worked better for me</p>

#### [ Reid Barton (Apr 24 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596825):
<p>Yes, that works... something about the arrow</p>

#### [ Simon Hudon (Apr 24 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125596872):
<p>I decided not to spend more time investigating that issue because <code>&lt;-</code> works. It's still annoying</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597061):
<p>You have to use <code>tk "&lt;-"</code> instead of <code>tk "←"</code></p>

#### [ Mario Carneiro (Apr 24 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597070):
<p>by some weird setup on lean's part, the token that lean knows as <code>&lt;-</code> is parsed from both <code>&lt;-</code> and <code>←</code></p>

#### [ Mario Carneiro (Apr 24 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597074):
<p>so if you write <code>tk "←"</code> it doesn't work at all, and <code>tk "&lt;-"</code> works with both <code>&lt;-</code> and <code>←</code></p>

#### [ Simon Hudon (Apr 24 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597075):
<p>Ah! I bet that was a fun lesson for you to learn!</p>

#### [ Simon Hudon (Apr 24 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597116):
<p>Btw, can you think of a better name than <code>bridge_gap</code>?</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597120):
<p>I expect this is in part because this is a built in notation (like the forward arrow for functions), since it shows up in <code>do</code> notation</p>

#### [ Simon Hudon (Apr 24 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597133):
<p>That makes sense. I'm actually glad that notation is built in</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597137):
<p>Also I think that the polarity of <code>&lt;-</code> should be reversed</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597139):
<p><code>eq.mpr</code> is the forward one</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597186):
<p>I'm not, if I had my way all notation would be declared in lean</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597187):
<p>maybe I'll get it in lean 4</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597189):
<p>but it does seem like a really hard one to do generically</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597202):
<p><code>convert</code>?</p>

#### [ Simon Hudon (Apr 24 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597243):
<p>That's a bit too close to <code>conv</code>, no?</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597245):
<p>to be fair it's actually doing a very similar thing</p>

#### [ Simon Hudon (Apr 24 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597248):
<p>That's true</p>

#### [ Andrew Ashworth (Apr 24 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597254):
<p>every time i see <code>conv</code> i think it's talking about convolution</p>

#### [ Simon Hudon (Apr 24 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597256):
<p>Is it something you'd like to have in <code>mathlib</code> btw?</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597260):
<p>little tactics like this are not a big deal</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597312):
<p>go right ahead</p>

#### [ Simon Hudon (Apr 24 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597315):
<p>Cool</p>

#### [ Mario Carneiro (Apr 24 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597328):
<p>I've been busy with my other obligations this past week, but I promise I'll finish updating mathlib and get on those PRs</p>

#### [ Simon Hudon (Apr 24 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125597577):
<p>I think the amount of work you've put on <code>mathlib</code> is actually amazing. I think you shouldn't feel like you have to apologize</p>

#### [ Sean Leather (Apr 24 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125605769):
<p><a href="/user_uploads/3121/bGfjZkmMdvJegOrpJ6MnVKEB/22.png" target="_blank" title="22.png">22</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/bGfjZkmMdvJegOrpJ6MnVKEB/22.png" target="_blank" title="22"><img src="/user_uploads/3121/bGfjZkmMdvJegOrpJ6MnVKEB/22.png"></a></div>

#### [ Sean Leather (Apr 24 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125605781):
<p>... for anyone keeping count.</p>

#### [ Johan Commelin (Apr 24 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125606413):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> wishing you luck. I just want to thank you for everything you're doing. Please don't feel any pressure from the game these guys are playing...</p>

#### [ Johan Commelin (Apr 24 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125606414):
<p>/me wouldn't want another hermit</p>

#### [ Sean Leather (Apr 24 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125606808):
<p>I haven't followed the entire conversation, but, to be clear, I think the PR count should not be taken as a backlog waiting to be completed but rather as a sign of interest in the growth of mathlib.</p>

#### [ Sean Leather (Apr 24 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125606862):
<p>Personally, I have my own backlog of things I want to contribute, but I'm waiting (patiently, mind you) for stabilization of mathlib wrt Lean.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125609412):
<p>I absolutely agree. I put in a couple of PR's for docs recently and once I did that I felt my job was done -- people can even see the docs if they want. There was no need at all to pester anyone to accept the PR's and I had plenty of other things to worry about. The fact that Lean doesn't keep changing at the minute is also really nice</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125609414):
<p>because I am not typing <code>leanpkg upgrade</code> all the time</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125609417):
<p>so if I really wanted something in mathlib that wasn't there yet, I could just edit the mathlib in <code>_target</code> in my project</p>

#### [ Patrick Massot (Apr 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125609536):
<p>Yes, this is what I did in <a href="https://github.com/PatrickMassot/mathlib/tree/wlog_ext" target="_blank" title="https://github.com/PatrickMassot/mathlib/tree/wlog_ext">https://github.com/PatrickMassot/mathlib/tree/wlog_ext</a>  (which is upstream + 2 PR)</p>

#### [ Scott Morrison (Apr 24 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125616698):
<p>I like <code>bridge_gap</code> (or whatever it ends up called). I had a primitive version that I was calling <code>its</code>. That is, I'd write <code>its X</code> as a generalised version of <code>exact X</code>, and I would be left with whatever goals were required to unify <code>X</code> with the actual goal.</p>

#### [ Scott Morrison (Apr 24 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125616701):
<p>(of course, apostrophe man would probably complain)</p>

#### [ Scott Morrison (Apr 24 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125616706):
<p>I'm certainly planning in discarding <code>its</code> in favour of this one once it's in mathlib.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125619917):
<p>how about <code>itis</code>? Signed, Apostrophe man.</p>

#### [ Simon Hudon (Apr 24 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125620284):
<p>What a cool super hero name :D</p>

#### [ Simon Hudon (Apr 24 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125620361):
<p>I submitted as <code>convert</code>. I'm not sure why <code>itis</code> works.</p>

#### [ Simon Hudon (Apr 24 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125620365):
<p>I'm wondering if <code>refine_congr</code> would be a good name.</p>

#### [ Kenny Lau (Apr 24 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125631877):
<p><a href="/user_uploads/3121/QoX4a9GPQ88G78zBt2MfjLzX/2018-04-25.png" target="_blank" title="2018-04-25.png">23</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/QoX4a9GPQ88G78zBt2MfjLzX/2018-04-25.png" target="_blank" title="23"><img src="/user_uploads/3121/QoX4a9GPQ88G78zBt2MfjLzX/2018-04-25.png"></a></div>

#### [ Kenny Lau (Apr 24 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125631910):
<p>Now I need to sleep</p>

#### [ Andrew Ashworth (Apr 24 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/apply%20with%20new%20equality%20goals/near/125632009):
<p>it would be less than 23 if you finished all your [WIPs] :)</p>


{% endraw %}
