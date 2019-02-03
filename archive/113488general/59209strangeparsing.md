---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59209strangeparsing.html
---

## Stream: [general](index.html)
### Topic: [strange parsing](59209strangeparsing.html)

---


{% raw %}
#### [ Mario Carneiro (May 19 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126782270):
<p>I just discovered that this parses:</p>
<div class="codehilite"><pre><span></span>#printnat
-- inductive nat : Type
-- constructors:
-- nat.zero : ℕ
-- nat.succ : ℕ → ℕ
</pre></div>


<p>I guess spaces are optional?</p>

#### [ Kevin Buzzard (May 19 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796448):
<p>So what happens when one command happens to be a prefix of another one? What are all the commands? <code>#print #exit #check #eval #reduce</code></p>

#### [ Kevin Buzzard (May 19 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796490):
<p><code>#eval1+1 -- 2</code></p>

#### [ Kevin Buzzard (May 19 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796501):
<p><code>#help</code></p>

#### [ Kevin Buzzard (May 19 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796502):
<p><code>#helpoptions</code> works</p>

#### [ Kevin Buzzard (May 19 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796503):
<p>aah bingo <code>#helpcommands</code></p>

#### [ Kevin Buzzard (May 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796698):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">er_has_run_out_of_ink</span> <span class="o">:=</span> <span class="mi">4</span>

<span class="bp">#</span><span class="n">printer_has_run_out_of_ink</span>
</pre></div>

#### [ Kevin Buzzard (May 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796699):
<p>well there you go</p>

#### [ Kenny Lau (May 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796700):
<p>lol</p>

#### [ Kevin Buzzard (May 19 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126797263):
<p>I think it's possible to define new commands, because sometimes I can import something and then magically use <code>#find</code>. If I define <code>#che</code> then maybe this breaks <code>#check</code>. Can I just define <code>#</code> and break everything?</p>

#### [ Sebastian Ullrich (May 19 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126797466):
<p>No, the longest match wins</p>


{% endraw %}
