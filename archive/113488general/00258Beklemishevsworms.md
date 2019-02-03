---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00258Beklemishevsworms.html
---

## Stream: [general](index.html)
### Topic: [Beklemishev's worms](00258Beklemishevsworms.html)

---


{% raw %}
#### [ Kenny Lau (Dec 31 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev%27s%20worms/near/154084805):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">next_aux</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="bp">-&gt;</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">hd</span> <span class="bp">::</span> <span class="n">tl</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">hd</span> <span class="bp">&lt;</span> <span class="n">N</span> <span class="k">then</span> <span class="mi">0</span> <span class="k">else</span> <span class="n">next_aux</span> <span class="n">tl</span> <span class="bp">+</span> <span class="mi">1</span>

<span class="n">def</span> <span class="n">next</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="bp">-&gt;</span> <span class="n">list</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">::</span> <span class="n">tl</span><span class="o">)</span> <span class="o">:=</span> <span class="n">tl</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">tl</span><span class="o">)</span> <span class="o">:=</span> <span class="k">let</span> <span class="n">index</span> <span class="o">:=</span> <span class="n">next_aux</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">tl</span><span class="o">,</span>
    <span class="n">B</span> <span class="o">:=</span> <span class="n">n</span> <span class="bp">::</span> <span class="n">list</span><span class="bp">.</span><span class="k">take</span> <span class="n">index</span> <span class="n">tl</span><span class="o">,</span>
    <span class="n">G</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">drop</span> <span class="n">index</span> <span class="n">tl</span> <span class="k">in</span>
    <span class="o">((</span><span class="bp">++</span> <span class="n">B</span><span class="o">)</span><span class="err">^</span><span class="o">[</span><span class="n">m</span><span class="bp">+</span><span class="mi">1</span><span class="o">]</span> <span class="n">B</span><span class="o">)</span> <span class="bp">++</span> <span class="n">G</span>

<span class="c1">-- Beklemishev&#39;s worms</span>
<span class="n">def</span> <span class="n">worm_step</span> <span class="o">(</span><span class="n">initial</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">step</span> <span class="o">:</span> <span class="n">nat</span><span class="o">,</span> <span class="n">list</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="o">[</span><span class="n">initial</span><span class="o">]</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">m</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">next</span> <span class="n">m</span> <span class="o">(</span><span class="n">worm_step</span> <span class="n">m</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">range</span> <span class="mi">52</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">worm_step</span> <span class="mi">2</span><span class="o">)</span>

<span class="c1">-- It will terminate</span>
<span class="kn">theorem</span> <span class="n">worm_principle</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">s</span><span class="o">,</span> <span class="n">worm_step</span> <span class="n">n</span> <span class="n">s</span> <span class="bp">=</span> <span class="o">[]</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kenny Lau (Dec 31 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev%27s%20worms/near/154084808):
<p>Try to fill the sorry :P</p>

#### [ Kevin Buzzard (Dec 31 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev%27s%20worms/near/154087365):
<p>It's like Goodstein's theorem. I'd never seen it before. Nice! Is there some proof using ordinals like Goodstein?</p>

#### [ Kevin Buzzard (Dec 31 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev%27s%20worms/near/154087416):
<p>Could you make it so that the proof is <code>dec_trivial</code>?</p>

#### [ Kevin Buzzard (Dec 31 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev%27s%20worms/near/154087424):
<p>add some clever decidability instance</p>

#### [ Mario Carneiro (Dec 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev%27s%20worms/near/154098834):
<p>Not really. (See <a href="https://www.researchgate.net/publication/27709556_The_Worm_principle" target="_blank" title="https://www.researchgate.net/publication/27709556_The_Worm_principle">https://www.researchgate.net/publication/27709556_The_Worm_principle</a> for the original proof that this function terminates.) You can make any theorem provable by <code>dec_trivial</code> because if it's provable then it's decidable, but the really important part of this argument is the well-foundedness of a particular order. I would suggest mapping to <code>onote</code></p>

#### [ Mario Carneiro (Jan 01 2019 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev%27s%20worms/near/154106468):
<p>Here's the ordinal function:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">build_aux</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">nat</span> <span class="bp">×</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">((</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span> <span class="k">let</span> <span class="o">(</span><span class="n">l&#39;</span><span class="o">,</span> <span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="n">build_aux</span> <span class="n">l</span> <span class="k">in</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">l&#39;</span><span class="o">,</span> <span class="n">L</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span> <span class="k">let</span> <span class="o">(</span><span class="n">l&#39;</span><span class="o">,</span> <span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="n">build_aux</span> <span class="n">l</span> <span class="k">in</span> <span class="o">([],</span> <span class="n">l&#39;</span> <span class="bp">::</span> <span class="n">L</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="o">([],</span> <span class="o">[])</span>

<span class="n">def</span> <span class="n">build</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">let</span> <span class="o">(</span><span class="n">l&#39;</span><span class="o">,</span> <span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="n">build_aux</span> <span class="n">l</span> <span class="k">in</span> <span class="n">l&#39;</span> <span class="bp">::</span> <span class="n">L</span>

<span class="kn">theorem</span> <span class="n">build_lt</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">build</span> <span class="n">l</span><span class="o">,</span> <span class="n">sizeof</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">sizeof</span> <span class="n">l</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span><span class="n">ω</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">ordinal</span><span class="bp">.</span><span class="n">omega</span>
<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">map</span> <span class="o">:</span> <span class="n">list</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">ordinal</span> <span class="bp">|</span> <span class="n">l</span> <span class="o">:=</span>
<span class="k">if</span> <span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="n">l</span><span class="bp">.</span><span class="n">length</span> <span class="k">else</span>
<span class="n">list</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span> <span class="n">ω</span> <span class="err">^</span> <span class="n">map</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">build</span> <span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="n">build_lt</span> <span class="n">l</span><span class="o">))</span>
</pre></div>


{% endraw %}
