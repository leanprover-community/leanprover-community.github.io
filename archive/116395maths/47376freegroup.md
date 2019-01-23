---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/47376freegroup.html
---

## Stream: [maths](index.html)
### Topic: [free group](47376freegroup.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494694):
@**Kevin Buzzard**  here's my old version of free group https://github.com/kckennylau/Lean/blob/c6eac863b23d58d40deaab62489f6069f860407e/free_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494732):
is this what you wanted?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494739):
you see, ambient has two universe parameters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494792):
and this fucks up everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494806):
Yes!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494807):
I thought Lean would somehow fix this, but the stupid issue is still there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494846):
Maybe you can get  a contradiction with a diagonal argument if you can get it to work all in the same universe :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494847):
I didn't read all of what Mario had to say about this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494854):
It's a bit annoying though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494860):
it's maximally impredicative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494861):
it's philosophically unsound

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494862):
You could be even less constructive by replacing generate with span

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494903):
I never know which is which

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494905):
they are synonymous in my head

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494906):
you can't just quantify through every gorup and pretend that you have the UMP wrt every group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494911):
but the one where you say "if I am a subgroup of the big product containing S, then I contain span S"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494912):
the point is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494913):
you need to build the ambient group from S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494914):
if you want things to work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494954):
I don't really understand why you can't just quantify through every group and pretend you have the UMP. Maybe I should read Mario's posts more carefully, wherever they've gone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494956):
because it's cheating

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494958):
I don't want to make the set of all sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494960):
not because it's cheating

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494961):
but because it leads to hell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494962):
whereas free groups won't take you to hell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494963):
because they really do exist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494967):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124494970):
but that isn't the way to justify it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495021):
To build the free group in the ZFC approach, do you first build the abstract group (the subset of the product) and then say "aah it's generated by S so there's something isomorphic to it in V_kappa"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495025):
correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495026):
Can one prove such a theorem in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495031):
"If I am an object in some universe then sometimes you can build some object in some smaller universe which is isomorphic to me"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495075):
actually

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495077):
what cardinality do you need?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495083):
if you have n letters, to make a word of length k, you have at most k! n^k ways right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495084):
no, just n^k

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495086):
so it's just n^omega

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495126):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495127):
I mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495128):
now that I built it in the proper way, I don't see why we're beating a dead horse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495179):
@**Mario Carneiro** ves algum problema em o meu pull?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124495277):
@**Kevin Buzzard** "but that impredicative construction is not like constructing the set of all sets because it really exists" it is actually only correct iff you can justify its existence predicatively. that's the wrong justification for the right thing, and it doesn't tell you that it actually exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496544):
`n^omega` is not at all the sum of `n^k` as I'm sure you know. Finitely-generated groups are all countable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496589):
The point is that if `S` has cardinality $$\kappa$$ and if $$\kappa'$$ is the max of $$\kappa$$ and $$\aleph_0$$ then any group generated by `S` has cardinality at most $$\kappa'$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496590):
eew what kind of a `\kappa` is that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496824):
@**Kevin Buzzard** by n^omega I mean union n^k

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124496825):
ordinal exponent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497132):
@**Kevin Buzzard** You can do such "arguments by cardinality" for universe resizing in lean as well. An example of this is:
```
theorem  lift_down {a : cardinal.{u}} {b : cardinal.{max u v}} : b ≤ lift a → ∃ a', lift a' = b
```
which says that a cardinal that is smaller than a cardinal lifted from a small universe is also lifted from the small universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497193):
that epsilon-abstraction though @**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497199):
say what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497208):
so you can't find that cardinal explicitly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497215):
which cardinal are you referring to? the exists in that theorem is unique

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497255):
axiom of unique choice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497259):
cardinal theory uses choice everywhere, so meh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497261):
i see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497262):
fair enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497263):
but it is explicitly constructed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497264):
so do you see any problem with my pr

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497279):
I don't think so. The only other thing I might want is a constructive reduced word function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497320):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497529):
@**Mario Carneiro** linked list though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124497631):
you need decidable equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124499790):
https://github.com/kckennylau/Lean/blob/master/free_group.lean#L266

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124499791):
@**Mario Carneiro** done!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512164):
https://github.com/kckennylau/category-theory/blob/master/src/free_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512166):
@**Mario Carneiro** could you help me prove `reduce.exact`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512261):
do you know that the reduced word is minimal in length in the equivalence class?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512264):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512267):
that's `reduce.min`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512272):
that just says that the reduced word is smaller than the input

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512280):
I mean if v ~~ w then length (reduce w) <= length v

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512283):
oh, I don't know that then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512336):
You may find http://us.metamath.org/mpeuni/mmtheorems154.html helpful; that's my construction of free groups in metamath by a similar method (it's more cumbersome in ZFC since it has to describe the whole reduction sequence, not just the result)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512381):
...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512522):
I think I see the proof strategy. It goes by induction on the length of an extension sequence, proving that if two extension sequences (where one has length <= n) end at the same point, then they start at the same point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512523):
I thought you wrote it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512524):
I'm rereading the proof now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512530):
An extension sequence is a sequence that starts at a reduced word and inserts cancelling pairs one at a time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512533):
and the first step in the proof shows that every word has an extension sequence that terminates with it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124512626):
Since the length of an extension sequence is also (half) the difference in length between the initial word and the reduced word, you could try induction on that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513001):
Okay, here's a suggestion in your language: can you prove the following?
```
inductive red (IT : Type u) [inv_type IT] :
  inv_type.to_inv_mon IT → inv_type.to_inv_mon IT → Prop
| cons : ∀ a x y, red x y → red (a :: x) (a :: y)
| cancel : ∀ a x, red (a :: a⁻¹ :: x) x

theorem eqv_gen_red (IT : Type u) [inv_type IT]
  {x y : inv_type.to_inv_mon IT} : x ≈ y ↔ eqv_gen (red IT) x y :=
sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513020):
this will considerably simplify your induction for the `reduce.exact` theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513023):
but I don't need to simply `reduced.sound`, I need to prove `reduced.exact`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513068):
yeah that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513074):
You could also fold in the eqv_gen constructors into the constructors of `red` if you prefer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513077):
although splitting it this way gives you the ability to talk about one step reduction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513180):
proving multiplication amounts to the same amount of work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513182):
```
case inv_mon.to_group.rel.mul
IT : Type u,
_inst_1 : inv_type IT,
x y c d p q : inv_type.to_inv_mon IT,
h1 : inv_mon.to_group.rel (inv_type.to_inv_mon IT) c p,
h2 : inv_mon.to_group.rel (inv_type.to_inv_mon IT) d q,
ih1 : eqv_gen (red IT) c p,
ih2 : eqv_gen (red IT) d q
⊢ eqv_gen (red IT) (c * d) (p * q)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513183):
i.e. I can't prove it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513231):
Try proving `eqv_gen (red IT) x y ->  eqv_gen (red IT) (a * x * b) (a * y * b)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513281):
which reduces to `red IT x y -> red IT (a * x * b) (a * y * b)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/free%20group/near/124513325):
(You could also do the left and right multiplications as separate lemmas)


{% endraw %}
