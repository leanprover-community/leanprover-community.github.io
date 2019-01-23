---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47442leanwebeditornotcompiling.html
---

## Stream: [general](index.html)
### Topic: [lean-web-editor not compiling?](47442leanwebeditornotcompiling.html)

---


{% raw %}
#### [ Scott Morrison (Apr 03 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124551978):
@**Gabriel Ebner**, I'm trying to build the lean-web-editor from scratch, and running into a problem.

#### [ Scott Morrison (Apr 03 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124552025):
When I try
````
mkdir -p build/release
pushd build/release
emconfigure cmake ../../src/ -DCMAKE_BUILD_TYPE=Emscripten
make
````

#### [ Scott Morrison (Apr 03 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124552038):
I get the following error: https://gist.github.com/semorrison/5145439a8e501380dd102edf50ea67c8

#### [ Gabriel Ebner (Apr 03 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124566399):
I don't think anyone has ever tried building the emscripten version on macOS.  We even hardcode Linux on x86_64 as the host platform: https://github.com/leanprover/lean/blob/96c932ab210ac4e71ad3439d128fb4f75b314e1e/src/CMakeLists.txt#L290

#### [ Gabriel Ebner (Apr 03 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124566406):
You can try to look at the `config.log` file, which should show the exact error message.

#### [ Gabriel Ebner (Apr 03 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124566407):
But I'd suggest to do the emscripten build in docker or a VM instead.

#### [ Sebastian Ullrich (Apr 03 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124567096):
And feel free to set up a Travis script :smile:


{% endraw %}
