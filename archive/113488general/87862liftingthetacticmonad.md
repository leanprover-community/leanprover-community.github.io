---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87862liftingthetacticmonad.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lifting the tactic monad](https://leanprover-community.github.io/archive/113488general/87862liftingthetacticmonad.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 24 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682369):
<p>Several times I have wanted to use a lift of the tactic monad, in order to carry along some additional state. (As a simple example, I would like to carry along a ℕ that limits how much more computation is allowed, that several different subtactics need to respect.)</p>

#### [ Scott Morrison (Aug 24 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682450):
<p>I've successfully written some infrastructure to do this (essentially, some typeclasses and coercions that let you move up and down from standard <code>tactic α</code> to <code>stateful_tactic β α</code>), but it was gross and hackish.</p>

#### [ Scott Morrison (Aug 24 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682468):
<p>Is this something that others would find useful? If so, could we agree on a basic design that everyone would be happy with?</p>

#### [ Johan Commelin (Aug 24 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682484):
<p>I think <a href="https://github.com/EdAyers/lean-humanproof/blob/a3df90b4ccd1356283e47cf56b986701944f4100/src/robot.lean#L38" target="_blank" title="https://github.com/EdAyers/lean-humanproof/blob/a3df90b4ccd1356283e47cf56b986701944f4100/src/robot.lean#L38">https://github.com/EdAyers/lean-humanproof/blob/a3df90b4ccd1356283e47cf56b986701944f4100/src/robot.lean#L38</a> might be an example of how to do that...</p>

#### [ Johan Commelin (Aug 24 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682490):
<p>So you need to use <code>state_t</code>...</p>

#### [ Scott Morrison (Aug 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682628):
<p>Yes --- that's exactly another example of what I have in mind.</p>

#### [ Scott Morrison (Aug 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682641):
<p>The problem is now writing metatactics that are "monad polymorphic".</p>

#### [ Scott Morrison (Aug 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682671):
<p>We need a typeclass that you can decorate your lift of <code>tactic</code> (e.g. <span class="user-mention" data-user-id="121918">@Edward Ayers</span>'s <code>robot</code>) with, that says that it really is a lift of <code>tactic</code>.</p>

#### [ Scott Morrison (Aug 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132682966):
<p>Ah, there is more in <code>state_t</code> than I'd seen before.</p>

#### [ Scott Morrison (Aug 24 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132684057):
<p>I think I'm still not understanding how I'm meant to use <code>state_t</code>. I want to be able to write something like</p>
<div class="codehilite"><pre><span></span>variables {m : Type → Type → Type} [stateful_tactic m]

meta def my_meta_tactic {α β} (f : α → β) (t : m σ α) : m σ β :=
do
  get_state &gt;&gt;= trace, -- prints the current state, a term of type σ
  r ← t,
  trace r,             -- prints the result of t, a term of type α
  get_state &gt;&gt;= trace, -- prints the new state, a term of type σ
  done,
  return (f r)
</pre></div>


<p>Here <code>trace</code> and <code>done</code> are meant to just be the standard ones from <code>tactic</code>, that are being automatically lifted to <code>stateful_tactic</code><br>
(such that they just preserve the σ state).</p>

#### [ Scott Morrison (Aug 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132684651):
<p>Clearly <code>state_t</code> isn't quite doing this: it doesn't even mention <code>tactic</code>.</p>

#### [ Rob Lewis (Aug 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132685496):
<p>Your <code>m</code> is just <code>λ σ, state_t σ tactic</code>. I'm not sure if the coercions from <code>tactic</code> are in the library, but they're very easy to write.</p>

#### [ Edward Ayers (Aug 24 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132690060):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="kn">structure</span> <span class="n">my_state</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">my_bool</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span>
<span class="o">(</span><span class="n">my_nat</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span>
<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">meta</span> <span class="n">def</span> <span class="n">state_tactic</span> <span class="o">:</span> <span class="kt">Type</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="n">state_t</span> <span class="n">my_state</span> <span class="n">tactic</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">of_tactic</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">state_tactic</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">state_t</span><span class="bp">.</span><span class="n">lift</span>
<span class="n">meta</span> <span class="kn">instance</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="o">(</span><span class="n">tactic</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">state_tactic</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">of_tactic</span><span class="bp">⟩</span>
<span class="kn">open</span> <span class="n">tactic</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">my_meta_tactic</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">state_tactic</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">state_tactic</span> <span class="n">β</span> <span class="o">:=</span>
<span class="n">do</span>
    <span class="n">state</span> <span class="err">←</span> <span class="n">get</span><span class="o">,</span> <span class="c1">--get the state</span>
    <span class="n">trace</span> <span class="n">state</span><span class="bp">.</span><span class="n">my_nat</span><span class="o">,</span>
    <span class="n">r</span> <span class="err">←</span> <span class="n">t</span><span class="o">,</span>
    <span class="n">put</span> <span class="o">{</span><span class="n">my_nat</span><span class="o">:=</span> <span class="mi">100</span><span class="o">,</span> <span class="bp">..</span><span class="n">state</span><span class="o">},</span> <span class="c1">--set the state</span>
    <span class="n">done</span><span class="o">,</span> <span class="c1">-- done is a tactic but the coercion converts it to a state_tactic.</span>
    <span class="n">return</span> <span class="err">$</span> <span class="n">f</span> <span class="n">r</span>
</pre></div>

#### [ Edward Ayers (Aug 24 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132690204):
<p>All of the <code>alternative</code> stuff works out of the box. <code>&lt;|&gt;</code>, <code>guard</code> and so on.</p>

#### [ Scott Morrison (Aug 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132691315):
<p>Thanks <span class="user-mention" data-user-id="121918">@Edward Ayers</span>. This isn't quite there yet: I still want to abstract over <code>my_state</code>. That is, I want to be able to write <code>my_meta_tactic</code> so that it works with many different monads, as long as they come with a promise that they contain <code>my_state</code>, but possibly may carry additional state as well.</p>

#### [ Scott Morrison (Aug 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132691330):
<p>That is, sometimes I will write tactics that refer to some specific notion of state.</p>

#### [ Scott Morrison (Aug 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132691379):
<p>But other times I want to write a meta tactic that is merely sufficient polymorphic that is can pass through notions of state that other people might need.</p>

#### [ Edward Ayers (Aug 24 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132692605):
<p>I guess if you are only storing bools nats and strings you can use <code>tactic.set_options</code> as a quick fix.</p>

#### [ Edward Ayers (Aug 24 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132693624):
<p>I came up with a crazy idea that would solve this. The trouble is the type universes don't work and one would have to implement the <code>dependent_dict</code> object!</p>
<div class="codehilite"><pre><span></span><span class="c1">--I think that you can implement this as an rbtree but it&#39;s a lot of effort.</span>
<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">constant</span> <span class="n">dependent_dict</span> <span class="o">(</span><span class="n">key</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">key</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span>
<span class="kn">namespace</span> <span class="n">dependent_dict</span>
    <span class="kn">variables</span> <span class="o">{</span><span class="n">key</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">key</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
    <span class="kn">constant</span> <span class="n">get</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">key</span><span class="o">)</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">dependent_dict</span> <span class="n">key</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="o">(</span><span class="n">α</span> <span class="n">k</span><span class="o">)</span>
    <span class="kn">constant</span> <span class="n">set</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">key</span><span class="o">)</span> <span class="o">(</span><span class="n">value</span> <span class="o">:</span> <span class="n">α</span> <span class="n">k</span><span class="o">)</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">dependent_dict</span> <span class="n">key</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">dependent_dict</span> <span class="n">key</span> <span class="n">α</span>
<span class="kn">end</span> <span class="n">dependent_dict</span>

<span class="n">meta</span> <span class="kn">structure</span> <span class="n">custom_state</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">name</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span>
<span class="o">(</span><span class="n">type</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
<span class="o">(</span><span class="n">default</span> <span class="o">:</span> <span class="n">type</span><span class="o">)</span>
<span class="c1">-- [TODO] define an ordering according to `name`</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">custom_state_tactic</span> <span class="o">:=</span> <span class="n">state_t</span> <span class="o">(</span><span class="n">dependent_dict</span> <span class="n">custom_state</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">c</span><span class="o">:</span><span class="n">custom_state</span><span class="o">,</span> <span class="n">c</span><span class="bp">.</span><span class="n">type</span><span class="o">))</span> <span class="n">tactic</span>
<span class="kn">namespace</span> <span class="n">custom_state_tactic</span>
    <span class="n">meta</span> <span class="n">def</span> <span class="n">get</span> <span class="o">(</span><span class="n">st</span> <span class="o">:</span> <span class="n">custom_state</span><span class="o">)</span> <span class="o">:</span> <span class="n">custom_state_tactic</span> <span class="n">st</span><span class="bp">.</span><span class="n">type</span> <span class="o">:=</span> <span class="n">do</span>
        <span class="n">d</span> <span class="err">←</span> <span class="n">state_t</span><span class="bp">.</span><span class="n">get</span><span class="o">,</span>
        <span class="n">pure</span> <span class="err">$</span> <span class="n">option</span><span class="bp">.</span><span class="n">get_or_else</span> <span class="o">(</span><span class="n">dependent_dict</span><span class="bp">.</span><span class="n">get</span> <span class="n">st</span><span class="bp">.</span><span class="n">name</span> <span class="n">d</span><span class="o">)</span> <span class="n">st</span><span class="bp">.</span><span class="n">default</span>
    <span class="n">meta</span> <span class="n">def</span> <span class="n">set</span> <span class="o">(</span><span class="n">st</span> <span class="o">:</span> <span class="n">custom_state</span><span class="o">)</span> <span class="o">(</span><span class="n">value</span> <span class="o">:</span> <span class="n">st</span><span class="bp">.</span><span class="n">type</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">custom_state_tactic</span> <span class="n">unit</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
        <span class="n">d</span> <span class="err">←</span> <span class="n">state_t</span><span class="bp">.</span><span class="n">get</span><span class="o">,</span>
        <span class="n">state_t</span><span class="bp">.</span><span class="n">put</span> <span class="o">(</span><span class="n">dependent_dict</span><span class="bp">.</span><span class="n">set</span> <span class="n">st</span> <span class="n">value</span> <span class="n">d</span><span class="o">)</span>
<span class="kn">end</span> <span class="n">custom_state_tactic</span>
</pre></div>

#### [ Edward Ayers (Aug 24 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132693642):
<p>So the idea is you would always use <code>custom_state_tactic</code> but define your own instance of <code>custom_state</code> to get the values that you care about.</p>

#### [ Edward Ayers (Aug 24 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132693690):
<p>I don't think this will work but I thought I'd share.</p>

#### [ Edward Ayers (Aug 24 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132693809):
<p>It also wouldn't work because you could give two <code>custom_state</code>s the same name but different types, and I don't think we have decidable equality for types</p>

#### [ Reid Barton (Aug 24 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132701340):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> are you familiar with the design of <a href="http://hackage.haskell.org/package/mtl" target="_blank" title="http://hackage.haskell.org/package/mtl">mtl</a>?<br>
<a href="http://hackage.haskell.org/package/mtl-2.2.2/docs/Control-Monad-State-Class.html" target="_blank" title="http://hackage.haskell.org/package/mtl-2.2.2/docs/Control-Monad-State-Class.html">MonadState</a> is your "monad that comes with a promise that it contains <code>my_state</code>", I think.</p>

#### [ Reid Barton (Aug 24 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132701413):
<p>But I'm not sure if this encompasses everything you want</p>

#### [ Sebastian Ullrich (Aug 24 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132702480):
<p><code>monad_state</code> is already in Lean 3. A <code>monad_tactic</code> might be introduced in Lean 4.</p>

#### [ Reid Barton (Aug 24 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703270):
<p>It would just be <code>has_monad_lift_t tactic</code>, right?</p>

#### [ Reid Barton (Aug 24 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703274):
<p>Up to specializing names</p>

#### [ Sebastian Ullrich (Aug 24 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703524):
<p>That is not sufficient for lifting <code>tactic _ -&gt; tactic _</code> functions or even more complex ones</p>

#### [ Reid Barton (Aug 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703985):
<p>Oh, I've never actually wanted to do that with IO, and I'm not sure I trust any of the packages which claim to solve that problem anyways.</p>

#### [ Reid Barton (Aug 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132703997):
<p>Maybe <code>tactic</code> has more compelling use cases</p>

#### [ Sebastian Ullrich (Aug 24 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132704242):
<p>Yeah, it's way more important for <code>tactic</code> since it has a bunch of combinators like <code>try</code>, <code>focus</code>, <code>any_goals</code>, ...</p>

#### [ Edward Ayers (Aug 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lifting%20the%20tactic%20monad/near/132912880):
<p>Using <code>monad_state</code>works really well for me.</p>


{% endraw %}
