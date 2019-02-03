---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27349Teachingsetup.html
---

## Stream: [general](index.html)
### Topic: [Teaching setup](27349Teachingsetup.html)

---


{% raw %}
#### [ Patrick Massot (Jan 19 2019 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20setup/near/156440184):
<p>For people interested in using Lean for teaching, here are some news about my setup.  I'll use Lean on students in the maths department computer labs. I don't have root access on these machines, but I have easy access to the system admins who can install stuff. The computers run Ubuntu 18.04 directly from their hard drive but admins can easily run commands simultaneously on all computers (provided they are switched on). Of course they prefer to install stuff from the official repositories, but they are ready to install packages provided by me. Of course they don't want to give me access to the students home directories. I could tell the students to install Lean in their home directory, but I'd prefer avoiding losing time, especially compiling mathlib. And I absolutely don't want them to have write access to mathlib, jump to definition, modify something by accident and have everything recompiling or broken. So I created two deb packages. The first one installs Lean by putting in <code>/usr/bin/</code> the content of Lean's <code>bin</code> folder, and in <code>/usr/lib/</code> the content of Lean's <code>lib</code> folder. I don't put the <code>include</code> folder anywhere. The second package is <code>lean-mathlib</code> which copies in <code>/usr/lib/lean-mathlib/</code> the <code>leanpkg.path</code>, <code> leanpkg.toml</code> and  <code>src</code> from compiled mathlib. I will also give the admins the vscode deb file from Microsoft or, better, tell them what to add to <code>/etc/apt/source.list.d/</code>. Then I'll give the student a <code>tar</code> archive containing an empty Lean project whose <code>leanpkg.toml</code> is </p>
<div class="codehilite"><pre><span></span>[package]
name = &quot;math114&quot;
version = &quot;0.1&quot;
lean_version = &quot;3.4.2&quot;
path = &quot;src&quot;

[dependencies]
mathlib = { path = &quot;/usr/lib/lean-mathlib/&quot; }
</pre></div>


<p>I checked on a my machine and it seems to work nicely. Lean does use the precompiled mathlib, which is owned by root hence read-only. In case I want to upgrade mathlib I can distribute a new deb file to my admins (I hope this won't be needed before next year).  I'll also tell students to install the VScode Lean extension on day one. Maybe I'll also distribute a VScode config, I'm not sure (at the very least I don't want VScode to bug them with upgrade messages). Of course (almost?) each lecture will feature a lean file for students to download, with specific definitions and lemmas, as well as sorried lemmas to complete. I hope this will be easy. I'm only waiting for mathlib to become Lean 3.4.2 compatible before shipping by deb files to the admins. </p>
<p>Any comment or suggestion is welcome.</p>

#### [ Kevin Buzzard (Jan 19 2019 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20setup/near/156443689):
<p>The reason we have the 3.4.1 mathlib branch nightmare is that when I did this over the summer I thought "wouldn't it be a great idea if everyone was on the same version of mathlib?" and persuaded Mario to make a 3.4.1 branch. In practice I was surprised to find out that actually this consistency didn't matter too much. There were people for whom it did not matter <em>at all</em> which version of mathlib they had, as long as it worked, because they never really pushed it to the limit. And then there were people who wanted to use stuff like quadratic reciprocity, so Chris had to write it, so Chris had to write some polynomial stuff, and then this got merged, and then all of a sudden there were people who wanted to use Chris' s work and had a genuine reason to want to update mathlib anyway -- "you can't stop progress", as Mario put it. On the other hand this is my summer project students I'm talking about here, and they were free to do whatever they wanted, so I guess in retrospect it was not surprising that some of them wanted newer mathlibs -- mathlib was actively changing because of the work they were doing at that time. With my first year students Oct-Dec the only issue I had with updating mathlib was that I would notice things like <code>existsi</code> being hard to use, and then <code>use</code> being introduced, and then me wanting to use <code>use</code>, and then realising that I would have to give the students access to <code>use</code> too. Our ICT guys were very reluctant to update mathlib more than once every 6 months.</p>
<p>With CoCalc the advantage was that I could set "homework" that actually contained an entire _target directory with whatever version of mathlib I wanted, and with .olean files as well, so I was in complete control, which was much better.</p>

#### [ Patrick Massot (Jan 24 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20setup/near/156805636):
<p>Some news about my teaching setup. At <a href="https://gist.github.com/PatrickMassot/b828897dc92b98ec5e7c9038123c89b5" target="_blank" title="https://gist.github.com/PatrickMassot/b828897dc92b98ec5e7c9038123c89b5">https://gist.github.com/PatrickMassot/b828897dc92b98ec5e7c9038123c89b5</a> you can find a quick and dirty python script which builds deb packages for Lean and mathlib, as outlined in the first message of this thread. You need <a href="http://www.pyinvoke.org/" target="_blank" title="http://www.pyinvoke.org/">invoke</a> (use <code>sudo pip3 install invoke</code>, after <code>sudo apt install python3-pip</code> if needed). Put the file somewhere, and run <code>inv lean</code> and then <code>inv mathlib</code> to create two deb files. See <code>inv --help lean</code> and <code>inv --help mathlib</code> if you want to specify a lean version or a package version.</p>

#### [ Patrick Massot (Jan 24 2019 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20setup/near/156805729):
<p>In particular, if you already have something like <code>lean-mathlib_3.4.2-1.deb</code> and want to upgrade, <code>inv mathlib -p 2</code> will get the latest mathlib and create <code>lean-mathlib_3.4.2-2.deb</code> that you can install on top of the preceding one</p>


{% endraw %}
