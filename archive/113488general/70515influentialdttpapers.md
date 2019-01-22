---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70515influentialdttpapers.html
---

## [general](index.html)
### [influential dtt papers](70515influentialdttpapers.html)

#### [Andrew Ashworth (Mar 01 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123120262):
is there a list out there of really important papers in dtt? i recently read "Elimination with a Motive" that was linked in this chat and finally understood how `cases` works

#### [Mario Carneiro (Mar 01 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121079):
link?

#### [Mario Carneiro (Mar 01 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121130):
I'm still in the paper gathering stage, so I don't think I can help you that much, although I have been able to find good papers (maybe influential, maybe not) on specific topics

#### [Andrew Ashworth (Mar 01 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121198):
[Elimination With a Motive](https://pdfs.semanticscholar.org/d224/e96c59a81a471625faf87118b6299094e1e4.pdf)

#### [Mario Carneiro (Mar 01 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121265):
Conor McBride is generally known for writing a number of DTT papers, so you could look there

#### [Andrew Ashworth (Mar 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121307):
yeah, he seems to have a lot of proof pearls

#### [Andrew Ashworth (Mar 01 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121321):
i like how even in the abstract he says : "I adopt a technique standard in `folklore', generalizing the ~x and expressing the restriction by equation...". Where do I learn this fabled folklore?!

#### [Andrew Ashworth (Mar 01 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121364):
maybe by reading all his papers :|

#### [Mario Carneiro (Mar 01 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121920):
Of course, that's code for "not written down yet", and is the bane of new researchers :)

#### [Simon Hudon (Mar 01 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121930):
That's the fun of literature review. What a fun summer that was ... *reaches for bottle of whiskey*

#### [Simon Hudon (Mar 01 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123121980):
If that's helpful, I treat gathering a literature review like browsing wikipedia. There's a section at the end with their references and you just download all the papers with the interesting titles, read their intro and conclusion and start over with their reference section

#### [Andrew Ashworth (Mar 01 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123122397):
that paper also explains where "no confusion" comes from

#### [Andrew Ashworth (Mar 01 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123122438):
when I read about `no_confusion` in TPIL i was anything but not confused

#### [Simon Hudon (Mar 01 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123122446):
```quote
when I read about `no_confusion` in TPIL i was anything but not confused
```
But it's supposed to be precluded by `no_confusion`!!!

#### [Kevin Buzzard (Mar 01 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/influential%20dtt%20papers/near/123127085):
```quote
when I read about `no_confusion` in TPIL i was anything but not confused
```
I was just the same. I'd never heard of the concept before and IIRC it's dropped in without any explanation right in the middle of the preliminary discussion on type classes when, rather than talking about things like Haskell type classes (which I kind of understood) they start going on about making a canonical nat and then randomly dropping a proof that 1 isn't 2 using no_confusion. That was a part of TPIL that I had to read again and again before it made sense. I flagged this up to Jeremy who I think might have done some rearranging as a consequence...

