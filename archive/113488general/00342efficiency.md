---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00342efficiency.html
---

## Stream: [general](index.html)
### Topic: [efficiency](00342efficiency.html)

---


{% raw %}
#### [ Scott Morrison (Nov 13 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570420):
<p>Hi <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, <span class="user-mention" data-user-id="110111">@Keeley Hoek</span>  and I are having some "fun" profiling <code>rewrite_search</code>, and discovered that all the arithmetic is slow.</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570429):
<p>don't generate proofs during the search</p>

#### [ Scott Morrison (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570430):
<p>We're going to experiment to see if typeclass resolution is partly to blame, but I'm also wondering if you have a sense of whether it's better to use <code>nat</code> or <code>int</code>.</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570435):
<p>how are you proving things?</p>

#### [ Scott Morrison (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570438):
<p>Maybe Keeley can tell me that <code>nat</code> won't actually do for our purposes.</p>

#### [ Scott Morrison (Nov 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570441):
<p>Nope, everything is in meta land.</p>

#### [ Scott Morrison (Nov 13 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570457):
<p>oh --- sorry, it's not that part that is slow</p>

#### [ Scott Morrison (Nov 13 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570486):
<p>it is the edit distance calculations that are slow</p>

#### [ Scott Morrison (Nov 13 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570489):
<p>so this has nothing to do with proofs</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570491):
<p>they should both be pretty fast</p>

#### [ Keeley Hoek (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570510):
<p>We could use <code>nat</code> I think<br>
I just have to find all the typeclass names I think</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570511):
<p>for numbers less than 2^30 or so it's just using the C++ addition which should be super fast</p>

#### [ Scott Morrison (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570517):
<p>ok, all our numbers should be small enough, I think</p>

#### [ Keeley Hoek (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570540):
<p>do you have any idea why <code>min</code> could be (relatively speaking) slow?</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570542):
<p>there is a lot of overhead for VM stuff but no more than anything else</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570604):
<p>You can look at the code generated for a definition using <code>set_option trace.compiler.optimize_bytecode true</code></p>

#### [ Scott Morrison (Nov 13 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570617):
<p>oooh...</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570676):
<p>If you inline the definition of <code>min</code> it's almost as fast as it possibly could be</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570686):
<p>if you don't inline there is possible inefficiency in creating and destroying the <code>nat.decidable_linear_ordered_semiring</code></p>

#### [ Mario Carneiro (Nov 13 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570729):
<p>but I don't know how significant it is</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570739):
<p>(And by inline I mean <code>attribute [inline] min</code>)</p>

#### [ Keeley Hoek (Nov 13 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570933):
<p>ooooh</p>

#### [ Keeley Hoek (Nov 13 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570948):
<p>can you inline instances?</p>

#### [ Keeley Hoek (Nov 13 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147570951):
<p>like where they are used</p>

#### [ Mario Carneiro (Nov 13 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147571233):
<p>you don't want to inline instances, you want to inline projections. My experiments with <code>min</code> on <code>nat</code> show exactly the kind of simplification you would want</p>

#### [ Keeley Hoek (Nov 13 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147582312):
<p>Just for the record: we ended up getting a factor-of-three speedup by inlining a bunch of important things in the hotpath, and eliminating some pesky table lookups in favor of using more memory---and parallelisation is to come!</p>

#### [ Kenny Lau (Nov 13 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147582752):
<p>finally someone more clever than me is using a more clever approach to speed up things! :D</p>

#### [ Kenny Lau (Nov 14 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147668689):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> would you have any insight as to how I could speed up <a href="https://github.com/leanprover/mathlib/pull/461/commits/f80e9fce6b081cf26f551b3ae2e5c83327f9bd59#diff-1f7cb4d661f00b6d887925434b41ad5dR293" target="_blank" title="https://github.com/leanprover/mathlib/pull/461/commits/f80e9fce6b081cf26f551b3ae2e5c83327f9bd59#diff-1f7cb4d661f00b6d887925434b41ad5dR293">this</a> without doing what I did?</p>

#### [ Keeley Hoek (Nov 14 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669081):
<p>Unfortunately not without contriving a tactic kenny<br>
---but I must get to bed!</p>

#### [ Keeley Hoek (Nov 14 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669084):
<p>:O the string <code>@mv_polynomial σ α (@comm_ring.to_comm_semiring α _inst_3)</code> appears 31 times!</p>

#### [ Keeley Hoek (Nov 14 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669239):
<p>But its definitely something to think about<br>
<code>(@comm_ring.to_comm_semiring α _inst_3)</code> 67 times!</p>

#### [ Keeley Hoek (Nov 14 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669365):
<p>Can you think of a general way to hint about this kind of stuff? <br>
Maybe you could say "use <code>comm_ring.to_comm_semiring</code> everywhere you can first"</p>

#### [ Keeley Hoek (Nov 14 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147669375):
<p>To some tactic</p>

#### [ Kenny Lau (Nov 14 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147670232):
<p>I don't write tactics...</p>

#### [ Keeley Hoek (Nov 14 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/efficiency/near/147670331):
<p>:D<br>
It's on the list, then!</p>


{% endraw %}
