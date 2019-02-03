---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75934Conflictingtransitivecoercions.html
---

## Stream: [general](index.html)
### Topic: [Conflicting transitive coercions?](75934Conflictingtransitivecoercions.html)

---


{% raw %}
#### [ Nicholas Scheel (May 26 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127117518):
<p>I have two terms that pretty-print the same but won't be considered equivalent because they seem to use slightly different coerce instances:</p>
<div class="codehilite"><pre><span></span>invalid type ascription, term has type
  @eq int
    ((@coe nat Zalpha
        (@coe_to_lift nat Zalpha (@coe_trans nat int Zalpha int.has_coe (@coe_base int Zalpha Zalpha.has_coe)))
        (fib (@has_add.add nat nat.has_add m 1))).r)
    0
but is expected to have type
  @eq int
    ((@coe nat Zalpha
        (@coe_to_lift nat Zalpha
           (@coe_base nat Zalpha (@nat.cast_coe Zalpha Zalpha.has_zero Zalpha.has_one Zalpha.has_add)))
        (fib (@has_add.add nat nat.has_add m 1))).r)
    0
</pre></div>


<p>(part of Kevin's project: <a href="https://github.com/kbuzzard/lean-squares-in-fibonacci/blob/master/src/Zalpha.lean" target="_blank" title="https://github.com/kbuzzard/lean-squares-in-fibonacci/blob/master/src/Zalpha.lean">https://github.com/kbuzzard/lean-squares-in-fibonacci/blob/master/src/Zalpha.lean</a>)<br>
I'm giving up for tonight, but do you have any suggestions on how this could be resolved or avoided?</p>

#### [ Kevin Buzzard (May 26 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127120917):
<p>Polynomials: I think you have to avoid the general multivariate code because there is a whole bunch of theory specific to the one variable case. You can have a coercion to the multivariable case and prove it's injective and then you get some theorems for free</p>

#### [ Kevin Buzzard (May 26 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127120965):
<p>Coercions -- these are unfortunately one of the dark arts as far as mathematicians are concerned. You can't set it up the way we do it -- coercions and partial coercions invoked in all directions often without remark. Welcome to type theory. Your coercions I think in general all have to go in one direction, and if you coerce from X to Y and from Y to Z and from X to Z independently then the two maps X -&gt; Z have to be <em>definitionally</em> equal or the entire system breaks.</p>

#### [ Kevin Buzzard (May 26 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121012):
<p>This leads to non-trivial problems with the entire system -- for example if you want to coerce a metric space into a topological space then this sounds harmless on the face of it, but if you want the product of metric spaces to be a metric space and the product of topological spaces to be a topological space then you are going to have to think hard whether the two induced topological structures on the product of two metric spaces are definitionally equal, and probably for the way you naively just set it up in your head the answer is "they are equal, but it's a theorem not a definition", which is not good enough.</p>

#### [ Kevin Buzzard (May 26 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121071):
<p>This whole thing falls into a general category of "easy in maths, hard in Lean" concepts which I think are extremely important to (a) isolate and (b) work around, because I believe that Lean should not just offer "what it is" to mathematicians, it should attempt to do the much harder job of offering Lean "what mathematicians do, the way they do it".</p>

#### [ Mario Carneiro (May 26 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121114):
<p>What is <code>Zalpha.has_coe</code>?</p>

#### [ Mario Carneiro (May 26 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121118):
<p>Looks like there are two coercions there, and there is a needed theorem to show they are the same</p>

#### [ Mario Carneiro (May 26 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121128):
<p>I wouldn't go so far as to say that all coercion chains have to be defeq, but you should have a theorem proving they are equal as a simp lemma to clean these kind of things up</p>

#### [ Mario Carneiro (May 26 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121191):
<p>From what I can see, there are two paths: you have a defined coercion <code>int -&gt; Zalpha</code> which is composed with the natural map <code>nat -&gt; int</code>, and then also there is a coercion <code>nat -&gt; Zalpha</code> because <code>Zalpha</code> is a ring or ringlike thing</p>

#### [ Mario Carneiro (May 26 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121241):
<p>You can use <code>nat.eq_cast</code> to prove that they are equal</p>

#### [ Kevin Buzzard (May 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121352):
<p>Are they not defeq, and is this a problem?</p>

#### [ Mario Carneiro (May 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121355):
<p>They aren't even proven equal</p>

#### [ Mario Carneiro (May 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121357):
<p>there is a missing theorem here</p>

#### [ Mario Carneiro (May 26 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121368):
<p>I think you should remove <code>instance : has_coe ℤ ℤα := ⟨of_int⟩</code>, and then after proving it's a ring you should prove <code>of_int z = z</code></p>

#### [ Mario Carneiro (May 26 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121370):
<p>where the right <code>z</code> is being coerced using the cast function</p>

#### [ Mario Carneiro (May 26 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127121460):
<p>compare with how <code>rat.of_int</code> is handled in <code>rat.lean</code></p>

#### [ Nicholas Scheel (May 26 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127132931):
<p>til <code>unfold_coes</code></p>

#### [ Nicholas Scheel (May 26 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127133498):
<p>Thanks for the advice <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>! It seems to be working much much better :)</p>

#### [ Nicholas Scheel (May 26 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Conflicting%20transitive%20coercions%3F/near/127133604):
<p>I guess when they write "canonical" in</p>
<blockquote>
<p>Canonical homomorphism from the integers to any ring(-like) structure <code>α</code></p>
</blockquote>
<p>They really mean <em>canonical</em> – don't use anything else!</p>


{% endraw %}
