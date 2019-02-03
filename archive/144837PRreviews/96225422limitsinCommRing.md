---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/96225422limitsinCommRing.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#422 limits in CommRing](https://leanprover-community.github.io/archive/144837PRreviews/96225422limitsinCommRing.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Oct 15 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796679):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>, I've started a WIP branch to construct products and equalizers in CommRing.</p>

#### [ Scott Morrison (Oct 15 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796726):
<p>Products work just fine. Equalizers still has lots of sorries, mostly because I'm not willing to get my hands dirty and do things by brute force. All the remaining goals are just about manipulating <code>is_ring_hom</code>. I wish most of them were solved by <code>simp</code>.</p>

#### [ Scott Morrison (Oct 15 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796732):
<p>There's also an instance where <code>by subtype_instance</code> doesn't do what I hoped it would do. Perhaps <span class="user-mention" data-user-id="110026">@Simon Hudon</span> would like to look at this?</p>

#### [ Scott Morrison (Oct 15 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796738):
<p>Typical examples of the remaining goals are:</p>
<div class="codehilite"><pre><span></span>R S : examples.CommRing,
f g : R ⟶ S
⊢ set.mem (add_monoid.zero ↥R) {r : ↥R | ⇑f r = ⇑g r}
</pre></div>

#### [ Scott Morrison (Oct 15 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796787):
<p>(A subproblem here is to explain to me why this has <code>set.mem</code> instead of <code>\in</code>, and <code>add_monoid.zero ↥R</code> instead of <code>0</code>! I'm really confused by both.)</p>

#### [ Scott Morrison (Oct 15 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796790):
<p>If anyone wants to hack on this branch, please feel free.</p>

#### [ Scott Morrison (Oct 15 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796796):
<p>I've just arrived at a conference I'm organising, and probably should stop working on lean for a while. :-)</p>

#### [ Kevin Buzzard (Oct 15 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796810):
<p>I was going to say "you should post more precise coordinates about where this branch is" and then I remembered that you can click on the link in the title of the thread :D</p>

#### [ Mario Carneiro (Oct 15 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796847):
<p>the weird unfolding is probably because you have a universe metavariable</p>

#### [ Scott Morrison (Oct 15 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796858):
<p>The equalizers file is at <a href="https://github.com/leanprover/mathlib/pull/422/files#diff-cc1aad82649d34fb81afe5403e9bd67f" target="_blank" title="https://github.com/leanprover/mathlib/pull/422/files#diff-cc1aad82649d34fb81afe5403e9bd67f">https://github.com/leanprover/mathlib/pull/422/files#diff-cc1aad82649d34fb81afe5403e9bd67f</a>.</p>

#### [ Scott Morrison (Oct 15 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805078):
<p>I've just pushed an attempt at products in <code>Top</code>, that reduces it to two <code>sorry</code> statements, which don't mention any category theory.</p>

#### [ Scott Morrison (Oct 15 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805099):
<p>If you pull the <code>limits-examples</code> branch of <code>https://github.com/leanprover-community/mathlib/</code>, you'll find <code>https://github.com/leanprover-community/mathlib/blob/limits-examples/category_theory/examples/topological_spaces/products.lean</code></p>

#### [ Scott Morrison (Oct 15 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805150):
<p>The two remaining goals are just</p>
<div class="codehilite"><pre><span></span>β : Type u,
f : β → Top,
b : β
⊢ continuous (λ (g : Π (b : β), ↥(f b)), g b)
</pre></div>


<p>(here <code>↥(f b)</code> just means the underlying type of the <code>Top</code>)</p>

#### [ Scott Morrison (Oct 15 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805155):
<p>and</p>
<div class="codehilite"><pre><span></span>α : Type u,
β : α → Type v,
R : Π (a : α), topological_space (β a),
γ : Type w,
_inst_1 : topological_space γ,
f : Π (a : α), γ → β a,
Rh : ∀ (a : α), continuous (f a)
⊢ continuous (λ (x : γ) (b : α), f b x)
</pre></div>

#### [ Scott Morrison (Oct 15 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805170):
<p>which I think needs no explaination, and is presumably meant to be proved by switching the arguments in <code>continuous_pi</code> (which I discovered only because I tried to name this lemma <code>continuous_pi</code>).</p>

#### [ Scott Morrison (Oct 15 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805232):
<p>Duh, the second one is exactly <code>continuous_pi</code>.</p>

#### [ Mario Carneiro (Oct 15 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805241):
<p>I am not sure what we are looking for, but I think that statement looks much nicer than the one with the fans</p>

#### [ Mario Carneiro (Oct 15 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805244):
<p>it's much more obvious what we need to prove</p>

#### [ Scott Morrison (Oct 15 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805327):
<p>duh, and the first one is just continuous_apply</p>

#### [ Scott Morrison (Oct 15 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805338):
<p>I agree, Mario. The problem was really <span class="user-mention" data-user-id="110031">@Patrick Massot</span> typing <code>tidy</code> a bit too soon. :-)</p>

#### [ Scott Morrison (Oct 15 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805378):
<p>I just pushed <a href="https://github.com/leanprover-community/mathlib/blob/limits-examples/category_theory/examples/topological_spaces/products.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/limits-examples/category_theory/examples/topological_spaces/products.lean">this</a>.</p>

#### [ Mario Carneiro (Oct 15 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805379):
<p>I'm surprised case on the fans is not done by the auto_cases stuff</p>

#### [ Scott Morrison (Oct 15 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805387):
<p>No, it's not. auto_cases is pretty timid</p>

#### [ Scott Morrison (Oct 15 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805393):
<p>if you're trying to construct a fan, tidy will use split and intro to get you most of the way there</p>

#### [ Scott Morrison (Oct 15 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805435):
<p>(just in case anyone followed that link, I was a moment too fast, and you might want to reload it :-)</p>

#### [ Mario Carneiro (Oct 15 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805455):
<p>what does it mean that <code>Top.pi_π</code> is <code>@[simp]</code>? (Also that name is a bit confusing...)</p>

#### [ Scott Morrison (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805498):
<p>Tagging it with @[simp] like that somehow(?!) encourages Lean to unfold its definition more freely later.</p>

#### [ Scott Morrison (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805499):
<p>I don't understand that mechanism at all.</p>

#### [ Scott Morrison (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805501):
<p>But I've found that you can often avoid stating lots of <code>rfl</code> lemmas just by putting <code>@[simp]</code> on the construction itself.</p>

#### [ Mario Carneiro (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805502):
<p>oh, that means it marks the equation lemmas as <code>@[simp]</code></p>

#### [ Scott Morrison (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805505):
<p>Sorry, voodoo-programming. :-)</p>

#### [ Mario Carneiro (Oct 15 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805506):
<p>because it's a <code>def</code></p>

#### [ Scott Morrison (Oct 15 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805514):
<p>Cool, okay, I'll say that's why, if asked in future. :-)</p>

#### [ Scott Morrison (Oct 15 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805517):
<p>The first @[simp] was unnecessary, so I removed it.</p>

#### [ Scott Morrison (Oct 15 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805558):
<p>I agree the name is bad. But I uniformly use <code>π</code> and <code>iota</code> for the maps in cones and cocones</p>

#### [ Scott Morrison (Oct 15 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805559):
<p>and I think <code>pi</code> is the correct name when talking about product types</p>

#### [ Scott Morrison (Oct 15 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805566):
<p>so you end up with the name collision <code>pi_π</code> for the maps out of product types ... :-(</p>

#### [ Mario Carneiro (Oct 15 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805642):
<p>why the <code>dsimp</code> in the first construction and <code>convert</code> in the second instead of directly applying the theorem?</p>

#### [ Scott Morrison (Oct 15 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805644):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, if you have a chance, could you explain that "universe metavariable" comment from above?</p>

#### [ Scott Morrison (Oct 15 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805646):
<p>I've fixed those; reload.</p>

#### [ Scott Morrison (Oct 15 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805691):
<p>It's now the <a href="https://github.com/leanprover-community/mathlib/blob/limits-examples/category_theory/examples/rings/equalizers.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/limits-examples/category_theory/examples/rings/equalizers.lean"><code>rings/equalizers.lean</code></a> file that I'm really unhappy about...</p>

#### [ Mario Carneiro (Oct 15 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805814):
<p>It's a weird bug that Kenny discovered. Here's a MWE:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">sg</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">instance</span> <span class="n">mm</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">monoid</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span> <span class="c1">-- ∀ (a : α), semigroup.mul a sorry = a</span>
  <span class="bp">..</span><span class="n">sg</span> <span class="o">}</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">sg</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">semigroup</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">instance</span> <span class="n">mm</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">:</span> <span class="n">monoid</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span> <span class="c1">-- ∀ (a : α), a * 1 = a</span>
  <span class="bp">..</span><span class="n">sg</span> <span class="o">}</span>
</pre></div>

#### [ Scott Morrison (Oct 15 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805815):
<p>If I could understand why <code>set.mem</code> and <code>add_monoid</code> have mysteriously appeared, I could ask Simon why <code>subtype_instance</code> doesn't work. :-)</p>

#### [ Scott Morrison (Oct 15 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805835):
<p>That is weird!</p>

#### [ Mario Carneiro (Oct 15 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805838):
<p>the presence of universe metavariables in the type of the theorem causes lean to unfold all sorts of stuff</p>

#### [ Scott Morrison (Oct 15 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805894):
<p>indeed, changing <code>CommRing</code> to <code>CommRing.{v}</code> solves that problem</p>

#### [ Patrick Massot (Oct 15 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135817239):
<blockquote>
<p>I agree, Mario. The problem was really Patrick Massot typing <code>tidy</code> a bit too soon. :-)</p>
</blockquote>
<p>What happened is I copied the proof from Type and started to edit where things went wrong...</p>

#### [ Patrick Massot (Oct 15 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135817319):
<p>Thanks for your explanations Scott. I think it's unavoidable that  notations needs to be learned in order to use the category theory goodies. But hopefully it will be much easier with more examples</p>

#### [ Patrick Massot (Oct 15 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135817428):
<blockquote>
<p>There's also an instance where <code>by subtype_instance</code> doesn't do what I hoped it would do. Perhaps Simon Hudon would like to look at this?</p>
</blockquote>
<p>This tactic is really specialized, it's meant to prove substuff is stuff, starting from the definition of substuff, assuming that definition obeys standard naming conventions. It never claimed to be able to prove any random subtype of some stuff is stuff.</p>


{% endraw %}
