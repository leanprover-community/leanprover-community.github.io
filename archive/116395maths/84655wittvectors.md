---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/84655wittvectors.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [witt vectors](https://leanprover-community.github.io/archive/116395maths/84655wittvectors.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jul 24 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216141):
<p>Anyone interested in sharpening his teeth on polynomials is encouraged to look here: <a href="https://gist.github.com/jcommelin/77240367c2815ca0c45da188ba78be19" target="_blank" title="https://gist.github.com/jcommelin/77240367c2815ca0c45da188ba78be19">https://gist.github.com/jcommelin/77240367c2815ca0c45da188ba78be19</a></p>

#### [ Johan Commelin (Jul 24 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216160):
<p>A bunch of stuff from the preamble will be obsolete as soon as Mario pushes his latest mathlib edits.</p>

#### [ Johan Commelin (Jul 24 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216186):
<p>In the final lemma there are a bunch of <code>sorry</code>s. The proof is extremely slow, and I am continuously struggling with deterministic timeouts.</p>

#### [ Johan Commelin (Jul 24 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216194):
<p>I have no idea why. It didn't feel to me like I was pushing limits.</p>

#### [ Johan Commelin (Jul 24 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216304):
<p>So there is about 180 lines of preamble. And then about 50 lines of interesting stuff <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Johan Commelin (Jul 24 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130216538):
<p>(A bit of motivation for these crazy polynomials: They are useful for defining rings of Witt vectors, and those show up all over the place in number theory. For example, the ring of p-adic integers turns out to be the ring of Witt vectors of the finite field with p elements.)</p>

#### [ Kevin Buzzard (Jul 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130220198):
<blockquote>
<p>In the final lemma there are a bunch of <code>sorry</code>s. The proof is extremely slow, and I am continuously struggling with deterministic timeouts.</p>
</blockquote>
<p>There is sometimes a reason for this ("your code is crappy for a reason which you didn't realise") but typically you have to get lucky with an expert looking at it and spotting what you did wrong. My valuation stuff got slow recently and I don't know why, but I didn't even bother posting 200 lines of Lean code and saying "why does this take three seconds to compile and I had to put some type class thing up to 100 to make it work?" because it's such a boring question; if I really cared I would try and minimise; currently I just grit my teeth and work around it.</p>

#### [ Johan Commelin (Jul 24 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130221163):
<p>So how do you work around deterministic timeouts? What determines such a timeout? Can I set some option to let Lean work harder?</p>

#### [ Kevin Buzzard (Jul 24 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130221200):
<p>Did you see the <code>1 &lt;= k &lt;= n</code> example? That one seemed to debate some discussion from the experts</p>

#### [ Kevin Buzzard (Jul 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130221240):
<p>Here's a conjecture: these things are almost always caused by the type class inference system. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what do you think about my conjecture?</p>

#### [ Mario Carneiro (Jul 25 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130259324):
<p>that's a bit of a general claim. Another way to make lean take a long time is to use lots of definitional equality or kernel computation, possibly on accident; and elaboration can often take a suspiciously long time to complete (not crazy but like 10-15 seconds for a term proof) for reasons I don't well understand</p>

#### [ Kevin Buzzard (Jul 25 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/130263224):
<p>There's a file in the perfectoid repo which takes 10 seconds to compile and I was half-thinking about trying to work out why so really I was looking for clues here.</p>

#### [ Johan Commelin (Aug 07 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131034587):
<p>Anyone care to take a look at <a href="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L107" target="_blank" title="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L107">https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L107</a> ? That file is self-contained, but depends on the latest mathlib.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131036884):
<p>I don't know what the type of anything is, but the lemma you're applying needs that the things you're applying it to are in a multiplicative group and the elements you're talking about look suspicious to me</p>

#### [ Kevin Buzzard (Aug 07 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131036897):
<p>A field is not a group under multiplication. Are you using the right lemma?</p>

#### [ Mario Carneiro (Aug 07 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037022):
<p>oh, good call</p>

#### [ Mario Carneiro (Aug 07 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037035):
<p>there are mirror versions of all the group lemmas for fields with namespace <code>division_ring</code> or <code>field</code></p>

#### [ Kevin Buzzard (Aug 07 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037136):
<p>This has happened to me so many times :-)</p>

#### [ Kevin Buzzard (Aug 07 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037218):
<p>"I can't find an instance of exactly what it says in the goal" usually for me means "the thing you want me to match with doesn't match because of something in square brackets"</p>

#### [ Mario Carneiro (Aug 07 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131037272):
<p>heh, I remember so many questions from you like that</p>

#### [ Johan Commelin (Aug 07 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131038606):
<p>I'm slowly making progress... <code>conv</code> is still confusing me.</p>

#### [ Johan Commelin (Aug 07 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131038649):
<p><code>conv in (λ _, _)</code> gives an error:</p>
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">mk_pattern</span><span class="o">,</span> <span class="bp">#</span><span class="mi">1</span> <span class="n">expr</span> <span class="kn">parameter</span> <span class="n">does</span> <span class="n">not</span> <span class="n">occur</span> <span class="k">in</span> <span class="n">the</span> <span class="n">target</span> <span class="n">or</span> <span class="o">(</span><span class="n">other</span><span class="o">)</span> <span class="n">expr</span> <span class="kn">parameter</span> <span class="n">types</span>
<span class="n">state</span><span class="o">:</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">Prime</span><span class="o">,</span>
<span class="n">n</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">eval₂</span> <span class="n">C</span> <span class="n">witt_polynomial</span> <span class="o">(</span><span class="n">X_in_terms_of_W</span> <span class="n">m</span><span class="o">)</span> <span class="bp">=</span> <span class="n">X</span> <span class="n">m</span>
<span class="err">⊢</span> <span class="n">witt_polynomial</span> <span class="n">n</span> <span class="bp">=</span>
      <span class="n">C</span> <span class="o">(</span><span class="err">↑</span><span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="bp">*</span> <span class="n">X</span> <span class="n">n</span> <span class="bp">+</span>
        <span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span>
          <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">),</span>
             <span class="n">eval₂</span> <span class="n">C</span> <span class="n">witt_polynomial</span> <span class="o">(</span><span class="n">C</span> <span class="err">↑</span><span class="n">p</span> <span class="err">^</span> <span class="n">x</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="bp">*</span>
               <span class="n">eval₂</span> <span class="n">C</span> <span class="n">witt_polynomial</span> <span class="o">(</span><span class="n">X_in_terms_of_W</span> <span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">x</span><span class="bp">.</span><span class="n">val</span><span class="o">)))</span> <span class="bp">=</span>
    <span class="err">?</span><span class="n">m_1</span>
</pre></div>

#### [ Johan Commelin (Aug 07 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131038700):
<p>But there is clearly a lambda in there...</p>

#### [ Johan Commelin (Aug 07 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131039097):
<p>Ok, I navigated to the lambda by hand.</p>

#### [ Johan Commelin (Aug 07 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131039113):
<p>Then I did some rewrites using ring homomorphisms, but Lean couldn't find an instance for them, nor for some rings.</p>

#### [ Johan Commelin (Aug 07 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131039123):
<p>Outside the <code>conv</code>, Lean found those instances without any trouble.</p>

#### [ Johan Commelin (Aug 07 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131039128):
<p>Is this a known issue?</p>

#### [ Kevin Buzzard (Aug 07 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131041397):
<p>I have this gut feeling that I've gone from never using <code>conv</code> (because I had no idea how it worked or what it did, before Patrick and I pushed the experts to explain it and then Patrick wrote <code>conv.md</code>) to over-using it. I tend to use it to do rewrites under a lambda -- but remember that <code>simp</code> does this too, so perhaps <code>simp only</code> will do what you're trying to do without having to use <code>conv</code>. One problem with <code>conv</code> is that if you're trying to find <code>f x = g x</code> in some <code>lam x, f x = g x</code> then <code>conv</code> won't match <code>f x</code> because it complains it doesn't know what <code>x</code> is. I don't know what your problem is but I look at pretty much every Lean function and it's some sort of lambda, so trying to match a lambda with so many holes sounds a bit scary to me, and trying to fill in the holes also looks hard for the reason I just mentioned above. Will <code>simp</code> not work for you?</p>

#### [ Johan Commelin (Aug 07 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131041784):
<p>"I worked my way around it..."</p>

#### [ Johan Commelin (Aug 07 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042169):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I have the feeling that I can not extract sublemmas for this proof. Yet I'm constantly plagued with deterministic timeouts. <a href="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L108" target="_blank" title="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L108">https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L108</a></p>

#### [ Johan Commelin (Aug 07 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042206):
<p>I fought the mess (and the mess won)</p>

#### [ Mario Carneiro (Aug 07 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042285):
<p>I wanted to ask: why are you using a <code>finset.univ.sum</code> over <code>fin n</code> when the function to sum over does not depend on the assumption <code>x.2</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042296):
<p>It would be much easier to use <code>(finset.range n).sum (\lam x, ...)</code></p>

#### [ Johan Commelin (Aug 07 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042395):
<p>Ok. The answer is: I've never used <code>finset.range</code> before, and didn't know about it.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042772):
<p>deterministic time-outs usually mean that you've made a mistake in your code and Lean, instead of saying "look an error", is trying to coerce an int into a nat or something else that it can't do but is unfortunately bad at spotting that it can't do.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042792):
<p>bad coercions, and trying to prove things which aren't refl by refl, are sometimes the cause</p>

#### [ Kevin Buzzard (Aug 07 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042797):
<p>(even if they look refl)</p>

#### [ Johan Commelin (Aug 07 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042913):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Ok, in the definition after the <code>witt_polynomial</code> I am using <code>i.2</code>.</p>

#### [ Johan Commelin (Aug 07 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042956):
<p>So now I need some hackery to make that recursive definition work.</p>

#### [ Mario Carneiro (Aug 07 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131042975):
<p>I see that... I'm working on the hackery</p>

#### [ Mario Carneiro (Aug 07 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131043298):
<p>This should get you started:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">range_sum_eq_fin_univ_sum</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">show</span> <span class="bp">_</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">multiset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">α</span> <span class="bp">_</span> <span class="err">↑</span><span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">map</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">),</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">map_pmap</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">pmap_eq_map</span><span class="o">]</span><span class="bp">;</span> <span class="n">refl</span>

<span class="n">def</span> <span class="n">witt_polynomial</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">R</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="o">(</span><span class="n">C</span> <span class="n">p</span> <span class="err">^</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">X</span> <span class="n">i</span> <span class="err">^</span> <span class="o">(</span><span class="n">p</span><span class="err">^</span><span class="o">(</span><span class="n">n</span><span class="bp">-</span><span class="n">i</span><span class="o">))))</span>

<span class="n">def</span> <span class="n">X_in_terms_of_W</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">:=</span> <span class="o">(</span><span class="n">X</span> <span class="n">n</span> <span class="bp">-</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">,</span>
  <span class="k">have</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">i</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="o">(</span><span class="n">C</span> <span class="n">p</span><span class="err">^</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span> <span class="bp">*</span> <span class="o">(</span><span class="n">X_in_terms_of_W</span> <span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span><span class="err">^</span><span class="o">(</span><span class="n">p</span><span class="err">^</span><span class="o">(</span><span class="n">n</span><span class="bp">-</span><span class="n">i</span><span class="bp">.</span><span class="n">val</span><span class="o">))))))</span> <span class="bp">*</span> <span class="n">C</span> <span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="n">p</span><span class="err">^</span><span class="n">n</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">X_in_terms_of_W_eq</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">X_in_terms_of_W</span> <span class="n">n</span> <span class="bp">=</span>
    <span class="o">(</span><span class="n">X</span> <span class="n">n</span> <span class="bp">-</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">C</span> <span class="n">p</span> <span class="err">^</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">X_in_terms_of_W</span> <span class="n">i</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">i</span><span class="o">)))</span> <span class="bp">*</span>
      <span class="n">C</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="err">↑</span><span class="n">p</span> <span class="err">^</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">X_in_terms_of_W</span><span class="o">,</span> <span class="n">range_sum_eq_fin_univ_sum</span><span class="o">]</span>
</pre></div>

#### [ Mario Carneiro (Aug 07 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131043305):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Hey look, a nontrivial equation lemma</p>

#### [ Johan Commelin (Aug 07 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131043423):
<p>Thanks!</p>

#### [ Johan Commelin (Aug 07 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131043492):
<p>That's a really sweet example of equation lemma hackery!</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046126):
<p><code>finset.sum finset.univ (λ i : fin (n+1), (C p^i.val * (X i.val)^(p^(n-i.val))))</code></p>
<p>Is this really still the best way to sum from 0 to n? It's the constant mentioning of <code>.val</code> which is a bit irritating. Is there some big operator or something which makes this better-looking?</p>

#### [ Chris Hughes (Aug 07 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046219):
<p>No, the best way is <code>(range (n+1)).sum ...</code></p>

#### [ Johan Commelin (Aug 07 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046245):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Mario suggested a better way. I'll push my current file.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046341):
<p>Oh yes I see the post now. I ignored it initially because I'd not even begun to look at the file, but I have WiFi for the next 10 minutes so I downloaded the version on GH and am now looking through it.</p>

#### [ Johan Commelin (Aug 07 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046344):
<p><a href="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L114" target="_blank" title="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L114">https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L114</a></p>

#### [ Johan Commelin (Aug 07 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046356):
<p>Ok, make sure you download again (-;</p>

#### [ Johan Commelin (Aug 07 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046430):
<p>I've all sorts of rewrites that are failing, and it is beyond me why they fail...</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046616):
<p>I see! Range is nice to look at, but summing over <code>fin n</code> is cool because <code>i.2</code> is exactly what you need to make the equation compiler swallow it. Then you switch back to get the equation lemma you really want.</p>

#### [ Johan Commelin (Aug 07 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046705):
<p>Yes. Pretty cool stuff, right? Kudos to Mario.</p>

#### [ Johan Commelin (Aug 07 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046716):
<p>I feel I've made progress today.</p>

#### [ Johan Commelin (Aug 07 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046727):
<p>But the proof is still extremely slow. And it is fragile beyond imagination.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046820):
<p>on line 135 or so you have two different <code>n</code>'s.</p>

#### [ Mario Carneiro (Aug 07 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046849):
<p>that's from the first two lines. You can ignore the first <code>n</code> after the first line</p>

#### [ Johan Commelin (Aug 07 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046851):
<p>Yes, I don't know why <code>strong_induction</code> introduces a new <code>n</code></p>

#### [ Johan Commelin (Aug 07 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131046859):
<p>I'll clear the first one</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047007):
<p>Inserting <code>repeat {sorry},end #exit</code> on line 124 and the proof still takes forever to compile (a second or two). I can't work with Lean when it's like this. Something you're doing is taking far longer than it should, and rather than biting the bullet nowadays I try to fix it.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047028):
<p>It's line 119</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047040):
<p><code>  simp only [eval₂_mul, eval₂_add, eval₂_sub, eval₂_neg, eval₂_C, eval₂_X],</code></p>

#### [ Johan Commelin (Aug 07 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047098):
<p>How do you figure out which line it is?</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047100):
<p><code>elaboration: tactic execution took 3.44s</code>.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047112):
<p>I just keep cutting and pasting <code>repeat {sorry}, end #exit</code> higher and higher up the file until I find it</p>

#### [ Kevin Buzzard (Aug 07 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047125):
<p>Nowadays when I write Lean code I notice it straight away and deal with the problem when it appears.</p>

#### [ Johan Commelin (Aug 07 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047143):
<p>Ok... so somehow I need to speed up that line...</p>

#### [ Johan Commelin (Aug 07 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047196):
<p>In mathspeak it says that the <code>eval2</code> is a ring homomorphism, and that it therefore commutes with mul and add.</p>

#### [ Johan Commelin (Aug 07 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047210):
<p>And thus the ring hom can be moved "inside".</p>

#### [ Johan Commelin (Aug 07 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047369):
<div class="codehilite"><pre><span></span>  <span class="n">rw</span> <span class="o">[</span><span class="n">eval₂_mul</span><span class="o">,</span> <span class="n">eval₂_C</span><span class="o">],</span>
  <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">eval₂_sub</span><span class="o">],</span>
  <span class="n">rw</span> <span class="n">eval₂_X</span><span class="o">,</span>
</pre></div>

#### [ Johan Commelin (Aug 07 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131047376):
<p>Somehow <code>simp only</code> succeeds, while <code>rw</code> doesn't...</p>

#### [ Johan Commelin (Aug 07 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050069):
<p>Ok, it is still really ugly... but progress: <a href="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L115" target="_blank" title="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L115">https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L115</a></p>

#### [ Johan Commelin (Aug 07 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050137):
<p>Now I need <code>i.property</code> but I no longer have access to it <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Johan Commelin (Aug 07 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050148):
<p>And the proof is still relatively slow.</p>

#### [ Johan Commelin (Aug 07 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050156):
<p>Anyway, I need to go home now. See you later!</p>

#### [ Mario Carneiro (Aug 07 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131050849):
<p>After lots of testing, I think I know the problem: <code>eval₂_*</code> is a bad simp lemma, not because it is written incorrectly, but because it is too expensive to instantiate. It takes a second or so to figure out if one of these rules even applies, and simp has to go through tons of them at all parts of the expression</p>

#### [ Kevin Buzzard (Aug 07 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131051808):
<p>I've just been dropping these <code>sorry,end #exit</code> lines in near the beginning and even the rewrites are taking time. <code>simp only [eval₂_sub]</code> seems to take about 200ms but <code>rw @eval₂_sub _ _ _ _ _ _ (X n) (finset.sum (finset.range n) (λ (i : ℕ), C ↑p ^ i * X_in_terms_of_W i ^ p ^ (n - i))) _ _ C _ witt_polynomial</code> also takes about 200ms</p>

#### [ Kevin Buzzard (Aug 07 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131051831):
<p>and then <code>rw eval₂_X</code> takes about 600ms</p>

#### [ Mario Carneiro (Aug 07 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131053242):
<p>For me the <code>eval2_sub</code> proof works provided I have the <code>foobar</code> instance:</p>
<div class="codehilite"><pre><span></span>instance foobar : comm_ring (mv_polynomial ℕ ℚ) := by apply_instance
</pre></div>

#### [ Kevin Buzzard (Aug 07 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054040):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">inst_2</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">inst_3</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">inst_4</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">inst_5</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">inst_6</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">ℚ</span> <span class="bp">→</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span><span class="o">))</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="kn">lemma</span> <span class="n">X_in_terms_of_W_prop</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">X_in_terms_of_W</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">eval₂</span> <span class="n">C</span> <span class="n">witt_polynomial</span> <span class="bp">=</span> <span class="n">X</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_induction_on</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">clear</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">n</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">X_in_terms_of_W_eq</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">eval₂_mul</span><span class="o">,</span> <span class="n">eval₂_C</span><span class="o">],</span>
  <span class="n">rw</span> <span class="bp">@</span><span class="n">eval₂_sub</span> <span class="n">ℚ</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">ℕ</span> <span class="n">inst_1</span> <span class="n">inst_2</span> <span class="n">inst_3</span>
    <span class="o">(</span><span class="n">X</span> <span class="n">n</span><span class="o">)</span>
    <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">C</span> <span class="err">↑</span><span class="n">p</span> <span class="err">^</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">X_in_terms_of_W</span> <span class="n">i</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">i</span><span class="o">)))</span>
    <span class="n">inst_4</span> <span class="n">inst_5</span> <span class="n">C</span> <span class="n">inst_6</span> <span class="n">witt_polynomial</span><span class="o">,</span>
  <span class="n">sorry</span><span class="o">,</span><span class="kn">end</span> <span class="bp">#</span><span class="kn">exit</span>
</pre></div>


<p>That last rw is taking 150ms. Is that a long time for a rewrite?</p>

#### [ Kevin Buzzard (Aug 07 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054089):
<p>I filled in every field.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054347):
<p>and <code>rw @eval₂_X ℚ (mv_polynomial ℕ ℚ) ℕ inst_1 inst_2 inst_3' inst_4' C inst_5' witt_polynomial n</code> (the line after) is taking over 300ms.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054427):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">inst_3&#39;</span> <span class="o">:</span> <span class="n">comm_semiring</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">inst_4&#39;</span> <span class="o">:</span> <span class="n">comm_semiring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">inst_5&#39;</span> <span class="o">:</span> <span class="n">is_semiring_hom</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">ℚ</span> <span class="bp">→</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span><span class="o">))</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>


<p>I thought that <code>rw</code> looked at the head of the expression, and it's not hard to find <code>eval_2</code>, there's only two possibilities, and one of them fits perfectly. I don't understand why these rewrites are taking so long.</p>

#### [ Johan Commelin (Aug 07 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054652):
<p>That's exactly what I was thinking.</p>

#### [ Mario Carneiro (Aug 07 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054696):
<p>By the way, in the expression <code>(X_in_terms_of_W n).eval₂ C witt_polynomial = X n</code> are you aware that the <code>R</code> variable of <code>witt_polynomial</code> is instantiated as <code>Q</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131054768):
<p>if you try to assert that it has type <code>mv_polynomial ℕ R</code> it doesn't typecheck</p>

#### [ Mario Carneiro (Aug 07 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131055665):
<p>Oh wow, this has a 1000% improvement in speed:</p>
<div class="codehilite"><pre><span></span>generalize e : eval₂ C witt_polynomial = f,
haveI : is_ring_hom f := by subst f; apply eval₂.is_ring_hom,
</pre></div>


<p>Most of the proof only uses that <code>f</code> is a ring hom. For the rest, you can use the equality to recover the eval</p>

#### [ Johan Commelin (Aug 07 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131056663):
<p>Mario, yes, I was aware of that. In the end, we want some identity over <code>\Z</code>. I only wrote the general definition of <code>witt_polynomial</code> so that I didn't constantly have to <code>map</code> them to other rings.</p>

#### [ Johan Commelin (Aug 07 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131056734):
<p>Ok, so I put that bit of code somewhere in the beginning of my proof? And then I get massive speedups, and afterwards it is recovered/unfolded towards the end?</p>

#### [ Johan Commelin (Aug 07 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131058032):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Does your suggestion classify as best practice or is it a fragile hack? Is this a sign that we need to improve <code>eval2</code>, or is there nothing to worry about?</p>

#### [ Mario Carneiro (Aug 08 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131082758):
<p>It is a hack, although not that fragile, it's just a weird workaround for inexplicable slowdown</p>

#### [ Mario Carneiro (Aug 08 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131082897):
<p>I found another weird way to speed things up:</p>
<div class="codehilite"><pre><span></span>set_option profiler true

instance eval_witt_hom : is_ring_hom (eval₂ C (witt_polynomial R)) :=
@mv_polynomial.eval₂.is_ring_hom _ _ _ _ _ _ _ _ _
  (@C.is_ring_hom R ℕ _ (λ a b, _inst_2 a b) _) _

lemma X_in_terms_of_W_prop (n : ℕ) : (X_in_terms_of_W n).eval₂ C (witt_polynomial ℚ) = X n :=
begin
  apply nat.strong_induction_on n,
  intros n H,
  rw [X_in_terms_of_W_eq],
  simp,
end
</pre></div>


<p>the <code>simp</code> application runs fine as long as you have that instance. The elaboration of <code>eval_witt_hom</code> takes about 500 ms written like this, but if I write <code>_inst_2</code> instead of eta expanded, elaboration jumps to 8.3 s. If I use <code>by apply_instance</code> it takes about 1 s</p>

#### [ Mario Carneiro (Aug 08 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131082996):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> This stuff is closer to your area of expertise than mine, although I am not sure how easy it is to separate mathlib from this issue</p>

#### [ Mario Carneiro (Aug 08 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131087058):
<p>Okay, here's a complete proof with no unreasonable slowdowns:</p>
<div class="codehilite"><pre><span></span>instance eval_witt_hom : is_ring_hom (eval₂ C (witt_polynomial R)) :=
@mv_polynomial.eval₂.is_ring_hom _ _ _ _ _ _ _ _ _
  (@C.is_ring_hom R ℕ _ (λ a b, _inst_2 a b) _) _

lemma X_in_terms_of_W_prop&#39;
  (f : mv_polynomial ℕ ℚ → mv_polynomial ℕ ℚ) [is_ring_hom f]
  (fC : ∀ (a : ℚ), f (C a) = C a)
  (fX : ∀ (n : ℕ), f (X n) = witt_polynomial ℚ n)
  (n : ℕ) : f (X_in_terms_of_W n) = X n :=
begin
  apply nat.strong_induction_on n,
  clear n, intros n H,
  rw [X_in_terms_of_W_eq],
  simp only [is_ring_hom.map_mul f, is_ring_hom.map_sub f, fC, fX, ring_hom_sum.finset f],
  rw [finset.sum_congr rfl, (_ : witt_polynomial ℚ n -
    (finset.range n).sum (λ i, C p ^ i * X i ^ p ^ (n - i)) = C (p ^ n) * X n)],
  { rw [mul_right_comm, ← C_mul, mul_one_div_cancel, C_1, one_mul],
    exact pow_ne_zero _ (nat.cast_ne_zero.2 $ ne_of_gt pp.pos) },
  { simp [witt_polynomial, nat.sub_self],
    rw ring_hom_powers (@C ℚ ℕ _ _ _) },
  { intros i h,
    simp [is_ring_hom.map_mul f, ring_hom_powers f, fC] at h ⊢,
    rw H _ h }
end

lemma X_in_terms_of_W_prop (n : ℕ) : (X_in_terms_of_W n).eval₂ C (witt_polynomial ℚ) = X n :=
begin
  letI : is_ring_hom (@C ℚ ℕ _ _ _) := by apply_instance,
  haveI H := @eval_witt_hom _ ℚ _ _,
  have fC := eval₂_C C (witt_polynomial ℚ),
  have fX := eval₂_X C (witt_polynomial ℚ),
  revert H fC fX, generalize : eval₂ C (witt_polynomial ℚ) = f,
  introsI, exact X_in_terms_of_W_prop&#39; f fC fX n
end
</pre></div>

#### [ Johan Commelin (Aug 08 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131088141):
<p>Wow! Thanks for your help Mario! I wouldn't have been able to come up with this myself.</p>

#### [ Johan Commelin (Aug 08 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131088204):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is it ok that your proof explicitly mentions <code>_inst_2</code>? I always assumed that was "forbidden".</p>

#### [ Mario Carneiro (Aug 08 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131088256):
<p>You should see if <code>λ a b, by apply_instance</code> also works without slowdown. If not, you can just name the instance and refer to it</p>

#### [ Johan Commelin (Aug 08 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131088298):
<p>Ok, I'll merge this into my file as soon as I'm back at work.</p>

#### [ Johan Commelin (Aug 08 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131091024):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> You also changed the definition of <code>witt_polynomial</code> to make the ring <code>R</code> explicit, didn't you?</p>

#### [ Mario Carneiro (Aug 08 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131091040):
<p>I did, it was making things a bit confusing. You don't have to</p>

#### [ Johan Commelin (Aug 08 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131092231):
<p>Is there a way to tease more information out of Lean when it gives the error <code>command expected</code>?</p>

#### [ Mario Carneiro (Aug 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131092296):
<p>that means that the parser was reset, you are between definitions or something, and you give a non-keyword</p>

#### [ Mario Carneiro (Aug 08 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131092301):
<p>Or it means you have <code>checking visible lines</code> mode enabled and you should scroll down to refresh the parser</p>

#### [ Johan Commelin (Aug 08 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131092457):
<p>I see... a very descriptive error message <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Kevin Buzzard (Aug 08 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131095998):
<blockquote>
<p>Or it means you have <code>checking visible lines</code> mode enabled and you should scroll down to refresh the parser</p>
</blockquote>
<p>Johan -- we're talking about the little message in the blue bar at the bottom of the VS Code window which says something like "checking visible lines and above". I constantly refer to this as "evil mode" and it used to be the case that whenever I see a student whose blue bar said this, I would tell them to click on the blue bar and change it to "checking visible files". There is a place for the "visible lines and above" choice, but for my users it causes more trouble than it solves, because it means that sometimes the answer to "there's a red line -- what is wrong with my code?" is "nothing is wrong with your code, it's just that Lean isn't reading all of it". Nowadays I just show my students how to make it say "checking visible files" by selecting File-&gt;Preferences-&gt;Settings (ctrl-, on linux), then searching for <code>linesandabove</code> in the default user settings, hovering over <code>"lean.roiModeDefault": "linesAndAbove"</code> (if it says that -- you want it to say <code>visible</code>, clicking the little pencil just to the left of it [thus moving the variable into the part of the settings which you can edit], and then making sure it says <code>"lean.roiModeDefault": "visible"</code> in user settings.</p>

#### [ Gabriel Ebner (Aug 08 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131096086):
<blockquote>
<p>Nowadays I just show my students how to make it say "checking visible files"</p>
</blockquote>
<p>BTW, this is the default now.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131096702):
<p>Thanks for switching it back Gabriel. It's fine if you know what you're doing, but experience indicated that it was confusing for new users. I love the way that you just sit there in the background occasionally making things better for me.</p>

#### [ Johan Commelin (Aug 08 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131097020):
<p>Thanks for the explanation Kevin!</p>

#### [ Johan Commelin (Aug 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101387):
<p>Aaaaahrg. I'm completely stuck again!</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">quux</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">A</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">n</span> <span class="bp">+</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>

<span class="kn">lemma</span> <span class="n">X_in_terms_of_W_prop₂</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">witt_polynomial</span> <span class="n">k</span><span class="o">)</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X_in_terms_of_W</span> <span class="bp">=</span> <span class="n">X</span> <span class="n">k</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_induction_on</span> <span class="n">k</span><span class="o">,</span>
  <span class="n">clear</span> <span class="n">k</span><span class="o">,</span> <span class="n">intros</span> <span class="n">k</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="n">only</span> <span class="o">[</span><span class="n">witt_polynomial</span><span class="o">],</span>
  <span class="n">conv</span>
  <span class="k">begin</span>
    <span class="n">to_lhs</span><span class="o">,</span>
    <span class="n">congr</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">quux</span> <span class="n">k</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">C</span> <span class="err">↑</span><span class="n">p</span> <span class="err">^</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">X</span> <span class="n">i</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">k</span> <span class="bp">-</span> <span class="n">i</span><span class="o">)),</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="c1">-- generalize e : eval X_in_terms_of_W = f,</span>
  <span class="c1">-- haveI : is_ring_hom f := by subst f; apply eval.is_ring_hom,</span>
  <span class="c1">-- simp only [ring_hom_sum.finset f],</span>
  <span class="c1">-- repeat {sorry}, end #exit</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Aug 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101390):
<p>Yesterday's trick isn't working.</p>

#### [ Johan Commelin (Aug 08 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101554):
<p><del>After this sorry is removed, I think we are mostly good to go for the definition of witt vectors.</del> Meh... I forgot that I still need to convince Lean that I actually get a polynomial over <code>\Z</code> instead of <code>\Q</code>.</p>

#### [ Johan Commelin (Aug 08 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101563):
<p>But maybe we first need to figure out why Lean is misbehaving like a toddler...</p>

#### [ Johan Commelin (Aug 08 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131101710):
<p>I pushed the stuff that I have right now: <a href="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L135" target="_blank" title="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L135">https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L135</a></p>

#### [ Johan Commelin (Aug 08 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131102445):
<p>Ok, so I have polynomials over <code>\Q</code>, but actually all their coefficients lie in <code>\Z</code>. What is the best way to extract this polynomial over <code>\Z</code>? I currently have the following:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">witt_structure_int</span> <span class="o">(</span><span class="err">Φ</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="n">bool</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">bool</span> <span class="bp">×</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span> <span class="n">rat</span><span class="bp">.</span><span class="n">num</span> <span class="o">(</span><span class="n">rat</span><span class="bp">.</span><span class="n">coe_int_num</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">witt_structure_rat</span> <span class="o">(</span><span class="n">map</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast</span> <span class="err">Φ</span><span class="o">)</span> <span class="n">n</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Aug 08 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131103604):
<p>Your rewrite on line 144 is, for me, trying to rewrite when the goal is <code>| X_in_terms_of_W</code>. But if I add another <code>skip</code> then I see Lean trying to do this:</p>
<div class="codehilite"><pre><span></span>_inst_1 : nat.Prime,
k : ℕ,
H : ∀ (m : ℕ), m &lt; k → eval₂ C X_in_terms_of_W (witt_polynomial m) = X m
| finset.sum (finset.range (k + 1)) (λ (i : ℕ), C ↑p ^ i * X i ^ p ^ (k - i))
scratch6.lean:145:4: error

rewrite tactic failed, did not find instance of the pattern in the target expression
  finset.sum (finset.range (k + 1)) (λ (i : ℕ), C ↑p ^ i * X i ^ p ^ (k - i))
state:
10 goals
_inst_1 : nat.Prime,
k : ℕ,
H : ∀ (m : ℕ), m &lt; k → eval₂ C X_in_terms_of_W (witt_polynomial m) = X m
⊢ finset.sum (finset.range (k + 1)) (λ (i : ℕ), C ↑p ^ i * X i ^ p ^ (k - i)) = ?m_1
</pre></div>


<p>But when you <code>set_option pp.all true</code> I see a whole bunch of typeclass inference stuff which doesn't look like it matches up. The thing you're trying to rewrite has a whole bunch of unsolved metavariables. Your goal looks like this: </p>
<div class="codehilite"><pre><span></span> (@finset.sum.{0 0} nat
       (@mv_polynomial.{0 0} nat rat
...
</pre></div>


<p>and the thing you're trying to rewrite looks like this:</p>
<div class="codehilite"><pre><span></span>  @finset.sum.{0 ?l_1} nat (@mv_polynomial.{0 ?l_1} nat ?m_2 ?m_3) ...
</pre></div>


<p>Maybe if you are more precise with your rewrite it might help, i.e. throw in some <code>@</code>s and say exactly what the type of some more things are. I am kind of wondering whether the type class inference system doesn't know enough about what your types are, and is making some bad guesses about what instances it should use.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105049):
<p><a href="https://gist.github.com/kbuzzard/5254103e5f33b022636a9491fb6719e9" target="_blank" title="https://gist.github.com/kbuzzard/5254103e5f33b022636a9491fb6719e9">https://gist.github.com/kbuzzard/5254103e5f33b022636a9491fb6719e9</a></p>
<p>That's the beginning of the <code>set_option pp.all true</code> output. The <code>quux</code> thing is the thing at the top. The goal is the much longer thing at the bottom, most of which I've truncated. The much longer thing at the bottom corresponds to just the first three lines of the top. Lines 3 and 50 match perfectly. Lines 1 and 2 are supposed to match with lines 16 to 49. We have a universe metavariable <code>?l_1</code> which can be zero, then a term metavariable <code>?m_2</code> which can be <code>rat</code>. What I'm worried about is line 2, which says that type class inference wants to prove something is an add_comm_monoid, and it's going to do this by showing it's an add_comm_group and then it will use an instance called <code>add_comm_group.to_add_comm_monoid</code>. But lines 25 to 42 seem to be showing that the rationals are an add_comm_monoid by showing that they're a field, and then a comm_ring, and then a comm_semiring (note that we have now diverged from the plan, because a comm_semiring isn't an add_comm_group) and then an add_comm_monoid.</p>
<p>Now this might not be the problem, but somehow it looks to me like it <em>might</em> be an obstruction to the rewrite succeeding. Can you somehow tell Lean that you're not working with <code>?m_2</code> but with <code>rat</code>?</p>

#### [ Johan Commelin (Aug 08 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105249):
<p>Like so?</p>
<div class="codehilite"><pre><span></span><span class="n">rw</span> <span class="n">quux</span> <span class="n">k</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="o">((</span><span class="n">C</span> <span class="err">↑</span><span class="n">p</span> <span class="err">^</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">X</span> <span class="n">i</span> <span class="err">^</span> <span class="n">p</span> <span class="err">^</span> <span class="o">(</span><span class="n">k</span> <span class="bp">-</span> <span class="n">i</span><span class="o">))</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">ℚ</span><span class="o">)),</span>
</pre></div>


<p>Alas, that still fails.</p>

#### [ Johan Commelin (Aug 08 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105757):
<p>Hmm, now the output of <code>pp.all</code> shows an insane amount of similarities between the goal and what the rewrite offers.</p>

#### [ Johan Commelin (Aug 08 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105807):
<p>But it is not enough. The <code>rw</code> is using modules <span class="emoji emoji-1f631" title="scream">:scream:</span> whereas the goal is sane, and just works with rings.</p>

#### [ Kevin Buzzard (Aug 08 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131105895):
<p>What you're trying to rewrite: <a href="https://gist.github.com/kbuzzard/8b4048c89309808fe829c5e59caaa503" target="_blank" title="https://gist.github.com/kbuzzard/8b4048c89309808fe829c5e59caaa503">https://gist.github.com/kbuzzard/8b4048c89309808fe829c5e59caaa503</a></p>
<p>Goal: <a href="https://gist.github.com/kbuzzard/f515877383946b5eb84f03e31cb988c3" target="_blank" title="https://gist.github.com/kbuzzard/f515877383946b5eb84f03e31cb988c3">https://gist.github.com/kbuzzard/f515877383946b5eb84f03e31cb988c3</a></p>
<p>They're not the same. The question perhaps is which differences are superficial and which ones are stopping the rewrite</p>

#### [ Johan Commelin (Aug 08 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131106029):
<p>I'm scared by <a href="https://gist.github.com/kbuzzard/8b4048c89309808fe829c5e59caaa503#file-pattern-lean-L21" target="_blank" title="https://gist.github.com/kbuzzard/8b4048c89309808fe829c5e59caaa503#file-pattern-lean-L21">https://gist.github.com/kbuzzard/8b4048c89309808fe829c5e59caaa503#file-pattern-lean-L21</a></p>

#### [ Johan Commelin (Aug 08 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131106164):
<p>Sorry!!! I messed up. I did not have enough <code>skip</code>s in the <code>conv</code>. <span class="emoji emoji-1f62d" title="sob">:sob:</span></p>

#### [ Kevin Buzzard (Aug 08 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131106990):
<p>Didn't I mention that? ;-)</p>

#### [ Johan Commelin (Aug 08 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108053):
<p>Hmmm, it seems to me that whenever I make any progress using <code>simp</code> or <code>dsimp</code>, afterwards everything breaks, because it cleans up to much.</p>

#### [ Johan Commelin (Aug 08 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108058):
<p>So I find my self doing long chains of <code>rw</code>s</p>

#### [ Johan Commelin (Aug 08 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108116):
<p>And now I have <code>(\lam i, f i) i</code>. And I need <code>f i</code>. How do I do that without <code>dsimp</code>?</p>

#### [ Johan Commelin (Aug 08 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108302):
<p>Ok, so I think this is called beta-reduction. Is there a tactic that will do beta-reduction, and nothing else?</p>

#### [ Johan Commelin (Aug 08 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108886):
<p>Ok! "I worked my way around it."</p>

#### [ Johan Commelin (Aug 08 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108907):
<p>All sorries are gone in this part! <span class="emoji emoji-1f419" title="octopus">:octopus:</span></p>

#### [ Johan Commelin (Aug 08 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108917):
<p>Now I need to figure out how to get some polynomials that are defined over Q to believe that they actually live over Z.</p>

#### [ Johan Commelin (Aug 08 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131108918):
<p><a href="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L218" target="_blank" title="https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L218">https://github.com/jcommelin/mathlib/blob/witt/algebra/witt_vector.lean#L218</a></p>

#### [ Patrick Massot (Aug 08 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109022):
<p>You can have a look at <a href="https://github.com/leanprover/lean/blob/28f4143be31b7aa3c63a907be5443ca100025ef1/library/init/meta/simp_tactic.lean#L71" target="_blank" title="https://github.com/leanprover/lean/blob/28f4143be31b7aa3c63a907be5443ca100025ef1/library/init/meta/simp_tactic.lean#L71">https://github.com/leanprover/lean/blob/28f4143be31b7aa3c63a907be5443ca100025ef1/library/init/meta/simp_tactic.lean#L71</a></p>

#### [ Patrick Massot (Aug 08 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109042):
<p>turning off everything but beta</p>

#### [ Kenny Lau (Aug 08 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109241):
<p>I think you only need to specify that beta is turned on</p>

#### [ Kenny Lau (Aug 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109276):
<p>but I'm not sure</p>

#### [ Patrick Massot (Aug 08 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/witt%20vectors/near/131109373):
<p>I think we could have a tactic doing only this and unfolding composition (ie <code>rw comp_app</code>)</p>


{% endraw %}
