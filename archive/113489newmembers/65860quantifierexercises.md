---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65860quantifierexercises.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [quantifier exercises](https://leanprover-community.github.io/archive/113489newmembers/65860quantifierexercises.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Olli (Sep 08 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561165):
<p>could I get a hint how to make progress here:</p>
<p><a href="https://gist.github.com/luxbock/853bdcdde0f333502055c6913fc91e9c" target="_blank" title="https://gist.github.com/luxbock/853bdcdde0f333502055c6913fc91e9c">https://gist.github.com/luxbock/853bdcdde0f333502055c6913fc91e9c</a></p>

#### [ Reid Barton (Sep 08 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561182):
<p>You can't make progress without some classical axiom.</p>

#### [ Kenny Lau (Sep 08 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561221):
<p>please provide a minimum <em>working</em> example (MWE).</p>

#### [ Reid Barton (Sep 08 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561226):
<p>Most directly, <code>classical.by_contradiction</code></p>

#### [ Reid Barton (Sep 08 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561272):
<p>Or, wait. Also what Kenny said. Where did <code>a</code> come from?</p>

#### [ Olli (Sep 08 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561286):
<p>sorry, I'll edit to include the full context and also my attempt with <code>by_contradiction</code> where I got stuck</p>

#### [ Kenny Lau (Sep 08 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561341):
<p>please provide a <em>minimum</em> working example (MWE).</p>

#### [ Olli (Sep 08 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561389):
<p><a href="https://gist.github.com/luxbock/853bdcdde0f333502055c6913fc91e9c" target="_blank" title="https://gist.github.com/luxbock/853bdcdde0f333502055c6913fc91e9c">https://gist.github.com/luxbock/853bdcdde0f333502055c6913fc91e9c</a> updated</p>

#### [ Kenny Lau (Sep 08 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561447):
<p>I don't think that's what you want to prove.</p>

#### [ Reid Barton (Sep 08 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561512):
<p>This <code>variable a : α</code> isn't doing what you want--now you have to prove <code>p a</code> for <em>every</em> <code>a</code></p>

#### [ Olli (Sep 08 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561518):
<p>this is one of the exercises from here:<br>
<a href="https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html">https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html</a></p>

#### [ Olli (Sep 08 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561524):
<p>so my attempt is clearly wrong (it does not work after all), but I don't know how to make progress beyond <code>by_contradiction (λ ha, _)</code></p>

#### [ Olli (Sep 08 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561578):
<p>I don't know how to go about getting a <code>p a</code> from what I have:</p>
<div class="codehilite"><pre><span></span>nanpx : (∀ (x : α), p x → false) → false,
hnpa : ¬p a
⊢ false
</pre></div>

#### [ Kenny Lau (Sep 08 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561580):
<blockquote>
<p>Notice that the declaration <code>variable a : α</code> amounts to the assumption that there is at least one element of type <code>α</code>. This assumption is needed in the <strong>second</strong> example, as well as in the <strong>last two</strong>.</p>
</blockquote>

#### [ Kenny Lau (Sep 08 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561587):
<p>your example is neither the second nor the last two</p>

#### [ Reid Barton (Sep 08 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561594):
<p>You can never get <code>p a</code>, because <code>a</code> is an arbitrary member of <code>α</code>, and it might not be one for which <code>p</code> holds.</p>

#### [ Reid Barton (Sep 08 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561638):
<p>So line 11 <code>suffices hpa : p a, from ...</code> is already the wrong way to go.</p>

#### [ Reid Barton (Sep 08 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561691):
<p>The way to do this is to use <code>by_contradiction</code> at the top level--suppose <code>¬ (∃ x, p x)</code>, then what?</p>

#### [ Olli (Sep 08 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561703):
<p>thanks, I'll try to see where backtracking to beginning gets me. although now that <span class="user-mention" data-user-id="110064">@Kenny Lau</span>  commented about the <code>variable</code> declaration, I'm a little bit confused about if I need to change anything outside this example</p>

#### [ Olli (Sep 08 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561756):
<p>oh I think I understand what you mean, I don't need the <code>variable</code> declaration for this particular example</p>

#### [ Olli (Sep 08 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561761):
<p>I just copy/pasted the exercises from the page and I'm filling in the <code>sorry</code>'s</p>

#### [ Olli (Sep 08 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561824):
<p>actually that can't be the case, so yeah I am confused about what you meant <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Kenny Lau (Sep 08 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561866):
<p>You don't need <code>variable a : α</code></p>

#### [ Olli (Sep 08 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561876):
<p>I think I need it, because <code>p</code> uses it</p>

#### [ Olli (Sep 08 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133561917):
<p>oh sorry, I now realize what you meant</p>

#### [ Olli (Sep 08 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133562068):
<p>got it, thanks for the help</p>

#### [ Wojciech Nawrocki (Sep 09 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587708):
<p>I'm doing the same exercise atm!<br>
I found some disparities in mathlib's intuitionist and classical namespaces, namely in intuitionist we have this:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">not_forall</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
    <span class="o">[</span><span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="bp">¬</span> <span class="n">p</span> <span class="n">x</span><span class="o">)]</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">p</span> <span class="n">x</span><span class="o">)]</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">¬</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="bp">¬</span> <span class="n">p</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">not</span><span class="bp">.</span><span class="n">imp_symm</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">nx</span> <span class="n">x</span><span class="o">,</span> <span class="n">nx</span><span class="bp">.</span><span class="n">imp_symm</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="n">not_forall_of_exists_not</span><span class="bp">⟩</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">not_forall_not</span> <span class="o">[</span><span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)]</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">¬</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="bp">¬</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">decidable_of_iff</span> <span class="o">(</span><span class="bp">¬</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="n">not_exists</span><span class="bp">;</span>
<span class="n">exact</span> <span class="n">not_iff_comm</span><span class="bp">.</span><span class="mi">1</span> <span class="n">not_exists</span>
</pre></div>


<p>but in classical only this:</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="kn">theorem</span> <span class="n">not_forall</span> <span class="o">:</span> <span class="o">(</span><span class="bp">¬</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="bp">¬</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">not_forall</span>
</pre></div>


<p>So from <code>classical.not_forall.mp h</code> with <code>h: ¬ ∀ x, ¬ p x</code> we get a double negation. Now, I know that <code>¬¬p ↔ p</code> is easy to prove from classical axioms, but despite how common its usage seems to be, there is no theorem for it built into the library. Is there some reason why double-negation is redundant, or should I make a PR to add it?</p>

#### [ Kevin Buzzard (Sep 09 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587798):
<p>lean and mathlib are pretty huge, it would surprise me if <code>¬¬p ↔ p</code> were not there already.</p>

#### [ Mario Carneiro (Sep 09 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587800):
<p>The idea is that you should use the "intuitionist" theorem and use <code>classical.dec</code> to fulfill the decidability assumptions</p>

#### [ Mario Carneiro (Sep 09 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587811):
<p>(aka <code>classical.prop_decidable</code>)</p>

#### [ Wojciech Nawrocki (Sep 09 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587813):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <code>#find</code> tells me that there are versions for <code>decidable p</code>, but not for generic propositions in classical reasoning</p>

#### [ Wojciech Nawrocki (Sep 09 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587853):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> oh i see, so i should use all the <code>decidable</code> stuff with classical reasoning and then that one axiom to make it work? Ok</p>

#### [ Mario Carneiro (Sep 09 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587871):
<p>This is why you often see <code>local attribute [instance] classical.prop_decidable</code> at the top of files that do classical reasoning</p>

#### [ Kevin Buzzard (Sep 09 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587881):
<p>I've taken to using <code>local attribute [instance, priority 1] classical.prop_decidable</code></p>

#### [ Kevin Buzzard (Sep 09 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587918):
<p>because I ran into situations where this local attribute clobbered some decidability result which type class inference had given me and I ended up with typeclass problems.</p>

#### [ Mario Carneiro (Sep 09 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133587936):
<p>is <code>priority 0</code> problematic?</p>

#### [ Wojciech Nawrocki (Sep 09 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133588002):
<p>I see, this attribute is indeed used in <a href="https://github.com/leanprover/lean/blob/master/library/init/classical.lean#L90" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/classical.lean#L90"><code>classical.lean</code></a></p>

#### [ Kevin Buzzard (Sep 09 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133588287):
<blockquote>
<p>is <code>priority 0</code> problematic?</p>
</blockquote>
<p>my bad, I just went back to the file where some undergrads were having trouble and indeed I fixed it with <code>priority 0</code></p>

#### [ Olli (Sep 11 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133703971):
<p>is it possible to solve the barber paradox exercise without using <code>classical</code>?https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html</p>

#### [ Mario Carneiro (Sep 11 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704194):
<p>yes</p>

#### [ Olli (Sep 11 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704251):
<p>can I have a hint? this is what I have so far:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">S</span> <span class="n">x</span> <span class="n">x</span> <span class="bp">↔</span> <span class="bp">¬</span> <span class="n">S</span> <span class="n">x</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">saa</span> <span class="o">:</span> <span class="n">S</span> <span class="n">a</span> <span class="n">a</span> <span class="bp">→</span> <span class="bp">¬</span><span class="n">S</span> <span class="n">a</span> <span class="n">a</span><span class="o">,</span> <span class="k">from</span> <span class="o">(</span><span class="n">h</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">mp</span><span class="o">,</span>
<span class="k">have</span> <span class="n">nsaa</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">S</span> <span class="n">a</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">S</span> <span class="n">a</span> <span class="n">a</span><span class="o">,</span> <span class="k">from</span> <span class="o">(</span><span class="n">h</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">mpr</span><span class="o">,</span>
<span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Sep 11 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704259):
<p>hint: solve exercise 3.7.2</p>

#### [ Mario Carneiro (Sep 11 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704266):
<p>also your problem statement isn't quite right for the barber paradox</p>

#### [ Olli (Sep 11 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704322):
<p>thanks, looks like I actually overlooked 3.7.2, so I'll go back to that and try to figure it out from there (and also fix what you mentioned)</p>

#### [ Mario Carneiro (Sep 11 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/quantifier%20exercises/near/133704328):
<div class="codehilite"><pre><span></span>example {α} (b : α) (r : α → α → Prop)
  (H : ∀ x : α, r b x ↔ ¬ r x x) : false := sorry
</pre></div>


{% endraw %}
