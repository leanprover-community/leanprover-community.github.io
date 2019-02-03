---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68366howtoleanwithelan.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [howto lean with elan](https://leanprover-community.github.io/archive/113488general/68366howtoleanwithelan.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Apr 20 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446301):
<p><a href="https://gist.github.com/jcommelin/1d45a0ea7a84a87db8a28a12e93cac32" target="_blank" title="https://gist.github.com/jcommelin/1d45a0ea7a84a87db8a28a12e93cac32">https://gist.github.com/jcommelin/1d45a0ea7a84a87db8a28a12e93cac32</a><br>
This is still WIP. I did not test it yet.</p>

#### [ Johan Commelin (Apr 20 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446346):
<p>Posting it here, because I gotta go now.</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446397):
<blockquote>
<p>Then add source .elan/env to your shell initialization script, say ~/.bashrc</p>
</blockquote>
<p>Does this part not work out of the box via the elan installer?</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446413):
<blockquote>
<p>elan run nightly-2018-04-06 leanpkg new my_playground</p>
</blockquote>
<p>You can do <code>elan run --install ...</code> to skip step 1</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446465):
<p>Scenario 2: <code>build</code> implies <code>configure</code></p>

#### [ Johan Commelin (Apr 20 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446569):
<p>Thanks for the feedback!</p>

#### [ Johan Commelin (Apr 20 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446577):
<blockquote>
<blockquote>
<p>Then add source .elan/env to your shell initialization script, say ~/.bashrc</p>
</blockquote>
<p>Does this part not work out of the box via the elan installer?</p>
</blockquote>
<p>Not for me. It edited <code>.profile</code> and <code>.bash_profile</code> but those files do nothing for me.</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446628):
<blockquote>
<p>Launch VScode from the terminal, while you are inside the directory lean-stacks-project. (This will make sure that VScode knows about the right version of Lean.)</p>
</blockquote>
<p>The location from where you start VS Code should not be relevant, as long as <code>elan</code> is in your PATH. Actually, I would recommend configuring the path in the VS Code settings rather than bothering with the terminal. You should open an issue in the plugin repo about <code>~</code> not being accepted.</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446631):
<p>And thank you for testing and writing this!</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446861):
<blockquote>
<p>It edited .profile and .bash_profile but those files do nothing for me.</p>
</blockquote>
<p>It should after you log out and back in (i.e. in a new login shell). Actually, your desktop environment should usually read <code>.profile</code> as well next time, so you shouldn't have to configure VS Code at all. This should probably be tested by multiple people on different configurations.</p>

#### [ Johan Commelin (Apr 20 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446877):
<p>Ok, <code>elan</code> is magic to me.</p>

#### [ Johan Commelin (Apr 20 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446881):
<p>If I have two folders <code>a/</code> and <code>b/</code>, and I have to different <code>toml</code> files in them</p>

#### [ Johan Commelin (Apr 20 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446883):
<p>And I have two instances of vscode open</p>

#### [ Johan Commelin (Apr 20 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446923):
<p>In one I navigate to <code>a/</code>, in the other to <code>b/</code></p>

#### [ Johan Commelin (Apr 20 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446924):
<p>How will they call the right version of Lean?, How does elan figure this out?</p>

#### [ Johan Commelin (Apr 20 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446927):
<p>I assumed via some <code>PWD</code> in the <code>env</code></p>

#### [ Johan Commelin (Apr 20 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446929):
<p>But if you don't call vscode from the terminal, that won't work</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446945):
<p>It sure does. The vscode plugin takes care to set the cwd of the server process to the opened directory.</p>

#### [ Johan Commelin (Apr 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446985):
<p>Aah, wonderful</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446987):
<p>Which automatically makes <code>elan</code> work, without either of the two knowing about the other tool :)</p>

#### [ Johan Commelin (Apr 20 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125446989):
<p>Fantastic</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125447468):
<p>elan 0.5.0 will make <code>leanpkg +nightly-2018-04-06</code>work even if it's not installed yet btw</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125448267):
<p>I've opened an issue about what I imagine would be a nicer elan+mathlib workflow: <a href="https://github.com/Kha/elan/issues/7" target="_blank" title="https://github.com/Kha/elan/issues/7">https://github.com/Kha/elan/issues/7</a></p>

#### [ Johan Commelin (Apr 20 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125448647):
<p>Thanks, great ideas!</p>

#### [ Johan Commelin (Apr 20 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125448653):
<p>Do you plan to work on this soon?</p>

#### [ Johan Commelin (Apr 20 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125448694):
<p>Because then I will postpone my howto for a little bit</p>

#### [ Patrick Massot (Apr 20 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464426):
<p>Nice work Johan!</p>

#### [ Patrick Massot (Apr 20 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464474):
<p>I think you could do the small corrections suggested by Sebastian without waiting so that we can point new users to this while Sebastian works on elan</p>

#### [ Johan Commelin (Apr 20 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464484):
<p>Hmm, that's true</p>

#### [ Patrick Massot (Apr 20 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464485):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> what about VScode <code>open folder</code> operation? Is it no longer relevant?</p>

#### [ Johan Commelin (Apr 20 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125464496):
<p>I'll see if I can find some time on Monday</p>

#### [ Sebastian Ullrich (Apr 20 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125469732):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> You still need it, I think? You should use it anyway for easier navigation etc. Note that vscode-lean doesn't seem to support the new multi-root workspaces yet.</p>

#### [ Johan Commelin (Apr 23 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125554858):
<p>Voila, an update:<br>
<a href="https://gist.github.com/jcommelin/1d45a0ea7a84a87db8a28a12e93cac32" target="_blank" title="https://gist.github.com/jcommelin/1d45a0ea7a84a87db8a28a12e93cac32">https://gist.github.com/jcommelin/1d45a0ea7a84a87db8a28a12e93cac32</a><br>
This incorporates the suggestions by <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span></p>

#### [ Johan Commelin (Apr 23 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125554901):
<p>What would be the proper place to post this how to?</p>

#### [ Johan Commelin (Apr 23 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125554903):
<p>I'm fine with leaving it as a gist right now, but that isn't very visible to newcomers</p>

#### [ Johan Commelin (Apr 23 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125554906):
<p>Or should we just link to it from several READMEs?</p>

#### [ Patrick Massot (Apr 23 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125558443):
<p>I think you can PR it to <code>mathlib/docs/elan.md</code> and link to it from <code>mathlib</code> main README.</p>

#### [ Patrick Massot (Apr 23 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125558500):
<p>I would add that you can put the <code>source .elan/env</code> in your <code>.bashrc</code> or <code>.zshrc</code> instead of <code>.profile</code> if you want to enjoy it from terminal immediately. Reading "It is recommended that you re-login, so that your environment knows about Elan." would be <em>extremely</em> off-putting for me.</p>

#### [ Johan Commelin (Apr 23 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125558961):
<p>But it already says:</p>
<blockquote>
<p>(Alternatively, type <code>source $HOME/.elan/env</code> into your terminal. Now this terminal session knows about Elan.)</p>
</blockquote>

#### [ Patrick Massot (Apr 23 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559111):
<p>It still doesn't suggest the shell startup scripts. And I think this emphasis is currently much more on the relogging option.</p>

#### [ Johan Commelin (Apr 23 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559355):
<p>I agree that the emphasis is on logging in again. You don't need the startup scripts after logging in. So if you don't want to relogin, I would just source it straight into the current terminal session.</p>

#### [ Johan Commelin (Apr 23 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559365):
<p>The reason I put emphasis on the relogin is that you can just launch VScode from a GUI launcher afterwards. Which is nice.</p>

#### [ Johan Commelin (Apr 23 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559368):
<p>Otherwise you have to launch it from a terminal... which some newcomers might not really be happy with...</p>

#### [ Johan Commelin (Apr 23 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125559408):
<p>But I agree that asking for a relogin is maybe also something that people are not happy with...</p>

#### [ Johan Commelin (Apr 23 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125566458):
<p>Ok, I just reinstalled the desktop pc in my office. I just tested the howto, and it seems to work (-;</p>

#### [ Patrick Massot (Apr 23 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125566513):
<p>Nice! So you can PR it and then prove that Spec vs global section thing.</p>

#### [ Johan Commelin (Apr 23 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567126):
<p>Ok, so to make a pull request, should I fork leanprover/mathlib? Or is there another way to do this?</p>

#### [ Patrick Massot (Apr 23 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567127):
<p>fork</p>

#### [ Patrick Massot (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567135):
<p>This sounds aggressive but that's the usual procedure</p>

#### [ Johan Commelin (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567140):
<p>okido</p>

#### [ Patrick Massot (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567142):
<p>Then create a branch from master in your fork and PR from there</p>

#### [ Sebastian Ullrich (Apr 23 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567188):
<blockquote>
<p>Do you plan to work on this soon?</p>
</blockquote>
<p>I don't think I will get to it before Lean 3.4.1 is released... so perhaps at that point you can just hard-code 3.4.1 as the Lean version to use, with or without elan.</p>

#### [ Patrick Massot (Apr 23 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567192):
<p>Any news about 3.4.1?</p>

#### [ Patrick Massot (Apr 23 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567207):
<p>I guess you wait for Mario here</p>

#### [ Sebastian Ullrich (Apr 23 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567210):
<p>yes</p>

#### [ Patrick Massot (Apr 23 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567258):
<p>We need mathlib to work with nightly-2018-04-20</p>

#### [ Patrick Massot (Apr 23 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125567260):
<p>Otherwise 3.4.1 is pointless</p>

#### [ Johan Commelin (Apr 23 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125572029):
<p>A student popped in. But here is the PR: <a href="https://github.com/leanprover/mathlib/pull/113" target="_blank" title="https://github.com/leanprover/mathlib/pull/113">https://github.com/leanprover/mathlib/pull/113</a></p>

#### [ Patrick Massot (Apr 23 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125572125):
<p>Thanks! I wrote a tiny comment</p>

#### [ Johan Commelin (Apr 23 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125572299):
<p>Fixed</p>

#### [ Patrick Massot (Apr 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573243):
<p>I felt like I should double that effort. So I just opened another doc PR: <a href="https://github.com/leanprover/mathlib/pull/114" target="_blank" title="https://github.com/leanprover/mathlib/pull/114">https://github.com/leanprover/mathlib/pull/114</a></p>

#### [ Patrick Massot (Apr 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573300):
<p>Maybe this is a nice challenge for me: each time someone PRs some doc, I double it.</p>

#### [ Patrick Massot (Apr 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573308):
<p>Simon: if you PR something now, we hit the 20 mark</p>

#### [ Patrick Massot (Apr 23 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573341):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> <span class="user-mention" data-user-id="110064">@Kenny Lau</span> <span class="user-mention" data-user-id="110026">@Simon Hudon</span> I hope you don't mind I've stolen your explanations (with attribution) in the above PR</p>

#### [ Simon Hudon (Apr 23 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573411):
<p>Do we get royalties? :D</p>

#### [ Patrick Massot (Apr 23 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125573501):
<p>Your royalty is writing this piece of doc didn't distracted you from writing your tactic writing tutorials</p>

#### [ Simon Hudon (Apr 23 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125574242):
<p>Sounds like you win twice</p>

#### [ Patrick Massot (Apr 23 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125574275):
<p>I love this negociation</p>

#### [ Patrick Massot (Apr 23 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/125574327):
<p>But actually I'm a bit serious. Gathering some Zulip explanations into mathlib doc is something I can do. And I'm very happy if this allows experts to work on expert stuff I couldn't do.</p>

#### [ Simon Hudon (Dec 12 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151493765):
<p>I'm trying to use a local version of lean and hoping <code>elan</code> will help me with that. I wrote <code>elan toolchain link lean-tweaked ~/lean/lean-master</code> but then <code>elan</code> crashes. Am I the only one with this issue?</p>

#### [ Gabriel Ebner (Dec 12 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151510146):
<p>I've run into this as well, something in elan panics and the error message is less than helpful.  An easy workaround is to add the symlink manually:</p>
<div class="codehilite"><pre><span></span>ln -s ~/lean/lean-master ~/.elan/toolchains/lean-tweaked
</pre></div>

#### [ Sebastian Ullrich (Dec 12 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151510342):
<p>I haven't encountered that before, but I'm open to PRs</p>

#### [ Simon Hudon (Dec 12 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151521010):
<p>Basically, I'd change these lines <a href="https://github.com/Kha/elan/blob/master/src/elan/toolchain.rs#L150-L154" target="_blank" title="https://github.com/Kha/elan/blob/master/src/elan/toolchain.rs#L150-L154">https://github.com/Kha/elan/blob/master/src/elan/toolchain.rs#L150-L154</a> to</p>
<div class="codehilite"><pre><span></span><span class="w">        </span><span class="k">match</span><span class="w"> </span><span class="n">install_method</span><span class="w"> </span><span class="p">{</span><span class="w"></span>
<span class="w">            </span><span class="n">InstallMethod</span>::<span class="nb">Copy</span><span class="p">(</span><span class="n">_</span><span class="p">)</span><span class="w"> </span><span class="o">|</span><span class="w"></span>
<span class="w">            </span><span class="n">InstallMethod</span>::<span class="n">Dist</span><span class="p">(..)</span><span class="w"> </span><span class="o">=&gt;</span><span class="w"> </span><span class="o">!</span><span class="bp">self</span><span class="p">.</span><span class="n">is_custom</span><span class="p">(),</span><span class="w"></span>
<span class="w">            </span><span class="n">InstallMethod</span>::<span class="n">Link</span><span class="p">(</span><span class="n">_</span><span class="p">)</span><span class="w"> </span><span class="o">=&gt;</span><span class="w"> </span><span class="kc">true</span><span class="w"></span>
<span class="w">        </span><span class="p">}</span><span class="w"></span>
</pre></div>

#### [ Simon Hudon (Dec 12 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/howto%20lean%20with%20elan/near/151521150):
<p>I should probably keep testing it. My setup seems a bit broken and I'm not sure if it's because of what I did to Lean (which I think shouldn't break anything) or what I did to <code>elan</code> (which I don't think should break anything either)</p>


{% endraw %}
