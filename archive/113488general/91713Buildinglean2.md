---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91713Buildinglean2.html
---

## Stream: [general](index.html)
### Topic: [Building lean2](91713Buildinglean2.html)

---


{% raw %}
#### [ Ali Caglayan (Aug 01 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130742054):
Is anyone able to build lean2 on their machine? I've tried twice already and its always failed. I am currently trying a third time. I am building on Ubuntu bionic

#### [ Ali Caglayan (Aug 01 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130742067):
Infact I've tried a third time and still no luck

#### [ Ali Caglayan (Aug 01 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130742119):
Traceback (most recent call last):
  File "/home/ali/lean2/src/../bin/linja", line 758, in <module>
    sys.exit(main())
  File "/home/ali/lean2/src/../bin/linja", line 743, in main
    return call_ninja(args)
  File "/home/ali/lean2/src/../bin/linja", line 517, in call_ninja
    proc = subprocess.Popen([g_ninja_path] + ninja_option + targets, stdout=proc_out, stderr=proc_err)
  File "/usr/lib/python2.7/subprocess.py", line 394, in __init__
    errread, errwrite)
  File "/usr/lib/python2.7/subprocess.py", line 1047, in _execute_child
    raise child_exception
OSError: [Errno 8] Exec format error
CMakeFiles/standard_lib.dir/build.make:57: recipe for target 'CMakeFiles/standard_lib' failed
make[2]: *** [CMakeFiles/standard_lib] Error 1
CMakeFiles/Makefile2:323: recipe for target 'CMakeFiles/standard_lib.dir/all' failed
make[1]: *** [CMakeFiles/standard_lib.dir/all] Error 2
Makefile:162: recipe for target 'all' failed
make: *** [all] Error 2

#### [ Ali Caglayan (Aug 01 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130742145):
This is a fresh clone of lean2 using the build/release cmake

#### [ Sebastian Ullrich (Aug 01 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130743827):
@**Ali Caglayan** I don't remember much about building Lean 2, but have you installed ninja? Can you call it from a command line, like say `ninja --version`?

#### [ Ali Caglayan (Aug 01 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130743901):
@**Sebastian Ullrich**  I was hoping not to install ninja as I don't exactly have a lot of space.

#### [ Sebastian Ullrich (Aug 01 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130743931):
Lean 2 depends on ninja

#### [ Ali Caglayan (Aug 01 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130743954):
In the install instructions it said it was optional. I will try this again with more room.

#### [ Ali Caglayan (Aug 01 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130743973):
See https://github.com/leanprover/lean/blob/master/doc/make/ubuntu-16.04.md

#### [ Sebastian Ullrich (Aug 02 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130744505):
Those are for Lean 3. I think there is some crazy code in Lean 2 that downloads ninja if you don't have it yet, but as you can see, it will try to call ninja in the end. Maybe you can make Lean work without linja, which is a wrapper around ninja for Lean, but I don't remember enough details about it.

#### [ Ali Caglayan (Aug 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130746377):
I have managed to build it now. The whole problem was no having ninja.

#### [ Ali Caglayan (Aug 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Building%20lean2/near/130746386):
I guess I can uninstall ninja now its built


{% endraw %}
