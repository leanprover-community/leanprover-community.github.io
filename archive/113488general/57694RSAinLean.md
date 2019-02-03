---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57694RSAinLean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [RSA in Lean](https://leanprover-community.github.io/archive/113488general/57694RSAinLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 12 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784575):
<p>I have to give a talk for high school students. Topic: cryptography.<br>
I've done this before, and I would usually fool around in Python. Does anyone know of an implementation of DH or RSA in Lean?</p>

#### [ Mario Carneiro (Sep 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784629):
<p>lolno</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784633):
<p>I stay away from Lean when I'm giving talks like this. I spend time talking about WhatsApp because that's what they know in the UK.</p>

#### [ Johan Commelin (Sep 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784638):
<p>But you could do both, right?</p>

#### [ Mario Carneiro (Sep 12 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784644):
<p>then again, all you need is a bit of group exponentiation on <code>zmod</code> to implement DH</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784645):
<p>My school talks are usually only 30-40 mins</p>

#### [ Mario Carneiro (Sep 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784651):
<p>and I think RSA is about as easy</p>

#### [ Johan Commelin (Sep 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784655):
<p>Aah, I have 75 minutes. The students are coming to an open day of the math department.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784661):
<p>I might even be tempted to refuse to speak to schoolkids for so long. They're not used to concentrating for that kind of time (at least in the UK)</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784706):
<p>I would talk for 30, give them 15 minutes to do a project, and then talk for 30 more. Active learning!</p>

#### [ Johan Commelin (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784708):
<p>You've got tenure <span class="emoji emoji-1f606" title="lol">:lol:</span> Refusing is not on my list of options.</p>

#### [ Johan Commelin (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784715):
<p>Right, that's what I was thinking.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784717):
<p>They could spend the 15 minutes trying to install Lean :-)</p>

#### [ Johan Commelin (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784723):
<p>So they could do their project with a hand calculator or python or whatever.</p>

#### [ Johan Commelin (Sep 12 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784726):
<p>I was just thinking of demoing Lean. Not them playing with it.</p>

#### [ Kenny Lau (Sep 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784729):
<p>oh no it takes a whole hour to install lean</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784741):
<p>maybe a 7 minute talk, then an hour working together trying to install Lean, and then 8 minute wrap-up at the end.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784807):
<p>I've done super-hard computations on my phone using the pari-gp app and a bluetooth keyboard.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784809):
<p>and the app is a one click install on Android.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784813):
<p>You could give them some 5 digit numbers to factor on their stock calculator</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784823):
<p>but I would stay away from Lean. I've tried it with Math Olympiad level schoolkids and they found it tough</p>

#### [ Johan Commelin (Sep 12 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784830):
<p>Ok, thanks for the advice. I'll stick to python.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784871):
<p>on the other hand I should say that on some Wed in mid-Oct (18th?) I am giving another Lean school talk.</p>

#### [ Kenny Lau (Sep 12 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784881):
<p>can I come? :P</p>

#### [ Mario Carneiro (Sep 12 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784909):
<p>If you are interested in incorporating lean, you can just mention it without going in depth. Make them know formal proving is a thing, and move on</p>

#### [ Johan Commelin (Sep 12 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133784986):
<p>Right. That's also an option.</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133785610):
<blockquote>
<p>can I come? :P</p>
</blockquote>
<p>My recent experience with going to give school talks in the UK is that you can't get beyond the entrance until you've proved (or at least claimed) that you're the person they're expecting to give the talk, and they've given you something to wear around your neck saying "visitor".</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133785614):
<p>It's very different to how it was 20 years ago</p>

#### [ Kevin Buzzard (Sep 12 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/RSA%20in%20Lean/near/133785615):
<p>so my guess is no</p>


{% endraw %}
