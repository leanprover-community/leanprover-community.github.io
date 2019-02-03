---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93323Iaccidentallychangedacorefile.html
---

## Stream: [general](index.html)
### Topic: [I accidentally changed a core file](93323Iaccidentallychangedacorefile.html)

---


{% raw %}
#### [ Kenny Lau (Sep 06 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444111):
<p>I accidentally changed a core file and everything is now shit. I honestly don't know what to do.</p>

#### [ Kenny Lau (Sep 06 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444149):
<p>Do I need to rebuild Lean?</p>

#### [ Keeley Hoek (Sep 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444331):
<p>do you use elan</p>

#### [ Kenny Lau (Sep 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444344):
<p>I don't</p>

#### [ Kevin Buzzard (Sep 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444360):
<p>why not just download the binary again?</p>

#### [ Keeley Hoek (Sep 06 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444361):
<p>tears<br>
did you build it from source? download a zip distribution?</p>

#### [ Kenny Lau (Sep 06 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444469):
<p>oh nvm I did the standard trick and it worked again</p>

#### [ Kenny Lau (Sep 06 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444475):
<p>(standard trick = turning it off and on again)</p>

#### [ Kenny Lau (Sep 06 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444645):
<p>I still think something has changed</p>

#### [ Kenny Lau (Sep 06 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444710):
<p>This is what I do:</p>
<div class="codehilite"><pre><span></span>cd /c/
git clone https://github.com/leanprover/lean
cd lean
mkdir -p build/release
cd build/release
cmake -DCMAKE_BUILD_TYPE=RELEASE -G Ninja ../../src
ninja
cd /c/
git clone https://github.com/leanprover/mathlib
cd mathlib
/c/lean/bin/leanpkg build
</pre></div>

#### [ Kenny Lau (Sep 06 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133444915):
<p>I think it's alright</p>

#### [ Kevin Buzzard (Sep 06 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133445045):
<p>I think that script looks OK, I mean, it will just download a reasonable version of everything</p>

#### [ Keeley Hoek (Sep 06 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133445409):
<p>sure. if you mess up the standard library again, it is enough to just cd into the "lean" folder you already have sitting around and <code>git reset --hard HEAD</code> (and avoid the waiting)</p>

#### [ Kenny Lau (Sep 06 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133446802):
<p>do I need to restart Lean after that? <span class="user-mention" data-user-id="110111">@Keeley Hoek</span></p>

#### [ Keeley Hoek (Sep 06 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133446886):
<p>yes definitely</p>

#### [ Keeley Hoek (Sep 06 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133447053):
<p>and I guess it is best to cd into build/release and run ninja again, but not obligatory (and ninja should be very fast compared to normal)</p>

#### [ Kenny Lau (Sep 06 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20accidentally%20changed%20a%20core%20file/near/133447150):
<p>oh ok</p>


{% endraw %}
