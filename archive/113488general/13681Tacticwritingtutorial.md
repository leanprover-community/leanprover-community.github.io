---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13681Tacticwritingtutorial.html
---

## Stream: [general](index.html)
### Topic: [Tactic writing tutorial](13681Tacticwritingtutorial.html)

---


{% raw %}
#### [ Patrick Massot (Dec 03 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758082):
<p>More and more people are writing tactics, and providing bits of explanations here, but I never remember. So I decided to use my last hope option: I tried to teach it. The result is at <a href="https://github.com/leanprover-community/mathlib/blob/tactic_tutorial/docs/extras/tactic_writing.md" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tactic_tutorial/docs/extras/tactic_writing.md">https://github.com/leanprover-community/mathlib/blob/tactic_tutorial/docs/extras/tactic_writing.md</a> Not only I hope this will help me remember this stuff, but also I hope it will allow experts to clear my misconceptions. And of course it would be a nice extra if it could teach someone something useful, so I'd be interested to know if any tactic writing newbie can read it (I know Johan already read it, because he carefully monitors our community repository).</p>

#### [ Patrick Massot (Dec 03 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758135):
<p>Of course I also hope more stuff will be added here, by me or others. Don't hesitate to contribute, it's in the community repository.</p>

#### [ Mario Carneiro (Dec 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758907):
<p>This is a really nice writeup. A comment: the "pseudo-python" syntax</p>
<div class="codehilite"><pre><span></span><span class="n">t</span> <span class="o">=</span> <span class="n">infer_type</span><span class="p">(</span><span class="n">H</span><span class="p">)</span>
<span class="k">return</span> <span class="n">H</span> <span class="k">if</span> <span class="n">unify</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">t</span><span class="p">)</span> <span class="k">else</span> <span class="n">find_matching_type</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">HS</span><span class="p">)</span>
</pre></div>


<p>was a bit confusing for me due to the infix conditional. Is this really how they do it in python? How about something a bit more C-like:</p>
<div class="codehilite"><pre><span></span><span class="n">t</span> <span class="o">=</span> <span class="n">infer_type</span><span class="p">(</span><span class="n">H</span><span class="p">)</span>
<span class="k">if</span> <span class="n">unify</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">t</span><span class="p">):</span>
  <span class="k">return</span> <span class="n">H</span>
<span class="k">else</span><span class="p">:</span>
  <span class="n">find_matching_type</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">HS</span><span class="p">)</span>
</pre></div>

#### [ Mario Carneiro (Dec 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758978):
<p>although it occurs to me that what lean is doing with <code>unify</code> is more like a try catch than a conditional:</p>
<div class="codehilite"><pre><span></span><span class="n">t</span> <span class="o">=</span> <span class="n">infer_type</span><span class="p">(</span><span class="n">H</span><span class="p">)</span>
<span class="k">try</span><span class="p">:</span>
  <span class="n">unify</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">t</span><span class="p">)</span>
  <span class="k">return</span> <span class="n">H</span>
<span class="n">catch</span><span class="p">:</span>
  <span class="n">find_matching_type</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">HS</span><span class="p">)</span>
</pre></div>

#### [ Patrick Massot (Dec 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150758996):
<p>What I wrote is indeed valid python</p>

#### [ Johan Commelin (Dec 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759013):
<p>Yes, I thought so as well. So why did you call it pseudo-python?</p>

#### [ Patrick Massot (Dec 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759019):
<p>But I agree the <code>try</code>/<code>except</code> (not catch) version is closer to what is happening in Lean. But I didn't want to include too much python...</p>

#### [ Patrick Massot (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759058):
<p>You guys need to learn more python</p>

#### [ Mario Carneiro (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759063):
<p>(NB: I don't know python, I'm inventing pythonic syntax on the fly. code highlighting says the word isn't <code>catch</code>)</p>

#### [ Mario Carneiro (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759064):
<p>ah</p>

#### [ Patrick Massot (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759076):
<p>Maybe I should switch to a more generic imperative pseudo-code</p>

#### [ Mario Carneiro (Dec 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759091):
<p>the funny thing is I've written several complete programs in python, but some of the syntax differences are meh</p>

#### [ Mario Carneiro (Dec 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759560):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> you should take a look at this</p>

#### [ Mario Carneiro (Dec 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759657):
<blockquote>
<p>Parsing a token is introduced by <code>lean.parser.tk</code> followed by a string which must be taken from a predetermined list (the initial value of this list seems to be hardwired into Lean source code, in <code>frontends/lean/token_table.cpp</code>). </p>
</blockquote>
<p>This list is added to when you use literals in <code>notation</code>, <code>infix</code>, or <code>precedence</code>.</p>

#### [ Mario Carneiro (Dec 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759735):
<p>Importantly, marking something as a token causes it to no longer be a valid name, just like <code>have</code></p>

#### [ Mario Carneiro (Dec 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759767):
<p>which is why so many interactive tactics use the same few tokens <code>:</code> <code>using</code> <code>generalizing</code> <code>with</code> for separators</p>

#### [ Patrick Massot (Dec 03 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759857):
<p>Thanks Mario, this is one of the places where I hoped there would be clarifications</p>

#### [ Patrick Massot (Dec 03 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150759997):
<p>Jeremy, I hope you don't mind I'm invading PIL's territory, but this tutorial is written from a different perspective, more hands-on and shallow. And of course you can contribute too!</p>

#### [ Patrick Massot (Dec 03 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150760035):
<p>Note to myself: I should replace paths to the core library or Lean source code with actual http links</p>

#### [ Mario Carneiro (Dec 03 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150760593):
<p>For the monad cheat sheet:</p>
<ul>
<li><code>return</code>: produce a value in the monad (type: <code>A -&gt; m A</code>)</li>
<li><code>ma &gt;&gt;= f</code>: get the value of type <code>A</code> from <code>ma : m A</code> and pass it to <code>f : A -&gt; m B</code>. Alternate syntax: <code>do a &lt;- ma, f a</code></li>
<li><code>f &lt;$&gt; ma</code>: apply the function <code>f : A -&gt; B</code> to the value in <code>ma : m A</code> to get a <code>m B</code>. Same as <code>do a &lt;- ma, return (f a)</code></li>
<li><code>ma &gt;&gt; mb</code>: same as <code>do a &lt;- ma, mb</code>; here the return value of <code>ma</code> is ignored and then <code>mb</code> is called. Alternate syntax: <code>do ma, mb</code></li>
<li><code>mf &lt;*&gt; ma</code>: same as <code>do f &lt;- mf, f &lt;$&gt; ma</code>, or <code>do f &lt;- mf, a &lt;- ma, return (f a)</code>.</li>
<li><code>ma &lt;* mb</code>: same as <code>do a &lt;- ma, mb, return a</code></li>
<li><code>ma *&gt; mb</code>: same as <code>do ma, mb</code>, or <code>ma &gt;&gt; mb</code>. Why two notations for the same thing? Historical reasons</li>
<li><code>pure</code>: same as <code>return</code>. Again, historical reasons</li>
</ul>

#### [ Mario Carneiro (Dec 03 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150760832):
<ul>
<li><code>failure</code>: failed value (specific monads usually have a more useful form of this, like <code>fail</code> and <code>failed</code> for tactics)</li>
<li><code>ma &lt;|&gt; ma'</code> recover from failure: runs <code>ma</code> and if it fails then runs <code>ma'</code>.</li>
<li><code>a $&gt; mb</code>: same as <code>const a &lt;$&gt; mb</code> or <code>do mb, return a</code></li>
<li><code>ma &lt;$ b</code>: same as <code>const b &lt;$&gt; ma</code> or <code>do ma, return b</code></li>
</ul>

#### [ Scott Morrison (Dec 03 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150761418):
<p>oof <code>&lt;*</code> and <code>&lt;$</code> are so confusing... "return the value on the ???"</p>

#### [ Patrick Massot (Dec 03 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150797886):
<p>Does anyone know how to print the list of currently registered tokens?</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150797962):
<p><code>#print notation</code></p>

#### [ Mario Carneiro (Dec 03 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798018):
<p>hm, <code>generalizing</code> isn't on that list</p>

#### [ Patrick Massot (Dec 03 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798100):
<p>with and using are not there either</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798650):
<p>Reading the code, I don't see any other way of listing all tokens, although you can test if a name is a token easily enough</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798684):
<p>i.e. <code>#print wit</code> and <code>#print with</code> give different errors</p>

#### [ Kenny Lau (Dec 03 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150798705):
<p>so... it is a Δ1 set</p>

#### [ Patrick Massot (Dec 03 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799491):
<blockquote>
<ul>
<li><code>a $&gt; mb</code>: same as <code>const a &lt;$&gt; mb</code> or <code>do mb, return a</code></li>
<li><code>ma &lt;$ b</code>: same as <code>const b &lt;$&gt; ma</code> or <code>do ma, return b</code></li>
</ul>
</blockquote>
<p>Are these <code>const</code> descriptions really correct? It looks like <code>const</code> is missing its type argument</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799644):
<p>it's implicit</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799649):
<p><code>const a := λ_, a</code></p>

#### [ Mario Carneiro (Dec 03 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799732):
<p>Actually most of these are actually defined using <code>const</code>, many more than I used, but it's not a very transparent way to write it</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799786):
<p><code>map_const α β := map ∘ const β</code></p>

#### [ Mario Carneiro (Dec 03 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799793):
<p>crystal clear</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799857):
<p><code>map_const</code> is <code>&lt;$</code> btw</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799885):
<p>oops, it's not implicit</p>

#### [ Patrick Massot (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799889):
<p>Here I see <code>function.const : Π {α : Sort u_1} (β : Sort u_2), α → β → α</code></p>

#### [ Patrick Massot (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799899):
<p>And I don't see how it would make sense to have it implicit</p>

#### [ Patrick Massot (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799903):
<p>how would you infer it?</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799923):
<p>you would normally write that with B implicit</p>

#### [ Mario Carneiro (Dec 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150799939):
<p>because it's inferrable from the last argument</p>

#### [ Patrick Massot (Dec 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150800016):
<p>when you apply the constant function yes, but not when talking about the function</p>

#### [ Mario Carneiro (Dec 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150800017):
<p>but <code>const</code> is often used partially applied, and in that case having it implicit can be problematic</p>

#### [ Patrick Massot (Dec 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150800035):
<p>we're almost synchronous</p>

#### [ Patrick Massot (Dec 03 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150804993):
<p>So, should I open a PR, or are there more suggestions, contributions, or questions?</p>

#### [ Rob Lewis (Dec 03 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150806366):
<p>This looks really nice, Patrick, thanks! I see a few small mistakes/typos. I can make adjustments myself or comment on a PR, either way is no problem. But it's bedtime now, so tomorrow.</p>

#### [ Jeremy Avigad (Dec 04 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150814115):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Indeed, this is very nice. Do you want to consider becoming one of the authors of Programming in Lean? For personal reasons, I'd like to maintain tight control over TPiL (because it has been a labor of love for a number of years), but we never got very far with PiL, and I'd be happy to have collaborators for that. (We added Jared Roesch to the list of authors early on, because he intended to work on it, but in the end he never did, so his name should be removed.) In Amsterdam, I can show you how to set up and maintain the Sphinx repository (but maybe you are already comfortable doing that).  A caveat: the repository is set up for a Linux installation of Sphinx, and I don't know if it is possible to get it running on Windows. (I know that Rob Lewis has had trouble getting our Logic and Proof running on Windows.)</p>

#### [ Patrick Massot (Dec 04 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150833320):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> Thanks for the kind words and your trust. I think there is room for both an informal tutorial and PIL. But I'd love to help with any documentation project. I've already compiled TPIL, so I guess I could handle compiling PIL as well.  I'm tempted to write we can discuss all this in Amsterdam, but unfortunately I'll be extremely busy after the Amsterdam workshop, so maybe we should start now, especially if you have something specific in mind (not that I really have time, but it will be much worse after Christmas).</p>

#### [ Patrick Massot (Dec 04 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150833394):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> please feel free to correct typos and mistakes directly. The community repository is dedicated to that. I think you can even do the correction from github, without pulling the branch. And pulling the branch won't be a problem either, there is nothing to compile, it's all markdown.</p>

#### [ Patrick Massot (Dec 04 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20writing%20tutorial/near/150833417):
<p>Actually maybe we should consider including a Lean file gathering all examples from the tutorial. I have it on my computer of course, but I wouldn't know where to put it in the repository</p>


{% endraw %}
