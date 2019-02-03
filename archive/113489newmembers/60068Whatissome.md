---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60068Whatissome.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [What is `some`?](https://leanprover-community.github.io/archive/113489newmembers/60068Whatissome.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135790900):
<p>I'm learning non-constructive definitions from <em><a href="https://leanprover.github.io/introduction_to_lean/introduction_to_lean.pdf" target="_blank" title="https://leanprover.github.io/introduction_to_lean/introduction_to_lean.pdf">An Introduction to Lean</a></em> (p. 25) and the command <code>some h</code> is used -- what does it mean?</p>

#### [ Kenny Lau (Oct 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135790908):
<p><code>h : \alpha |- some h : option \alpha</code></p>

#### [ Chris Hughes (Oct 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135790924):
<p>It's <code>classical.some</code>. Given a proof that <code>exists x, p x</code>, classical.some will return that <code>x</code></p>

#### [ Chris Hughes (Oct 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135790968):
<p>Ignore Kenny, he's talking about <code>option.some</code> which is completely different.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791033):
<blockquote>
<p>It's <code>classical.some</code>. Given a proof that <code>exists x, p x</code>, classical.some will return that <code>x</code></p>
</blockquote>
<p>Oh nice -- so it's the eliminator for <code>exists</code>? But how is it different from <code>exists.elim</code>, or doing cases on the proof?</p>

#### [ Patrick Massot (Oct 14 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791057):
<p>It's the non-broken one, yes</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791100):
<p><code>exists.elim</code> actually is broken? That explains a lot of problems I've had. Is it broken for finite sets too or only where choice is needed?</p>

#### [ Chris Hughes (Oct 14 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791157):
<p>Almost. If you're trying to make a proof then you don't need it, you can just use <code>cases</code> or <code>exists.elim</code>. It's only if you're trying to make data that you need it. The one difference is between this and other eliminators is that you don't have<br>
<code>classical.some (exists.intro x h) = x</code>, since this would cause contradictions because of proof irrelevance. <code>exists.elim</code> is not actually broken, that's just something people like to say when making fun of constructive mathematics.</p>

#### [ Kenny Lau (Oct 14 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791218):
<p><code>s/people/Patrick Massot/</code></p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791383):
<p>Count me in too. Some of us don't care about constructive maths because we've spent decades doing normal maths and we're not going to change now. Others are younger and more open to these wacky ideas.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791431):
<p>Ps Abhi you should never have to ask what anything is. Copy and paste the code into a Lean session, make sure it compiles, and then just right-click on the thing that you want to know about.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791496):
<blockquote>
<p>Ps Abhi you should never have to ask what anything is. Copy and paste the code into a Lean session, make sure it compiles, and then just right-click on the thing that you want to know about.</p>
</blockquote>
<p>Yeah, I didn't realise it was something in the <code>classical</code> library. I thought it was something like <code>have</code>, which you can check, but won't really give anything useful.</p>

#### [ Chris Hughes (Oct 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791502):
<p>Sometimes the definitions can be a bit mysterious to a newcomer. <code>classical.some</code> is probably one of those</p>

#### [ Kevin Buzzard (Oct 14 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791503):
<p><a href="/user_uploads/3121/DmskDK_GG1JoMmyzIS7d-gMq/some.png" target="_blank" title="some.png">some.png</a> the <code>some</code> you're talking about is in <code>classical.lean</code>. Admittedly its definition is complicated :-/</p>
<div class="message_inline_image"><a href="/user_uploads/3121/DmskDK_GG1JoMmyzIS7d-gMq/some.png" target="_blank" title="some.png"><img src="/user_uploads/3121/DmskDK_GG1JoMmyzIS7d-gMq/some.png"></a></div>

#### [ Kevin Buzzard (Oct 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791520):
<p>On the other hand, the last chapter of TPIL, which no doubt you have read because you've had all of about 8 days to learn about this stuff (;-) ) explains something about the <code>classical</code> stuff.</p>

#### [ Patrick Massot (Oct 14 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791521):
<p>it could be worse (of course you need to understand the <code>{... // ...}</code> notation</p>

#### [ Mario Carneiro (Oct 14 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/What%20is%20%60some%60%3F/near/135791627):
<p>Yeah, I wouldn't say that's a particularly complicated definition. The complicated one is <code>epsilon</code>, which is surprisingly rarely used but is basically the same as <code>some</code> except you don't even need to prove existence first</p>


{% endraw %}
