---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63778coqwoes.html
---

## Stream: [general](index.html)
### Topic: [coq woes](63778coqwoes.html)

---


{% raw %}
#### [ Sean Leather (Apr 24 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609345):
<p>I'm stuck on trying to understand something in a Coq proof. Any experts on here who can spare a few minutes to help?</p>

#### [ Sean Leather (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609411):
<p>The issue is partially at <a href="https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L423-L431" target="_blank" title="https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L423-L431"><code>typ_open_types</code></a>, which uses <a href="https://github.com/spl/formal_binders/blob/master/ML_Core_Definitions.v#L78-L81" target="_blank" title="https://github.com/spl/formal_binders/blob/master/ML_Core_Definitions.v#L78-L81"><code>typ_body</code></a>.</p>

#### [ Sean Leather (Apr 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609462):
<p>There is an <code>exists</code> in <code>typ_body</code>, and I'm trying to figure out how it is used in the proof of <code>typ_open_types</code>.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609466):
<p>Is there a coq chatroom like this one?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609469):
<p>Of course I cannot help at all, I was just wondering.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609470):
<p>There's certainly a mailing list, right?</p>

#### [ Sean Leather (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609474):
<blockquote>
<p>Is there a coq chatroom like this one?</p>
</blockquote>
<p>No idea.</p>

#### [ Sean Leather (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609483):
<blockquote>
<p>There's certainly a mailing list, right?</p>
</blockquote>
<p>I don't want to sign up for one if I don't have to. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609486):
<p>I'm trying to translate this into Lean.</p>

#### [ Sean Leather (Apr 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125609531):
<p>I've been doing fine so far, but this part has me a bit stuck.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610071):
<p>You need to help me help you on this one, because it uses some non-standard stuff :). So from looking at the thing, your <code>typ_body</code> is now some <code>L</code> for which <code>K</code>. Then they do <code>pick_freshes</code>? What is that :)? And is <code>poses</code> some variation on <code>pose</code>?</p>

#### [ Sean Leather (Apr 24 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610073):
<blockquote>
<p>You need to help me help you on this one, because it uses some non-standard stuff <span class="emoji emoji-1f603" title="smiley">:smiley:</span>.</p>
</blockquote>
<p>Absolutely!</p>

#### [ Sean Leather (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610085):
<p><code>pick_freshes</code> is a tactic.</p>

#### [ Sean Leather (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610087):
<p><code>poses</code> is another tactic.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610088):
<p>Ooh, now it's all clear then!</p>

#### [ Sean Leather (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610089):
<p><code>LibTactic.v</code> I believe. I usually <code>grep</code> for it.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610091):
<p>Alright, let's see :).</p>

#### [ Sean Leather (Apr 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610139):
<p>What does <code>introv [L K]</code> mean?</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610141):
<p>It destructs the existential into two parts.</p>

#### [ Sean Leather (Apr 24 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610144):
<p>Right, thought so.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610153):
<p>Your <code>introv [L K] WT</code> basically first <code>intros T Us</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610159):
<p>And <code>rewrite*</code> and <code>apply*</code> just pull hypotheses from the context, right?</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610161):
<p>Yes.</p>

#### [ Sean Leather (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610204):
<p>... which makes it difficult to figure out what's getting used.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610205):
<p>Btw, I don't think <code>LibTactics.v</code> has these <code>pick_freshes</code>. It might be coming from something home-baked there?</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610209):
<p>There's a <code>Metatheory</code> import there, whatever that is.</p>

#### [ Sean Leather (Apr 24 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610210):
<p>Oh, <code>pick_freshes</code> comes from <code>Metatheory_var.v</code> or <code>Metatheory_fresh.v</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610220):
<p>Err, or <code>Metatheory_Env.v</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610277):
<p>Correction: <code>ML_Core_Infrastructure.v</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610293):
<p>Also, I meant <code>Lib_Tactic.v</code> in this project.</p>

#### [ Sean Leather (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610344):
<p><a href="https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L113-L117" target="_blank" title="https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L113-L117"><code>pick_fresh</code> and <code>pick_freshes</code></a></p>

#### [ Sean Leather (Apr 24 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610349):
<p><a href="https://github.com/spl/formal_binders/blob/master/Lib_Tactic.v#L32-L33" target="_blank" title="https://github.com/spl/formal_binders/blob/master/Lib_Tactic.v#L32-L33"><code>poses</code></a></p>

#### [ Sean Leather (Apr 24 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610420):
<p>I think I get the gist of those. What I'm currently struggling with is what happens to the <code>L</code> and <code>K</code>. Do they get used and how?</p>

#### [ Sean Leather (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610490):
<p>Because <code>K</code> is a function, right? Something like this out of <code>typ_body</code>:</p>
<div class="codehilite"><pre><span></span><span class="k">forall</span> <span class="n">Xs</span><span class="o">,</span> <span class="n">fresh</span> <span class="n">L</span> <span class="n">n</span> <span class="n">Xs</span> <span class="o">-&gt;</span> <span class="n">type</span> <span class="o">(</span><span class="n">typ_open_vars</span> <span class="n">T</span> <span class="n">Xs</span><span class="o">)</span>
</pre></div>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610498):
<p><code>pick_fresh</code> and <code>poses</code> don't seem to do anything funny to them, so <code>rewrite* (@typ_substs_intro Xs). apply* typ_substs_types</code> so it's either of these two invocations.</p>

#### [ Sean Leather (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610503):
<p>I agree.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610509):
<p>Yes, <code>K</code> is a function.</p>

#### [ Sean Leather (Apr 24 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610548):
<p>I think the culprit is <a href="https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L380-L386" target="_blank" title="https://github.com/spl/formal_binders/blob/master/ML_Core_Infrastructure.v#L380-L386"><code>typ_substs_intro</code></a>.</p>

#### [ Sean Leather (Apr 24 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610566):
<div class="codehilite"><pre><span></span><span class="kn">Lemma</span> <span class="n">typ_substs_intro</span> <span class="o">:</span> <span class="k">forall</span> <span class="n">Xs</span> <span class="n">Us</span> <span class="n">T</span><span class="o">,</span>
  <span class="n">fresh</span> <span class="o">(</span><span class="n">typ_fv</span> <span class="n">T</span> <span class="err">\</span><span class="n">u</span> <span class="n">typ_fv_list</span> <span class="n">Us</span><span class="o">)</span> <span class="o">(</span><span class="n">length</span> <span class="n">Xs</span><span class="o">)</span> <span class="n">Xs</span> <span class="o">-&gt;</span>
  <span class="n">types</span> <span class="o">(</span><span class="n">length</span> <span class="n">Xs</span><span class="o">)</span> <span class="n">Us</span> <span class="o">-&gt;</span>
  <span class="o">(</span><span class="n">typ_open</span> <span class="n">T</span> <span class="n">Us</span><span class="o">)</span> <span class="o">=</span> <span class="n">typ_substs</span> <span class="n">Xs</span> <span class="n">Us</span> <span class="o">(</span><span class="n">typ_open_vars</span> <span class="n">T</span> <span class="n">Xs</span><span class="o">).</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610591):
<p>(So sacrilege: pasting Coq onto a Lean forum...)</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610674):
<p>Right, so the last apply in the original proof is probably discharging one of the unresolved arguments of rewrites resulting from rewriting <code>typ_subst_intro</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610679):
<p>(BTW, it would be nice if I could run this. I tried, fixed a few things, but <code>coqc Lib_ListFacts.v</code> doesn't finish in several hours.)</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610760):
<p>Well that's the overarching problem of reading Coq. (Btw, even <code>rewrite*</code> is non-standard.)</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610828):
<p>Still, we rewrite <code>(typ_open T Us)</code> with <code>typ_subst Xs Us (typ_open_vars T Xs)</code>, we have <code>Xs Us T</code> from rewriting, there should be 2 new obligations, <code>fresh (...)</code> and <code>types ...</code>. Either of these may have been discharged by some form of <code>assumption</code> resulting from <code>rewrite*</code>, leaving the last one for the final <code>apply</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610833):
<p>So my confusion comes down to this (I think): when <code>typ_body</code> is destructed into <code>L</code> and <code>K</code> as <code>forall Xs, fresh L n Xs -&gt; type (typ_open_vars T Xs)</code>, is <code>K</code> being used, and, if so, how does <code>fresh L n Xs </code> get instantiated since nothing is known about <code>L</code>?</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610946):
<p>It doesn't necessarily need to be instantiated for <code>K</code> to still be used.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125610966):
<p>I don't think the <code>rewrite*</code> or <code>apply*</code> would go beyond defeq or some form of <code>assumption</code> (resulting from the <code>*</code> suffix).</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611013):
<p>You can still use <code>K</code> to discharge <code>Pi_Xs, _ -&gt; _</code> which is what I think ends up happening.</p>

#### [ Sean Leather (Apr 24 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611076):
<p><code>typ_subst_intro</code> expects <code>fresh (typ_fv T \u typ_fv_list Us) (length Xs) Xs</code>. Where does that come from?</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611153):
<p>It's probably either <code>Fr</code> or <code>Fr'</code>, resulting from <code>pick_freshes</code> and <code>assumption</code>'d from the <code>rewrite*</code> call.</p>

#### [ Sean Leather (Apr 24 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611178):
<p>Ah, right.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611236):
<p><code>apply* typ_substs_types</code> then most likely solves <code>types (length Xs) Us</code></p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611248):
<p>Can logically <code>K</code> and <code>L</code> help with that? let's see. So they basically map a "parameterized" fresh name to a parameterized type?</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611293):
<p>It is most likely the case that it's the very last tactic (<code>apply*</code>) that uses <code>K</code> in the <code>Pi</code> form.</p>

#### [ Sean Leather (Apr 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611304):
<div class="codehilite"><pre><span></span><span class="k">rewrite</span><span class="o">*</span> <span class="o">(@</span><span class="n">typ_substs_intro</span> <span class="n">Xs</span><span class="o">).</span> <span class="k">apply</span><span class="o">*</span> <span class="n">typ_substs_types</span><span class="o">.</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">Lemma</span> <span class="n">typ_substs_types</span> <span class="o">:</span> <span class="k">forall</span> <span class="n">Xs</span> <span class="n">Us</span> <span class="n">T</span><span class="o">,</span>
  <span class="n">types</span> <span class="o">(</span><span class="n">length</span> <span class="n">Xs</span><span class="o">)</span> <span class="n">Us</span> <span class="o">-&gt;</span>
  <span class="n">type</span> <span class="n">T</span> <span class="o">-&gt;</span>
  <span class="n">type</span> <span class="o">(</span><span class="n">typ_substs</span> <span class="n">Xs</span> <span class="n">Us</span> <span class="n">T</span><span class="o">).</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611313):
<blockquote>
<p>You can still use <code>K</code> to discharge <code>Pi_Xs, _ -&gt; _</code> which is what I think ends up happening.</p>
</blockquote>
<p>I don't understand this.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611446):
<p>It's as you said, there is no reasonable way to instantiate it. So we can just end up assuming the argument comes from someplace.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611464):
<p>Aka. the goal transforming to <code>fresh L n Xs -&gt; type (typ_open_vars T Xs)</code> (or <code>fresh L n Xs |- type (...)</code>)</p>

#### [ Sean Leather (Apr 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611572):
<p>I'm thinking it would help me to understand <code>poses</code>/<code>pose</code> better.</p>

#### [ Sean Leather (Apr 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611630):
<p>And to figure out where <code>Fr</code> comes from.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611637):
<p>I think <code>Fr</code> and <code>Fr'</code> are related to the other hypothesis?</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611647):
<p>At least if <code>pick_freshes</code> doesn't ever mess with either <code>L</code> or <code>K</code>.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611652):
<p>Which it doesn't seem to becasue its argument is a subterm of the other hypothesis (<code>length Us</code>).</p>

#### [ Sean Leather (Apr 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611702):
<div class="codehilite"><pre><span></span><span class="kn">Ltac</span> <span class="n">pick_freshes_gen</span> <span class="n">L</span> <span class="n">n</span> <span class="n">Y</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">Fr</span> <span class="o">:=</span> <span class="n">fresh</span> <span class="s2">&quot;Fr&quot;</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">L</span> <span class="o">:=</span> <span class="n">beautify_fset</span> <span class="n">L</span> <span class="k">in</span>
  <span class="o">(</span><span class="k">destruct</span> <span class="o">(</span><span class="n">var_freshes</span> <span class="n">L</span> <span class="n">n</span><span class="o">)</span> <span class="k">as</span> <span class="o">[</span><span class="n">Y</span> <span class="n">Fr</span><span class="o">]).</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611708):
<p>Does that introduce <code>Fr</code>? It's used by <code>pick_freshes</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611730):
<p>Oh, and I think <code>pick_freshes</code>/<code>pick_freshes_gen</code> might get <code>L</code> from the assumptions.</p>

#### [ Sean Leather (Apr 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611776):
<p>Via <code>gather_vars</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611781):
<div class="codehilite"><pre><span></span><span class="kn">Ltac</span> <span class="n">gather_vars</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">vars</span> <span class="o">=&gt;</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">var</span> <span class="o">=&gt;</span> <span class="o">{{</span> <span class="n">x</span> <span class="o">}})</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">C</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">env</span> <span class="o">=&gt;</span> <span class="n">dom</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">D</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">trm</span> <span class="o">=&gt;</span> <span class="n">trm_fv</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">E</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">typ</span> <span class="o">=&gt;</span> <span class="n">typ_fv</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">F</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="kt">list</span> <span class="n">typ</span> <span class="o">=&gt;</span> <span class="n">typ_fv_list</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">G</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">env</span> <span class="o">=&gt;</span> <span class="n">env_fv</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">sch</span> <span class="o">=&gt;</span> <span class="n">sch_fv</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="n">constr</span><span class="o">:(</span><span class="n">A</span> <span class="err">\</span><span class="n">u</span> <span class="n">B</span> <span class="err">\</span><span class="n">u</span> <span class="n">C</span> <span class="err">\</span><span class="n">u</span> <span class="n">D</span> <span class="err">\</span><span class="n">u</span> <span class="n">E</span> <span class="err">\</span><span class="n">u</span> <span class="n">F</span> <span class="err">\</span><span class="n">u</span> <span class="n">G</span> <span class="err">\</span><span class="n">u</span> <span class="n">H</span><span class="o">).</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611793):
<p>I suppose the <code>gather_vars</code> tactic could also be getting something from <code>K</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611916):
<p>Right, so <code>Fr</code> comes from <code>pick_freshes</code> and includes <code>L</code> in the free variable finite set.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125611959):
<p>1) <code>pose</code> introduces <code>h := t : T</code>, a bit like <code>let</code> in lean. <code>poses</code> is their homebrew thing for transforming the introduced <code>h</code> into <code>h : T</code> without <code>t</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612021):
<p>I think the <code>K</code> obligation of <code>fresh L n Xs</code> <em>could</em> be satisfied by <code>Fr</code> by narrowing down the union of finite sets to extract only <code>L</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612030):
<p>... the finite set created by <code>gather_vars</code>, which scours the assumptions for variables.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612065):
<p>Wouldn't that require something more magical than what <code>rewrite*</code> or <code>apply*</code> can do?</p>

#### [ Sean Leather (Apr 24 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612079):
<p>Yes.</p>

#### [ Sean Leather (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612094):
<p>There are other tactics that do that, but, to think of it, they're not being used here, are they?</p>

#### [ Sean Leather (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612101):
<p>Other homemade tactics, I mean.</p>

#### [ Sean Leather (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612106):
<p>So maybe I'm jumping ahead of myself.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612109):
<p>Right, so here's the thing.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612151):
<div class="codehilite"><pre><span></span><span class="n">poses</span> <span class="n">Fr&#39;</span> <span class="n">Fr</span><span class="bp">.</span>
<span class="n">rewrite</span> <span class="o">(</span><span class="n">fresh_length</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>  <span class="n">Fr</span><span class="o">)</span> <span class="k">in</span> <span class="n">WT</span><span class="o">,</span> <span class="n">Fr&#39;</span><span class="bp">.</span>
<span class="n">rewrite</span><span class="bp">*</span> <span class="o">(</span><span class="bp">@</span><span class="n">typ_substs_intro</span> <span class="n">Xs</span><span class="o">)</span><span class="bp">.</span> <span class="n">apply</span><span class="bp">*</span> <span class="n">typ_substs_types</span>
</pre></div>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612163):
<p>The only non-standard one is <code>poses</code> which doesn't do much beyond <code>pose</code> (according to its definition).</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612172):
<p><code>rewrite(*)</code> and <code>apply*</code> are standard in the sense that they cannot call anything magical.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612231):
<p>The only remaining tactic is <code>pick_freshes (length Us) Xs</code> which can order you a pizza for what we know.</p>

#### [ Sean Leather (Apr 24 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612251):
<p>Well, I have a vague understanding of what <code>pick_freshes</code> does. It looks at <em>all</em> of the assumptions and picks out all the <code>vars</code> it can find, so that it can choose a free variable not in the resultant finite set of <code>vars</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612268):
<p>And, if I understand <code>fresh "Fr"</code> correctly, <code>pick_freshes</code> is creating the assumption <code>Fr</code>, which is later used by <code>poses</code>.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612351):
<p>Right. Let's say you have <code>p : Prop</code>. <code>pose p</code> then introduces <code>P := p : Prop</code>. <code>poses p</code> also calls <code>clearbody P</code> which gives you <code>p, P : Prop</code> in the context.</p>

#### [ Sean Leather (Apr 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612424):
<div class="codehilite"><pre><span></span><span class="k">rewrite</span> <span class="o">(</span><span class="n">fresh_length</span> <span class="o">_</span> <span class="o">_</span> <span class="o">_</span>  <span class="n">Fr</span><span class="o">)</span> <span class="k">in</span> <span class="n">WT</span><span class="o">,</span> <span class="n">Fr&#39;</span><span class="o">.</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">Lemma</span> <span class="n">fresh_length</span> <span class="o">:</span> <span class="k">forall</span> <span class="n">xs</span> <span class="n">L</span> <span class="n">n</span><span class="o">,</span> <span class="n">fresh</span> <span class="n">L</span> <span class="n">n</span> <span class="n">xs</span> <span class="o">-&gt;</span> <span class="n">n</span> <span class="o">=</span> <span class="n">length</span> <span class="n">xs</span><span class="o">.</span>
</pre></div>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612474):
<p>Right, this fully applies <code>fresh_length</code> so you have <code>n = length xs</code>, you make this rewrite in both <code>WT</code> and <code>Fr'</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612482):
<div class="codehilite"><pre><span></span><span class="kn">Definition</span> <span class="n">list_for_n</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kn">Set</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">A</span> <span class="o">-&gt;</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="kt">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="kt">list</span> <span class="n">A</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">n</span> <span class="o">=</span> <span class="n">length</span> <span class="n">L</span> <span class="o">/\</span> <span class="n">list_forall</span> <span class="n">P</span> <span class="n">L</span><span class="o">.</span>
</pre></div>


<div class="codehilite"><pre><span></span> <span class="kn">Definition</span> <span class="n">types</span> <span class="o">:=</span> <span class="n">list_for_n</span> <span class="n">type</span><span class="o">.</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612495):
<p>That's where the rewritten <code>length</code> assumptions are used, I believe.</p>

#### [ Sean Leather (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612499):
<p>That = <code>types</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612567):
<p>As in here:</p>
<div class="codehilite"><pre><span></span><span class="kn">Lemma</span> <span class="n">typ_substs_intro</span> <span class="o">:</span> <span class="k">forall</span> <span class="n">Xs</span> <span class="n">Us</span> <span class="n">T</span><span class="o">,</span>
  <span class="n">fresh</span> <span class="o">(</span><span class="n">typ_fv</span> <span class="n">T</span> <span class="err">\</span><span class="n">u</span> <span class="n">typ_fv_list</span> <span class="n">Us</span><span class="o">)</span> <span class="o">(</span><span class="n">length</span> <span class="n">Xs</span><span class="o">)</span> <span class="n">Xs</span> <span class="o">-&gt;</span>
  <span class="n">types</span> <span class="o">(</span><span class="n">length</span> <span class="n">Xs</span><span class="o">)</span> <span class="n">Us</span> <span class="o">-&gt;</span>
  <span class="o">(</span><span class="n">typ_open</span> <span class="n">T</span> <span class="n">Us</span><span class="o">)</span> <span class="o">=</span> <span class="n">typ_substs</span> <span class="n">Xs</span> <span class="n">Us</span> <span class="o">(</span><span class="n">typ_open_vars</span> <span class="n">T</span> <span class="n">Xs</span><span class="o">).</span>
</pre></div>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612582):
<p><code>types</code> is simple enough then, it's a filtered vector, conceptually</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612705):
<p><code>typ_substs_types</code> however is <code>_ -&gt; type (typ_substs Xs Us T)</code>, so there's no way for <code>apply*</code> to resolve <code>types</code> with it</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612758):
<p>So I was wrong wrt. what the last <code>apply*</code> pertains to it seems.</p>

#### [ Sean Leather (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612814):
<p>Yes, I think so. After <code>rewrite* (@typ_substs_intro ...)</code>, you get <code>type (typ_substs ...)</code> in the goal.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612824):
<p>Right, so that one is magically discharged.</p>

#### [ Sean Leather (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612829):
<p>... which is fulfilled by <code>apply* typ_substs_types</code></p>

#### [ Sean Leather (Apr 24 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612906):
<p>Are you sure there isn't more magic being done by <code>rewrite*</code> and/or <code>apply*</code>? Do those use the <code>Hint</code>s that are all over the place in this project?</p>

#### [ Sean Leather (Apr 24 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125612911):
<div class="codehilite"><pre><span></span>$ git grep Hint <span class="p">|</span> wc -l
     <span class="m">204</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613182):
<p><span class="user-mention" data-user-id="110027">@Moses Schönfinkel</span> I have to go prepare lunch and feed my kid. Sorry. I'll be back on later. Feel free to leave any insightful and illuminating thoughts here for me to read upon my return. <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Kevin Buzzard (Apr 24 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613470):
<p>I'm sure the moderators will have shut this thread down by then ;-)</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613746):
<p>Can / should I migrate this to a separate stream? <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Moses Schönfinkel (Apr 24 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613761):
<p>For example <code>maths</code> is this completely random topic that few here care about and has its own stream.. errrm :).</p>

#### [ Kevin Buzzard (Apr 24 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613807):
<p>:-) I have no idea -- as I'm sure you are aware, I was not being remotely serious.</p>

#### [ Moses Schönfinkel (Apr 24 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125613940):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> I'll take a closer look when I get home, I have some teaching to do</p>

#### [ Sean Leather (Apr 24 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125615229):
<p>Thanks. Lunch is over. I'll continue looking at it in the meantime, at least until the moderators or Kevin shut me down. If that happens, I'm sure I'll lose my mind, since I will no longer be able to voice my confusion publicly. <span class="emoji emoji-1f4a9" title="poop">:poop:</span></p>

#### [ Sean Leather (Apr 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125616072):
<p>Annotated:</p>
<div class="codehilite"><pre><span></span><span class="kn">Lemma</span> <span class="n">typ_open_types</span> <span class="o">:</span> <span class="k">forall</span> <span class="n">T</span> <span class="n">Us</span><span class="o">,</span>
  <span class="n">typ_body</span> <span class="o">(</span><span class="n">length</span> <span class="n">Us</span><span class="o">)</span> <span class="n">T</span> <span class="o">-&gt;</span>
</pre></div>


<p><code>Definition typ_body n T := exists L, forall Xs, fresh L n Xs -&gt; type (typ_open_vars T Xs).</code></p>
<div class="codehilite"><pre><span></span>  <span class="n">types</span> <span class="o">(</span><span class="n">length</span> <span class="n">Us</span><span class="o">)</span> <span class="n">Us</span> <span class="o">-&gt;</span>
</pre></div>


<p><code>Definition types := list_for_n type.</code></p>
<p><code>Definition list_for_n (A : Set) (P : A -&gt; Prop) (n : nat) (L : list A) := n = length L /\ list_forall P L.</code></p>
<div class="codehilite"><pre><span></span>  <span class="n">type</span> <span class="o">(</span><span class="n">typ_open</span> <span class="n">T</span> <span class="n">Us</span><span class="o">).</span>
<span class="kn">Proof</span><span class="o">.</span>
  <span class="n">introv</span> <span class="o">[</span><span class="n">L</span> <span class="n">K</span><span class="o">]</span> <span class="n">WT</span><span class="o">.</span>
</pre></div>


<p><code>L : vars</code> (a.k.a. <code>FinSet</code>)</p>
<p><code>K : forall Xs, fresh L n Xs -&gt; type (typ_open_vars T Xs)</code></p>
<div class="codehilite"><pre><span></span>  <span class="n">pick_freshes</span> <span class="o">(</span><span class="n">length</span> <span class="n">Us</span><span class="o">)</span> <span class="n">Xs</span><span class="o">.</span>
</pre></div>


<p>Creates an assumption named <code>Fr</code> defined as the union of all finite sets of variables in the context for some list. That is, I think <code>Fr : fresh L (length Us) Xs</code> because <code>destruct (var_freshes L n) as [Y Fr]</code> and <code>Lemma var_freshes : forall L n, { xs : list var | fresh L n xs }.</code></p>
<div class="codehilite"><pre><span></span>  <span class="n">poses</span> <span class="n">Fr&#39;</span> <span class="n">Fr</span><span class="o">.</span>
</pre></div>


<p>Copies <code>Fr</code> to <code>Fr'</code>.</p>
<div class="codehilite"><pre><span></span>  <span class="k">rewrite</span> <span class="o">(</span><span class="n">fresh_length</span> <span class="o">_</span> <span class="o">_</span> <span class="o">_</span>  <span class="n">Fr</span><span class="o">)</span> <span class="k">in</span> <span class="n">WT</span><span class="o">,</span> <span class="n">Fr&#39;</span><span class="o">.</span>
</pre></div>


<p><code>Lemma fresh_length : forall xs L n, fresh L n xs -&gt; n = length xs.</code></p>
<div class="codehilite"><pre><span></span>  <span class="k">rewrite</span><span class="o">*</span> <span class="o">(@</span><span class="n">typ_substs_intro</span> <span class="n">Xs</span><span class="o">).</span>
</pre></div>


<p><code>Lemma typ_substs_intro : forall Xs Us T,
  fresh (typ_fv T \u typ_fv_list Us) (length Xs) Xs -&gt;
  types (length Xs) Us -&gt;
  (typ_open T Us) = typ_substs Xs Us (typ_open_vars T Xs).</code></p>
<div class="codehilite"><pre><span></span>  <span class="k">apply</span><span class="o">*</span> <span class="n">typ_substs_types</span><span class="o">.</span>
</pre></div>


<p><code>Lemma typ_substs_types : forall Xs Us T,
  types (length Xs) Us -&gt;
  type T -&gt;
  type (typ_substs Xs Us T).</code></p>
<div class="codehilite"><pre><span></span><span class="kn">Qed</span><span class="o">.</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125616985):
<p>See <a href="https://gist.github.com/spl/a204842b476cc46fb1b879ee2baedfbd" target="_blank" title="https://gist.github.com/spl/a204842b476cc46fb1b879ee2baedfbd">https://gist.github.com/spl/a204842b476cc46fb1b879ee2baedfbd</a> for an easier-to-read and updated version of the above.</p>

#### [ Sean Leather (Apr 24 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617573):
<p>Okay, I believe I have a better handle on what's going on.</p>

#### [ Sean Leather (Apr 24 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617576):
<p>I've found where <code>L</code> and <code>K</code> are used.</p>

#### [ Sean Leather (Apr 24 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617617):
<p>There is definitely more magic being applied here than meets the eye.</p>

#### [ Sean Leather (Apr 24 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617635):
<p>I believe the <code>fresh</code> properties are being manipulated into their expected forms using the magic in <code>Metatheory_Fresh.v</code>.</p>

#### [ Sean Leather (Apr 24 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617695):
<p>I couldn't explain the technical mechanism, but I believe it has to do with all the <code>Hint</code>s to get certain tactics to perform automagically.</p>

#### [ Sean Leather (Apr 24 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617702):
<p>In particular, for <code>fresh</code>, it's:</p>
<div class="codehilite"><pre><span></span>Metatheory_Fresh.v:Hint Extern 1 (fresh _ _ _) =&gt; fresh_solve.
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617835):
<p>Also, there's this dark magic underlying <code>pick_freshes</code>:</p>
<div class="codehilite"><pre><span></span><span class="c">(** [gather_vars_with F] return the union of all the finite sets</span>
<span class="c">  of variables [F x] where [x] is a variable from the context such that</span>
<span class="c">  [F x] type checks. In other words [x] has to be of the type of the</span>
<span class="c">  argument of [F]. The resulting union of sets does not contain any</span>
<span class="c">  duplicated item. This tactic is an extreme piece of hacking necessary</span>
<span class="c">  because the tactic language does not support a &quot;fold&quot; operation on</span>
<span class="c">  the context. *)</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617855):
<p>Used as so:</p>
<div class="codehilite"><pre><span></span><span class="kn">Ltac</span> <span class="n">gather_vars</span> <span class="o">:=</span>
  <span class="k">let</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">vars</span> <span class="o">=&gt;</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">var</span> <span class="o">=&gt;</span> <span class="o">{{</span> <span class="n">x</span> <span class="o">}})</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">C</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">env</span> <span class="o">=&gt;</span> <span class="n">dom</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">D</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">trm</span> <span class="o">=&gt;</span> <span class="n">trm_fv</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">E</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">typ</span> <span class="o">=&gt;</span> <span class="n">typ_fv</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">F</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="kt">list</span> <span class="n">typ</span> <span class="o">=&gt;</span> <span class="n">typ_fv_list</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">G</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">env</span> <span class="o">=&gt;</span> <span class="n">env_fv</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="k">let</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">gather_vars_with</span> <span class="o">(</span><span class="k">fun</span> <span class="n">x</span> <span class="o">:</span> <span class="n">sch</span> <span class="o">=&gt;</span> <span class="n">sch_fv</span> <span class="n">x</span><span class="o">)</span> <span class="k">in</span>
  <span class="n">constr</span><span class="o">:(</span><span class="n">A</span> <span class="err">\</span><span class="n">u</span> <span class="n">B</span> <span class="err">\</span><span class="n">u</span> <span class="n">C</span> <span class="err">\</span><span class="n">u</span> <span class="n">D</span> <span class="err">\</span><span class="n">u</span> <span class="n">E</span> <span class="err">\</span><span class="n">u</span> <span class="n">F</span> <span class="err">\</span><span class="n">u</span> <span class="n">G</span> <span class="err">\</span><span class="n">u</span> <span class="n">H</span><span class="o">).</span>
</pre></div>

#### [ Sean Leather (Apr 24 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125617906):
<p>And (it just clicked for me) that is how <code>typ_fv</code> and <code>typ_fv_list</code> are appearing.</p>

#### [ Moses Schönfinkel (Apr 25 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125659086):
<p>Sorry I didn't manage to get around to using my computer yesterday! :(</p>

#### [ Sean Leather (Apr 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125659347):
<p>I progressed a bit further, as you can see. I'm slightly better at systematically reverse engineering Coq proofs now. Thanks for that! <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Moses Schönfinkel (Apr 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125659582):
<p>What a wonderful world this would be if you could run it :-\.</p>

#### [ Sean Leather (Apr 25 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660053):
<p>I've reverted to working on my Lean version of this proof. I have an idea of how to do the part of the <code>fresh</code> manipulation that is implemented with hidden dark magic in Coq, and I'm trying to work it out, in Lean, without magic.</p>

#### [ Moses Schönfinkel (Apr 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660224):
<p>You can also try Lean, with magic.</p>

#### [ Sean Leather (Apr 25 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660234):
<p>You mean, by writing tactics? I've avoided that so far, just so I can get a handle on how to do the proofs.</p>

#### [ Moses Schönfinkel (Apr 25 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660331):
<p>Yeah. I'm not entirely sure how useful learning it would be as of right now, given Lean 4 might (will?) change that.</p>

#### [ Sean Leather (Apr 25 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660442):
<p>That unknown future always seems to hang in the air, doesn't it? The possibility of change infects one's thoughts.</p>

#### [ Sean Leather (Apr 25 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660520):
<p>Apparently, Coq has changed a lot over the years, too. This project was supposed to work with 8.1, and now, with 8.8, it just compiles for more hours than I've been willing to wait.</p>

#### [ Kevin Buzzard (Apr 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660564):
<p>When mathematicians hear talks about the great things that have been achieved using computer proof checkers</p>

#### [ Kevin Buzzard (Apr 25 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660567):
<p>then the odd order theorem is always mentioned as one of the jewels in the crown</p>

#### [ Kevin Buzzard (Apr 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660572):
<p>(before Kepler it was _the_ jewel)</p>

#### [ Kevin Buzzard (Apr 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660577):
<p>and apparently that no longer compiles in Coq current</p>

#### [ Kevin Buzzard (Apr 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660579):
<p>so I have heard</p>

#### [ Kevin Buzzard (Apr 25 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660584):
<p>if either if you are in a position to formally verify this rumour I'd appreciate it</p>

#### [ Sean Leather (Apr 25 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660643):
<p><a href="https://github.com/math-comp/odd-order" target="_blank" title="https://github.com/math-comp/odd-order">https://github.com/math-comp/odd-order</a> is 8 days old. Maybe it's an update.</p>

#### [ Sean Leather (Apr 25 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660693):
<p>Anyway, that's what I got from the first page of a Google search. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Johan Commelin (Apr 25 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660745):
<p>Hmm, seems like it's working again.</p>

#### [ Johan Commelin (Apr 25 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660750):
<p>I heard this rumour on the ssreflect mailing list about a year ago</p>

#### [ Johan Commelin (Apr 25 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660751):
<p>Sounded pretty broken back then</p>

#### [ Johan Commelin (Apr 25 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660763):
<p>They were talking about distributing the proof with an old version of Coq inside a docker package. Just to make sure people could easily return to a version that compiles.</p>

#### [ Johan Commelin (Apr 25 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125660765):
<p>All the better if it actually compiles with the latest release!</p>

#### [ Sean Leather (Apr 25 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125661171):
<blockquote>
<p>They were talking about distributing the proof with an old version of Coq inside a docker package. Just to make sure people could easily return to a version that compiles.</p>
</blockquote>
<p>I just discovered <a href="https://github.com/proofengineering/coq-docker" target="_blank" title="https://github.com/proofengineering/coq-docker">https://github.com/proofengineering/coq-docker</a></p>

#### [ Sean Leather (Apr 25 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125663903):
<p>Et voilà! I just figured out <a href="https://github.com/proofengineering/coq-docker/issues/1" target="_blank" title="https://github.com/proofengineering/coq-docker/issues/1">how to install Coq 8.1</a> and built the Coq project. <span class="emoji emoji-1f423" title="hatching chick">:hatching_chick:</span></p>

#### [ Kevin Buzzard (Apr 25 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664059):
<p>They occasionally prove false in Coq, right? And then of course things get patched. Do the patches extend back as far as things like 8.1? I know that this might all sound trivial to CS people but mathematicians, who are still in my view extremely skeptical about this formal proof verification thing, are not going to be too impressed by "proof of odd order theorem in a system which can also prove anything".</p>

#### [ Kevin Buzzard (Apr 25 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664078):
<p><a href="https://github.com/clarus/falso" target="_blank" title="https://github.com/clarus/falso">https://github.com/clarus/falso</a></p>

#### [ Kevin Buzzard (Apr 25 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664079):
<p>8.1 &lt; 8.4.6</p>

#### [ Mario Carneiro (Apr 25 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664080):
<blockquote>
<p>which can also prove anything</p>
</blockquote>
<p>only on tuesdays</p>

#### [ Kevin Buzzard (Apr 25 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664121):
<p>only if you use a type with 256 constructors</p>

#### [ Sean Leather (Apr 25 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664193):
<p>For my purpose, I'm just trying to figure out what some Coq proof does and translate that to Lean. So, since we <em>never</em> prove false in Lean, there shouldn't be any problem, right?</p>

#### [ Kevin Buzzard (Apr 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125664204):
<p>I guess so!</p>

#### [ Sean Leather (Apr 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125665013):
<p>Great. I can walk through the proof in CoqIde now. But it doesn't show the magic happening behind the scenes.</p>

#### [ Sean Leather (Apr 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125665098):
<p>Oh, but I can remove the <code>*</code> from <code>rewrite*</code> to see the subgoals. <span class="emoji emoji-1f4a1" title="light bulb">:light_bulb:</span></p>

#### [ Moses Schönfinkel (Apr 25 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125667062):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Remember you also can't trust that pesky hardware Lean runs on!</p>

#### [ Sean Leather (Apr 25 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coq%20woes/near/125668364):
<p>And... my Coq woes are over! I have successfully translated this particular Coq proof into Lean. <span class="emoji emoji-1f64c" title="raised hands">:raised_hands:</span></p>


{% endraw %}
