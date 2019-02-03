---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02870makingisomorphismclassagroup.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [making isomorphism class a group](https://leanprover-community.github.io/archive/113488general/02870makingisomorphismclassagroup.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 31 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464358):
<p>Let's say I have a bunch of groups, and I use <code>quotient</code> to make isomorphism classes. Is there a constructive way to make the isomorphism classes inherit the structure of a group?</p>

#### [ Simon Hudon (Mar 31 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464513):
<p>I don't know but I'd like to find out. Let's say our groups are specified as:</p>
<div class="codehilite"><pre><span></span>variables {I : Type} (G : I -&gt; Type) [Π i, group (G i)]
</pre></div>

#### [ Simon Hudon (Mar 31 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464561):
<p>Are we also given the isomorphisms between those groups or to you want to construct them somehow?</p>

#### [ Kenny Lau (Mar 31 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464564):
<p>I have already constructed the quotient</p>

#### [ Simon Hudon (Mar 31 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464567):
<p>Can you show it?</p>

#### [ Kenny Lau (Mar 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464607):
<div class="codehilite"><pre><span></span>import data.set.basic group_theory.subgroup

universe u

namespace group

variables {α : Type u} [group α] (S : set α)

inductive generate : set α
| basic : ∀ x ∈ S, generate x
| one : generate 1
| mul_inv : ∀ x y, generate x → generate y → generate (x * y⁻¹)

namespace generate

def is_subgroup : is_subgroup (generate S) :=
{ one_mem := generate.one S,
  mul_inv_mem := λ x y hx hy, generate.mul_inv x hx y hy }

end generate

variables {β : Type u} [group β]
variables α β

class isomorphism extends α ≃ β :=
( is_group_hom : is_group_hom to_fun )

namespace isomorphism

variables {γ : Type u} [group γ]
variables {β γ}

@[refl] protected def refl : isomorphism α α :=
{ is_group_hom := λ x y, rfl
  .. equiv.refl α }

variables {α β γ}

@[symm] protected def symm (e : isomorphism α β) : isomorphism β α :=
{ is_group_hom := λ x y, calc
          e.inv_fun (x * y)
        = e.inv_fun (e.to_fun (e.inv_fun x) * e.to_fun (e.inv_fun y)) : by rw [e.right_inv, e.right_inv]
    ... = e.inv_fun (e.to_fun (e.inv_fun x * e.inv_fun y)) : by rw e.is_group_hom
    ... = e.inv_fun x * e.inv_fun y : by rw e.left_inv,
  .. equiv.symm e.to_equiv }

@[trans] protected def trans (e₁ : isomorphism α β) (e₂ : isomorphism β γ) : isomorphism α γ :=
{ is_group_hom := λ x y, by unfold equiv.trans; dsimp; rw [e₁.is_group_hom, e₂.is_group_hom],
  .. equiv.trans e₁.to_equiv e₂.to_equiv }

end isomorphism

end group

variable (S : Type u)

namespace free_group

structure to_be_named (G : Type u) [group G] :=
( gen : set G )
( gen_gen : group.generate gen = set.univ )
( func : gen → S )
( inj : function.injective func )

def to_be_named.quotient_rel : setoid Σ G [H : group G], @to_be_named S G H :=
⟨λ G H, nonempty $ @group.isomorphism G.1 G.2.1 H.1 H.2.1,
 λ G, ⟨@group.isomorphism.refl G.1 G.2.1⟩,
 λ G H ⟨e⟩, ⟨@group.isomorphism.symm G.1 G.2.1 H.1 H.2.1 e⟩,
 λ G H K ⟨e₁⟩ ⟨e₂⟩, ⟨@group.isomorphism.trans G.1 G.2.1 H.1 H.2.1 K.1 K.2.1 e₁ e₂⟩⟩

def something : Type (u+1) :=
quotient (to_be_named.quotient_rel S)

noncomputable def rep : something S → Σ G [H : group G], @to_be_named S G H :=
λ G, classical.some (@quotient.exists_rep _ (to_be_named.quotient_rel S) G)

#check λ G, classical.some (@quotient.exists_rep _ (to_be_named.quotient_rel S) G)

structure funny_structure : Type (u+1) :=
( G : something S )
( func : S → (rep S G).1 )
( im_gen : @group.generate _ (rep S G).2.1 (func &#39;&#39; set.univ) = set.univ )

def some_product : Type (u+1) :=
Π A : funny_structure S, (rep S A.G).1

noncomputable instance some_product.group : group (some_product S) :=
{ mul := λ f g x, @has_mul.mul _ (@semigroup.to_has_mul _ (@monoid.to_semigroup _ (@group.to_monoid _ (rep S (x.G)).2.1))) (f x) (g x),
  mul_assoc := λ f g h, funext $ λ x, by apply mul_assoc,
  one := λ x, @has_one.one _ (@monoid.to_has_one _ (@group.to_monoid _ (rep S (x.G)).2.1)),
  one_mul := λ f, funext $ λ x, by apply one_mul,
  mul_one := λ f, funext $ λ x, by apply mul_one,
  inv := λ f x, @has_inv.inv _ (@group.to_has_inv _ (rep S (x.G)).2.1) (f x),
  mul_left_inv := λ f, funext $ λ x, by apply mul_left_inv }

def aux_func : S → some_product S :=
λ x A, A.func x

end free_group

def free_group : Type (u+1) :=
group.generate (free_group.aux_func S &#39;&#39; set.univ)

instance free_group.group : group (free_group S) :=
is_subgroup.group group.generate.is_subgroup

def free_group.from_S : S → free_group S :=
λ x, ⟨free_group.aux_func S x, group.generate.basic _ ⟨x, trivial, rfl⟩⟩
</pre></div>

#### [ Kenny Lau (Mar 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464610):
<p>this is WIP so there are errors on the bottom, ignore those</p>

#### [ Kenny Lau (Mar 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464612):
<p>the quotient is appropriately named <code>something</code></p>

#### [ Simon Hudon (Mar 31 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464943):
<p>So you'd like to remove <code>noncomputable</code> from your <code>group</code> instance?</p>

#### [ Kenny Lau (Mar 31 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465033):
<p>right</p>

#### [ Kevin Buzzard (Mar 31 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465035):
<p>You had to prove that the composite of group homs is a group hom?? That's not there already?</p>

#### [ Kenny Lau (Mar 31 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465038):
<p>you'll be surprised</p>

#### [ Simon Hudon (Mar 31 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465249):
<p>Instead of <code>classical.some</code> and <code>quotient.exists_rep</code> in <code>rep</code>, can you try and use <code>quotient.lift</code>?</p>

#### [ Kenny Lau (Mar 31 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465250):
<p>to where?</p>

#### [ Simon Hudon (Mar 31 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465316):
<p>Not sure yet</p>

#### [ Simon Hudon (Mar 31 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465376):
<p>You're basically taking the value of a quotient type and sticking it in a sigma type. Because the sigma type is in <code>Type u</code> depending on which representative you extract, you will be able to tell members of the quotient sets apart.</p>

#### [ Simon Hudon (Mar 31 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465422):
<p>There are two possibilities I can see to stay constructive: instead of using a sigma type, use an existential quantification (not sure if that's workable with the group) or extract something other than the element of one of the group. A representative value that will be the same for every element of a given equivalence class</p>

#### [ Simon Hudon (Mar 31 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465475):
<p>Or maybe Mario's <code>trunc</code> contraption can make the sigma type into something that isn't data</p>

#### [ Kenny Lau (Mar 31 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124467440):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> do we even need the quotient?</p>

#### [ Simon Hudon (Mar 31 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124467543):
<p>I think you're right, you don't need it, at least not there</p>

#### [ Kenny Lau (Mar 31 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124467547):
<p>I think the reason the author introduced it is because of some foundational issues with ZFC</p>

#### [ Kenny Lau (Mar 31 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124467552):
<p>the paper is here for reference <a href="https://www3.nd.edu/~andyp/notes/CategoricalFree.pdf" target="_blank" title="https://www3.nd.edu/~andyp/notes/CategoricalFree.pdf">https://www3.nd.edu/~andyp/notes/CategoricalFree.pdf</a></p>

#### [ Kenny Lau (Apr 01 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469143):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> this can be viewed in two ways</p>

#### [ Kenny Lau (Apr 01 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469144):
<p>you will view it as "another reason why ZFC is stupid"</p>

#### [ Kenny Lau (Apr 01 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469192):
<p>I will view it as "another reason why Lean is stupid"</p>

#### [ Simon Hudon (Apr 01 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469193):
<p>I'm wondering if you even need the sigma type</p>

#### [ Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469228):
<p>I did it without any quotient</p>

#### [ Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469233):
<p>and without injectivity</p>

#### [ Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469234):
<p>the only reason why the paper introduced those is to justify it in ZFC</p>

#### [ Simon Hudon (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469235):
<p>And sigma type?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469236):
<p>well the sigma type has UMP as pi type right</p>

#### [ Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469237):
<p>that means, (Sigma x1 x2) -&gt; x3 is the same as x1 -&gt; x2 -&gt; x3</p>

#### [ Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469240):
<p>since they're there, the sigma doesn't need to be there anymore</p>

#### [ Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469243):
<p>am I speaking English</p>

#### [ Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469244):
<p>that thing there with that sigma is no longer used</p>

#### [ Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469245):
<p>I can't English</p>

#### [ Simon Hudon (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469246):
<p>What's UMP?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469247):
<p>universal mapping property</p>

#### [ Kenny Lau (Apr 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469273):
<p>or in CS language, "destructor" / "eliminator"</p>

#### [ Simon Hudon (Apr 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469290):
<p>Ah I see</p>

#### [ Simon Hudon (Apr 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469291):
<p>So why is it that not needing a quotient type makes Lean stupid?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469296):
<p>well if I need to explain I would have to bring another concept from math philosophy into here :P</p>

#### [ Kenny Lau (Apr 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469297):
<p>called predicativity</p>

#### [ Simon Hudon (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469336):
<p>Cool, I'm all ears</p>

#### [ Kenny Lau (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469337):
<p>inductive types are predicative</p>

#### [ Kenny Lau (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469338):
<p>they're philosophically well-founded</p>

#### [ Kenny Lau (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469339):
<p>bigger things are built on top of smaller things</p>

#### [ Kenny Lau (Apr 01 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469348):
<p>like "canonical", this word can't be properly defined, but a common criterion is whether the quantifiers quantify over the object to be constructed</p>

#### [ Kenny Lau (Apr 01 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469349):
<p>e.g. in ZFC, omega is constructed to be the intersection of every inductive set</p>

#### [ Kenny Lau (Apr 01 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469388):
<p>instead of building it from below, omega is constructed from above, which makes it philosophically not well-founded, and we call that impredicative</p>

#### [ Kenny Lau (Apr 01 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469389):
<p>in ZFC, omega := {x | x in A for every inductive A}</p>

#### [ Kenny Lau (Apr 01 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469390):
<p>but the "for every" quantifier there, quantifiers over omega itself</p>

#### [ Kenny Lau (Apr 01 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469399):
<p>now, the free group construction in the paper is equally impredicative</p>

#### [ Kenny Lau (Apr 01 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469400):
<p>in the sense that it takes the product of every possible group and then find the subgroup generated by the image of S</p>

#### [ Kenny Lau (Apr 01 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469440):
<p>but that product would have to already include that group to be constructed</p>

#### [ Kenny Lau (Apr 01 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469442):
<p>ZFC is an impredicative theory</p>

#### [ Kenny Lau (Apr 01 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469443):
<p>but that's unavoidable, because we want a strong foundation theory to do maths</p>

#### [ Kenny Lau (Apr 01 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469449):
<p>the common construction of free group is predicative</p>

#### [ Kenny Lau (Apr 01 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469450):
<p>because it builds on smaller things, i.e. individual words</p>

#### [ Kenny Lau (Apr 01 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469494):
<p>in ZFC, i.e. in the paper, the author constructed the free product by considering every group generated by a set that injects into S</p>

#### [ Kenny Lau (Apr 01 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469495):
<p>there's still a limitation on the size</p>

#### [ Kenny Lau (Apr 01 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469497):
<p>in Lean, i.e. in my file, I don't even need to care about the size, since Lean allows it</p>

#### [ Kenny Lau (Apr 01 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469498):
<p><a href="https://github.com/kckennylau/Lean/blob/master/free_group.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/free_group.lean">https://github.com/kckennylau/Lean/blob/master/free_group.lean</a></p>

#### [ Simon Hudon (Apr 01 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469550):
<p>Why is that a problem?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469551):
<p>it's not very well-founded is it</p>

#### [ Simon Hudon (Apr 01 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469644):
<p>Isn't the "big things built from smaller things" idea supported by the hierarchy of universes?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469683):
<p>well but one universe is already big enough</p>

#### [ Kenny Lau (Apr 01 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469696):
<p>philosophy aside, this construction is quite funny</p>

#### [ Kenny Lau (Apr 01 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469737):
<p>what do you think of my file? is it mathematically correct? should I PR it?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469743):
<p>I wonder why this construction isn't more well-known</p>

#### [ Simon Hudon (Apr 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469796):
<p>I don't think I can make a judgement about your construction. Mario and Kevin probably should be the ones to comment</p>

#### [ Kenny Lau (Apr 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469797):
<p>ok</p>

#### [ Simon Hudon (Apr 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469798):
<p>Or Johannes</p>

#### [ Simon Hudon (Apr 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469800):
<p>It looks like a cool construction :)</p>

#### [ Kenny Lau (Apr 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470041):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> <a href="https://github.com/kckennylau/Lean/commit/c6eac863b23d58d40deaab62489f6069f860407e#diff-fdee7d198ee1f7316cba5649313e084a" target="_blank" title="https://github.com/kckennylau/Lean/commit/c6eac863b23d58d40deaab62489f6069f860407e#diff-fdee7d198ee1f7316cba5649313e084a">https://github.com/kckennylau/Lean/commit/c6eac863b23d58d40deaab62489f6069f860407e#diff-fdee7d198ee1f7316cba5649313e084a</a></p>

#### [ Kenny Lau (Apr 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470042):
<p>rip universe limitation</p>

#### [ Kenny Lau (Apr 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470043):
<p>now it can be in any universe</p>

#### [ Simon Hudon (Apr 01 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470084):
<p>Yeah, that's universe polymorphism for you ;-)</p>

#### [ Kenny Lau (Apr 01 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470096):
<p>I wonder if <code>free_group.{u v} S</code> and <code>free_group.{u w} S</code> are different</p>

#### [ Kenny Lau (Apr 01 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470183):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> this is such a convenient construction</p>

#### [ Kenny Lau (Apr 01 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470185):
<p>basically constructing an object from its UMP</p>

#### [ Kenny Lau (Apr 01 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470187):
<p>I can probably construct the abelianization this way also</p>

#### [ Simon Hudon (Apr 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470229):
<p>That looks like the free objects I've worked with before. I remember being blown away by how cool they are :D</p>

#### [ Kenny Lau (Apr 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470232):
<p>you've seen this construction before?</p>

#### [ Simon Hudon (Apr 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470238):
<p>I've seen it in free monads mostly</p>

#### [ Kenny Lau (Apr 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470283):
<p>do you have any idea how I can fix the file to remove the need for manual typeclassing?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470285):
<p>group to monoid, monoid to semigroup, semigroup to has_mul...</p>

#### [ Simon Hudon (Apr 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470335):
<p>What happens when you replace it with an underscore?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470337):
<p>can't synthesize that thing</p>

#### [ Simon Hudon (Apr 01 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470383):
<p>Right but what instances are in your context?</p>

#### [ Kenny Lau (Apr 01 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470384):
<p>the thing is that the instances aren't declared to the left of the colon</p>

#### [ Kenny Lau (Apr 01 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470385):
<p>rather, they're introduced as variables</p>

#### [ Kenny Lau (Apr 01 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470392):
<p>because of how I defined ambient</p>

#### [ Simon Hudon (Apr 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470433):
<p>Right, so you can write:</p>
<div class="codehilite"><pre><span></span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">G</span> <span class="n">HG</span> <span class="n">f</span><span class="o">,</span> <span class="k">by</span> <span class="n">resetI</span> <span class="bp">;</span> <span class="n">exact</span> <span class="bp">@</span><span class="n">has_mul</span><span class="bp">.</span><span class="n">mul</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">...</span>
</pre></div>

#### [ Kenny Lau (Apr 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470434):
<p>I thought definitions shouldn't have any tactics</p>

#### [ Kenny Lau (Apr 01 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470435):
<p>because they're difficult to destruct</p>

#### [ Simon Hudon (Apr 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470476):
<p>This tactic won't create a complicated term. But it's also useful to just try it and see if it works. Otherwise, you can also use a separate <code>def</code></p>

#### [ Kenny Lau (Apr 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470479):
<p>hmm...</p>

#### [ Kenny Lau (Apr 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470578):
<p>free functors on steroids</p>

#### [ Kenny Lau (Apr 01 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470859):
<p><a href="https://github.com/kckennylau/Lean/blob/master/abelianization.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/abelianization.lean">https://github.com/kckennylau/Lean/blob/master/abelianization.lean</a></p>

#### [ Kenny Lau (Apr 01 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470860):
<p>comes with commutators for free!</p>

#### [ Mario Carneiro (Apr 01 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124472206):
<p>I'm familiar with this construction, which is sometimes used as an application of category theory: use the adjoint functor theorem to construct free groups. When you unwind the category theory it's exactly this construction: taking a suitable quotient over all groups</p>

#### [ Mario Carneiro (Apr 01 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124472250):
<p>The universe issues that arise in ZFC also arise in lean, because they are valid concerns and can cause inconsistency if they are not attended to. In lean this expresses as a bumping up of the universe level of the constructed free group</p>

#### [ Mario Carneiro (Apr 01 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124472296):
<p>To prove that the universe doesn't need to increase, you need a size limitation which amounts to doing the standard (internal) free group construction anyway. This is why I'm not a big fan of this approach - it's just shuffling proof obligations around</p>

#### [ Mario Carneiro (Apr 01 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124472356):
<p>When you write the UMP predicatively, it ends up weaker than people want (and use), because the free group you've constructed lives in <code>max u (v+1)</code> but is only universal wrt groups in <code>Type v</code>, which is strictly lower. In particular, the free group UMP doesn't apply to itself, which we want to be true for it to really be a free group. Otherwise it's only an approximation - if you try proving equivalence to the standard internal definition you will get stuck</p>

#### [ Mario Carneiro (Apr 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124473230):
<p>Re: making the isomorphism class a group, it is impossible to do this computably for some reasonable definitions of the problem. Suppose we want to take a quotient of all groups (in some universe) with respect to isomorphism. First of all, note that a quotient is with respect to a relation, meaning a Prop, meaning data about the isomorphism itself will be lost. We can define such a quotient, let's call it <code>Q</code>. Now each element <code>q : Q</code> somehow "represents" a group unique up to isomorphism, but I claim that there is no computable function <code>rep : Q -&gt; Group</code> such that <code>G ~= rep (mk G)</code> for all groups <code>G</code>.</p>
<p>Now one way to define such a function is by applying choice as you've done to just pick one of the groups in the class, but maybe you thought there might be a way of using all the groups at once to form a new group which is isomorphic to each of the groups in the equivalence class. Supposing this is possible, and supposing also that you computably have the isomorphism <code>f G : G ~= rep (mk G)</code>, i.e. that's not just an existence statement, then you have <code>choice</code> for group isomorphisms, since if <code>nonempty (G ~= H)</code> then <code>mk G = mk H</code> and hence you can construct <code>G ~= rep (mk G) = rep (mk H) ~= H</code>.</p>
<p>To turn this into at least unique choice, we can construct a group <code>H</code> which is isomorphic to <code>G = C_2</code> iff <code>α</code> is nonempty. For example, <code>H := Σ g : G, g ≠ 0 → trunc α</code> will do the trick. Then given an isomorphism <code>f : G ~= H</code>, we have <code>f 1 : psum (trunc α) (1 = 0)</code> from which we obtain an element of <code>trunc α</code>. This is not as strong as full choice, but it is known unprovable in lean.</p>

#### [ Kenny Lau (Apr 01 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476618):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> so what should I do? I'm confused, you keep saying it's unprovable but you're giving an algorithm</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476658):
<p>I'm showing that if you could construct it you could prove something that is known unprovable</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476659):
<p>thus it's not computable</p>

#### [ Kenny Lau (Apr 01 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476664):
<p>ok, then what should I do?</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476675):
<p>Live with the fact that going from an isomorphism class to a specific group is nonconstructive?</p>

#### [ Kenny Lau (Apr 01 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476715):
<p>oh well, but I didn't use isomorphism class in the end</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476721):
<p>maybe you can phrase it independently of the choice then?</p>

#### [ Kenny Lau (Apr 01 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476722):
<p>phrase what?</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476723):
<p>your theorem, whatever it is</p>

#### [ Kenny Lau (Apr 01 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476724):
<p>that free group exists?</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476762):
<p>I'm not sure what you are trying to do now...</p>

#### [ Kenny Lau (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476765):
<p>I realized that using isomorphism class is because of some stupid limitation of ZFC</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476766):
<p>it's a limitation of lean too, I say</p>

#### [ Kenny Lau (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476767):
<p>I just stopped using it</p>

#### [ Kenny Lau (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476768):
<p>and then I constructed the free group and proved its property</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476769):
<p>did you though?</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476770):
<p>watch your universe levels</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476777):
<p>I'm claiming you didn't construct the real free group</p>

#### [ Kenny Lau (Apr 01 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476778):
<p>I'm starting to suspect so</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476818):
<p>Have you ever heard of system F encodings or church encodings?</p>

#### [ Kenny Lau (Apr 01 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476824):
<p>I've heard of church encodings, if you're referring to the numbers</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476865):
<p>I'm talking about the types. Something like this:</p>
<div class="codehilite"><pre><span></span>def unit := ∀ X : Type, X → X
def nat := ∀ X : Type, X → (X → X) → X
def prod (α β) := ∀ X : Type, (α → β → X) → X
</pre></div>

#### [ Kenny Lau (Apr 01 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476870):
<p>oh</p>

#### [ Kenny Lau (Apr 01 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476871):
<p>I get it, go on</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476912):
<p>This sort of thing works great in system F, where there is only one impredicative data type <code>Type</code>, because then <code>unit : Type</code> etc and this has the expected universal property</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476915):
<p>But in lean, it's not as strong as you want because the elimination property only goes to <code>Type 0</code> in this case while the constructed type lives in <code>Type 1</code></p>

#### [ Mario Carneiro (Apr 01 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476923):
<p>Note that real eliminators such as are generated by <code>inductive</code> eliminate to <code>Sort u</code> where <code>u</code> is independent of the universes involved in the definition of the inductive type itself</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476924):
<p>This allows creation of type families over the inductive type in very large universes</p>

#### [ Kenny Lau (Apr 01 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476963):
<p>fair enough</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476968):
<p>There is a curious property about these weak eliminators, though: <em>If</em> there exists a real type with the right eliminator, then you can prove that the weak type and the strong type are isomorphic, so the weak type inherits the strong eliminator</p>

#### [ Kenny Lau (Apr 01 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476969):
<p>hence what you mean by moving proof obligations around</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476970):
<p>That means that your free group construction is correct if there is a free group</p>

#### [ Kenny Lau (Apr 01 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476971):
<p>and here am I thinking that it's a brand new construction that nobody knows :P</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477010):
<p>The size limitation thing is really important but manifests in weird ways in ZFC and lean</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477057):
<p>I think it's also related to the "B" in BNF, bounded natural functors used in isabelle for generating arbitrary (co)inductive types</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477060):
<p>which literally have an axiom on limitation of size, to prevent universe issues</p>

#### [ Kenny Lau (Apr 01 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477066):
<p><span class="emoji emoji-1f171" title="b button">:b_button:</span>ounded <span class="emoji emoji-1f171" title="b button">:b_button:</span>atural <span class="emoji emoji-1f171" title="b button">:b_button:</span>unctors</p>

#### [ Mario Carneiro (Apr 01 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477111):
<p>now I need to make a "bounded natural blunders" joke</p>

#### [ Kenny Lau (Apr 01 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477264):
<p>I'm thoroughly confused now</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493878):
<p>Well that's really annoying. I thought that type theory was getting around these silly ZFC universe problems</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493882):
<p>but it's just moving them to Lean universe problems</p>

#### [ Kenny Lau (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493885):
<p>same thought here</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493886):
<p>Why do you care about isomorphic groups?</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493887):
<p>Why not just work with all groups?</p>

#### [ Kenny Lau (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493888):
<p>right, I worked with all groups at the end</p>

#### [ Kenny Lau (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493889):
<p>I was following the paper, which used isomorphic groups</p>

#### [ Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493891):
<p>my conjecture is that the author used isomorphism classes to make it justified in ZFC</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493928):
<p>Similarly you don't need to work with "generated by a subset of S"</p>

#### [ Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493931):
<p>which i take to be a really shitty thing to do</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493932):
<p>That just seemed to be a red herring</p>

#### [ Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493933):
<p>right</p>

#### [ Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493934):
<p>I didn't use that in my construction</p>

#### [ Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493935):
<p>but then it still depends on the universe</p>

#### [ Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493936):
<p>since you're quantifying over every group anyway</p>

#### [ Kenny Lau (Apr 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493984):
<p>that's the thing with impredicative constructions</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493986):
<p>you can send the other elements of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> to the identity</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493987):
<p>Oh I broke zulip</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493988):
<p>I can't edit $S$ into <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span></p>

#### [ Kenny Lau (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494040):
<p>you see, in ZFC this is the way you would do it:</p>

#### [ Kenny Lau (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494042):
<p>firstly you consider only the isomorphism classes</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494043):
<p>Bingo, I had to reload the page.</p>

#### [ Kenny Lau (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494044):
<p>and you only consider the groups generated by a subset of S</p>

#### [ Kenny Lau (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494045):
<p>because in some sense you can build it from S</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494082):
<p>I don't see where the subset comes in</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494085):
<p>but I do see where the isomorphism classes come in</p>

#### [ Kenny Lau (Apr 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494087):
<p>well</p>

#### [ Kenny Lau (Apr 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494088):
<p>they are both limitations on the size of the set</p>

#### [ Kenny Lau (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494094):
<p>after these two restrictions, you can justify the existence of the set by building it from a large enough set that you still build from S</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494096):
<p>I don't see where they're needed in the ZFC proof.</p>

#### [ Kenny Lau (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494098):
<p>if you don't limit the size of the generator, your set is still too big</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494099):
<p>I want my generator to have size S</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494100):
<p>exactly</p>

#### [ Kenny Lau (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494140):
<p>ah</p>

#### [ Kenny Lau (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494141):
<p>hmm</p>

#### [ Kenny Lau (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494142):
<p>that's what you meant</p>

#### [ Kenny Lau (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494143):
<p>I suppose it's ok then</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494144):
<p>So in ZFC I start with S and then I choose some cardinal kappa such that in V_kappa there is a copy of every group generated by S</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494151):
<p>Lean is better because in Lean I don't think you even need that S generates G</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494154):
<p>But as Mario points out, your answer is in the wrong universe.</p>

#### [ Kenny Lau (Apr 01 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494204):
<p>I think you do need that S generates G if you don't want to run into universe problems</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494300):
<p>In ZFC you do, but I don't see where you need it in Lean.</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494347):
<p>You just put a group structure on the product of G over all pairs (G,f:S -&gt; G)</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494353):
<p>and give this a map from S</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494354):
<p>and then take the intersection over all the subgroups containing the image of S</p>

#### [ Kevin Buzzard (Apr 01 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494362):
<p>This should definitely be in <a class="stream" data-stream-id="116395" href="/#narrow/stream/116395-maths">#maths</a></p>


{% endraw %}
