---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78536UBUHxs.html
---

## Stream: [general](index.html)
### Topic: [λ (⟨U,BU,Hx,s⟩](78536UBUHxs.html)

---


{% raw %}
#### [ Kevin Buzzard (May 18 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741686):
<p>In the middle of defining a big structure, I have <code>(λ (a : X), sorry)</code>, where X is some explicit structure which takes four...erm...inputs or whatever they're called. Everything typechecks fine. The moment I replace <code>(λ (a : X), sorry)</code> with <code>(λ (⟨U,BU,Hx,s⟩ : X),sorry)</code> I get three errors on the <code>⟨</code> (and plenty more errors too) -- <code>invalid binder, identifier expected</code>, <code>invalid match/convoy expression, expected type is not known</code> and <code>invalid type ascription, term has type
  Π (_x : ?m_1), ?m_2[_x] : Sort (imax ? ?)
but is expected to have type
  X : Type u</code>. What is going on? If I try to fill in some more sorries, are things likely to get better or worse?</p>

#### [ Mario Carneiro (May 18 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741736):
<p>You can't add types to a lambda match</p>

#### [ Mario Carneiro (May 18 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741743):
<p>the syntax is literally <code>λ ⟨U,BU,Hx,s⟩, term</code></p>

#### [ Mario Carneiro (May 18 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741748):
<p>stuff like <code>λ (⟨U,BU,Hx,s⟩ : X), term</code> or <code>λ ⟨U,BU,Hx,(s:t)⟩, term</code> is not well formed</p>

#### [ Kevin Buzzard (May 18 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741942):
<p>Oh!</p>

#### [ Kevin Buzzard (May 18 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741966):
<p>And there was me trying to be helpful</p>

#### [ Kevin Buzzard (May 18 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741971):
<p>Thanks Mario.</p>

#### [ Kevin Buzzard (May 18 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741976):
<p>What is the logic behind that?</p>

#### [ Mario Carneiro (May 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742103):
<p>it's just the way the syntax is. I would appreciate more space to give type ascriptions (and in particular to provide explicit types which are defeq to the "default" types), but that's a lean issue.</p>

#### [ Kevin Buzzard (May 18 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742169):
<p>The moment I take this away I am faced with <code>invalid match/convoy expression, expected type is not known</code> errors</p>

#### [ Mario Carneiro (May 18 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742283):
<p>You will often not be able to use lambda match for this reason, since it requires type information fairly early in the elaboration process. Typing <code>by exact λ ⟨U,BU,Hx,s⟩, term</code> may help, and you can also use type ascription for the whole lambda, i.e. <code>(λ ⟨U,BU,Hx,s⟩, term : X -&gt; Y)</code></p>

#### [ Kevin Buzzard (May 18 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742363):
<p>I tried type ascription for the whole lambda and it didn't seem to fix the problem.</p>

#### [ Kevin Buzzard (May 18 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742410):
<p>Maybe I should get on with some marking and come back to this later on. Thanks for the tips.</p>

#### [ Kevin Buzzard (May 18 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742415):
<p>If I still struggle I will attempt to minimise and ask again.</p>

#### [ Kevin Buzzard (May 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743335):
<p><code>context: 'eliminator' elaboration is not used for 'quotient.lift' because resulting type is not of the expected form</code></p>

#### [ Kevin Buzzard (May 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743336):
<p>whatever that means</p>

#### [ Kevin Buzzard (May 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743340):
<p>I have explicitly written the type of everything</p>

#### [ Kevin Buzzard (May 18 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743379):
<p>and I replace <code>lam  (b : X), ...</code></p>

#### [ Kevin Buzzard (May 18 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743380):
<p>with <code>lam \&lt;A,B,C,D\&gt;,...</code></p>

#### [ Kevin Buzzard (May 18 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743381):
<p>and I am dead</p>

#### [ Kevin Buzzard (May 18 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743382):
<p>and everything after the ... has been given an explicit type etc</p>

#### [ Kevin Buzzard (May 18 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743393):
<p>aah</p>

#### [ Kevin Buzzard (May 18 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743396):
<p>and now the <code>by exact</code> trick works</p>

#### [ Kevin Buzzard (May 18 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743439):
<p>so in fact I had to use both <code>by exact</code> and type ascription for the whole lambda. What a struggle! Thanks Mario as ever.</p>

#### [ Kevin Buzzard (May 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743454):
<p>The URL for this topic is <code>.../topic/.CE.BB.20(.E2.9F.A8U.2CBU.2CHx.2Cs.E2.9F.A9</code></p>

#### [ Kevin Buzzard (May 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743455):
<p>:-)</p>

#### [ Kevin Buzzard (May 18 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743576):
<p>The other irritation was that after almost every edit in VS Code, I had to drag the file up and down to see what the actual errors, if any, were. Somehow the localised "just try and process the bit the user is working on" thing worked very poorly in this instance.</p>

#### [ Gabriel Ebner (May 18 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743921):
<p>You can click on the <code>Lean: (checking ...)</code> status bar item on the bottom to change what parts of the file are being checked.</p>

#### [ Kevin Buzzard (May 19 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126797317):
<p>Oh this is news to me -- and helpful news too! Thanks Gabriel.</p>


{% endraw %}
