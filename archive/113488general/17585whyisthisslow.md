---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17585whyisthisslow.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [why is this slow?](https://leanprover-community.github.io/archive/113488general/17585whyisthisslow.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 16 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134047650):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span>
<span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">multivariate_polynomial</span>
<span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">associated</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">namespace</span> <span class="n">algebraic_closure</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">k</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">k</span><span class="o">]</span>

<span class="n">def</span> <span class="n">irred</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">p</span> <span class="bp">|</span> <span class="kn">irreducible</span> <span class="n">p</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">big_ring</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">irred</span> <span class="n">k</span><span class="o">)</span> <span class="n">k</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">big_ring</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">comm_ring</span>

<span class="kn">set_option</span> <span class="n">profiler</span> <span class="n">true</span>
<span class="n">def</span> <span class="n">big_ideal</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">big_ring</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">span</span> <span class="err">$</span> <span class="err">⋃</span> <span class="n">p</span> <span class="o">:</span> <span class="n">irred</span> <span class="n">k</span><span class="o">,</span> <span class="o">{</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">eval₂</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="n">p</span><span class="o">)</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="o">}</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">parsing took 0.154ms</span>
<span class="cm">elaboration of big_ideal took 7.53s</span>
<span class="cm">type checking of big_ideal took 9.17ms</span>
<span class="cm">decl post-processing of big_ideal took 11.1ms</span>
<span class="cm">compilation of algebraic_closure.big_ideal took 0.205ms</span>
<span class="cm">-/</span>

<span class="kn">end</span> <span class="n">algebraic_closure</span>
</pre></div>

#### [ Kenny Lau (Sep 16 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134047652):
<p>is there any way to make this faster?</p>

#### [ Kenny Lau (Sep 16 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134047761):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span></p>

#### [ Chris Hughes (Sep 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134048125):
<p>This compiles in no time. I don't know the solution though.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">big_ideal</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">irred</span> <span class="n">k</span><span class="o">)</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">span</span> <span class="err">$</span> <span class="err">⋃</span> <span class="n">p</span> <span class="o">:</span> <span class="n">irred</span> <span class="n">k</span><span class="o">,</span> <span class="o">{</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">eval₂</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="n">p</span><span class="o">)</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Sep 16 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049306):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <span class="user-mention" data-user-id="110044">@Chris Hughes</span> I suspect Chris's span is the wrong one, which means we will have to once again wait for the refactoring</p>

#### [ Kevin Buzzard (Sep 16 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049357):
<p>So what exactly is being refactored? Yeah I am putting "research level" coding on hold at the minute and thinking more about organisational stuff. The question of why it's slow is still of independent interest. What is causing the hold-up? Is it type class inference?</p>

#### [ Kenny Lau (Sep 16 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049370):
<p>if we specify that we're talking about the span as an ideal (which is this case) or that we're talking about the span as a k-module (which is not this case) then it would be more convenient</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049729):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> is this another +1 for saying which ring we're talking about explicitly? </p>
<p>I guess there is also now the option of making the "ideal" version of things into its own little interface -- e.g. ideal.span could mean "the span of this subset of the ring R as an R-module"</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049730):
<p>I would love to be able to debug this sort of thing. Presumably the <code>by exact</code> insertion changes the elaboration strategy somehow. But in my mind this just raises a bunch of questions as to how it's working and how the change makes any difference.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134049731):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">big_ideal&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">big_ring</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">exact</span> <span class="o">(</span><span class="n">span</span> <span class="err">$</span> <span class="err">⋃</span> <span class="n">p</span> <span class="o">:</span> <span class="n">irred</span> <span class="n">k</span><span class="o">,</span> <span class="o">{</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">eval₂</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="n">p</span><span class="o">)</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="o">})</span>
</pre></div>


<p>is much quicker for me and seems to give the same answer.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050085):
<p>Stupid <code>#print notation ⋃</code> gives me a useless answer. I had to grep through the source code to find it's <code>set.Union</code>.</p>

#### [ Chris Hughes (Sep 16 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050127):
<p>So in future presumably <code>span</code> will take the ring as an explicit argument?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050575):
<p>hopefully. Hey I got Kenny's version working quickly:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">big_ideal&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">big_ring</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">span</span> <span class="err">$</span> <span class="err">⋃</span> <span class="n">p</span> <span class="o">:</span> <span class="n">irred</span> <span class="n">k</span><span class="o">,</span> <span class="o">{</span><span class="bp">@</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">eval₂</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="bp">_</span> <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="n">p</span><span class="o">)</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Sep 16 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050576):
<p>I'm hoping that <code>submodule</code> will as well.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050582):
<p>In your polynomial code, <code>module R (polynomial R)</code> takes precedence over <code>module (polynomial R) (polynomial R)</code> making it really difficult to talk about ideals of polynomial rings!</p>

#### [ Chris Hughes (Sep 16 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050723):
<p>Change it then. I didn't really think about that problem when I wrote it.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050770):
<p>rofl</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">big_ideal&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">big_ring</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">span</span> <span class="err">$</span> <span class="err">⋃</span> <span class="n">p</span> <span class="o">:</span> <span class="n">irred</span> <span class="n">k</span><span class="o">,</span> <span class="o">{</span><span class="bp">@</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">eval₂</span> <span class="n">k</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">big_ring</span> <span class="n">k</span><span class="o">)</span> <span class="bp">_</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="bp">_</span> <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="n">p</span><span class="o">)</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">}</span>
</pre></div>


<p>breaks it again -- apparently explictly telling Lean to use <code>big_ring k</code> rather than letting it work it out for itself is a bad idea. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what is going on here?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why%20is%20this%20slow%3F/near/134050855):
<p>Adding <code>instance : is_semiring_hom (mv_polynomial.C : k → big_ring k) := by apply_instance </code> speeds Kenny's original code up a bit.</p>


{% endraw %}
