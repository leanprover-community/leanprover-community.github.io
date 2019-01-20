---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: general/leanpkg.html
---

## [general](index.html)
### [leanpkg](leanpkg.html)

#### Andrew Ashworth (Sep 23 2018 at 15:27):
the mingw bash script sets a bunch of environment variables

#### Andrew Ashworth (Sep 23 2018 at 15:27):
also, I use MSYS2 with no issues

#### Olli (Sep 23 2018 at 15:28):
I see, yeah I will try installing MSYS2, and I just confirmed that I was able to add mathlib to a new project and it appears to work fine from VSCode which is good

#### Reid Barton (Sep 23 2018 at 17:47):
@**Olli**, so is your conclusion that leanpkg is not compatible with MSYS, but is compatible with MSYS2?

#### Olli (Sep 23 2018 at 18:05):
@**Reid Barton** yes that appears to be correct

#### Olli (Sep 23 2018 at 18:20):
MSYS2 contains `test.exe`

#### Bryan Gin-ge Chen (Sep 23 2018 at 19:45):
Is it also true that using the git-for-windows bash shell also works for you? I don't think I have msys2 on my windows 10 machine and I got leanpkg working there.

#### Olli (Sep 23 2018 at 20:33):
yes, I should probably have tried that first, but had totally forgot I even had it installed

#### Bryan Gin-ge Chen (Sep 23 2018 at 20:37):
That's great, thanks for being so patient and looking into it. Now we should look into editing these solutions into the various docs that are floating around out there...

#### Mario Carneiro (Sep 23 2018 at 20:54):
I don't think git bash is fully usable for lean, although I forget why. I made some attempts to do this when I started and some necessary packages were missing with no clear way to get them

#### Mario Carneiro (Sep 23 2018 at 20:55):
Certainly CMD and powershell won't work

#### Mario Carneiro (Sep 23 2018 at 20:56):
I haven't tested Cygwin extensively, but it has its own issues to deal with and I found MSYS2 much easier

#### Mario Carneiro (Sep 23 2018 at 20:56):
I'd be curious to see if anyone makes lean work with WSL

#### Bryan Gin-ge Chen (Sep 23 2018 at 21:02):
I've been using git bash up to now and haven't noticed anything wrong, but all I'm doing with regards to lean is just running `leanpkg upgrade` and `leanpkg build` occasionally. I did have to mess around with my console program to get unicode characters to print properly though.

#### Scott Morrison (Oct 25 2018 at 00:16):
Hi @**Reid Barton**, did you ever sort this out? Can we just delete the `lean-3.4.1` branch of `mathlib`? I see that Mario has been occasionally updating, but it still requires manual intervention.

#### Reid Barton (Oct 25 2018 at 00:17):
No, we can't just delete it unfortunately--leanpkg requires a branch matching the lean version to exist, when that version is a stable version

#### Reid Barton (Oct 25 2018 at 00:20):
I think the best "solution" we have for now is for somebody to figure out how to write a git hook that Mario can use to update the branch head automatically

#### Neil Strickland (Jan 18 2019 at 16:30):
I am also using git bash without obvious problems.  I have msys2 installed but it is not in the path so that should not make a difference.
@**Bryan Gin-ge Chen** , what did you do to fix the unicode?

#### Bryan Gin-ge Chen (Jan 18 2019 at 16:34):
For me it was an issue with a setting in my console program, [`cmder`](http://cmder.net/) which seems to be a reskin or repackaging of [`conemu`](https://conemu.github.io/). I had to add the setting `chcp utf8` to the environment per [this page](https://conemu.github.io/en/UnicodeSupport.html).

#### Neil Strickland (Jan 18 2019 at 16:54):
Thanks.  That suggestion doesn't seem immediately applicable to me as I am just using git bash in vscode (and git bash outside vscode seems to handle unicode correctly).  I poked around a bit more and found this page https://github.com/Microsoft/vscode/issues/60330, but the suggestions there seemed to have no effect.  I'll probably just leave it now as it is not really causing me any trouble, it's just untidy.

