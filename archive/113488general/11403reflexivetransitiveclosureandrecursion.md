---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11403reflexivetransitiveclosureandrecursion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [reflexive-transitive closure and recursion](https://leanprover-community.github.io/archive/113488general/11403reflexivetransitiveclosureandrecursion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Shachar Itzhaky (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127960102):
<p>Lean has a transitive closure but I want a reflexive-transitive one. So I wrote the following definition:</p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="o">{</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
<span class="kn">variable</span> <span class="n">R</span> <span class="o">:</span> <span class="n">D</span> <span class="bp">-&gt;</span> <span class="n">D</span> <span class="bp">-&gt;</span> <span class="kt">Prop</span>

<span class="kn">inductive</span> <span class="n">rtc</span> <span class="o">:</span> <span class="n">D</span> <span class="bp">-&gt;</span> <span class="n">D</span> <span class="bp">-&gt;</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">s</span><span class="o">,</span> <span class="n">rtc</span> <span class="n">s</span> <span class="n">s</span>
<span class="bp">|</span> <span class="n">step</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">s</span> <span class="n">u</span> <span class="n">t</span><span class="o">),</span> <span class="n">R</span> <span class="n">s</span> <span class="n">u</span> <span class="bp">→</span> <span class="n">rtc</span> <span class="n">u</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">rtc</span> <span class="n">s</span> <span class="n">t</span>
</pre></div>


<p>I was happy that without knowing much Lean upfront, I was able to prove a simple theorem.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">rtc_trans</span> <span class="o">:</span> <span class="k">forall</span> <span class="o">(</span><span class="n">s</span> <span class="n">u</span> <span class="n">t</span> <span class="o">:</span> <span class="n">D</span><span class="o">),</span> <span class="n">rtc</span> <span class="n">R</span> <span class="n">s</span> <span class="n">u</span> <span class="bp">-&gt;</span> <span class="n">rtc</span> <span class="n">R</span> <span class="n">u</span> <span class="n">t</span> <span class="bp">-&gt;</span> <span class="n">rtc</span> <span class="n">R</span> <span class="n">s</span> <span class="n">t</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">s</span> <span class="n">u</span> <span class="n">t</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span> <span class="n">induction</span> <span class="n">H1</span><span class="o">,</span> <span class="o">{</span> <span class="n">exact</span> <span class="n">H2</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">apply</span> <span class="n">rtc</span><span class="bp">.</span><span class="n">step</span><span class="o">,</span> <span class="n">apply</span> <span class="n">H1_a</span><span class="o">,</span> <span class="n">apply</span> <span class="n">H1_ih</span><span class="o">,</span> <span class="n">apply</span> <span class="n">H2</span> <span class="o">}</span>
  <span class="kn">end</span>
</pre></div>


<p>The proof utilizes <code>rtc.drec</code>. Which is fine. But it would be very illustrative to carry out the same proof via a recursive definition. This, however, requires a <code>match</code>, and I was not able to destructure <code>rtc R s t</code> in any way:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">hmm</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">rtc</span> <span class="n">R</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">H</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">rtc</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">true</span><span class="bp">.</span><span class="n">intro</span>
  <span class="bp">|</span> <span class="n">rtc</span><span class="bp">.</span><span class="n">step</span> <span class="n">R</span> <span class="n">u</span> <span class="bp">_</span> <span class="n">su</span> <span class="n">ut</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">true</span><span class="bp">.</span><span class="n">intro</span>
</pre></div>


<p>This fails to typecheck because <code>rtc.refl _ _</code> gets the type <code>rtc R _x _x</code>, which does not unify with <code>rtc R s t</code>. While the error message sounds reasonable, it sounds weird that there is an inductive type that cannot be <code>match</code>ed on. Is there any way around that?</p>

#### [ Kenny Lau (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127960356):
<p>put the hypothesis after the colon and use the equation compiler instead of <code>match</code></p>

#### [ Kenny Lau (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127960364):
<p>put everything after the colon</p>

#### [ Johannes Hölzl (Jun 12 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127960374):
<p>In mahlib we have the reflexive transitive closure: <a href="https://github.com/leanprover/mathlib/blob/master/logic/relation.lean#L61" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/logic/relation.lean#L61">https://github.com/leanprover/mathlib/blob/master/logic/relation.lean#L61</a></p>

#### [ Johannes Hölzl (Jun 12 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127960479):
<p><code>match</code> can do cases on <code>rtc</code> but you need to give it the allowance, e.g. one of <code>s</code> and <code>t</code> in <code>rtc s t</code> should be a variable, and you need to pass this variable into <code>match</code> so that it can change it, a.l.a <code>match s, h : rtc s t where _, rtc.refl _ := ... end</code></p>

#### [ Shachar Itzhaky (Jun 13 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127977723):
<p>Thanks... I know nothing about the equation compiler and I am still struggling with dependent match but at least fixing one side of the rtc to a variable makes sense to me. I am trying to encode a system that has both unfolding rules --- one that unfolds the first step of the path, and one that unfolds the last step. I will probably define those as two inductive Props and prove their equivalence.</p>
<p>What is the meaning of the <code>refl</code> constructor having an empty implicit parameter list <code>{}</code>?</p>

#### [ Andrew Ashworth (Jun 13 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127977878):
<p>it is an instruction to lean to infer the implicit argument from the return type</p>

#### [ Andrew Ashworth (Jun 13 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127977884):
<p>consider </p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">sum</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">inl</span> <span class="o">{}</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">sum</span>
<span class="bp">|</span> <span class="n">inr</span> <span class="o">{}</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">sum</span>
</pre></div>

#### [ Andrew Ashworth (Jun 13 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127977895):
<p>here the empty implicit parameter list is an annotation to infer the type alpha in <code>inl</code> and beta in <code>inr</code></p>

#### [ Andrew Ashworth (Jun 13 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978043):
<p>hrm, maybe not the greatest example since the definition goes through without the brackets anyway...</p>

#### [ Andrew Ashworth (Jun 13 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978175):
<p>ok, if you paste this</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">sum&#39;</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">inl</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">sum&#39;</span>
<span class="bp">|</span> <span class="n">inr</span> <span class="o">{}</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">sum&#39;</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">sum&#39;</span>
</pre></div>

#### [ Andrew Ashworth (Jun 13 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978178):
<p>then you'll see a difference in how lean evaluates the expression</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978234):
<p>Ok, so in fact the <code>{}</code> is for <em>beta</em>  in <code>inl</code> (since alpha is already there).</p>

#### [ Andrew Ashworth (Jun 13 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978248):
<p>oops, haha</p>

#### [ Andrew Ashworth (Jun 13 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978250):
<p>yes</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978257):
<p>How does Lean know that alpha has to be implicit, in inl without the <code>{}</code>?</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978303):
<p>Oh silly me, of course the first parameter is of type alpha.</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978461):
<p>Ok, this was immaterial to the discussion of matches, back to struggling with <code>match s, h : rtc R s t</code> then. Can anyone explain that cryptic line above?</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127978796):
<p>I didn't manage to put the type annotation <code>H : rtc R s t</code> but the match seemed to work even without it, by virtue of having <code>s</code> available to the equation compiler perhaps?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">hmm</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">rtc</span> <span class="n">R</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">s</span><span class="o">,</span> <span class="n">H</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rtc</span><span class="bp">.</span><span class="n">refl</span> <span class="o">:=</span> <span class="k">fun</span> <span class="n">h</span><span class="o">,</span> <span class="n">trivial</span>
  <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rtc</span><span class="bp">.</span><span class="n">step</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">:=</span> <span class="k">fun</span> <span class="n">h</span><span class="o">,</span> <span class="n">trivial</span>
</pre></div>


<p>I am a bit perplexed still by the fact that the match branches have type <code>?? -&gt; true</code> rather than just <code>true</code>...</p>

#### [ Andrew Ashworth (Jun 13 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127979054):
<p>if you had to write out the definition by hand using <code>rtc.drec_on</code> or <code>rtc.rec_on</code>, how would you avoid the first argument? (match uses those under the hood iirc, but somebody correct me if I'm mistaken)</p>

#### [ Andrew Ashworth (Jun 13 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127979117):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">hmm&#39;</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">rtc</span> <span class="n">R</span> <span class="n">s</span> <span class="n">t</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="n">rtc</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">true</span><span class="bp">.</span><span class="n">intro</span><span class="o">)</span>
  <span class="o">(</span><span class="k">by</span> <span class="n">intros</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">true</span><span class="bp">.</span><span class="n">intro</span><span class="o">)</span>
</pre></div>

#### [ Shachar Itzhaky (Jun 13 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127979287):
<p>Yes, it looks like it does — it just clashes somehow with my understanding of Type Theory and CIC (where there is a <code>fix</code> construct).</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127979411):
<p>BTW the compiler seems to make quite a monster out of my small match:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">ReflexiveTransitiveClosure</span><span class="bp">.</span><span class="n">hmm</span><span class="bp">._</span><span class="n">match_1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">D</span> <span class="bp">→</span> <span class="n">D</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">t</span> <span class="bp">_</span><span class="n">a</span> <span class="o">:</span> <span class="n">D</span><span class="o">),</span> <span class="n">rtc</span> <span class="n">R</span> <span class="bp">_</span><span class="n">a</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">true</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">{</span><span class="n">D</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">D</span> <span class="bp">→</span> <span class="n">D</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">t</span> <span class="bp">_</span><span class="n">a</span> <span class="o">:</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="bp">_</span><span class="n">a_1</span> <span class="o">:</span> <span class="n">rtc</span> <span class="n">R</span> <span class="bp">_</span><span class="n">a</span> <span class="n">t</span><span class="o">),</span>
  <span class="n">rtc</span><span class="bp">.</span><span class="n">dcases_on</span> <span class="bp">_</span><span class="n">a_1</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">H_1</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">=</span> <span class="bp">_</span><span class="n">a</span><span class="o">),</span> <span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">a</span> <span class="o">:</span> <span class="n">rtc</span> <span class="n">R</span> <span class="n">t</span> <span class="n">t</span><span class="o">)</span> <span class="o">(</span><span class="n">H_2</span> <span class="o">:</span> <span class="bp">_</span><span class="n">a</span> <span class="bp">==</span> <span class="n">rtc</span><span class="bp">.</span><span class="n">refl</span><span class="o">),</span> <span class="n">id_rhs</span> <span class="n">true</span> <span class="n">trivial</span><span class="o">)</span> <span class="n">H_1</span> <span class="bp">_</span><span class="n">a_1</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">D</span><span class="o">)</span> <span class="o">{</span><span class="n">t_2</span> <span class="o">:</span> <span class="n">D</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">rtc</span> <span class="n">R</span> <span class="bp">_</span><span class="n">a</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">a_1</span> <span class="o">:</span> <span class="n">R</span> <span class="n">u</span> <span class="n">t_2</span><span class="o">)</span> <span class="o">(</span><span class="n">H_1</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">t_2</span><span class="o">),</span>
       <span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a_1</span> <span class="o">:</span> <span class="n">R</span> <span class="n">u</span> <span class="n">t</span><span class="o">)</span> <span class="o">(</span><span class="n">H_2</span> <span class="o">:</span> <span class="bp">_</span><span class="n">a_1</span> <span class="bp">==</span> <span class="n">rtc</span><span class="bp">.</span><span class="n">step</span> <span class="n">u</span> <span class="n">a</span> <span class="n">a_1</span><span class="o">),</span> <span class="n">id_rhs</span> <span class="n">true</span> <span class="n">trivial</span><span class="o">)</span> <span class="n">H_1</span> <span class="n">a_1</span><span class="o">)</span>
    <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="n">t</span><span class="o">)</span>
    <span class="o">(</span><span class="n">heq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="n">a_1</span><span class="o">)</span>
</pre></div>

#### [ Andrew Ashworth (Jun 13 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127979551):
<p>i don't know if this is any prettier to you </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">hmm&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">D</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">rtc</span> <span class="n">R</span> <span class="n">s</span> <span class="n">t</span><span class="o">),</span> <span class="n">true</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">rtc</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">)</span> <span class="o">:=</span> <span class="n">true</span><span class="bp">.</span><span class="n">intro</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">rtc</span><span class="bp">.</span><span class="n">step</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">true</span><span class="bp">.</span><span class="n">intro</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">hmm&#39;</span><span class="bp">._</span><span class="n">main</span>
</pre></div>

#### [ Andrew Ashworth (Jun 13 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127979666):
<p>when I want a definition that unfolds nicely I tend to write it out by hand using the appropriate recursion lemma. If you use the equation compiler as I did above, the main def is somewhat ugly but it generates quite nice ._eqn1, ._eqn2 branches</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127995826):
<p>Yes, I ended up doing that myself, eventually. I found <code>hmm'._main</code> but what are <code>._eqn1</code>, <code>._eqn2</code>?</p>
<p>At any rate, the purpose of this mental exercise was to demonstrate that explicit induction and "normal" recursion coincide, so of course I could write it with <code>rec_on</code> but that would miss the point...</p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127996308):
<p>You can try <code>#print prefix hmm'</code> to see everything starting <code>hmm'.</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/127996316):
<p>although in the back of my mind I think there might be an easier way of just seeing the equation lemmas...</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002149):
<p>I somehow get <code>no declaration starting with prefix 'hmm''</code>.</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002289):
<p>In lean, type ascriptions have required parentheses, it should be <code>(H : rtc R s t)</code> not <code>H : rtc R s t</code></p>

#### [ Shachar Itzhaky (Jun 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002346):
<p>I was convinced I tried that when the original suggestion didn't work... but yeah, parenthesis do the trick! Although, as I said, the definition goes through without the ascription as well.</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002348):
<p>Lean is a bit limited in its ability to do induction on inductive predicates using the equation compiler. I recommend using the <code>induction</code> tactic instead if you have any problems with writing it the way Andrew suggested</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002364):
<p>Yes, I will reiterate: using tactic mode as well as <code>rec_on</code> were pretty smooth. The reason I am in this discussion is that I wanted to demonstrate to my students how induction is just a form of recursion that they know from programming.</p>

#### [ Mario Carneiro (Jun 13 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002429):
<p>I usually point at the type of rec_on, remark that it looks a lot like induction, and then use it to define a recursive function and also prove some property about it</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002441):
<p><span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span> I assume this is "the Lean way" then.</p>

#### [ Mario Carneiro (Jun 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002498):
<p>In the case of an inductive predicate like <code>rtc</code>, it actually can't be used for recursion, since it has small elimination</p>

#### [ Mario Carneiro (Jun 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002499):
<p>it can only be used to prove props</p>

#### [ Mario Carneiro (Jun 13 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002543):
<p>If you put the inductive type in <code>Type</code> though it could</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002564):
<p>Of course. The analogue that I can refer to is that in Coq I wrote the same proof, once with <code>induction</code>, and once with <code>Fixpoint</code> -- of course, since you destructure the <code>Prop</code> inside the def, the function must return a <code>Prop</code>.</p>

#### [ Shachar Itzhaky (Jun 13 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflexive-transitive%20closure%20and%20recursion/near/128002573):
<p>I still see that as a form of recursion though, since it's expressed via <code>Fixpoint</code>.</p>


{% endraw %}
