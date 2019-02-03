---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68203emscriptenbuild.html
---

## Stream: [general](index.html)
### Topic: [emscripten build](68203emscriptenbuild.html)

---


{% raw %}
#### [ Sebastian Ullrich (Apr 30 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887589):
<p>I see the emscripten situation is as stellar as ever :| .<br>
Using the official Arch Linux build:</p>
<div class="codehilite"><pre><span></span>$ pacaur -Qo $(which emconfigure)
/usr/lib/emscripten/emconfigure is owned by emscripten 1.37.36-1
 $ emconfigure cmake ../../src -DCMAKE_BUILD_TYPE=Emscripten
-- Lean library will be installed at /usr/local/lib/lean
-- Disabled multi-thread support, it will not be safe to run multiple threads in parallel
-- Using standard malloc.
-- Found PythonInterp: /usr/bin/python (found version &quot;3.6.4&quot;)
-- git commit sha1: 17fe3decaf8ae236f0d0ff51ac8fd7f6940acdee
-- Configuring done
-- Generating done
-- Build files have been written to: /home/sebastian/projects/lean/build/emscripten
$ make
...
checking how to switch to text section... configure: error: Cannot determine text section directive
ERROR:root:Configure step failed with non-zero return code 1! Command line: [&#39;./configure&#39;, &#39;CC_FOR_BUILD=gcc&#39;, &#39;CFLAGS=-m32 -DPIC -Oz -O3&#39;, &#39;--host=x86_64-pc-linux-gnu&#39;, &#39;--build=i686-pc-linux-gnu&#39;, &#39;--disable-assembly&#39;, &#39;--prefix=/home/sebastian/projects/lean/build/emscripten/gmp-root&#39;] at /home/sebastian/projects/lean/build/emscripten/gmp-prefix/src/gmp
make[2]: *** [CMakeFiles/gmp.dir/build.make:109: gmp-prefix/src/gmp-stamp/gmp-configure] Error 1
make[1]: *** [CMakeFiles/Makefile2:1180: CMakeFiles/gmp.dir/all] Error 2
make: *** [Makefile:163: all] Error 2
</pre></div>

#### [ Sebastian Ullrich (Apr 30 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887631):
<p>/cc <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> <span class="user-mention" data-user-id="110524">@Scott Morrison</span> <span class="user-mention" data-user-id="110066">@loki der quaeler</span></p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887638):
<p><a href="https://gitter.im/leanprover_public/lean_js" target="_blank" title="https://gitter.im/leanprover_public/lean_js">https://gitter.im/leanprover_public/lean_js</a></p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887639):
<p>(for reference)</p>

#### [ Johan Commelin (Apr 30 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887687):
<p>Once we have multiplayer lean on cocalc we can forget about these headaches <span class="emoji emoji-1f3ae" title="video game">:video_game:</span></p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887852):
<p>no because I want people who are idly reading my blog with no cocalc account to be able to see modern lean and mathlib doing stuff at the click of a button.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887854):
<p>so we have one 3.4.1 headache</p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887855):
<p>but then that's it</p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887857):
<p>[assuming Mario can get mathlib working with 3.4.1]</p>

#### [ Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887859):
<p>[or else the number of headaches goes up again]</p>

#### [ Johan Commelin (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887860):
<p>Ok, fair enough</p>

#### [ Gabriel Ebner (Apr 30 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125890720):
<p>try this:</p>
<div class="codehilite"><pre><span></span><span class="gh">diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt</span>
<span class="gh">index 863f6a66d..6163d9b32 100644</span>
<span class="gd">--- a/src/CMakeLists.txt</span>
<span class="gi">+++ b/src/CMakeLists.txt</span>
<span class="gu">@@ -287,7 +287,7 @@ if (EMSCRIPTEN)</span>
             URL https://gmplib.org/download/gmp/gmp-6.1.1.tar.bz2
             URL_HASH SHA256=a8109865f2893f1373b0a8ed5ff7429de8db696fc451b1036bd7bdf95bbeffd6
             BUILD_IN_SOURCE 1
<span class="gd">-            CONFIGURE_COMMAND emconfigure ./configure &quot;CC_FOR_BUILD=gcc&quot; &quot;CFLAGS=-m32 -DPIC ${CFLAGS_EMSCRIPTEN}&quot; --host=x86_64-pc-linux-gnu --build=i686-pc-linux-gnu --disable-assembly --prefix=${gmp_install_prefix}</span>
<span class="gi">+           CONFIGURE_COMMAND emconfigure ./configure &quot;CC_FOR_BUILD=gcc&quot; &quot;CCAS=gcc -c&quot; &quot;CFLAGS=-m32 -DPIC ${CFLAGS_EMSCRIPTEN}&quot; --host=x86_64-pc-linux-gnu --build=i686-pc-linux-gnu --disable-assembly --prefix=${gmp_install_prefix}</span>
             BUILD_COMMAND emmake make -j4
             INSTALL_COMMAND make install
     )
</pre></div>

#### [ Sebastian Ullrich (Apr 30 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125891597):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Seems to work, thanks!</p>


{% endraw %}
