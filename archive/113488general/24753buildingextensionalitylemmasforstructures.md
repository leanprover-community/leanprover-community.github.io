---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24753buildingextensionalitylemmasforstructures.html
---

## Stream: [general](index.html)
### Topic: [building @[extensionality] lemmas for structures](24753buildingextensionalitylemmasforstructures.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 13 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132045472):
Hi @**Simon Hudon**, I'm wondering if you've thought recently about building `@[extensionality]` lemmas for structures automatically. I know we had some discussion about this a long time ago (gitter?), and some attempts at a `congr_struct` tactic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132046891):
Hi Scott! No, I haven't thought of it but I think it shouldn't be hard. We could invoke it with `@[make_extentionality]` to distinguish from the lemma itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132046948):
shouldn't that obviously be a derive handler?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 13 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132046968):
From memory the problems quickly arose when there were dependent fields. First there's the question of whether to use rewrites or heqs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047029):
But I think correctly building the statements for later fields, in either approach, seemed hardish.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047037):
can't you just use `congr` to generate the lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047051):
At the time I knew almost nothing about writing tactics, and haven't thought much about it since, however. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047080):
However, I don't usually find that extensionality lemmas are automatable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047104):
since they are often mathematically nontrivial, e.g. `units A` only depends on the first component

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047105):
@**Mario Carneiro** I also thought about making it a derive handler but I think it has to be a type class for that, no?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047165):
I thought the thing after `derive` was just a label

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047194):
You mean ... make a metavariable of type `a = b`, actually run the `cases a, cases b, congr` tactic, then inspect the goals, take those as arguments for your declaration, and have the proof by `cases a, cases b, congr ; assumption`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047240):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047277):
or more directly, just generate the `congr_lemma` and inspect its type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 13 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047460):
I see. We'd need a cleanup phase that decides when fields are propositional and omits those `heq`s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047519):
no, that's why I am suggesting you use the `congr_lemma`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047521):
it does that already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047629):
Looking at the code for `derive_attr`, I think you're right Mario and it is of course a much better way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047635):
oh, okay: why doesn't `congr` do that then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047661):
Doesn't it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 13 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047751):
I just tried on `category_theory.functor`, and got goals for the propositional fields.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132047967):
I'm surprised. You can clean them up I think using `match_eq` / `match_heq` and then using `is_proof` on the results.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 13 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132048418):
@**Mario Carneiro** The annoying thing with `derive` is that it parses a `pexpr` and does some basic name resolution. We may get around it by defining a dummy like `def extensionality := ()`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 14 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132126240):
@**Scott Morrison** Any luck in building it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 15 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/building%20%40%5Bextensionality%5D%20lemmas%20for%20structures/near/132141380):
Sorry, haven't got back to it. Writing `ext` lemmas by hand is annoying but not critical. :-)

