---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/70126CoqsProgramtactic.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Coq's Program tactic](https://leanprover-community.github.io/archive/113489newmembers/70126CoqsProgramtactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Wojciech Nawrocki (Dec 16 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151888312):
<p>Is there something akin to Coq's <a href="https://coq.inria.fr/refman/addendum/program.html" target="_blank" title="https://coq.inria.fr/refman/addendum/program.html">Program</a> tactic in Lean? I thought that the equation compiler is basically that, but it seems to fail in the case when it should generate an equality at the type level. In my example:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- type-level list</span>
<span class="kn">inductive</span> <span class="n">InList</span><span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">Z</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L</span> <span class="n">n</span><span class="o">},</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">S</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L</span> <span class="n">n</span> <span class="n">n&#39;</span><span class="o">},</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n&#39;</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n</span>

<span class="c1">-- type of functions that map the list L to natural numbers</span>
<span class="n">def</span> <span class="n">ListMap</span> <span class="o">(</span><span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">ℕ</span>

<span class="n">def</span> <span class="n">id_map</span> <span class="o">{</span><span class="n">L</span><span class="o">}:</span> <span class="n">ListMap</span> <span class="n">L</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span><span class="o">),</span> <span class="n">n</span>

<span class="c1">-- extends m with n</span>
<span class="n">def</span> <span class="n">extend_map</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span><span class="o">:</span> <span class="n">ListMap</span> <span class="n">L</span><span class="o">):</span> <span class="n">ListMap</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span>
<span class="o">:=</span> <span class="bp">λ</span> <span class="n">n&#39;</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n&#39;</span><span class="o">),</span>
  <span class="k">match</span> <span class="n">v</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">InList</span><span class="bp">.</span><span class="n">Z</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- i would like to synthesize n = n&#39; here</span>
  <span class="bp">|</span> <span class="n">InList</span><span class="bp">.</span><span class="n">S</span> <span class="o">:=</span> <span class="n">sorry</span>
  <span class="kn">end</span>
</pre></div>


<p>the <code>match</code> fails with</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="bp">_</span><span class="n">match</span> <span class="n">InList</span><span class="bp">.</span><span class="n">Z</span>
<span class="n">term</span>
  <span class="n">InList</span><span class="bp">.</span><span class="n">Z</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">InList</span> <span class="o">(</span><span class="err">?</span><span class="n">m_1</span> <span class="bp">::</span> <span class="err">?</span><span class="n">m_2</span><span class="o">)</span> <span class="err">?</span><span class="n">m_1</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">InList</span> <span class="o">(</span><span class="n">n</span> <span class="bp">::</span> <span class="n">L</span><span class="o">)</span> <span class="n">n&#39;</span>
</pre></div>

#### [ Kenny Lau (Dec 16 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151888604):
<div class="codehilite"><pre><span></span><span class="c1">-- type-level list</span>
<span class="kn">inductive</span> <span class="n">InList</span><span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">Z</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L</span> <span class="n">n</span><span class="o">},</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">S</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L</span> <span class="n">n</span> <span class="n">n&#39;</span><span class="o">},</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n&#39;</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n</span>

<span class="c1">-- type of functions that map the list L to natural numbers</span>
<span class="n">def</span> <span class="n">ListMap</span> <span class="o">(</span><span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">ℕ</span>

<span class="n">def</span> <span class="n">id_map</span> <span class="o">{</span><span class="n">L</span><span class="o">}:</span> <span class="n">ListMap</span> <span class="n">L</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span><span class="o">),</span> <span class="n">n</span>

<span class="c1">-- extends m with n</span>
<span class="n">def</span> <span class="n">extend_map</span> <span class="o">{</span><span class="n">L</span><span class="o">}</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span><span class="o">:</span> <span class="n">ListMap</span> <span class="n">L</span><span class="o">):</span> <span class="n">ListMap</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span>
<span class="o">:=</span> <span class="bp">λ</span> <span class="n">n&#39;</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n&#39;</span><span class="o">),</span>
  <span class="k">match</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="n">v</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="n">InList</span><span class="bp">.</span><span class="n">Z</span> <span class="o">:=</span> <span class="k">have</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n&#39;</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span> <span class="n">sorry</span>
  <span class="bp">|</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="n">InList</span><span class="bp">.</span><span class="n">S</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">sorry</span>
  <span class="kn">end</span>
</pre></div>

#### [ Wojciech Nawrocki (Dec 16 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889015):
<p>Thank you, I was hoping it could be done automatically, but this is fairly concise :)</p>

#### [ Kenny Lau (Dec 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889146):
<p>no, it is done automatically, <code>have n = n' := rfl</code> is just demonstrating it</p>

#### [ Kenny Lau (Dec 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889151):
<p>if you put an underscore to replace <code>sorry</code> you will see the lemma being <code>n = n</code></p>

#### [ Wojciech Nawrocki (Dec 16 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889297):
<p>Oh indeed, so it seems the compiler will only equate variables which are being matched rather than everything that <code>v</code> in <code>match v with</code> depends on.</p>

#### [ Kenny Lau (Dec 16 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889365):
<p>right</p>

#### [ Wojciech Nawrocki (Dec 16 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151895563):
<p>Hm no that's not right, it generalizes the matched variable and the state I get in</p>
<div class="codehilite"><pre><span></span>  <span class="k">match</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="n">v</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">InList</span><span class="bp">.</span><span class="n">Z</span> <span class="o">:=</span> <span class="k">begin</span>
     <span class="c1">-- state here</span>
  <span class="kn">end</span>
  <span class="bp">|</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="o">(</span><span class="n">InList</span><span class="bp">.</span><span class="n">S</span> <span class="n">h</span><span class="o">)</span> <span class="o">:=</span> <span class="n">n</span>
  <span class="kn">end</span>
</pre></div>


<p>is </p>
<div class="codehilite"><pre><span></span><span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">m</span> <span class="o">:</span> <span class="n">ListMap</span> <span class="n">L</span><span class="o">,</span>
<span class="n">n&#39;</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">v</span> <span class="o">:</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n</span> <span class="bp">::</span> <span class="n">L</span><span class="o">)</span> <span class="n">n&#39;</span><span class="o">,</span>
<span class="bp">_</span><span class="n">match</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="bp">_</span><span class="n">a</span> <span class="bp">_</span><span class="n">a_1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">InList</span> <span class="o">(</span><span class="bp">_</span><span class="n">a</span> <span class="bp">::</span> <span class="n">L</span><span class="o">)</span> <span class="bp">_</span><span class="n">a_1</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="err">⊢</span> <span class="bp">ℕ</span>
</pre></div>


<p>where <code>n</code> and <code>n'</code> are not equal</p>

#### [ Chris Hughes (Dec 16 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151895778):
<p>In this state <code>n</code> and <code>n</code> have both effectively been replaced with <code>_x</code>, it just hasn't cleared the old <code>n</code> and <code>n'</code></p>

#### [ Wojciech Nawrocki (Dec 16 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151896024):
<p>The example posted here is a bit simplified to make sense without context, but basically I need the <code>n</code> and <code>n'</code> to be equal in the type of <code>v</code>, since my obligation for the return value is that they match, and for that I need the "old" values to be <code>_x</code> so that they can be substituted within <code>v</code>.</p>

#### [ Chris Hughes (Dec 16 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151896140):
<p>Can you not use <code>InList.Z</code> instead of <code>v</code>. <code>v</code> isn't a variable any more, since you're dealing with the case <code>v = InList.Z</code></p>

#### [ Wojciech Nawrocki (Dec 16 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151896583):
<p>Sorry, I oversimplified again. The return type is dependent on <code>n</code> and needs to be a value given as an argument to <code>extend_map</code>. A fuller example:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- type-level list</span>
<span class="kn">inductive</span> <span class="n">InList</span><span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">Z</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L</span> <span class="n">n</span><span class="o">},</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">S</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L</span> <span class="n">n</span> <span class="n">n&#39;</span><span class="o">},</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n&#39;</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n</span>

<span class="kn">inductive</span> <span class="n">Foo</span><span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">A</span><span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">Foo</span> <span class="n">n</span>
<span class="bp">|</span> <span class="n">B</span><span class="o">:</span> <span class="n">Foo</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="n">C</span><span class="o">:</span> <span class="n">Foo</span> <span class="mi">2</span>

<span class="c1">-- type of functions that map the list L to dependent `Foo`s in the list</span>
<span class="n">def</span> <span class="n">ListMap</span> <span class="o">(</span><span class="n">L</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Foo</span> <span class="n">n</span>

<span class="n">def</span> <span class="n">id_map</span> <span class="o">{</span><span class="n">L</span><span class="o">}:</span> <span class="n">ListMap</span> <span class="n">L</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="n">InList</span> <span class="n">L</span> <span class="n">n</span><span class="o">),</span> <span class="n">Foo</span><span class="bp">.</span><span class="n">A</span> <span class="n">n</span>

<span class="c1">-- extends m with e</span>
<span class="n">def</span> <span class="n">extend_map</span> <span class="o">{</span><span class="n">L</span> <span class="n">n</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span> <span class="n">Foo</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span><span class="o">:</span> <span class="n">ListMap</span> <span class="n">L</span><span class="o">):</span> <span class="n">ListMap</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span>
<span class="o">:=</span> <span class="bp">λ</span> <span class="n">n&#39;</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n&#39;</span><span class="o">),</span>
  <span class="k">match</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="n">v</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">InList</span><span class="bp">.</span><span class="n">Z</span> <span class="o">:=</span> <span class="bp">_</span> <span class="c1">-- needs to be e and have type `Foo n`, but Lean generalizes to type `Foo _x`</span>
  <span class="bp">|</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="o">(</span><span class="n">InList</span><span class="bp">.</span><span class="n">S</span> <span class="n">h</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
  <span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Dec 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151896987):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">extend_map</span> <span class="o">{</span><span class="n">L</span> <span class="n">n</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span> <span class="n">Foo</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span><span class="o">:</span> <span class="n">ListMap</span> <span class="n">L</span><span class="o">):</span> <span class="n">ListMap</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span>
<span class="o">:=</span> <span class="bp">λ</span> <span class="n">n&#39;</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="n">InList</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">L</span><span class="o">)</span> <span class="n">n&#39;</span><span class="o">),</span>
  <span class="k">match</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="n">v</span><span class="o">,</span> <span class="n">e</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">InList</span><span class="bp">.</span><span class="n">Z</span> <span class="o">:=</span> <span class="n">id</span> <span class="c1">-- needs to be e and have type `Foo n`, but Lean generalizes to type `Foo _x`</span>
  <span class="bp">|</span> <span class="n">n</span><span class="o">,</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="o">(</span><span class="n">InList</span><span class="bp">.</span><span class="n">S</span> <span class="n">h</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
  <span class="kn">end</span>
</pre></div>

#### [ Wojciech Nawrocki (Dec 16 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151897653):
<p>Hm that seems to work 🧙, thanks!</p>


{% endraw %}
