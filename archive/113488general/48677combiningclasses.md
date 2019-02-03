---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48677combiningclasses.html
---

## Stream: [general](index.html)
### Topic: [combining classes](48677combiningclasses.html)

---


{% raw %}
#### [ Reid Barton (Dec 13 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151584488):
<p>If I have <code>class C t extends A t, B t.</code> I guess it doesn't mean that anything which is an instance of <code>A</code> and <code>B</code> is automatically an instance of <code>C</code>? Does it make sense to write an instance for <code>C</code> to make that true?</p>

#### [ Reid Barton (Dec 13 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151584538):
<p>hmm, it seems not to be a good idea.</p>

#### [ Mario Carneiro (Dec 13 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151585886):
<p>no, it means that a <code>C t</code> is an <code>A t</code> and a <code>B t</code></p>

#### [ Mario Carneiro (Dec 13 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151585889):
<p>so that instance would be a loop</p>

#### [ Reid Barton (Dec 13 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586018):
<p>So is it a bad idea to define this class <code>C</code> in the first place then?</p>

#### [ Mario Carneiro (Dec 13 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586529):
<p>It has the same concerns as any other class introduction</p>

#### [ Reid Barton (Dec 13 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586740):
<p>I can't use C as a shorthand for A + B though</p>

#### [ Reid Barton (Dec 13 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586752):
<p>because I don't see any way to arrange that there is an instance of C whenever there is one of both A and B</p>

#### [ Reid Barton (Dec 13 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586801):
<p>In GHC, this works because GHC doesn't have these weird backwards instances "try to get A from C"</p>

#### [ Reid Barton (Dec 13 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586810):
<p>In particular, I'm looking at <a href="https://github.com/leanprover/mathlib/blob/master/category_theory/fully_faithful.lean#L52" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/category_theory/fully_faithful.lean#L52">https://github.com/leanprover/mathlib/blob/master/category_theory/fully_faithful.lean#L52</a></p>

#### [ Johan Commelin (Dec 13 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151587244):
<p>Right, so I've only been proving that things are <code>fully_faithful</code> but I never put it as an assumption. It's a bit awkard.</p>

#### [ Reid Barton (Dec 13 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151587292):
<p>I guess that works, to an extent</p>

#### [ Johan Commelin (Dec 13 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151588362):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> But you would also want the type class system to try to deduce that <code>F</code> is <code>full</code> by searching for an instance that <code>F</code> is <code>fully_faithful</code> (which you say GHC wouldn't do). So the search <em>must</em> go both ways. We really need a smarter system, that wouldn't run into these <em>trivial</em> loops.</p>

#### [ Mario Carneiro (Dec 13 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151588420):
<p>GHC would require that you prove <code>F</code> is <code>full</code> before proving it is <code>fully_faithful</code>, so it doesn't have to do the search</p>

#### [ Andrew Ashworth (Dec 13 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590559):
<p>The smarter you make type class search, the more memory it will use... I'm sure you could use high power search techniques like contraction hierarchies, along with keeping visited nodes in memory so you could detect loops... I suspect/speculate it hasn't been done because 90% of CS users would riot over the unnecessary resource usage in large projects that do not need these features. Maybe I'm completely off-base.</p>

#### [ Andrew Ashworth (Dec 13 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590617):
<p>It would definitely be interesting to benchmark different algorithms over a large code-base though - those would be interesting results.</p>

#### [ Johan Commelin (Dec 13 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590726):
<p>I understand.</p>

#### [ Kevin Buzzard (Dec 13 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590731):
<p>Mathematicians seem to me to be a class of users who are constantly running into these issues with the type class system though.</p>

#### [ Johan Commelin (Dec 13 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590737):
<p>Lean 4 will give us the possibility to swap out the type class search algorithm...</p>

#### [ Johan Commelin (Dec 13 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590739):
<p>So then everyone can be happy.</p>

#### [ Kevin Buzzard (Dec 13 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590801):
<p>You made <code>group</code> a class and we thought "Oh I get it, a locally analytic topological vector space must be a class" and then it turns out that it's harder than that</p>

#### [ Kevin Buzzard (Dec 13 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590860):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> in a given use case you could try adding the loopy instance with priority 0, and then hope that this discouragement is enough in practice. It feels like any code you ship should come with a warning though.</p>

#### [ Kevin Buzzard (Dec 13 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590875):
<p>The system would be likely to loop rather than fail so for buggy code where it should error with a failure you'll instead perhaps get a more obscure error</p>

#### [ Kevin Buzzard (Dec 13 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590987):
<p>Johan I guess I made one explicit example of where we weren't happy very clear to Sebastian the other day -- type class inference failing to unify two terms of a subsingleton type -- so he knows we want more here. Loops are another issue. We definitely want them. "Defeq loops" should be fine but even they can cause problems because the system doesn't abort. "Oh look we've been here before -- let's press on"</p>

#### [ Gabriel Ebner (Dec 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151594433):
<p>Haskell has this nice <a href="https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/glasgow_exts.html#the-constraint-kind" target="_blank" title="https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/glasgow_exts.html#the-constraint-kind">constraint kinds extension</a>, which allows you to define aliases for combinations of type classes:</p>
<div class="codehilite"><pre><span></span><span class="kr">type</span> <span class="kt">Stringy</span> <span class="n">a</span> <span class="ow">=</span> <span class="p">(</span><span class="kt">Read</span> <span class="n">a</span><span class="p">,</span> <span class="kt">Show</span> <span class="n">a</span><span class="p">)</span> <span class="c1">-- Read and Show are type classes</span>
<span class="kr">type</span> <span class="kt">C</span> <span class="n">t</span> <span class="ow">=</span> <span class="p">(</span><span class="kt">A</span> <span class="n">t</span><span class="p">,</span> <span class="kt">B</span> <span class="n">t</span><span class="p">)</span> <span class="c1">-- Reid&#39;s example</span>
</pre></div>


<p>In principle, there is no fundamental reason why we couldn't do something like this in Lean as well.  <span class="user-mention" data-user-id="112680">@Johan Commelin</span> I wouldn't count on customizing type class inference.</p>

#### [ Johan Commelin (Dec 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151594520):
<p>Ooh, too bad. I thought I heard at some point that it would be possible...</p>


{% endraw %}
