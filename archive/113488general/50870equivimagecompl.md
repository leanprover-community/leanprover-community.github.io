---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50870equivimagecompl.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [equiv.image_compl](https://leanprover-community.github.io/archive/113488general/50870equivimagecompl.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Apr 01 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501726):
<p>Do we have <code>example (f : equiv a b) (s : set a) : f '' -s = - f '' s</code> hidden somewhere?</p>

#### [ Patrick Massot (Apr 01 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501766):
<p>(or not hidden would also be good)</p>

#### [ Mario Carneiro (Apr 01 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501930):
<p>Didn't this come up earlier?</p>

#### [ Mario Carneiro (Apr 01 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501972):
<p>You asked about this identity and we found it wasn't there, then you wrote a proof</p>

#### [ Patrick Massot (Apr 01 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501974):
<p>Really?</p>

#### [ Patrick Massot (Apr 01 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501980):
<p>I'm trying to get back to doing Lean, but I forgot where I stopped</p>

#### [ Patrick Massot (Apr 01 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501988):
<p>But I don't see that one in my file</p>

#### [ Mario Carneiro (Apr 01 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502043):
<p><a href="#narrow/stream/113488-general/subject/image.20of.20complement/near/123655801" title="#narrow/stream/113488-general/subject/image.20of.20complement/near/123655801">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/image.20of.20complement/near/123655801</a></p>

#### [ Patrick Massot (Apr 01 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502045):
<p>Ok, I can see I already asked the question</p>

#### [ Patrick Massot (Apr 01 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502051):
<p>But I don't see my proof there</p>

#### [ Patrick Massot (Apr 01 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502052):
<p>So presumably I never proved it</p>

#### [ Patrick Massot (Apr 01 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502055):
<p>because real life caught me</p>

#### [ Patrick Massot (Apr 01 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502328):
<p>This is so painful</p>

#### [ Patrick Massot (Apr 01 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502482):
<p>I give up for tonight. I'm stuck at proving that if b is not in the image of S then its preimage is not in S</p>

#### [ Patrick Massot (Apr 02 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503021):
<p>I had a new idea while feeding the cat, so now I'm stuck at <code>example (f : equiv α β) (b) : f (f.inv_fun b) = b := sorry</code></p>

#### [ Kenny Lau (Apr 02 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503061):
<p><code>f.right_inv b</code>?</p>

#### [ Patrick Massot (Apr 02 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503062):
<p>This so frustrating <span class="emoji emoji-1f479" title="ogre">:ogre:</span></p>

#### [ Patrick Massot (Apr 02 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503067):
<p>that's funny (and frustrating). I tried a million variations on <code>rw f.right_inv b</code> in my main proof</p>

#### [ Patrick Massot (Apr 02 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503068):
<p>it always fail</p>

#### [ Patrick Massot (Apr 02 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503069):
<p>but when you extract the statement as a lemma it works</p>

#### [ Kenny Lau (Apr 02 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503109):
<p>maybe if you stop writing <code>f.to_fun</code> as <code>f</code> then <code>rw</code> will work</p>

#### [ Patrick Massot (Apr 02 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503110):
<p>I did not write this</p>

#### [ Patrick Massot (Apr 02 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503158):
<p>even inside conversion mode it fails</p>

#### [ Patrick Massot (Apr 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503205):
<p>I think this is the most ridiculous proof I ever wrote in Lean. The ratio "ugliness of proof"/"triviality of statement" is probably my worse so far</p>

#### [ Patrick Massot (Apr 02 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503210):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">fuck</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">f</span><span class="bp">.</span><span class="n">right_inv</span> <span class="n">b</span>

<span class="kn">lemma</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">image_compl</span>  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="bp">-</span><span class="n">s</span> <span class="bp">=</span> <span class="bp">-</span><span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">b</span> <span class="n">b_in_image_compl</span><span class="o">,</span>
    <span class="n">rcases</span> <span class="n">b_in_image_compl</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">a_compl_s</span><span class="o">,</span> <span class="n">f_a_b</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">apply_eq_iff_eq_inverse_apply</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="n">f_a_b</span> <span class="n">at</span> <span class="n">a_compl_s</span><span class="o">,</span>
    <span class="n">exact</span> <span class="o">(</span><span class="n">mt</span> <span class="o">(</span><span class="bp">@</span><span class="n">mem_image_iff_of_inverse</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">f</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">b</span> <span class="n">s</span> <span class="n">f</span><span class="bp">.</span><span class="n">left_inv</span> <span class="n">f</span><span class="bp">.</span><span class="n">right_inv</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span>
<span class="n">a_compl_s</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">subset_def</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">b</span> <span class="n">b_in_compl_image</span><span class="o">,</span>
    <span class="n">apply</span> <span class="o">(</span><span class="bp">@</span><span class="n">mem_image_iff_of_inverse</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span><span class="bp">.</span><span class="n">left_inv</span> <span class="n">f</span><span class="bp">.</span><span class="n">right_inv</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">b_not_in_image</span> <span class="o">:=</span> <span class="n">not_mem_of_mem_compl</span> <span class="n">b_in_compl_image</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_compl_eq</span><span class="o">,</span>
    <span class="n">by_contra</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">:=</span> <span class="n">mem_image_of_mem</span> <span class="n">f</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">fuck</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
    <span class="n">finish</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Apr 02 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503212):
<p>But at least Lean was defeated</p>

#### [ Mario Carneiro (Apr 02 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503802):
<p>Actually, I recommend not using <code>f.right_inv</code> in favor of the coercions</p>

#### [ Kevin Buzzard (Apr 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504087):
<p>Another example of mathematicians getting very frustrated about how sometimes something which is "trivial in maths" can be hard in Lean.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504088):
<p>In the long term these really need to be fixed somehow</p>

#### [ Kevin Buzzard (Apr 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504090):
<p>if CS people want mathematicians to use the software.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504131):
<p>And funnily enough, just the same thing happened to me with rw</p>

#### [ Simon Hudon (Apr 02 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504132):
<p>I don't think it will ever happen that a mathematician using this or another theorem prover and will, 100% of the time, think "this is trivial" and have the prover confirm that (when the statement is true).</p>

#### [ Kevin Buzzard (Apr 02 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504133):
<p>no, with exact</p>

#### [ Kevin Buzzard (Apr 02 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504140):
<p><code>exact (congr_fun H HUigx)</code> failed (type mismatch)</p>

#### [ Kevin Buzzard (Apr 02 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504143):
<p>but <code>have H2 := congr_fun H HUigx, exact H2</code> succeeded</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504524):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>  I definitely think that this should happen in the future.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504526):
<p>I am suggesting we meet you somewhere in the middle.</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504533):
<p>But if it doesn't happen then what hope is there for people to start adopting this computer viewpoint?</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504534):
<p>I think it's a matter of education on our part and adding lemmas on your part</p>

#### [ Kevin Buzzard (Apr 02 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504574):
<p>We already saw this week how Chris couldn't prove something which was mathematically trivial, and then we found a framework for it and it became straightforward to prove</p>

#### [ Simon Hudon (Apr 02 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504629):
<p>In that case, I think we're on the same page. In general, we probably need to build packages to better support undergraduate level mathematics and at least the basics of graduate level math.</p>

#### [ Simon Hudon (Apr 02 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504631):
<p>Improving the automation and the documentation for building your own tactics will probably help you bridge the gap too.</p>

#### [ Mario Carneiro (Apr 02 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124507833):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  I wrote a proof of this that should appear in mathlib once it finishes checking. It's not nearly as complicated as you made it, and after appropriate sublemmas it's a one-liner:</p>
<div class="codehilite"><pre><span></span>theorem image_compl_subset {f : α → β} {s : set α} (H : injective f) :
  f &#39;&#39; -s ⊆ -(f &#39;&#39; s) :=
subset_compl_iff_disjoint.2 $ by simp [image_inter H]

theorem subset_image_compl {f : α → β} {s : set α} (H : surjective f) :
  -(f &#39;&#39; s) ⊆ f &#39;&#39; -s :=
compl_subset_iff_union.2 $
by rw ← image_union; simp [image_univ_of_surjective H]

theorem image_compl_eq {f : α → β} {s : set α} (H : bijective f) :
  f &#39;&#39; -s = -(f &#39;&#39; s) :=
subset.antisymm (image_compl_subset H.1) (subset_image_compl H.2)
</pre></div>

#### [ Patrick Massot (Apr 02 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124518916):
<p>Thank you very much <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>. I noticed that many support lemmas were missing. I'll use my crappy version in the mean time. But I'm still very much interested in any explanation why I could not avoid having this one lemma in order to rewrite.</p>

#### [ Mario Carneiro (Apr 02 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124518965):
<p>I am not quite sure what you were doing, but I think you wrote things in a non-idiomatic way (which is to say, not the way that mathlib is designed to help with), which made the proof more painful than it should have been</p>

#### [ Mario Carneiro (Apr 02 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519016):
<p>The idiomatic version of your <code>fuck</code> lemma is <code>f (f.symm x) = x</code> (and it's called <code>apply_inverse_apply</code>)</p>

#### [ Kenny Lau (Apr 02 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519028):
<p><code> rw fuck at this </code></p>

#### [ Kenny Lau (Apr 02 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519031):
<p>i.e. <code>fuck this</code></p>

#### [ Patrick Massot (Apr 02 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519141):
<p>I'll tell you exactly what I was doing. First my brain absolutely refuses to think in this kind of situation, it's only filled with anger. Then I search for all lemmas in mathlib which seem vaguely related and try to apply them. But I got stuck with sorts of coercions issues, and stuff like rw refuses to rewrite etc, so I'm get even more upset. So of course the proof ends up not looking like what I would write on paper (of course in the beginning I would write nothing but then I'm able to write some proof on paper)</p>

#### [ Patrick Massot (Apr 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519148):
<p>But why does <code> rw f.right_inv b </code> fails?</p>

#### [ Kenny Lau (Apr 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519156):
<p><code>rw</code> matches exactly the expression</p>

#### [ Kenny Lau (Apr 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519157):
<p>without any definitorial expansion</p>

#### [ Patrick Massot (Apr 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519160):
<p>Something else I notice with your solution is I should have gave up on proving this on <code>equiv</code> but go back to functions and <code>bijective f</code></p>

#### [ Patrick Massot (Apr 02 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519200):
<p>At least this removes the coercion hell</p>

#### [ Kenny Lau (Apr 02 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519201):
<p>don't</p>

#### [ Kenny Lau (Apr 02 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519203):
<p>the <code>bijective f</code> has no data</p>

#### [ Kenny Lau (Apr 02 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519205):
<p>i.e. it is not constructive</p>

#### [ Sebastian Ullrich (Apr 02 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519206):
<blockquote>
<p><code>rw</code> matches exactly the expression </p>
</blockquote>
<p>This is only correct for the expression _head_</p>

#### [ Kenny Lau (Apr 02 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519212):
<p>matches the expression pattern</p>

#### [ Patrick Massot (Apr 02 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519265):
<p>I still fail to see how this explains my situation</p>

#### [ Patrick Massot (Apr 02 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519276):
<p>I only copied the hypothesis into the statement of a lemma, and this rw accepts to do its job</p>

#### [ Mario Carneiro (Apr 02 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519374):
<p>kenny, <code>bijective f</code> is a precondition to the theorem. Constructively, <code>bijective f</code> is weaker than <code>equiv</code>, so the theorem is stronger</p>

#### [ Kenny Lau (Apr 02 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519379):
<p>well</p>

#### [ Mario Carneiro (Apr 02 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519430):
<p>... but the proof uses excluded middle, although the theorem itself has no data anyway so it doesn't matter computation-wise</p>

#### [ Mario Carneiro (Apr 02 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519479):
<p>It's not possible to prove the versions I stated without excluded middle</p>

#### [ Patrick Massot (Apr 02 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519482):
<p>Needless to say, I'm perfectly happy with excluded middle in this proof</p>

#### [ Patrick Massot (Apr 02 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519488):
<p>And it's even better if I can get the opportunity to deduce from this the statement for equiv which could be constructive</p>

#### [ Kenny Lau (Apr 02 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519491):
<p>excluded middle is an overgeneralization of the situation observed from finite situations</p>


{% endraw %}
