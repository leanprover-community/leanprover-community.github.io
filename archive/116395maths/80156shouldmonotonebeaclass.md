---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/80156shouldmonotonebeaclass.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [should monotone be a class?](https://leanprover-community.github.io/archive/116395maths/80156shouldmonotonebeaclass.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (May 28 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127196629):
<p>Should</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">monotone</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span><span class="o">⦃</span><span class="n">a</span> <span class="n">b</span><span class="o">⦄,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">b</span>
</pre></div>


<p>be a class? I need compositions of these guys (and then applying a functor to them)...</p>

#### [ Johan Commelin (May 28 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127196637):
<p>I wouldn't mind if the type class inference system helped me a bit (-;</p>

#### [ Johan Commelin (May 28 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127196644):
<p>Ooh, this is line 37 of <code>order/basic.lean</code></p>

#### [ Andrew Ashworth (May 28 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127196934):
<p>would type class inference even help? don't you just need a lemma that says the composition of two monotonically increasing functions is also monotonic?</p>

#### [ Johan Commelin (May 28 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127197054):
<p>That exists. But now I need to explicitly refer to it every time I use functoriality</p>

#### [ Johan Commelin (May 28 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127197061):
<p>I'dd rather just have that transparently dealt with by Lean</p>

#### [ Andrew Ashworth (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127197325):
<p>ahhh. I'm surprised you would reach for type class inference in this case, it's not my first choice. I would try parameters in sections, auto params, and figuring out how to write a mini tactic or helper lemma as well</p>

#### [ Johan Commelin (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198037):
<p>Ok, I don't really understand what you mean.</p>

#### [ Johan Commelin (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198050):
<p>I have proved that the simplicial complex is a complex, up to 1 sorry: <a href="https://github.com/jcommelin/mathlib/blob/simplicial/algebraic_topology/simplicial_set.lean#L15-L22" target="_blank" title="https://github.com/jcommelin/mathlib/blob/simplicial/algebraic_topology/simplicial_set.lean#L15-L22">https://github.com/jcommelin/mathlib/blob/simplicial/algebraic_topology/simplicial_set.lean#L15-L22</a></p>

#### [ Johan Commelin (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198057):
<p>The only thing in that proof is pulling some identity through a functor</p>

#### [ Johan Commelin (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198061):
<p>I have no idea how to do that.</p>

#### [ Johan Commelin (May 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127198116):
<p>See <a href="https://github.com/jcommelin/mathlib/blob/simplicial/algebraic_topology/simplex_category.lean#L80" target="_blank" title="https://github.com/jcommelin/mathlib/blob/simplicial/algebraic_topology/simplex_category.lean#L80">https://github.com/jcommelin/mathlib/blob/simplicial/algebraic_topology/simplex_category.lean#L80</a> for the corresponding identity in the source category.</p>

#### [ Johan Commelin (May 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202542):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">simplicial_set</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">objs</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
<span class="o">(</span><span class="n">maps</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="o">[</span><span class="n">m</span><span class="o">]</span> <span class="bp">→</span> <span class="o">[</span><span class="n">n</span><span class="o">]}</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">monotone</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">objs</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">objs</span> <span class="n">m</span><span class="o">)</span>
<span class="o">(</span><span class="n">comp</span> <span class="o">{</span><span class="n">l</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="o">[</span><span class="n">l</span><span class="o">]</span> <span class="bp">→</span> <span class="o">[</span><span class="n">m</span><span class="o">]}</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="o">[</span><span class="n">m</span><span class="o">]</span> <span class="bp">→</span> <span class="o">[</span><span class="n">n</span><span class="o">]}</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">monotone</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">hg</span> <span class="o">:</span> <span class="n">monotone</span> <span class="n">g</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">maps</span> <span class="n">hf</span><span class="o">)</span> <span class="err">∘</span> <span class="o">(</span><span class="n">maps</span> <span class="n">hg</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">maps</span> <span class="o">(</span><span class="n">monotone_comp</span> <span class="n">hf</span> <span class="n">hg</span><span class="o">)))</span>

<span class="kn">namespace</span> <span class="n">simplicial_set</span>
<span class="n">def</span> <span class="n">δ</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">simplicial_set</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">])</span> <span class="o">:=</span>
<span class="n">maps</span> <span class="o">(</span><span class="n">simplex_category</span><span class="bp">.</span><span class="n">δ_monotone</span> <span class="n">i</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">simplicial_identity₁</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">simplicial_set</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">])</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">@</span><span class="n">δ</span> <span class="n">X</span> <span class="n">n</span><span class="o">)</span> <span class="n">i</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">j</span><span class="bp">.</span><span class="n">succ</span> <span class="bp">=</span> <span class="n">δ</span> <span class="n">j</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">i</span><span class="bp">.</span><span class="n">raise</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">unfold</span> <span class="n">δ</span><span class="o">,</span>
<span class="n">rw</span> <span class="n">comp</span><span class="o">,</span>
<span class="n">rw</span> <span class="n">comp</span><span class="o">,</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (May 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202543):
<p>How do I remove the final sorry in my file?</p>

#### [ Johan Commelin (May 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202612):
<p>In <code>simplex_category.lean</code>, I have</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">simplicial_identity₁</span> <span class="o">(</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">])</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span><span class="o">)</span> <span class="o">:</span> <span class="n">δ</span> <span class="n">j</span><span class="bp">.</span><span class="n">succ</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">δ</span> <span class="n">i</span><span class="bp">.</span><span class="n">raise</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">j</span> <span class="o">:=</span> <span class="s2">&quot;long proof&quot;</span>
</pre></div>

#### [ Johan Commelin (May 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202623):
<p>I just want to pull this through <code>maps</code>, but I have no clue at all how to do it.</p>

#### [ Patrick Massot (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202700):
<p>I would need to get your files to try to help you</p>

#### [ Johan Commelin (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202716):
<p>I linked them a few posts up</p>

#### [ Johan Commelin (May 28 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202725):
<p>But generic pointers are also welcome</p>

#### [ Johan Commelin (May 28 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202927):
<p>Also, why does my state look like</p>
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="n">simplicial_set</span><span class="o">,</span>
<span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">),</span>
<span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span>
<span class="err">⊢</span> <span class="n">maps</span> <span class="bp">_</span> <span class="err">∘</span> <span class="n">maps</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">maps</span> <span class="bp">_</span> <span class="err">∘</span> <span class="n">maps</span> <span class="bp">_</span>
</pre></div>


<p>after I <code>unfold δ</code>?</p>

#### [ Johan Commelin (May 28 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202946):
<p>Why the underscores?</p>

#### [ Johan Commelin (May 28 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127202977):
<p>I expected something more useful, like <code>maps (simplex_category.δ_monotone i) ∘ maps (simplex_category ... etc</code></p>

#### [ Patrick Massot (May 28 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203036):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">simplicial_identity₁</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">simplicial_set</span><span class="o">}</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="o">[</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">])</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">@</span><span class="n">δ</span> <span class="n">X</span> <span class="n">n</span><span class="o">)</span> <span class="n">i</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">j</span><span class="bp">.</span><span class="n">succ</span> <span class="bp">=</span> <span class="n">δ</span> <span class="n">j</span> <span class="err">∘</span> <span class="n">δ</span> <span class="n">i</span><span class="bp">.</span><span class="n">raise</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">finish</span> <span class="o">[</span><span class="n">δ</span><span class="o">,</span> <span class="n">comp</span><span class="o">,</span> <span class="n">simplex_category</span><span class="bp">.</span><span class="n">simplicial_identity₁</span><span class="o">]</span>
</pre></div>

#### [ Johan Commelin (May 28 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203158):
<p>Brilliant!</p>

#### [ Johan Commelin (May 28 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203160):
<p>I need to understand <code>finish</code></p>

#### [ Johan Commelin (May 28 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203163):
<p>But this is awesome, thanks!</p>

#### [ Patrick Massot (May 28 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127203167):
<p>No! Don't try to understand it, it's magic!</p>

#### [ Mario Carneiro (May 28 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127218334):
<blockquote>
<p>Why the underscores?</p>
</blockquote>
<p>The only explicit arg in <code>maps</code> is <code>monotone f</code>, which is a proof. Lean hides proof arguments by default, but this makes it hard to understand these goals unless the <code>f</code> is explicit too</p>

#### [ Mario Carneiro (May 28 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127218337):
<p>You can enable proof printing with <code>set_option pp.proofs true</code></p>

#### [ Johan Commelin (May 28 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127218384):
<p>Ok, thanks for the explanation!</p>

#### [ Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222060):
<p>Johan, those <code>_</code>s used to really confuse me. Everyone has told you all the right things but let me tell you the stupid version</p>

#### [ Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222097):
<p>All proofs are the same</p>

#### [ Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222100):
<p>and are instantly forgotten</p>

#### [ Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222101):
<p>so don't even get names</p>

#### [ Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222104):
<p>and this is kind of good but kind of annoying</p>

#### [ Kevin Buzzard (May 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222108):
<p>because if you have a subtype, so a value and then a proof, it might well just get displayed as &lt;a,_&gt;</p>

#### [ Kevin Buzzard (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222119):
<p>and this is annoying because sometimes you want to change the goal to something defeq with show, so you cut and paste the output from the pretty printer and write "show &lt;the goal&gt;"</p>

#### [ Kevin Buzzard (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222120):
<p>and it doesn't work</p>

#### [ Mario Carneiro (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222121):
<p>it's not instantly forgotten</p>

#### [ Mario Carneiro (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222123):
<p>it's there, it's a term</p>

#### [ Kevin Buzzard (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222125):
<p>because Lean can't reconstruct the _s</p>

#### [ Kevin Buzzard (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222126):
<p>yes so Lean is only pretending it forgot</p>

#### [ Mario Carneiro (May 28 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222128):
<p>it's just a big and ugly term</p>

#### [ Kevin Buzzard (May 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222173):
<p>and if you set_option pp.proofs true</p>

#### [ Mario Carneiro (May 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222175):
<p>lean can reconstruct the _</p>

#### [ Kevin Buzzard (May 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222181):
<p>then you can see them all and cut and paste them all again</p>

#### [ Kevin Buzzard (May 28 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/should%20monotone%20be%20a%20class%3F/near/127222184):
<p>and it turns out sometimes they're really ugly and long</p>


{% endraw %}
