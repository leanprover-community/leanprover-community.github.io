---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50870equivimagecompl.html
---

## Stream: [general](index.html)
### Topic: [equiv.image_compl](50870equivimagecompl.html)

---


{% raw %}
#### [ Patrick Massot (Apr 01 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501726):
Do we have `example (f : equiv a b) (s : set a) : f '' -s = - f '' s` hidden somewhere?

#### [ Patrick Massot (Apr 01 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501766):
(or not hidden would also be good)

#### [ Mario Carneiro (Apr 01 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501930):
Didn't this come up earlier?

#### [ Mario Carneiro (Apr 01 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501972):
You asked about this identity and we found it wasn't there, then you wrote a proof

#### [ Patrick Massot (Apr 01 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501974):
Really?

#### [ Patrick Massot (Apr 01 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501980):
I'm trying to get back to doing Lean, but I forgot where I stopped

#### [ Patrick Massot (Apr 01 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124501988):
But I don't see that one in my file

#### [ Mario Carneiro (Apr 01 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502043):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/image.20of.20complement/near/123655801

#### [ Patrick Massot (Apr 01 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502045):
Ok, I can see I already asked the question

#### [ Patrick Massot (Apr 01 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502051):
But I don't see my proof there

#### [ Patrick Massot (Apr 01 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502052):
So presumably I never proved it

#### [ Patrick Massot (Apr 01 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502055):
because real life caught me

#### [ Patrick Massot (Apr 01 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502328):
This is so painful

#### [ Patrick Massot (Apr 01 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124502482):
I give up for tonight. I'm stuck at proving that if b is not in the image of S then its preimage is not in S

#### [ Patrick Massot (Apr 02 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503021):
I had a new idea while feeding the cat, so now I'm stuck at `example (f : equiv α β) (b) : f (f.inv_fun b) = b := sorry`

#### [ Kenny Lau (Apr 02 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503061):
`f.right_inv b`?

#### [ Patrick Massot (Apr 02 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503062):
This so frustrating :ogre:

#### [ Patrick Massot (Apr 02 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503067):
that's funny (and frustrating). I tried a million variations on `rw f.right_inv b` in my main proof

#### [ Patrick Massot (Apr 02 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503068):
it always fail

#### [ Patrick Massot (Apr 02 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503069):
but when you extract the statement as a lemma it works

#### [ Kenny Lau (Apr 02 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503109):
maybe if you stop writing `f.to_fun` as `f` then `rw` will work

#### [ Patrick Massot (Apr 02 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503110):
I did not write this

#### [ Patrick Massot (Apr 02 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503158):
even inside conversion mode it fails

#### [ Patrick Massot (Apr 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503205):
I think this is the most ridiculous proof I ever wrote in Lean. The ratio "ugliness of proof"/"triviality of statement" is probably my worse so far

#### [ Patrick Massot (Apr 02 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503210):
```lean
lemma fuck (f : equiv α β) (b) : f (f.inv_fun b) = b := f.right_inv b

lemma equiv.image_compl  (f : equiv α β) (s : set α) :
  f '' -s = -(f '' s) :=
begin
  apply subset.antisymm,
  { intros b b_in_image_compl,
    rcases b_in_image_compl with ⟨a, a_compl_s, f_a_b⟩,
    rw (equiv.apply_eq_iff_eq_inverse_apply f a b).1 f_a_b at a_compl_s,
    exact (mt (@mem_image_iff_of_inverse α β f.to_fun f.inv_fun b s f.left_inv f.right_inv).1)      
a_compl_s },
  { intros,
    rw subset_def,
    intros b b_in_compl_image,
    apply (@mem_image_iff_of_inverse _ _ _ _ _ _ f.left_inv f.right_inv).2,
    have b_not_in_image := not_mem_of_mem_compl b_in_compl_image,
    rw set.mem_compl_eq,
    by_contra,
    have := mem_image_of_mem f a,
    rw fuck at this,
    finish }
end
```

#### [ Patrick Massot (Apr 02 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503212):
But at least Lean was defeated

#### [ Mario Carneiro (Apr 02 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124503802):
Actually, I recommend not using `f.right_inv` in favor of the coercions

#### [ Kevin Buzzard (Apr 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504087):
Another example of mathematicians getting very frustrated about how sometimes something which is "trivial in maths" can be hard in Lean.

#### [ Kevin Buzzard (Apr 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504088):
In the long term these really need to be fixed somehow

#### [ Kevin Buzzard (Apr 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504090):
if CS people want mathematicians to use the software.

#### [ Kevin Buzzard (Apr 02 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504131):
And funnily enough, just the same thing happened to me with rw

#### [ Simon Hudon (Apr 02 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504132):
I don't think it will ever happen that a mathematician using this or another theorem prover and will, 100% of the time, think "this is trivial" and have the prover confirm that (when the statement is true).

#### [ Kevin Buzzard (Apr 02 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504133):
no, with exact

#### [ Kevin Buzzard (Apr 02 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504140):
`exact (congr_fun H HUigx)` failed (type mismatch)

#### [ Kevin Buzzard (Apr 02 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504143):
but `have H2 := congr_fun H HUigx, exact H2` succeeded

#### [ Kevin Buzzard (Apr 02 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504524):
@**Simon Hudon**  I definitely think that this should happen in the future.

#### [ Kevin Buzzard (Apr 02 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504526):
I am suggesting we meet you somewhere in the middle.

#### [ Kevin Buzzard (Apr 02 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504533):
But if it doesn't happen then what hope is there for people to start adopting this computer viewpoint?

#### [ Kevin Buzzard (Apr 02 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504534):
I think it's a matter of education on our part and adding lemmas on your part

#### [ Kevin Buzzard (Apr 02 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504574):
We already saw this week how Chris couldn't prove something which was mathematically trivial, and then we found a framework for it and it became straightforward to prove

#### [ Simon Hudon (Apr 02 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504629):
In that case, I think we're on the same page. In general, we probably need to build packages to better support undergraduate level mathematics and at least the basics of graduate level math.

#### [ Simon Hudon (Apr 02 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124504631):
Improving the automation and the documentation for building your own tactics will probably help you bridge the gap too.

#### [ Mario Carneiro (Apr 02 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124507833):
@**Patrick Massot**  I wrote a proof of this that should appear in mathlib once it finishes checking. It's not nearly as complicated as you made it, and after appropriate sublemmas it's a one-liner:
```
theorem image_compl_subset {f : α → β} {s : set α} (H : injective f) :
  f '' -s ⊆ -(f '' s) :=
subset_compl_iff_disjoint.2 $ by simp [image_inter H]

theorem subset_image_compl {f : α → β} {s : set α} (H : surjective f) :
  -(f '' s) ⊆ f '' -s :=
compl_subset_iff_union.2 $
by rw ← image_union; simp [image_univ_of_surjective H]

theorem image_compl_eq {f : α → β} {s : set α} (H : bijective f) :
  f '' -s = -(f '' s) :=
subset.antisymm (image_compl_subset H.1) (subset_image_compl H.2)
```

#### [ Patrick Massot (Apr 02 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124518916):
Thank you very much @**Mario Carneiro**. I noticed that many support lemmas were missing. I'll use my crappy version in the mean time. But I'm still very much interested in any explanation why I could not avoid having this one lemma in order to rewrite.

#### [ Mario Carneiro (Apr 02 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124518965):
I am not quite sure what you were doing, but I think you wrote things in a non-idiomatic way (which is to say, not the way that mathlib is designed to help with), which made the proof more painful than it should have been

#### [ Mario Carneiro (Apr 02 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519016):
The idiomatic version of your `fuck` lemma is `f (f.symm x) = x` (and it's called `apply_inverse_apply`)

#### [ Kenny Lau (Apr 02 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519028):
` rw fuck at this `

#### [ Kenny Lau (Apr 02 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519031):
i.e. `fuck this`

#### [ Patrick Massot (Apr 02 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519141):
I'll tell you exactly what I was doing. First my brain absolutely refuses to think in this kind of situation, it's only filled with anger. Then I search for all lemmas in mathlib which seem vaguely related and try to apply them. But I got stuck with sorts of coercions issues, and stuff like rw refuses to rewrite etc, so I'm get even more upset. So of course the proof ends up not looking like what I would write on paper (of course in the beginning I would write nothing but then I'm able to write some proof on paper)

#### [ Patrick Massot (Apr 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519148):
But why does ` rw f.right_inv b ` fails?

#### [ Kenny Lau (Apr 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519156):
`rw` matches exactly the expression

#### [ Kenny Lau (Apr 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519157):
without any definitorial expansion

#### [ Patrick Massot (Apr 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519160):
Something else I notice with your solution is I should have gave up on proving this on `equiv` but go back to functions and `bijective f`

#### [ Patrick Massot (Apr 02 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519200):
At least this removes the coercion hell

#### [ Kenny Lau (Apr 02 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519201):
don't

#### [ Kenny Lau (Apr 02 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519203):
the `bijective f` has no data

#### [ Kenny Lau (Apr 02 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519205):
i.e. it is not constructive

#### [ Sebastian Ullrich (Apr 02 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519206):
> `rw` matches exactly the expression 

This is only correct for the expression _head_

#### [ Kenny Lau (Apr 02 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519212):
matches the expression pattern

#### [ Patrick Massot (Apr 02 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519265):
I still fail to see how this explains my situation

#### [ Patrick Massot (Apr 02 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519276):
I only copied the hypothesis into the statement of a lemma, and this rw accepts to do its job

#### [ Mario Carneiro (Apr 02 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519374):
kenny, `bijective f` is a precondition to the theorem. Constructively, `bijective f` is weaker than `equiv`, so the theorem is stronger

#### [ Kenny Lau (Apr 02 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519379):
well

#### [ Mario Carneiro (Apr 02 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519430):
... but the proof uses excluded middle, although the theorem itself has no data anyway so it doesn't matter computation-wise

#### [ Mario Carneiro (Apr 02 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519479):
It's not possible to prove the versions I stated without excluded middle

#### [ Patrick Massot (Apr 02 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519482):
Needless to say, I'm perfectly happy with excluded middle in this proof

#### [ Patrick Massot (Apr 02 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519488):
And it's even better if I can get the opportunity to deduce from this the statement for equiv which could be constructive

#### [ Kenny Lau (Apr 02 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv.image_compl/near/124519491):
excluded middle is an overgeneralization of the situation observed from finite situations


{% endraw %}
