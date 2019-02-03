---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39393annoyance.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [$ annoyance](https://leanprover-community.github.io/archive/113488general/39393annoyance.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 17 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710552):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">subtype_is_partial_order</span> <span class="o">:</span>
<span class="n">partial_order</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">U</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Us</span> <span class="n">Vs</span><span class="o">,</span><span class="n">Us</span><span class="bp">.</span><span class="mi">1</span> <span class="err">⊆</span> <span class="n">Vs</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Us</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="n">Us</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Us</span> <span class="n">Vs</span> <span class="n">Ws</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Us</span> <span class="n">Vs</span> <span class="n">HUV</span> <span class="n">HVU</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span> <span class="n">HUV</span> <span class="n">HVU</span>
<span class="c1">--  le_antisymm := λ Us Vs, subtype.eq $ set.subset.antisymm -- doesn&#39;t work, annoyingly</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 17 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710573):
<p>I wanted to write a beautiful partial order on some subsets of a type.</p>

#### [ Kevin Buzzard (May 17 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710640):
<p><code>le_refl</code> is a bit meh because I had to write <code>Us.1</code>, but I do understand that <code>set.subset.refl</code> needs to be told what it's refling in general</p>

#### [ Kevin Buzzard (May 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710677):
<p><code>le_trans</code> is perfect and I could probably even have written <code>\lam _ _ _</code></p>

#### [ Kevin Buzzard (May 17 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710770):
<p><code>le_antisymm</code> is a bit annoying though because in functional programming if you write <code>\lam x y, blah y</code> then you can normally remove the <code>y</code>s. But I can't remove <code>HUV</code> and <code>HVU</code> here because of my <code>$</code> trickery. Is this just some annoyance in functional programming that I have to put up with or is there some other idiom which means I can get rid of <code>HUV</code> and <code>HVU</code> somehow?</p>

#### [ Kevin Buzzard (May 17 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710780):
<p><code>le_antisymm := λ Us Vs, subtype.eq ∘ set.subset.antisymm</code> doesn't work either</p>

#### [ Kevin Buzzard (May 17 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710801):
<p>I can see why these things don't work, I just want something which looks a bit cooler if possible. Not for any particularly good reason, I'm just trying to write tidy code</p>

#### [ Kevin Buzzard (May 17 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710885):
<p>Here's a succinct way of asking my question:</p>

#### [ Kevin Buzzard (May 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710887):
<div class="codehilite"><pre><span></span>  <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">HUV</span> <span class="n">HVU</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span> <span class="n">HUV</span> <span class="n">HVU</span>
</pre></div>

#### [ Kevin Buzzard (May 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126710927):
<p>Can I get rid of those last two variables?</p>

#### [ Chris Hughes (May 17 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126711207):
<p><code>le_antisymm := λ Us Vs, subtype.eq ∘ set.subset.antisymm</code> doesn't work because there are two arguments, and <code>f ∘ g</code> is <code>λ x, f (g x)</code>not <code>λ x y, f (g x y)</code>The eta reduction doesn't work because the arguments are inside brackets.</p>

#### [ Chris Hughes (May 17 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126711306):
<p>I think you just have to put up with it, but it doesn't look that annoying.</p>

#### [ Chris Hughes (May 17 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126711333):
<p>This works <code>le_antisymm := λ Us Vs HUV, subtype.eq ∘ set.subset.antisymm HUV</code></p>

#### [ Chris Hughes (May 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126711384):
<p>If you want to be extra confusing.</p>

#### [ Chris Hughes (May 17 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126716170):
<blockquote>
<p>I can see why these things don't work, I just want something which looks a bit cooler if possible. Not for any particularly good reason, I'm just trying to write tidy code</p>
</blockquote>
<p>I should have read the question</p>

#### [ Sebastian Ullrich (May 17 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126718633):
<p><code>λ Us Vs, ((∘) ∘ (∘)) subtype.eq set.subset.antisymm</code></p>

#### [ Reid Barton (May 17 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126718805):
<p>At least you can't write the awful <code>(f .) . g</code> in lean.</p>

#### [ Reid Barton (May 17 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126718821):
<p>I had to work out on paper whether that does what I remember it doing.</p>

#### [ Patrick Massot (May 17 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126718822):
<p>what would that mean?</p>

#### [ Sebastian Ullrich (May 17 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126718828):
<p>Yes, I'll definitely fix that for Lean 4</p>

#### [ Reid Barton (May 17 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126718896):
<p>Haskell <code>.</code> is Lean's <code>∘</code>, and <code>(f .)</code> means <code>λ h, f ∘ h</code></p>

#### [ Patrick Massot (May 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126718929):
<p>Aaaarg, I did that rookie mistake again! I called some variable <code>a</code></p>

#### [ Patrick Massot (May 17 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126718983):
<p>Sebastian, will this mistake be forgiven in Lean 4?</p>

#### [ Sebastian Ullrich (May 17 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126719304):
<p>absolutely</p>

#### [ Kevin Buzzard (May 17 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126720531):
<p><code>#eval (+) 2 2 -- 4</code></p>

#### [ Kevin Buzzard (May 18 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126720580):
<p>I remember reading that one could do this in Haskell but I didn't know it was a Lean thing</p>

#### [ Kevin Buzzard (May 18 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126720690):
<p><code>#check ((∘) ∘ (∘)) -- (?M_1 → ?M_2) → (?M_4 → ?M_3 → ?M_1) → ?M_4 → ?M_3 → ?M_2</code></p>

#### [ Kevin Buzzard (May 18 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126720691):
<p>I love Lean</p>

#### [ Kevin Buzzard (May 18 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126720732):
<p>who needs pencil and paper</p>

#### [ Kevin Buzzard (May 18 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126722090):
<p>Ok so I used pencil and paper</p>

#### [ Kevin Buzzard (May 18 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126722151):
<p>Recall that <code>(∘) f g x = (f ∘ g) x = f (g x)</code>. So</p>
<div class="codehilite"><pre><span></span>   ((∘) ∘ (∘)) a b c d
=  (∘) ((∘) a) b c d
=  ((∘) a) (b c) d
=  (∘) a (b c) d
=  a (b c d)
</pre></div>

#### [ Kevin Buzzard (May 18 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126722157):
<p>which is indeed what we wanted to do</p>

#### [ Kevin Buzzard (May 18 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126722175):
<p>At the back of my mind I always feel like computer scientists learn this sort of stuff in their first year of undergrad whereas this is never taught to mathematicians at all</p>

#### [ Brendan Zabarauskas (May 18 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126729532):
<p>Depends on the computer science course <span class="emoji emoji-1f629" title="weary">:weary:</span></p>

#### [ Mario Carneiro (May 18 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126729645):
<p>I don't think this is actually accurate, but I admit it as Kevin's warped view of what computer science is. I think it is accurate to say that you become comfortable with this when learning Haskell and not before</p>

#### [ Mario Carneiro (May 18 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126729702):
<p>I think that the demographics of this chat are disproportionately skewed towards functional programmers (for good reason), so it's easy to get that impression</p>

#### [ Brendan Zabarauskas (May 18 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20annoyance/near/126729800):
<p>Correct. I'm one who had to learn FP and type theory/programming language stuff in my own time. But might be getting off topic here.</p>


{% endraw %}
