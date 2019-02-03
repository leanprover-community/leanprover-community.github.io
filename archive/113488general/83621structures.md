---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83621structures.html
---

## Stream: [general](index.html)
### Topic: [structures](83621structures.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 08 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/123459639):
<p>When I was building the complexes, I think I tried to make them a field all in one go, and there were problems which perhaps were something to do with neg or sub. <span class="user-mention" data-user-email="di.gama@gmail.com" data-user-id="110049">@Mario Carneiro</span> showed me how to fix these problems by showing first that the complexes were an additive group and then only afterwards that they were a field. But I cannot remember what the problems were. Can anyone here guess? Was it something to do with defining sub or neg myself vs letting the system somehow do it for me? I now cannot really imagine how the system would do it for me.</p>

#### [ Johan Commelin (Aug 02 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764601):
<p>How am I supposed to finish of this triviality?</p>
<div class="codehilite"><pre><span></span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">cat</span> <span class="o">:</span> <span class="n">category</span> <span class="n">C</span>
<span class="err">⊢</span> <span class="o">{</span><span class="n">Hom</span> <span class="o">:=</span> <span class="n">category</span><span class="bp">.</span><span class="n">Hom</span> <span class="n">cat</span><span class="o">,</span>
     <span class="n">identity</span> <span class="o">:=</span> <span class="mi">𝟙</span><span class="o">,</span>
     <span class="n">compose</span> <span class="o">:=</span> <span class="n">category</span><span class="bp">.</span><span class="n">compose</span> <span class="n">cat</span><span class="o">,</span>
     <span class="n">left_identity</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
     <span class="n">right_identity</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
     <span class="n">associativity</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">}</span> <span class="bp">=</span>
    <span class="n">cat</span>
</pre></div>

#### [ Johan Commelin (Aug 02 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764615):
<p>It is just asking me whether sum structure <code>cat</code> is equal to the structure built from the fields of <code>cat</code>.</p>

#### [ Kenny Lau (Aug 02 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764618):
<p><code>congr</code> or <code>ext</code></p>

#### [ Johan Commelin (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764621):
<p>To which I reply: "Yes! Of course it is."</p>

#### [ Kenny Lau (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764627):
<p>oh no</p>

#### [ Kenny Lau (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764628):
<p><code>cases cat</code></p>

#### [ Kenny Lau (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764629):
<p>then <code>dsimp</code></p>

#### [ Johan Commelin (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764631):
<p>aha</p>

#### [ Kenny Lau (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764633):
<p>I'm not sure because this is not an MWE</p>

#### [ Johan Commelin (Aug 02 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764636):
<p><code>congr</code> failed, and <code>ext</code> did nothing.</p>

#### [ Kenny Lau (Aug 02 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764680):
<p>if <code>ext</code> did nothing, then it is because you don't have an extensionality lemma, i.e. the interface</p>

#### [ Kenny Lau (Aug 02 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764686):
<p><code>@[extensionality] lemma category.ext : ...</code></p>

#### [ Johan Commelin (Aug 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764754):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">op_op&#39;</span> <span class="o">:</span> <span class="bp">@</span><span class="n">opposites</span><span class="bp">.</span><span class="n">Opposite</span> <span class="n">C</span> <span class="o">(</span><span class="bp">@</span><span class="n">opposites</span><span class="bp">.</span><span class="n">Opposite</span> <span class="n">C</span> <span class="n">cat</span><span class="o">)</span> <span class="bp">=</span> <span class="n">cat</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">unfreeze_local_instances</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">cat</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">opposites</span><span class="bp">.</span><span class="n">Opposite</span><span class="o">],</span>
  <span class="n">congr</span>
<span class="kn">end</span> <span class="c1">-- We win!</span>
</pre></div>

#### [ Johan Commelin (Aug 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764756):
<p>That worked.</p>

#### [ Johan Commelin (Aug 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764759):
<p>Thanks!</p>

#### [ Kenny Lau (Aug 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130764760):
<p>nice</p>

#### [ Chris Hughes (Aug 02 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765215):
<p>My guess is that perhaps you wanted the<code> add_group</code> axioms to prove some other the other field axioms</p>

#### [ Kenny Lau (Aug 02 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765227):
<p>add group?</p>

#### [ Chris Hughes (Aug 02 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765298):
<p>What's the question?</p>

#### [ Kenny Lau (Aug 02 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765311):
<p>you're replying to the message from March</p>

#### [ Chris Hughes (Aug 02 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130765345):
<p>I see.</p>

#### [ Patrick Massot (Aug 02 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767424):
<p>Johan, I think you shouldn't need to directly call <code>unfreeze_local_instances</code>. What are you trying to do?</p>

#### [ Johan Commelin (Aug 02 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767475):
<p>Well, I tried to do the <code>cases cat</code> and it complained... it told me to <code>unfreeze</code> stuff, and I happily complied.</p>

#### [ Johan Commelin (Aug 02 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767488):
<p>I am trying to investigate how far the double <code>op</code> of a category <code>C</code> is from being defeq to <code>C</code>.</p>

#### [ Patrick Massot (Aug 02 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767489):
<p>Do you have a MWE I could try?</p>

#### [ Johan Commelin (Aug 02 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767500):
<p>Hmm, it depends on an old version of Scott's PR...</p>

#### [ Johan Commelin (Aug 02 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130767508):
<p>If you have his PR checked out somewhere, I suppose you could copy paste my latest snippet.</p>

#### [ Johan Commelin (Aug 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130768912):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> <a href="https://github.com/jcommelin/lean-homotopy-theory/blob/playground/src/categories/op_op.lean" target="_blank" title="https://github.com/jcommelin/lean-homotopy-theory/blob/playground/src/categories/op_op.lean">https://github.com/jcommelin/lean-homotopy-theory/blob/playground/src/categories/op_op.lean</a></p>

#### [ Johan Commelin (Aug 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130768914):
<p>That's a file in a fork of a project by Reid, depending on an old version of Scott's PR.</p>

#### [ Kevin Buzzard (Aug 02 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130768988):
<p>If you're being asked to unfreeze local instances then it's probably because you're doing cases on some random class -- that's when this happens to me. I think the last time it happened, Chris pointed out that I had access to all the things I wanted, with <code>cat.foo</code>, <code>cat.bar</code> etc, so I didn't need to unfreeze anything.</p>

#### [ Johan Commelin (Aug 02 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769080):
<p>Is unfreezing a bad thing to do?</p>

#### [ Scott Morrison (Aug 02 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769237):
<p><code>Opposite (Opposite C)</code> isn't going to be defeq to <code>C</code>. It's going to be provably equal, or isomorphic, but since we know those are both evil notions, in the end we probably just want to prove it's equivalent. (My intuition is that even proving the equality is just going to invite trouble later, when you rewrite along the equality.)</p>

#### [ Johan Commelin (Aug 02 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769289):
<p>Right. But it's pretty close to being defeq (whatever that means). As expected, there is nothing going into the proofs I just linked to.</p>

#### [ Kevin Buzzard (Aug 02 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769490):
<p>The CS people love stuff being defeq but because categories are one level up in the mathematical hierarchy from sets, it's basically never the right question to ask if they're isomorphic, let alone defeq</p>

#### [ Johan Commelin (Aug 02 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130769616):
<p>Sure. But <code>op op</code> is somewhat special right? And I can imagine it would help a lot, in this special case.</p>

#### [ Mario Carneiro (Aug 04 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130879231):
<p>I don't think there is any harm in proving an equality of categories when it happens to be true. Of course there should be theorems saying equality implies isomorphism and isomorphism implies equivalence</p>

#### [ Mario Carneiro (Aug 04 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130879241):
<p>the main point is to not expect that equality is much stronger or easier to work with than these other two notions</p>

#### [ Scott Morrison (Aug 04 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130879244):
<p>I agree. Just don't rewrite the source or target of a functor/natural transformation by an equation of categories and expect to be happy later. :-)</p>

#### [ Mario Carneiro (Aug 04 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130879337):
<p>I think one way to handle this is to use a <code>have</code> subproof to show that some equality of categories holds (say an embedded op op cancellation), and then use <code>cast h</code> as a functor and have theorems about it</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130882057):
<blockquote>
<p>I don't think there is any harm in proving an equality of categories when it happens to be true. Of course there should be theorems saying equality implies isomorphism and isomorphism implies equivalence</p>
</blockquote>
<p>Maybe the CS experience is different, but it's very rare for categories to be isomorphic in "real life" maths.</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structures/near/130882101):
<p>I think it's about as common as equality of categories, like in this case</p>


{% endraw %}
