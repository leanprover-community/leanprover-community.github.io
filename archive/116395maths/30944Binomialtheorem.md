---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/30944Binomialtheorem.html
---

## Stream: [maths](index.html)
### Topic: [Binomial theorem](30944Binomialtheorem.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 08 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127788179):
Hey! I proved the binomial theorem, if anyone finds it interesting its in a gist here: https://gist.github.com/MonoidMusician/ad43301ee3b4e71c0e1c3d440c6898c5

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 08 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127788226):
just curious: is there an existing definition of the binomial coefficient anywhere, maybe with some lemmas? I couldn't find one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127788345):
@**Chris Hughes** did this but I'm not sure it ever made it into mathlib. I think Chris did pretty much everything in my introduction to proof course. He even did the multinomial theorem (I think this is one of the reasons he's so good at finite stuff :-) )

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 08 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127789175):
```quote
just curious: is there an existing definition of the binomial coefficient anywhere, maybe with some lemmas? I couldn't find one
```
`data.nat.choose`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 11 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127889314):
Hi @**Nicholas Scheel** , it would be great to PR this into mathlib. (@**Chris Hughes**, too :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 11 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127908813):
```quote
Hi @**Nicholas Scheel** , it would be great to PR this into mathlib. (@**Chris Hughes**, too :-)
```
The main reason I didn't do this, is we don't have a sensible definition of sums between naturals yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 11 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127910585):
You mean sums from a to b? Mario always argued that you should do sums from a to a+b (or perhaps a+b-1) and seeing the troubles Patrick had when summing from a to b I am inclined to take Mario's word for it. I know from years of worrying about this sort of thing that I'm completely happy to see a sum from i to j if (and only if) j>=i-1, but if j<i-1 then I always feel something has gone wrong.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 11 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127912967):
I'm just waiting for some definition to end up in the library. I actually needed non commutative products for Sylow, so it would be useful if Patrick PRed his big operators.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 11 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127914048):
I'm sorry I don't have a lot of time for Lean, and it seemed more fun to jump on the perfectoid train because it means team work. But help is very much welcome on the bigop front.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 11 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127914094):
Last time I looked you were doing great with the bigop thing, there didn't seem to be any problems like there were with type class inference for the modules, and I was just leaving you to do it. Then you went back to the normed vector spaces and had type class problems again, which to be honest was a bit depressing, all I remember was the CS people talking about how interesting out_param was. What is the current state of the bigop stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 11 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Binomial%20theorem/near/127914287):
I got tired of nat substraction mainly, especially since `cooper` seems to promise to make all this easier


{% endraw %}
