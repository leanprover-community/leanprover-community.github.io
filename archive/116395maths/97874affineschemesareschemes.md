---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/97874affineschemesareschemes.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [affine schemes are schemes](https://leanprover-community.github.io/archive/116395maths/97874affineschemesareschemes.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 23 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963591):
<p>I just reached a milestone:</p>

#### [ Kevin Buzzard (May 23 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963592):
<p><code>noncomputable definition scheme_of_affine_scheme (R : Type u) [comm_ring R] : scheme := [definition which typechecks]</code></p>

#### [ Kevin Buzzard (May 23 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963595):
<p>This was a very surprising process.</p>

#### [ Kevin Buzzard (May 23 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963635):
<p>Several times over the last few months I have confidently felt that I was "just a few hours' work away" from this result</p>

#### [ Kevin Buzzard (May 23 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963640):
<p>and then I would run into a "trivial to a mathematician, not so trivial in dependent type theory" type issue</p>

#### [ Kevin Buzzard (May 23 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963649):
<p>The most recent was last night, where I had to write down a map <code>F U -&gt; F (id '' U)</code> (here <code>U : set X</code>)</p>

#### [ Kevin Buzzard (May 23 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963689):
<p>and I foolishly rewrote <code>id '' U</code> to <code>U</code> and used the identity map and ran into all sorts of problems</p>

#### [ Kevin Buzzard (May 23 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963722):
<p>but this time I was ready for it -- I changed it to a more general construction which gave a map <code>F U -&gt; F V</code> for any <code>V \sub U</code> and applied it in this case.</p>

#### [ Kevin Buzzard (May 23 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963728):
<p>There is a subtlety happening here which I am not entirely sure I 100% understand.</p>

#### [ Kevin Buzzard (May 23 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963731):
<p>I think it might be to do with an equivalence of categories</p>

#### [ Kevin Buzzard (May 23 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963780):
<p>A mathematician takes a topological space X and then defines a presheaf of abelian groups on X to be, for every open set U in X an abelian group F U</p>

#### [ Kevin Buzzard (May 23 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963790):
<p>and for every pair of opens V in U, a restriction map F U -&gt; F V</p>

#### [ Kevin Buzzard (May 23 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963798):
<p>[the model is that F U is the set of "functions on U", so this restriction map is restriction of functions]</p>

#### [ Kevin Buzzard (May 23 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963846):
<p>and this pair F,res has to satisfy two axioms: res : F U -&gt; F U is the identity</p>

#### [ Kevin Buzzard (May 23 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963850):
<p>and if W in V in U the two maps F U -&gt; F W (res, and res circ res) are the same</p>

#### [ Kevin Buzzard (May 23 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963909):
<p>And then an algebraic geometry textbook might then say "here's a cool way of looking at this: let's make the set of open subsets of X into a category -- the objects are the opens and there's one morphism from U to V iff V is a subset of U, and then the axioms for a presheaf are just the statement that F is a functor"</p>

#### [ Kevin Buzzard (May 23 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963914):
<p>but somehow this is just a language, this particular fact that something is a functor is never really used in any deep way</p>

#### [ Kevin Buzzard (May 23 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963926):
<p>there are plenty of functors around like global sections functors which really do play a role, with derived functors etc etc, but this is not one of them.</p>

#### [ Kevin Buzzard (May 23 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963929):
<p>In dependent type theory, I think there is something deeper going on.</p>

#### [ Kevin Buzzard (May 23 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963972):
<p>The "category of open sets" is somehow replaced by a much more complex category, the category of terms each of which can be proved to be an open set</p>

#### [ Kenny Lau (May 23 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963975):
<p>but there is only countably many terms!</p>

#### [ Kevin Buzzard (May 23 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963983):
<p>and there's a morphism t1 -&gt; t2 precisely when there's a proof that the open set corresponding to t2 is a subset of the open set corresponding to t1</p>

#### [ Kevin Buzzard (May 23 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963989):
<p>I don't care</p>

#### [ Kevin Buzzard (May 23 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963990):
<p>I don't think I care</p>

#### [ Kevin Buzzard (May 23 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126963995):
<p>Maybe I haven't got the language right</p>

#### [ Kevin Buzzard (May 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964038):
<p>I am happy that if I have a term and a proof that it is an open set then it's in</p>

#### [ Kevin Buzzard (May 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964042):
<p>and the term might be U and the proof might be sorry</p>

#### [ Kevin Buzzard (May 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964046):
<p>and that pretty much covers everything</p>

#### [ Kevin Buzzard (May 23 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964050):
<p>So in some sense I did not even realise when I defined a presheaf that I was defining it on this much bigger category</p>

#### [ Kevin Buzzard (May 23 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964053):
<p>but because the two categories are equivalent it doesn't matter mathematically</p>

#### [ Kevin Buzzard (May 23 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964063):
<p>but a consequence of this incorrect mindset was that I often wanted to identify things like F ((U cap V) cap W) and F(U cap (V cap W)) as _equal_</p>

#### [ Kevin Buzzard (May 23 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964064):
<p>because to a mathematician they are equal</p>

#### [ Kevin Buzzard (May 23 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964104):
<p>but in dependent type theory they are just canonically isomorphic</p>

#### [ Johan Commelin (May 23 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964106):
<p>Isn't this another instance of "we really need transport of structure"?</p>

#### [ Chris Hughes (May 23 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964107):
<p>No they're equal?</p>

#### [ Kevin Buzzard (May 23 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964109):
<p>and the correct way to move between them is via the restriction map associated to the proof that the sets are equal</p>

#### [ Kevin Buzzard (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964113):
<p>Chris, perhaps they really are equal, but by equal here I think I mean defeq</p>

#### [ Kevin Buzzard (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964118):
<p>Johan -- in this case I am suggesting another approach</p>

#### [ Johan Commelin (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964122):
<p>I know, but it means that you are becoming more of a CS guy...</p>

#### [ Mario Carneiro (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964124):
<p>Here you actually have transport of structure, because <code>eq.rec</code> asserts that everything you can express commutes with equality</p>

#### [ Kevin Buzzard (May 23 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964125):
<p>"transport of structure" in this situation seems to be some sort of brute force collapsing of the bigger category into the equivalent smaller one</p>

#### [ Johan Commelin (May 23 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964170):
<p>That brute force is exactly what we need, if we ever hope to get up to speed with formalising maths</p>

#### [ Kevin Buzzard (May 23 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964171):
<p>The <code>eq.rec</code> remark is true, <em>however</em></p>

#### [ Mario Carneiro (May 23 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964172):
<p>but that doesn't mean the transport is easy to use without a lot of lemmas</p>

#### [ Kevin Buzzard (May 23 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964174):
<p>in practice, because I was dealing with complicated things on top of all this</p>

#### [ Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964180):
<p>eq.rec did not suffice to solve all my problems.</p>

#### [ Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964185):
<p>If I had some complex term with <code>id '' U</code> in</p>

#### [ Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964187):
<p>and all of a sudden I thought "crap, my life would be much easier if that term was just U`</p>

#### [ Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964191):
<p>then sometimes I would try and rewrite and the rewrite would fail</p>

#### [ Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964193):
<p>or it would be a PITA to formulate</p>

#### [ Kevin Buzzard (May 23 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964198):
<p>because the naively written rewrite was not type correct</p>

#### [ Kevin Buzzard (May 23 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964242):
<p>because H used to be proof of V subset (id '' U) and that needed rewriting as swell</p>

#### [ Kevin Buzzard (May 23 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964245):
<p>and congr was not good enough at this sort of thing</p>

#### [ Kevin Buzzard (May 23 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964248):
<p>and subst was not either</p>

#### [ Kevin Buzzard (May 23 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964251):
<p>sorry, subst, not congr</p>

#### [ Kenny Lau (May 23 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964262):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> have you pushed?</p>

#### [ Mario Carneiro (May 23 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964263):
<p>the <code>eq.rec</code> term itself acts as a function <code>F U -&gt; F (id '' U)</code>, and then you need to know this is functorial for later stuff</p>

#### [ Kevin Buzzard (May 23 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964268):
<p>In this particular case all my problems went away when I started thinking about the equivalent category</p>

#### [ Kevin Buzzard (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964269):
<p>Kenny, I just pushed</p>

#### [ Mario Carneiro (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964304):
<p>and this is true, but more complicated to prove; and you may need <em>that</em> proof to be functorial and it gets yet more complicated...</p>

#### [ Mario Carneiro (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964309):
<p>this is what HoTT people deal with</p>

#### [ Kevin Buzzard (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964310):
<p>Mario -- I'm sure you're right</p>

#### [ Kevin Buzzard (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964311):
<p>This certainly sounds like the sort of issue which we have to deal with here</p>

#### [ Kevin Buzzard (May 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964312):
<p>And to be quite frank I did feel like I had dodged a bullet</p>

#### [ Kevin Buzzard (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964317):
<p>When I realised I couldn't use id, I knew things might be bad</p>

#### [ Mario Carneiro (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964318):
<p>At the same time, you have already a robust language of restriction maps that you already know are functorial, because they are the object of study</p>

#### [ Kevin Buzzard (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964320):
<p>when I realised I could use res, I had some hope</p>

#### [ Mario Carneiro (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964321):
<p>the choice is obvious</p>

#### [ Kevin Buzzard (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964323):
<p>and then when gigantic one-page-long goals started yielding to refl I realised I'd had the right insight</p>

#### [ Kevin Buzzard (May 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964327):
<blockquote>
<p>the choice is obvious</p>
</blockquote>
<p>To you</p>

#### [ Kevin Buzzard (May 23 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964367):
<p>I would argue that the choice is not at all obvious to a practicing algebraic geometer trained in ZFC</p>

#### [ Kevin Buzzard (May 23 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964368):
<p>and in some sense this is a problem</p>

#### [ Kevin Buzzard (May 23 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964369):
<p>because it means that we are teaching people in slightly the wrong way</p>

#### [ Mario Carneiro (May 23 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964370):
<p>The important part is to recognize the issue itself</p>

#### [ Kevin Buzzard (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964376):
<p>As is so often the case (I have seen this time and time again in mathematics)</p>

#### [ Kevin Buzzard (May 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964382):
<p>the insight came to me ten minutes after I'd spent an hour being stuck and whining here about how stupid Lean was, and then turned off my laptop and thought about something else</p>

#### [ Kevin Buzzard (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964432):
<p>but I could _envisage_ situations where that bullet cannot be dodged and you have to take the hit and transport your structures</p>

#### [ Andrew Ashworth (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126964433):
<p>Did you get any insights with the ALEXANDRIA / Peter Koepke lecture person today?</p>

#### [ Kenny Lau (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126967797):
<p>I reached another milestone:</p>

#### [ Kenny Lau (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126967803):
<p><code>definition scheme_of_affine_scheme (R : Type u) [comm_ring R] : scheme := [definition which typechecks]</code></p>

#### [ Kenny Lau (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126967862):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (May 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126968834):
<p>So an affine scheme is one that is isomorphic to Spec(A) for some ring A</p>

#### [ Kenny Lau (May 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126968835):
<p>my question is: how important is that ring A?</p>

#### [ Johan Commelin (May 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969006):
<p>What do you mean? Whether you should carry A around?</p>

#### [ Johan Commelin (May 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969021):
<p>In <em>maths</em> it is not important at all. Only the fact that it exists</p>

#### [ Kenny Lau (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969044):
<p>I see</p>

#### [ Patrick Massot (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969051):
<p>I don't understand that question. You can recover A from its affine scheme, is that what you want to know?</p>

#### [ Kenny Lau (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969054):
<p>oh really</p>

#### [ Kenny Lau (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969056):
<p>is it just the global section?</p>

#### [ Kenny Lau (May 23 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969119):
<p>now a scheme is covered by affine schemes. Are the affine schemes important?</p>

#### [ Johan Commelin (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969162):
<p>Nope</p>

#### [ Johan Commelin (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969165):
<p>Only the existence</p>

#### [ Kenny Lau (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969166):
<p>interesting</p>

#### [ Johan Commelin (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969168):
<blockquote>
<p>is it just the global section?</p>
</blockquote>
<p>Yes, up to isomorphism</p>

#### [ Patrick Massot (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969169):
<p>Sure, global sections of the structure sheaf gives you back A</p>

#### [ Patrick Massot (May 23 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969172):
<p>Too late</p>

#### [ Johan Commelin (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969184):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> This what the Gamma-Spec adjunction is all about</p>

#### [ Johan Commelin (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969190):
<p>So, if you feel like writing an interface for schemes (-;</p>

#### [ Johan Commelin (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969196):
<p>That is what would be the first challenge</p>

#### [ Patrick Massot (May 23 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969247):
<p><a href="https://stacks.math.columbia.edu/tag/01I2" target="_blank" title="https://stacks.math.columbia.edu/tag/01I2">https://stacks.math.columbia.edu/tag/01I2</a></p>

#### [ Patrick Massot (May 23 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969260):
<p>Oh! The new Stacks project website went live!</p>

#### [ Kevin Buzzard (May 23 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969396):
<p>indeed</p>

#### [ Patrick Massot (May 23 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969798):
<p>Kevin, will you come to <a href="http://www.ihes.fr/~abbes/Gabber/gabber60-programme.html" target="_blank" title="http://www.ihes.fr/~abbes/Gabber/gabber60-programme.html">http://www.ihes.fr/~abbes/Gabber/gabber60-programme.html</a>?</p>

#### [ Kevin Buzzard (May 23 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/126969927):
<p>I wasn't planning on it. I just have too much on at the minute.</p>

#### [ Kenny Lau (May 28 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127201413):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> why are you using the broken definition of <code>basis</code> in <code>009I</code>?</p>

#### [ Kenny Lau (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127201813):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">presheaf_on_basis_stalk</span><span class="bp">.</span><span class="n">setoid</span>  <span class="o">:</span>
   <span class="n">setoid</span> <span class="o">(</span><span class="n">presheaf_on_basis_stalk</span><span class="bp">.</span><span class="n">aux</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Us</span> <span class="n">Vt</span><span class="o">,</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">W</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">Hx</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">W</span><span class="o">)</span> <span class="o">(</span><span class="n">BW</span> <span class="o">:</span> <span class="n">W</span> <span class="err">∈</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">HWU</span> <span class="o">:</span> <span class="n">W</span> <span class="err">⊆</span> <span class="n">Us</span><span class="bp">.</span><span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">HWV</span> <span class="o">:</span> <span class="n">W</span> <span class="err">⊆</span> <span class="n">Vt</span><span class="bp">.</span><span class="n">U</span><span class="o">),</span>
   <span class="n">FPTB</span><span class="bp">.</span><span class="n">res</span> <span class="n">Us</span><span class="bp">.</span><span class="n">BU</span> <span class="n">BW</span> <span class="n">HWU</span> <span class="n">Us</span><span class="bp">.</span><span class="n">s</span> <span class="bp">=</span> <span class="n">FPTB</span><span class="bp">.</span><span class="n">res</span> <span class="n">Vt</span><span class="bp">.</span><span class="n">BU</span> <span class="n">BW</span> <span class="n">HWV</span> <span class="n">Vt</span><span class="bp">.</span><span class="n">s</span><span class="o">,</span>
</pre></div>

#### [ Kenny Lau (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127201818):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> do you think we can change this definition to saying that they agree in the intersection?</p>

#### [ Kenny Lau (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127201822):
<p>oh no, we can't</p>

#### [ Kevin Buzzard (May 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202622):
<p>It was a real annoyance that the intersection of two basis elements was not a basis element</p>

#### [ Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202625):
<p>I proved several results under two additional hypotheses:</p>

#### [ Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202632):
<p>1) intersection of two basis elements was a basis element</p>

#### [ Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202633):
<p>2) intersection of no basis elemnts was a basis element</p>

#### [ Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202636):
<p>Both of these are true for the D_f basis of Spec(R)</p>

#### [ Kevin Buzzard (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202638):
<p>So in some cases I actually cut corners</p>

#### [ Kevin Buzzard (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202689):
<p>Kenny if you are sufficiently fanatical to go through those proofs and actually prove the correct statements then feel free</p>

#### [ Kevin Buzzard (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202702):
<p>Even the definition of a sheaf got so much more complicated when working with a basis not closed under intersection</p>

#### [ Kevin Buzzard (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202719):
<p>You have to check that the two functions are equal on the intersection by covering each intersection with new basis elements and checking that the res's coincide</p>

#### [ Kevin Buzzard (May 28 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202726):
<p>I just couldn't be bothered</p>

#### [ Kevin Buzzard (May 28 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202851):
<p>cf <a href="https://stacks.math.columbia.edu/tag/009L" target="_blank" title="https://stacks.math.columbia.edu/tag/009L">https://stacks.math.columbia.edu/tag/009L</a></p>

#### [ Kevin Buzzard (May 28 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202852):
<p>That's the tag I did</p>

#### [ Kevin Buzzard (May 28 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/affine%20schemes%20are%20schemes/near/127202880):
<p>not the one before</p>


{% endraw %}
