---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84306undead.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [undead](https://leanprover-community.github.io/archive/113488general/84306undead.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 23 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132629895):
<p>"Undead" is a game from [Simon Tatham's portable puzzle collection] (<a href="https://www.chiark.greenend.org.uk/~sgtatham/puzzles/" target="_blank" title="https://www.chiark.greenend.org.uk/~sgtatham/puzzles/">https://www.chiark.greenend.org.uk/~sgtatham/puzzles/</a>). These games are perfect information one player puzzle games, and often solving a level completely (for me at least, in most of these games) involves finding a constructive proof that there is precisely one solution to the level. I'm probably going to supervise a masters project this coming academic year on games like this, so I thought it was about time I understood what I could do with them in Lean.</p>
<p>Here's a [pic of an undead level] (<a href="http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead_initial.png" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead_initial.png">http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead_initial.png</a>). The diagonal lines in some squares are (two-sided) mirrors. The vacant squares need to be each filled with exactly one of a vampire, ghost or zombie. There are 9 vacant squares and we're told at the top that we need to fill them with three ghosts, three vampires and three zombies. The numbers around the outside of the board are the number of monsters you can see if you look into the board from where the number is, with the caveat that you can't see a ghost directly and you can't see a vampire through a mirror. So for example, the zero on the top row, second from the left, indicates that you can't see the monster in the top left hand corner through a mirror, so it must be a vampire, and the 3 at the left of the top row indicates that exactly one of the monsters in the first column is a ghost (because you can only see three of the four monsters in that column).</p>
<div class="message_inline_image"><a href="http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead_initial.png" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead_initial.png"><img src="https://uploads.zulipusercontent.net/92ef1384545d96f90cc96adcb994bdac8caeb2a5/687474703a2f2f777777662e696d70657269616c2e61632e756b2f7e62757a7a6172642f78656e612f626c6f672f756e646561645f696e697469616c2e706e67"></a></div><p>This sort of game is really easy to model in Lean; like mathematics, it seems to fit very gracefully into the language of dependent type theory. The nine empty squares can be thought of as 9 variables of type <code>square</code> (or type <code>monster</code> or whatever), the 16 numbers and three totals give 19 equations involving these variables, and the two main claims here are (1) that there's a solution to the equations and (2) it's unique.</p>
<p>Here is a formalisation of the level in Lean, plus some preliminary lemmas.</p>
<p><a href="https://gist.github.com/kbuzzard/53712d672a894d7b158a512f7aa5f836" target="_blank" title="https://gist.github.com/kbuzzard/53712d672a894d7b158a512f7aa5f836">https://gist.github.com/kbuzzard/53712d672a894d7b158a512f7aa5f836</a></p>
<p>The lemmas reduce the problem to the following position:</p>
<div class="message_inline_image"><a href="http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead.png" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/xena/blog/undead.png"><img src="https://uploads.zulipusercontent.net/1d14fa6dc9bea88e32196efc36215e0269995eb3/687474703a2f2f777777662e696d70657269616c2e61632e756b2f7e62757a7a6172642f78656e612f626c6f672f756e646561642e706e67"></a></div><p>(and actually a little further because I worked out something about a7 after taking that screenshot). The search space initially has size 3^9, which is a bit big perhaps for Lean, but the lemmas I prove about the solution reduce the space to something like 2^7 * 3, which sounds a bit more reasonable. I think I'd now like to brute force it and get a proof that there's a unique solution, plus a description of the solution, but I'm not sure how to do that in Lean. I have these random facts like "variable a6 isn't a vampire" but I am not sure how to write the procedural code in Lean which will save me from generating a gazillion cases with a6 being a vampire. The issue is that I want to do cases on all 8 remaining variables at once, but for the variables where I've proved something I want to immediately eliminate all cases which contradict what I've proved. Am I making sense? I just want to solve the level now, in Lean, without running out of memory, and ideally I'd like to output the solution. I feel like I've done the lion's share of the work now but I've not quite finished.</p>

#### [ Sean Leather (Aug 23 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132630343):
<p><code>@[derive decidable_eq]</code></p>

#### [ Kevin Buzzard (Aug 23 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132630393):
<p>Oh yeah that was it :-) I derived it myself :-) I think I'd find it easier to remember that if I understood what was going on there. Is this the same as <code>@[simp]</code>? It doesn't look like it.</p>

#### [ Sean Leather (Aug 23 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132630465):
<p><code>init/meta/derive.lean</code> says: “Attribute that can automatically derive typeclass instances.”</p>

#### [ Sean Leather (Aug 23 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132630478):
<p>Maybe that note will also help me remember the syntax. I don't use it very often, so I have to keep looking for it. But if I know that it's an attribute, I know it must be in <code>@[...]</code>.</p>

#### [ Kevin Buzzard (Aug 23 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132655747):
<p>I'm working on square 7. After the line <code>  cases a₂;cases a₃;cases a₅;cases h₇;cases h₁₅,</code> in tactic mode, it's difficult for me to see what happened. Each of the a's has three possibilities, so after the three cases tactics there are now 27 goals. But for most of them (I think) there is a contradiction with assumptions h7 and h15, so after that entire line is processed we are back to one goal (unless I have misunderstood Lean's output). However I don't seem to be able to read off which of the cases we are in. Is there a trick for me to track which of the 27 branches survived?</p>

#### [ Chris Hughes (Aug 23 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132656912):
<p>Prove it's equivalent to proving <code>∃! (a₁ ∈ [vampire, ghost]) (a₂ ∈ [ghost, zmobie]) ...</code> and use dec_trivial. You might have to guide simp a bit, and prove lemmas like <code>a ! = zombie iff a = vampire or a = ghost</code></p>

#### [ Kevin Buzzard (Aug 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657067):
<p>Actually I am now confused about whether I have even done what I think I've done. Is this a bug? What happens if you type this into a Lean file:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">vampire</span> <span class="o">:</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">ghost</span> <span class="o">:</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">zombie</span> <span class="o">:</span> <span class="n">square</span>

<span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">square</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">a</span><span class="bp">;</span><span class="n">cases</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">c</span><span class="bp">;</span><span class="n">cases</span> <span class="n">d</span><span class="o">,</span>
  <span class="n">repeat</span> <span class="o">{</span><span class="n">sorry</span><span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>and then put your cursor just after the end comma in the <code>cases a;cases b,</code> line? I expect to see 9 goals but I only see one. Typing "sorry" makes the next one appear :-) Typing a few sorries eventually sorts things out and then it's back to 9 goals.</p>

#### [ Kevin Buzzard (Aug 23 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657172):
<p>Even weirder:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">vampire</span> <span class="o">:</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">ghost</span> <span class="o">:</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">zombie</span> <span class="o">:</span> <span class="n">square</span>

<span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">square</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">a</span><span class="bp">;</span><span class="n">cases</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">sorry</span><span class="o">,</span>
  <span class="n">sorry</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">c</span><span class="bp">;</span><span class="n">cases</span> <span class="n">d</span><span class="o">,</span>
  <span class="n">repeat</span> <span class="o">{</span><span class="n">sorry</span><span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>After the <code>b,</code> there are 9 cases, after the next sorry there are 8, and after the next one it drops to one. The others are still there, they're just not being displayed for some reason.</p>
<div class="codehilite"><pre><span></span>
</pre></div>

#### [ Chris Hughes (Aug 23 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657277):
<p>It seems to be being parsed as this</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">square</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">a</span><span class="bp">;</span> <span class="o">{</span><span class="n">cases</span> <span class="n">b</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">c</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">d</span><span class="o">,</span>
  <span class="n">repeat</span> <span class="o">{</span><span class="n">sorry</span><span class="o">}},</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Aug 23 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657330):
<p>Actually not quite.</p>

#### [ Gabriel Ebner (Aug 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657422):
<p>I think the <code>;</code> just messes up the information on the current line.  If you put <code>skip,</code> on another line it shows the expected number of goals.</p>

#### [ Gabriel Ebner (Aug 23 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657546):
<p>Information about the goal is stored in a very unstructured form at the moment: essentially there is a function <code>tactic.save_info</code> which stores the corresponding string at a user-specified position (= line/column pair, and yes this can be almost anywhere..).</p>

#### [ Kevin Buzzard (Aug 23 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657821):
<p>If you put <code>skip</code> then on the line <em>before</em> the <code>skip</code> it displays correctly. So perhaps it's the second semicolon which is causing the confusion.</p>

#### [ Gabriel Ebner (Aug 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132657983):
<p>Yes, the semicolon seems to break the goal output between the surrounding commas.  If you add a <code>skip,</code> then you add a comma which keeps the breakage away.</p>

#### [ Patrick Massot (Aug 23 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132660215):
<p>I've noticed repeatedly that using semi-colon is very confusing in this way</p>

#### [ Patrick Massot (Aug 23 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132660271):
<p>About the general problem, isn't something that could be handled entirely by the type class system? It looks like problem designed for solving using prolog.</p>

#### [ Andrew Ashworth (Aug 23 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132660854):
<p>i believe sebastian solved the n-queens problem using type classes</p>

#### [ Andrew Ashworth (Aug 23 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132660967):
<p>this is really an abuse of inference I think :)</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661039):
<blockquote>
<p>Prove it's equivalent to proving <code>∃! (a₁ ∈ [vampire, ghost]) (a₂ ∈ [ghost, zmobie]) ...</code> and use dec_trivial. You might have to guide simp a bit, and prove lemmas like <code>a ! = zombie iff a = vampire or a = ghost</code></p>
</blockquote>
<p>So how does <code>dec_trivial</code> work? Does it look at hypotheses? Why doesn't this work:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">decidable_eq</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">vampire</span> <span class="o">:</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">ghost</span> <span class="o">:</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">zombie</span> <span class="o">:</span> <span class="n">square</span>

<span class="kn">open</span> <span class="n">square</span>

<span class="kn">lemma</span> <span class="n">thing</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">square</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">vampire</span> <span class="bp">∨</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">ghost</span> <span class="bp">∨</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">zombie</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>
</pre></div>


<p>It looks pretty decidably trivial to me. How can I make this work?</p>

#### [ Chris Hughes (Aug 23 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661087):
<p>Prove fintype square</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661203):
<p><code>@[derive fintype]</code>?</p>

#### [ Kenny Lau (Aug 23 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661276):
<p>look at my <code>three</code> elsewhere lol</p>

#### [ Patrick Massot (Aug 23 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661277):
<p>What is this derive? I see this from time to time but never know what it means</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661358):
<p>What I wrote doesn't work.</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661371):
<p><code>failed to find a derive handler for 'fintype'</code></p>

#### [ Andrew Ashworth (Aug 23 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661688):
<p>I believe the derive stuff is user-written extensions that add functionality to a type. like <code>@[derive decidable_eq]</code> adds an automatically generated instance saying that the type is decidable</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661874):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">finset_square</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">square</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">val</span> <span class="o">:=</span> <span class="o">[</span><span class="n">vampire</span><span class="o">,</span><span class="n">ghost</span><span class="o">,</span><span class="n">zombie</span><span class="o">],</span>
  <span class="n">nodup</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">repeat</span> <span class="o">{</span><span class="n">constructor</span><span class="o">,</span><span class="n">intro</span> <span class="n">a</span><span class="o">,</span><span class="n">cases</span> <span class="n">a</span><span class="o">,</span><span class="n">repeat</span> <span class="o">{</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">}},</span>
    <span class="n">constructor</span><span class="o">,</span>
  <span class="kn">end</span>
<span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">square</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">elems</span> <span class="o">:=</span> <span class="n">finset_square</span><span class="o">,</span>
  <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span><span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span><span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="o">}</span>
</pre></div>


<p>:-)</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661922):
<p>I reckon that could be automated...</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132661973):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">three</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">elems</span> <span class="o">:=</span> <span class="o">{</span><span class="n">A</span><span class="o">,</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span><span class="o">},</span>
  <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">}</span>
</pre></div>


<p>Kenny's <code>three</code></p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662313):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">decidable_eq</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">vampire</span> <span class="o">:</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">ghost</span> <span class="o">:</span> <span class="n">square</span>
<span class="bp">|</span> <span class="n">zombie</span> <span class="o">:</span> <span class="n">square</span>

<span class="kn">open</span> <span class="n">square</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">square</span> <span class="o">:=</span> <span class="o">{</span>
  <span class="n">elems</span> <span class="o">:=</span> <span class="o">{</span><span class="n">vampire</span><span class="o">,</span><span class="n">ghost</span><span class="o">,</span><span class="n">zombie</span><span class="o">},</span>
  <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span><span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span><span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="o">}</span>

<span class="kn">open</span> <span class="n">square</span>

<span class="kn">lemma</span> <span class="n">thing2</span> <span class="o">:</span> <span class="bp">∃!</span> <span class="n">a</span> <span class="o">:</span> <span class="n">square</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">vampire</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>
</pre></div>


<p>That looks pretty trivial too. Error is</p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
⊢ decidable (∃! (a : square), a = vampire)
</pre></div>

#### [ Kenny Lau (Aug 23 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662380):
<p>you need to import something iirc</p>

#### [ Chris Hughes (Aug 23 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662383):
<p><code>unfold exists_unique</code> first</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662611):
<p>rofl I just tried it for the actual problem and I got this error: <a href="https://gist.github.com/kbuzzard/84dbdf0fab4b96148099f49ac4f1770e" target="_blank" title="https://gist.github.com/kbuzzard/84dbdf0fab4b96148099f49ac4f1770e">https://gist.github.com/kbuzzard/84dbdf0fab4b96148099f49ac4f1770e</a> . I think I've seen this before when you do exists_unique with multiple variables, it unfolds to something quite unwieldy.</p>

#### [ Patrick Massot (Aug 23 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662675):
<p>nice goal!</p>

#### [ Kevin Buzzard (Aug 23 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662688):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∃!</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">c</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">exists_unique</span><span class="o">,</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">∃ (x : ℕ),</span>
<span class="cm">    (∃ (x_1 : ℕ),</span>
<span class="cm">         (∃ (x_2 : ℕ), x + x_1 + x_2 = 0 ∧ ∀ (y : ℕ), x + x_1 + y = 0 → y = x_2) ∧</span>
<span class="cm">           ∀ (y : ℕ),</span>
<span class="cm">             (∃ (x_1 : ℕ), x + y + x_1 = 0 ∧ ∀ (y_1 : ℕ), x + y + y_1 = 0 → y_1 = x_1) → y = x_1) ∧</span>
<span class="cm">      ∀ (y : ℕ),</span>
<span class="cm">        (∃ (x : ℕ),</span>
<span class="cm">           (∃ (x_1 : ℕ), y + x + x_1 = 0 ∧ ∀ (y_1 : ℕ), y + x + y_1 = 0 → y_1 = x_1) ∧</span>
<span class="cm">             ∀ (y_1 : ℕ),</span>
<span class="cm">               (∃ (x : ℕ), y + y_1 + x = 0 ∧ ∀ (y_2 : ℕ), y + y_1 + y_2 = 0 → y_2 = x) → y_1 = x) →</span>
<span class="cm">        y = x</span>
<span class="cm">-/</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Aug 23 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662703):
<p>Does it have to do that? Why not just "exists a b c, a + b + c = 0 and forall a' b' c', a' + b' + c' = 0 implies a=a' and b=b' and c=c'"?</p>

#### [ Chris Hughes (Aug 23 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132662959):
<p>It's parsed as a load of nested <code>exists_uniques</code>. I imagine your definition is quite hard to write</p>

#### [ Reid Barton (Aug 23 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663069):
<p>Wait, does it even mean the right thing then?</p>

#### [ Reid Barton (Aug 23 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663141):
<p>Isn't this "there exists a unique a such that there exists a unique b such that ...", but maybe for some other a there's multiple b's which would work, and so there isn't actually a unique (a,b,c)</p>

#### [ Reid Barton (Aug 24 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663480):
<p>Say <code>P x y</code> holds if and only if (x, y) is (1, 2) or (3, 4) or (3, 5). Then <code>∃! x y, P x y = ∃! x, ∃! y, P x y</code> is true because <code>∃! y, P x y</code> holds only for x = 1.</p>

#### [ Reid Barton (Aug 24 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663491):
<p>But I'm sure what you really wanted is <code>∃! p, P p.1 p.2</code>.</p>

#### [ Patrick Massot (Aug 24 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663542):
<p>That's a pretty nasty trap</p>

#### [ Sebastian Ullrich (Aug 24 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663616):
<p><em>makes note to remove this "feature" as soon as possible</em></p>

#### [ Kevin Buzzard (Aug 24 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663779):
<p>I think I once tried to prove exactly the goal above and decided at the end of it that it seemed to be an extremely roundabout way of saying the correct thing.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663910):
<p>I think it unfolds to something more complicated than what Reid is suggesting.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663916):
<p>In particular I'm suggesting that Chris' comment is oversimplifying the matter.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132663971):
<p>Here's an example of an intermediate goal that you have to prove when proving the exists_unique statement above:</p>
<div class="codehilite"><pre><span></span>y : ℕ,
h : ∃ (x : ℕ), 0 + y + x = 0 ∧ ∀ (y_1 : ℕ), 0 + y + y_1 = 0 → y_1 = x
⊢ y = 0
</pre></div>

#### [ Reid Barton (Aug 24 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664036):
<p>This is after you set a and b to 0, right?</p>

#### [ Reid Barton (Aug 24 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664041):
<p>You shouldn't be given the <code>∀ (y_1 : ℕ), 0 + y + y_1 = 0 → y_1 = x</code> part of the hypothesis</p>

#### [ Reid Barton (Aug 24 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664053):
<p>I think. Actually staring at this is making me confused.</p>

#### [ Reid Barton (Aug 24 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664101):
<p>But in general, the way that Lean interprets <code>∃! x y, ...</code> is as <code>∃! x, ∃! y, ...</code>, right?</p>

#### [ Mario Carneiro (Aug 24 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664341):
<blockquote>
<p>Description: An alternate definition of double existential uniqueness (see 2eu4 2371). A mistake sometimes made in the literature is to use ∃!𝑥∃!𝑦 to mean "exactly one 𝑥 and exactly one 𝑦." (For example, see Proposition 7.53 of [TakeutiZaring] p. 53.) It turns out that this is actually a weaker assertion, as can be seen by expanding out the formal definitions. This theorem shows that the erroneous definition can be repaired by conjoining ∀𝑥∃* 𝑦𝜑 as an additional condition. The correct definition apparently has never been published. (∃* means "exists at most one.")</p>
</blockquote>
<p><a href="http://us.metamath.org/mpeuni/2eu5.html" target="_blank" title="http://us.metamath.org/mpeuni/2eu5.html">http://us.metamath.org/mpeuni/2eu5.html</a></p>

#### [ Reid Barton (Aug 24 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664344):
<p>You want to prove (0, 0, 0) is the unique solution (let's say). Then you ought to be able to prove</p>
<div class="codehilite"><pre><span></span><span class="n">y</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="mi">0</span> <span class="bp">+</span> <span class="n">y</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span>
<span class="err">⊢</span> <span class="n">y</span> <span class="bp">=</span> <span class="mi">0</span>
</pre></div>

#### [ Mario Carneiro (Aug 24 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664437):
<p>the simplest way to assert multiple existential uniqueness is to claim unique existence of a triple</p>

#### [ Mario Carneiro (Aug 24 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132664553):
<p>also: why are you using lean as a sat solver? It's not particularly smart for this</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132665771):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> you might like this challenge:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">∃</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="n">p</span> <span class="n">m</span> <span class="n">n</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">p</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">∧</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">n</span><span class="o">))</span> <span class="bp">↔</span> <span class="bp">∃!</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">p</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Mario -- did I get this right? I just spent 15 minutes on it and failed to do one way; I don't want to waste Kenny's time. </p>
<p>I'm using Lean as a whatever-you-said because I'm trying to figure out what can and can't and should be done using Lean when it comes to puzzles like this.</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132665962):
<p>as Reid points out, as well as the quote I gave, that theorem is false</p>

#### [ Reid Barton (Aug 24 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666080):
<p>There are other tools out there which are a better fit for these kinds of constraint satisfaction problems. One of which even shares an author with Lean.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666081):
<p>right, I just went back to it and figured that it couldn't possibly be provable.</p>

#### [ Reid Barton (Aug 24 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666088):
<p>However, you can't beat the convenience of already knowing the input language.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666093):
<p>In which case I don't understand what this exists_unique even means.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666142):
<p>I could solve this undead puzzle in python just with some dull loop. I was trying to work out what Lean could offer me that python couldn't.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666168):
<p>So Lean really does do what Chris says? "There exists a unique x such that there exists a unique y such that..."? That's not what I would have guessed from the notation.</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666375):
<div class="codehilite"><pre><span></span>example : ¬ ∀ (p : ℕ → ℕ → Prop),
  (∃ m n, p m n ∧ (∀ b c : ℕ, p b c → b = m ∧ c = n)) ↔ ∃! m n : ℕ, p m n :=
λ H, begin
  let p := λ m n, m = 0 → n = 0,
  have : ∃! m n : ℕ, p m n,
  { refine ⟨0, ⟨0, λ _, rfl, λ n h, h rfl⟩, λ m h, _⟩,
    rcases h with ⟨m&#39;, h₁, h₂⟩,
    by_contra h,
    have := h₂ 1 h.elim,
    rw ← h₂ 0 (λ _, rfl) at this,
    cases this },
  rcases (H _).2 this with ⟨m, n, h₁, h₂⟩,
  simpa [(h₂ 0 0 id).1.symm] using h₂ 1 1 id
end
</pre></div>

#### [ Mario Carneiro (Aug 24 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666391):
<p>this is what all nested binders are unfolded to in lean</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666452):
<p>in most cases it works brilliantly - forall, exists, indexed union, supremum, infinite sum... it is only exists unique which doesn't have a nice interpretation</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666531):
<p>rofl</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">p</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">4</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">silly</span> <span class="o">:</span> <span class="bp">∃!</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">existsi</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">left</span><span class="o">,</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span><span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span><span class="o">,</span><span class="n">exact</span> <span class="n">H</span><span class="o">,</span><span class="n">cases</span> <span class="n">H</span><span class="o">,</span><span class="n">cases</span> <span class="n">H</span><span class="o">,</span><span class="n">cases</span> <span class="n">H_left</span><span class="o">,</span><span class="n">cases</span> <span class="n">H</span><span class="o">,</span><span class="n">cases</span> <span class="n">H_left</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">y</span> <span class="n">Hy</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">p</span> <span class="n">at</span> <span class="n">Hy</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">Hy</span> <span class="k">with</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">Hx</span> <span class="k">with</span> <span class="n">H</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span><span class="o">,</span><span class="n">exact</span> <span class="n">H</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span><span class="o">,</span><span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">Hy</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="n">at</span> <span class="n">H1</span><span class="o">,</span><span class="n">rw</span> <span class="n">Hx</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">H1</span> <span class="mi">4</span><span class="o">,</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="mi">4</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">,</span>
    <span class="n">revert</span> <span class="n">this</span><span class="o">,</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">H</span><span class="o">,</span><span class="n">rw</span> <span class="n">Hy</span><span class="o">,</span><span class="n">simp</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">Hy</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="n">dsimp</span> <span class="n">at</span> <span class="n">H1</span><span class="o">,</span><span class="n">rw</span> <span class="n">Hx</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">H1</span> <span class="mi">3</span><span class="o">,</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">=</span> <span class="mi">4</span><span class="o">,</span>
    <span class="n">revert</span> <span class="n">this</span><span class="o">,</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">H</span><span class="o">,</span><span class="n">rw</span> <span class="n">Hy</span><span class="o">,</span><span class="n">simp</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Aug 24 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666593):
<p>I had no idea <code>∃!</code> meant that in Lean. That is for me a very surprising design decision. <code>∃! a b</code> doesn't even mean the same as <code>∃! b a</code>, right?</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666599):
<p>no, they are not logically equivalent</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666608):
<p>frankly the problem is that <code>∃!</code> is a shitty binder notation</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666610):
<p>wo</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666611):
<p>w</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666618):
<p>it's not monotone</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666626):
<p>So in fact the thing I'm trying to prove with this undead thing is not even formulated correctly.</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666669):
<p>like I said, the easy way to say this without having to think much is to use exists unique in a pair type</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666698):
<p>I don't care what Lean thinks <code>∃!</code> means. All I want to say is that there exists a unique 9-tuple with some property, and I've just realised that I'd better spell it out rather than using this terrifying notation.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666757):
<p>I wonder if any of the mathematicians here can find a mathematician who thinks <code>∃! a b, p a b</code> means anything other than what I suggested it meant above with that false lemma.</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666837):
<p>I see. The reason this has happened is that Lean has one inbuilt system for dealing with multiple variables with one binder, and to put it bluntly it doesn't work with this one, so really perhaps a different system should be used for this one binder and that might be what Sebastian was saying. Maybe I've caught up at last.</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132666999):
<blockquote>
<p>I wonder if any of the mathematicians here can find a mathematician who thinks ∃! a b, p a b means anything other than what I suggested it meant above with that false lemma.</p>
</blockquote>
<p>Most mathematicians think ∃! a b, p a b means what you wrote. They also think that ∃! a, ∃! b, p a b encodes this statement, and they are wrong</p>

#### [ Mario Carneiro (Aug 24 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132667051):
<p>it is obvious once you give it more than a cursory examination, but it's one of those things that often escapes notice</p>

#### [ Kevin Buzzard (Aug 24 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead/near/132667177):
<blockquote>
<p>Most mathematicians think ∃! a b, p a b means what you wrote. They also think that ∃! a, ∃! b, p a b encodes this statement, and they are wrong</p>
</blockquote>
<p>I don't think I'd ever even considered the concept <code>∃! a, ∃! b, p a b</code> until this evening and I suspect that many mathematicians would also not have come across it. It looks very weird to me. Of course, hindsight is a wonderful thing...</p>


{% endraw %}
