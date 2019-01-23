---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/27081Leavetermmodecalconceyouenterit.html
---

## Stream: [new members](index.html)
### Topic: [Leave term mode/calc once you enter it?](27081Leavetermmodecalconceyouenterit.html)

---

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135604247):
Part of my proof involved calc, but now I want to return to tactic mode to complete my proof. How do I do this?

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135604263):
The way I've done this in the past is to do the term mode in a separate lemma.

#### [Andrew Ashworth (Oct 11 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135604665):
just type `begin` `end` again

#### [Mario Carneiro (Oct 11 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135604690):
depends on how you have set it up. You could have the calc block inside tactic mode, or you could have a tactic block in one of the steps of a calc block

#### [Kevin Buzzard (Oct 11 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135605855):
```lean
example : 2 + 2 = 5 :=
begin
  show 3 + 1 = 5,
  exact calc 3 + 1 = 1 + 3 : by simp
        ...        = 2 + 2 : by simp
        ...        = 5     : begin
             show 2 + 2 = 5,
             -- I'm not getting anywhere
             sorry
        end,
end
```

@**Abhimanyu Pallavi Sudhir**  -- post a MWE if what I said doesn't help.

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135607561):
Here's the code:
```lean
import tactic.norm_num
definition cong_mod_37 (a b : ℤ) := ∃ k : ℤ, 37 * k = a - b

theorem cong_mod_37_equiv_reln : equivalence cong_mod_37 :=
begin
  split,
    rw reflexive,
    intro x,
    rw cong_mod_37,
    rw sub_self,
    fapply exists.intro,
      exact 0,
    norm_num,
  split,
    rw symmetric,
    intros x y,
    intro HXY,
    rw cong_mod_37,
    rw cong_mod_37 at HXY,
    cases HXY with n Hn,
    fapply exists.intro,
      exact -n,
    show 37 * -n = y - x,
    exact calc 37 * -n = -(37*n) : by rw ←neg_mul_eq_mul_neg
          ... = -(x - y) : by rw Hn
          ... = y - x : by rw neg_sub
--split,  
    rw transitive,

    end
```

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135607593):
I did what you said, but that doesn't work.

#### [Rob Lewis (Oct 11 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135607681):
You need a comma at the end of the `calc`.

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leave%20term%20mode/calc%20once%20you%20enter%20it%3F/near/135607719):
Oh... thanks. Yep, now it's working.

