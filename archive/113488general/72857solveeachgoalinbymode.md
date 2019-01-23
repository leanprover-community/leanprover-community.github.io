---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72857solveeachgoalinbymode.html
---

## Stream: [general](index.html)
### Topic: [solve each goal in "by" mode](72857solveeachgoalinbymode.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125302926):
In `by` mode, i.e. `by xxx; yyy; zzz`, is there a way to not apply the tactics to every goal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125302994):
you can use seq_focus, i.e. `xxx; [yyy, zzz]`, or use a big tactic block `by { xxx, yyy, zzz }`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125302996):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125302998):
I was trying `focus [yyy, zzz]` but it failed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303002):
turns out you don't say `focus`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303011):
how would you write this?
```
by simp [reduce.step, h] at H; cases L; injections;
    [cc, { rw ← h_2, from list.suffix_append _ _ } ]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303082):
```
begin
  simp [reduce.step, h] at H,
  cases L; injections, {cc},
  rw ← h_2,
  exact list.suffix_append _ _
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303125):
but it's three lines longer, lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303133):
four lines longer. i can't count

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303142):
If you have to represent complicated control flow, you probably shouldn't be using `by`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 19 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve%20each%20goal%20in%20%22by%22%20mode/near/125303150):
at some point it's saving lines by just deleting newlines

