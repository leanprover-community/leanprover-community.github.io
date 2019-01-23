---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56077islawfulmonadio.html
---

## Stream: [general](index.html)
### Topic: [is_lawful_monad io](56077islawfulmonadio.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151810212):
I can't seem to find an instance of `is_lawful_monad io` in Lean 3.  Is that a deliberate omission in that `io` is not intended to satisfy the monad laws, or just something that wasn't implemented?  Is there a good way to manually introduce this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Dec 15 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151814377):
`io` is postulated in Lean 3 (and implemented in C++) so it would be impossible to prove the monad laws. You could probably add a constant of type `is_lawful_monad io` and make it an instance. It doesn't seem like it would be troublesome but maybe there's something I'm not thinking of

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151815085):
@**Joe Hendrix** It's certainly consistent to add an instance of `is_lawful_monad io` since there are trivial implementations of the io interface like `\lam _ _, unit` that satisfy the monad laws

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151815143):
(not surprisingly, this trick does not support `tactic.unsafe_run_io`.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151815238):
If you are asking whether `io` is "morally" a lawful monad, first you have to figure out what you mean by that since an `io` action is not an inspectable thing, so you have to define it in terms of sequences of observable behaviors; but once you do that, then the answer seems to be that it is a monad in the appropriate sense. There is just very little that the assumption of lawfulness will give you, since equality of `io` actions is a kind of useless thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 15 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822149):
Yes, I didn't mean inconsistent with the under logic, but the operational semantics.  At a minimum one, I'd want `f = g` to imply that the set of functional traces to be the same (e.g. if there was file io, they'd write the same contents, but one may take longer to do so than the other).  
I don't see equality of `io` as useless, programs often involve input and output, and being able to prove equivalence of two programs is often useful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822196):
I think you probably need more than just the monad laws for that, though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822201):
You need a `lawful_io` class that says how `catch` and `fail` interact, what `iterate` does, and so on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822302):
you could axiomatize the file system, but that's probably not correct. I don't know if any reordering of the file system calls is permissible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 15 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822689):
Yes, I think getting a complete set of axioms including all the predefined constants would be difficult.  In my current case, I literally just needed the monad laws; I had a `state_t` monad that wrapped `io` to provide lookahead when reading a file.  I wanted to prove that peeking one byte ahead and then dropping the byte was the same as just reading the byte.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 15 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151822910):
Another alternative, if you are interested in provably correct IO, is to have a mini language of your own, defined as `list my_io_command` or similar, which you can put a monad instance on and define a simple interpretation function into `io`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joe Hendrix (Dec 15 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_lawful_monad%20io/near/151828407):
Yes, I've done something like that with a free monad.  In this case, I was just wondering if I overlooked existing `io` monad laws.


{% endraw %}
