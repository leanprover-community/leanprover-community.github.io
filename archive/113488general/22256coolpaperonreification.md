---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22256coolpaperonreification.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [cool paper on reification](https://leanprover-community.github.io/archive/113488general/22256coolpaperonreification.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Andrew Ashworth (Jun 03 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486086):
<p>just in case anybody else is interested in proofs by reflection: <a href="https://people.csail.mit.edu/jgross/personal-website/papers/2018-reification-by-parametricity-itp-draft.pdf" target="_blank" title="https://people.csail.mit.edu/jgross/personal-website/papers/2018-reification-by-parametricity-itp-draft.pdf">https://people.csail.mit.edu/jgross/personal-website/papers/2018-reification-by-parametricity-itp-draft.pdf</a></p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486131):
<p>it's my favorite topic right now since i'm trying to teach myself how to write reflective tactics in lean</p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486177):
<p>i wish i was in oxford so i could attend the workshops at ITP :|</p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486552):
<p>does lean have a <code>vm_compute</code> equivalent?</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486600):
<p>No. <span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> This paper relates to our discussion about proof by <code>#eval</code></p>

#### [ Simon Hudon (Jun 03 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486602):
<p>I had a conversation with <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> a while back on proofs by reflection. He was pointing out to me that they are not as beneficial in Lean as they are in Coq because of some details of computation in the kernel</p>

#### [ Simon Hudon (Jun 03 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486604):
<p>I don't remember which detail that was</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486617):
<p>It's possible to do proof by reflection using the <em>kernel</em> for computation, but it's not very fast</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486658):
<p>doing proof by reflection using the VM is not supported (directly)</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486661):
<p>but you can use tactics, computing in the VM, to craft appropriate theorems as certificates for the kernel</p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486668):
<p>is there an example of that in lean? I think the idea of verified decision procedures is very appealing theoretically</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486669):
<p><code>norm_num</code> and <code>ring</code> use this latter strategy</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486708):
<p><code>cooper</code> uses kernel reflection, and <code>vm_cooper</code> uses "tactic reflection"</p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486709):
<p>and in lean 4, i think we will be able to extract tactics and use them?</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486711):
<p>sure, that's one thing compilation should allow</p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486712):
<p>not tactics, i mean regular function defs</p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486718):
<p>so we could extract the <code>check_is_even</code> program as described in the paper and have it run in C++</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486719):
<p>You can <code>#eval check_is_even</code> currently</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486756):
<p>to run in the VM</p>

#### [ Mario Carneiro (Jun 03 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127486764):
<p>or you can <code>#reduce check_is_even</code> to run in the kernel</p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487123):
<p>but, in a sense, we can't reason about vm evaluation, it's outside lean, is my current understanding</p>

#### [ Andrew Ashworth (Jun 03 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487175):
<p>if there was a <code>#eval that produced exprs</code> we could though</p>

#### [ Mario Carneiro (Jun 03 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487290):
<p>no but we can trust the results</p>

#### [ Mario Carneiro (Jun 03 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487328):
<p>like if we evaluate a <code>bool</code> expr and get <code>tt</code> we believe the same should hold true of reduce</p>

#### [ Mario Carneiro (Jun 03 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487339):
<p>The reasoning would go into the definition of the function being evaluated itself</p>

#### [ Andrew Ashworth (Jun 03 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487721):
<p>reasoning would go into the definition? do you have a concrete example? I don't quite follow. As I understand it the kernel is quite strict. If we use nat, it will reduce everything strictly using the zero / succ nat representation. However, vm evaluation might use a bignum library for speed. How can we say their behavior is equivalent?<br>
(maybe I should just be reading more about reflection / I don't understand how Lean uses GMP)</p>

#### [ Mario Carneiro (Jun 03 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127487986):
<p>The assumption, the trust, goes into assuming that the VM respects the lean model. You verify the lean model</p>

#### [ Andrew Ashworth (Jun 03 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127488045):
<p>ah, gotcha</p>

#### [ Mario Carneiro (Jun 03 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127488054):
<p>But that's not much different from assuming the kernel is correctly implemented in C++. You expand your trust level a bit and get fast evaluation</p>

#### [ Andrew Ashworth (Jun 03 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127488200):
<p>it's interesting to me that reflection is slow because generating the reified syntax and reducing the output of the interpretation function are such huge constant overheads. I would've guessed that the manipulations you might do on the AST you create would've been a bigger deal in practice for most problems</p>

#### [ Andrew Ashworth (Jun 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cool%20paper%20on%20reification/near/127495213):
<p>well, you weren't kidding about kernel computation</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">is_even</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">is_even</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">ssuc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">is_even</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">is_even</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">))</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">prove_even</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">[</span><span class="n">repeat</span> <span class="o">{</span><span class="n">constructor</span><span class="o">}]</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">is_even</span> <span class="mi">2000</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">do</span> <span class="n">timetac</span> <span class="s2">&quot;&quot;</span> <span class="n">prove_even</span>

<span class="n">def</span> <span class="n">check_is_even</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n&#39;</span><span class="o">))</span> <span class="o">:=</span> <span class="n">check_is_even</span> <span class="n">n&#39;</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">nat</span><span class="bp">.</span><span class="n">case_strong_induction_on</span>
<span class="kn">theorem</span> <span class="n">cie_sound</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">check_is_even</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">tt</span> <span class="bp">→</span> <span class="n">is_even</span> <span class="n">n</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">case_strong_induction_on</span> <span class="n">n</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">is_even</span><span class="bp">.</span><span class="n">zero</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">n&#39;</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n&#39;</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">,</span> <span class="k">have</span> <span class="n">h₃</span> <span class="o">:</span> <span class="n">check_is_even</span> <span class="mi">1</span> <span class="bp">=</span> <span class="n">ff</span><span class="o">,</span> <span class="k">from</span> <span class="n">rfl</span><span class="o">,</span> <span class="k">by</span> <span class="n">contradiction</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="n">h₃</span><span class="o">,</span> <span class="n">is_even</span><span class="bp">.</span><span class="n">ssuc</span> <span class="bp">_</span> <span class="o">((</span><span class="n">h₂</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_succ</span> <span class="n">m</span><span class="o">)</span> <span class="n">h₃</span><span class="o">)))</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">is_even</span> <span class="mi">2000</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">do</span> <span class="n">timetac</span> <span class="s2">&quot;&quot;</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="n">cie_sound</span> <span class="mi">2000</span> <span class="n">rfl</span><span class="o">]</span>
</pre></div>


{% endraw %}
