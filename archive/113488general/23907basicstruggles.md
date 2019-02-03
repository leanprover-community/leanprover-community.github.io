---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23907basicstruggles.html
---

## Stream: [general](index.html)
### Topic: [basic struggles](23907basicstruggles.html)

---


{% raw %}
#### [ Johan Commelin (Aug 07 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131024386):
<p>I find myself struggling with things that are extremely math-trivial. If I have a goal of the form <code>a = b</code>, how do I turn that into <code>a * c = b * c</code>? (Assume that <code>a b c : R</code> and <code>[comm_ring R]</code>.)</p>

#### [ Simon Hudon (Aug 07 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131024655):
<p>Have you tried <code>mul_right_cancel_iff</code>?</p>

#### [ Johan Commelin (Aug 07 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131024771):
<p>Hmmm, I only need the easy implication, for which I don't need a cancellative instance.</p>

#### [ Johan Commelin (Aug 07 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131024779):
<p>And in fact I don't have an instance of cancellative semiblabla... <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Simon Hudon (Aug 07 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025662):
<p>Ok, I think I see the issue. If <code>R</code> was a multiplicative group, you'd have a <code>left_cancel_semigroup</code> for free. As it is, your statement is not true I think because rings don't have a multiplicative inverse for every non-zero element.</p>

#### [ Simon Hudon (Aug 07 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025717):
<p>If you had a field though ...</p>

#### [ Simon Hudon (Aug 07 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025720):
<p>Can you choose your <code>c</code> so that it has an inverse?</p>

#### [ Johan Commelin (Aug 07 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025721):
<p>Hmmz, sorry, I've been brainfarting...</p>

#### [ Johan Commelin (Aug 07 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025729):
<p>My <code>c</code> has an inverse</p>

#### [ Simon Hudon (Aug 07 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025730):
<p>How rude! :)</p>

#### [ Johan Commelin (Aug 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025770):
<p>I'll copy-paste my goal.</p>

#### [ Johan Commelin (Aug 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025771):
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="n">witt_polynomial</span> <span class="n">n</span> <span class="bp">-</span>
         <span class="n">map₂</span> <span class="n">witt_polynomial</span> <span class="n">C</span>
           <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">),</span> <span class="err">↑</span><span class="n">p</span> <span class="err">^</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">*</span> <span class="n">X_in_terms_of_W</span> <span class="o">(</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">))))</span> <span class="bp">*</span>
      <span class="n">C</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="err">↑</span><span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="bp">=</span>
    <span class="n">X</span> <span class="n">n</span>
</pre></div>

#### [ Johan Commelin (Aug 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025773):
<p>So you see that there is this term <code>C (1 / _)</code>.</p>

#### [ Johan Commelin (Aug 07 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025775):
<p>I would like to move it to the other side.</p>

#### [ Johan Commelin (Aug 07 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025784):
<p>This goal has been misbehaving quite a lot, lately.</p>

#### [ Simon Hudon (Aug 07 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025850):
<p>What is the statement that <code>C (1 / _)</code> has an inverse like?</p>
<p>(it does look pretty hairy)</p>

#### [ Johan Commelin (Aug 07 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131025960):
<p>Well <code>1 / _</code> has an inverse in <code>rat</code>. And <code>C</code> is a ring hom. So it maps inverses to inverses.</p>

#### [ Simon Hudon (Aug 07 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026067):
<p>So in short, <code>C _</code> is the inverse <code>C (1 / _)</code> I assume. It is surprisingly hard to sneak in I realize. Any chance <code>C</code> has an inverse? Then you could transform your goal from <code>R</code> to <code>rat</code> just long enough to play with the inverse.</p>

#### [ Simon Hudon (Aug 07 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026077):
<p>(That's probably a long shot: if you had that inverse of C, <code>R</code> would probably be a field)</p>

#### [ Johan Commelin (Aug 07 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026078):
<p>No, <code>C</code> is the function <code>R \to mv_polynomial Xs R</code> that takes a ring element to the constant polynomial.</p>

#### [ Simon Hudon (Aug 07 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026130):
<p>I'm starting to think your assumptions are not strong enough for what you're trying to do</p>

#### [ Johan Commelin (Aug 07 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026132):
<p>Ok, so <code>rat</code> is a field, therefore <code>p^(n+1)</code> has an inverse (it is nonzero). Now I apply <code>C</code> to <code>p^(n+1)</code> and I get a crazy element of some ring, and it will still have an inverse.</p>

#### [ Johan Commelin (Aug 07 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026138):
<p>So I want to multiply both sides with <code>C (p^(n+1))</code>.</p>

#### [ Mario Carneiro (Aug 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026180):
<p>you are thinking backwards</p>

#### [ Simon Hudon (Aug 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026193):
<p>What if you multiply by <code>C 1</code> on the right</p>

#### [ Mario Carneiro (Aug 07 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026194):
<p>you want to multiply some equation that will be your new goal by <code>C (1 / ↑p ^ (n + 1))</code></p>

#### [ Johan Commelin (Aug 07 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026201):
<p>Right</p>

#### [ Johan Commelin (Aug 07 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026247):
<p>So I use suffices?</p>

#### [ Simon Hudon (Aug 07 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026248):
<p>... and then decompose it to <code>C (x * 1/x)</code> and then <code>C x * C (1/x)</code></p>

#### [ Mario Carneiro (Aug 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026254):
<p>Here's a trick: <code>rw (_ : _ - _ = X n * C (p ^ (n + 1)))), {simp}</code></p>

#### [ Mario Carneiro (Aug 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026262):
<p>(maybe <code>simp</code> won't kill that goal, you may need to do some more careful rewrites, but it should still be relatively easy)</p>

#### [ Simon Hudon (Aug 07 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026263):
<p>Whaaaa?</p>

#### [ Mario Carneiro (Aug 07 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026310):
<p>there should be a simp lemma <code>C(1/x) = 1/C x</code></p>

#### [ Mario Carneiro (Aug 07 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026311):
<p>then <code>simp</code> will kill the goal</p>

#### [ Johan Commelin (Aug 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026422):
<p>Too bad:</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="err">⊢</span> <span class="n">has_sub</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="bp">ℕ</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Aug 07 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026426):
<p>It didn't figure out the base ring...</p>

#### [ Mario Carneiro (Aug 07 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026517):
<p>You have to add a type ascription</p>

#### [ Mario Carneiro (Aug 07 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131026526):
<p>or fill it in a bit more, <code>witt_polynomial n - _ = ...</code></p>

#### [ Johan Commelin (Aug 07 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131027462):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm not sure if <code>1/C x</code> makes sense? There is no division in the polynomial ring, right?</p>

#### [ Johan Commelin (Aug 07 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131027506):
<p>Or maybe there is, in the sense of Euclidean domains... but that is not what we want here.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131027510):
<p>Oh, I see... <code>C x</code> is a unit of the ring</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/basic%20struggles/near/131027588):
<p>maybe this is why I thought <code>C_mul</code> was not a good simp lemma</p>


{% endraw %}
