---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/17253orderisowoes.html
---

## Stream: [new members](index.html)
### Topic: [order_iso woes](17253orderisowoes.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Oct 10 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135512696):
<p>I'm trying to generalize <a href="https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L366" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L366">this function</a> (there's a typo, that should be a def not a lemma; nonetheless it works...). I want to prove that an <code>order_iso</code>gives rise to a <code>galois_insertion</code> but I'm stuck on what seems to me to be simple:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">galois_connection</span> <span class="n">order</span><span class="bp">.</span><span class="n">order_iso</span>

<span class="kn">namespace</span> <span class="n">order_iso</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">γ</span><span class="o">]</span>
<span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">oi</span> <span class="o">:</span> <span class="n">order_iso</span> <span class="n">r</span> <span class="n">s</span><span class="o">)</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">implicit</span> <span class="n">true</span>

<span class="kn">theorem</span> <span class="n">to_galois_connection</span> <span class="o">:</span>
  <span class="n">galois_connection</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">)</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">galois_connection</span><span class="bp">;</span>
<span class="n">exact</span> <span class="bp">λ</span> <span class="o">{</span><span class="n">b</span> <span class="n">g</span><span class="o">},</span> <span class="k">calc</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">b</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">g</span> <span class="bp">↔</span>
  <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">b</span><span class="o">)</span> <span class="bp">≤</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">g</span><span class="o">))</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">oi</span><span class="bp">.</span><span class="n">right_inv</span>
<span class="bp">...</span> <span class="bp">↔</span> <span class="n">b</span> <span class="bp">≤</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">g</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="o">{</span> <span class="c1">-- rw oi.ord</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">r</span> <span class="n">b</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">g</span><span class="o">)</span> <span class="bp">↔</span>
    <span class="n">s</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">g</span><span class="o">))</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">@</span><span class="n">order_iso</span><span class="bp">.</span><span class="n">ord</span> <span class="n">β</span> <span class="n">γ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">oi</span> <span class="n">b</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">g</span><span class="o">)),</span>
  <span class="n">change</span> <span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">g</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span> <span class="n">g</span><span class="o">,</span>
  <span class="n">sorry</span> <span class="o">}</span>

<span class="kn">protected</span> <span class="n">def</span> <span class="n">to_galois_insertion</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">γ</span><span class="o">]</span> <span class="o">:</span> <span class="bp">@</span><span class="n">galois_insertion</span> <span class="n">β</span> <span class="n">γ</span> <span class="bp">_</span> <span class="bp">_</span>
  <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">)</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">inv_fun</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">choice</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span> <span class="n">oi</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">gc</span> <span class="o">:=</span> <span class="n">to_galois_connection</span> <span class="n">oi</span><span class="o">,</span>
  <span class="n">le_l_u</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="n">le_of_eq</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">right_inv</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
  <span class="n">choice_eq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">order_iso</span>
</pre></div>


<p>In the tactic state near where I gave up, the only difference I see between the goal and <code>this</code> is that the goal uses ≤ and <code>this</code> uses <code>r</code> and <code>s</code>.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135521752):
<p>This is a job for <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Mario Carneiro (Oct 10 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135521873):
<p>You should be able to use function coercion instead of <code>to_fun</code> and <code>inv_fun</code> everywhere</p>

#### [ Kenny Lau (Oct 10 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525340):
<p>This is ridiculous.</p>

#### [ Kenny Lau (Oct 10 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525381):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">γ</span><span class="o">]</span>
<span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">oi</span> <span class="o">:</span> <span class="n">order_iso</span> <span class="n">r</span> <span class="n">s</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 10 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525382):
<p>game: spot the error</p>

#### [ Mario Carneiro (Oct 10 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525444):
<p>no error?</p>

#### [ Kenny Lau (Oct 10 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525621):
<p>even Mario missed it</p>

#### [ Kenny Lau (Oct 10 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525626):
<p>the correct declaration should be</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">γ</span><span class="o">]</span>
<span class="o">(</span><span class="n">oi</span> <span class="o">:</span> <span class="bp">@</span><span class="n">order_iso</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)</span> <span class="o">(</span><span class="bp">≤</span><span class="o">))</span>
</pre></div>

#### [ Johan Commelin (Oct 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525779):
<p>In particular, this means that <code>order_iso</code> is not what we want it to be.</p>

#### [ Kenny Lau (Oct 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525786):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">galois_connection</span> <span class="n">order</span><span class="bp">.</span><span class="n">order_iso</span>

<span class="kn">namespace</span> <span class="n">order_iso</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">γ</span><span class="o">]</span>
<span class="o">(</span><span class="n">oi</span> <span class="o">:</span> <span class="bp">@</span><span class="n">order_iso</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)</span> <span class="o">(</span><span class="bp">≤</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">to_galois_connection</span> <span class="o">:</span> <span class="n">galois_connection</span> <span class="n">oi</span> <span class="n">oi</span><span class="bp">.</span><span class="n">symm</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">b</span> <span class="n">g</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">ord&#39;</span> <span class="n">oi</span><span class="o">,</span> <span class="n">apply_inverse_apply</span><span class="o">]</span>

<span class="kn">protected</span> <span class="n">def</span> <span class="n">to_galois_insertion</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">galois_insertion</span> <span class="n">β</span> <span class="n">γ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">oi</span> <span class="n">oi</span><span class="bp">.</span><span class="n">symm</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">choice</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span> <span class="n">oi</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">gc</span> <span class="o">:=</span> <span class="n">to_galois_connection</span> <span class="n">oi</span><span class="o">,</span>
  <span class="n">le_l_u</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span><span class="o">,</span> <span class="n">le_of_eq</span> <span class="o">(</span><span class="n">oi</span><span class="bp">.</span><span class="n">right_inv</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
  <span class="n">choice_eq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">order_iso</span>
</pre></div>

#### [ Kenny Lau (Oct 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525822):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> how many of this error do you think are in mathlib?</p>

#### [ Mario Carneiro (Oct 10 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525870):
<p>Oh, I missed the context</p>

#### [ Mario Carneiro (Oct 10 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525877):
<p>I thought you meant those variables don't typecheck</p>

#### [ Mario Carneiro (Oct 10 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525899):
<p>are you saying that this is in mathlib?</p>

#### [ Mario Carneiro (Oct 10 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525974):
<p>I guess there is a tension here between <code>order_iso</code>, which works with explicit relations, and <code>galois_connection</code>, which works with types with a <code>preorder</code> instance</p>

#### [ Kenny Lau (Oct 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525988):
<p>I'm saying that there are errors like this in mathlib</p>

#### [ Mario Carneiro (Oct 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526005):
<p>I'm sure there are, but someone has to notice them first</p>

#### [ Mario Carneiro (Oct 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526012):
<p>if no one notices them then they aren't doing anyone harm</p>

#### [ Johan Commelin (Oct 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526075):
<blockquote>
<p>if no one notices them then they aren't doing anyone harm</p>
</blockquote>
<p>Except that you might think you have formalised something, but it turns out to be something else.</p>

#### [ Mario Carneiro (Oct 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526085):
<p>that's where the fun is</p>

#### [ Johan Commelin (Oct 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526089):
<p>Isn't this exactly related to <a href="#narrow/stream/113488-general/subject/stacks.20project.20.2F.20schemes/near/123090992" title="#narrow/stream/113488-general/subject/stacks.20project.20.2F.20schemes/near/123090992">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/stacks.20project.20.2F.20schemes/near/123090992</a></p>

#### [ Kevin Buzzard (Oct 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135529045):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> , now all the people who bothered to click and investigate are in on the joke, can you paste one line of explanation for those of us that are so busy preparing 1st year lectures that we don't even understand the issue at hand here and would hence prefer it if your comments were less cryptic?</p>

#### [ Kenny Lau (Oct 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135531256):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> basically there are two orders on each type when there should only be one order</p>

#### [ Bryan Gin-ge Chen (Oct 10 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135541695):
<p>Thanks Kenny! I'm glad it turned out to be something simple.</p>


{% endraw %}
