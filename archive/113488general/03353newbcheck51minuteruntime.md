---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03353newbcheck51minuteruntime.html
---

## [general](index.html)
### [newb,  "#check 5" 1 minute runtime?](03353newbcheck51minuteruntime.html)

#### [drocta (May 31 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127381913):
First, sorry if this is not the correct place for me to seek help for this. I haven't used zulip before and couldn't find a page with the rules to follow for this specific chat. (Should I have put this in an existing topic?)
I tried installing Lean 3.4.1 on windows 7, and when I try to run a test2.lean which consists of just "#check 5", it takes a minute and 5 seconds before it gives me the output.
> 5 : ℕ
> <unknown>:1:1: error: unknown declaration 'main'

(when running "lean --run ../../progs/test2.lean" )
Someone else let me know that they tried a similar file
(specifically, 

> constant m : nat
> #check m

which I tried before "#check 5" and also takes a minute for me)
 on linux, and for them it ran in under a second.
They didn't have an idea for why it was running slowly except possibly my antivirus, but it still runs just as slow for me when I have that turned off.

I tend to have my computer's memory use fairly high. Would this cause Lean to run this slowly for this test case?

During the minute that it is running, my cpu use goes to around 100%  (from around 20%). I tried closing my antivirus software and it didn't seem to improve the running speed.

Could anyone provide me with advice for what to do differently?

Thank you for your consideration

#### [Patrick Massot (May 31 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127382236):
```quote
First, sorry if this is not the correct place for me to seek help for this. I haven't used zulip before and couldn't find a page with the rules to follow for this specific chat. (Should I have put this in an existing topic?)
```
I don't think we have any specific rule. Mario only pretends to complain when he sees Lolcats or memes. We only try to minimize code when asking for help, and avoid asking Sebastian about Lean 4 progress every day. That being said, I have no Windows computer so I cannot help. I can only tell you this shouldn't happen

#### [drocta (May 31 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127382343):
Alright, thank you

#### [Reid Barton (May 31 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127382889):
I don't think you want "--run"

#### [Reid Barton (May 31 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127382917):
But I don't know whether that will make it not slow.

#### [drocta (May 31 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383242):
Ah! Thanks, I tried it without the "--run" , and it no longer complains about lacking main, though it still takes slightly over a minute.

#### [drocta (May 31 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383487):
Ah, I just tried running it with --profile , and, in addition to much more text than I expected, it ended with
> 5 : ℕ
cumulative profiling times:
        compilation 6.75s
        decl post-processing 2.45s
        elaboration 85.4s
        elaboration: tactic compilation 11.5s
        elaboration: tactic execution 13.2s
        parsing 12.9s
        type checking 1.44s

Which I suppose says something, thought I'm not quite sure what.

#### [Mario Carneiro (May 31 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383840):
Have you compiled the library files? If your core lean contains no .olean files then that could explain the long startup, since lean has to compile everything every time. Try running `lean --make` first

#### [Mario Carneiro (May 31 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383863):
You don't want to use `--run` unless you are using lean noninteractively

#### [Mario Carneiro (May 31 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383870):
it's basically the same as affixing `#eval main` to the end of the given file

#### [drocta (May 31 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383939):
Ah, I had not! I will run that now, Thank you!

#### [drocta (May 31 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127384026):
Ah, when I ran `lean --make`by itself it finished in under a second and didn't say anything, and then I tried `lean ../../progs/test2.lean` again and it still took a bit. I will time it to see if it is still taking a minute.

#### [drocta (May 31 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127384140):
Still took a minute and 5 seconds.
I noticed that when I ran `lean --path` it told me that "leanpkg_path_file" was "/could-not-find-home". Could that be related?

#### [drocta (May 31 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127384205):
oh, I tried `lean --make ..\..\progs\test2.lean` and it is saying stuff

#### [drocta (May 31 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127384302):
Ah! Great! It runs in 7 seconds now. There we go. Thank you!

#### [Reid Barton (Jun 01 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127387966):
Interesting. I guess the precompiled binaries don't contain precompiled .olean files? Are they platform-dependent?

#### [Kevin Buzzard (Jun 01 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127388291):
I almost always use linux nightlies and they have plenty of .olean files usually

