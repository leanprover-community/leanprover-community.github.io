---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68366howtoleanwithelan.html
---

## Stream: [general](index.html)
### Topic: [howto lean with elan](68366howtoleanwithelan.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446301):
https://gist.github.com/jcommelin/1d45a0ea7a84a87db8a28a12e93cac32
This is still WIP. I did not test it yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446346):
Posting it here, because I gotta go now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446397):
>  Then add source .elan/env to your shell initialization script, say ~/.bashrc

Does this part not work out of the box via the elan installer?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446413):
> elan run nightly-2018-04-06 leanpkg new my_playground

You can do `elan run --install ...` to skip step 1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446465):
Scenario 2: `build` implies `configure`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446569):
Thanks for the feedback!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446577):
```quote
>  Then add source .elan/env to your shell initialization script, say ~/.bashrc

Does this part not work out of the box via the elan installer?
```
Not for me. It edited `.profile` and `.bash_profile` but those files do nothing for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446628):
> Launch VScode from the terminal, while you are inside the directory lean-stacks-project. (This will make sure that VScode knows about the right version of Lean.)

The location from where you start VS Code should not be relevant, as long as `elan` is in your PATH. Actually, I would recommend configuring the path in the VS Code settings rather than bothering with the terminal. You should open an issue in the plugin repo about `~` not being accepted.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446631):
And thank you for testing and writing this!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446861):
>  It edited .profile and .bash_profile but those files do nothing for me.

It should after you log out and back in (i.e. in a new login shell). Actually, your desktop environment should usually read `.profile` as well next time, so you shouldn't have to configure VS Code at all. This should probably be tested by multiple people on different configurations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446877):
Ok, `elan` is magic to me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446881):
If I have two folders `a/` and `b/`, and I have to different `toml` files in them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446883):
And I have two instances of vscode open

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446923):
In one I navigate to `a/`, in the other to `b/`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446924):
How will they call the right version of Lean?, How does elan figure this out?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446927):
I assumed via some `PWD` in the `env`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446929):
But if you don't call vscode from the terminal, that won't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446945):
It sure does. The vscode plugin takes care to set the cwd of the server process to the opened directory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446985):
Aah, wonderful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446987):
Which automatically makes `elan` work, without either of the two knowing about the other tool :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446989):
Fantastic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125447468):
elan 0.5.0 will make `leanpkg +nightly-2018-04-06`work even if it's not installed yet btw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125448267):
I've opened an issue about what I imagine would be a nicer elan+mathlib workflow: https://github.com/Kha/elan/issues/7

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125448647):
Thanks, great ideas!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125448653):
Do you plan to work on this soon?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125448694):
Because then I will postpone my howto for a little bit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 20 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464426):
Nice work Johan!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 20 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464474):
I think you could do the small corrections suggested by Sebastian without waiting so that we can point new users to this while Sebastian works on elan

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464484):
Hmm, that's true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 20 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464485):
@**Sebastian Ullrich** what about VScode `open folder` operation? Is it no longer relevant?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464496):
I'll see if I can find some time on Monday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 20 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125469732):
@**Patrick Massot** You still need it, I think? You should use it anyway for easier navigation etc. Note that vscode-lean doesn't seem to support the new multi-root workspaces yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125554858):
Voila, an update:
https://gist.github.com/jcommelin/1d45a0ea7a84a87db8a28a12e93cac32
This incorporates the suggestions by @**Sebastian Ullrich**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125554901):
What would be the proper place to post this how to?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125554903):
I'm fine with leaving it as a gist right now, but that isn't very visible to newcomers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125554906):
Or should we just link to it from several READMEs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125558443):
I think you can PR it to `mathlib/docs/elan.md` and link to it from `mathlib` main README.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125558500):
I would add that you can put the `source .elan/env` in your `.bashrc` or `.zshrc` instead of `.profile` if you want to enjoy it from terminal immediately. Reading "It is recommended that you re-login, so that your environment knows about Elan." would be *extremely* off-putting for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125558961):
But it already says:
>    (Alternatively, type `source $HOME/.elan/env` into your terminal. Now this terminal session knows about Elan.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559111):
It still doesn't suggest the shell startup scripts. And I think this emphasis is currently much more on the relogging option.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559355):
I agree that the emphasis is on logging in again. You don't need the startup scripts after logging in. So if you don't want to relogin, I would just source it straight into the current terminal session.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559365):
The reason I put emphasis on the relogin is that you can just launch VScode from a GUI launcher afterwards. Which is nice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559368):
Otherwise you have to launch it from a terminal... which some newcomers might not really be happy with...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559408):
But I agree that asking for a relogin is maybe also something that people are not happy with...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125566458):
Ok, I just reinstalled the desktop pc in my office. I just tested the howto, and it seems to work (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125566513):
Nice! So you can PR it and then prove that Spec vs global section thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567126):
Ok, so to make a pull request, should I fork leanprover/mathlib? Or is there another way to do this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567127):
fork

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567135):
This sounds aggressive but that's the usual procedure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567140):
okido

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567142):
Then create a branch from master in your fork and PR from there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 23 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567188):
```quote
Do you plan to work on this soon?
```
I don't think I will get to it before Lean 3.4.1 is released... so perhaps at that point you can just hard-code 3.4.1 as the Lean version to use, with or without elan.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567192):
Any news about 3.4.1?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567207):
I guess you wait for Mario here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 23 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567210):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567258):
We need mathlib to work with nightly-2018-04-20

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567260):
Otherwise 3.4.1 is pointless

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125572029):
A student popped in. But here is the PR: https://github.com/leanprover/mathlib/pull/113

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125572125):
Thanks! I wrote a tiny comment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 23 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125572299):
Fixed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573243):
I felt like I should double that effort. So I just opened another doc PR: https://github.com/leanprover/mathlib/pull/114

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573300):
Maybe this is a nice challenge for me: each time someone PRs some doc, I double it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573308):
Simon: if you PR something now, we hit the 20 mark

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573341):
@**Gabriel Ebner** @**Kenny Lau** @**Simon Hudon** I hope you don't mind I've stolen your explanations (with attribution) in the above PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573411):
Do we get royalties? :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573501):
Your royalty is writing this piece of doc didn't distracted you from writing your tactic writing tutorials

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125574242):
Sounds like you win twice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125574275):
I love this negociation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125574327):
But actually I'm a bit serious. Gathering some Zulip explanations into mathlib doc is something I can do. And I'm very happy if this allows experts to work on expert stuff I couldn't do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Dec 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151493765):
I'm trying to use a local version of lean and hoping `elan` will help me with that. I wrote `elan toolchain link lean-tweaked ~/lean/lean-master` but then `elan` crashes. Am I the only one with this issue?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 12 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151510146):
I've run into this as well, something in elan panics and the error message is less than helpful.  An easy workaround is to add the symlink manually:
```
ln -s ~/lean/lean-master ~/.elan/toolchains/lean-tweaked
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Dec 12 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151510342):
I haven't encountered that before, but I'm open to PRs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Dec 12 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151521010):
Basically, I'd change these lines https://github.com/Kha/elan/blob/master/src/elan/toolchain.rs#L150-L154 to

```rust
        match install_method {
            InstallMethod::Copy(_) |
            InstallMethod::Dist(..) => !self.is_custom(),
            InstallMethod::Link(_) => true
        }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Dec 12 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151521150):
I should probably keep testing it. My setup seems a bit broken and I'm not sure if it's because of what I did to Lean (which I think shouldn't break anything) or what I did to `elan` (which I don't think should break anything either)

