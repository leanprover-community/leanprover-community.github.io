---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25977dectrivialperformance.html
---

## Stream: [general](index.html)
### Topic: [dec_trivial performance](25977dectrivialperformance.html)

---


{% raw %}
#### [ Moses Schönfinkel (Sep 25 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dec_trivial%20performance/near/134590634):
<p>I have a computation resolved by <code>dec_trivial</code> that takes about 5 minutes with extreme deterministic timeout lean server setting. How does one diagnose this kind of performance problem - is there a way to inspect what's happening or is the situation similar to <code>#reduce</code> where you're somewhat out of luck in this regard and the best bet is to step through C++ with a debugger? (As a side note, what is being computed is handled by <code>#eval</code> in a few milliseconds.)</p>

#### [ Simon Hudon (Sep 25 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dec_trivial%20performance/near/134617717):
<p><code>dec_trivial</code> is really a blunt instrument. If your proof involves any natural numbers, that's going to take a long time. As you say, it is analogous to <code>#reduce</code>. If you're working with numbers, consider using <code>norm_num</code></p>

#### [ Moses Schönfinkel (Sep 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dec_trivial%20performance/near/134728240):
<p>Sadly I am not - however, this is a great reply, I'll have to take a look at the kinds of tricks <code>norm_num</code> plays and perhaps tailor a solution for myself. Thanks!</p>


{% endraw %}
