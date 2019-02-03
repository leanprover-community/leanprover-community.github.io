---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56077islawfulmonadio.html
---

## Stream: [general](index.html)
### Topic: [is_lawful_monad io](56077islawfulmonadio.html)

---


{% raw %}
#### [ Joe Hendrix (Dec 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151810212):
<p>I can't seem to find an instance of <code>is_lawful_monad io</code> in Lean 3.  Is that a deliberate omission in that <code>io</code> is not intended to satisfy the monad laws, or just something that wasn't implemented?  Is there a good way to manually introduce this?</p>

#### [ Simon Hudon (Dec 15 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151814377):
<p><code>io</code> is postulated in Lean 3 (and implemented in C++) so it would be impossible to prove the monad laws. You could probably add a constant of type <code>is_lawful_monad io</code> and make it an instance. It doesn't seem like it would be troublesome but maybe there's something I'm not thinking of</p>

#### [ Mario Carneiro (Dec 15 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151815085):
<p><span class="user-mention" data-user-id="110994">@Joe Hendrix</span> It's certainly consistent to add an instance of <code>is_lawful_monad io</code> since there are trivial implementations of the io interface like <code>\lam _ _, unit</code> that satisfy the monad laws</p>

#### [ Mario Carneiro (Dec 15 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151815143):
<p>(not surprisingly, this trick does not support <code>tactic.unsafe_run_io</code>.)</p>

#### [ Mario Carneiro (Dec 15 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151815238):
<p>If you are asking whether <code>io</code> is "morally" a lawful monad, first you have to figure out what you mean by that since an <code>io</code> action is not an inspectable thing, so you have to define it in terms of sequences of observable behaviors; but once you do that, then the answer seems to be that it is a monad in the appropriate sense. There is just very little that the assumption of lawfulness will give you, since equality of <code>io</code> actions is a kind of useless thing</p>

#### [ Joe Hendrix (Dec 15 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822149):
<p>Yes, I didn't mean inconsistent with the under logic, but the operational semantics.  At a minimum one, I'd want <code>f = g</code> to imply that the set of functional traces to be the same (e.g. if there was file io, they'd write the same contents, but one may take longer to do so than the other).  <br>
I don't see equality of <code>io</code> as useless, programs often involve input and output, and being able to prove equivalence of two programs is often useful.</p>

#### [ Mario Carneiro (Dec 15 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822196):
<p>I think you probably need more than just the monad laws for that, though</p>

#### [ Mario Carneiro (Dec 15 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822201):
<p>You need a <code>lawful_io</code> class that says how <code>catch</code> and <code>fail</code> interact, what <code>iterate</code> does, and so on</p>

#### [ Mario Carneiro (Dec 15 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822302):
<p>you could axiomatize the file system, but that's probably not correct. I don't know if any reordering of the file system calls is permissible</p>

#### [ Joe Hendrix (Dec 15 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822689):
<p>Yes, I think getting a complete set of axioms including all the predefined constants would be difficult.  In my current case, I literally just needed the monad laws; I had a <code>state_t</code> monad that wrapped <code>io</code> to provide lookahead when reading a file.  I wanted to prove that peeking one byte ahead and then dropping the byte was the same as just reading the byte.</p>

#### [ Mario Carneiro (Dec 15 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822910):
<p>Another alternative, if you are interested in provably correct IO, is to have a mini language of your own, defined as <code>list my_io_command</code> or similar, which you can put a monad instance on and define a simple interpretation function into <code>io</code></p>

#### [ Joe Hendrix (Dec 15 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151828407):
<p>Yes, I've done something like that with a free monad.  In this case, I was just wondering if I overlooked existing <code>io</code> monad laws.</p>


{% endraw %}
