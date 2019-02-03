---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61616euclideandivision.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [euclidean division](https://leanprover-community.github.io/archive/113488general/61616euclideandivision.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Nicholas Scheel (Mar 26 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/euclidean%20division/near/124205800):
<p>Is there a proof of Euclidean division (divmod) in the libraries somewhere? I've been looking around for theorems with <code>mod</code> in the core library and mathlib but couldn't find anything ...</p>

#### [ Simon Hudon (Mar 26 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/euclidean%20division/near/124206823):
<p>Have you looked in <code>init.data.nat.lemmas</code> in the core library?</p>
<p><a href="https://github.com/leanprover/lean/blob/master/library/init/data/nat/lemmas.lean#L660-L740" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/data/nat/lemmas.lean#L660-L740">https://github.com/leanprover/lean/blob/master/library/init/data/nat/lemmas.lean#L660-L740</a></p>

#### [ Nicholas Scheel (Mar 26 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/euclidean%20division/near/124207213):
<p>ahh that makes sense now, thanks! I must have glossed over it earlier</p>

#### [ Simon Hudon (Mar 26 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/euclidean%20division/near/124207315):
<p>No problems! The naming scheme is fairly regular so if you search for <code>_mod_</code> in the core library or mathlib, it should give you a good list of available lemmas. If you miss any, they're usually close to the ones you do find</p>


{% endraw %}
