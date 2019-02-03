---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92086computevalueoffunction.html
---

## Stream: [general](index.html)
### Topic: [compute value of function](92086computevalueoffunction.html)

---


{% raw %}
#### [ jmc (Mar 19 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932056):
<p>Hi. Lean-newbie here. I've got a function f : \N \to \Z with a pretty involved definition. I would like to see what Lean thinks that the value of f is on 0,1,2,3 for example.<br>
My current approach has been:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">f</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">refl</span>
</pre></div>


<p>and then just trying different values of n, until I am lucky. But there should be a better way...</p>
<p>(Ok, I just saw there is a "new members" stream. If someone can move this topic overthere, please feel free to do so.)</p>

#### [ Simon Hudon (Mar 19 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932203):
<p>Try:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="n">f</span> <span class="mi">0</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="n">f</span> <span class="mi">1</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="n">f</span> <span class="mi">2</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="n">f</span> <span class="mi">3</span>
</pre></div>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932204):
<p>You can just <code>#eval f x</code></p>

#### [ jmc (Mar 19 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932212):
<p>Aah, thanks!</p>

#### [ Simon Hudon (Mar 19 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932223):
<p>It uses the virtual machine so if <code>f</code> is computation intensive, this will ensure swift execution</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932268):
<p>If you want slow execution, you can try <code>#reduce f x</code> ;).</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932273):
<p>(Also your <code>refl</code> trick made me giggle so you're awarded a pointless internet point.)</p>

#### [ Simon Hudon (Mar 19 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932327):
<p>(I think we can use octopuses to award those internet points)</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932332):
<p>What an excellent idea.</p>

#### [ jmc (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932348):
<p>Thanks for the point!</p>

#### [ Simon Hudon (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932349):
<p>thanks)</p>

#### [ Andrew Ashworth (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932352):
<p>the <code>rfl</code> thing is considered good style if you go by "Software Foundations"</p>

#### [ Andrew Ashworth (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932357):
<p>it's basically inline unit testing</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932360):
<p>I have no recollection of that in SF o_O?</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932361):
<p>Aaah right.</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932362):
<p>You mean his auto-tests.</p>

#### [ Andrew Ashworth (Mar 19 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932423):
<p>yeah, for ex</p>

#### [ Andrew Ashworth (Mar 19 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932425):
<div class="codehilite"><pre><span></span><span class="kn">Definition</span> <span class="n">hd</span> <span class="o">(</span><span class="n">default</span><span class="o">:</span><span class="kt">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span><span class="o">:</span><span class="n">natlist</span><span class="o">)</span> <span class="o">:</span> <span class="kt">nat</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">l</span> <span class="k">with</span>
  <span class="o">|</span> <span class="n">nil</span> <span class="err">⇒</span> <span class="n">default</span>
  <span class="o">|</span> <span class="n">h</span> <span class="o">::</span> <span class="n">t</span> <span class="err">⇒</span> <span class="n">h</span>
  <span class="k">end</span><span class="o">.</span>
<span class="kn">Definition</span> <span class="n">tl</span> <span class="o">(</span><span class="n">l</span><span class="o">:</span><span class="n">natlist</span><span class="o">)</span> <span class="o">:</span> <span class="n">natlist</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">l</span> <span class="k">with</span>
  <span class="o">|</span> <span class="n">nil</span> <span class="err">⇒</span> <span class="n">nil</span>
  <span class="o">|</span> <span class="n">h</span> <span class="o">::</span> <span class="n">t</span> <span class="err">⇒</span> <span class="n">t</span>
  <span class="k">end</span><span class="o">.</span>
<span class="kn">Example</span> <span class="n">test_hd1</span><span class="o">:</span> <span class="n">hd</span> <span class="mi">0</span> <span class="o">[</span><span class="mi">1</span><span class="o">;</span><span class="mi">2</span><span class="o">;</span><span class="mi">3</span><span class="o">]</span> <span class="o">=</span> <span class="mi">1</span><span class="o">.</span>
<span class="kn">Proof</span><span class="o">.</span> <span class="kp">reflexivity</span><span class="o">.</span> <span class="kn">Qed</span><span class="o">.</span>
<span class="kn">Example</span> <span class="n">test_hd2</span><span class="o">:</span> <span class="n">hd</span> <span class="mi">0</span> <span class="bp">[]</span> <span class="o">=</span> <span class="mi">0</span><span class="o">.</span>
<span class="kn">Proof</span><span class="o">.</span> <span class="kp">reflexivity</span><span class="o">.</span> <span class="kn">Qed</span><span class="o">.</span>
<span class="kn">Example</span> <span class="n">test_tl</span><span class="o">:</span> <span class="n">tl</span> <span class="o">[</span><span class="mi">1</span><span class="o">;</span><span class="mi">2</span><span class="o">;</span><span class="mi">3</span><span class="o">]</span> <span class="o">=</span> <span class="o">[</span><span class="mi">2</span><span class="o">;</span><span class="mi">3</span><span class="o">].</span>
<span class="kn">Proof</span><span class="o">.</span> <span class="kp">reflexivity</span><span class="o">.</span> <span class="kn">Qed</span><span class="o">.</span>
</pre></div>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932428):
<p>Yeah absolutely.</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932431):
<p>Oh boy that book is such an excellent introduction to these things.</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932446):
<p>Compare that to CPDT... :-\.</p>

#### [ Moses Schönfinkel (Mar 19 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932448):
<p>(Sorry Adam...)</p>

#### [ Andrew Ashworth (Mar 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932498):
<p>yeah, if you do 2 semesters of software foundations</p>

#### [ Andrew Ashworth (Mar 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932500):
<p>first</p>

#### [ Andrew Ashworth (Mar 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932503):
<p>maybe you can understand cpdt, except you still won't</p>

#### [ jmc (Mar 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/compute%20value%20of%20function/near/123932504):
<p>Anyway, the function in question is the Ramanujan tau function (<a href="https://en.wikipedia.org/wiki/Ramanujan%27s_tau_function" target="_blank" title="https://en.wikipedia.org/wiki/Ramanujan%27s_tau_function">https://en.wikipedia.org/wiki/Ramanujan%27s_tau_function</a>)<br>
Already <code>#reduce \tau 2</code> is extremely slow for my implementation.<br>
But <code>#eval \tau 4</code> is pretty fast. And the first 5 values are correct (^;</p>


{% endraw %}
