---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/86268helpmefindlemmas.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [help me find lemmas](https://leanprover-community.github.io/archive/113489newmembers/86268helpmefindlemmas.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Nov 24 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148255862):
<p>Surely these are somewhere?</p>
<div class="codehilite"><pre><span></span>lemma le_pred_of_lt {n m : ℕ} (h : n &lt; m) : n ≤ m - 1 := sorry
lemma pred_le_self (n : ℕ) : n - 1 ≤ n := sorry
</pre></div>

#### [ Reid Barton (Nov 24 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148255973):
<p>Second is a special case of <code>nat.sub_le</code>, do you specifically need it for 1?</p>

#### [ Scott Morrison (Nov 24 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148256181):
<p>Thanks, that'll do fine for the second.</p>

#### [ Scott Morrison (Nov 24 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268678):
<p>We seem to have <code>le_sub_iff_add_le</code> for commutative groups, but not <code>le_sub_of_add_le</code> for <code>nat</code>?</p>

#### [ Scott Morrison (Nov 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268719):
<p>Am I missing something? I want <code>n + k ≤ b</code> implies <code>n ≤ b - k</code>.</p>

#### [ Mario Carneiro (Nov 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268721):
<p>I am sure it's there</p>

#### [ Mario Carneiro (Nov 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268722):
<p><code>nat.basic</code> has a really comprehensive list of facts like this</p>

#### [ Mario Carneiro (Nov 24 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268728):
<p><code>nat.le_sub_right_of_add_le</code></p>

#### [ Scott Morrison (Nov 24 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268774):
<p>ah, missing the <code>right</code>, thanks</p>

#### [ Scott Morrison (Nov 24 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148268883):
<p>I should use find more -- it would have successfully found this lemma, it turns out.</p>

#### [ Scott Morrison (Nov 24 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269200):
<div class="codehilite"><pre><span></span>H_left : n + k ≤ b,
H_right : b &lt; m + k
⊢ b - k &lt; m
</pre></div>

#### [ Mario Carneiro (Nov 24 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269357):
<p><code>nat.sub_lt_right_iff_lt_add</code></p>

#### [ Scott Morrison (Nov 24 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269625):
<p>Ah, okay. I just found <code>sub_lt_sub_right_iff</code> and managed to use that.</p>

#### [ Scott Morrison (Nov 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269664):
<p>So ... is there some long term plan to avoid me having to memorize all these? :-)</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148269669):
<p>go to <code>nat.basic</code> and browse around, that's what I jst did</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270509):
<p>Is the following a crazy idea: we know that we can't just take all the standard results about naturals and mark them as [simp] (some of them are one-way implications for example). Scott is complaining that he cannot find lemmas which are "standard" though. Can we tag a shedload of lemmas in data.nat.basic as "standard" and then instead of Scott having to play guess-the-name (which is still sometimes hard, despite the heroic efforts of the name-that-lemma team), he can just explicitly look for the lemma in the "standard" list. I am not saying that there should be a tactic which attempts to apply more than one standard lemma at once. But I am saying that there could be a <code>standard</code> tactic which literally tries to find exactly which lemma you need from a list, and applies it if it's there, and fails otherwise. </p>
<p>I have had problems recently looking for A -&gt; B if it happens to be the case that A &lt;-&gt; B. I personally never know whether to expect to see A -&gt; B or B -&gt; A or both or neither in the library if A &lt;-&gt; B is in there and I am not sure that there is a rule, especially if one direction needs some random thing I don't care about like decidability. Now I understand the philosophy of the library -- "if it looks standard, it should be there". OK so now let's make it easy to find the standard stuff by tagging it all with standard.</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270555):
<p>if the bidirectional version is there, the one directional versions should not be there normally, unless the assumptions are different in each direction</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270567):
<p>if A -&gt; B requires fewer assumptions than B -&gt; A, you will probably find A -&gt; B with a weak assumption and A &lt;-&gt; B with a strong assumption</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270619):
<p>Ah so there is some logic to it? I'd not realised this. Of course the other thing is when you look for A &lt;-&gt; B and it turns out that it's B &lt;-&gt; A which is in there.</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270627):
<p>in that case it's usually up to "simplification order"</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270629):
<p>Is that just me not knowing the implicit total order on all predicates...yeah, that.</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270674):
<p>for stuff involving subtraction vs addition, subtraction is on the left</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270679):
<p>So how does that work for add_assoc?</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270689):
<p>left assoc on the left, right assoc on the right. not much else to go on in that case</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270697):
<p>But the thing on the right has more characters in, so it's more complicated.</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270700):
<p>It's a comp lemma.</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270703):
<p>well that depends on the parser</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270752):
<p>what's the logic here?</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270755):
<p>honestly I would always write an assoc lemma with explicit parens</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270758):
<p>(I should double check that's not a lie)</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270760):
<p>Even then I'm looking at it and thinking it's 50-50</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270765):
<p>it is 50-50, I'm not going to lie</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270782):
<p>but you have to pick one order, and it was picked way back in core, and we stick with it</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270787):
<p>"Something is simpler if it has fewer brackets". Is that just nonsense?</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270799):
<p>I'm not sure how much stock to put in what the parser thinks is the best order</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270842):
<p>I guess that works for mul_add though</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270846):
<p>I don't know, I wouldn't bet on it</p>

#### [ Kevin Buzzard (Nov 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270856):
<p>OK, so it is random. The reason I am talking about add_assoc explicitly is that since I learnt that many simp or iff lemmas are of the form A = B, A &lt;-&gt; B with B less complicated than A, I've been able to start guessing which is on the left much better. But I still can't guess for add_assoc, so I just have to do look-up.</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270863):
<p>yeah, just do the old <code>.1</code> <code> .2</code></p>

#### [ Mario Carneiro (Nov 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270918):
<p>If I were to list a bunch of bracketing combinations in some order, I would probably start from left assoc, maybe that's just me</p>

#### [ Scott Morrison (Nov 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270919):
<p>So far my only idea for escaping "look up the damn lemmas" hell is to experiment with marking them all as <code>back</code>, and calling <code>back</code> a lot.</p>

#### [ Scott Morrison (Nov 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270923):
<p>I actually think this will solve a lot of my problems.</p>

#### [ Scott Morrison (Nov 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270930):
<p>And <code>back?</code> prints the term-mode proof it finds, so it's easy to replace it if it is slow.</p>

#### [ Scott Morrison (Nov 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270934):
<p>However .... all these <code>&lt;-&gt;</code> lemmas cause a problem.</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270938):
<p>metamath (more accurately, one of it's IDEs) had a one-step automatic proof function. It's a life saver for this stuff</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270980):
<p>you just write down all the assumptions you need and hit "go" and it finds the lemma</p>

#### [ Mario Carneiro (Nov 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148270990):
<p>you have to be pretty specific, but it's great for doing lookups in context</p>

#### [ Scott Morrison (Nov 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148271221):
<p>...</p>

#### [ Kevin Buzzard (Nov 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148271610):
<p><a href="https://www.urbandictionary.com/define.php?term=the%20old%20one%20two" target="_blank" title="https://www.urbandictionary.com/define.php?term=the%20old%20one%20two">https://www.urbandictionary.com/define.php?term=the%20old%20one%20two</a></p>

#### [ Johan Commelin (Nov 24 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148280408):
<blockquote>
<p>So ... is there some long term plan to avoid me having to memorize all these? :-)</p>
</blockquote>
<p>Yes, the long term goal is that you write some automation so that <em>we</em> can all avoid memorising these (-;</p>

#### [ Scott Morrison (Nov 24 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148288111):
<p>The only thing I know how to do for "lemmas involve nat subtraction" is to get <code>back</code> up and running and trying beat problems over the head with that. I suspect it will probably work (<code>back</code>, especially if it calls <code>simp</code> along the way, it's not so far from <code>auto</code>) but it won't be pretty.</p>

#### [ Kevin Buzzard (Nov 24 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148288271):
<p>Are these nat subtraction problems solved in Coq? Why are they arising? I am struggling to relate this to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mo>⊕</mo><mrow><mi>i</mi><mo>∈</mo><mi>I</mi></mrow></msub><msub><mi>M</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">\oplus_{i\in I}M_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8607em;vertical-align:-0.17737em;"></span><span class="base"><span class="mord"><span class="mbin">⊕</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">i</span><span class="mrel mtight">∈</span><span class="mord mathit mtight" style="margin-right:0.07847em;">I</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.17737em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> but I never looked at the big operators paper seriously.</p>

#### [ Andrew Ashworth (Nov 24 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148288448):
<p>Nat problems are solved by Omega in coq, aka Cooper in lean</p>

#### [ Scott Morrison (Nov 24 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148294216):
<p>The interaction between big operators and (un)natural subtraction is arising for me because I was working with sums of subset of the naturals, because the <code>k</code> in <code>choose n k</code> really ought to be a natural number.</p>

#### [ Keeley Hoek (Nov 25 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148300063):
<p>Hey Scott, is there a reason why back @ <a href="https://github.com/leanprover/mathlib/pull/410" target="_blank" title="https://github.com/leanprover/mathlib/pull/410">https://github.com/leanprover/mathlib/pull/410</a> should still have the WIP tag (not that you decide)/is there any programming work I can do to make it mergeable</p>

#### [ Scott Morrison (Nov 25 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302416):
<p>Yes, I'm sorry this PR has been abandonware for a while.</p>

#### [ Scott Morrison (Nov 25 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302462):
<p>I think the major obstacle is working out what to do with <code>apply_rules</code>. I haven't got around to looking at how <code>apply_rules</code> is used in mathlib yet.</p>

#### [ Scott Morrison (Nov 25 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302463):
<p>Can we just replace all the uses of <code>apply_rules</code> with <code>back</code>?</p>

#### [ Scott Morrison (Nov 25 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302517):
<p>It also needs some consideration of lemmas to tag, perhaps.</p>

#### [ Scott Morrison (Nov 25 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302537):
<p>The actual core code at &lt;<a href="https://github.com/leanprover/mathlib/pull/410/files#diff-e8836d95f7cd2f7e1c5ee370e791af03R33" target="_blank" title="https://github.com/leanprover/mathlib/pull/410/files#diff-e8836d95f7cd2f7e1c5ee370e791af03R33">https://github.com/leanprover/mathlib/pull/410/files#diff-e8836d95f7cd2f7e1c5ee370e791af03R33</a>&gt; could perhaps be rewritten, it reads a bit spaghetti-like at the moment, but I'm not sure what to do.</p>

#### [ Scott Morrison (Nov 25 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148302594):
<p>Something that would probably be easy for you, <span class="user-mention" data-user-id="110111">@Keeley Hoek</span>, but I was confused by, is combining the <code>back</code> and <code>elim</code> attributes into just <code>back</code> and <code>back!</code>.</p>

#### [ Sebastien Gouezel (Nov 25 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148312045):
<p>I don't think <code>apply_rules</code> is used anywhere yet, so you can safely remove it. I wrote it for proofs of continuity and limits, where it would be most useful, but there is a bug in Lean 3 <code>apply</code> (which unfolds too much) that prevents <code>apply</code> from working without underscores on continuity lemmas. So that I could never use it efficiently!</p>

#### [ Keeley Hoek (Nov 25 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148312348):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> When <code>back</code> and <code>elim</code> are the same attribute what should their single unified description string be?<br>
but sure, I'll do that and then do a tiny shuffle</p>

#### [ Scott Morrison (Nov 25 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148312403):
<p>I forget which way round they go now. One counts as progress even if you don't discharge the goal.</p>

#### [ Keeley Hoek (Nov 25 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148320789):
<p>I put in my 2-cents and did the stuff<br>
I got rid of that <code>precedence `?`:0</code> thing that worried you scott too</p>

#### [ Scott Morrison (Nov 26 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148337859):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> I cleaned up a few things, but also realised the current implementation of <code>back</code> is hopelessly inefficient, and will need to be replaced.</p>

#### [ Scott Morrison (Nov 26 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/help%20me%20find%20lemmas/near/148342141):
<p>(I'll continue this in the <code>PR reviews</code> stream.</p>


{% endraw %}
