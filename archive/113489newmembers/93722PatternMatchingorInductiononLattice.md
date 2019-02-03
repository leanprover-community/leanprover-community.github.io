---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/93722PatternMatchingorInductiononLattice.html
---

## Stream: [new members](index.html)
### Topic: [Pattern Matching or Induction on Lattice?](93722PatternMatchingorInductiononLattice.html)

---


{% raw %}
#### [ AHan (Nov 29 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148769128):
<p>If I have a type which is an instance of lattice, how can I pattern match or do induction on it?<br>
For example,</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">lattice</span>
<span class="kn">open</span> <span class="n">lattice</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">semilattice_sup_bot</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">lemma</span> <span class="n">x</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>  <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">a</span>
<span class="bp">|</span> <span class="n">a</span> <span class="o">:=</span>
</pre></div>

#### [ Johan Commelin (Nov 29 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148770964):
<p><span class="user-mention" data-user-id="133545">@AHan</span> Why are you trying to do?</p>

#### [ Johan Commelin (Nov 29 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148770966):
<p>Pattern matching doesn't work on any odd type. (This has nothing to do with lattices.) You need <code>α</code> to be inductive.</p>

#### [ AHan (Nov 29 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148771305):
<p>I want to prove something like</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">lex_acc_of_bot</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">),</span> <span class="o">(</span><span class="n">ra</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="n">acc</span> <span class="o">(</span><span class="n">lex</span> <span class="n">ra</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johan Commelin (Nov 29 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148771643):
<p>Ok, I don't know enough about this... (I don't know what <code>ra</code> and <code>lex</code> are). But what had you hoped to pattern match on? Whether <code>a</code> was the bottom element, or something like that?</p>

#### [ Johan Commelin (Nov 29 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148771654):
<p>For your lemma, you could do induction on the list; maybe that helps?</p>

#### [ AHan (Nov 29 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148771977):
<p>Oh sorry I should say it clearer</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">lex</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">nil</span> <span class="o">{}</span> <span class="o">{</span><span class="n">a</span> <span class="n">l</span><span class="o">}</span> <span class="o">:</span> <span class="n">lex</span> <span class="o">[]</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">rel</span> <span class="o">{</span><span class="n">a₁</span> <span class="n">a₂</span><span class="o">}</span> <span class="o">(</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a₁</span> <span class="n">a₂</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">length</span> <span class="bp">≤</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">length</span><span class="o">)</span> <span class="o">:</span> <span class="n">lex</span> <span class="o">(</span><span class="n">a₁</span> <span class="bp">::</span> <span class="n">l₁</span><span class="o">)</span> <span class="o">(</span><span class="n">a₂</span> <span class="bp">::</span> <span class="n">l₂</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">{</span><span class="n">a</span> <span class="n">l₁</span> <span class="n">l₂</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">lex</span> <span class="n">l₁</span> <span class="n">l₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">lex</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l₁</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l₂</span><span class="o">)</span>
</pre></div>


<p>and <code>ra</code> is actually <code>lt</code></p>

#### [ Kevin Buzzard (Nov 29 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148771981):
<p>I found Chris' notes on well founded recursion very useful for this sort of thing.</p>

#### [ Kevin Buzzard (Nov 29 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148772038):
<p>To get the equation compiler to match on a random thing, you need to explicitly trigger it with the <code>match</code> command. Hang on I'll get to a PC and send some links</p>

#### [ AHan (Nov 29 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148772043):
<p>I have tried to do induction on list<br>
But the lex order I defined doesn't necessarily decrease on the length of the list... I can't apply the induction hypothesis...</p>

#### [ Kevin Buzzard (Nov 29 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148772103):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#match-expressions" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#match-expressions">https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#match-expressions</a> for pattern matching</p>
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md</a> for well-founded recursion</p>

#### [ AHan (Nov 29 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Pattern%20Matching%20or%20Induction%20on%20Lattice%3F/near/148772752):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  Thanks a lot for the sharing!<br>
So I think the main problem here is, I have to prove that something will decrease....<br>
And I have no idea how to prove this.... lol</p>


{% endraw %}
