---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52991makeexplicitargumentimplicit.html
---

## Stream: [general](index.html)
### Topic: [make explicit argument implicit](52991makeexplicitargumentimplicit.html)

---


{% raw %}
#### [ Zesen Qian (Jul 30 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130584404):
<p>Hi, is it possible to temprorarily make an argument implicit? Say, instead of <code>id bool true</code>, I write something like <code>id _ true</code> and let the elaborator to infer the omitted argument for me. (id : \forall A, A -&gt; A is completely explicit)</p>

#### [ Zesen Qian (Jul 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585249):
<p>funny, seems lean can already do it exactly like I demonstrated. never knew that.</p>

#### [ Reid Barton (Jul 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585255):
<p>You can already write <code>id _ true</code> and the elaborator will infer the argument (though <code>true</code> is a <code>Prop</code>, not a <code>bool</code>).<br>
Did you have something else in mind?</p>

#### [ Reid Barton (Jul 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585263):
<p>Ah, okay.</p>

#### [ Reid Barton (Jul 30 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585319):
<p>A useful trick with this is also to define a notation <code>local notation `id'` := id _</code> if you want to make an argument implicit in an entire file/section of code.</p>

#### [ Zesen Qian (Jul 30 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20explicit%20argument%20implicit/near/130585371):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> good, thanks.</p>


{% endraw %}
