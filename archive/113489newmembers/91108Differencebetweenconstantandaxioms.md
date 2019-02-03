---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/91108Differencebetweenconstantandaxioms.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Difference between constant and axioms](https://leanprover-community.github.io/archive/113489newmembers/91108Differencebetweenconstantandaxioms.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154074362):
<p>I just noticed that <code>propext</code> is defined as a constant:</p>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">propext</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">↔</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span>
</pre></div>


<p>Is this an alternative to <code>axiom</code>? What would change if I made it an axiom?</p>

#### [ Kenny Lau (Dec 31 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154074420):
<p>nothing at all</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154074521):
<p>Why are there two different commands then? I would think it may make sense to use <code>axiom</code> for things whose type has type <code>Prop</code> and <code>constant</code> for things whose type has some other type (like a function), but the two examples I've seen are exactly the opposite.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154074573):
<p>I.e. <code>choice</code> defines a function and is an <code>axiom</code> but <code>propext</code> defines a (unproven) proof and is a <code>constant</code>.</p>

#### [ Kevin Buzzard (Dec 31 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154078889):
<p>There's no difference between <code>theorem</code> and <code>lemma</code> of course. But for constants and axioms I thought the rule of thumb was that constants were for data and axioms for propositions. As you spotted, this convention does not seem to be being followed here</p>

#### [ Kevin Buzzard (Dec 31 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154079192):
<p>The main difference between data and propositions in Lean is that Lean remembers how you constructed data but throws away your proof of a proposition and just remembers that it's proved. But of course here with constants and axioms this information doesn't exist, so they feel a lot more similar to each other than theorems and definitions do. If you're brave enough to look at Lean's source code and know enough C++ to understand it then you could maybe just check to see what the difference is.</p>

#### [ Gabriel Ebner (Dec 31 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154079304):
<p>Interestingly enough, <code>propext</code> was an <code>axiom</code> four years ago: <a href="https://github.com/leanprover/lean/blob/0da4f191fc2a37e34d53179d5cf924021de4fd15/library/logic/axioms/propext.lean" target="_blank" title="https://github.com/leanprover/lean/blob/0da4f191fc2a37e34d53179d5cf924021de4fd15/library/logic/axioms/propext.lean">https://github.com/leanprover/lean/blob/0da4f191fc2a37e34d53179d5cf924021de4fd15/library/logic/axioms/propext.lean</a><br>
But yeah, it doesn't matter that much.  In the C++ code, you could tell the difference between axiom and constant, but this is not really used and not exposed to lean either.  Another difference is that you can do <code>meta constant</code> but not <code>meta axiom</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080836):
<p>By the way, <code>propext</code> and <code>funext</code> together prove that all proofs (of a proposition) are equal, don't they? Since <code>propext</code> shows that <code>f(trivial) = trivial, g(trivial) = trivial</code> for any two functions <code>f : true \to P</code> and <code>g : true \to P</code>. So does that mean type theories in which proofs are distinct lack <code>propext</code>?</p>

#### [ Chris Hughes (Dec 31 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080842):
<p>You don't need any axioms to prove that.</p>

#### [ Kevin Buzzard (Dec 31 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080884):
<p>I think the extra "axiom" is not just that all proofs of P are equal, but that they are definitionally equal.</p>

#### [ Chris Hughes (Dec 31 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080886):
<p>look at the theorem <code>proof_irrel</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080899):
<p>Oh. <code>rfl</code> is just anti-climactic.</p>

#### [ Kevin Buzzard (Dec 31 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080938):
<p>:-)</p>

#### [ Chris Hughes (Dec 31 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080939):
<p>But I see actually, even if it wasn't definitional, then propext would imply that anyway.</p>

#### [ Chris Hughes (Dec 31 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154080950):
<p>Because every true <code>Prop</code> would be equal to <code>true</code> and <code>true</code> has only one proof.</p>

#### [ Chris Hughes (Dec 31 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081030):
<p>Proof relevant type theories tend to lack the type <code>Prop</code> altogether I think. Proof irrelevance is the only thing distinguishing <code>Prop</code> and <code>Type</code> so propositions tend to be defined using <code>Type</code> and some of them I think have an <code>is_Prop</code> predicate that says that the type has only one element.</p>

#### [ Kevin Buzzard (Dec 31 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081033):
<p>My recent thoughts about <code>quot</code>, and Mario's comments about them (sparked by Chris' observation that I used quot.sound to prove quot'.sound) made all this a bit clearer to me. There is just a whole bunch of stuff which, if you don't have it, would make maths basically impossible to do, and the CS people have made what appears to a mathematician to be a random small set of this stuff into axioms and then deduced all the rest of it. I'm not sure that the fact that propext is an axiom is remotely important.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081242):
<blockquote>
<p>Because every true <code>Prop</code> would be equal to <code>true</code> and <code>true</code> has only one proof.</p>
</blockquote>
<p>When I try writing that proof, though, Lean just changes it to <code>eq.refl H1</code> (when I print it).</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081244):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">proof_irrel&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">H1</span> <span class="bp">=</span> <span class="n">H2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">ta</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">true</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">propext</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span> <span class="o">{</span> <span class="n">intro</span><span class="o">,</span> <span class="n">trivial</span> <span class="o">},</span> <span class="o">{</span> <span class="n">intro</span><span class="o">,</span> <span class="n">exact</span> <span class="n">H1</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="n">ta</span> <span class="n">at</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081245):
<p>(deleted)</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081246):
<p>(deleted)</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081247):
<p>Oh wait, I'm using a rewrite so it tries refl.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081294):
<p>Wasn't there a version of <code>rw</code> that didn't try <code>refl</code>?</p>

#### [ Kenny Lau (Dec 31 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081304):
<p>I think you can tweak the settings</p>

#### [ Kevin Buzzard (Dec 31 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081307):
<p>I completely agree that it's a pain to experiment with stuff using <code>rw</code> becasue of this refl thing. I think "dunfold" and "delta" unfold functions without trying refl at the end but I don't know about rw.</p>

#### [ Chris Hughes (Dec 31 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081313):
<p>I'm not sure this proof would actually work. Substitutions using equality of types are far more complicated and subtle than they might appear.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081426):
<blockquote>
<p>I'm not sure this proof would actually work. Substitutions using equality of types are far more complicated and subtle than they might appear.</p>
</blockquote>
<p>? Surely rewrite works on <code>↔</code>, which is equality of types. E.g.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">HP</span> <span class="o">:</span> <span class="n">P</span><span class="o">)</span> <span class="o">(</span><span class="n">HPQ</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">=</span> <span class="n">Q</span><span class="o">)</span> <span class="o">:</span> <span class="n">sorry</span> <span class="o">:=</span> <span class="k">by</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">HPQ</span> <span class="n">at</span> <span class="n">HP</span><span class="o">,</span> <span class="n">sorry</span> <span class="o">}</span>
</pre></div>

#### [ Chris Hughes (Dec 31 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081485):
<p>Actually, it definitely does work.</p>

#### [ Chris Hughes (Dec 31 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081500):
<p>This is the easiest way.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">proof_irrel&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">H1</span> <span class="bp">=</span> <span class="n">H2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">ta</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">true</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">propext</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span> <span class="o">{</span> <span class="n">intro</span><span class="o">,</span> <span class="n">trivial</span> <span class="o">},</span> <span class="o">{</span> <span class="n">intro</span><span class="o">,</span> <span class="n">exact</span> <span class="n">H1</span> <span class="o">},</span>
  <span class="n">revert</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">ta</span><span class="o">,</span>

<span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081565):
<p>And then use <code>no_confusion</code>? Hm, <code>true</code> doesn't have no_confusion.</p>

#### [ Chris Hughes (Dec 31 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081610):
<p>That's because it's unnecessary. But if there was no proof irrelevance there would be.</p>

#### [ Chris Hughes (Dec 31 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081617):
<p>Actually, this is what you should do.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">proof_irrel&#39;</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">H1</span> <span class="bp">=</span> <span class="n">H2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">ta</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">true</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">propext</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span> <span class="o">{</span> <span class="n">intro</span><span class="o">,</span> <span class="n">trivial</span> <span class="o">},</span> <span class="o">{</span> <span class="n">intro</span><span class="o">,</span> <span class="n">exact</span> <span class="n">H1</span> <span class="o">},</span>
  <span class="n">revert</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">ta</span><span class="o">,</span>
  <span class="k">assume</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H1</span><span class="o">,</span> <span class="n">cases</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">refl</span>

<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Dec 31 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081619):
<p><code>no_confusion</code> is usually good for proving things are not equal.</p>

#### [ Abhimanyu Pallavi Sudhir (Dec 31 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081671):
<p>Yeah, I got confused (between the uniqueness of the constructors and their exhaustiveness)</p>

#### [ Chris Hughes (Dec 31 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154081681):
<p>To illustrate how complicated proof relevant equality can be, try proving this <code>example</code> without using <code>eq</code> anywhere in the proof. (Hint: it's impossible)</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">eq2</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">:</span> <span class="n">eq2</span> <span class="n">a</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h₁</span> <span class="n">h₂</span> <span class="o">:</span> <span class="n">eq2</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">eq2</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kenny Lau (Dec 31 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154082070):
<div class="codehilite"><pre><span></span><span class="n">prelude</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">notation</span> <span class="bp">`</span><span class="kt">Prop</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">Sort</span> <span class="mi">0</span>

<span class="kn">structure</span> <span class="n">iff</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">mp</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">mpr</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">a</span><span class="o">)</span>

<span class="kn">inductive</span> <span class="n">eq</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">:</span> <span class="n">eq</span> <span class="n">a</span>

<span class="kn">infix</span> <span class="bp">`</span> <span class="bp">↔</span> <span class="bp">`</span><span class="o">:</span><span class="mi">20</span> <span class="o">:=</span> <span class="n">iff</span>
<span class="kn">infix</span> <span class="bp">`</span> <span class="bp">=</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">eq</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">,</span> <span class="n">subst</span><span class="o">]</span>
<span class="kn">lemma</span> <span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">P</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">P</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="n">h₂</span> <span class="n">h₁</span>

<span class="kn">infixr</span> <span class="bp">`</span> <span class="bp">▸</span> <span class="bp">`</span><span class="o">:</span><span class="mi">75</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">subst</span>

<span class="kn">constant</span> <span class="n">propext</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">↔</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span>

<span class="kn">inductive</span> <span class="n">true</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">intro</span> <span class="o">:</span> <span class="n">true</span>

<span class="kn">lemma</span> <span class="n">proof_irrel</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">H1</span> <span class="bp">=</span> <span class="n">H2</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">true</span> <span class="bp">=</span> <span class="n">a</span><span class="o">,</span> <span class="k">from</span> <span class="n">propext</span> <span class="bp">⟨λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H1</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">true</span><span class="bp">.</span><span class="n">intro</span><span class="bp">⟩</span><span class="o">,</span>
<span class="o">(</span><span class="n">this</span> <span class="bp">▸</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span> <span class="n">true</span><span class="bp">.</span><span class="n">drec_on</span> <span class="n">H1</span> <span class="o">(</span><span class="n">true</span><span class="bp">.</span><span class="n">drec_on</span> <span class="n">H2</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="n">true</span><span class="bp">.</span><span class="n">intro</span><span class="o">)))</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">H1</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">a</span><span class="o">,</span> <span class="n">H1</span> <span class="bp">=</span> <span class="n">H2</span><span class="o">)</span> <span class="n">H1</span> <span class="n">H2</span>
</pre></div>

#### [ Chris Hughes (Dec 31 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154084763):
<p>What does the <code>subst</code> attribute do?</p>

#### [ Kevin Buzzard (Dec 31 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154087217):
<p>Where is a complete list of all attributes and their explanations? Oh -- is <code>[subst]</code> it only used in core? Are users not supposed to use it?</p>

#### [ Kenny Lau (Dec 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154087286):
<p>I have no idea, I just copied the code out of the core library</p>

#### [ Patrick Massot (Dec 31 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154088165):
<blockquote>
<p>Proof relevant type theories tend to lack the type <code>Prop</code> altogether I think. Proof irrelevance is the only thing distinguishing <code>Prop</code> and <code>Type</code> so propositions tend to be defined using <code>Type</code> and some of them I think have an <code>is_Prop</code> predicate that says that the type has only one element.</p>
</blockquote>
<p>This is not true. Impredicativity is also an important difference. I think Coq has Prop for this reason, and no definitional proof irrelevance</p>

#### [ Chris Hughes (Dec 31 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154089302):
<p>What do you mean precisely by impredicativity?</p>

#### [ Kevin Buzzard (Dec 31 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154089447):
<p>Coq has no definitional proof irrelevance? But does it have proof irrelevance?</p>

#### [ Chris Hughes (Dec 31 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154089637):
<p>I heard once it was an optional extra like <code>propext</code>. Though I guess that means <code>Prop</code> would still be special in the sense that any two proofs are not provably unequal.</p>

#### [ Mario Carneiro (Dec 31 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096231):
<p>right, you have to have this property if impredicativity is to be consistent</p>

#### [ Mario Carneiro (Dec 31 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096238):
<p>because if a type has two elements, then you can build a cantor's paradox sort of thing using impredicativity</p>

#### [ Chris Hughes (Dec 31 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096291):
<p>What does impredicativity mean precisely?</p>

#### [ Mario Carneiro (Dec 31 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096563):
<p><code>forall x : A, P : Prop</code> if <code>P : Prop</code></p>

#### [ Mario Carneiro (Dec 31 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096566):
<p>even if <code>A : Type</code></p>

#### [ Mario Carneiro (Dec 31 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096610):
<p>this means that propositions can quantify over themselves</p>

#### [ Kevin Buzzard (Dec 31 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096683):
<p><code>(forall x : A, P) : Prop</code> is what we're talking about here, presumably. The universe isn't the max, it's the imax.</p>

#### [ Mario Carneiro (Dec 31 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096698):
<p>in a predicative universe, the pi type has level max of the universe levels of the parts</p>

#### [ Mario Carneiro (Dec 31 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154096701):
<p>but we have this funny imax thing for level 0</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 01 2019 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154114592):
<blockquote>
<p>this means that propositions can quantify over themselves</p>
</blockquote>
<p>Isn't that just <code>P → P</code>?</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 01 2019 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154114602):
<p>Even with functions between types, the type of <code>P → Q</code> is the types of <code>P</code> and <code>Q</code>, so I don't understand why this makes <code>Prop</code> special.</p>

#### [ Mario Carneiro (Jan 01 2019 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154114948):
<p>I mean a function whose domain of quantification includes itself</p>

#### [ Mario Carneiro (Jan 01 2019 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154115111):
<p>which permits self application</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">p</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">⦃</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">⦄,</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">p</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span>
<span class="n">def</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">p</span> <span class="n">p</span>
</pre></div>

#### [ Mario Carneiro (Jan 01 2019 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154115115):
<p>you can use this to do a variety of diagonalization type arguments</p>

#### [ Kenny Lau (Jan 01 2019 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154116038):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> if you quantify over all <code>Type</code>, you get <code>Type 1</code></p>

#### [ Reid Barton (Jan 01 2019 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129709):
<p>A classic example of an impredicative definition of a Prop is defining the subgroup generated by a subset S of a group G to be the intersection of all the subgroups of G which contain S</p>

#### [ Reid Barton (Jan 01 2019 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129773):
<p>which is to say <code>def belongs_to_subgroup_generated_by (S : set G) (x : G) : Prop := \forall (P : G \to Prop), is_subgroup P \and (\forall y, S y \to P y) \to P x</code></p>

#### [ Reid Barton (Jan 01 2019 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129817):
<p>If <code>Prop</code> had a universe hierarchy like <code>Type</code>, you wouldn't be allowed to use the same <code>Prop</code> on both sides of that equation</p>

#### [ Chris Hughes (Jan 01 2019 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129832):
<p>It hadn't occurred to me how important this was.</p>

#### [ Kenny Lau (Jan 01 2019 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154129986):
<p>of course it hadn't, you guys don't even care about foundations / of course it hadn't, this is hard core logic stuff</p>

#### [ Reid Barton (Jan 01 2019 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130031):
<p>It's really hard to imagine from a classical perspective how anyone could object to the construction "take all the subsets of G, keep the ones which are subgroups containing S, and form their intersection".</p>

#### [ Reid Barton (Jan 01 2019 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130032):
<p>Before using Lean, I was not convinced that "impredicative" meant anything at all.</p>

#### [ Kenny Lau (Jan 01 2019 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130044):
<p>From a "classical perspective", you run into issues like Δ0-predicates are absolute</p>

#### [ Kenny Lau (Jan 01 2019 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130092):
<p>that somehow P(ω) (i.e. powerset of ω) is not absolute</p>

#### [ Kenny Lau (Jan 01 2019 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130094):
<p>because taking powerset is not a predicative thing to do</p>

#### [ Reid Barton (Jan 01 2019 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130151):
<p>Right, well, so the conclusion is that caring about predicativity is not a math thing to do.</p>

#### [ Reid Barton (Jan 01 2019 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130166):
<p>Especially since this example of an impredicative definition is something that one will encounter in a first course on algebra, it's not some scary thing involving universes or whatever.</p>

#### [ Kenny Lau (Jan 01 2019 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130173):
<p>mathematicians have gone too far, doing impredicative stuff like that</p>

#### [ Kenny Lau (Jan 01 2019 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130179):
<p>how are they going to compute their examples if their definitions are impredicative</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130229):
<p>who cares about examples? We want theorems!</p>

#### [ Kenny Lau (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130240):
<p>what do you want theorems for?</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130245):
<p>fun</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130247):
<p>and promotion</p>

#### [ Kenny Lau (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130248):
<p>wasn't number theory created to solve diophantine equations</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130253):
<p>yes but now its job is to create theorems explaining what the structure of the solutions is</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130292):
<p>because solving them all turned out to be too hard</p>

#### [ Kenny Lau (Jan 01 2019 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130294):
<p>but now your impredicative definitions are not helping us to solve the equations, because they are incomputable</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130303):
<p>yes but we don't care about solving them because that's too hard. We now care about whether the solutions lie on some union of simple subvarieties or something. Nobody will get promoted for solving a Diophantine equation.</p>

#### [ Kenny Lau (Jan 01 2019 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130343):
<p>Can you compute the integers of Q[X]/(X^3-3X+1)?</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130349):
<p>sure, I read an algorithm to do that once</p>

#### [ Kenny Lau (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130358):
<p>that doesn't mean you can compute it</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130359):
<p>it's in Cohen's book on computational number theory</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130362):
<p>sure it means I can compute it</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130364):
<p>I just ask a PhD student to compute it for me</p>

#### [ Kenny Lau (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130367):
<p>that isn't <strong>you</strong> computing it</p>

#### [ Kevin Buzzard (Jan 01 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130372):
<p>I think you have a lot to learn about the real world</p>

#### [ Chris Hughes (Jan 01 2019 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154130934):
<p>Lean is designed for computer science, so impredicative definitions can't be that useless from a computational perspective. You can't compute with them, but you can still use them to help prove your program does what it's supposed to.</p>

#### [ Mario Carneiro (Jan 01 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132613):
<p>By the way, HoTT uses predicative universes only (in the usual setup), so if you thought it would be a great thing that solves all your problems then this is one place where it isn't all sunshine and roses</p>

#### [ Mario Carneiro (Jan 01 2019 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132623):
<p>Also Agda makes a big deal about being 100% predicative</p>

#### [ Mario Carneiro (Jan 01 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132730):
<p>It's true that in regular math predicativity doesn't really come up, but it shows up in non-absoluteness like Kenny says, or in model theory where adding more ordinals causes new subsets of nat to appear... you have this weird situation where you've built the set but not the elements, and that's where things like Cohen reals come from</p>

#### [ Mario Carneiro (Jan 01 2019 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132796):
<p>Also, we've discussed impredicative encodings of inductive types before, like <code>xnat : Type := \all X : Type, X -&gt; (X -&gt; X) -&gt; X</code>, which doesn't typecheck in lean because <code>Type</code> is predicative</p>

#### [ Mario Carneiro (Jan 01 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Difference%20between%20constant%20and%20axioms/near/154132846):
<p>Or when we have an object that is "defined by a universal property" and we want to just write that property but it doesn't work because the universe quantifier isn't large enough, so instead we re-express it by some kind of construction "from below"... that's predicativity</p>


{% endraw %}
