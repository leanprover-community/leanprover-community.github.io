---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/47597heckeoperator.html
---

## Stream: [kbb](https://leanprover-community.github.io/archive/141825kbb/index.html)
### Topic: [hecke operator](https://leanprover-community.github.io/archive/141825kbb/47597heckeoperator.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 14 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133964447):
<p>The next step would be to define <a href="https://en.wikipedia.org/wiki/Hecke_operator#Explicit_formula" target="_blank" title="https://en.wikipedia.org/wiki/Hecke_operator#Explicit_formula">https://en.wikipedia.org/wiki/Hecke_operator#Explicit_formula</a> on the subspace of <code>Petersson_weight k</code> functions on the upper half plane.</p>

#### [ Johan Commelin (Sep 14 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133964469):
<p>Afterwards, we need to show that it preserves <code>holomorphic</code>, <code>bounded_at_infinity</code> and <code>zero_at_infinity</code>.</p>

#### [ Johan Commelin (Sep 14 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133964474):
<p>We also need to prove that it is linear.</p>

#### [ Johan Commelin (Sep 14 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133972202):
<p>Ok, this stuff is a mess. I just wanted to plug a matrix with determinant <code>m</code> into the Möbius transform action. Of course that doesn't work...</p>

#### [ Kenny Lau (Sep 14 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133972741):
<p>wow this is really a heck of an operator</p>

#### [ Johan Commelin (Sep 14 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133973372):
<p>Ok, I think we should forget about Hecke operators. We can define them if we want. But we won't even get close to formalising the abstract of Kevin's paper.</p>

#### [ Johan Commelin (Sep 14 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133973393):
<p>Until 5 minutes ago, I thought that the only thing missing was the fact that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>S</mi><mi>k</mi></msub></mrow><annotation encoding="application/x-tex">S_k</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:-0.05764em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> is finite-dimensional (which requires Riemann–Roch).</p>

#### [ Johan Commelin (Sep 14 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133973470):
<p>But of course, with the definition of the Hecke operator that we are now going after, we will get a linear operator on a complex vector space. This beast will have a characteristic polynomial defined over <code>complex</code>.</p>

#### [ Johan Commelin (Sep 14 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/133973490):
<p>Such polynomials do not have very interesting splitting fields.</p>

#### [ Patrick Massot (Sep 15 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012391):
<p>How do you prove this polynomial has interesting coefficients in the real world?</p>

#### [ Reid Barton (Sep 15 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012447):
<p>are the coefficients actually rational?</p>

#### [ Patrick Massot (Sep 15 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012451):
<p>I guess there are integers</p>

#### [ Patrick Massot (Sep 15 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012458):
<p>But I know no number theory</p>

#### [ Patrick Massot (Sep 15 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012512):
<p>And it probably also requires Fourier series for modular forms</p>

#### [ Reid Barton (Sep 15 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012524):
<p>If they are actually integers, then can't we define the splitting field to be the smallest subfield of C which contains the roots?</p>

#### [ Johan Commelin (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012563):
<p>The Hecke operator acts on the singular homology of the modular curve. This has Q coeffients</p>

#### [ Reid Barton (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012567):
<p>Then we don't need either splitting fields or to prove that the coefficients are integers</p>

#### [ Johan Commelin (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012570):
<p>By Hodge theory you recover the cusp forms in the complexification of this cohomology group.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012574):
<p>But maybe I'm using a sledgehammer, there might be a more low-brow proof.</p>

#### [ Reid Barton (Sep 15 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012578):
<p>Of course then we wouldn't know that the this field is a finite extension...</p>

#### [ Johan Commelin (Sep 15 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012591):
<p>Right...</p>

#### [ Johan Commelin (Sep 15 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012594):
<p>Somehow I don't mind sorrying finite-dimensionality of S_k, but sorrying this fact feels like a big cheat.</p>

#### [ Patrick Massot (Sep 15 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012653):
<p>I guess Hecke's point of view was less sophisticated</p>

#### [ Johan Commelin (Sep 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012721):
<p>Probably. I think using Fourier coefficients there is another approach.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012733):
<p>But then, we didn't want to do Fourier coefficients either.</p>

#### [ Johan Commelin (Sep 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134012777):
<p>So maybe we just define the Hecke operator over <code>complex</code>, and then wrap up the project.</p>

#### [ Johan Commelin (Sep 18 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163084):
<p>Let's put this discussion in the correct thread.</p>

#### [ Johan Commelin (Sep 18 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163095):
<p>The following lemma is crucial:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">M_trans_SL2Z_H</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">{</span><span class="n">h</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">}</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="n">SL2Z</span><span class="o">}</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">}</span> <span class="o">:</span>
<span class="n">M_trans</span> <span class="n">h</span> <span class="o">(</span><span class="n">SL2Z_M</span> <span class="n">m</span> <span class="n">M</span> <span class="n">A</span><span class="o">)</span> <span class="bp">=</span> <span class="n">SL2Z_H</span> <span class="n">M</span> <span class="err">∘</span> <span class="o">(</span><span class="n">M_trans</span> <span class="n">h</span> <span class="n">A</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">funext</span> <span class="n">z</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">M_trans</span><span class="o">,</span> <span class="n">SL2Z_M</span><span class="o">,</span> <span class="n">SL2Z_H</span><span class="o">,</span> <span class="err">«</span><span class="n">M</span><span class="err">ö</span><span class="n">bius_transform</span><span class="err">»</span><span class="o">],</span>

<span class="c1">-- m : ℤ,</span>
<span class="c1">-- h : m &gt; 0,</span>
<span class="c1">-- M : SL2Z,</span>
<span class="c1">-- A : Mat m,</span>
<span class="c1">-- z : ↥ℍ</span>
<span class="c1">-- ⊢ (↑(M.a) * ↑(A.b) + (↑(M.b) * ↑(A.d) + (↑(M.a) * ↑(A.a) + ↑(M.b) * ↑(A.c)) * ↑z)) /</span>
<span class="c1">--       (↑(M.c) * ↑(A.b) + (↑(M.d) * ↑(A.d) + (↑(M.c) * ↑(A.a) + ↑(M.d) * ↑(A.c)) * ↑z)) =</span>
<span class="c1">--     (↑(M.b) + ↑(M.a) * ((↑(A.b) + ↑(A.a) * ↑z) / (↑(A.d) + ↑(A.c) * ↑z))) /</span>
<span class="c1">--       (↑(M.d) + ↑(M.c) * ((↑(A.b) + ↑(A.a) * ↑z) / (↑(A.d) + ↑(A.c) * ↑z)))</span>

  <span class="c1">-- ring, -- fails</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Sep 18 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163130):
<p>I'm not surprised that <code>ring</code> fails, because there are divisions. But boy, I really don't want to prove this stuff by hand.</p>

#### [ Patrick Massot (Sep 18 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163207):
<p>I could try since Johannes is working for me right now</p>

#### [ Patrick Massot (Sep 18 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163212):
<p>Did you push everything?</p>

#### [ Johannes Hölzl (Sep 18 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163237):
<p>Hm, isabelle has <code>field_simps</code> for these kind of things. <code>field_simps</code> is a collection which applies distributivity, and tries to remove the <code>x / d</code>. Sometimes it needs to introduces <code>if</code> to check if <code>d = 0</code></p>

#### [ Patrick Massot (Sep 18 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163272):
<p>We need this <em>so</em> badly</p>

#### [ Johan Commelin (Sep 18 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163669):
<p>I pushed some stuff</p>

#### [ Johan Commelin (Sep 18 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163689):
<p>I've got <code>M</code> out of <code>f</code>, so now we need to do the cocycle computation</p>

#### [ Johan Commelin (Sep 18 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163742):
<p>Which is just as ugly as the other thing I just posted.</p>

#### [ Patrick Massot (Sep 18 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134163769):
<p>Did you do the other ugly thing?</p>

#### [ Johan Commelin (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164244):
<p>No, everything I did was pushed.</p>

#### [ Johan Commelin (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164251):
<p>I went to the last sorry: proving that the result again has weight <code>k</code></p>

#### [ Johan Commelin (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164256):
<p>I now have the following goal</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on&#39;</span> <span class="n">o</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">),</span> <span class="mi">1</span> <span class="bp">/</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">A</span><span class="bp">.</span><span class="n">c</span><span class="o">)</span> <span class="bp">*</span> <span class="err">↑</span><span class="o">(</span><span class="n">SL2Z_H</span> <span class="n">M</span> <span class="n">z</span><span class="o">)</span> <span class="bp">+</span> <span class="err">↑</span><span class="o">(</span><span class="n">A</span><span class="bp">.</span><span class="n">d</span><span class="o">))</span> <span class="err">^</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span> <span class="n">f</span><span class="bp">.</span><span class="n">val</span> <span class="o">(</span><span class="n">M_trans</span> <span class="n">h</span> <span class="n">A</span> <span class="o">(</span><span class="n">SL2Z_H</span> <span class="n">M</span> <span class="n">z</span><span class="o">)))</span>
      <span class="bp">_</span> <span class="bp">=</span>
    <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">M</span><span class="bp">.</span><span class="n">c</span><span class="o">)</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">z</span> <span class="bp">+</span> <span class="err">↑</span><span class="o">(</span><span class="n">M</span><span class="bp">.</span><span class="n">d</span><span class="o">))</span> <span class="err">^</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span>
      <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on&#39;</span> <span class="n">o</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Mat</span> <span class="n">m</span><span class="o">),</span> <span class="mi">1</span> <span class="bp">/</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">A</span><span class="bp">.</span><span class="n">c</span><span class="o">)</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">z</span> <span class="bp">+</span> <span class="err">↑</span><span class="o">(</span><span class="n">A</span><span class="bp">.</span><span class="n">d</span><span class="o">))</span> <span class="err">^</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span> <span class="n">f</span><span class="bp">.</span><span class="n">val</span> <span class="o">(</span><span class="n">M_trans</span> <span class="n">h</span> <span class="n">A</span> <span class="n">z</span><span class="o">))</span> <span class="bp">_</span>
</pre></div>

#### [ Johan Commelin (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164263):
<p>How do I get past that <code>quotient.lift_on'</code>?</p>

#### [ Patrick Massot (Sep 18 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164264):
<p>I'm working on M_trans_SL2Z_H</p>

#### [ Johannes Hölzl (Sep 18 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164721):
<p>eliminate <code>o</code>. Easiest: <code>rcases o with &lt;x&gt;</code>.</p>

#### [ Johan Commelin (Sep 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164982):
<p>Thanks, that worked!</p>

#### [ Johan Commelin (Sep 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164990):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> The name is wrong. The final <code>_H</code> should be <code>_M</code>.</p>

#### [ Johan Commelin (Sep 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134164995):
<p>With <code>_H</code> it is another lemma, and I need that one now (-;</p>

#### [ Patrick Massot (Sep 18 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165060):
<p>but do you still want <code> {m : ℤ} {h : m &gt; 0} {M : SL2Z} {A : Mat m} : M_trans h (SL2Z_M m M A) = SL2Z_H M ∘ (M_trans h A)</code>?</p>

#### [ Patrick Massot (Sep 18 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165078):
<p>Or only the other one?</p>

#### [ Johan Commelin (Sep 18 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165198):
<p>No, the one you are working on is used</p>

#### [ Johan Commelin (Sep 18 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165204):
<p>I just realised that I had the wrong name.</p>

#### [ Johan Commelin (Sep 18 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165210):
<p>You can already see it being used</p>

#### [ Johan Commelin (Sep 18 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134165214):
<p>In what I last pushed</p>

#### [ Johan Commelin (Sep 18 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134166605):
<p>Aaahrg, the final sorry is a real pain. I'm now even confused about the maths again.</p>

#### [ Johan Commelin (Sep 18 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134166644):
<p>OTOH, those are the better moments of theorem proving (-; I'm rather confused about the maths than that I'm fight silly <code>↑</code></p>

#### [ Patrick Massot (Sep 18 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167046):
<p>I just pushed something</p>

#### [ Patrick Massot (Sep 18 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167084):
<p>Things are reduced to many variation on <a href="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L16" target="_blank" title="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L16">https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L16</a> which itself is a variation on <a href="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/upper_half_space.lean#L37" target="_blank" title="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/upper_half_space.lean#L37">https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/upper_half_space.lean#L37</a></p>

#### [ Patrick Massot (Sep 18 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167087):
<p>But I'm tired of fighting this</p>

#### [ Patrick Massot (Sep 18 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167137):
<p>After writing <a href="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L32-L49" target="_blank" title="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L32-L49">https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L32-L49</a></p>

#### [ Patrick Massot (Sep 18 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167150):
<p>One day we will think back and laugh. But right now it's only screaming: Lean is nowhere near ready!</p>

#### [ Johan Commelin (Sep 18 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167160):
<p>Right, it's really annoying</p>

#### [ Johan Commelin (Sep 18 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167368):
<p>I also pushed. I didn't really get very far.</p>

#### [ Patrick Massot (Sep 18 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167442):
<p>Maybe we can switch sides</p>

#### [ Johan Commelin (Sep 18 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167477):
<p>So, on my side that maths is confusing.</p>

#### [ Johan Commelin (Sep 18 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167510):
<p>If you take an <code>f</code> of weight <code>k</code>. After you plug it into Hecke, you want to check that the result has weight <code>k</code>.</p>

#### [ Johan Commelin (Sep 18 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167565):
<p>But this means that you get <code>f(A • M z)</code>, where <code>A : Mat m</code> and <code>M : SL2Z</code></p>

#### [ Johan Commelin (Sep 18 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167575):
<p>Now you can't use the weight property of <code>f</code>.</p>

#### [ Johan Commelin (Sep 18 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167579):
<p>Because the <code>M</code> is not on the left.</p>

#### [ Johan Commelin (Sep 18 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167618):
<p>But <code>A M A¯¹</code> doesn't have to be in <code>SL2Z</code>...</p>

#### [ Johan Commelin (Sep 18 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167622):
<p>So now I'm confused.</p>

#### [ Patrick Massot (Sep 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167681):
<p>M should be on the left</p>

#### [ Patrick Massot (Sep 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167699):
<p>We are acting from the left</p>

#### [ Patrick Massot (Sep 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167710):
<p>At least on my piece of paper</p>

#### [ Patrick Massot (Sep 18 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167717):
<p>And on Wikipedia</p>

#### [ Johan Commelin (Sep 18 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167915):
<p>Yes, but <code>M</code> acts before <code>A</code> does, right?</p>

#### [ Johan Commelin (Sep 18 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134167998):
<p>It is <code>f (A • (M • z))</code>. So <code>M</code> is in fact acting on the left.</p>

#### [ Reid Barton (Sep 18 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168094):
<p>Yeah you want to write <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi><mi>M</mi><mo>=</mo><mi>M</mi><msup><mi>A</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">AM = MA'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> for some other <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>A</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">A'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.751892em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> of det m, I think. The action of M will permute the terms of the sum</p>

#### [ Patrick Massot (Sep 18 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168109):
<p>It didn't seem necessary earlier today</p>

#### [ Patrick Massot (Sep 18 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168230):
<p>I think using reflexivity of the equivalence relation is enough</p>

#### [ Patrick Massot (Sep 18 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168259):
<p>or reflexivity of equality</p>

#### [ Johan Commelin (Sep 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168287):
<p>Hmmm... Reid, that might be the trick</p>

#### [ Johan Commelin (Sep 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168312):
<p>I tried writing <code>AM = M'A</code>, but then your <code>M'</code> is not in SL2Z</p>

#### [ Johan Commelin (Sep 18 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168320):
<p>But maybe with your attack it works.</p>

#### [ Patrick Massot (Sep 18 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168382):
<p>You need to prove to compute the term in the sum corresponding to AM until you get the one corresponding to M</p>

#### [ Johan Commelin (Sep 18 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168396):
<p>Because <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>A</mi><mo mathvariant="normal">′</mo></msup><mo>=</mo><msup><mi>M</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mi>A</mi><mi>M</mi></mrow><annotation encoding="application/x-tex">A' = M^{-1}AM</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span><span class="mord mathit">A</span><span class="mord mathit" style="margin-right:0.10903em;">M</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>M</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mo>∈</mo><mrow><mi mathvariant="normal">S</mi><mi mathvariant="normal">L</mi><mn>2</mn><mi mathvariant="normal">Z</mi></mrow></mrow><annotation encoding="application/x-tex">M^{-1} \in \mathrm{SL2Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.853208em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span><span class="mrel">∈</span><span class="mord"><span class="mord mathrm">S</span><span class="mord mathrm">L</span><span class="mord mathrm">2</span><span class="mord mathrm">Z</span></span></span></span></span></p>

#### [ Johan Commelin (Sep 18 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168457):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I don't think that will work. You really need to use that <code>f</code> has weight <code>k</code> at some point. So you need to rewrite things.</p>

#### [ Patrick Massot (Sep 18 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168465):
<p>of course you use that!</p>

#### [ Johan Commelin (Sep 18 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168470):
<p>Ok, then I'm confused about your plan.</p>

#### [ Reid Barton (Sep 18 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168637):
<p>The book I have writes the action of SL(2, Z) (or more generally GL+(2, R)) on functions on the upper half plane as a right action, which I think makes more sense</p>

#### [ Reid Barton (Sep 18 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168658):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>f</mi><msub><mi mathvariant="normal">∣</mi><mi>k</mi></msub><mi>γ</mi><mo>)</mo><mo>(</mo><mi>z</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mi>det</mi><mi>γ</mi></mrow><mrow><mo>(</mo><mi>c</mi><mi>z</mi><mo>+</mo><mi>d</mi><msup><mo>)</mo><mi>k</mi></msup></mrow></mfrac><mi>f</mi><mo>(</mo><mi>γ</mi><mi>z</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(f|_k \gamma)(z) = \frac{\det \gamma}{(cz + d)^k} f(\gamma z)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9322159999999999em;"></span><span class="strut bottom" style="height:1.4646359999999998em;vertical-align:-0.5324199999999999em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mord"><span class="mord mathrm">∣</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.05556em;">γ</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.9322159999999999em;"><span style="top:-2.6425799999999997em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mopen mtight">(</span><span class="mord mathit mtight">c</span><span class="mord mathit mtight" style="margin-right:0.04398em;">z</span><span class="mbin mtight">+</span><span class="mord mathit mtight">d</span><span class="mclose mtight"><span class="mclose mtight">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7820285714285713em;"><span style="top:-2.786em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span></span></span></span></span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.446108em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mop mtight">det</span><span class="mord mathit mtight" style="margin-right:0.05556em;">γ</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.5324199999999999em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.05556em;">γ</span><span class="mord mathit" style="margin-right:0.04398em;">z</span><span class="mclose">)</span></span></span></span></p>

#### [ Johan Commelin (Sep 18 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168754):
<p>True, but it acts on the left on the plane, right?</p>

#### [ Reid Barton (Sep 18 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168764):
<p>and also the Hecke operators<br>
<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>f</mi><msub><mi mathvariant="normal">∣</mi><mi>k</mi></msub><msub><mi>T</mi><mi>p</mi></msub><mo>)</mo><mo>=</mo><msup><mi>p</mi><mrow><mi>k</mi><mi mathvariant="normal">/</mi><mn>2</mn><mo>−</mo><mn>1</mn></mrow></msup><msub><mo>∑</mo><mi>δ</mi></msub><mi>f</mi><msub><mi mathvariant="normal">∣</mi><mi>k</mi></msub><mi>δ</mi></mrow><annotation encoding="application/x-tex">(f|_k T_p) = p^{k/2-1} \sum_\delta f|_k \delta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.18771em;vertical-align:-0.29971000000000003em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mord"><span class="mord mathrm">∣</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.13889em;">T</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.13889em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathit">p</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">2</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1863979999999999em;"><span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03785em;">δ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29971000000000003em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mord"><span class="mord mathrm">∣</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.03785em;">δ</span></span></span></span> "where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>δ</mi></mrow><annotation encoding="application/x-tex">\delta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03785em;">δ</span></span></span></span> runs over a set of representatives for the distinct right cosets of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="normal">Γ</mi><mn>1</mn></msub><mo>(</mo><mi>N</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\Gamma_1(N)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Γ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10903em;">N</span><span class="mclose">)</span></span></span></span> in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="normal">Δ</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">\Delta_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.969438em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Δ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span>"</p>

#### [ Reid Barton (Sep 18 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168767):
<p>Yes</p>

#### [ Johan Commelin (Sep 18 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168805):
<p>In Lean we only have the action on the plane, so far...</p>

#### [ Johan Commelin (Sep 18 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168811):
<p>Well, and the action on other matrices.</p>

#### [ Reid Barton (Sep 18 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134168877):
<p>Then to check that the Hecke operator preserves modular forms of weight k you need to show that<br>
<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><msub><mo>∑</mo><mi>δ</mi></msub><mi>f</mi><msub><mi mathvariant="normal">∣</mi><mi>k</mi></msub><mi>δ</mi><mo>)</mo><msub><mi mathvariant="normal">∣</mi><mi>k</mi></msub><mi>γ</mi><mo>=</mo><msub><mo>∑</mo><mi>δ</mi></msub><mi>f</mi><msub><mi mathvariant="normal">∣</mi><mi>δ</mi></msub></mrow><annotation encoding="application/x-tex">(\sum_\delta f|_k\delta)|_k \gamma = \sum_\delta f|_\delta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.0497100000000001em;vertical-align:-0.29971000000000003em;"></span><span class="base"><span class="mopen">(</span><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1863979999999999em;"><span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03785em;">δ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29971000000000003em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mord"><span class="mord mathrm">∣</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.03785em;">δ</span><span class="mclose">)</span><span class="mord"><span class="mord mathrm">∣</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03148em;">k</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.05556em;">γ</span><span class="mrel">=</span><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">∑</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.1863979999999999em;"><span style="top:-2.40029em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03785em;">δ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.29971000000000003em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mord"><span class="mord mathrm">∣</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.33610799999999996em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.03785em;">δ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> and the strategy is going to be to move <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>γ</mi></mrow><annotation encoding="application/x-tex">\gamma</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05556em;">γ</span></span></span></span> past <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>δ</mi></mrow><annotation encoding="application/x-tex">\delta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03785em;">δ</span></span></span></span> and reindex</p>

#### [ Reid Barton (Sep 18 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169028):
<p>Yeah, I'm just trying to show how to isolate the step where you reindex the sum</p>

#### [ Reid Barton (Sep 18 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169140):
<p>do we even know yet that the Hecke operator preserves holomorphic functions?</p>

#### [ Johan Commelin (Sep 18 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169222):
<p>That statement does not make sense yet (-;</p>

#### [ Johan Commelin (Sep 18 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169245):
<p>Hmmm, maybe we could turn it into a sensible statement.</p>

#### [ Johan Commelin (Sep 18 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169264):
<p>At the moment the Hecke operators are being defined as operators on functions of weight k</p>

#### [ Reid Barton (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169287):
<p>do we know that (az + b)/(cz + d) is itself a holomorphic function?</p>

#### [ Johan Commelin (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169290):
<p>Afterwards we want to check that the preserve holomorphic functions and functions bound at infinity.</p>

#### [ Reid Barton (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169295):
<p>right</p>

#### [ Johan Commelin (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169296):
<p>We do not know that</p>

#### [ Reid Barton (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169301):
<p>I see</p>

#### [ Johan Commelin (Sep 18 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169311):
<p>It might be a nice example of a holomorphic function (-;</p>

#### [ Kenny Lau (Sep 18 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169484):
<p>are there any sorry that I can fill in?</p>

#### [ Patrick Massot (Sep 18 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169536):
<p><strong>YES</strong></p>

#### [ Johan Commelin (Sep 18 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169571):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> It might be good to read the discussion of the last 20 minutes</p>

#### [ Johan Commelin (Sep 18 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169605):
<p>There is some non-trivialish math going into this. (Nothing you don't understand in 30 secs) But still...</p>

#### [ Kenny Lau (Sep 18 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169681):
<p>where is the sorry?</p>

#### [ Johan Commelin (Sep 18 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169717):
<p>Look in the Hecke file</p>

#### [ Kenny Lau (Sep 18 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169722):
<p>is it WIP?</p>

#### [ Kenny Lau (Sep 18 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169736):
<p>I don't want to cause pull conflict</p>

#### [ Patrick Massot (Sep 18 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169829):
<p>I stand by my claim we don't need any reordering</p>

#### [ Johan Commelin (Sep 18 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169842):
<p>I'm not working on it right now</p>

#### [ Johan Commelin (Sep 18 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169845):
<p>Need to do some emails</p>

#### [ Patrick Massot (Sep 18 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169848):
<p>Hold on 10 sec</p>

#### [ Patrick Massot (Sep 18 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169981):
<p>Ok, look at <a href="https://github.com/semorrison/kbb/blob/master/src/hecke_operator.lean#L76" target="_blank" title="https://github.com/semorrison/kbb/blob/master/src/hecke_operator.lean#L76">https://github.com/semorrison/kbb/blob/master/src/hecke_operator.lean#L76</a></p>

#### [ Patrick Massot (Sep 18 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169986):
<p>I claim there is no problem here</p>

#### [ Patrick Massot (Sep 18 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134169993):
<p>Except we miss a field tactic</p>

#### [ Patrick Massot (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170009):
<p>Kenny: you can fill in all sorries in that file</p>

#### [ Kenny Lau (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170053):
<p>well you just pulled</p>

#### [ Kenny Lau (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170054):
<p>pushed*</p>

#### [ Patrick Massot (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170062):
<p>yes</p>

#### [ Patrick Massot (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170066):
<p>Don't forget what I wrote: Things are reduced to many variation on <a href="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L16" target="_blank" title="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L16">https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/hecke_operator.lean#L16</a> which itself is a variation on <a href="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/upper_half_space.lean#L37" target="_blank" title="https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/upper_half_space.lean#L37">https://github.com/semorrison/kbb/blob/42b4509e2d9ca5beaeb712a17fc0f5754f73854c/src/upper_half_space.lean#L37</a></p>

#### [ Patrick Massot (Sep 18 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170071):
<p>About the other sorries in that file</p>

#### [ Patrick Massot (Sep 18 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170090):
<p>And if you really feel like impressing us, you can get rid of all quadruples of integers and use matrices everywhere</p>

#### [ Patrick Massot (Sep 18 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170094):
<p>I'm giving up on this.</p>

#### [ Patrick Massot (Sep 18 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170167):
<p>Honestly I think the upshot of this story is that Lean is not yet ready for anything involving divisions</p>

#### [ Kenny Lau (Sep 18 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170192):
<p>I don't feel like impressing anyone</p>

#### [ Mario Carneiro (Sep 18 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170199):
<p>You could always just apply division cancellation theorems, it's not that hard...</p>

#### [ Patrick Massot (Sep 18 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170223):
<p>Mario, did you see <a href="https://github.com/semorrison/kbb/blob/master/src/hecke_operator.lean#L32-L49" target="_blank" title="https://github.com/semorrison/kbb/blob/master/src/hecke_operator.lean#L32-L49">https://github.com/semorrison/kbb/blob/master/src/hecke_operator.lean#L32-L49</a>?</p>

#### [ Mario Carneiro (Sep 18 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170224):
<p>I'm not too keen on replacing these direct and logical proofs with arcane tactic-generated proofs</p>

#### [ Patrick Massot (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170283):
<p>The trouble with division cancellations theorems is that terms must be next to each other</p>

#### [ Johan Commelin (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170285):
<p>I am very keen on have a tactic that will write the direct and logical proof for me.</p>

#### [ Patrick Massot (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170290):
<p>hence the endless conv</p>

#### [ Patrick Massot (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170297):
<p>No, this is stupid</p>

#### [ Patrick Massot (Sep 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170303):
<p>We don't want to see this proof</p>

#### [ Patrick Massot (Sep 18 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170311):
<p>We want Lean to compute, as with ring</p>

#### [ Mario Carneiro (Sep 18 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170313):
<p>I think it can be done better than that</p>

#### [ Mario Carneiro (Sep 18 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170324):
<p>plus a little <code>calc</code> would go a long way in that proof</p>

#### [ Mario Carneiro (Sep 18 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170327):
<p>what is all the uparrow stuff?</p>

#### [ Johan Commelin (Sep 18 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170367):
<p>ℤ-matrices acting on ℂ</p>

#### [ Johan Commelin (Sep 18 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170408):
<p>There is a boatload of stuff in this repo that could be generalised. But some thing's can't... for example this lemma could be about arbitrary matrices in <code>GL2R+</code>. But that would shift the arrows somewhere else.</p>

#### [ Johan Commelin (Sep 18 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170826):
<p>I'm looking forward to Lean Forward... these things are the basic Lego blocks that Sander Dahmen works with.</p>

#### [ Mario Carneiro (Sep 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170886):
<p>Okay, I've downloaded and set up kbb. What area needs my attention?</p>

#### [ Johan Commelin (Sep 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170900):
<p><code>hecke_operator.lean</code></p>

#### [ Johan Commelin (Sep 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170907):
<p>You'll get pulled into the other files by <code>import</code></p>

#### [ Johan Commelin (Sep 18 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170919):
<p>Beware, there are minor dragons in these files.</p>

#### [ Johan Commelin (Sep 18 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170944):
<p>Every 10 lines will give you another opportunity for a major refactor (-;</p>

#### [ Patrick Massot (Sep 18 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170952):
<p>The area where you write a field tactic</p>

#### [ Johan Commelin (Sep 18 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134170967):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> you might want to tell <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> which <code>sorry</code> you are working on.</p>

#### [ Kenny Lau (Sep 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171012):
<p>all of them</p>

#### [ Mario Carneiro (Sep 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171030):
<p>lol that's not happening before friday Patrick</p>

#### [ Patrick Massot (Sep 18 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171055):
<p>I'm sure Kevin will understand</p>

#### [ Patrick Massot (Sep 18 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171072):
<p>Do you think you could do it before he turns 60?</p>

#### [ Johan Commelin (Sep 18 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171083):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Any improvements of the repo would be appreciated.</p>

#### [ Johan Commelin (Sep 18 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134171095):
<p><code>matrices</code> and <code>determinants</code> seem to be almost ready to merge. And independent of the other files.</p>

#### [ Kenny Lau (Sep 18 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172685):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> what's the math proof of the thing that Patrick claims to be true?</p>

#### [ Kenny Lau (Sep 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172738):
<p>and what is the second thing?</p>

#### [ Patrick Massot (Sep 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172751):
<p>The maths proof is to expand everythings and compute</p>

#### [ Patrick Massot (Sep 18 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172759):
<p>But probably there is a better way to setup all this</p>

#### [ Kenny Lau (Sep 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172828):
<p>I filled in two of the sorries</p>

#### [ Kenny Lau (Sep 18 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134172834):
<p>see if you can learn anything therefrom</p>

#### [ Johan Commelin (Sep 19 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134223218):
<p>Reid quoted some formulas containing the Petersson slash operator (of weight <code>k</code>). Would it make sense to mimic that notation, somehow? I think we should also wrap <code>M_trans</code> and <code>SL2Z_H</code> into notation (<code>has_scalar</code>). I hope it will make statements more readable. Maybe it will even improve proofs, I don't know.</p>

#### [ Johan Commelin (Sep 19 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134225022):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I agree with Patrick's claim. I made some small rewrites. Maybe now it is easier to math-see why it is true. I still wish <code>ring</code> would kill this. But it doesn't... because there are divisions. I hate divisions in Lean.</p>

#### [ Johan Commelin (Sep 19 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/hecke%20operator/near/134225043):
<p>(Oooh, I also pushed those small rewrites.)</p>


{% endraw %}
