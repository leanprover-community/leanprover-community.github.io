---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88411libgmpdependency.html
---

## Stream: [general](index.html)
### Topic: [libgmp dependency](88411libgmpdependency.html)

---


{% raw %}
#### [ Scott Morrison (Sep 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libgmp%20dependency/near/134657745):
<p>I know on macOS you have to install <code>libgmp</code> before Lean will work. Does anyone know if there is a similar requirement on linux? (There doesn't appear to be on Windows.)</p>

#### [ Reid Barton (Sep 26 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libgmp%20dependency/near/134671562):
<p>The toolchains installed by elan contain static binaries, which I find a bit surprising, but should mean you don't need libgmp. However all the machines I have lean on also have libgmp installed anyways, so no definitive proof.</p>

#### [ Sebastian Ullrich (Sep 26 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libgmp%20dependency/near/134685427):
<p>Yes, on Linux it's definitely a static binary. I'm not even sure why it's not on macOS</p>


{% endraw %}
