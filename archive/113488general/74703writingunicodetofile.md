---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74703writingunicodetofile.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [writing unicode to file](https://leanprover-community.github.io/archive/113488general/74703writingunicodetofile.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Rob Lewis (Jan 18 2019 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156363926):
<p>Does anyone have experience using file i/o with unicode characters? Lean seems to be mangling them. But I'm pretty sure something like this has worked for me in the past.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">system</span><span class="bp">.</span><span class="n">io</span>
<span class="kn">open</span> <span class="n">io</span> <span class="n">tactic</span>
<span class="n">run_cmd</span> <span class="n">unsafe_run_io</span> <span class="err">$</span> <span class="n">do</span> <span class="n">h</span> <span class="err">←</span> <span class="n">mk_file_handle</span> <span class="s2">&quot;oops.txt&quot;</span> <span class="n">mode</span><span class="bp">.</span><span class="n">write</span><span class="o">,</span> <span class="n">fs</span><span class="bp">.</span><span class="n">put_str</span> <span class="n">h</span> <span class="s2">&quot;α β γ&quot;</span>
</pre></div>


<p>The contents of <code>oops.txt</code> are <code>� � �</code>. This is on my desktop, so no Windows nonsense going on.</p>

#### [ Reid Barton (Jan 18 2019 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156363965):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> ^</p>

#### [ Patrick Massot (Jan 18 2019 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156366966):
<p><a href="https://github.com/leanprover/lean/commit/4e16bc7192f9f32b03222142e659fa3dae4b8025" target="_blank" title="https://github.com/leanprover/lean/commit/4e16bc7192f9f32b03222142e659fa3dae4b8025">https://github.com/leanprover/lean/commit/4e16bc7192f9f32b03222142e659fa3dae4b8025</a></p>

#### [ Rob Lewis (Jan 18 2019 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156367421):
<p>Aha. I suppose this is related to this conversation: <a href="#narrow/stream/113488-general/topic/Character.20encoding.20of.20VM/near/132250034" title="#narrow/stream/113488-general/topic/Character.20encoding.20of.20VM/near/132250034">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character.20encoding.20of.20VM/near/132250034</a></p>

#### [ Rob Lewis (Jan 18 2019 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156367559):
<p>And it looks like I'm using an old version of Lean that doesn't include that commit!</p>

#### [ Sebastian Ullrich (Jan 18 2019 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156368083):
<p><em>starts writing the 3.4.2 changelog</em></p>

#### [ Patrick Massot (Jan 18 2019 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156374294):
<p>I'm currently compiling mathlib from scratch using Lean 3.4.2 (building on work by Bryan). I hope to open a mathlib PR very soon</p>

#### [ Patrick Massot (Jan 18 2019 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156374710):
<p>I'm now merging Johannes' latest commit, but it touches <code>order/basic</code> so I guess this is most recompiling from scratch...</p>

#### [ Patrick Massot (Jan 18 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156375416):
<p><a href="https://github.com/leanprover/mathlib/pull/609" target="_blank" title="https://github.com/leanprover/mathlib/pull/609">https://github.com/leanprover/mathlib/pull/609</a></p>

#### [ Kevin Buzzard (Jan 18 2019 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156376140):
<p>Is the general idea that the moment lean 3.4.2 and mathlib are playing well together, we should all switch? ooh -- I see that <a href="https://leanprover.github.io/download/" target="_blank" title="https://leanprover.github.io/download/">https://leanprover.github.io/download/</a> now links to 3.4.2 so any new users are going to end up with 3.4.2. <span class="user-mention" data-user-id="110087">@Scott Morrison</span> do any installation procedures of yours or mine need updating I wonder?</p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156376525):
<p>Not quite at the moment but as soon as this PR is merged <a href="https://github.com/leanprover/mathlib/pull/610" target="_blank" title="https://github.com/leanprover/mathlib/pull/610">https://github.com/leanprover/mathlib/pull/610</a></p>

#### [ Patrick Massot (Jan 18 2019 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377384):
<p>I was faster</p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377551):
<p>Hah, I missed that, probably because I was adding comments to mine.</p>

#### [ Patrick Massot (Jan 18 2019 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377662):
<p>My PR includes your commits (using it cherry-pick`) but also the latest upstream commits</p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377704):
<p>I rebased mine on master before I PR'd so it should be up to date as well.</p>

#### [ Patrick Massot (Jan 18 2019 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377836):
<p>Ok, they should have the same effect then. I'll close mine</p>

#### [ Scott Morrison (Jan 19 2019 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156412063):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think my installation instructions are still correct.</p>

#### [ Scott Morrison (Jan 19 2019 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156412120):
<p>On &lt;<a href="https://github.com/leanprover/mathlib/blob/master/docs/elan.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/elan.md">https://github.com/leanprover/mathlib/blob/master/docs/elan.md</a>&gt;, it suggests using <code>leanpkg +nightly new my_playground</code> to create a new repository.</p>

#### [ Scott Morrison (Jan 19 2019 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156412132):
<p>That still seems reasonable, but it might be better to add a comment explaining what <code>+nightly</code> actually does, and explaining the alternatives.</p>

#### [ Scott Morrison (Jan 19 2019 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156412135):
<p>If anyone has advice about what should go there, I'm happy to update that file.</p>


{% endraw %}
