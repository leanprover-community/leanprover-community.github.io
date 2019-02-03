---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/44342Definitionwithimplicittypes.html
---

## Stream: [new members](index.html)
### Topic: [Definition with implicit types](44342Definitionwithimplicittypes.html)

---


{% raw %}
#### [ Ken Roe (Jul 11 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437343):
<p>Can someone correct the syntax for this definition:</p>
<p>def bind_option : {Π X : Type}, {Π Y : Type},<br>
                option X → (X → option Y)<br>
                      → option Y<br>
| option.none f := @option.none Y<br>
| (option.some x) f := f x</p>

#### [ Simon Hudon (Jul 11 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437504):
<p>What error do you get?</p>

#### [ Simon Hudon (Jul 11 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437545):
<p>Also, can you enclose your code between three ticks: </p>
<div class="codehilite"><pre><span></span>```lean
-- your code here
```
</pre></div>

#### [ Chris Hughes (Jul 11 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437565):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">bind_option</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:</span>
<span class="n">option</span> <span class="n">X</span> <span class="bp">→</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">Y</span><span class="o">)</span>
<span class="bp">→</span> <span class="n">option</span> <span class="n">Y</span>
<span class="bp">|</span> <span class="n">option</span><span class="bp">.</span><span class="n">none</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">option</span><span class="bp">.</span><span class="n">none</span> <span class="n">Y</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">option</span><span class="bp">.</span><span class="n">some</span> <span class="n">x</span><span class="o">)</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">x</span>
</pre></div>

#### [ Chris Hughes (Jul 11 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437580):
<p>pattern matching is done on everything after the colon, which is why is moved the Types before the colon.</p>

#### [ Kenny Lau (Jul 11 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437585):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">bind_option</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:</span>
<span class="n">option</span> <span class="n">X</span> <span class="bp">→</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">Y</span><span class="o">)</span>
<span class="bp">→</span> <span class="n">option</span> <span class="n">Y</span>
<span class="bp">|</span> <span class="n">none</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">none</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">some</span> <span class="n">x</span><span class="o">)</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">x</span>
</pre></div>

#### [ Chris Hughes (Jul 11 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437635):
<p>Also Pi should be out of the brackets like this <code> Π {X Y : Type},</code></p>

#### [ Chris Hughes (Jul 11 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437641):
<p>If you were to put the Types after the colon.</p>

#### [ Chris Hughes (Jul 11 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129437648):
<p>Incidentally this function exists in the library and it's called <code>option.bind</code> I think</p>

#### [ Ken Roe (Jul 11 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438139):
<p>Not quite--I get the following error on the "f x" term of the last line:</p>
<p>function expected at<br>
  f x<br>
term has type<br>
  option Y</p>

#### [ Mario Carneiro (Jul 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438270):
<p>perhaps you have something on the following line(s)?</p>

#### [ Mario Carneiro (Jul 11 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438273):
<p>after the definition</p>

#### [ Ken Roe (Jul 11 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438577):
<p>This was the problem.  The error goes away if I add a period.</p>

#### [ Mario Carneiro (Jul 11 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438647):
<p>Usually we fix this by just having the next line start with some kind of command like <code>def</code>, <code>namespace</code>, or a comment. Presumably that line is giving you an error anyway otherwise</p>

#### [ Kenny Lau (Jul 11 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129438654):
<p>what can there be after that thing? I think all my lines start with keywords</p>

#### [ Sebastian Ullrich (Jul 11 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129456152):
<p>Btw, we're thinking of not allowing function applications to stretch over empty lines in Lean 4 to fix such issues. I do hope that would not break anyone's weird code...?</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129456661):
<p>I see newbie errors like this all the time (I'm currently teaching Lean to a bunch of people)</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129456667):
<p>the function expects one or two more values so it just starts eating into the next command</p>

#### [ Kevin Buzzard (Jul 11 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Definition%20with%20implicit%20types/near/129456671):
<p>resulting in errors which completely throw the user</p>


{% endraw %}
