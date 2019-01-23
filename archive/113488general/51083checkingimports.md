---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51083checkingimports.html
---

## Stream: [general](index.html)
### Topic: [checking imports](51083checkingimports.html)

---

#### [Jakob von Raumer (Oct 10 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135554082):
whenever I open vscode, lean seems to re-check all imported files... wasn't this better some time ago?

#### [Jakob von Raumer (Oct 10 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135554225):
(my issue here is that I need to close all other programs, to check some imports from the hott3 library, they use up almost all of my RAM)

#### [Chris Hughes (Oct 10 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135554646):
Did you run `leanpkg build` in the appropriate directory?

#### [Jakob von Raumer (Oct 10 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135555511):
Nope, shame on my, kind of assumed that vscode would somehow invoke that... :grinning_face_with_smiling_eyes:

#### [Jakob von Raumer (Oct 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135555567):
Uhm, and `leanpkg build` also doesn't eat all of my RAMs :ram:

#### [Jakob von Raumer (Oct 10 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135555870):
But unfortunately it doesn't change the fact that vscode checks everything at startup, even after a successful `leanpkg build`...

#### [Johan Commelin (Oct 10 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135555902):
Are you using `elan`? Did you run `leanpkg build` in the root of your project, or in a subdir?

#### [Jakob von Raumer (Oct 10 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556008):
In the root dir... What is `elan`?

#### [Johan Commelin (Oct 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556127):
Ok, you are not using `elan`.

#### [Johan Commelin (Oct 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556135):
Kevin wrote this page today: https://xenaproject.wordpress.com/installing-lean-and-mathlib/

#### [Johan Commelin (Oct 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556149):
Jakob, how did you install lean and mathlib?

#### [Jakob von Raumer (Oct 10 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556619):
Lean: Using the sources

#### [Jakob von Raumer (Oct 10 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556643):
Mathlib: Not sure if I have it at all... but hott3 doesn't depend on it, does it?

#### [Jakob von Raumer (Oct 10 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135556718):
Oh, there's a global installation of mathlib at `~/.lean/_target/deps`

#### [Johan Commelin (Oct 10 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135557237):
Hmmm... I don't really know enough to help you here.

#### [Rob Lewis (Oct 10 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135557629):
You have fresh .olean files in your Lean root directory, right? What exactly are you opening in VS Code?

#### [Jakob von Raumer (Oct 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135559479):
What's my lean root directory? I'm opening the folder of a project of mine in VS, which references `hott3` in its `.toml`

#### [Rob Lewis (Oct 10 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135560271):
Wherever you built the executable. If the executable lies in `lean/bin/`, then you should also have `lean/library/` with the core lib. The `.lean` files there should have fresh `.olean` files. In your project folder, do you have `_target/deps/hott3`? Are there `olean` files in there?

#### [Rob Lewis (Oct 10 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135560283):
And are there compilation errors when you run `leanpkg build`?

#### [Jakob von Raumer (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135561866):
Yes there's `.olean` files in `_target/deps/hott3` and not so fresh ones in `lean/library`... `leanpkg buid` goes through with warning but no errors.

#### [Jakob von Raumer (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135562001):
Hm, but if I run `leanpkg build` in `~/.lean`, I get loads of errors

#### [Jakob von Raumer (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135562103):
Oh, that's because stuff is not in `LEAN_PATH`

#### [Jakob von Raumer (Oct 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135562473):
Hu, but `lean --path` gives all I would expect...

#### [Jakob von Raumer (Oct 10 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563098):
Should `leanpkg build` build all the deps or just the files needed?

#### [Patrick Massot (Oct 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563180):
only needed

#### [Jakob von Raumer (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563290):
Thanks.

#### [Jakob von Raumer (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563297):
And should it build files that haven't changed since the last build?

#### [Jakob von Raumer (Oct 10 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135563570):
If there's only deps and no actual content in `~/.lean`, how come `leanpkg build` does anything at all, if I execute it there? :confused:

#### [Gabriel Ebner (Oct 10 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135564693):
Forget about `~/.lean`, it's independent and not used in this case (check `lean -p`, if it doesn't appear you don't need to worry about it).
The easiest way to ensure all olean files are built is to run `lean --make` in the project folder.
(You should also open the project folder in vscode (not a subfolder or superfolder), but I don't think that's the problem here.)

#### [Jakob von Raumer (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135565841):
Now it works :shrug: Not sure what was wrong. I did a rebuild of lean itself

#### [Patrick Massot (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135565898):
Why do you build Lean?

#### [Jakob von Raumer (Oct 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135565994):
I noticed it's been a while since I last built it

#### [Patrick Massot (Oct 10 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135566068):
Why building it at all? What's wrong with the distributed binaries? Are you modifying Lean?

#### [Jakob von Raumer (Oct 10 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135566172):
I used to,  ages ago. Before most of the library was moved to `mathlib`... I guess I could as well use the binaries now.

#### [Scott Morrison (Oct 11 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20imports/near/135571392):
Yeah, while Lean itself is stable at the moment, all the instructions people are giving assume you're using a binary (ideally provided by elan). `lean --make` in the `library/` directory of a built-from-sources copy of Lean can help with the issue you were experiencing.

