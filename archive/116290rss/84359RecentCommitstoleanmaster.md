---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116290rss/84359RecentCommitstoleanmaster.html
---

## [rss](index.html)
### [Recent Commits to lean:master](84359RecentCommitstoleanmaster.html)

#### [rss-bot (Mar 30 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124418914):
**[fix(library/init/core): closes #1951](https://github.com/leanprover/lean/commit/d387103aa2bebfc98220733d9607a16663ec1ef2)**
fix(library/init/core): closes #1951

- Add has_pow type class
- Make `^` notation right associative
https://github.com/leanprover/lean/commit/d387103aa2bebfc98220733d9607a16663ec1ef2

#### [rss-bot (Mar 30 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124418915):
**[test(tests/lean/1952b): another test for issue #1952](https://github.com/leanprover/lean/commit/6e0bf8473b1980e6692a61a924b4c6eae195619d)**
test(tests/lean/1952b): another test for issue #1952

This is an example used in one of the comments.
https://github.com/leanprover/lean/commit/6e0bf8473b1980e6692a61a924b4c6eae195619d

#### [rss-bot (Mar 30 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124418916):
**[fix(library/type_context): elim_delayed_abstraction must check whethe…](https://github.com/leanprover/lean/commit/66e7873c2254f8184528e619e65bbba8f450234b)**
fix(library/type_context): elim_delayed_abstraction must check whether metavariable is already assigned

fixes #1952
https://github.com/leanprover/lean/commit/66e7873c2254f8184528e619e65bbba8f450234b

#### [rss-bot (Apr 02 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124537305):
**[chore(library/util): don't hide commit hash for nightlies](https://github.com/leanprover/lean/commit/17affbd45d732c4b21bb5b7c187024bd4bbb41a6)**
chore(library/util): dont hide commit hash for nightlies
https://github.com/leanprover/lean/commit/17affbd45d732c4b21bb5b7c187024bd4bbb41a6

#### [rss-bot (Apr 02 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124546854):
**[fix(util/numeric/mpbq): remove unimplemented move constructor](https://github.com/leanprover/lean/commit/96c932ab210ac4e71ad3439d128fb4f75b314e1e)**
fix(util/numeric/mpbq): remove unimplemented move constructor

Apparently g++ started preferring it over the copy constructor in more places
https://github.com/leanprover/lean/commit/96c932ab210ac4e71ad3439d128fb4f75b314e1e

#### [rss-bot (Apr 06 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124721321):
**[fix(init/core): remove out_param from has_pow](https://github.com/leanprover/lean/commit/8f55ec4c50379c612731ced2424fd3eda0cf69a6)**
fix(init/core): remove out_param from has_pow

With the current elaboration scheme, out_params and coercions do not mix well,
as evidenced by the following example by @digama:

```
variables {α : Type*} [group α]
def gpow : α → ℤ → α := sorry
instance group.has_pow : has_pow α ℤ := ⟨gpow⟩

example (a : α) : a ^ 0 = 1 := sorry -- failed to synth ⊢ has_pow α ℕ
example (a : α) : a ^ (0:ℕ) = 1 := sorry -- ok, coerces
example (a : α) : a ^ (0:ℤ) = 1 := sorry -- ok
```

The issue is that
* we first try to solve `has_pow ?α ?β`, which is postponed
* then infer `?α = nat` from `a`
* then at some point call `elaborator::synthesize()` and default `β` to `nat`
* then try to solve `has_pow nat nat`, which fails at `int =?= nat`
https://github.com/leanprover/lean/commit/8f55ec4c50379c612731ced2424fd3eda0cf69a6

#### [rss-bot (Apr 06 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124721322):
**[chore(tests/lean/struct_class): make test less prone to breakage](https://github.com/leanprover/lean/commit/3d692c53b5286e80436b7fbc6193d4cc759dfd49)**
chore(tests/lean/struct_class): make test less prone to breakage
https://github.com/leanprover/lean/commit/3d692c53b5286e80436b7fbc6193d4cc759dfd49

#### [rss-bot (Apr 10 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124862310):
**[chore(library/delayed_abstraction): add missing 'virtual'](https://github.com/leanprover/lean/commit/d36b859c6579ce1b86f257a494bb99417c7cdac1)**
chore(library/delayed_abstraction): add missing virtual
https://github.com/leanprover/lean/commit/d36b859c6579ce1b86f257a494bb99417c7cdac1

#### [rss-bot (Apr 10 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124862311):
**[refactor(library/typed_expr): move typed_expr to frontends/lean](https://github.com/leanprover/lean/commit/c08a3bc55704611acc655c5f7a38b761b07132c4)**
refactor(library/typed_expr): move typed_expr to frontends/lean
https://github.com/leanprover/lean/commit/c08a3bc55704611acc655c5f7a38b761b07132c4

#### [rss-bot (Apr 10 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124862312):
**[refactor(library/typed_expr): do not use macros for implementing type…](https://github.com/leanprover/lean/commit/bcaa0b2ad3c1e081ab1a63c0130e8773d6b23bef)**
refactor(library/typed_expr): do not use macros for implementing typed_expr

Remark: in Lean4, we will not have macro_defs.
https://github.com/leanprover/lean/commit/bcaa0b2ad3c1e081ab1a63c0130e8773d6b23bef

#### [rss-bot (Apr 10 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124862313):
**[chore(*): rename expr_struct_* to expr_*](https://github.com/leanprover/lean/commit/8dd53cd94f6eb5ee03d539cbb92020fdf3778654)**
chore(*): rename expr_struct_* to expr_*

We dont need to modifier `_struct` anymore since we dont use the
pointer equality based hashtables anymore.
https://github.com/leanprover/lean/commit/8dd53cd94f6eb5ee03d539cbb92020fdf3778654

#### [rss-bot (Apr 10 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124862314):
**[chore(kernel): remove m_hash_alloc field from expressions](https://github.com/leanprover/lean/commit/faf8e025e7e076827f9c4311ec6cf199329f9897)**
chore(kernel): remove m_hash_alloc field from expressions

This field was originally added to create hashtables based on pointer
equality. We dont use them anymore, and the caches based on
m_hash_alloc can be implemented using m_hash without any performance
impact. This commit also fixes two places where `expr_set` was used
instead of `expr_struct_set`.

This commit is also important for the Lean4 plans where `expr` will
be implemented in Lean, and fields like `m_hash_alloc` would require us
to track state.
https://github.com/leanprover/lean/commit/faf8e025e7e076827f9c4311ec6cf199329f9897

#### [rss-bot (Apr 12 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124957144):
**[test(tests/lean/1956): test for #1956](https://github.com/leanprover/lean/commit/f863667e1feec22b49b51d925ec01aab4fbe60f9)**
test(tests/lean/1956): test for #1956
https://github.com/leanprover/lean/commit/f863667e1feec22b49b51d925ec01aab4fbe60f9

#### [rss-bot (Apr 12 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124957145):
**[fix(frontends/lean/definition_cmds): fixes #1956](https://github.com/leanprover/lean/commit/e201ee2ae05b441c24c509b0418f349501d89b9e)**
fix(frontends/lean/definition_cmds): fixes #1956
https://github.com/leanprover/lean/commit/e201ee2ae05b441c24c509b0418f349501d89b9e

#### [rss-bot (Apr 12 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/124986444):
**[fix(init/core): typed_expr should accept Props](https://github.com/leanprover/lean/commit/92499bad5f845ab8fbd455bf549fec47c5bad3bc)**
fix(init/core): typed_expr should accept Props

Fixes #1954
https://github.com/leanprover/lean/commit/92499bad5f845ab8fbd455bf549fec47c5bad3bc

#### [rss-bot (Apr 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125036930):
**[chore(.travis.yml): trigger AppVeyor nightly build from Travis](https://github.com/leanprover/lean/commit/ee6f32368752e4100dc6e8622b08586f8ff14f52)**
chore(.travis.yml): trigger AppVeyor nightly build from Travis
https://github.com/leanprover/lean/commit/ee6f32368752e4100dc6e8622b08586f8ff14f52

#### [rss-bot (Apr 14 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125084175):
**[fix(.appveyor.yml): nightly build](https://github.com/leanprover/lean/commit/d97d77fd30601f06c751ca376c0cdddd59cf52f9)**
fix(.appveyor.yml): nightly build
https://github.com/leanprover/lean/commit/d97d77fd30601f06c751ca376c0cdddd59cf52f9

#### [rss-bot (Apr 16 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125160362):
**[chore(tests/lean/run/simp_norm): fix test](https://github.com/leanprover/lean/commit/169f7f2764d11cadacc17b7a0c983c4237a9bec0)**
chore(tests/lean/run/simp_norm): fix test
https://github.com/leanprover/lean/commit/169f7f2764d11cadacc17b7a0c983c4237a9bec0

#### [rss-bot (Apr 16 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125160363):
**[test(tests/lean/run/parse_match_issue): test for previous commit](https://github.com/leanprover/lean/commit/00e1dcced42c976862141780df211a726e8194a1)**
test(tests/lean/run/parse_match_issue): test for previous commit

The new test is the repro for the issue fixed in the previous commit.
https://github.com/leanprover/lean/commit/00e1dcced42c976862141780df211a726e8194a1

#### [rss-bot (Apr 16 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125160364):
**[fix(library/type_context): improve `is_def_eq_args`](https://github.com/leanprover/lean/commit/48492743afe4342b3639b4dcdaca3242c3503845)**
fix(library/type_context): improve `is_def_eq_args`
https://github.com/leanprover/lean/commit/48492743afe4342b3639b4dcdaca3242c3503845

#### [rss-bot (Apr 16 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125162798):
**[fix(library/noncomputable): bug at is_noncomputable](https://github.com/leanprover/lean/commit/0b5f1f36a9bb65e3bd60abb7be179a7a6e1e7761)**
fix(library/noncomputable): bug at is_noncomputable

In Lean4, the check should be based on the compiler.
That is, a definition should be marked as noncomputable when we cannot
generate code for it.
https://github.com/leanprover/lean/commit/0b5f1f36a9bb65e3bd60abb7be179a7a6e1e7761

#### [rss-bot (Apr 16 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125166415):
**[fix(library/type_context): unifier failed to solve `?m =?= fun x_1 ..…](https://github.com/leanprover/lean/commit/e6764047a14ce4383d29b2858fa9e2e246d4f13b)**
fix(library/type_context): unifier failed to solve `?m =?= fun x_1 ... x_n, ?m x_1 ... x_n`

Before this commit, the unifier would try to solve the unification consraint

     ?m =?= fun x_1 ... x_n, ?m x_1 ... x_n

by assigning

     ?m := fun x_1 ... x_n, ?m x_1 ... x_n

which fails the occurs check.

This commit skips the assignment by using eta-reduction.
https://github.com/leanprover/lean/commit/e6764047a14ce4383d29b2858fa9e2e246d4f13b

#### [rss-bot (Apr 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125167931):
**[chore(.appveyor.yml): fix non-nightly builds](https://github.com/leanprover/lean/commit/d4157186b227a68654ec6f771919d507bce882b9)**
chore(.appveyor.yml): fix non-nightly builds
https://github.com/leanprover/lean/commit/d4157186b227a68654ec6f771919d507bce882b9

#### [rss-bot (Apr 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125170419):
**[chore(*): release version 3.4.0](https://github.com/leanprover/lean/commit/4be96eaaaf71273e6dcf0edbba3e29338d3aef1d)**
chore(*): release version 3.4.0
https://github.com/leanprover/lean/commit/4be96eaaaf71273e6dcf0edbba3e29338d3aef1d

#### [rss-bot (Apr 17 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125174792):
**[chore(*): add note saying 3.4.0 is the last release for the 3.x family](https://github.com/leanprover/lean/commit/dd6e91fa1aa34a14f31c086c8d7876a82d2a212b)**
chore(*): add note saying 3.4.0 is the last release for the 3.x family
https://github.com/leanprover/lean/commit/dd6e91fa1aa34a14f31c086c8d7876a82d2a212b

#### [rss-bot (Apr 20 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125451076):
**[fix(*): revert broken `typed_expr` refactorings](https://github.com/leanprover/lean/commit/f59c2f0ef59fdc1833b6ead6adca721123bd7932)**
fix(*): revert broken `typed_expr` refactorings

The refactoring will instead be part of Lean 4
https://github.com/leanprover/lean/commit/f59c2f0ef59fdc1833b6ead6adca721123bd7932

#### [Sebastian Ullrich (Apr 20 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125451078):
@**Mario Carneiro**

#### [rss-bot (Apr 29 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125832989):
**[chore(*): release version 3.4.1](https://github.com/leanprover/lean/commit/17fe3decaf8ae236f0d0ff51ac8fd7f6940acdee)**
chore(*): release version 3.4.1
https://github.com/leanprover/lean/commit/17fe3decaf8ae236f0d0ff51ac8fd7f6940acdee

#### [Kevin Buzzard (Apr 29 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125836870):
Here's hopin'

#### [rss-bot (May 01 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/125920186):
**[chore(README): update README](https://github.com/leanprover/lean/commit/e181232c8ffd2bc2ba1b2f9799f8ac0ea0e4e505)**
chore(README): update README
https://github.com/leanprover/lean/commit/e181232c8ffd2bc2ba1b2f9799f8ac0ea0e4e505

#### [rss-bot (May 18 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/126739907):
**[chore(src/CMakeLists): prepare for next release](https://github.com/leanprover/lean/commit/a4aae537fe771ee92d746d4a2be1e73c543e48b9)**
chore(src/CMakeLists): prepare for next release

(not that were currently planning for one in the 3.x series)
https://github.com/leanprover/lean/commit/a4aae537fe771ee92d746d4a2be1e73c543e48b9

#### [rss-bot (Jun 21 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/128426487):
**[fix(library/init/data/list/basic): list.lt](https://github.com/leanprover/lean/commit/ceacfa7445953cbc8860ddabc55407430a9ca5c3)**
fix(library/init/data/list/basic): list.lt
https://github.com/leanprover/lean/commit/ceacfa7445953cbc8860ddabc55407430a9ca5c3

#### [rss-bot (Aug 22 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/132603199):
**[fix(library/compiler/cse): deactivate CSE for constructor applications](https://github.com/leanprover/lean/commit/b13ac127fd83f3724d2f096b1fb85dc6b15e3746)**
fix(library/compiler/cse): deactivate CSE for constructor applications

Fixes 1968
https://github.com/leanprover/lean/commit/b13ac127fd83f3724d2f096b1fb85dc6b15e3746

#### [rss-bot (Oct 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/136621939):
**[fix(bin/leanpkg): handle spaces in paths on POSIX systems](https://github.com/leanprover/lean/commit/687745d887ebd89da94ba36d853eff12746af136)**
fix(bin/leanpkg): handle spaces in paths on POSIX systems
https://github.com/leanprover/lean/commit/687745d887ebd89da94ba36d853eff12746af136

#### [rss-bot (Oct 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/136621940):
**[fix(lean/bin/leanpkg.bat): handle spaces in paths](https://github.com/leanprover/lean/commit/428cf7278cbb490dfefabd554d5d49996ab9a4a0)**
fix(lean/bin/leanpkg.bat): handle spaces in paths

Fixes #1973. Ive tested it locally and this appears to be enough to solve the problem.
https://github.com/leanprover/lean/commit/428cf7278cbb490dfefabd554d5d49996ab9a4a0

#### [rss-bot (Oct 27 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/136621941):
**[fix(frontends/dependencies): ignore `.olean` files when listing depen…](https://github.com/leanprover/lean/commit/254c5e9a4e3f31dc8d3c30a3f21b4ea6ee90e7e0)**
fix(frontends/dependencies): ignore `.olean` files when listing dependencies
https://github.com/leanprover/lean/commit/254c5e9a4e3f31dc8d3c30a3f21b4ea6ee90e7e0

#### [rss-bot (Nov 12 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/147510147):
**[feat(leanpkg): add git branch tracking for dependencies](https://github.com/leanprover/lean/commit/1229f9b2d7f0a1eff10bb33f1cab220f4f6f06ab)**
feat(leanpkg): add git branch tracking for dependencies
https://github.com/leanprover/lean/commit/1229f9b2d7f0a1eff10bb33f1cab220f4f6f06ab

#### [rss-bot (Dec 09 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/151237693):
**[feat(library/system/io): encode/decode UTF-8 for text-mode streams](https://github.com/leanprover/lean/commit/4e16bc7192f9f32b03222142e659fa3dae4b8025)**
feat(library/system/io): encode/decode UTF-8 for text-mode streams

Co-authored-by: Sebastian Ullrich sebasti@nullri.ch
https://github.com/leanprover/lean/commit/4e16bc7192f9f32b03222142e659fa3dae4b8025

#### [rss-bot (Dec 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/151482002):
**[fix(library/process): fix Windows build](https://github.com/leanprover/lean/commit/30d883efef422facab3bf351d9fcff90c943298f)**
fix(library/process): fix Windows build
https://github.com/leanprover/lean/commit/30d883efef422facab3bf351d9fcff90c943298f

#### [rss-bot (Jan 06 2019 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/154520946):
**[fix(library/process): really fix Windows build](https://github.com/leanprover/lean/commit/69111751859b0b260932e6fe8dda1b4f4ab14217)**
fix(library/process): really fix Windows build
https://github.com/leanprover/lean/commit/69111751859b0b260932e6fe8dda1b4f4ab14217

#### [rss-bot (Jan 06 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/154532357):
**[chore(library/init/meta/coinductive_predicates): remove](https://github.com/leanprover/lean/commit/e79cb3f2c4987dcfbec8e3e15eb83837cabe1058)**
chore(library/init/meta/coinductive_predicates): remove

The command has outstanding bugs and should be better off in mathlib
https://github.com/leanprover/lean/commit/e79cb3f2c4987dcfbec8e3e15eb83837cabe1058

#### [rss-bot (Jan 11 2019 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/154931437):
**[fix(library/module_mgr): ignore '\r' changes](https://github.com/leanprover/lean/commit/92826917a252a6092cffaf5fc5f1acb1f8cef379)**
fix(library/module_mgr): ignore \r changes
https://github.com/leanprover/lean/commit/92826917a252a6092cffaf5fc5f1acb1f8cef379

#### [rss-bot (Jan 11 2019 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/154931438):
**[chore(.travis.yml): gpg key for new rvm maintainer](https://github.com/leanprover/lean/commit/be4b7822efd4ef0e1e716b0c664565d12eb8152f)**
chore(.travis.yml): gpg key for new rvm maintainer

[OS X builds are currently failing on Travis](https://travis-ci.org/leanprover/lean/jobs/477775262#L1091), the underlying issue seems to be that [rvm has a new maintainer with a new gpg key](https://github.com/rvm/rvm/issues/4520).
https://github.com/leanprover/lean/commit/be4b7822efd4ef0e1e716b0c664565d12eb8152f

#### [rss-bot (Jan 12 2019 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/154988338):
**[refactor(library/init/meta/transfer): remove transfer and relators](https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb)**
refactor(library/init/meta/transfer): remove transfer and relators
https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb

#### [rss-bot (Jan 18 2019 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/156371310):
**[chore(*): release version 3.4.2](https://github.com/leanprover/lean/commit/cbd2b6686ddb566028f5830490fe55c0b3a9a4cb)**
chore(*): release version 3.4.2
https://github.com/leanprover/lean/commit/cbd2b6686ddb566028f5830490fe55c0b3a9a4cb

#### [rss-bot (Jan 18 2019 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116290-rss/topic/Recent Commits to lean:master/near/156371312):
**[doc(doc/changes): 3.4.2 changelog](https://github.com/leanprover/lean/commit/f3f98ea71f298a52fbf75be3c5feccfe444ff54b)**
doc(doc/changes): 3.4.2 changelog
https://github.com/leanprover/lean/commit/f3f98ea71f298a52fbf75be3c5feccfe444ff54b

