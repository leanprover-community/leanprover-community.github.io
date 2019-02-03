---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21093Relationshipbetweenreposleanandleannightly.html
---

## Stream: [general](index.html)
### Topic: [Relationship between repos lean and lean-nightly](21093Relationshipbetweenreposleanandleannightly.html)

---


{% raw %}
#### [ Ching-Tsun Chou (Mar 11 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship%20between%20repos%20lean%20and%20lean-nightly/near/123582525):
<p>I am confused about the relationship between the following two repos:</p>
<p><a href="https://github.com/leanprover/lean" target="_blank" title="https://github.com/leanprover/lean">https://github.com/leanprover/lean</a></p>
<p><a href="https://github.com/leanprover/lean-nightly" target="_blank" title="https://github.com/leanprover/lean-nightly">https://github.com/leanprover/lean-nightly</a></p>
<p>I thought the latter contains snapshots of the former which also appear as nightly builds.  But the latest nightly in:</p>
<p><a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a><br>
commit: 5f38fd46d102e81ea798b97d18825ca583150aca</p>
<p>does not appear to exist in the lean repo.  Was my understanding wrong?</p>
<p>Thanks!</p>

#### [ Simon Hudon (Mar 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship%20between%20repos%20lean%20and%20lean-nightly/near/123582599):
<p>I believe that hash is a commit to the <code>lean-nightly</code> project which is not a fork of <code>lean</code> it is used more like some server space. When travis is done building <code>lean</code>, it pushes a release <code>lean-nightly</code> which is not a commit in <code>lean-nightly</code></p>

#### [ Sebastian Ullrich (Mar 11 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship%20between%20repos%20lean%20and%20lean-nightly/near/123583589):
<p>These are still test releases. I will remove them once the change is live.</p>

#### [ Ching-Tsun Chou (Mar 11 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship%20between%20repos%20lean%20and%20lean-nightly/near/123583642):
<p>What about the nightlies here?</p>
<p><a href="https://leanprover.github.io/download/" target="_blank" title="https://leanprover.github.io/download/">https://leanprover.github.io/download/</a></p>
<p>How are they related to the ones in lean-nightly?</p>
<p>Thanks!</p>

#### [ Sebastian Ullrich (Mar 11 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship%20between%20repos%20lean%20and%20lean-nightly/near/123584437):
<p>The download page will link to the releases page when the change is done</p>


{% endraw %}
