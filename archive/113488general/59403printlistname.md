---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59403printlistname.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [print list name](https://leanprover-community.github.io/archive/113488general/59403printlistname.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Aug 09 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155695):
<p>My first attempt at writing a tactic. I want a tactic that will <code>fail</code> by printing a list of tactics. I've copy-pasted code by Scott:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">get_applicable_lemmas</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">name</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">cs</span> <span class="err">←</span> <span class="n">attribute</span><span class="bp">.</span><span class="n">get_instances</span> <span class="bp">`</span><span class="n">applicable</span><span class="o">,</span>
   <span class="n">fail</span> <span class="c1">-- &lt;what do I put here?&gt;</span>
</pre></div>


<p>(Whoops, there was still code that tried to apply the tactics, only failing if none applied. That's now gone.)</p>

#### [ Johan Commelin (Aug 09 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155709):
<p>Oh, and maybe there is a far easier way to look up all the current applicable lemmas then by writing a failing tactic. If so, I'dd also like to learn that method (-;</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155768):
<p>I don't quite get what you are tying to do</p>

#### [ Johan Commelin (Aug 09 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155771):
<p>I want Lean to print me a list of all lemmas that are tagged with <code>applicable</code>.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155775):
<p>Hmmm, can I do this with <code>#print attribute applicable</code> or something similar?</p>

#### [ Johan Commelin (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155837):
<p>Where do I what sorts of things I can <code>#print</code> anyways? So far I've learned two or three incantations by osmosis in this chat. Is this documented anywhere?</p>

#### [ Johan Commelin (Aug 09 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131155843):
<p><code>#print attribute</code> is not a valid print command )-;</p>

#### [ Johan Commelin (Aug 09 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131156105):
<p>So, I need to fold <code>\lam n, n.to_string</code> over this list, right? And I can just use the regular fold. I don't need some <code>meta</code>-fold.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131156112):
<p>Because monads are just cool mathematical goodies.</p>

#### [ Johan Commelin (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131156361):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">get_applicable_lemmas</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">cs</span> <span class="err">←</span> <span class="n">attribute</span><span class="bp">.</span><span class="n">get_instances</span> <span class="bp">`</span><span class="n">applicable</span><span class="o">,</span>
   <span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">foldl</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">s</span> <span class="n">n</span><span class="o">,</span> <span class="n">name</span><span class="bp">.</span><span class="n">to_string</span> <span class="n">n</span> <span class="bp">++</span> <span class="s2">&quot;, &quot;</span> <span class="bp">++</span> <span class="n">s</span><span class="o">)</span> <span class="s2">&quot;&quot;</span> <span class="n">cs</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Aug 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131156365):
<p>That seems to do what I want (-;</p>

#### [ Kevin Buzzard (Aug 09 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131157813):
<blockquote>
<p>So, I need to fold <code>\lam n, n.to_string</code> over this list, right? And I can just use the regular fold. I don't need some <code>meta</code>-fold.</p>
</blockquote>
<p>Whilst I'm kind-of out of my depth, I think that the fact that you can use regular fold is one thing that Lean has over Coq. I <em>think</em> that in Coq you have to learn one language to write proofs and then another language to write tactics.</p>

#### [ Mario Carneiro (Aug 09 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158150):
<p>here's another way:</p>
<div class="codehilite"><pre><span></span>meta def get_applicable_lemmas : tactic unit :=
do cs ← attribute.get_instances `applicable,
   cs.mmap&#39; tactic.trace
</pre></div>

#### [ Mario Carneiro (Aug 09 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158225):
<p>or <code>attribute.get_instances `applicable &gt;&gt;= list.mmap' tactic.trace</code> if you want to be clever</p>

#### [ Johan Commelin (Aug 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158259):
<p>Right! That's nice (-;</p>

#### [ Johan Commelin (Aug 09 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158315):
<p>Of course I should have thought of looking for some <code>map</code>-like.</p>

#### [ Mario Carneiro (Aug 09 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158319):
<p>here I am using a kind of "meta map" <code>mmap</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158331):
<p>although this is because I want to map from inside a monad</p>

#### [ Mario Carneiro (Aug 09 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158372):
<p><code>mmap'</code> is more of a "for each" or "scan" type function than a map - it doesn't return any output</p>

#### [ Johan Commelin (Aug 09 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131158948):
<p>What is the difference between <code>tactic unit</code> vs <code>tactic name</code> vs <code>tactic string</code>?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131159099):
<p>that's like asking what the difference is between <code>option unit</code> and <code>option nat</code> and <code>option real</code></p>

#### [ Kevin Buzzard (Aug 09 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131159156):
<p>If you're passing information around between tactics then you might want to use <code>tactic blah</code> (which means "blah plus the extra option of failure"), but at the end of it all when you want to run the tactic you may as well return something of type "tactic unit" because no other tactic wants the output.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131159165):
<p>The changing of the state is not an output of the tactic, that all goes on within the monad</p>

#### [ Johan Commelin (Aug 09 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/print%20list%20name/near/131159173):
<p>Right. That makes sense.</p>


{% endraw %}
