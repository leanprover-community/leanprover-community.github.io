---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79716memoryleakinserver.html
---

## Stream: [general](index.html)
### Topic: [memory leak in server?](79716memoryleakinserver.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017339):
```
invalid import: data.set.basic
excessive memory consumption detected at 'replace' (potential solution: increase memory consumption threshold)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017352):
Why do those happen?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Feb 27 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017356):
restart lean. That sort of thing happend to me all the time lately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017359):
I feel like it's happening more and more often to me too at the minute. Is Lean a bit less stable than it was or something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017400):
I am trying to define a structure sheaf, I could do without random errors :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Feb 27 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017464):
Also simp randomly fails, and then succeeds without me doing anything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123019223):
Yeah we got it working in the end.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Feb 27 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123019247):
nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123032936):
I wanted to knock up a quick "proof by induction" example for pedagogical reasons and I choose to prove that the sum of the first n integers (or first n+1 integers for you CS guys) equalled n(n+1)/2.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123032996):
I had to decide on my infrastructure so I went for list.sum (list.range (succ n))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033010):
but then I realised that to apply the inductive step I needed some result of the form "the sum from 0 to n+1 of f(i) equals (the sum from 0 to n of f(i)) + f(n+1)"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033015):
and I couldn't spot this immediately in list, which made me wonder whether I was using the wrong inductive type to do this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Feb 27 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033166):
I also get the feeling that this issue got worse.  It seems like there is a new memory leak in server mode.  @**Sebastian Ullrich** Any ideas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 27 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033171):
(moving to (no topic))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Feb 27 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033762):
It's certainly annoying. Not sure how to debug something like this - first find a test case like a script doing trivial edits, confirm the issue, and then...?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Feb 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033917):
The "human test script" that I used was: open default.lean, change something in init/core.lean, go back to default.lean, repeat.  Yes, debugging this is not easy.  Since this seems to be a regression, we can try to bisect it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Feb 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033931):
Last time we had such an issue, I spent hours in valgrind+gdb, chasing pointers to see which data is alive at the moment.  Unfortunately none of the memory issues were real leaks in the past, the memory was always reachable via caches/etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Feb 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033988):
What about opportunistic cache reclaiming?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Feb 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123034039):
We kill our child threads if they are idle for a few milliseconds, and their caches die with them.  This was sufficient in the past.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Feb 27 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123034329):
@**Gabriel Ebner** Have you ever used [massif](http://valgrind.org/docs/manual/ms-manual.html) before? Maybe I should give it a try.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Feb 27 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123035399):
I don't think so.  I mainly used the memcheck monitor commands.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 07 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123411331):
@**Gabriel Ebner** There seems to be a shared_ptr cycle, assuming valgrind isn't lying:
```
==13508== 4,260,044 (272 direct, 4,259,772 indirect) bytes in 1 blocks are definitely lost in loss record 13,808 of 13,808
==13508==    at 0x4C2E0EF: operator new(unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==13508==    by 0xC0FFA3: __gnu_cxx::new_allocator<std::_Sp_counted_ptr_inplace<lean::module_info, std::allocator<lean::module_info>, (__gnu_cxx::_Lock_policy)2> >::allocate(unsigned long, void const*) (new_allocator.h:104)
...
==13508==    by 0xDBE2A8: std::shared_ptr<lean::module_info> std::make_shared<lean::module_info, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, lean::module_src, long&>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, lean::module_src&&, long&) (shared_ptr.h:636)
==13508==    by 0xDBA2BD: lean::fs_module_vfs::load_module(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) (module_mgr.cpp:446)
==13508==    by 0xBF4BEE: lean::server::load_module(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) (server.cpp:699)
==13508==    by 0xDB70AB: lean::module_mgr::build_module(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, lean::rb_tree<lean::name, lean::name_quick_cmp>) (module_mgr.cpp:157)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 08 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123433929):
@**Sebastian Ullrich** I think the module_mgr refactoring accidentally created a cyclic reference: https://github.com/leanprover/lean/commit/e8c057f1de65917ebe3501b81b8e09a198af25ff#diff-958f55d9f5b994ecd756301253778733R279

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 08 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123433930):
```diff
diff --git a/src/library/module_mgr.cpp b/src/library/module_mgr.cpp
index c0a0cc8ec..0c961b1a2 100644
--- a/src/library/module_mgr.cpp
+++ b/src/library/module_mgr.cpp
@@ -269,6 +269,7 @@ void module_mgr::build_lean(std::shared_ptr<module_info> const & mod, name_set c
     }
     auto initial_env = m_initial_env;
+    auto id = mod->m_id;
     mod->m_result = map<module_info::parse_result>(
         get_end(snapshots),
         [=](module_parser_result const & res) {
@@ -276,7 +277,7 @@ void module_mgr::build_lean(std::shared_ptr<module_info> const & mod, name_set c
             lean_always_assert(res.m_snapshot_at_end);
             parse_res.m_loaded_module = cache_preimported_env(
-                    export_module(res.m_snapshot_at_end->m_env, mod->m_id),
+                    export_module(res.m_snapshot_at_end->m_env, id),
                     initial_env, [=] { return ldr; });
             parse_res.m_opts = res.m_snapshot_at_end->m_options;
diff --git a/src/library/tactic/tactic_state.cpp b/src/library/tactic/tactic_state.cpp
index d134ba745..5b9676729 100644
--- a/src/library/tactic/tactic_state.cpp
+++ b/src/library/tactic/tactic_state.cpp
@@ -842,11 +842,11 @@ vm_obj io_run_tactic(vm_obj const &, vm_obj const & tac, vm_obj const &) {
     tactic_state s = mk_tactic_state_for(vm.env(), vm.get_options(), "_io_run_tactic",
                                          metavar_context(), local_context(), mk_true());
     vm_obj r = invoke(tac, to_obj(s));
-    if (tactic::is_result_success(r)) {
-        return mk_io_result(tactic::get_result_value(r));
-    } else {
+    // if (tactic::is_result_success(r)) {
+    //     return mk_io_result(tactic::get_result_value(r));
+    // } else {
         return mk_io_failure("tactic failed"); // TODO(Leo): improve exception message
-    }
+    // }
 }
 unsigned tactic_user_state::alloc(vm_obj const & v) {
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 08 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123433951):
Although I still get leaks when working on the core library.  Do you have an automated test for the leak?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123436362):
@**Gabriel Ebner** Nice, now memcheck reports 0 lost! How did you even find that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123436458):
I'm using a --server file with the following content on a clean-oleaned tree
```
{"seq_num": 0, "command": "roi", "mode": "open-files", "files": [{"file_name":"library/init/core.lean", "ranges":[]}]}
{"seq_num": 0, "command": "sync", "file_name": "library/init/core.lean"}
{"seq_num": 0, "command": "sync_output"}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123437977):
[Doing 2 trivial changes to core.lean, before vs after fix](/user_uploads/3121/0YWB38Fds34rPXmERFthjEEi/pasted_image.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123437983):
The humps should signify the edits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 09 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123485667):
@**Gabriel Ebner** By the way, I found a "leak" in that we don't reset the memory pools of the main thread until the very end. But that should only contribute a few MB in the long run I suppose.


{% endraw %}
