---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80964mathliboleanfiles.html
---

## Stream: [general](index.html)
### Topic: [mathlib olean files](80964mathliboleanfiles.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 22 2019 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626057):
<p>I just upgraded to Lean 3.4.2 and mathlib master. I've got everything compiling. <span class="user-mention" data-user-id="110044">@Chris Hughes</span>  and <span class="user-mention" data-user-id="110064">@Kenny Lau</span> I know it's a pain for you to compile mathlib sometimes. Here is a link: <a href="http://wwwf.imperial.ac.uk/~buzzard/xena/mathlib.tar" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/xena/mathlib.tar">mathlib.tar</a>  . I packed up mathlib (including all the .olean files) into a "tarball" (using POSIX tar so file timestamps should be to the nearest nanosecond or whatever). Q1 : can you untar this file back into a mathlib directory? And Q2: if you can, what are the timestamps like? For me, if I look in <code>src/topology</code> then I see <code>basic.lean</code> was created at 16:12 today and <code>basic.olean</code> at 16:49, so Lean knows that I didn't edit <code>basic.lean</code>after I created <code>basic.olean</code>. I took the tarball and untarred it on another unix computer and the timestamps survived. If by the time these files get to you the timestamps of <code>basic.lean</code> and <code>basic.olean</code> are "the time it is now", then the experiment has failed (do files have timestamps in Windows? I know nothing!) because Lean might decide it's time to recompile basic.lean anyway. But if the times are different then maybe this saves you some time compiling mathlib.</p>

#### [ Patrick Massot (Jan 22 2019 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626147):
<p><code>&lt;|&gt;</code> install Linux</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626177):
<p>Sure, but I'm sure you know that for some people this simply isn't an option.</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626241):
<p>I'm not sure how to get linux running on a Microsoft Surface Pro, for example.</p>

#### [ Patrick Massot (Jan 22 2019 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626256):
<p>I think it's about time Chris and Kenny leave that category of people</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626289):
<p>Yeah but you have a job</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626302):
<p>They are poor students :-/</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626391):
<p>Apparently winzip can extract tarballs. I just don't know what it does with the timestamps. My understanding is that if all the timestamps come out the same then we have to think again. But even this might not be unsolvable.</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626410):
<p>Imagine if I just zipped up the .olean files and they could somehow unzip them into a mathlib directory.</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626456):
<p>Then the fact that they're timestamped "now" is to our advantage.</p>

#### [ Patrick Massot (Jan 22 2019 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626502):
<p>How can poor students afford buying Windows?</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626598):
<p>I think they get their parents' old laptops :-/</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626652):
<p>They might need Windows for other things. My 16 year old son wants to run software like Unity to develop games and this is Windows only, so we are forced to have a Windows machine at home.</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626729):
<p>All I'm saying is that "switch OS" is of course a solution but it might not be a solution that works for everyone. If we could figure out a way to save my students some time then this would be advantageous for me.</p>

#### [ Patrick Massot (Jan 22 2019 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626803):
<p>Then you could test installing mathlib on a windows machine</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626829):
<p>yes, but it's easier for them to test it :-)</p>

#### [ Kevin Buzzard (Jan 22 2019 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156626901):
<p>anyway, I'm still at work! I just finished talking to Ramon, who has actually started on schemes :D</p>

#### [ Kevin Buzzard (Jan 22 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20olean%20files/near/156638858):
<p>(deleted)</p>


{% endraw %}
