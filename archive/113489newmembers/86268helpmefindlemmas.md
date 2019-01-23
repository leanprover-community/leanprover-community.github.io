---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/86268helpmefindlemmas.html
---

## Stream: [new members](index.html)
### Topic: [help me find lemmas](86268helpmefindlemmas.html)

---


{% raw %}
#### [ Scott Morrison (Nov 24 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148255862):
Surely these are somewhere?
```
lemma le_pred_of_lt {n m : ℕ} (h : n < m) : n ≤ m - 1 := sorry
lemma pred_le_self (n : ℕ) : n - 1 ≤ n := sorry
```

#### [ Reid Barton (Nov 24 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148255973):
Second is a special case of `nat.sub_le`, do you specifically need it for 1?

#### [ Scott Morrison (Nov 24 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148256181):
Thanks, that'll do fine for the second.

#### [ Scott Morrison (Nov 24 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268678):
We seem to have `le_sub_iff_add_le` for commutative groups, but not `le_sub_of_add_le` for `nat`?

#### [ Scott Morrison (Nov 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268719):
Am I missing something? I want `n + k ≤ b` implies `n ≤ b - k`.

#### [ Mario Carneiro (Nov 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268721):
I am sure it's there

#### [ Mario Carneiro (Nov 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268722):
`nat.basic` has a really comprehensive list of facts like this

#### [ Mario Carneiro (Nov 24 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268728):
`nat.le_sub_right_of_add_le`

#### [ Scott Morrison (Nov 24 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268774):
ah, missing the `right`, thanks

#### [ Scott Morrison (Nov 24 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268883):
I should use find more -- it would have successfully found this lemma, it turns out.

#### [ Scott Morrison (Nov 24 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269200):
```
H_left : n + k ≤ b,
H_right : b < m + k
⊢ b - k < m
```

#### [ Mario Carneiro (Nov 24 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269357):
`nat.sub_lt_right_iff_lt_add`

#### [ Scott Morrison (Nov 24 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269625):
Ah, okay. I just found `sub_lt_sub_right_iff` and managed to use that.

#### [ Scott Morrison (Nov 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269664):
So ... is there some long term plan to avoid me having to memorize all these? :-)

#### [ Mario Carneiro (Nov 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269669):
go to `nat.basic` and browse around, that's what I jst did

#### [ Kevin Buzzard (Nov 24 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270509):
Is the following a crazy idea: we know that we can't just take all the standard results about naturals and mark them as [simp] (some of them are one-way implications for example). Scott is complaining that he cannot find lemmas which are "standard" though. Can we tag a shedload of lemmas in data.nat.basic as "standard" and then instead of Scott having to play guess-the-name (which is still sometimes hard, despite the heroic efforts of the name-that-lemma team), he can just explicitly look for the lemma in the "standard" list. I am not saying that there should be a tactic which attempts to apply more than one standard lemma at once. But I am saying that there could be a `standard` tactic which literally tries to find exactly which lemma you need from a list, and applies it if it's there, and fails otherwise. 

I have had problems recently looking for A -> B if it happens to be the case that A <-> B. I personally never know whether to expect to see A -> B or B -> A or both or neither in the library if A <-> B is in there and I am not sure that there is a rule, especially if one direction needs some random thing I don't care about like decidability. Now I understand the philosophy of the library -- "if it looks standard, it should be there". OK so now let's make it easy to find the standard stuff by tagging it all with standard.

#### [ Mario Carneiro (Nov 24 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270555):
if the bidirectional version is there, the one directional versions should not be there normally, unless the assumptions are different in each direction

#### [ Mario Carneiro (Nov 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270567):
if A -> B requires fewer assumptions than B -> A, you will probably find A -> B with a weak assumption and A <-> B with a strong assumption

#### [ Kevin Buzzard (Nov 24 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270619):
Ah so there is some logic to it? I'd not realised this. Of course the other thing is when you look for A <-> B and it turns out that it's B <-> A which is in there.

#### [ Mario Carneiro (Nov 24 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270627):
in that case it's usually up to "simplification order"

#### [ Kevin Buzzard (Nov 24 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270629):
Is that just me not knowing the implicit total order on all predicates...yeah, that.

#### [ Mario Carneiro (Nov 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270674):
for stuff involving subtraction vs addition, subtraction is on the left

#### [ Kevin Buzzard (Nov 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270679):
So how does that work for add_assoc?

#### [ Mario Carneiro (Nov 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270689):
left assoc on the left, right assoc on the right. not much else to go on in that case

#### [ Kevin Buzzard (Nov 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270697):
But the thing on the right has more characters in, so it's more complicated.

#### [ Kevin Buzzard (Nov 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270700):
It's a comp lemma.

#### [ Mario Carneiro (Nov 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270703):
well that depends on the parser

#### [ Kevin Buzzard (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270752):
what's the logic here?

#### [ Mario Carneiro (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270755):
honestly I would always write an assoc lemma with explicit parens

#### [ Mario Carneiro (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270758):
(I should double check that's not a lie)

#### [ Kevin Buzzard (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270760):
Even then I'm looking at it and thinking it's 50-50

#### [ Mario Carneiro (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270765):
it is 50-50, I'm not going to lie

#### [ Mario Carneiro (Nov 24 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270782):
but you have to pick one order, and it was picked way back in core, and we stick with it

#### [ Kevin Buzzard (Nov 24 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270787):
"Something is simpler if it has fewer brackets". Is that just nonsense?

#### [ Mario Carneiro (Nov 24 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270799):
I'm not sure how much stock to put in what the parser thinks is the best order

#### [ Mario Carneiro (Nov 24 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270842):
I guess that works for mul_add though

#### [ Mario Carneiro (Nov 24 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270846):
I don't know, I wouldn't bet on it

#### [ Kevin Buzzard (Nov 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270856):
OK, so it is random. The reason I am talking about add_assoc explicitly is that since I learnt that many simp or iff lemmas are of the form A = B, A <-> B with B less complicated than A, I've been able to start guessing which is on the left much better. But I still can't guess for add_assoc, so I just have to do look-up.

#### [ Mario Carneiro (Nov 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270863):
yeah, just do the old `.1` ` .2`

#### [ Mario Carneiro (Nov 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270918):
If I were to list a bunch of bracketing combinations in some order, I would probably start from left assoc, maybe that's just me

#### [ Scott Morrison (Nov 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270919):
So far my only idea for escaping "look up the damn lemmas" hell is to experiment with marking them all as `back`, and calling `back` a lot.

#### [ Scott Morrison (Nov 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270923):
I actually think this will solve a lot of my problems.

#### [ Scott Morrison (Nov 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270930):
And `back?` prints the term-mode proof it finds, so it's easy to replace it if it is slow.

#### [ Scott Morrison (Nov 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270934):
However .... all these `<->` lemmas cause a problem.

#### [ Mario Carneiro (Nov 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270938):
metamath (more accurately, one of it's IDEs) had a one-step automatic proof function. It's a life saver for this stuff

#### [ Mario Carneiro (Nov 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270980):
you just write down all the assumptions you need and hit "go" and it finds the lemma

#### [ Mario Carneiro (Nov 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270990):
you have to be pretty specific, but it's great for doing lookups in context

#### [ Scott Morrison (Nov 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148271221):
...

#### [ Kevin Buzzard (Nov 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148271610):
https://www.urbandictionary.com/define.php?term=the%20old%20one%20two

#### [ Johan Commelin (Nov 24 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148280408):
```quote
So ... is there some long term plan to avoid me having to memorize all these? :-)
```
 Yes, the long term goal is that you write some automation so that *we* can all avoid memorising these (-;

#### [ Scott Morrison (Nov 24 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148288111):
The only thing I know how to do for "lemmas involve nat subtraction" is to get `back` up and running and trying beat problems over the head with that. I suspect it will probably work (`back`, especially if it calls `simp` along the way, it's not so far from `auto`) but it won't be pretty.

#### [ Kevin Buzzard (Nov 24 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148288271):
Are these nat subtraction problems solved in Coq? Why are they arising? I am struggling to relate this to $$\oplus_{i\in I}M_i$$ but I never looked at the big operators paper seriously.

#### [ Andrew Ashworth (Nov 24 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148288448):
Nat problems are solved by Omega in coq, aka Cooper in lean

#### [ Scott Morrison (Nov 24 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148294216):
The interaction between big operators and (un)natural subtraction is arising for me because I was working with sums of subset of the naturals, because the `k` in `choose n k` really ought to be a natural number.

#### [ Keeley Hoek (Nov 25 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148300063):
Hey Scott, is there a reason why back @ https://github.com/leanprover/mathlib/pull/410 should still have the WIP tag (not that you decide)/is there any programming work I can do to make it mergeable

#### [ Scott Morrison (Nov 25 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302416):
Yes, I'm sorry this PR has been abandonware for a while.

#### [ Scott Morrison (Nov 25 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302462):
I think the major obstacle is working out what to do with `apply_rules`. I haven't got around to looking at how `apply_rules` is used in mathlib yet.

#### [ Scott Morrison (Nov 25 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302463):
Can we just replace all the uses of `apply_rules` with `back`?

#### [ Scott Morrison (Nov 25 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302517):
It also needs some consideration of lemmas to tag, perhaps.

#### [ Scott Morrison (Nov 25 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302537):
The actual core code at <https://github.com/leanprover/mathlib/pull/410/files#diff-e8836d95f7cd2f7e1c5ee370e791af03R33> could perhaps be rewritten, it reads a bit spaghetti-like at the moment, but I'm not sure what to do.

#### [ Scott Morrison (Nov 25 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302594):
Something that would probably be easy for you, @**Keeley Hoek**, but I was confused by, is combining the `back` and `elim` attributes into just `back` and `back!`.

#### [ Sebastien Gouezel (Nov 25 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148312045):
I don't think `apply_rules` is used anywhere yet, so you can safely remove it. I wrote it for proofs of continuity and limits, where it would be most useful, but there is a bug in Lean 3 `apply` (which unfolds too much) that prevents `apply` from working without underscores on continuity lemmas. So that I could never use it efficiently!

#### [ Keeley Hoek (Nov 25 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148312348):
@**Scott Morrison|110087** When `back` and `elim` are the same attribute what should their single unified description string be?
but sure, I'll do that and then do a tiny shuffle

#### [ Scott Morrison (Nov 25 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148312403):
I forget which way round they go now. One counts as progress even if you don't discharge the goal.

#### [ Keeley Hoek (Nov 25 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148320789):
I put in my 2-cents and did the stuff
I got rid of that ```precedence `?`:0``` thing that worried you scott too

#### [ Scott Morrison (Nov 26 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148337859):
@**Keeley Hoek** I cleaned up a few things, but also realised the current implementation of `back` is hopelessly inefficient, and will need to be replaced.

#### [ Scott Morrison (Nov 26 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148342141):
(I'll continue this in the `PR reviews` stream.


{% endraw %}
