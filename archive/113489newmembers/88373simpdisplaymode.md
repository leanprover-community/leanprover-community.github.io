---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/88373simpdisplaymode.html
---

## Stream: [new members](index.html)
### Topic: [simp display mode](88373simpdisplaymode.html)

---


{% raw %}
#### [ Andreas Swerdlow (Aug 06 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130969966):
Is there some way of getting lean to show what lemmas simp used in a particular line? I added an include in my file and suddenly a lot of my simps don't do what they used to. I want to be able to see which lemmas it is now having problems with.

#### [ Chris Hughes (Aug 06 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970048):
`set_option trace.simplify.rewrite true`

#### [ Kevin Buzzard (Aug 06 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970060):
see my post from just now about \u m * n :-)

#### [ Mario Carneiro (Aug 06 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970090):
you said "just click on `simp` and see" but I don't know what you mean by that

#### [ Kevin Buzzard (Aug 06 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970092):
But that is slightly surprising. It might be that your include contained a lemma tagged `@[simp]` which is now being applied when it wasn't before. If you can locate the lemma then...I'm not sure you can untag it actually, but you can stop `simp` from using it and then hopefully sanity will be restored

#### [ Kevin Buzzard (Aug 06 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970096):
Oh -- I'd put the `set_option` earlier

#### [ Mario Carneiro (Aug 06 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970153):
you can only locally untag a simp lemma

#### [ Andreas Swerdlow (Aug 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970368):
@**Chris Hughes**  thanks

#### [ Andreas Swerdlow (Aug 06 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970448):
The offending include file is one of my own. So I tried untagging all of the simp lemmas in the source file but this did not solve the problem

#### [ Kevin Buzzard (Aug 06 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970698):
https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md#when-it-is-unadvisable-to-use-simp

#### [ Kevin Buzzard (Aug 06 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970809):
If you're using `simp` in the middle of a proof, then you're asking for trouble. You should only use `simp` to close a goal. Although it's kind of annoying, if your goal is `A` and then `simp` turns it into `B`, you're supposed to write `suffices : B, simpa using this` or `simp [this]` or `simp!` or some other random incantation until `simp` eventually is convinced that it can prove that `B` implies `A`, and then go on. This makes imports far less likely to break code.


{% endraw %}
