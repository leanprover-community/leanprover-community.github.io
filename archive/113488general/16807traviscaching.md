---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16807traviscaching.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [travis caching](https://leanprover-community.github.io/archive/113488general/16807traviscaching.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (May 31 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127367872):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Could you help me try to set up build caching on travis? The from-scratch build times are nearing the time limit for public jobs. I tried following <a href="https://docs.travis-ci.com/user/caching/" target="_blank" title="https://docs.travis-ci.com/user/caching/">https://docs.travis-ci.com/user/caching/</a> but I can't find the <em>Build branch updates</em> option.</p>

#### [ Gabriel Ebner (May 31 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127369867):
<p>I think this option is now called "build pushed branches".</p>

#### [ Gabriel Ebner (May 31 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370039):
<p>I'm not sure the caching feature will fix the timeouts though.  The cache is only saved when a build is completed.  The next time somebody changes <code>tactic/interactive.lean</code> everything will need to be rebuilt, the build won't finish, and the cache remains out of date (forever, since all future builds fail as well).</p>

#### [ Simon Hudon (May 31 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370064):
<p>If you want to separate a preparatory step, you can use build stages.</p>

#### [ Gabriel Ebner (May 31 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370225):
<p>I don't see any good way to break up the build into stages though.  The main <code>lean --make</code> invocation takes almost an hour (is that right?  it's much faster locally?), and we need to cache its output.</p>

#### [ Simon Hudon (May 31 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370341):
<p>can we build a few directories in the first stage and then the rest?</p>

#### [ Gabriel Ebner (May 31 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370819):
<p>That's one option.  2) We could break up mathlib into multiple repositories, add binary releases, and then use the binary releases for travis in the dependent repositories.  This is also a bit of work, and the development workflow is probably worse.  3)  Probably the least effort: somebody sets up a machine with Jenkins somewhere (<span class="user-mention" data-user-id="110049">@Mario Carneiro</span>?).  Then mathlib can build for hours (probably less, a full mathlib build only takes a bit over 9 minutes here).</p>

#### [ Simon Hudon (May 31 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370904):
<p>I do not believe 3) is the least effort. The people I know who have their own Jenkins setup say that it's much more trouble than using Travis.</p>

#### [ Simon Hudon (May 31 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370978):
<p>You could probably do a mix of 1) and 2) and create different subsets of mathlib that will build in separate stages on Travis</p>

#### [ Gabriel Ebner (May 31 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127371131):
<p>Jenkins has a bit of a learning curve since you can't copy a random <code>.travis.yml</code>.  But executing three lines of shell script is pretty easy, you just need to insert it as a build step.  Fighting with travis build stages and caching may be more work.  We've had a pretty good experience with jenkins in our group.</p>

#### [ Gabriel Ebner (May 31 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127372187):
<p>I just wanted to bring it up as an option, it took me about a minute to set up mathlib in jenkins (12 minutes build time): <a href="http://clogic92.dmg.tuwien.ac.at/job/mathlib/2/console" target="_blank" title="http://clogic92.dmg.tuwien.ac.at/job/mathlib/2/console">http://clogic92.dmg.tuwien.ac.at/job/mathlib/2/console</a>  (GH integration and zulip notification is not much more work.)  The main problem is of course hosting, so if we can easily fix travis then this is probably the way to go.</p>

#### [ Simon Hudon (May 31 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127372267):
<p>Nice! Do you need to dedicate your own computer or can you put it only on something like AWS?</p>

#### [ Gabriel Ebner (May 31 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127372439):
<p>You can of course use AWS, but that probably gets pricy.  It is probably easier and cheaper to host it at a university.</p>

#### [ Simon Hudon (May 31 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127372946):
<p>That's probably easier than maintaining the machines yourself too</p>

#### [ Johan Commelin (May 31 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375769):
<p>Maybe CoCalc wants to help, and has the experience? I have no clue if they would be open to something like that?</p>

#### [ Johan Commelin (May 31 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375778):
<p>Maybe we should just ask William... <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> what do you think?</p>

#### [ Johan Commelin (May 31 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375786):
<p>You know him best.</p>

#### [ Kevin Buzzard (May 31 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375832):
<p>I know him but I have no understanding of this thread</p>

#### [ Johan Commelin (May 31 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375849):
<p>We are talking about a self-hosted Travis replacement. Where we can have compile times &gt;1hr.</p>

#### [ Johan Commelin (May 31 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375866):
<p>But self-hosting implies that you have to maintain stuff</p>

#### [ Johan Commelin (May 31 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376502):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> <span class="user-mention" data-user-id="110026">@Simon Hudon</span> I don't know if you guys are familiar with CoCalc. It is a cloud environment for scientific computing. And William is a mathematician who is interested in Lean. So that helps.</p>

#### [ Johan Commelin (May 31 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376614):
<p>William is interested in Lean in the sense that he wants to make it available in CoCalc, once he has figured out how to make a good user interface for it.</p>

#### [ Simon Hudon (May 31 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376638):
<p>Cool! Does he not like the online version?</p>

#### [ Johan Commelin (May 31 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376645):
<p>If you guys want to consider the Jenkins approach, and would like me to ask William, just tell me.</p>

#### [ Johan Commelin (May 31 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376662):
<p>The online version is way to slow when you want to do serious stuff. And it is not collaborative.</p>

#### [ Johan Commelin (May 31 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376681):
<p>With CoCalc you would have fast servers running Lean, and just a UI in the browser.</p>

#### [ Simon Hudon (May 31 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376687):
<p>You want it to be like Google Docs or just have some git support?</p>

#### [ Johan Commelin (May 31 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376732):
<p>So far he has collaborative editors for LaTeX (with live preview) and Python (+ all its scientific extensions), Jupyter etc...</p>

#### [ Johan Commelin (May 31 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376740):
<p>No, Google Docs like</p>

#### [ Johan Commelin (May 31 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376748):
<p>But a VScode-like UI</p>

#### [ Johan Commelin (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376834):
<p>So, they definitely have the computing power for the Jenkins instance. The question is if they want to support it. (They don't have that much staff...)</p>

#### [ Simon Hudon (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376846):
<p>VSCode is available online for some languages: <a href="https://stackblitz.com/" target="_blank" title="https://stackblitz.com/">https://stackblitz.com/</a> maybe that would help</p>

#### [ Johan Commelin (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376853):
<p>Yes, I gave him that link.</p>

#### [ Simon Hudon (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376859):
<p>Cool</p>

#### [ Johan Commelin (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376862):
<p>But now you need to add in collaboration, and the Lean extension.</p>

#### [ Scott Morrison (Jun 01 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127389254):
<p>I don't think we should be asking William Stein to help us with things like travis.</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127391794):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> I'm okay with self-hosting Jenkins, provided that it doesn't need 100% uptime. That is, the server does not need to be running when someone pushes a commit, it just builds when it's available</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127391801):
<p>I don't know that much about Jenkins though</p>

#### [ Mario Carneiro (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127391816):
<p>Not sure about available CMU resources</p>

#### [ Gabriel Ebner (Jun 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127404557):
<p>I don't think running Jenkins on your laptop is a good idea.  It should have a public IP so that other people can look at the build logs in case of failure.  (But you don't need six nines availability either.)</p>

#### [ Mario Carneiro (Jun 03 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127479860):
<p>Simon suggested that we use a staged build <a href="https://docs.travis-ci.com/user/build-stages/" target="_blank" title="https://docs.travis-ci.com/user/build-stages/">https://docs.travis-ci.com/user/build-stages/</a> , since the different jobs have independent timeouts. The idea would be to run <code>lean --make</code> for 45 minutes or so in the first job, and then always succeed and update the cache. Then stage 2 would be a regular lean build using the artifacts from the first run. <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Could you see if this works with the caching? Travis documentation suggests using S3 for common files so I'm not sure if the cache sharing trick will work.</p>

#### [ Simon Hudon (Jun 03 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127479873):
<p>What do you mean by the cache sharing trick?</p>

#### [ Simon Hudon (Jun 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127480016):
<p>Rather: why do you think that sharing cache between phases might not work?</p>

#### [ Mario Carneiro (Jun 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127480017):
<p>They run in separate VMs</p>

#### [ Simon Hudon (Jun 03 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127480560):
<p>Ok but when I used it, my later stages inherited the cache from the early stages. I don't see why that wouldn't happen for mathlib</p>

#### [ Scott Morrison (Jun 04 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127539236):
<p>I just investigated setting up a copy of Jenkins (it's easy!), but couldn't get too far. When I asked it to scan the leanprover organization on github, it quickly errored: it asks for things through the API that only people with commit access can use:</p>
<div class="codehilite"><pre><span></span>ERROR: [Mon Jun 04 20:46:32 AEST 2018] Could not fetch sources from navigator org.jenkinsci.plugins.github_branch_source.GitHubSCMNavigator@48f109dc
java.io.FileNotFoundException: https://api.github.com/repos/leanprover/lean/collaborators/Kha/permission
    at com.squareup.okhttp.internal.huc.HttpURLConnectionImpl.getInputStream(HttpURLConnectionImpl.java:243)
    at com.squareup.okhttp.internal.huc.DelegatingHttpsURLConnection.getInputStream(DelegatingHttpsURLConnection.java:210)
    at com.squareup.okhttp.internal.huc.HttpsURLConnectionImpl.getInputStream(HttpsURLConnectionImpl.java:25)
    at org.kohsuke.github.Requester.parse(Requester.java:612)
    at org.kohsuke.github.Requester.parse(Requester.java:594)
    at org.kohsuke.github.Requester._to(Requester.java:272)
Caused: org.kohsuke.github.GHFileNotFoundException: {&quot;message&quot;:&quot;Must have push access to view collaborator permission.&quot;,&quot;documentation_url&quot;:&quot;https://developer.github.com/v3/repos/collaborators/#review-a-users-permission-level&quot;}
    at org.kohsuke.github.Requester.handleApiError(Requester.java:686)
    at org.kohsuke.github.Requester._to(Requester.java:293)
    at org.kohsuke.github.Requester.to(Requester.java:234)
    at org.kohsuke.github.GHRepository.getPermission(GHRepository.java:502)
    at org.jenkinsci.plugins.github_branch_source.GitHubSCMSource$1.fetch(GitHubSCMSource.java:874)
    at org.jenkinsci.plugins.github_branch_source.GitHubSCMSourceRequest.getPermissions(GitHubSCMSourceRequest.java:474)
    at
</pre></div>

#### [ Johan Commelin (Jun 04 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540280):
<p>Can you get it to work with one of your own lean repos?</p>

#### [ Scott Morrison (Jun 04 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540943):
<p>I got Jenkins to read the .travis.yml file from one of my own repos, and it starts off happily enough, but then says:</p>
<div class="codehilite"><pre><span></span>leanpkg test
OSX &#39;readlink&#39; command does not support option &#39;-f&#39;, please install &#39;greadlink&#39;. If you use &#39;brew&#39;, you can install &#39;greadlink&#39; using &#39;brew install coreutils&#39;
</pre></div>

#### [ Scott Morrison (Jun 04 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540984):
<p><code>coreutils</code> is already installed, and <code>leanpkg test</code> works just fine on the command line. :-(</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540996):
<p>Different <code>PATH</code>s, probably?</p>

#### [ Johan Commelin (Jun 04 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540998):
<p>Hmmm, I don't know how to help you with that one. (I don't really have any Jenkins experience myself.) Are you on a Mac? Or is Jenkins just very Mac-oriented?</p>

#### [ Scott Morrison (Jun 04 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127541257):
<p>I think I'm going to pause my Jenkins experiments for now. (I have a big fat machine with plenty of RAM and cores, with a fixed IP address, but I would have to negotiate some holes in firewalls with my ... uncooperative ... IT staff.)</p>

#### [ Johan Commelin (Jun 04 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127541270):
<p>Aah, yes, I forgot that William isn't the only one with big fat machines. So do you (-;</p>

#### [ Gabriel Ebner (Jun 05 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127592452):
<p>I think the easiest way to setup jenkins with github nowadays is to use the blue ocean interface with Jenkinsfile (docs <a href="https://jenkins.io/doc/book/blueocean/getting-started/" target="_blank" title="https://jenkins.io/doc/book/blueocean/getting-started/">here</a> and <a href="https://jenkins.io/doc/book/blueocean/creating-pipelines/" target="_blank" title="https://jenkins.io/doc/book/blueocean/creating-pipelines/">here</a>).  All you need to do is install elan and add <a href="https://github.com/gebner/mathlib/blob/master/Jenkinsfile" target="_blank" title="https://github.com/gebner/mathlib/blob/master/Jenkinsfile">this file to the repo</a>.  Then everything seems to work out of the box, including status information on PRs (<a href="https://github.com/gebner/mathlib/pull/1" target="_blank" title="https://github.com/gebner/mathlib/pull/1">look here</a>).  (This is a linux machine btw, and we use it for another project so I can't easily repurpose it for mathlib.)<br>
You definitely want a public IP with an open http port so people can look at the build log.  On the permission side, I think anybody in the lean github organization can authorize it.  The best way to automatically trigger jenkins is via webhooks, then it starts building a few seconds after a PR gets created or a commit is pushed.  Unfortunately I can't create webhooks on <em>any</em> of the lean projects.  In the worst case, jenkins can poll github in regular intervals.</p>

#### [ Scott Morrison (Jun 07 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127693739):
<p>So while I have a machine I can run Jenkins on, it seems there’s no way I can convince local IT people to let that Jenkins interface be publicly accessible. I could set it up to poll github in order to initiate builds, but I’d need some mechanism to output the build logs to a web server. If anyone knows of an out-of-the-box solution to this, I’m happy to pursue it, but perhaps there are better avenues.</p>

#### [ Johan Commelin (Jun 07 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127695721):
<p>Can't you have it push the build logs by ssh to some web server?</p>

#### [ Scott Morrison (Jun 07 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127695909):
<p>Yes, that's what I had in mind. I guess I was asking if someone knows of an easy-to-configure Jenkins plugin that does this. I'd be happy to contribute hardware and a little setup time, but I don't want to feel responsible for managing an intricate web of scripts. :-)</p>

#### [ Reid Barton (Jan 30 2019 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157223784):
<p>from <code>.travis.yml</code>:</p>
<div class="codehilite"><pre><span></span>  - rm `git status | grep &quot;\.lean&quot; | sed &quot;s/\.lean/.olean/&quot;` ||  true
  - rm `git status | grep &quot;\.lean&quot;` || true
</pre></div>


<p>Is there a reason we couldn't replace this with</p>
<div class="codehilite"><pre><span></span>  - git clean -d -f
</pre></div>


<p>This should remove all untracked files, which I think is what the <code>rm</code> lines are trying to accomplish, while leaving ignored files, e.g. built <code>.olean</code> files.</p>

#### [ Reid Barton (Jan 30 2019 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157224087):
<p>The <code>rm</code> lines failed for <a href="https://github.com/leanprover/mathlib/issues/641" target="_blank" title="https://github.com/leanprover/mathlib/issues/641">#641</a>, because the cache contained an entire directory left over from a rename, and in that situation <code>git status</code> only reports the directory as a whole as untracked.</p>

#### [ Kevin Buzzard (Jan 30 2019 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157224385):
<p>641 divides <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>2</mn><msup><mn>2</mn><mn>5</mn></msup></msup><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">2^{2^5}+1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9869199999999999em;"></span><span class="strut bottom" style="height:1.07025em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord"><span class="mord mathrm">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9869199999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight"><span class="mord mathrm mtight">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8913142857142857em;"><span style="top:-2.931em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">5</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord mathrm">1</span></span></span></span>, the 5th Fermat number, disproving a conjecture of Fermat.</p>

#### [ Reid Barton (Jan 30 2019 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157224926):
<p>Oh wait this won't actually work, because the old <code>.olean</code> files will still be left behind and lean will use them (argh)</p>

#### [ Sebastian Ullrich (Jan 30 2019 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157225645):
<p><code>git clean</code> first, then remove all .olean files without corresponding .lean file?</p>

#### [ Reid Barton (Jan 30 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157225832):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> and I arrived at the same conclusion</p>

#### [ Sebastian Ullrich (Jan 30 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157225861):
<p>Definitely an improvement over the old code :)</p>

#### [ Reid Barton (Jan 30 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157226203):
<p>By the way, GHC seems to ignore object files without matching source files. I think that's a better behavior than Lean's</p>

#### [ Reid Barton (Jan 30 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/157226787):
<p>GHC is also pretty smart about not recompiling downstream modules if a dependency was modified in a way that can't affect clients. It might be worth borrowing those techniques at some point, though I don't know how effective they would be in the Lean world</p>


{% endraw %}
