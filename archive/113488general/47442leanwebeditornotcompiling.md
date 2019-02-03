---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47442leanwebeditornotcompiling.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lean-web-editor not compiling?](https://leanprover-community.github.io/archive/113488general/47442leanwebeditornotcompiling.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 03 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124551978):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>, I'm trying to build the lean-web-editor from scratch, and running into a problem.</p>

#### [ Scott Morrison (Apr 03 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124552025):
<p>When I try</p>
<div class="codehilite"><pre><span></span>mkdir -p build/release
pushd build/release
emconfigure cmake ../../src/ -DCMAKE_BUILD_TYPE=Emscripten
make
</pre></div>

#### [ Scott Morrison (Apr 03 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124552038):
<p>I get the following error: <a href="https://gist.github.com/semorrison/5145439a8e501380dd102edf50ea67c8" target="_blank" title="https://gist.github.com/semorrison/5145439a8e501380dd102edf50ea67c8">https://gist.github.com/semorrison/5145439a8e501380dd102edf50ea67c8</a></p>

#### [ Gabriel Ebner (Apr 03 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124566399):
<p>I don't think anyone has ever tried building the emscripten version on macOS.  We even hardcode Linux on x86_64 as the host platform: <a href="https://github.com/leanprover/lean/blob/96c932ab210ac4e71ad3439d128fb4f75b314e1e/src/CMakeLists.txt#L290" target="_blank" title="https://github.com/leanprover/lean/blob/96c932ab210ac4e71ad3439d128fb4f75b314e1e/src/CMakeLists.txt#L290">https://github.com/leanprover/lean/blob/96c932ab210ac4e71ad3439d128fb4f75b314e1e/src/CMakeLists.txt#L290</a></p>

#### [ Gabriel Ebner (Apr 03 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124566406):
<p>You can try to look at the <code>config.log</code> file, which should show the exact error message.</p>

#### [ Gabriel Ebner (Apr 03 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124566407):
<p>But I'd suggest to do the emscripten build in docker or a VM instead.</p>

#### [ Sebastian Ullrich (Apr 03 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-web-editor%20not%20compiling%3F/near/124567096):
<p>And feel free to set up a Travis script <span class="emoji emoji-1f604" title="smile">:smile:</span></p>


{% endraw %}
