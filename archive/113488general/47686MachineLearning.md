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
@**Andrew Ashworth** Let's switch threads

#### [ Simon Hudon (Mar 31 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463678):
You should consider changing names :stuck_out_tongue_closed_eyes:

#### [ Andrew Ashworth (Mar 31 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463722):
but yeah, ml isn't going to break into real time radar imaging anytime soon, mostly because you need a ton of compute horsepower

#### [ Simon Hudon (Mar 31 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463729):
if it did, what would it improve?

#### [ Andrew Ashworth (Mar 31 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463730):
depends on what your end application is

#### [ Andrew Ashworth (Mar 31 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463771):
for radar, a big problem is distinguishing objects from noise

#### [ Andrew Ashworth (Mar 31 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463774):
we use tons of linear approximations everywhere that aren't totally applicable

#### [ Andrew Ashworth (Mar 31 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463782):
but who cares because everything is a gaussian if you actually want to compute things

#### [ Andrew Ashworth (Mar 31 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463788):
unfortunately noise is rarely linear, rarely uncorrelated, and better ways of doing it are too complicated to do in real time

#### [ Andrew Ashworth (Mar 31 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463828):
but maybe a well trained ml model would be efficient enough? I don't know, but i think it might be true in the future

#### [ Andrew Ashworth (Mar 31 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463831):
gotta stay ahead of the curve and do some learning :)

#### [ Simon Hudon (Mar 31 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463833):
If it was computationally feasible, would it bring in safety risks?

#### [ Andrew Ashworth (Mar 31 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463841):
hmm, possibly, but we already accept some risk of error in the process

#### [ Andrew Ashworth (Mar 31 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463843):
since it's statistical, we design the system to some probability pf of a false alarm

#### [ Andrew Ashworth (Mar 31 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463845):
(of detecting an object, in this example)

#### [ Andrew Ashworth (Mar 31 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463887):
can you talk about that false alarm probability in a deep learning model? kinda... sorta... I don't know well enough to say that rigorously

#### [ Simon Hudon (Mar 31 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463888):
Already having an estimate for the probability of failure of a ML model seems pretty difficult, isn't it?

#### [ Andrew Ashworth (Mar 31 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463938):
yup. but even a handwavy one would be nice though

#### [ Andrew Ashworth (Mar 31 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463947):
i mean, current estimates are based on assuming gaussian noise, which doesn't reflect reality

#### [ Andrew Ashworth (Mar 31 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463948):
it's a complicated subject

#### [ Simon Hudon (Mar 31 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463949):
I'm wondering if the best that can be done with an ML system is counting errors and retiring / replacing models whose number of errors exceeds the tolerance. I'm not sure if it's any good though

#### [ Simon Hudon (Mar 31 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124463994):
Sorry, I might not be focusing on what you care about, I think a lot about guarantees. In your case, the hope seems to be an increase in average accuracy, does that make sense?

#### [ Andrew Ashworth (Mar 31 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464000):
yeah. it doesn't make sense to speak of guarantees in object detection, just minimizing the ratio of detections to false alarms

#### [ Simon Hudon (Mar 31 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464040):
You could think of a guarantee as an upper bound on the probability of failure

#### [ Simon Hudon (Mar 31 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464089):
Whenever I think of ML lately, I think of a software tool that was on the news recently where judges would use ML to help them make their judgement faster. It was found that the process exaggerated an existing racial bias. I see that as a conflict between efficiency and correctness. If you can't make any statement about the correctness of the software, what good is it?

#### [ Andrew Ashworth (Mar 31 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464095):
haha, that's a dangerous statement to make

#### [ Andrew Ashworth (Mar 31 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464097):
cowboy c coders brought us the computer revolution :)

#### [ Simon Hudon (Mar 31 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464099):
My skin has grown impervious to the rocks I'm being thrown :stuck_out_tongue_winking_eye:

#### [ Simon Hudon (Mar 31 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464144):
Which revolution do you mean? The age of personal computing or putting white supremacists in the White House?

#### [ Andrew Ashworth (Mar 31 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464192):
both, because as you know, it's a fact that automation has put many out of work, but that's getting a little off-topic

#### [ Simon Hudon (Mar 31 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464241):
That's true (both things)

#### [ Andrew Ashworth (Mar 31 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464249):
```quote
I'm wondering if the best that can be done with an ML system is counting errors and retiring / replacing models whose number of errors exceeds the tolerance. I'm not sure if it's any good though
```
back in the day, when humans interpreted radar returns, firing a bad operator was exactly what was done

#### [ Simon Hudon (Mar 31 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Machine%20Learning/near/124464292):
I'm slowly getting to respect the development of cowboy developers and I realize that everything doesn't need to be bullet proof. But there is an extent where rolling out a technology should be after proper study


{% endraw %}
