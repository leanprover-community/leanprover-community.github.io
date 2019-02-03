---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77009AccessingNattypewithininductiveTyp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Accessing Nat type within inductive Typ](https://leanprover-community.github.io/archive/113488general/77009AccessingNattypewithininductiveTyp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Cameron Crossman (Dec 13 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151722800):
<p>I have the following inductive definition<br>
inductive Typ<br>
  | Nat<br>
  | Fun : Typ → Typ → Typ</p>
<p>and I am trying to write a theorem and start by assuming some variable p is of type Typ.Nat, how do I go about doing so?  I get  </p>
<p>type expected at<br>
  Typ.Nat<br>
term has type<br>
  Typ</p>
<p>error from assume p : Typ.Nat or something similar. Thanks!</p>

#### [ Chris Hughes (Dec 13 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151723856):
<p>Something like this might be what you want</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Typ</span>
<span class="bp">|</span> <span class="n">Nat</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">Typ</span>
<span class="bp">|</span> <span class="n">Fun</span> <span class="o">:</span> <span class="n">Typ</span> <span class="bp">→</span> <span class="n">Typ</span> <span class="bp">→</span> <span class="n">Typ</span>
</pre></div>

#### [ Chris Hughes (Dec 13 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151723870):
<p>Hang on.</p>

#### [ Chris Hughes (Dec 13 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151723876):
<p>Typ.Nat is not a Type, it's a constructor.</p>

#### [ Cameron Crossman (Dec 13 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151723976):
<p>Oh okay <span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Cameron Crossman (Dec 13 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151724023):
<p>So I just construct of that type with variable p : Typ.Nat or something along those lines</p>

#### [ Chris Hughes (Dec 13 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151724050):
<p><code>Typ.nat : Typ</code></p>

#### [ Reid Barton (Dec 13 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151724057):
<p><code>Typ</code> has nothing to do with actual types, despite the name</p>

#### [ Chris Hughes (Dec 13 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151724064):
<p>(deleted)</p>

#### [ Reid Barton (Dec 13 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151724065):
<p>Maybe you want to define an interpretation <code>Typ -&gt; Type</code></p>

#### [ Cameron Crossman (Dec 13 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Accessing%20Nat%20type%20within%20inductive%20Typ/near/151724268):
<p>thanks!</p>


{% endraw %}
