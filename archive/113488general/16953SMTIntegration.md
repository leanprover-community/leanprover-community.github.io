---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16953SMTIntegration.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [SMT Integration](https://leanprover-community.github.io/archive/113488general/16953SMTIntegration.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Wojciech Nawrocki (Jan 25 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156879205):
<p>What's the status of integrating SMT solvers with Lean? There are some references to it in the documentation, (e.g. <a href="https://leanprover.github.io/reference/tactics.html#the-smt-state" target="_blank" title="https://leanprover.github.io/reference/tactics.html#the-smt-state">https://leanprover.github.io/reference/tactics.html#the-smt-state</a>) but all are empty. It would be nice to have some automatic solving.</p>

#### [ Simon Hudon (Jan 25 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156879540):
<p>The smt tactics are not very much used. I just started this week looking at wrapping <code>veriT</code> into Lean tactics and as far as I know, that's the only such work going on in Lean</p>

#### [ Simon Hudon (Jan 25 2019 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156879683):
<p>Maybe Jasmin Blanchette's team has something related in the works but I don't know any details.</p>

#### [ Simon Cruanes (Jan 25 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156880647):
<p>What fragment do you plan to encode into SMTLIB, and how?</p>

#### [ Simon Hudon (Jan 25 2019 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156880726):
<p>Right now, I haven't settled on a fragment, I'm just looking at building the interface for now.</p>

#### [ Simon Cruanes (Jan 25 2019 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156881643):
<p>I suppose the closest existing thing is SMTCoq, especially regarding proof reconstruction, but that's a lot of work</p>

#### [ Simon Hudon (Jan 25 2019 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156886857):
<p>I'm looking at SMTCoq and Blanchette's work for Isabelle. I think it's probably work worth doing.</p>

#### [ Simon Hudon (Jan 25 2019 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156886925):
<p>I'm building proof obligation generators in Lean and smt solvers are useful to discharge those</p>

#### [ Simon Cruanes (Jan 25 2019 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156886946):
<p>I know Jasmin has been talking about an independent Sledgehammer-like tool that could be shared between proof assistants, but that'd be even more work…<br>
If you do it directly in Lean it'll be easier to reconstruct proofs.</p>

#### [ Simon Hudon (Jan 25 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156887476):
<p>That's my opinion too. I think whereas Jasmin's project is more general and long term, mine is to address an immediate need and I'm ok with doing it imperfectly at first</p>

#### [ Gabriel Ebner (Jan 25 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156887796):
<p>There is <a href="https://github.com/leanprover/smt2_interface" target="_blank" title="https://github.com/leanprover/smt2_interface">https://github.com/leanprover/smt2_interface</a> from quite some time ago, but it doesn't generate proofs.</p>

#### [ Simon Hudon (Jan 25 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/SMT%20Integration/near/156888238):
<p>Thanks for the link! I was trying to find it again but didn't look in the most obvious place</p>


{% endraw %}
