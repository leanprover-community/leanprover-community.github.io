---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16807traviscaching.html
---

## Stream: [general](index.html)
### Topic: [travis caching](16807traviscaching.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 31 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127367872):
@**Gabriel Ebner** Could you help me try to set up build caching on travis? The from-scratch build times are nearing the time limit for public jobs. I tried following https://docs.travis-ci.com/user/caching/ but I can't find the *Build branch updates* option.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 31 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127369867):
I think this option is now called "build pushed branches".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 31 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370039):
I'm not sure the caching feature will fix the timeouts though.  The cache is only saved when a build is completed.  The next time somebody changes `tactic/interactive.lean` everything will need to be rebuilt, the build won't finish, and the cache remains out of date (forever, since all future builds fail as well).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370064):
If you want to separate a preparatory step, you can use build stages.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 31 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370225):
I don't see any good way to break up the build into stages though.  The main `lean --make` invocation takes almost an hour (is that right?  it's much faster locally?), and we need to cache its output.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370341):
can we build a few directories in the first stage and then the rest?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 31 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370819):
That's one option.  2) We could break up mathlib into multiple repositories, add binary releases, and then use the binary releases for travis in the dependent repositories.  This is also a bit of work, and the development workflow is probably worse.  3)  Probably the least effort: somebody sets up a machine with Jenkins somewhere (@**Mario Carneiro**?).  Then mathlib can build for hours (probably less, a full mathlib build only takes a bit over 9 minutes here).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370904):
I do not believe 3) is the least effort. The people I know who have their own Jenkins setup say that it's much more trouble than using Travis.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127370978):
You could probably do a mix of 1) and 2) and create different subsets of mathlib that will build in separate stages on Travis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 31 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127371131):
Jenkins has a bit of a learning curve since you can't copy a random `.travis.yml`.  But executing three lines of shell script is pretty easy, you just need to insert it as a build step.  Fighting with travis build stages and caching may be more work.  We've had a pretty good experience with jenkins in our group.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 31 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127372187):
I just wanted to bring it up as an option, it took me about a minute to set up mathlib in jenkins (12 minutes build time): http://clogic92.dmg.tuwien.ac.at/job/mathlib/2/console  (GH integration and zulip notification is not much more work.)  The main problem is of course hosting, so if we can easily fix travis then this is probably the way to go.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127372267):
Nice! Do you need to dedicate your own computer or can you put it only on something like AWS?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 31 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127372439):
You can of course use AWS, but that probably gets pricy.  It is probably easier and cheaper to host it at a university.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127372946):
That's probably easier than maintaining the machines yourself too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375769):
Maybe CoCalc wants to help, and has the experience? I have no clue if they would be open to something like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375778):
Maybe we should just ask William... @**Kevin Buzzard** what do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375786):
You know him best.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 31 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375832):
I know him but I have no understanding of this thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375849):
We are talking about a self-hosted Travis replacement. Where we can have compile times >1hr.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127375866):
But self-hosting implies that you have to maintain stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376502):
@**Mario Carneiro** @**Gabriel Ebner** @**Simon Hudon** I don't know if you guys are familiar with CoCalc. It is a cloud environment for scientific computing. And William is a mathematician who is interested in Lean. So that helps.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376614):
William is interested in Lean in the sense that he wants to make it available in CoCalc, once he has figured out how to make a good user interface for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376638):
Cool! Does he not like the online version?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376645):
If you guys want to consider the Jenkins approach, and would like me to ask William, just tell me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376662):
The online version is way to slow when you want to do serious stuff. And it is not collaborative.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376681):
With CoCalc you would have fast servers running Lean, and just a UI in the browser.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376687):
You want it to be like Google Docs or just have some git support?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376732):
So far he has collaborative editors for LaTeX (with live preview) and Python (+ all its scientific extensions), Jupyter etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376740):
No, Google Docs like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376748):
But a VScode-like UI

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376834):
So, they definitely have the computing power for the Jenkins instance. The question is if they want to support it. (They don't have that much staff...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376846):
VSCode is available online for some languages: https://stackblitz.com/ maybe that would help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376853):
Yes, I gave him that link.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376859):
Cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127376862):
But now you need to add in collaboration, and the Lean extension.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 01 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127389254):
I don't think we should be asking William Stein to help us with things like travis.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127391794):
@**Gabriel Ebner** I'm okay with self-hosting Jenkins, provided that it doesn't need 100% uptime. That is, the server does not need to be running when someone pushes a commit, it just builds when it's available

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127391801):
I don't know that much about Jenkins though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 01 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127391816):
Not sure about available CMU resources

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127404557):
I don't think running Jenkins on your laptop is a good idea.  It should have a public IP so that other people can look at the build logs in case of failure.  (But you don't need six nines availability either.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127479860):
Simon suggested that we use a staged build https://docs.travis-ci.com/user/build-stages/ , since the different jobs have independent timeouts. The idea would be to run `lean --make` for 45 minutes or so in the first job, and then always succeed and update the cache. Then stage 2 would be a regular lean build using the artifacts from the first run. @**Gabriel Ebner** Could you see if this works with the caching? Travis documentation suggests using S3 for common files so I'm not sure if the cache sharing trick will work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127479873):
What do you mean by the cache sharing trick?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127480016):
Rather: why do you think that sharing cache between phases might not work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127480017):
They run in separate VMs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 03 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127480560):
Ok but when I used it, my later stages inherited the cache from the early stages. I don't see why that wouldn't happen for mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127539236):
I just investigated setting up a copy of Jenkins (it's easy!), but couldn't get too far. When I asked it to scan the leanprover organization on github, it quickly errored: it asks for things through the API that only people with commit access can use:
````
ERROR: [Mon Jun 04 20:46:32 AEST 2018] Could not fetch sources from navigator org.jenkinsci.plugins.github_branch_source.GitHubSCMNavigator@48f109dc
java.io.FileNotFoundException: https://api.github.com/repos/leanprover/lean/collaborators/Kha/permission
	at com.squareup.okhttp.internal.huc.HttpURLConnectionImpl.getInputStream(HttpURLConnectionImpl.java:243)
	at com.squareup.okhttp.internal.huc.DelegatingHttpsURLConnection.getInputStream(DelegatingHttpsURLConnection.java:210)
	at com.squareup.okhttp.internal.huc.HttpsURLConnectionImpl.getInputStream(HttpsURLConnectionImpl.java:25)
	at org.kohsuke.github.Requester.parse(Requester.java:612)
	at org.kohsuke.github.Requester.parse(Requester.java:594)
	at org.kohsuke.github.Requester._to(Requester.java:272)
Caused: org.kohsuke.github.GHFileNotFoundException: {"message":"Must have push access to view collaborator permission.","documentation_url":"https://developer.github.com/v3/repos/collaborators/#review-a-users-permission-level"}
	at org.kohsuke.github.Requester.handleApiError(Requester.java:686)
	at org.kohsuke.github.Requester._to(Requester.java:293)
	at org.kohsuke.github.Requester.to(Requester.java:234)
	at org.kohsuke.github.GHRepository.getPermission(GHRepository.java:502)
	at org.jenkinsci.plugins.github_branch_source.GitHubSCMSource$1.fetch(GitHubSCMSource.java:874)
	at org.jenkinsci.plugins.github_branch_source.GitHubSCMSourceRequest.getPermissions(GitHubSCMSourceRequest.java:474)
	at 
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540280):
Can you get it to work with one of your own lean repos?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540943):
I got Jenkins to read the .travis.yml file from one of my own repos, and it starts off happily enough, but then says:
````
leanpkg test
OSX 'readlink' command does not support option '-f', please install 'greadlink'. If you use 'brew', you can install 'greadlink' using 'brew install coreutils'
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540984):
`coreutils` is already installed, and `leanpkg test` works just fine on the command line. :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 04 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540996):
Different `PATH`s, probably?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127540998):
Hmmm, I don't know how to help you with that one. (I don't really have any Jenkins experience myself.) Are you on a Mac? Or is Jenkins just very Mac-oriented?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127541257):
I think I'm going to pause my Jenkins experiments for now. (I have a big fat machine with plenty of RAM and cores, with a fixed IP address, but I would have to negotiate some holes in firewalls with my ... uncooperative ... IT staff.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127541270):
Aah, yes, I forgot that William isn't the only one with big fat machines. So do you (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 05 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127592452):
I think the easiest way to setup jenkins with github nowadays is to use the blue ocean interface with Jenkinsfile (docs [here](https://jenkins.io/doc/book/blueocean/getting-started/) and [here](https://jenkins.io/doc/book/blueocean/creating-pipelines/)).  All you need to do is install elan and add [this file to the repo](https://github.com/gebner/mathlib/blob/master/Jenkinsfile).  Then everything seems to work out of the box, including status information on PRs ([look here](https://github.com/gebner/mathlib/pull/1)).  (This is a linux machine btw, and we use it for another project so I can't easily repurpose it for mathlib.)
You definitely want a public IP with an open http port so people can look at the build log.  On the permission side, I think anybody in the lean github organization can authorize it.  The best way to automatically trigger jenkins is via webhooks, then it starts building a few seconds after a PR gets created or a commit is pushed.  Unfortunately I can't create webhooks on *any* of the lean projects.  In the worst case, jenkins can poll github in regular intervals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 07 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127693739):
So while I have a machine I can run Jenkins on, it seems there’s no way I can convince local IT people to let that Jenkins interface be publicly accessible. I could set it up to poll github in order to initiate builds, but I’d need some mechanism to output the build logs to a web server. If anyone knows of an out-of-the-box solution to this, I’m happy to pursue it, but perhaps there are better avenues.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 07 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127695721):
Can't you have it push the build logs by ssh to some web server?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 07 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis%20caching/near/127695909):
Yes, that's what I had in mind. I guess I was asking if someone knows of an easy-to-configure Jenkins plugin that does this. I'd be happy to contribute hardware and a little setup time, but I don't want to feel responsible for managing an intricate web of scripts. :-)


{% endraw %}
