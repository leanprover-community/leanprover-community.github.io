---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26505leanhomepagestillpointingtogitter.html
---

## Stream: [general](index.html)
### Topic: [lean home page still pointing to gitter](26505leanhomepagestillpointingtogitter.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 10 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521404):
<p>I occasionally notice that <a href="https://leanprover.github.io/documentation/" target="_blank" title="https://leanprover.github.io/documentation/">Lean's web pages</a> still point to gitter, and we occasionally get questions there; perhaps the signage isn't good enough for everyone. How could we go about changing this? I could make a PR but someone will have to point me to the location of the git source for those pages (not least so I can check the PR is not already made).</p>

#### [ Scott Morrison (Oct 10 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521477):
<p>I think we just run into the general problem that PRs here risk annoying Leo.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521556):
<p>I know, but on this particular occasion I am personally prepared to take the risk. I have been extremely good at not annoying Leo recently -- a few months ago I was desperate to email him to tell him 100 things and Tom Hales just basically went "No. No. No. No. No. Leave him alone." This is a one-line PR to fix something which is broken and the review process is trivial.</p>

#### [ Mario Carneiro (Oct 10 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521622):
<p>are you saying you need us to say "no no no"?</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521627):
<p>If you're not going to tell me how to do it I'm going to go rogue and figure it out myself.</p>

#### [ Mario Carneiro (Oct 10 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521670):
<p>I guess I don't know if the website is also defunct or just the tool</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135522279):
<p>"Small bug fixes (few lines of code) are always welcome.". From the docs (which I'm currently reading -- I'm trying to put together an "installation options overview" page)</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135522296):
<p>"Bug reports are always welcome, but nitpicking issues are not". Hmm.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135522369):
<p>But I've now found two links to Zulip in the Lean docs / GH pages, and one link to gitter.</p>

#### [ Jeremy Avigad (Oct 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135548324):
<p>I think <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> has permissions to the relevant repo.</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135550144):
<p>Unfortunately I don't. If someone could open a PR with some new wording (is it still a "public" "chat room"?), I'll talk to Leo</p>

#### [ Kevin Buzzard (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135565883):
<p>I would do this but I don't know the URL of the repo.</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135566152):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> <a href="https://github.com/leanprover/leanprover.github.io/blob/master/documentation/index.md" target="_blank" title="https://github.com/leanprover/leanprover.github.io/blob/master/documentation/index.md">https://github.com/leanprover/leanprover.github.io/blob/master/documentation/index.md</a>. You should be able to edit it right on Github.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135566628):
<p><a href="https://github.com/leanprover/leanprover.github.io/pull/75" target="_blank" title="https://github.com/leanprover/leanprover.github.io/pull/75">https://github.com/leanprover/leanprover.github.io/pull/75</a></p>

#### [ Sebastian Ullrich (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135566974):
<p>(Okay, now I have write access. Thanks for the PR.)</p>

#### [ Patrick Massot (Oct 10 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135567577):
<p>Sebastian, are you willing to get other PR to that repo? Like one about the sentence "The current version of Lean is Lean 3, and is under active development."</p>

#### [ Sebastian Ullrich (Oct 10 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135567853):
<p>Oh. Yes.</p>

#### [ Patrick Massot (Oct 10 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135568270):
<p><a href="https://github.com/leanprover/leanprover.github.io/pull/76" target="_blank" title="https://github.com/leanprover/leanprover.github.io/pull/76">https://github.com/leanprover/leanprover.github.io/pull/76</a></p>

#### [ Kevin Buzzard (Oct 10 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135568597):
<p>Good catch Patrick. As you all know I've been pushing for more users in the maths community recently, and it's good to get the docs right. I don't care that Lean 4 is coming and there might be some chaos -- mathematicians need a <em>lot</em> of training in general and the sooner they start the better. In fact in some sense now we have a stable Lean it's quite a good time for new users to appear.</p>


{% endraw %}
