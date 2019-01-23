---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59209strangeparsing.html
---

## Stream: [general](index.html)
### Topic: [strange parsing](59209strangeparsing.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 19 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126782270):
I just discovered that this parses:
```
#printnat
-- inductive nat : Type
-- constructors:
-- nat.zero : ℕ
-- nat.succ : ℕ → ℕ
```
I guess spaces are optional?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796448):
So what happens when one command happens to be a prefix of another one? What are all the commands? `#print #exit #check #eval #reduce`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796490):
`#eval1+1 -- 2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796501):
`#help`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796502):
`#helpoptions` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796503):
aah bingo `#helpcommands`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796698):
```lean
definition er_has_run_out_of_ink := 4

#printer_has_run_out_of_ink 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796699):
well there you go

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 19 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126796700):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126797263):
I think it's possible to define new commands, because sometimes I can import something and then magically use `#find`. If I define `#che` then maybe this breaks `#check`. Can I just define `#` and break everything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 19 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/strange%20parsing/near/126797466):
No, the longest match wins

