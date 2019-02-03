---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87399Icantbuildlean.html
---

## Stream: [general](index.html)
### Topic: [I can't build lean](87399Icantbuildlean.html)

---


{% raw %}
#### [ Kenny Lau (Mar 08 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457140):
<p><code>ninja</code> gives me error. here's an excerpt:</p>
<div class="codehilite"><pre><span></span>C:\lean\library\init\algebra\ordered_group.lean:342:7: error: _interaction: trying to evaluate sorry
C:\lean\library\init\algebra\ordered_group.lean:342:7: error: unknown identifier &#39;h&#39;
C:\lean\library\init\algebra\ordered_group.lean:342:9: error: invalid &#39;begin-end&#39; expression, &#39;,&#39; expected
C:\lean\library\init\algebra\ordered_group.lean:343:2: error: sync
C:\lean\library\init\algebra\ordered_group.lean:340:0: error: invalid reference to undefined universe level parameter &#39;u_1&#39;
C:\lean\library\init\algebra\ring.lean:168:11: error: _interaction: trying to evaluate sorry
C:\lean\library\init\algebra\ordered_group.lean:340:0: error: invalid reference to undefined universe level parameter &#39;u_6&#39;
C:\lean\library\init\algebra\ordered_group.lean:343:6: error: unknown identifier &#39;neg_add_cancel_left&#39;
C:\lean\library\init\algebra\ordered_group.lean:343:26: error: invalid &#39;begin-end&#39; expression, &#39;,&#39; expected
C:\lean\library\init\algebra\ordered_group.lean:344:0: error: sync
C:\lean\library\init\algebra\ring.lean:168:11: error: invalid reference to undefined universe level parameter &#39;u_2&#39;
C:\lean\library\init\algebra\ring.lean:168:11: error: invalid reference to undefined universe level parameter &#39;u_4&#39;
C:\lean\library\init\algebra\ring.lean:168:11: error: invalid reference to undefined universe level parameter &#39;u_11&#39;
C:\lean\library\init\algebra\ring.lean:168:11: error: invalid reference to undefined universe level parameter &#39;u_16&#39;
C:\lean\library\init\algebra\ring.lean:168:39: error: invalid reference to undefined universe level parameter &#39;u_1&#39;
C:\lean\library\init\algebra\ring.lean:168:39: error: invalid reference to undefined universe level parameter &#39;u_6&#39;
C:\lean\library\init\algebra\ring.lean:169:22: error: unknown identifier &#39;add_left_cancel&#39;
C:\lean\library\init\algebra\ordered_group.lean:335:0: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : b ≤ -a + c
⊢ has_bind tactic
C:\lean\library\init\algebra\ordered_group.lean:335:0: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : b ≤ -a + c
⊢ has_bind tactic
C:\lean\library\init\algebra\ordered_group.lean:337:2: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : b ≤ -a + c
⊢ has_bind tactic
C:\lean\library\init\algebra\ordered_group.lean:342:2: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : a + b ≤ c
⊢ has_bind tactic
C:\lean\library\init\algebra\ring.lean:174:8: error: _interaction: trying to evaluate sorry
C:\lean\library\init\algebra\ring.lean:174:8: error: invalid reference to undefined universe level parameter &#39;u_2&#39;
C:\lean\library\init\algebra\ring.lean:174:8: error: invalid reference to undefined universe level parameter &#39;u_4&#39;
C:\lean\library\init\algebra\ring.lean:174:8: error: invalid reference to undefined universe level parameter &#39;u_11&#39;
C:\lean\library\init\algebra\ordered_group.lean:336:2: error: don&#39;t know how to synthesize placeholder
context:
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : b ≤ -a + c
⊢ Type ?
C:\lean\library\init\algebra\ring.lean:174:8: error: invalid reference to undefined universe level parameter &#39;u_16&#39;
C:\lean\library\init\algebra\ordered_group.lean:341:0: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : a + b ≤ c
⊢ has_bind tactic
C:\lean\library\init\algebra\ring.lean:174:41: error: invalid reference to undefined universe level parameter &#39;u_1&#39;
C:\lean\library\init\algebra\ring.lean:174:41: error: invalid reference to undefined universe level parameter &#39;u_6&#39;
C:\lean\library\init\algebra\ring.lean:167:36: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ring α,
a : α
⊢ has_bind tactic
C:\lean\library\init\algebra\ring.lean:175:23: error: unknown identifier &#39;add_left_cancel&#39;
C:\lean\library\init\algebra\ordered_group.lean:341:0: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : a + b ≤ c
⊢ has_bind tactic
C:\lean\library\init\algebra\ordered_group.lean:344:0: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : a + b ≤ c
⊢ has_bind tactic
C:\lean\library\init\algebra\ring.lean:168:36: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ring α,
a : α
⊢ has_bind tactic
C:\lean\library\init\algebra\ordered_group.lean:348:7: error: _interaction: trying to evaluate sorry
C:\lean\library\init\algebra\ordered_group.lean:348:7: error: _interaction: trying to evaluate sorry
C:\lean\library\init\algebra\ordered_group.lean:341:0: error: failed to synthesize type class instance for
α : Type u,
</pre></div>

#### [ Kenny Lau (Mar 08 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457142):
<p>The error is kinda long and I don't know where to copy it from</p>

#### [ Kenny Lau (Mar 08 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457453):
<p><a href="https://github.com/leanprover/lean" target="_blank" title="https://github.com/leanprover/lean">https://github.com/leanprover/lean</a></p>

#### [ Kenny Lau (Mar 08 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457454):
<p>nvm lean is still building</p>

#### [ Simon Hudon (Mar 08 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457457):
<p>When you install Lean, where does it put the library? Try deleting that</p>

#### [ Kenny Lau (Mar 08 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457613):
<p>I've got a new error</p>

#### [ Kenny Lau (Mar 08 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457614):
<div class="codehilite"><pre><span></span>[36/40] Building CXX object shell/CMakeFiles/lean.dir/server.cpp.obj
[37/40] Linking CXX executable shell\lean_js.exe
[38/40] Linking CXX executable shell\lean.exe
FAILED: shell/lean.exe
cmd.exe /C &quot;cd . &amp;&amp; C:\msys64\mingw64\bin\c++.exe  -Wall -Wextra -std=c++11  -D LEAN_WINDOWS -D LEAN_WIN_STACK_SIZE=104857600 -D LEAN_JSON -D_GLIBCXX_USE_CXX11_ABI=0 -D LEAN_MULTI_THREAD -D LEAN_AUTO_THREAD_FINALIZATION -DLEAN_BUILD_TYPE=&quot;RELEASE&quot; -O3 -DNDEBUG  -Wl,--stack,104857600 -pthread shell/CMakeFiles/lean.dir/lean.cpp.obj shell/CMakeFiles/lean.dir/server.cpp.obj shell/CMakeFiles/lean.dir/leandoc.cpp.obj  -o shell\lean.exe -Wl,--major-image-version,0,--minor-image-version,0  libleanstatic.a -lgmp -lpsapi -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 &amp;&amp; cmd.exe /C &quot;cd /D C:\lean\build\release\shell &amp;&amp; C:\msys64\mingw64\bin\cmake.exe -E remove -f C:/lean/src/../bin/lean.exe &amp;&amp; C:\msys64\mingw64\bin\cmake.exe -E copy C:/lean/build/release/shell/lean.exe C:/lean/src/../bin/&quot;&quot;
Error copying file &quot;C:/lean/build/release/shell/lean.exe&quot; to &quot;C:/lean/src/../bin/&quot;.
ninja: build stopped: subcommand failed.
</pre></div>

#### [ Kenny Lau (Mar 08 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457639):
<p>I've reverted to an older version by <code>git checkout</code></p>

#### [ Kenny Lau (Mar 08 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457641):
<p>and then I tried to build it again</p>

#### [ Simon Hudon (Mar 08 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457693):
<p>Did you pick a revision which builds on Travis and AppVeyor?</p>

#### [ Kenny Lau (Mar 08 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457699):
<p>I used <code>832d235</code> because Kevin Buzzard is currently running on that</p>

#### [ Kenny Lau (Mar 08 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457703):
<p>how do I check if it builds on Travis and AppVeyor?</p>

#### [ Simon Hudon (Mar 08 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457826):
<p>You can go: <a href="https://github.com/leanprover/lean/commits/master" target="_blank" title="https://github.com/leanprover/lean/commits/master">https://github.com/leanprover/lean/commits/master</a></p>
<p>The commits that pass both have a green check mark</p>

#### [ Kenny Lau (Mar 08 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457889):
<p>the last green check mark is March 2 :o</p>

#### [ Mario Carneiro (Mar 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457903):
<p><span class="user-mention" data-user-email="kc_kennylau@yahoo.com.hk" data-user-id="110064">@Kenny Lau</span> The last error you posted usually indicates that <code>lean.exe</code>is locked (usually because it is running somewhere), so the copy command fails. I have had success with deleting <code>lean.exe</code> and then running <code>ninja</code> again</p>

#### [ Kenny Lau (Mar 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457913):
<p>oh thanks, lemme try</p>

#### [ Kenny Lau (Mar 08 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457963):
<p>but should I just go with the green check marks</p>

#### [ Mario Carneiro (Mar 08 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458050):
<p>Sometimes this fails as well because <code>ninja</code> fails to detect that <code>lean.exe</code> has been deleted, and starts running the build script from after when the file should already exist. When this happens I just touch any cpp file and run <code>ninja</code> again to force recompilation</p>

#### [ Kenny Lau (Mar 08 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458375):
<p><span class="user-mention" data-user-email="di.gama@gmail.com" data-user-id="110049">@Mario Carneiro</span> I deleted lean.exe, now it's complaining that lean.exe isn't there</p>

#### [ Mario Carneiro (Mar 08 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458388):
<p>see my last comment</p>

#### [ Mario Carneiro (Mar 08 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458408):
<p>open any cpp file, add and delete a space somewhere, and save, then run ninja again</p>

#### [ Kenny Lau (Mar 08 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458452):
<p>oh</p>

#### [ Kenny Lau (Mar 08 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458456):
<p>nice</p>

#### [ Kenny Lau (Mar 08 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458579):
<p>parabens por mim, it worked</p>

#### [ Kevin Buzzard (Mar 08 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458722):
<p>I just built lean head on Ubuntu 16.04 -- hopefully no memory leaks any more!</p>


{% endraw %}
