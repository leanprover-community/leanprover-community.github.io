---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03982Universeissues.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Universe issues](https://leanprover-community.github.io/archive/113488general/03982Universeissues.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 06 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734232):
<p>I seem to not understand universes properly, or more precisely how to use them properly. I ran into the following issue with some code:</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734247):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">foo</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">),</span> <span class="n">true</span>

<span class="kn">theorem</span> <span class="n">baz</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">bar</span><span class="o">:</span> <span class="n">foo</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">bar</span> <span class="n">β</span><span class="o">,</span> <span class="c1">-- error</span>
  <span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 06 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734249):
<p>The error was</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734254):
<div class="codehilite"><pre><span></span>type mismatch at application
  bar β
term
  β
has type
  Type u_3 : Type (u_3+1)
but is expected to have type
  Type u_2 : Type (u_2+1)
state:
X : Type u_1,
bar : foo X,
β : Type u_3
⊢ true
</pre></div>

#### [ Kevin Buzzard (Apr 06 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734270):
<p>I figured I'd investigate more, so I next wrote this:</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734321):
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span> <span class="n">x</span>
<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">universes</span> <span class="n">true</span>
<span class="kn">definition</span> <span class="n">foo&#39;</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">),</span> <span class="n">true</span>
<span class="kn">theorem</span> <span class="n">baz&#39;</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span> <span class="o">(</span><span class="n">bar&#39;</span> <span class="o">:</span> <span class="n">foo&#39;</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">bar&#39;</span> <span class="n">β</span><span class="o">,</span> <span class="c1">-- error</span>
  <span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 06 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734337):
<p>and this time I got</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734344):
<div class="codehilite"><pre><span></span>type mismatch at application
  bar&#39; β
term
  β
has type
  Type x : Type (x+1)
but is expected to have type
  Type u_1 : Type (u_1+1)
state:
X : Type w,
bar&#39; : foo&#39;.{w u_1} X,
β : Type x
⊢ true
</pre></div>

#### [ Kevin Buzzard (Apr 06 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734362):
<p>This made me realise that I didn't understand what was going on, because there is still this universe <code>u_1</code> mentioned, even though I thought I'd just explicitly written down what universe everything was in.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734377):
<p>In particular, <code>bar'</code> seems to mention this universe <code>u_1</code> and I'm not sure where this universe got involved.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734425):
<p>Some experimentation led me to something which worked:</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734429):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">foo&#39;&#39;</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">),</span> <span class="n">true</span>

<span class="kn">theorem</span> <span class="n">baz&#39;&#39;</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">(</span><span class="n">bar&#39;&#39;</span> <span class="o">:</span> <span class="n">foo&#39;&#39;</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">bar&#39;&#39;</span> <span class="n">β</span><span class="o">,</span> <span class="c1">-- works</span>
  <span class="n">exact</span> <span class="n">H</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 06 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734435):
<p>i.e. "keep X and beta in the same universe and you'll be fine"</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734441):
<p>But this raises two questions for me:</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734444):
<p>1) why wasn't I fine before?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734450):
<p>2) Will this fix cause me problems later?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734513):
<p>In reality, X is a topological space and it is covered by open sets <code>U i</code> where each <code>i</code> has type <code>beta</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734523):
<p>that is, <code>U : beta -&gt; set X</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734570):
<p>My instinct is always to just let everything live in different universes because who cares about universes anyway, that's the joy of type theory</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734615):
<p>In ZFC I would just let X and beta be in Type</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734623):
<p>but that might be a bridge too far</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734636):
<p>When you defined <code>foo</code>, it had two universe parameters, corresponding to the two <code>Type*</code> instances</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734672):
<p>what does that even mean</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734676):
<p>foo is a thing</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734677):
<p>and it has a type</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734681):
<p>which lives in a universe</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734686):
<p>it is universe polymorphic</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734733):
<p>Think of it as being implicitly a forall over the universe variables</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734745):
<p>except that lean has no universe variable binders, so it's all just free variables and substitution</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734749):
<p><code>foo'</code> mentions a universe I don't even see</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734760):
<p>or at least something mentions this universe</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734763):
<p><code>foo</code> and <code>foo'</code> are the same</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734774):
<p>wait</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734777):
<p>are they exactly the same?</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734780):
<p>except <code>foo'</code> is more explicit about the two universe variables, <code>u</code> and <code>v</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734790):
<p>Should I think that <code>foo'</code> is really "for all universes u, ..."</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734791):
<p>yes, they are exactly the same as far as lean is concerned</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734842):
<p>yes. All universe polymorphic functions are like this</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734852):
<p>like when I make variables and then secretly I am writing "for all v..."</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734853):
<p>exactly</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734858):
<p>But where is this <code>u_1</code> coming from?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734860):
<p>Didn't I name all my universes with <code>foo'</code>?</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734877):
<p><code>foo'</code> has two universe variables, named <code>u</code> and <code>v</code> in the definition, but since it's like a forall, whenever you use it these variables can be substituted for other things</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734880):
<p>gotcha</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734925):
<p>So <code>foo'</code> is <code>for all universes u and v, [what I wrote]</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734930):
<p>so why do I get a problem?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734932):
<p>why can't we just do universe unification or something?</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734940):
<p><code>u_1</code> is the name of a universe variable in <code>baz'</code>, since you reference <code>foo' X</code> which only fixes its first parameter by unification, lean invents a second variable <code>u_1</code> so it becomes <code>bar' : foo'.{w u_1} X</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734953):
<p>aah</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734955):
<p>yes I just independently realised this</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124734965):
<p>But now <code>bar'</code> should be "for all universes u_1, ..."</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735011):
<p>it is</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735027):
<p><code>bar'.{w x u_1}</code> has type <code>forall (X : Type w) (bar' : foo'.{w u_1} X) (β : Type x), true</code></p>

#### [ Mario Carneiro (Apr 06 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735048):
<p>And since <code>u_1</code> and <code>x</code> are separate universe variables being generalized, inside the proof you can't assume they are equal</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735061):
<p>so <code>bar' β</code> is a type error since <code>bar'</code> accepts a <code>Type u_1</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735108):
<p>OK so you have convinced me that the underlying way that universes work mean that my initial attempts should not work.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735113):
<p>So now the question is should I try to re-arrange things to make them work?</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735122):
<p>just write <code>foo'.{w x}</code> instead of <code>foo'</code> in the type of <code>bar'</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735127):
<p>Or should I go down the "might bite me later and I have no understanding as to whether it will" route of letting all universes be u</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735130):
<p>aah, oh great, so I can do what I want to do.</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735186):
<p>In general, I try to avoid types with "internal universe variables" like <code>foo'</code> here, which has a forall whose universe is not constrained by the input parameters</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735198):
<div class="codehilite"><pre><span></span><span class="kn">definition</span>  <span class="n">foo&#39;</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span>  <span class="bp">∀</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">),</span> <span class="n">true</span>

<span class="kn">theorem</span>  <span class="n">baz&#39;</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">bar&#39;</span> <span class="o">:</span> <span class="n">foo&#39;</span><span class="bp">.</span><span class="o">{</span><span class="n">w</span> <span class="n">x</span><span class="o">}</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">bar&#39;</span> <span class="n">β</span><span class="o">,</span> <span class="c1">-- works :-)</span>
<span class="n">exact</span> <span class="n">H</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 06 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735206):
<p>I need to think about the last thing you said</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735215):
<p>that means to prefer <code>def foo' (X : Type u) := ∀ (β : Type u), true</code> over <code>def foo' (X : Type u) := ∀ (β : Type v), true</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735219):
<p>because this is a massively minimised thing and in reality I will have to decide whether I can try to avoid the thing you want me to avoid</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735225):
<p>Thanks a lot for the fix and the advice though.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735281):
<p>How do I know whether the thing you prefer will be safe for me?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735290):
<p>hmm, I need to go and feed children</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735295):
<p>thanks</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735417):
<p>It is slightly less universe parametric (it requires that two variables be the same), so you may need extra <code>ulift</code>s around, which may or may not be better than the often required <code>.{w x}</code> stuff that arises with this approach</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735479):
<p>Generally you will have to be "universe conscious" when working with definitions with internal universe variables - lots of things will require annotation. <code>cardinal</code>, <code>ordinal</code>, and <code>Set</code> (the ZFC sets) are like this</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/124735490):
<p><code>category</code> may also be, this exact thing was a point of discussion with Scott a few weeks ago</p>

#### [ Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942604):
<p>What is happening here:</p>

#### [ Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942641):
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>

<span class="kn">structure</span> <span class="n">scheme</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">scheme_of_affine_scheme</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">scheme</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">R</span> <span class="c1">-- universe issue</span>
<span class="o">}</span>

<span class="c">/-</span><span class="cm"></span>

<span class="cm">type mismatch at field &#39;β&#39;</span>
<span class="cm">  R</span>
<span class="cm">has type</span>
<span class="cm">  Type u : Type (u+1)</span>
<span class="cm">but is expected to have type</span>
<span class="cm">  Type u_1 : Type (u_1+1)</span>

<span class="cm">-/</span>
</pre></div>

#### [ Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942655):
<p>Seems to me that scheme has decided that it wants to live in a different universe to beta and R</p>

#### [ Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942656):
<p>oh</p>

#### [ Kevin Buzzard (May 22 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942657):
<p>heh</p>

#### [ Kevin Buzzard (May 22 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942661):
<p>ignore the irrelevant names</p>

#### [ Kevin Buzzard (May 22 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942676):
<p>If I change theorem to definition, it works</p>

#### [ Kevin Buzzard (May 22 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942682):
<p>And this works too:</p>

#### [ Kevin Buzzard (May 22 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942700):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">scheme_of_affine_scheme</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">scheme</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">R</span> <span class="c1">-- works</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 22 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942731):
<p>OK so maybe the answer is simply "don't use theorem to define something which isn't a Prop"</p>

#### [ Kevin Buzzard (May 22 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942856):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">scheme_of_affine_scheme</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">scheme</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">R</span> <span class="c1">-- works</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 22 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126942867):
<p>I guess I don't understand what's going on, but on the other hand I can see I was doing something dumb.</p>

#### [ Chris Hughes (May 22 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943048):
<p>This gives some small insight.</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">universes</span> <span class="n">true</span>
<span class="n">def</span> <span class="n">scheme_of_affine_scheme</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">scheme</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="c1">-- R : Type u</span>
<span class="c1">-- ⊢ scheme.{?l_1}</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">scheme_of_affine_scheme</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">scheme</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="c1">-- R : Type u</span>
<span class="c1">-- ⊢ scheme.{u_1}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 22 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943257):
<p>Aah so in the first case scheme is in some universe and Lean isn't too fussed, it will decide later</p>

#### [ Kevin Buzzard (May 22 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943303):
<p>but in the second case Lean decided to go for it and make a decision</p>

#### [ Kevin Buzzard (May 22 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943307):
<p>because it's a lemma so the universe is supposed to be Prop</p>

#### [ Kevin Buzzard (May 22 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/126943312):
<p>and it wasn't Prop so Lean panicked</p>

#### [ Chris Hughes (Jun 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/127406709):
<p>The lemma <code>card_univ</code> below does not work without the <code>.{u}</code> in the <code>fintype</code> instance</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span>
<span class="kn">open</span> <span class="n">set</span> <span class="n">fintype</span>
<span class="kn">universe</span> <span class="n">u</span>

<span class="n">def</span> <span class="n">equiv_univ</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">mem_univ</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">ha</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">card_univ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)]:</span>
  <span class="bp">@</span><span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="bp">@</span><span class="n">card_congr</span> <span class="n">α</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">equiv_univ</span> <span class="n">α</span><span class="o">))</span>
</pre></div>


<p>The following do not work.</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">universes</span> <span class="n">true</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">card_univ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)]:</span>
  <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">card_congr</span> <span class="o">(</span><span class="n">equiv_univ</span> <span class="n">α</span><span class="o">))</span>
</pre></div>


<p>Gives the error</p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
α : Type u,
_inst_1 : fintype.{u} α,
_inst_2 : fintype.{?l_1} ↥univ.{u}
⊢ fintype.{u} ↥univ.{u}
</pre></div>


<p>and  </p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">universes</span> <span class="n">true</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">card_univ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">f</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)]:</span>
  <span class="bp">@</span><span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="bp">@</span><span class="n">card_congr</span> <span class="n">α</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">_</span> <span class="n">f</span> <span class="o">(</span><span class="n">equiv_univ</span> <span class="n">α</span><span class="o">))</span>
</pre></div>


<p>Gives the error</p>
<div class="codehilite"><pre><span></span>type mismatch at application
  card_congr.{u u_1} (equiv_univ.{u} α)
term
  equiv_univ.{u} α
has type
  equiv.{u+1 (max 1 (u+1))} α
    (@coe_sort.{(max (u+1) 1) (max 1 (u+1))+1} (set.{u} α) (@set.has_coe_to_sort.{u} α) (@set.univ.{u} α)) : Type u
but is expected to have type
  equiv.{u+1 u_1+1} α
    (@coe_sort.{(max (u+1) 1) (max 1 (u+1))+1} (set.{u} α) (@set.has_coe_to_sort.{u} α)
       (@set.univ.{u} α)) : Type (max (max u u_1) u_1 u)
</pre></div>


<p>What's going on here? And will the <code>.{u}</code> in the fintype instance make the lemma more difficult to use. It worked in my application, but will it always work?</p>

#### [ Gabriel Ebner (Jun 01 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/127406993):
<blockquote>
<p>And will the .{u} in the fintype instance make the lemma more difficult to use.</p>
</blockquote>
<p>No, not at all.  It is the only possible choice, the elaborator just can't figure it out for whatever reason.</p>

#### [ Gabriel Ebner (Jun 01 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Universe%20issues/near/127407052):
<p>(The universe parameter <code>.{u}</code> is always there, whether you write it explicitly or not.)</p>


{% endraw %}
