---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/07055Independentforallonnat.html
---

## Stream: [maths](index.html)
### Topic: [Independent forall on nat](07055Independentforallonnat.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130859554):
Are there any known independent propositions of the form `∀ x : ℕ, p x `, where `p` is a decidable predicate?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 03 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130860599):
My vague understanding of Friedman's work is that he comes up with statements about finite objects which are independent of ZFC, but they can be typically proved using large cardinal axioms. But are you talking about independence in Lean + the three usual axioms, which I think is a much stronger statement?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 03 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130860948):
more or less yes. Does independence in ZFC not imply independence in lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130861681):
No, of course Con(ZFC) is independent of ZFC and provable in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130861700):
But Con(lean) can be expressed as a Pi01 sentence, i.e. as `∀ x : ℕ, p x` where `p` is decidable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130861795):
I don't know if any of the "cheap shot" independent statements like `N = Z` can be written as arithmetic statements

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 03 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862188):
http://www.ams.org/notices/200604/fea-davis.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 03 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862251):
This seems to give arguments which prove that p exists without explicitly writing it down, and perhaps it's possible to explicitly write it down but when you've finished it will be pretty horrible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862424):
There are already lean predicates which will suffice to state this result with an exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862584):
specifically, `evaln k e 0` in the `computability` lib will evaluate a partial recursive function `e` for `k` steps, so there is some `e` for which `\lam n, (evaln n e 0).is_none` satisfies the conditions (using a partial recursive function that searches for a contradiction in lean)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 03 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862738):
My impression is that this e will be huge though. My impression is that Friedman is actually writing down some precise statements about graphs which are explicit examples of p if independence in ZFC is what you're looking for. See for example the last result in the linked paper. He's quantifying over three variables not one but you just choose a computable bijection between N^3 and N to fix this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862758):
sure, the encoding isn't optimized for size

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862820):
it's about as complicated as it is to describe a proof system like lean or ZFC+inaccessibles or anything of higher consistency strength

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 03 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862821):
Of course all this assumes lean/ZFC/whatever we're talking about is consistent. I guess you'll have to wait for some Tarski version of Friedman to come along before you can see an explicit and comprehensible p for Lean...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862835):
I think some of Friedman's work has the consistency strength of some weakly Mahlo cardinals which is more than enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 03 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862913):
Oh so maybe there's hope with some weird statement about finite graphs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862978):
I was somewhat disillusioned with Friedman's claims of "simplicity" when it turned out (in Scott Aaronson's project https://www.scottaaronson.com/blog/?p=2725 to build a TM whose halting is independent of ZFC) that it's cheaper to just build a tiny metamath verifier than to define some of Friedman's combinatorial objects

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130863138):
If you are only going for "explicit and comprehensible", not size from scratch, it's not so bad at all. It is certainly easier than defining schemes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 03 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130863454):
> this e will be huge though

It occurs to me that I don't know what you mean by "huge" here. This number is huge the same way Graham's number is huge: it is numerically very large, but its description is relatively compact. Since you usually aren't working from scratch in lean anyway, but are building up a language as you go, it's perfectly reasonable to get "explicit and comprehensible" by judicious use of sensibly named definitions while still producing a numerically huge result. But I don't see why this should matter to a mathematician

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 03 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130863916):
I just mean "irritating to write down explicitly" :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 04 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130865143):
@**Chris Hughes** so the basic trick is to make `p n` equal to a statement something like "if you write n in base 256 and then interpret the resulting list of numbers as a text file, then this text file is not a proof of X in Lean" where X is carefully chosen. But then you have to build a lean parser etc all within p, and also to get exactly what you ask you need to do some other trickery with computable functions too to actually get this trick to work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 04 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130865344):
yikes, that's an extreme solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 04 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130865398):
I was thinking more along the lines of formalizing a syntax for a dependent type theory like lean, not the real lean language which has lots of irrelevant garbage. It would look a lot like formalizing that paper of mine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 04 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130865404):
Except easier because there are much simpler languages with the same consistency strength

