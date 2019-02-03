---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38732monadicmerge.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [monadic merge](https://leanprover-community.github.io/archive/113488general/38732monadicmerge.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Mar 20 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123983991):
<p>The monad refactoring PR was merged! Congratulations <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> !</p>

#### [ Patrick Massot (Mar 20 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123983995):
<p>You can give us Lean 4 now <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sebastian Ullrich (Mar 20 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984190):
<p>Breaking every existing monad instance with that merge should provide a small taste of Lean 4 <span class="emoji emoji-1f61b" title="stuck out tongue">:stuck_out_tongue:</span></p>

#### [ Simon Hudon (Mar 20 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984312):
<p>I have a sense you may experience what the Haskell implementers experienced. The Haskell users act like addicts when breaking change occurs. Instead of yelling "You bastards! You broke my code" they say "Amazing! Where's the rest?"</p>

#### [ Patrick Massot (Mar 20 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984389):
<p>Are there existing monad instances? Besides the tactic monad of course (you didn't break that one, did you?)</p>

#### [ Moses Schönfinkel (Mar 20 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984393):
<p><code>list</code> had better be a monad</p>

#### [ Patrick Massot (Mar 20 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984394):
<p>And the IO monad that is used by leanpkg</p>

#### [ Patrick Massot (Mar 20 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984396):
<p>I'm sure you also didn't break that one</p>

#### [ Patrick Massot (Mar 20 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984439):
<p>Come on, Leo wouldn't merge a Lean branch with broken <code>list</code></p>

#### [ Moses Schönfinkel (Mar 20 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984443):
<p><code>option</code> had better be a monad</p>

#### [ Simon Hudon (Mar 20 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984444):
<p>There's also <code>state</code> and <code>option</code> I believe</p>

#### [ Moses Schönfinkel (Mar 20 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984445):
<p>let's try #print instances monad</p>

#### [ Moses Schönfinkel (Mar 20 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/123984456):
<div class="codehilite"><pre><span></span><span class="n">native</span><span class="bp">.</span><span class="n">resultT_monad</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">m</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">M</span><span class="o">]</span> <span class="o">(</span><span class="n">E</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">),</span> <span class="n">monad</span> <span class="o">(</span><span class="n">native</span><span class="bp">.</span><span class="n">resultT</span> <span class="n">M</span> <span class="n">E</span><span class="o">)</span>
<span class="n">native</span><span class="bp">.</span><span class="n">result_monad</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">E</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">),</span> <span class="n">monad</span> <span class="o">(</span><span class="n">native</span><span class="bp">.</span><span class="n">result</span> <span class="n">E</span><span class="o">)</span>
<span class="n">list</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">list</span>
<span class="n">smt_tactic</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">smt_tactic</span>
<span class="n">vm_core</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">vm_core</span>
<span class="n">option_t</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">m</span><span class="o">],</span> <span class="n">monad</span> <span class="o">(</span><span class="n">option_t</span> <span class="n">m</span><span class="o">)</span>
<span class="n">conv</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">conv</span>
<span class="n">monad</span><span class="bp">.</span><span class="n">transformed_monad</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">)</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">)</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">m</span><span class="o">],</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">monad</span><span class="bp">.</span><span class="n">monad_transformer</span> <span class="n">t</span><span class="o">]</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">m</span><span class="o">],</span> <span class="n">monad</span> <span class="o">(</span><span class="n">t</span> <span class="n">m</span><span class="o">)</span>
<span class="n">state_t</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">m</span><span class="o">],</span> <span class="n">monad</span> <span class="o">(</span><span class="n">state_t</span> <span class="n">σ</span> <span class="n">m</span><span class="o">)</span>
<span class="n">state</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">),</span> <span class="n">monad</span> <span class="o">(</span><span class="n">state</span> <span class="n">σ</span><span class="o">)</span>
<span class="n">option</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">option</span>
<span class="n">task</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">task</span>
<span class="n">interaction_monad</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">state</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">},</span> <span class="n">monad</span> <span class="o">(</span><span class="n">interaction_monad</span> <span class="n">state</span><span class="o">)</span>
<span class="n">exceptional</span><span class="bp">.</span><span class="n">monad</span> <span class="o">:</span> <span class="n">monad</span> <span class="n">exceptional</span>
<span class="n">monad_fail</span><span class="bp">.</span><span class="n">to_monad</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">monad_fail</span> <span class="n">m</span><span class="o">],</span> <span class="n">monad</span> <span class="n">m</span>
</pre></div>

#### [ Sebastian Ullrich (Mar 21 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124001851):
<p>I meant instances outside of core</p>

#### [ Patrick Massot (Mar 21 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003440):
<p>Are there any in mathlib? My limited understanding is that monads are important in core or for people doing programming in Lean, but not for mathematicians</p>

#### [ Kevin Buzzard (Mar 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003584):
<p>I guess I use the tactic monad...</p>

#### [ Patrick Massot (Mar 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003591):
<p>Sure, but this one is not broken</p>

#### [ Kevin Buzzard (Mar 21 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003593):
<p>...and the occasional list...</p>

#### [ Patrick Massot (Mar 21 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003715):
<p>also not broken</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003768):
<p><code>computation</code>, <code>roption</code>, <code>pfun</code>, <code>seq</code>, <code>wseq</code>, <code>filter</code></p>

#### [ Patrick Massot (Mar 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003771):
<p>Are these names of monads in mathlib?</p>

#### [ Patrick Massot (Mar 21 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003773):
<p>Is mathlib currently broken?</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003776):
<p>probably, haven't had time to check</p>

#### [ Mario Carneiro (Mar 21 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124003787):
<p>seems very unlikely that sebastian's huge merge didn't break mathlib</p>

#### [ Mario Carneiro (Mar 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124034102):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> What happened to the proofs of <code>is_lawful_functor option</code>?</p>

#### [ Mario Carneiro (Mar 21 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124034711):
<p>Oh, found it - <code>init.data.option.instances</code>. This is the first time I've seen a file in <code>init</code> import namespace which is not imported by default. Was that deliberate?</p>

#### [ Sebastian Ullrich (Mar 22 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124035075):
<p>No, definitely not. Thanks for noticing.</p>

#### [ Sebastian Ullrich (Mar 22 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124035078):
<p>We should have some noticing tool for that :)</p>

#### [ Kevin Buzzard (Mar 22 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124035133):
<p>Looks like you do :-)</p>

#### [ Sebastian Ullrich (Mar 22 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124035943):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> fixed</p>

#### [ Mario Carneiro (Mar 22 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monadic%20merge/near/124039009):
<p><code>mathlib</code> should now be fixed, although I built against sebastian's commit which won't appear until tomorrow's nightly build</p>


{% endraw %}
