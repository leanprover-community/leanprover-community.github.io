---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91011GetoleanfileswithoutelanonWin10.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Get olean files without elan on Win10](https://leanprover-community.github.io/archive/113488general/91011GetoleanfileswithoutelanonWin10.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 27 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136602966):
<p>I'd like to download updates to mathlib manually from github, then produce the olean files. How can I do this? I saw <a href="https://github.com/leanprover/lean/blob/master/doc/make/msvc.md" target="_blank" title="https://github.com/leanprover/lean/blob/master/doc/make/msvc.md">these</a> instructions, but apparently they aren't compatible with VS2018.</p>

#### [ Kevin Buzzard (Oct 27 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136604656):
<p>I <em>think</em> that <code>elan</code> is supposed to do all of this for you. But if you choose not to use it for some reason, then you can use <code>leanpkg</code> to build the <code>.olean</code> files. Maybe this old page <a href="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/" target="_blank" title="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/">https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/</a> helps you? But I think that users are now encouraged to use <code>elan</code></p>

#### [ Chris Hughes (Oct 27 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605169):
<p>elan still doesn't work with spaces in user names.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 27 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605314):
<blockquote>
<p>elan still doesn't work with spaces in user names.</p>
</blockquote>
<p>Wait, which usernames?</p>

#### [ Kenny Lau (Oct 27 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605377):
<p>your username</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605386):
<blockquote>
<p>your username</p>
</blockquote>
<p>Yeah, I mean -- the Windows username? For file paths and stuff?</p>

#### [ Kenny Lau (Oct 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605389):
<p>yes</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605391):
<p>Ok, that's not a problem, then.</p>

#### [ Kevin Buzzard (Oct 27 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Get%20olean%20files%20without%20elan%20on%20Win10/near/136605739):
<p>Yes, I think the issue is exactly with file paths. What's even more frustrating is that apparently the problem has been fixed, but the PR has not yet been accepted (and might never be, I guess, until Lean 4 comes out next year)</p>


{% endraw %}
