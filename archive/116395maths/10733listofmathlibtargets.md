---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/10733listofmathlibtargets.html
---

## Stream: [maths](index.html)
### Topic: [list of mathlib targets](10733listofmathlibtargets.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 25 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132746533):
<p>Over the next couple of days I'm going to have a good look at the perfectoid project from a "bottom up" perspective and try and get a coherent idea of some easy targets for mathlib. For example (although not directly related to the perfectoid project) I would imagine it would be relatively easy to define PID's now and prove that Euclidean domains are PID's and that PID's are UFD's. My feeling is that achievable goals like this should be on some sort of informal list somewhere. Once the p-adic numbers get accepted then defining the adeles of a number field should also be on this list (and if people aren't happy with a definition being on the list then I can propose a random simple theorem about adeles, but for me a definition is fine). Where should such a list live? I remember once, when I was thinking about formalising my graduate course of earlier this year, I thought about formalising the adeles and I made it an issue in mathlib, but now I realise that probably there is a huge list of little things which I'd like to see in mathlib (several of which I'll probably end up doing myself) and I don't think it's sane to have an issue for each of them.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132746635):
<p>I should perhaps say that as well as some easy targets I guess I might also end up listing some harder targets. Is there already a place for this? I've realised now that I want mathlib to become the new Bourbaki; that's what people are doing here, and that's the style that they're writing. I think it would be nice to help things along the way by having a list of goals.</p>

#### [ Johan Commelin (Aug 25 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132747583):
<p>p-adic numbers are already in mathlib: <a href="https://github.com/leanprover/mathlib/pull/262" target="_blank" title="https://github.com/leanprover/mathlib/pull/262">https://github.com/leanprover/mathlib/pull/262</a></p>

#### [ Kevin Buzzard (Aug 25 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132748753):
<p>I didn't notice that it already got merged! I was just leaving for a holiday the day it did</p>

#### [ Patrick Massot (Aug 25 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132750840):
<p>There is <a href="https://github.com/leanprover/mathlib/blob/master/docs/wip.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/wip.md">https://github.com/leanprover/mathlib/blob/master/docs/wip.md</a> but you can also use <a href="https://github.com/leanprover-community/mathlib/wiki" target="_blank" title="https://github.com/leanprover-community/mathlib/wiki">https://github.com/leanprover-community/mathlib/wiki</a></p>

#### [ Kevin Buzzard (Aug 25 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751311):
<p>This is not works in progress -- this is stuff which I want there to be progress on :-)</p>

#### [ Scott Morrison (Aug 25 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751428):
<p>I agree PIDs are gap that needs fixing soon! I've been suggesting my students <span class="user-mention" data-user-id="120536">@Jack Crawford</span> and Ed Hofflin look at those, but as they're still getting started on Lean it may take a while.</p>

#### [ Scott Morrison (Aug 25 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751469):
<p>Let's have a list on the leanprover-community wiki!</p>

#### [ Kevin Buzzard (Aug 25 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751530):
<p>How does that work? If you start something, can other people edit it?</p>

#### [ Scott Morrison (Aug 25 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751532):
<p>I think so --- everyone who has commit access on leanprover-community, and I think the intention is that everyone who wants to make PRs to mathlib can have this.</p>

#### [ Scott Morrison (Aug 25 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751573):
<p>You should try editing the list I wrote for ideas of things to go over next week: <a href="https://github.com/leanprover-community/mathlib/wiki/Lean-in-Orsay,-2018" target="_blank" title="https://github.com/leanprover-community/mathlib/wiki/Lean-in-Orsay,-2018">https://github.com/leanprover-community/mathlib/wiki/Lean-in-Orsay,-2018</a></p>

#### [ Reid Barton (Aug 25 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751574):
<p>My first thought would be to just use the github issue tracker. You can organize issues using labels, so I don't think having lots of "feature request" issues would be overwhelming.</p>

#### [ Scott Morrison (Aug 25 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751593):
<p>What if we used issues on the main mathlib repository to indicate defects, and issues on the leanprover-community fork of mathlib for summaries of work in progress, or for wishlists?</p>

#### [ Reid Barton (Aug 25 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751747):
<p>That's possible if that arrangement is clearly signposted somewhere (like, at the top of mathlib's README.md). I do like the idea of including entries for work-in-progress since we're already at the stage at which it can be hard to keep track of what everyone is working on.<br>
Actually, brainstorming small projects of just the sort that Kevin mentioned is on my list of things to do next week, and part of the aim here is to give potential new contributors things to work on.</p>

#### [ Reid Barton (Aug 25 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132751831):
<p>For example, Zulip has the "good first issue" tag<br>
<a href="https://github.com/zulip/zulip/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22" target="_blank" title="https://github.com/zulip/zulip/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22">https://github.com/zulip/zulip/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22</a></p>

#### [ Scott Morrison (Aug 25 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752066):
<p>Maybe it does make sense to have them all in one place...</p>

#### [ Reid Barton (Aug 25 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752140):
<p>I'm kind of neutral about it. I do also see the appeal of keeping a separate list.</p>

#### [ Reid Barton (Aug 25 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752210):
<p>BTW, one of the items on my wishlist is the structure theorem for f.g. modules over a PID. Guess I didn't realize there are no PIDs yet either :)</p>

#### [ Scott Morrison (Aug 25 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752296):
<p>Smith normal form is a great project for someone who wants to learn how to do recursion well!</p>

#### [ Jack Crawford (Aug 25 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132752682):
<p>Yeah <span class="user-mention" data-user-id="110087">@Scott Morrison</span>  I’m pretty keen on tackling Smith Normal Form sometime soon, along with PIDs. (At least, after midsems next week)</p>

#### [ Johan Commelin (Aug 25 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132756802):
<p>Someone should also take a serious stab at algebraic closures.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758625):
<p>I'm occasionally pestering <span class="user-mention" data-user-id="110064">@Kenny Lau</span> to do these :-) Kenny -- can you give us an update of what needs to be done?</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758632):
<p>I think the issue is that there's some infrastructure which isn't there yet, but I've forgotten what.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758642):
<p>For a while the hold-up was no robust theory of polynomials in 1 variable, but that is now done thanks to Chris.</p>

#### [ Kenny Lau (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758645):
<p>splitting fields</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758647):
<p><em>boggle</em></p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758649):
<p>Do you need all the facts about them?</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758702):
<p>I mean -- uniqueness? That's the annoying one</p>

#### [ Kenny Lau (Aug 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758704):
<p>no</p>

#### [ Kenny Lau (Aug 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758705):
<p>we don't even need minimality</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758731):
<p>Given a polynomial of degree n over a field K it's not too hard to prove by induction on n that there's a bigger field L contaning K where that polynomial factors into linear factors.</p>

#### [ Kenny Lau (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758734):
<p>yeah</p>

#### [ Kenny Lau (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758735):
<p>right</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758740):
<p>Is that tough?</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758741):
<p>Oh!</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758787):
<p>You need that K[X]/(irred poly) is a field.</p>

#### [ Kenny Lau (Aug 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758792):
<p>and you also need to prove that K[X] is UFD</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758794):
<p>I don't think you need as much as that</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758798):
<p>Do you need uniqueness?</p>

#### [ Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758807):
<p>no</p>

#### [ Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758808):
<p>actually we don't need it to be a field</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758809):
<p>It suffices to prove we can add a root of a poly to a field and get a new field</p>

#### [ Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758810):
<p>given f</p>

#### [ Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758812):
<p>K[X]/(f) is a ring</p>

#### [ Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758813):
<p>now what do you do with rings</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758814):
<p>now take a max ideal</p>

#### [ Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758815):
<p>you quotient by a maximal ideal</p>

#### [ Kenny Lau (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758816):
<p>tada</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758817):
<p>right</p>

#### [ Kenny Lau (Aug 25 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758860):
<p>genius</p>

#### [ Kevin Buzzard (Aug 25 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132758861):
<p>I think Chris proved quotient by a max ideal was a field, recently</p>

#### [ Chris Hughes (Aug 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759244):
<p>Polynomials are a Euclidean domain is there. I don't think Euclidean implies PID and PID implies prime ideals are maximal is that hard.</p>

#### [ Kenny Lau (Aug 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759250):
<p>also PID doesn't imply prime ideals are maximal</p>

#### [ Kenny Lau (Aug 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759251):
<p>also s/is/are/</p>

#### [ Johan Commelin (Aug 25 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759352):
<p>Would the following idea be an option. It's a bit of a hack, because of <code>K : Type u</code>, then <code>K-bar : Type (u+1)</code>.</p>

#### [ Johan Commelin (Aug 25 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759361):
<p>You let <code>Alg(K)</code> be the type of algebraic extensions of <code>K</code>, and then apply Zorn's lemma.</p>

#### [ Johan Commelin (Aug 25 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759365):
<p>Maybe with some trickery you can even get <code>K-bar</code> back into <code>Type u</code>. I'm not an expert on this.</p>

#### [ Johan Commelin (Aug 25 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132759411):
<p>Anyway, whatever the definition, we will want a theorem that says that <code>K-bar</code> is unique up to iso.</p>

#### [ Morenikeji Neri (Aug 26 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132787623):
<p>I've actually defined PIDs and have a proof that compiles of ED -&gt; PID (with some help from Chris) <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Aug 26 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132787801):
<p>great, now get it to mathlib :P</p>

#### [ Scott Morrison (Aug 26 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132788247):
<p>I saw that yesterday!</p>

#### [ Scott Morrison (Aug 26 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/list%20of%20mathlib%20targets/near/132788248):
<p>I'm hoping we can bring the proof down to something much smaller. After all, to explain it to a human is only a few lines!</p>


{% endraw %}
