---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61646Unfoldingcarefully.html
---

## Stream: [general](index.html)
### Topic: [Unfolding carefully](61646Unfoldingcarefully.html)

---


{% raw %}
#### [ Moses Schönfinkel (Apr 11 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124924517):
<p>Suppose I have the following goal <code>f a = c (f (d a))</code>. What I am looking to do is to <code>unfold1 f</code> but only on the left hand side. Currently I do <code>generalize hack : f (d a) = x, unfold1 f, rw &lt;- hack</code>. Apart from the fact that it's a hack, the <code>generalize</code> takes a couple of seconds to execute. I tried using <code>conv { to_lhs ... }</code> but <code>unfold1</code> is not an option in conv (and simp fails with deterministic timeout). a) Why on Earth is <code>generalize</code> so slow in this case - is it because <code>c</code> is some horrible dependently typed function with explicit well founded termination proofs? b) Is there a nicer trick to invoke <code>unfold1</code> on left hand side only?</p>

#### [ Kenny Lau (Apr 11 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124924577):
<p>use <code>change</code>?</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124924634):
<p>that would involve me having to explicitly state the effect of unfolding if I understand your suggestion; right?</p>

#### [ Simon Hudon (Apr 11 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124932179):
<p>What about using transitivity instead of generalize?</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933566):
<p>ooh that is actually brilliant! what I ended up doing is something I'm ashamed of but it saves me 15 seconds on each recompile - I reformulated the lemma such that it contains a pre-generalized expression and an equality (which I will, of course, change now :P)</p>

#### [ Simon Hudon (Apr 11 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933627):
<p>Great! Glad to be of help! So, the way I use <code>transitivity</code> to protect parts of my formulas is to do <code>transitivity, blah, blah, refl</code></p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933640):
<p>Yeah I have never thought of that. Thanks a lot. I wish <code>conv</code> was a bit less constrained.</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933693):
<p>if this worked, then <code>conv { to_lhs, dsimp1 f }</code> would be just fine for me - but <code>interactive.conv.*</code> only has a bunch of tactics for reasons I'm not sure I want to know about :P</p>

#### [ Simon Hudon (Apr 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933694):
<p>If you have something more specific that you want to use, let's say <code>g</code> instead of <code>=</code>, you can also make your own protection lemmas:</p>
<div class="codehilite"><pre><span></span>lemma protect (x y : α) (z : β)
  (h : x = y)
  (h : g y z)
: g x z := ...
</pre></div>


<p>This allows you to select exactly what part of the formula you want to rewrite when you expect something very specific. And <code>z</code> is protected.</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933756):
<p>ah, right; this is basically the general version that I ended up doing, but I think the transitivity is such a neat hack :P</p>

#### [ Simon Hudon (Apr 11 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933767):
<blockquote>
<p>if this worked, then <code>conv { to_lhs, dsimp1 f }</code> would be just fine for me - but <code>interactive.conv.*</code> only has a bunch of tactics for reasons I'm not sure I want to know about :P</p>
</blockquote>
<p>I think Coq is more targeted like that <code>rewrite h at 1,3</code>. I found I missed that at first but I'm not sure it makes for stable proofs</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933776):
<p>yes, in Coq I can rewrite where I want</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933779):
<p>I can also rewrite under binders</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933780):
<p>(with setoid rewrites)</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933785):
<p>in Lean I've only used <code>simp</code> to rewrite under binders, not sure how else it can be even done</p>

#### [ Simon Hudon (Apr 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933788):
<p><code>simp</code> helps there with binders and congruence lemmas but it's a bit less controlled</p>

#### [ Simon Hudon (Apr 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933835):
<p>... yeah, exactly</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933842):
<p>stability of proofs has never been an issue for me, because, I, urm... write them once and then I... forget about them...</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933846):
<p>I may need to try to write Coq in "industrial" settings :P</p>

#### [ Simon Hudon (Apr 11 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933853):
<p>Question: I've only used Coq as a noob so I never experienced scaling up proofs that uses the <code>at 1,3</code> notation. Do you find that your proofs breaks a lot when you do that?</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933855):
<p>yes, they do</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933858):
<p>it's the absolute worst thing one can do</p>

#### [ Simon Hudon (Apr 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933923):
<p>In my temporal logic tactics language, I have played with a tactic you call as <code>rw_using : f x = g x, { /- proof -/ }</code>. For some reason, I liked not clearing a temporary assumption.</p>

#### [ Simon Hudon (Apr 11 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933971):
<p>In temporal logic, that was doubly useful because the proof of equality was typically done in normal Lean logic</p>

#### [ Simon Hudon (Apr 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933979):
<p>Otherwise, I really haven't found a drop in replacement for that Coq notation</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124933983):
<p>I wish I understood exactly how <code>simp</code> works but I have never had the willpower to look at it</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934025):
<p>I believe it's been modeled to resemble the Isabelle heuristics you get when you're within a single <code>theory</code> section thing</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934037):
<p>where <code>theory</code> just aggregates a set of related constants, definitions, proofs, etc. and you abuse this implicit relation in automation</p>

#### [ Simon Hudon (Apr 11 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934038):
<p>I feel like I really don't understand what Isabelle does with any given proof. It's hard for me to understand that comparison</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934081):
<p>you basically help guide automation in Isabelle by aggregating related stuff together in "theories", which is something like making a hint database in Coq</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934160):
<p>(so like a beefy namespace that implicitly provides hints for automation)</p>

#### [ Simon Hudon (Apr 11 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934166):
<p>Ah I see. Does it make things clearer to use the theories or the databases?</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934172):
<p>databases are less implicit so you have to go over the trouble of creating them</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934174):
<p>so in Isabelle you get nice behaviour by default but it's less controlled because it's just "whatever you put in this theory"</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934230):
<p>I think people with purely math background would have easier time using Isabelle, simply because you get nice implicit heuristic-guided behaviour out of the box (+ the Sledgehammer)</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934236):
<p>if I understand Kevin correctly, he uses Lean because he wants dependent types</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934246):
<p>(or I should say, he's not using Isabelle because he wants dependent types)</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934254):
<p>and <code>simp</code> in Lean takes after Isabelle default simplifier, I believe</p>

#### [ Simon Hudon (Apr 11 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934307):
<p>Any chance that something like sledgehammer would work with dependent types? Or is it more of a matter of structuring databases like Isabelle?</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934321):
<p>it would work, Sledgehammer is almost like an outside tool that ships proof obligations to SMT solvers and ATPs</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934329):
<p>Sledgehammer is really the most unimpressive piece of Isabelle; it just tries to invoke every automating algorithm it can get its grabby mittens on</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934605):
<p>That may be the understatement of the century</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934614):
<p>:D</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934637):
<p>Sledgehammer is the result of a multi-year research project that produced a good amount of papers <a href="http://www.cl.cam.ac.uk/~lp15/papers/Automation/" target="_blank" title="http://www.cl.cam.ac.uk/~lp15/papers/Automation/">http://www.cl.cam.ac.uk/~lp15/papers/Automation/</a></p>

#### [ Sebastian Ullrich (Apr 11 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124934693):
<p>The hard parts are relevance filtering of lemmas to pass to the external solver, and of course translating between HOL and FOL</p>

#### [ Moses Schönfinkel (Apr 11 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124936062):
<p>ok ok I will change it to 2 out of 10 on the scale of impressiveness, making it the second least impressive Isabelle feature right after its bundled development IDE <span class="emoji emoji-1f600" title="grinning">:grinning:</span></p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947660):
<p>I use Lean because when I had never heard of any theorem provers apart from Coq, and never used any at all, I watched a live stream of Tom Hales in Cambridge talking about (amongst other things) FAbstracts, and someone asked him which language he would be using, and he said "...Lean?" and I thought "OK that'll do for me"</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947669):
<p>and I certainly didn't know what a dependent type was at that point</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947672):
<p>I just decided to jump in</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947753):
<blockquote>
<p>I wish I understood exactly how <code>simp</code> works but I have never had the willpower to look at it</p>
</blockquote>
<p>I wish I understood more about how <code>simp</code> works but I learnt a couple of <code>set_option</code> options and wrote <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md</a></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124947824):
<p>Looking at the output of <code>set_option trace.simplify true</code> gave me some sort of idea about the absolute inanity of what simp was doing</p>

#### [ Chris Hughes (Apr 11 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948004):
<blockquote>
<blockquote>
<p>I wish I understood exactly how <code>simp</code> works but I have never had the willpower to look at it</p>
</blockquote>
<p>I wish I understood more about how <code>simp</code> works but I learnt a couple of <code>set_option</code> options and wrote <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md</a></p>
</blockquote>
<p>That bit at the end sounds interesting. Does that mean if I had <code>a + b ≡ c [MOD n]</code> and <code>h : a ≡ d [MOD n]</code> I could rewrite to get <code>a + d ≡ c [MOD n]</code>? How would that work with complicated examples, with lots of addition and multiplication?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948228):
<p>I have never used that MOD business so I'm not sure</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948232):
<p>Oh, Gabriel said that</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948276):
<p>I didn't understand it so I didn't use it</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948281):
<p>[and you mean d + b = c of course]</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948297):
<p>Aah but I do remember that this might work in calc mode.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948305):
<p>If your relation is tagged with trans then I think calc supports it</p>

#### [ Chris Hughes (Apr 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948370):
<p>Can I mix equality and an congruences in calc?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948374):
<p>I haven't ever seen this done</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948382):
<p>I think that either in the reference manual or in TPIL they are pretty formal about what you can do with calc</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948467):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html#calculational-proofs" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html#calculational-proofs">https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html#calculational-proofs</a></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948471):
<p>searching TPIL for calc doesn't find that</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948475):
<p>so I always look at <a href="https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/calc.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/calc.md">https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/calc.md</a></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948494):
<p>and indeed there is an example with different operators, = and &lt; and &lt;=</p>

#### [ Patrick Massot (Apr 11 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948495):
<blockquote>
<p>searching TPIL for calc doesn't find that</p>
</blockquote>
<p>It does actually, but you don't recognize it</p>

#### [ Patrick Massot (Apr 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948549):
<p>3rd result</p>

#### [ Patrick Massot (Apr 11 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948575):
<p>I know this because I filled  a Sphinx bug report before understanding this <span class="emoji emoji-1f633" title="flushed">:flushed:</span></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948619):
<p>Oh! So "It's somewhere in Chapter 4" is the best I get?</p>

#### [ Patrick Massot (Apr 11 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948622):
<p>yes</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948624):
<p>"PS here's the first occurrence of the string Calc"</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948630):
<p>"feel free to look and see if there are any others"</p>

#### [ Patrick Massot (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948643):
<p>Web pages of TPIL are too big</p>

#### [ Patrick Massot (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948645):
<p>from this point of view</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948653):
<p>That's one interpretation</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948657):
<p>Another is "search is crap"</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948662):
<p>I know we've all been spoilt by Google...</p>

#### [ Patrick Massot (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948720):
<p>google would show you the same</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948722):
<p>or maybe section 4.3 should be tagged calc</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948723):
<p>and the search should prioritise tags</p>

#### [ Patrick Massot (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948726):
<p>one hit for this page, and not all occurences on the search result page</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948728):
<p>is that possible in Sphinx?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948737):
<p>Google might have a better idea about moving the "right" answer to <a href="https://github.com/leanprover/lean/issues/1" target="_blank" title="https://github.com/leanprover/lean/issues/1">#1</a> in the list...</p>

#### [ Chris Hughes (Apr 11 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948751):
<blockquote>
<p>Can I mix equality and an congruences in calc?</p>
</blockquote>
<p>I tried it and you can.</p>

#### [ Patrick Massot (Apr 11 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948888):
<p>Go to google and typein search bar: <code>site:https://leanprover.github.io/theorem_proving_in_lean/ calc</code></p>

#### [ Patrick Massot (Apr 11 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948904):
<p>Google is smarter than Sphynx</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948916):
<blockquote>
<p>Can I mix equality and an congruences in calc?</p>
</blockquote>
<p><code>@[trans] protected theorem trans : a ≡ b [MOD n] → b ≡ c [MOD n] → a ≡ c [MOD n] := eq.trans
</code></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948919):
<p>and lo and behold</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948923):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">modeq</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">b</span> <span class="o">[</span><span class="n">MOD</span> <span class="n">m</span><span class="o">])</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≡</span> <span class="n">d</span> <span class="o">[</span><span class="n">MOD</span> <span class="n">m</span><span class="o">])</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">d</span> <span class="o">[</span><span class="n">MOD</span> <span class="n">m</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">b</span> <span class="o">[</span><span class="n">MOD</span> <span class="n">m</span><span class="o">]</span> <span class="o">:</span> <span class="n">H1</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:</span> <span class="n">H2</span>
<span class="bp">...</span> <span class="bp">≡</span> <span class="n">d</span> <span class="o">[</span><span class="n">MOD</span> <span class="n">m</span><span class="o">]</span> <span class="o">:</span> <span class="n">H3</span>
</pre></div>

#### [ Kevin Buzzard (Apr 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948977):
<p>Google is smarter than everything :-/</p>

#### [ Chris Hughes (Apr 11 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948981):
<p>what if I have two relations that are "co transitive" in the same sense that <code>le</code> and <code>lt</code> are. Can I make them work with calc?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124948986):
<p>Right, e.g. a congruence mod 8 might imply a congruence mod 4</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949001):
<p>I have no idea how Lean is doing the &lt; and &lt;= thing</p>

#### [ Patrick Massot (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949002):
<p>calc knowing about that would be pretty cool</p>

#### [ Chris Hughes (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949003):
<p>I thought that was a useless question, but obviously not.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949008):
<p>I know from experience that it will let you prove <code>a &lt; d</code> by writing <code>a &lt;= b &lt; c &lt;= d</code></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949012):
<p>so it knows <code>lt_of_le_of_lt</code></p>

#### [ Patrick Massot (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949014):
<p>yes, this is already really cool</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949018):
<p>but it wouldn't surprise me if this were hard wired in somehow</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949020):
<p>as a common use case</p>

#### [ Patrick Massot (Apr 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949055):
<p>but I suspect this special case is hard-wired</p>

#### [ Chris Hughes (Apr 11 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949064):
<p><code>lt_of_lt_of_le</code> is tagged with trans. So it might just be a case of doing that.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949138):
<p>Oh well spotted!</p>

#### [ Patrick Massot (Apr 11 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949150):
<p>indeed</p>

#### [ Chris Hughes (Apr 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949181):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span><span class="n">r&#39;</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">r</span>
<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span><span class="n">s&#39;</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">s</span>

<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">r</span><span class="bp">.</span><span class="n">trans</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">rs</span><span class="bp">.</span><span class="n">trans</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">s</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">rs</span><span class="bp">.</span><span class="n">trans1</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">s</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span> <span class="k">calc</span>
  <span class="n">a</span> <span class="n">r&#39;</span> <span class="n">b</span> <span class="o">:</span> <span class="n">h₁</span>
  <span class="bp">...</span> <span class="n">s&#39;</span> <span class="n">c</span> <span class="o">:</span> <span class="n">h₂</span>
</pre></div>

#### [ Chris Hughes (Apr 11 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949227):
<p>That pasted from VScode without any extra spaces.</p>

#### [ Patrick Massot (Apr 11 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949231):
<p><span class="emoji emoji-1f62f" title="hushed">:hushed:</span></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949234):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">modeq</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">helpful</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">b</span> <span class="o">[</span><span class="n">MOD</span> <span class="mi">8</span><span class="o">]</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≡</span> <span class="n">c</span> <span class="o">[</span><span class="n">MOD</span> <span class="mi">16</span><span class="o">]</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">c</span> <span class="o">[</span><span class="n">MOD</span> <span class="mi">4</span><span class="o">]</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">b</span> <span class="o">[</span><span class="n">MOD</span> <span class="mi">8</span><span class="o">])</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≡</span> <span class="n">d</span> <span class="o">[</span><span class="n">MOD</span> <span class="mi">16</span><span class="o">])</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">d</span> <span class="o">[</span><span class="n">MOD</span> <span class="mi">4</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">b</span> <span class="o">[</span><span class="n">MOD</span> <span class="mi">8</span><span class="o">]</span> <span class="o">:</span> <span class="n">H1</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:</span> <span class="n">H2</span>
<span class="bp">...</span> <span class="bp">≡</span> <span class="n">d</span> <span class="o">[</span><span class="n">MOD</span> <span class="mi">16</span><span class="o">]</span> <span class="o">:</span> <span class="n">H3</span>
</pre></div>

#### [ Kevin Buzzard (Apr 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949241):
<p>(deleted)</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949244):
<p>so did that</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949257):
<p>So it's really not hard coded in, there is some dark art with trans tags</p>

#### [ Patrick Massot (Apr 11 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949301):
<p>Let's keep that in Lean 4</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949304):
<p>Conclusion in my example must be a = c mod 8 after second line</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949314):
<p>it uses this:</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949316):
<p><code>#check trans_rel_left -- ∀ (r : ?M_1 → ?M_1 → Prop), r ?M_2 ?M_3 → ?M_3 = ?M_4 → r ?M_2 ?M_4
</code></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949323):
<p>(I know because some messing around gave me some explicit error messages)</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949327):
<p>and then it uses my trans-tagged theorem for 3rd line</p>

#### [ Patrick Massot (Apr 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949380):
<p>To the <code>docs/extras/calc</code>!</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949384):
<p>Yes, this deserves to be better known</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949399):
<p>I mean it's mentioned in TPIL but somehow it hadn't dawned on me how far you could push this</p>

#### [ Chris Hughes (Apr 11 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949401):
<p>So now I know the point of <code>@[trans]</code> and <code>@[refl]</code> but I'm still not sure why you would tag something <code>@[symm]</code></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949503):
<p><a href="#narrow/stream/113488-general/topic/simp.20is.20amazing" title="#narrow/stream/113488-general/topic/simp.20is.20amazing">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp.20is.20amazing</a></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949509):
<p>Gabriel's comment is in that thread</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949511):
<p>but I don't know any longer if it was about simp</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949557):
<p>If you tag something symm then there's some tactic called symmetry which will work ;-)</p>

#### [ Patrick Massot (Apr 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949669):
<p>We need to formalize something using this calc power</p>

#### [ Patrick Massot (Apr 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949671):
<p>What about some version of Hensel's lemma?</p>

#### [ Patrick Massot (Apr 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949678):
<p>There should be chains of congruence modulo different stuff there</p>

#### [ Patrick Massot (Apr 11 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949719):
<p>And it may even be useful for perfectoids, who knows?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949725):
<p><code>theorem X (a b m : ℕ) (H : a ≡ b [MOD m]) : b ≡ a [MOD m] := by symmetry;assumption</code></p>

#### [ Chris Hughes (Apr 11 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949738):
<p><code>theorem X (a b m : ℕ) (H : a ≡ b [MOD m]) : b ≡ a [MOD m] := H.symm</code></p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949739):
<p>symmetry tactic replaces a hypothesis with another one if the fact that one implies the other is marked with symm</p>

#### [ Chris Hughes (Apr 11 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949789):
<p>I know what it does, but it seems fairly useless.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949806):
<p>Simon's cool use of transivity is above, and refl is used everywhere, but who knows what symmetry is for :-)</p>

#### [ Chris Hughes (Apr 11 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124949874):
<blockquote>
<p>Simon's cool use of transivity is above, and refl is used everywhere, but who knows what symmetry is for :-)</p>
</blockquote>
<p>What's Simon's cool use of transitivity?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124950966):
<p>At the start of this thread</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953029):
<blockquote>
<p>To the <code>docs/extras/calc</code>!</p>
</blockquote>
<p><a href="https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/calc.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/calc.md">https://github.com/kbuzzard/mathlib/blob/WIP_docs/docs/WIPs/calc.md</a></p>

#### [ Chris Hughes (Apr 12 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953112):
<p>Can I use calc if I haven't defined an infix for my relation?</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953180):
<p>I don't know!</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953181):
<p>As you can see I defined infixes for mine.</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953284):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I wrote some calc docs (see link above) extending what is written in TPIL, together with some notes for things I struggled with myself after reading TPIL (e.g. I would sometimes get into a real mess with some syntax error or proof error manifesting itself as a red squiggle under a random <code>...</code>). Three questions:</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953288):
<p>1) Shall I PR to mathlib?</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953293):
<p>2) Chris asks if <code>calc</code> can be used with operators that aren't infix</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953362):
<p>3) I made some guesses as to how calc works. In particular I note that <code>trans_rel_right</code> and <code>trans_rel_left</code> are not tagged <code>[trans]</code>. Are these special cases which are tried first?</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953417):
<p>And an idle question -- would it be possible to break <code>calc</code> by proving e.g. <code>a &lt; b -&gt; b &lt; c -&gt; a &lt;= c</code> and tagging with <code>[trans]</code>?</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124953555):
<p>And <span class="user-mention" data-user-id="110031">@Patrick Massot</span> After Mario accepted my last mathlib PRs I just nuked the entire repo and forked it again (do you remember I had a bad commit history because I never branched?). Now I have a branch with my WIPs. I know I can google for how to do this but I'm sure you will know instantly -- what is the best way to just PR the calc.md file? Sorry to bother you.</p>

#### [ Patrick Massot (Apr 12 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971220):
<p>Since you have only one file to PR and don't care about keeping the history of this file, here the simplest route: copy that calc.md somewhere else (say /home/kevin/), then, inside mathlib,</p>
<div class="codehilite"><pre><span></span>git checkout master
git checkout -b docs-calc
cp /home/kevin/calc.md docs/extras/
</pre></div>


<p>then edit <code>docs/extras.md</code> to add a link to <code>docs/extra/calc.md</code></p>
<div class="codehilite"><pre><span></span>git add docs/extras.md docs/extra/calc.md
git commit
git push
</pre></div>


<p>The last command will complain you should explicitly say to create an upstream branch. Copy-paste the suggested command (I never remember the syntax since git always helps me here).</p>

#### [ Patrick Massot (Apr 12 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971277):
<p>I forgot: don't forget to make sure your master is in sync with Mario's before <code>git check-out -b docs-calc</code></p>

#### [ Patrick Massot (Apr 12 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971317):
<p>assuming you followed conventional names, that would mean <code>git pull upstream master</code> after <code>git checkout master</code></p>

#### [ Mario Carneiro (Apr 12 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971318):
<p>It's not a big problem if you PR off an old version of mathlib, since I usually rebase it on the current head when I merge the PR anyway</p>

#### [ Mario Carneiro (Apr 12 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971319):
<p>unless there's a conflict of course</p>

#### [ Mario Carneiro (Apr 12 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971320):
<p>but docs don't usually cause conflicts if they are new</p>

#### [ Patrick Massot (Apr 12 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971369):
<p>sure</p>

#### [ Patrick Massot (Apr 12 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971371):
<p>I'm only trying to explain good practice</p>

#### [ Mario Carneiro (Apr 12 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124971558):
<p>I agree with everything you said.</p>
<p>I would add that if you intend to PR some addition, you should write it "in place", i.e. with the file located in mathlib where you want it to be, by first checking out <code>master</code> then checking out a new branch (i.e. the first two lines of Patrick's script), then making any modifications there.  Then any commits you make will branch from master nicely. If you need to set the work aside, you can just commit what you have to the branch and move to the current master or somewhere else, and come back to your PR when you are ready to resume work with <code>git checkout my-pr</code>.</p>

#### [ Patrick Massot (Apr 12 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124972034):
<p>No -b in your last sentence</p>

#### [ Patrick Massot (Apr 12 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124972076):
<p>Otherwise of course this is the correct way. I was explaining how to fix the mess.</p>

#### [ Mario Carneiro (Apr 12 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124972188):
<p>oops, typo (copy-o?)</p>

#### [ Kevin Buzzard (Apr 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124990989):
<p>OK done. Thanks both for the advice. Mario -- it's a bit of a WIP because I guessed how the transitivity worked in calc mode. First I guessed that Lean went from <code>A op1 B op2 C op3 D</code> to <code>A op4 D</code> via "reading from left to right", i.e. first attempting to figure out how <code>A op1 B op2 C</code> can become <code>A op5 C</code> and then merging this with <code>C op3 D</code> (i.e. I don't know if it does anything clever like trying to merge two random consecutive theorems in the middle), and secondly I guessed that when trying to merge two ops to become another one it first uses rw if one is <code>=</code> and then tries lemmas tagged <code>trans</code> if neither op is <code>=</code>. These are just plain guesses.</p>

#### [ Chris Hughes (Apr 12 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124992197):
<p>I did some testing and I don't think it tries to do anything clever with changing the order. <code>L2</code> doesn't work below, but the rest do. You can also state that three relations are transitive together.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">r</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">t</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span><span class="n">r&#39;</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">r</span>
<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span><span class="n">s&#39;</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">s</span>
<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span><span class="n">t&#39;</span><span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="o">:=</span> <span class="n">t</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">rrr</span><span class="bp">.</span><span class="n">trans</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">srr</span><span class="bp">.</span><span class="n">trans</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">s</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">sts</span><span class="bp">.</span><span class="n">trans</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">s</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">t</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">s</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">rss</span><span class="bp">.</span><span class="n">trans</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">s</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">trs</span><span class="bp">.</span><span class="n">trans</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">t</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">r</span> <span class="n">b</span> <span class="n">c</span> <span class="bp">→</span> <span class="n">s</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">L1</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">s</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">t</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">h₃</span> <span class="o">:</span> <span class="n">r</span> <span class="n">c</span> <span class="n">d</span><span class="o">)</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">d</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">a</span> <span class="n">s&#39;</span> <span class="n">b</span> <span class="o">:</span> <span class="n">h₁</span>
   <span class="bp">...</span> <span class="n">t&#39;</span> <span class="n">c</span> <span class="o">:</span> <span class="n">h₂</span>
   <span class="bp">...</span> <span class="n">r&#39;</span> <span class="n">d</span> <span class="o">:</span> <span class="n">h₃</span>

<span class="kn">lemma</span> <span class="n">L2</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">s</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">h₃</span> <span class="o">:</span> <span class="n">t</span> <span class="n">c</span> <span class="n">d</span><span class="o">)</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">d</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">a</span> <span class="n">r&#39;</span> <span class="n">b</span> <span class="o">:</span> <span class="n">h₁</span>
   <span class="bp">...</span> <span class="n">s&#39;</span> <span class="n">c</span> <span class="o">:</span> <span class="n">h₂</span>
   <span class="bp">...</span> <span class="n">t&#39;</span> <span class="n">d</span> <span class="o">:</span> <span class="n">h₃</span>

<span class="kn">lemma</span> <span class="n">L2&#39;</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">s</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">h₃</span> <span class="o">:</span> <span class="n">t</span> <span class="n">c</span> <span class="n">d</span><span class="o">)</span> <span class="o">:</span> <span class="n">r</span> <span class="n">a</span> <span class="n">d</span> <span class="o">:=</span>
<span class="n">rss</span><span class="bp">.</span><span class="n">trans</span> <span class="n">h₁</span> <span class="o">(</span><span class="n">sts</span><span class="bp">.</span><span class="n">trans</span> <span class="n">h₂</span> <span class="n">h₃</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">L3</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">t</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">r</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">s</span> <span class="n">a</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">a</span> <span class="n">t&#39;</span> <span class="n">b</span> <span class="o">:</span> <span class="n">h₁</span>
   <span class="bp">...</span> <span class="n">r&#39;</span> <span class="n">c</span> <span class="o">:</span> <span class="n">h₂</span>
</pre></div>

#### [ Kevin Buzzard (Apr 12 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unfolding%20carefully/near/124993108):
<p>Thanks for checking. That was one way of doing it. The other way is to read the source code, but I sort-of suspect (perhaps incorrectly) that it will be in C++ not Lean.</p>


{% endraw %}
