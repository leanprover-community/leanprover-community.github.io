---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68203emscriptenbuild.html
---

## Stream: [general](index.html)
### Topic: [emscripten build](68203emscriptenbuild.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 30 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887589):
I see the emscripten situation is as stellar as ever :| .
Using the official Arch Linux build:
```
$ pacaur -Qo $(which emconfigure)
/usr/lib/emscripten/emconfigure is owned by emscripten 1.37.36-1
 $ emconfigure cmake ../../src -DCMAKE_BUILD_TYPE=Emscripten
-- Lean library will be installed at /usr/local/lib/lean
-- Disabled multi-thread support, it will not be safe to run multiple threads in parallel
-- Using standard malloc.
-- Found PythonInterp: /usr/bin/python (found version "3.6.4") 
-- git commit sha1: 17fe3decaf8ae236f0d0ff51ac8fd7f6940acdee
-- Configuring done
-- Generating done
-- Build files have been written to: /home/sebastian/projects/lean/build/emscripten
$ make
...
checking how to switch to text section... configure: error: Cannot determine text section directive
ERROR:root:Configure step failed with non-zero return code 1! Command line: ['./configure', 'CC_FOR_BUILD=gcc', 'CFLAGS=-m32 -DPIC -Oz -O3', '--host=x86_64-pc-linux-gnu', '--build=i686-pc-linux-gnu', '--disable-assembly', '--prefix=/home/sebastian/projects/lean/build/emscripten/gmp-root'] at /home/sebastian/projects/lean/build/emscripten/gmp-prefix/src/gmp
make[2]: *** [CMakeFiles/gmp.dir/build.make:109: gmp-prefix/src/gmp-stamp/gmp-configure] Error 1
make[1]: *** [CMakeFiles/Makefile2:1180: CMakeFiles/gmp.dir/all] Error 2
make: *** [Makefile:163: all] Error 2
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 30 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887631):
/cc @**Gabriel Ebner** @**Scott Morrison** @**loki der quaeler**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887638):
https://gitter.im/leanprover_public/lean_js

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887639):
(for reference)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 30 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887687):
Once we have multiplayer lean on cocalc we can forget about these headaches :video_game:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887852):
no because I want people who are idly reading my blog with no cocalc account to be able to see modern lean and mathlib doing stuff at the click of a button.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887854):
so we have one 3.4.1 headache

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887855):
but then that's it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887857):
[assuming Mario can get mathlib working with 3.4.1]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887859):
[or else the number of headaches goes up again]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 30 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125887860):
Ok, fair enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 30 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125890720):
try this:
```udiff
diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index 863f6a66d..6163d9b32 100644
--- a/src/CMakeLists.txt
+++ b/src/CMakeLists.txt
@@ -287,7 +287,7 @@ if (EMSCRIPTEN)
             URL https://gmplib.org/download/gmp/gmp-6.1.1.tar.bz2
             URL_HASH SHA256=a8109865f2893f1373b0a8ed5ff7429de8db696fc451b1036bd7bdf95bbeffd6
             BUILD_IN_SOURCE 1
-            CONFIGURE_COMMAND emconfigure ./configure "CC_FOR_BUILD=gcc" "CFLAGS=-m32 -DPIC ${CFLAGS_EMSCRIPTEN}" --host=x86_64-pc-linux-gnu --build=i686-pc-linux-gnu --disable-assembly --prefix=${gmp_install_prefix}
+           CONFIGURE_COMMAND emconfigure ./configure "CC_FOR_BUILD=gcc" "CCAS=gcc -c" "CFLAGS=-m32 -DPIC ${CFLAGS_EMSCRIPTEN}" --host=x86_64-pc-linux-gnu --build=i686-pc-linux-gnu --disable-assembly --prefix=${gmp_install_prefix}
             BUILD_COMMAND emmake make -j4
             INSTALL_COMMAND make install
     )
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 30 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emscripten%20build/near/125891597):
@**Gabriel Ebner** Seems to work, thanks!

