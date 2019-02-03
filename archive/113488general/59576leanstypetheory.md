---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59576leanstypetheory.html
---

## Stream: [general](index.html)
### Topic: [lean's type theory](59576leanstypetheory.html)

---


{% raw %}
#### [ Mario Carneiro (Mar 17 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123826805):
<p>Okay, I'm a bit embarrassed to release this in this very early form, but there's enough meat in it that it can be useful to others even before it's done. This will probably become a major part of my master's thesis. What you will find:</p>
<ul>
<li>A definition of the axioms of lean<ul>
<li>The basic DTT stuff</li>
<li>let binders and definitions</li>
<li>inductive types (in full gory detail)</li>
<li>the computation rules (beta, eta, zeta, delta, iota)</li>
<li>Quotient types</li>
<li>propext and choice</li>
</ul>
</li>
<li>Algorithmic equality (aka lean's defeq)<ul>
<li>proof that algorithmic equality is not transitive and defeq is not decidable</li>
</ul>
</li>
<li>Unique typing<ul>
<li>A long and complicated proof, involving a hierarchy of church-rosser theorems. I'm really glad it worked out, but the complexity shows, and I need to trim it down and make it more accessible</li>
</ul>
</li>
<li>Soundness (unfinished)<ul>
<li>It is exactly as simple as it sounds like, but the language is huge and there are a lot of cases.</li>
</ul>
</li>
</ul>
<p><a href="https://github.com/digama0/lean-type-theory/releases/download/v0.1/main.pdf" target="_blank" title="https://github.com/digama0/lean-type-theory/releases/download/v0.1/main.pdf">https://github.com/digama0/lean-type-theory/releases/download/v0.1/main.pdf</a></p>

#### [ Kevin Buzzard (Mar 17 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123835473):
<p>Oh many thanks for this -- as you saw, I made some sort of effort to engage with this kind of material without reading the source code (i.e. restricting to the docs) and it was tough. I am relieved to see that iota reduction applies to things defined by recursion rather than just cases!</p>

#### [ Kevin Buzzard (Mar 17 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123836058):
<p>I spent some time yesterday trying to get to the bottom of this <code>accrec</code> example and it would have been a darn sight easier if I'd had access to this paper then.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837211):
<p>I think it's great that we finally have a written description of the type theory implemented in Lean.  Ideally it should also be included in the reference manual, and/or published somewhere.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837329):
<p>section 2.3: I don't think it is a good idea to require full whnf in the algorithmic equivalence since we don't do it any of the implementations.  We do lazy delta-reduction, that is, do full beta/iota/quotient/zeta and only unfold the constant with the larger definitional height, once.  I think you should just replace ↓ by ⇝* here.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837381):
<p>section 2.4: "Lean takes a simpler approach and simply zeta expands these binders when necessary for checking.":  I don't think you've defined "Lean" anywhere.  Not all of the implementations follow this approach.  The C++ <code>type_checker</code>, the Haskell <code>tc</code>, and <code>trepplein</code> all eagerly unfold lets.  However, the <code>type_context</code> doesn't.  I believe the term ζ-reduction typically refers to x ⇝ e'.</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837575):
<p>There are a few white lies in algorithmic equivalence, and I'd be happy to give a more honest account but I'm not quite sure how. (One thing I have noticed is that sometimes pure congruence proofs don't check, because one side is eagerly iota reduced to something that is not recognizably equivalent anymore.)</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837576):
<p>section 2.6.2: "Here we have K-like elimination": do you mean large elimination?  K-like reduction for acc would not be strongly normalizing, right?</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837581):
<p>I don't use the term "subsingleton elimination" anywhere in the paper, I may have mixed up my terms. I use K-like elimination to refer to large eliminating props</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837625):
<p>When I talk about "lean does X", I am usually referring to lean.exe's kernel. I didn't want to get into checking expressions with lets in the context, like <code>type_context</code> does, which is why I omitted that approach.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837626):
<blockquote>
<p>but there is a second reduction rule used for K-like eliminators. It can be thought of as a combination of proof irrelevance to change the major<br>
premise into a constructor followed by the iota rule.</p>
</blockquote>
<p>Yes, you might want to clean up the definitions (and actually define them). ^^</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837628):
<p>which part?</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837668):
<p>Also: I just finished the proof of soundness. Celebrate! Lean can't prove false</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837669):
<p>K-like elimination refers to K-like reduction here, and subsingleton elimination on the page before, afaict.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837670):
<p>That's not using algorithmic defeq, right?</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837680):
<p>Soundness for both algorithmic and ideal typechecking</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837721):
<p>I proved it for the ideal version, and the algorithmic check implies ideal check</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837765):
<blockquote>
<p>algorithmic check implies ideal check</p>
</blockquote>
<p>That's not proven yet, right?</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837766):
<p>It's pretty trivial</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837767):
<p>the algorithmic rules are a subset of the ideal ones</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837772):
<p>the ideal check is basically what lean would do if it was nondeterministic and tried all the tricks at once</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837816):
<p>Except that the ideal ones have extra side conditions that require the well-typedness of all terms that occur.  The implication requires at the very least subject reduction for ⇝, which is not completely obvious to me.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837861):
<p>Ok, I see subjection reduction is Lemma 3.10.</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837866):
<p>Note that -&gt;_kappa is a bit different from -&gt;, it has slightly different rules for iota stuff</p>

#### [ Mario Carneiro (Mar 17 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123837869):
<p>I never explicitly stated subject reduction for -&gt; (using the ideal check), but maybe I should be more precise about it</p>

#### [ Gabriel Ebner (Mar 17 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838082):
<p>I think the general approach for the algorithmic defeq is good.  It's better to have an over-approximation than to precisely model the actual (current implementation of the) type-checker.  If you can show this defeq proof system to be sound, then all "reasonable" type-checkers should be correct.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838128):
<p>section 2.3:  you're also missing η-expansion, see <a href="https://github.com/leanprover/lean/blob/07bb7d809b6be49f38ce4e427c54a82708ae281f/src/kernel/type_checker.cpp#L517-L529" target="_blank" title="https://github.com/leanprover/lean/blob/07bb7d809b6be49f38ce4e427c54a82708ae281f/src/kernel/type_checker.cpp#L517-L529">https://github.com/leanprover/lean/blob/07bb7d809b6be49f38ce4e427c54a82708ae281f/src/kernel/type_checker.cpp#L517-L529</a></p>

#### [ Mario Carneiro (Mar 17 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838372):
<p>Would it suffice to replace the eta rule with extensionality "e x &lt;-&gt; e' x =&gt; e &lt;-&gt; e'"?</p>

#### [ Mario Carneiro (Mar 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838415):
<p>or is this only used when solving lam x:a. e &lt;-&gt; e'</p>

#### [ Gabriel Ebner (Mar 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838416):
<p>Yes, you can then recover η via the conversion rule.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838417):
<p>Yes, in practice it is only used when one side is a lambda.</p>

#### [ Mario Carneiro (Mar 17 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838454):
<p>I know some typecheckers prefer extensionality over eta, since it's pretty easy to figure out when to use it</p>

#### [ Mario Carneiro (Mar 17 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838801):
<blockquote>
<blockquote>
<p>but there is a second reduction rule used for K-like eliminators. It can be thought of as a combination of proof irrelevance to change the major<br>
premise into a constructor followed by the iota rule.</p>
</blockquote>
<p>Yes, you might want to clean up the definitions (and actually define them). ^^</p>
</blockquote>
<p>I don't follow. That passage looks alright, is something missing?</p>

#### [ Gabriel Ebner (Mar 17 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838901):
<p>K-like elimination refers to multiple concepts in the paper: 1) subsingleton elimination, and 2) K-like reduction.  For example, <code>and</code> has 1) but not 2).</p>

#### [ Mario Carneiro (Mar 17 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838941):
<p>I use it essentially only for (1), (2) is more of a remark that comes up once as a sort of historical note "why K?"</p>

#### [ Gabriel Ebner (Mar 17 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838949):
<p>You use it for 2) in section 2.6.4.  Although it is not clear how you obtain the <code>b</code> there.</p>

#### [ Mario Carneiro (Mar 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838988):
<p>I need a name for inductive types that eliminate to Type but live in Prop. "Large elimination" seems to also suggest when the type itself is large, so it's not a great name. Will subsingleton elimination cover exactly this usage?</p>

#### [ Mario Carneiro (Mar 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838989):
<p>the b is obtained from the LHS as described in the paragraph after</p>

#### [ Mario Carneiro (Mar 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838990):
<p>and it only applies if you can obtain all of b that way</p>

#### [ Gabriel Ebner (Mar 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838991):
<p>I've only seen "subsingleton elimination" in this usage.</p>

#### [ Mario Carneiro (Mar 17 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838996):
<p>cool, I'll stop saying K-like then</p>

#### [ Gabriel Ebner (Mar 17 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123838997):
<p>Ah, next page, ok.</p>

#### [ Mario Carneiro (Mar 17 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123840473):
<p>Huh, I've been telling myself that defeq is only undecidable in inconsistent contexts, but this is not true, almost trivially: if <code>x : 0 |- A = B</code> is some undecidable defeq problem, then <code>|- \lam x : 0. A = \lam x : 0. B</code> is also an undecidable defeq problem</p>

#### [ Patrick Massot (Mar 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843167):
<p>I swear one day I'll have time to actually read this paper (or maybe a version with a bit higher word/symbol ratio). In the mean time I'm surprised by the source code. It' funny to see Lean consistently use unicode to be more readable than Coq but you still write <code>\Gamma\vdash \alpha:\U_\ell\quad \Gamma\vdash e:\beta</code> in your LaTeX source like it's still 1990.</p>

#### [ Patrick Massot (Mar 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843211):
<p>You even use <code>$$</code>!</p>

#### [ Patrick Massot (Mar 17 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843221):
<p>And a non-semantic use of <code>\frac</code></p>

#### [ Patrick Massot (Mar 17 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843223):
<p>Ok, I go back to work</p>

#### [ Simon Hudon (Mar 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843262):
<p>Yeah LaTeX is pretty horrible. Nothing seems to measure up though. And people have tried a lot</p>

#### [ Patrick Massot (Mar 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843270):
<p>Mario's LaTeX is horrible</p>

#### [ Patrick Massot (Mar 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843272):
<p>Nothing keeps him in 1990</p>

#### [ Patrick Massot (Mar 17 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843279):
<p>He could use <code>xeLaTeX</code> (or <code>LuaLaTeX</code>) and <code>unicode-math</code></p>

#### [ Simon Hudon (Mar 17 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843280):
<p>Maybe that and underwater basket weaving are the things he doesn't rock at. But seriously, what does 2018 LaTeX look like?</p>

#### [ Patrick Massot (Mar 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843324):
<p>At least <a href="https://gitlab.com/PatrickMassot/h-principle/blob/master/src/hol_approx.tex" target="_blank" title="https://gitlab.com/PatrickMassot/h-principle/blob/master/src/hol_approx.tex">https://gitlab.com/PatrickMassot/h-principle/blob/master/src/hol_approx.tex</a></p>

#### [ Patrick Massot (Mar 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843336):
<p>(some unicode is not used in this example because this source code is also meant for MathJax consumption)</p>

#### [ Simon Hudon (Mar 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843337):
<p>I have not actually tried those. You actually enter your formulas with unicode and don't need spacing commands?</p>

#### [ Patrick Massot (Mar 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843341):
<p>You still need spacing commands</p>

#### [ Patrick Massot (Mar 17 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843343):
<p>but no <code>\Gamma</code></p>

#### [ Simon Hudon (Mar 17 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843383):
<p>That is pretty nice</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843396):
<p>I'm never sure if unicode is going to get mangled somewhere</p>

#### [ Simon Hudon (Mar 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843397):
<p>I've been trying org-mode for my dissertation. Maybe I should add one of those too</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843441):
<p>I remember Floris sent in a tex file with lean snippets, and the journal typesetter complained about the unicode</p>

#### [ Patrick Massot (Mar 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843444):
<p>Oh yes, you could have trouble with the journal</p>

#### [ Patrick Massot (Mar 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843450):
<p>Today you still need to fight arXiv if you want to use 21th century LaTeX</p>

#### [ Simon Hudon (Mar 17 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843452):
<p>can you use those tools as preprocessors?</p>

#### [ Patrick Massot (Mar 17 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843459):
<p>That's the reason why you see more and more papers on arxiv where only the pdf is available and not the TeX source</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843504):
<p>No one has ever convincingly explained to me why <code>$$</code> is worse than <code>\[</code> (or something else?)</p>

#### [ Gabriel Ebner (Mar 17 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843560):
<p>section 3.4: why do you consider η-reduction?  I don't think any Lean typechecker has that.</p>

#### [ Patrick Massot (Mar 17 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843567):
<p>$$ has spacing issues (beyond being harder to parsers)</p>

#### [ Patrick Massot (Mar 17 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843569):
<p><a href="https://tex.stackexchange.com/questions/503/why-is-preferable-to/69854" target="_blank" title="https://tex.stackexchange.com/questions/503/why-is-preferable-to/69854">https://tex.stackexchange.com/questions/503/why-is-preferable-to/69854</a> probably contains useful links</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843622):
<p>How else are you going to get eta reduction unless you put it in? Also: the constraints on the kappa reduction relation are very tight. I went through no less than 10 variations on it before I was able to get the church rosser theorem to go through</p>

#### [ Simon Hudon (Mar 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843662):
<blockquote>
<p>That's the reason why you see more and more papers on arxiv where only the pdf is available and not the TeX source</p>
</blockquote>
<p>Do you mean that it is not used as a preprocessor and therefore people only submit pdfs?</p>

#### [ Gabriel Ebner (Mar 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843665):
<p>Not at all?  None of the typecheckers uses it, AFAIK.  Trepplein definitely doesn't.  We only do η for defeq.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843671):
<p>I just got the feeling that η is a serious complication here, and the main reason you need a new and different reduction relation and defeq relation.</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843679):
<p>the whole point of the kappa reduction is so that the statement of Theorem 3.15 holds</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843724):
<p>The alternative would be to try to put eta or extensionality in the =p relation</p>

#### [ Gabriel Ebner (Mar 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843729):
<p>I thought it is included in the ... in the definition of =p.</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843730):
<p>the ... only includes compatibility rules</p>

#### [ Gabriel Ebner (Mar 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843772):
<p>I don't think it says that anywhere. (at least not above and below the definition)</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843778):
<p>It's a very spartan relation, it's just replacing proofs and nothing else (except for that lambda thing)</p>

#### [ Mario Carneiro (Mar 17 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123843925):
<p>I will investigate whether it suffices to have one-sided extensionality e =p e' x =&gt; lam x:a. e =p e' and remove eta from the kappa reduction. If so that would allow me to remove the context from -&gt;k, which would be nice</p>

#### [ Mario Carneiro (Mar 17 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844178):
<p>I think the biggest departure from the usual reduction relation is the K reduction (which I have renamed K+), because it is super aggressive unfolding of a proof, which guarantees nontermination when it sees an acc.rec</p>

#### [ Kevin Buzzard (Mar 17 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844779):
<p>so is this paper about what Lean does, or what it should do in your opinion :-)</p>

#### [ Kevin Buzzard (Mar 17 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844830):
<p>And do the devs have any comments about whether Lean 4 will do the same thing when it comes to definitional equality?</p>

#### [ Gabriel Ebner (Mar 17 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844835):
<p>Not sure if I count as a dev anymore, but I seriously doubt there will be any foundational changes in Lean 4.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844845):
<p>That's good to know -- I guess there were foundational changes from Lean 2 to Lean 3 so I suppose it wasn't something one could definitely assume...</p>

#### [ Gabriel Ebner (Mar 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844931):
<p>There were exactly two foundational changes from Lean 2 to Lean 3: 1) let-expressions in the kernel (completely harmless), 2) mutually inductive types are no longer supported by the kernel (these are now simulated).  Also the axioms for choice and quotients got some mostly cosmetic changes.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123844940):
<p>Oh I thought there was some change to the underlying type theory -- HoTT in Lean 2?</p>

#### [ Gabriel Ebner (Mar 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845033):
<p>Oh yes, HoTT got removed from the kernel (you had to pass an extra command-line flag to use it, and there was a separate library).  Completely forgot about that.  But we now have a reasonably way to do it without kernel changes: <a href="https://github.com/gebner/hott3" target="_blank" title="https://github.com/gebner/hott3">https://github.com/gebner/hott3</a></p>

#### [ Mario Carneiro (Mar 17 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845396):
<blockquote>
<p>so is this paper about what Lean does, or what it should do in your opinion :-)</p>
</blockquote>
<p>The motivation is of course what lean does, but this is badly behaved in a number of ways which make it completely unsuitable for theoretical treatment, so I replace it with a better version, show soundness of the original version with respect to that, and then forget about the original thing</p>

#### [ Mario Carneiro (Mar 17 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845485):
<p>As Gabriel mentions, there are multiple "leans", and they don't all agree on the foundational stuff. This is in part what I wanted to address with this paper, to get down a single system that we can talk about as the ideal lean, and look at how close we can get to that. One thing which should be true, however, is that all existing lean kernels are underestimates of the typing judgment in this paper. That means that anything you can't prove with the ideal judgment can't be verified in these kernels either, which is the soundness result I want</p>

#### [ Gabriel Ebner (Mar 17 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845593):
<p>AFAICT all existing kernels even fit within the <em>algorithmic</em> definitional equality check.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845655):
<p>NB: I think the algorithmic definitional equality is not just an ugly approximation of the ideal one, but also important as a practical <em>optimization</em>: using the algorithmic definitional equality, we can elide almost all type-inference calls during type-checking.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845731):
<p>Compare also the various variants of the typing rules proved equivalent in [1].<br>
[1] A.Bauer, P. Haselwarter, T. Wintertaler, A modular formalization of type theory in Coq, TYPES (2017). <a href="http://math.andrej.com/2017/05/29/a-modular-formalization-of-type-theory-in-coq/" target="_blank" title="http://math.andrej.com/2017/05/29/a-modular-formalization-of-type-theory-in-coq/">http://math.andrej.com/2017/05/29/a-modular-formalization-of-type-theory-in-coq/</a></p>

#### [ Mario Carneiro (Mar 17 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123845987):
<p>I'm also having difficulty with stating strong normalization because of my struggles here, I think. What is the reduction relation of interest here? Is it just head reduction? I think it is supposed to include reduction under binders, but then once we decide "arbitrarily" not to reduce some things that should be reducible, in what sense are we talking about the "right" relation? I.e. what does strong normalization have to do with consistency?</p>

#### [ Gabriel Ebner (Mar 17 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846304):
<p>Weak head reduction is enough for consistency.  But strong normalization for the full reduction relation is definitely interesting as well.</p>

#### [ Gabriel Ebner (Mar 17 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846367):
<p>Since we've talked about η today, I think I've found a novel way to break transitivity with just K-like reduction for <code>eq</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foo</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">ℕ</span> <span class="mi">0</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="mi">42</span> <span class="mi">0</span>
<span class="n">def</span> <span class="n">bar</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec</span> <span class="bp">ℕ</span> <span class="mi">0</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="k">if</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="bp">ℕ</span> <span class="k">else</span> <span class="n">empty</span><span class="o">)</span> <span class="o">(</span><span class="mi">42</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="mi">0</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="mi">42</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">bar</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="mi">42</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">=</span> <span class="n">bar</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Mario Carneiro (Mar 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846714):
<p>I found an interesting potential computational rule for <code>quot.sound</code>:</p>
<div class="codehilite"><pre><span></span>variables (α : Sort*) (r : α → α → Prop) (a : α)
  (f : α → Sort*) (H : ∀ (a b : α), r a b → f a = f b)
  (e : f a) (b : α) (h : r a b)

example : @eq.rec (quot r) (quot.mk r a) (quot.lift f H) e
            (quot.mk r b) (quot.sound h) = cast (H a b h) e :=
by change H a b h with (congr_arg (quot.lift f H) (quot.sound h):_);
   induction quot.sound h; refl
</pre></div>

#### [ Mario Carneiro (Mar 17 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846769):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> That was a big pain during the proof of church rosser. It's actually not a theoretical problem, but rather a side effect of K reductions without accounting for eta reduction</p>

#### [ Mario Carneiro (Mar 17 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846775):
<p>I fixed it by making sure that all recursors have the right number of arguments at all times</p>

#### [ Mario Carneiro (Mar 17 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123846824):
<p>Alternatively, any K-like inductive should be eta expanded before normalization</p>

#### [ Mario Carneiro (Mar 17 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123847134):
<p>The problem is that unapplied K recursors are stuck terms when they shouldn't be</p>
<div class="codehilite"><pre><span></span>variables (α : Sort*) (a : α) (C : α → Sort*) (e : C a)
#reduce λ h, @eq.rec α a C e a h -- λ (h : a = a), e   &lt;- good
#reduce @eq.rec α a C e a -- eq.rec e                  &lt;- bad
</pre></div>

#### [ Mario Carneiro (Mar 17 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%27s%20type%20theory/near/123847259):
<p>I originally had the recursors evaluating to lambdas like this, but it was a notational nightmare since the number of unapplications depends on how many variables there are (the only one you have "control" over is the major premise, once that one is allowed to be a variable you have to deal with the parameters and such, and any of those could be variables or things equivalent to variables...), so I opted instead for an up-front eta expansion, since during reduction a recursor never loses its major premise</p>


{% endraw %}
