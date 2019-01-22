---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/02213DoesLeancontainnumericalbases.html
---

## [new members](index.html)
### [Does Lean contain numerical bases?](02213DoesLeancontainnumericalbases.html)

#### [Abhimanyu Pallavi Sudhir (Nov 10 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147407947):
Specifically, I want a way to extract the base-n digits of a number as a list. Does this already exist?

#### [Andrew Ashworth (Nov 10 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147408048):
that seems pretty specialized, so i doubt it

#### [Kenny Lau (Nov 10 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147408056):
```lean
#eval nat.to_digits 2 100 --[0, 0, 1, 0, 0, 1, 1]
```

#### [Andrew Ashworth (Nov 10 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147408061):
woah, i'm wrong

#### [Chris Hughes (Nov 10 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147408167):
That's just there so numerals can be printed and parsed.

#### [Bryan Gin-ge Chen (Nov 10 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147410490):
[Here it is in core lean](https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/repr.lean#L77). As a newbie to functional programming, I thought this was super cool.

#### [Kevin Buzzard (Nov 10 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147411489):
oh so that's how `repr` works :-)

#### [Kevin Buzzard (Nov 10 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147411727):
```lean
def nat.repr2 (n : ℕ) : string :=
((nat.to_digits 2 n).map nat.digit_char).reverse.as_string

@[priority 10000]
instance nat.has_repr2 : has_repr nat :=
⟨nat.repr2⟩

#eval 7 -- 111
```

woo I have binary Lean!

#### [Chris Hughes (Nov 10 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147412552):
Hide that in xenalib somwhere and confuse everyone.

#### [Abhimanyu Pallavi Sudhir (Nov 10 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147431978):
```quote
```lean
#eval nat.to_digits 2 100 --[0, 0, 1, 0, 0, 1, 1]
```
```
Nice!

#### [Kevin Buzzard (Nov 10 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Does%20Lean%20contain%20numerical%20bases%3F/near/147432166):
The way to find it is to think "hmm, how are naturals being printed?" then "hmm, what is the definition of `nat.repr`?"

