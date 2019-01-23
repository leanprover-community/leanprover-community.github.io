---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53317NewversionsofPresburgertactics.html
---

## Stream: [general](index.html)
### Topic: [New versions of Presburger tactics](53317NewversionsofPresburgertactics.html)

---


{% raw %}
#### [ Seul Baek (Oct 30 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136761498):
This project has been neglected for a long time, so I decided to tidy it up a bit. The new versions are available at https://github.com/skbaek/qe/. The main changes are :

1. Now there are tactics for `nat`, although they are slower than `int` equivalents due to quantifiers added during translation
2. There are versions that use `znum` instead of `int` in the shadow syntax for optimization
3. Makes more use of typeclasses
4.  Also includes a tactic for DLO without endpoints for `rat`
5. The `leanpkg.toml` file is fixed, so you can install it using `leanpkg`

The main tactics are in the `main.lean` files of each directory. You can see the `tests.lean` files for examples of how they are used. As you might expect, `znum` is more efficient when handling large numbers, so there are examples which time out for `int`-based tactics but works with `znum`.

3 and 4 were done just to show that the shared-framework approach is viable. The idea (from [Tobias Nipkow](http://www21.in.tum.de/~nipkow/pubs/jar10.pdf)) is that QE-based FoL decision procedures mostly follow the same scheme, so the common part should be factored out using some module or typeclass system. Once this work is done, it is easy to cook up more decision procedures, since all you need to do is define (and prove soundness for) a single quantifier elimination step.

#### [ Patrick Massot (Oct 30 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136763199):
Thanks! Could you include a glossary of what all those acronyms mean? Maybe in a README.md?

#### [ Patrick Massot (Oct 30 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136763375):
What are all those commented out lines in the test files? Things that should work but don't?

#### [ Patrick Massot (Oct 30 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136763429):
For the purpose of using tests as documentation, it would probably be more efficient to move those test files somewhere more visible

#### [ Seul Baek (Oct 30 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136764118):
```quote
Thanks! Could you include a glossary of what all those acronyms mean? Maybe in a README.md?
```
Yes, I should either do that, or actually give intelligible names to definitions, which I was too lazy to type out when doing the proofs.

#### [ Seul Baek (Oct 30 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136764373):
The commented out lines are either theorems which currently time out, or nontheorems which would be useful for testing the soundness of unverified vm-versions of the tactics (which currently don't exist, but are easy to implement if necessary).

#### [ Seul Baek (Oct 30 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136764898):
Do you mean that it would be useful to add some introductory information about the tactics for users, and include tests as part of it? So far I've been using the tests just to check that it works, but I guess you're right that this would be more helpful as documentation.

#### [ Rob Lewis (Oct 30 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136765454):
Maybe call them "examples" instead of "tests," if they're being used as documentation. But yeah, this would be super helpful!

#### [ Rob Lewis (Oct 30 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136765465):
How much of mathlib does this depend on?

#### [ Rob Lewis (Oct 30 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136766401):
This looks great, by the way, I'm excited to try it out.

#### [ Seul Baek (Oct 30 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136767194):
It depends mainly on the `int` and `nat` libraries, along with some inequality stuff from algebraic libraries. At one point I needed some gcd lemmas not included in the master branch, so the current .toml file is tweaked to get 3.4.1 instead. But when I look for it now I can't pinpoint that incompatibility, so perhaps it works with master now.

#### [ Seul Baek (Oct 30 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136767205):
Thanks!

#### [ Tobias Grosser (Oct 30 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136767372):
Very interesting.

#### [ Tobias Grosser (Oct 30 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136774706):
@**Seul Baek** , when trying to compile this I get some errors:

```
$leanpkg  build
configuring qe 0.1
test: unrecognized option: -d
mathlib: cloning https://github.com/leanprover/mathlib to _target/deps/mathlib
> mkdir -p _target/deps/mathlib
> git clone https://github.com/leanprover/mathlib _target/deps/mathlib
Cloning into '_target/deps/mathlib'...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 8217 (delta 1), reused 1 (delta 1), pack-reused 8209
Receiving objects: 100% (8217/8217), 5.24 MiB | 1.50 MiB/s, done.
Resolving deltas: 100% (5901/5901), done.
> git checkout --detach dbb3ff0b5b2e42aa71d8167d7efdb3aa12d6e483    # in directory _target/deps/mathlib
HEAD is now at dbb3ff0 feat(data/zmod/quadratic_reciprocity): quadratic reciprocity (#327)
> lean --make src
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: file 'basic' not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: file 'tauto' not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: file 'list' not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/bak/qe_eq.lean:1:0: error: file 'axms' not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: file 'dp' not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: file 'pfrm' not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: file 'reify' not found in the LEAN_PATH
/home/grosser/Projects/qe/src/lia/int_atm/dot_prod.lean:1:0: error: file 'list' not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: invalid import: basic
could not resolve import: basic
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: invalid import: tauto
could not resolve import: tauto
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: invalid import: list
could not resolve import: list
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: invalid import: dp
could not resolve import: dp
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: invalid import: pfrm
could not resolve import: pfrm
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: invalid import: reify
could not resolve import: reify
/home/grosser/Projects/qe/src/lia/int_atm/dot_prod.lean:1:0: error: invalid import: list
could not resolve import: list
```

#### [ Seul Baek (Oct 30 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136777126):
Oops, I forgot to push the commit in which I deleted older versions of files. I think it should work now.

#### [ Tobias Grosser (Oct 30 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136801178):
I also needed:

```
diff --git a/src/list.lean b/src/list.lean
index 6af0ace..369287c 100644
--- a/src/list.lean
+++ b/src/list.lean
@@ -248,3 +248,5 @@ begin
   intro heq, constructor; intros h a ha,
   rw ← heq, apply h _ ha, rw heq, apply h _ ha,
 end
+
+end list
```

#### [ Tobias Grosser (Oct 30 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136804241):
Nice. Some expressions already work nicely.

#### [ Tobias Grosser (Oct 30 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136804252):
Others time out quite a bit.


{% endraw %}
