---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10421canIfixthisdeterministictimeout.html
---

## Stream: [general](index.html)
### Topic: [can I fix this deterministic timeout?](10421canIfixthisdeterministictimeout.html)

---


{% raw %}
#### [ Kevin Buzzard (May 09 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334659):
<p>I am in the middle of a long proof and finding it hard to shorten. I have a hypothesis H3 in my local context. I have a killer theorem which I want to apply, which takes 11 inputs (it's one of these obvious-to-a-mathematician statements of the form "if something happens, then when you replace everything by something equiv to it then it still happens). I want one of the inputs to be H3, but if I put H3 into it then I get a deterministic timeout. Instead I write (_ : [type of H3]) as an input and then I get an extra goal, which I can clear with <code>exact H3</code>.</p>

#### [ Kevin Buzzard (May 09 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334716):
<p>Am I missing a trick here? Am I likely to have made an error? I am not sure I can minimise.</p>

#### [ Mario Carneiro (May 09 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334730):
<p>that's a bit vague. does <code>by exact H3</code> work?</p>

#### [ Kevin Buzzard (May 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334745):
<p>I know it's vague, but deterministic timeouts are a big vague too :-/</p>

#### [ Mario Carneiro (May 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334754):
<p>is the type of H3 exactly the same as the expected type?</p>

#### [ Kevin Buzzard (May 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334808):
<p>I believe so</p>

#### [ Kevin Buzzard (May 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334811):
<p><code>by exact H3</code> doesn't work</p>

#### [ Kevin Buzzard (May 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334814):
<p>in the sense that I still get the timeout</p>

#### [ Kevin Buzzard (May 09 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334827):
<p><code>  have H3 : (Π (i : γ), loc Rr (powers (f i))) ≃ Π (i : γ), loc R (non_zero_on_U (Ui i)) := equiv.prod H2,</code></p>

#### [ Kevin Buzzard (May 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334848):
<p>[is equiv.prod already there, by the way? If X i equiv Y i for all i then prod_i X i = prod_i Y i]</p>

#### [ Mario Carneiro (May 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334861):
<p><code>Pi_congr_right</code></p>

#### [ Kevin Buzzard (May 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334873):
<p>and <code> (H3 : ((Π (i : γ), loc Rr (powers (f i))) ≃ (Π (i : γ), loc R (non_zero_on_U (Ui i))))) </code> as my input gives me a timeout</p>

#### [ Mario Carneiro (May 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334919):
<p><code>prod</code> is the binary product</p>

#### [ Kevin Buzzard (May 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334923):
<p>thanks</p>

#### [ Kevin Buzzard (May 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334927):
<p>that would be why I couldn't find it ;-)</p>

#### [ Kevin Buzzard (May 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334945):
<p>I should say that one can't determine the type of H3 immediately, type class inference is doing a lot of work here</p>

#### [ Mario Carneiro (May 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334953):
<p>I'm afraid this is a little too restricted to get the full picture</p>

#### [ Kevin Buzzard (May 09 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126334954):
<p>I have about 15 implicit inputs as well as about 10 explicit ones</p>

#### [ Mario Carneiro (May 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335008):
<p>I suggest leaving this for later then, <code>refine</code> with a <code>_</code> and then insert it after the unification works</p>

#### [ Kevin Buzzard (May 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335023):
<p>yes this works fine</p>

#### [ Kevin Buzzard (May 09 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335029):
<p>Here's the function I'm trying to apply</p>

#### [ Kevin Buzzard (May 09 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335030):
<p><code>fourexact_from_iso_to_fourexact :
  ∀ {A B C A' B' C' : Type u_1} [_inst_1 : add_comm_group A] [_inst_2 : add_comm_group A']
  [_inst_3 : add_comm_group B] [_inst_4 : add_comm_group B'] [_inst_5 : add_comm_group C] [_inst_6 : add_comm_group C']
  (ab : A → B) [_inst_7 : is_add_group_hom ab] (bc : B → C) [_inst_8 : is_add_group_hom bc],
    (∀ (b : B), bc b = 0 → (∃! (a : A), ab a = b)) →
    ∀ (fa : A ≃ A') [_inst_9 : is_add_group_hom ⇑fa] (fb : B ≃ B') [_inst_10 : is_add_group_hom ⇑fb]
    (fc : C ≃ C') [_inst_11 : is_add_group_hom ⇑fc] (ab' : A' → B') [_inst_12 : is_add_group_hom ab']
    (bc' : B' → C') [_inst_13 : is_add_group_hom bc'],
      (∀ (a : A), ⇑fb (ab a) = ab' (⇑fa a)) →
      (∀ (b : B), ⇑fc (bc b) = bc' (⇑fb b)) → ∀ (b' : B'), bc' b' = 0 → (∃! (a' : A'), ab' a' = b')</code></p>

#### [ Kevin Buzzard (May 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335088):
<p>I have 13 things which need to be inferred by type class inference because someone somewhere decided that <code>add_comm_group</code> and <code>is_add_group_hom</code> were type classes</p>

#### [ Kevin Buzzard (May 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335099):
<p>and I have six add_comm_groups</p>

#### [ Mario Carneiro (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335108):
<p>I assume all those searches are trivial though, right?</p>

#### [ Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335109):
<p>and I want Lean to infer them from things like <code>ab</code> and <code>fb</code> etc</p>

#### [ Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335116):
<p>yes everything should be trivial</p>

#### [ Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335117):
<p>oh</p>

#### [ Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335119):
<p>let me rephrase</p>

#### [ Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335120):
<p>that</p>

#### [ Mario Carneiro (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335124):
<p>like they are in the context</p>

#### [ Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335126):
<p>I have no idea whether these searches are trivial</p>

#### [ Kevin Buzzard (May 09 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335129):
<p>I doubt they're in the context</p>

#### [ Kevin Buzzard (May 09 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335179):
<p>I could easily put them in with <code>by apply_instance</code></p>

#### [ Kevin Buzzard (May 09 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335183):
<p>If I put them in the context, will type class inference pick them up? I thought not</p>

#### [ Mario Carneiro (May 09 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335185):
<p>I suggest you have a type for group isos instead of <code>(fa : A ≃ A') [_inst_9 : is_add_group_hom ⇑fa] </code></p>

#### [ Kevin Buzzard (May 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335190):
<p>I have a type for R-algebra isos ;-)</p>

#### [ Kevin Buzzard (May 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335208):
<p>and instances which give me the equiv and the add_group_hom</p>

#### [ Kevin Buzzard (May 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335210):
<p>but I'm letting type class inference do all of this</p>

#### [ Kevin Buzzard (May 09 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335264):
<p>This whole experience has been extremely hard going, by the way.</p>

#### [ Kevin Buzzard (May 09 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335267):
<p>I've had to set that other parameter which causes me trouble up to 100</p>

#### [ Mario Carneiro (May 09 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335269):
<p>I suggest you apply this theorem by writing <code>apply fourexact_from_iso_to_fourexact ... bc'</code> giving all the function arguments, and then prove the remaining goals</p>

#### [ Kevin Buzzard (May 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335271):
<p>yes that's exactly what I'm doing</p>

#### [ Kevin Buzzard (May 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335276):
<p>it avoids the time out</p>

#### [ Kevin Buzzard (May 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335279):
<p>It does mean that all of a sudden I go from 1 goal to 11</p>

#### [ Kevin Buzzard (May 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335287):
<p>I have <code>set_option class.instance_max_depth 100</code> too</p>

#### [ Kevin Buzzard (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335317):
<p>and all I am doing is proving something which is so trivial that it is not even explicitly mentioned in the stacks project</p>

#### [ Mario Carneiro (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335330):
<p>An alternative is <code>have := fourexact_from_iso_to_fourexact ... bc' </code> then <code>refine this ...</code> with the remaining args</p>

#### [ Kevin Buzzard (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335333):
<p>I have a workaround</p>

#### [ Kevin Buzzard (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335336):
<p>I was just wondering what was happening</p>

#### [ Kevin Buzzard (May 09 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335342):
<p>I was going to take the 11 goals</p>

#### [ Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335353):
<p>and then solve them all in squiggly brackets with "show" at the top of each one</p>

#### [ Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335355):
<p>This theorem is more complicated than it needs to be btw</p>

#### [ Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335359):
<p>I know full well</p>

#### [ Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335360):
<p>you don't need any groups at all</p>

#### [ Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335362):
<p>because it's all trivial</p>

#### [ Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335366):
<p>and your silly system doesn't know this</p>

#### [ Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335368):
<p>the statement is just about functions</p>

#### [ Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335369):
<p>so all the TC args can go away</p>

#### [ Kevin Buzzard (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335370):
<p>TC?</p>

#### [ Mario Carneiro (May 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335372):
<p>typeclass</p>

#### [ Kevin Buzzard (May 09 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335416):
<p>yes you're right</p>

#### [ Kevin Buzzard (May 09 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335419):
<p>It's a statement about pointed sets</p>

#### [ Kevin Buzzard (May 09 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335421):
<p>Are there pointed sets in Lean?</p>

#### [ Kevin Buzzard (May 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335433):
<p>I've been carrying the group homs around because in practice one uses some algebra to prove the diagram commutes -- "both maps are the unique group hom with some property" etc.</p>

#### [ Kevin Buzzard (May 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335436):
<p>You need a zero though, to define kernel</p>

#### [ Mario Carneiro (May 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335437):
<p>Floris knows a lot about pointed sets in lean</p>

#### [ Kevin Buzzard (May 09 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335438):
<p>But you don't need anything else</p>

#### [ Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335440):
<p>I'll rephrase it in terms of pointed sets</p>

#### [ Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335480):
<p>and then someone will make [is_pointed_set_hom] a typeclass</p>

#### [ Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335482):
<p>and I'll be back to square one ;-)</p>

#### [ Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335483):
<p>So it's not just about functions in fact</p>

#### [ Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335485):
<p>I need that a kernel maps to a kernel</p>

#### [ Mario Carneiro (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335486):
<p>For your purposes I would just take the pointedness assumption as an argument</p>

#### [ Kevin Buzzard (May 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335488):
<p>so I need that 0 maps to 0</p>

#### [ Kevin Buzzard (May 09 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335501):
<p>I need that my equivs are equivs of pointed sets</p>

#### [ Mario Carneiro (May 09 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335571):
<p>You should study how the <code>transfer</code> tactic works, even if you don't use the tactic the supporting theorems may be of use to you</p>

#### [ Kevin Buzzard (May 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335843):
<p>I am solving my 11 goals and I think I located the reason for the time-out. If I put <code>H3</code> explicitly into the system then type class inference tries to prove it's a group hom and type class inference isn't very good at this sort of thing in my experience.</p>

#### [ Kevin Buzzard (May 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335852):
<p>Ever since I've been trying to use type class inference to prove things are group homs / ring homs etc, I've been having trouble.</p>

#### [ Kevin Buzzard (May 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335860):
<p>I've now realised that this is just another one of my type class woes</p>

#### [ Kevin Buzzard (May 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335920):
<div class="codehilite"><pre><span></span>  <span class="k">show</span> <span class="n">is_add_group_hom</span> <span class="n">H3&#39;</span><span class="o">,</span>
    <span class="n">apply_instance</span><span class="o">,</span>
</pre></div>

#### [ Kevin Buzzard (May 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335929):
<p>There's the time-out. So your instinct was right</p>

#### [ Kevin Buzzard (May 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335931):
<p>Thanks.</p>

#### [ Kevin Buzzard (May 09 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335940):
<p>It's a product of group homs</p>

#### [ Kevin Buzzard (May 09 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126335954):
<p>and maybe there's no instance that if X i -&gt; Y i is a group hom for all i then Pi i, X i -&gt; Pi i, Y i is a group hom</p>

#### [ Mario Carneiro (May 09 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126336362):
<p>that one is up to you, I don't think <code>is_add_group_hom</code> even exists in mathlib</p>

#### [ Mario Carneiro (May 09 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126336409):
<p>but you have to show that <code>Pi_congr_right</code> as defined respects the Pi group structure</p>

#### [ Kevin Buzzard (May 10 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337259):
<p>I have type class inference issues :-(</p>

#### [ Kevin Buzzard (May 10 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337281):
<p>How do I say "for all i, the proof (e i) of equiv (X i) (Y i) is a ring hom" (say)</p>

#### [ Kevin Buzzard (May 10 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337291):
<p>in the sense that I want that to be the assumption, inferred by type class inference</p>

#### [ Kevin Buzzard (May 10 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337294):
<p>This has nothing to do with equiv.</p>

#### [ Kevin Buzzard (May 10 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337333):
<p>Let me formulate something easier, and in the correct thread.</p>

#### [ Mario Carneiro (May 10 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337602):
<p>It's just <code>\forall i, is_ring_hom (e i)</code></p>

#### [ Kevin Buzzard (May 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337667):
<p>It was getting it in the brackets I was worried about</p>

#### [ Kevin Buzzard (May 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337670):
<p>But <code>[∀ (i : γ), ring (F i)]</code> works fine</p>

#### [ Kevin Buzzard (May 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337671):
<p>I've never seen that construction before</p>

#### [ Kevin Buzzard (May 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126337681):
<p>Thanks as ever. I'm back on track!</p>

#### [ Patrick Massot (May 10 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353221):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> You should start reading from <a href="https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L61" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L61">https://github.com/leanprover/mathlib/blob/master/algebra/pi_instances.lean#L61</a></p>

#### [ Patrick Massot (May 10 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353227):
<p>and add things if needed</p>

#### [ Kevin Buzzard (May 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353552):
<p>We use this stuff in the schemes work.</p>

#### [ Kevin Buzzard (May 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353555):
<p>But it's only objects.</p>

#### [ Kevin Buzzard (May 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353556):
<p>I now realise we need the morphisms too.</p>

#### [ Kevin Buzzard (May 10 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353562):
<p>Currently my impression is that the morphisms which are classes are kind of random, and not all are classes.</p>

#### [ Kevin Buzzard (May 10 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353613):
<p>For morphisms, I find myself needing both "if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>→</mo><msub><mi>Y</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">X \to Y_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.22222em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> are group homs, then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>→</mo><msub><mi mathvariant="normal">Π</mi><mi>i</mi></msub><msub><mi>Y</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">X \to \Pi_i Y_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">→</span><span class="mord"><span class="mord mathrm">Π</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.22222em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> is"</p>

#### [ Kevin Buzzard (May 10 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353619):
<p>and "if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>X</mi><mi>i</mi></msub><mo>→</mo><msub><mi>Y</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">X_i\to Y_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.07847em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">→</span><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.22222em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> are group homs, then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="normal">Π</mi><mi>i</mi></msub><msub><mi>X</mi><mi>i</mi></msub><mo>→</mo><msub><mi mathvariant="normal">Π</mi><mi>i</mi></msub><msub><mi>Y</mi><mi>i</mi></msub></mrow><annotation encoding="application/x-tex">\Pi_i X_i \to \Pi_i Y_i</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Π</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.07847em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">→</span><span class="mord"><span class="mord mathrm">Π</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.22222em;">Y</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.31166399999999994em;"><span style="top:-2.5500000000000003em;margin-left:-0.22222em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">i</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> is too"</p>

#### [ Kevin Buzzard (May 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353780):
<p>It was these instances that caused the time-out :-)</p>

#### [ Kevin Buzzard (May 10 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353781):
<p>It knew that the product of groups was a group and then timed out trying to prove using type class inference only that the product of the morphisms was a morphism</p>

#### [ Mario Carneiro (May 10 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353850):
<p>how are those functions being specified?</p>

#### [ Mario Carneiro (May 10 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353853):
<p>you wrote the type but not the term there</p>

#### [ Patrick Massot (May 10 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353929):
<p>Then I'm confused. How could you write: "<code>[∀ (i : γ), ring (F i)]</code> I've never seen that construction before"</p>

#### [ Patrick Massot (May 10 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353979):
<p>Anyway, I think having Lean figuring out by itself that composition and products of morphisms are morphisms is a good reason to try to use type class here.  But you need to add instances to that <code>pi_instance</code> file, which was written at a time were morphisms were defs</p>

#### [ Patrick Massot (May 10 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353984):
<p>That may require improving Simon's <code>pi_instance</code> tactic</p>

#### [ Patrick Massot (May 10 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126353986):
<p>I'm not sure</p>

#### [ Kevin Buzzard (May 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354452):
<blockquote>
<p>how are those functions being specified?</p>
</blockquote>
<p>There's only one sensible specification in each case. I just noticed that the Android Zulip app doesn't do maths mode.</p>

#### [ Kevin Buzzard (May 10 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354495):
<blockquote>
<p>Then I'm confused. How could you write: "<code>[∀ (i : γ), ring (F i)]</code> I've never seen that construction before"</p>
</blockquote>
<p>I glanced at the Pi file at the time, realised I understood what it did, forgot how it did it, then had to do it myself. Patrick I'm nearly 50. It's completely consistent that I have to write <code>[∀ (i : γ), ring (F i)]</code> again in two months' time and again claim that I've never seen it before.</p>

#### [ Kevin Buzzard (May 10 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354504):
<p>I mean "...according to my memory banks" :-)</p>

#### [ Kevin Buzzard (May 10 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354551):
<p>It's pretty depressing. Sometimes I want to know something about some technical number theory question so I google, find a good mathoverflow answer, read it, learn a lot, and then discover to my surprise that I had written the answer myself 5 years ago. The first time that happened to me was a genuine shock. Now I just consider it normal.</p>

#### [ Kevin Buzzard (May 10 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354556):
<p>It's not depressing at all -- it's pretty funny :-)</p>

#### [ Mario Carneiro (May 10 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354687):
<blockquote>
<p>There's only one sensible specification in each case.</p>
</blockquote>
<p>Not quite: are you giving an explicit lambda term or a definition?</p>

#### [ Kevin Buzzard (May 10 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354747):
<p>I don't understand the subtlety you've found, but what I am saying is that I need the following two facts:</p>

#### [ Mario Carneiro (May 10 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354750):
<p>I'm just asking what you wrote</p>

#### [ Mario Carneiro (May 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354769):
<p>the typeclass system is trying to solve <code>is_add_group_hom ...</code>; what is in the place of the <code>...</code>?</p>

#### [ Mario Carneiro (May 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354775):
<p>the typeclass system is very sensitive to the way you write things</p>

#### [ Kevin Buzzard (May 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354778):
<p>(1) If gamma is a type and for all i in gamma I have (f i : X -&gt; Y i), which type class inference knows is a group hom (actually in my case this one was a ring hom) then the induced map from X to Pi i, Y i sending x i to f i (x) is a group hom</p>

#### [ Mario Carneiro (May 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354787):
<blockquote>
<p>the induced map from X to Pi i, Y i sending x i to f i (x)</p>
</blockquote>
<p>and how did you write that</p>

#### [ Kevin Buzzard (May 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354850):
<p><code>\lam x i,f i x</code> I guess</p>

#### [ Mario Carneiro (May 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354851):
<p>did you prove that in a lemma?</p>

#### [ Kevin Buzzard (May 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354854):
<p>I proved it in an instance</p>

#### [ Mario Carneiro (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354856):
<p>show me</p>

#### [ Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354862):
<p>well I didn't yet</p>

#### [ Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354863):
<p>are you saying I'm going to run into trouble?</p>

#### [ Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354864):
<p>I proved the other one</p>

#### [ Mario Carneiro (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354866):
<p>well if the instance isn't there of course it will fail</p>

#### [ Mario Carneiro (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354868):
<p>but yes, that instance is trouble</p>

#### [ Mario Carneiro (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354870):
<p>you want to wrap that function in a definition</p>

#### [ Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354872):
<p>Oh</p>

#### [ Kevin Buzzard (May 10 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354873):
<p>Here's the one I did</p>

#### [ Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354894):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">Prod</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">G</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
 <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">Fi</span> <span class="n">i</span><span class="o">,</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">Fi</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
<span class="k">show</span> <span class="n">H</span> <span class="n">i</span> <span class="o">((</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">))</span> <span class="bp">=</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">),</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">(</span><span class="n">add</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">))</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354915):
<p>You don't know the type class I'm using here</p>

#### [ Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354919):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_add_group_hom</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354924):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">add</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">y</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">is_group_hom</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">β</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">hf</span> <span class="n">x</span> <span class="n">y</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354926):
<p>Are there problems with this?</p>

#### [ Mario Carneiro (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354934):
<p>this is bad: <code>is_add_group_hom (λ Fi i, H i (Fi i))</code></p>

#### [ Kevin Buzzard (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354935):
<p>Hmm</p>

#### [ Kevin Buzzard (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354936):
<p>Well thanks for spotting this</p>

#### [ Mario Carneiro (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354937):
<p>it's okay as a def but as an instance it requires higher order unification</p>

#### [ Kevin Buzzard (May 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354938):
<p>On the other hand</p>

#### [ Kevin Buzzard (May 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354982):
<p>these morphisms between mathematical objects are being defined to be type classes</p>

#### [ Kevin Buzzard (May 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354990):
<p>so I am being pushed to use the type class inference system</p>

#### [ Mario Carneiro (May 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354991):
<p>you just need to define <code>Pi_lift H := λ Fi i, H i (Fi i</code> and give that the instance</p>

#### [ Kevin Buzzard (May 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126354993):
<p>Oh so I can still use type class inference</p>

#### [ Mario Carneiro (May 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355001):
<p>the typeclass system needs a constant to key on</p>

#### [ Kevin Buzzard (May 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355005):
<p>This is of course the problem with me using things I don't understand completely</p>

#### [ Kevin Buzzard (May 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355008):
<p>It's exactly what I tell my graduate students not to do</p>

#### [ Kevin Buzzard (May 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355045):
<p>I don't know what "constant" or "key on" mean in your last post</p>

#### [ Mario Carneiro (May 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355051):
<p>for example if you want to show <code>is_group_hom (f o g)</code> it's no problem but <code>is_group_hom (\lam x, f (g x))</code> is not likely to work</p>

#### [ Kevin Buzzard (May 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355055):
<p><em>boggle</em></p>

#### [ Sean Leather (May 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355056):
<p>Mario probably means a unique definition name.</p>

#### [ Sean Leather (May 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355059):
<p><code>function.compose</code> in that case.</p>

#### [ Kevin Buzzard (May 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355062):
<p>I just spent some time changing f circ g's to lam x, f (g x) because Kenny told me that things were better that way</p>

#### [ Kevin Buzzard (May 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355069):
<p>in the sense that they were easier to work with</p>

#### [ Kenny Lau (May 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355070):
<blockquote>
<p>I just spent some time changing f circ g's to lam x, f (g x) because Kenny told me that things were better that way</p>
</blockquote>
<p>you see, things have a context</p>

#### [ Mario Carneiro (May 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355071):
<p>That's true for the most part, but if it shows up as the target of a typeclass problem you want it to be "obviously a morphism"</p>

#### [ Kenny Lau (May 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355112):
<blockquote>
<p>for example if you want to show <code>is_group_hom (f o g)</code> it's no problem but <code>is_group_hom (\lam x, f (g x))</code> is not likely to work</p>
</blockquote>
<p>but aren't they definitionally equivalent?</p>

#### [ Mario Carneiro (May 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355113):
<p>and that means writing things functorially</p>

#### [ Mario Carneiro (May 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355116):
<p>they are, but typeclass inference doesn't work up to definitional equivalence</p>

#### [ Kevin Buzzard (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355122):
<p>I wonder if this has anything to do with the fact that three times now I've had to <code>set_option class.instance_max_depth 100</code></p>

#### [ Mario Carneiro (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355123):
<p>it's doing a big search through the whole library. It doesn't have time to unify everything properly</p>

#### [ Kenny Lau (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355124):
<p>what do they work up to?</p>

#### [ Mario Carneiro (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355136):
<p>unification of metavariables unfolding reducibles only</p>

#### [ Kevin Buzzard (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355141):
<p>I want to give hints to the system</p>

#### [ Kenny Lau (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355142):
<p>is that another type of equivalence?</p>

#### [ Kevin Buzzard (May 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355145):
<p>because in every case I know exactly what I want it to do</p>

#### [ Mario Carneiro (May 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355189):
<p>it's almost syntactic equality, except that reducible definitions are eagerly expanded</p>

#### [ Kevin Buzzard (May 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355191):
<p>In some cases it's even "I want you to use precisely the instance which I just defined in another file precisely so that this next line will work"</p>

#### [ Mario Carneiro (May 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355201):
<p>the key is to write the typeclass problem so that it's obvious to the system</p>

#### [ Mario Carneiro (May 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355208):
<p>that basically means that all your typeclass instances should have the form <code>my_class (my_operation A B C)</code></p>

#### [ Kevin Buzzard (May 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355209):
<p>To put this into some context, the fact that the product of group homs is a group hom is the sort of thing which is explained in an undergraduate maths lecture in the 15 minute period just after the definition of a group hom has been given, and is then never mentioned again and everyone thinks it's obvious</p>

#### [ Mario Carneiro (May 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355248):
<p>with some assumptions like <code>my_class A</code> <code>my_class2 B</code></p>

#### [ Mario Carneiro (May 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355249):
<p>and your typeclass problems should look like <code>my_class (my_op (my_other_op A) B)</code></p>

#### [ Mario Carneiro (May 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355250):
<p>no lambdas</p>

#### [ Kevin Buzzard (May 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355259):
<p>Well this is very helpful. Whereabouts is all this documented? ;-)</p>

#### [ Sean Leather (May 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355260):
<p>Look up. <span class="emoji emoji-2b06" title="arrow up">:arrow_up:</span> <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Kevin Buzzard (May 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355303):
<p>I don't know why I'm bothering writing docs, I could just refer people to <a href="" target="_blank" title="">https://leanprover.zulipchat.com/</a></p>

#### [ Sean Leather (May 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355314):
<p>TBD: The <a href="https://leanprover.github.io/reference/declarations.html#type-classes" target="_blank" title="https://leanprover.github.io/reference/declarations.html#type-classes">type class reference section</a> is currently empty.</p>

#### [ Kevin Buzzard (May 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355316):
<p>Oh, on a related topic, why <code>Pi_congr_right</code>?</p>

#### [ Kevin Buzzard (May 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355356):
<p>I mean, why the name?</p>

#### [ Kevin Buzzard (May 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355357):
<p><code>equiv.Pi_congr_right :
  Π {α : Sort u_3} {β₁ : α → Sort u_4} {β₂ : α → Sort u_5},
    (Π (a : α), β₁ a ≃ β₂ a) → ((Π (a : α), β₁ a) ≃ Π (a : α), β₂ a)</code></p>

#### [ Kevin Buzzard (May 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355359):
<p>That looks like <code>equiv.Pi</code> to me</p>

#### [ Kevin Buzzard (May 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355360):
<p>modulo the fact that that name is probably illegal</p>

#### [ Kevin Buzzard (May 10 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355407):
<p>but I don't see anything <code>right</code> about it, other than the fact that it's right</p>

#### [ Kevin Buzzard (May 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355562):
<p>Are these fundamental constructions already in Lean:</p>

#### [ Kevin Buzzard (May 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355566):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">Pi_lift₁</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">G</span> <span class="n">i</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Fi</span> <span class="n">i</span><span class="o">,</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">Fi</span> <span class="n">i</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">Pi_lift₂</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">G</span> <span class="n">i</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">i</span><span class="o">,</span> <span class="n">H</span> <span class="n">i</span> <span class="n">x</span>
</pre></div>

#### [ Mario Carneiro (May 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355579):
<p>Pi takes two arguments</p>

#### [ Mario Carneiro (May 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355606):
<p>a domain and a family</p>

#### [ Mario Carneiro (May 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355620):
<p>Pi_congr_left is likely to be much messier though so I left it out</p>

#### [ Kevin Buzzard (May 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355632):
<p>So is the following now OK:</p>

#### [ Kevin Buzzard (May 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355671):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">is_add_group_hom</span><span class="bp">.</span><span class="n">Pi_lift</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">G</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
 <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">Pi_lift_map₁</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
<span class="k">show</span> <span class="n">H</span> <span class="n">i</span> <span class="o">((</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">))</span> <span class="bp">=</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">),</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">(</span><span class="n">add</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">))</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (May 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355673):
<p>yep that's ok</p>

#### [ Kevin Buzzard (May 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355683):
<p>Can you appreciate that this is a subtlety that people are unlikely to guess, and it's up to the very few people who appreciate the subtlety to somehow get the news around? :-/</p>

#### [ Mario Carneiro (May 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355684):
<p>certainly</p>

#### [ Kevin Buzzard (May 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355685):
<p>I don't recall this being mentioned in TPIL</p>

#### [ Kevin Buzzard (May 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355686):
<p>although as we've seen earlier in this thread, that's not saying much</p>

#### [ Kevin Buzzard (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355727):
<p>I guess I felt the same way about <code>simp</code> earlier on.</p>

#### [ Mario Carneiro (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355728):
<p>In a way, it's "your fault" in generalizing from "typeclasses can do X" to "typeclasses can do Y"</p>

#### [ Kevin Buzzard (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355729):
<p>I would tag arbitrary things with simp and then had to be rolled back by people that actually knew what simp did</p>

#### [ Kevin Buzzard (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355730):
<p>I mean, by people who knew _how simp actually worked_</p>

#### [ Kevin Buzzard (May 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355731):
<p>and I guess the same is happening here.</p>

#### [ Mario Carneiro (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355734):
<p>everything has limitations, and most of the existing documentation is vague about where the limitations are</p>

#### [ Kevin Buzzard (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355738):
<p>In maths, generalizing like that is a _really_ important skill</p>

#### [ Kevin Buzzard (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355739):
<p>It's not so clear that such limitations exist in maths</p>

#### [ Kevin Buzzard (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355741):
<p>If you understand the idea behind a proof</p>

#### [ Kevin Buzzard (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355742):
<p>then you can see the same idea working in many other situations</p>

#### [ Mario Carneiro (May 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355743):
<p>on the one hand, you can assume Leo is magic and made everything work (which is not an unreasonable rule of thumb)</p>

#### [ Kevin Buzzard (May 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355786):
<p>I feel like I need you a huge amount less than I needed you last October</p>

#### [ Kevin Buzzard (May 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355787):
<p>but I still need you from time to time :-)</p>

#### [ Kevin Buzzard (May 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355788):
<p>Many thanks as ever</p>

#### [ Mario Carneiro (May 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355789):
<p>but sometimes if you don't know you should stick to areas that you know how to use already... it's a balancing act</p>

#### [ Mario Carneiro (May 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355800):
<p>I don't use <code>finish</code> or <code>cc</code> because I don't understand them well</p>

#### [ Kevin Buzzard (May 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355804):
<p>Don't say that in front of your advisor</p>

#### [ Kevin Buzzard (May 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355805):
<p>didn't he write at least one of them?</p>

#### [ Mario Carneiro (May 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355808):
<p>yes, Jeremy wrote <code>finish</code></p>

#### [ Mario Carneiro (May 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355855):
<p>I'm not sure he understands it either, since it's a complicated set of heuristics calling in to less understood things like e-matching</p>

#### [ Kevin Buzzard (May 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355863):
<p>My impression is that computer scientists are much better at generating work that they "don't understand"</p>

#### [ Kevin Buzzard (May 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355865):
<p>much better than mathematicians, I mean</p>

#### [ Kevin Buzzard (May 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355869):
<p>If I use theorem X whose proof I've not read, in my proof, then I can just argue that I have a complete understanding of "theorem X implies the result I proved"</p>

#### [ Kevin Buzzard (May 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355870):
<p>and all proofs are irrelevant</p>

#### [ Mario Carneiro (May 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355910):
<p>says the man who is rediscovering his own proofs every five years :)</p>

#### [ Kevin Buzzard (May 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355911):
<p>:-)</p>

#### [ Kevin Buzzard (May 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355913):
<p>That's how irrelevant they are :-)</p>

#### [ Kevin Buzzard (May 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355915):
<p>I don't rediscover the proofs I created in my 20s and 30s, those are pretty much hard wired</p>

#### [ Kevin Buzzard (May 10 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355920):
<p>It's the stuff I do in my 40s that I occasionally do again</p>

#### [ Kevin Buzzard (May 10 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355923):
<p>This schemes code is getting quite unwieldy, and occasionally I prove some lemma and in the middle of the proof I think "I ran into this issue before, I think I already proved this lemma"</p>

#### [ Kevin Buzzard (May 10 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355925):
<p>With the tag system I can really control well this sort of thing, most of the time</p>

#### [ Kevin Buzzard (May 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126355969):
<p>but when I go "off piste" because the tag says "this is now clear, as every mathematican knows" and Lean is saying "but the diagrams! You have to check they commute!" and I end up with 1000 lines of code checking a triviality, that's when I duplicate</p>

#### [ Kevin Buzzard (May 10 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126356137):
<p>My esteemed co-author writes</p>

#### [ Kevin Buzzard (May 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126356138):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">deus</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">α</span> <span class="o">[</span><span class="mi">1</span><span class="bp">/</span><span class="n">S</span><span class="o">]</span> <span class="bp">/</span><span class="err">ᵣ</span> <span class="o">(</span><span class="n">S</span><span class="bp">⁻¹</span> <span class="n">I</span><span class="o">))</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">instance</span> <span class="n">salva</span> <span class="o">:</span> <span class="n">module</span> <span class="o">(</span><span class="n">α</span> <span class="o">[</span><span class="mi">1</span><span class="bp">/</span><span class="n">S</span><span class="o">]</span> <span class="bp">/</span><span class="err">ᵣ</span> <span class="o">(</span><span class="n">S</span><span class="bp">⁻¹</span> <span class="n">I</span><span class="o">))</span> <span class="o">(</span><span class="n">α</span> <span class="o">[</span><span class="mi">1</span><span class="bp">/</span><span class="n">S</span><span class="o">]</span> <span class="bp">/</span><span class="err">ᵣ</span> <span class="o">(</span><span class="n">S</span><span class="bp">⁻¹</span> <span class="n">I</span><span class="o">))</span> <span class="o">:=</span> <span class="n">ring</span><span class="bp">.</span><span class="n">to_module</span>
<span class="kn">instance</span> <span class="n">me</span> <span class="o">:</span> <span class="n">is_submodule</span> <span class="o">(</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">ker</span> <span class="o">(</span><span class="n">to_be_named_aux3</span> <span class="n">S</span> <span class="n">I</span><span class="o">))</span> <span class="o">:=</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">ker</span><span class="bp">.</span><span class="n">is_submodule</span> <span class="o">(</span><span class="n">to_be_named_aux3</span> <span class="n">S</span> <span class="n">I</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126356147):
<p>Are these OK (modulo the names)</p>

#### [ Kenny Lau (May 10 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126356199):
<blockquote>
<p>My esteemed co-author writes</p>
</blockquote>
<p>right</p>

#### [ Mario Carneiro (May 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357426):
<p>I would hope that <code>is_submodule (is_ring_hom.ker f)</code> always works</p>

#### [ Kevin Buzzard (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357465):
<p>Kenny look how stupid type class inference is:</p>

#### [ Kevin Buzzard (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357470):
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>
<span class="kn">definition</span> <span class="n">Pi_lift_map₁</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">G</span> <span class="n">i</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Fi</span> <span class="n">i</span><span class="o">,</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">Fi</span> <span class="n">i</span><span class="o">)</span>

<span class="n">class</span> <span class="n">foomap</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">preserves_structure</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">Pi_foomap_is_foomap</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">Pi_lift_map₁</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">Pi_lift_map₁</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span> <span class="n">foomap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">Fi</span> <span class="n">i</span><span class="o">,</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">Fi</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Mario Carneiro (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357471):
<p>the <code>salva</code> instance is trouble</p>

#### [ Kevin Buzzard (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357473):
<p>even though they're defeq</p>

#### [ Kevin Buzzard (May 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357481):
<p>the last example fails</p>

#### [ Mario Carneiro (May 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357486):
<p>It can be a local instance, but you don't necessarily want to always have that ring be a module over itself</p>

#### [ Kevin Buzzard (May 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357493):
<p>I think this is because type class inference doesn't have a constant to key on</p>

#### [ Kevin Buzzard (May 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357497):
<blockquote>
<p>It can be a local instance, but you don't necessarily want to always have that ring be a module over itself</p>
</blockquote>
<p>That ring _is_ always a module over itself, so what do you actually mean?</p>

#### [ Kevin Buzzard (May 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357615):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">Pi_lift_map₁</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span> <span class="o">(</span><span class="n">Pi_lift_map₁</span> <span class="n">H</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">Fi</span> <span class="n">i</span><span class="o">,</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">Fi</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">foomap</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span> <span class="n">foomap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">Fi</span> <span class="n">i</span><span class="o">,</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">Fi</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357617):
<p>well I've learnt something today</p>

#### [ Mario Carneiro (May 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357680):
<p>I mean that when you make it an instance you are saying "this is the only ring I want to consider this as a module over"</p>

#### [ Mario Carneiro (May 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357686):
<p>because modules infer their ring argument from typeclass inference</p>

#### [ Mario Carneiro (May 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357727):
<p>Any ring is a module over itself, but that doesn't mean that's the only ring you want to consider, for example R as a Q-module</p>

#### [ Johan Commelin (May 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357733):
<p>But if you consider R as an R-module, and later you need it as Q-module, then this could be inferred by some statement about forgetting scalars, right?</p>

#### [ Johan Commelin (May 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357734):
<p>Except that we might get a diamond...</p>

#### [ Mario Carneiro (May 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357735):
<p>forgetting scalars?</p>

#### [ Johan Commelin (May 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357736):
<p>From R to Q</p>

#### [ Mario Carneiro (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357778):
<p>as in you want to compose with a ring hom?</p>

#### [ Johan Commelin (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357781):
<p>Every R-module is a Q-module</p>

#### [ Johan Commelin (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357783):
<p>That is what I mean</p>

#### [ Kevin Buzzard (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357785):
<p>I can envisage your implied assertion that each abelian group can only be a module over one ring as being problematic</p>

#### [ Johan Commelin (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357786):
<p>And somehow <em>newbie me</em> would wish that typeclass inference can do that for me</p>

#### [ Kevin Buzzard (May 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357787):
<p>I just found something else problematic too</p>

#### [ Kevin Buzzard (May 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357792):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Pi_congr_right</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">β₁</span> <span class="n">β₂</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">β₁</span> <span class="n">a</span> <span class="err">≃</span> <span class="n">β₂</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">a</span><span class="o">,</span> <span class="n">β₁</span> <span class="n">a</span><span class="o">)</span> <span class="err">≃</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">a</span><span class="o">,</span> <span class="n">β₂</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">H</span> <span class="n">a</span><span class="o">,</span> <span class="n">F</span> <span class="n">a</span> <span class="o">(</span><span class="n">H</span> <span class="n">a</span><span class="o">),</span> <span class="bp">λ</span> <span class="n">H</span> <span class="n">a</span><span class="o">,</span> <span class="o">(</span><span class="n">F</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">H</span> <span class="n">a</span><span class="o">),</span>
 <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357793):
<p>That's your(?) definition of Pi_congr_right</p>

#### [ Kevin Buzzard (May 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357802):
<p>but you did not use <code>definition Pi_lift_map₁ {γ : Type u} {F : γ → Type u} {G : γ → Type u} 
  (H : ∀ i : γ, F i → G i) : (Π i, F i) → Π i, G i := λ Fi i, H i (Fi i)</code></p>

#### [ Johan Commelin (May 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357804):
<p>Ok, I guess I don't understand typeclass inference... and what I mean is that I would like every R-module to automatically coerce to a Q-module when that's necessary</p>

#### [ Mario Carneiro (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357808):
<p>of course not, you just wrote it</p>

#### [ Kevin Buzzard (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357853):
<p>but I am using <code>Pi_congr_right</code> to construct my product instances</p>

#### [ Kevin Buzzard (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357855):
<p>so now I can't use type class inference on them</p>

#### [ Mario Carneiro (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357858):
<p>You will need a theorem saying that <code>\u Pi_congr_right </code> is a group hom</p>

#### [ Mario Carneiro (May 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357860):
<p>it's defeq to your other one about Pi_lift</p>

#### [ Kevin Buzzard (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357865):
<p>I see, so I don't try and get you to rewrite Pi_congr_right</p>

#### [ Mario Carneiro (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357871):
<p>right, that's too much for TC inference</p>

#### [ Mario Carneiro (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357879):
<p>even if it was rewritten it wouldn't help</p>

#### [ Kevin Buzzard (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357881):
<p>But am I safe making this an instance?</p>

#### [ Mario Carneiro (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357883):
<p>yes</p>

#### [ Kevin Buzzard (May 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357887):
<p>I mean the proof that \u= Pi_congr_right is a group</p>

#### [ Kevin Buzzard (May 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357927):
<p>hom</p>

#### [ Kevin Buzzard (May 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357934):
<p>OK I see.</p>

#### [ Kevin Buzzard (May 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357942):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I didn't think too hard about the module ring thing yet</p>

#### [ Kevin Buzzard (May 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357952):
<p>but one funny thing about type classes is that if the devs deem a structure to be worthy of being called a class</p>

#### [ Kevin Buzzard (May 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357956):
<p>then you are only supposed to ever have one instance of that class</p>

#### [ Kevin Buzzard (May 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357957):
<p>I am not being very precise</p>

#### [ Kevin Buzzard (May 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357997):
<p>I mean that if <code>group</code> is a class, and <code>G</code> is a type, then <code>H1 : group G</code> and <code>H2 : group G</code> are supposed to be equal</p>

#### [ Kevin Buzzard (May 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126357998):
<p>because otherwise how can type class inference decide whether you want to use <code>H1</code> or <code>H2</code></p>

#### [ Kevin Buzzard (May 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358003):
<p>So if you want more than one group structure on your type <code>G</code>, you have to jettison type classes</p>

#### [ Kevin Buzzard (May 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358006):
<p>This happens in the topological space stuff in Lean -- a topological space is a structure</p>

#### [ Kevin Buzzard (May 10 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358009):
<p>because Johannes wanted to put more than one topological space on a set so he could partially order them for some reason</p>

#### [ Kevin Buzzard (May 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358049):
<p>But you can't edit the source, so a group is a class, so if there's more than one group structure on G then you have to go it alone</p>

#### [ Johan Commelin (May 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358050):
<p>But there is only one instance of <code>module R R</code> right? So that shouldn't be the problem that Mario was talking about...</p>

#### [ Johan Commelin (May 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358055):
<p>At the same time there could be an instance of <code>module Q R</code></p>

#### [ Johan Commelin (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358056):
<p>Or is that giving a conflict somewhere?</p>

#### [ Kevin Buzzard (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358057):
<p>In semilinear algebra I've seen plenty of other ways of making R an R-module, but that's not the point right now ;-)</p>

#### [ Johan Commelin (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358064):
<p>Right (-;</p>

#### [ Kevin Buzzard (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358065):
<p>Let's have a look at <code>module</code></p>

#### [ Johan Commelin (May 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358068):
<p>Those shouldn't be instances... for a reason</p>

#### [ Kevin Buzzard (May 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358073):
<p>I can't find it :-)</p>

#### [ Kevin Buzzard (May 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358109):
<p>got it</p>

#### [ Kevin Buzzard (May 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358123):
<p>yes module takes both the ring and the module as parameters</p>

#### [ Kevin Buzzard (May 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358124):
<p>so I don't understand Mario's comment</p>

#### [ Kevin Buzzard (May 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358165):
<blockquote>
<p>because modules infer their ring argument from typeclass inference</p>
</blockquote>
<p>It's this though</p>

#### [ Johan Commelin (May 10 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358176):
<p>I'm still confused...</p>

#### [ Kevin Buzzard (May 10 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358179):
<p>In the definition of <code>module</code> do you see <code>out_param</code>?</p>

#### [ Johan Commelin (May 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358217):
<p>Yes</p>

#### [ Kevin Buzzard (May 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358227):
<p><code>out_param</code> is a great function, it is the identity function</p>

#### [ Kevin Buzzard (May 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358230):
<p>but behind the scenes in the C++ code, type class inference is affected by <code>out_param</code></p>

#### [ Johan Commelin (May 10 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358234):
<p>Ouch... I'm being cheated again</p>

#### [ Kevin Buzzard (May 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358250):
<p>That <code>out_param</code> mean in practice "if you give me a module, I'm going to try and guess the ring"</p>

#### [ Kevin Buzzard (May 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358294):
<p>My guess is that this was written by people with some specific usage in mind, who did not talk to a professional ring theorist beforehand</p>

#### [ Johan Commelin (May 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358304):
<p>So we might get rid of the <code>out_param</code> and hopefully stuff would be better?</p>

#### [ Johan Commelin (May 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358307):
<p>Or will mathlib break?</p>

#### [ Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358315):
<p>As you know from the docs</p>

#### [ Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358318):
<p>(i.e the chat)</p>

#### [ Johan Commelin (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358320):
<p>Haha: <code>docs = logs</code> is now an <code>axiom</code>?</p>

#### [ Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358322):
<p>there was some discussion about this at some point</p>

#### [ Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358326):
<p>Jan 19th on gitter between Mario and Sebastian</p>

#### [ Kevin Buzzard (May 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358328):
<p>according to my logs</p>

#### [ Johan Commelin (May 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358370):
<p>Ok, gitter is from before my time</p>

#### [ Kevin Buzzard (May 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358372):
<p>I'll quote it</p>

#### [ Kevin Buzzard (May 10 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358377):
<div class="codehilite"><pre><span></span>To review, the problem is that the definition:

class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  extends has_scalar α β, add_comm_group β :=
...

leads to a search problem in which ring ?M1 is solved before module ?M1 β, which leads to a loop when there is an instance like [ring A] [ring B] : ring (A x B)
I would like to make lean search for module ?M1 β only, obtaining α and the ring instance by unification
Johannes suggested using {out_param $ ring α} instead of [out_param $ ring α], but then it doesn&#39;t work as a typeclass, and all the multiplications etc in the theorem statements break
A possible solution is to skip out_param typeclass search problems until after all the others are solved

***

So the real issue is: You want the elaborator to handle applying a function {A B} [ring A] [module A B] (x : B) : ..., yes...?
Mario Carneiro
@digama0
Jan 19 10:10
yes
Sebastian Ullrich
@Kha
Jan 19 10:10
Where you want it to solve the second instance first, which fixes A and the first instance
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358390):
<p>Every now and again stuff like this happens and I become convinced that type class inference is too stupid to handle non-trivial maths stuff</p>

#### [ Kevin Buzzard (May 10 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358436):
<p>There is this diamond catastrophe, today we learn that it doesn't work for things defeq to stuff that works etc etc</p>

#### [ Kevin Buzzard (May 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358441):
<p>It is extremely delicate to get right</p>

#### [ Johan Commelin (May 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358442):
<p>Yeah, I see that (-;</p>

#### [ Johan Commelin (May 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358445):
<p>Anyway, lunch time over here... see you later!</p>

#### [ Kevin Buzzard (May 10 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358446):
<p>but on the plus side, every time I run into an explicit problem Mario has some workaround</p>

#### [ Kevin Buzzard (May 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358605):
<p>One instance for maps, one for equivs:</p>

#### [ Kevin Buzzard (May 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358606):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">Pi_lift</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">G</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
 <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">Pi_lift_map₁</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
<span class="k">show</span> <span class="n">H</span> <span class="n">i</span> <span class="o">((</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">))</span> <span class="bp">=</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">),</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">(</span><span class="n">add</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">))</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">Pi_congr_right</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)]</span>
<span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">add_group</span> <span class="o">(</span><span class="n">G</span> <span class="n">i</span><span class="o">)]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">,</span> <span class="n">F</span> <span class="n">i</span> <span class="err">≃</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">)]</span> <span class="o">:</span>
 <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">Pi_congr_right</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
 <span class="k">show</span> <span class="n">H</span> <span class="n">i</span> <span class="o">((</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">))</span> <span class="bp">=</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">a</span> <span class="n">i</span><span class="o">)</span> <span class="bp">+</span> <span class="n">H</span> <span class="n">i</span> <span class="o">(</span><span class="n">b</span> <span class="n">i</span><span class="o">),</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">(</span><span class="n">add</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">))</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (May 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358607):
<p>same proof</p>

#### [ Kevin Buzzard (May 10 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358608):
<p>unsurprising because equivs are maps</p>

#### [ Kevin Buzzard (May 10 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358658):
<p>[I'm in namespace is_add_group_hom]</p>

#### [ Kevin Buzzard (May 10 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358672):
<p>but apparently I need both instances</p>

#### [ Kevin Buzzard (May 10 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358778):
<p>I guess one thing I am unclear about is what is wrong with the following fix : I create a mathlib PR which adds the function <code>Pi_lift_map₁ H</code> which sends a product of maps to a map on the product and rewrites <code>equiv.Pi_congr_right</code> to use this function. I then delete my second instance and observe that type class inference should spot it. But Mario, I think, suggested that this would not work either.</p>

#### [ Kevin Buzzard (May 10 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358886):
<p>and oh wow I now have my type class inference working, my time-out was indeed caused by type class inference failing, it now doesn't fail, and I can feed my parameters into my functions :-) So finally my initial problem is solved in the best possible way!</p>

#### [ Kevin Buzzard (May 10 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126358942):
<p>I want to argue that this is all about transport of structure. I'm switching to the canonical thread.</p>

#### [ Mario Carneiro (May 10 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126359245):
<p>You don't need to reprove the theorem</p>

#### [ Kenny Lau (May 10 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126359246):
<p>why is everyone using "reprove" to mean "prove again" lol</p>

#### [ Mario Carneiro (May 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126359259):
<p>just define the <code>equiv.Pi_congr_right</code> instance to equal <code>Pi_lift</code></p>

#### [ Johan Commelin (May 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126359452):
<blockquote>
<p>and oh wow I now have my type class inference working, my time-out was indeed caused by type class inference failing, it now doesn't fail, and I can feed my parameters into my functions :-) So finally my initial problem is solved in the best possible way!</p>
</blockquote>
<p>Does it also solve your <code>max_depth</code> problem?</p>

#### [ Kevin Buzzard (May 10 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can%20I%20fix%20this%20deterministic%20timeout%3F/near/126365201):
<p>unfortunately not, but I don't know what other terrible type class sins I have committed.</p>


{% endraw %}
