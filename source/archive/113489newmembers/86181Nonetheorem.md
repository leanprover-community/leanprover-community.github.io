---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/86181Nonetheorem.html
---

## [new members](index.html)
### [None theorem](86181Nonetheorem.html)

#### [Ken Roe (Sep 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133185891):
Does someone know what tactic to use to prove the following:

```lean
theorem nonethm {t} : (none <|> none)=@none t:=
begin
    ...
end
```

#### [Chris Hughes (Sep 01 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133186005):
`theorem nonethm {t} : (none <|> none)=@none t:= rfl`

#### [Mario Carneiro (Sep 01 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133186270):
lol. `by simp` also works if you have `import data.option`

#### [Patrick Massot (Sep 01 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133188061):
Chris, you lose: Ken asked for a tactic. The best answer was `refl` :yum:

#### [Patrick Massot (Sep 01 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133188364):
A slightly more serious answer: I think stating the result as `theorem nonethm {t} : (none <|> none)= (none : option t)` makes it easier to read. I mention this because it's a general trick: you can often avoid using `@` by adding a type ascription.

#### [Ken Roe (Sep 01 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133189198):
Thanks.  A couple more questions:
1) I found data/option.lean in mathlib.  Where should I place the mathlib repository with respect to the Lean repository?  How do I configure VSCode so that it starts Lean with the appropriate search path?

2) Next, how do I prove the theorem:

```lean
theorem nonethm {t} {x:option t} : (x <|> none)=x:= begin
    ...
end
```

#### [Kenny Lau (Sep 01 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133189244):
```lean
theorem nonethm {t} {x : option t} : (x <|> none) = x :=
begin
  cases x; refl
end
```

#### [Bryan Gin-ge Chen (Sep 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133189359):
For question 1 I recommend using leanpkg. The advice on the [xena blog](https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/) is a little old but still worked for me a month or so ago.

