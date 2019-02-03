---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/88592Cantorgolf.html
---

## Stream: [maths](index.html)
### Topic: [Cantor golf](88592Cantorgolf.html)

---


{% raw %}
#### [ Kevin Buzzard (Dec 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151537525):
<p>1) Is there a very short proof of this in Lean / mathlib?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>2) Can anyone golf the mathlib proof of Cantor's Diagonal Argument (using only imports in mathlib):</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">cantor_surjective</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">function</span><span class="bp">.</span><span class="n">surjective</span> <span class="n">f</span> <span class="bp">|</span> <span class="n">h</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">D</span><span class="o">,</span> <span class="n">e</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">h</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">¬</span> <span class="n">f</span> <span class="n">a</span> <span class="n">a</span><span class="o">)</span> <span class="k">in</span>
<span class="o">(</span><span class="n">iff_not_self</span> <span class="o">(</span><span class="n">f</span> <span class="n">D</span> <span class="n">D</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">iff_of_eq</span> <span class="o">(</span><span class="n">congr_fun</span> <span class="n">e</span> <span class="n">D</span><span class="o">)</span>
</pre></div>

#### [ Rob Lewis (Dec 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151537662):
<p>For 1), <code>by tauto!</code>It shouldn't need classical logic but <code>by tauto</code> fails.</p>

#### [ Kevin Buzzard (Dec 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151537663):
<p>My answer to (1):</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">revert</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">generalize</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">cc</span>
<span class="kn">end</span>
</pre></div>


<p>I'm sure something much better will exist.</p>

#### [ Kevin Buzzard (Dec 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151537700):
<p>...and indeed it existed before I even posted! Many thanks Rob!</p>

#### [ Kevin Buzzard (Dec 12 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538379):
<p>Why my code no work?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">open</span> <span class="n">function</span>

<span class="kn">theorem</span> <span class="n">no_bijection_to_power_set&#39;</span>
  <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="n">bijective</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">Hi</span><span class="o">,</span> <span class="n">Hs</span><span class="bp">⟩</span><span class="o">,</span> <span class="c1">-- unexpected occurrence of recursive function error</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">Hs</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">f</span> <span class="n">x</span><span class="o">}</span> <span class="k">with</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">Hconclusion_so_far</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">x</span> <span class="err">∈</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">Hx</span><span class="o">],</span>
      <span class="k">have</span> <span class="n">Hlogical_nonsense</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Hconclusion_so_far</span><span class="o">,</span>
  <span class="n">tauto</span><span class="bp">!</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Dec 12 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538702):
<p>Changing <code>tauto!</code> to <code>sorry</code> fixes the error. Is it a combination of the equation compiler and the tactic? Why is this happening?</p>

#### [ Kevin Buzzard (Dec 12 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538742):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">open</span> <span class="n">function</span>

<span class="kn">theorem</span> <span class="n">no_bijection_to_power_set&#39;</span>
  <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="n">bijective</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">Hb</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">Hi</span><span class="o">,</span><span class="n">Hs</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">Hb</span> <span class="k">in</span> <span class="c1">-- unexpected occurrence of recursive function</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">Hs</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">f</span> <span class="n">x</span><span class="o">}</span> <span class="k">with</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">Hconclusion_so_far</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">x</span> <span class="err">∈</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">Hx</span><span class="o">],</span>
      <span class="k">have</span> <span class="n">Hlogical_nonsense</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Hconclusion_so_far</span><span class="o">,</span>
  <span class="n">tauto</span><span class="bp">!</span>
<span class="kn">end</span>
</pre></div>


<p>Also doesn't work.</p>

#### [ Reid Barton (Dec 12 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538747):
<p>For some reason using lambda with pattern matching like this makes a hypothesis (I think it's called <code>_fun_match</code>) which I guess represents some kind of recursion</p>

#### [ Reid Barton (Dec 12 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538832):
<p>if you use a tactic which tries to apply everything like <code>tauto</code>, it'll try to apply <code>_fun_match</code> and then you get this error</p>

#### [ Reid Barton (Dec 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538880):
<p>Same with let but I think the hypothesis name is different</p>

#### [ Reid Barton (Dec 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538901):
<p>You could use <code>begin rintros \&lt;Hi,Hs\&gt;, cases ...</code></p>

#### [ Kevin Buzzard (Dec 12 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151541033):
<p>I was trying to get out of tactic mode, on this occasion.</p>

#### [ Kevin Buzzard (Dec 12 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151541245):
<p>Here's the game. I have a version of Cantor's theorem in Lean, spelt out so that mathematicians with epsilon Lean experience can still understand it:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- Cantor&#39;s theorem in Lean</span>

<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">open</span> <span class="n">function</span>

<span class="c">/-</span><span class="cm"> Theorem: If X is any type, then there is no bijective function</span>
<span class="cm">   f from X to the power set of X.</span>
<span class="cm">-/</span>
<span class="kn">theorem</span> <span class="n">no_bijection_to_power_set</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">,</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">bijective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- Let f be a function from X to the power set of X</span>
  <span class="n">intro</span> <span class="n">f</span><span class="o">,</span>
  <span class="c1">-- Assume, for a contradiction, that f is bijective</span>
  <span class="n">intro</span> <span class="n">Hf</span><span class="o">,</span>
  <span class="c1">-- f is bijective, so it&#39;s surjective.</span>
  <span class="n">cases</span> <span class="n">Hf</span> <span class="k">with</span> <span class="n">Hi</span> <span class="n">Hs</span><span class="o">,</span>
  <span class="c1">-- it&#39;s also injective, but I don&#39;t even care</span>
  <span class="n">clear</span> <span class="n">Hi</span><span class="o">,</span>
  <span class="c1">-- Let S be the usual cunning set</span>
  <span class="k">let</span> <span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">f</span> <span class="n">x</span><span class="o">},</span>
  <span class="c1">-- What does surjectivity of f say when applied to S?</span>
  <span class="k">have</span> <span class="n">HCantor</span> <span class="o">:=</span> <span class="n">Hs</span> <span class="n">S</span><span class="o">,</span>
  <span class="c1">-- It tells us that there&#39;s x in X with f x = S!</span>
  <span class="n">cases</span> <span class="n">HCantor</span> <span class="k">with</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="c1">-- That means x is in f x if and only if x has is in S.</span>
  <span class="k">have</span> <span class="n">Hconclusion_so_far</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">Hx</span><span class="o">],</span>
  <span class="c1">-- but this means (x ∈ f x) ↔ ¬ (x ∈ f x)</span>
  <span class="k">have</span> <span class="n">Hlogical_nonsense</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Hconclusion_so_far</span><span class="o">,</span>
  <span class="c1">-- automation can now take over.</span>
  <span class="n">tauto</span><span class="bp">!</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>and I was trying to compress it into a term mode function.</p>
<p>I also have the mathlib proof</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">theorem</span> <span class="n">cantor_surjective</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">function</span><span class="bp">.</span><span class="n">surjective</span> <span class="n">f</span> <span class="bp">|</span> <span class="n">h</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">D</span><span class="o">,</span> <span class="n">e</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">h</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">¬</span> <span class="n">f</span> <span class="n">a</span> <span class="n">a</span><span class="o">)</span> <span class="k">in</span>
<span class="o">(</span><span class="n">iff_not_self</span> <span class="o">(</span><span class="n">f</span> <span class="n">D</span> <span class="n">D</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">iff_of_eq</span> <span class="o">(</span><span class="n">congr_fun</span> <span class="n">e</span> <span class="n">D</span><span class="o">)</span>
</pre></div>


<p>and I was attempting to expand this into a tactic mode proof. I could just use rcases, as you say.</p>

#### [ Rob Lewis (Dec 12 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151551702):
<p>You can use <code>simpa using Hlogical_nonsense</code> to avoid the weird <code>tauto</code> behavior, but I guess it doesn't look quite as good when you have to name the hypothesis.</p>


{% endraw %}
