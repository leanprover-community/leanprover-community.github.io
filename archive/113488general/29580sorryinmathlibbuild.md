---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29580sorryinmathlibbuild.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: ["sorry" in mathlib build](https://leanprover-community.github.io/archive/113488general/29580sorryinmathlibbuild.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ching-Tsun Chou (Mar 11 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22sorry%22%20in%20mathlib%20build/near/123576774):
<p>I just tried to build the latest mathlib (b15409291946) using the latest nightly Lean build (d6d44a19947e) and saw the following:</p>
<p>/Users/ctchou/Dropbox/Lean/mathlib-latest/tests/wlog.lean:55:0: warning: declaration '[anonymous]' uses sorry<br>
/Users/ctchou/Dropbox/Lean/mathlib-latest/tests/wlog.lean:67:0: warning: declaration '[anonymous]' uses sorry<br>
/Users/ctchou/Dropbox/Lean/mathlib-latest/tests/wlog.lean:76:0: warning: declaration '[anonymous]' uses sorry<br>
/Users/ctchou/Dropbox/Lean/mathlib-latest/tests/wlog.lean:87:0: warning: declaration '[anonymous]' uses sorry</p>
<p>Are they to be expected?</p>
<p>Thanks!</p>

#### [ Simon Hudon (Mar 11 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22sorry%22%20in%20mathlib%20build/near/123576911):
<p>Yes, that's in the test suite. I should change that</p>

#### [ Ching-Tsun Chou (Mar 11 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22sorry%22%20in%20mathlib%20build/near/123576929):
<p>Thanks for letting me know!</p>


{% endraw %}
