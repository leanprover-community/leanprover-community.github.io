---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56929Pipesinleanonwindows.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Pipes in lean on windows](https://leanprover-community.github.io/archive/113488general/56929Pipesinleanonwindows.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Sep 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Pipes%20in%20lean%20on%20windows/near/134519900):
<p>Just a quick question for someone in-the-know: does <code>lean</code> lack an implementation of pipes on windows? I'm looking in <code>src/library/pipe.(h/cpp)</code> and it looks empty for windows---am I missing something?</p>

#### [ Keeley Hoek (Sep 24 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Pipes%20in%20lean%20on%20windows/near/134523742):
<p>I guess since even the windows version is built with MSYS2 it doesn't matter</p>

#### [ Sebastian Ullrich (Sep 24 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Pipes%20in%20lean%20on%20windows/near/134535515):
<p>See <a href="https://github.com/leanprover/lean/blob/0eebde1b8b24b087935b75542a3858715097fff2/src/library/process.cpp#L104" target="_blank" title="https://github.com/leanprover/lean/blob/0eebde1b8b24b087935b75542a3858715097fff2/src/library/process.cpp#L104">https://github.com/leanprover/lean/blob/0eebde1b8b24b087935b75542a3858715097fff2/src/library/process.cpp#L104</a></p>


{% endraw %}
