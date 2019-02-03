---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/88568Unificationhintspaper.html
---

## Stream: [Lean Together 2019](index.html)
### Topic: [Unification hints paper](88568Unificationhintspaper.html)

---


{% raw %}
#### [ William Whistler (Jan 10 2019 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154848944):
<p><a href="https://www.cs.unibo.it/~sacerdot/PAPERS/tphol09.pdf" target="_blank" title="https://www.cs.unibo.it/~sacerdot/PAPERS/tphol09.pdf">https://www.cs.unibo.it/~sacerdot/PAPERS/tphol09.pdf</a></p>

#### [ Karl Palmskog (Jan 10 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154849729):
<p>Paper by Gonthier et al. that takes unification hints to the limit for proof automation: <a href="https://software.imdea.org/~aleks/papers/lessadhoc/journal.pdf" target="_blank" title="https://software.imdea.org/~aleks/papers/lessadhoc/journal.pdf">https://software.imdea.org/~aleks/papers/lessadhoc/journal.pdf</a> - see also Coq code with examples <a href="https://github.com/coq-community/lemma-overloading" target="_blank" title="https://github.com/coq-community/lemma-overloading">https://github.com/coq-community/lemma-overloading</a></p>

#### [ Andrew Ashworth (Jan 10 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154873490):
<p>Interesting paper! I will have to explore the lemma-overloading library on the weekend.</p>

#### [ Assia Mahboubi (Jan 10 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154875627):
<p>And here is the <a href="https://hal.inria.fr/hal-00816703/file/main.pdf" target="_blank" title="https://hal.inria.fr/hal-00816703/file/main.pdf">tutorial paper</a>, from proceedings of itp 2013, on which this afternoon demos were based.</p>

#### [ Johan Commelin (Jan 11 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154903922):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> This was an extremely interested session. Lean has support for unification hints, and nobody knew about it... <span class="emoji emoji-1f600" title="grinning">:grinning:</span> You might be interested, and I guess skimming these papers is one way to get up to speed.</p>

#### [ Johan Commelin (Jan 11 2019 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154903964):
<p>Assia, was very surprised to hear that we had unbundled categories. We could at some point try unification hints in the hierarchy of categorical classes.</p>

#### [ Karl Palmskog (Jan 12 2019 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154966221):
<p>Aleks Nanevski recently presented the "unification hints to the limit" paper referenced above for a non-academic functional programming audience: <a href="https://www.youtube.com/watch?v=yFIaP1YCcxQ" target="_blank" title="https://www.youtube.com/watch?v=yFIaP1YCcxQ">https://www.youtube.com/watch?v=yFIaP1YCcxQ</a></p>
<div class="youtube-video message_inline_image"><a data-id="yFIaP1YCcxQ" href="https://www.youtube.com/watch?v=yFIaP1YCcxQ" target="_blank" title="https://www.youtube.com/watch?v=yFIaP1YCcxQ"><img src="https://i.ytimg.com/vi/yFIaP1YCcxQ/default.jpg"></a></div>

#### [ Johan Commelin (Jan 12 2019 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/154983884):
<p>That's a very nice talk! Thanks <span class="user-mention" data-user-id="198375">@Karl Palmskog</span><br>
Tl;dr: If you hate rewriting stuff by associativity and commutativity, the speaker shows how to use unification hints to make this completely transparent.</p>

#### [ Reid Barton (Jan 15 2019 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155160653):
<p>Very nice indeed.<br>
Here's a Lean analogue of the main example of the talk:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">lattice</span>
<span class="kn">open</span> <span class="n">lattice</span>
<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">semilattice_sup</span> <span class="n">α</span><span class="o">]</span>

<span class="n">class</span> <span class="n">le_sup_class</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">le</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">le_sup_class_self</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">le_sup_class</span> <span class="n">x</span> <span class="n">x</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="n">le_refl</span> <span class="n">x</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">le_sup_class_left</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">le_sup_class</span> <span class="n">x</span> <span class="n">y</span><span class="o">]</span> <span class="o">:</span> <span class="n">le_sup_class</span> <span class="n">x</span> <span class="o">(</span><span class="n">y</span> <span class="err">⊔</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="n">le_trans</span> <span class="n">h</span><span class="bp">.</span><span class="n">le</span> <span class="n">le_sup_left</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">le_sup_class_right</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">le_sup_class</span> <span class="n">x</span> <span class="n">z</span><span class="o">]</span> <span class="o">:</span> <span class="n">le_sup_class</span> <span class="n">x</span> <span class="o">(</span><span class="n">y</span> <span class="err">⊔</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="n">le_trans</span> <span class="n">h</span><span class="bp">.</span><span class="n">le</span> <span class="n">le_sup_right</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">le_sup</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">le_sup_class</span> <span class="n">x</span> <span class="n">y</span><span class="o">]</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">h</span><span class="bp">.</span><span class="n">le</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="err">⊔</span> <span class="o">((</span><span class="n">c</span> <span class="err">⊔</span> <span class="n">a</span><span class="o">)</span> <span class="err">⊔</span> <span class="n">d</span><span class="o">)</span> <span class="err">⊔</span> <span class="n">e</span> <span class="o">:=</span>
<span class="n">le_sup</span>
</pre></div>

#### [ Reid Barton (Jan 15 2019 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155161018):
<p>I guess it could just be <code>le_class</code>--you could put the fact <code>x ⊓ y ≤ x</code> into the same system.</p>

#### [ Kevin Buzzard (Jan 15 2019 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155161531):
<p>The point is that type class inference did the dirty work for you.</p>

#### [ Johan Commelin (Jan 15 2019 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164104):
<p>And then, in the talk they used "canonical structures" instead of type class inference. I don't know if unification hints would give an additional benefit over type class inference...</p>

#### [ Johan Commelin (Jan 15 2019 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164150):
<p>I really like Reid's example. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What is your opinion on these things? Do you think they are useful? Or just cute hacks?</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164159):
<p>My very poor understanding of Cyril's point was that canonical structures and unification hints made a different part of the system do the work.</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164160):
<p>I've used them in restricted circumstances</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164208):
<p>this is slightly different from Cyril's unification hints</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164233):
<p>I have an example from <code>dioph</code> where I use typeclass inference to prove natural number inequalities so I can write things like <code>&amp;5 : fin 10</code> with an appropriate notation</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164258):
<p>Can one prove <code>a+b+c+d+e+f+g+h=b+(f+h)+(c+e+(a+g+d))</code> like this?</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164337):
<p>not easily</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155164358):
<p>I'll stick to <code>ring</code> :-)</p>

#### [ Gabriel Ebner (Jan 15 2019 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165730):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Of course you can, thanks for asking!  (But seriously, please use <code>simp</code> or <code>ring</code> instead.)</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>

<span class="n">class</span> <span class="n">ac_cancel_core</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">out_param</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">is_eq</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">c</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">ac_cancel_core</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">left</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">ac_cancel_core</span> <span class="n">a</span> <span class="n">b</span> <span class="n">d</span><span class="o">]</span> <span class="o">:</span> <span class="n">ac_cancel_core</span> <span class="n">a</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="n">c</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="bp">.</span><span class="n">is_eq</span><span class="o">]</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="n">right</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">ac_cancel_core</span> <span class="n">a</span> <span class="n">c</span> <span class="n">d</span><span class="o">]</span> <span class="o">:</span> <span class="n">ac_cancel_core</span> <span class="n">a</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="n">d</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="bp">.</span><span class="n">is_eq</span><span class="o">]</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="n">refl</span> <span class="o">:</span> <span class="n">ac_cancel_core</span> <span class="n">a</span> <span class="n">a</span> <span class="mi">0</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span>

<span class="kn">end</span> <span class="n">ac_cancel_core</span>

<span class="n">class</span> <span class="n">ac_cancel</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">out_param</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">is_eq</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">c</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">ac_cancel</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">core</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">ac_cancel_core</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">]</span> <span class="o">:</span> <span class="n">ac_cancel</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="bp">.</span><span class="n">is_eq</span><span class="o">]</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">ac_cancel</span> <span class="mi">0</span> <span class="n">b</span> <span class="n">b</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="n">plus</span> <span class="o">[</span><span class="n">h1</span> <span class="o">:</span> <span class="n">ac_cancel</span> <span class="n">a</span> <span class="n">c</span> <span class="n">d</span><span class="o">]</span> <span class="o">[</span><span class="n">h2</span> <span class="o">:</span> <span class="n">ac_cancel</span> <span class="n">b</span> <span class="n">d</span> <span class="n">e</span><span class="o">]</span> <span class="o">:</span> <span class="n">ac_cancel</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span> <span class="n">c</span> <span class="n">e</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h1</span><span class="bp">.</span><span class="n">is_eq</span><span class="o">,</span> <span class="n">h2</span><span class="bp">.</span><span class="n">is_eq</span><span class="o">]</span><span class="bp">⟩</span>

<span class="kn">end</span> <span class="n">ac_cancel</span>

<span class="kn">lemma</span> <span class="n">ac_refl</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">h</span> <span class="o">:</span> <span class="n">ac_cancel</span> <span class="n">a</span> <span class="n">b</span> <span class="mi">0</span><span class="o">]</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="bp">.</span><span class="n">is_eq</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span><span class="bp">+</span><span class="o">(</span><span class="n">c</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">c</span><span class="bp">+</span><span class="n">a</span><span class="o">)</span><span class="bp">+</span><span class="n">b</span> <span class="o">:=</span> <span class="n">ac_refl</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span><span class="bp">+</span><span class="n">b</span> <span class="bp">=</span> <span class="n">b</span><span class="bp">+</span><span class="n">a</span> <span class="o">:=</span> <span class="n">ac_refl</span>

<span class="c1">-- fails due to maximum class instance depth</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">e</span> <span class="n">f</span> <span class="n">g</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="bp">+</span><span class="n">c</span><span class="bp">+</span><span class="n">d</span><span class="bp">+</span><span class="n">e</span><span class="bp">+</span><span class="n">f</span><span class="bp">+</span><span class="n">g</span><span class="bp">+</span><span class="n">h</span><span class="bp">=</span><span class="n">b</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span><span class="bp">+</span><span class="n">h</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">c</span><span class="bp">+</span><span class="n">e</span><span class="bp">+</span><span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">g</span><span class="bp">+</span><span class="n">d</span><span class="o">))</span> <span class="o">:=</span>
<span class="n">ac_refl</span>
</pre></div>

#### [ Kevin Buzzard (Jan 15 2019 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165937):
<p>Oh wow! :-) So again if I've understood correctly, this is Lean's type class unification doing the work here, so C++, as opposed to if I used <code>ring</code> when it would be an algorithm written in Lean. </p>
<p>Wait -- did Gabriel just write the <code>add_comm_group</code> tactic which sometimes comes up? After Mario's <code>ring</code> people noticed that whilst it solved many of the questions that schoolkids would find trivial (like the one in my example), we were missing variants. One was a variant which solved problems in <code>add_comm_group</code>s and one was a variant which solved problems in modules. Neither of these things are rings, so the tactic had limited use in these situations.</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165968):
<p>Or maybe <code>simp</code> already does this case? But again this is a different part of the system I guess.</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165972):
<p>I would say that the algorithm is "written in lean" in this case</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165974):
<p>it's basically using lean like prolog</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165981):
<p>remember that "prolog like search" thing?</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155165984):
<p>vividly</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155166033):
<p>this is how you write programs in prolog, as big backtracking searches</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155166043):
<p>you have to be very careful about what instances you put in the classes, as they control the search</p>

#### [ Patrick Massot (Jan 15 2019 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155168520):
<p>See also the examples in <a href="https://github.com/leanprover/presentations/tree/master/20170116_POPL/backchain" target="_blank" title="https://github.com/leanprover/presentations/tree/master/20170116_POPL/backchain">https://github.com/leanprover/presentations/tree/master/20170116_POPL/backchain</a></p>

#### [ Patrick Massot (Jan 15 2019 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Unification%20hints%20paper/near/155168644):
<p>In particular <a href="https://github.com/leanprover/presentations/blob/master/20170116_POPL/backchain/back.lean#L87-L88" target="_blank" title="https://github.com/leanprover/presentations/blob/master/20170116_POPL/backchain/back.lean#L87-L88">https://github.com/leanprover/presentations/blob/master/20170116_POPL/backchain/back.lean#L87-L88</a> directly mentions that paper</p>


{% endraw %}
