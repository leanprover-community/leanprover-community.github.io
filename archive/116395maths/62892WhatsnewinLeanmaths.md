---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62892WhatsnewinLeanmaths.html
---

## Stream: [maths](index.html)
### Topic: [What's new in Lean maths?](62892WhatsnewinLeanmaths.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 09 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133605485):
<p>This thread is for people to occasionally announce or flag code which they or others have written, which is publically available, finished / usable, and which might be of general use or interest to the lean community. I'm starting it because I find looking through mathlib commits confusing and time-consuming, and because there are things which are happening other than mathlib commits.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133605676):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> has proved quadratic reciprocity! This is a bit of a milestone because all proofs have some sort of a combinatorial / counting nature to them, and manipulating finite sets, whilst second nature to mathematicians, can be quite tough in Lean. The PR is still open; it's <a href="https://github.com/leanprover/mathlib/pull/327" target="_blank" title="https://github.com/leanprover/mathlib/pull/327">https://github.com/leanprover/mathlib/pull/327</a> . There's a bunch of other stuff too -- Fermat's Little Theorem, Wilson's Theorem, the Legendre symbol of course, multiplicative group of a finite field is cyclic and so on. This PR covers a serious chunk of the third year basic number theory course at Imperial College London.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133605778):
<p>On a rather more mundane note, work of several people at <a href="https://github.com/leanprover/mathlib/commit/4421f46dc2e0ec818344bcd897c1ee75ff82cbad" target="_blank" title="https://github.com/leanprover/mathlib/commit/4421f46dc2e0ec818344bcd897c1ee75ff82cbad">https://github.com/leanprover/mathlib/commit/4421f46dc2e0ec818344bcd897c1ee75ff82cbad</a> and <a href="https://github.com/leanprover/mathlib/commit/085c0125015c29058ce5a418e88a791cb232ee4b" target="_blank" title="https://github.com/leanprover/mathlib/commit/085c0125015c29058ce5a418e88a791cb232ee4b">https://github.com/leanprover/mathlib/commit/085c0125015c29058ce5a418e88a791cb232ee4b</a> has given us the fact that submodules of the quotient module <code>M/N</code>biject with submodules of <code>M</code> containing <code>N</code> and we now also have basic definitions of Noetherian modules plus proofs that submodules and quotient modules of Noetherian modules are Noetherian.</p>

#### [ Johannes Hölzl (Sep 09 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133606251):
<ul>
<li><code>rcases</code> (and hence <code>rintros</code>) supports now also quotient types. This allows one to write <code>by rintro ⟨a⟩ ⟨b⟩; exact ...</code> instead of a sequence of <code>quotient.induction_on</code></li>
<li>(small change) more uniform naming <code>filter.vmap</code> is now <code>filter.comap</code></li>
<li>we have our first concrete categories in Lean: <code>CommRing</code>, <code>Top</code>, and <code>Meas</code>! Due to <span class="user-mention" data-user-id="110524">@Scott Morrison</span> and <span class="user-mention" data-user-id="110032">@Reid Barton</span></li>
</ul>

#### [ Patrick Massot (Sep 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133620485):
<p>I think this thread is a very good idea. But we shouldn't forget to update documentation as well. Do we have an example of <code>rcases</code> using quotients in the tactic doc? I guess the quadratic reciprocity stuff should be mentioned in the theories folder of documentation</p>

#### [ Patrick Massot (Sep 09 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133620495):
<p>It seems <a href="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md">https://github.com/leanprover/mathlib/blob/master/docs/tactics.md</a> mentions quotients but there are not so many examples there</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133625180):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- `filter [t1, ⋯, tn]` replaces a goal of the form `s ∈ f.sets`</span>
<span class="cm">and terms `h1 : t1 ∈ f.sets, ⋯, tn ∈ f.sets` with `∀x, x ∈ t1 → ⋯ → x ∈ tn → x ∈ s`.</span>

<span class="cm">`filter [t1, ⋯, tn] e` is a short form for `{ filter [t1, ⋯, tn], exact e }`.</span>
<span class="cm">-/</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">filter_upwards</span>
  <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">parse</span> <span class="n">types</span><span class="bp">.</span><span class="n">pexpr_list</span><span class="o">)</span>
  <span class="o">(</span><span class="n">e&#39;</span> <span class="o">:</span> <span class="n">parse</span> <span class="err">$</span> <span class="n">optional</span> <span class="n">types</span><span class="bp">.</span><span class="n">texpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span>
</pre></div>


<p>Since when did we have the <code>near</code> tactic?</p>

#### [ Patrick Massot (Sep 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133625225):
<p>I was about to try to find this</p>

#### [ Patrick Massot (Sep 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133625233):
<p>But I was never able to use it :(</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133625255):
<p>I recall Cyril showing a very nice version of this tactic in Coq</p>

#### [ Johannes Hölzl (Sep 10 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133632944):
<p>I added this 6 month ago. It's just a cheap version of Cyril's near tactic. Its more a reimplementation of Isabelle's <code>eventually</code> tactic</p>

#### [ Mario Carneiro (Sep 10 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133643643):
<p>Cross reference: <a href="#narrow/stream/113488-general/subject/abel.20tactic/near/133643278" title="#narrow/stream/113488-general/subject/abel.20tactic/near/133643278">abel tactic</a></p>

#### [ Kevin Buzzard (Sep 10 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/133648808):
<p>Oh this is great news. Summary: the situation before this tactic was that we could prove things like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><msup><mo>)</mo><mn>2</mn></msup><mo>=</mo><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>x</mi><mi>y</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">(x+y)^2=x^2+2xy+y^2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord mathrm">2</span><span class="mord mathit">x</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span> if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>y</mi></mrow><annotation encoding="application/x-tex">y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span> were elements of a commutative ring (or even a commutative semiring) using the <code>ring</code> tactic, but for analogous questions about abelian groups the <code>ring</code> tactic did not work, and until now, if <code>simp</code> did not solve the goal, then one had to get one's hands dirty.</p>

#### [ Kevin Buzzard (Sep 17 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/134103969):
<p>We have <code>linarith</code>, a new tactic that <span class="user-mention" data-user-id="110596">@Rob Lewis</span> has written, which should definitely be mentioned here. It proves a bunch of things which hitherto were quite annoying / fiddly to prove. See it in action here: <a href="#narrow/stream/113489-new-members/subject/Feedback.20(Heine.20Borel.20in.20progress)/near/134050573" title="#narrow/stream/113489-new-members/subject/Feedback.20(Heine.20Borel.20in.20progress)/near/134050573">https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Feedback.20(Heine.20Borel.20in.20progress)/near/134050573</a> (e.g. proving that if <code>0 &lt;= x</code> then <code>x/2 &lt;= x</code>).</p>

#### [ Johan Commelin (Sep 21 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/134356908):
<p>Today Kevin Buzzard is turning 50 <span class="emoji emoji-1f382" title="birthday">:birthday:</span>. <a href="#narrow/stream/113488-general/subject/Happy.20birthday.2C.20Kevin!" title="#narrow/stream/113488-general/subject/Happy.20birthday.2C.20Kevin!">Congratulate him here</a>!<br>
With a group of people we have been hacking like crazy to give him some birthday presents:</p>
<ul>
<li><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Made immense (really immense!) progress on his <code>exp</code> branch in the community fork. We now have <code>exp</code>, <code>cos</code>, <code>sin</code> (all both complex and real), basic identities like <code>sin_add</code>, a proof that these functions are continuous, the intermediate value theorem, and finally <code>pi</code>. Yeah! <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span> <span class="emoji emoji-1f942" title="clink">:clink:</span> </li>
<li>Other people have worked hard in a secret repository that is now public: <a href="https://github.com/semorrison/kbb" target="_blank" title="https://github.com/semorrison/kbb">https://github.com/semorrison/kbb</a> (I sincerely apologize if you would have liked to participate but didn't know about this. I tried to contact as many people as I thought would be interested out of band, but of course I couldn't start a thread about this in the <code>#general</code> stream.)</li>
<li>This repository contains a definition of <code>det</code> (determinant of matrices) and a proof that it is a monoid morphism. Thanks <span class="user-mention" data-user-id="110064">@Kenny Lau</span> </li>
<li><span class="user-mention" data-user-id="120536">@Jack Crawford</span> has a bunch of stuff on a different implementation of matrices. Well done! (There seems to be a trade-off, the current implementation of matrices is nice to prove things with, his could well be better for computations.)</li>
<li>A way to extract a matrix from a linear map between finite-dimensional vector spaces with bases.</li>
<li>Characteristic polynomials of square matrices. (But no properties at all.)</li>
<li>A proof that PID's are UFD's. Thanks <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> (This result might be helpful for constructing splitting fields, because you want to know that an arbitrary (nonzero) polynomial factors into a product of irreducibles.)</li>
<li>A (admittedly ad-hoc) definition of the modular group, plus a boatload of facts about it (e.g., we have a finite set of representatives of the action of <code>SL2Z</code> on matrices (over <code>int</code>) with determinant <code>m &gt; 0</code>).</li>
<li>A definition of complex derivatives, holomorphic function, modular forms.</li>
<li>A proof that holomorphic functions form a subring of the ring of functions (on an arbitrary open domain in the complex numbers).</li>
<li>A proof that modular forms form a submodule of functions on the upper half plane.</li>
<li>An almost definition of Hecke operators. (Sorry Kevin, Lean was fighting back hard.)<br>
Congratulations (and disucssions of about the maths!) can go <a href="#narrow/stream/113488-general/subject/Happy.20birthday.2C.20Kevin!" title="#narrow/stream/113488-general/subject/Happy.20birthday.2C.20Kevin!">here</a></li>
</ul>

#### [ Johan Commelin (Oct 02 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135037903):
<p>It's time for an update in this thread. And someone should also start the corresponding thread in <code>#general</code>.</p>

#### [ Johan Commelin (Oct 02 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135037915):
<p>We now have Hensel's Lemma, thanks to <span class="user-mention" data-user-id="110596">@Rob Lewis</span></p>

#### [ Johan Commelin (Oct 02 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135038009):
<p>We also have <code>holor</code>. A <code>holor</code> is a generalisation of vectors and matrices. It is what the physicists would call a "tensor".</p>

#### [ Johan Commelin (Oct 02 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135038047):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Did a bunch of topology. Stuff on locally compact spaced. He also contributed groupoids.</p>

#### [ Johan Commelin (Oct 02 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135038119):
<p>Quadratic reciprocity has been merged. Once again: thanks <span class="user-mention" data-user-id="110044">@Chris Hughes</span></p>

#### [ Rob Lewis (Oct 02 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135038132):
<p>For the sake of completeness, the <code>holor</code> library is from <span class="user-mention" data-user-id="129120">@Alexander Bentkamp</span> based on his work in Isabelle: <a href="https://link.springer.com/chapter/10.1007/978-3-319-66107-0_4" target="_blank" title="https://link.springer.com/chapter/10.1007/978-3-319-66107-0_4">https://link.springer.com/chapter/10.1007/978-3-319-66107-0_4</a></p>

#### [ Patrick Massot (Oct 02 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135039245):
<p>I don't see holors, locally compact spaces and quadratic reciprocity in <a href="https://github.com/leanprover/mathlib/tree/master/docs/theories" target="_blank" title="https://github.com/leanprover/mathlib/tree/master/docs/theories">https://github.com/leanprover/mathlib/tree/master/docs/theories</a> <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Kevin Buzzard (Oct 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135415885):
<p>Thanks to Chris and Kenny, and inspired by work of my UROP students over the summer (especially <span class="user-mention" data-user-id="120276">@Morenikeji Neri</span> ) we now have determinants! <a href="https://github.com/leanprover/mathlib/issues/404" target="_blank" title="https://github.com/leanprover/mathlib/issues/404">#404</a></p>

#### [ Mario Carneiro (Oct 08 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135415959):
<p>next stop characteristic polynomials?</p>

#### [ Johan Commelin (Oct 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135415986):
<p>Done in <code>kbb</code></p>

#### [ Kevin Buzzard (Oct 08 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135416119):
<p>My birthday present just keeps on giving</p>

#### [ Johan Commelin (Oct 08 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135416125):
<p>You only turn 50 once...</p>

#### [ Johan Commelin (Oct 15 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135843390):
<p>Thanks to the hard work Johannes we now have a nice start on Lebesgue integration: <a href="https://github.com/leanprover/mathlib/commit/0fe284916a73ce92227f77826ad9655b1329eb83" target="_blank" title="https://github.com/leanprover/mathlib/commit/0fe284916a73ce92227f77826ad9655b1329eb83">https://github.com/leanprover/mathlib/commit/0fe284916a73ce92227f77826ad9655b1329eb83</a></p>

#### [ Johan Commelin (Oct 15 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135843426):
<p>Patrick and Johannes have worked very hard on quotient topologies on algebraic structures: <a href="https://github.com/leanprover/mathlib/commit/2395183b5b424371d5170f6c7bca691a654ae5bb" target="_blank" title="https://github.com/leanprover/mathlib/commit/2395183b5b424371d5170f6c7bca691a654ae5bb">https://github.com/leanprover/mathlib/commit/2395183b5b424371d5170f6c7bca691a654ae5bb</a></p>

#### [ Johan Commelin (Oct 15 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135843497):
<p>Chris proved that subgroups of cyclic groups are cyclic: <a href="https://github.com/leanprover/mathlib/commit/c5930f574c54e3fd157b1ef8b93da8b1f50c8ed4" target="_blank" title="https://github.com/leanprover/mathlib/commit/c5930f574c54e3fd157b1ef8b93da8b1f50c8ed4">https://github.com/leanprover/mathlib/commit/c5930f574c54e3fd157b1ef8b93da8b1f50c8ed4</a></p>

#### [ Patrick Massot (Oct 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135846567):
<p>Uniform spaces have Hausdorff completions <a href="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L535" target="_blank" title="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L535">https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L535</a>. More precisely, there is a completion functor which is left-adjoint to the inclusion of complete Hausdorff spaces into all uniform spaces.</p>

#### [ Patrick Massot (Oct 15 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135846763):
<p>Abelian topological groups have a uniform space structure <a href="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/topological_groups.lean#L27" target="_blank" title="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/topological_groups.lean#L27">https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/topological_groups.lean#L27</a> characterized by uniform continuity of substraction. The completion of such a topological group is a topological group with its canonical uniform structure (in particular the later is complete). Separated topological ring also have completions with the expected properties</p>

#### [ Johannes Hölzl (Oct 17 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135954996):
<p>I merged <a href="https://github.com/leanprover/mathlib/issues/386" target="_blank" title="https://github.com/leanprover/mathlib/issues/386">#386</a> Chris' PR about trigonometric functions. So we have pi, exp, etc now</p>

#### [ Kenny Lau (Oct 17 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135955257):
<p>looks like I messed up something. Could someone help reset <code>leanprover-community/mathlib</code>?</p>

#### [ Johannes Hölzl (Oct 17 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135955276):
<p>fixed</p>

#### [ Kenny Lau (Oct 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/135955325):
<p>thanks</p>

#### [ Johannes Hölzl (Oct 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/136026140):
<p>each PID is a UFD is now in mathlib</p>

#### [ Johan Commelin (Nov 05 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817351):
<p>Ok, who is up for a summary of today?</p>

#### [ Johan Commelin (Nov 05 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817362):
<p>First of all: the module refactor landed!</p>

#### [ Johan Commelin (Nov 05 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817368):
<p>Second: Perfect closure has been merged.</p>

#### [ Kevin Buzzard (Nov 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817388):
<p>This is a green light for algebraic closure and Galois theory</p>

#### [ Johan Commelin (Nov 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817519):
<p>We now have all facts about <code>irrational</code> numbers that you would ever want to know.</p>

#### [ Johan Commelin (Nov 05 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817550):
<p>(Ok, ok, we don't yet have irrationality op <code>pi</code>.)</p>

#### [ Johan Commelin (Nov 05 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/146817557):
<p>We have Stone-Cech compactification.</p>

#### [ Patrick Massot (Nov 19 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/147997742):
<p>Simon's monotonicity tactic has been merged in mathlib.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">monotonicity</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">k</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h₀</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">≤</span> <span class="mi">0</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≤</span> <span class="n">x</span><span class="o">)</span>
<span class="o">:</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">*</span> <span class="n">z</span> <span class="bp">+</span> <span class="n">k</span> <span class="bp">≤</span> <span class="n">z</span> <span class="bp">*</span> <span class="o">(</span><span class="n">y</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">m</span><span class="o">)</span> <span class="bp">+</span> <span class="n">k</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">ac_mono</span><span class="bp">*</span>
</pre></div>

#### [ Patrick Massot (Nov 19 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/147998023):
<p>We can combine with norm_num too:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">linear_ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">k</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">3</span> <span class="bp">+</span> <span class="n">x</span><span class="o">)</span> <span class="bp">-</span> <span class="n">y</span> <span class="bp">≤</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">4</span> <span class="bp">+</span> <span class="n">x</span><span class="o">)</span> <span class="bp">-</span> <span class="n">z</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">mono</span><span class="bp">*</span> <span class="bp">;</span> <span class="n">norm_num</span>
</pre></div>

#### [ Johan Commelin (Nov 20 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/148016023):
<p>Great news! Thanks <span class="user-mention" data-user-id="110026">@Simon Hudon</span>! This is going to be very helpful. I really want to go back to the simplicial project now. Monotone functions are all over the place there.</p>

#### [ Simon Hudon (Nov 20 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/148016136):
<p>Please keep me posted of ups and downs of using the tactic :)</p>

#### [ Scott Morrison (Dec 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/150739441):
<p>(co)limits, and (co)limits in the category of Types!</p>

#### [ Scott Morrison (Dec 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/150739443):
<p>There's still more to come (support for all the special shapes, products, equalizers, etc).</p>

#### [ Scott Morrison (Dec 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/150739492):
<p>Also recently: equivalences of categories, along with a new tactic <code>slice</code>, for <code>conv</code>ing your way into long compositions, without having to use <code>rw category.assoc</code> by hand.</p>

#### [ Patrick Massot (Jan 05 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/154468807):
<p>Sébastien's bounded continuous function has been merged <span class="emoji emoji-1f389" title="tada">:tada:</span> Thank you so much Sébastien and Mario! This was a large PR, adding more than 600 lines to mathlib, even after getting Mario-compressed. </p>
<blockquote>
<p>The type of bounded continuous functions from a topological space to a metric space, with the corresponding uniform distance. We prove basic statements such as the completeness of the space when the target is complete, and the Arzela-Ascoli theorem saying that a set of functions with a common modulus of continuity is compact. When the target space is a normed space, we also put the canonical normed space structure on the space of bounded continuous functions, working pointwise and checking that everything is compatible with the distance.</p>
</blockquote>

#### [ Sebastien Gouezel (Jan 05 2019 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/154469138):
<p>Thanks a lot Mario, this is awesome!</p>

#### [ Patrick Massot (Jan 18 2019 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156374379):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> could you tell us something about this Giry monad?</p>

#### [ Johannes Hölzl (Jan 18 2019 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156375691):
<p>Yep, with the newest commits the Giry monad is in mathlib In category speak, its the monad for the <code>measure</code> functor in the category of <code>measurable</code> spaces and functions. With this we get a straight forward way to construct product: <code>prod M1 M2 := do { x &lt;- M1, y &lt;- M2, return (x, y) }</code> <br>
Also I added measurable equivalences, which are helpful to adopt measurability proofs to different (but isomorphic) spaces</p>

#### [ Johannes Hölzl (Jan 18 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156375770):
<p>the Giry monad will be also important to write down probabilistic programs or constructions. Especially in the theorem of Ionescu-Tulcea it provides a construction mechanism for discrete-time stochastic processes out of Markov kernels</p>

#### [ Simon Hudon (Jan 18 2019 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156396464):
<p>Can you use it in the category <code>types</code>?</p>

#### [ Kevin Buzzard (Jan 19 2019 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156408538):
<p><span class="user-mention" data-user-id="120726">@Luca Gerolla</span> do you understand a word of this? Luca formalised some stochastic stuff in Lean</p>

#### [ Luca Gerolla (Jan 19 2019 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156432294):
<p>I can understand the probability notions (after googling) - in class we just focused on Kolmogorov extension theorem since we only studied discrete time-homogeneous Markov processes. <br>
Fascinating to see this general approach to formalise discrete-time stochastic processes :-)</p>

#### [ Johannes Hölzl (Jan 19 2019 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156443607):
<p>the next step is to work on projective families, then Ionescu-Tulcea isn't far.</p>

#### [ Johannes Hölzl (Jan 19 2019 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156443615):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> no, we need the category of measurable spaces</p>

#### [ Simon Hudon (Jan 19 2019 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156446651):
<p>Doesn't that limit the applicability to writing programs?</p>

#### [ Johannes Hölzl (Jan 20 2019 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156458525):
<p>Yes, the need to have a probability measure limits the program. Measurability is a very wide and adaptible concept. If you really want your program to be outside of measurability the Giry monad can't help you</p>

#### [ Simon Hudon (Jan 20 2019 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156489827):
<p>I was wondering if you could embed it in type with a trick like:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">M</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">measurable_space</span><span class="o">)</span>
<span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">Giry</span> <span class="n">s</span><span class="o">)</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">-&gt;</span> <span class="n">a</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Jan 20 2019 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156490029):
<p>That allows you to implement <code>pure</code>, <code>map</code> and (i believe) <code>bind</code></p>

#### [ Kevin Buzzard (Jan 20 2019 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156491890):
<p>A scheme is a topological space equipped with some structure and satisfying some axioms. It makes sense to talk about morphisms of schemes (which are continuous maps on the topological spaces plus some other data involving the extra structure plus some axioms), and schemes form a category.</p>
<p>The category of schemes has finite products. In short, if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>T</mi></mrow><annotation encoding="application/x-tex">T</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">T</span></span></span></span> are schemes, then there's a product scheme <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mo>×</mo><mi>T</mi></mrow><annotation encoding="application/x-tex">S\times T</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.13889em;">T</span></span></span></span>, defined up to unique isomorphism, and satisfying the usual universal property. However the underlying topological space of a product of schemes is <em>not</em> the product of the underlying topological spaces (and the underlying type of a product is not the product of the underlying types).</p>
<p>I have no idea what monads have got to do with measure theory, but it occurred to me last week when talking to Ramon that with our <code>scheme X</code> idea (this is "unbundled", right?) where <code>X</code> is the underlying type, one can't use instances like <code>scheme X -&gt; scheme Y -&gt; scheme X \times Y</code> because that's the wrong product. Can I use monads in some crazy way to help here? <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  seems to think that monads can help with products in this measurable situation...</p>
<p>What do products look like when everything gets bundled? Oh -- it's just a map <code>scheme \times scheme -&gt; scheme</code>, right?</p>
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Why are you having trouble extending a sheaf on a basis to a sheaf on the space, when I managed to do it without using categories? Is this anything to do with bundling or is this just universe issues?</p>

#### [ Johannes Hölzl (Jan 21 2019 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156502444):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> What is <code>Giry s</code> in your case? Is <code>x</code> a measure on <code>s</code>? And what is the measurable space on<code>a</code>?</p>

#### [ Johannes Hölzl (Jan 21 2019 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156502565):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I want to construct the usual product of the shape <code>measure A -&gt; measure B -&gt; measure (A x B)</code>. This would be the expected product from measure theory (assuming sigma finite measures). Here the Giry monad allows a factored proof.<br>
I don't see how monads will help with your problem...</p>

#### [ Chris Hughes (Jan 21 2019 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156542773):
<p>(deleted)</p>

#### [ Patrick Massot (Jan 22 2019 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156618466):
<p>Johannes and Sander defined the <a href="https://github.com/leanprover/mathlib/commit/edfa2061547510a41db4d0d471130badcb92ef20" target="_blank" title="https://github.com/leanprover/mathlib/commit/edfa2061547510a41db4d0d471130badcb92ef20">rank of a linear map</a>!</p>

#### [ Johannes Hölzl (Jan 23 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156682401):
<p>PR <a href="https://github.com/leanprover/mathlib/issues/553" target="_blank" title="https://github.com/leanprover/mathlib/issues/553">#553</a> was merged, we have now Lipschitz continuous functions, the Banach fixed-point theorem</p>

#### [ Johannes Hölzl (Jan 23 2019 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156682413):
<p>We also have the point wise order on products as the canonical order structure</p>

#### [ Johannes Hölzl (Jan 23 2019 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156688372):
<p>seqeuence spaces (PR <a href="https://github.com/leanprover/mathlib/issues/440" target="_blank" title="https://github.com/leanprover/mathlib/issues/440">#440</a>) is merged</p>

#### [ Johannes Hölzl (Jan 24 2019 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/156778780):
<p>Measures form a complete lattice now</p>

#### [ Johannes Hölzl (Jan 28 2019 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157051157):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> 's module refactoring is in mathlib now. A type can now have multiple modules over different base rings.</p>

#### [ Johannes Hölzl (Jan 29 2019 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157100526):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> splitting polynomials and <code>clear_aux_decl</code> are in mathlib now</p>

#### [ Johan Commelin (Jan 29 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157128654):
<p>This is great news! Thanks <span class="user-mention" data-user-id="110044">@Chris Hughes</span> <span aria-label="tada" class="emoji emoji-1f389" role="img" title="tada">:tada:</span> <br>
This means that we can now define all sorts of interesting extensions of  <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Q</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Q}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.85556em;vertical-align:-0.16667em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Q</span></span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">Q</mi><mi>p</mi></msub></mrow><annotation encoding="application/x-tex">\mathbb{Q}_p</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.974998em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">Q</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span>. Number theory is getting closer and closer!</p>

#### [ Johannes Hölzl (Jan 29 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157129032):
<p>no its not splitting fields, just the splitting polynomials. The splitting field PR is still a PR...</p>

#### [ Johan Commelin (Jan 29 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157129051):
<p>Aaah, too bad.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157134402):
<p>Number theory is still getting closer. I don't want to take on a new project right now but I feel like Dedekind domains might be accessible now, and probably would be an excellent test for the new module refactor.</p>

#### [ Kevin Buzzard (Jan 29 2019 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157134499):
<p>That can happen independently of the Galois theory stuff happening at Imperial and of any number fields stuff, it's pure commutative algebra.</p>

#### [ Johannes Hölzl (Jan 30 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157171442):
<p>Congratulations to <span class="user-mention" data-user-id="110064">@Kenny Lau</span>: his proof of the Hilbert basis theorem is now in mathlib!</p>

#### [ Kenny Lau (Jan 30 2019 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157171453):
<p>Thanks!</p>

#### [ Kevin Buzzard (Jan 30 2019 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20new%20in%20Lean%20maths%3F/near/157182521):
<p>I tried to prove Hilbert basis in September with the old version of modules and it was basically "impossible" -- I know that's a silly word, but what I mean is that the natural proof needed more from modules than mathlib could give me. Since then I've been regarding the proof of this theorem as a good benchmark for the theory of rings and modules, and think it's great that this now works. Commutative algebra is a bit like finite group theory -- there are a bunch of basic techniques, and once you have them all, there is a whole world of theorems which are accessible. It is also the correct generality for proofs of results which number theorists, algebraic geometers etc are interested in. As people might know, at Imperial we are working on Galois theory (mostly the students, not me) and if we can prove the <a href="https://en.wikipedia.org/wiki/Fundamental_theorem_of_Galois_theory" target="_blank" title="https://en.wikipedia.org/wiki/Fundamental_theorem_of_Galois_theory">fundamental theorem of Galois theory</a> (FTG) then this will be an even more powerful indication that things are going in the right direction. I can do Hilbert basis in 30 minutes in a lecture and it only relies on the definition of a Noetherian ring, but FTG takes several lectures in total and also relies on a bunch of definitions like normal and separable field extensions.</p>


{% endraw %}
