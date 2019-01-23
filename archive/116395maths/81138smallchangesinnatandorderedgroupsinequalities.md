---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/81138smallchangesinnatandorderedgroupsinequalities.html
---

## Stream: [maths](index.html)
### Topic: [small changes in nat and ordered groups inequalities](81138smallchangesinnatandorderedgroupsinequalities.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 07 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124761510):
Proposal 1.

The following lemma is useful:

```nat.le_add_right : ∀ (n k : ℕ), n ≤ n + k```

could we have the following lemma in mathlib:

```
def  nat.le_add_right_of_le:  ∀ (n m k : nat) (n_le_m : n <= m), n <= m + k
    | n m 0 n_le_m := n_le_m
    | n m (k +  1) n_le_m := nat.le_succ_of_le (nat.le_add_right_of_le n m k n_le_m)
```

Proposal 2.

Can we rename `lt_add_of_pos_of_lt` to  `lt_add_right_of_pos_of_lt` and `lt_add_of_lt_of_pos` `lt_add_left_of_lt_of_pos`?  Can we perhaps make things more standard, and change the signature of `lt_add_of_lt_of_pos` and rename it to `lt_add_of_pos_of_lt`?

Proposal 3.

Can we have this in mathlib: `def  nat.le_mul_right_of_le_of_pos:  ∀ (n m k : nat) (n_le_m : n <= m) (k_pos : 0  < k), n <= m * k :=  sorry` (I haven't tried proving it yet, but I assume induction should work too quite straightforwardly). Perhaps we would want a more general result too in `ordered_group.lean`, i.e. `le_mul_right_of_le_of_pos`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124762729):
Just to comment that `theorem  nat.le_add_right_of_le (n m k : nat) (n_le_m : n <= m) : n <= m + k := le_trans n_le_m $ nat.le_add_right _ _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124762821):
Things like `lt_add_of_pos_of_lt` are in the core lean library and it's very difficult currently to change anything in the core library, as the devs are busy with Lean 4 and are not amenable to "minor" changes like this. When Lean 4 hits a bunch of maths might be moved out of the core library and this might be the time to change these things. However I really want a place where comments such as this can sit festering until the devs are ready; it's difficult to find such a place as you can see from the Lean FAQ that opening minor issues is currently not really welcome.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 07 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124763149):
Proposal 3 also looks like a case for transitivity, because it's naturally the conjunction of `n <=m` and `m <= m * k`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 07 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774128):
Thanks, I didn't realise that these were from standard library. I thought it was in [mathlib in ordered_group.lean](https://github.com/leanprover/mathlib/blob/d84dfb17b9cfbb29e0f728fd22b4f5176f7bd0a9/algebra/ordered_group.lean), but actually it is in [standard library ordered_group.lean](https://github.com/leanprover/lean/blob/51a87212fa30883bc8f39b41fc9ed2bed1cfed77/library/init/algebra/ordered_group.lean). It appears that many lemmas are copied over to mathlib from standard library, but they appear with a single apostrophe at the end in mathlib!

I think you're talking about a place to keep the backlog. I've seen people using trello boards for this purpose. I've set one up for this:
https://trello.com/b/we2kRiDw/lean-4-proposals

I've added you to it. Happy to add everybody else if this is what we want to use? If a different solution catches on, I can migrate these proposals over.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774177):
The "apostrophe lemmas" have a different typeclass assumption, namely `ordered_comm_group`, which doesn't exist in core

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774178):
in an ideal world the core lemmas would be removed since you get them from the mathlib lemmas by typeclass inference, but core lib is basically frozen for now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774229):
I see, this all makes sense now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 07 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774281):
Do apostrophed lemmas somehow shadow non-apostrophed lemmas? Certainly vscode doesn't autosuggest them for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774324):
No, that sort of shadowing isn't allowed by lean. You have to have the file imported to see them in autosuggest

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774332):
One possibility is a "core lib wishlist" file we can maintain on mathlib. I used `pending.lean` for this briefly, but I've since become convinced that Leo is unlikely to ever accept a change from mathlib, so I have spent most of my time working around core as it exists rather than trying to change it. Such a wishlist may become useful if we ever fork lean, but I don't see what other good it would do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Apr 07 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774658):
Sounds a bit nuclear. Surely there must be a way for mathlib and stdlib to work closely together? Are main goals/objectives of lean and mathlib different?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774664):
Trust me, this isn't what I want, but Leo has gone hermit in a big way and we have to work around this if we want to keep using and improving lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 07 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124774705):
For now I'm keeping the possibility open but not making any steps towards a fork until it becomes absolutely necessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/small%20changes%20in%20nat%20and%20ordered%20groups%20inequalities/near/124791116):
I really hope Lean 4 and its reduced core lib will make all these problem disappear

