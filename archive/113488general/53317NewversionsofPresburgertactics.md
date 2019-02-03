---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53317NewversionsofPresburgertactics.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [New versions of Presburger tactics](https://leanprover-community.github.io/archive/113488general/53317NewversionsofPresburgertactics.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Seul Baek (Oct 30 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136761498):
<p>This project has been neglected for a long time, so I decided to tidy it up a bit. The new versions are available at <a href="https://github.com/skbaek/qe/" target="_blank" title="https://github.com/skbaek/qe/">https://github.com/skbaek/qe/</a>. The main changes are :</p>
<p>1. Now there are tactics for <code>nat</code>, although they are slower than <code>int</code> equivalents due to quantifiers added during translation<br>
2. There are versions that use <code>znum</code> instead of <code>int</code> in the shadow syntax for optimization<br>
3. Makes more use of typeclasses<br>
4. Also includes a tactic for DLO without endpoints for <code>rat</code><br>
5. The <code>leanpkg.toml</code> file is fixed, so you can install it using <code>leanpkg</code></p>
<p>The main tactics are in the <code>main.lean</code> files of each directory. You can see the <code>tests.lean</code> files for examples of how they are used. As you might expect, <code>znum</code> is more efficient when handling large numbers, so there are examples which time out for <code>int</code>-based tactics but works with <code>znum</code>.</p>
<p>3 and 4 were done just to show that the shared-framework approach is viable. The idea (from <a href="http://www21.in.tum.de/~nipkow/pubs/jar10.pdf" target="_blank" title="http://www21.in.tum.de/~nipkow/pubs/jar10.pdf">Tobias Nipkow</a>) is that QE-based FoL decision procedures mostly follow the same scheme, so the common part should be factored out using some module or typeclass system. Once this work is done, it is easy to cook up more decision procedures, since all you need to do is define (and prove soundness for) a single quantifier elimination step.</p>

#### [ Patrick Massot (Oct 30 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136763199):
<p>Thanks! Could you include a glossary of what all those acronyms mean? Maybe in a README.md?</p>

#### [ Patrick Massot (Oct 30 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136763375):
<p>What are all those commented out lines in the test files? Things that should work but don't?</p>

#### [ Patrick Massot (Oct 30 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136763429):
<p>For the purpose of using tests as documentation, it would probably be more efficient to move those test files somewhere more visible</p>

#### [ Seul Baek (Oct 30 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136764118):
<blockquote>
<p>Thanks! Could you include a glossary of what all those acronyms mean? Maybe in a README.md?</p>
</blockquote>
<p>Yes, I should either do that, or actually give intelligible names to definitions, which I was too lazy to type out when doing the proofs.</p>

#### [ Seul Baek (Oct 30 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136764373):
<p>The commented out lines are either theorems which currently time out, or nontheorems which would be useful for testing the soundness of unverified vm-versions of the tactics (which currently don't exist, but are easy to implement if necessary).</p>

#### [ Seul Baek (Oct 30 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136764898):
<p>Do you mean that it would be useful to add some introductory information about the tactics for users, and include tests as part of it? So far I've been using the tests just to check that it works, but I guess you're right that this would be more helpful as documentation.</p>

#### [ Rob Lewis (Oct 30 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136765454):
<p>Maybe call them "examples" instead of "tests," if they're being used as documentation. But yeah, this would be super helpful!</p>

#### [ Rob Lewis (Oct 30 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136765465):
<p>How much of mathlib does this depend on?</p>

#### [ Rob Lewis (Oct 30 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136766401):
<p>This looks great, by the way, I'm excited to try it out.</p>

#### [ Seul Baek (Oct 30 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136767194):
<p>It depends mainly on the <code>int</code> and <code>nat</code> libraries, along with some inequality stuff from algebraic libraries. At one point I needed some gcd lemmas not included in the master branch, so the current .toml file is tweaked to get 3.4.1 instead. But when I look for it now I can't pinpoint that incompatibility, so perhaps it works with master now.</p>

#### [ Seul Baek (Oct 30 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136767205):
<p>Thanks!</p>

#### [ Tobias Grosser (Oct 30 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136767372):
<p>Very interesting.</p>

#### [ Tobias Grosser (Oct 30 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136774706):
<p><span class="user-mention" data-user-id="116585">@Seul Baek</span> , when trying to compile this I get some errors:</p>
<div class="codehilite"><pre><span></span>$leanpkg  build
configuring qe 0.1
test: unrecognized option: -d
mathlib: cloning https://github.com/leanprover/mathlib to _target/deps/mathlib
&gt; mkdir -p _target/deps/mathlib
&gt; git clone https://github.com/leanprover/mathlib _target/deps/mathlib
Cloning into &#39;_target/deps/mathlib&#39;...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 8217 (delta 1), reused 1 (delta 1), pack-reused 8209
Receiving objects: 100% (8217/8217), 5.24 MiB | 1.50 MiB/s, done.
Resolving deltas: 100% (5901/5901), done.
&gt; git checkout --detach dbb3ff0b5b2e42aa71d8167d7efdb3aa12d6e483    # in directory _target/deps/mathlib
HEAD is now at dbb3ff0 feat(data/zmod/quadratic_reciprocity): quadratic reciprocity (#327)
&gt; lean --make src
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: file &#39;basic&#39; not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: file &#39;tauto&#39; not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/bak/qe.lean:1:0: error: file &#39;list&#39; not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/bak/qe_eq.lean:1:0: error: file &#39;axms&#39; not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: file &#39;dp&#39; not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: file &#39;pfrm&#39; not found in the LEAN_PATH
/home/grosser/Projects/qe/src/dnf/main.lean:1:0: error: file &#39;reify&#39; not found in the LEAN_PATH
/home/grosser/Projects/qe/src/lia/int_atm/dot_prod.lean:1:0: error: file &#39;list&#39; not found in the LEAN_PATH
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
</pre></div>

#### [ Seul Baek (Oct 30 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136777126):
<p>Oops, I forgot to push the commit in which I deleted older versions of files. I think it should work now.</p>

#### [ Tobias Grosser (Oct 30 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136801178):
<p>I also needed:</p>
<div class="codehilite"><pre><span></span>diff --git a/src/list.lean b/src/list.lean
index 6af0ace..369287c 100644
--- a/src/list.lean
+++ b/src/list.lean
@@ -248,3 +248,5 @@ begin
   intro heq, constructor; intros h a ha,
   rw ← heq, apply h _ ha, rw heq, apply h _ ha,
 end
+
+end list
</pre></div>

#### [ Tobias Grosser (Oct 30 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136804241):
<p>Nice. Some expressions already work nicely.</p>

#### [ Tobias Grosser (Oct 30 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20versions%20of%20Presburger%20tactics/near/136804252):
<p>Others time out quite a bit.</p>


{% endraw %}
