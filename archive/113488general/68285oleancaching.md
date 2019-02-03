---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68285oleancaching.html
---

## Stream: [general](index.html)
### Topic: [olean caching](68285oleancaching.html)

---


{% raw %}
#### [ Simon Hudon (Oct 07 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366355):
<p>I just created a PR to get <code>git</code> to preserve your <code>olean</code> files and restore them when you switch branches. I'd like to know if it works for people. Please let me know if you try it and if it helps.</p>

#### [ Kenny Lau (Oct 07 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366398):
<p>:D</p>

#### [ Simon Hudon (Oct 07 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366500):
<p>In particular, I'd like to know if it needs to be adapter for windows because I use shell scripts</p>

#### [ Patrick Massot (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366580):
<p>If you manage to allow us to switch mathlib branches back and forth without recompiling I phone the inquisition.</p>

#### [ Simon Hudon (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366585):
<p>Let me just delete a branch, one sec</p>

#### [ Patrick Massot (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366589):
<p>That would be one sorcery prowess too many for your own good.</p>

#### [ Simon Hudon (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366693):
<p>Can the quota be negotiated?</p>

#### [ Simon Hudon (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366699):
<p>If you want to try it before the branch is merged, here are the files</p>
<p><a href="/user_uploads/3121/KxJGKo8Df8IDgnEp7wUA57ar/cache_olean.zip" target="_blank" title="cache_olean.zip">cache_olean.zip</a></p>

#### [ Simon Hudon (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366707):
<p>You unzip them in your mathlib directory and call <code>./install_hooks.sh</code></p>

#### [ Patrick Massot (Oct 07 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366752):
<p>I'll negociate for you if you manage to convince Travis to put mathlib olean for linux somewhere git will find them each we git pull mathlib</p>

#### [ Simon Hudon (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366768):
<p>What it does is:</p>
<p>* when you commit, it makes a copy of your olean files<br>
  * when you checkout a branch, it checks if a cache exists for that branch and restores it if one exists<br>
  * when you rebase a branch A on top of branch B, it caches the files of A and restores the files of B</p>

#### [ Kenny Lau (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366769):
<p>just the olean files?</p>

#### [ Simon Hudon (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366770):
<p>Yes, just the olean files</p>

#### [ Simon Hudon (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366815):
<blockquote>
<p>I'll negociate for you if you manage to convince Travis to put mathlib olean for linux somewhere git will find them each we git pull mathlib</p>
</blockquote>
<p>That's a tall order. You're asking for a complete new feature, all I did was a small hack :P</p>

#### [ Simon Hudon (Oct 07 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366831):
<p>Actually ... that's feasible</p>

#### [ Simon Hudon (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366894):
<p>Actually, I think doing it half-way is more than half-way useful</p>

#### [ Simon Hudon (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366921):
<p>Do you guys feel like giving it a spin?</p>

#### [ Patrick Massot (Oct 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366972):
<p>I'll definitely try tomorrow, but I really need to go to bed now</p>

#### [ Simon Hudon (Oct 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366985):
<p>I thought you enjoyed working with Lean</p>

#### [ Simon Hudon (Oct 07 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135367104):
<p>Sleep well :)</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368285):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Does this work the same way for packages that include <code>mathlib</code> as a dependency?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368290):
<p>Wait, maybe that question doesn't make sense.</p>

#### [ Simon Hudon (Oct 08 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368396):
<p>You can make it work in that situation I believe. Once you configured the package, go in <code>_target/deps/mathlib</code> and call <code>./install_hooks.sh</code>. If different versions of the same package use different branches of mathlib, switching between the versions of your package might get cheaper (we'd have to test it to make sure)</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368397):
<div class="codehilite"><pre><span></span>hint: The &#39;.git/hooks/post-checkout&#39; hook was ignored because it&#39;s not set as executable.
hint: You can disable this warning with `git config advice.ignoredHook false`.
</pre></div>


<p>Should I change the permissions on these files?</p>

#### [ Simon Hudon (Oct 08 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368405):
<p>Yes good idea. And I'll make fixes to the scripts</p>

#### [ Simon Hudon (Oct 08 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369137):
<p>Any luck?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369336):
<p>I've been switching back and forth between <code>master</code> and <code>tutorials</code> and running <code>lean --make</code> and each time it does a full rebuild. If I do <code>lean --make</code> does that force a rebuild no matter what?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369338):
<p>I'm on my macbook.</p>

#### [ Scott Morrison (Oct 08 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369347):
<p>No, it doesn't/</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369392):
<p>Hmm, my master was out of date. Let me try again.</p>

#### [ Scott Morrison (Oct 08 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369401):
<p>The problem is likely that master has introduced changes to stuff way down the dependency tree.</p>

#### [ Scott Morrison (Oct 08 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369406):
<p>If you rebase tutorial onto master it should make life better.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369458):
<p>I think I see what you're saying, but shouldn't caching all the olean files associated to a given commit also preserve the build status?</p>

#### [ Simon Hudon (Oct 08 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369461):
<p>It should. Can you <code>ls .bin/branches</code> and tell me what you get?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369505):
<p>Where's <code>.bin</code>?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369569):
<p>Oh I see, I guess <code>.bin</code> somehow hasn't been created.</p>

#### [ Simon Hudon (Oct 08 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135370095):
<p>It is created when you commit or rebase. You can also manually call <code>.git/hooks/cache_olean.sh</code></p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371074):
<p>I ran <code>cache_olean.sh</code> after building on tutorials and master, and the olean files seem to be in .bin/branches/ but running lean --make still starts a rebuild.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371280):
<p>What if you run <code>restore_olean.sh</code> before rebuilding?</p>

#### [ Scott Morrison (Oct 08 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371281):
<blockquote>
<p>./install_hooks.sh <br>
cp: .git/hooks: Not a directory</p>
</blockquote>

#### [ Scott Morrison (Oct 08 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371293):
<p>Just needs a <code>mkdir -p .git/hooks</code> in <code>install_hooks.sh</code>.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371296):
<p>I tried running <code>restore_olean.sh</code> and it's rebuilding again.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371359):
<p>I pushed a commit that fixes this.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371360):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> Can you check what the time stamp is on the most recently modified file in <code>.bin/branches/tutorial</code>? I'm assuming that's the one you're trying to cache.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371362):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> You're too fast! Thanks!</p>

#### [ Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371403):
<p>Ah, but I fixed the wrong problem.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371406):
<p>The actual problem is that I don't have a .git directory.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371409):
<p>I have a .git file, because I'm using a submodule.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371412):
<p>Crap...</p>

#### [ Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371419):
<p>This is not going to affect many people at all, but I guess I want a fix myself. :-)</p>

#### [ Simon Hudon (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371422):
<p>Darn! How come you work without git?</p>

#### [ Scott Morrison (Oct 08 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371433):
<p>The problem is that I work with git for _everything_. My entire home directory is a giant git repository, and everything else is a git submodule, so things get synchronised between my computers.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371473):
<p>Actually, if you go in <code>_target/deps/mathlib</code> and call <code>install_hooks.sh</code> there, I'm hoping that will do the job</p>

#### [ Scott Morrison (Oct 08 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371478):
<p>Well, but I mostly want this for mathlib itself.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371479):
<p>Switching between branches that touch tactic/basic.lean is unpleasant...</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371534):
<p>The timestamps all seem to be from when I ran <code>cache_olean.sh</code>.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371560):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, why do you put <code>cache_olean.sh</code> and <code>restore_olean.sh</code> in the <code>.git/hooks</code> directory, rather than leaving them in the root directory?</p>

#### [ Simon Hudon (Oct 08 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371597):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> That is useful information. I'll look into preserving time stamps properly</p>

#### [ Simon Hudon (Oct 08 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371606):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I want to be able to use the hooks even on branches where the files aren't in the repo</p>

#### [ Scott Morrison (Oct 08 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371621):
<p>Ah, good point.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371622):
<p>The timestamps of the <code>.lean</code> files are bumped when I checkout a new branch. So do we need the timestamps of the olean files to be more recent than that?</p>

#### [ Simon Hudon (Oct 08 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371782):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> do you mean that the .lean timestamps are set to the time at which you checkout the files?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371788):
<p>Yes.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371797):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Maybe there's a way to include a search step at the beginning of the script to climb up the directory structure until a <code>.git</code> is found.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371843):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> What platform are you on?</p>

#### [ Scott Morrison (Oct 08 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371844):
<p>There's a nice fix, almost pushed.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371847):
<p><code>git rev-parse --git-dir</code> tells you where your <code>.git</code> directory really is.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371856):
<p>e.g. for me: <code>/Users/scott/.git/modules/projects/lean/mathlib</code></p>

#### [ Scott Morrison (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371910):
<p>Okay, pushed that change.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371918):
<p>I think we need more hooks. I want my olean files cached even if we don't  make a commit!</p>

#### [ Simon Hudon (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371919):
<p>Thanks! Did you put that <code>.git</code> dir in a variable?</p>

#### [ Scott Morrison (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371922):
<p>e.g. I never commit to master, but I want a cache.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371923):
<p>Yeah, me too! I haven't found a good hook for that</p>

#### [ Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371959):
<p>I just have <code>GITDIR=`git rev-parse --git-dir</code> in most of the scripts.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371971):
<p>What if when we checkout, we _first_ restore, _then_ cache.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371973):
<p>I think we might need to get <code>leanpkg</code> or, emacs / VS code to do that after you build</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371974):
<p>macOS. Not all of the .lean files have their timestamps bumped, but the ones that don't exist in <code>master</code> certainly do.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371977):
<p>If there was something to restore, then it just harmlessly puts it back again.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371978):
<p>But if there was nothing to restore, then we build a cache?</p>

#### [ Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371979):
<p>hmm...</p>

#### [ Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371980):
<p>no</p>

#### [ Scott Morrison (Oct 08 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371996):
<p>because that cache will be wrong. :-)</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372054):
<p>All the files that are changed between branches have their timestamps set to the time I do the checkout.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372179):
<p>What if on every checkout we:<br>
1) run cache before checkout (saving the state of the branch we're leaving)</p>

#### [ Scott Morrison (Oct 08 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372180):
<p>2) run restore after checkout</p>

#### [ Scott Morrison (Oct 08 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372181):
<p>3) run cache after that</p>

#### [ Simon Hudon (Oct 08 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372182):
<p>What a bummer. I found this information here. <a href="https://confluence.atlassian.com/bbkb/preserving-file-timestamps-with-git-and-mercurial-781386524.html" target="_blank" title="https://confluence.atlassian.com/bbkb/preserving-file-timestamps-with-git-and-mercurial-781386524.html">https://confluence.atlassian.com/bbkb/preserving-file-timestamps-with-git-and-mercurial-781386524.html</a></p>
<p>It recommends a certain build system as a solution</p>

#### [ Simon Hudon (Oct 08 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372223):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> run cache after the restore or after build?</p>

#### [ Scott Morrison (Oct 08 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372227):
<p>I was thinking just immediately after the restore.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372229):
<p>This has the effect of actually creating the cache merely by checking out.</p>

#### [ Scott Morrison (Oct 08 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372240):
<p>Otherwise I don't see how a cache for master will ever be created</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372244):
<p>Could we just <code>touch</code> all the <code>.olean</code> files right before restoring?</p>

#### [ Scott Morrison (Oct 08 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372295):
<p>I think the problem is that risk making things worse.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372296):
<p>Yeah</p>

#### [ Scott Morrison (Oct 08 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372301):
<p>(deleted)</p>

#### [ Scott Morrison (Oct 08 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372304):
<p>(deleted)</p>

#### [ Simon Hudon (Oct 08 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372307):
<p>What I'm thinking of is, after a checkout, look at each lean file and set its time stamp to that of the latest commit that changed it</p>

#### [ Scott Morrison (Oct 08 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372309):
<p>oof...</p>

#### [ Scott Morrison (Oct 08 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372341):
<p>(Presumably you mean to the time stamp of the corresponding olean file.)</p>

#### [ Reid Barton (Oct 08 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372349):
<p>What if you just don't use <code>cp -a</code>?</p>

#### [ Simon Hudon (Oct 08 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372408):
<p>The olean files will all be interpreted as up-to-date but some might not be</p>

#### [ Simon Hudon (Oct 08 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372469):
<blockquote>
<p>(Presumably you mean to the time stamp of the corresponding olean file.)</p>
</blockquote>
<p>No. For any source file we need to determine if we need to rebuild it. One information we need is when we last built it which is why we shouldn't overwrite the time stamp of the olean file. The other one is when we last change it which is why we wouldn't want git to overwrite the time stamp of a file but it does.</p>

#### [ Simon Hudon (Oct 08 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372480):
<p>I think we'd like to know if the file was built since the last commit that changed it</p>

#### [ Scott Morrison (Oct 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135386341):
<p>This olean caching stuff is really important, and I will be super happy if we can get it working smoothly. I'm not sure I can help at the moment with the timestamp issues, but let me know if there's anything I can do.</p>

#### [ Scott Morrison (Oct 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135386369):
<p>I hope one day we could even build a distributed cache; I could certainly contribute CPU cycles building olean files for central distribution.</p>

#### [ Simon Hudon (Oct 08 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135407646):
<p>I'll keep at it</p>

#### [ Chris Hughes (Oct 08 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135420726):
<p>I just have 17 copies of mathlib saved, so I never have to switch branches.</p>

#### [ Johan Commelin (Oct 08 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135420896):
<p>Diskspace is cheap...</p>

#### [ Simon Hudon (Oct 08 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135421237):
<p>I used to work like that. As the number of branches changes, I find it hard to manage</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451769):
<p>Interesting. I am not really up-to-speed here, but i might be interesting to look at existing tools which address these issues.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451775):
<p>Specifically, there is 'ninja' a very fast alternative for make.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451788):
<p>And 'ccache' which caches the compilation of C/C++ files.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451800):
<p>If lean would have a way to export the "include" files, it might be possible to adapt these tools (or use at least their design).</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451863):
<p>My feeling is that connecting .olean files to git branches is pretty fragile "hacky".</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451886):
<p>Hashing the source files and having a proxy for returning the right source file in case a hash is already known is a strategy that works well in the OS projects I have been working on.</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451892):
<p>lean already uses ninja for compilation</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451958):
<p>You would have to hash the file plus the hashes of dependent files, git-style</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451968):
<p>Right. The ccache docu explains well what is needed to do this kind of caching.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452307):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> , are you saying lean is using 'ninja' for compiling the lean binary, or is it called as part of 'lean --make'?</p>

#### [ Gabriel Ebner (Oct 09 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452480):
<p>ninja can optionally be used to compile lean itself.  lean --make doesn't use ninja (the equivalent linja tool in Lean 2 did though).  Ninja doesn't do anything more fancy than lean --make, I believe.  (Does ninja use content hashes or modification times?)  Something like ccache might be interesting when switching between branches.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452491):
<p>Also, to get the dependent files lean already has a command '--deps'.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452558):
<p>Ninja does not do anything more fancy than lean --make, I assume.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452561):
<p>However, it is _very_ fast.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452568):
<p>in checking if files have been modified.</p>

#### [ Gabriel Ebner (Oct 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452580):
<p>That is pretty much the least expensive part of running <code>lean --make</code> though.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452581):
<p>This does not matter for the perf problems we have today, but I feel it will matter in the future.</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452640):
<p>the problem is that the usual dependency analysis will say that too many files are affected and compile them all</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452658):
<p>Right, it's more a difference between 5 seconds and 0.01 second on clean builds. It really improves productivity on large C++ code bases and might be useful for lean as well (especially if we interactively want to update proofs).</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452665):
<p>Right. Most of likely requires changes in lean proper.</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452711):
<p>0.01 second vs 1 second to tell me that nothing needs doing doesn't seem so useful</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452724):
<p>but if you could reason that most of the library is unaffected by a new theorem in <code>logic.basic</code> that would be a HUGE gain</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452727):
<p>like an hour compilation</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452737):
<p>I mean these are orthogonal.</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452748):
<p>is it? I'm talking about proper caching and dependency analysis</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452800):
<p>You need all a) proper dependency analysis, b) good caching, c) worry about how to check if files have changed.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452808):
<p>ninja is really good in minimizing file IO and stat calls to very quickly check for c)</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452818):
<p>If there were thousands of files then I can see this being a problem</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452822):
<p>but at that point total compile times will dwarf all of this</p>

#### [ Gabriel Ebner (Oct 09 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452860):
<p>In server mode we don't even do any file IO?  We actually have a precomputed dependency graph.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452893):
<p>But it does not help with a) and b).</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452900):
<p>I see.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452946):
<p>So my feeling is at some point we would just need proper caching in server mode.</p>

#### [ Tobias Grosser (Oct 09 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452960):
<p>Which would be a lean specific thing, that just needs to be implemented, right?</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135479143):
<p>"just"</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135479146):
<p>:)</p>

#### [ Simon Hudon (Oct 09 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500213):
<p>I have created a branch of <code>ccache</code> to try and add support for Lean. I saw an issue discussion that suggests that it might be a simple business so I thought I'd try it out: <a href="https://github.com/leanprover-community/ccache" target="_blank" title="https://github.com/leanprover-community/ccache">https://github.com/leanprover-community/ccache</a></p>

#### [ Sebastian Ullrich (Oct 09 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500355):
<p>Wow, I've been thinking about doing this for a long time, but didn't think anyone would ever actually go ahead with it...</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500422):
<p>Though are you sure you don't want to modify <a href="https://github.com/mozilla/sccache" target="_blank" title="https://github.com/mozilla/sccache">https://github.com/mozilla/sccache</a> instead :) ?</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500445):
<p>(No idea if it would actually be easier, just newer code base, cloud support, and my preference for Rust)</p>

#### [ Simon Hudon (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500578):
<p>That sounds like an even more useful tool. I don't know what it would take to adapt though</p>

#### [ Simon Hudon (Oct 09 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500603):
<p>Do I understand correctly that it allows sharing binaries between team members or community members?</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500732):
<p>I assume it's intended for sharing with trusted team members. Securing public r/w access to some cloud storage doesn't sound like a simple issue.</p>

#### [ Simon Hudon (Oct 09 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500844):
<p>I think I'll put that issue aside to handle a simpler problem :)</p>

#### [ Patrick Massot (Oct 09 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500878):
<p>Sounds like an important issues, I've seen people discussing assuming <code>nat = int</code>, they probably shouldn't be trusted</p>

#### [ Kenny Lau (Oct 09 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500931):
<p>how about we remove <code>*.olean</code> from <code>gitignore</code>?</p>

#### [ Simon Hudon (Oct 09 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501059):
<p>It is a big no-no. We don't want to keep the history of those files, we just want appropriate binaries. Keeping those binaries will make <code>git</code> slower and will make merging more complicated.</p>

#### [ Chris Hughes (Oct 09 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501140):
<p>Also <code>olean</code> is OS dependent</p>

#### [ Simon Hudon (Oct 09 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501243):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> it looks like <code>sccache</code> works with Lean out of the box. You just call <code>sccache leanpkg build</code>. Does that make sense to you?</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501295):
<p>I have no idea. Does it look like it actually does anything?</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501320):
<p>(<span class="user-mention" data-user-id="110044">@Chris Hughes</span> It's not, AFAIK. Though it will be architecture-dependent in Lean 4)</p>

#### [ Simon Hudon (Oct 09 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501394):
<p>It does look like it actually calls <code>leanpkg</code> but I'll have to experiment and see if a cache is created.</p>

#### [ Sebastian Ullrich (Oct 09 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501476):
<p>Yes, that would be the important part <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>

#### [ Simon Hudon (Oct 09 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501579):
<p>If it does work out of the box, the next step would be integration: how do we make it invisible to the Lean user</p>

#### [ Simon Hudon (Oct 10 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135502099):
<p>I think part of it working with <code>leanpkg</code> and <code>elan</code> is to create a symbolic link so that when <code>lean</code> is called, it calls <code>sccache lean</code> instead. <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Does that sound like that could break the build system?</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135502577):
<p>That could work</p>

#### [ Simon Hudon (Oct 10 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135502811):
<p>Right now, I put a shell script called <code>~/.sccache/bin/lean</code> that just prints "calling lean" and I put it in my path (I checked with <code>which lean</code>) but <code>leanpkg</code> does not seem to call it</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503095):
<p>oh <a href="https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/bin/leanpkg#L24" target="_blank" title="https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/bin/leanpkg#L24">https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/bin/leanpkg#L24</a></p>

#### [ Simon Hudon (Oct 10 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503113):
<p>So how does <code>elan</code> redirect to the right version of <code>lean</code>?</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503160):
<p>It doesn't in that case, it just calls the right version of <code>leanpkg</code> :)</p>

#### [ Simon Hudon (Oct 10 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503203):
<p>argh!</p>

#### [ Simon Hudon (Oct 10 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503261):
<p>Any chance we might hard code <code>ccache</code> or <code>sccache</code> into <code>elan</code>?</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503278):
<p>How would that help?</p>

#### [ Simon Hudon (Oct 10 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503369):
<p>Maybe it could call a <code>leanpkg-2</code> bash script instead of <code>leanpkg</code> and also produce the <code>leanpkg-2</code> script so that the paths are set properly (for <code>sccache</code>). I have a feeling that that bash script did not change a lot between versions. Am I right?</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503577):
<p>I see. But if you want to support both <code>sccache leanpkg</code> and <code>sccache lean</code> anyway, are you sure you save any code by making the former call the latter?</p>

#### [ Simon Hudon (Oct 10 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503683):
<p>Actually, what I'd like to do is just replace every call to <code>lean</code> to <code>sccache lean</code>. <code>sccache</code> seems to index its cache by command line arguments.</p>

#### [ Simon Hudon (Oct 10 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503859):
<p>Actually, it might be enough to have <code>elan</code> rename <code>lean</code> to <code>lean-2</code> and create a bash script <code>lean</code> in its place to call <code>sccache</code> when <code>elan</code> downloads a version of <code>lean</code></p>

#### [ Simon Hudon (Oct 10 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135570892):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> It's starting to look to me like we may have to alter the way <code>lean --make</code> works for either of <code>sccache</code> or <code>ccache</code> to be useable</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135570906):
<p>I wouldn't be surprised :)</p>

#### [ Simon Hudon (Oct 10 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135570924):
<p>Bummer, I was hoping it might be a small(-ish) thing to do</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135571003):
<p>I was fully prepared that someone might at some point write an alternative <code>leanpkg</code> that fixes many issues with it (and would probably not be written in Lean)</p>

#### [ Simon Hudon (Oct 11 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135571113):
<p>Is there a way to use <code>lean</code> to export all the dependencies in a project? <code>lean --deps</code> seems to interact poorly with leanpkg.toml files</p>

#### [ Simon Hudon (Oct 11 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135571264):
<p>If I could use it, maybe I could generate a Makefile (or ninja config?) and that might be a better starting point than <code>lean --make</code></p>

#### [ Sebastian Ullrich (Oct 11 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135571728):
<p>I don't think so, you basically have to parse the file header...</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135614724):
<p>+1 for 'ninja + make', at best if it's auto-generated from the lean files.</p>

#### [ Simon Hudon (Oct 11 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135614792):
<p>The other tool I've heard of is Bazel. Have you heard of it and would you endorse it?</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615005):
<p>Never used it.</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615032):
<p>I feel it might be too high level.</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615039):
<p>In the end we know all dependences.</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615050):
<p>And just want to declare them and execute.</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615213):
<p>I mean, you might also try to use cmake:<br>
<a href="https://cmake.org/pipermail/cmake/2011-April/043761.html" target="_blank" title="https://cmake.org/pipermail/cmake/2011-April/043761.html">https://cmake.org/pipermail/cmake/2011-April/043761.html</a></p>

#### [ Tobias Grosser (Oct 11 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615236):
<p>Not sure if this makes things easier.</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615286):
<p>I fell, getting dependences out of lean files is certainly a useful component in any of these tools.</p>

#### [ Simon Hudon (Oct 11 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615513):
<p>In the end, we'll probably need to parse the Lean files ourselves though, no? Unless we can get <code>lean</code> to get them out for us.</p>

#### [ Simon Hudon (Oct 11 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615802):
<p>In the meantime, I started a branch in <code>sccache</code> and I talked to the developers on how to support Lean. It sounds doable. I just need to learn a bit more of Rust. And they seem willing to take our patch</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615854):
<p>Cool. This sounds very exciting, indeed.</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615893):
<p>What is the problem with --deps?</p>

#### [ Reid Barton (Oct 11 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615984):
<p>As far as I can tell, it just doesn't work properly</p>

#### [ Simon Hudon (Oct 11 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135616006):
<p>I can't get it to work at the scale of a project. It seems to work off of <code>LEAN_PATH</code> which is no longer required (and indeed harmful) to work with <code>leanpkg</code></p>

#### [ Tobias Grosser (Oct 11 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135616582):
<p>I see. I have no idea of this code, but fixing it seems the most direct thing to do. In fact, does it do a lot more than parsing the imports?</p>

#### [ Tobias Grosser (Oct 11 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135616638):
<p>AFAIU it should just parse the imports and then print this to stdout in some way.</p>

#### [ Reid Barton (Oct 11 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135616639):
<p>Simon, have you gotten it to work under any circumstances?</p>

#### [ Reid Barton (Oct 11 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135617597):
<p>Oh, I figured out why it is broken. It thinks that the presence of both <code>foo.lean</code> and <code>foo.olean</code> means that the import of <code>foo</code> is ambiguous.</p>

#### [ Reid Barton (Oct 11 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135617619):
<p>So, this is something we could work around (in principle, at least)</p>

#### [ Simon Hudon (Oct 11 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135618364):
<p>I was actually thinking that temporarily setting <code>LEAN_PATH</code> might fix it but I'm not done experimenting with it</p>

#### [ Reid Barton (Oct 11 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135618381):
<p>I looked at <code>strace -e trace=file</code> output and it's clearly not failing to find the files it's looking for</p>

#### [ Reid Barton (Oct 11 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135618449):
<p>And it is looking in the correct paths as reported by <code>lean -p</code> (and examining the source seems to indicate that <code>lean -p</code> is using the same path information as <code>lean --deps</code>)</p>

#### [ Simon Hudon (Oct 11 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135618997):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Any chance we may get a fix for <code>lean --deps</code>?</p>

#### [ Sebastian Ullrich (Oct 11 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619199):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Yes, I feel that could be a reasonable change. It would be great if you or someone else could investigate fixing it</p>

#### [ Simon Hudon (Oct 11 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619323):
<p>Sure I'll look into it. Do you have a suggestion of where I should start?</p>

#### [ Sebastian Ullrich (Oct 11 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619525):
<p>The relevant call should be this one: <a href="https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/src/shell/lean.cpp#L698" target="_blank" title="https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/src/shell/lean.cpp#L698">https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/src/shell/lean.cpp#L698</a></p>

#### [ Sebastian Ullrich (Oct 11 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619547):
<p>Wow, <code>display_deps</code> is still testing for <code>.hlean</code> and <code>.lua</code></p>

#### [ Reid Barton (Oct 11 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619731):
<p>What I have inferred from looking at the source and the strace output: Say the module imports <code>data.rbmap</code>. <code>display_deps</code> calls</p>
<div class="codehilite"><pre><span></span><span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">find_file</span><span class="p">(</span><span class="n">search_path</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">paths</span><span class="p">,</span> <span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">base</span><span class="p">,</span> <span class="n">optional</span><span class="o">&lt;</span><span class="kt">unsigned</span><span class="o">&gt;</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">rel</span><span class="p">,</span> <span class="n">name</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">fname</span><span class="p">,</span>
                      <span class="n">std</span><span class="o">::</span><span class="n">initializer_list</span><span class="o">&lt;</span><span class="kt">char</span> <span class="k">const</span> <span class="o">*&gt;</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">extensions</span><span class="p">)</span> <span class="p">{</span>
</pre></div>


<p>in <code>src/util/lean_path.cpp</code>. That calls <code>file_path</code> just above, because the import is not relative. That one tries each extension in the given list and pushes all the successes into a list of results.</p>

#### [ Reid Barton (Oct 11 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619803):
<p>Because both <code>data/rbmap/default.lean</code> and <code>data/rbmap/default.olean</code> are found, that function raises an "ambiguous import" exception. Then <code>display_deps</code> catches the exception and reports an uninformative "file not found" error message.</p>

#### [ Reid Barton (Oct 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619828):
<p>You may want to verify this by inserting tracing printfs and/or having <code>display_deps</code> show the original exception</p>

#### [ Simon Hudon (Oct 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619830):
<p>Wow! you're fast!</p>

#### [ Sebastian Ullrich (Oct 11 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619917):
<p>Nice work! This is the code the regular path uses for importing, you may want to adapt that <a href="https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/src/library/module_mgr.cpp" target="_blank" title="https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/src/library/module_mgr.cpp">https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/src/library/module_mgr.cpp</a></p>

#### [ Reid Barton (Oct 11 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619925):
<p>I was just looking into this earlier (see my messages of 42 minutes ago)</p>

#### [ Sebastian Ullrich (Oct 11 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620046):
<p>Note that this code already looks completely different in Lean 4. So fixing this would only make sense if it was a big win for Lean 3 users (which a working <code>sccache</code> would probably be)</p>

#### [ Simon Hudon (Oct 11 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620153):
<p>I think it would be. It seems like a small fix on the Lean side and I'm hopeful <code>sccache</code> should be easily ported from Lean 3 to Lean 4 (once it works for Lean 3)</p>

#### [ Simon Hudon (Oct 11 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620168):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Can I leave that fix to you?</p>

#### [ Reid Barton (Oct 11 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620573):
<p>I can take a shot at it. We should make sure we have some working setup for <code>sccache</code> before upstreaming the change to Lean though. For testing purposes, you should be able to just remove <code>".olean"</code> from the list of extensions in <code>display_deps</code>.</p>

#### [ Simon Hudon (Oct 11 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620680):
<blockquote>
<p>we have some working setup for sccache before upstreaming the change to Lean though</p>
</blockquote>
<p>I think the fix is usable on its own. Why do you think we should wait?</p>

#### [ Reid Barton (Oct 11 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620813):
<p>Only because Lean 3 is currently in this state where it doesn't change without a particularly good reason</p>

#### [ Simon Hudon (Oct 11 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620982):
<p>It makes it harder to progress if we wait for everything to be ready before we push anything. If we do the heavy lifting, I don't think they will begrudge us fixing a problem even if the <code>sccache</code> idea doesn't pan out.</p>

#### [ Simon Hudon (Oct 11 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135624103):
<p>I just tried removing <code>.olean</code> from the list in <code>display_deps</code> and it's working. Is that a good enough fix?</p>

#### [ Reid Barton (Oct 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135627574):
<p>It seems like it should be good enough for us, though there could be other bugs lurking underneath. The other question is whether it would break any other users of Lean and specifically of <code>lean --deps</code>. The only way I could imagine the change breaking a working system is if that system uses out-of-tree builds (output <code>.olean</code> files not located in the same place as the corresponding source files) and also relies on <code>.olean</code> files as inputs without corresponding source <code>.lean</code> files. That seems pretty unlikely to me, considering that lean's library itself is not built out-of-tree, so at a minimum the implicit import of <code>init</code> will fail.</p>

#### [ Simon Hudon (Oct 11 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135627687):
<p>That's also my impression. I wonder if they had anything else in mind when they put <code>.olean</code> in that list.</p>

#### [ Simon Hudon (Oct 11 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135627908):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Here's the fix that did it for me: <a href="https://github.com/cipher1024/lean/commit/d2d81a3539bdf952eaf6126d2be69f2fda0b2f1f" target="_blank" title="https://github.com/cipher1024/lean/commit/d2d81a3539bdf952eaf6126d2be69f2fda0b2f1f">https://github.com/cipher1024/lean/commit/d2d81a3539bdf952eaf6126d2be69f2fda0b2f1f</a></p>

#### [ Simon Hudon (Oct 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135628632):
<p>Also, is <code>--make</code> the only way to produce <code>.olean</code> files? For me, even if I give a file name, it seems to build the whole project. Is there any way around that?</p>

#### [ Reid Barton (Oct 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135628799):
<p>It should only build the file you specify (and its dependencies if necessary)</p>

#### [ Simon Hudon (Oct 11 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135628948):
<p>You're right, I misinterpreted what I saw</p>

#### [ Simon Hudon (Oct 11 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135629007):
<p>Now with the fix, I managed to build a make file that discovers dependencies and builds what it needs.</p>

#### [ Tobias Grosser (Oct 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135629452):
<p>Nice!</p>

#### [ Simon Hudon (Oct 11 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135629798):
<p>I decided to go for bare minimum and only use <code>make</code>. We can make it more sophisticated once we see it is working.</p>

#### [ Tobias Grosser (Oct 11 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135629867):
<p>Seems like a good idea. Looking forward to checkout the make file.</p>

#### [ Simon Hudon (Oct 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135631243):
<p>I'll push it in a branch in a moment. If you have comments, I'd love to hear them</p>

#### [ Simon Hudon (Oct 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135631248):
<p>It won't be functional because I hard coded a path to my Lean version</p>

#### [ Sebastian Ullrich (Oct 11 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632212):
<p>You can use elan to manage your local Lean fork :)</p>

#### [ Simon Hudon (Oct 11 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632230):
<p>Niiice! How?</p>

#### [ Sebastian Ullrich (Oct 11 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632317):
<p><code>elan help toolchain link</code></p>

#### [ Sebastian Ullrich (Oct 11 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632390):
<p>"crate", oops</p>

#### [ Simon Hudon (Oct 11 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632476):
<p>Haha! I didn't even notice! I was thinking that you've been pretty thorough in replacing Rust with Lean :)</p>

#### [ Simon Hudon (Oct 11 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632579):
<p>Btw, have you looked at my commit?</p>

#### [ Sebastian Ullrich (Oct 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632845):
<p>Yeah, I think it should be fine. You can remove ".lua" too.</p>

#### [ Simon Hudon (Oct 11 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632879):
<p>Will do!</p>

#### [ Simon Hudon (Oct 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135634431):
<p>Here we go: <a href="https://github.com/leanprover/lean/pull/1978" target="_blank" title="https://github.com/leanprover/lean/pull/1978">https://github.com/leanprover/lean/pull/1978</a></p>

#### [ Simon Hudon (Oct 11 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135637248):
<p>Is it possible to use <code>elan</code> to refer to a specific git commit on github?</p>

#### [ Simon Hudon (Oct 12 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135641178):
<p><span class="user-mention" data-user-id="122318">@Tobias Grosser</span> here is what I did for the Makefile. It generates dependency files for each <code>.lean</code> file before it gets started building any files and the first time you get a lot of error messages because they are missing.</p>
<p><a href="https://github.com/leanprover-community/mathlib/commit/d090d711c0b438223479635b663e720dab2d07e7" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/d090d711c0b438223479635b663e720dab2d07e7">https://github.com/leanprover-community/mathlib/commit/d090d711c0b438223479635b663e720dab2d07e7</a></p>

#### [ Simon Hudon (Oct 12 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135642448):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> You use emacs right? What do you use for Rust?</p>

#### [ Tobias Grosser (Oct 12 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135655934):
<p>Nice. </p>
<blockquote>
<p><span class="user-mention" data-user-id="122318">@Tobias Grosser</span> here is what I did for the Makefile. It generates dependency files for each <code>.lean</code> file before it gets started building any files and the first time you get a lot of error messages because they are missing.</p>
<p><a href="https://github.com/leanprover-community/mathlib/commit/d090d711c0b438223479635b663e720dab2d07e7" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/d090d711c0b438223479635b663e720dab2d07e7">https://github.com/leanprover-community/mathlib/commit/d090d711c0b438223479635b663e720dab2d07e7</a></p>
</blockquote>
<p>Now just the sccache needs to work. I feel this might indeed be a great improvement. </p>
<p>Best Tobias</p>

#### [ Johan Commelin (Oct 16 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135919858):
<p>My laptop just crashed while compiling mathlib. This is the first time it crashed in a couple of years. We really need to make mathlib easier on prehistoric hardware <span class="emoji emoji-1f409" title="dragon">:dragon:</span></p>

#### [ Simon Hudon (Oct 16 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135923867):
<p>I'm sciencing as fast as I can ... it's coming</p>

#### [ Kenny Lau (Oct 16 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135924071):
<p>or we can make mathlib compile <em>faster</em></p>

#### [ Simon Hudon (Oct 16 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135924198):
<p>I don't think we should pick just one</p>

#### [ Scott Morrison (Nov 19 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996200):
<p>Hi <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, would you have time to give a status update on <code>sccache</code> integration, in particular pointing out if there are places someone else could help write code/investigate issues/do some research?</p>

#### [ Simon Hudon (Nov 19 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996348):
<p>Sure. I can push what I currently have</p>

#### [ Simon Hudon (Nov 19 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996392):
<p>What I did is provide a way for sscache to determine if an olean file is outdated or not through hashing.</p>

#### [ Simon Hudon (Nov 19 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996477):
<p>I'm still struggling to get the tests to pass. I think once that work, we should have a version sscache that can locally cache any lean build we like.</p>

#### [ Simon Hudon (Nov 19 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996521):
<p>I wrote a Makefile to take advantage of it and I pushed it on leanprover-community. I also made a patch to lean itself to fix the way it computes dependencies</p>

#### [ Simon Hudon (Nov 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996650):
<p>After I'm done with this part, one possible extension (if you want to spend the time) is figure out how to get some cloud storage to store a Lean cache. That would involve configuring sccache itself and setting up instructions for people who want to access the cache.</p>

#### [ Simon Hudon (Nov 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996663):
<p>At this point I see that more as goody than as a must have though</p>

#### [ Scott Morrison (Nov 20 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148010429):
<p>I pushed two minor changes to the <code>build-system</code> branch.</p>

#### [ Scott Morrison (Nov 21 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148089909):
<p>Where is that "is an olean file outdated, via hashing" code?</p>

#### [ Scott Morrison (Nov 21 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090026):
<p>Using timestamps to decide whether to recompile makes life really difficult. Do we know an obstacle (besides patching Lean), to instead have each olean file contain a hash of its source file and of the olean files for each of its imports? To decide if an olean file is stale or not you would read those hash from the olean file, and compare them against the current hashes of those files.</p>

#### [ Scott Morrison (Nov 21 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090031):
<p>Once one <code>.lean</code> file changes, this would propagate staleness of all dependent <code>.olean</code> files.</p>

#### [ Scott Morrison (Nov 21 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090032):
<p>And no timestamps would ever be considered.</p>

#### [ Scott Morrison (Nov 21 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090072):
<p>Or, <span class="user-mention" data-user-id="110026">@Simon Hudon</span>, is this what you've already done?</p>

#### [ Simon Hudon (Nov 21 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090145):
<p>That's what I'm working on yes. More exactly, when calling <code>sccache lean --make foo.lean</code>, we get the list of modules imported (directly or indirectly) by <code>foo.lean</code>, we hash all of them (including <code>foo.lean</code>) and recompile only if that hash changes.</p>

#### [ Scott Morrison (Nov 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090216):
<p>I see -- you hash the source files of the imports, or the olean files?</p>

#### [ Scott Morrison (Nov 21 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090260):
<p>And this is all being done by the sccache wrapper, with no modification of Lean?</p>

#### [ Simon Hudon (Nov 21 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090261):
<p>The sources</p>

#### [ Simon Hudon (Nov 21 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090263):
<p>That's correct</p>

#### [ Scott Morrison (Nov 21 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090270):
<p>But won't we then get burnt still by Lean being wrong about what is stale?</p>

#### [ Simon Hudon (Nov 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090279):
<p>I'd like to hash the olean but all the ways I have thought of are flawed</p>

#### [ Simon Hudon (Nov 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090284):
<p>What do you mean?</p>

#### [ Scott Morrison (Nov 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090288):
<p>Say we have files A &lt; B &lt; C, and A and B are already built correctly, according to their hashes, while C needs to be rebuilt.</p>

#### [ Scott Morrison (Nov 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090292):
<p>But suppose the timestamps on A.olean and B.olean are messed up.</p>

#### [ Scott Morrison (Nov 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090339):
<p>When sccache invokes Lean on C.lean, what is to stop Lean from going and recompiling A and B?</p>

#### [ Simon Hudon (Nov 21 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090365):
<p>I don't think this will be happening but I have to double check. Maybe <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> can tell us. If we call <code>lean --make foo.lean</code>, will Lean attempt to rebuild any of the dependencies? If so, is there a way to tell it not to?</p>

#### [ Simon Hudon (Nov 21 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090473):
<p>One thing I have considered is to manually set the modification time of the <code>olean</code> files when they don't need to be rebuilt. That should solve the issue.</p>

#### [ Sebastian Ullrich (Nov 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148095554):
<p>Yeah, that's what I would have proposed, too</p>

#### [ Johan Commelin (Dec 15 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/151848308):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> <span class="user-mention" data-user-id="110026">@Simon Hudon</span> Any updates on the caching front? (Yes, indeed, I thought of it again because I'm currently recompiling... <span class="emoji emoji-1f606" title="lol">:lol:</span>)</p>

#### [ Simon Hudon (Dec 15 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/151848324):
<p>Haha! I actually managed to make progress on it today and yesterday. Now I'm testing it and I'm hoping I can roll out a version soon</p>

#### [ Johan Commelin (Dec 15 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/151848327):
<p>Awesome news!</p>

#### [ Simon Hudon (Dec 17 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/152043694):
<p>I managed to build a version that passes all their tests:</p>
<p><a href="https://github.com/leanprover-community/sccache/tree/lean-support-2" target="_blank" title="https://github.com/leanprover-community/sccache/tree/lean-support-2">https://github.com/leanprover-community/sccache/tree/lean-support-2</a></p>

#### [ Simon Hudon (Dec 17 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/152043765):
<p>When I try it with my Makefile though, it fails. There seems to be issue with the timing when <code>sccache</code> produces the binaries</p>

#### [ Simon Hudon (Dec 17 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/152043832):
<p>If someone wants to try it for themselves, I can share the Makefile</p>


{% endraw %}
