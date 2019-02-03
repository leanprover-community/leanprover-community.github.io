---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83047partialfunctions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [partial functions](https://leanprover-community.github.io/archive/113488general/83047partialfunctions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Victor Porton (Jul 07 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129261641):
<p>Why this does not work?</p>
<p>-- Switch from a function on a subset to a function to option monad<br>
def subfunc_to_option {α β: Type} {c: α → Prop} (f: {x:α // c x} → β) : α → option β :=<br>
λ y: α, if c y then some (f (<a href="http://subtype.mk" target="_blank" title="http://subtype.mk">subtype.mk</a> y (arbitrary (c y) [true_inhabited (c y)]))) else none</p>

#### [ Kenny Lau (Jul 07 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129261658):
<p>put [decidable_pred c] in the list of assumptions (before the colon)</p>

#### [ Victor Porton (Jul 07 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129261720):
<p>Kenny, I did what you say. Moreover <code>open classical</code> is already in effect. But it does not work now too</p>

#### [ Chris Hughes (Jul 07 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262022):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">subfunc_to_option</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">c</span><span class="o">]</span>
<span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">c</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">c</span> <span class="n">y</span> <span class="k">then</span> <span class="n">some</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">subtype</span><span class="bp">.</span><span class="n">mk</span> <span class="n">y</span> <span class="n">h</span><span class="o">))</span> <span class="k">else</span> <span class="n">none</span>
</pre></div>

#### [ Chris Hughes (Jul 07 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262116):
<p><code>if h : c y</code> instead of <code>if c y</code> gives you access to the proof.</p>

#### [ Victor Porton (Jul 07 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262182):
<p>Chris, Thanks it works now. But I am curious why my old code (with <code>arbitrary</code>) didn't work.</p>

#### [ Chris Hughes (Jul 07 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262210):
<p>Because there was no way of telling that the type <code>c y</code> was inhabited.</p>

#### [ Chris Hughes (Jul 07 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262269):
<p>It's actually very unusual to use <code>inhabited</code> on Props.</p>

#### [ Chris Hughes (Jul 07 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262352):
<p>Also <code>open classical</code> only opens the classical namespace, it doesn't give you decidability. You need <code>local attribute [instance] classical.prop_decidable</code> for that.</p>

#### [ Victor Porton (Jul 07 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262806):
<p>I tried to synthesize the function in another direction. Now I know where is my error but don't know how to fix it:</p>
<p>-- Switch from function to option monad to a function on a subset<br>
def option_to_subfunc {α β: Type} (f: α → (option β)) :=<br>
λ y: {x:α // f x ≠ none},<br>
match f y with<br>
| some x := y<br>
| none   := sorry</p>

#### [ Chris Hughes (Jul 07 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262898):
<p>You needed to give the type, and write <code>end</code> at the end of your <code>match</code></p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="bp">→</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">},</span>
<span class="k">match</span> <span class="n">f</span> <span class="n">y</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">y</span>
<span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Jul 07 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262906):
<p><span class="user-mention" data-user-id="119326">@Victor Porton</span> If you surround your code between three backticks, then it will be typeset in a codeblock. If you append "lean" to the first 3 backticks, then it will get highlighting!</p>

#### [ Kevin Buzzard (Jul 07 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262950):
<p>Again <code>f y</code> does not make sense because alpha is not equal to the subtype you are using. f wants an input of type alpha and you are feeding it <code>y</code>. Did you read about subtypes in Theorem in Lean?</p>

#### [ Victor Porton (Jul 07 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262952):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Your code does not validate. What I really wanted to ask is what to do instead of <code>sorry</code>. I am lost about this</p>

#### [ Chris Hughes (Jul 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262957):
<p>It does make sense because there's a coercion</p>

#### [ Victor Porton (Jul 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262963):
<p>Yes, I knew that here there is a coercion</p>

#### [ Kevin Buzzard (Jul 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262965):
<p>Oh -- it does make sense in this context because there's a coercion!</p>

#### [ Kevin Buzzard (Jul 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129262967):
<p>:-)</p>

#### [ Chris Hughes (Jul 07 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263099):
<p>In response to a question in (no topic) that should have been here.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="bp">→</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">},</span>
<span class="k">have</span> <span class="n">hfy</span> <span class="o">:</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">≠</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
<span class="k">match</span> <span class="n">f</span> <span class="n">y</span><span class="o">,</span> <span class="n">hfy</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">x</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hfy</span><span class="o">,</span> <span class="n">y</span>
<span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hfy</span><span class="o">,</span> <span class="o">(</span><span class="n">hfy</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span>
<span class="kn">end</span>
</pre></div>

#### [ Victor Porton (Jul 07 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263253):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span>  1.  The values type of your <code>option_to_subfunc</code> is wrong; it should be <code>\beta</code> not <code>{x:α // f x ≠ none}</code>. 2. Do I understand correctly that the values in <code>have</code> are "ignored" (not included into the result) when building the value of the defined object? 3. What this elimination do? (I am a very novice and understand your code partially.)</p>

#### [ Victor Porton (Jul 07 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263319):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Sorry for a stupid question but I do not understand what <code>:=</code> after <code>have</code> means</p>

#### [ Chris Hughes (Jul 07 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263329):
<p>It's the same as <code>from</code></p>

#### [ Victor Porton (Jul 07 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263344):
<p>I am trying to read your code</p>

#### [ Victor Porton (Jul 07 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263411):
<p>Sorry, what is <code>λ hfy, y</code>?</p>

#### [ Chris Hughes (Jul 07 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263412):
<p>I put <code>hfy</code> after the <code>match</code> so I would have access to the fact that <code>f y ≠ none</code>. In the <code>none</code> cases <code>hfy</code> has type <code>none ≠ none</code> which is obviously false, so I can use <code>false.elim</code> to define the function</p>

#### [ Chris Hughes (Jul 07 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263460):
<p><code>hfy</code> is just a proof that <code>f y = none</code> or in the <code>some</code> case that <code>some ≠ none</code></p>

#### [ Chris Hughes (Jul 07 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263520):
<p>I think this is the function you want</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">},</span>
<span class="k">have</span> <span class="n">hfy</span> <span class="o">:</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">≠</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
<span class="k">match</span> <span class="n">f</span> <span class="n">y</span><span class="o">,</span> <span class="n">hfy</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">x</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hfy</span><span class="o">,</span> <span class="n">x</span>
<span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hfy</span><span class="o">,</span> <span class="o">(</span><span class="n">hfy</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span>
<span class="kn">end</span>
</pre></div>

#### [ Victor Porton (Jul 07 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263532):
<p>what is <code>(hfy rfl).elim</code>?</p>

#### [ Chris Hughes (Jul 07 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263533):
<p><code>match f y, hfy with</code> means I now have to define a function with type <code>Π x : option β, x ≠ none → β </code></p>

#### [ Chris Hughes (Jul 07 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263572):
<p><code>hfy rfl</code> is a proof of <code>false</code></p>

#### [ Chris Hughes (Jul 07 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263574):
<p><code>(hfy rfl).elim</code> is another way of writing <code>false.elim (hfy rfl)</code>.</p>

#### [ Victor Porton (Jul 07 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263581):
<p>I need to time to review all you wrote</p>

#### [ Chris Hughes (Jul 07 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263582):
<p><code>false.elim</code> is a function that gives you a term of any type given a proof of <code>false</code></p>

#### [ Victor Porton (Jul 07 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263706):
<p>What I don't understand: Why is it <code>| some x := λ hfy, x</code> not <code>| some x := x</code>. It should be a value in <code>\b</code>, right? But <code>λ hfy, x</code> is a function and so it looks for me that it can't be in <code>\b</code></p>

#### [ Victor Porton (Jul 07 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263710):
<p>err.. wrong</p>

#### [ Chris Hughes (Jul 07 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263833):
<p><code>match f y, hfy</code> with means I now have to define a function with type <code>Π x : option β, x ≠ none → β</code>, not <code>option β → β</code> any more.  Even though I'm not using the fact that <code>x  ≠ none</code> in the <code>some</code> case, I still have access to it.</p>

#### [ Victor Porton (Jul 07 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263923):
<p>Hm, it is harder than I expected, I yet do not understand the details of this simple construct. I initially started to learn Lean to rewrite my English book in Lean. Now I suspect that it would take me too much time to master Lean. What is your advice: learn Lean or just to keep writing math in English?</p>

#### [ Chris Hughes (Jul 07 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129263975):
<p>What field of maths is your book on?</p>

#### [ Chris Hughes (Jul 07 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264037):
<p>I think maybe a good way to think about the function is that the output of type <code>β</code> is the function of type <code>Π x : option β, x ≠ none → β</code> applied to <code>f y</code> and <code>hfy</code></p>

#### [ Victor Porton (Jul 07 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264039):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I discovered a new subfield of general topology (though some man expressed that he does not consider it a subfield of general topology). For example the formula $f\circ\mu \leq \nu\circ f$ means that $f$ is a continuous morphisms from $\mu$ to $\nu$.</p>

#### [ Chris Hughes (Jul 07 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264095):
<p>I don't really know much about topology (I'm a first year undergraduate). I think <span class="user-mention" data-user-id="110031">@Patrick Massot</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  know about topology in lean.</p>

#### [ Victor Porton (Jul 07 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264096):
<p>Honestly, I am somehow lost in your Lean discussion. I may re-read it again</p>

#### [ Victor Porton (Jul 07 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264123):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> This does not matter, as I build my version of topology from scratch, without using the classical GT</p>

#### [ Victor Porton (Jul 07 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264230):
<p>Is <code>match f y, hfy</code> the same as <code>match \&lt;f y, hfy\&gt;</code>?</p>

#### [ Chris Hughes (Jul 07 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264474):
<p>more or less</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">},</span>
<span class="k">have</span> <span class="n">hfy</span> <span class="o">:</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">≠</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
<span class="k">match</span> <span class="o">(</span><span class="bp">⟨</span><span class="n">f</span> <span class="n">y</span><span class="o">,</span> <span class="n">hfy</span><span class="bp">⟩</span> <span class="o">:</span> <span class="err">Σ&#39;</span> <span class="n">x</span> <span class="o">:</span> <span class="n">option</span> <span class="n">β</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">)</span> <span class="k">with</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">some</span> <span class="n">x</span><span class="o">,</span> <span class="n">hfy</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">x</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">none</span><span class="o">,</span> <span class="n">hfy</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="o">(</span><span class="n">hfy</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Jul 07 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264557):
<p>I think that might be more confusing though.</p>

#### [ Victor Porton (Jul 07 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264689):
<p>It seems that I do (or almost do) understand your last ("more confusing") code. But why the "less confusing" code (which I don't understand) uses <code>some x := λ hfy, x</code> not <code>some x := x</code>?</p>

#### [ Victor Porton (Jul 07 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264699):
<p>oh, it seems I got the idea</p>

#### [ Victor Porton (Jul 07 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129264809):
<p>I have yet a question. How does the following work?</p>
<div class="codehilite"><pre><span></span><span class="k">match</span> <span class="n">f</span> <span class="n">y</span><span class="o">,</span> <span class="n">hfy</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">x</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hfy</span><span class="o">,</span> <span class="n">x</span>
<span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">hfy</span><span class="o">,</span> <span class="o">(</span><span class="n">hfy</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span>
<span class="kn">end</span>
</pre></div>


<p>We have two expressions in <code>match</code> arguments and just one in the math conditions. How do they match?</p>

#### [ Chris Hughes (Jul 07 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265113):
<p>I don't really understand enough about the equation compiler to answer the question properly.</p>

#### [ Victor Porton (Jul 07 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265139):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Anyway much thanks for your support. Also what does $\Sigma'$ mean? It has added apostrophe</p>

#### [ Victor Porton (Jul 07 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265189):
<p>Now I "almost" understand. Thanks</p>

#### [ Chris Hughes (Jul 07 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265206):
<p>It's just like Sigma, except the constructors can be either proofs or data, whereas Sigma only takes data.</p>

#### [ Chris Hughes (Jul 07 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265352):
<p>This is perhaps a better way of writing the function</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">},</span>
<span class="k">let</span> <span class="n">g</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">x</span> <span class="o">:</span> <span class="n">option</span> <span class="n">β</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
  <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">match</span> <span class="n">x</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">x</span>
  <span class="bp">|</span> <span class="n">none</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">h</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span>
  <span class="kn">end</span> <span class="k">in</span>
<span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">y</span><span class="o">)</span> <span class="n">y</span><span class="bp">.</span><span class="n">property</span>
</pre></div>

#### [ Victor Porton (Jul 07 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265357):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> It gets better as I rewrote it more understandably</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">},</span>
<span class="k">have</span> <span class="n">hfy</span> <span class="o">:</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">≠</span> <span class="n">none</span> <span class="o">:=</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
<span class="k">match</span> <span class="n">f</span> <span class="n">y</span><span class="o">,</span> <span class="n">hfy</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">x</span><span class="o">,</span> <span class="n">hfy</span> <span class="o">:=</span> <span class="n">x</span>
<span class="bp">|</span> <span class="n">none</span>  <span class="o">,</span> <span class="n">hfy</span> <span class="o">:=</span> <span class="o">(</span><span class="n">hfy</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span>
<span class="kn">end</span>
</pre></div>

#### [ Victor Porton (Jul 07 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265405):
<p>I don't understand your last code. For example, what is <code>property</code>?</p>

#### [ Chris Hughes (Jul 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265438):
<p>Another way of writing <code>y.2</code></p>

#### [ Victor Porton (Jul 07 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265498):
<p>Why do you think the the second way is better?</p>

#### [ Chris Hughes (Jul 07 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265655):
<p>I had to try out a few things to get the first way to work. For example this didn't work. I don't really have a good reason why the second way is better other than that. </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">},</span>
<span class="k">match</span> <span class="n">f</span> <span class="n">y</span><span class="o">,</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">some</span> <span class="n">x</span><span class="o">,</span> <span class="n">hfy</span> <span class="o">:=</span> <span class="n">x</span>
<span class="bp">|</span> <span class="n">none</span>  <span class="o">,</span> <span class="n">hfy</span> <span class="o">:=</span> <span class="o">(</span><span class="n">hfy</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Jul 07 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129265731):
<p>It's clearer what's going on, because in the first method, it's not obvious that hfy will have type <code>some x ≠ none</code> or <code>none ≠ none</code>, and not <code>f y ≠ none</code> in the match expression.</p>

#### [ Mario Carneiro (Jul 07 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129266827):
<p>In that last one, <code>y.2</code> has the type <code>f y.1 ≠ none</code>, so it is important that you write <code>f y.1</code> instead of <code>f (\u y)</code></p>

#### [ Patrick Massot (Jul 07 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129267274):
<p>What about </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">option</span><span class="bp">.</span><span class="n">is_some</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)}</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">|</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">get</span> <span class="n">h</span>
</pre></div>

#### [ Chris Hughes (Jul 07 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129267284):
<p>I thought the function probably already existed, but I couldn't find it.</p>

#### [ Patrick Massot (Jul 07 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129267287):
<p><code>option.is_some</code> is directly about what you care about instead of its negation</p>

#### [ Patrick Massot (Jul 07 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129267327):
<p>I don't know if it already exists</p>

#### [ Chris Hughes (Jul 07 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129267409):
<p>I think I saw it before, but I was thrown off by the fact <code>is_some</code> is <code>bool</code> rather than <code>Prop</code></p>

#### [ Patrick Massot (Jul 07 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129267412):
<p>Oh, you mean <code>is_some</code> already existed.</p>

#### [ Patrick Massot (Jul 07 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129267418):
<p>I thought you were referring to <code>option_to_subfunc</code></p>

#### [ Chris Hughes (Jul 07 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129267469):
<p>I was referring to <code>option_to_subfunc</code> or things like it, and I saw <code>option.get</code> but I didn't like it because <code>is_some</code> is <code>bool</code></p>

#### [ Victor Porton (Jul 07 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129270457):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> What is this <code>|</code>?</p>

#### [ Victor Porton (Jul 07 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129270466):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Oh, it is pattern matching, I got</p>

#### [ Victor Porton (Jul 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129270785):
<p>weird, I can't find <code>def option</code> in Lean library</p>

#### [ Victor Porton (Jul 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129270788):
<p>got: <code>inductive option</code></p>

#### [ Victor Porton (Jul 07 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129270836):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Where is <code>option.get</code> defined?</p>

#### [ Victor Porton (Jul 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129270857):
<p>found: <code>basic.lean</code></p>

#### [ Victor Porton (Jul 07 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129271074):
<p>I also don't understand <code>(hfy rfl).elim</code>. Does it contain <code>hfy</code> applied to <code>rfl</code>? I would be not surprised if <code>rfl</code> were applied to an equality, but I see inequality applied to <code>rfl</code> what looks for me the "opposite" of what can be done. What is it?</p>

#### [ Chris Hughes (Jul 07 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129271212):
<p><code>hfy</code> has type <code>none ≠ none</code> which is definitionally equal to <code>none = none → false</code>. <code>rfl</code> is a proof that <code>none = none</code> so <code>hfy rfl</code> has type <code>false</code></p>

#### [ Victor Porton (Jul 07 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129273495):
<p>How having a function <code>f</code> determine its domain?</p>

#### [ Kenny Lau (Jul 07 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129273497):
<p>it's in the type of the function</p>

#### [ Victor Porton (Jul 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129273512):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> So use <code>match</code>?</p>

#### [ Victor Porton (Jul 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129273518):
<p>I have <code>f: (Σ c:α → Prop, {x:α // c x})</code> and want to get the <code>c</code></p>

#### [ Kenny Lau (Jul 07 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129273519):
<p>I... don't think that's how this works</p>

#### [ Victor Porton (Jul 07 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129273563):
<p>What I try is like:</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">subfunc_to_option2</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="c1">--[decidable_pred c]</span>
<span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="o">(</span><span class="err">Σ</span> <span class="n">c</span><span class="o">:</span><span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">c</span> <span class="n">x</span><span class="o">})</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">f</span><span class="bp">.</span><span class="mi">1</span> <span class="n">y</span> <span class="k">then</span> <span class="n">some</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">subtype</span><span class="bp">.</span><span class="n">mk</span> <span class="n">y</span> <span class="n">h</span><span class="o">))</span> <span class="k">else</span> <span class="n">none</span>
</pre></div>

#### [ Victor Porton (Jul 07 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129273670):
<p>is this possible?</p>

#### [ Victor Porton (Jul 08 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129274227):
<p>This does not compile (types of sides equality in <code>inv1</code> do not match). How to fix the error?</p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="c1">-- Switch from a function on a subset to a function to option monad</span>
<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">subfunc_to_option</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="c1">--[decidable_pred c]</span>
<span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">c</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">c</span> <span class="n">y</span> <span class="k">then</span> <span class="n">some</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">subtype</span><span class="bp">.</span><span class="n">mk</span> <span class="n">y</span> <span class="n">h</span><span class="o">))</span> <span class="k">else</span> <span class="n">none</span>

<span class="c1">-- Switch from function to option monad to a function on a subset</span>
<span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">option</span><span class="bp">.</span><span class="n">is_some</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)}</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">|</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">get</span> <span class="n">h</span>

<span class="kn">theorem</span> <span class="n">inv1</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">option_to_subfunc</span> <span class="o">(</span><span class="bp">@</span><span class="n">subfunc_to_option</span> <span class="n">α</span> <span class="n">β</span> <span class="n">c</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Chris Hughes (Jul 08 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129274270):
<p>I'm not sure what you're trying to do. I don't think the type of <code>f</code> is what you want it to be. You cannot do <code>f.1</code> because <code>f</code> is not a sigma type.</p>

#### [ Victor Porton (Jul 08 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129274320):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I tried to eliminate <code>{c: α → Prop}</code> from my definition. I tried it for completeness, but probably the proper way to do it is using an implicit argument (as in your code) instead</p>

#### [ Victor Porton (Jul 08 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129274321):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Note that the issue in my very last question was different</p>

#### [ Victor Porton (Jul 08 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129274440):
<p>Side question: I subscribed to desktop notifications for this chat, but I get no notifications. Will I receive the notifications, if I close the browser window?</p>

#### [ Chris Hughes (Jul 08 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129274488):
<p>One way to fix the error is to use <code>==</code> instead of <code>=</code> which allows you to state equality when the types are different (your types are different, but they should be equal). This can be unwieldy however. Another way would be to prove that they are equal when applied to an argument, something like this</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">inv1</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">c</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">c</span><span class="o">]</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">c</span> <span class="n">x</span><span class="o">},</span> <span class="n">option_to_subfunc</span> <span class="o">(</span><span class="bp">@</span><span class="n">subfunc_to_option</span> <span class="n">α</span> <span class="n">β</span> <span class="n">c</span> <span class="bp">_</span> <span class="n">f</span><span class="o">)</span> <span class="bp">⟨</span><span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">sorry</span><span class="bp">⟩</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Victor Porton (Jul 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129274550):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> "unwieldy"? What is particularly bad with <code>==</code>? the second way (to write <code>y</code> explicitly) seems even worse for me.</p>

#### [ Victor Porton (Jul 08 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129274878):
<p>Can the following be proved?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">eq_xxx</span> <span class="o">(</span><span class="n">t</span><span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span><span class="o">:</span> <span class="n">t</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">a</span><span class="bp">==</span><span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span><span class="bp">=</span><span class="n">b</span><span class="o">)</span>
</pre></div>


<p>(that is if values of the same type are <code>==</code> then they are <code>=</code>)</p>

#### [ Chris Hughes (Jul 08 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129275360):
<p><code>eq_of_heq</code></p>

#### [ Mario Carneiro (Jul 08 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129275452):
<p><span class="user-mention" data-user-id="119326">@Victor Porton</span> You should receive notifications if you are directly addressed, like this</p>

#### [ Victor Porton (Jul 08 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129275513):
<p>hm, it looks now I am really stalled to fill the <code>sorry</code>ies in my source:</p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="c1">-- Switch from a function on a subset to a function to option monad</span>
<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">subfunc_to_option</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="c1">--[decidable_pred c]</span>
<span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">α</span> <span class="bp">//</span> <span class="n">c</span> <span class="n">x</span><span class="o">}</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">y</span><span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">c</span> <span class="n">y</span> <span class="k">then</span> <span class="n">some</span> <span class="o">(</span><span class="n">f</span> <span class="o">(</span><span class="n">subtype</span><span class="bp">.</span><span class="n">mk</span> <span class="n">y</span> <span class="n">h</span><span class="o">))</span> <span class="k">else</span> <span class="n">none</span>

<span class="c1">-- Switch from function to option monad to a function on a subset</span>
<span class="n">def</span> <span class="n">option_to_subfunc</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">option</span><span class="bp">.</span><span class="n">is_some</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)}</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">|</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">option</span><span class="bp">.</span><span class="n">get</span> <span class="n">h</span>

<span class="kn">theorem</span> <span class="n">inv1</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">option_to_subfunc</span> <span class="o">(</span><span class="bp">@</span><span class="n">subfunc_to_option</span> <span class="n">α</span> <span class="n">β</span> <span class="n">c</span> <span class="n">f</span><span class="o">)</span> <span class="bp">==</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">theorem</span> <span class="n">inv2</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">c</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span><span class="o">):</span> <span class="n">subfunc_to_option</span> <span class="o">(</span><span class="bp">@</span><span class="n">option_to_subfunc</span> <span class="n">β</span> <span class="n">α</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>How to learn to use <code>==</code>? Maybe I should read Coq docs on this?</p>

#### [ Mario Carneiro (Jul 08 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129275523):
<p>To address the larger goal of the definitions you are making, I think you want to use <code>roption</code> (in <code>data.pfun</code>) and the isomorphism theorems between <code>roption</code> and <code>option</code>. A function <code>A -&gt; roption B</code> is the same as a partial function (from a subset of <code>A</code> to <code>B</code>)</p>

#### [ Victor Porton (Jul 08 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129299190):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> First, how <code>roption</code> would be better for my purposes than <code>option</code>? My project uses classical logic. (However someone suggested me to mark which theorems need axiom of choice explicitly.) Now we have three isomorphic objects (and thus three isomorphisms): a partial function, <code>A-&gt;option B</code> and <code>A-&gt;roption B</code>. I do not see how it could be better than my initial idea.</p>

#### [ Mario Carneiro (Jul 08 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129307057):
<p>Because a function <code>A -&gt; roption B</code> <em>is</em> a "subfunc" as you call it. It is literally a pair of a domain and a partial function on that domain</p>

#### [ Mario Carneiro (Jul 08 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129307117):
<p>so you can leverage the proofs of isomorphism there to obtain an isomorphism from <code>A -&gt; option B</code> to a partial function</p>

#### [ Victor Porton (Jul 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129307187):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Either you don't understand me, or I do not understand you. The "subfunc" by definition is a function on a _subtype_ of <code>A</code>. But <code>A -&gt; roption B</code> is a function on the type <code>A</code>, not on its arbitrary subtype as I want. It may be isomorphic, but they are _not_ the same.</p>

#### [ Mario Carneiro (Jul 08 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129307195):
<p>The isomorphism is almost trivial though, unlike the one from option</p>

#### [ Mario Carneiro (Jul 08 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129307237):
<p>And furthermore there is already a definition which gives this isomorphism, <code>as_subtype</code></p>

#### [ Victor Porton (Jul 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129307448):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks. As there is undocumented things like <code>==</code> which I may need for my Lean-related project, I prefer to lay it aside for an indefinite future. Moreover, I am going to lay aside abstract math research and get busy myself writing a free Python program (for an applied computer science, not abstract mathematics) now</p>

#### [ Mario Carneiro (Jul 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20functions/near/129307457):
<p>It's not undocumented, but it's a pain to work with</p>


{% endraw %}
