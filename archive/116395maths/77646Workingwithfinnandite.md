---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/77646Workingwithfinnandite.html
---

## Stream: [maths](index.html)
### Topic: [Working with `fin n` (and `ite`?)](77646Workingwithfinnandite.html)

---


{% raw %}
#### [ Johan Commelin (May 14 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534552):
<p>How should I do this:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">helpme</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">fin</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="c1">-- λ k, if k &lt; i then f ⟨k, sorry⟩ else if k = i then 0 else f (nat.pred k)</span>
</pre></div>

#### [ Johan Commelin (May 14 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534604):
<p>As you can see, I have a definition that almost works. (And I could get rid of the <code>sorry</code> in the middle by digging through some files in mathlib.)</p>

#### [ Kevin Buzzard (May 14 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534611):
<p>if <code>k : fin n</code> then <code>k</code> is a pair consisting of a nat and a proof that the nat is less than <code>n</code>.</p>

#### [ Kevin Buzzard (May 14 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534614):
<p>You can access each element of the pair with <code>k.1</code> and <code>k.2</code> for example</p>

#### [ Johan Commelin (May 14 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534617):
<p>But I am not sure if this is the right way to define this... for example, I want to prove that <code>helpme f</code> takes positive values if <code>f</code> does...</p>

#### [ Johan Commelin (May 14 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534630):
<p>And I just get a goal <code>0 &lt; ite ...</code> and I have no way how to tackle that.</p>

#### [ Kevin Buzzard (May 14 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534685):
<p>yeah, these CS people don't like <code>if</code>, I think it must be the new <code>goto</code> (for people old enough to remember that command)</p>

#### [ Johannes Hölzl (May 14 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534688):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> the first step is to simplify the problem: I guess you want a function like <code>fin n -&gt; fin (n+1)</code>. This can be done by doing it on the naturals (see <code>raise_fin</code> in <code>mathlib</code>s <code>data/fin.lean</code>).</p>

#### [ Johannes Hölzl (May 14 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534708):
<p>I like <code>if</code> and <code>if h :</code> the problem is that we don't have a if-splitter tactic (a tactic which looks for a <code>if</code> in your goal and introduces a cases for it)</p>

#### [ Johan Commelin (May 14 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534755):
<p>No, I'm going in the opposite direction of <code>raise_fin</code></p>

#### [ Johannes Hölzl (May 14 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534756):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> if you see a <code>ite</code> and don't know how to continuous: do the case distinction by <code>by_cases p</code> and then rewrite using <code>if_pos</code> and <code>if_neg</code> (or if it is a dependent if then <code>dif_neg</code> and <code>dif_pos</code>).</p>

#### [ Johannes Hölzl (May 14 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534767):
<p>like <code>fin.succ</code>?</p>

#### [ Johan Commelin (May 14 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534881):
<p>No, I just want to skip one <code>i : fin (n+1)</code>, and in this way get a function on <code>n</code> elements... I then collapse the domain to <code>fin n</code></p>

#### [ Johan Commelin (May 14 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534923):
<p>Sorry, I see that I messed up my types...</p>

#### [ Johan Commelin (May 14 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534924):
<p>Let me fix it</p>

#### [ Johannes Hölzl (May 14 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534937):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">fin</span><span class="bp">.</span><span class="n">lift</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">))</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="k">if</span> <span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">j</span><span class="bp">.</span><span class="mi">1</span> <span class="k">then</span> <span class="n">j</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="k">else</span> <span class="n">j</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="n">by_cases</span> <span class="o">(</span><span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">j</span><span class="bp">.</span><span class="mi">1</span><span class="o">),</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">if_pos</span> <span class="n">h</span><span class="o">],</span> <span class="n">exact</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_lt_succ</span> <span class="n">j</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">if_neg</span> <span class="n">h</span><span class="o">],</span> <span class="n">exact</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_of_lt</span> <span class="n">j</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">}</span>
  <span class="kn">end</span><span class="bp">⟩</span>
</pre></div>

#### [ Johannes Hölzl (May 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534978):
<p>Argh, sorry wrong way around... (CORRECTED)</p>

#### [ Johan Commelin (May 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534980):
<p>Thanks!</p>

#### [ Johan Commelin (May 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126534982):
<p>That gives me the idea on how to work with this stuff</p>

#### [ Johan Commelin (May 14 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535054):
<p>I also fixed my type signature</p>

#### [ Johannes Hölzl (May 14 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535116):
<p>I was working a little bit on cubes and chains (see: <a href="https://gist.github.com/johoelzl/ace6a2304b58f77a561777f6ac411647" target="_blank" title="https://gist.github.com/johoelzl/ace6a2304b58f77a561777f6ac411647">https://gist.github.com/johoelzl/ace6a2304b58f77a561777f6ac411647</a> )<br>
I didn't yet continue it, but it might be worthwhile to use <code>vector n R</code> instead of <code>fin n -&gt; R</code>. I'm still unsure about this...</p>

#### [ Johan Commelin (May 14 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535129):
<p>In the end, I think <code>fin n</code> is a particularly good choice for this. Because <code>fin n</code> are the objects of the simplex category</p>

#### [ Johan Commelin (May 14 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535176):
<p>We just need to define all the maps <code>fin n \to fin m</code></p>

#### [ Johan Commelin (May 14 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535182):
<p>And I am currently struggling with the incarnation in the singular chain complex...</p>

#### [ Johan Commelin (May 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535564):
<p>Anyway, I am voting for an <code>ite</code> tactic. Maybe I'll try to cargo-cult it myself after I've defined singular homology.</p>

#### [ Kevin Buzzard (May 14 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535796):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> You are running into the same sort of issues, in a broad sense, that I am currently running into. You want to model certain things (e.g. R^n) and there are several equivalent ways of doing it (e.g. lists of length n, "vector n", or an inductive definition). My impression is that it's a bit of a dark art to see which definition is "best". As mathematicians we regard all these definitions as trivially equivalent, and indeed are capable of switching between various ways of thinking about one underlying idea without ever even fussing about the details, because we all know how to switch. In this game, every time you switch then all of a sudden the lemma or definition you had in one of the contexts becomes unavailable and you either end up writing infrastructure which will help you to switch between the notions, or (and my impression is that this is what the CS people advocate) deciding what the "best" way to do it is (you see that this is the question Johannes raises -- it is far far more important for CS people than for maths people) and writing everything for this decision and then writing the functions which translate to and from other situations.</p>

#### [ Kevin Buzzard (May 14 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535805):
<p>I'm now just about sufficiently competent at Lean to be able to make a really lousy decision about how to model a situation and then struggle through all the proofs I need using this model.</p>

#### [ Kevin Buzzard (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535850):
<p>If you want my advice then find some mathlib functions related to what you're doing and see how a CS person does it.</p>

#### [ Johan Commelin (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535851):
<p>Yes, I think I agree. (Though your problems are way bigger then mine...)</p>

#### [ Kevin Buzzard (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535854):
<p>This morning I wanted to say something was compact</p>

#### [ Kevin Buzzard (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535856):
<p>so I just wrote down some random definition of compact</p>

#### [ Kevin Buzzard (May 14 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535857):
<p>and then wrote 100 lines of code</p>

#### [ Kevin Buzzard (May 14 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535861):
<p>and then I actually wanted to use some compactness result from the library</p>

#### [ Kevin Buzzard (May 14 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535870):
<p>and then found that they had a trivially equivalent but in some sense completely different way of saying "finite subcover"</p>

#### [ Kevin Buzzard (May 14 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535921):
<p>and of course it's at this point that you realise that their way of doing it is mathematically equivalent but, in terms of usability, much better.</p>

#### [ Kevin Buzzard (May 14 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126535932):
<p>So before you write too much more code you might want to explain what you want to do and suggest some basic definitions which will be at the foundation of everything, and then see what the CS people think of them.</p>

#### [ Mario Carneiro (May 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126550609):
<p>Re: <code>fin</code>, I did a lot of index work like this in <code>dioph</code>, using <code>fin2</code> for convenience. It might help to look at stuff like <code>insert_perm</code> and <code>remap_left</code></p>

#### [ Johan Commelin (May 14 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Working%20with%20%60fin%20n%60%20%28and%20%60ite%60%3F%29/near/126552700):
<p>Thanks!</p>


{% endraw %}
