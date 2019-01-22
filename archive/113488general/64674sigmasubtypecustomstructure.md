---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64674sigmasubtypecustomstructure.html
---

## [general](index.html)
### [sigma, subtype, custom structure](64674sigmasubtypecustomstructure.html)

#### [Sean Leather (Sep 06 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sigma%2C%20subtype%2C%20custom%20structure/near/133436036):
On [#316](https://github.com/leanprover/mathlib/pull/316), there are the following comments:

@**Scott Morrison**:
> The first is that this may encourage us to overuse `sigma` types and `subtype`s at the expense of bespoke structures.

@**Reid Barton**:
> But somehow a bare `sigma` feels so low-level. Would it make any sense to replace it with a generic bundled structure? I guess it's basically the same thing...

I bring this up here because it is off-topic for that particular issue but is still an issue that I've wondered about myself.

In my [finmap](https://github.com/spl/lean-finmap) work, I've been using `sigma` as a singleton mapping between a key and value used in association lists and `finmap` itself. This is partly because it's already done in `hash_map` and partly because it's just the right type for the job. As far as the library goes, it works perfectly.

But in usage, it means that whatever I insert, I must use `sigma` instead of a custom `structure`. I then end up defining a type that is defeq `sigma`. I'd rather use a custom `structure` that then provides the appropriate interface used by the library. But I'm not sure if this is desirable or how best to do it. I can think of possibly using a type class or an equivalence.

