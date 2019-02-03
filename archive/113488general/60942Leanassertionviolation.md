---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60942Leanassertionviolation.html
---

## Stream: [general](index.html)
### Topic: [Lean assertion violation](60942Leanassertionviolation.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 05 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293256):
<div class="codehilite"><pre><span></span>universes u v

theorem set.subset.trans {α : Type*} {a b c : set α} (ab : a ⊆ b) (bc : b ⊆ c) : a ⊆ c :=
assume x h, bc (ab h)

def set.preimage {α : Type u} {β : Type v} (f : α → β) (s : set β) : set α := {x | f x ∈ s}
infix ` ⁻¹&#39; `:80 := set.preimage

structure presheaf_of_types (α : Type*) :=
(F : Π U : set α,  Type*)
(res : ∀ (U V : set α) (H : V ⊆ U),
  (F U) → (F V))
(Hcomp : ∀ (U V W : set α)
  (HUV : V ⊆ U) (HVW : W ⊆ V),
  (res U W (set.subset.trans HVW HUV)) = (res V W HVW) ∘ (res U V HUV) )

definition presheaf_of_types_pushforward
  {α : Type*}
  {β : Type*}
  (f : α → β)
  (FPT : presheaf_of_types α)
  : presheaf_of_types β :=
  { F := λ V : set β, FPT.F (set.preimage f V),
    res := λ V₁ V₂ H,
    FPT.res (set.preimage f V₁) (set.preimage f V₂)(λ x Hx,H Hx),
    Hcomp := λ Uβ Vβ Wβ HUV HVW,rfl -- assertion violation
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293261):
<div class="codehilite"><pre><span></span>LEAN ASSERTION VIOLATION
File: /home/travis/build/leanprover/lean/src/frontends/lean/elaborator.cpp
Line: 3167
Task: /home/buzzard/Encfs/Computer_languages/Lean/lean/bug.lean: presheaf_of_types_pushforward
m_ctx.match(e, *val2)
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293307):
<p>Here's a (mathlib-free) assertion violation. Is this a known issue? If not, is my MWE minimal enough? If so, shall I file a bug report? I'd be happy to hear advice before working on this any more</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293311):
<p>I'm looking into it</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293312):
<p><code>Lean (version 3.3.1, commit d6d44a19947e, Release)</code> Ubuntu 16.04</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293315):
<p>Can reproduce</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293322):
<p>Thanks.</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293326):
<p>I get the feeling structure notation is too sophisticated for our (the implementers') own good <span class="emoji emoji-1f605" title="sweat smile">:sweat_smile:</span></p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293365):
<p>ha ha</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293368):
<p>so it's my fault? :-)</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293370):
<p>I wasn't expecting rfl to work, it's just sometimes worth a try</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293376):
<p>It's obviously our fault for enabling you to do weird things :)</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293379):
<p>I would be interested to know what the first thing you do in this situation is. If it's to fire up some C++ debugger then fair enough, you've lost me already, but if it's to just set some options and watch more carefully then I would be interested to follow along for a while</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293419):
<p>What do I do that is weird?</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293548):
<p>actually I wonder whether I am now grown up enough to fire up a C++ debugger myself</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293628):
<p>It's a unification error, so I'm now looking at the <code>is_def_eq_detail</code> trace. The terms are still quite big - if you find a way to minimize them, that would be great.</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123293638):
<p>OK I will try and minimise more</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294055):
<div class="codehilite"><pre><span></span>definition presheaf_of_types_pushforward
  {β : Type*}
  : presheaf_of_types β :=
  { F := sorry,
    res := sorry,
    Hcomp := λ Uβ Vβ Wβ HUV HVW,rfl -- assertion violation
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294056):
<p>No idea if that helps</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294100):
<p>I just replaced some stuff with sorry</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294184):
<div class="codehilite"><pre><span></span>definition presheaf_of_types_pushforward
  {β : Type*}
  : presheaf_of_types β :=
  { Hcomp := λ Uβ Vβ Wβ HUV HVW,rfl -- assertion violation
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294251):
<p>oh I have made it smaller</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294257):
<div class="codehilite"><pre><span></span>universes u v

structure presheaf_of_types (α : Type*) :=
(F : Π U : set α,  Type*)
(res : ∀ (U V : set α) ,
  (F U) → (F V))
(Hcomp : ∀ (U V W : set α),
  (res U W  = (res V W) ∘ (res U V) ))

set_option trace.type_context.is_def_eq_detail true

definition presheaf_of_types_pushforward
  {β : Type*}
  : presheaf_of_types β :=
  { Hcomp := λ Uβ Vβ Wβ,rfl -- assertion violation
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123294683):
<div class="codehilite"><pre><span></span>structure presheaf_of_types (α : Type*) :=
(F : Π U : set α,  Type*)
(res : ∀ (U V : set α) ,
  (F U) → (F V))
(Hidem : ∀ U : set α, res U U = (res U U) ∘ (res U U))

set_option trace.type_context.is_def_eq_detail true

definition presheaf_of_types_pushforward
  {β : Type*}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295041):
<div class="codehilite"><pre><span></span>structure presheaf_of_types (α : Type) :=
(res : ∀ (U V : set α) ,
  {x : α // U x} → {x : α // V x})
(Hidem : ∀ U : set α, res U U = (res U U) ∘ (res U U))

definition presheaf_of_types_pushforward
  {β : Type}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295092):
<p>I'm going to stop there because all I am doing now is taking things like my general F from set alpha to Type and replacing it with an arbitrary explicit F (in this case the map sending U to the subtype corresponding to U)</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295103):
<p>oh here's an even better one, I can just use some random map unit to unit</p>

#### [ Kevin Buzzard (Mar 05 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295104):
<div class="codehilite"><pre><span></span>structure presheaf_of_types (α : Type) :=
(res : ∀ (U V : set α) ,
  unit → unit)
(Hidem : ∀ U : set α, res U U = (res U U) ∘ (res U U))

definition presheaf_of_types_pushforward
  {β : Type}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295160):
<p>Still simpler:</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295163):
<div class="codehilite"><pre><span></span>structure presheaf_of_types (α : Type) :=
(res : ∀ (U : set α) ,
  unit → unit)
(Hidem : ∀ U : set α, res U = (res U) ∘ (res U))

definition presheaf_of_types_pushforward
  {β : Type}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295210):
<div class="codehilite"><pre><span></span>structure presheaf_of_types (α : Type) :=
(res : unit → unit)
(Hidem : ∀ U : set α, res = (res) ∘ (res))

definition presheaf_of_types_pushforward
  {β : Type}
  : presheaf_of_types β :=
  { Hidem := λ U, rfl,
}
</pre></div>

#### [ Sebastian Ullrich (Mar 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295231):
<p>Thanks! That should do hopefully.</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295270):
<div class="codehilite"><pre><span></span>structure presheaf_of_types :=
(res : unit → unit)
(Hidem : ∀ U : unit, res = res ∘ res)

set_option trace.type_context.is_def_eq_detail true

definition presheaf_of_types_pushforward
  : presheaf_of_types :=
  { Hidem := λ U, rfl,
}
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295286):
<p>Thanks for asking for more minimisation -- in some sense that was quite instructive. Initially I just removed everything not directly related to the violation in the form I had it, but after you asked more I realised there was nothing stopping me trying to find simpler violations</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295366):
<p>Adding the field <code>res := id</code> makes the problem go away</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295482):
<p>Hey, is it doing a prolog-like search?</p>

#### [ Patrick Massot (Mar 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295495):
<p>Poor Kevin was deprived of a prolog-like search yesterday</p>

#### [ Patrick Massot (Mar 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295496):
<p>Please be nice this time</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295504):
<p>I should never have equated this phrase with "random thing I don't understand"</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295549):
<p>but looking at the debugging output it looks like it might be backtracking...</p>

#### [ Patrick Massot (Mar 05 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295576):
<p>I'm picturing you asking to Scholze: "are you doing a a prolog-like search" at the end of a really tough talk.</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295702):
<p>Maybe I don't even know what backtracking means. I guess I look at these debugging outputs and think "oh look it's trying lots of things in what looks like a systematic manner"</p>

#### [ Patrick Massot (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295706):
<p>It's not enough</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295709):
<p>but I probably need to look more closely to distinguish the difference between "if this fails, discard it and try something else"</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295710):
<p>and "let's actually backtrack here"</p>

#### [ Patrick Massot (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295711):
<p>You want to start following a path and then come back to an earlier branch point</p>

#### [ Kevin Buzzard (Mar 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123295714):
<p>yes this is just dawning on me now</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298542):
<p><span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span> Congrats, I think you found a bug where definitional equality is not idempotent</p>

#### [ Kevin Buzzard (Mar 05 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298548):
<p>Is that a good thing?</p>

#### [ Kevin Buzzard (Mar 05 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298549):
<p>Do I get an achievement?</p>

#### [ Patrick Massot (Mar 05 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298550):
<p>I'm jalous</p>

#### [ Patrick Massot (Mar 05 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298585):
<p>My conv bug seems much less cool</p>

#### [ Gabriel Ebner (Mar 05 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298715):
<p><span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> "Idempotent"??  Do you mean <code>is_def_eq(t, t)</code> returns false?</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298717):
<p>On the first run it returns true for two terms, then false on any subsequent runs</p>

#### [ Kevin Buzzard (Mar 05 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298811):
<p>ooh can I prove false??</p>

#### [ Kevin Buzzard (Mar 05 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298814):
<p>I would definitely get an achievement for that</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298816):
<p>Nah, it's just the elaborator</p>

#### [ Kevin Buzzard (Mar 05 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298818):
<p>aah well</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298831):
<p>Apparently <code>elim_delayed_abstractions</code> accidentally supports backtracking assignments to a metavar... not the correct place for a Prolog-like search</p>

#### [ Kevin Buzzard (Mar 05 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298834):
<p>you lost me at the prolog-like search bit</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298883):
<p>That was mostly a joke :)</p>

#### [ Gabriel Ebner (Mar 05 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298896):
<p>Wow, this is unexpected.</p>

#### [ Kevin Buzzard (Mar 05 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298946):
<p>Kenny posted this about a week ago</p>

#### [ Kevin Buzzard (Mar 05 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298947):
<p><code>instance error (α : Type) : group α := { mul_assoc := λ x y z, rfl }
</code></p>

#### [ Kevin Buzzard (Mar 05 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298948):
<p>without any further comment</p>

#### [ Kevin Buzzard (Mar 05 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123298954):
<p>and it might be the same thing</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123299000):
<p>Yep, same assertion</p>

#### [ Patrick Massot (Mar 05 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20assertion%20violation/near/123299285):
<p><a href="/user_uploads/3121/JbuLIJprxGe-IqMGOyrrJlyK/users.png" target="_blank" title="users.png">users.png</a><br>
One little bug and everybody flies out, except devs. So sad...</p>
<div class="message_inline_image"><a href="/user_uploads/3121/JbuLIJprxGe-IqMGOyrrJlyK/users.png" target="_blank" title="users.png"><img src="/user_uploads/3121/JbuLIJprxGe-IqMGOyrrJlyK/users.png"></a></div>


{% endraw %}
