---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87399Icantbuildlean.html
---

## Stream: [general](index.html)
### Topic: [I can't build lean](87399Icantbuildlean.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457140):
`ninja` gives me error. here's an excerpt:
```
C:\lean\library\init\algebra\ordered_group.lean:342:7: error: _interaction: trying to evaluate sorry
C:\lean\library\init\algebra\ordered_group.lean:342:7: error: unknown identifier 'h'
C:\lean\library\init\algebra\ordered_group.lean:342:9: error: invalid 'begin-end' expression, ',' expected
C:\lean\library\init\algebra\ordered_group.lean:343:2: error: sync
C:\lean\library\init\algebra\ordered_group.lean:340:0: error: invalid reference to undefined universe level parameter 'u_1'
C:\lean\library\init\algebra\ring.lean:168:11: error: _interaction: trying to evaluate sorry
C:\lean\library\init\algebra\ordered_group.lean:340:0: error: invalid reference to undefined universe level parameter 'u_6'
C:\lean\library\init\algebra\ordered_group.lean:343:6: error: unknown identifier 'neg_add_cancel_left'
C:\lean\library\init\algebra\ordered_group.lean:343:26: error: invalid 'begin-end' expression, ',' expected
C:\lean\library\init\algebra\ordered_group.lean:344:0: error: sync
C:\lean\library\init\algebra\ring.lean:168:11: error: invalid reference to undefined universe level parameter 'u_2'
C:\lean\library\init\algebra\ring.lean:168:11: error: invalid reference to undefined universe level parameter 'u_4'
C:\lean\library\init\algebra\ring.lean:168:11: error: invalid reference to undefined universe level parameter 'u_11'
C:\lean\library\init\algebra\ring.lean:168:11: error: invalid reference to undefined universe level parameter 'u_16'
C:\lean\library\init\algebra\ring.lean:168:39: error: invalid reference to undefined universe level parameter 'u_1'
C:\lean\library\init\algebra\ring.lean:168:39: error: invalid reference to undefined universe level parameter 'u_6'
C:\lean\library\init\algebra\ring.lean:169:22: error: unknown identifier 'add_left_cancel'
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
C:\lean\library\init\algebra\ring.lean:174:8: error: invalid reference to undefined universe level parameter 'u_2'
C:\lean\library\init\algebra\ring.lean:174:8: error: invalid reference to undefined universe level parameter 'u_4'
C:\lean\library\init\algebra\ring.lean:174:8: error: invalid reference to undefined universe level parameter 'u_11'
C:\lean\library\init\algebra\ordered_group.lean:336:2: error: don't know how to synthesize placeholder
context:
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : b ≤ -a + c
⊢ Type ?
C:\lean\library\init\algebra\ring.lean:174:8: error: invalid reference to undefined universe level parameter 'u_16'
C:\lean\library\init\algebra\ordered_group.lean:341:0: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ordered_comm_group α,
a b c : α,
h : a + b ≤ c
⊢ has_bind tactic
C:\lean\library\init\algebra\ring.lean:174:41: error: invalid reference to undefined universe level parameter 'u_1'
C:\lean\library\init\algebra\ring.lean:174:41: error: invalid reference to undefined universe level parameter 'u_6'
C:\lean\library\init\algebra\ring.lean:167:36: error: failed to synthesize type class instance for
α : Type u,
_inst_1 : ring α,
a : α
⊢ has_bind tactic
C:\lean\library\init\algebra\ring.lean:175:23: error: unknown identifier 'add_left_cancel'
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
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457142):
The error is kinda long and I don't know where to copy it from

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457453):
https://github.com/leanprover/lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457454):
nvm lean is still building

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457457):
When you install Lean, where does it put the library? Try deleting that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457613):
I've got a new error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457614):
```
[36/40] Building CXX object shell/CMakeFiles/lean.dir/server.cpp.obj
[37/40] Linking CXX executable shell\lean_js.exe
[38/40] Linking CXX executable shell\lean.exe
FAILED: shell/lean.exe
cmd.exe /C "cd . && C:\msys64\mingw64\bin\c++.exe  -Wall -Wextra -std=c++11  -D LEAN_WINDOWS -D LEAN_WIN_STACK_SIZE=104857600 -D LEAN_JSON -D_GLIBCXX_USE_CXX11_ABI=0 -D LEAN_MULTI_THREAD -D LEAN_AUTO_THREAD_FINALIZATION -DLEAN_BUILD_TYPE="RELEASE" -O3 -DNDEBUG  -Wl,--stack,104857600 -pthread shell/CMakeFiles/lean.dir/lean.cpp.obj shell/CMakeFiles/lean.dir/server.cpp.obj shell/CMakeFiles/lean.dir/leandoc.cpp.obj  -o shell\lean.exe -Wl,--major-image-version,0,--minor-image-version,0  libleanstatic.a -lgmp -lpsapi -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 && cmd.exe /C "cd /D C:\lean\build\release\shell && C:\msys64\mingw64\bin\cmake.exe -E remove -f C:/lean/src/../bin/lean.exe && C:\msys64\mingw64\bin\cmake.exe -E copy C:/lean/build/release/shell/lean.exe C:/lean/src/../bin/""
Error copying file "C:/lean/build/release/shell/lean.exe" to "C:/lean/src/../bin/".
ninja: build stopped: subcommand failed.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457639):
I've reverted to an older version by `git checkout`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457641):
and then I tried to build it again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457693):
Did you pick a revision which builds on Travis and AppVeyor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457699):
I used `832d235` because Kevin Buzzard is currently running on that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457703):
how do I check if it builds on Travis and AppVeyor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457826):
You can go: https://github.com/leanprover/lean/commits/master

The commits that pass both have a green check mark

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457889):
the last green check mark is March 2 :o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457903):
@**Kenny Lau** The last error you posted usually indicates that `lean.exe`is locked (usually because it is running somewhere), so the copy command fails. I have had success with deleting `lean.exe` and then running `ninja` again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457913):
oh thanks, lemme try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123457963):
but should I just go with the green check marks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458050):
Sometimes this fails as well because `ninja` fails to detect that `lean.exe` has been deleted, and starts running the build script from after when the file should already exist. When this happens I just touch any cpp file and run `ninja` again to force recompilation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458375):
@**Mario Carneiro** I deleted lean.exe, now it's complaining that lean.exe isn't there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458388):
see my last comment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 08 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458408):
open any cpp file, add and delete a space somewhere, and save, then run ninja again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458452):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458456):
nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458579):
parabens por mim, it worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 08 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20can%27t%20build%20lean/near/123458722):
I just built lean head on Ubuntu 16.04 -- hopefully no memory leaks any more!

