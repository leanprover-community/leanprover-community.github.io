---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81964XofYofZnaming.html
---

## Stream: [general](index.html)
### Topic: [X_of_Y_of_Z naming](81964XofYofZnaming.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 12 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954801):
What theorem is called `X_of_Y_of_Z`? Is it `Y -> Z -> X` or `Z -> Y -> X` or even something else? Or are things more fluid than this?

#### [ Chris Hughes (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954877):
`Y -> Z -> X`

#### [ Chris Hughes (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954879):
as in `lt_of_le_of_lt`

#### [ Kevin Buzzard (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954882):
Right, that's why I asked.

#### [ Kevin Buzzard (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954886):
I just don't understand how the brackets work

#### [ Kevin Buzzard (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954890):
If "of" means "follows from"

#### [ Andrew Ashworth (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954892):
is `of` right associative

#### [ Andrew Ashworth (Apr 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954929):
since it represents `->`

#### [ Kevin Buzzard (Apr 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954935):
then `Y->Z->X` is `Y->(Z->X)`

#### [ Kevin Buzzard (Apr 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954938):
which is `(X_of_Z)_of_Y`

#### [ Andrew Ashworth (Apr 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954942):
it is also a mystery to me, hah

#### [ Simon Hudon (Apr 12 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954957):
I think `X_of_Y_of_Z` is `Y -> Z -> X`: only the consequent is out of order in the name

#### [ Kevin Buzzard (Apr 12 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954958):
well `(X_of_Y)_of_Z` seems to mean `Z->(Y->X)` and `X_of_(Y_of_Z)` seems to mean `(Z->Y)->X`

#### [ Kevin Buzzard (Apr 12 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955010):
So are you clear on the logic? What does `A_of_B_of_C_of_D` say?

#### [ Kevin Buzzard (Apr 12 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955028):
I don't know these fancy CS terms like consequent by the way

#### [ Kevin Buzzard (Apr 12 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955031):
Sorry

#### [ Andrew Ashworth (Apr 12 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955034):
somewhere, a logician is crying

#### [ Kevin Buzzard (Apr 12 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955038):
next you'll be telling me that something is a minor premise

#### [ Simon Hudon (Apr 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955076):
```quote
well `(X_of_Y)_of_Z` seems to mean `Z->(Y->X)` and `X_of_(Y_of_Z)` seems to mean `(Z->Y)->X`
```
I disagree with that assessment. I would say that `A_of_B_of_C_of_D` is `B -> C -> D -> A`

#### [ Chris Hughes (Apr 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955081):
I think `of` doesn't follow right or left associativity rules

#### [ Simon Hudon (Apr 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955083):
Consequent is the only positive term in a chain of implications, i.e. the right-most term.

#### [ Andrew Ashworth (Apr 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955144):
if i had to guess i would think like simon it's right assoc

#### [ Andrew Ashworth (Apr 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955153):
so a_of_b... is B -> C -> D -> A

#### [ Andrew Ashworth (Apr 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955170):
so how do we put parentheses in our theorem names? who knows

#### [ Andrew Ashworth (Apr 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955173):
oh

#### [ Andrew Ashworth (Apr 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955179):
i have seen `imp` used in theorem names

#### [ Simon Hudon (Apr 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955181):
```quote
I don't know these fancy CS terms like consequent by the way
```
I wonder if we could create a sitcom where a mathematician and a computer scientist share a flat. I'm sure they'd get into lots of crazy (conceptual) hijinks

#### [ Andrew Ashworth (Apr 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955184):
so `(a->b)->c` is `c_of_a_imp_b`

#### [ Simon Hudon (Apr 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955228):
```quote
if i had to guess i would think like simon it's right assoc
```
I don't think that's an associativity rule actually.

#### [ Andrew Ashworth (Apr 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955235):
if it isn't that way, it should be, it should follow the same rules as `->`

#### [ Andrew Ashworth (Apr 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955238):
otherwise my brain may explode

#### [ Simon Hudon (Apr 12 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955256):
As for `imp`, the difference is that you use `imp` where you would normally use `le` or `lt`: `and_imp_and_of_imp_of_imp` for example to state that conjunction is monotonic in both arguments

#### [ Andrew Ashworth (Apr 12 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955306):
frankly speaking, trying to remember how a theorem should be named is kinda of ridiculous. when lean 4 comes out i'm sure @**Moses Schönfinkel** will write the Lean SearchAbout we've been waiting for :)

#### [ Andrew Ashworth (Apr 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955407):
i have the same general hatred when it comes to reading C++ qualifiers

#### [ Andrew Ashworth (Apr 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955416):
the rule is, read it from the right and wrap around, which is terrible

#### [ Andrew Ashworth (Apr 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955431):
http://goshdarnfunctionpointers.com

#### [ Simon Hudon (Apr 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955478):
Now I remember that fun :)

#### [ Kevin Buzzard (Apr 12 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955781):
Looking through mathlib it does seem to be consistently using `X_of_Y_of_Z : Y -> Z -> X`

#### [ Kevin Buzzard (Apr 12 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955786):
and there was me thinking there would be some sort of logic ;-)

#### [ Kevin Buzzard (Apr 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955852):
```
lt_of_lt_of_le 
lt_of_le_of_lt 
pos_of_dvd_of_pos
decidable_of_decidable_of_iff
neg_of_nat_of_succ
lt_add_of_le_of_pos
mem_of_eq_of_mem
mem_of_subset_of_mem
eq_of_subset_of_subset
nat.not_coprime_of_dvd_of_dvd
eq_of_le_of_forall_le_of_dense
mul_nonpos_of_nonpos_of_nonneg
lt_add_of_lt_of_nonneg
eq_of_sublist_of_length_le
not_mem_cons_of_ne_of_not_mem
eq_of_sorted_of_perm
heq_of_heq_of_eq
decidable_of_decidable_of_iff
div_of_neg_of_pos
```

#### [ Chris Hughes (Apr 12 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956074):
Does it really matter? If I want `pos_of_dvd_of_pos` and I get `pos_of_pos_of_dvd` they're both the same thing.

#### [ Kevin Buzzard (Apr 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956089):
oh they are very anal about names here :-)

#### [ Kevin Buzzard (Apr 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956144):
looking through that stacks file you wrote I see `lemma thingy ...` so perhaps you are less fussy than them ;-)

#### [ Simon Hudon (Apr 12 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956317):
The logic I see is: `<something>_of_<list_of_assumptions_separated_by_of>` and that list of assumptions is in the order that you should feed them to a function application if you build the proof term by hand. You could advocate for `<list_of_assumptions_separated_by_of>_of_<something>` so that the name mentions assumptions in the same order as the type but I think it's very useful that the first thing you see in the name is what you can achieve with it.

#### [ Kevin Buzzard (Apr 12 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956617):
Yes that's why they went for of rather than imp, right? I like that, I just can't make any sense of the logic for the rest of it when there are two ofs

#### [ Simon Hudon (Apr 12 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956706):
You mean like `lt_of_lt_of_le`? It proves `lt` from two assumptions: 1. `lt`; 2. `le`. The order of those assumptions is the same as in the name

#### [ Kevin Buzzard (Apr 12 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956718):
right, as in `lt_of_lt_and_le`

#### [ Simon Hudon (Apr 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956722):
Yeah, exactly

#### [ Kevin Buzzard (Apr 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956763):
but not as in `lt_is_implied_by_lt_which_is_implied_by_le`

#### [ Kevin Buzzard (Apr 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956769):
i.e. not as in `lt_of_lt_of_le`

#### [ Kevin Buzzard (Apr 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956776):
if "of" is supposed to mean "is implied by"

#### [ Kevin Buzzard (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956791):
and also not as in "(lt_is_implied_by_lt)_is_implied_by_le"

#### [ Kevin Buzzard (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956839):
but actually exactly as in "(lt_is_implied_by_le)_is_implied_by_lt"

#### [ Kevin Buzzard (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956842):
i.e. exactly "(lt_of_le)_of_lt"

#### [ Simon Hudon (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956847):
Right. I guess that's where the associativity talk is relevant. It's `(lt of lt) of le` with the little twist that the assumptions are shuffled ..

#### [ Kevin Buzzard (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956852):
Aah

#### [ Kevin Buzzard (Apr 12 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956860):
for you `X -> Y ->Z` and `Y -> X -> Z` are exactly the same

#### [ Simon Hudon (Apr 12 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956861):
Yes. As you said

#### [ Simon Hudon (Apr 12 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956866):
Because it's equivalent to `lt_of_lt_and_le`, the assumptions commute

#### [ Simon Hudon (Apr 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956921):
They are logically equivalent

#### [ Kevin Buzzard (Apr 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956924):
so you're saying `lt_of_lt_of_le` and `lt_of_le_of_lt` should be defeq? ;-)

#### [ Simon Hudon (Apr 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956928):
Nooooooo, no, no, no! :stuck_out_tongue_closed_eyes:

#### [ Kevin Buzzard (Apr 12 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956937):
then why did you name one after what the other one does? ;-)

#### [ Simon Hudon (Apr 12 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956942):
Because I'm a bad person

#### [ Simon Hudon (Apr 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124957006):
Of course the names leave out important information that we have to rely on your imagination to fill in. The full name should be `x_lt_z_of_x_lt_y_of_y_le_z`. Then swapping the assumptions is not semantically meaningful, it's just confusing.

#### [ Simon Hudon (Apr 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124957015):
Note: defeq and logically equivalent, are not the same by the way ;-)

#### [ Mario Carneiro (Apr 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958788):
The `X_of_Y_of_Z` means `Y -> Z -> X` convention is used throughout mathlib, and it was documented a long time ago in Jeremy's style notes

#### [ Kevin Buzzard (Apr 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958797):
Yes, I learnt that now, from example

#### [ Kevin Buzzard (Apr 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958799):
I was just querying the logic

#### [ Mario Carneiro (Apr 12 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958807):
> The hypotheses are listed in the order they appear, *not* reverse order. For example, the theorem `A → B → C` would be named `C_of_A_of_B`.

https://github.com/leanprover/mathlib/blob/master/docs/naming.md

#### [ Mario Carneiro (Apr 12 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958868):
The logic is, the consequent is the most important part, so it comes first (this is important for autocomplete), but otherwise there is no reshuffling of names from the order they appear in the statement or the order you use them

#### [ Mario Carneiro (Apr 12 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958921):
Don't think too hard about currying these things, theorems are generally fully applied anyway

#### [ Moses Schönfinkel (Apr 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124973894):
@**Andrew Ashworth** I 100% will.


{% endraw %}
