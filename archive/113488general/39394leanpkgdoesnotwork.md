---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39394leanpkgdoesnotwork.html
---

## Stream: [general](index.html)
### Topic: [leanpkg does not work](39394leanpkgdoesnotwork.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 10 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129424899):
after git clone Xena-UROP-2018 from GitHub, I want to do `leanpkg upgrade` but it failed and post many error:

`/usr/local/leanpkg/leanpkg/main.lean:1:0: error: file 'init' not found in the LEAN_PATH
/usr/local/leanpkg/leanpkg/resolve.lean:1:0: error: file 'init' not found in the LEAN_PATH
/usr/local/leanpkg/leanpkg/manifest.lean:1:0: error: file 'init' not found in the LEAN_PATH
/usr/local/leanpkg/leanpkg/toml.lean:1:0: error: file 'init' not found in the LEAN_PATH `

I don't know how to do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129431669):
Which OS?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129431724):
Are you using the command line? What's the output of `lean --version`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129437075):
it gives me `Lean (version 3.4.1, commit 17fe3decaf8a, Release)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129437080):
I run this on Mac

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 11 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129456013):
How did you install Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129456073):
If you type `leanpkg`, what is the first line of the output? I have files with the same names as those which are giving you errors, in my unix install, but there is no mention of `init`. It's certainly possible to get it all working on a mac.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129460129):
@**Blair Shi**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129460708):
Macos high Sierra 10.13.2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129460895):
@**Kevin Buzzard** 

```
dyn3159-100:xena-UROP-2018 shifengzheng$ leanpkg
/usr/local/leanpkg/leanpkg/main.lean:1:0: error: file 'init' not found in the LEAN_PATH
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129460969):
@**Sebastian Ullrich** I just downloaded the package `lean-3.4.1` and then in my vscode I set 
`    "lean.executablePath": "/Users/shifengzheng/lean-3.4.1-darwin/bin/lean",`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 11 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462153):
@**Blair Shi** Why do you have files in `/usr/local/` then? Do you have an old Homebrew installation or something like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462557):
@**Blair Shi** @**Blair Shi** (wait -- there are two?) the error shows that the version of `leanpkg` which is running is *not* the one in `Users/shifengzheng/lean-3.4.1-darwin/bin/`, it is some other version installed in `usr/local`. You might want to completely remove the `/usr/local/leanpkg` directory and add `Users/shifengzheng/lean-3.4.1-darwin/bin/` to the path on your command line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462558):
@**Sebastian Ullrich**  before I did not have `leanpkg`in my `/usr/local/` but when I typed `leanpkg` in terminal, it reported `<unknown>:1:1: error: file '/usr/local/leanpkg/leanpkg/main.lean' not found`. So I put leanpkg into my `/usr/local/`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462561):
I don't think you can just move `leanpkg` and hope for things to still work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462565):
I think you have to move the entire installation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462644):
What I'm saying is that you can move the directory `/Users/shifengzheng/lean-3.4.1-darwin` to anywhere you like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462648):
but you should leave the contents intact.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129462654):
When you've decided where to put it, point VS Code and your command line PATH to it, and then things should be OK.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129465999):
I moved `lean-3.4.1-darwin` to `/usr/local/` and added path to LEAN_PATH and removed the previous `leanpkg`in `local`
```
dyn3159-100:xena-UROP-2018 shifengzheng$ echo $LEAN_PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/lean-3.4.1-darwin/bin/
```
But stil not work. 
```
dyn3159-100:xena-UROP-2018 shifengzheng$ leanpkg
<unknown>:1:1: error: file '/usr/local/leanpkg/leanpkg/main.lean' not found
```
Did I set the wrong path or did I miss to do something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 11 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466184):
Kevin said to modify `PATH`, not `LEAN_PATH`. Please `unset LEAN_PATH`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 11 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466360):
Could you post the output of `which leanpkg` and `bash -x leanpkg`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466476):
@**Sebastian Ullrich**  sorry for my misunderstanding. I `unset LEAN_PATH` and did what you said
```
dyn3159-100:xena-UROP-2018 shifengzheng$ which leanpkg
/usr/local/bin/leanpkg
dyn3159-100:xena-UROP-2018 shifengzheng$ bash -x leanpkg
++ uname
+ unamestr=Darwin
+ [[ Darwin == \D\a\r\w\i\n ]]
+ command -v greadlink
+ READLINK=greadlink
+++ greadlink -f leanpkg
++ dirname /Users/shifengzheng/xena-UROP-2018/leanpkg
+ leandir=/Users/shifengzheng/xena-UROP-2018/..
++ greadlink -f /Users/shifengzheng/xena-UROP-2018/..
+ leandir=/Users/shifengzheng
+ librarydir=/Users/shifengzheng/lib/lean
+ test -d /Users/shifengzheng/lib/lean
+ librarydir=/Users/shifengzheng
+ LEAN_PATH=/Users/shifengzheng/library:/Users/shifengzheng/leanpkg
+ PATH=/Users/shifengzheng/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
+ exec lean --run /Users/shifengzheng/leanpkg/leanpkg/main.lean
<unknown>:1:1: error: file '/Users/shifengzheng/leanpkg/leanpkg/main.lean' not found
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 11 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466541):
Apparently you still have an old `leanpkg` at `/usr/local/bin`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 11 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466576):
Blair -- I'll be at Imperial in about 10 minutes and will try and sort things out. Sorry it's taken so long -- I had other things to do this morning.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 11 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20does%20not%20work/near/129466958):
I find a solution to deal with this issue. I just put the `Xena-UROP-2018` to my `my_playground` which already set up `mathlib`. Now it works

