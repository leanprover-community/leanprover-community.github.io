---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/47790deltarings.html
---

## Stream: [maths](index.html)
### Topic: [delta rings](47790deltarings.html)

---


{% raw %}
#### [ Johan Commelin (Jul 20 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993188):
<p>Fix a prime <code>p</code>.</p>

#### [ Kenny Lau (Jul 20 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993189):
<p>57</p>

#### [ Johan Commelin (Jul 20 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993230):
<p>Consider the following attempt at a definition:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">delta_ring</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="kn">extends</span> <span class="n">comm_ring</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">δ</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span>
<span class="o">(</span><span class="n">add_prop</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span><span class="o">},</span> <span class="n">δ</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">δ</span><span class="o">(</span><span class="n">a</span><span class="o">)</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="n">δ</span><span class="o">(</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="n">b</span><span class="err">^</span><span class="n">p</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="n">p</span><span class="o">)</span><span class="bp">/</span><span class="n">p</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Jul 20 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993244):
<p>How should one explain to Lean that <code>(a^p + b^p - (a+b)^p)/p</code> in fact makes sense?</p>

#### [ Kenny Lau (Jul 20 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993254):
<p>must that expression have a unique value?</p>

#### [ Kenny Lau (Jul 20 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993256):
<p>yes</p>

#### [ Kenny Lau (Jul 20 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993260):
<p>you can define a function that spits out that value?</p>

#### [ Johan Commelin (Jul 20 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993265):
<p>Yes, you can. But doesn't that make the definition extremely convoluted?</p>

#### [ Kenny Lau (Jul 20 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993273):
<p>delta_ring.aux : A \to A \to prime \to A</p>

#### [ Johan Commelin (Jul 20 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993326):
<p>And I guess Lean gets happier if I give an explicit definition? Instead of just claiming that the value exists because certain binomial coefficients will always have a factor <code>p</code>?</p>

#### [ Kenny Lau (Jul 20 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993331):
<p>at least I would be happier</p>

#### [ Johan Commelin (Jul 20 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993446):
<p>Here is the full "definition":</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">delta_ring</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="kn">extends</span> <span class="n">comm_ring</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">δ</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">A</span><span class="o">)</span>
<span class="o">(</span><span class="n">zero_prop</span> <span class="o">:</span> <span class="n">δ</span><span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">one_prop</span> <span class="o">:</span> <span class="n">δ</span><span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="o">(</span><span class="n">add_prop</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span><span class="o">},</span> <span class="n">δ</span><span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">δ</span><span class="o">(</span><span class="n">a</span><span class="o">)</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="n">δ</span><span class="o">(</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="n">b</span><span class="err">^</span><span class="n">p</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="n">p</span><span class="o">)</span><span class="bp">/</span><span class="n">p</span><span class="o">)</span>
<span class="o">(</span><span class="n">mul_prop</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span><span class="o">},</span> <span class="n">δ</span><span class="o">(</span><span class="n">a</span><span class="bp">*</span><span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span><span class="err">^</span><span class="n">p</span><span class="bp">*</span><span class="n">δ</span><span class="o">(</span><span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="n">b</span><span class="err">^</span><span class="n">p</span><span class="bp">*</span><span class="n">δ</span><span class="o">(</span><span class="n">a</span><span class="o">)</span> <span class="bp">+</span> <span class="n">p</span><span class="bp">*</span><span class="n">δ</span><span class="o">(</span><span class="n">a</span><span class="o">)</span><span class="bp">*</span><span class="n">δ</span><span class="o">(</span><span class="n">b</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Jul 20 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993460):
<p>would you say that including <code>^</code> make the definition more convoluted?</p>

#### [ Johan Commelin (Jul 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993517):
<p>What do you mean?</p>

#### [ Johan Commelin (Jul 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993524):
<p>Ok, I see what you are getting at...</p>

#### [ Kenny Lau (Jul 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993526):
<p><code>^</code> is also an auxiliary function that doesn't follow from the ring axioms</p>

#### [ Johan Commelin (Jul 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993538):
<p>Well, as a mathematician, I am used to the notation <code>^</code>, but not to the function <code>delta_ring.aux</code>.</p>

#### [ Kenny Lau (Jul 20 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993539):
<p>that's an arbitrary distinction</p>

#### [ Johan Commelin (Jul 20 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993552):
<p>By that logic every definition in maths is arbitrary.</p>

#### [ Kenny Lau (Jul 20 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993609):
<p>alright</p>

#### [ Johan Commelin (Jul 20 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993628):
<p>Anyway, do you think it is easy to define <code>aux</code> constructively?</p>

#### [ Kenny Lau (Jul 20 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993631):
<p>I think the function ((a+b)^p-a^p-b^p)/p might be useful more generally</p>

#### [ Kenny Lau (Jul 20 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993686):
<p>hmm, let me think about that</p>

#### [ Johan Commelin (Jul 20 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993702):
<p>I guess I first need to prove that <code>binom p i</code> is divisible by <code>p</code> for <code>0 &lt; i &lt; p</code>.</p>

#### [ Kenny Lau (Jul 20 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993748):
<p>can we somehow extend that definition to all natural numbers?</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993814):
<p>no, p has to be prime (if you are working over an arbitrary ring)</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993818):
<p>Kenny didn't you already write this function somehow?</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993832):
<p>I think Chris did some binomial / factorial things</p>

#### [ Kenny Lau (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993835):
<p>f(a,b,2) = ab<br>
f(a,b,3) = aab+abb<br>
f(a,b,5) = aaaab+2aaabb+2aabbb+abbbb<br>
f(a,b,7) = aaaaaab+3aaaaabb+5aaaabbb+5aaabbbb+3aabbbbb+abbbbbb</p>

#### [ Kenny Lau (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993838):
<p>there's nothing that can go between the lines?</p>

#### [ Kenny Lau (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993841):
<p>hmm</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993843):
<p>no</p>

#### [ Kenny Lau (Jul 20 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993849):
<p>what does a mathematician think about this function?</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993887):
<p>If Chris proved that binom p i * i! * (p-i)! = p! then proving it's a multiple of p is fine as long as you know that if p divides ab then p divides a or b.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993894):
<p>You then prove that p doesn't divide i! for i&lt;p and you're done</p>

#### [ Kenny Lau (Jul 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993914):
<p>I know that "pCa is divisible by p for all a" iff p is a prime</p>

#### [ Kenny Lau (Jul 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993918):
<p>i'm asking whether that function can be extended</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993933):
<p>sure it can be extended -- just define it to be 37 for n not prime</p>

#### [ Kenny Lau (Jul 20 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129993941):
<p>well</p>

#### [ Kenny Lau (Jul 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994038):
<p>I think the GPOV is to define the relevant elements of Z[X,Y] first</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994048):
<p>You're inventing Witt vectors</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994051):
<p>you can do stuff for prime powers somehow</p>

#### [ Kenny Lau (Jul 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994052):
<p>indeed</p>

#### [ Johan Commelin (Jul 20 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994100):
<p>Alternatively, Kenny puts Witt vectors into mathlib (-;</p>

#### [ Johan Commelin (Jul 20 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994126):
<p>I mean, we are doing this perfectoid stuff. But the mathematicians are already moving on...</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994127):
<p>The trendy way to do Witt vectors nowadays is to note that if k is a perfect field of char p and R is a k-algebra then the cotangent complex vanishes</p>

#### [ Kevin Buzzard (Jul 20 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994138):
<p>a la Scholze perfectoid spaces paper</p>

#### [ Johan Commelin (Jul 20 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994141):
<p>Nowadays you're only hot if you're doing diamonds or prisms...</p>

#### [ Patrick Massot (Jul 20 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994229):
<p>Let's try perfectoid spaces first...</p>

#### [ Johan Commelin (Jul 20 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994239):
<p>(Kevin, I think the perfectoid project is really cool. So I'm just trying to do some related things to the side, while you are wrapping up <code>Cont</code> et al.)</p>

#### [ Kenny Lau (Jul 20 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994278):
<p>where are the prism emojis when I need them</p>

#### [ Kenny Lau (Jul 20 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994432):
<p>do we have valuations of integers at a prime?</p>

#### [ Kenny Lau (Jul 20 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994437):
<p>I think Alexandria has that</p>

#### [ Johan Commelin (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994447):
<p>Ok, mathlib knows how to raise ring elements to <code>nat</code>-powers, right? Why is this failing?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Frob</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">A</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span><span class="err">^</span><span class="n">p</span>
</pre></div>


<p>Error:</p>
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">Prime</span><span class="o">,</span>
<span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">A</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">A</span>
<span class="err">⊢</span> <span class="n">has_pow</span> <span class="n">A</span> <span class="bp">ℕ</span>
</pre></div>

#### [ Kenny Lau (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994461):
<p>did you import the right things?</p>

#### [ Johan Commelin (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994463):
<p>No</p>

#### [ Kenny Lau (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994465):
<p>that's why</p>

#### [ Johan Commelin (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994467):
<p>Hmmm, I want Lean to tell me what to import...</p>

#### [ Patrick Massot (Jul 20 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994468):
<p>Johan, if you don't know what to do for the perfectoid project, you can do</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">prod</span> <span class="o">[</span><span class="n">complete_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">complete_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">complete_space</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">instance</span> <span class="n">separated</span><span class="bp">.</span><span class="n">prod</span> <span class="o">[</span><span class="n">separated</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">separated</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">separated</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>which is on my TODO list</p>

#### [ Kenny Lau (Jul 20 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994510):
<p>imports? <span class="user-mention" data-user-id="110031">@Patrick Massot</span></p>

#### [ Kenny Lau (Jul 20 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994523):
<p>and is that MWE?</p>

#### [ Kenny Lau (Jul 20 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994564):
<p>never mind</p>

#### [ Patrick Massot (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994623):
<p><code>import analysis.topology.uniform_space</code></p>

#### [ Patrick Massot (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994632):
<p>and then you get a MWE</p>

#### [ Kenny Lau (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994637):
<p>hmm</p>

#### [ Patrick Massot (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994640):
<p>I'm not saying this is difficult</p>

#### [ Patrick Massot (Jul 20 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129994650):
<p>I see Johan is blocked because he waits for Kevin</p>

#### [ Kevin Buzzard (Jul 20 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995452):
<p>I am dealing with universe issues raised by Mario. I have defined an "equivalence class of valuations" on (R : Type u) to be a pre-order on R which is induced from a valuation v : R -&gt; M with M a certain kind of totally ordered monoid, with (M : Type u). I now have to prove that if M had type v then actually there's M' of type u inducing the same pre-order. I dug and dug, and I am now having to define universal properties of quotient groups. But I've screwed up:</p>
<p><a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/a0d3bd5de20ed91d2e318914bac742c073b3c4f7/src/for_mathlib/quotient_group.lean#L48" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/a0d3bd5de20ed91d2e318914bac742c073b3c4f7/src/for_mathlib/quotient_group.lean#L48">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/a0d3bd5de20ed91d2e318914bac742c073b3c4f7/src/for_mathlib/quotient_group.lean#L48</a></p>
<p>I need to prove that if G is commutative then so is G/N but I think I managed to define multiplication on G in two different ways. I'm spending all day dealing with admin though. If anyone wants to fix up my easy group theory stuff then feel free!</p>

#### [ Kevin Buzzard (Jul 20 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995483):
<p>I will get back to all this this evening hopefully</p>

#### [ Johan Commelin (Jul 20 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995722):
<p>Ok, I started doing this because I was watching Bhargav Bhatt's talk from the Gabber birthday conference.</p>

#### [ Johan Commelin (Jul 20 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995792):
<p>It's quite fun! So far I've got: <a href="https://gist.github.com/jcommelin/b09dcc1c3494e123e84afc96a91fd61c" target="_blank" title="https://gist.github.com/jcommelin/b09dcc1c3494e123e84afc96a91fd61c">https://gist.github.com/jcommelin/b09dcc1c3494e123e84afc96a91fd61c</a></p>

#### [ Johan Commelin (Jul 20 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995813):
<p>Making good use of <code>tactic.ring</code>!</p>

#### [ Kenny Lau (Jul 20 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995924):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">wtf</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">A</span><span class="o">)</span> <span class="o">(</span><span class="n">T</span> <span class="o">:</span> <span class="n">set</span> <span class="n">B</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">set</span><span class="bp">.</span><span class="n">prod</span> <span class="n">S</span> <span class="n">T</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">inter</span> <span class="o">(</span><span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">S</span><span class="o">)</span> <span class="o">(</span><span class="n">prod</span><span class="bp">.</span><span class="n">snd</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">T</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Jul 20 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995932):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span>

<span class="kn">instance</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">prod</span> <span class="o">[</span><span class="n">complete_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">complete_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">complete_space</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">f</span> <span class="n">hf</span><span class="o">,</span>
    <span class="k">let</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="n">hx1</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span> <span class="err">$</span> <span class="n">cauchy_map</span> <span class="n">uniform_continuous_fst</span> <span class="n">hf</span> <span class="k">in</span>
    <span class="k">let</span> <span class="bp">⟨</span><span class="n">x2</span><span class="o">,</span> <span class="n">hx2</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span> <span class="err">$</span> <span class="n">cauchy_map</span> <span class="n">uniform_continuous_snd</span> <span class="n">hf</span> <span class="k">in</span>
    <span class="bp">⟨</span><span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">x2</span><span class="o">),</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">nhds_prod_eq</span><span class="o">,</span> <span class="n">filter</span><span class="bp">.</span><span class="n">prod_def</span><span class="o">]</span><span class="bp">;</span>
      <span class="k">from</span> <span class="n">filter</span><span class="bp">.</span><span class="n">le_lift</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">s</span> <span class="n">hs</span><span class="o">,</span> <span class="n">filter</span><span class="bp">.</span><span class="n">le_lift&#39;</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">t</span> <span class="n">ht</span><span class="o">,</span>
        <span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">f</span><span class="bp">.</span><span class="n">sets</span> <span class="o">:=</span> <span class="n">hx1</span> <span class="n">hs</span><span class="o">,</span>
        <span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">prod</span><span class="bp">.</span><span class="n">snd</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">t</span> <span class="err">∈</span> <span class="n">f</span><span class="bp">.</span><span class="n">sets</span> <span class="o">:=</span> <span class="n">hx2</span> <span class="n">ht</span><span class="o">,</span>
        <span class="n">filter</span><span class="bp">.</span><span class="n">inter_mem_sets</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">)</span><span class="bp">⟩</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Jul 20 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995939):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span></p>

#### [ Kenny Lau (Jul 20 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129995948):
<p>26 minutes</p>

#### [ Patrick Massot (Jul 20 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/129996119):
<p>Thanks!</p>

#### [ Johan Commelin (Jul 20 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001219):
<p>I still don't really know how to go about defining</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">delta_ring</span><span class="bp">.</span><span class="n">aux</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="c1">-- λ a b, (a^p + b^p - (a+b)^p)/p</span>
</pre></div>


<p>I know how to do this in maths, but I don't know how to go forward in Lean.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001353):
<p>I'm not saying it's the best way, but one way would be to define the function from fin (p-1) to nat sending i to (p choose i) / p, and then do a finset.sum [I guess you need p as an input for this function].</p>

#### [ Kevin Buzzard (Jul 20 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001422):
<p>Presumably at some point though you'll need that p times your function is what you want it to be, and there you'll need the binomial theorem, which <span class="user-mention" data-user-id="110044">@Chris Hughes</span> has done I believe. Looking at what he did might help.</p>

#### [ Johan Commelin (Jul 20 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001461):
<p>Ok, I already have that property stated (and sorried). So I'm able to prove properties of delta rings already (-;</p>

#### [ Johan Commelin (Jul 20 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130001483):
<p>I'll take a look at what Chris did.</p>

#### [ Chris Hughes (Jul 20 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130004696):
<blockquote>
<p>Presumably at some point though you'll need that p times your function is what you want it to be, and there you'll need the binomial theorem, which <span class="user-mention" data-user-id="110044">@Chris Hughes</span> has done I believe. Looking at what he did might help.</p>
</blockquote>
<p>I can PR it, but I'm not sure whether to call it <code>binomial</code> or <code>add_pow</code>.</p>

#### [ Johan Commelin (Jul 20 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008512):
<p>I wouldn't mind if well-known theorems with well-known names preserve their well-known names.</p>

#### [ Johan Commelin (Jul 20 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008530):
<p>To me it would increase readability of proofs</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008597):
<p>How do you feel about a random German in 1992 deciding to call his seminorms valuations even though they are seminorms, and now we have this annoying problem that our definition of valuation in the perfectoid project is both standard and non-standard simultaneously? :-/</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008664):
<p>If someone told me that we were going to ditch that stupid bracket notation for quadratic residues, I would crack open the champagne.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008683):
<p>Oh -- wait -- for binomial we can just call it both</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008712):
<p>that's what they do with left_distrib, right? That's the formally correct historical name, but add_mul (or mul_add, which ever one left distrib is) is a modern sensible name.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008795):
<p>Chris -- do you prove that <code>binomial(a,b)*b!*(a-b)!=a!</code>?</p>

#### [ Kenny Lau (Jul 20 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008811):
<p>do we have valuation of an integer over a prime?</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008820):
<p>It's <code>list.count p (factor n)</code> Kenny</p>

#### [ Johan Commelin (Jul 20 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008827):
<p>Kevin, it is <code>choose(a,b)</code>, I think. So we can call the binomial theorem <code>binomial</code>, if we want...</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008944):
<p><code>factors n</code> sorry</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130008945):
<p><a href="https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean">https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean</a></p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130009004):
<p>lines 226 and 236 show that that's a list of the primes dividing n with multiplicity</p>

#### [ Kevin Buzzard (Jul 20 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130009294):
<p><a href="https://github.com/dorhinj/leanstuff/blob/3dbf2626138fa7d4ae8ba6d55529713e2d5acd3a/choose.lean#L55" target="_blank" title="https://github.com/dorhinj/leanstuff/blob/3dbf2626138fa7d4ae8ba6d55529713e2d5acd3a/choose.lean#L55">https://github.com/dorhinj/leanstuff/blob/3dbf2626138fa7d4ae8ba6d55529713e2d5acd3a/choose.lean#L55</a> -- there's the factorial fact</p>

#### [ Chris Hughes (Jul 20 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130011551):
<blockquote>
<p><a href="https://github.com/dorhinj/leanstuff/blob/3dbf2626138fa7d4ae8ba6d55529713e2d5acd3a/choose.lean#L55" target="_blank" title="https://github.com/dorhinj/leanstuff/blob/3dbf2626138fa7d4ae8ba6d55529713e2d5acd3a/choose.lean#L55">https://github.com/dorhinj/leanstuff/blob/3dbf2626138fa7d4ae8ba6d55529713e2d5acd3a/choose.lean#L55</a> -- there's the factorial fact</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> It's also here <a href="https://github.com/leanprover/mathlib/blob/master/data/nat/choose.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/nat/choose.lean">https://github.com/leanprover/mathlib/blob/master/data/nat/choose.lean</a></p>

#### [ Kevin Buzzard (Jul 20 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130012395):
<p>I couldn't find the binomial theorem though</p>

#### [ Chris Hughes (Jul 20 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130012405):
<p>I haven't PRed it yet.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130012416):
<p>I mean I couldn't find it in your github repo</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130014183):
<p>Question: Why is <code>(a^p + b^p - (a+b)^p)/p</code> uniquely defined? Is division by <code>p</code> always uniquely defined (when applied to multiples of <code>p</code>)? Seems like if the ring has characteristic <code>p</code> this will be a problem...</p>

#### [ Kenny Lau (Jul 20 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130014372):
<p>it isn't uniquely defined, but there's a canonical choice</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130014441):
<p>It's good old informal mathematicians again, meaning "do it in Q, note the answer is in Z, now map it into any ring"</p>

#### [ Johan Commelin (Jul 20 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130014936):
<blockquote>
<p>it isn't uniquely defined, but there's a canonical choice</p>
</blockquote>
<p>Did you just use the word 'choice'?</p>

#### [ Johan Commelin (Jul 20 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015002):
<p>I just realised that I think Witt vectors and Hensel's lemma are two very nice (and manageable, I hope) companions to the perfectoid project. They aren't logically necessary, but I think they might be really helpful if one wants to do some examples...</p>

#### [ Kenny Lau (Jul 20 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015089):
<p>yeah, I chose the word "choice"</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015091):
<p>I think it's a shame that you have to write it this roundabout way, since it loses the clarity</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015112):
<p>Another way to say what you are trying to say is to form <code>x^p + y^p - (x+y)^p</code> as a multivariate polynomial in Z[x,y], divide by <code>p</code>, and evaluate it at <code>a,b</code></p>

#### [ Johan Commelin (Jul 20 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015162):
<p>Yes, I completely agree. But I don't know yet how to convince Lean that I can divide that polynomial by <code>p</code></p>

#### [ Mario Carneiro (Jul 20 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015179):
<p>As a polynomial in <code>Z[x,y]</code>, you can use <code>int.div</code> on the coefficients</p>

#### [ Johan Commelin (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015193):
<p>Aah, and that is always defined, although it sometimes outputs 57. Is that right?</p>

#### [ Johan Commelin (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015200):
<p>Or probably the floor of x / y.</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015202):
<p>yes that</p>

#### [ Johan Commelin (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015206):
<p>Ok, so then the definition is not hard.</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015209):
<blockquote>
<p>Another way to say what you are trying to say is to form <code>x^p + y^p - (x+y)^p</code> as a multivariate polynomial, divide by <code>p</code>, and evaluate it at <code>a,b</code></p>
</blockquote>
<p>This is just some standard polynomial which shows up in some graduate commutative algebra thing, so mathematicians abuse notation. It means exactly what you said yes. The polynomials even have names -- they're in Z[x,y] but then they get coerced into R[x,y] for any comm_ring R</p>

#### [ Kenny Lau (Jul 20 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015277):
<p>by GPOV</p>

#### [ Johan Commelin (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015306):
<p>So then I only need to prove the property that <code>p * aux_poly = x^p + y^p - (x+y)^p</code></p>

#### [ Johan Commelin (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015318):
<p>And that requires the binomial theorem</p>

#### [ Kenny Lau (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015319):
<p>aux_poly x y p</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015326):
<p>you're going to need the binomial theorem at some point</p>

#### [ Johan Commelin (Jul 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015329):
<p>sure</p>

#### [ Chris Hughes (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015370):
<p>It's in your stack project <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015374):
<p>I didn't think to look there</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015379):
<p>I don't think you actually need the binomial theorem for this, but you mathematicians like your hammers</p>

#### [ Johan Commelin (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015386):
<p>Why not?</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015389):
<p>It's an easy proof by induction</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015390):
<p>if you define <code>aux_poly</code> to be the explicit <code>(choose p i) / p</code> etc etc then it's the same as the binomial theorem</p>

#### [ Kenny Lau (Jul 20 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015397):
<p>it isn't because you can't fill in the gap that p causes</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015402):
<p>forget that</p>

#### [ Kenny Lau (Jul 20 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015406):
<p>you can't extend the definition of aux_poly to all nat</p>

#### [ Johan Commelin (Jul 20 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015419):
<p>you can, he just did that... but you get nonsense</p>

#### [ Patrick Massot (Jul 20 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015505):
<p>I'm trying to figure out what GPOV stand for (I mean understand the acronym, I understand the maths). Google is not very helpful</p>

#### [ Johan Commelin (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015601):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I just realised that trying to convert arithmetic geometers and/or number theorists to Lean is going to be futile. They start every talk with "For me all rings are commutative." If they can't do that at the top of their Lean files, and they really have to type <code>comm_ring</code> instead of <code>ring</code> all the time, they will drop out immediately...</p>

#### [ Johan Commelin (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015614):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> General Point Of View?</p>

#### [ Johan Commelin (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015628):
<p>There is also nPOV = n-categorical POV</p>

#### [ Kenny Lau (Jul 20 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015638):
<p>Grothendieck's point of view</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015717):
<p>you could always fork mathlib</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015731):
<p><code>comm_ring</code> is in core</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015735):
<p>oh crap</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015738):
<p><code>comm_ring</code> -&gt; <code>ring</code></p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015741):
<p><code>ring</code> -&gt; <code>non_comm_ring</code></p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015742):
<p>that's what it should be</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015765):
<p><code>local notation `ring` := comm_ring</code> should work</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015784):
<p>and then <code>local notation `non_comm_ring` := ring</code>?</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015846):
<p>do you actually care about that?</p>

#### [ Kevin Buzzard (Jul 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015854):
<p>I will grudgingly confess to occasionally using the ring of 2 x 2 matrices</p>

#### [ Kenny Lau (Jul 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015863):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> you're lucky all rings have unity</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015872):
<p>maybe don't use stupid overrides in that file</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015972):
<p>also, overriding the notation for <code>ring</code> doesn't prevent you from using matrix rings</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130015986):
<p>of course typeclass inference doesn't care about your notation</p>

#### [ Mario Carneiro (Jul 20 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130016100):
<p>Now I am picturing some mathematician starting their talk with "in this lecture, all rings are commutative" and proceed to do amazing things by commuting matrices that don't commute</p>

#### [ Johan Commelin (Jul 20 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130018032):
<blockquote>
<p>of course typeclass inference doesn't care about your notation</p>
</blockquote>
<p>It doesn't? I don't know if I am happy or sad about that...</p>

#### [ Mario Carneiro (Jul 20 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130018603):
<p>well the alternative is the "commutative by fiat" lecture scenario I mentioned</p>

#### [ Johan Commelin (Jul 23 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135388):
<p>Ok, so now I want to define the <code>aux_poly</code> in two variables. What would be the best way to do that? I currently have</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">delta_ring_aux_poly</span>

<span class="kn">open</span> <span class="n">mv_polynomial</span>

<span class="n">def</span> <span class="n">delta_ring</span><span class="bp">.</span><span class="n">aux_poly1</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">X0</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="n">X</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_lt_succ</span> <span class="mi">1</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">X1</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="n">X</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">le_refl</span> <span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">exact</span> <span class="o">(</span><span class="n">X0</span><span class="err">^</span><span class="n">p</span> <span class="bp">+</span> <span class="n">X1</span><span class="err">^</span><span class="n">p</span> <span class="bp">-</span> <span class="o">(</span><span class="n">X0</span><span class="bp">+</span><span class="n">X1</span><span class="o">)</span><span class="err">^</span><span class="n">p</span><span class="o">),</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">delta_ring</span><span class="bp">.</span><span class="n">aux_poly2</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">,</span> <span class="n">n</span><span class="bp">/</span><span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">zero_div</span> <span class="n">p</span><span class="o">)</span> <span class="n">delta_ring</span><span class="bp">.</span><span class="n">aux_poly1</span>

<span class="kn">end</span> <span class="n">delta_ring_aux_poly</span>

<span class="n">def</span> <span class="n">delta_ring</span><span class="bp">.</span><span class="n">aux</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">functorial</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast</span> <span class="n">delta_ring</span><span class="bp">.</span><span class="n">aux_poly2</span><span class="o">)</span><span class="bp">.</span><span class="kn">eval</span> <span class="err">∘</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">i</span><span class="o">,</span>
<span class="kn">end</span>
 <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">A</span> <span class="bp">→</span> <span class="o">((</span><span class="n">fin</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">→</span> <span class="n">A</span><span class="o">))</span>
<span class="c1">--  sorry</span>
<span class="c1">-- λ a b, (a^p + b^p - (a+b)^p)/p</span>
</pre></div>

#### [ Johan Commelin (Jul 23 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135453):
<p>It it better to use <code>choose</code> here, and explicitly define it as  some <code>finset.sum</code>?</p>

#### [ Johan Commelin (Jul 23 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135463):
<p>I don't really like the <code>finsupp.map_range</code>, but that is just <em>my</em> gut feeling.</p>

#### [ Mario Carneiro (Jul 23 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135543):
<p>This looks like a pretty faithful rendition of my suggestion</p>

#### [ Mario Carneiro (Jul 23 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135548):
<p>the last bit looks incomplete though</p>

#### [ Johan Commelin (Jul 23 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135588):
<p>It is.</p>

#### [ Johan Commelin (Jul 23 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135602):
<p>I don't know how to define functions out of <code>fin n</code>. Do we have to use if-then-else for that?</p>

#### [ Mario Carneiro (Jul 23 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135611):
<p>there should be a <code>fin.cons</code> function</p>

#### [ Mario Carneiro (Jul 23 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135619):
<p>you can also use a <code>match</code> block</p>

#### [ Mario Carneiro (Jul 23 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135625):
<p>there is <code>fin.cases</code></p>

#### [ Mario Carneiro (Jul 23 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135683):
<p>Probably it is easier to use <code>bool</code> rather than <code>fin 2</code> here</p>

#### [ Johan Commelin (Jul 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135764):
<p>Aah, that is a nice suggestion</p>

#### [ Johan Commelin (Jul 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135767):
<p>I'll try that</p>

#### [ Mario Carneiro (Jul 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135777):
<p>You can use <code>cond</code> to case on <code>bool</code></p>

#### [ Johan Commelin (Jul 23 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135846):
<p>Hmm, what exactly do you mean with that?</p>

#### [ Johan Commelin (Jul 23 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135892):
<p>Aah</p>

#### [ Johan Commelin (Jul 23 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135898):
<p>So <code>cond</code> is in fact my function. I want to look at <code>cond i a b</code></p>

#### [ Mario Carneiro (Jul 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130135907):
<p>yes</p>

#### [ Johan Commelin (Jul 23 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130136703):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Are you planning on PR-ing your binomial theorem sometime soon?</p>

#### [ Johan Commelin (Jul 23 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130144619):
<p>So, now I need to sum over <code>fin n</code>. Hooray! I don't even know how to deal with the case <code>n = 1</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="mi">57</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)),</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="err">^</span> <span class="n">x</span><span class="bp">.</span><span class="n">val</span><span class="o">))</span> <span class="bp">=</span>
    <span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="mi">0</span> <span class="mi">1</span><span class="o">)</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johan Commelin (Jul 23 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130144647):
<p>I would like to tell Lean that <code>finset.univ</code> is <code>singleton 0</code> in this case.</p>

#### [ Johan Commelin (Jul 23 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130144649):
<p>But I don't know how to do that.</p>

#### [ Johan Commelin (Jul 23 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130144655):
<p>(Technically <code>singleton \&lt;0,_\&gt;</code>...)</p>

#### [ Kenny Lau (Jul 23 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130145367):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="mi">57</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)),</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="err">^</span> <span class="n">x</span><span class="bp">.</span><span class="n">val</span><span class="o">))</span> <span class="bp">=</span>
    <span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="mi">0</span> <span class="mi">1</span><span class="o">)</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="o">:</span> <span class="n">finset</span> <span class="err">$</span> <span class="n">fin</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="mi">0</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">finset</span><span class="bp">.</span><span class="n">ext&#39;</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">begin</span>
    <span class="n">cases</span> <span class="n">hx</span> <span class="k">with</span> <span class="n">hx</span> <span class="n">hx1</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">simp</span><span class="o">,</span> <span class="n">refl</span> <span class="o">},</span>
    <span class="n">cases</span> <span class="n">hx1</span>
  <span class="kn">end</span><span class="o">,</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">H1</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum_singleton</span><span class="o">]</span><span class="bp">;</span> <span class="n">refl</span>
</pre></div>

#### [ Johan Commelin (Jul 23 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130145441):
<p>You were able to convince Lean that you get a singleton! I couldn't even get it to typecheck the type of H1.</p>

#### [ Johan Commelin (Jul 23 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/delta%20rings/near/130161570):
<blockquote>
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Are you planning on PR-ing your binomial theorem sometime soon?</p>
</blockquote>
<p>Thanks! <span class="emoji emoji-1f44f" title="clap">:clap:</span> <span class="emoji emoji-1f419" title="octopus">:octopus:</span></p>


{% endraw %}
