---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00992rflandwildcardpattern.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rfl and wildcard pattern](https://leanprover-community.github.io/archive/113488general/00992rflandwildcardpattern.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jun 08 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127771996):
<p>Have a look at <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/b1e6489145be504e64a009226c6811bfd84a5070/src/valuations.lean#L143-L151" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/b1e6489145be504e64a009226c6811bfd84a5070/src/valuations.lean#L143-L151">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/b1e6489145be504e64a009226c6811bfd84a5070/src/valuations.lean#L143-L151</a>:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mul_assoc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">),</span> <span class="n">mul</span> <span class="o">(</span><span class="n">mul</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="n">z</span> <span class="bp">=</span> <span class="n">mul</span> <span class="n">x</span> <span class="o">(</span><span class="n">mul</span> <span class="n">y</span> <span class="n">z</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="n">some</span> <span class="err">$</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">mul_assoc</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="bp">_</span><span class="o">)</span> <span class="n">none</span>     <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="bp">_</span><span class="o">)</span> <span class="n">none</span>     <span class="o">(</span><span class="n">some</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="bp">_</span><span class="o">)</span> <span class="n">none</span>     <span class="n">none</span>     <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">none</span>     <span class="o">(</span><span class="n">some</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">none</span>     <span class="o">(</span><span class="n">some</span> <span class="bp">_</span><span class="o">)</span> <span class="n">none</span>     <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">none</span>     <span class="n">none</span>     <span class="o">(</span><span class="n">some</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="n">none</span> <span class="n">none</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>What would be a way to compress this down to three lines?  Replacing lines 3 to N by <code>|_ _ _ := rfl</code> doesn' work.</p>

#### [ Simon Hudon (Jun 08 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127772157):
<p>I would try something like:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mul_assoc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">),</span> <span class="n">mul</span> <span class="o">(</span><span class="n">mul</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="n">z</span> <span class="bp">=</span> <span class="n">mul</span> <span class="n">x</span> <span class="o">(</span><span class="n">mul</span> <span class="n">y</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">casesm</span><span class="bp">*</span> <span class="n">option</span> <span class="bp">_</span> <span class="bp">;</span> <span class="o">(</span><span class="n">apply</span> <span class="n">congr_arg</span> <span class="n">some</span> <span class="o">(</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">mul_assoc</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">)</span> <span class="bp">&lt;|&gt;</span> <span class="n">refl</span><span class="o">))</span> <span class="o">}</span>
</pre></div>

#### [ Simon Hudon (Jun 08 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127772285):
<p>Maybe this would be clearer and faster:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mul_assoc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">),</span> <span class="n">mul</span> <span class="o">(</span><span class="n">mul</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="n">z</span> <span class="bp">=</span> <span class="n">mul</span> <span class="n">x</span> <span class="o">(</span><span class="n">mul</span> <span class="n">y</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">casesm</span><span class="bp">*</span> <span class="n">option</span> <span class="bp">_</span><span class="o">,</span>
     <span class="o">{</span> <span class="n">exact</span> <span class="n">congr_arg</span> <span class="n">some</span> <span class="o">(</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">mul_assoc</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">)</span> <span class="o">},</span>
     <span class="n">all_goals</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">rfl</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>

#### [ Patrick Massot (Jun 08 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127774966):
<p>Thanks. You need to try <code>rfl</code> first or replace names by wildcards since <code>x</code>, <code>y</code>, <code>z</code> are defined only in one case</p>

#### [ Patrick Massot (Jun 08 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127774970):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mul_assoc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">),</span> <span class="n">mul</span> <span class="o">(</span><span class="n">mul</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="n">z</span> <span class="bp">=</span> <span class="n">mul</span> <span class="n">x</span> <span class="o">(</span><span class="n">mul</span> <span class="n">y</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">casesm</span><span class="bp">*</span> <span class="n">option</span> <span class="bp">_</span><span class="o">,</span>
     <span class="n">all_goals</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">congr_arg</span> <span class="n">some</span> <span class="o">(</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">&lt;|&gt;</span>  <span class="n">exact</span> <span class="n">rfl</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Jun 08 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775025):
<p>Isn't the correct answer to your initial question <code>obviously</code>?</p>

#### [ Patrick Massot (Jun 08 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775053):
<p>Ok, it's time for some tactic lecture. How to you get Lean to see the name of the theorem we are proving is <code>mul_assoc</code> and there are three variables in order to use this information instead of explicitly writing <code>_root_.mul_assoc _ _ _</code>? Then you can do a bunch of other proofs with the same tactic</p>

#### [ Patrick Massot (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775095):
<p>I don't think we have <code>obviously</code> yet. But indeed it would be the correct answer</p>

#### [ Patrick Massot (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775102):
<p>Maybe we can add Scott's repo as a dependency</p>

#### [ Johan Commelin (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775105):
<p>Exactly.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775112):
<p>But I think it requires adding lots of attribute through mathlib.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775113):
<p>So it might not go as smoothly as we hope.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775144):
<p>His library is not orthogonal to mathlib, so it won't be an easy PR, I guess.</p>

#### [ Patrick Massot (Jun 08 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775194):
<p>I don't think it's true</p>

#### [ Simon Hudon (Jun 08 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775202):
<p>My pull request has not been merged yet but if you want to use my branch the code would end up very similar to your indexed product.</p>

#### [ Johan Commelin (Jun 08 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775278):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I would love to be proved wrong. But what I've seen so far, is that you need to put a lot of attributes at a lot of definitions. And then afterwards life becomes easy.</p>

#### [ Patrick Massot (Jun 08 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775330):
<p>At least you can add lean-tidy to the project and then <code>import tidy.tidy</code> and get access to <code>obviously</code>. Then it doesn't prove this lemma</p>

#### [ Patrick Massot (Jun 08 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775340):
<p>Simon I don't understand what you wrote</p>

#### [ Johan Commelin (Jun 08 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775402):
<blockquote>
<p>At least you can add lean-tidy to the project and then <code>import tidy.tidy</code> and get access to <code>obviously</code>. Then it doesn't prove this lemma</p>
</blockquote>
<p>Right... but your point is that it might still prove other lemma's?</p>

#### [ Patrick Massot (Jun 08 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775419):
<p>I hope so</p>

#### [ Patrick Massot (Jun 08 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775434):
<p>Let's see what time is it in Australia.</p>

#### [ Simon Hudon (Jun 08 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775439):
<p>I made a pull request with <code>refine_struct</code> that would be useful here. It hasn't been merged yet but you can still use it.</p>

#### [ Patrick Massot (Jun 08 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775487):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> We currently have this proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mul_assoc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">),</span> <span class="n">mul</span> <span class="o">(</span><span class="n">mul</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="n">z</span> <span class="bp">=</span> <span class="n">mul</span> <span class="n">x</span> <span class="o">(</span><span class="n">mul</span> <span class="n">y</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">casesm</span><span class="bp">*</span> <span class="n">option</span> <span class="bp">_</span><span class="o">,</span>
      <span class="n">all_goals</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">congr_arg</span> <span class="n">some</span> <span class="o">(</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">mul_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">&lt;|&gt;</span>  <span class="n">refl</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>


<p>Question: should this be killed by one of your magic tactics?</p>

#### [ Patrick Massot (Jun 08 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775493):
<p>Simon: But the question at hand has no structure to refine</p>

#### [ Simon Hudon (Jun 08 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775587):
<p>Aren't you building up to a monoid or semigroup?</p>

#### [ Patrick Massot (Jun 08 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775601):
<p>True</p>

#### [ Patrick Massot (Jun 08 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775607):
<p>I don't know what I was thinking</p>

#### [ Simon Hudon (Jun 08 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775614):
<p>You may be able to have only one proof for the whole instance</p>

#### [ Patrick Massot (Jun 08 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775662):
<p>I was carelessly browsing code in lean-perfectoid and saw this lemma with seven stupid lines and focussed on it. But of course its only use is in an instance later.</p>

#### [ Simon Hudon (Jun 08 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775784):
<p>That's a pretty common mindset for me. That's actually a fun part of doing engineering: some days I don't feel smart so I can do some mindless tasks until I feel inspired again. The downside is that I don't consider much contexts while doing that so I end up improving the minutia of solutions that should just scrapped altogether</p>

#### [ Patrick Massot (Jun 08 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775861):
<p>It's a bit annoying that this PR is not merged because it's content is scattered among several files, so it's not immediate to incorporate it into another project</p>

#### [ Simon Hudon (Jun 08 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775950):
<p>What you can do is link to my repo in your toml file</p>

#### [ Simon Hudon (Jun 08 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127775976):
<p>I may have to update that branch first but I can do that right now</p>

#### [ Patrick Massot (Jun 08 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127776127):
<p>That may be a good solution if <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> need more time to review your PR, because the Perfectoid project will need a lot of instances of algebraic objects.</p>

#### [ Simon Hudon (Jun 08 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127777679):
<p>It's ready when you are.</p>

#### [ Patrick Massot (Jun 08 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779269):
<p>After doing <code>field ← get_current_field,</code> how would you replace <code>whatever.something</code> with <code>_root_.something</code> inside <code>field</code> so that I can later use it in the relevant version of <code>derive_field</code>?</p>

#### [ Simon Hudon (Jun 08 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779369):
<p>Is <code>whatever</code> something like <code>semigroup</code>?</p>

#### [ Patrick Massot (Jun 08 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779372):
<p>yes</p>

#### [ Simon Hudon (Jun 08 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779429):
<p>Why do you need to strip it away?</p>

#### [ Patrick Massot (Jun 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779454):
<p>because it doesn't work otherwise</p>

#### [ Patrick Massot (Jun 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779456):
<p>see the handcrafted proof above</p>

#### [ Simon Hudon (Jun 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779538):
<p>Do you have an instance of <code>semigroup</code> for <code>α</code>?</p>

#### [ Patrick Massot (Jun 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779562):
<p><code>linear_ordered_comm_group</code> actually</p>

#### [ Patrick Massot (Jun 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779564):
<p>and the goal is to build <code>linear_ordered_comm_monoid (option α)</code></p>

#### [ Patrick Massot (Jun 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779611):
<p>but <code>to_string field</code> turns out to be <code>comm_monoid.mul_assoc</code> here</p>

#### [ Patrick Massot (Jun 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779616):
<p>but the proof then needs <code>_root_.mul_assoc</code></p>

#### [ Simon Hudon (Jun 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779821):
<p>I find it odd: the types are very similar. Can you give me the error you get when your proof fails?</p>

#### [ Simon Hudon (Jun 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127779827):
<p>(It is possible to do what you ask but I think we're better off taking a different approach)</p>

#### [ Patrick Massot (Jun 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127780142):
<p>I minimized to </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">pi_instances</span>

<span class="n">class</span> <span class="n">linear_ordered_comm_group</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
    <span class="kn">extends</span> <span class="n">comm_group</span> <span class="n">α</span><span class="o">,</span> <span class="n">linear_order</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">mul_le_mul_left</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span>

<span class="n">class</span> <span class="n">linear_ordered_comm_monoid</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
    <span class="kn">extends</span> <span class="n">comm_monoid</span> <span class="n">α</span><span class="o">,</span> <span class="n">linear_order</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">mul_le_mul_left</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_comm_group</span> <span class="n">α</span><span class="o">]</span>


<span class="n">def</span> <span class="n">mul</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span>        <span class="bp">_</span>        <span class="o">:=</span> <span class="n">none</span>

<span class="n">def</span> <span class="n">one</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">some</span> <span class="mi">1</span>

<span class="n">def</span> <span class="n">le</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="bp">_</span><span class="o">)</span> <span class="n">none</span>     <span class="o">:=</span> <span class="n">false</span>
<span class="bp">|</span> <span class="n">none</span>     <span class="bp">_</span>        <span class="o">:=</span> <span class="n">true</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">linear_ordered_comm_monoid</span> <span class="o">(</span><span class="n">option</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine_struct</span> <span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="n">mul</span><span class="o">,</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">one</span><span class="o">,</span> <span class="n">le</span> <span class="o">:=</span> <span class="n">le</span><span class="o">,</span> <span class="bp">..</span> <span class="o">}</span><span class="bp">;</span> <span class="o">{</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">derive_field_option</span> <span class="o">}</span>
</pre></div>


<p>The game is to add <code>derive_field_option</code> to <code>algebra.pi_instances</code> (from your branch of course) to make it work</p>

#### [ Patrick Massot (Jun 08 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127780175):
<p>Again, this is not crucial, Kenny did it by hand, I'm only trying to slowly learn tactic writing for specialized automation</p>

#### [ Simon Hudon (Jun 08 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127780177):
<p>Nice :) I'm going to play a bit :D</p>

#### [ Patrick Massot (Jun 08 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127780228):
<p>I should go and take care of my family (I'm not even talking about the work I should have been doing)</p>

#### [ Simon Hudon (Jun 08 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127780239):
<p>Ah family! They keep interrupting math, don't they? :D</p>

#### [ Patrick Massot (Jun 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127780314):
<p>The version which doesn't work is:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">derive_field_option</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">b</span> <span class="err">←</span> <span class="n">target</span> <span class="bp">&gt;&gt;=</span> <span class="n">is_prop</span><span class="o">,</span>
  <span class="k">if</span> <span class="n">b</span> <span class="k">then</span> <span class="n">do</span>
     <span class="n">field</span> <span class="err">←</span> <span class="n">get_current_field</span><span class="o">,</span>
     <span class="n">trace</span> <span class="o">(</span><span class="n">to_string</span> <span class="n">field</span><span class="o">),</span>
     <span class="n">intros</span><span class="o">,</span>
     <span class="bp">`</span><span class="o">[</span><span class="n">casesm</span><span class="bp">*</span> <span class="n">option</span> <span class="bp">_</span><span class="o">],</span>
     <span class="bp">`</span><span class="o">[</span><span class="n">all_goals</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">congr_arg</span> <span class="n">some</span> <span class="o">(</span><span class="n">field</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">&lt;|&gt;</span> <span class="n">exact</span> <span class="n">rfl</span> <span class="o">}]</span>
  <span class="k">else</span> <span class="n">do</span> <span class="n">skip</span>
</pre></div>

#### [ Scott Morrison (Jun 11 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20and%20wildcard%20pattern/near/127888806):
<p>Just arrived back from underwater. I've starred the proof you asked about, @Patrick, and will try out <code>obviously</code>. I suspect it requires more case bashing (on <code>option</code>) than obviously is by default willing to do.</p>


{% endraw %}
