---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79716memoryleakinserver.html
---

## Stream: [general](index.html)
### Topic: [memory leak in server?](79716memoryleakinserver.html)

---


{% raw %}
#### [ Kevin Buzzard (Feb 27 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017339):
<div class="codehilite"><pre><span></span>invalid import: data.set.basic
excessive memory consumption detected at &#39;replace&#39; (potential solution: increase memory consumption threshold)
</pre></div>

#### [ Kevin Buzzard (Feb 27 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017352):
<p>Why do those happen?</p>

#### [ Chris Hughes (Feb 27 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017356):
<p>restart lean. That sort of thing happend to me all the time lately</p>

#### [ Kevin Buzzard (Feb 27 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017359):
<p>I feel like it's happening more and more often to me too at the minute. Is Lean a bit less stable than it was or something?</p>

#### [ Kevin Buzzard (Feb 27 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017400):
<p>I am trying to define a structure sheaf, I could do without random errors :-)</p>

#### [ Chris Hughes (Feb 27 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123017464):
<p>Also simp randomly fails, and then succeeds without me doing anything.</p>

#### [ Kevin Buzzard (Feb 27 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123019223):
<p>Yeah we got it working in the end.</p>

#### [ Kenny Lau (Feb 27 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123019247):
<p>nice</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123032936):
<p>I wanted to knock up a quick "proof by induction" example for pedagogical reasons and I choose to prove that the sum of the first n integers (or first n+1 integers for you CS guys) equalled n(n+1)/2.</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123032996):
<p>I had to decide on my infrastructure so I went for list.sum (list.range (succ n))</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033010):
<p>but then I realised that to apply the inductive step I needed some result of the form "the sum from 0 to n+1 of f(i) equals (the sum from 0 to n of f(i)) + f(n+1)"</p>

#### [ Kevin Buzzard (Feb 27 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033015):
<p>and I couldn't spot this immediately in list, which made me wonder whether I was using the wrong inductive type to do this.</p>

#### [ Gabriel Ebner (Feb 27 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033166):
<p>I also get the feeling that this issue got worse.  It seems like there is a new memory leak in server mode.  <span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> Any ideas?</p>

#### [ Simon Hudon (Feb 27 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033171):
<p>(moving to (no topic))</p>

#### [ Sebastian Ullrich (Feb 27 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033762):
<p>It's certainly annoying. Not sure how to debug something like this - first find a test case like a script doing trivial edits, confirm the issue, and then...?</p>

#### [ Gabriel Ebner (Feb 27 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033917):
<p>The "human test script" that I used was: open default.lean, change something in init/core.lean, go back to default.lean, repeat.  Yes, debugging this is not easy.  Since this seems to be a regression, we can try to bisect it.</p>

#### [ Gabriel Ebner (Feb 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033931):
<p>Last time we had such an issue, I spent hours in valgrind+gdb, chasing pointers to see which data is alive at the moment.  Unfortunately none of the memory issues were real leaks in the past, the memory was always reachable via caches/etc.</p>

#### [ Mario Carneiro (Feb 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123033988):
<p>What about opportunistic cache reclaiming?</p>

#### [ Gabriel Ebner (Feb 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123034039):
<p>We kill our child threads if they are idle for a few milliseconds, and their caches die with them.  This was sufficient in the past.</p>

#### [ Sebastian Ullrich (Feb 27 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123034329):
<p><span class="user-mention" data-user-email="gebner@gebner.org" data-user-id="110043">@Gabriel Ebner</span> Have you ever used <a href="http://valgrind.org/docs/manual/ms-manual.html" target="_blank" title="http://valgrind.org/docs/manual/ms-manual.html">massif</a> before? Maybe I should give it a try.</p>

#### [ Gabriel Ebner (Feb 27 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123035399):
<p>I don't think so.  I mainly used the memcheck monitor commands.</p>

#### [ Sebastian Ullrich (Mar 07 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123411331):
<p><span class="user-mention" data-user-email="gebner@gebner.org" data-user-id="110043">@Gabriel Ebner</span> There seems to be a shared_ptr cycle, assuming valgrind isn't lying:</p>
<div class="codehilite"><pre><span></span>==13508== 4,260,044 (272 direct, 4,259,772 indirect) bytes in 1 blocks are definitely lost in loss record 13,808 of 13,808
==13508==    at 0x4C2E0EF: operator new(unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==13508==    by 0xC0FFA3: __gnu_cxx::new_allocator&lt;std::_Sp_counted_ptr_inplace&lt;lean::module_info, std::allocator&lt;lean::module_info&gt;, (__gnu_cxx::_Lock_policy)2&gt; &gt;::allocate(unsigned long, void const*) (new_allocator.h:104)
...
==13508==    by 0xDBE2A8: std::shared_ptr&lt;lean::module_info&gt; std::make_shared&lt;lean::module_info, std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt;, lean::module_src, long&amp;&gt;(std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt;&amp;&amp;, lean::module_src&amp;&amp;, long&amp;) (shared_ptr.h:636)
==13508==    by 0xDBA2BD: lean::fs_module_vfs::load_module(std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, bool) (module_mgr.cpp:446)
==13508==    by 0xBF4BEE: lean::server::load_module(std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, bool) (server.cpp:699)
==13508==    by 0xDB70AB: lean::module_mgr::build_module(std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, bool, lean::rb_tree&lt;lean::name, lean::name_quick_cmp&gt;) (module_mgr.cpp:157)
</pre></div>

#### [ Gabriel Ebner (Mar 08 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123433929):
<p><span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> I think the module_mgr refactoring accidentally created a cyclic reference: <a href="https://github.com/leanprover/lean/commit/e8c057f1de65917ebe3501b81b8e09a198af25ff#diff-958f55d9f5b994ecd756301253778733R279" target="_blank" title="https://github.com/leanprover/lean/commit/e8c057f1de65917ebe3501b81b8e09a198af25ff#diff-958f55d9f5b994ecd756301253778733R279">https://github.com/leanprover/lean/commit/e8c057f1de65917ebe3501b81b8e09a198af25ff#diff-958f55d9f5b994ecd756301253778733R279</a></p>

#### [ Gabriel Ebner (Mar 08 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123433930):
<div class="codehilite"><pre><span></span><span class="gh">diff --git a/src/library/module_mgr.cpp b/src/library/module_mgr.cpp</span>
<span class="gh">index c0a0cc8ec..0c961b1a2 100644</span>
<span class="gd">--- a/src/library/module_mgr.cpp</span>
<span class="gi">+++ b/src/library/module_mgr.cpp</span>
<span class="gu">@@ -269,6 +269,7 @@ void module_mgr::build_lean(std::shared_ptr&lt;module_info&gt; const &amp; mod, name_set c</span>
     }
     auto initial_env = m_initial_env;
<span class="gi">+    auto id = mod-&gt;m_id;</span>
     mod-&gt;m_result = map&lt;module_info::parse_result&gt;(
         get_end(snapshots),
         [=](module_parser_result const &amp; res) {
<span class="gu">@@ -276,7 +277,7 @@ void module_mgr::build_lean(std::shared_ptr&lt;module_info&gt; const &amp; mod, name_set c</span>
             lean_always_assert(res.m_snapshot_at_end);
             parse_res.m_loaded_module = cache_preimported_env(
<span class="gd">-                    export_module(res.m_snapshot_at_end-&gt;m_env, mod-&gt;m_id),</span>
<span class="gi">+                    export_module(res.m_snapshot_at_end-&gt;m_env, id),</span>
                     initial_env, [=] { return ldr; });
             parse_res.m_opts = res.m_snapshot_at_end-&gt;m_options;
<span class="gh">diff --git a/src/library/tactic/tactic_state.cpp b/src/library/tactic/tactic_state.cpp</span>
<span class="gh">index d134ba745..5b9676729 100644</span>
<span class="gd">--- a/src/library/tactic/tactic_state.cpp</span>
<span class="gi">+++ b/src/library/tactic/tactic_state.cpp</span>
<span class="gu">@@ -842,11 +842,11 @@ vm_obj io_run_tactic(vm_obj const &amp;, vm_obj const &amp; tac, vm_obj const &amp;) {</span>
     tactic_state s = mk_tactic_state_for(vm.env(), vm.get_options(), &quot;_io_run_tactic&quot;,
                                          metavar_context(), local_context(), mk_true());
     vm_obj r = invoke(tac, to_obj(s));
<span class="gd">-    if (tactic::is_result_success(r)) {</span>
<span class="gd">-        return mk_io_result(tactic::get_result_value(r));</span>
<span class="gd">-    } else {</span>
<span class="gi">+    // if (tactic::is_result_success(r)) {</span>
<span class="gi">+    //     return mk_io_result(tactic::get_result_value(r));</span>
<span class="gi">+    // } else {</span>
         return mk_io_failure(&quot;tactic failed&quot;); // TODO(Leo): improve exception message
<span class="gd">-    }</span>
<span class="gi">+    // }</span>
 }
 unsigned tactic_user_state::alloc(vm_obj const &amp; v) {
</pre></div>

#### [ Gabriel Ebner (Mar 08 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123433951):
<p>Although I still get leaks when working on the core library.  Do you have an automated test for the leak?</p>

#### [ Sebastian Ullrich (Mar 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123436362):
<p><span class="user-mention" data-user-email="gebner@gebner.org" data-user-id="110043">@Gabriel Ebner</span> Nice, now memcheck reports 0 lost! How did you even find that?</p>

#### [ Sebastian Ullrich (Mar 08 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123436458):
<p>I'm using a --server file with the following content on a clean-oleaned tree</p>
<div class="codehilite"><pre><span></span>{&quot;seq_num&quot;: 0, &quot;command&quot;: &quot;roi&quot;, &quot;mode&quot;: &quot;open-files&quot;, &quot;files&quot;: [{&quot;file_name&quot;:&quot;library/init/core.lean&quot;, &quot;ranges&quot;:[]}]}
{&quot;seq_num&quot;: 0, &quot;command&quot;: &quot;sync&quot;, &quot;file_name&quot;: &quot;library/init/core.lean&quot;}
{&quot;seq_num&quot;: 0, &quot;command&quot;: &quot;sync_output&quot;}
</pre></div>

#### [ Sebastian Ullrich (Mar 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123437977):
<p><a href="/user_uploads/3121/0YWB38Fds34rPXmERFthjEEi/pasted_image.png" target="_blank" title="pasted_image.png">Doing 2 trivial changes to core.lean, before vs after fix</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/0YWB38Fds34rPXmERFthjEEi/pasted_image.png" target="_blank" title="Doing 2 trivial changes to core.lean, before vs after fix"><img src="/user_uploads/3121/0YWB38Fds34rPXmERFthjEEi/pasted_image.png"></a></div>

#### [ Sebastian Ullrich (Mar 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123437983):
<p>The humps should signify the edits</p>

#### [ Sebastian Ullrich (Mar 09 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/memory%20leak%20in%20server%3F/near/123485667):
<p><span class="user-mention" data-user-email="gebner@gebner.org" data-user-id="110043">@Gabriel Ebner</span> By the way, I found a "leak" in that we don't reset the memory pools of the main thread until the very end. But that should only contribute a few MB in the long run I suppose.</p>


{% endraw %}
