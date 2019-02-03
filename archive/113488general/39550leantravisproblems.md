---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39550leantravisproblems.html
---

## Stream: [general](index.html)
### Topic: [lean travis problems](39550leantravisproblems.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 29 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357753):
<p><a href="https://travis-ci.org/leanprover/lean/jobs/359716662#L1465" target="_blank" title="https://travis-ci.org/leanprover/lean/jobs/359716662#L1465">https://travis-ci.org/leanprover/lean/jobs/359716662#L1465</a></p>

#### [ Kenny Lau (Mar 29 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357759):
<p>lol</p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357892):
<p>travis is a real headache at the minute, but it affects end users because if mathlib works with lean HEAD but travis doesn't like lean HEAD then the nightly doesn't appear, and then end users who use the nightlies (like me) on more than one machine (like me) find themselves in situations where the nightly on one machine is too old for some reason, but the canonical upgrade process ("upgrade to current lean nightly and mathlib head") doesn't work.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357952):
<p>Is travis trying to be too clever? I would imagine that Leo / Sebastian don't usually commit versions of Lean which don't compile for them.</p>

#### [ Gabriel Ebner (Mar 29 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124357965):
<p>The failure is in the external smt2_interface package.</p>

#### [ Gabriel Ebner (Mar 29 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358009):
<p>And it shouldn't affect nightlies (they are uploaded in another configuration)</p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358010):
<p>Oh that's good :-)</p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358069):
<p>Since the recent incident where I upgraded Lean using my usual process and found mathlib not compiling, I've tried to become more aware of what actually happens here. So travis can give a red X at <a href="https://github.com/leanprover/lean/commits/master" target="_blank" title="https://github.com/leanprover/lean/commits/master">https://github.com/leanprover/lean/commits/master</a> after a new commit but the nightly might change anyway?</p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358088):
<p>Note that 8 out of the last 10 commits have been given red X's. Usually I would not care, but recent events have made me more cautious.</p>

#### [ Kenny Lau (Mar 29 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358094):
<p>or just use git</p>

#### [ Gabriel Ebner (Mar 29 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358144):
<blockquote>
<p>Note that 8 out of the last 10 commits have been given red X's.</p>
</blockquote>
<p>That's a diplomatic way to say "none of the last 20 builds have been successful". <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358156):
<p>I know I can use git Kenny, I am more concerned with people like Chris, who really don't want to have to download a bunch of stuff onto their (possibly low-spec) machine so they can spend hours compiling Lean.</p>

#### [ Gabriel Ebner (Mar 29 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358200):
<p>There's already a PR for smt2_interface, I'll merge it and then travis should be green again.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358215):
<p>I hope I'm not nagging. I just saw the effects of travis failure recently and was hoping not to have to go through it again. When Lean 3.4 appears there will be an alternative solution -- "get to 3.4 and then don't upgrade again".</p>

#### [ Kenny Lau (Mar 29 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358219):
<p>stop that "don't upgrade again" crap</p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358270):
<p>Kenny I need a solution which works for people who don't want to be bothered by upgrades. Imagine if all the software on your computer needed upgrading constantly and you had to build it from source.</p>

#### [ Kenny Lau (Mar 29 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358278):
<p>not all softwares are beta</p>

#### [ Kevin Buzzard (Mar 29 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358376):
<p>In practice I get people coming to Xena on Thursdays and they have managed to put their Lean in an unusable state and I just want to fix it with "download the nightly, use leanpkg upgrade/build, that's the end". This happened with Luca recently. He had edited a file in mathlib and then reverted his edits, but ended up with an olean file which did not match his lean file and this produced strange errors. We downloaded the nightly and fixed it really quickly. But with Chris more recently this approach did not work. Luca can't compile Lean from source without a huge amount of hassle.</p>

#### [ Gabriel Ebner (Mar 29 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358651):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> The latest nightly is from Tuesday, did you expect a newer one?</p>

#### [ Gabriel Ebner (Mar 29 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358673):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> What is the recommended way to get nightlies in travis scripts these days (i.e. for mathib, etc.)?</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358828):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  I was just expressing concern about the recent red X's. I have not cared about them in the past, but then they bit me, so now I am more wary.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358841):
<p>Basically I reported a lean assertion violation in the lean issues tracker, and then thought "hmm maybe I should upgrade to the latest nightly to check it's still there" and then I thought "but wait, there's a red X so there's a chance that upgrading will break mathlib, which is far more of a problem to me than anything else"</p>

#### [ Gabriel Ebner (Mar 29 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358856):
<p>To be fair, mathlib is broken with the current nightly.  (The <code>unit_eq</code> lemma is gone.)</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358906):
<p>My algorithm for dealing with the fact that this is beta software is "upgrade to latest nightly iff it won't cause a problem with mathlib".</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358949):
<p>My current test for this is "are there any signs of red X's in the list of commits? If not, was the last mathlib commit some time after the last Lean commit? If so, upgrade!"</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124358966):
<p>I would be happy to be told about better tests. Ideally I want to be able to do the tests without bothering anyone else, but I would rather fail in the sense that I didn't upgrade when upgrading was possible, because failing by upgrading and then finding mathlib doesn't compile hurts me more (it's harder to roll back).</p>

#### [ Gabriel Ebner (Mar 29 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359097):
<p>Why is it hard to roll back?  You can just download the previous nightly.  If you haven't seen it yet: <a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a></p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359107):
<p>It's hard to roll back because <code>leanpkg upgrade</code> upgrades mathlib to HEAD</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359110):
<p>so I have to manually intervene and figure out which version of mathlib I had before and then switch to this commit.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359150):
<p>and in the past I have not made a note of which commit I was switching from.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359166):
<p>More generally, when students have done something dumb like editing mathlib files and they were using a nightly from 2 months ago, if the current nightly does not work then I have to decide which version of mathlib to checkout with which version of the nightly.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359169):
<p>These are problems I actually see in practice.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359271):
<p>I am well aware that this is software which is not quite "end-user ready" yet, but somehow I am just trying to give examples of the problems I see and am hoping that we are actually almost in a position to be able to solve them. I had not seen the nightly releases link -- thanks. I had heard talk about it but I hadn't really understood that it had happened.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359283):
<p>If leanpkg could download the "approved mathlib commit" for each of the nightlies then this would be perfect. But maybe this is asking too much. I should however be able to download the nightly onto a student's machine, look at the commit #, and then guess an appropriate mathlib commit.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359321):
<p>This is important because it means I don't need to compile Lean on a student's machine.</p>

#### [ Sebastian Ullrich (Mar 29 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124359348):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span></p>
<blockquote>
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> What is the recommended way to get nightlies in travis scripts these days (i.e. for mathib, etc.)?</p>
</blockquote>
<p>I was planning to figure out a script that also correctly takes <code>lean_version</code> into account, but at that point we're halfway to a proper <code>leanget</code> application that would also be useful to end users...</p>

#### [ Sebastian Ullrich (Mar 29 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124362031):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> I guess this works :)</p>
<div class="codehilite"><pre><span></span>curl -s https://api.github.com/repos/leanprover/lean-nightly/releases | jq -r &#39;.[0].assets | map(select(.name | contains(&quot;linux&quot;))) | .[0].browser_download_url&#39;
</pre></div>

#### [ Kevin Buzzard (Mar 29 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124363946):
<p>I wonder if it works on a fresh OS X install?</p>

#### [ Kenny Lau (Mar 30 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124430175):
<p>why does the latest build fail?</p>

#### [ Kenny Lau (Mar 31 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20travis%20problems/near/124433328):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>


{% endraw %}
