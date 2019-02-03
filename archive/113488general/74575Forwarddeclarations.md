---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74575Forwarddeclarations.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Forward declarations](https://leanprover-community.github.io/archive/113488general/74575Forwarddeclarations.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Aug 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227150):
<p>Is it possible to forward declare definitions in lean? I'd like to write something like</p>
<div class="codehilite"><pre><span></span>structure some_data -- forward declare structure because lean can&#39;t look ahead

def mutator_fn := some_data → some_data

structure some_data :=
  (the_data : list nat)
  (data_mutator : mutator_fn)

def some_data.mutate (my_data : some_data) : some_data := my_data.data_mutator my_data
</pre></div>


<p>and that way <code>my_data.mutate</code> would be able mutate itself, for example.</p>
<p>If you can't I'm pretty sad. :( Has it ever been asked for?</p>

#### [ Scott Morrison (Aug 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227260):
<p>I'm not exactly sure what you're after yet, but "mutual defs" may be what you want, and I think are as close as you're going to get.</p>

#### [ Keeley Hoek (Aug 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227578):
<p>I'm now all about mutual definitions!</p>

#### [ Mario Carneiro (Aug 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227588):
<p>This sounds like an obvious source of unsoundness, so it's definitely by design that this isn't doable. I think you should explain in more detail what you are trying to do - there is likely a standard "functional" approach to your problem that does not require forward declaration.</p>

#### [ Mario Carneiro (Aug 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227747):
<p>Rather than forward declaration, the structure can just refer to itself. Since this makes it recursive you have to define it with <code>inductive</code>:</p>
<div class="codehilite"><pre><span></span>meta inductive some_data
| mk (the_data : list nat)
     (data_mutator : some_data → some_data) : some_data
</pre></div>


<p>This has to be <code>meta</code>, though, because it <em>is</em> unsound</p>

#### [ Keeley Hoek (Aug 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227775):
<p>Sure, this was just for programming in lean just like another functional language (i.e. with reckless abandon). Often functions invoke each other, for example. I was willing to sell my soul to the <code>meta</code>s :D</p>

#### [ Mario Carneiro (Aug 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227827):
<p>here is the mutator:</p>
<div class="codehilite"><pre><span></span>meta def some_data.mutate : some_data → some_data
| ⟨d, m⟩ := m ⟨d, m⟩
</pre></div>

#### [ Keeley Hoek (Aug 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227844):
<p>cheers</p>

#### [ Kenny Lau (Aug 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227848):
<p>what does <code>meta</code> mean?</p>

#### [ Johan Commelin (Aug 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227901):
<p>Roughly that you are doing <em>raw</em> Lean. Without proof checking. So all tactics are written in <code>meta</code> land.</p>

#### [ Johan Commelin (Aug 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227918):
<p>But Mario can give you a definition that is a lot better.</p>

#### [ Mario Carneiro (Aug 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227919):
<p>It turns off the safety</p>

#### [ Mario Carneiro (Aug 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227946):
<p>you can do unbounded recursion and non-positive inductives and other unsound things, as well as being able to call meta constants that have a definition in C++</p>

#### [ Keeley Hoek (Aug 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227961):
<p>Actually, how might I solve a related problem, like declaring (toy example):</p>
<div class="codehilite"><pre><span></span>meta structure vertex :=
( color : string )
( adj_list : list edge )

meta structure edge :=
( start end : vertex )
( weight : nat )
</pre></div>

#### [ Mario Carneiro (Aug 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131227962):
<p>mutual inductive</p>

#### [ Keeley Hoek (Aug 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228003):
<p>(thanks again for the practically instant help)</p>

#### [ Keeley Hoek (Aug 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228007):
<p>beat me!</p>

#### [ Mario Carneiro (Aug 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228035):
<div class="codehilite"><pre><span></span>meta mutual inductive vertex, edge
with vertex : Type
| mk (color : string) (adj_list : list edge) : vertex
with edge : Type
| mk (start end_ : vertex) (weight : nat) : edge
</pre></div>

#### [ Mario Carneiro (Aug 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228039):
<p><code>end</code> is a keyword</p>

#### [ Mario Carneiro (Aug 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131228161):
<p>Note that these are dangerous even in pure programming lean, because the pointer structure has cycles and lean is reference counted</p>

#### [ Keeley Hoek (Aug 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131229142):
<p>(In principle) there are countermeasures against rc cycles though, right? Are you saying that lean isn't able to find them at the moment?---if so, appreciate the heads up. thanks again :)</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131229209):
<p>Well, lean is pretty explicitly designed to make rc cycles impossible as a result of the type system</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131229223):
<p>I don't know if it does something special for meta mutual inductives, but I doubt it</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Forward%20declarations/near/131229297):
<p>the goal is to have a strong enough type system that lean can assume powerful things about your code. Functional stuff like common subexpression evaluation is one simple example</p>


{% endraw %}
