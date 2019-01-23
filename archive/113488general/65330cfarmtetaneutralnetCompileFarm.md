---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65330cfarmtetaneutralnetCompileFarm.html
---

## Stream: [general](index.html)
### Topic: [cfarm.tetaneutral.net - Compile Farm](65330cfarmtetaneutralnetCompileFarm.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135489637):
@**Tobias Grosser** I have an account now. How do I use it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135490060):
```quote
@**Tobias Grosser** I have an account now. How do I use it?
```
We need a Would-you-please-move-this-to-another-thread-Thank-you-emoji

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 09 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135491195):
Looks like the instructions are at https://cfarm.tetaneutral.net/machines/list/, just ssh into one of the machines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135491224):
it requires a password and I don't know where to get the password from

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 09 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135491301):
Oh, uh... hmm. I would assume you're supposed to use ssh certificates but I also don't see how to set that up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 09 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135491328):
I just requested an account a minute or two ago, so I don't know.
I see there is a Login link in the top right of the web page though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 09 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135497171):
@**Johan Commelin**, indeed. Sorry for this distraction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 09 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135497287):
I use my ssh key to login. Not sure how this is handled today, but either you should have had a way to specify a password when registering or an ssh key, I assume.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135497370):
The website states: Once your account is created, you will be able to upload SSH keys and gain SSH access to all machines of the platform.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135497395):
So seems you need to wait until your account is confirmed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 10 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135503836):
I have an account now and I uploaded an SSH public key using the web interface but it takes some time for the key to be propagated to the machines. Kenny are you in the same situation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135504194):
I have no idea what SSH is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135504205):
what do you mean by upload an SSH public key

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 10 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135504482):
You'll want to do something like this https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 10 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135505466):
Yes, then you can use the cfarm web interface to add the ssh key to your account

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135511481):
```quote
@**Johan Commelin**, indeed. Sorry for this distraction.
```
No worries (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135566947):
So what do I do when they ask me for the password?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 11 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135571403):
Upload an ssh key, so it doesn't ask you for a password?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135571587):
it's still asking me for a password

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135571589):
and 1.5 hour has already passed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135571947):
I had to wait at least several hours (haven't tried to log in today)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135581252):
I can now log in. Time to see if I can build lean on a POWER8 system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135584158):
ok, got this working now... 2406 is the CPU% column
```
 31366 rwbarton  20   0 10.851g 3.304g  15872 S  2406  1.3  50:19.98 lean
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135584219):
The big sparc machine had unsatisfactory results--the release version of lean crashed, and the debug version mostly doesn't crash, but building mathlib did trigger some assertion and is super slow.
```
LEAN ASSERTION VIOLATION
File: /home/rwbarton/lean/lean/src/library/type_context.cpp
Line: 1230
Task: /home/rwbarton/lean/mathlib2/computability/primrec.lean: primcodable.prod
idx < m_tmp_data->m_uassignment.size()
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135584707):
mathlib on the POWER8 machine:
```
> lean --make .
28590.38user 105.69system 18:55.94elapsed 2526%CPU (0avgtext+0avgdata 10297280maxresident)k
```
Pretty parallel but not so good single-threaded performance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135584713):
Maybe tomorrow I'll try the xeons

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135585081):
Aha, this machine is actually 20 cores with 8-way SMT (IBM equivalent of hyperthreading)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135585133):
I wonder if that means a well-chosen cpu set would be faster

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135594900):
@**Reid Barton** could you teach me how to use it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135594908):
I just connect ssh and then do `lean --make`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135594914):
how do I make sure I'm using the server's CPU?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595827):
ok I can see that it automatically redirects me to the server

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595836):
but now how do I communicate between the server and my computer?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595896):
@**Kenny Lau** What kind of communication do you want?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595903):
You can copy files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595904):
how?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595907):
`scp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595915):
It uses `ssh`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595919):
But what do you want to copy?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595926):
Can't you just `git clone` on that server?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595937):
then how do I send the olean files back?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595952):
Aah, from the server to your box?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595957):
both ways

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595961):
Both times `scp` on your box

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595967):
how to use `scp`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596019):
`scp my_file.olean server:~/destination.olean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596028):
`scp -r server:~/a_directory/ my_directory/` ## recursive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596053):
what is `-R`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596062):
Sorry, should be `-r`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596091):
`scp` can also be used as `scp server1:path1 server2:path2`. It's pretty general (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596150):
I guess there are ways to recurse and only copy olean files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596157):
Maybe `rsync` can help. It will also use your ssh keys.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596163):
@**Kenny Lau** What OS are you on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596166):
windows

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596196):
/me shuts his eyes while Tux :penguin: slaps Kenny in the face.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596251):
@**Kenny Lau** I'm not sure if `rsync` is available. Can you try if it is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596254):
it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596261):
You're lucky (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596264):
I'm using something that has the unix commands

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596372):
Do you know `man`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596412):
oh no `scp` is copying the files one by one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596418):
it will take years

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596427):
`Ctrl-C`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596429):
Also try `man man`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596489):
so how do I even use this if I can't copy the files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596494):
Did you try `man man`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596498):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596508):
What happened?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596512):
i get a long manual?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596514):
Great. Try `man rsync`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596578):
how do I refer to my computer from the server?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596583):
That's harder.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596587):
:(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596588):
You can setup a reverse tunnel using ssh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596600):
See `man ssh`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596614):
But why would you want that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596636):
I don't have rsync, but the server has rsync

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596704):
Aah, to use `rsync` the other side needs some form of an ssh server I think. So that won't help you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596713):
A better solution would be to install rsync locally.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596720):
how do I do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596727):
I dunno. Haven't touched windows in 15 years.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596729):
just treat me as using bash

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596734):
You know that the latest Total War series also runs on Linux?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135598090):
ok so I `rsync`ed lean and mathlib, but now I can't run lean.exe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 11 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135599665):
You won't be able to do what you want with a Windows host machine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 11 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135599674):
Oleans aren't compatible between operating systems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 11 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135605471):
exes are certainly not compatible between operating systems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135610588):
this is so sad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135610648):
Right. Please blame Bill Gates.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135610978):
so then how do you install lean on linux?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611116):
@**Kenny Lau** Would you mind explaining the bigger goal that you have in mind with this service?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611154):
Also is X installed on that server, can you do ssh with X forwarding? If so, just install VScode, and run it on the server. The rest is history.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611165):
But I guess that you can't have X forwarding.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611189):
well with this service I can test the compile times quicklier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611361):
Have you looked at the travis config?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611366):
For mathlib on github

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611378):
It will tell Travis how to compile mathlib. I guess it could also tell you how to use this server

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611385):
https://github.com/leanprover/mathlib/blob/master/.travis.yml

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611432):
```
[kc_kennylau@gcc2-power8 ~]$ curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh -s -- --default-toolchain none -y
info: downloading installer
curl: (22) The requested URL returned error: 404 Not Found
elan: command failed: curl -sSfL https://github.com/Kha/elan/releases/download/v0.7.1/elan-powerpc64le-unknown-linux-gnu.tar.gz -o /tmp/tmp.Yt4psW5eYO/elan-init.tar.gz
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611536):
`which wget`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611546):
Oh nvm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611550):
I didn't read the error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611649):
That `elan` command is asking `curl` to write something to `/tmp/`. Maybe you don't have permissions there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611686):
But `curl` is also getting a 404

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611689):
Before that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611768):
then how did Tobias Grosser manage to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611771):
This explains why: https://github.com/Kha/elan/releases/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611780):
You are on a powerpc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611791):
That architecture is not supported by `elan`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 11 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611801):
@**Tobias Grosser** Can you tell how you did this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612036):
I did not get anything running on powerpc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612101):
$ssh gcc20.fsffrance.org

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612170):
In fact, I did not use the compilefarm to compile lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612179):
I would start with gcc20.fsffrance.org

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612241):
The easiest is probably to create a linux docker image with a current lean environment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612267):
And then use udocker to run it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612274):
Also, I am not sure kenny why you want to copy files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612283):
ignore the part about copying files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612287):
OK.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612298):
In theory you should be able to just run:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612306):
grosser@gcc20:~$       curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh -s -- --default-toolchain none -y
info: downloading installer

/tmp/tmp.OXhfu8gCPt/elan-init: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.15' not found (required by /tmp/tmp.OXhfu8gCPt/elan-init)
/tmp/tmp.OXhfu8gCPt/elan-init: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.14' not found (required by /tmp/tmp.OXhfu8gCPt/elan-init)
grosser@gcc20:~$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612314):
Unfortunately this gives an error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612324):
As the glibc version is not correct.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135613129):
What you can do instead on gcc20:

```
curl https://raw.githubusercontent.com/indigo-dc/udocker/master/udocker.py > udocker
chmod u+rx ./udocker
./udocker install
./udocker pull ubuntu
./udocker create --name=lean ubuntu
./udocker run lean
apt-get update
apt-get install curl git
curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh -s -- --default-toolchain none -y
 git clone https://github.com/leanprover/mathlib.git
leanpkg --make
```

to get back into your lean folder just run
```
./udocker run lean
cd mathlib
ls
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135613307):
I feel obliged to point out that copying build results from the farm machines isn't good practice in terms of security, even if the risks are low for olean files. Better to only copy things to the farm machines.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135624545):
I would suggest using the machines gcc120-gcc123, I got 10 minutes mathlib build time on gcc120 and elan worked without any issues. Note they are on nonstandard ports (45000 through 45003 respectively)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135624586):
Though Scott's machine is still the leader at 8 minutes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135628807):
@**Reid Barton**, this seems to be a great idea.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Oct 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135628814):
Did not see gcc120ff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638198):
I did `curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh` and it said elan has been installed when in fact it hasn't been.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638203):
and I thus can't install elan.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638264):
I tried on both gcc120 port 45000 and gcc121 port 45001

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638319):
Did you do the step printed out at the end of the elan output, i.e., `source <something>`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638323):
Or log out and log back in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640639):
```
[kc_kennylau@gcc120 ~]$ curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh
info: downloading installer

Welcome to Lean!

This will download and install Elan, a tool for managing different Lean
versions used in packages you create or download. It will also install a
default version of Lean and its package manager, leanpkg, for editing files not
belonging to any package.

It will add the leanpkg, lean, and elan commands to Elan's bin directory,
located at:

  /home/kc_kennylau/.elan/bin

This path will then be added to your PATH environment variable by modifying the
profile files located at:

  /home/kc_kennylau/.profile
  /home/kc_kennylau/.bash_profile

You can uninstall at any time with elan self uninstall and these changes will
be reverted.

Current installation options:

     default toolchain: stable
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
1

info: updating existing elan installation


Elan is installed now. Great!

To get started you need Elan's bin directory ($HOME/.elan/bin) in your PATH
environment variable. Next time you log in this will be done automatically.

To configure your current shell run source $HOME/.elan/env
[kc_kennylau@gcc120 ~]$ source $HOME/.lean/env
-bash: /home/kc_kennylau/.lean/env: No such file or directory
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640694):
Hmm, that is odd. It worked for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640704):
i'm on windows using msys2 mingw 64, if that makes any difference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640724):
Wait no! you typed it wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640726):
`.elan` not `.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640804):
I'm stupid.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640807):
it worked now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640834):
I wonder who thought naming the downloader for `lean` an anagram of `lean` was a good idea :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640838):
Maybe they should have chosen a less easily confused name, like `rustup`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640888):
you want the downloader for lean to be called `rustup`? That's indeed less easily confused with `lean`

