---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82562oleanviewer.html
---

## Stream: [general](index.html)
### Topic: [olean viewer](82562oleanviewer.html)

---


{% raw %}
#### [ Mario Carneiro (Dec 19 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152149295):
Hi all, I'm ready to present a first cut at an [olean file parser](https://github.com/digama0/olean-rs), written in Lean and Rust. I'm hoping it can be useful for people that want to do analysis on lean files without having to grep the files or something. Plus this makes lots of other goodies accessible like notations and VM code for definitions.

#### [ Simon Hudon (Dec 19 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152150579):
That's a cool idea. Does the olean file format contain enough information for building useful linting tools? For example, could it be used to identify redundant imports?

#### [ Mario Carneiro (Dec 19 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152151691):
yes

#### [ Mario Carneiro (Dec 19 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152151708):
well, you would have to figure out what definitions come from where, so you would have to read all the olean files not just the target file

#### [ Kenny Lau (Dec 19 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152158823):
I thought olean is OS-dependent

#### [ Scott Morrison (Dec 19 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152160989):
@**Kenny Lau**, I don't think it is. I managed to move olean files between windows and os x.

#### [ Kenny Lau (Dec 19 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152161042):
then what’s stopping us from removing olean from gitignore?

#### [ Scott Morrison (Dec 19 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152161057):
because lean cares deeply about timestamps, and git won't get these right

#### [ Scott Morrison (Dec 19 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152161071):
(besides that most people have a deep revulsion to binary artifacts in version control :-)

#### [ Mario Carneiro (Dec 19 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152162356):
I can say for sure now that it's not OS dependent

#### [ Mario Carneiro (Dec 19 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152162367):
although it is pretty haphazard

#### [ Mario Carneiro (Dec 19 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152162379):
Because of the way intermediate exprs are saved and reused, you can't skip over any part of the file. If some macro is not understood, then everything stops

#### [ Joe Hendrix (Dec 19 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152165778):
Thanks for writing this.  I don't have an immediate use, but was always curious what was in those files.  I'm curious how much Lean 4 will help with runtime performance (assuming they keep .olean files).

#### [ Patrick Massot (Dec 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152172886):
```quote
Hi all, I'm ready to present a first cut at an [olean file parser](https://github.com/digama0/olean-rs), written in Lean and Rust. I'm hoping it can be useful for people that want to do analysis on lean files without having to grep the files or something. Plus this makes lots of other goodies accessible like notations and VM code for definitions.
```
 It looks like a very useful tool (once documented), but is it wise to do it for Lean 3? From Sebastian's talk that we watch yesterday, it seems this tool will have to be rewritten from the beginning for Lean 4. Maybe it would make more sense to focus on stuff that will be easier to port (like modules over multiple rings), unless this olean tool is something you could use for academic purposes (papers, thesis...).

#### [ Mario Carneiro (Dec 19 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152176116):
meh, I've been hearing that for a long time

#### [ Mario Carneiro (Dec 19 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152176179):
I expect it will require a lot of adjustment for lean 4; in fact it's best to think of this as documenting the lean 3 olean file format

#### [ Mario Carneiro (Dec 19 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152176183):
which isn't going to change since lean 3 is EOL

#### [ Mario Carneiro (Dec 19 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152176268):
lean 4 offers lots of things that may make this less necessary, but right now, in lean 3, it's difficult to get at some information without lots of hackery. Well here's a nice package of hackery so that you don't have to

#### [ Sebastian Ullrich (Dec 19 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152176286):
Yeah, you should be able to use Lean's actual implementation in Lean 4 for this

#### [ Mario Carneiro (Dec 19 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152176349):
it's a brave new world

#### [ Mario Carneiro (Dec 20 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152242814):
@**Sebastian Ullrich** This probably doesn't affect lean 4 because it's been changed too much, but I discovered a very peculiar condition by checking the olean parser against everything in mathlib. I've got it down to just one error, in `group_theory.coset`. The offending definition is:
```lean
@[elab_as_eliminator, elab_strategy, to_additive quotient_add_group.induction_on]
lemma induction_on {C : quotient s → Prop} (x : quotient s)
  (H : ∀ z, C (quotient_group.mk z)) : C x :=
quotient.induction_on' x H
attribute [elab_as_eliminator, elab_strategy] quotient_add_group.induction_on
```
The bizarre part here is the use of the `elab_strategy` attribute, which is supposed to be internal-use-only. This attribute has data, an enum which can have three possible values. Unlike lean's deserializer, I'm validating the byte before storing it in the enum, and I'm finding weird random numbers like `126` instead of `0,1,2` like expected.

Since `elab_strategy` is internal only, it shouldn't even be allowed in user files, but I guess it is in this case. I checked what the parser does when it reads an elab_strategy, and it calls `elaborator_strategy_attribute_data::parse(p)`, which isn't implemented, so it falls back on the default implementation which does nothing. So the `m_status` variable ends up filled with random junk, which then gets written into the olean file during serialization.

#### [ Sebastian Ullrich (Dec 20 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152243057):
Ah, interesting. Yeah, all attribute parsing will have to be reimplemented in Lean in Lean 4.

#### [ Mario Carneiro (Dec 21 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152321223):
argh... `#eval` and `example` leave no trace in the olean file. I was hoping to get a hold of some code to execute, but this makes things harder

#### [ Mario Carneiro (Dec 22 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152387511):
I upgraded the viewer so it can now follow lean cross references in a project. One application of this is viewing the dependencies of a file. Here is the list of dependencies of `analysis.real`, in the order lean sees them:
```
$ cargo run -- -p ../mathlib -d analysis.real
    Finished dev [unoptimized + debuginfo] target(s) in 0.09s
     Running `target\debug\olean-rs.exe -p ../mathlib -d analysis.real`
can't find init.data.lemmas
path = ["C:\\Users\\Mario\\lean\\lean\\library", "C:\\Users\\Mario\\lean\\lean\\lib\\lean\\library", "C:\\Users\\Mario\\lean\\mathlib\\./."]
can't find analysis.emetric_space
path = ["C:\\Users\\Mario\\lean\\lean\\library", "C:\\Users\\Mario\\lean\\lean\\lib\\lean\\library", "C:\\Users\\Mario\\lean\\mathlib\\./."]
init.core
init.logic
[snip]
init.data
init
data.prod
data.dlist
data.dlist.basic
category.basic
tactic.basic
tactic.cache
logic.basic
data.option.defs
logic.function
tactic.rcases
tactic.generalize_proofs
tactic.split_ifs
data.list.defs
data.sum
tactic.ext
tactic.tauto
tactic.replacer
tactic.simpa
meta.rb_map
category.functor
category.applicative
category.traversable.basic
tactic.squeeze
tactic.interactive
tactic.finish
data.subtype
data.set.basic
algebra.order
order.basic
order.lattice
data.bool
data.option.basic
tactic.pi_instances
order.bounded_lattice
order.complete_lattice
order.bounds
data.equiv.basic
algebra.group
algebra.ordered_group
algebra.ring
data.nat.cast
algebra.ordered_ring
data.nat.basic
data.buffer
data.buffer.parser
tactic.alias
tactic.mk_iff_of_inductive_prop
logic.relator
logic.relation
data.sigma.basic
data.sigma
data.fin
data.list.basic
data.list.perm
tactic.wlog
algebra.order_functions
tactic.monotonicity.basic
order.boolean_algebra
order.complete_boolean_algebra
order.galois_connection
data.set.lattice
category.traversable.instances
category.traversable.lemmas
category.traversable
category.traversable.derive
tactic.monotonicity.interactive
tactic
data.nat.sqrt
data.nat.pairing
data.equiv.nat
data.equiv.encodable
data.equiv.denumerable
logic.embedding
order.order_iso
data.vector
data.vector2
category.traversable.equiv
data.array.lemmas
data.list.sort
data.quot
data.char
data.string
algebra.field
algebra.char_zero
algebra.ordered_field
data.int.basic
algebra.group_power
data.multiset
data.finset
algebra.big_operators
data.fintype
data.equiv.list
data.set.finite
data.set.function
data.set.countable
order.conditionally_complete_lattice
data.real.cau_seq
data.real.cau_seq_completion
data.nat.gcd
data.pnat
data.int.sqrt
data.rat
algebra.archimedean
data.real.basic
data.real.nnreal
order.zorn
data.list
order.filter
order.liminf_limsup
algebra.module
algebra.pi_instances
data.set.intervals
data.equiv.algebra
analysis.topology.topological_space
analysis.topology.continuity
analysis.topology.uniform_space
data.finsupp
linear_algebra.basic
data.nat.prime
algebra.gcd_domain
data.int.gcd
ring_theory.associated
ring_theory.ideals
analysis.topology.topological_structures
analysis.metric_space
tactic.converter.old_conv
tactic.converter.interactive
tactic.norm_num
tactic.ring
tactic.linarith
analysis.real
```

#### [ Reid Barton (Dec 24 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20viewer/near/152483090):
How hard would it to be to produce a "class hierarchy", showing all the classes defined and which ones extend which others?


{% endraw %}
