---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/22656Compoundstatmenttoadmitsecondgoalofhave.html
---

## Stream: [new members](index.html)
### Topic: [Compound statment to admit second goal of have](22656Compoundstatmenttoadmitsecondgoalofhave.html)

---


{% raw %}
#### [ Ken Roe (Jul 21 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061451):
<p>I tried the following to do a "have" and admit the second goal.  What is the correct syntax:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">dummy</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="k">have</span> <span class="n">h</span><span class="o">:</span><span class="n">n</span><span class="bp">=</span><span class="mi">1</span><span class="bp">+</span><span class="mi">2</span><span class="bp">;</span><span class="o">(</span><span class="n">skip</span><span class="bp">|</span><span class="n">admit</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jul 21 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061504):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">dummy</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="k">have</span> <span class="n">h</span><span class="o">:</span><span class="n">n</span><span class="bp">=</span><span class="mi">1</span><span class="bp">+</span><span class="mi">2</span><span class="o">,</span>
    <span class="o">{</span> <span class="c1">-- here we only see the first goal</span>
       <span class="n">sorry</span>
    <span class="o">},</span>
    <span class="o">{</span> <span class="c1">-- here we only see the second goal</span>
      <span class="n">sorry</span>
    <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>Is that what you mean?</p>

#### [ Ken Roe (Jul 21 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061512):
<p>thanks</p>

#### [ Kevin Buzzard (Jul 21 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061557):
<p>No problem. Note that the <code>have h: ...</code> turns one goal <code>G</code> into two goals -- first the proof of <code>h</code>, and second the proof of <code>G</code> assuming <code>h</code> (in addition to anything else which we were assuming when we wrote the <code>have</code>).</p>
<p>If you would rather have the goals the other way around, you can use <code>suffices</code> :-)</p>

#### [ Ken Roe (Jul 21 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061635):
<p>Actually, I tried the following:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">dummy</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="k">have</span> <span class="n">h</span><span class="o">:</span><span class="n">n</span><span class="bp">=</span><span class="mi">1</span><span class="bp">+</span><span class="mi">2</span><span class="o">,{</span> <span class="n">skip</span> <span class="o">},{</span> <span class="n">admit</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>


<p>I would like to end up in a state where only the first goal is open and the second goal is solved.</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061700):
<p>Since <code>n = 3</code> and <code>n = 1 + 2</code> are definitionally the same goal, you can use <code>change</code>:</p>
<div class="codehilite"><pre><span></span>theorem dummy (n :ℕ) : n = 3 :=
begin
    change n = 1 + 2,
end
</pre></div>

#### [ Mario Carneiro (Jul 21 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061786):
<p>If the transformation from one goal to the other is not definitional but easy, you can use <code>suffices</code>:</p>
<div class="codehilite"><pre><span></span>theorem dummy (n :ℕ) : n = 3 :=
begin
    suffices h : n = 1 + 2, {exact h},
end
</pre></div>

#### [ Kevin Buzzard (Jul 21 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130061999):
<p>Here are some more tips. If you have two goals, you can use <code>tactic.swap</code> to switch them. If you have more than one goal and you want to work on one of them, you can write <code>show &lt;statement of goal&gt;</code> and it will switch this goal to the top. One of my students was even telling me about some sort of <code>rotate</code> tactic but I've never used it.</p>

#### [ Mario Carneiro (Jul 21 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062011):
<p>the mathlib <code>swap</code> tactic takes an optional argument; <code>swap n</code> moves the nth goal to the top</p>

#### [ Ken Roe (Jul 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062367):
<p>Igt appears "have h:a, swap, admit" does what I want.  Now, I want to figure out something more complex:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>
<span class="kn">open</span> <span class="n">monad</span>
<span class="kn">open</span> <span class="n">expr</span>
<span class="kn">open</span> <span class="n">smt_tactic</span>

<span class="n">def</span> <span class="n">andFuns</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">q</span><span class="o">,</span> <span class="o">(</span><span class="n">a</span> <span class="n">q</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">b</span> <span class="n">q</span><span class="o">))</span><span class="bp">.</span>

<span class="n">def</span> <span class="n">existsFuns</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="n">a</span> <span class="n">e</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span>

<span class="n">def</span> <span class="n">test</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">3</span><span class="o">)</span>
<span class="n">def</span> <span class="n">test2</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">8</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">test1</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">andFuns</span> <span class="n">test</span> <span class="n">test2</span><span class="o">)</span> <span class="o">(</span><span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">v</span> <span class="o">:=</span>
<span class="k">begin</span>

    <span class="k">have</span> <span class="n">h</span><span class="o">:</span> <span class="o">(</span><span class="n">andFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">test</span> <span class="n">e</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">test2</span> <span class="n">e</span><span class="o">))</span> <span class="n">v</span><span class="o">,</span>
    <span class="n">swap</span><span class="o">,</span><span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>In the above theorem, I would like to create a tactic that automates the conversion of "(λ (e:ℕ), (andFuns test test2) (v+1)) v" to "h(andFuns (λ (e:ℕ), test e) (λ (e:ℕ), test2 e)) v". </p>
<p>I have created the following meta tactic which has many syntax errors.  How do I correct the errors:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">divide_lambda</span> <span class="o">:</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">binder_info</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="bp">``</span><span class="o">(</span><span class="n">andFuns</span> <span class="err">%%</span><span class="n">l</span> <span class="err">%%</span><span class="n">r</span><span class="o">)</span> <span class="n">v</span> <span class="n">y</span> <span class="o">:=</span>
      <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">andFuns</span><span class="o">)</span> <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">l</span> <span class="n">v</span> <span class="n">y</span><span class="o">))</span>
                           <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">r</span> <span class="n">v</span> <span class="n">y</span><span class="o">))</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">x</span> <span class="n">y</span> <span class="n">v</span> <span class="o">:=</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="o">(</span><span class="n">app</span> <span class="n">x</span> <span class="n">y</span><span class="o">))</span> <span class="n">v</span><span class="o">)</span><span class="bp">.</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">transform_lambda_app</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="o">(</span><span class="n">app</span> <span class="n">x</span> <span class="n">y</span><span class="o">))</span> <span class="n">val</span><span class="o">)</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">eq</span> <span class="n">x</span> <span class="n">y</span> <span class="n">val</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">none</span><span class="bp">.</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">split_lambda</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">{</span> <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
     <span class="n">nt</span> <span class="err">←</span> <span class="n">transform_lambda_app</span> <span class="n">t</span><span class="o">,</span>
     <span class="o">(</span><span class="k">have</span> <span class="n">h</span><span class="o">:</span><span class="n">nt</span><span class="bp">;</span><span class="n">swap</span><span class="bp">;</span><span class="n">admit</span><span class="o">)</span> <span class="o">}</span><span class="bp">.</span>
</pre></div>

#### [ Mario Carneiro (Jul 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062736):
<p>I'm confused - <code>(λ (e:ℕ), (andFuns test test2) (v+1)) v</code> and <code>h(andFuns (λ (e:ℕ), test e) (λ (e:ℕ), test2 e)) v</code> are not the same</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062747):
<p>are the <code>v</code> supposed to be de bruijn variables?</p>

#### [ Ken Roe (Jul 21 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130062892):
<p>I didn't state the theorem quite right:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test1</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">andFuns</span> <span class="n">test</span> <span class="n">test2</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">v</span> <span class="o">:=</span>
<span class="k">begin</span>

    <span class="k">have</span> <span class="n">h</span><span class="o">:</span> <span class="o">(</span><span class="n">andFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">test</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">test2</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="mi">1</span><span class="o">)))</span> <span class="n">v</span><span class="o">,</span>
    <span class="n">swap</span><span class="o">,</span><span class="n">admit</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Hopefully this make more sense.</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063016):
<p>You should be able to use <code>change</code> instead of <code>swap, admit</code> if you got it right</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063050):
<div class="codehilite"><pre><span></span>theorem test1 (v: ℕ) : (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin
    change (andFuns (λ (e:ℕ), test (e+1)) (λ (e:ℕ), test2 (e+1))) v,
end
</pre></div>

#### [ Mario Carneiro (Jul 21 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063159):
<p>Here is fixing the syntax errors, although it doesn't work yet:</p>
<div class="codehilite"><pre><span></span>meta def divide_lambda : name → binder_info → expr → expr → expr → expr → expr
| n b e1 `(andFuns %%l %%r) v y :=
      (app (app `(andFuns) (divide_lambda n b e1 l v y))
                           (divide_lambda n b e1 r v y))
| n b e1 x y v := (app (lam n b e1 (app x y)) v).

meta def transform_lambda_app : expr → option expr
| (app (lam n b e1 (app x y)) val) := some (divide_lambda n b e1 x y val)
| _ := none.

meta def split_lambda : tactic unit :=
do { t ← target,
     nt ← transform_lambda_app t,
     change nt }

theorem test1 (v: ℕ) : (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin
  split_lambda,
end
</pre></div>

#### [ Ken Roe (Jul 21 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063222):
<p>It looks like change works.  The theorem looks like this now:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test1</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">andFuns</span> <span class="n">test</span> <span class="n">test2</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">v</span> <span class="o">:=</span>
<span class="k">begin</span>

    <span class="n">change</span> <span class="o">(</span><span class="n">andFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">test</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">test2</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="mi">1</span><span class="o">)))</span> <span class="n">v</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Now the challenge is to get the tactic working that generates the expression.  The tactic code now looks like this:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">divide_lambda</span> <span class="o">:</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">binder_info</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="bp">``</span><span class="o">(</span><span class="n">andFuns</span> <span class="err">%%</span><span class="n">l</span> <span class="err">%%</span><span class="n">r</span><span class="o">)</span> <span class="n">v</span> <span class="n">y</span> <span class="o">:=</span>
      <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">andFuns</span><span class="o">)</span> <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">l</span> <span class="n">v</span> <span class="n">y</span><span class="o">))</span>
                           <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">r</span> <span class="n">v</span> <span class="n">y</span><span class="o">))</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">x</span> <span class="n">y</span> <span class="n">v</span> <span class="o">:=</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="o">(</span><span class="n">app</span> <span class="n">x</span> <span class="n">y</span><span class="o">))</span> <span class="n">v</span><span class="o">)</span><span class="bp">.</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">transform_lambda_app</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="o">(</span><span class="n">app</span> <span class="n">x</span> <span class="n">y</span><span class="o">))</span> <span class="n">val</span><span class="o">)</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">eq</span> <span class="n">x</span> <span class="n">y</span> <span class="n">val</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">none</span><span class="bp">.</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">split_lambda</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">{</span> <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
     <span class="n">nt</span> <span class="err">←</span> <span class="n">transform_lambda_app</span> <span class="n">t</span><span class="o">,</span>
     <span class="o">(</span><span class="n">change</span> <span class="n">nt</span><span class="o">)</span> <span class="o">}</span><span class="bp">.</span>
</pre></div>


<p>I'm getting the error "invalid pattern, must be an application, constant, variable, type ascription, aliasing pattern or inaccessible term" in divide_lambda on the pattern "n b e1 ``(andFuns %%l %%r) v y".</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063291):
<p>use single backtick on line 2</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063366):
<p>For me the tactic fails in <code>transform_lambda_app</code> because right after the <code>begin</code> the goal says <code>⊢ andFuns test test2 (v + 1)</code> so there is no lambda in sight</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063382):
<p>I wasn't aware of this - it looks like lean is really eager to unfold raw lambda-app beta reductions</p>

#### [ Mario Carneiro (Jul 21 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063528):
<p>I'm not exactly sure what your goal is; perhaps this is a suitable compromise:</p>
<div class="codehilite"><pre><span></span>theorem test1 (v: ℕ) : id (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin
  -- split_lambda,
  change id (andFuns (λ (e:ℕ), test (e+1)) (λ (e:ℕ), test2 (e+1))) v,
end
</pre></div>

#### [ Mario Carneiro (Jul 21 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130063733):
<p>This works, with the <code>id</code> to protect the lambda at the start:</p>
<div class="codehilite"><pre><span></span>meta def divide_lambda : name → binder_info → expr → expr → expr → expr
| n b e1 `(andFuns %%l %%r) y :=
      (app (app `(andFuns) (divide_lambda n b e1 l y))
                           (divide_lambda n b e1 r y))
| n b e1 x y := (lam n b e1 (app x y))

meta def transform_lambda_app : expr → option expr
| (app (lam n b e1 (app x y)) val) := some (app (divide_lambda n b e1 x y) val)
| (app `(id %%(lam n b e1 (app x y))) val) := some (app (divide_lambda n b e1 x y) val)
| _ := none

meta def split_lambda : tactic unit :=
do { t ← target,
    trace t.to_raw_fmt,
     nt ← transform_lambda_app t,
     change nt }

theorem test1 (v: ℕ) : id (λ (e:ℕ), (andFuns test test2) (e+1)) v :=
begin
  split_lambda,
end
</pre></div>

#### [ Ken Roe (Jul 21 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130066480):
<p>Thanks--Now for the next trick, I would like to extend split_lambda to be able to propagate an expression into a closure.  Note that now, the tactic may need to rename variables,</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">existsFuns</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="bp">∃</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="n">t</span><span class="o">),</span> <span class="n">a</span> <span class="n">e</span> <span class="n">n</span><span class="o">))</span><span class="bp">.</span>

<span class="kn">theorem</span> <span class="n">capture</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">id</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">andFuns</span> <span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">))</span> <span class="n">test</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="n">q</span><span class="o">))</span> <span class="n">v</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">change</span>
        <span class="n">andFuns</span> <span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="bp">=</span><span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="n">q</span><span class="o">)))</span>
                <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">test</span> <span class="o">(</span><span class="n">e</span> <span class="bp">+</span> <span class="n">q</span><span class="o">))</span> <span class="n">v</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Notice how the (e+q) is propagated inside a closure involving "x".  The variable may in some cases need to be renamed.   Is there a way to get a fresh variable name and to rename the variables when reconstructing lambda expressions?<br>
end</p>

#### [ Mario Carneiro (Jul 21 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130067152):
<p>You don't have to worry about variable capture for the most part. Lean uses unique names in all lambdas, so it shouldn't be a problem</p>

#### [ Mario Carneiro (Jul 21 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130067208):
<p>The tactics <code>mk_fresh_name</code> and <code>get_unused_name</code> can be used to generate unique and human-readable names respectively</p>

#### [ Ken Roe (Jul 21 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130069632):
<p>OK--I've updated my tactic.  It looks like this now:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">divide_lambda</span> <span class="o">:</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">binder_info</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="bp">`</span><span class="o">(</span><span class="n">andFuns</span> <span class="err">%%</span><span class="n">l</span> <span class="err">%%</span><span class="n">r</span><span class="o">)</span> <span class="n">y</span> <span class="o">:=</span>
      <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">andFuns</span><span class="o">)</span> <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">l</span> <span class="n">y</span><span class="o">))</span>
                           <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">r</span> <span class="n">y</span><span class="o">))</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="bp">`</span><span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="err">%%</span><span class="n">ll</span><span class="o">))</span> <span class="n">y</span> <span class="o">:=</span>
      <span class="o">(</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="err">%%</span><span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">ll</span> <span class="n">y</span><span class="o">))))</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="o">(</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="o">(</span><span class="n">app</span> <span class="n">x</span> <span class="n">y</span><span class="o">))</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">transform_lambda_app</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="o">(</span><span class="n">app</span> <span class="n">x</span> <span class="n">y</span><span class="o">))</span> <span class="n">val</span><span class="o">)</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="n">val</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">id</span> <span class="err">%%</span><span class="o">(</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="o">(</span><span class="n">app</span> <span class="n">x</span> <span class="n">y</span><span class="o">)))</span> <span class="n">val</span><span class="o">)</span> <span class="o">:=</span> <span class="n">some</span> <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="n">val</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">none</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">split_lambda</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="o">{</span> <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
     <span class="n">trace</span> <span class="n">t</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">,</span>
     <span class="n">nt</span> <span class="err">←</span> <span class="n">transform_lambda_app</span> <span class="n">t</span><span class="o">,</span>
     <span class="n">trace</span> <span class="n">nt</span><span class="bp">.</span><span class="n">to_raw_fmt</span><span class="o">,</span>
     <span class="n">change</span> <span class="n">nt</span> <span class="o">}</span>
</pre></div>


<p>I' trying to use it in this theorem:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">capture</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">id</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">andFuns</span> <span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="n">test3</span> <span class="n">x</span><span class="o">))</span> <span class="n">test</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span><span class="bp">+</span><span class="n">q</span><span class="o">))</span> <span class="n">v</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">split_lambda</span><span class="o">,</span>
    <span class="c1">--change</span>
    <span class="c1">--    andFuns (existsFuns (λ (y e:ℕ), test3 y (e+q)))</span>
    <span class="c1">--            (λ (e:ℕ), test (e + q)) v,</span>
<span class="kn">end</span>
</pre></div>


<p>It seems like no output goal is being generated.  I suspect the tactic is crashing somehow.  Is the pattern matching being done properly in divide_lambda?</p>

#### [ Mario Carneiro (Jul 21 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130069868):
<p>I get an error <code>trying to evaluate sorry</code> in the test theorem, which means that there is a syntax error in the tactic</p>

#### [ Mario Carneiro (Jul 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130069927):
<p>and the error at <code>divide_lambda</code> says the <code>existsFuns</code> branch has incorrect type <code>expr -&gt; expr</code> instead of <code>expr</code></p>

#### [ Mario Carneiro (Jul 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130069932):
<p>because you used <code>expr.app</code> applied to only one argument</p>

#### [ Ken Roe (Jul 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Compound%20statment%20to%20admit%20second%20goal%20of%20have/near/130071032):
<p>OK-- I fixed divide_lambda</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">divide_lambda</span> <span class="o">:</span> <span class="n">name</span> <span class="bp">→</span> <span class="n">binder_info</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="bp">`</span><span class="o">(</span><span class="n">andFuns</span> <span class="err">%%</span><span class="n">l</span> <span class="err">%%</span><span class="n">r</span><span class="o">)</span> <span class="n">y</span> <span class="o">:=</span>
      <span class="o">(</span><span class="n">app</span> <span class="o">(</span><span class="n">app</span> <span class="bp">`</span><span class="o">(</span><span class="n">andFuns</span><span class="o">)</span> <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">l</span> <span class="n">y</span><span class="o">))</span>
                           <span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">r</span> <span class="n">y</span><span class="o">))</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="bp">`</span><span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="err">%%</span><span class="n">ll</span><span class="o">))</span> <span class="n">y</span> <span class="o">:=</span>
      <span class="bp">`</span><span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="err">%%</span><span class="o">(</span><span class="n">divide_lambda</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">ll</span> <span class="n">y</span><span class="o">)))</span>
<span class="bp">|</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:=</span> <span class="o">(</span><span class="n">lam</span> <span class="n">n</span> <span class="n">b</span> <span class="n">e1</span> <span class="o">(</span><span class="n">app</span> <span class="n">x</span> <span class="n">y</span><span class="o">))</span>
</pre></div>


<p>but I get the error:</p>
<div class="codehilite"><pre><span></span><span class="n">tactic</span><span class="bp">.</span><span class="n">change</span> <span class="n">failed</span><span class="o">,</span> <span class="n">given</span> <span class="n">type</span>
  <span class="n">andFuns</span> <span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">v</span> <span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">test3</span> <span class="n">e</span> <span class="o">(</span><span class="n">e</span> <span class="bp">+</span> <span class="n">q</span><span class="o">)))</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">test</span> <span class="o">(</span><span class="n">e</span> <span class="bp">+</span> <span class="n">q</span><span class="o">))</span> <span class="n">v</span>
<span class="n">is</span> <span class="n">not</span> <span class="n">definitionally</span> <span class="n">equal</span> <span class="n">to</span>
  <span class="n">id</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">andFuns</span> <span class="o">(</span><span class="n">existsFuns</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">test3</span> <span class="n">x</span><span class="o">))</span> <span class="n">test</span> <span class="o">(</span><span class="n">e</span> <span class="bp">+</span> <span class="n">q</span><span class="o">))</span> <span class="n">v</span>
</pre></div>


<p>It appears the bound variable "x" is being changed to "e".  Why is this happening?  It appears the capture mechanism is not naming variables properly.</p>


{% endraw %}
