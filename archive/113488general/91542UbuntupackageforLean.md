---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91542UbuntupackageforLean.html
---

## Stream: [general](index.html)
### Topic: [Ubuntu package for Lean?](91542UbuntupackageforLean.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 02 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133216835):
How does that work? I could attempt to maintain it if it's only really a matter of making sure the set up runs on my 18.04 machine and accepting PRs from people who wanted to fix it on other versions of Ubuntu

#### [ Kevin Buzzard (Sep 02 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133216837):
Mathlib could be a separate package

#### [ Kevin Buzzard (Sep 02 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133216895):
One advantage could be that we could show wavering windows users "look, all this fuss about command line and git -- if you were using Ubuntu then all you have to do is type apt install mathlib and that's genuinely it"

#### [ Kevin Buzzard (Sep 02 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133216896):
Several people talked to me over the summer about switching from Windows to Ubuntu

#### [ Patrick Massot (Sep 02 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133217683):
That's something I'm seriously considering. But learning how to do that is not trivial.

#### [ Bryan Gin-ge Chen (Sep 02 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133218000):
I guess the first thing to do is to skim through these docs http://packaging.ubuntu.com/html/ . Then it looks like there's a related (abandoned?) repository here https://github.com/leanprover/ppa-updater which might be a good place to start.

#### [ Patrick Massot (Sep 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133219585):
Indeed this is probably a good place to start. But it almost certainly goes back to Lean 2 days, so there will be a lot to change. @**Sebastian Ullrich** do you have any thought to share about this?

#### [ Kevin Buzzard (Sep 02 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133220913):
I've emailed Soonho Kong, who seems to be the package maintainer

#### [ Mario Carneiro (Sep 02 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133221017):
I don't think Soonho is working on Lean anymore

#### [ Mario Carneiro (Sep 02 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133221019):
He was one of the main developers of lean in lean 1/2 era

#### [ Mario Carneiro (Sep 02 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133221063):
but he finished his PhD and works at Toyota now IIRC

#### [ Kevin Buzzard (Sep 02 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133221684):
But he might own, in some sense, the correct name for the package?

#### [ Sebastian Ullrich (Sep 02 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133225599):
I really don't see system packages as the right solution for software like Lean, especially when we go back to frequent nightly releases. Which is why I wrote a Lean version manager...

#### [ Patrick Massot (Sep 02 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133226600):
There are slightly different issues here, depending on who wants Lean. Maybe CoCalc will make that unnecessary but, up to now, anyone who wants to use Lean for teaching must go to their system administrators and explain how to install Lean on, say, 50 machines so that students can use it. It's much, much easier if the request is: dear system administrator, could you `apt install lean`? The same also applies when we want to encourage a colleague to try Lean. This is very different from talking about people who will want "Lean 4 beta 53" because they can't resist the hype.

#### [ Patrick Massot (Sep 02 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133226646):
Clearly I will download every single nightly of Lean 4, without needing a Debian package. But today I cannot tell a colleague: you should try Lean, it's fun!

#### [ Sebastian Ullrich (Sep 02 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133227626):
I think you've got that backwards: installing elan is a one-liner and does not need sudo. Installing a Lean PPA in Ubuntu would mean that people need to change their system configuration and add the PPA source before they can `apt install` it - until the package is included in the official repository, which I believe could take quite some time (ditto for every single update).

#### [ Sebastian Ullrich (Sep 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133227778):
If the goal of a system-wide installation for teaching is to allow students to start using Lean immediately without configuration, that's not really possibly anyway, is it? As far as I know, there is no way to install the VS Code extension system-wide, and even VS Code itself is now encouraging user installs over system ones.

#### [ Patrick Massot (Sep 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133227781):
I don't know how to install VScode at user level. I download a deb file from their site and `dpkg -i` it.

#### [ Sebastian Ullrich (Sep 02 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133227839):
Oh, I guess that is just on Windows. I'm assuming you have to do updates manually in that case. Does it notify you about them?

#### [ Patrick Massot (Sep 02 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133227850):
Yes, I get notifications, I press a button which opens the webpage where I should download a new deb file

#### [ Sebastian Ullrich (Sep 02 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133227892):
I see

#### [ Patrick Massot (Sep 02 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133227899):
I really don't know what is the right solution. I only see that everybody who arrives here has trouble installing everything. And this is really scary.

#### [ Bryan Gin-ge Chen (Sep 02 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133228751):
As a relatively new member, let me say that mathlib's [current install guide](https://github.com/leanprover/mathlib/blob/master/docs/elan.md) worked well enough for me on my mac, but I didn't attempt it on my windows system because of the `Assumptions` text at the top. I gather that elan actually can be installed on windows, but I just ended up following the [install guide on the xena blog](https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/) and got things working that way.

#### [ Sebastian Ullrich (Sep 03 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133232210):
Btw, the Isabelle people decided to forgo Debian packaging in favor of bundling up everything themselves https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=494491#44

#### [ Johannes Hölzl (Sep 03 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133232422):
But compared to Isabelle, Lean doesn't have any dependencies. Isabelle needs Poly/ML, a JDK, jEdit etc. We only need VS code or emacs, which are already packed for Debian.

#### [ Scott Morrison (Sep 03 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133232432):
Something I've been wondering is whether we can run elan directly from the VS Code extension.

#### [ Scott Morrison (Sep 03 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133232472):
That is, if it discovers it can't find a copy of Lean, it pops up an infobox "Would you like to install Lean, using elan?"

#### [ Scott Morrison (Sep 03 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133232473):
If that can work cross platform then we're getting to have a pretty nice experience for new users.

#### [ Sebastian Ullrich (Sep 03 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133232524):
Oh, that does sound far nicer to me than the other way around, bundling VS Code with Lean

#### [ Johan Commelin (Sep 03 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133240006):
That would be genius! Then the install instructions would become: (1) Download VScode. (2) Fire it up. (3) Search for the Lean extension and install it. (4) Start using Lean. (5) Click yes on the pop up. (6) Get yourself coffee :coffee: or tea :tea:.

#### [ Gabriel Ebner (Sep 03 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133257966):
Adding elan auto-installation to the vscode extension is not hard.  On Linux it works really well.  However on windows elan was pretty broken the last time I tried it.

#### [ Johan Commelin (Sep 03 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258037):
Windows install guide: (1) Download virtualbox. (2) Install ubuntu. (3) Follow the Linux install guide.

#### [ Johan Commelin (Sep 03 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258056):
Install guide for students with bad laptops: (1) Use CoCalc. `-- this one should work soon, I hope`

#### [ Johan Commelin (Sep 03 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258240):
```quote
Adding elan auto-installation to the vscode extension is not hard.  On Linux it works really well.  However on windows elan was pretty broken the last time I tried it.
```
I guess VScode knows what OS it is on? So you could potentially implement this Linux-only, right?

#### [ Gabriel Ebner (Sep 03 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258515):
Yes, you can definitely figure out the OS from a vscode extension. We can disable it on windows, if necessary.  That said, you need to work on it yourself if you want it before I get back from vacation in October.

#### [ Scott Morrison (Sep 03 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258552):
Thanks for looking into this, Gabriel! Is what you did for Linux available somewhere?

#### [ Johan Commelin (Sep 03 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258564):
I see. Didn't know you were on holidays (-; Enjoy!

#### [ Scott Morrison (Sep 03 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258586):
I can grab a student with a windows laptop and try to investigate. :-)

#### [ Gabriel Ebner (Sep 03 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258778):
Oh I see there was a small misunderstanding. *elan* works well on Linux, if you open a project in vscode then elan will automatically download the right binary.  But there us no auto-installation implemented at all.

#### [ Johan Commelin (Sep 03 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133258793):
Indeed

#### [ Adam Kurkiewicz (Sep 11 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133727845):
Sorry to be jumping in so late, but my perspective on this topic is that this is a sort of initiative that would benefit from some external funding and somebody whose job it would be to make sure that everything works. That's for two of reasons:

1. Writing & maintaining packages and installers is not novel or exciting. It's hard to rely on somebody's enthusiasm to constantly make sure everything is working on multiple platforms, with multiple versions, etc.
2. It's not exactly rocket science. It probably wouldn't be cost-efficient for most people here to be getting drawn away from their research to handle support requests from lean + vscode/ lean + emacs users. Conversely, not supporting user requests would mean a lot of frustrated users.

I wish I had a good answer on who could pay for this sort of (I imagine on-going) stream of work, but, unfortunately, "writing Ubuntu packages" doesn't make for a great funding proposal. However, if attached to some sexy idea, this could become a partial focus of some broader project. Now, I think "Writing bug-free software" or "Automated checking of mathematical proofs" could sound sufficiently exciting to receive funding, although what exactly goes into the proposal will have to be thoroughly thought through.

Streams of funding to look at would be:
1. Catalyst Grants. Not sure if Lean is considered "early stage", but some other mentioned tools, like elan or CoCalc maybe would. The current call for applications closes on 31st of December: https://www.digital-science.com/investment/catalyst-grant/
2. Google Summer of Code. Not sure if Lean is affiliated, but if it isn't, it probably should be!

I'm happy to put the work into writing a funding proposal, and running the project if it's funded, as long as we could agree on what should go into it.

#### [ Reid Barton (Sep 11 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133728610):
>  Sorry to be jumping in so late, but my perspective on this topic is that this is a sort of initiative that would benefit from some external funding and somebody whose job it would be to make sure that everything works.

Agreed. It's perhaps not exactly a full-time job at this point, but it is a non-negligible fraction of one and once Lean 4 is released and we're no longer "frozen" on a fixed version of Lean indefinitely, it will become even more so.

#### [ Reid Barton (Sep 11 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133728881):
GHC (the Glasgow Haskell Compiler, the de facto standard compiler for the Haskell programming language) happens to be, like Lean, a project led by developer(s) at Microsoft Research, although GHC is much older and has many more users. In the case of GHC, MSR itself funds the release manager role, at one point directly by hiring an engineer part of whose job was GHC release management, and now indirectly through a Haskell consultancy company.

#### [ Reid Barton (Sep 11 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133729032):
I'm not sure GSOC would be a good source of funding for release management, primarily because the release manager's job is never-ending, as OS distributors find creative new ways to break software. (I do think GSOC is an excellent idea for projects to extend mathlib, though!)

#### [ Adam Kurkiewicz (Sep 11 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ubuntu%20package%20for%20Lean%3F/near/133730652):
Thanks Reid, this is a very insightful perspective. I agree that ultimately MSR will likely take on this responsibility. I was trying to think smaller, and about a solution that would be good for between now and until lean becomes large and old enough to graduate to a software product with its own release manager :).


{% endraw %}
