---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/43083indirectrecursioncheck.html
---

## Stream: [new members](index.html)
### Topic: [indirect recursion check](43083indirectrecursioncheck.html)

---


{% raw %}
#### [ Scott Olson (Sep 27 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134713724):
<p>A while ago I was porting some code from Coq to Lean and it was going very well, but there was one definition that reduces to something like this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">bool</span> <span class="o">:=</span>
    <span class="n">f</span> <span class="n">n</span>

<span class="n">def</span> <span class="n">bar</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">foo</span> <span class="n">bar</span> <span class="n">n</span>
</pre></div>


<p>I get "unexpected occurrence of recursive function" on <code>bar</code>. Is there any way to make this kind of definition work, and prove termination? I'm actually kind of surprised it worked in Coq in the first place...</p>

#### [ Scott Olson (Sep 27 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134713786):
<p>Effectively, you need to prove that <code>foo</code> only calls <code>bar</code> with something smaller than <code>n+1</code>, which it does in this case. Maybe it's technically possible, but the equation compiler in particular doesn't support it?</p>

#### [ Simon Hudon (Sep 27 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134717621):
<p>It this example, you can inline <code>foo</code> but I assume that's not an option with what you're working on ...</p>

#### [ Simon Hudon (Sep 27 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134717700):
<p>Otherwise, you can make <code>foo</code> and <code>bar</code> into mutually recursive functions</p>

#### [ Scott Olson (Sep 27 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134719571):
<p>It is possible but inconvenient to inline <code>foo</code> in the real code. It turned out more convenient to use a different approach to defining <code>bar</code> entirely.</p>
<p>When I try a mutually recursive approach, I still get the same "unexpected occurrence of recursive function" error (which comes from the pattern compiler, I assume):</p>
<div class="codehilite"><pre><span></span><span class="n">mutual</span> <span class="n">def</span> <span class="n">foo</span><span class="o">,</span> <span class="n">bar</span>
<span class="k">with</span> <span class="n">foo</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">f</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">n</span>
<span class="k">with</span> <span class="n">bar</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">foo</span> <span class="n">bar</span> <span class="n">n</span>
</pre></div>

#### [ Scott Olson (Sep 27 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134719682):
<p>When I find the time, I'll look up the original Coq example again for comparison.</p>

#### [ Mario Carneiro (Sep 27 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134719755):
<p>the idea is to define <code>bar</code> and <code>foo bar</code> by mutual recursion</p>

#### [ Mario Carneiro (Sep 27 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134719758):
<p>so you wouldn't have that first parameter in <code>foo</code></p>

#### [ Simon Hudon (Sep 27 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134719838):
<p>What Mario said</p>

#### [ Simon Hudon (Sep 27 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720141):
<p>So that would look like:</p>
<div class="codehilite"><pre><span></span><span class="n">mutual</span> <span class="n">def</span> <span class="n">foo</span><span class="o">,</span> <span class="n">bar</span>
<span class="k">with</span> <span class="n">foo</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">bar</span> <span class="n">n</span> <span class="c1">-- this will be trouble because `n` doesn&#39;t decrease</span>
<span class="k">with</span> <span class="n">bar</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">foo</span> <span class="n">n</span>
</pre></div>

#### [ Scott Olson (Sep 27 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720156):
<p>Hmm, I suspect I still haven't fully understood, but here's my latest attempt:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- (To be clear this is elsewhere, can&#39;t be changed, inconvenient to inline.)</span>
<span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">bool</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">n</span>

<span class="n">mutual</span> <span class="n">def</span> <span class="n">foo_bar</span><span class="o">,</span> <span class="n">bar</span>
<span class="k">with</span> <span class="n">foo_bar</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">foo</span> <span class="n">bar</span> <span class="n">n</span>
<span class="k">with</span> <span class="n">bar</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="n">true</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">foo_bar</span> <span class="n">n</span>
</pre></div>


<p>Which has the same "unexpected occurrence of recursive function" message.</p>

#### [ Mario Carneiro (Sep 27 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720226):
<p>that is trouble, because you need to know that <code>foo</code> doesn't look at future values of <code>bar</code></p>

#### [ Scott Olson (Sep 27 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720245):
<p>Yeah, it's definitely fair for Lean to reject it. I think I'll come back to this thread when I've found the Coq example to compare with</p>

#### [ Mario Carneiro (Sep 27 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720292):
<p>One option, used with things like <code>list.map</code>, is to use a theorem like <code>map_congr</code> to acquire an assumption that is needed for the recursion, or use a partial function like <code>list.pmap</code></p>

#### [ Scott Olson (Sep 27 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720313):
<p>I <em>think</em> the difference is Coq allowed the code with an explicit termination proof, whereas Lean's equation compiler won't even touch it</p>

#### [ Scott Olson (Sep 27 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720318):
<p>Unlike simpler examples where you just need to prove something is decreasing</p>

#### [ Mario Carneiro (Sep 27 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720321):
<p>lean allows explicit termination proofs, but you have to thread the proof through in a kind of awkward way</p>

#### [ Mario Carneiro (Sep 27 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720365):
<p>I would need a more concrete example to demonstrate</p>

#### [ Scott Olson (Sep 27 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/indirect%20recursion%20check/near/134720386):
<p>I've got to head out for now but I'll come back to this with more details</p>


{% endraw %}
