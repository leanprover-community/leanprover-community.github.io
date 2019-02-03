---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46061installingmathlibglobally.html
---

## Stream: [general](index.html)
### Topic: [installing mathlib globally](46061installingmathlibglobally.html)

---


{% raw %}
#### [ Kevin Buzzard (Jun 25 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128610501):
<p>Cocalc want to install one mathlib globally. I think Sebastian Ullrich once told me that there was no documentation for <code>leanpkg.path</code> because this was not a file that an end user was ever supposed to mess with. I am assuming <code>builtin_path</code> points to where the core lean library is. I am assuming that there's no file with the same name in Lean and mathlib, so I guess in theory they could do the slightly horrible-sounding thing of dumping all of mathlib in the core lean directory. But actually I am a bit confused about what is really reading leanpkg.path. Oh -- is this something the lean plugin does in VS Code?</p>

#### [ Gabriel Ebner (Jun 25 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128614273):
<p>My suggestion would be to create a dummy project with all of the suggested dependencies (e.g. mathlib) listed in the leanpkg.toml file.  Then you can run <code>leanpkg build</code> as usual to create the olean files.  To check files you then run <code>lean my_file.lean</code> or <code>lean --server</code> <em>from that directory</em>, this will pick up the correct leanpkg.path file.  I believe this is the solution that is easiest to maintain.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615134):
<p>I think CoCalc wants to have 1 install of mathlib for &gt;1000 users.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615169):
<p>So, I imagine an install of mathlib in <code>/opt/lean/mathlib/</code>, and then users can add that path as a dependency to their projects.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615252):
<p>Even better (and this is what Kevin is saying, I think) would be if Lean could automatically pick up mathlib, without users even having to specify it as a dependency. So Lean should look in <code>/opt/lean/</code> or something like that, and automatically make all those libs available to all users.</p>

#### [ Gabriel Ebner (Jun 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615345):
<p>Does cocalc support multiple files (that can include each other)?</p>

#### [ Johan Commelin (Jun 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615355):
<p>What do you mean with that? CoCalc is just a website.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615363):
<p>With a gigantic cloud (i.e. server park) behind it.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615380):
<p>You create an account (or login with Github) and you get an online python/LaTeX/etc environment.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615385):
<p>(Even shell access!)</p>

#### [ Johan Commelin (Jun 25 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615390):
<p>And you can collaboratively edit those files.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615436):
<p>So it is quite nice for typing up a LaTeX document, or doing some scientific computing in python/Sage...</p>

#### [ Gabriel Ebner (Jun 25 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615445):
<p>Ah, so you can have multiple files and directories and so on.  This was not really clear from the first look.  I only saw single jupyter notebooks.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615452):
<p>No, you basically get a free linux account on a cloud server, together with a nice web-frontend</p>

#### [ Johan Commelin (Jun 25 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615478):
<p>So, if we want realtime online collaboration for Lean, then we should lend these guys a helping hand!</p>

#### [ Gabriel Ebner (Jun 25 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128615533):
<p>I don't think we should promote completely non-standard configurations on cocalc.  It makes the transition between cocalc and your personal machine unnecessarily hard.  One option is to have a script that creates a standard <code>leanpkg.toml</code>, but then symlinks the <code>_target/mathlib</code> directory from a read-only compiled version in <code>/opt/lean/mathlib</code> or sth like that.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128616386):
<p>Yes, that might be an idea.</p>

#### [ Johan Commelin (Jun 25 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128616437):
<p>Maybe even <code>/opt/lean/mathlib/v2018_summer/</code></p>

#### [ Johan Commelin (Jun 25 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128616442):
<p>So that we don't get lots of users complaining that their stuff ain't compiling after an upgrade.</p>

#### [ Kevin Buzzard (Jun 25 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128618868):
<blockquote>
<p>I don't think we should promote completely non-standard configurations on cocalc.  It makes the transition between cocalc and your personal machine unnecessarily hard.  </p>
</blockquote>
<p>This will be for kids who want to do their homework in Lean but don't want to go through the hassle of installing it; I am not 100% sure that the accounts can access the internet, so I am not sure how well leanpkg will work.</p>

#### [ Johan Commelin (Jun 25 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/installing%20mathlib%20globally/near/128619714):
<p>The default accounts on CoCalc do not have internet access</p>


{% endraw %}
