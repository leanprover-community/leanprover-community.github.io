---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03807mathlibisbroken.html
---

## Stream: [general](index.html)
### Topic: [mathlib is broken](03807mathlibisbroken.html)

---


{% raw %}
#### [ Kenny Lau (Jan 12 2019 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987864):
<p>The new Lean (merged just yesterday) breaks mathlib</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987876):
<p>naturally</p>

#### [ Kenny Lau (Jan 12 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987880):
<p>what should we do then?</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987884):
<p>the breakage is mostly just theorems that moved from here to there or vice versa</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987937):
<p>travis seems to disagree</p>

#### [ Kenny Lau (Jan 12 2019 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987962):
<div class="codehilite"><pre><span></span>$ cd /c/lean

Kenny Lau@DESKTOP-F01EMD3 MINGW64 /c/lean
$ git log -1 --pretty=oneline
92826917a252a6092cffaf5fc5f1acb1f8cef379 fix(library/module_mgr): ignore &#39;\r&#39; changes

Kenny Lau@DESKTOP-F01EMD3 MINGW64 /c/lean
$ cd /c/mathlib

Kenny Lau@DESKTOP-F01EMD3 MINGW64 /c/mathlib
$ git pull
Already up-to-date.

Kenny Lau@DESKTOP-F01EMD3 MINGW64 /c/mathlib
$ winpty /c/lean/bin/lean --make
C:\mathlib\tactic\mk_iff_of_inductive_prop.lean:50:9: error: unknown identifier
&#39;drop_pis&#39;
[...]
</pre></div>

#### [ Kenny Lau (Jan 12 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988008):
<p>I think travis uses the old lean</p>

#### [ Gabriel Ebner (Jan 12 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988014):
<p>Travis uses the Lean version specified in leanpkg.toml.</p>

#### [ Kenny Lau (Jan 12 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988024):
<p>which is 3.4.1</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988027):
<p>in that case I think we're fine</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988030):
<p>we can just make an update commit at some point</p>

#### [ Kenny Lau (Jan 12 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988031):
<p>so I need to refrain from using 3.4.2? I really like the <code>\r</code> fix though...</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988078):
<p>adapting to 3.4.2 isn't totally trivial, at least we have to import the removed things and remove any mathlib patches for the bugs</p>

#### [ Kenny Lau (Jan 12 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988090):
<p><a href="https://github.com/leanprover/lean/compare/17fe3de...master" target="_blank" title="https://github.com/leanprover/lean/compare/17fe3de...master">https://github.com/leanprover/lean/compare/17fe3de...master</a></p>

#### [ Kenny Lau (Jan 12 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988092):
<p>changes</p>

#### [ Kenny Lau (Jan 12 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988093):
<p>I'll just go back to 3.4.1 then</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988149):
<p>I can't find a 3.4.2 on lean repo</p>

#### [ Mario Carneiro (Jan 12 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988150):
<p>are you sure it's released?</p>

#### [ Sebastian Ullrich (Jan 12 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988152):
<p>It's not. The nightly is.</p>

#### [ Kenny Lau (Jan 12 2019 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988195):
<p>I build Lean myself</p>

#### [ Sebastian Ullrich (Jan 12 2019 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988205):
<p>I'm ready to release 3.4.2, but maybe someone wants to port mathlib first and make sure everything works out. With the intended branch layout, that would happen on the <code>master</code> branch while regular mathlib stays on the <code>3.4.1</code> default branch :) ...</p>

#### [ Kenny Lau (Jan 12 2019 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988460):
<p>oh man imagine when Lean 4 comes out</p>

#### [ Kenny Lau (Jan 12 2019 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154994675):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I think coinductive was removed, and I think <code>tactic/mk_iff_of_inductive_prop.lean</code> depends on it</p>

#### [ Bryan Gin-ge Chen (Jan 13 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/155049149):
<p><a href="https://github.com/leanprover-community/mathlib/tree/3.4.2" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/3.4.2">The branch <code>3.4.2</code> in <code>leanprover-community/mathlib</code></a> compiles with the latest nightly Lean. I didn't commit any changes to <code>leanpkg.toml</code> so if you want to try it out, you'll have to change <code>3.4.1</code> to <code>nightly</code> after you checkout.</p>
<p>For reference, here are the relevant commits to base Lean <a href="https://github.com/leanprover/lean/commit/e79cb3f2c4987dcfbec8e3e15eb83837cabe1058" target="_blank" title="https://github.com/leanprover/lean/commit/e79cb3f2c4987dcfbec8e3e15eb83837cabe1058">removing coinductive_predicates</a> and <a href="https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb" target="_blank" title="https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb">removing relators and transfer</a>.</p>
<p>All I did was copy the old <code>coinductive_predicates</code> to <code>meta</code>, merge the old <code>relator</code> into <code>logic/relator</code>, copy <code>transfer</code> to <code>tactics</code>, and then add the necessary <code>import</code> statements. I think the only thing that was removed that hasn't been added back in this branch is the transfer-related stuff in <code>library/data/dlist</code> since it only seemed to be used in the code in <code>int</code> that was removed.</p>

#### [ Mario Carneiro (Jan 14 2019 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/155054930):
<p>Looks good. <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> , I think we are go for launch</p>

#### [ Bryan Gin-ge Chen (Jan 14 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/155088895):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I forgot to mention that the file <a href="https://github.com/leanprover-community/mathlib/blob/3.4.2/tests/coinductive.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/3.4.2/tests/coinductive.lean"><code>tests/coinductive</code></a> currently uses <code>#check</code>, <code>#print</code> and <code>admit</code>, which seems to be against mathlib style.</p>

#### [ Abhimanyu Pallavi Sudhir (Jan 18 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/156375247):
<blockquote>
<p>so I need to refrain from using 3.4.2? I really like the <code>\r</code> fix though...</p>
</blockquote>
<p>What's the <code>\r</code> fix?</p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/156375747):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> It's a fix for an issue that windows users were having with unnecessary recompilation: see <a href="https://github.com/leanprover/lean/pull/1986" target="_blank" title="https://github.com/leanprover/lean/pull/1986">https://github.com/leanprover/lean/pull/1986</a></p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/156375774):
<p>I've PR'd the 3.4.2 branch: <a href="https://github.com/leanprover/mathlib/pull/610" target="_blank" title="https://github.com/leanprover/mathlib/pull/610">https://github.com/leanprover/mathlib/pull/610</a></p>


{% endraw %}
