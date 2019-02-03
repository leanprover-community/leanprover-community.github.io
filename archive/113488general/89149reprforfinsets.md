---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89149reprforfinsets.html
---

## Stream: [general](index.html)
### Topic: [repr for finsets](89149reprforfinsets.html)

---


{% raw %}
#### [ Pablo Le Hénaff (Jun 20 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364636):
<p>Is there a way to define a has_repr instance for finsets ?</p>

#### [ Pablo Le Hénaff (Jun 20 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364637):
<p>I would like to run some algorithms with eval</p>

#### [ Sean Leather (Jun 20 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364702):
<p>One option: use <code>finset.sort</code>.</p>

#### [ Pablo Le Hénaff (Jun 20 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364765):
<p>oh ! that's cool, i never noticed it. Thanks</p>

#### [ Sean Leather (Jun 20 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364782):
<p>No problem. If you come up with something useful, please share it with us.</p>

#### [ Simon Hudon (Jun 20 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364852):
<p>do you need a total order to use it? You could probably get rid of that constraint if you convert each element to string and then sorting the result</p>

#### [ Pablo Le Hénaff (Jun 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364936):
<p>yes total order is an assumption. good idea</p>

#### [ Sean Leather (Jun 20 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128364939):
<p>By “get rid of,” you mean push the total order off onto the string, right? That's not a bad idea for all of the constraints.</p>

#### [ Simon Hudon (Jun 20 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365001):
<p>Yes, we need a total order on strings but this is readily available. Basically, what I meant was "weaken the assumptions to make it more generally usable". What are the other constraints?</p>

#### [ Sean Leather (Jun 20 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365019):
<p>Right, that's what I thought. So <code>finset.image</code> to <code>string</code> and <code>finset.sort</code> the result.</p>
<div class="codehilite"><pre><span></span>variables (r : α → α → Prop) [decidable_rel r] [is_trans α r] [is_antisymm α r] [is_total α r]
</pre></div>

#### [ Simon Hudon (Jun 20 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365103):
<p>Not quite. In this situation, <code>α</code> is now <code>string</code> so <code>r</code> is now the linear order on strings.</p>

#### [ Sean Leather (Jun 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365291):
<p>I don't understand. Something like <code>finset.sort (&lt;) ∘ finset.image to_string</code> doesn't work?</p>

#### [ Pablo Le Hénaff (Jun 20 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365353):
<p>there are missing instances for string, they shouldn't be too hard to write</p>

#### [ Simon Hudon (Jun 20 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365478):
<p>Yes it does. But because we're using <code>(&lt;)</code> on string, we have weaker assumptions about <code>α</code> and we can discharge the assumptions about <code>string</code> once and for all. That means that <code>to_repr</code> has type:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_repr</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">has_to_repr</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">-&gt;</span> <span class="n">string</span>
</pre></div>


<p>instead of</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_repr</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">has_to_repr</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_linear_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">-&gt;</span> <span class="n">string</span>
</pre></div>

#### [ Sean Leather (Jun 20 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365628):
<p>That of course depends on how <code>to_string : α → string</code> is defined for your <code>α</code>.</p>

#### [ Pablo Le Hénaff (Jun 20 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365630):
<p>You also need to make sure that  has_repr.to_repr for  \alpha is injective (and maybe use map instead of image)<br>
but that's not so interesting</p>

#### [ Simon Hudon (Jun 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365654):
<p>Interesting, I didn't think of injectivity</p>

#### [ Simon Hudon (Jun 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365661):
<p>You could get around it by first converting to a <code>multiset</code> I think</p>

#### [ Simon Hudon (Jun 20 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128365720):
<p>But injectivity might be a good law to have in <code>has_to_repr</code></p>

#### [ Mario Carneiro (Jun 20 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128380291):
<p>It's a good point that we can sort strings here, I hadn't thought of that. I'll add a has_repr instance for multiset and finset then</p>

#### [ Kevin Buzzard (Jun 20 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128381791):
<p>While you're at it, you could add one for pnat (<code>nat.repr \circ subtype.val</code>)</p>

#### [ Chris Hughes (Jun 20 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128382396):
<p>or <code>subtype.has_repr</code></p>

#### [ Kevin Buzzard (Jun 20 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128382427):
<p>I also made an instance of has_to_string pnat (when I was goofing around with pnat a few weeks ago).</p>

#### [ Chris Hughes (Jun 20 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128382504):
<p>Why were you goofing around with pnat?</p>

#### [ Kevin Buzzard (Jun 20 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/repr%20for%20finsets/near/128382797):
<p>I was trying to get on top of exactly what one should do when defining a new structure in Lean. If I had to define pnat I would start by writing down the definition as a subtype, and then I realised that I would not really know what to do next. So I read pnat.lean quite carefully to try and get a feeling for it. I then read <code>real.lean</code> for the same sort of reason.</p>


{% endraw %}
