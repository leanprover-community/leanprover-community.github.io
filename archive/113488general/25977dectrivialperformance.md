---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25977dectrivialperformance.html
---

## Stream: [general](index.html)
### Topic: [dec_trivial performance](25977dectrivialperformance.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Sep 25 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dec_trivial%20performance/near/134590634):
I have a computation resolved by `dec_trivial` that takes about 5 minutes with extreme deterministic timeout lean server setting. How does one diagnose this kind of performance problem - is there a way to inspect what's happening or is the situation similar to `#reduce` where you're somewhat out of luck in this regard and the best bet is to step through C++ with a debugger? (As a side note, what is being computed is handled by `#eval` in a few milliseconds.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 25 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dec_trivial%20performance/near/134617717):
`dec_trivial` is really a blunt instrument. If your proof involves any natural numbers, that's going to take a long time. As you say, it is analogous to `#reduce`. If you're working with numbers, consider using `norm_num`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Sep 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dec_trivial%20performance/near/134728240):
Sadly I am not - however, this is a great reply, I'll have to take a look at the kinds of tricks `norm_num` plays and perhaps tailor a solution for myself. Thanks!

