---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54332reduceisabitslow.html
---

## Stream: [general](index.html)
### Topic: [#reduce is a bit slow?](54332reduceisabitslow.html)

---


{% raw %}
#### [ Arseniy Alekseyev (Jul 17 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129783924):
<p>These reductions work a bit slow for me:</p>
<div class="codehilite"><pre><span></span>#reduce (10 : fin 3) -- over 10 seconds
#reduce (15 : fin 3) -- over 5 minutes
</pre></div>


<p>Is this normal? :-)</p>

#### [ Simon Hudon (Jul 17 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784259):
<p>It is. Natural numbers are represented in unary notation so arithmetic on them in the kernel (not the VM) is bound to be slow. Numerals such as <code>(15 : fin 3)</code> are represented using the <code>bit0</code>, <code>bit1</code> and <code>zero</code> functions as <code>bit1 (bit1 (bit1 (bit1 zero)))</code> and <code>bit1 (x : a) := x + x + 1</code>. You're a getting a bunch of additions and each one is one addition and one modulo.</p>

#### [ Mario Carneiro (Jul 17 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784278):
<p>yes, #reduce is very slow, particularly for well founded recursive functions like mod. I would estimate this is something like cubic in the <em>value</em> of <code>n : fin 3</code> there</p>

#### [ Simon Hudon (Jul 17 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784327):
<p>If you want to test your definitions, I recommend <code>#eval</code></p>

#### [ Simon Hudon (Jul 17 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784340):
<p>It uses the virtual machine instead of the kernel to do its computations.</p>

#### [ Arseniy Alekseyev (Jul 17 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784454):
<p>Ah, #eval is probably what I want. Thanks! <br>
@Mario, I figured unary numbers were the reason, but I'm not sure cubic is enough to explain it. Could it also be exponential due to call-by-name somewhere? Does lean use call-by-name?</p>

#### [ Mario Carneiro (Jul 17 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784467):
<p>cubic in the value of n means exponential in the length</p>

#### [ Mario Carneiro (Jul 17 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784536):
<p>And yes, #reduce is essentially call by name execution, although it's not exactly implemented that way</p>

#### [ Arseniy Alekseyev (Jul 17 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784540):
<p>Not sure what you mean, the value is 15: 15 cubed is not a large number. Do you call value something else?</p>

#### [ Mario Carneiro (Jul 17 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784547):
<p>I mean 15 cubed</p>

#### [ Mario Carneiro (Jul 17 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129784583):
<p>but there is also a large constant factor due to the kernel manipulation of expressions at every stage (the expressions get huge, like 100000 lines long)</p>

#### [ Arseniy Alekseyev (Jul 17 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129785191):
<p>Ok, the expression (1 + 1 + 1 + 1 ... : fin 20) has clear exponential scaling: the time ~exactly doubles with each +1. The binary encoding (as explained by Simon) made the timings of the original example much more random-looking.</p>

#### [ Mario Carneiro (Jul 17 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129785300):
<p>actually on second thought I'm not sure if it is really exponential, since it is in fact <code>bit0</code> on <code>fin 3</code>, which should be constant time - it does not first calculate <code>15 : nat</code> and then turn it into a <code>fin 3</code></p>

#### [ Arseniy Alekseyev (Jul 17 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129785576):
<p>Given that it's approximately as slow as the empirically exponential-time (1 + 1 + ... ), I say it's almost certainly the same. Mod 3 won't help if all the call-by-name-duplication of the terms happens before you have a chance to compute the mod.</p>

#### [ Mario Carneiro (Jul 17 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129785673):
<p>I honestly don't know exactly what kind of optimization if any is in place for duplication caused by beta reduction, but it is surely nonzero - I'm pretty sure there is a whnf_core cache which allows to avoid repeated calculation of normal forms</p>

#### [ Simon Hudon (Jul 17 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129785938):
<p>Still, because we're talking about <code>fin</code>, you perform the modulo at every addition</p>

#### [ Simon Hudon (Jul 17 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129785953):
<p>It does not do it in nat first. All those <code>1</code>s are of type <code>fin 3</code></p>

#### [ Arseniy Alekseyev (Jul 17 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129786041):
<p>probably type class stuff has something to do with it too because replacing + with fin.add makes it fast again</p>

#### [ Mario Carneiro (Jul 17 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129786062):
<p>that's very strange</p>

#### [ Mario Carneiro (Jul 17 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129786070):
<p>typeclass stuff should be a negligible fraction of the work</p>

#### [ Arseniy Alekseyev (Jul 17 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129786199):
<p>I guess with call-by-name it's not really about the work but about whether you somehow duplicate the argument or not (and whether or not the detection you mentioned kicks in)</p>

#### [ Arseniy Alekseyev (Jul 17 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129786231):
<p>anyway, I'm going to stop looking because #eval solves my problem and sounds like this slowness is expected. thanks!</p>

#### [ Arseniy Alekseyev (Jul 17 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129800058):
<p>Even more pathological example:</p>
<div class="codehilite"><pre><span></span>#reduce (λ (x : nat) (y : x &lt; 1), (fin.mk x y + 0 : fin 1)) -- 5 seconds
#reduce (λ (x : nat) (y : x &lt; 2), (fin.mk x y + 0 : fin 2)) -- &gt; 1 minute
</pre></div>


<p>no "15" necessary :-)</p>

#### [ Gabriel Ebner (Jul 17 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129800675):
<p>Please be aware that <code>fin</code> contains both a natural number <em>and</em> a proof.  The <code>#reduce</code> command normalizes both parts, including the proof.  You can use <code>set_option pp.all true</code> to see the full term.  If you run <code>#reduce (10 : fin 3).1</code>, you'll only get the number (in unary) but not the proof; this is a bit faster.</p>

#### [ Gabriel Ebner (Jul 17 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129800677):
<p>In any case, avoid kernel computation.</p>

#### [ Kevin Buzzard (Jul 17 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20is%20a%20bit%20slow%3F/near/129800877):
<p>Lean was not designed to do fully-verified computation quickly :-) <code>#reduce 10000+10000</code> will bring the system to its knees. This is the whole point of <code>#eval</code></p>


{% endraw %}
