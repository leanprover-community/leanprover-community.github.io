---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/01949minimumoffiniteset.html
---

## Stream: [maths](index.html)
### Topic: [minimum of finite set](01949minimumoffiniteset.html)

---


{% raw %}
#### [ Patrick Massot (May 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993170):
<blockquote>
<p>with <code>sup</code> you don't need to use <code>iget</code>. <code>max</code> is the better name but I think <code>sup</code> has the better behaviour.</p>
</blockquote>
<p>What is this sup you are talking about?</p>

#### [ Chris Hughes (May 23 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993263):
<p><code>finset.sup</code> defined, or at least used in <code>multivariate_polynomial</code></p>

#### [ Chris Hughes (May 23 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993324):
<p>Only defined for <code>semilattice_sup_bot</code></p>

#### [ Patrick Massot (May 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993423):
<p>That's unexpected</p>

#### [ Patrick Massot (May 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993424):
<p>Thanks</p>

#### [ Patrick Massot (May 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993428):
<p>I still can't use it though. I'll try harder</p>

#### [ Chris Hughes (May 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993435):
<p>Why not?</p>

#### [ Chris Hughes (May 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993443):
<p>It takes the sup of the image of a given function.</p>

#### [ Patrick Massot (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993499):
<p>failed to synthesize type class instance for ⊢ semilattice_sup_bot ℝ</p>

#### [ Patrick Massot (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993510):
<p>It means I need to learn</p>

#### [ Patrick Massot (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993514):
<p>what is a semilattice_sup_bot</p>

#### [ Chris Hughes (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993517):
<p>reals aren't a semilattice sup bot</p>

#### [ Chris Hughes (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993519):
<p>It needs a least element of the type.</p>

#### [ Kenny Lau (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993522):
<p><code>ennreal</code> is</p>

#### [ Kenny Lau (May 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993533):
<p>the nonnegative (in your case, positif) reals also is</p>

#### [ Patrick Massot (May 23 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993723):
<p>Using the type of nonnegative real would probably mess up lots of things</p>

#### [ Patrick Massot (May 23 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993749):
<p>in my norms.lean</p>

#### [ Johan Commelin (May 23 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993759):
<p>Incidentally, I just defined some stuff on nonnegative reals this week...</p>

#### [ Johan Commelin (May 23 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993770):
<p>Like that it is a comm_semiring, and its topology</p>

#### [ Patrick Massot (May 23 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993831):
<p>Nooo! I don't want to do topological commutative semi-ring theory!</p>

#### [ Johan Commelin (May 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993927):
<p>Well, it is very useful for defining the standard simplices. Because it takes care of the condition that all the coordinates are positive</p>

#### [ Andrew Ashworth (May 23 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126993946):
<p>is this part of your bigop project? I am dying to have useable matrices and summations in Lean, maybe I will take a look</p>

#### [ Patrick Massot (May 23 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126994048):
<p>No, I'm back to calculus while I wait for omega/cooper to be usable, just in case it makes using nat possible</p>

#### [ Andrew Ashworth (May 23 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126994149):
<p>well, studying cooper was also on my recreational to-do list, so i'll have to get on it</p>

#### [ Patrick Massot (May 23 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126994166):
<p>I was not able to import it in any way</p>

#### [ Patrick Massot (May 23 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995176):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> The point of my questions about max is to try to get a norm on ℝ^n. But this goes through the dreaded definition of Lean metric spaces. Could you get me started by doing</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">metric_space</span><span class="bp">.</span><span class="n">fintype_function</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">β</span><span class="o">]</span>
<span class="o">:</span> <span class="n">metric_space</span> <span class="o">(</span><span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
</pre></div>


<p>(using the max distance between images) I think I could manage from there.</p>

#### [ Johannes Hölzl (May 23 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995281):
<p>Do you want to use the max distance in general, or just because we don't have sqrt yet?</p>

#### [ Patrick Massot (May 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995324):
<p>We started using max on products a long time ago. It's partly for lack of square root tooling, but I also don't see why square root would be better</p>

#### [ Patrick Massot (May 23 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995353):
<p>The current state of this story is <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean</a></p>

#### [ Patrick Massot (May 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995399):
<p>(with products of two types only)</p>

#### [ Kevin Buzzard (May 23 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995564):
<p>(and added segfault)</p>

#### [ Kevin Buzzard (May 23 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995569):
<p>(no)</p>

#### [ Kevin Buzzard (May 23 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995576):
<p>(assertion violation)</p>

#### [ Patrick Massot (May 23 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995619):
<p>The version up at github has no assertion violation</p>

#### [ Patrick Massot (May 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126995689):
<p>And I was linking to this only so that Johannes could see my definition of normed group</p>

#### [ Johannes Hölzl (May 23 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126996448):
<p>For me somehow the Euclidean distance (l_2-norm) as the canonical distance. But yeah, we can first start with the max-distance. That's one advantage of uniform spaces: the produce construction is more canonical :-)</p>

#### [ Kevin Buzzard (May 23 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126997326):
<p>"more canonical" :-)</p>

#### [ Kevin Buzzard (May 23 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126997332):
<p>We didn't formalise canonical yet</p>

#### [ Kevin Buzzard (May 23 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/126997334):
<p>let alone make it a partial order</p>

#### [ Johannes Hölzl (May 24 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127000110):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>  <a href="https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105" target="_blank" title="https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105">https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105</a> here is the metric space for finite function.<br>
<span class="user-mention" data-user-id="110026">@Simon Hudon</span>  I think I will change <code>max</code> to my version of <code>maxi</code>. How would you do these kind of proofs?</p>

#### [ Mario Carneiro (May 24 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127000293):
<p>We can make <code>imax</code> (I usually use the <code>i</code> as a prefix) as an alternative to <code>max</code> defined for inhabited sets if you like. If it is defined as <code>max.iget</code> then we get all the theorems for free</p>

#### [ Mario Carneiro (May 24 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127000354):
<p>I want to make <code>finset.max</code> a special case of <code>finset.sup</code> by defining a <code>with_bot A := option A</code>  type which extends the order with <code>none &lt;= some a</code></p>

#### [ Johannes Hölzl (May 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127002306):
<p>I still don't see cases where the current <code>max</code> has advantages, or how to do proofs properly. Using <code>with_bot</code>, could we just use <code>sup</code> instead of the current <code>max</code>, and use <code>sup</code> + <code>iget</code> as <code>max</code>?</p>

#### [ Simon Hudon (May 24 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127003581):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  Sorry, I haven't been following. Which proofs do you mean?</p>

#### [ Mario Carneiro (May 24 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127012241):
<p>Using <code>with_bot</code>, <code>sup</code> over <code>with_bot</code> would be the same as <code>max</code> is currently (in particular, it would return an <code>option</code>), and then you could postprocess the result with <code>iget</code> if that makes sense in your application. I like the way <code>max</code> works at the moment because it lets you work relationally with max, i.e. "x is the max of s" rather than a term "max of s" which may or may not actually be a max of s</p>

#### [ Sean Leather (May 24 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014486):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">maxi</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">inhabited</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="o">:=</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="n">image</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">max</span><span class="bp">.</span><span class="n">iget</span>

<span class="kn">lemma</span> <span class="n">maxi_empty</span> <span class="o">:</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span><span class="bp">.</span><span class="n">maxi</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">default</span> <span class="n">β</span>
</pre></div>


<p>I don't understand how <code>maxi_empty</code> is useful.</p>

#### [ Johannes Hölzl (May 24 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014487):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> the proofs in <a href="https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105" target="_blank" title="https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105">https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105</a> Its a little bit of a special case (we are working essentially in R &gt;= 0) and we explicitly want <code>s = empty -&gt; max s = 0</code>. Without adding my own rules for <code>maxi</code> (a.k.a. <code>imax</code>) I would need a lot of annoying case distinctions (ala <code>finset.univ = empty</code>)</p>

#### [ Johannes Hölzl (May 24 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014574):
<p>At least at the beginning <code>maxi_empty</code> is helpful: the following rules have a special condition to compare to the default when <code>s = empty</code>, which can be resolved using <code>by simp * at *</code>.</p>

#### [ Sean Leather (May 24 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014687):
<p>I see: <code>(hd : s = ∅ → b ≤ default β)</code> is what you mean. So with an <code>option</code> result, you don't need that? But you still think using <code>inhabited</code> is better?</p>

#### [ Sean Leather (May 24 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014782):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">le_maxi_of_forall</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">a</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">hd</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">default</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">s</span><span class="bp">.</span><span class="n">maxi</span> <span class="n">f</span>
</pre></div>


<p>looks a lot <a href="https://github.com/leanprover/mathlib/pull/133/commits/351dd66c84cc45c53f7de49836f0086d35071327#diff-e7d41a6a4fb2225734fc2fb30e4dceeeR1069" target="_blank" title="https://github.com/leanprover/mathlib/pull/133/commits/351dd66c84cc45c53f7de49836f0086d35071327#diff-e7d41a6a4fb2225734fc2fb30e4dceeeR1069">like</a></p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">le_max_of_mem</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">max</span> <span class="n">b</span> <span class="n">s</span>
</pre></div>

#### [ Sean Leather (May 24 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127014831):
<p>BTW, I'm really just trying to wrap my head around the use of <code>inhabited</code> and why it's better. I'm not trying to claim mine is universally better or anything. Since I haven't tried to implement it or use it myself, I don't have an intuition for it.</p>

#### [ Johannes Hölzl (May 24 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015010):
<p><code>le_maxi_of_forall</code> is slightly different, as it is about a lower bound. Either <code>s</code> is empty, than you compare it to the default: handling the case where <code>s</code> is empty, <strong>or</strong> where the default value is well defined. In your <code>le_max_of_mem</code> case you show that an element is a lower bound, also there is no difference between non-empty <code>s</code> and <code>b</code> being well defined.</p>

#### [ Sean Leather (May 24 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015170):
<p>Right. But they both deal with a “default,” whether that be <code>b</code> in <code>le_max_of_mem</code> or <code>default β</code> in <code>le_maxi_of_forall</code>. That's the similarity I see.</p>

#### [ Mario Carneiro (May 24 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015318):
<p>I'm not a fan of these <code>inhabited</code> solutions because <code>default</code> is (supposed to be) a completely arbitrary element with no semantic value. It's not supposed to be compared to stuff because in a given structure you have no idea what it could be. If it happens to work out in some type, that should be treated as coincidence and should not be relied on.</p>

#### [ Mario Carneiro (May 24 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015323):
<p>which is why I find the hypothesis <code> s = ∅ → b ≤ default β</code> very strange</p>

#### [ Mario Carneiro (May 24 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127015335):
<p>if you care about having a particular fallback value, there is <code>get_or_else</code> for that</p>

#### [ Patrick Massot (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127197478):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> did you decide something about this <code>max</code> debate? Can I use <a href="https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105" target="_blank" title="https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105">https://gist.github.com/johoelzl/2ea9c95fb3a4773c8da5f63384906105</a> or is it already outdated with respect to current mathlib?</p>

#### [ Johannes Hölzl (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127197858):
<p>I'm not sure yet. I didn't try to write the proof only using the <code>option</code> variant of <code>max</code>. <span class="user-mention" data-user-id="110045">@Sean Leather</span> did you use <code>max</code> already?<br>
But we have a new possibility now: use <code>nnreal</code> to define <code>dist</code> and <code>norm</code> (or maybe <code>nndist</code>). Then we can use <code>sup</code> and don't need to worry about the empty case. It should still easily embed into <code>real</code>.</p>

#### [ Patrick Massot (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127197894):
<p>I don't understand how <code>nnreal</code> could help here</p>

#### [ Sebastien Gouezel (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127198066):
<p>Please, please, please don't use nnreals for dist and norm! I tried to do something like that for Gromov hyperbolic space (except that I needed distances taking the value infinity, so I used ennreal). And then I had to start everything over again using ereal once I was deep enough in the theory, when I had to do serious computations and inequalities, as the fact that subtraction on ennreal (or nnreal, or nat) is truncating things makes everything a total mess -- I think Patrick has been bitten by this quite a few times, right?</p>

#### [ Patrick Massot (May 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127198135):
<p>Oh yes, I don't want more crazy substraction</p>

#### [ Sean Leather (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/minimum%20of%20finite%20set/near/127200413):
<blockquote>
<p>I'm not sure yet. I didn't try to write the proof only using the <code>option</code> variant of <code>max</code>. <span class="user-mention" data-user-id="110045">@Sean Leather</span> did you use <code>max</code> already?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> No, I haven't started using the <code>max</code> in mathlib.</p>


{% endraw %}
