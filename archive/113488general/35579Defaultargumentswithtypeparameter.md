---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35579Defaultargumentswithtypeparameter.html
---

## Stream: [general](index.html)
### Topic: [Default arguments with type parameter](35579Defaultargumentswithtypeparameter.html)

---


{% raw %}
#### [ Keeley Hoek (Aug 18 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default%20arguments%20with%20type%20parameter/near/132355082):
<p>I've got a (honest, in-a-program) function</p>
<div class="codehilite"><pre><span></span>def do_some_stuff {α : Type} (cfg : config α) := xxx
</pre></div>


<p>In an ideal world, I'd like to be able to have a default <code>config</code>, with a fixed parameter <code>α</code> (obviously), so I could write <code>do_some_stuff</code> and everything would work great. I guess I want to be able to write (and compile)</p>
<div class="codehilite"><pre><span></span>def default_config : config string := xxx
def do_some_stuff {α : Type} (cfg : config α := default_config) := xxx
</pre></div>


<p>with that having the meaning that if <code>cfg</code> is omitted, the type <code>α</code> is forced to be <code>string</code>.</p>
<p>I see that I might be "fighting the system". What do you think is the best way to emulate this kind of option-passing interface?</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default%20arguments%20with%20type%20parameter/near/132357334):
<p>This comes up in core lean in some of the structures, where you have to give <code>A</code> such that <code>A = B</code>, and the proof of <code>A = B</code> is <code>rfl</code> but this only works if <code>A</code> is <code>B</code>. You can set this up using auto params instead of opt params:</p>
<div class="codehilite"><pre><span></span>def config : Type → Type := sorry
def default_config : config string := sorry
meta def default_config_tac : tactic unit := `[exact default_config]
def do_some_stuff {α : Type} (cfg : config α . default_config_tac) : α := sorry

example : string := do_some_stuff -- ok
example : nat := do_some_stuff (sorry : config ℕ) -- ok
example : nat := do_some_stuff -- error
</pre></div>

#### [ Keeley Hoek (Aug 18 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default%20arguments%20with%20type%20parameter/near/132357505):
<p>Thanks so much Mario. Do you know where I could read about the auto params "." period syntax?</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default%20arguments%20with%20type%20parameter/near/132357514):
<p>It might be in the reference manual? It's very simple. You can only put a name of a def of a <code>tactic unit</code> there, and it gets called when the argument is not supplied</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default%20arguments%20with%20type%20parameter/near/132357522):
<p>I wish it would accept an expression so you could write a tactic inline there, but alas</p>

#### [ Keeley Hoek (Aug 18 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default%20arguments%20with%20type%20parameter/near/132357563):
<p>ok sweet! cheers!</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Default%20arguments%20with%20type%20parameter/near/132357567):
<p>(actually there is a good reason you can't write a tactic inline, since that would be <code>meta</code>)</p>


{% endraw %}
