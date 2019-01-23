---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78536UBUHxs.html
---

## Stream: [general](index.html)
### Topic: [λ (⟨U,BU,Hx,s⟩](78536UBUHxs.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741686):
In the middle of defining a big structure, I have `(λ (a : X), sorry)`, where X is some explicit structure which takes four...erm...inputs or whatever they're called. Everything typechecks fine. The moment I replace `(λ (a : X), sorry)` with `(λ (⟨U,BU,Hx,s⟩ : X),sorry)` I get three errors on the `⟨` (and plenty more errors too) -- `invalid binder, identifier expected`, `invalid match/convoy expression, expected type is not known` and `invalid type ascription, term has type
  Π (_x : ?m_1), ?m_2[_x] : Sort (imax ? ?)
but is expected to have type
  X : Type u`. What is going on? If I try to fill in some more sorries, are things likely to get better or worse?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 18 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741736):
You can't add types to a lambda match

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 18 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741743):
the syntax is literally `λ ⟨U,BU,Hx,s⟩, term`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 18 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741748):
stuff like `λ (⟨U,BU,Hx,s⟩ : X), term` or `λ ⟨U,BU,Hx,(s:t)⟩, term` is not well formed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741942):
Oh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741966):
And there was me trying to be helpful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741971):
Thanks Mario.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126741976):
What is the logic behind that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 18 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742103):
it's just the way the syntax is. I would appreciate more space to give type ascriptions (and in particular to provide explicit types which are defeq to the "default" types), but that's a lean issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742169):
The moment I take this away I am faced with `invalid match/convoy expression, expected type is not known` errors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 18 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742283):
You will often not be able to use lambda match for this reason, since it requires type information fairly early in the elaboration process. Typing `by exact λ ⟨U,BU,Hx,s⟩, term` may help, and you can also use type ascription for the whole lambda, i.e. `(λ ⟨U,BU,Hx,s⟩, term : X -> Y)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742363):
I tried type ascription for the whole lambda and it didn't seem to fix the problem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742410):
Maybe I should get on with some marking and come back to this later on. Thanks for the tips.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126742415):
If I still struggle I will attempt to minimise and ask again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743335):
`context: 'eliminator' elaboration is not used for 'quotient.lift' because resulting type is not of the expected form`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743336):
whatever that means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743340):
I have explicitly written the type of everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743379):
and I replace `lam  (b : X), ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743380):
with `lam \<A,B,C,D\>,...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743381):
and I am dead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743382):
and everything after the ... has been given an explicit type etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743393):
aah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743396):
and now the `by exact` trick works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743439):
so in fact I had to use both `by exact` and type ascription for the whole lambda. What a struggle! Thanks Mario as ever.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743454):
The URL for this topic is `.../topic/.CE.BB.20(.E2.9F.A8U.2CBU.2CHx.2Cs.E2.9F.A9`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743455):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 18 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743576):
The other irritation was that after almost every edit in VS Code, I had to drag the file up and down to see what the actual errors, if any, were. Somehow the localised "just try and process the bit the user is working on" thing worked very poorly in this instance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 18 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126743921):
You can click on the `Lean: (checking ...)` status bar item on the bottom to change what parts of the file are being checked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 19 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%CE%BB%20%28%E2%9F%A8U%2CBU%2CHx%2Cs%E2%9F%A9/near/126797317):
Oh this is news to me -- and helpful news too! Thanks Gabriel.

