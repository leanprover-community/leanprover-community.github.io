---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/82089identitytypeandrefl.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [identity type and refl](https://leanprover-community.github.io/archive/113489newmembers/82089identitytypeandrefl.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Shaun Steenkamp (Nov 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147599492):
<p>Is it possible to pattern match on the refl constructor of the identity type (eq.refl) in Lean similar to what one can do in Agda? I tried defining one by pattern matching but it didn't seem to work.</p>

#### [ Mario Carneiro (Nov 13 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147599789):
<p>yes, there are several ways</p>

#### [ Mario Carneiro (Nov 13 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147599806):
<p><code>subst</code> and <code>cases</code> both work, as does the pattern matcher</p>

#### [ Mario Carneiro (Nov 13 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147599845):
<p>note that one side of the equality must be a variable and must participate in the pattern match (be right of the colon) for it to work</p>

#### [ Reid Barton (Nov 13 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147599908):
<p>Can you give an example of code you expect to work but doesn't?</p>

#### [ Shaun Steenkamp (Nov 13 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147599959):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">subst</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">ℓ</span><span class="o">}(</span><span class="n">P</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">ℓ&#39;</span><span class="o">){</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">A</span><span class="o">}</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">P</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">P</span> <span class="n">b</span> <span class="o">:=</span>
  <span class="k">assume</span> <span class="n">p</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">,</span>
  <span class="k">assume</span> <span class="n">x</span> <span class="o">:</span> <span class="n">P</span> <span class="n">a</span><span class="o">,</span>
  <span class="k">show</span> <span class="n">P</span> <span class="n">b</span><span class="o">,</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">p</span> <span class="n">x</span>
</pre></div>

#### [ Shaun Steenkamp (Nov 13 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600005):
<p>works fine</p>

#### [ Shaun Steenkamp (Nov 13 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600010):
<p>but then</p>

#### [ Shaun Steenkamp (Nov 13 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600023):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">subst_const</span>
  <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">ℓ</span><span class="o">}</span>
  <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">ℓ&#39;</span><span class="o">}</span>
  <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">A</span><span class="o">}</span>
  <span class="o">:</span> <span class="bp">Π</span>
  <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span>
  <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">B</span><span class="o">)</span>
  <span class="o">,</span> <span class="c1">---------------------</span>
  <span class="n">subst</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="o">,</span> <span class="n">B</span><span class="o">)</span> <span class="n">p</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span><span class="o">)</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span>
</pre></div>


<p>doesn't work</p>

#### [ Shaun Steenkamp (Nov 13 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600110):
<p>This is something I've used a lot in Agda, and I figured if I try to do some of these "basic" things in Lean that could help me learn it, but I think that maybe I don't understand the basic syntax well enough yet...</p>

#### [ Reid Barton (Nov 13 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600115):
<p>Yes, that is because the requirement "one side of the equality must be a variable and must participate in the pattern match (be right of the colon)" (or in this case, below the colon <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span>) is not met</p>

#### [ Reid Barton (Nov 13 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600331):
<p><code>y</code> needs to move past the colon, and the last line should read <code>| _ (eq.refl _) _ := eq.refl _</code></p>

#### [ Reid Barton (Nov 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600352):
<p>or replace <code>eq.refl _</code> with <code>rfl</code></p>

#### [ Shaun Steenkamp (Nov 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600361):
<p>okay, got it, can I still keep y implicit?</p>

#### [ Shaun Steenkamp (Nov 13 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600498):
<p>it seems I can</p>

#### [ Shaun Steenkamp (Nov 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/identity%20type%20and%20refl/near/147600555):
<p>thank you very much for your help!! ^_^</p>


{% endraw %}
