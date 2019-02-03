---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03353newbcheck51minuteruntime.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [newb,  "#check 5" 1 minute runtime?](https://leanprover-community.github.io/archive/113488general/03353newbcheck51minuteruntime.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ drocta (May 31 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127381913):
<p>First, sorry if this is not the correct place for me to seek help for this. I haven't used zulip before and couldn't find a page with the rules to follow for this specific chat. (Should I have put this in an existing topic?)<br>
I tried installing Lean 3.4.1 on windows 7, and when I try to run a test2.lean which consists of just "#check 5", it takes a minute and 5 seconds before it gives me the output.</p>
<blockquote>
<p>5 : ℕ<br>
&lt;unknown&gt;:1:1: error: unknown declaration 'main'</p>
</blockquote>
<p>(when running "lean --run ../../progs/test2.lean" )<br>
Someone else let me know that they tried a similar file<br>
(specifically, </p>
<blockquote>
<p>constant m : nat<br>
#check m</p>
</blockquote>
<p>which I tried before "#check 5" and also takes a minute for me)<br>
 on linux, and for them it ran in under a second.<br>
They didn't have an idea for why it was running slowly except possibly my antivirus, but it still runs just as slow for me when I have that turned off.</p>
<p>I tend to have my computer's memory use fairly high. Would this cause Lean to run this slowly for this test case?</p>
<p>During the minute that it is running, my cpu use goes to around 100%  (from around 20%). I tried closing my antivirus software and it didn't seem to improve the running speed.</p>
<p>Could anyone provide me with advice for what to do differently?</p>
<p>Thank you for your consideration</p>

#### [ Patrick Massot (May 31 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127382236):
<blockquote>
<p>First, sorry if this is not the correct place for me to seek help for this. I haven't used zulip before and couldn't find a page with the rules to follow for this specific chat. (Should I have put this in an existing topic?)</p>
</blockquote>
<p>I don't think we have any specific rule. Mario only pretends to complain when he sees Lolcats or memes. We only try to minimize code when asking for help, and avoid asking Sebastian about Lean 4 progress every day. That being said, I have no Windows computer so I cannot help. I can only tell you this shouldn't happen</p>

#### [ drocta (May 31 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127382343):
<p>Alright, thank you</p>

#### [ Reid Barton (May 31 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127382889):
<p>I don't think you want "--run"</p>

#### [ Reid Barton (May 31 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127382917):
<p>But I don't know whether that will make it not slow.</p>

#### [ drocta (May 31 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383242):
<p>Ah! Thanks, I tried it without the "--run" , and it no longer complains about lacking main, though it still takes slightly over a minute.</p>

#### [ drocta (May 31 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383487):
<p>Ah, I just tried running it with --profile , and, in addition to much more text than I expected, it ended with</p>
<blockquote>
<p>5 : ℕ<br>
cumulative profiling times:<br>
        compilation 6.75s<br>
        decl post-processing 2.45s<br>
        elaboration 85.4s<br>
        elaboration: tactic compilation 11.5s<br>
        elaboration: tactic execution 13.2s<br>
        parsing 12.9s<br>
        type checking 1.44s</p>
</blockquote>
<p>Which I suppose says something, thought I'm not quite sure what.</p>

#### [ Mario Carneiro (May 31 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383840):
<p>Have you compiled the library files? If your core lean contains no .olean files then that could explain the long startup, since lean has to compile everything every time. Try running <code>lean --make</code> first</p>

#### [ Mario Carneiro (May 31 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383863):
<p>You don't want to use <code>--run</code> unless you are using lean noninteractively</p>

#### [ Mario Carneiro (May 31 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383870):
<p>it's basically the same as affixing <code>#eval main</code> to the end of the given file</p>

#### [ drocta (May 31 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127383939):
<p>Ah, I had not! I will run that now, Thank you!</p>

#### [ drocta (May 31 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127384026):
<p>Ah, when I ran <code>lean --make</code>by itself it finished in under a second and didn't say anything, and then I tried <code>lean ../../progs/test2.lean</code> again and it still took a bit. I will time it to see if it is still taking a minute.</p>

#### [ drocta (May 31 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127384140):
<p>Still took a minute and 5 seconds.<br>
I noticed that when I ran <code>lean --path</code> it told me that "leanpkg_path_file" was "/could-not-find-home". Could that be related?</p>

#### [ drocta (May 31 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127384205):
<p>oh, I tried <code>lean --make ..\..\progs\test2.lean</code> and it is saying stuff</p>

#### [ drocta (May 31 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127384302):
<p>Ah! Great! It runs in 7 seconds now. There we go. Thank you!</p>

#### [ Reid Barton (Jun 01 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127387966):
<p>Interesting. I guess the precompiled binaries don't contain precompiled .olean files? Are they platform-dependent?</p>

#### [ Kevin Buzzard (Jun 01 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newb%2C%20%20%22%23check%205%22%201%20minute%20runtime%3F/near/127388291):
<p>I almost always use linux nightlies and they have plenty of .olean files usually</p>


{% endraw %}
