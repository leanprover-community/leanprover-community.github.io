---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26436aPRforcategorytheory.html
---

## Stream: [general](index.html)
### Topic: [a PR for category theory](26436aPRforcategorytheory.html)

---


{% raw %}
#### [ Scott Morrison (Jun 04 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127523861):
<p>Dear all, (<span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> in particular!)<br>
I'm finally about to create a mathlib branch for some category theory, and I would be happy to have some guidance about the scope of the initial PR.</p>
<p>Options:<br>
1. Just the definitions of category, functor, natural transformation, and compositions of these.<br>
2. Also some basic constructions, e.g. functor categories, and product categories.<br>
3. Also definitions of basic notions such as products, equalizers, and limits.<br>
4. Also an example, e.g. showing that the category of types has limits.</p>
<p>(I could add many more things, but I think that's probably more than enough for a single PR.)</p>
<p>Essentially it's a question about whether it's easier to have things in very small increments, or easier to have bigger blocks, so that design decisions can be validated by examples and applications.</p>

#### [ Mario Carneiro (Jun 04 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127532640):
<p>Hey, just a heads up, but I am currently traveling and will soon be busy with the lean summer school in Hanoi for the next couple weeks, so my activity here will probably be spotty.</p>

#### [ Scott Morrison (Jun 04 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127535041):
<p>No worries! And thanks for letting us know. Will there be materials from the summer school available online?</p>

#### [ Johannes Hölzl (Jun 04 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127536040):
<p>Hi Scott, I think it would be good to start with a PR for 1. definitions. Then its easier to comment on it. For the summer school: <a href="https://hanoifabs.wordpress.com/" target="_blank" title="https://hanoifabs.wordpress.com/">https://hanoifabs.wordpress.com/</a> will be very ad-hoc, e.g. there are not a lot of slides.</p>

#### [ Johan Commelin (Jun 04 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127536139):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> And you are also flying there, right? So the next two weeks are bad timing for PR's in general?</p>

#### [ Johannes Hölzl (Jun 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127536198):
<p>Yes, I just landed in Hanoi. I guess the next 3 weeks are quiet busy. First Formal Abstract Summer School in Hanoi and then Hales60 in Pittsburgh.</p>

#### [ Scott Morrison (Jun 04 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127536352):
<p>Thanks, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> . The PR I put up at <a href="https://github.com/leanprover/mathlib/pull/152" target="_blank" title="https://github.com/leanprover/mathlib/pull/152">https://github.com/leanprover/mathlib/pull/152</a> is just the first few definitions.</p>

#### [ Sebastian Ullrich (Jun 08 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127762084):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> What _is_ happening over in Hanoi/in the fabstracts repo <span class="emoji emoji-1f606" title="laughing">:laughing:</span> ? <a href="https://github.com/formalabstracts/formalabstracts/pulls" target="_blank" title="https://github.com/formalabstracts/formalabstracts/pulls">https://github.com/formalabstracts/formalabstracts/pulls</a></p>

#### [ Johannes Hölzl (Jun 08 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127762135):
<p>Well, we try to teach people to use github, but some used the wrong formalabstracts fork. They should use Tom's personal formalabstract repo, not the project ones...</p>

#### [ Johannes Hölzl (Jun 08 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/127762151):
<p>Teaching git (as setting up remotes) is harder than thought...</p>

#### [ Johan Commelin (Jul 09 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20PR%20for%20category%20theory/near/129351495):
<p>What is the status of this PR? I would love to have basic category theory available in mathlib!</p>


{% endraw %}
