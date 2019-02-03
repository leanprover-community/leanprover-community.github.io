---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59421defusingdot.html
---

## Stream: [general](index.html)
### Topic: [def using dot](59421defusingdot.html)

---


{% raw %}
#### [ Chris Hughes (Apr 05 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124678478):
<p>How does this definition work? </p>
<div class="codehilite"><pre><span></span><span class="n">def</span>  <span class="n">empty</span><span class="bp">.</span><span class="n">elim</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="n">empty</span> <span class="bp">→</span> <span class="n">C</span><span class="bp">.</span>
</pre></div>


<p>What does the dot at the end do? I haven't seen that before.</p>

#### [ Kenny Lau (Apr 05 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124678484):
<p>"it's too obvious I don't even wanna write "rfl""</p>

#### [ Simon Hudon (Apr 05 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124680675):
<p>I don't think that's it. I think it's a definition by pattern matching and <code>empty</code> has no constructors. I haven't seen <code>.</code> used that way before but it looks to me like it signals that we're done with the pattern matching.</p>

#### [ Chris Hughes (Apr 05 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124680900):
<p>How does this notation work in general, for things with constructors?</p>

#### [ Simon Hudon (Apr 05 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124680970):
<p>You mean with the dot or just pattern matching definitions?</p>

#### [ Chris Hughes (Apr 05 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124680993):
<p>With the dot</p>

#### [ Simon Hudon (Apr 05 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681319):
<p>I haven't seen many more examples but I found these:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_succ_le_zero</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">succ</span> <span class="n">n</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">false</span>
<span class="bp">.</span>
<span class="kn">lemma</span> <span class="n">bool</span><span class="bp">.</span><span class="n">ff_ne_tt</span> <span class="o">:</span> <span class="n">ff</span> <span class="bp">=</span> <span class="n">tt</span> <span class="bp">→</span> <span class="n">false</span>
<span class="bp">.</span>
</pre></div>


<p>I think you just put it in instead of a pattern matching to signal that there are no constructors.</p>

#### [ Gabriel Ebner (Apr 05 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681520):
<p>In general the dot is an optional command delimiter, you can always use it if you want:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">|</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="bp">.</span>
</pre></div>

#### [ Gabriel Ebner (Apr 05 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681558):
<p>If you want to write a definition using pattern matching and you have zero equations, then the dot is mandatory.  The examples above have zero equations.</p>

#### [ Gabriel Ebner (Apr 05 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681664):
<p>In case you didn't know, this definition syntax is essentially just sugar for a nested match.  Here it is maybe clearer that there are zero equations:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">ff</span> <span class="bp">=</span> <span class="n">tt</span><span class="o">)</span> <span class="o">:</span> <span class="n">C</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">h</span> <span class="k">with</span> <span class="kn">end</span>
</pre></div>

#### [ Gabriel Ebner (Apr 05 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/def%20using%20dot/near/124681854):
<p>To give you an intuition for when this zero-equation magic works, recall that the equation compiler is (ignoring lots and lots of details) a wrapper around the <code>cases</code> tactic.  Whenever iterated <code>cases</code> would yield zero subgoals, then you can use this magic.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">n</span><span class="o">,</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">0</span><span class="o">)</span><span class="bp">.</span>
</pre></div>


{% endraw %}
