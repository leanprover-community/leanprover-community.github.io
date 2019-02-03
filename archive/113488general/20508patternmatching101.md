---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20508patternmatching101.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [pattern matching 101](https://leanprover-community.github.io/archive/113488general/20508patternmatching101.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 25 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662292):
<p>Easy question: how do I do pattern matching against values? Given <code>k : nat</code>, naively I could try writing</p>
<div class="codehilite"><pre><span></span>match n with
| k := something
| _ := something_else
end
</pre></div>


<p>a glorified <code>if n = k then something else something_else</code>, but of course this doesn't work, because Lean doesn't treat the <code>k</code> in the pattern as related to the earlier <code>k</code>.</p>
<p>Am I just meant to use <code>if ... then ... else</code>? Or can I get the pattern matcher to help me?</p>

#### [ Kenny Lau (Apr 25 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662332):
<p>you need to use <code>if then else</code>. <code>match</code> only deals with constructors.</p>

#### [ Scott Morrison (Apr 25 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662414):
<p>That's what I feared. How sad. So if I want to write something that given <code>some n</code> where <code>n = k</code> does <code>X</code>, and given any other <code>some n</code> or <code>none</code> does <code>Y</code>... What's the idiomatic way to write this?</p>

#### [ Scott Morrison (Apr 25 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662422):
<p>(Preferably your answer shouldn't use <code>option.is_some</code> or friends, just pretend <code>option</code> is a bare inductive type with no dressing up.)</p>

#### [ Scott Morrison (Apr 25 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662463):
<p>In particular, how can I do this without writing the symbol <code>Y</code> twice?</p>

#### [ Sebastian Ullrich (Apr 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662781):
<p>Other languages have pattern guards for this, but Lean doesn't... yet. You'll have to factor <code>Y</code> out into a <code>let</code>.</p>

#### [ Sean Leather (Apr 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662792):
<blockquote>
<p>That's what I feared. How sad. So if I want to write something that given <code>some n</code> where <code>n = k</code> does <code>X</code>, and given any other <code>some n</code> or <code>none</code> does <code>Y</code>... What's the idiomatic way to write this?</p>
</blockquote>
<p>This sounds like something you'd use pattern match guards for in Haskell:</p>
<div class="codehilite"><pre><span></span><span class="kr">case</span> <span class="n">n</span> <span class="kr">of</span>
  <span class="kt">Just</span> <span class="n">k</span> <span class="o">|</span> <span class="n">n</span> <span class="o">==</span> <span class="n">k</span> <span class="ow">-&gt;</span> <span class="n">something</span>
  <span class="kr">_</span> <span class="ow">-&gt;</span> <span class="n">something_else</span>
</pre></div>

#### [ Kenny Lau (Apr 25 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662838):
<blockquote>
<p>In particular, how can I do this without writing the symbol <code>Y</code> twice?</p>
</blockquote>
<p><code>if o = some k then _ else Y</code></p>

#### [ Scott Morrison (Apr 25 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662856):
<p>okay, good, except I've over-minimised of course, and there are lots of other fields that I don't care about matching :-)</p>

#### [ Kenny Lau (Apr 25 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125662899):
<p>so maybe give us more context?</p>

#### [ Simon Hudon (Apr 25 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125671684):
<p>Is it possible that your type is like the following?</p>
<div class="codehilite"><pre><span></span>inductive my_type
| constr : a -&gt; b -&gt; c -&gt; d -&gt; e -&gt; my_type
| other : a&#39; -&gt; b&#39; -&gt; my_type
</pre></div>


<p>In Haskell, a common advice is to make that two or more types, separate the sum aspect and the product aspect.</p>

#### [ Simon Hudon (Apr 25 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125671764):
<p>Then, you can use selectors on to access whatever part of the product that you care about</p>

#### [ Scott Morrison (Apr 25 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125671847):
<p>hmm, my type </p>
<div class="codehilite"><pre><span></span>inductive edit_distance_progress (l₁: list α) (l₂: list α)
| exactly : ℕ → edit_distance_progress
| at_least : ℕ → partial_edit_distance_data α → edit_distance_progress
</pre></div>

#### [ Scott Morrison (Apr 25 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125671851):
<p>and I need to check if I have an <code>exactly _ _ k</code> for some specified value of <code>k</code>.</p>

#### [ Simon Hudon (Apr 25 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672040):
<p>Ok, it's not as bad as I thought. I thought because you didn't want to repeat <code>Y</code>. Is it a pattern for <code>partial_edit_distance_data α</code>?</p>

#### [ Scott Morrison (Apr 25 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672190):
<p>I'm not sure what you mean. The offending code (which works, just looks gross) is &lt;<a href="https://github.com/semorrison/lean-tidy/blob/master/src/tidy/rewrite_search.lean#L64-L84" target="_blank" title="https://github.com/semorrison/lean-tidy/blob/master/src/tidy/rewrite_search.lean#L64-L84">https://github.com/semorrison/lean-tidy/blob/master/src/tidy/rewrite_search.lean#L64-L84</a>&gt;. You can see lines 72-74 and lines 76-78 are almost identical because of this.</p>

#### [ Sean Leather (Apr 25 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672413):
<p>Why can't you do something like <code>if update_edit_distance h.distance = exactly _ _ k then ... else ...</code> as Kenny suggested?</p>

#### [ Scott Morrison (Apr 25 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672494):
<p>Oh... somehow I thought those <code>_</code>s would be a problem, but of course they're not. Thank you!</p>

#### [ Scott Morrison (Apr 25 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672566):
<p>I will need an extra decidable instance for this. I remember there is some trick for synthesising decidable instances for boring inductive types....? Anyone remember?</p>

#### [ Sean Leather (Apr 25 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672589):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">decidable_eq</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="bp">...</span>
</pre></div>

#### [ Scott Morrison (Apr 25 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672652):
<p>Lovely! And where do I find out what derive is doing? :-)</p>

#### [ Sean Leather (Apr 25 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672714):
<p>I'm sure there's a <code>#print</code> that'll tell you, but I never remember which one. <span class="emoji emoji-1f60a" title="blush">:blush:</span></p>

#### [ Sean Leather (Apr 25 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pattern%20matching%20101/near/125672780):
<p>Perhaps <code>#print &lt;type-name&gt;.decidable_eq</code>?</p>


{% endraw %}
