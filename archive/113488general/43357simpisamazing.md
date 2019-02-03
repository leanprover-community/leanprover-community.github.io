---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43357simpisamazing.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp is amazing](https://leanprover-community.github.io/archive/113488general/43357simpisamazing.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Mar 04 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123265688):
<p>I was proving some lemmas about disjoint finsets, and I was amazed to find that this goal was solved by <code>simp {contextual := tt}</code>, when I previously had a 10 line proof.</p>
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">,</span>
<span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="bp">∀</span> <span class="o">⦃</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">⦄</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">},</span>
    <span class="n">a</span> <span class="err">∉</span> <span class="n">s</span> <span class="bp">→</span>
    <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">),</span> <span class="n">disjoint</span> <span class="n">s</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">card</span> <span class="o">(</span><span class="n">s</span> <span class="err">∪</span> <span class="n">t</span><span class="o">)</span> <span class="bp">=</span> <span class="n">card</span> <span class="n">s</span> <span class="bp">+</span> <span class="n">card</span> <span class="n">t</span><span class="o">)</span> <span class="bp">→</span>
    <span class="bp">∀</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">),</span> <span class="n">disjoint</span> <span class="o">(</span><span class="n">insert</span> <span class="n">a</span> <span class="n">s</span><span class="o">)</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">card</span> <span class="o">(</span><span class="n">insert</span> <span class="n">a</span> <span class="n">s</span> <span class="err">∪</span> <span class="n">t</span><span class="o">)</span> <span class="bp">=</span> <span class="n">card</span> <span class="o">(</span><span class="n">insert</span> <span class="n">a</span> <span class="n">s</span><span class="o">)</span> <span class="bp">+</span> <span class="n">card</span> <span class="n">t</span>
</pre></div>


<p>To solve this goal before I noticed that <code>simp</code> did it, I had to rewrite <code>card (insert a s) + card t</code> to <code>card s + card (insert a t)</code> which involves using <code>rw ← card_insert_of_not_mem</code>, where card_insert_of_not_mem is a <code>simp</code> lemma, used in the wrong direction, so I'm wondering how simp managed it. The only <code>@[simp]</code> lemma it used which isn't already in the library is <code>disjoint_insert_left [decidable_eq α] {a : α} {s t : finset α} :  disjoint (insert a s) t ↔ a ∉ t ∧ disjoint s t</code></p>

#### [ Kevin Buzzard (Mar 04 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123266504):
<p>Chris -- you can find out how simp did it -- I ran into this when preparing my blog post on congruence being an equivalence relation</p>

#### [ Kevin Buzzard (Mar 04 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123266547):
<p>and I wrote it up as something-which-might-be-useful-as-a-document at</p>

#### [ Kevin Buzzard (Mar 04 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123266550):
<p><a href="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md">https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md</a></p>

#### [ Kevin Buzzard (Mar 04 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123266551):
<p>Do you want to edit it and then we could submit it as a PR?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123266554):
<p>I still have no idea how simp works in practice, all I know is that it randomly looks through its database and tries stuff. I have no idea about its strategy though.</p>

#### [ Chris Hughes (Mar 04 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123267383):
<p>It's way more sophisticated than I previously thought. Another capability that I only discovered today is that if a simp lemma of the form <code>p → x = y</code> can be used if there is a proof of p in the context. Looking at the trace I can see that it didn't use the method I used, and instead rewrote <code>card (insert a s ∪ t)</code> to <code>card (insert a (s ∪ t))</code> and then must have somehow worked out that it should try to prove and prove <code>a ∉  s ∪ t</code>, from proofs of <code>a ∉ s</code> and <code>a ∉ t</code> in the context, so it could use card_insert_of_not_mem, which seems quite sophisticated to me. I can't add to the docs really, because I don't know what's going on.</p>

#### [ Andrew Ashworth (Mar 04 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123267882):
<p>i like how you mention Prolog-like search in your simp.md</p>

#### [ Andrew Ashworth (Mar 04 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123267935):
<p>I would amend that to backtracking search, as described in <a href="https://en.wikipedia.org/wiki/Backtracking" target="_blank" title="https://en.wikipedia.org/wiki/Backtracking">https://en.wikipedia.org/wiki/Backtracking</a>, if you want to give a good description of it</p>

#### [ Andrew Ashworth (Mar 04 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268115):
<p>I agree with you that these days, nobody has heard of Prolog</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268168):
<blockquote>
<p>I agree with you that these days, nobody has heard of Prolog</p>
</blockquote>
<p>Oh the reason I mention it is far more mundane! I have no CS background at all and had no idea what a Prolog-like search meant but the phrase is mentioned several times in the Lean docs so I just started using it as meaning "something I don't understand at all" because I had no idea how simp worked</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268207):
<p>I'm not sure I like the word backtracking here.  The only place where simp backtracks in any meaningful sense is when you have a conditional simp lemma (such as <code>p -&gt; x = y</code> above), and simp fails to discharge the assumption.  Otherwise simp never goes back to a previous step.</p>

#### [ Andrew Ashworth (Mar 04 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268208):
<p>i've been mislead</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268209):
<p>I am going to PR these simp docs in the hope that other people can actually make them correct and helpful.</p>

#### [ Andrew Ashworth (Mar 04 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268218):
<p>tpil describes simp as a prolog-like search, which in my mind means backtracking</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268263):
<p>Where does TPIL say that?  I can't find either backtrack or prolog.</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268267):
<p>If you're looking for a short buzzwordy description, I'd use "simp applies a conditional term rewriting system".</p>

#### [ Andrew Ashworth (Mar 04 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268271):
<p>hmm, looking at the current version, it mentions it when describing the type class instance resolution mechanism</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268275):
<p>I can quite believe I've conflated the two. As I say, I was using the entire phrase as a joke for a while</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268276):
<p>Indeed, type class inference is essentially a version of λProlog and uses backtracking.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268315):
<p>I would just use it to describe anything I couldn't understand.</p>

#### [ Andrew Ashworth (Mar 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268316):
<p>i'll just claim that i was bamboozled by kevin :)</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268317):
<p>I'll fix it</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268318):
<p>Prolog = try to <code>apply</code> all the theorems you know and repeat for the generated subgoals</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268378):
<p><a href="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md">https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md</a></p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268379):
<p>With a bit of artistic license:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">prolog</span> <span class="o">(</span><span class="n">lemmas</span> <span class="o">:</span> <span class="n">list</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">first</span> <span class="err">$</span> <span class="n">lemmas</span><span class="bp">.</span><span class="n">for</span> <span class="err">$</span> <span class="bp">λ</span><span class="n">l</span><span class="o">,</span> <span class="n">applyc</span> <span class="n">l</span><span class="bp">;</span> <span class="n">prolog</span>
</pre></div>

#### [ Gabriel Ebner (Mar 04 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268428):
<p>Re: documentation.  If you mention congruence, you could show off simp's support for congruence relations.  If you show reflexivity and transitivity for <code>cong</code>, and have congruence lemmas for <code>+</code>, etc., then you can rewrite with congruences as if they were equations.</p>

#### [ Patrick Massot (Mar 04 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268470):
<p>I think you should mention the <code>@[simp] lemma my_lemma : fact &lt;-&gt; true</code> trick</p>

#### [ Patrick Massot (Mar 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123268480):
<p>especially since it could be confusing when reading existing Lean code</p>

#### [ Reid Barton (Mar 04 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123272385):
<p><span class="user-mention" data-user-email="chrishughes24@gmail.com" data-user-id="110044">@Chris Hughes</span>, if you just want to see what simp ended up doing (and not all the things that it didn't do), then I've found <code>set_option trace.simplify.rewrite true</code> to produce a more manageable amount of information.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123273896):
<p>I've added Reid's comment. Patrick -- is this some trick for getting simp to know about facts which are not necessarily of the form <code>x=y</code> or <code>x iff y</code>? Assuming it is I've added it too. I am not sure I am competent enough to add Gabriel's comment so it's unedited at the bottom of <a href="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md">https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md</a></p>

#### [ Patrick Massot (Mar 04 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123273963):
<p>Yes. It's more a comment to your first bullet than a third one</p>

#### [ Patrick Massot (Mar 04 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20is%20amazing/near/123274002):
<p>If you want a cheap way to document stuff about simp not in TPIL you can also search for simp in <a href="https://github.com/leanprover/lean/blob/master/doc/changes.md" target="_blank" title="https://github.com/leanprover/lean/blob/master/doc/changes.md">https://github.com/leanprover/lean/blob/master/doc/changes.md</a></p>


{% endraw %}
