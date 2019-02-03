---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/47318Exerciseschapter4xrr.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)](https://leanprover-community.github.io/archive/113489newmembers/47318Exerciseschapter4xrr.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Carlesso Diego (Dec 04 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150837580):
<p>Hello! First time I write here! I'm trying to learn Lean step by step following the online tutorial "theorem proving in Lean" doing as many exercises as I can. <br>
At the moment I'm having a problem (probably more on the logic part of the thing) on the first one of exercise 2 in chapter 4:<br>
α → (( ∀ x: α, r ) ↔ r)</p>
<p>theorem e1: α → (( ∀ x: α, r ) ↔ r) :=<br>
assume y:α,<br>
iff.intro<br>
(assume h: (∀ x, r),<br>
show r, from h y<br>
)<br>
-- wrong from now on<br>
(assume hr: r,<br>
assume x : α,<br>
assume hyr : (∀ x , r),<br>
show (∀ x: α , r), from hyr<br>
)</p>
<p>First of all, I don't know if assuming y:α solve the "α →" part, but I'm struggling in the second part of the iff.intro (I think that the first part is correct) <br>
the error is : </p>
<p>" type mismatch at application<br>
{mp := λ (h : α → r), show r, from h y, mpr := λ (hr : r) (x : α) (hyr : α → r), show α → r, from hyr}<br>
term<br>
λ (hr : r) (x : α) (hyr : α → r), show α → r, from hyr<br>
has type<br>
r → α → (α → r) → α → r<br>
but is expected to have type<br>
r → α → r "</p>
<p>And I understand why it returns that error, but, how am I supposed to show (∀ x: α , r) from r otherwise? It's probably something stupid I'm missing but as stupid as it is I can't see it. Looking at the others in ex2 I think it's probably something I'm getting wrong in bringing outside a universal quantifier.<br>
Also, I've never used Zulip or something like that, so let me know if I did something wrong.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150837685):
<p>For Zulip -- if you write your code between triple backticks <code> ``` </code> then it gets formatted nicely. Even better, if you write <code> ```lean </code> for the top triple backtick then you get syntax highlighting as well.</p>

#### [ Kevin Buzzard (Dec 04 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150837694):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">e1</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">((</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">r</span> <span class="o">)</span> <span class="bp">↔</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">y</span><span class="o">:</span><span class="n">α</span><span class="o">,</span>
<span class="n">iff</span><span class="bp">.</span><span class="n">intro</span>
<span class="o">(</span><span class="k">assume</span> <span class="n">h</span><span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">r</span><span class="o">),</span>
<span class="k">show</span> <span class="n">r</span><span class="o">,</span> <span class="k">from</span> <span class="n">h</span> <span class="n">y</span>
<span class="o">)</span>
<span class="c1">-- wrong from now on</span>
<span class="o">(</span><span class="k">assume</span> <span class="n">hr</span><span class="o">:</span> <span class="n">r</span><span class="o">,</span>
<span class="k">assume</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="k">assume</span> <span class="n">hyr</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">,</span> <span class="n">r</span><span class="o">),</span>
<span class="k">show</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">:</span> <span class="n">α</span> <span class="o">,</span> <span class="n">r</span><span class="o">),</span> <span class="k">from</span> <span class="n">hyr</span>
<span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Dec 04 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150837731):
<p>But your code doesn't run for me -- can you post some fully working example so I can get it to compile without having to think?</p>

#### [ Patrick Massot (Dec 04 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150837935):
<p>Carlesso, What Kevin means is you should include your <code>variables (α : Type) (r : Prop)</code> line as well, so that anyone can copy-paste your code right away</p>

#### [ Patrick Massot (Dec 04 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150837993):
<p>About the question itself, you are complicating things needlessly. It's probably because the question is a bit silly</p>

#### [ Patrick Massot (Dec 04 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150838017):
<p>The proof of the second implication is simply <code>assume hr _, hr</code></p>

#### [ Patrick Massot (Dec 04 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150838020):
<p>The whole point is that <code>r</code> does not depend on anything</p>

#### [ Patrick Massot (Dec 04 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150838222):
<p>and the first one can be shortened to <code>assume h, h y</code>. If you really want to use term mode, you can go all the way down the obfuscation road until you reach <code>theorem e1 (α : Type) (r : Prop): α → (( ∀ x: α, r ) ↔ r) := λ y, ⟨λ h, h y, λ h _, h⟩</code></p>

#### [ Patrick Massot (Dec 04 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150838259):
<p>The opposite extreme is to load mathlib and replace the proof by <code>by tauto</code>.</p>

#### [ Carlesso Diego (Dec 04 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150842750):
<blockquote>
<p>Carlesso, What Kevin means is you should include your <code>variables (α : Type) (r : Prop)</code> line as well, so that anyone can copy-paste your code right away</p>
</blockquote>
<p>Ok!, sorry about that, I will keep that in mind.</p>
<p>About the problem you are right! and what you suggest work well; I was aware of <code>r</code>  but I wasn't able to "say" that in Lean.</p>
<blockquote>
<p>About the question itself, you are complicating things needlessly. It's probably because the question is a bit silly</p>
</blockquote>
<p>I was trying to be consistent with the "solution scheme" that the chapter has, for example <code>(∀x, p x ∧ q x ) ↔ (∀ x, p x) ∧ (∀ x, q x) </code> is :</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span> <span class="n">r</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="kn">theorem</span> <span class="n">e2</span><span class="o">:</span> <span class="o">(</span><span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">x</span> <span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">q</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">iff</span><span class="bp">.</span><span class="n">intro</span>
    <span class="o">(</span>
    <span class="k">assume</span> <span class="n">h</span><span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">x</span><span class="o">),</span>
    <span class="k">show</span><span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">q</span> <span class="n">x</span><span class="o">),</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">intro</span>
        <span class="o">(</span><span class="k">assume</span> <span class="n">y</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="k">show</span> <span class="n">p</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">left</span><span class="o">(</span><span class="n">h</span> <span class="n">y</span><span class="o">))</span>
        <span class="o">(</span><span class="k">assume</span> <span class="n">y</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="k">show</span> <span class="n">q</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">right</span><span class="o">(</span><span class="n">h</span> <span class="n">y</span><span class="o">))</span>
    <span class="o">)</span>
    <span class="o">(</span><span class="k">assume</span> <span class="n">h1</span><span class="o">:(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">q</span> <span class="n">x</span><span class="o">),</span>
    <span class="k">assume</span> <span class="n">y</span><span class="o">:</span><span class="n">α</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hp</span><span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">),</span> <span class="k">from</span> <span class="n">h1</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hq</span><span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">q</span> <span class="n">x</span><span class="o">),</span> <span class="k">from</span> <span class="n">h1</span><span class="bp">.</span><span class="n">right</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hp2</span><span class="o">:</span> <span class="n">p</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span> <span class="n">hp</span> <span class="n">y</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hq2</span> <span class="o">:</span> <span class="n">q</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span> <span class="n">hq</span> <span class="n">y</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">p</span> <span class="n">y</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">intro</span> <span class="n">hp2</span> <span class="n">hq2</span>
    <span class="o">)</span>
</pre></div>


<p>It's a different exercise; I don't know if it could be solved with your method (right now it works), I have not reached that part on TPIL yet I think, or I'm not very practical to use it right now;  but it's just to show you what an exercise there looks like and what I was trying to get. <br>
Thank you by the way, problem solved!</p>

#### [ Mario Carneiro (Dec 04 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150843010):
<p>here's a compactified proof of that theorem:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
<span class="kn">theorem</span> <span class="n">e2</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">q</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">H</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">H</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">H</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">right</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">H₁</span><span class="o">,</span> <span class="n">H₂</span><span class="bp">⟩</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">H₁</span> <span class="n">x</span><span class="o">,</span> <span class="n">H₂</span> <span class="n">x</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Mario Carneiro (Dec 04 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150843154):
<p>and a proof of the first theorem in that style:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">e1</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">((</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">r</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">iff</span><span class="bp">.</span><span class="n">intro</span>
  <span class="o">(</span> <span class="k">assume</span> <span class="n">h</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">r</span><span class="o">),</span>
    <span class="k">show</span> <span class="n">r</span><span class="o">,</span> <span class="k">from</span> <span class="n">h</span> <span class="n">y</span> <span class="o">)</span>
  <span class="o">(</span> <span class="k">assume</span> <span class="n">hr</span> <span class="o">:</span> <span class="n">r</span><span class="o">,</span>
    <span class="k">assume</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
    <span class="k">show</span> <span class="n">r</span><span class="o">,</span> <span class="k">from</span> <span class="n">hr</span> <span class="o">)</span>
</pre></div>

#### [ Carlesso Diego (Dec 04 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150844606):
<p>Thank you!, that's perfect!</p>

#### [ Kevin Buzzard (Dec 04 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150845046):
<blockquote>
<p>Carlesso, What Kevin means is you should include your <code>variables (α : Type) (r : Prop)</code> line as well, so that anyone can copy-paste your code right away</p>
</blockquote>
<p>Yes -- sorry for the brevity! I just had 2 minutes before a lecture and I wanted to help but then the code didn't run so I had to give up :-)</p>

#### [ Carlesso Diego (Dec 04 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Exercises%20chapter%204%20-%20%CE%B1%20%E2%86%92%20%28%28%20%E2%88%80%20x%3A%20%CE%B1%2C%20r%20%29%20%E2%86%94%20r%29/near/150845940):
<blockquote>
<blockquote>
<p>Carlesso, What Kevin means is you should include your <code>variables (α : Type) (r : Prop)</code> line as well, so that anyone can copy-paste your code right away</p>
</blockquote>
<p>Yes -- sorry for the brevity! I just had 2 minutes before a lecture and I wanted to help but then the code didn't run so I had to give up :-)</p>
</blockquote>
<p>Don't worry!, I didn't think about the variables thing, I'm working with different exercises in the same file and I forgot about them, totally my fault. Thank you for your time anyway! :)</p>


{% endraw %}
