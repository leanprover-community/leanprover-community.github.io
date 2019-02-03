---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/27988reasoningaboutemptysetinlean.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [reasoning about empty set in lean](https://leanprover-community.github.io/archive/113489newmembers/27988reasoningaboutemptysetinlean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Marcus Klaas (Dec 02 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729616):
<p>Hi y'all. Sorry to bother again. I'm having trouble working with the empty set. Specifically, I'd like to prove that a set is not empty whenever I can produce a concrete element of it:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span> <span class="o">}</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>but so far, I haven't been successful. What can I do here?</p>

#### [ Rob Lewis (Dec 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729661):
<p><code>set.ne_empty_of_mem</code> will probably be helpful!</p>

#### [ Rob Lewis (Dec 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729662):
<p>You'll have to import <code>data.set.basic</code> from mathlib.</p>

#### [ Marcus Klaas (Dec 02 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729664):
<p>Thanks! I will try it.</p>

#### [ Kenny Lau (Dec 02 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729714):
<p>no import needed :)</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span> <span class="o">}</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="o">(</span><span class="n">congr_fun</span> <span class="n">H</span> <span class="mi">1</span><span class="o">)</span><span class="bp">.</span><span class="n">mp</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729721):
<p>...says the person with over 1 year's Lean experience ;-)</p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729723):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span> <span class="o">}</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">ne_empty_iff_exists_mem</span><span class="o">,</span>
  <span class="n">use</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">rfl</span><span class="o">,</span> <span class="c1">-- refl doesn&#39;t work!</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729730):
<p><code>refl</code> is really bad at set membership.</p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729783):
<p><code>example (a : ℕ) : a ∈ {x : ℕ | x = a} := by refl -- fails </code></p>

#### [ Reid Barton (Dec 02 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729785):
<p>I wonder whether we could fool it into working somehow</p>

#### [ Marcus Klaas (Dec 02 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729786):
<p>Hmmm I don't seem to have the mathlib tho.. <del>can I install it using elan?</del> I have found a way to do it ^^</p>

#### [ Reid Barton (Dec 02 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729787):
<p>basically by adding what Kevin just wrote as a <code>relfexivity</code> lemma</p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reasoning%20about%20empty%20set%20in%20lean/near/150729838):
<p><span class="user-mention" data-user-id="143658">@Marcus Klaas</span> mathlib is great. It's not just for mathematicians. It has a bunch of useful tactics in, and a whole host of useful data structures. If you work with Lean projects (as I do -- all my files, even scratch files, are within a Lean project) then you can just make mathlib a dependency for that project and then <code>leanpkg upgrade</code> will download mathlib.</p>


{% endraw %}
