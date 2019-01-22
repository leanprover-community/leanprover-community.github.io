---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116290rss/57455RecentCommitstoleanlean4.html
---

## [rss](index.html)
### [Recent Commits to lean:lean4](57455RecentCommitstoleanlean4.html)

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037471):
**[chore(.travis.yml): trigger AppVeyor nightly build from Travis](https://github.com/leanprover/lean/commit/39cf4b6a54ca3bfb89ba4817001f26dcf0bbca60)**
chore(.travis.yml): trigger AppVeyor nightly build from Travis
https://github.com/leanprover/lean/commit/39cf4b6a54ca3bfb89ba4817001f26dcf0bbca60

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037472):
**[test(tests/lean/run/deriv): add benchmark](https://github.com/leanprover/lean/commit/d57c2df9c1681b3713d591b12da3162952c0bebd)**
test(tests/lean/run/deriv): add benchmark
https://github.com/leanprover/lean/commit/d57c2df9c1681b3713d591b12da3162952c0bebd

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037473):
**[chore(kernel/type_checker): remove dead code](https://github.com/leanprover/lean/commit/a241bd332851aa6e8f8ecda4331d6ce5c2f2bdf3)**
chore(kernel/type_checker): remove dead code
https://github.com/leanprover/lean/commit/a241bd332851aa6e8f8ecda4331d6ce5c2f2bdf3

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037474):
**[chore(library/parray): style](https://github.com/leanprover/lean/commit/5b530f24aa2f33234dcb74736537fe89f8b50ed9)**
chore(library/parray): style
https://github.com/leanprover/lean/commit/5b530f24aa2f33234dcb74736537fe89f8b50ed9

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037475):
**[fix(library/parray): bug introduced when memory_pool was removed](https://github.com/leanprover/lean/commit/3d9c0ab27736f77804d13b870dbfff8b0c2305e0)**
fix(library/parray): bug introduced when memory_pool was removed
https://github.com/leanprover/lean/commit/3d9c0ab27736f77804d13b870dbfff8b0c2305e0

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037476):
**[chore(library): cleanup constants.txt](https://github.com/leanprover/lean/commit/1e1161138894d1440cd5abbda3b6d722956c765a)**
chore(library): cleanup constants.txt
https://github.com/leanprover/lean/commit/1e1161138894d1440cd5abbda3b6d722956c765a

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037477):
**[chore(library/app_builder): remove dead code](https://github.com/leanprover/lean/commit/8b8c2ddf374f316bacbc910c3dd6358cc9add7d9)**
chore(library/app_builder): remove dead code
https://github.com/leanprover/lean/commit/8b8c2ddf374f316bacbc910c3dd6358cc9add7d9

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037478):
**[chore(library/tactic/algebraic_normalizer): remove dead code](https://github.com/leanprover/lean/commit/a41ad717ed33e38ab729b1abb6693fcf5e570990)**
chore(library/tactic/algebraic_normalizer): remove dead code

This is going to be implemented in Lean.
https://github.com/leanprover/lean/commit/a41ad717ed33e38ab729b1abb6693fcf5e570990

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037479):
**[refactor(util): move mpz/mpq to util](https://github.com/leanprover/lean/commit/4b6583ae9f6e15f47fb324d7ceffd6fc9ef80e87)**
refactor(util): move mpz/mpq to util

The new lean_obj objects will be defined at util.
Reason: we will define `name`, `options`, `format`, ... on top of lean_obj.
lean_obj depends on mpz.
Remark: lean_obj will replace vm_obj.
https://github.com/leanprover/lean/commit/4b6583ae9f6e15f47fb324d7ceffd6fc9ef80e87

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037480):
**[chore(numerics): remove numeric_traits](https://github.com/leanprover/lean/commit/74f10fdf5c95bf88819007892c2f1774d36bc579)**
chore(numerics): remove numeric_traits

numeric_traits is dead code. It was used to implement a simplex that was
parametric on the number type. This code has been moved to Z3.
So, we dont need it anymore.
https://github.com/leanprover/lean/commit/74f10fdf5c95bf88819007892c2f1774d36bc579

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037481):
**[chore(library/shared_environment): remove dead file](https://github.com/leanprover/lean/commit/3e4594d6be9821df0495203bf05cbf66eaaa6cf8)**
chore(library/shared_environment): remove dead file
https://github.com/leanprover/lean/commit/3e4594d6be9821df0495203bf05cbf66eaaa6cf8

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037482):
**[chore(library/ac_match): remove dead file](https://github.com/leanprover/lean/commit/aa39591be53eaf91f92ebd1f16aeb43bce0d140b)**
chore(library/ac_match): remove dead file
https://github.com/leanprover/lean/commit/aa39591be53eaf91f92ebd1f16aeb43bce0d140b

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037483):
**[chore(util/sequence): remove dead code](https://github.com/leanprover/lean/commit/d1cdae9d904153fd297f2b30ec2b1a5541dafddc)**
chore(util/sequence): remove dead code
https://github.com/leanprover/lean/commit/d1cdae9d904153fd297f2b30ec2b1a5541dafddc

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037484):
**[chore(kernel): remove opportunistic hash consing support](https://github.com/leanprover/lean/commit/efb9fb0802c3ae22d0e6f7b11b51db261237f41f)**
chore(kernel): remove opportunistic hash consing support

It just adds extra complexity and is in conflict for our plans for
Lean4. Moreover, in our experiments it impacts negatively on
performance: master and lean4 branches. The negative impact has been
confirmed by @kha too.
https://github.com/leanprover/lean/commit/efb9fb0802c3ae22d0e6f7b11b51db261237f41f

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037485):
**[chore(util): remove memory_pool](https://github.com/leanprover/lean/commit/39ef7aeee2f9e1ed7442bbfc2a349f6dddd07861)**
chore(util): remove memory_pool

memory_pool object introduces memory contention and unnecessary
complexity. Moreover, it actually reduces performance when we compile
Lean using JEMALLOC.

Here are the numbers for corelib

jemalloc with memory_pool:    13.83 secs
jemalloc without memory_pool: 13.60 secs
https://github.com/leanprover/lean/commit/39ef7aeee2f9e1ed7442bbfc2a349f6dddd07861

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037486):
**[chore(util): remove dead code](https://github.com/leanprover/lean/commit/1dd71656947b9606008aea9d9dbf3e2449fc0c81)**
chore(util): remove dead code
https://github.com/leanprover/lean/commit/1dd71656947b9606008aea9d9dbf3e2449fc0c81

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037487):
**[chore(util,library): remove small_object_allocator](https://github.com/leanprover/lean/commit/db4b00c7d80e4fa7d5cffd7b0d5ac5727de2a428)**
chore(util,library): remove small_object_allocator

We use small_object_allocator to allocate vm_objs.
However small_object_allocator is not thread safe. So, we need to copy
vm_objs between threads. Moreover, in our experiments, we observed that
JEMALLOC is actually faster than the small_object_allocator.

Here are numbers for the reduced corelib.

small_object_allocator:  15.62 secs
gcc 4.9 allocator:       16.19 secs
jemalloc:                13.83 secs
https://github.com/leanprover/lean/commit/db4b00c7d80e4fa7d5cffd7b0d5ac5727de2a428

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037488):
**[chore(util/lru_cache): remove dead code](https://github.com/leanprover/lean/commit/4c14668bf05d5fa063f9dac0411604d8d43ce033)**
chore(util/lru_cache): remove dead code
https://github.com/leanprover/lean/commit/4c14668bf05d5fa063f9dac0411604d8d43ce033

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037489):
**[chore(library): remove arith_instance](https://github.com/leanprover/lean/commit/1465b58369614dc261969437ee49580943784491)**
chore(library): remove arith_instance

It was used by norm_num. We dont need it anymore.
https://github.com/leanprover/lean/commit/1465b58369614dc261969437ee49580943784491

#### [rss-bot (Apr 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent%20Commits%20to%20lean%3Alean4/near/125037490):
**[chore(util/numerics): remove more leftovers from Lean1](https://github.com/leanprover/lean/commit/e3c1f6c7da4cbe18a8c3d1dfea8c4887d33d2640)**
chore(util/numerics): remove more leftovers from Lean1
https://github.com/leanprover/lean/commit/e3c1f6c7da4cbe18a8c3d1dfea8c4887d33d2640

