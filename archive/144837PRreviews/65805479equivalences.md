---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/65805479equivalences.html
---

## Stream: [PR reviews](index.html)
### Topic: [#479 equivalences](65805479equivalences.html)

---


{% raw %}
#### [ Scott Morrison (Nov 16 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147792343):
<p>This one was overdue, and lurking in my other repository.</p>

#### [ Scott Morrison (Nov 16 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147792347):
<ul>
<li>Define <code>equivalence C D</code> for an equivalence of categories,</li>
<li><code>[refl]</code>, <code>[symm]</code>, and <code>[trans]</code> for equivalences,</li>
<li>a typeclass <code>is_equivalence</code> to decorate functors,</li>
<li>and the proofs that a functor is an equivalence if and only if it is fully faithful and essentially surjective.</li>
</ul>

#### [ Scott Morrison (Nov 16 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147792389):
<p>One thing to note: <code>ess_surj</code> here is the constructive version, that picks a particular up-to-isomorphism-preimage for every object, not merely asserting that one exists.</p>

#### [ Scott Morrison (Nov 16 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147792396):
<p>If this is upsetting, I can add an extra constructor that uses choice and just takes the existence statement.</p>

#### [ Reid Barton (Nov 16 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793562):
<p>I think it might be best to just make <code>ess_surj</code> a Prop</p>

#### [ Reid Barton (Nov 16 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793709):
<p>I'm actually not sure... when does one really use the fact that ess. surj. + fully faithful implies an equivalence?</p>

#### [ Mario Carneiro (Nov 16 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793744):
<p>I thought that was the only purpose of ess surj</p>

#### [ Reid Barton (Nov 16 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793912):
<p>I see... I guess the point is that you don't have to construct the functoriality of the inverse functor</p>

#### [ Reid Barton (Nov 16 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793968):
<p>or the naturality of one of the isomorphisms</p>

#### [ Reid Barton (Nov 16 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147793980):
<p>or both isomorphisms actually</p>

#### [ Reid Barton (Nov 16 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147794043):
<p>Maybe it would be simplest to just discard <code>ess_surj</code> and inline its fields into arguments of <code>equivalence_of_fully_faithfully_ess_surj</code></p>

#### [ Reid Barton (Nov 16 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147794205):
<p>The same thing happens for adjunctions (<a href="https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/adjunction.lean#L280" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/adjunction.lean#L280">https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/adjunction.lean#L280</a>)</p>

#### [ Reid Barton (Nov 16 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147794676):
<p>But in actual math, providing that structure would always be trivial, anyways</p>

#### [ Reid Barton (Nov 16 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147795637):
<p>I guess another way of putting it is: when would you need choice to prove that a functor (which you're proving is an equivalence) is essentially surjective, rather than just writing down a formula for an inverse image of an object</p>

#### [ Scott Morrison (Nov 16 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/147801654):
<p>I’d be happy with the inlining solution.</p>

#### [ Scott Morrison (Nov 28 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148697250):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, what do you think here? Inlining <code>ess_surj</code> feels to me like to makes the code more cluttered, and I don't really understand the argument against having it.</p>

#### [ Johan Commelin (Nov 28 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148697336):
<p>I wouldn't mind keeping it. I think it might turn out to be useful... although I don't have a concrete example. But I think essential images show up, and probably we want to know that functors are essentially surjective onto their essential image, etc...</p>

#### [ Scott Morrison (Nov 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698817):
<p>Besides this question about <code>ess_surj</code>, the equivalences branch is now ready to go. It's mostly the basic facts about equivalences.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698824):
<p>It also contains a new category theory-specific  tactic <code>slice</code>.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698840):
<div class="codehilite"><pre><span></span>/--
`slice` is a conv tactic; if the current focus is a composition of several morphisms,
`slice a b` reassociates as needed, and zooms in on the `a`-th through `b`-th morphisms.

Thus if the current focus is `(a ≫ b) ≫ ((c ≫ d) ≫ e)`, then `slice 2 3` zooms to `b ≫ c`.
 -/
</pre></div>

#### [ Scott Morrison (Nov 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698845):
<div class="codehilite"><pre><span></span>/--
`slice_lhs a b { tac }` zooms to the left hand side, uses associativity for categorical
composition as needed, zooms in on the `a`-th through `b`-th morphisms, and invokes `tac`.
-/
</pre></div>

#### [ Scott Morrison (Nov 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698864):
<p>There's also a note in the PR:</p>
<div class="codehilite"><pre><span></span>-- TODO someone might like to generalise this tactic to work with other associative structures.
</pre></div>


<p>but that someone is not me at the moment, and hopefully won't hold up this PR.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148698918):
<p>(It's possible <span class="user-mention" data-user-id="110026">@Simon Hudon</span> will be interested, however, as he's done similar stuff already.)</p>

#### [ Mario Carneiro (Nov 28 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700202):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> oh dear, something went wrong in the merge. Did I miss a dependent PR?</p>

#### [ Scott Morrison (Nov 28 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700271):
<p>I don't think so?</p>

#### [ Scott Morrison (Nov 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700278):
<p>Shall I rebase onto current master?</p>

#### [ Scott Morrison (Nov 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700281):
<p>Or is it too late for that? :-)</p>

#### [ Scott Morrison (Nov 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700305):
<p>It looks okay to me? I see it sitting on top of master now.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700446):
<p>Oh, I see there are problems.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700487):
<p>ok, fix coming</p>

#### [ Scott Morrison (Nov 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700495):
<p>I think it's minor, some imports, but I'm not sure how they got messed up.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700541):
<p>It looks like changing the line <code>import category_theory.embedding</code> to <code>import category_theory.fully_faithful</code> at the top of <code>category_theory/equivalences.lean</code> solves the problem.</p>

#### [ Scott Morrison (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700584):
<p>I've no idea how it was passing locally and on travis with that wrong, but okay. :-)</p>

#### [ Scott Morrison (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700595):
<p>I guess just that <code>.olean</code> files never get deleted!?</p>

#### [ Mario Carneiro (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700599):
<p>right</p>

#### [ Scott Morrison (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700602):
<p>Is it best if you make that change?</p>

#### [ Scott Morrison (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700609):
<p>Or should I make a commit on community?</p>

#### [ Mario Carneiro (Nov 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700618):
<p>eh, it's not checked out here, just send a PR</p>

#### [ Scott Morrison (Nov 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700659):
<p>ok, I will fix some documentation failures I'm noticing at the same time :-)</p>

#### [ Mario Carneiro (Nov 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148700709):
<p>ok</p>

#### [ Scott Morrison (Nov 28 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148701010):
<p><a href="https://github.com/leanprover/mathlib/issues/500" target="_blank" title="https://github.com/leanprover/mathlib/issues/500">#500</a></p>

#### [ Reid Barton (Nov 28 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148711889):
<blockquote>
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, what do you think here? Inlining <code>ess_surj</code> feels to me like to makes the code more cluttered, and I don't really understand the argument against having it.</p>
</blockquote>
<p>My only objection is that the name <code>ess_surj</code> is wrong, because "essentially surjective" is a property but <code>ess_surj F</code> values are not unique in any sense at all (except when <code>F</code> is actually an equivalence).</p>

#### [ Reid Barton (Nov 28 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148711978):
<p>It should be named <code>ess_left_inverse_on_objects</code> (or maybe right--I've lost any grasp I may have once had on the difference between left and right), or <code>ess_surj_data</code> or <code>ess_surj_choices</code> or something.</p>

#### [ Scott Morrison (Nov 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23479%20equivalences/near/148741371):
<p>Okay! I will rename it to something sufficiently unpleasant looking to warn people off. :-)</p>


{% endraw %}
