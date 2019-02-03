---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72225EckmannHilton.html
---

## Stream: [general](index.html)
### Topic: [Eckmann–Hilton](72225EckmannHilton.html)

---


{% raw %}
#### [ Johan Commelin (Sep 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496192):
<p>Today I thought it was a good idea to stretch the type class system a bit. In fact, I ended up not using it at all <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span><br>
<a href="https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf" target="_blank" title="https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf">https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf</a><br>
Statement: Two unital binary operations that distribute over each other are in fact one and the same. Also, they are commutative and associative, so in fact a monoid structure.<br>
This is used to prove that homotopy groups are abelian.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496199):
<p>Any comments are welcome.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496250):
<p>In particular, feel free to shoehorn this into the type class system.<br>
Golfing is appreciated.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496443):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Did you already have this somewhere in your repo?</p>

#### [ Reid Barton (Sep 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496454):
<p>Nope I hadn't gotten that far. Cool!</p>

#### [ Reid Barton (Sep 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496542):
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="kn">notation</span> <span class="n">a</span> <span class="bp">`</span> <span class="bp">`</span><span class="n">m</span><span class="bp">`</span> <span class="bp">`</span> <span class="n">b</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">has_mul</span><span class="bp">.</span><span class="n">mul</span> <span class="n">X</span> <span class="n">m</span> <span class="n">a</span> <span class="n">b</span>
</pre></div>


<p>Does this really work? Also, it doesn't work for me. :)</p>

#### [ Reid Barton (Sep 07 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496632):
<p>Oh nice. Copy and paste from github (even the raw page) doesn't preserve the source text correctly.</p>

#### [ Reid Barton (Sep 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496705):
<p>Maybe you could choose something less sneaky like <code>local notation a `&lt;`m`&gt;` b := @has_mul.mul X m a b</code></p>

#### [ Johan Commelin (Sep 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496835):
<p>Hmm, maybe I should.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496843):
<p>But those are non-breaking spaces.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496999):
<p>Hmmm... that's really nasty of GitHub.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497000):
<p>They should know better.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497006):
<p>I'll use fishhooks, like you suggested.</p>

#### [ Reid Barton (Sep 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497009):
<p>Somehow when I pasted the source into emacs, they turned into regular spaces.<br>
Not sure whether github or firefox or emacs is to blame</p>

#### [ Johan Commelin (Sep 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497108):
<p>Ok, fair enough.</p>

#### [ Johan Commelin (Sep 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497111):
<p>Anyway, it is fixed now.</p>

#### [ Reid Barton (Sep 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497452):
<p>Haha, Lean prints both mul operations as <code>*</code>. It knows!!</p>

#### [ Johan Commelin (Sep 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497578):
<p>Yes! I thought that was hilarious <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Johan Commelin (Sep 07 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133501859):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> What would be the proper place for this in mathlib? Somewhere in <code>group_theory</code>?</p>

#### [ Johan Commelin (Sep 10 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133684290):
<p>PR'd this: <a href="https://github.com/leanprover/mathlib/pull/335" target="_blank" title="https://github.com/leanprover/mathlib/pull/335">https://github.com/leanprover/mathlib/pull/335</a></p>


{% endraw %}
