---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72857solveeachgoalinbymode.html
---

## Stream: [general](index.html)
### Topic: [solve each goal in "by" mode](72857solveeachgoalinbymode.html)

---


{% raw %}
#### [ Kenny Lau (Apr 19 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125302926):
<p>In <code>by</code> mode, i.e. <code>by xxx; yyy; zzz</code>, is there a way to not apply the tactics to every goal?</p>

#### [ Mario Carneiro (Apr 19 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125302994):
<p>you can use seq_focus, i.e. <code>xxx; [yyy, zzz]</code>, or use a big tactic block <code>by { xxx, yyy, zzz }</code></p>

#### [ Kenny Lau (Apr 19 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125302996):
<p>aha</p>

#### [ Kenny Lau (Apr 19 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125302998):
<p>I was trying <code>focus [yyy, zzz]</code> but it failed</p>

#### [ Kenny Lau (Apr 19 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303002):
<p>turns out you don't say <code>focus</code></p>

#### [ Kenny Lau (Apr 19 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303011):
<p>how would you write this?</p>
<div class="codehilite"><pre><span></span>by simp [reduce.step, h] at H; cases L; injections;
    [cc, { rw ← h_2, from list.suffix_append _ _ } ]
</pre></div>

#### [ Mario Carneiro (Apr 19 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303082):
<div class="codehilite"><pre><span></span>begin
  simp [reduce.step, h] at H,
  cases L; injections, {cc},
  rw ← h_2,
  exact list.suffix_append _ _
end
</pre></div>

#### [ Kenny Lau (Apr 19 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303125):
<p>but it's three lines longer, lol</p>

#### [ Kenny Lau (Apr 19 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303133):
<p>four lines longer. i can't count</p>

#### [ Mario Carneiro (Apr 19 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303142):
<p>If you have to represent complicated control flow, you probably shouldn't be using <code>by</code></p>

#### [ Mario Carneiro (Apr 19 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303150):
<p>at some point it's saving lines by just deleting newlines</p>


{% endraw %}
