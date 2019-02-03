---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40971MathlibQuiz.html
---

## Stream: [general](index.html)
### Topic: [Mathlib Quiz](40971MathlibQuiz.html)

---


{% raw %}
#### [ Patrick Massot (Aug 25 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132761188):
<p>On the occasion of the first Orsay Lean User Meeting, I've created a small Mathlib quizz at <a href="https://www.quiz-maker.com/QTNPVLT" target="_blank" title="https://www.quiz-maker.com/QTNPVLT">https://www.quiz-maker.com/QTNPVLT</a> I'd be interested to see how well people here can estimate answers to these questions. It starts easy, but quickly becomes hard if you are not very familiar with either mathlib or Lean introspection capabilities.</p>

#### [ Chris Hughes (Aug 25 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132761514):
<p>Does "What are the most used definitions and lemma/theorems (cite at most 5)?" include definitions used mainly by tactics?</p>

#### [ Patrick Massot (Aug 25 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132761557):
<p>yes</p>

#### [ Mario Carneiro (Aug 25 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132763365):
<p>I got 1/7</p>

#### [ Sean Leather (Aug 26 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132777337):
<p>2/7 but that's completely due to luck. I really had no idea on any of them. Are these important or useful factoids to know?</p>

#### [ Scott Morrison (Aug 26 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132777629):
<p>I think Patrick is just happy he learned how to use the reflection tools. :-)</p>

#### [ Patrick Massot (Aug 26 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132780581):
<p>I think Scott is jealous because he understood I have bigger graphs :-p</p>

#### [ Patrick Massot (Aug 26 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132780682):
<p><a href="/user_uploads/3121/-lOedO1v1Xr5tpN0cQ5KaoGj/Untitled.pdf" target="_blank" title="Untitled.pdf">Untitled.pdf</a></p>

#### [ Patrick Massot (Aug 26 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132780940):
<p>More seriously, I think the evolution of these numbers will be interesting to watch</p>

#### [ Patrick Massot (Aug 26 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132780947):
<p>And exploring some parts of the graph could be useful</p>

#### [ Patrick Massot (Aug 26 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132780949):
<p>or at least fun</p>

#### [ Patrick Massot (Aug 26 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132781331):
<p>A more artistic view of the largest connected component<br>
<a href="/user_uploads/3121/t9_V-aZukc7OUu-wOkBpp5s_/big_comp.png" target="_blank" title="big_comp.png">big_comp.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/t9_V-aZukc7OUu-wOkBpp5s_/big_comp.png" target="_blank" title="big_comp.png"><img src="/user_uploads/3121/t9_V-aZukc7OUu-wOkBpp5s_/big_comp.png"></a></div>

#### [ Chris Hughes (Aug 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132781660):
<p>It didn't show me the answers after I finished.</p>

#### [ Patrick Massot (Aug 26 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132782240):
<p>I have no idea what happens when you take the quiz, I didn't try. And I picked the first website that google suggested</p>

#### [ Patrick Massot (Aug 26 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132782242):
<p>The answers will be officially announced during the opening ceremony of the Orsay meeting, and then written here.</p>

#### [ Floris van Doorn (Aug 26 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132782455):
<p>3/7 without having used mathlib... Some questions were ambiguous though: with "using a definition" do you mean it appears in the .lean file or that it appears in the resulting proof term?</p>

#### [ Patrick Massot (Aug 26 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132782514):
<p>appearing in the type or proof term</p>

#### [ Patrick Massot (Aug 26 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132782521):
<p>I don't know how to ask Lean what appears in the file</p>

#### [ Patrick Massot (Aug 26 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132782838):
<p>People who want to play with the big connected component can download<br>
<a href="/user_uploads/3121/CzGvwzGef4Ogf92yLZmu8sZO/mathlib_known_big_comp.gephi" target="_blank" title="mathlib_known_big_comp.gephi">mathlib_known_big_comp.gephi</a></p>

#### [ Patrick Massot (Aug 26 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132782841):
<p>play with <a href="https://gephi.org/users/download/" target="_blank" title="https://gephi.org/users/download/">https://gephi.org/users/download/</a></p>

#### [ Patrick Massot (Aug 26 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132782842):
<p>A fun game is to guess what the neighboring big blobs are about</p>

#### [ Patrick Massot (Aug 27 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132877956):
<p>You can see what people estimated in the quiz at <a href="https://www.quiz-maker.com/Account-Quiz-Results?qp=255630x6e929BBA-4#tab-1" target="_blank" title="https://www.quiz-maker.com/Account-Quiz-Results?qp=255630x6e929BBA-4#tab-1">https://www.quiz-maker.com/Account-Quiz-Results?qp=255630x6e929BBA-4#tab-1</a></p>

#### [ Patrick Massot (Aug 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132878452):
<p>There are 217 files in mathlib, this was mostly underestimated. They contain about 1000 definitions and 4000 theorems.</p>

#### [ Patrick Massot (Aug 27 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132878602):
<p>The longest path is 28 steps long, and lives in computability theory: <code>[nat, nat.sqrt, nat.lt_succ_sqrt, nat.le_sqrt, nat.sqrt_lt, nat.sqrt_add_eq,    
nat.unpair_mkpair, nat.primrec.prec1, nat.primrec.cases1, nat.primrec.pred,     
primrec.dom_denumerable, primrec.nat_iff, primrec.unpair, primrec₂.unpaired,    
primrec₂.unpaired', primrec₂.nat_iff', primrec.option_cases, primrec.           
option_bind, primrec.option_map, primrec.sum_cases, primrec.list_nth, primrec.  
nat_strong_rec, nat.partrec.code.evaln_prim, nat.partrec.code.eval_part, nat.   
partrec.code.fixed_point, nat.partrec.code.fixed_point₂, computable_pred.rice,  
computable_pred.halting_problem]</code></p>

#### [ Patrick Massot (Aug 27 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132878687):
<p>The most used mathlib theorem is <code>primrec.comp</code> which is used 62 times. It states that a composition of primitive recursive functions is a rimitive recursive function.</p>

#### [ Patrick Massot (Aug 27 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132878700):
<p>This is also from the computability stuff (come on Mario, what about doing maths in mathlib?)</p>

#### [ Patrick Massot (Aug 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132878809):
<p>The statement and proof term using the biggest number of other constant is <a href="https://github.com/leanprover/mathlib/blob/b3fc801318bdb28121f3e3974b287cdcf4d63032/analysis/limits.lean#L16" target="_blank" title="https://github.com/leanprover/mathlib/blob/b3fc801318bdb28121f3e3974b287cdcf4d63032/analysis/limits.lean#L16">has_sum_of_absolute_convergence</a></p>

#### [ Patrick Massot (Aug 27 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132878996):
<p>It involves: <code>[real.topological_ring, real.ring, topological_ring.to_topological_add_monoid, has_sum, real.metric_space, metric_space.to_uniform_space', uniform_space.to_topological_space, nhds, nat.ordered_semiring, ordered_semiring.to_ordered_cancel_comm_monoid, ordered_cancel_comm_monoid.to_ordered_comm_monoid, ordered_comm_monoid.to_partial_order, partial_order.to_preorder, filter.at_top, real.decidable_linear_ordered_comm_group, abs, finset.range, real.add_comm_monoid, finset.sum, filter.tendsto, Exists, real, nat, finset.exists_nat_subset_range, finset.subset.trans, finset.zero_le_sum, finset.range_subset, iff.mp, abs_sub, congr_fun, abs_of_nonneg, abs_nonneg, finset.subset.refl, finset.sdiff_subset_sdiff, finset.sum_le_sum_of_subset_of_nonneg, finset.abs_sum_le_sum_abs, add_self_div_two, add_div, add_lt_add, abs_neg, abs_add_le_abs_add_abs, le_trans, trivial, eq_self_iff_true, neg_add_cancel_left, add_left_comm, neg_add_rev, sub_eq_add_neg, add_comm, finset.sum_sdiff, eq.symm, trans_rel_right, lt_of_le_of_lt, trans_rel_left, eq.subst, filter.mem_at_top, filter.image_mem_map, two_pos, div_pos_of_pos_of_pos, mem_uniformity_dist, cauchy_nhds, cauchy_downwards, true_and, set.mem_set_of_eq, filter.mem_at_top_sets, filter.mem_map, exists_prop, funext, eq.refl, imp_congr_eq, forall_congr_eq, not_false_iff, iff_false_intro, filter.map_eq_bot_iff, ne.def, congr_arg, congr, propext, eq.trans, le_refl, set.prod_mk_mem_set_prod_eq, Exists.intro, Exists.dcases_on, filter.at_top_ne_bot, filter.map_ne_bot, and.intro, cauchy_iff, iff.mpr, real.complete_space, complete_space.complete, finset.has_mem, real.ordered_comm_monoid, discrete_linear_ordered_field.to_linear_ordered_field, linear_ordered_field.to_linear_ordered_ring, linear_ordered_ring.to_ordered_ring, ordered_ring.to_ordered_semiring, ordered_comm_monoid.to_add_comm_monoid, real.discrete_linear_ordered_field, discrete_linear_ordered_field.to_decidable_linear_ordered_comm_ring, decidable_linear_ordered_comm_ring.to_decidable_linear_ordered_comm_group, preorder.to_has_lt, division_ring.to_domain, domain.to_ring, real.ordered_cancel_comm_monoid, decidable_linear_ordered_comm_group.to_add_comm_group, add_comm_group.to_add_group, has_add, has_sub, add_group.to_add_monoid, decidable_linear_ordered_comm_group, real.add_comm_semigroup, add_comm_semigroup.to_add_semigroup, eq.rec, id, add_comm_monoid.to_add_monoid, add_monoid.to_add_semigroup, add_semigroup.to_has_add, real.has_le, add_group.to_has_neg, has_neg.neg, real.preorder, has_add.add, real.add_group, add_group_has_sub, has_sub.sub, prod.cases_on, set.image, finset.has_sdiff, has_sdiff.sdiff, finset.has_subset, division_ring.to_zero_ne_one_class, real.linear_ordered_field, linear_ordered_field.to_field, field.to_division_ring, division_ring.to_ring, nat.inhabited, lattice.semilattice_sup, inhabited, False, not, True, eq.mp, eq.mpr, and.dcases_on, prod.snd, prod.fst, set_of, lattice.nat.semilattice_sup_bot, lattice.semilattice_sup_bot.to_semilattice_sup, lattice.semilattice_sup.to_partial_order, preorder.to_has_le, ge, domain.to_zero_ne_one_class, zero_ne_one_class.to_has_one, has_one.one, real.ring, ring.to_distrib, distrib.to_has_add, bit0, real.division_ring, division_ring_has_div, has_div.div, nat.has_le, has_le.le, id_rhs, prod.mk, dist, has_lt.lt, real.domain, domain.to_no_zero_divisors, no_zero_divisors.to_has_zero, has_zero.zero, real.has_lt, gt, eq, classical.prop_decidable, finset.lattice.lattice, lattice.lattice.to_semilattice_sup, finset.inhabited, set.prod, set.has_subset, has_subset.subset, uniformity, filter.sets, set.has_mem, has_mem.mem, prod, set, filter.lattice.complete_lattice, lattice.complete_lattice.to_bounded_lattice, lattice.bounded_lattice.to_order_bot, lattice.order_bot.to_has_bot, lattice.has_bot.bot, filter, ne, and, finset.partial_order, filter.map, cauchy, finset, real.metric_space, metric_space.to_uniform_space', uniform_space.to_topological_space, nhds, nat.ordered_semiring, ordered_semiring.to_ordered_cancel_comm_monoid, ordered_cancel_comm_monoid.to_ordered_comm_monoid, ordered_comm_monoid.to_partial_order, partial_order.to_preorder, filter.at_top, real.decidable_linear_ordered_comm_group, abs, finset.range, real.add_comm_monoid, finset.sum, filter.tendsto, Exists, real, nat]</code></p>

#### [ Patrick Massot (Aug 27 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132879010):
<p>That 219 names</p>

#### [ Patrick Massot (Aug 27 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132879023):
<p>One could also play to compute cumulative sizes of proofs in various ways</p>

#### [ Sean Leather (Aug 28 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mathlib%20Quiz/near/132898487):
<p>I'm surprised more people didn't guess “blah.” <span class="emoji emoji-1f644" title="rolling eyes">:rolling_eyes:</span></p>


{% endraw %}
