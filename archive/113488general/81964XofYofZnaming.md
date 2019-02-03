---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81964XofYofZnaming.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [X_of_Y_of_Z naming](https://leanprover-community.github.io/archive/113488general/81964XofYofZnaming.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 12 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954801):
<p>What theorem is called <code>X_of_Y_of_Z</code>? Is it <code>Y -&gt; Z -&gt; X</code> or <code>Z -&gt; Y -&gt; X</code> or even something else? Or are things more fluid than this?</p>

#### [ Chris Hughes (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954877):
<p><code>Y -&gt; Z -&gt; X</code></p>

#### [ Chris Hughes (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954879):
<p>as in <code>lt_of_le_of_lt</code></p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954882):
<p>Right, that's why I asked.</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954886):
<p>I just don't understand how the brackets work</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954890):
<p>If "of" means "follows from"</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954892):
<p>is <code>of</code> right associative</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954929):
<p>since it represents <code>-&gt;</code></p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954935):
<p>then <code>Y-&gt;Z-&gt;X</code> is <code>Y-&gt;(Z-&gt;X)</code></p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954938):
<p>which is <code>(X_of_Z)_of_Y</code></p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954942):
<p>it is also a mystery to me, hah</p>

#### [ Simon Hudon (Apr 12 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954957):
<p>I think <code>X_of_Y_of_Z</code> is <code>Y -&gt; Z -&gt; X</code>: only the consequent is out of order in the name</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124954958):
<p>well <code>(X_of_Y)_of_Z</code> seems to mean <code>Z-&gt;(Y-&gt;X)</code> and <code>X_of_(Y_of_Z)</code> seems to mean <code>(Z-&gt;Y)-&gt;X</code></p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955010):
<p>So are you clear on the logic? What does <code>A_of_B_of_C_of_D</code> say?</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955028):
<p>I don't know these fancy CS terms like consequent by the way</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955031):
<p>Sorry</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955034):
<p>somewhere, a logician is crying</p>

#### [ Kevin Buzzard (Apr 12 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955038):
<p>next you'll be telling me that something is a minor premise</p>

#### [ Simon Hudon (Apr 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955076):
<blockquote>
<p>well <code>(X_of_Y)_of_Z</code> seems to mean <code>Z-&gt;(Y-&gt;X)</code> and <code>X_of_(Y_of_Z)</code> seems to mean <code>(Z-&gt;Y)-&gt;X</code></p>
</blockquote>
<p>I disagree with that assessment. I would say that <code>A_of_B_of_C_of_D</code> is <code>B -&gt; C -&gt; D -&gt; A</code></p>

#### [ Chris Hughes (Apr 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955081):
<p>I think <code>of</code> doesn't follow right or left associativity rules</p>

#### [ Simon Hudon (Apr 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955083):
<p>Consequent is the only positive term in a chain of implications, i.e. the right-most term.</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955144):
<p>if i had to guess i would think like simon it's right assoc</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955153):
<p>so a_of_b... is B -&gt; C -&gt; D -&gt; A</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955170):
<p>so how do we put parentheses in our theorem names? who knows</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955173):
<p>oh</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955179):
<p>i have seen <code>imp</code> used in theorem names</p>

#### [ Simon Hudon (Apr 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955181):
<blockquote>
<p>I don't know these fancy CS terms like consequent by the way</p>
</blockquote>
<p>I wonder if we could create a sitcom where a mathematician and a computer scientist share a flat. I'm sure they'd get into lots of crazy (conceptual) hijinks</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955184):
<p>so <code>(a-&gt;b)-&gt;c</code> is <code>c_of_a_imp_b</code></p>

#### [ Simon Hudon (Apr 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955228):
<blockquote>
<p>if i had to guess i would think like simon it's right assoc</p>
</blockquote>
<p>I don't think that's an associativity rule actually.</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955235):
<p>if it isn't that way, it should be, it should follow the same rules as <code>-&gt;</code></p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955238):
<p>otherwise my brain may explode</p>

#### [ Simon Hudon (Apr 12 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955256):
<p>As for <code>imp</code>, the difference is that you use <code>imp</code> where you would normally use <code>le</code> or <code>lt</code>: <code>and_imp_and_of_imp_of_imp</code> for example to state that conjunction is monotonic in both arguments</p>

#### [ Andrew Ashworth (Apr 12 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955306):
<p>frankly speaking, trying to remember how a theorem should be named is kinda of ridiculous. when lean 4 comes out i'm sure <span class="user-mention" data-user-id="110027">@Moses Schönfinkel</span> will write the Lean SearchAbout we've been waiting for :)</p>

#### [ Andrew Ashworth (Apr 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955407):
<p>i have the same general hatred when it comes to reading C++ qualifiers</p>

#### [ Andrew Ashworth (Apr 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955416):
<p>the rule is, read it from the right and wrap around, which is terrible</p>

#### [ Andrew Ashworth (Apr 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955431):
<p><a href="http://goshdarnfunctionpointers.com" target="_blank" title="http://goshdarnfunctionpointers.com">http://goshdarnfunctionpointers.com</a></p>

#### [ Simon Hudon (Apr 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955478):
<p>Now I remember that fun :)</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955781):
<p>Looking through mathlib it does seem to be consistently using <code>X_of_Y_of_Z : Y -&gt; Z -&gt; X</code></p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955786):
<p>and there was me thinking there would be some sort of logic ;-)</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124955852):
<div class="codehilite"><pre><span></span>lt_of_lt_of_le
lt_of_le_of_lt
pos_of_dvd_of_pos
decidable_of_decidable_of_iff
neg_of_nat_of_succ
lt_add_of_le_of_pos
mem_of_eq_of_mem
mem_of_subset_of_mem
eq_of_subset_of_subset
nat.not_coprime_of_dvd_of_dvd
eq_of_le_of_forall_le_of_dense
mul_nonpos_of_nonpos_of_nonneg
lt_add_of_lt_of_nonneg
eq_of_sublist_of_length_le
not_mem_cons_of_ne_of_not_mem
eq_of_sorted_of_perm
heq_of_heq_of_eq
decidable_of_decidable_of_iff
div_of_neg_of_pos
</pre></div>

#### [ Chris Hughes (Apr 12 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956074):
<p>Does it really matter? If I want <code>pos_of_dvd_of_pos</code> and I get <code>pos_of_pos_of_dvd</code> they're both the same thing.</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956089):
<p>oh they are very anal about names here :-)</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956144):
<p>looking through that stacks file you wrote I see <code>lemma thingy ...</code> so perhaps you are less fussy than them ;-)</p>

#### [ Simon Hudon (Apr 12 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956317):
<p>The logic I see is: <code>&lt;something&gt;_of_&lt;list_of_assumptions_separated_by_of&gt;</code> and that list of assumptions is in the order that you should feed them to a function application if you build the proof term by hand. You could advocate for <code>&lt;list_of_assumptions_separated_by_of&gt;_of_&lt;something&gt;</code> so that the name mentions assumptions in the same order as the type but I think it's very useful that the first thing you see in the name is what you can achieve with it.</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956617):
<p>Yes that's why they went for of rather than imp, right? I like that, I just can't make any sense of the logic for the rest of it when there are two ofs</p>

#### [ Simon Hudon (Apr 12 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956706):
<p>You mean like <code>lt_of_lt_of_le</code>? It proves <code>lt</code> from two assumptions: 1. <code>lt</code>; 2. <code>le</code>. The order of those assumptions is the same as in the name</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956718):
<p>right, as in <code>lt_of_lt_and_le</code></p>

#### [ Simon Hudon (Apr 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956722):
<p>Yeah, exactly</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956763):
<p>but not as in <code>lt_is_implied_by_lt_which_is_implied_by_le</code></p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956769):
<p>i.e. not as in <code>lt_of_lt_of_le</code></p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956776):
<p>if "of" is supposed to mean "is implied by"</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956791):
<p>and also not as in "(lt_is_implied_by_lt)_is_implied_by_le"</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956839):
<p>but actually exactly as in "(lt_is_implied_by_le)_is_implied_by_lt"</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956842):
<p>i.e. exactly "(lt_of_le)_of_lt"</p>

#### [ Simon Hudon (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956847):
<p>Right. I guess that's where the associativity talk is relevant. It's <code>(lt of lt) of le</code> with the little twist that the assumptions are shuffled ..</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956852):
<p>Aah</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956860):
<p>for you <code>X -&gt; Y -&gt;Z</code> and <code>Y -&gt; X -&gt; Z</code> are exactly the same</p>

#### [ Simon Hudon (Apr 12 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956861):
<p>Yes. As you said</p>

#### [ Simon Hudon (Apr 12 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956866):
<p>Because it's equivalent to <code>lt_of_lt_and_le</code>, the assumptions commute</p>

#### [ Simon Hudon (Apr 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956921):
<p>They are logically equivalent</p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956924):
<p>so you're saying <code>lt_of_lt_of_le</code> and <code>lt_of_le_of_lt</code> should be defeq? ;-)</p>

#### [ Simon Hudon (Apr 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956928):
<p>Nooooooo, no, no, no! <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Kevin Buzzard (Apr 12 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956937):
<p>then why did you name one after what the other one does? ;-)</p>

#### [ Simon Hudon (Apr 12 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124956942):
<p>Because I'm a bad person</p>

#### [ Simon Hudon (Apr 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124957006):
<p>Of course the names leave out important information that we have to rely on your imagination to fill in. The full name should be <code>x_lt_z_of_x_lt_y_of_y_le_z</code>. Then swapping the assumptions is not semantically meaningful, it's just confusing.</p>

#### [ Simon Hudon (Apr 12 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124957015):
<p>Note: defeq and logically equivalent, are not the same by the way ;-)</p>

#### [ Mario Carneiro (Apr 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958788):
<p>The <code>X_of_Y_of_Z</code> means <code>Y -&gt; Z -&gt; X</code> convention is used throughout mathlib, and it was documented a long time ago in Jeremy's style notes</p>

#### [ Kevin Buzzard (Apr 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958797):
<p>Yes, I learnt that now, from example</p>

#### [ Kevin Buzzard (Apr 12 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958799):
<p>I was just querying the logic</p>

#### [ Mario Carneiro (Apr 12 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958807):
<blockquote>
<p>The hypotheses are listed in the order they appear, <em>not</em> reverse order. For example, the theorem <code>A → B → C</code> would be named <code>C_of_A_of_B</code>.</p>
</blockquote>
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/naming.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/naming.md">https://github.com/leanprover/mathlib/blob/master/docs/naming.md</a></p>

#### [ Mario Carneiro (Apr 12 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958868):
<p>The logic is, the consequent is the most important part, so it comes first (this is important for autocomplete), but otherwise there is no reshuffling of names from the order they appear in the statement or the order you use them</p>

#### [ Mario Carneiro (Apr 12 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124958921):
<p>Don't think too hard about currying these things, theorems are generally fully applied anyway</p>

#### [ Moses Schönfinkel (Apr 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/X_of_Y_of_Z%20naming/near/124973894):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> I 100% will.</p>


{% endraw %}
