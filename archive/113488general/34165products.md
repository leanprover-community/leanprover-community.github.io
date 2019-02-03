---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34165products.html
---

## Stream: [general](index.html)
### Topic: [products](34165products.html)

---


{% raw %}
#### [ Patrick Massot (Jul 30 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130544059):
<p>If I have <code>(a b c : Type) (f : a → b) (g : a → c)</code>, do we have a name or notation for the function mapping <code>x</code> to <code>(f x, g x)</code>?</p>

#### [ Sebastian Ullrich (Jul 30 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545155):
<p>We probably don't yet, but Haskell has one, if anyone wants to copy that</p>
<div class="codehilite"><pre><span></span>&gt; :t (&amp;&amp;&amp;)
(&amp;&amp;&amp;) :: Arrow a =&gt; a b c -&gt; a b c&#39; -&gt; a b (c, c&#39;)
&gt; :t snd &amp;&amp;&amp; fst
snd &amp;&amp;&amp; fst :: (a, c) -&gt; (c, a)
</pre></div>


<p>where <code>Arrow</code> is an abstraction of functions <a href="https://wiki.haskell.org/Arrow_tutorial" target="_blank" title="https://wiki.haskell.org/Arrow_tutorial">https://wiki.haskell.org/Arrow_tutorial</a></p>

#### [ Simon Hudon (Jul 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545270):
<p>For this particular operator, <code>applicative</code> is sufficient: <code>x &amp;&amp;&amp; y = prod.mk &lt;$&gt; x &lt;*&gt; y</code> </p>
<p>(that is to say, we only need <code>applicative (a b)</code>)</p>

#### [ Patrick Massot (Jul 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545321):
<p>You're trying to scare me with your notations</p>

#### [ Patrick Massot (Jul 30 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545322):
<p>It works pretty well</p>

#### [ Simon Hudon (Jul 30 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545369):
<p>What works well? Scaring you or using the notation?</p>

#### [ Patrick Massot (Jul 30 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545371):
<p>scaring me</p>

#### [ Simon Hudon (Jul 30 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545382):
<p>Oh, good, so my work here is done</p>

#### [ Simon Hudon (Jul 30 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545488):
<p>As far as I know, the definition is not in mathlib so you make it as simple as you need and leave it to others to generalize so that it looks more like Haskell (the generalization has a few stumbling blocks I think)</p>

#### [ Patrick Massot (Jul 30 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545538):
<p>Ok, I may do that. But first I'll sleep. Thanks!</p>

#### [ Simon Hudon (Jul 30 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545596):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Simon Hudon (Jul 30 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130545597):
<p>Good night!</p>

#### [ Nicholas Scheel (Jul 30 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130583767):
<p>here’s some discussion on the Arrow class: <a href="https://www.eyrie.org/~zednenem/2017/07/twist" target="_blank" title="https://www.eyrie.org/~zednenem/2017/07/twist">https://www.eyrie.org/~zednenem/2017/07/twist</a></p>
<p>PureScript has opted not to create an Arrow class (see link 3 above); instead it just defined <code>(&amp;&amp;&amp;)</code> using <code>Strong</code> and <code>Category</code>: <a href="https://pursuit.purescript.org/packages/purescript-profunctor/4.0.0/docs/Data.Profunctor.Strong#v:fanout" target="_blank" title="https://pursuit.purescript.org/packages/purescript-profunctor/4.0.0/docs/Data.Profunctor.Strong#v:fanout">https://pursuit.purescript.org/packages/purescript-profunctor/4.0.0/docs/Data.Profunctor.Strong#v:fanout</a></p>

#### [ Simon Hudon (Jul 30 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130586742):
<p>I think in Haskell as well, people think Arrow might not have been the right abstraction</p>

#### [ Sebastian Ullrich (Jul 30 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130587542):
<blockquote>
<p>PureScript has opted not to create an Arrow class (see link 3 above); instead it just defined <code>(&amp;&amp;&amp;)</code> using <code>Strong</code> and <code>Category</code>: <a href="https://pursuit.purescript.org/packages/purescript-profunctor/4.0.0/docs/Data.Profunctor.Strong#v:fanout" target="_blank" title="https://pursuit.purescript.org/packages/purescript-profunctor/4.0.0/docs/Data.Profunctor.Strong#v:fanout">https://pursuit.purescript.org/packages/purescript-profunctor/4.0.0/docs/Data.Profunctor.Strong#v:fanout</a></p>
</blockquote>
<p>Is there actually any implementation anywhere apart from <code>Function</code> <span class="emoji emoji-1f605" title="sweat smile">:sweat_smile:</span> ? But thanks for the information!</p>

#### [ Nicholas Scheel (Jul 30 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/products/near/130589452):
<p>haha, we can go one step away from Function with Star <span class="emoji emoji-1f609" title="wink">:wink:</span> <a href="https://github.com/purescript/purescript-profunctor/blob/v4.0.0/src/Data/Profunctor/Star.purs#L70" target="_blank" title="https://github.com/purescript/purescript-profunctor/blob/v4.0.0/src/Data/Profunctor/Star.purs#L70">https://github.com/purescript/purescript-profunctor/blob/v4.0.0/src/Data/Profunctor/Star.purs#L70</a> (actually that package has a variety of profunctors, a number of which implement Strong)</p>


{% endraw %}
