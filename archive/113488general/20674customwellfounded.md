---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20674customwellfounded.html
---

## Stream: [general](index.html)
### Topic: [custom well-founded](20674customwellfounded.html)

---


{% raw %}
#### [ Kenny Lau (Apr 19 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289818):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">bnot</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">x</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="o">(</span><span class="n">x</span><span class="o">,</span> <span class="n">bnot</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span><span class="o">)</span>
</pre></div>


<p>How do I tell Lean that whenever <code>red.step L1 L2</code> is true, it is also true that <code>list.sizeof L2 &lt; list.sizeof L1</code>?</p>

#### [ Kenny Lau (Apr 19 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289821):
<p>I don't want to provide a custom proof at the end of every recursion</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289871):
<p>You could prove that <code>red.step</code> itself is well-founded...</p>

#### [ Kenny Lau (Apr 19 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289872):
<p>it's in the wrong direction though</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289874):
<p><code>swap red.step</code> then</p>

#### [ Kenny Lau (Apr 19 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289890):
<p>what is swap?</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289892):
<p>exactly what it sounds like</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289895):
<p>it's defined in <code>init.function</code> and swaps a binary operator (aka relation converse)</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289937):
<p>oh, I guess it is in <code>function</code> ns</p>

#### [ Kenny Lau (Apr 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289939):
<p>right</p>

#### [ Kenny Lau (Apr 19 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289940):
<p>so if I prove that <code>swap red.step</code> is well-founded, then I won't have to worry about anything?</p>

#### [ Kenny Lau (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289987):
<p>do you suppose I prove <code>has_well_founded (list (α × bool))</code>?</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289991):
<p>No, except perhaps locally if you like</p>

#### [ Kenny Lau (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289993):
<p>I mean, is it <code>has_well_founded (list (α × bool))</code> that I should prove?</p>

#### [ Kenny Lau (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289994):
<p>and then I can use recursion?</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125289995):
<p>yes</p>

#### [ Kenny Lau (Apr 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290000):
<p>because "prove well-founded" is kinda vague of an instruction</p>

#### [ Mario Carneiro (Apr 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290004):
<p>you can also define a <code>well_founded</code> proof and then refer to it in your wf definition using <code>using_well_founded</code></p>

#### [ Mario Carneiro (Apr 19 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290010):
<p>there are several examples of that in mathlib, just look for the keyword</p>

#### [ Kenny Lau (Apr 19 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290053):
<p>as I said, I don't want to write a custom proof at the end of every recursion</p>

#### [ Kenny Lau (Apr 19 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290054):
<p>I will be doing recurison much</p>

#### [ Kenny Lau (Apr 19 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290109):
<p>how would I prove that <code>red.step</code> is well-founded?</p>

#### [ Kenny Lau (Apr 19 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290113):
<p>I don't know how to use list lengths to prove that it is well-founded</p>

#### [ Johannes Hölzl (Apr 19 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125290273):
<p>my first idea would be to use <code>subrelation.wf</code> and <code>inv_image.wf</code>.</p>

#### [ Kenny Lau (Apr 19 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291560):
<div class="codehilite"><pre><span></span><span class="n">H1</span> <span class="o">:</span> <span class="n">step</span> <span class="n">L₁</span> <span class="n">L₄</span><span class="o">,</span>
<span class="err">⊢</span> <span class="n">function</span><span class="bp">.</span><span class="n">swap</span> <span class="n">step</span> <span class="n">L₄</span> <span class="n">L₁</span>
</pre></div>

#### [ Kenny Lau (Apr 19 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291563):
<p>Lean's automater couldn't match this with "assumption"</p>

#### [ Kenny Lau (Apr 19 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291564):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Apr 19 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291620):
<p>try <code>exact this</code> as the tactic instead</p>

#### [ Kenny Lau (Apr 19 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291756):
<p>can I not change the tactic ;_;</p>

#### [ Kenny Lau (Apr 19 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291845):
<p>Now I used <code>λ L₁ L₂, red.step L₂ L₁</code> as the well-founded relation instead and Lean is giving me ths ;_;</p>

#### [ Kenny Lau (Apr 19 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291850):
<div class="codehilite"><pre><span></span><span class="k">match</span> <span class="n">failed</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="n">L₃</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">red</span><span class="bp">.</span><span class="n">trans</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="bp">_</span><span class="n">p</span> <span class="o">:</span> <span class="err">Σ&#39;</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₂</span><span class="o">),</span> <span class="n">red</span> <span class="n">L₂</span> <span class="n">L₃</span><span class="o">),</span> <span class="n">red</span> <span class="o">(</span><span class="bp">_</span><span class="n">p</span><span class="bp">.</span><span class="n">fst</span><span class="o">)</span> <span class="n">L₃</span><span class="o">,</span>
<span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">),</span>
<span class="n">H1</span> <span class="o">:</span> <span class="n">step</span> <span class="n">L₁</span> <span class="n">L₄</span><span class="o">,</span>
<span class="n">H2</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₄</span> <span class="n">L₂</span><span class="o">,</span>
<span class="n">H23</span> <span class="o">:</span> <span class="n">red</span> <span class="n">L₂</span> <span class="n">L₃</span>
<span class="err">⊢</span> <span class="n">step</span> <span class="n">L₁</span> <span class="n">L₄</span>
</pre></div>

#### [ Kenny Lau (Apr 19 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291860):
<p>keru mouri</p>

#### [ Kenny Lau (Apr 19 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291948):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> sauva mi</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291962):
<p>You should use <code>using_well_founded</code> like I said</p>

#### [ Kenny Lau (Apr 19 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291996):
<p>I don’t want to use it after every single recursion ;_;</p>

#### [ Mario Carneiro (Apr 19 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125291997):
<p>it's just one line, which you can copy around</p>

#### [ Chris Hughes (Apr 20 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125467953):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">red</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">axiom</span> <span class="n">red_length</span> <span class="o">(</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">red</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="bp">→</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">length</span> <span class="bp">&lt;</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">length</span>

<span class="kn">lemma</span> <span class="n">red_well_founded</span> <span class="o">:</span> <span class="n">well_founded</span> <span class="o">(</span><span class="bp">@</span><span class="n">red</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">subrelation</span><span class="bp">.</span><span class="n">wf</span> <span class="n">red_length</span>
<span class="o">(</span><span class="n">measure_wf</span> <span class="n">list</span><span class="bp">.</span><span class="n">length</span><span class="o">)</span>
</pre></div>


<p>This might help if you haven't already worked it out.</p>

#### [ Kenny Lau (Apr 21 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125473548):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> thanks, but it still bugs me to provide a proof of well-foundedness</p>

#### [ Kenny Lau (Apr 21 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20well-founded/near/125473597):
<p>so in the end I proved</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">sizeof</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)},</span> <span class="n">red</span><span class="bp">.</span><span class="n">step</span> <span class="n">L₁</span> <span class="n">L₂</span> <span class="bp">→</span> <span class="n">L₂</span><span class="bp">.</span><span class="n">sizeof</span> <span class="bp">&lt;</span> <span class="n">L₁</span><span class="bp">.</span><span class="n">sizeof</span>
</pre></div>


<p>and then in recursions I do:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">red</span><span class="bp">.</span><span class="n">append</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="n">L₄</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">bool</span><span class="o">)},</span>
  <span class="n">red</span> <span class="n">L₁</span> <span class="n">L₃</span> <span class="bp">→</span> <span class="n">red</span> <span class="n">L₂</span> <span class="n">L₄</span> <span class="bp">→</span> <span class="n">red</span> <span class="o">(</span><span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span><span class="o">)</span> <span class="o">(</span><span class="n">L₃</span> <span class="bp">++</span> <span class="n">L₄</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span> <span class="o">:=</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">red</span><span class="bp">.</span><span class="n">step_trans</span> <span class="n">H3</span> <span class="n">H4</span><span class="o">)</span> <span class="o">:=</span> <span class="k">have</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">red</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">H3</span><span class="o">,</span>
  <span class="n">red</span><span class="bp">.</span><span class="n">step_trans</span> <span class="o">(</span><span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">append_left</span> <span class="n">H3</span><span class="o">)</span> <span class="o">(</span><span class="n">red</span><span class="bp">.</span><span class="n">append</span> <span class="n">red</span><span class="bp">.</span><span class="n">refl</span> <span class="n">H4</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">red</span><span class="bp">.</span><span class="n">step_trans</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">)</span> <span class="n">H3</span> <span class="o">:=</span> <span class="k">have</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">red</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">red</span><span class="bp">.</span><span class="n">step_trans</span> <span class="o">(</span><span class="n">red</span><span class="bp">.</span><span class="n">step</span><span class="bp">.</span><span class="n">append_right</span> <span class="n">H1</span><span class="o">)</span> <span class="o">(</span><span class="n">red</span><span class="bp">.</span><span class="n">append</span> <span class="n">H2</span> <span class="n">H3</span><span class="o">)</span>
</pre></div>


{% endraw %}
