---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27427howdoestypeclassinferencework.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [how does type class inference work?](https://leanprover-community.github.io/archive/113488general/27427howdoestypeclassinferencework.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Dec 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151259224):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">foo</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">blah</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="n">class</span> <span class="n">bar</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">foo</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">blah2</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span>

<span class="n">class</span> <span class="n">baz</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">foo</span> <span class="n">A</span> <span class="bp">.</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">bar</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="o">{</span><span class="n">blah</span> <span class="o">:=</span> <span class="mi">4</span><span class="o">,</span> <span class="n">blah2</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">bar</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- works</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">baz</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- fails</span>
</pre></div>


<p>Why doesn't this work?</p>

#### [ Mario Carneiro (Dec 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151259885):
<p>why would it work? You declared an instance of <code>bar</code> but not <code>baz</code></p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260147):
<p>I can figure out how to make an instance of <code>baz</code>, that's why I can believe it would work. All the fields are there. This is my problem -- I don't know what the type class inference system is _doing_.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260186):
<p>Oh sorry there's a typo -- I meant to write</p>
<p><code>example : foo ℤ := by apply_instance -- works</code></p>
<p>I didn't declare an instance of <code>foo</code> but it found it anyway.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260244):
<p>I literally do not know what it can and cannot do.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260256):
<p>All I know is that it can do less than me, because I can solve <code>baz</code>.</p>

#### [ Kenny Lau (Dec 10 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260277):
<p><code>class baz (A : Type) extends foo A .</code><br>
this creates an instance <code>baz.to_foo</code></p>

#### [ Kenny Lau (Dec 10 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260291):
<p>if you want to make <code>baz</code> from <code>foo</code> then you would need to use <code>{ .. infer_instance }</code></p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260308):
<p>Well, maybe I should just create an instance <code>baz.from_foo</code></p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260369):
<p>or maybe <code>foo.to_baz</code> would be more appropriate.</p>

#### [ Kenny Lau (Dec 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260399):
<p>congratulations, you've thrown yourself into a loop</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260514):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">foo</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">blah</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="n">class</span> <span class="n">bar</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">foo</span> <span class="n">A</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">blah2</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span>

<span class="n">class</span> <span class="n">baz</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">foo</span> <span class="n">A</span> <span class="bp">.</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">bar</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="o">{</span><span class="n">blah</span> <span class="o">:=</span> <span class="mi">4</span><span class="o">,</span> <span class="n">blah2</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- works</span>

<span class="c1">-- type class inference is so stupid, why doesn&#39;t it just guess this.</span>
<span class="kn">instance</span> <span class="n">foo</span><span class="bp">.</span><span class="n">to_baz</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">foo</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">baz</span> <span class="n">A</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- fails? WTF?</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">baz</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- still fails</span>
</pre></div>


<p>I broke everything.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260535):
<p>I don't understand why everything is broken. Everything is defeq, right?</p>

#### [ Kenny Lau (Dec 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260617):
<p>you now have <code>foo.to_baz</code> and <code>baz.to_foo</code></p>

#### [ Kenny Lau (Dec 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260621):
<p>so the machine gets stuck forever</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260645):
<p><code>example (A : Type) (H : foo A) : H = baz.to_foo A := rfl</code></p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260716):
<p>I don't understand why it gets stuck forever. What is it doing? I am pretty convinced it's not playing the "let's see how many instances I can make from this instance, for no reason whatsoever" game. I ask the type class inference system to produce me a term of a typeclass, it should just try and try until it finds one and then stop.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260728):
<p>Of course I completely understand that I have made a loop. What I don't understand is why this even matters.</p>

#### [ Kenny Lau (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260734):
<p>oh it <em>is</em> playing that game</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260737):
<p>It is??</p>

#### [ Kenny Lau (Dec 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260742):
<p>wait no it isn't</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260756):
<p>But your response makes me think that you can write some simple thing which will make it play this game.</p>

#### [ Kenny Lau (Dec 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260772):
<p>well you want it to figure out <code>baz</code>. then it goes like "hey I can make this from <code>foo</code>". then it goes like "hey I can make this from <code>baz</code>". ad nauseam</p>

#### [ Kenny Lau (Dec 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260775):
<p>so maybe priority is the answer</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260823):
<p>Do you know where it starts? At the top or the bottom?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260859):
<p>It says "Hmm, I want to make  an instance of <code>baz A</code>". Now does it say "OK so how do we make instances of <code>baz A</code>? or does it say "OK what other typeclasses can I make with <code>A</code>"? Hmm, I guess it must be the former.</p>

#### [ Kenny Lau (Dec 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260883):
<p>it is the former</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260925):
<p>So the type class system looks through <em>all instances</em> and tries to find one whose head term is <code>baz</code>?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260929):
<p>Say it finds ten such things. What does it do now?</p>

#### [ Kenny Lau (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260970):
<p>apply each one</p>

#### [ Kenny Lau (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260973):
<p>(but mind you, it uses depth-first search)</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260979):
<p>"Head term" -- is that the right phrase? I mean "a term which is a function <code>baz [something]</code></p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151260983):
<p>What is depth-first search?</p>

#### [ Kenny Lau (Dec 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261002):
<p>depth-first search = dig this hole as deep as possible until you find gold or you are blocked by a stone, and then move on to the next hole</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261014):
<p>Is this the one where it finds the first instance of <code>baz A</code> and finds that it needs <code>moo A</code> and it checks for a term of type <code>moo A</code> and temporarily forgets all about the other nine ideas about <code>baz</code> and just looks for <code>moo</code> stuff?</p>

#### [ Kenny Lau (Dec 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261087):
<p>breadth-first search = dig this hole 1 cm, go to next hole and dig 1cm, and so on until you run out of holes, and then go back to the first hole and dig 1cm, etc</p>

#### [ Kenny Lau (Dec 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261114):
<blockquote>
<p>Is this the one where it finds the first instance of <code>baz A</code> and finds that it needs <code>moo A</code> and it checks for a term of type <code>moo A</code> and if it can't find that it forgets all about the other nine ideas about <code>baz</code> and just looks for <code>moo</code> stuff?</p>
</blockquote>
<p>precisely</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261125):
<p>How does it conclude that it is blocked by a stone?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261151):
<p>Can this only happen when there are literally no instances which have the right head term or whatever the phrase is?</p>

#### [ Kenny Lau (Dec 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261160):
<p>yes</p>

#### [ Kenny Lau (Dec 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261214):
<p>so for example there is no instance that produces <code>ordered_canonical_discrete_ordered_field</code> or whatever the flying that is</p>

#### [ Kenny Lau (Dec 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261221):
<p>because it's the highest structure</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261260):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">H1</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H11</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H1</span> <span class="n">A</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H12</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H1</span> <span class="n">A</span> <span class="bp">.</span>
</pre></div>


<p>Does this segfault for you?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261317):
<p>I am trying to do some simple experiments.</p>

#### [ Kenny Lau (Dec 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261336):
<p>no it doesn't</p>

#### [ Sebastian Ullrich (Dec 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261421):
<blockquote>
<p>Can this only happen when there are literally no instances which have the right head term or whatever the phrase is?</p>
</blockquote>
<p>No, it's sufficient that no instance of the target class can be unified with the target</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261476):
<p>Hmm, thanks, I'll restart VS Code.</p>

#### [ Kenny Lau (Dec 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261537):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> what's the difference?</p>

#### [ Patrick Massot (Dec 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261551):
<p>The head symbol could match but not the rest</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261571):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">H1</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H11</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H1</span> <span class="n">A</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H12</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H1</span> <span class="n">A</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H111</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H11</span> <span class="n">A</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H121</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H12</span> <span class="n">A</span> <span class="bp">.</span>

<span class="kn">instance</span> <span class="n">H1</span><span class="bp">.</span><span class="n">to_H11</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H1</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">H11</span> <span class="n">A</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">instance</span> <span class="n">H11</span><span class="bp">.</span><span class="n">to_H111</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H11</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">H111</span> <span class="n">A</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">H121</span> <span class="n">unit</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">H111</span> <span class="n">unit</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>


<p>That seems to have gone really well.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261646):
<p>I am trying to get into trouble. I am trying to get max class inference thingy error</p>

#### [ Kenny Lau (Dec 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261672):
<p>but you didn't create any loop...</p>

#### [ Kenny Lau (Dec 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261675):
<p>oh wait you did</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261679):
<p>Right, H1 and H11 loop</p>

#### [ Kevin Buzzard (Dec 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151261682):
<p>but I managed to get past the loop and up to H111</p>

#### [ Patrick Massot (Dec 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262058):
<p>Kevin, in your case there exactly one instance to try at each step, and it clearly succeeds without ever risking a loop:</p>
<div class="codehilite"><pre><span></span>[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : H111 unit := @H11.to_H111 ?x_1 ?x_2
[class_instances] (1) ?x_2 : H11 unit := @H1.to_H11 ?x_3 ?x_4
[class_instances] (2) ?x_4 : H1 unit := @H12.to_H1 ?x_5 ?x_6
[class_instances] (3) ?x_6 : H12 unit := @H121.to_H12 ?x_7 ?x_8
[class_instances] (4) ?x_8 : H121 unit := unit.H121
</pre></div>


<p>You can simply draw the instance graph and see it</p>

#### [ Kevin Buzzard (Dec 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262747):
<p>I want to make it get stuck in a loop</p>

#### [ Kevin Buzzard (Dec 10 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262764):
<p>To find <code>H111</code> it suffices to find <code>H1</code>. Can I make it look for <code>H1</code> by going back to <code>H12</code>?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262817):
<p>Oh I see, that instance is not even there.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262875):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">H1</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H11</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H1</span> <span class="n">A</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H12</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H1</span> <span class="n">A</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H111</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H11</span> <span class="n">A</span> <span class="bp">.</span>

<span class="n">class</span> <span class="n">H121</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">H12</span> <span class="n">A</span> <span class="bp">.</span>

<span class="kn">instance</span> <span class="n">H1</span><span class="bp">.</span><span class="n">to_H11</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H1</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">H11</span> <span class="n">A</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">instance</span> <span class="n">H11</span><span class="bp">.</span><span class="n">to_H111</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H11</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">H111</span> <span class="n">A</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">instance</span> <span class="n">H1</span><span class="bp">.</span><span class="n">to_H12</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H1</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">H12</span> <span class="n">A</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">instance</span> <span class="n">H12</span><span class="bp">.</span><span class="n">to_H121</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">H12</span> <span class="n">A</span><span class="o">]</span> <span class="o">:</span> <span class="n">H121</span> <span class="n">A</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">H121</span> <span class="n">unit</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">H111</span> <span class="n">unit</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- max depth reached</span>
</pre></div>


<p>Bingo.</p>

#### [ Kevin Buzzard (Dec 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151262890):
<p>So whatever is type class inference thinking here? Why go back to <code>H12</code> when we have been there already?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263019):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">class_instances</span> <span class="n">true</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">H111</span> <span class="n">unit</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- max depth reached</span>
</pre></div>


<p>gives random stuff such as</p>
<div class="codehilite"><pre><span></span>[class_instances] (0) ?x_0 : has_one ℕ := unsigned.has_one
</pre></div>


<p>Who said anything about nat?</p>

#### [ Kevin Buzzard (Dec 10 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263079):
<p>I'm glad the type class inference system's job isn't finding its way out of mazes.</p>

#### [ Mario Carneiro (Dec 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263165):
<p>usually one writes a depth first search with a search stack to prevent loops like this</p>

#### [ Patrick Massot (Dec 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263180):
<p>The nat thing is related to my question to Sebastian about shortcut. It has nothing to do with your problem, it's something Lean solves for itself in its meta-work</p>

#### [ Mario Carneiro (Dec 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263184):
<p>I'm not sure why typeclass inference doesn't have one</p>

#### [ Mario Carneiro (Dec 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263234):
<p>then again, this wouldn't prevent problems with loops that look different the second time around</p>

#### [ Mario Carneiro (Dec 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151263243):
<p>i.e. the same instances are being used but the instantiations are different</p>

#### [ Kevin Buzzard (Dec 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151264966):
<p>OK this is great. I have to interview a bunch of people now but I will probably be back later on with more dumb questions. This has been a great start. Thanks to all.</p>

#### [ Joe Hendrix (Dec 10 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20type%20class%20inference%20work%3F/near/151390897):
<p>Conceptually, Lean could require one to prove instance backchaining is well-founded.  Haskell has static checks to ensure this, but those can be bypassed via language pragma.</p>


{% endraw %}
