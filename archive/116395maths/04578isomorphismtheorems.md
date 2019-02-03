---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/04578isomorphismtheorems.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [isomorphism theorems](https://leanprover-community.github.io/archive/116395maths/04578isomorphismtheorems.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 03 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133249273):
<p>I need what is apparently called the "fourth isomorphism theorem" for R-modules, R a commutative ring. Of course more generally we will need all the isomorphism theorems for groups and R-modules, plus various extra bits and bobs. I might do some of this today in a coding session with the undergraduates. I propose doing the thing I actually want, which is that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> is a general ring (commutativity not necessary) and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span> is a sub-<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-module of the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>-module <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi></mrow><annotation encoding="application/x-tex">M</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span></span></span></span> then there's a canonical order-preserving bijection between submodules of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi><mi mathvariant="normal">/</mi><mi>N</mi></mrow><annotation encoding="application/x-tex">M/N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span> and submodules of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>M</mi></mrow><annotation encoding="application/x-tex">M</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">M</span></span></span></span> containing <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span>. My proposal is that I write this code at about 2pm today UK time so before then perhaps I should have a clue about the best way to say this. Here are some dumb questions.</p>
<p>The reason I want this is that I want that a quotient module of a Noetherian module is Noetherian. Because Noetherian modules are not yet in mathlib, but they are in mathlib-community, am I right in thinking I should be doing this work in a fork of the mathlib-community repo?</p>
<p>What should this file be called? <code>fourth_isomorphism_theorem.lean</code> sounds daft. Should it just be tagged onto quotient_module.lean in <code>linear_algebra</code>? I don't know how much more commutative algebra should up in this directory -- this stuff is not linear algebra any more.</p>
<p>Those of us who care about Galois insertions might now point out that the result I want is perhaps something to do with Galois insertions or Galois connections. Currently my instinct is to completely ignore all of this because I don't see what it buys us. I'd be interested in opinions. My proposal is to write an equiv between the type of submodules of M/N and the type of submodules of M containing N and then prove that it is order-preserving. Now my (good) understanding of <code>equiv</code> tells me exactly what I should be proving about the constructions. But my (poor) understanding of lattices doesn't tell me exactly what I should be proving about the order: I mean -- I know I should be proving that the constructions in each direction preserve inclusion, but should I be proving that some map is some morphism of lattices, or something? </p>
<p>My goal is that a quotient module of a Noetherian module is Noetherian, and I want the proof to be "this set is well-founded, by definition of Noetherian module, and hence this subset is well-founded, so we're done". What structures should I be using to formalise this statement in order for it to be mathlib-ready?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133253484):
<p>Gaargh. I've checked out the <code>noetherian</code> branch of community mathlib and it doesn't build. <code>order/conditionally_complete_lattice.lean</code> has a problem in line 128 for example: </p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">-Adding a point to a set preserves its boundedness above.-/</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">bdd_above_insert</span> <span class="o">:</span> <span class="n">bdd_above</span> <span class="o">(</span><span class="n">insert</span> <span class="n">a</span> <span class="n">s</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">bdd_above</span> <span class="n">s</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="k">show</span> <span class="n">bdd_above</span> <span class="o">(</span><span class="n">insert</span> <span class="n">a</span> <span class="n">s</span><span class="o">)</span> <span class="bp">→</span> <span class="n">bdd_above</span> <span class="n">s</span><span class="o">,</span> <span class="k">from</span> <span class="n">bdd_above_subset</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">),</span>
 <span class="k">show</span> <span class="n">bdd_above</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">bdd_above</span> <span class="o">(</span><span class="n">insert</span> <span class="n">a</span> <span class="n">s</span><span class="o">),</span> <span class="k">by</span> <span class="n">rw</span><span class="o">[</span><span class="n">insert_eq</span><span class="o">]</span><span class="bp">;</span> <span class="n">finish</span><span class="bp">⟩</span>
</pre></div>


<p>-&gt;</p>
<div class="codehilite"><pre><span></span>α : Type u,
_inst_1 : semilattice_sup α,
s : set α,
a : α
⊢ bdd_above s → bdd_above (insert a s)
conditionally_complete_lattice.lean:131:62: error

solve1 tactic failed, focused goal has not been solved
state:
α : Type u,
_inst_1 : semilattice_sup α,
s : set α,
a : α,
a_1 : bdd_above s,
a_2 : ¬bdd_above (insert a s)
⊢ false
</pre></div>


<p>(<code>finish</code> is failing). Is there an easy fix for this?</p>

#### [ Kenny Lau (Sep 03 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133253600):
<p><code>finish [bdd_above_insert]</code>?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133253683):
<p>but there are 100 errors</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133253685):
<p>so I'd rather find out what's going on</p>

#### [ Johan Commelin (Sep 03 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133253804):
<p>Maybe your <code>olean</code> files aren't matching with this branch? Did you try a recompile from scratch?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133253841):
<p>maybe I messed up. I thought I'd done exactly that</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133253870):
<p>I've removed all the olean files and am trying again</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133253923):
<p>Dumb question: if I clone a lean repo, make all the .olean files, and then checkout a different branch, do all the .olean files magically disappear?</p>

#### [ Johan Commelin (Sep 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254408):
<p>Nope. They are in <code>.gitignore</code>. So git doesn't touch them.</p>

#### [ Johannes Hölzl (Sep 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254454):
<p>Also, Lean should know which olean files to rebuild. But sometimes it happens that a olean file is flying around were the corresponding lean file was removed. This produces strange results sometimes...</p>

#### [ Johan Commelin (Sep 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254456):
<p>So if you are on a very recent <code>mathlib:master</code>, and you've built. Then you checkout <code>noetherian</code> which is a couple of days old, then you get <code>olean</code>-files that are too new.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254459):
<p>no there are still errors.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254464):
<p>I removed all .olean files and the noetherian branch does not compile. Is this to do with "This branch is 2 commits ahead, 37 commits behind leanprover:master."?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254469):
<p>Is there a magic merge type command I can type to rebase or whatever the right word is?</p>

#### [ Johan Commelin (Sep 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254480):
<p>With <code>noetherian</code> checked out, you could try <code>git merge master</code>.</p>

#### [ Johan Commelin (Sep 03 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254519):
<p>There shouldn't be any conflicts.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254531):
<p><code>git merge master</code> reports <code>already up to date</code> and nothing seemed to happen.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254533):
<p>It would be really nice to get a working <code>noetherian.lean</code> by 2pm</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254547):
<p>I can happily dump the entire repo and clone again.</p>

#### [ Johan Commelin (Sep 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254553):
<p>Give me 2 minutes</p>

#### [ Johan Commelin (Sep 03 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254638):
<div class="codehilite"><pre><span></span>git checkout master
git pull
git checkout noetherian
git merge master
git push origin noetherian
</pre></div>

#### [ Johan Commelin (Sep 03 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254646):
<p>Can you checkout <code>noetherian</code> and <code>git pull origin noetherian</code>?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254687):
<p>I'm building using <code>nightly-2018-06-21</code>. Is this an issue?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254693):
<p>I just cloned again from github</p>

#### [ Johan Commelin (Sep 03 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254704):
<p>I'll also rebuild. But this machine is not the fastest in the world.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254881):
<p>Will switching lean version change the behaviour of <code>finish</code>?</p>

#### [ Johan Commelin (Sep 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254935):
<p>I'm glad your version of 2pm is still 90 minutes away...</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254941):
<p>Oh!</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254944):
<p>I might have found my erro</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254945):
<p>r</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133254968):
<p>I think I just don't understand branches. Maybe I thought I had pulled but I hadn't pulled.</p>

#### [ Johan Commelin (Sep 03 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255015):
<p>Does my little log of shell commands make sense to you?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255019):
<p>I just cloned the repo again</p>

#### [ Johan Commelin (Sep 03 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255040):
<p>I pushed a commit that merges the latest master into <code>noetherian</code></p>

#### [ Johan Commelin (Sep 03 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255302):
<p>Woohow... I'm also getting boatloads of errors.</p>

#### [ Johan Commelin (Sep 03 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255308):
<p>Did I break the system?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255417):
<p>which version of Lean are you using?</p>

#### [ Johan Commelin (Sep 03 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255438):
<p>Whatever <code>elan</code> gave me. I think/hope the most recent. Let me check.</p>

#### [ Johan Commelin (Sep 03 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255457):
<p><code>Lean (version 3.4.1, commit 17fe3decaf8a, Release)</code></p>

#### [ Johan Commelin (Sep 03 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255549):
<p>Everything is complaining that <code>data/set/basic.lean</code> uses sorry.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255648):
<p>so <code>data/set/basic.lean</code> works fine in regular mathlib but I have an error in community mathlib</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255745):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">insert_diff_singleton</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">insert</span> <span class="n">a</span> <span class="o">(</span><span class="n">s</span> <span class="err">\</span> <span class="o">{</span><span class="n">a</span><span class="o">})</span> <span class="bp">=</span> <span class="n">insert</span> <span class="n">a</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">insert_eq</span><span class="o">,</span> <span class="n">union_diff_self</span><span class="o">]</span>
</pre></div>


<p>takes an age to compile and then I get a deterministic time-out</p>

#### [ Johannes Hölzl (Sep 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133255803):
<p>what does <code>git status</code> say? Are there any changed files?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256008):
<p>I only just cloned</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256024):
<div class="codehilite"><pre><span></span><span class="n">buzzard</span><span class="bp">@</span><span class="n">ebony</span><span class="o">:</span><span class="bp">~/</span><span class="n">lean</span><span class="bp">-</span><span class="n">projects</span><span class="bp">/</span><span class="n">mathlib</span><span class="bp">-</span><span class="n">community</span><span class="err">$</span> <span class="n">git</span> <span class="n">status</span>
<span class="n">On</span> <span class="n">branch</span> <span class="n">noetherian</span>
<span class="n">Your</span> <span class="n">branch</span> <span class="n">is</span> <span class="n">up</span><span class="bp">-</span><span class="n">to</span><span class="bp">-</span><span class="n">date</span> <span class="k">with</span> <span class="err">&#39;</span><span class="n">origin</span><span class="bp">/</span><span class="n">noetherian&#39;</span><span class="bp">.</span>
<span class="n">nothing</span> <span class="n">to</span> <span class="n">commit</span><span class="o">,</span> <span class="n">working</span> <span class="n">directory</span> <span class="n">clean</span>
<span class="n">buzzard</span><span class="bp">@</span><span class="n">ebony</span><span class="o">:</span><span class="bp">~/</span><span class="n">lean</span><span class="bp">-</span><span class="n">projects</span><span class="bp">/</span><span class="n">mathlib</span><span class="bp">-</span><span class="n">community</span><span class="err">$</span>
</pre></div>

#### [ Johan Commelin (Sep 03 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256027):
<p>The latest commit on the <code>noetherian</code> branch is a merging in <code>master</code>. I just did that.</p>

#### [ Scott Morrison (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256033):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, rebasing might have been better than merging. :-) (Says someone who only learnt to rebase last week.)</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256073):
<p>The issue existed before the merge</p>

#### [ Scott Morrison (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256076):
<p>I noticed the noetherian branch was broken, too.</p>

#### [ Scott Morrison (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256079):
<p>Sorry, should have said something!</p>

#### [ Kevin Buzzard (Sep 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256096):
<p>is the master branch broken?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256224):
<p>[of community-mathlib]</p>

#### [ Scott Morrison (Sep 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256260):
<p>no, it's good</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256280):
<p>which version of Lean are you using?</p>

#### [ Scott Morrison (Sep 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256283):
<p>I'm guessing the culprit is Mario's changes data/set/basic</p>

#### [ Scott Morrison (Sep 03 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256361):
<p>What are these "versions" of which you speak? I use elan, so running lean automatically runs whichever version each respository says it needs. :-)</p>

#### [ Scott Morrison (Sep 03 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256378):
<p>Looking at the leanpkg.toml for mathlib, that's 3.4.1</p>

#### [ Johan Commelin (Sep 03 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256482):
<p>Ok, what should we do?</p>

#### [ Johan Commelin (Sep 03 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256491):
<p>Can we still rebase?</p>

#### [ Johan Commelin (Sep 03 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256511):
<p>Then we can use a built latest master branch, and look at the 5 changes or so, that are introduced by noetherian</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256573):
<p>Oh I can work around this, I don't need it to compile. I will just work with mathlib master and not use the Noetherian branch.</p>

#### [ Johan Commelin (Sep 03 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256588):
<p>Sure, but you want to work on noetherian modules, right?</p>

#### [ Johan Commelin (Sep 03 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256596):
<p>So you want the TFAE theorem</p>

#### [ Johan Commelin (Sep 03 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256616):
<p>And that is on the noetherian branch, and it depends on changes to <code>data/set/basic.lean</code> that seem to cause wreckage.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256624):
<p>right</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256675):
<p>so I'll just not have noetherian modules and I can still do the thing I was planning on doing, which was proving the 4th isomorphism theorem for R-modules</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256678):
<p>we just don't get the application</p>

#### [ Johan Commelin (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256680):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="110524">@Scott Morrison</span> would it be ok to rewrite history on this branch?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256690):
<p>It's OK, I have changed my plans</p>

#### [ Scott Morrison (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256691):
<p>fine with me :-)</p>

#### [ Johan Commelin (Sep 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256706):
<p>And you don't get the lattice structure and all the other foundational stuff that Mario did.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256717):
<p>I don't need this stuff right now</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256723):
<p>I just need it at some point</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256725):
<p>it's no longer time-critical</p>

#### [ Johannes Hölzl (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256729):
<p>Should I rebase it?</p>

#### [ Johan Commelin (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256735):
<p>Yes please.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256736):
<p>I don't mind either way</p>

#### [ Johan Commelin (Sep 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133256739):
<p>Throw away my merge commit.</p>

#### [ Johannes Hölzl (Sep 03 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133257077):
<p>just a second I need to fix some stuff which broke by Marios <code>data/set/basic.lean</code> changes</p>

#### [ Johannes Hölzl (Sep 03 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133257831):
<p><code>noetherian</code> is now rebased and fixes the problems with the simp set. But maybe we just shouldn't add <code>singleton_union</code> and <code>union_singleton</code> to the simp set...</p>

#### [ Johan Commelin (Sep 03 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133258618):
<p>Thanks a lot!</p>

#### [ Johan Commelin (Sep 03 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133258637):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> A fresh clone should repair your issues.</p>

#### [ Kenny Lau (Sep 03 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133258753):
<p><em>A clone of Kevin Buzzard arrives with a wrench</em></p>

#### [ Johan Commelin (Sep 03 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133266146):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> What did you end up doing?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133267878):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">quotient_module</span>

<span class="kn">open</span> <span class="n">is_submodule</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">quotient_rel</span>

<span class="kn">definition</span> <span class="n">module</span><span class="bp">.</span><span class="n">correspondence_theorem</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span>
  <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">M</span><span class="o">)</span> <span class="o">[</span><span class="n">is_submodule</span> <span class="n">N</span><span class="o">]</span> <span class="o">:</span>
<span class="o">{</span><span class="n">Xbar</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="bp">//</span> <span class="n">is_submodule</span> <span class="n">Xbar</span><span class="o">}</span> <span class="err">≃</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">set</span> <span class="n">M</span> <span class="bp">//</span> <span class="n">is_submodule</span> <span class="n">X</span> <span class="bp">∧</span> <span class="n">N</span> <span class="err">⊆</span> <span class="n">X</span><span class="o">}</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Xbar</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">Xbar</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="bp">⟨</span>
    <span class="bp">@@</span><span class="n">is_submodule</span><span class="bp">.</span><span class="n">preimage</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">Xbar</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_</span> <span class="o">(</span><span class="n">is_linear_map_quotient_mk</span> <span class="n">N</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span><span class="k">begin</span>
      <span class="k">show</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="n">n</span> <span class="err">∈</span> <span class="n">Xbar</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
      <span class="k">have</span> <span class="o">:</span> <span class="err">⟦</span><span class="n">n</span><span class="err">⟧</span> <span class="bp">=</span> <span class="err">⟦</span><span class="mi">0</span><span class="err">⟧</span><span class="o">,</span>
        <span class="n">apply</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span><span class="o">,</span>
        <span class="k">show</span> <span class="n">n</span> <span class="bp">-</span> <span class="mi">0</span> <span class="err">∈</span> <span class="n">N</span><span class="o">,</span>
        <span class="n">simpa</span><span class="o">,</span>
      <span class="n">rw</span> <span class="n">this</span><span class="o">,</span>
      <span class="n">haveI</span> <span class="o">:=</span> <span class="n">Xbar</span><span class="bp">.</span><span class="n">property</span><span class="o">,</span>
      <span class="k">show</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="err">∈</span> <span class="n">Xbar</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
      <span class="n">exact</span> <span class="bp">@</span><span class="n">is_submodule</span><span class="bp">.</span><span class="n">zero</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">Xbar</span><span class="bp">.</span><span class="n">val</span> <span class="bp">_</span><span class="o">,</span>
<span class="kn">end</span><span class="bp">⟩⟩</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="bp">⟨</span><span class="o">((</span><span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="err">&#39;&#39;</span> <span class="n">X</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">)),</span>
    <span class="k">by</span> <span class="n">haveI</span> <span class="o">:=</span> <span class="n">X</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">is_submodule</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="n">is_linear_map_quotient_mk</span> <span class="n">N</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">Pbar</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span><span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">set</span><span class="bp">.</span><span class="n">image_preimage_eq</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">exists_rep</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">P</span><span class="o">,</span><span class="n">HP</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span><span class="bp">⟨</span><span class="k">begin</span>
    <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">M</span><span class="o">),</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">P</span> <span class="bp">∧</span> <span class="n">y</span> <span class="bp">≈</span> <span class="n">x</span><span class="o">,</span>
      <span class="n">simpa</span> <span class="kn">using</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">rcases</span> <span class="n">H2</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span><span class="n">H3</span><span class="o">,</span><span class="n">H4</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">quotient_rel_eq</span> <span class="n">at</span> <span class="n">H4</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H5</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">-</span> <span class="o">(</span><span class="n">y</span> <span class="bp">-</span> <span class="n">x</span><span class="o">)</span> <span class="err">∈</span> <span class="n">P</span><span class="o">,</span>
      <span class="n">refine</span> <span class="bp">@</span><span class="n">is_submodule</span><span class="bp">.</span><span class="n">sub</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">HP</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H3</span> <span class="bp">_</span><span class="o">,</span> <span class="c1">-- fixing type class inference issues</span>
      <span class="n">exact</span> <span class="n">HP</span><span class="bp">.</span><span class="mi">2</span> <span class="n">H4</span><span class="o">,</span> <span class="c1">-- goal still x ∈ P.val, but H5 is y - (y - x) ∈ P.val</span>
    <span class="n">convert</span> <span class="n">H5</span><span class="o">,</span> <span class="c1">-- goal is now x = y - (y - x)</span>
    <span class="n">simp</span><span class="o">,</span> <span class="c1">-- solves this</span>
  <span class="kn">end</span>
  <span class="o">,</span><span class="k">by</span> <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset_preimage_image</span><span class="bp">⟩</span><span class="o">,</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Sep 03 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133267879):
<p>4th isomorphism theorem!</p>

#### [ Kevin Buzzard (Sep 03 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133267919):
<p>I spent about an hour talking about the mathematics (some of the audience had not seen quotient groups before) and then about an hour writing the code, although I would never have done it if Chris hadn't shown up and occasionally made comments like "oh you need to put <code>local attribute [instance] quotient_rel</code>".</p>

#### [ Kevin Buzzard (Sep 03 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133267998):
<p>It's only a bijection between the sets, but checking that it's inclusion-preserving will be trivial because this is just a diagram chase using functions, not using the module properties at all. Note the excessive number of <code>@</code>s in the proof; this is apparently (according to <span class="user-mention" data-user-id="110044">@Chris Hughes</span> ) because Chris has figured out how to make type class inference work OK for quotient structures, but quotient modules haven't been through his filter yet.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133268001):
<p>Chris -- what needs doing?</p>

#### [ Johan Commelin (Sep 03 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133268214):
<p>Ok, that's really cool! So this was basically a very successful live Lean coding session in front of students!</p>

#### [ Kevin Buzzard (Sep 03 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133268371):
<p><code>to_fun</code> was particularly painful. There are tricks here which would have made my life a lot easier, someone just needs to take the tricks from quotient groups and apply them here.</p>

#### [ Johan Commelin (Sep 03 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133268612):
<p>So, how far are we from showing that quotient of Noetherian is Noetherian?</p>

#### [ Johan Commelin (Sep 03 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133268620):
<p>By now it is math-trivial...</p>

#### [ Johan Commelin (Sep 03 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133268689):
<p>But in Lean? We need that a suitable sublattice of a well-founded lattice is well-founded. And we need to glue everything.</p>

#### [ Chris Hughes (Sep 03 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133268697):
<p>Very easy. I think it's just an application of <code>inv_image_wf</code> with the isomorphism.</p>

#### [ Chris Hughes (Sep 03 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133268722):
<p>But you also need <code>S \sub T \iff f S \sub f T</code></p>

#### [ Kevin Buzzard (Sep 03 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133269273):
<p>I'm just doing that now. I just used <code>tidy</code> for the first time <span class="emoji emoji-1f600" title="grinning">:grinning:</span></p>

#### [ Kevin Buzzard (Sep 03 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133269333):
<p>In fact both inclusions are <code>by tidy</code></p>

#### [ Kevin Buzzard (Sep 03 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133271268):
<p>OK dumb question: where is the construction which gives a module from a submodule?</p>

#### [ Johan Commelin (Sep 03 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133271286):
<p><a href="https://github.com/leanprover/mathlib/blob/master/linear_algebra/subtype_module.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/linear_algebra/subtype_module.lean">https://github.com/leanprover/mathlib/blob/master/linear_algebra/subtype_module.lean</a></p>

#### [ Kevin Buzzard (Sep 03 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133271296):
<p>Thanks.</p>

#### [ Johan Commelin (Sep 03 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133271342):
<p>This could potentially be <code>subtype_instance</code>d</p>

#### [ Kevin Buzzard (Sep 03 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133271824):
<p>so now I find myself proving that a submodule of a submodule is a submodule :-/</p>

#### [ Johan Commelin (Sep 03 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133271968):
<p>Yes... that is really annoying.</p>

#### [ Johan Commelin (Sep 03 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133272026):
<p>In the end we'll want some lattice inclusion for that part of the story as well. And it seems you are already proving it.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133275777):
<p>tidy is just pwning a lot of these goals. It's just a lot of chasing trivialities around and perhaps tidy is just the thing for it.</p>

#### [ Kevin Buzzard (Sep 03 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133275793):
<p>Yes, my goal before I go to bed today is to prove that submodules and quotient modules of Noetherian modules are Noetherian.</p>

#### [ Johan Commelin (Sep 03 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133275837):
<p>Do you check what kind of proofs <code>tidy</code> generates? Or do you just write <code>by tidy</code> and move on?</p>

#### [ Kevin Buzzard (Sep 03 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133277571):
<p>I write <code>by tidy</code> and then observe that in contrast to Scott I am unable to immediately see what proofs it generates, so I am forced to move on.</p>

#### [ Patrick Massot (Sep 03 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133277630):
<p>you could use the hole command to see what it does</p>

#### [ Kevin Buzzard (Sep 03 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133278197):
<p>I need some advice. I have <code>f : equiv X Y</code> between two types both of which have <code>`le</code>. I have proved a &lt;= b -&gt; f a &lt;= f b<code> and </code>c &lt;= d -&gt; f.symm c &lt;= f.symm d<code> (so f is an equivalence of preorders). I now want to deduce </code>a  &lt; b &lt;-&gt; f a &lt; f b` and I just wrote a boring proof of this. I feel like I'm missing some trick.</p>

#### [ Chris Hughes (Sep 03 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133278580):
<p>This is the least boring proof I could come up with</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">β</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">b</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hf&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">f</span><span class="bp">.</span><span class="n">symm</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="bp">↔</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">f</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">have</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">↔</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">b</span><span class="o">,</span> <span class="k">from</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span>
<span class="bp">⟨</span><span class="n">hf</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">inverse_apply_apply</span> <span class="n">f</span> <span class="n">a</span><span class="o">,</span> <span class="err">←</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">inverse_apply_apply</span> <span class="n">f</span> <span class="n">b</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="n">hf&#39;</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">b</span><span class="o">)</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">lt_iff_le_not_le</span><span class="o">,</span> <span class="n">this</span><span class="o">]</span>
</pre></div>

#### [ Kevin Buzzard (Sep 03 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133279287):
<p>I am wondering now if this proof should be generated by a tactic. I have beefed up my f to an equivalence of sets-equipped-with-le and then anything that I can define in a reasonable way just using le should be the same on both sides.</p>

#### [ Mario Carneiro (Sep 04 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133280969):
<p>You should use the theorems about order isomorphisms</p>

#### [ Kevin Buzzard (Sep 04 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133281184):
<p>right.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133281198):
<p>I am drowning in trivialities, switching between your <code>is_submodule M</code>, the subtype <code>{X : set M // is_submodule X}</code>, and related subtypes such as <code>{X : set M // is_submodule X \and X \sub N}</code>.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133281203):
<p>furthermore there is a hot tub full of teenage girls about 10 metres from me and they're getting really loud</p>

#### [ Kevin Buzzard (Sep 04 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133281245):
<p>I think it might be about time to tell my daughter to quieten down a bit. I can't really think straight any more</p>

#### [ Kevin Buzzard (Sep 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133298907):
<p>OK sanity restored (they're all asleep). <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> or <span class="user-mention" data-user-id="110031">@Patrick Massot</span>  I need advice -- mostly about management of code . I have proved subs of Noeth mods are Noeth and I have essentially proved quotients of Noeth mods are Noeth. Currently the proofs are horrible, it was getting harder and harder to work last night and some lemmas are called <code>temp_name</code> etc so I don't even feel it's ready to PR. But I have momentum and I'd like to finish the job. Currently in the <code>noetherian</code> branch of community mathlib (which I am actively working on) there's a bunch of stuff at the beginning of <code>noetherian.lean</code> which Mario wrote and which has nothing to do with Noetherian stuff -- it sets up a new type <code>submodule R M</code> which is the R-submodules of the R-module M. Mario set it up as a structure but it has precisely the structure of a subtype, it's the subsets of M with some property. The...whatever they're called...are called <code>N.s</code> (the subset) and <code>N.sub</code> (the proof it's a submodule) rather than <code>N.val</code> and <code>N.property</code>. Which is preferable and why? I propose moving this stuff somewhere else, because I want to use this language in the correspondence theorem. The proof that subquotients of Noetherian things are Noetherian naturally uses this submodule lattice all over the place but I want to use the same language for the correspondence theorem. Currently I've moved the definition of submodule to <code>submodule.lean</code> in <code>linear_algebra</code> even though it's not linear algebra in my opinion -- this is absolutely commutative ring theory. My main organisational problem is that I now want to prove things like "there's an injective map <code>submodule R (quotient M N) -&gt; submodule R M</code> which I've proved in some sense -- I have a Lean theorem saying some interpretation of this -- but I am convinced I'm not using the right language. Mario proved <code>submodule R M</code> (see how much easier it is to understand if you use maths notation rather than alpha beta?) is a partial order so now I seem to want to prove theorems about order embeddings, and use the fact that if <code>X -&gt; Y</code> is an order embedding then the order on <code>X</code> is induced from the order of <code>Y</code> somehow. Where do I look for this theorem and the relevant definitions -- are these theorems about orders, or semi-bot-sup-lattices, or what? Should this go into yet another file, called <code>submodule_order.lean</code> or does it all go in <code>submodule.lean</code> -- should this file be in ring theory or linear algebra, etc etc? </p>
<p>What I'm trying to say is: the maths is now in Lean, but it's not in a good state. When I was writing the schemes repo I would just dump it all in and move on. But Scott and others have convinced me that this is not a good long term plan, so I now want to spend just an hour or two making it as mathlib-ready as I can before actually PR'ing it. If anyone has any comments on (a) the merits of creating random new files like submodule.lean and where they should go or (b) the abstract theorem I should be proving about the relationship between the partial orders <code>submodule R (quotient M N)</code> and <code>submodule R M</code> (there's an injective map from the left to the right which preserves the order relation; this must already be a concept in Lean) then I'd be grateful to hear them. I am reluctant to put any more commutative ring theory into <code>linear_algebra</code> by the way.</p>

#### [ Kenny Lau (Sep 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133298942):
<p>did you sleep?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133298951):
<p>I did. The joys of earplugs.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133298957):
<p>I've just spent 2 hours tidying up though</p>

#### [ Kevin Buzzard (Sep 04 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133299046):
<p>Kenny do you know what kind of Lean structure I have? I have two partial orders X and Y, an injection X -&gt; Y, and a proof that a &lt;= b iff f a &lt;= f b. Furthermore (although I don't know if this is relevant) if f a &lt;= d &lt;= f b then there exists c such that f c = d.</p>

#### [ Kenny Lau (Sep 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133299103):
<p>I don't even know what kind of mathematical structure you have</p>

#### [ Patrick Massot (Sep 04 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133299133):
<p>Do you know about <a href="https://github.com/leanprover/mathlib/blob/master/order/order_iso.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/order/order_iso.lean">https://github.com/leanprover/mathlib/blob/master/order/order_iso.lean</a>?</p>

#### [ Patrick Massot (Sep 04 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133299204):
<p>It seems to be exactly the file you want</p>

#### [ Kevin Buzzard (Sep 04 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133299219):
<p>right -- thanks. I've never looked at that file I don't think. This is exactly why I asked here :-)</p>

#### [ Kevin Buzzard (Sep 04 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133299231):
<p>Aah so that's the meaning of the symbol <code>≼o</code> which I've seen several times before :-)</p>

#### [ Scott Morrison (Sep 04 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133299325):
<p>Your PR should also certainly create a whole new folder <code>commutative_algebra</code>. It's time!</p>

#### [ Kevin Buzzard (Sep 04 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133299632):
<p>Thanks Scott. OK so current proposal: new directory <code>commutative_algebra</code>, move file <code>noetherian.lean</code> into it, leave current files about modules where they are, nonsense about order embeddings in a file called something like <code>module_order.lean</code>(is this a bad name?) perhaps in ring_theory (because this part works for general rings), and now short proofs that subquotients of Noetherian modules are Noetherian ends up in Noetherian.lean. Hmm. Maybe even this part should be done for general rings; the theory very quickly becomes a commutative-ring-only theory, but this very basic part seems to work in general (we are doing "Noetherian left modules" I suspect, but I don't think it's an unreasonable convention to have "all modules over a non-comm ring, if not stated otherwise, are left modules" -- I think that's the current convention anyway.</p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396163):
<p>The 4th isomorphism theorem needed some rewriting after Chris' changes to quotient modules. What is really striking now is that the theorem is still pretty much the same, but the <em>complete</em> proof that the correspondence is order-preserving is <code>by tidy</code>. Commutative algebra comes with a whole bunch of diagram chases and my intial impression is that <code>tidy</code> seems like it will be a really useful tool. I don't know if Mario is worried that compile times will go through the roof though...</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">submodule</span>
<span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">quotient_module</span> <span class="c1">-- I propose moving this to ring_theory</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tidy</span>
<span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">order_iso</span>

<span class="kn">open</span> <span class="n">is_submodule</span>
<span class="kn">open</span> <span class="n">quotient_module</span>

<span class="kn">definition</span> <span class="n">module</span><span class="bp">.</span><span class="n">correspondence_equiv</span> <span class="o">(</span><span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span><span class="o">)</span> <span class="o">[</span><span class="n">module</span> <span class="n">R</span> <span class="n">M</span><span class="o">]</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="n">set</span> <span class="n">M</span><span class="o">)</span> <span class="o">[</span><span class="n">is_submodule</span> <span class="n">N</span><span class="o">]</span> <span class="o">:</span>
<span class="o">(</span><span class="n">has_le</span><span class="bp">.</span><span class="n">le</span> <span class="o">:</span> <span class="n">submodule</span> <span class="n">R</span> <span class="o">(</span><span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="bp">→</span> <span class="n">submodule</span> <span class="n">R</span> <span class="o">(</span><span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="err">≃</span><span class="n">o</span>
<span class="o">(</span><span class="n">has_le</span><span class="bp">.</span><span class="n">le</span> <span class="o">:</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">submodule</span> <span class="n">R</span> <span class="n">M</span> <span class="bp">//</span> <span class="n">N</span> <span class="err">⊆</span> <span class="n">X</span><span class="o">}</span> <span class="bp">→</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">submodule</span> <span class="n">R</span> <span class="n">M</span> <span class="bp">//</span> <span class="n">N</span> <span class="err">⊆</span> <span class="n">X</span><span class="o">}</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Xbar</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">submodule</span><span class="bp">.</span><span class="n">pullback</span> <span class="o">(</span><span class="n">mk</span> <span class="o">:</span> <span class="n">M</span> <span class="bp">→</span> <span class="o">(</span><span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">))</span>
    <span class="o">(</span><span class="n">is_linear_map_quotient_mk</span> <span class="n">N</span><span class="o">)</span> <span class="n">Xbar</span><span class="o">,</span><span class="bp">λ</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span><span class="k">begin</span>
      <span class="k">show</span> <span class="err">↑</span><span class="n">n</span> <span class="err">∈</span> <span class="n">Xbar</span><span class="bp">.</span><span class="n">s</span><span class="o">,</span>
      <span class="n">haveI</span> <span class="o">:=</span> <span class="n">Xbar</span><span class="bp">.</span><span class="n">sub</span><span class="o">,</span>
      <span class="k">have</span> <span class="o">:</span> <span class="o">((</span><span class="mi">0</span> <span class="o">:</span> <span class="n">M</span><span class="o">)</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="err">∈</span> <span class="n">Xbar</span><span class="bp">.</span><span class="n">s</span><span class="o">,</span>
        <span class="n">exact</span> <span class="bp">@</span><span class="n">is_submodule</span><span class="bp">.</span><span class="n">zero</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">Xbar</span><span class="bp">.</span><span class="n">s</span> <span class="bp">_</span><span class="o">,</span>
      <span class="n">suffices</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">M</span><span class="o">),</span>
        <span class="n">rwa</span> <span class="n">this</span><span class="o">,</span>
      <span class="n">rw</span> <span class="n">quotient_module</span><span class="bp">.</span><span class="n">eq</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">Hn</span><span class="o">],</span>
    <span class="kn">end</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="n">submodule</span><span class="bp">.</span><span class="n">pushforward</span> <span class="n">mk</span> <span class="o">(</span><span class="n">is_linear_map_quotient_mk</span> <span class="n">N</span><span class="o">)</span> <span class="n">X</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">P</span><span class="o">,</span> <span class="n">submodule</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">set</span><span class="bp">.</span><span class="n">image_preimage_eq</span> <span class="n">quotient_module</span><span class="bp">.</span><span class="n">quotient</span><span class="bp">.</span><span class="n">exists_rep</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">P</span><span class="o">,</span><span class="n">HP</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="k">begin</span>
    <span class="k">show</span> <span class="n">submodule</span><span class="bp">.</span><span class="n">pullback</span> <span class="n">mk</span> <span class="bp">_</span> <span class="o">(</span><span class="n">submodule</span><span class="bp">.</span><span class="n">pushforward</span> <span class="n">mk</span> <span class="bp">_</span> <span class="n">P</span><span class="o">)</span> <span class="bp">=</span> <span class="n">P</span><span class="o">,</span>
    <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">split</span><span class="o">,</span><span class="n">swap</span><span class="o">,</span><span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset_preimage_image</span><span class="o">,</span>
    <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span><span class="n">Hy</span><span class="o">,</span><span class="n">Hyx</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">change</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">quotient</span> <span class="n">M</span> <span class="n">N</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span> <span class="n">at</span> <span class="n">Hyx</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">quotient_module</span><span class="bp">.</span><span class="n">eq</span> <span class="n">at</span> <span class="n">Hyx</span><span class="o">,</span>
    <span class="n">suffices</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">-</span> <span class="o">(</span><span class="n">y</span> <span class="bp">-</span> <span class="n">x</span><span class="o">)</span> <span class="err">∈</span> <span class="n">P</span><span class="o">,</span>
      <span class="n">simpa</span><span class="o">,</span>
    <span class="n">haveI</span> <span class="o">:=</span> <span class="n">P</span><span class="bp">.</span><span class="n">sub</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">is_submodule</span><span class="bp">.</span><span class="n">sub</span> <span class="n">Hy</span> <span class="o">(</span><span class="n">HP</span> <span class="n">Hyx</span><span class="o">),</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">ord</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span><span class="o">,</span> <span class="c1">-- I love you Scott Morrison</span>
<span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Sep 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396242):
<p>Well, <code>tidy</code> can also tell you the proof. That will shave a bit of time off future compiles.</p>

#### [ Johan Commelin (Sep 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396246):
<p>Use the hole command, Luke!</p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396341):
<p><code>  ord := begin intros a b, dsimp at *, simp at *, fsplit, work_on_goal 0 { intros a_1 a_2 a_3, simp at *, solve_by_elim }, intros a_1 a_2 a_3, induction a_2, work_on_goal 0 { simp at *, solve_by_elim }, refl end, -- I love you Scott Morrison</code></p>

#### [ Kevin Buzzard (Sep 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396363):
<p>Should I use that proof instead? I am tempted to change the comment to "this proof brought to you by tidy"</p>

#### [ Patrick Massot (Sep 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396406):
<p>I don't think we want that kind of proof in mathlib</p>

#### [ Patrick Massot (Sep 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396410):
<p>But it should be very easy to clean</p>

#### [ Patrick Massot (Sep 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396471):
<p>or else you can leave <code>by tidy</code></p>

#### [ Patrick Massot (Sep 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396481):
<p>we already have proofs by tidy (somewhat hidden by autoparam)</p>

#### [ Johan Commelin (Sep 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396482):
<p>If you leave <code>tidy</code> there, what does the profiler say?</p>

#### [ Johan Commelin (Sep 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396489):
<p>I guess it is pretty fast.</p>

#### [ Johan Commelin (Sep 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/isomorphism%20theorems/near/133396503):
<p>And the proof looks a lot more readable to me if it is just <code>tidy</code> (-;</p>


{% endraw %}
