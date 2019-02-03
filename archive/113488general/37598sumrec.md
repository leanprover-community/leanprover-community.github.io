---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37598sumrec.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [sum.rec](https://leanprover-community.github.io/archive/113488general/37598sumrec.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (May 01 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949453):
<p>I'm having a surprisingly hard time working with <code>sum.rec</code>. Specifically, I'm having trouble convincing Lean to give me an ordinary, non-dependent function as the result. I pasted a transcript here: <a href="https://gist.github.com/rwbarton/b6cbf07bd07afd89f8c2b4feef8cec5f" target="_blank" title="https://gist.github.com/rwbarton/b6cbf07bd07afd89f8c2b4feef8cec5f">https://gist.github.com/rwbarton/b6cbf07bd07afd89f8c2b4feef8cec5f</a></p>

#### [ Kenny Lau (May 01 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949466):
<p>the type of the second term depends on the type of the first term though</p>

#### [ Kenny Lau (May 01 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949476):
<p>sorry, I thought you were talking about sigma. ignore what I said.</p>

#### [ Reid Barton (May 01 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949537):
<p>I'm especially confused that <code>surjective ((λ a, sum.rec f g a) : α ⊕ β → γ)</code> produces an error that seems to be complaining that the argument needs to be a non-dependent function, though I can kind of imagine how this might not be considered a bug</p>

#### [ Reid Barton (May 01 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949607):
<p>It'd be really convenient for me if there was also a non-dependent eliminator <code>sum.rec' : (α → γ) → (β → γ) → α ⊕ β → γ</code></p>

#### [ Reid Barton (May 01 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949617):
<p>I noticed someone else came across the same issue, too:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">continuous_sum_rec</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">}</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">}</span>
  <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">hg</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">g</span><span class="o">)</span> <span class="o">:</span> <span class="bp">@</span><span class="n">continuous</span> <span class="o">(</span><span class="n">α</span> <span class="err">⊕</span> <span class="n">β</span><span class="o">)</span> <span class="n">γ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">sum</span><span class="bp">.</span><span class="n">rec</span> <span class="n">α</span> <span class="n">β</span> <span class="o">(</span><span class="bp">λ_</span><span class="o">,</span> <span class="n">γ</span><span class="o">)</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>

#### [ Reid Barton (May 01 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949693):
<p>That whole result type should really just be <code>continuous (sum.rec' f g)</code>.</p>

#### [ Reid Barton (May 01 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125949778):
<p>I assume the same issue arises for any other type with multiple constructors, too</p>

#### [ Mario Carneiro (May 01 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125954356):
<p>I think the problem is that <code>sum.rec</code> uses the eliminator strategy, meaning it relies heavily on the expected type to determine the motive, but <code>surjective</code> does not give a sufficiently specific expected type <code>?M1 -&gt; ?M2</code>. You can fix the issue by annotating the metavariables of <code>surjective</code>:</p>
<div class="codehilite"><pre><span></span>@surjective (α ⊕ β) γ (λ a, sum.rec f g a)
</pre></div>

#### [ Mario Carneiro (May 01 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125954449):
<p>The eliminator strategy makes <code>T.rec</code> more or less unusable when unapplied; apparently superfluous eta expansions here are important to trigger the right strategy</p>

#### [ Kevin Buzzard (May 01 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955363):
<p>Could this also be fixed by writing a second recursor?</p>

#### [ Kevin Buzzard (May 01 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955364):
<p>i.e. is this a problem that the interface could solve?</p>

#### [ Kenny Lau (May 01 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955375):
<p>yes</p>

#### [ Mario Carneiro (May 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955398):
<p>yes, but that would require changing lean (which generates all the <code>inductive</code> theorems)</p>

#### [ Kenny Lau (May 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955402):
<p>I think I'm instead reading "yes but you would need to PR core"</p>

#### [ Mario Carneiro (May 01 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955456):
<p>yes, that's what I mean</p>

#### [ Kevin Buzzard (May 01 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955531):
<p>So you can't just write a new recursor, with a different name, which runs on top of unmodded Lean 3.4.1?</p>

#### [ Mario Carneiro (May 01 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955538):
<p>You can, but you would have to do so for every inductive type</p>

#### [ Kevin Buzzard (May 01 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955548):
<p>but you could solve his one specific problem with <code>sum.rec</code>.</p>

#### [ Kevin Buzzard (May 01 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955590):
<p>I have to ask these stupid questions because I have no understanding of the status of these elab commands</p>

#### [ Kevin Buzzard (May 01 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955595):
<p>all I know is that if you don't like one, you can sometimes add an <code>@</code> and get another one</p>

#### [ Mario Carneiro (May 01 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955604):
<p>Sure, <code>or.elim</code> already exists and <code>sum.elim</code> could be similar</p>

#### [ Kevin Buzzard (May 01 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955859):
<p><code>example (a b c : Prop) : @or.elim a b c = @or.rec_on a b c := rfl</code></p>

#### [ Kevin Buzzard (May 01 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955868):
<p>so the only way these function differ is by magic</p>

#### [ Kevin Buzzard (May 01 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955871):
<p>as far as I am concerned</p>

#### [ Kevin Buzzard (May 01 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955929):
<p>Aah do they have different tags?</p>

#### [ Kevin Buzzard (May 01 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955943):
<p>Not only are they the same theorem</p>

#### [ Kevin Buzzard (May 01 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955947):
<p>they are the same proof</p>

#### [ Kevin Buzzard (May 01 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125955959):
<p>but one is tagged <code>[reducible]</code>and is protected</p>

#### [ Kevin Buzzard (May 01 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956008):
<p><code>[reducible]</code> is all about how eagerly the elaborator unfolds the definition, or something...</p>

#### [ Kevin Buzzard (May 01 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956015):
<p><code>protected</code> I have no idea. Something about avoiding overloading?</p>

#### [ Reid Barton (May 01 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956098):
<p><code>protected</code> means if you wrote <code>open or</code> (which you probably wouldn't), then you still wouldn't get the name <code>rec_on</code> as a synonym for <code>or.rec_on</code></p>

#### [ Kevin Buzzard (May 01 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956298):
<p>one is a def and one is a theorem. Does this make any difference?</p>

#### [ Kevin Buzzard (May 01 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956533):
<p><code>unknown identifier 'rec_on'</code></p>

#### [ Kevin Buzzard (May 01 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956543):
<p>so nobody is allowed to have <code>rec_on</code>?</p>

#### [ Kevin Buzzard (May 01 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956918):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">ordinal_notation</span>
<span class="kn">open</span> <span class="n">nonote</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">rec_on</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">rec_on :</span>
<span class="cm">  Π (o : nonote),</span>
<span class="cm">    ?M_1 0 →</span>
<span class="cm">    (Π (e : nonote) (n : ℕ+) (a : nonote) (h : below a e), ?M_1 e → ?M_1 a → ?M_1 (oadd e n a h)) → ?M_1 o</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kevin Buzzard (May 01 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125956920):
<p>Do I win five pounds?</p>

#### [ Reid Barton (May 01 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125957006):
<p>then that means that <code>nonote.rec_on</code> was not declared as protected</p>

#### [ Kevin Buzzard (May 01 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125957707):
<p>What is the complete list of unprotected <code>rec_on</code>s? And are these bugs?</p>

#### [ Kenny Lau (May 01 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125960643):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- This is a recursor-like theorem for `nonote` suggesting an</span>
<span class="cm">  inductive definition, which can&#39;t actually be defined this</span>
<span class="cm">  way due to conflicting dependencies. -/</span>
<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">def</span> <span class="n">rec_on</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">nonote</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">o</span> <span class="o">:</span> <span class="n">nonote</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="n">C</span> <span class="mi">0</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">e</span> <span class="n">n</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span> <span class="n">C</span> <span class="n">e</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">oadd</span> <span class="n">e</span> <span class="n">n</span> <span class="n">a</span> <span class="n">h</span><span class="o">))</span> <span class="o">:</span> <span class="n">C</span> <span class="n">o</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">o</span> <span class="k">with</span> <span class="n">o</span> <span class="n">h</span><span class="o">,</span> <span class="n">induction</span> <span class="n">o</span> <span class="k">with</span> <span class="n">e</span> <span class="n">n</span> <span class="n">a</span> <span class="n">IHe</span> <span class="n">IHa</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">H0</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">H1</span> <span class="bp">⟨</span><span class="n">e</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">fst</span><span class="bp">⟩</span> <span class="n">n</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">snd</span><span class="bp">⟩</span> <span class="n">h</span><span class="bp">.</span><span class="n">snd&#39;</span> <span class="o">(</span><span class="n">IHe</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">IHa</span> <span class="bp">_</span><span class="o">)</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>(set_theory.ordinal_notation, line 857)</p>

#### [ Kenny Lau (May 01 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125960644):
<p>it isn't automatically generated</p>

#### [ Kenny Lau (May 01 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum.rec/near/125960649):
<p>but indeed, <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> should have made it protected</p>


{% endraw %}
