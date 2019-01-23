---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76230withoutlossofadvertisement.html
---

## Stream: [general](index.html)
### Topic: [without loss of advertisement](76230withoutlossofadvertisement.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491146):
Let me share my joy of using @**Simon Hudon** recent contributions (not yet merged, see https://github.com/PatrickMassot/mathlib/tree/wlog_ext for a version including both relevant PR if you want to play with it).

I defined homeomorphisms between topological spaces `X` and `Y`, and the support of a homeomorphism `f` from `X` to itself (if you don't know what this means, think `homeo X X` coerces to invertible functions from `X` to `X` and `supp f` is the set of `x` in `X` such that `f x ≠ x`, that's good enough approximation). I want to prove the trivial yet important fact that two homeos with disjoint support commute. I already had various proofs of that, some versions written with the help of Mario. But I'd like to show what the latest version looks like. So statement is:

```lean
example {f g : homeo X X} (H : supp f ∩ supp g = ∅) : f * g = g * f
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491159):
First consider the pen and paper proof: We need to prove f (g x) = g (f x) for all x in X. If x is neither in supp f nor in supp g then it's obvious, so let's discard this case. WLOG x is in supp f since everything is obviously symmetric in f and g. By H, x is not in supp g. Also the support of f is stable under f (because its complement the fixed points set is obviously stable). So f x is also not in supp g. So g x = x and g (f x) = f x and we are done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491165):
Simon's work help with the first and third sentences. First "We need to prove f (g x) = g (f x) for all x in X". But actually `homeo X X` is not quite `X → X` so we can't do `funext x`. We only need a extensionality lemma for homeos, and tag it with the `[extensionality]` attribute to later write `ext x` in place of `funext x`. Same would work for sets etc. 

Now the third sentence is much more spectacular: "WLOG x is in supp f since everything is obviously symmetric in f and g". I still cannot write this without sweating and thinking: Oh my god, Lean will disagree it's obvious. Simon's tactic turns this into: `wlog h : x ∈ supp f using f g`. Period. No disagrement. :heart_eyes:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491204):
Here is what it looks like. Notice also liberal use of the finish tactic.

```lean
lemma fundamental' {f g : homeo X X} (H : supp f ∩ supp g = ∅) : f * g = g * f :=
begin
  ext x,
  by_cases H' : x ∈ supp f ∨ x ∈ supp g,
  { -- Here we assume H' : x ∈ supp f ∨ x ∈ supp g
    wlog h : x ∈ supp f using f g,
    have x_not_supp_g : x ∉ supp g := (subset_compl_iff_disjoint.2 H) h,
    have f_x_supp_f : f x ∈ supp f, 
    { have : f x ∈ f '' supp f := mem_image_of_mem f h, 
      finish [stable_support f] },
    have : f x ∉ supp g := (subset_compl_iff_disjoint.2 H) f_x_supp_f,
    finish [fix_of_not_in_supp] },
  { -- Now we assume H' : ¬(x ∈ supp f ∨ x ∈ supp g)
    rw not_or_distrib at H',
    finish [fix_of_not_in_supp] }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491205):
And a `calc` version for good measure.

```lean
lemma fundamental'' {f g : homeo X X} (H : supp f ∩ supp g = ∅) : f * g = g * f :=
begin
  ext x,
  by_cases H' : x ∈ supp f ∨ x ∈ supp g,
  { -- Here we assume H' : x ∈ supp f ∨ x ∈ supp g
    wlog h : x ∈ supp f using f g,
    exact calc 
    (f * g) x = f (g x) : by simp
          ... = f x     : by { have x_not_supp_g : x ∉ supp g := (subset_compl_iff_disjoint.2 H) h,
                               finish [fix_of_not_in_supp] }
          ... = g (f x) : by { have f_x_supp_f : f x ∈ supp f,
                               { have : f x ∈ f '' supp f := mem_image_of_mem f h, 
                                 finish [stable_support f] },
                               have : f x ∉ supp g := (subset_compl_iff_disjoint.2 H) f_x_supp_f,
                               finish [fix_of_not_in_supp] }
          ... = (g * f) x : by simp },
  { -- Now we assume H' : ¬(x ∈ supp f ∨ x ∈ supp g)
    rw not_or_distrib at H',
    finish [fix_of_not_in_supp] }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491206):
Term mode people will have a really hard time converting me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491435):
What a nice homage! Thank you! I'm so happy that you like those tools :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 21 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491663):
let's see how long we'll need to wait before they merge the PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125491898):
```quote
What a nice homage! Thank you! I'm so happy that you like those tools :)
```
I'm not only the annoying user who can't code anything by himself, and keep reminding you to work on these tactics (and write tactic writing tutorials covering `pi_instance` and `wlog`). I also love using them, and documenting things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492035):
And I think the community is currently working really well. It seems to me we recently went from the pretty horrible situation where the main dev felt harassed by frustrated users to a pretty nice situation. Leo and Sebastian are peacefully working on Lean 4 while everybody else finds some place in the Lean 3 world. Clearly we don't want Leo to spend time writing tactics like `wlog`. We want power users like Mario, you, Scott... to write these. And then we have dumb users like me who can come up with examples finding bugs, suggests new tactics, write documentation... And everybody has fun, I think. And it seems Lean 4 will expose even more to Lean without touching C++ code or even PRing the main repo, so we are clearly going in the right direction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492037):
```quote
let's see how long we'll need to wait before they merge the PR
```
Ok, we still have some frustration...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492044):
But I'm optimistic anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492086):
And I hope that writing an example non-trivially using `wlog` actually helps getting the PR merged more than complaining that reviewing PR takes time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 21 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492181):
I always like to see a tool in use, that definitely brings it up the todo list

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492500):
> And I think the community is currently working really well.

I've also had a very positive experience in the community with people eager to help and grateful when you give then a nudge. I was surprised and saddened that Leo described his experience as harassment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125492683):
```quote
And then we have dumb users like me who can come up with examples finding bugs, suggests new tactics, write documentation...
```

Yeah! Darn those dumb users, leeching off the community and only proving important mathematical theorems!

But seriously, I'm really glad you decided to champion the cause of documentation. It's often neglected but it makes such a big difference!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 21 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493169):
Is lack of documentation why Coq hasn't been adopted widespreadly (ok this is not really English) after 30 years?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493254):
Hard to say. To be fair, I found Coq much harder to pick up than Lean. I never actually ended up applying it to large problems. I think the standard library is ill-organized and much harder to use than Lean's.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Apr 21 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493319):
That's because there is no organisation so to speak; no hierarchy either. You have, for example, two different versions for Z<theroem> and N<theorem>.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493359):
Maybe you could summarize that as: when you're a beginner, you have to get over a lot humps before you can begin to try stuff on your own. It feels like with Lean, once you installed it, you start hacking and it progressively becomes harder as you get more ambitious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493361):
Yeah, it looks a bit like a research project that just happened to be useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125493372):
And I find it doesn't help that the library is built around ML modules more than around type classes. Type classes are really tremendous to make things simple to use.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505376):
My 2 cents: I think that the Coq community, and the automated theorem proving community in general, have done a bad job of advertising to mathematicians. I remember the edition of the Notices of the AMS coming out a few years ago which concentrated on this stuff and wondering if it was the future, but somehow the jewels in the crown at the time were things like "yet another proof of the 4 colour theorem" and maybe this was just after the odd order theorem, which was something mathematicians had long moved on from.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505378):
My gut feeling is that a different approach is needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505426):
so that's why I'm going to try concentrating on getting undergraduates in mathematics to prove a bunch of basic stuff, because I think it might have a different kind of outcome.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505430):
Maybe a bunch of young people who know about this stuff will somehow integrate it into the maths community in a different way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505485):
Let me absolutely echo the opinions of the others in this thread -- I've had a really good time learning Lean here, I would never have got anywhere without this group, and now I feel like I actually understand certain aspects of the software well enough to be able to use it without being continually frustrated.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505489):
The strategy of "if you don't get it, find out about it and then write some docs" also works really well for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505498):
And also the idea of choosing a non-trivial thing to work on and then just working on it has taught me a huge amount. There are just over 5000 lines of code in the stacks project directory now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505645):
Roughly, how many lines are pure commutative algebra and how many use geometric language?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505821):
it wouldn't surprise me if nearly 1000 lines were cut-and-pasted stacks project LaTeX :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505839):
I guess it's almost all algebra at the minute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505885):
@**Johan Commelin** pointed out a typo in my definition of scheme and I told him not to believe my definition until we had some proof of a lemma about schemes which was geometric

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505886):
and I am not sure how geometric you think this is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505887):
but he suggested the Spec / Gamma duality, Hom(S,Spec(A)) = Hom(A,Gamma(S))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505888):
I know the distinction is hard to make (Grothendieck did this on purpose!). Let's say: how many lines not containing "sheaf" or "presheaf"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505890):
which I think would be a true test

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505898):
Oh there are lots and lots of lines proving abstract stuff of the form "if I have a presheaf only defined on a basis of open sets for a topology, but it satisfies the sheaf axiom for a cofinal set of covers, then it extends uniquely to a sheaf on the whole space"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505943):
I don't really know how to answer your questions precisely though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505944):
There's a bunch of lemmas about rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505948):
and then a bunch of lemmas about presheaves and sheaves

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505950):
and then some actual mathematics saying that some sequence of rings is exact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 21 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505959):
and I'm just in the process of writing the glue which will glue it all together.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125505966):
Did you try to separate nicely as much sheaf theory from ring theory as possible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506367):
so would you say it took you about a year of using lean before you felt confident in doing things in it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 21 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506370):
i wonder how much faster your summer undergraduates and fall students will learn lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506407):
I think he started less than a year ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506410):
Last July maybe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506411):
Maybe even August

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 21 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506463):
two semesters of focused effort sounds about right though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 21 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506465):
coincidentally that's how long it takes to get through software foundations 1-3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 21 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506571):
if i had to guess that right there is the reason it never took off in 30 years

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 21 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506611):
imagine if you had to spend two semesters before you could write latex or use a computer algebra system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 21 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125506667):
Also don't forget it's not like Coq was ready on year one and then waited for 30 years

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 22 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125509691):
Yes I started when I was in MSRI in July/August 2017

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 22 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125509731):
but I'm not entirely sure you can call my efforts focussed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 22 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125509732):
I was teaching a class of 220 students in one of the terms, and being head of pure maths and teaching a graduate course in the other one :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 22 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without%20loss%20of%20advertisement/near/125509733):
On the other hand I pretty much gave up all of my other hobbies

