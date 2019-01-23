---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/27022desugaringhave.html
---

## Stream: [new members](index.html)
### Topic: [desugaring have](27022desugaringhave.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 02 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226383):
https://gist.github.com/luxbock/f0c19afd8d88fef9c13814ba072b9eb5

Can anyone explain what I'm doing wrong? I tried adding parentheses in different places but couldn't make it work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Etienne Laurin (Sep 02 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226658):
I think you need to add parenthesis around `(and.right h)` and  `(and.left h)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 02 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226707):
In this case around and.left h

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 02 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226708):
You need parentheses around the argument of a function. `f x y` means `(f x) y`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 02 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226719):
thanks, yeah that did it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 04 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133333637):
https://gist.github.com/luxbock/0e19b04aaca49ccf18e5df060d2d3e8e

same as last time, except now I feel fairly confident that I should have got this right, but I don't understand why it's not able to infer the right types for the disjunction. I realize this is probably not how you'd ever write things, but nevertheless am I doing something wrong here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133336029):
I get a gazillion errors when I copy paste

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133336459):
but apart from that, as I'm sure you know, the problem is that `or.inl hq` doesn't have enough information to know it's a proof of `q or r`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133336492):
Here are two ways to fix it: for the first error, replace the offending line with `and.intro hp (@or.inl q r hq))` i.e. use the `@` trick and tell Lean the implicit variables yourself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133336556):
For the second line, you could write `and.intro hp (or.inr hr : q ∨ r))` , i.e. tell Lean the type you want it to be.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 05 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133358915):
thanks, that does indeed work.

The reason I find this confusing is because based on reading the tutorial, I thought that `have` would desugar as I wrote it. It should have all the same information compared writing it with `have`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 05 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133360074):
My non-expert guess as to what is going on is this. Lean sometimes doesn't have enough information to work out what the type of something is (e.g. when you type `or.inr hr`). When this happens it inserts a metavariable instead (e.g. `?m_1[hpr, _, _]`). You talk about desugaring, but I think the process which is behaving differently in the two cases is the elaboration process, when these metavariables get solved. Elaboration is a complicated thing and depends on a lot of stuff going on in the background, for example whether various terms are tagged `elab_simple` or `elab_as_eliminator` or whatever -- even changing the way you apply a function `f {a} b` from `f b` to `@f _ b` can (and often does) change the elaboration strategy. In short, I don't think this is about desugaring, it's about the complex elaboration process which goes on behind the scenes after that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Olli (Sep 05 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133365624):
yeah it was a good exercise to do, because I learned something from it


{% endraw %}
