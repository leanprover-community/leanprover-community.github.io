---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04805notationquestion.html
---

## Stream: [general](index.html)
### Topic: [notation question](04805notationquestion.html)

---


{% raw %}
#### [ Kevin Buzzard (May 06 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173744):
<p>The following might be impossible in Lean but I thought I'd ask. It's just an issue with notation.</p>

#### [ Kevin Buzzard (May 06 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173745):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">S</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="n">local</span> <span class="kn">infix</span> <span class="bp">`</span><span class="err">♥</span><span class="bp">`</span> <span class="o">:</span> <span class="mi">50</span> <span class="o">:=</span> <span class="n">R</span>

<span class="kn">definition</span> <span class="n">euclidean₁</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">{{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">S</span><span class="o">}},</span> <span class="n">x</span> <span class="err">♥</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">♥</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">♥</span> <span class="n">z</span>
<span class="kn">definition</span> <span class="n">euclidean₂</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">S</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">{{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">S</span><span class="o">}},</span> <span class="n">R</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">R</span> <span class="n">x</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">R</span> <span class="n">y</span> <span class="n">z</span>
<span class="kn">definition</span> <span class="n">euclidean₃</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">S</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">{{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">S</span><span class="o">}},</span> <span class="n">x</span> <span class="err">♥</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">♥</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">♥</span> <span class="n">z</span>
</pre></div>

#### [ Kevin Buzzard (May 06 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173746):
<p>(<code>\heartsuit</code> gives the heart, by the way)</p>

#### [ Kevin Buzzard (May 06 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173754):
<p>So mathematicians would normally _define_ a new relation with the infix notation, in contrast to functional programmers who want to define <code>R</code> first and then set up infix notation for it.</p>

#### [ Kevin Buzzard (May 06 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173755):
<p>This has the following annoying-for-mathematicians consequence.</p>

#### [ Kevin Buzzard (May 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173794):
<p>Definition 1 above is not so great because you can't see what you are defining -- it should say "euclidean1 heartsuit" or something.</p>

#### [ Kevin Buzzard (May 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173795):
<p>Definition 2 is correct, but doesn't use the notation, so mathematicians are left wondering why we have <code>R x y</code> instead of <code>x R y</code> or <code>x heartsuit y</code></p>

#### [ Kevin Buzzard (May 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173796):
<p>(infix notation is more normal in mathematics than CS perhaps)</p>

#### [ Kevin Buzzard (May 06 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173804):
<p>And definition 3 is wrong because the heart in the definition is unrelated to the R -- the heart is attached to the variable R and definition 3 introduces a new one.</p>

#### [ Kevin Buzzard (May 06 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173805):
<p>My dream is</p>

#### [ Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173806):
<p><code>definition euclidean_dream (R) := ∀ {{x y z : S}}, x ♥ y → x ♥ z → y ♥ z </code></p>

#### [ Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173843):
<p>but of course that doesn't even typecheck</p>

#### [ Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173847):
<p>Is there any way I can make my dream definition typecheck?</p>

#### [ Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173848):
<p>Actually I guess my dream is the impossible:</p>

#### [ Kevin Buzzard (May 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173849):
<p><code>definition euclidean_dream ♥ := ∀ {{x y z : S}}, x ♥ y → x ♥ z → y ♥ z </code></p>

#### [ Kevin Buzzard (May 06 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126173896):
<p>I don't mind a few incomprehensible lines with set-up beforehand, my question I guess is simply whether I can introduce a local variable in a definition and instantly have access to notation for it.</p>

#### [ Sebastian Ullrich (May 06 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126174227):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Something like this proposal? <a href="https://github.com/leanprover/lean/issues/1522#issuecomment-294872715" target="_blank" title="https://github.com/leanprover/lean/issues/1522#issuecomment-294872715">https://github.com/leanprover/lean/issues/1522#issuecomment-294872715</a></p>

#### [ Kevin Buzzard (May 06 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126174466):
<p>Yes! I didn't mention it in my posts above but I did try to do this with the type class notation types (indeed I wrote <code>has_heart</code> :-) ) but I couldn't get that to work either because <code>definition blah (S : Type) (R : S -&gt; S -&gt; Prop) [has_heart S]</code> wouldn't attach the heart to R and I couldn't figure out how to make the attachment whilst keeping it all looking clean and uncluttered. I am currently thinking a lot about trying to write code which looks really clean to mathematicians, who we can think of here as people who know exactly what a transitive binary relation is but have no idea what a typeclass is and don't want to see clutter when they are actually doing or reading mathematics in Lean.</p>

#### [ Reid Barton (May 06 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126176900):
<p>In Haskell you can convert an infix operator to an ordinary (prefix) function by surrounding the operator in parentheses. You can also use this notation at a binding site.<br>
The hypothetical Lean equivalent would be</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">euclidean</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">((</span><span class="err">♥</span><span class="o">)</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">S</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="o">{{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">S</span><span class="o">}},</span> <span class="n">x</span> <span class="err">♥</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">♥</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">♥</span> <span class="n">z</span>
</pre></div>

#### [ Kevin Buzzard (May 06 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20question/near/126178574):
<p>Lean would need to be told the associativity and left binding power, or at least default options for such things.</p>


{% endraw %}
