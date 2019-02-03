---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13549Accesibilityoflexicalorderoflists.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Accesibility of lexical order of lists](https://leanprover-community.github.io/archive/113489newmembers/13549Accesibilityoflexicalorderoflists.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ AHan (Nov 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148644364):
<p>I've seen there are proofs for accessibility and well-founded for lexical order of product<br>
And I also find out there is a definition for lexical order of list, but I can't find any proofs for it's accessibility and well-founded...<br>
Are them provided in other names or just not yet proved?</p>
<p>And if I were going to prove the accessibility of lexical order of list, I'm not quite sure what the type of the lemma should be, and when to use functions like acc.rec_on, acc.intro....<br>
( Is the type of the lemma like... this ?)</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">ra</span>  <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="n">def</span> <span class="n">list_lex_acc</span> <span class="o">:</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="n">ra</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span><span class="o">)</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Nov 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148646910):
<p>Nice question! If you write <code> ```lean </code> when quoting code then you get syntax highlighting as well. Here's a version of your question which typechecks straight out the box:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="kn">theorem</span> <span class="n">list_lex_acc</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="n">ra</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span><span class="o">)</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Nov 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647290):
<p>Off the top of my head, I guess some useful lemmas would be to prove that there are no solutions to <code>x &lt; []</code>, and then you could start proving that all lists of positive size were accessible by induction on first the length of the list, and secondly using well-founded induction on the first element of the list.</p>

#### [ AHan (Nov 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647442):
<p>Thanks for the suggestion!<br>
And are there any differences between using <code>def</code> and  <code>theorem</code> here ?<br>
Because in mathlib they used <code>def</code> for well_founded and accessibility of lexical order of product</p>

#### [ AHan (Nov 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647627):
<p>"well-founded induction" do you mean something like <code>well_founded.rec_on</code>?</p>

#### [ Reid Barton (Nov 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647639):
<p>I think you mean in the Lean core library (<code>def lex_wf (ha : well_founded ra) (hb : well_founded rb) : well_founded (lex ra rb) := ...</code>)?</p>

#### [ Reid Barton (Nov 27 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647724):
<p>There is a difference. I don't know why they used <code>def</code>, though</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647756):
<p>I just used theorem because the thing you want to prove has type Prop.</p>

#### [ AHan (Nov 27 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148647839):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>  Yes!</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648088):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_lt_empty</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">¬</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span> <span class="n">a</span> <span class="o">[])</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">intro</span> <span class="n">H</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">H</span>
</pre></div>


<p>There will be shorter proofs :-) I'm doing induction on <code>list.lex</code> here.</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648210):
<p>got it:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_lt_empty</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">¬</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span> <span class="n">a</span> <span class="o">[])</span> <span class="bp">.</span>
</pre></div>

#### [ Kevin Buzzard (Nov 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648277):
<p>oh no wait, lean segfaulted :D</p>

#### [ AHan (Nov 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648310):
<p>I can solve this case by</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">list_lex_acc</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="n">ra</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span><span class="o">)</span> <span class="n">a</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">a</span><span class="o">,</span>
<span class="k">begin</span>
    <span class="n">cases</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">acc</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span> <span class="n">intros</span><span class="o">,</span> <span class="n">cases</span> <span class="n">a</span><span class="o">,</span>
<span class="bp">...</span>
<span class="kn">end</span>
</pre></div>


<p>but I'm stuck at the second part, doing well-founded induction on the first element of the list...</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648514):
<p>Yeah it's messy now. I am at work and need to think about other things :-/</p>
<p>This <code>.</code> proof works for me.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">not_lt_empty</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">¬</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span> <span class="n">a</span> <span class="o">[])</span> <span class="bp">.</span>
</pre></div>

#### [ AHan (Nov 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648760):
<p>Wow.... what's <code>.</code> proof ...</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648767):
<p>But this exact file gives me a segfault:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="kn">theorem</span> <span class="n">list_lex_acc</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="n">ra</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span><span class="o">)</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">not_lt_empty</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">¬</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span> <span class="n">a</span> <span class="o">[])</span> <span class="bp">.</span>
</pre></div>


<p>with <code>Lean (version 3.4.1, commit 17fe3decaf8a, Release)</code>.</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648809):
<p>The <code>.</code> proof says "Check all the cases...actually, can't you see that there are no cases to check?". The equation compiler looks at all the constructors for <code>list.lex</code> and rules out <code>[]</code> appearing on the right hand side.</p>

#### [ Reid Barton (Nov 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648818):
<p>Doesn't segfault for me with the same version of lean</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648875):
<p>I have a blank line 9</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148648906):
<p>I can restart Lean and consistently get it to segfault. On linux.</p>

#### [ AHan (Nov 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148649005):
<p>No segfault with the same version of lean either... (on windows</p>

#### [ Kevin Buzzard (Nov 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148649143):
<p>I restarted VS Code and the problem has gone away <em>shrug</em></p>

#### [ AHan (Nov 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148649741):
<p>Oh I crashed on</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">ra</span>  <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">list_lex_acc</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="n">ra</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span><span class="o">)</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">not_lt_empty</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span> <span class="n">a</span> <span class="o">[])</span> <span class="bp">.</span>
</pre></div>


<p>but it works fine if I swap the lemma and the theorem...</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">ra</span>  <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">not_lt_empty</span> <span class="o">(</span><span class="n">ra</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span> <span class="n">a</span> <span class="o">[])</span> <span class="bp">.</span>

<span class="kn">theorem</span> <span class="n">list_lex_acc</span> <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="n">ra</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="n">acc</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">lex</span> <span class="n">ra</span><span class="o">)</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Nov 27 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148662338):
<p>Hmm. I think I found an infinite decreasing sequence! <code>[1] &gt; [0,1] &gt; [0,0,1] &gt; [0,0,0,1] &gt; ...</code>. So that will be why it's not in the library.</p>

#### [ Mario Carneiro (Nov 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148664949):
<p>Interesting. I think it's well founded if you reverse the order: <code>[] &lt; x :: xs</code>, and <code>x :: xs &lt; y :: ys</code> if <code>xs &lt; ys</code> or <code>xs = ys</code> and <code>x &lt; y</code></p>

#### [ Kenny Lau (Nov 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148664978):
<p>I don't recall having a "list" operation on ordinals...</p>

#### [ Kenny Lau (Nov 27 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665001):
<p>it would be <code>list(x) = 1 + x + x^2 + x^3 + ...</code></p>

#### [ Mario Carneiro (Nov 27 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665002):
<p>I do: <code>CNF</code> (although I don't see the relevance)</p>

#### [ Kenny Lau (Nov 27 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665062):
<p>but then it would be <code>list(x) = x^omega</code> but power in ordinal doesn't correspond to power in cardinal</p>

#### [ Mario Carneiro (Nov 27 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665114):
<p>right, I think the list ordering I gave has order type <code>(type A)^omega</code></p>

#### [ Kenny Lau (Nov 27 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665175):
<p>so it wouldn't be correct</p>

#### [ Kenny Lau (Nov 27 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665189):
<p>because there is no <code>x^cardinal.omega</code> in ordinals</p>

#### [ Mario Carneiro (Nov 27 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665327):
<p>what are you talking about?</p>

#### [ Mario Carneiro (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665346):
<p><code>x^omega</code> is perfectly well defined</p>

#### [ Mario Carneiro (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665354):
<p>it's an ordinal power</p>

#### [ Kenny Lau (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665377):
<p>but is it in bijection with <code>x^cardinal.omega</code>?</p>

#### [ Mario Carneiro (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665384):
<p>no... it's lists not infinite sequences</p>

#### [ Kenny Lau (Nov 27 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665391):
<p>ah</p>

#### [ Kenny Lau (Nov 27 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148665447):
<blockquote>
<p>Interesting. I think it's well founded if you reverse the order: <code>[] &lt; x :: xs</code>, and <code>x :: xs &lt; y :: ys</code> if <code>xs &lt; ys</code> or <code>xs = ys</code> and <code>x &lt; y</code></p>
</blockquote>
<p>feels like hilbert basis theorem now</p>

#### [ AHan (Nov 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148693519):
<p>So maybe we'll need a different definition for the lexical order of list in order to prove it's well-founded?</p>

#### [ AHan (Nov 29 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148780207):
<p>I ‘ve modified the lex of list as below</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">lattice</span>
<span class="kn">open</span> <span class="n">lattice</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">ra</span>  <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">inductive</span> <span class="n">lex</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">nil</span> <span class="o">{}</span> <span class="o">{</span><span class="n">a</span> <span class="n">l</span><span class="o">}</span> <span class="o">:</span> <span class="n">lex</span> <span class="o">[]</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">rel</span> <span class="o">{</span><span class="n">a₁</span> <span class="n">a₂</span><span class="o">}</span> <span class="o">(</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a₁</span> <span class="n">a₂</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">length</span> <span class="bp">≤</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">length</span><span class="o">)</span> <span class="o">:</span> <span class="n">lex</span> <span class="o">(</span><span class="n">a₁</span> <span class="bp">::</span> <span class="n">l₁</span><span class="o">)</span> <span class="o">(</span><span class="n">a₂</span> <span class="bp">::</span> <span class="n">l₂</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">{</span><span class="n">a</span> <span class="n">l₁</span> <span class="n">l₂</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">lex</span> <span class="n">l₁</span> <span class="n">l₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">lex</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l₁</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l₂</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">lex_acc_of_lex</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="n">lex</span> <span class="n">ra</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">acc</span> <span class="o">(</span><span class="n">lex</span> <span class="n">ra</span><span class="o">)</span> <span class="n">a</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">[]</span> <span class="n">h</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">h</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="bp">_</span> <span class="n">h</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply</span> <span class="n">list_nil_acc</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">l₁</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="bp">::</span> <span class="n">l₂</span><span class="o">)</span> <span class="n">h</span> <span class="o">:=</span>  <span class="n">sorry</span>
</pre></div>


<p>But I don't know how to tell lean that the recursion application will decrease....</p>

#### [ Kenny Lau (Nov 29 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accesibility%20of%20lexical%20order%20of%20lists/near/148782527):
<p>prove it? lol</p>


{% endraw %}
