---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51105toomanyaxiomsincommringclass.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [too many axioms in comm_ring class](https://leanprover-community.github.io/archive/113488general/51105toomanyaxiomsincommringclass.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 07 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123389686):
<p>I have to put a ring structure on a slightly complicated type (a subtype, consisting of functions with some properties). Every verification is going to be quite messy -- even defining zero and one will take some effort. So I really want to minimise the amount of stuff I want to prove. I am sure that Lean is asking me to do too much by default -- for example it wants a proof of add_comm, add_zero and zero_add, and the same story with multiplication and one. Of course I can deduce zero_add from add_zero once I've proved add_comm but in some sense I'm wondering why I am even being asked to do this, because this is true for every commutative ring. Is there a way of "fixing" this?</p>

#### [ Mario Carneiro (Mar 07 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123389751):
<p>The usual solution is to write a variant on <code>mk</code> that asserts only the properties you want to prove and proves the rest. This can be done generally for <code>comm_ring</code>, to provide several interfaces depending on which axioms you want.</p>

#### [ Mario Carneiro (Mar 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123389795):
<p>Warning: you can get into trouble if you do this for data fields, like we've discussed about deriving a topology from a metric</p>

#### [ Kevin Buzzard (Mar 07 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123389808):
<p>Aah I see. So there's an argument for <code>comm_ring.mk'</code> which takes what I need and builds the rest. I remember seeing this in the construction of the rationals -- I think there are about 4 constructors in the end.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123389869):
<p>Re: data fields. Once you have one and neg you can define zero ;-) so perhaps I should be careful here.</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123389984):
<p>If you want to derive zero or something else, one option is to have it be an optional argument, so that the user can still set up their desired choice of defeq equivalence class here</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123389986):
<p>that's what many structures do by default</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123389991):
<p>Oh, something annoying has happened.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390000):
<div class="codehilite"><pre><span></span>    Fring := λ U OU,{
      add := _,
      zero := _,
      add_comm := _,
      add_assoc := _,
      one := _,
      zero_add := _,
      neg := _,
      add_left_neg := _,
      mul := _,
      mul_assoc := _,
      add_zero := _,
      one_mul := _,
      mul_one := _,
      left_distrib := _,
      right_distrib := _,
      mul_comm := _
    },
</pre></div>

#### [ Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390004):
<p>There's my set-up (I'm not going to do mk' right now, I'm going to prove it's a ring and see what happens)</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390010):
<p>and I was expecting red underlines on all the _s</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390012):
<p>but I only have one under add_assoc</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390015):
<p>I mean on the _ of add_assoc</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390058):
<p>Am I expected to remember that addition takes two inputs? I thought Lean was going to tell me that.</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390070):
<p>Hm, I can probably explain why add_assoc specifically, but it's not all that relevant. They are all actually required, but lean won't be able to even contemplate the later stuff until you finish the early stuff</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390082):
<p>add_assoc is telling me I have a type mismatch!</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390085):
<p>with what?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390126):
<p>Wooah -- maybe type class inference is randomly doing stuff? How do I check that?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390130):
<div class="codehilite"><pre><span></span>type mismatch at field &#39;add_assoc&#39;
  ?m_1
has type
  ∀
  (a b c :
    (λ (U : set (X R))
     (HU :
       (λ (X_1 : set (X R)),
          set.mem (lattice.complete_boolean_algebra.neg X_1) {A : set (X R) | ∃ (E : set R), Spec.V E = A})
         U),
       {f // ∀ (u : X R),
          U u →
          (∃ (g : R),
             set.mem u (Spec.D&#39; g) ∧
               set.subset (Spec.D&#39; g) U ∧
                 ∃ (r : localization.away g),
                   ∀ (Q : X R) (HQQ : set.mem Q U) (H2 : set.mem Q (Spec.D&#39; g)), f Q HQQ = canonical_map g Q H2 r)})
      U
      OU), ?m_1 (?m_1 a b) c = ?m_1 a (?m_1 b c)
but is expected to have type
  ∀
  (a b c :
    (λ (U : set (X R)) (HU : (λ (X_1 : set (X R)), -X_1 ∈ {A : set (X R) | ∃ (E : set R), Spec.V E = A}) U),
       {f // ∀ (u : X R),
          U u →
          (∃ (g : R),
             u ∈ Spec.D&#39; g ∧
               Spec.D&#39; g ⊆ U ∧
                 ∃ (r : localization.away g),
                   ∀ (Q : X R) (HQQ : Q ∈ U) (H2 : Q ∈ Spec.D&#39; g), f Q HQQ = canonical_map g Q H2 r)})
      U
      OU), a + b + c = a + (b + c)
</pre></div>

#### [ Kevin Buzzard (Mar 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390131):
<p>So far I wrote nothing.</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390144):
<p>what's all that about localizations? What's the theorem?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390145):
<p>What does that add even mean on the bottom line?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390151):
<p>The ?m_1 presumably means "you didn't tell me what add meant yet"</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390153):
<p>it's <code>@has_add.add &lt;your type&gt; ?m_1 a b</code></p>

#### [ Mario Carneiro (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390154):
<p>which prints as <code>a + b</code></p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390158):
<p>Oh I see it's just some pretty printer cuteness</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390208):
<p>I told you my objects were complicated ;-)</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390210):
<p>this is probably some artifact of structure <code>notation</code> command</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390213):
<p>are you familiar with making defs for things?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390216):
<p>I have heard of <code>definition</code></p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390223):
<p>if that's what you mean</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390231):
<p>I'm trying to understand why your goal is a mile long before you start the proof</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390234):
<p>In brief, my objects are functions which are well-behaved locally</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390236):
<p>you left out the statement of the theorem above</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390241):
<p>I am defining a ring structure</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390276):
<p>on a complex type</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390279):
<p>on what?</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390288):
<p>give the type a name</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390289):
<p>It's a subtype of a pi type</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390297):
<p>Here's a toy example</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390299):
<p>do not prove an instance for a messy type</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390301):
<p>I want to consider functions on a topological space which are "locally well-behaved"</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390303):
<p>it will make typeclass inference cry</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390305):
<p>I am not using type class inference at all</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390311):
<p>I gave up on it</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390313):
<p>I'm not talking about the mathematical specifics of the type</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390314):
<p>I don't need it</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390320):
<p>I don't understand what you are asking but I am certainly interested in what you are thinking</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390321):
<p>what's the theorem? like paste the statement here</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390323):
<p>There is no theorem</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390324):
<p>I don't know why you keep asking this</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390326):
<p>I am trying to put a ring structure on a type</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390368):
<p>I am making a 1000 line definition</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390369):
<p>yes that</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390372):
<p>instance, def, theorem, it's all the same</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390373):
<p>:-)</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390376):
<p>My type is a subtype of a pi type</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390390):
<p>and the details involve a lot of commutative algebra</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390398):
<p>what exactly do you want to know about it?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390403):
<p>and I have a convoluted way of adding and multiplying two such things</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390451):
<p>Okay, toy example:</p>
<div class="codehilite"><pre><span></span>instance : ring {x // ∀ y, x is more awesome than y} :=
sorry
</pre></div>


<p>bad</p>
<div class="codehilite"><pre><span></span>def awesome_sauce := {x // ∀ y, x is more awesome than y}
instance : ring awesome_sauce :=
sorry
</pre></div>


<p>good</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390471):
<p>whatever is the difference?</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390472):
<p>I am getting the sense you typed some big term after <code>ring</code></p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390473):
<div class="codehilite"><pre><span></span>definition structure_presheaf_of_rings_on_affine_scheme (R : Type*) [comm_ring R]
: presheaf_of_rings (X R)
:= { PT := structure_presheaf_of_types_on_affine_scheme R,
    Fring := λ U OU,{
      add := _,
      zero := _,
      add_comm := _,
      add_assoc := _,
      one := _,
      zero_add := _,
      neg := _,
      add_left_neg := _,
      mul := _,
      mul_assoc := _,
      add_zero := _,
      one_mul := _,
      mul_one := _,
      left_distrib := _,
      right_distrib := _,
      mul_comm := _
    },
    res_is_ring_morphism := sorry,
}
</pre></div>

#### [ Kevin Buzzard (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390509):
<p>I typed that</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390515):
<p>I am right in the middle of a complex mathematical object</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390520):
<p>and your simple example is too simple for me to currently make sense of</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390526):
<p>In that case, you should probably define that <code>Fring</code> field in its own lemma</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390531):
<p>Why does this make any difference?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390538):
<p>But of course I will do this now you tell me to</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390549):
<p>My sense is that typeclass inference generally does poorly with inferring typeclasses on complicated things</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390553):
<p>it needs to know when not to unfold</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390597):
<p>and definitions are the best way to indicate this</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390599):
<p>I am not ever using typeclass inference</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390602):
<p>it causes me too much trouble</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390604):
<p>you are, <em>inside the structure instance itself</em></p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390607):
<p>?</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390616):
<p>because it's actually proven in stages, a semigroup plus some more stuff to make it a monoid, group, ring, then comm_ring</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390629):
<p>this I knew</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390639):
<p>But is this really typeclass inference?</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390641):
<p>and after the initial stages, it uses the semigroup instance to find the <code>+</code> which is used in later proofs</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390643):
<p>It's not just "comm_ring extends ring so let's just copy the fields"?</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390686):
<p>Actually, that depends on whether it is using the old or new structure command</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390688):
<p>:-)</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390690):
<p>I am using the default structure command</p>

#### [ Sebastian Ullrich (Mar 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390692):
<p>It looks like we don't do error recovery after that field type mismatch error. I could change that, but a smaller example would be nice :) .</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390699):
<p>I feel like the definition of a ring is extremely small compared to the monster I am creating.</p>

#### [ Sebastian Ullrich (Mar 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390703):
<p>Eh, I guess it shouldn't be hard to construct one by myself</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390747):
<p>This is not a big deal at this point</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390748):
<p>Even if it doesn't make a difference, I would recommend making this a definition and proving in stages simply for proof engineering reasons</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390750):
<p>I see.</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390752):
<p>you should try to keep your goal size down to something human readable</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390767):
<p>I thought I'd fix things up with <code>add_assoc := sorry</code> for the time being</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390770):
<p>I got</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390781):
<div class="codehilite"><pre><span></span>type mismatch at field &#39;add_assoc&#39;
  sorry
has type
  ∀
  (a b c :
    (λ (U : set (X R))
     (HU :
       (λ (X_1 : set (X R)),
          set.mem (lattice.complete_boolean_algebra.neg X_1) {A : set (X R) | ∃ (E : set R), Spec.V E = A})
         U),
...
</pre></div>

#### [ Kevin Buzzard (Mar 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390811):
<p>Wasn't expecting that!</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390821):
<p>did you sorry the <code>add</code> field first?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390824):
<p>that fixes it</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390832):
<p>Ok so here's a question</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390838):
<p>First I have a red line under add_assoc.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390840):
<p>I can't fix it with a sorry</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390841):
<p>I sorry the add and this fixes both.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390842):
<p>Q) Where does the new red line appear?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390844):
<p>And how do I fix it?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390846):
<p>A) zero_add</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390847):
<p>I can fix it by sorrying the zero and zero_add.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390849):
<p>Now I have a type mismatch at add_left_neg</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390890):
<p>I love the randomness of it all</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390891):
<p>it's whack a mole, I know</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390898):
<p>Here's how you can derive the answer: First, find the first nested structure that is not complete</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390904):
<p>so in the original case, that's <code>semigroup</code></p>

#### [ Mario Carneiro (Mar 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390909):
<p>next, find all fields that have nothing dependent on them</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390913):
<p>ha ha, I sorried all the data fields and now I have <code>don't know how to synthesize placeholder</code> on every other field apart from add_left_neg. ???</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390916):
<p>so in this case <code>add_assoc</code> because <code>add</code> has <code>add_assoc</code> depending on it</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390967):
<p>when you sorry it out, it is considered complete and you get the next error, because of the error recovery issue Sebastian mentioned</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390980):
<p>I have a grant deadline for Friday, I'd better go to work. Thanks for the comments. I will move the ring structure to a definition. Do I need to annotate the definition with reducible or irreducible or whatever?</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390981):
<p>But if you sorry <code>add_assoc</code> without <code>add</code>, then I think the sorry macro gets into trouble because the type it needs to be has a metavariable in it</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123390986):
<p>no, the regular reducibility is fine</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391025):
<p>I think I deserve another achievement for making sorry fail to find its own type</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391044):
<p>Thanks to Kenny's hard work on localisation lemmas we nearly have schemes, although not in a way Assia would approve of, as when I have defined this ring structure we will have a definition but no way of constructing examples :-)</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391045):
<p>I will then need to prove one more theorem and then we can have examples</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391085):
<p>what's the most trivial scheme?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391087):
<p>Mario -- you always said that the test case for you was whether one could prove any lemmas about the object</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391088):
<p>is a ring a scheme over itself?</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391091):
<p>but I will work on Assia's comments first -- she wants to see examples first.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391094):
<p>The spectrum of a ring is an affine scheme</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391096):
<p>and an affine scheme is a scheme</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391099):
<p>voila</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391100):
<p>do that</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391108):
<p>but I will be able to define a scheme correctly in Lean</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391110):
<p>without ever proving that an affine scheme is a scheme</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391111):
<p>because a scheme is an object with property X that looks locally like an affine scheme</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391114):
<p>and I did not prove that affine schemes have property X yet</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391155):
<p>but one can formulate "I look locally like an affine scheme" without mentioning X</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391159):
<p>so first I want the definition of a scheme</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391160):
<p>and then I need to prove one more theorem</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391165):
<p>I think you are not ready for assia's criterion yet</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391170):
<p>Thanks for the definition comments.</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391171):
<p>she talked about examples in situations where you already have the fundamental theorem of mystuffoids</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391176):
<p>you are still in the definition crafting stage</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391177):
<p>This is a fundamental issue</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391214):
<p>which goes beyond Lean</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391220):
<p>It's something I have found when lecturing</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391222):
<p>You introduce a new concept in a lecture</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391224):
<p>typically a new structure</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391226):
<p>and then you want to do two things simultaneously:</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391227):
<p>(1) give basic examples</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391232):
<p>(2) prove basic lemmas (e.g. subsets, quotients,  products, whatever)</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391237):
<p>(consequences of axioms)</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391241):
<p>and whenever I do this in a lecture I never know whether to do (1) or (2) first</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391242):
<p>because they are independent and both very important</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391245):
<p>they are both important, of course. They are even closely related since (1) is basically stuff that implies X and (2) is stuff implied by X</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391246):
<p>They are both "the first thing you should do after you defined the concept"</p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391288):
<p>Still, I should concentrate on defining the concept first. Cheers!</p>

#### [ Mario Carneiro (Mar 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391290):
<p><span class="emoji emoji-1f44b" title="wave">:wave:</span></p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391305):
<p>Current state of things at <a href="https://github.com/kbuzzard/lean-stacks-project/blob/master/src/scheme.lean" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/master/src/scheme.lean">https://github.com/kbuzzard/lean-stacks-project/blob/master/src/scheme.lean</a></p>

#### [ Kevin Buzzard (Mar 07 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123391348):
<p>probably lines 268 - 305 should be moved into a definition, if my understanding of what you're saying is correct. OK I really am gone now.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392619):
<p>dammit I refactored into a definition and then started with <code>  add := λ f₁ f₂, ⟨_,_⟩,</code> and got an assertion violation. I am going to roll back a bit I think. Does anyone have any advice as to which version to pick?</p>

#### [ Mario Carneiro (Mar 07 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392672):
<p>when I get an assertion violation in the middle of writing something, I try to finish writing it and see if it's okay once it is once again well-formed</p>

#### [ Johannes Hölzl (Mar 07 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392781):
<p><span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span>  I think a simpler solution for you would be to first start defining the operations, i.e. <code>instance : has_add (Fring)</code>, ... do this for all the data. Then you see at least that this works. Then you proof stat it is a monoid, a group, a semiring etc. this allows you to have a clear overview what's happening.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392795):
<p>In maths we care about refactoring to a far lesser degree.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392803):
<p>I've seen lecturers write a proof and then in the middle stop and say "oh, hmm, Ok we will need this:" and then write "sublemma : ..." and just insert something in the middle, and then press on.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392808):
<p>Either that or just splurge through everything.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392856):
<p>And then we get "and as we see from the proof of Theorem B, X -&gt; Y" later on</p>

#### [ Kevin Buzzard (Mar 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392859):
<p>and everyone is fine with this</p>

#### [ Kevin Buzzard (Mar 07 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123392877):
<p>PS I am not using instances at all. I wanted to completely avoid type class inference and also any coercions as much as possible, so I had a tight control over what was going on.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393347):
<p>Oh this is a really nice way of doing it. Thanks. My definitions are getting smaller and smaller, apparently this is what I should be aiming at.</p>

#### [ Mario Carneiro (Mar 07 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393512):
<blockquote>
<p>I've seen lecturers write a proof and then in the middle stop and say "oh, hmm, Ok we will need this:" and then write "sublemma : ..." and just insert something in the middle, and then press on.</p>
</blockquote>
<p>You should view this as analogous to writing a proof, then in the middle editing the statement, and returning to the proof. The fact that lectures are limited to a linear format is simply because of practical concerns of blackboard presentation, but we often think about things out of order like this. A lean script should not reflect these amendations themselves, so that at the end everything fits together.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393622):
<p>I added some of these comments to <a href="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/structures.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/structures.md">https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/structures.md</a></p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393634):
<p>Are you interested in a PR Mario? A lot of those WIPs are (a) works in progress and (b) already helpful for me in their current form.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393638):
<p>I am just letting them grow organically at this point rather than trying to tidy them.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393643):
<p>The advantage of a PR is that they become more visible to people. The disadvantage is that they become your problem.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393645):
<p>I am happy either way; a lot depends on how seriously you take that docs directory.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393687):
<p>My workflow now is much better now we're at zulip. If I have time I update my local docs. If I don't then I just star the messages and come back later.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123393693):
<p>I'm talking about when people give me good advice which I would like to keep track of.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394051):
<p>o_O</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394054):
<p>how clean is this:</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394057):
<div class="codehilite"><pre><span></span>definition structure_presheaf_value_is_comm_ring {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U)
: comm_ring (structure_presheaf_value U HU)
:= {
  add := (structure_presheaf_value_has_add U HU).add,
  mul := (structure_presheaf_value_has_mul U HU).mul,
  zero := (structure_presheaf_value_has_zero U HU).zero,
  one := (structure_presheaf_value_has_one U HU).one,
  add_comm := by simp,
  zero_add := by simp,
  add_zero := by simp,
  neg := (structure_presheaf_value_has_neg U HU).neg,
  add_left_neg := by simp,
  add_assoc := by simp,
  mul_assoc := by simp [mul_assoc],
  one_mul := by simp,
  mul_one := by simp,
  left_distrib := by simp [left_distrib],
  right_distrib := by simp [right_distrib],
  mul_comm := by simp [mul_comm]
}
</pre></div>

#### [ Kevin Buzzard (Mar 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394059):
<p>:-)</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394101):
<p>My original proofs were worse</p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394112):
<p>but because I wrote <a href="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md">https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/simp.md</a></p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394122):
<p>I remembered the "how to use simp better" thing -- i.e "if your proof looks like <code>funext (λ f,subtype.eq (funext (λ P,by simp)))</code></p>

#### [ Kevin Buzzard (Mar 07 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394161):
<p>then you might want to consider being more optimistic with when exactly you use simp"</p>

#### [ Mario Carneiro (Mar 07 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394226):
<p>Why is there the messy thing with <code>(structure_presheaf_value_has_add U HU).add</code>? As it is currently, there should be no difficulty making this thing an instance, and then it will pick those fields up automatically</p>

#### [ Mario Carneiro (Mar 07 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394345):
<p>even if you can't make them instances, you can use <code>..structure_presheaf_value_has_add U HU</code> etc to add the operations</p>

#### [ Mario Carneiro (Mar 07 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123394770):
<p>Re: PRs, I'm okay with docs of any kind. My recommendation is to try to write them with an authoritative locution style; I will let you know if you say false things. If you don't know something, leave it out, say you don't know in the doc, or ask about it here and then put in whatever you find out.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123395558):
<p>Messy thing: I am not concerned with such issues at the minute. I am completely avoiding instances simply because writing all this code is taking my Lean understanding to a new level and I realised that I did not trust myself to do all the clever things instances could do for me, and I would occasionally have problems with instances, so I decided to never use them just to see what like would be like without them. The advantage of doing it my way is that I can take one look and understand what is happening. I am still a learner.</p>

#### [ Kevin Buzzard (Mar 07 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123395617):
<p>I am always muddled about this .. thing. I forget the syntax, I never know whether it has to go at the beginning or the end or whether it doesn't matter, just stupid things which people your age only need to be told once but people my age need to have a reference for and basic examples of. I don't have the time right now to fart around with .. trying to make it work and as you can see from <a href="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/structures.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/structures.md">https://github.com/kbuzzard/mathlib/blob/master/docs/WIPs/structures.md</a> I have also not found the time to figure it out once and for all and then document it. I am afraid I need docs to work efficiently, and if stuff isn't documented properly then I shy away from it.</p>

#### [ Sebastian Ullrich (Mar 07 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123396002):
<p>Instead of declaring <code>mk'</code>s, the algebraic hierarchy could be amended with superclass defaults like</p>
<div class="codehilite"><pre><span></span>class add_comm_monoid (α : Type u) extends add_monoid α, add_comm_semigroup α :=
(add_zero := by simp [add_comm, zero_add])
</pre></div>

#### [ Mario Carneiro (Mar 07 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123396500):
<p>that doesn't actually work right now tho</p>

#### [ Sebastian Ullrich (Mar 07 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123396588):
<p>It doesn't?</p>

#### [ Mario Carneiro (Mar 07 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123397155):
<p>nvm, I misread what you are doing there</p>

#### [ Kevin Buzzard (Mar 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123402113):
<blockquote>
<p>Why is there the messy thing with <code>(structure_presheaf_value_has_add U HU).add</code>? As it is currently, there should be no difficulty making this thing an instance, and then it will pick those fields up automatically</p>
</blockquote>
<p>My co-author got their hands on it and now it looks like this:</p>

#### [ Kevin Buzzard (Mar 07 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123402117):
<div class="codehilite"><pre><span></span>definition structure_presheaf_value_is_comm_ring {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U)
: comm_ring (structure_presheaf_value U HU) :=
by refine {
  add := (+),
  zero := 0,
  neg := ((structure_presheaf_value_has_neg U HU).neg),
  mul := (*),
  one := 1,
  .. };
{simp [mul_assoc, left_distrib, right_distrib]} &lt;|&gt; simp [mul_comm]
</pre></div>

#### [ Scott Morrison (Mar 07 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123404579):
<p>I really like <span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span>’s suggestion for putting in superclass defaults in the algebraic hierarchy, at least where they are “uncontroversial”. I didn’t even know you can do that.</p>

#### [ Sebastian Ullrich (Mar 07 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/too%20many%20axioms%20in%20comm_ring%20class/near/123404588):
<p>It's not a very old feature :)</p>


{% endraw %}
