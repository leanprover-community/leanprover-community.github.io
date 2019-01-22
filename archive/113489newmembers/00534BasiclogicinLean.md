---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/00534BasiclogicinLean.html
---

## [new members](index.html)
### [Basic logic in Lean.](00534BasiclogicinLean.html)

#### [Kevin Buzzard (Oct 08 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135404145):
There has been some discussion about Q4 of my first M1F example sheet. The question and my solution are [here](https://github.com/kbuzzard/xena/tree/master/M1F/problem_bank/PB0104) . My solution from this time last year is [here](https://github.com/kbuzzard/xena/blob/a61d6db673ae8ab2672cbf6522894f743b08a6e6/M1F/2017-18/Example_Sheet_01/Questions_02_to_4/M1F_sheet01_solutions02_to_04.lean#L60) and is completely different. @**Chris Hughes** and @**Kenny Lau**  -- did you ever attempt to do M1F sheet 1 Q4 in Lean this time last year?

#### [Kevin Buzzard (Oct 08 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135404266):
@**Abhimanyu Pallavi Sudhir** 's solution is here: https://github.com/abhimanyupallavisudhir/lean/blob/master/m1f_sols/exsht01.lean

#### [Kevin Buzzard (Oct 08 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135404326):
Part of me feels like this would be a lot more fun in `bool`.

#### [Johan Commelin (Oct 08 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135404440):
You didn't teach them `ring`?

#### [Mario Carneiro (Oct 08 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135404664):
By the way, @**Scott Morrison** this is a good example of where `fin_cases` on things other than `fin` would help

#### [Mario Carneiro (Oct 08 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135404733):
we have a fintype instance for `Prop`, which would substitute for `classical.cases` in this case

#### [Mario Carneiro (Oct 08 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135405066):
It would do basically the same thing as this:
```lean
variables P Q R S : Prop

theorem m1f_sheet01_q04 : (P → (Q ∨ R)) ∧ (¬ Q → (R ∨ ¬ P)) ∧ ((Q ∧ R) → ¬ P) ↔
  (¬ P) ∨ (P ∧ Q ∧ ¬ R) ∨ (P ∧ ¬ Q ∧ R) :=
by refine classical.cases_true_false _ _ _ P;
   refine classical.cases_true_false _ _ _ Q;
   refine classical.cases_true_false _ _ _ R; simp
```

#### [Patrick Massot (Oct 08 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135405999):
```lean
theorem m1f_sheet01_q04 : (P → (Q ∨ R)) ∧ (¬ Q → (R ∨ ¬ P)) ∧ ((Q ∧ R) → ¬ P) ↔
  (¬ P) ∨ (P ∧ Q ∧ ¬ R) ∨ (P ∧ ¬ Q ∧ R) :=
by  split ; finish
```
:mischievous:

#### [Kevin Buzzard (Oct 08 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135407445):
```quote
You didn't teach them `ring`?
```
I wrote and am writing docs randomly and students are reading them randomly.

#### [Kevin Buzzard (Oct 08 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135407480):
http://wwwf.imperial.ac.uk/~buzzard/xena/

#### [Kevin Buzzard (Oct 08 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135407537):
yeah, I haven't pushed the stuff I wrote about `ring`. My bad.

#### [Kevin Buzzard (Oct 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135407586):
I'm currently trying to get all the questions up for sheet 1.

#### [Johan Commelin (Oct 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135407613):
It's just that I felt sorry when I saw that 10-line `calc`ulation.

#### [Kevin Buzzard (Oct 08 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135408370):
Ah nonono, wait, I gave the students the axiom that `x^2-3x+2=0 iff x = 1 or x = 2`

#### [Kevin Buzzard (Oct 08 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135408792):
But here's the problem -- giving them stuff is hard. It's hard to make a global import work for something which is not in mathlib on the systems my students use (cocalc, local lean set-up in our computer room, their Lean laptops). Can one pull a github dependency to a local machine easily using VS Code? Even that will not solve most of the problems. Both cocalc and my local ICT people have not given me a robust way of being able to add a growing library, and I didn't get this library written over the summer so I am having to write it now in real time.  However I do have a "homework" option with cocalc which I think should work. 

The vast majority of students use my Xena.zip set-up on a computer in our computer room, where Lean is installed on all machines by magic via my cheap instructions, and I forgot to put a back door in the zip file and they wrote the script and now it's difficult for me to get the set-up changed. [ Hmm. I wonder if their script downloads Xena.zip or uses a local copy? Surely the latter.]

#### [Kevin Buzzard (Oct 08 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135408822):
I guess my mistake here is that I did not completely write the library before I was forced to make decisions which could not be easily reversed.

#### [Kevin Buzzard (Oct 08 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135408915):
Basically my solutions from last year need heavy editing, because I don't want the students to have to struggle through easy-in-maths less-easy-in-lean stuff, it will just get in their way. So all the stuff like x^2-3x+2=0 iff x=1 or x=2 is being moved into a different library; they just cluttered up my solutions last year. I can't figure out how to deliver this library to them easily though in our computer room. Hmm.

I might go for making it all work out of the box on cocalc and then making public github repos for the problem sheets; I won't need to worry about .olean files because the libraries will be very small and easy to compile. Is it easy for a complete git beginner to clone a github repo and open it completely within VS Code? Oh -- you can link to a zip file or something and tell them to unzip and open folder maybe?

#### [Patrick Massot (Oct 08 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135409410):
You can put olean in the zip only if you know their OS

#### [Kevin Buzzard (Oct 08 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135409724):
Right. I think I will have to skip olean files. Patrick's position is not even the official one, I believe: didn't Sebastian say they were not even guaranteed to run on a different machine with the same OS?

#### [Gabriel Ebner (Oct 08 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135410223):
The olean files should be machine- and OS-independent (but they definitely depend on the Lean version).  However you need to be really careful with the file modification times.  They need to be 1) after the olean files for lean itself, 2) after the lean files, and 3) in the correct order (i.e. logic/function.olean should be older than analysis/real.olean)

#### [Scott Morrison (Oct 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135427947):
@**Gabriel Ebner**  --- presumably condition 3) is satisfied if they all have exactly the same timestamp?

#### [Scott Morrison (Oct 08 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135428020):
Cloning a repo from VS Code consists of opening a terminal inside VS Code and doing it on the command line there...

#### [Scott Morrison (Oct 08 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135428096):
The fact that you need to make updates really suggests you should be using `leanpkg`. There's no need to interact with the command line --- in VS Code there is a command to run `leanpkg upgrade`.

#### [Gabriel Ebner (Oct 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135450329):
Yes, apparently the check is less-than-or-equals.

#### [Mario Carneiro (Oct 09 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135450407):
I sometimes use `find . -name "*.olean" -exec touch {} +` for this

#### [Kevin Buzzard (Oct 09 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135471295):
Does this ensure that `logic/function.olean` has a timestamp which is less than or equal to that of `analysis/real.olean`?

#### [Gabriel Ebner (Oct 09 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135472635):
If you run `touch a b c d`, then `touch` will assign the same timestamp to all four files.  `find -exec touch {} +` calls `touch` a single time with all files as arguments.

#### [Kevin Buzzard (Oct 09 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Basic logic in Lean./near/135481231):
Oh that's pretty cool. I had just assumed it was running the command on each successful find.

