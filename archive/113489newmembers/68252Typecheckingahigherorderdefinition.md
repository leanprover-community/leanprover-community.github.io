---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/68252Typecheckingahigherorderdefinition.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Type checking a higher order definition](https://leanprover-community.github.io/archive/113489newmembers/68252Typecheckingahigherorderdefinition.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Jul 12 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129508130):
<p>Can someone fix the following definition so that it can be type checked:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">absAll</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">t</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">st</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">),</span> <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">q</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="o">(</span><span class="n">st</span> <span class="n">q</span><span class="o">)))</span><span class="bp">.</span>
</pre></div>

#### [ Simon Hudon (Jul 12 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129508344):
<p>What happens if you write this:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">absAll</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">t</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">st</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">q</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="o">(</span><span class="n">st</span> <span class="n">q</span> <span class="n">i</span><span class="o">)))</span><span class="bp">.</span>
</pre></div>

#### [ Ken Roe (Jul 12 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129509851):
<p>It works--maybe I should file a bug report.</p>

#### [ Simon Hudon (Jul 12 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129509899):
<p>That's not a bug, you made a mistake</p>

#### [ Simon Hudon (Jul 12 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129509927):
<p>The term of the definition has to be a function that takes two parameters (<code>st : t → ℕ → Prop</code> and <code>i : ℕ</code>) and returns a <code>Prop</code> (<code>∀ (q:t), (st q i)</code>)</p>

#### [ Simon Hudon (Jul 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129509976):
<p>You wrote <code>st q</code> which has type <code>ℕ -&gt; Prop</code>. But the body of a <code>∀</code> must be a <code>Prop</code></p>

#### [ Simon Hudon (Jul 12 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129510098):
<p>I encourage you to use typed holes (i.e. <code>_</code>) to explore what are the types expected from you. For instance, look at what Lean tells you when you write the following in your definition:</p>
<ul>
<li><code>(λ (st : t → ℕ → Prop), _)</code></li>
<li><code>(λ (st : t → ℕ → Prop) (i : ℕ), _)</code></li>
<li><code>(λ (st : t → ℕ → Prop) (i : ℕ), (∀ (q:t), _))</code></li>
</ul>

#### [ Simon Hudon (Jul 12 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129510432):
<p>I'm not sure what you're going for but you may prefer this definition:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">absAll</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">st</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="o">(</span><span class="n">q</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="o">(</span><span class="n">st</span> <span class="n">q</span> <span class="n">i</span><span class="o">)</span>
</pre></div>


<p>It is clearer and its equations are nicer too</p>

#### [ Kevin Buzzard (Jul 12 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129521382):
<p>What does "its equations are nicer" mean in this context?</p>
<p>Edit: I think I've answered my own question using <code>#print prefix absAll</code>. I am surprised! I knew that if you defined a fancy inductive type you got a bunch of generated equations, but I don't think I'd internalised that this was happening for just some random definition of a function.</p>
<p>Simon's version gives</p>
<div class="codehilite"><pre><span></span>absAll : Π {t : Type}, (t → ℕ → Prop) → ℕ → Prop
absAll.equations._eqn_1 : ∀ {t : Type} (st : t → ℕ → Prop) (i : ℕ), absAll st i = ∀ (q : t), st q i
</pre></div>


<p>I guess my revised question is why this equation is there at all! It just seems to be the definition of <code>absAll</code>.</p>

#### [ Sean Leather (Jul 12 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129521823):
<blockquote>
<p>I guess my revised question is why this equation is there at all! It just seems to be the definition of <code>absAll</code>.</p>
</blockquote>
<p>If you use <code>simp [absAll]</code>, I believe it uses that equation in the simplifier.</p>

#### [ Kevin Buzzard (Jul 12 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Type%20checking%20a%20higher%20order%20definition/near/129521916):
<p>Aah that would make sense. I don't use <code>simp</code> like this usually -- I am only just beginning to get the hang of what <code>simp</code> does, and now I tend to only feed it equalities (I used to feed it arbitrary strings of symbols which I hoped made sense :-) )</p>


{% endraw %}
