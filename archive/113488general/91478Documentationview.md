---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91478Documentationview.html
---

## Stream: [general](index.html)
### Topic: [Documentation view](91478Documentationview.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155152756):
@**Gabriel Ebner** What happened to the documentation view feature of vscode-lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 15 2019 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155154073):
@**Patrick Massot** I'm a bit busy at the moment so there's nothing new (though it's available in the released version now).  In the other [thread](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean-Together.202019/topic/Guinea.20pigs.20wanted!/near/154947296) you suggested that the documentation view should have back/forward buttons and a way to input your own url.  I completely agree.  (The webview api in vscode is unfortunately really, really stripped down...  Not even hyperlinks work by default, we are changing them to vscode commands on the fly....) 
@**Edward Ayers** if you want to look at this, I can give you pointers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 15 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155154095):
In case anybody has too much free time and wants to give feedback, run "ctrl+shift+p open documentation view" and post your complaints here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155154259):
Thanks Gabriel! Did you intend to ping Bryan instead of Ed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155154268):
@**Jeremy Avigad** Did you see that feature?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 15 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155154344):
No, Ed asked me in Amsterdam to please give him work on the vscode extension.  But I'm happy about contributions from all sides.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155154428):
By the way, am I correct in thinking that this was not in the previous release? If not then please forgive me for asking today

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 15 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155154578):
I made a release for Ed's translations PR yesterday, that's the first release with the documentation view.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155154690):
Weird... I did try to check before posting. Sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Jan 16 2019 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation%20view/near/155223205):
I just tried documentation view. It's great! Here are two comments.

The bigger one: once we move from the table of contents to a specific chapter, as far as I can tell it is impossible to go back to the table of contents without pressing ctrl-shift-P and choosing "open documentation view" again. That makes it less convenient to browse. I don't know the ideal solution here. Maybe the best solution is to assign a keystroke to "open documentation view", so that pressing that would return to the TOC.

The smaller issue: the natural way to play with the text and examples is to split the screen, put the text in the left, and then run the examples in the right. But even when I have a split screen, when I click on the "try it" button, the window opens on the left, and I have to manually move it to the right. Would it be possible to have the window open on the right?

