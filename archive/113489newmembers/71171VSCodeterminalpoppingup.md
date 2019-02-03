---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/71171VSCodeterminalpoppingup.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [VS Code terminal popping up](https://leanprover-community.github.io/archive/113489newmembers/71171VSCodeterminalpoppingup.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Casper Putz (Jan 23 2019 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156722159):
<p>When typing in VS Code I constantly have the terminal window popping up with all error messages. It makes it impossible to work... I had this problem before and cannot remember how to fix it. Does anybody know how to fix this?</p>

#### [ Rob Lewis (Jan 23 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156726759):
<p>I've never seen this, what are the error messages?</p>

#### [ Casper Putz (Jan 23 2019 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728064):
<p>When you type the Output terminal with lean error messages pops up (if it was closed) and the cursor moves to the terminal. The terminal contains a bunch of these messages (they are all the same):<br>
<code>LEAN ASSERTION VIOLATION
File: /home/travis/build/leanprover/lean/src/frontends/lean/elaborator.cpp
Line: 3167
Task: /home/cp/Git/finite_fields/src/finite_field.lean: zmod_ring_hom
m_ctx.match(e, *val2)</code></p>

#### [ Casper Putz (Jan 23 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728181):
<p>I now changed this function <code>zmod_ring_hom</code> and now I dont get the problem anymore, nor can I recreate it... If I get it again I will let you know.</p>

#### [ Rob Lewis (Jan 23 2019 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728216):
<p>Well, assertion violations are probably bad, but ignoring that. Are you using a debug version of Lean? (<code>lean --v</code> will tell you.) I thought assertions are only checked in debug.</p>

#### [ Casper Putz (Jan 23 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728480):
<p>Nope Release: Lean (version 3.4.2, nightly-2018-08-23, commit b13ac127fd83, Release).<br>
Can the problem be 3.4.2?</p>

#### [ Patrick Massot (Jan 23 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728562):
<p>At some point in the past, everybody was seeing assertion violations. But then they disappeared (for me)</p>

#### [ Patrick Massot (Jan 23 2019 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728642):
<p>You only need to search for "assertion violation" on this zulip. No need to run a debug version</p>

#### [ Scott Morrison (Jan 23 2019 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728662):
<p>I still see them occasionally, but have not tried to pin one down for a while.</p>

#### [ Scott Morrison (Jan 23 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728722):
<p>Usually they occur when working with half-written structures, with weird syntax violations.</p>

#### [ Casper Putz (Jan 23 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728792):
<p>Yes it was while writing a structure</p>

#### [ Casper Putz (Jan 23 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156728817):
<p>Then I just hope that it just does not happen again haha</p>

#### [ Rob Lewis (Jan 23 2019 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20Code%20terminal%20popping%20up/near/156729271):
<p>Ah, it looks like there are two levels of assertions, most of them are only checked in debug mode but some are checked in release.</p>


{% endraw %}
