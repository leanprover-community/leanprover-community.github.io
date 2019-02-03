---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47686MachineLearning.html
---

## Stream: [general](index.html)
### Topic: [Machine Learning](47686MachineLearning.html)

---


{% raw %}
#### [ Simon Hudon (Mar 31 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463630):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> Let's switch threads</p>

#### [ Simon Hudon (Mar 31 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463678):
<p>You should consider changing names <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463722):
<p>but yeah, ml isn't going to break into real time radar imaging anytime soon, mostly because you need a ton of compute horsepower</p>

#### [ Simon Hudon (Mar 31 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463729):
<p>if it did, what would it improve?</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463730):
<p>depends on what your end application is</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463771):
<p>for radar, a big problem is distinguishing objects from noise</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463774):
<p>we use tons of linear approximations everywhere that aren't totally applicable</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463782):
<p>but who cares because everything is a gaussian if you actually want to compute things</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463788):
<p>unfortunately noise is rarely linear, rarely uncorrelated, and better ways of doing it are too complicated to do in real time</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463828):
<p>but maybe a well trained ml model would be efficient enough? I don't know, but i think it might be true in the future</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463831):
<p>gotta stay ahead of the curve and do some learning :)</p>

#### [ Simon Hudon (Mar 31 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463833):
<p>If it was computationally feasible, would it bring in safety risks?</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463841):
<p>hmm, possibly, but we already accept some risk of error in the process</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463843):
<p>since it's statistical, we design the system to some probability pf of a false alarm</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463845):
<p>(of detecting an object, in this example)</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463887):
<p>can you talk about that false alarm probability in a deep learning model? kinda... sorta... I don't know well enough to say that rigorously</p>

#### [ Simon Hudon (Mar 31 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463888):
<p>Already having an estimate for the probability of failure of a ML model seems pretty difficult, isn't it?</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463938):
<p>yup. but even a handwavy one would be nice though</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463947):
<p>i mean, current estimates are based on assuming gaussian noise, which doesn't reflect reality</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463948):
<p>it's a complicated subject</p>

#### [ Simon Hudon (Mar 31 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463949):
<p>I'm wondering if the best that can be done with an ML system is counting errors and retiring / replacing models whose number of errors exceeds the tolerance. I'm not sure if it's any good though</p>

#### [ Simon Hudon (Mar 31 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463994):
<p>Sorry, I might not be focusing on what you care about, I think a lot about guarantees. In your case, the hope seems to be an increase in average accuracy, does that make sense?</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464000):
<p>yeah. it doesn't make sense to speak of guarantees in object detection, just minimizing the ratio of detections to false alarms</p>

#### [ Simon Hudon (Mar 31 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464040):
<p>You could think of a guarantee as an upper bound on the probability of failure</p>

#### [ Simon Hudon (Mar 31 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464089):
<p>Whenever I think of ML lately, I think of a software tool that was on the news recently where judges would use ML to help them make their judgement faster. It was found that the process exaggerated an existing racial bias. I see that as a conflict between efficiency and correctness. If you can't make any statement about the correctness of the software, what good is it?</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464095):
<p>haha, that's a dangerous statement to make</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464097):
<p>cowboy c coders brought us the computer revolution :)</p>

#### [ Simon Hudon (Mar 31 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464099):
<p>My skin has grown impervious to the rocks I'm being thrown <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span></p>

#### [ Simon Hudon (Mar 31 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464144):
<p>Which revolution do you mean? The age of personal computing or putting white supremacists in the White House?</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464192):
<p>both, because as you know, it's a fact that automation has put many out of work, but that's getting a little off-topic</p>

#### [ Simon Hudon (Mar 31 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464241):
<p>That's true (both things)</p>

#### [ Andrew Ashworth (Mar 31 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464249):
<blockquote>
<p>I'm wondering if the best that can be done with an ML system is counting errors and retiring / replacing models whose number of errors exceeds the tolerance. I'm not sure if it's any good though</p>
</blockquote>
<p>back in the day, when humans interpreted radar returns, firing a bad operator was exactly what was done</p>

#### [ Simon Hudon (Mar 31 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464292):
<p>I'm slowly getting to respect the development of cowboy developers and I realize that everything doesn't need to be bullet proof. But there is an extent where rolling out a technology should be after proper study</p>


{% endraw %}
