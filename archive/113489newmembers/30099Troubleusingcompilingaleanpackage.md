---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/30099Troubleusingcompilingaleanpackage.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Trouble using compiling a lean package](https://leanprover-community.github.io/archive/113489newmembers/30099Troubleusingcompilingaleanpackage.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Calle Sönne (Nov 17 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147882741):
<p>Im trying compile a leanpackage. I assume the way you do is by running leanpkg build in the folder where leanpkg.toml is located. However doing that gives me the following error:</p>
<p>error: override toolchain 'master' is not installed<br>
info: caused by: the toolchain file at '/home/calle/herstein/leanpkg.toml' specifies an uninstalled toolchain</p>
<p>I have tried running leanpkg build, leanpkg init, leanpkg .configure. All of them give the same error (even just running "lean" within the folder gives same error). Other than this lean is working fine and I can use/work on other packages.</p>
<p>Here is the leanpkg.toml file if that explains anything:</p>
<p>[package]                                                                                                                                                                                <br>
name = "herstein"<br>
version = "0.1"<br>
lean_version = "master"<br>
path = "src"</p>
<p>[dependencies]<br>
mathlib = {git = "<a href="https://github.com/leanprover/mathlib" target="_blank" title="https://github.com/leanprover/mathlib">https://github.com/leanprover/mathlib</a>", rev = "c7c0d2a1bb2f0ba353bbcb0510352a25c80fc186"}</p>

#### [ Johan Commelin (Nov 17 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147882884):
<p>Hi <span class="user-mention" data-user-id="132603">@Calle Sönne</span> Are you using <code>elan</code>? Which OS are you on?</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885359):
<p>He is using <code>elan</code>, it's on Windows, he showed me this on Thursday and I had no idea. Just running <code>leanpkg</code> by itself with no parameters gave this error</p>

#### [ Kenny Lau (Nov 17 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885375):
<p>and lean is funded by microsoft lmao</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885432):
<p>I'm funded by Imperial College but that doesn't mean that the "official" website they insist on generating for me bears any relation to what I have been doing over the last 10 years. Big organizations are complex things Kenny.</p>

#### [ Kenny Lau (Nov 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885448):
<p>what, <a href="https://www.imperial.ac.uk/people/k.buzzard" target="_blank" title="https://www.imperial.ac.uk/people/k.buzzard">this one</a>?</p>

#### [ Calle Sönne (Nov 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885540):
<p>Im using linux (Manjaro)</p>

#### [ Reid Barton (Nov 17 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885596):
<p>Is <code>lean_version = "master"</code> supposed to work?</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885621):
<blockquote>
<p>what, <a href="https://www.imperial.ac.uk/people/k.buzzard" target="_blank" title="https://www.imperial.ac.uk/people/k.buzzard">this one</a>?</p>
</blockquote>
<p>Yes. It's auto-generated you know! The script was written in about 2004.</p>

#### [ Calle Sönne (Nov 17 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885626):
<p>Im using elan version 0.7.1 and lean version 3.4.2 nightly-2018-11-13</p>

#### [ Reid Barton (Nov 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885670):
<p>I would put one of those version numbers in the <code>lean_version</code> field then.</p>

#### [ Reid Barton (Nov 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885673):
<p>elan uses that field to decide which lean to invoke and I don't think it understands "master"</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885676):
<p>Try <code>lean_version = "nightly-2018-11-13"</code></p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885683):
<p>(in leanpkg.toml)</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885737):
<p>I see, so this is the issue. I've never used elan and I didn't understand the error. The job of elan is to ensure that the version of Lean coincides with the version used by the package. This will be an issue in future when Lean 4 hits. But it never bites me now because every package I know of uses Lean 3.4.1 or some nightly after 3.4.1 which is basically the same as 3.4.1 but with some minor irrelevant bugfix</p>

#### [ Calle Sönne (Nov 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885738):
<p>That did it :) Thank you</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trouble%20using%20compiling%20a%20lean%20package/near/147885740):
<p>:-)</p>


{% endraw %}
