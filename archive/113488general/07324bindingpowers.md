---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07324bindingpowers.html
---

## Stream: [general](index.html)
### Topic: [binding powers](07324bindingpowers.html)

---


{% raw %}
#### [ Kenny Lau (Jan 26 2019 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156905008):
<p>What's the right way to declare a <code>notation</code> for <code>a ^[b] c</code>? what should the binding powers of <code>^[</code> and <code>]</code> be?</p>

#### [ Simon Hudon (Jan 26 2019 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156905496):
<p><code>]</code> should have a maximal binding power ( <code>:max</code> ) and you should chose a binding power for <code>^[</code> comparable to the operators it will be used with. If it's to be used as <code>^</code>, look at its binding power with <code>#print notation ^</code></p>

#### [ Kenny Lau (Jan 26 2019 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156905841):
<p>thanks</p>

#### [ Kenny Lau (Jan 26 2019 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156905857):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> it still behaves differently from <code>a ^ c</code></p>

#### [ Simon Hudon (Jan 26 2019 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156905901):
<p>How so?</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156905902):
<p>shouldn't <code>]</code> get minimum binding power?</p>

#### [ Kenny Lau (Jan 26 2019 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156905932):
<p><code>M ⊗ N → M ⊗ N</code> parses as <code>(M ⊗ N) → (M ⊗ N)</code> as intended, but I can't get <code>M ⊗[R] N → M ⊗[R] N</code> to be parsed the same</p>

#### [ Kenny Lau (Jan 26 2019 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156905964):
<p>neither <code>0</code> nor <code>max</code> work</p>

#### [ Simon Hudon (Jan 26 2019 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906024):
<p>If you put brackets around one of the two sides of the expression, that should fix the problem and tell me where the problem is. Can you try bracketing only one side at a time and tell me where the problem is?</p>

#### [ Kenny Lau (Jan 26 2019 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906037):
<p><code>(M ⊗[R] N) → M ⊗[R] N</code> parses as intended</p>

#### [ Simon Hudon (Jan 26 2019 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906081):
<p>Did you make the binding power of <code>]</code> 0 or max?</p>

#### [ Kenny Lau (Jan 26 2019 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906082):
<p>both</p>

#### [ Kenny Lau (Jan 26 2019 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906083):
<p>the situation is same for both</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906087):
<p>did you try making the bp the same as the open bracket?</p>

#### [ Kenny Lau (Jan 26 2019 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906088):
<p><code>M ⊗[R] N → M ⊗[R] N</code> is parsed as <code>M ⊗[R] (N → (M ⊗[R] N))</code></p>

#### [ Kenny Lau (Jan 26 2019 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906100):
<blockquote>
<p>did you try making the bp the same as the open bracket?</p>
</blockquote>
<p>it hangs</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906101):
<p>also is the bp greater than 25 or less?</p>

#### [ Kenny Lau (Jan 26 2019 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906127):
<p>M ⊗[R] N → M ⊗[R] N is parsed as M ⊗[R] (N → (M ⊗[R] N)) for (<code>⊗[</code>=100 and <code>]</code>=0) and (<code>⊗[</code>=100 and <code>]</code>=max)</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906390):
<p>this works:</p>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">tensor</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span>

<span class="kn">notation</span> <span class="n">M</span> <span class="bp">`</span> <span class="err">⊗</span><span class="o">[</span><span class="bp">`</span><span class="o">:</span><span class="mi">30</span> <span class="n">R</span> <span class="bp">`</span><span class="o">]</span> <span class="bp">`</span> <span class="n">N</span><span class="o">:</span><span class="mi">30</span> <span class="o">:=</span> <span class="n">tensor</span> <span class="n">R</span> <span class="n">M</span> <span class="n">N</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">M</span> <span class="n">R</span> <span class="n">N</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">M</span> <span class="err">⊗</span><span class="o">[</span><span class="n">R</span><span class="o">]</span> <span class="n">M</span> <span class="err">⊗</span><span class="o">[</span><span class="n">R</span><span class="o">]</span> <span class="n">N</span> <span class="bp">-&gt;</span> <span class="n">M</span> <span class="err">⊗</span><span class="o">[</span><span class="n">R</span><span class="o">]</span> <span class="n">N</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(((</span><span class="n">M</span> <span class="err">⊗</span><span class="o">[</span><span class="n">R</span><span class="o">]</span> <span class="n">M</span><span class="o">)</span> <span class="err">⊗</span><span class="o">[</span><span class="n">R</span><span class="o">]</span> <span class="n">N</span><span class="o">)</span> <span class="bp">-&gt;</span> <span class="o">(</span><span class="n">M</span> <span class="err">⊗</span><span class="o">[</span><span class="n">R</span><span class="o">]</span> <span class="n">N</span><span class="o">))</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Jan 26 2019 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906392):
<p>interesting</p>

#### [ Kenny Lau (Jan 26 2019 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906395):
<p>I don't understand binding powers</p>

#### [ Kenny Lau (Jan 26 2019 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906401):
<p>how can <code>N</code> have a binding power</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906406):
<p>me neither, I just put a bunch of stuff in there until it worked</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906408):
<p>actually it makes more sense to give a variable a binding power than a constant</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906414):
<p>when a variable has a bp it means that the expression there is parsed with that bp</p>

#### [ Mario Carneiro (Jan 26 2019 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156906460):
<p>if it sees a constant with a lower bp than the one currently used in the parse, it acts as though a <code>)</code> is inserted</p>

#### [ Patrick Massot (Jan 26 2019 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943529):
<p>I have a new binding power challenge!</p>
<div class="codehilite"><pre><span></span><span class="kn">notation</span> <span class="bp">`|`</span><span class="n">x</span><span class="bp">`|`</span> <span class="o">:=</span> <span class="n">abs</span> <span class="n">x</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">|</span><span class="n">x</span><span class="bp">|</span>  <span class="c1">-- works</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="bp">|</span><span class="n">x</span><span class="bp">|</span><span class="o">)</span> <span class="c1">-- fails!</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span> <span class="bp">|</span><span class="n">x</span><span class="bp">|</span> <span class="o">)</span> <span class="c1">-- works!</span>
</pre></div>

#### [ Patrick Massot (Jan 26 2019 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943536):
<p>The challenge is to fix the first line so that all lines work</p>

#### [ Patrick Massot (Jan 26 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943539):
<p>It took me for ever to understand what was happening when I hit this in the wild</p>

#### [ Simon Hudon (Jan 26 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943598):
<p>have you tried <code>#print notation (| |)</code>?</p>

#### [ Patrick Massot (Jan 26 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943607):
<p><code>no notation</code></p>

#### [ Patrick Massot (Jan 26 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943622):
<p>but I didn't try before, thanks!</p>

#### [ Patrick Massot (Jan 26 2019 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943732):
<p>Any other suggestion?</p>

#### [ Simon Hudon (Jan 26 2019 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943843):
<p>What about just <code>#print notation (|</code>?</p>

#### [ Sebastian Ullrich (Jan 26 2019 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943864):
<p><code>(| |)</code> is ASCII syntax for the anonymous constructor</p>

#### [ Patrick Massot (Jan 26 2019 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943867):
<p>nooo!</p>

#### [ Patrick Massot (Jan 26 2019 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943869):
<p>Can I override that?</p>

#### [ Patrick Massot (Jan 26 2019 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943872):
<p>Can you remove ascii from Lean 4?</p>

#### [ Sebastian Ullrich (Jan 26 2019 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943873):
<p>Not in Lean 3</p>

#### [ Sebastian Ullrich (Jan 26 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943879):
<p>You can do that yourself in Lean 4 :P</p>

#### [ Patrick Massot (Jan 26 2019 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943937):
<blockquote>
<p>What about just <code>#print notation (|</code>?</p>
</blockquote>
<p>no notation</p>

#### [ Patrick Massot (Jan 26 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156943987):
<p>Preventing <code>(|</code> from being used is really really sad</p>

#### [ Simon Hudon (Jan 26 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156944014):
<p>In general, I think scoping notations will be very useful in Lean 4</p>

#### [ Patrick Massot (Jan 26 2019 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156944405):
<p>Kevin, what did you do with absolute values in your classes? Did you use a fancy |? Or were you lucky with parentheses?</p>

#### [ Kevin Buzzard (Jan 26 2019 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156944545):
<p>No, I discovered exactly the same thing as you, tried to fix it, couldn't, so just started putting spaces after brackets.</p>

#### [ Kevin Buzzard (Jan 26 2019 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/binding%20powers/near/156944557):
<p>I didn't know why it was failing though, so this thread has been helpful!</p>


{% endraw %}
