---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40246documentationview.html
---

## Stream: [general](index.html)
### Topic: [documentation view](40246documentationview.html)

---


{% raw %}
#### [ Patrick Massot (Jan 15 2019 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155152756):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> What happened to the documentation view feature of vscode-lean?</p>

#### [ Gabriel Ebner (Jan 15 2019 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155154073):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I'm a bit busy at the moment so there's nothing new (though it's available in the released version now).  In the other <a href="#narrow/stream/179818-Lean-Together.202019/topic/Guinea.20pigs.20wanted!/near/154947296" title="#narrow/stream/179818-Lean-Together.202019/topic/Guinea.20pigs.20wanted!/near/154947296">thread</a> you suggested that the documentation view should have back/forward buttons and a way to input your own url.  I completely agree.  (The webview api in vscode is unfortunately really, really stripped down...  Not even hyperlinks work by default, we are changing them to vscode commands on the fly....) <br>
<span class="user-mention" data-user-id="121918">@Edward Ayers</span> if you want to look at this, I can give you pointers.</p>

#### [ Gabriel Ebner (Jan 15 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155154095):
<p>In case anybody has too much free time and wants to give feedback, run "ctrl+shift+p open documentation view" and post your complaints here.</p>

#### [ Patrick Massot (Jan 15 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155154259):
<p>Thanks Gabriel! Did you intend to ping Bryan instead of Ed?</p>

#### [ Patrick Massot (Jan 15 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155154268):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> Did you see that feature?</p>

#### [ Gabriel Ebner (Jan 15 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155154344):
<p>No, Ed asked me in Amsterdam to please give him work on the vscode extension.  But I'm happy about contributions from all sides.</p>

#### [ Patrick Massot (Jan 15 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155154428):
<p>By the way, am I correct in thinking that this was not in the previous release? If not then please forgive me for asking today</p>

#### [ Gabriel Ebner (Jan 15 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155154578):
<p>I made a release for Ed's translations PR yesterday, that's the first release with the documentation view.</p>

#### [ Patrick Massot (Jan 15 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155154690):
<p>Weird... I did try to check before posting. Sorry</p>

#### [ Jeremy Avigad (Jan 16 2019 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/155223205):
<p>I just tried documentation view. It's great! Here are two comments.</p>
<p>The bigger one: once we move from the table of contents to a specific chapter, as far as I can tell it is impossible to go back to the table of contents without pressing ctrl-shift-P and choosing "open documentation view" again. That makes it less convenient to browse. I don't know the ideal solution here. Maybe the best solution is to assign a keystroke to "open documentation view", so that pressing that would return to the TOC.</p>
<p>The smaller issue: the natural way to play with the text and examples is to split the screen, put the text in the left, and then run the examples in the right. But even when I have a split screen, when I click on the "try it" button, the window opens on the left, and I have to manually move it to the right. Would it be possible to have the window open on the right?</p>

#### [ Patrick Massot (Jan 31 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157262831):
<p>I just tried to use the VScode Lean documentation view in our computer rooms, with no success. Could it be that it tries to access TPIL without using the system-wide proxy setup?</p>

#### [ Patrick Massot (Jan 31 2019 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157262839):
<p><span class="user-mention" data-user-id="121918">@Edward Ayers</span> <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span></p>

#### [ Gabriel Ebner (Jan 31 2019 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157262898):
<p>Yes, I'm pretty sure it doesn't look at proxy settings.</p>

#### [ Patrick Massot (Jan 31 2019 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157262901):
<p>Note that VScode does successfully use the proxy when downloading the Lean extension</p>

#### [ Patrick Massot (Jan 31 2019 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157262922):
<p>Fixing this would be a nice improvement</p>

#### [ Edward Ayers (Jan 31 2019 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157263593):
<p>Did you have to set the <code>http.proxy</code> in the vscode settings for the extension downloading to work?</p>

#### [ Gabriel Ebner (Jan 31 2019 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157263646):
<p>Ideally, we could use the system proxy settings that vscode uses itself, but it looks like this is not possible yet: <a href="https://github.com/Microsoft/vscode/issues/12588" target="_blank" title="https://github.com/Microsoft/vscode/issues/12588">https://github.com/Microsoft/vscode/issues/12588</a></p>

#### [ Gabriel Ebner (Jan 31 2019 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157263693):
<p>The <code>http.proxy*</code> settings are the older (now deprecated) way to set the proxy in vscode (and it is ignored by most of vscode).  We could use this setting (but Patrick needs to set it).</p>

#### [ Patrick Massot (Jan 31 2019 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157263799):
<p>I didn't have to set anything to get the extension</p>

#### [ Gabriel Ebner (Jan 31 2019 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157263895):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> vscode has <em>two</em> settings for proxies: one is taken directly from the system settings and is used for extension fetching, etc.  But this is unfortunately not accessible to extensions (i.e., us).</p>

#### [ Kevin Buzzard (Jan 31 2019 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157265408):
<p><code>issues/12588</code>. Wow -- and I thought we had issues.</p>

#### [ Kevin Buzzard (Jan 31 2019 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157265536):
<p>When there are 4621 open issues, how do you get people to work on the one you want to be fixed?</p>

#### [ Mario Carneiro (Jan 31 2019 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157265790):
<p>in big companies the issues process has to be a lot more formal. There is triage and tagging, periodic review of priorities, and work is often aimed for milestones. Quite often the issues system is the force behind all work - i.e. if you want to change something you should make an issue first, so that the intent is logged and prioritized</p>

#### [ Mario Carneiro (Jan 31 2019 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157265860):
<p>so you have people working on the most important things and other people adding and organizing new issues</p>

#### [ Mario Carneiro (Jan 31 2019 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157265939):
<p>For a big github project, you can vote on your favorite issues by adding a thumbs up reaction to it; this sometimes helps, depending on the team, but it's just a suggestion</p>

#### [ Mario Carneiro (Jan 31 2019 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/documentation%20view/near/157266037):
<p>apparently people really want floating windows <a href="https://github.com/Microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+sort%3Areactions-%2B1-desc" target="_blank" title="https://github.com/Microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+sort%3Areactions-%2B1-desc">https://github.com/Microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+sort%3Areactions-%2B1-desc</a></p>


{% endraw %}
