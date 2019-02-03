---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/02213DoesLeancontainnumericalbases.html
---

## Stream: [new members](index.html)
### Topic: [Does Lean contain numerical bases?](02213DoesLeancontainnumericalbases.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 10 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147407947):
<p>Specifically, I want a way to extract the base-n digits of a number as a list. Does this already exist?</p>

#### [ Andrew Ashworth (Nov 10 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147408048):
<p>that seems pretty specialized, so i doubt it</p>

#### [ Kenny Lau (Nov 10 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147408056):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="n">nat</span><span class="bp">.</span><span class="n">to_digits</span> <span class="mi">2</span> <span class="mi">100</span> <span class="c1">--[0, 0, 1, 0, 0, 1, 1]</span>
</pre></div>

#### [ Andrew Ashworth (Nov 10 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147408061):
<p>woah, i'm wrong</p>

#### [ Chris Hughes (Nov 10 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147408167):
<p>That's just there so numerals can be printed and parsed.</p>

#### [ Bryan Gin-ge Chen (Nov 10 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147410490):
<p><a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/repr.lean#L77" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/repr.lean#L77">Here it is in core lean</a>. As a newbie to functional programming, I thought this was super cool.</p>

#### [ Kevin Buzzard (Nov 10 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147411489):
<p>oh so that's how <code>repr</code> works :-)</p>

#### [ Kevin Buzzard (Nov 10 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147411727):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">nat</span><span class="bp">.</span><span class="n">repr2</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">string</span> <span class="o">:=</span>
<span class="o">((</span><span class="n">nat</span><span class="bp">.</span><span class="n">to_digits</span> <span class="mi">2</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="n">nat</span><span class="bp">.</span><span class="n">digit_char</span><span class="o">)</span><span class="bp">.</span><span class="n">reverse</span><span class="bp">.</span><span class="n">as_string</span>

<span class="bp">@</span><span class="o">[</span><span class="n">priority</span> <span class="mi">10000</span><span class="o">]</span>
<span class="kn">instance</span> <span class="n">nat</span><span class="bp">.</span><span class="n">has_repr2</span> <span class="o">:</span> <span class="n">has_repr</span> <span class="n">nat</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">nat</span><span class="bp">.</span><span class="n">repr2</span><span class="bp">⟩</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="mi">7</span> <span class="c1">-- 111</span>
</pre></div>


<p>woo I have binary Lean!</p>

#### [ Chris Hughes (Nov 10 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147412552):
<p>Hide that in xenalib somwhere and confuse everyone.</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 10 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147431978):
<blockquote>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="n">nat</span><span class="bp">.</span><span class="n">to_digits</span> <span class="mi">2</span> <span class="mi">100</span> <span class="c1">--[0, 0, 1, 0, 0, 1, 1]</span>
</pre></div>


</blockquote>
<p>Nice!</p>

#### [ Kevin Buzzard (Nov 10 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147432166):
<p>The way to find it is to think "hmm, how are naturals being printed?" then "hmm, what is the definition of <code>nat.repr</code>?"</p>


{% endraw %}
