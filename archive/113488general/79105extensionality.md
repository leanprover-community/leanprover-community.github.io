---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79105extensionality.html
---

## Stream: [general](index.html)
### Topic: [extensionality](79105extensionality.html)

---


{% raw %}
#### [ Kenny Lau (May 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127167357):
<p>Now that we have the <code>ext</code> tactic, let's get started tagging every theorem with <code>@[extensionality]</code> :D</p>

#### [ Kevin Buzzard (May 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127168051):
<p>All of them?</p>

#### [ Mario Carneiro (May 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127168090):
<p>I'm not sure there are that many to add</p>

#### [ Kevin Buzzard (May 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127168094):
<p><code>unknown identifier 'ext'</code></p>

#### [ Kenny Lau (May 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171210):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> trust me, there is a <em>lot</em> to add</p>

#### [ Mario Carneiro (May 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171211):
<p>then PR them</p>

#### [ Mario Carneiro (May 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171213):
<p>do you have a nonexhaustive list?</p>

#### [ Kenny Lau (May 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171214):
<p>not really</p>

#### [ Kenny Lau (May 27 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171222):
<p>do you have a estimate of the number of files in mathlib</p>

#### [ Kenny Lau (May 27 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171224):
<p>or does <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> have some magic to count that</p>

#### [ Mario Carneiro (May 27 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171272):
<p>I mean, just name a few</p>

#### [ Kenny Lau (May 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171273):
<p>the Z[sqrt(d)] doesn't really have the ext lemma that I want</p>

#### [ Kenny Lau (May 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171279):
<p>sum, prod</p>

#### [ Kenny Lau (May 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171280):
<p>I can just name every class I know</p>

#### [ Mario Carneiro (May 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171296):
<p>"wrong" is a strong word</p>

#### [ Mario Carneiro (May 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171322):
<p>it's not suitable for the <code>ext</code> tactic</p>

#### [ Kenny Lau (May 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171325):
<p>my apologies</p>

#### [ Mario Carneiro (May 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171334):
<p>Actually it would be great if <code>ext</code> could handle the iff style</p>

#### [ Mario Carneiro (May 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127171336):
<p>because that's the form that <code>simp</code> likes</p>

#### [ Scott Morrison (Jun 04 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525559):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, what do you think of changing <code>ext</code> so that it fails if it doesn't apply at least one extensionality lemma?  (when given no identifiers)</p>

#### [ Scott Morrison (Jun 04 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525563):
<p>(This just follows the general principle that tactics should not "fail silently", as it's harder to manage flow control if they might.)</p>

#### [ Scott Morrison (Jun 04 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525567):
<p>(If it seems reasonable, I'm happy to fix it.)</p>

#### [ Simon Hudon (Jun 04 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525612):
<p>That makes sense. At the same time, that would differ from the behavior of <code>intros</code></p>

#### [ Simon Hudon (Jun 04 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525713):
<p>Basically, you'd like to know when you expect an extensionality lemma but that it's not found. Would it make sense to have a special syntax for that? We could do <code>ext+</code> for "apply extensionality once or more" and <code>ext*</code>for "zero or more times"</p>

#### [ Scott Morrison (Jun 04 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525714):
<p>My vote would be to change <code>intros</code> too, but it may be too late for that!</p>

#### [ Scott Morrison (Jun 04 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525728):
<p>Well --- is doing something zero or more times ever actually useful? If you're working interactively, you should just remove it, and if you're working programmatically, it's no hassle to handle a failure, and sometimes helpful to know whether or not progress was made.</p>

#### [ Simon Hudon (Jun 04 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525769):
<p>That's a good point</p>

#### [ Simon Hudon (Jun 04 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525778):
<p>I'm in</p>

#### [ Scott Morrison (Jun 04 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525827):
<p>Shall I do it?</p>

#### [ Simon Hudon (Jun 04 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525830):
<p>Yes please</p>

#### [ Scott Morrison (Jun 04 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/127525941):
<p><a href="https://github.com/leanprover/mathlib/pull/151" target="_blank" title="https://github.com/leanprover/mathlib/pull/151">https://github.com/leanprover/mathlib/pull/151</a></p>

#### [ Scott Morrison (Jun 15 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115186):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, there are lots of lemmas that seem to me natural to have <code>apply</code>d automatically by <code>ext</code>, e.g.:</p>

#### [ Scott Morrison (Jun 15 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115188):
<p><code>lemma pair.ext {α : Type u₁} {β : Type u₂} {X Y : α × β} (p1 : X.1 = Y.1) (p2 : X.2 = Y.2) : X = Y</code></p>

#### [ Scott Morrison (Jun 15 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115239):
<p>or even <code>lemma sigma.ext {α : Type u₁} (Z : α → Type u₂) (X Y : Σ a : α, Z a) (w1 : X.1 = Y.1) (w2 : @eq.rec_on _ X.1 _ _ w1 X.2 = Y.2) : X = Y</code></p>

#### [ Scott Morrison (Jun 15 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115251):
<p>This isn't possible at the moment: <code>ext</code> will happily apply one of these, but then choke because there's nothing to <code>intro</code>.</p>

#### [ Scott Morrison (Jun 15 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115254):
<p>What do you think of generalising a little more?</p>

#### [ Mario Carneiro (Jun 15 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115314):
<p>I thought <code>ext</code> does 0+ intros</p>

#### [ Scott Morrison (Jun 15 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115378):
<div class="codehilite"><pre><span></span>import tactic.interactive

universes u₁ u₂

@[extensionality] lemma pair.ext {α : Type u₁} {β : Type u₂} {X Y : α × β} (p1 : X.1 = Y.1) (p2 : X.2 = Y.2) : X = Y :=
begin
  induction X, induction Y, dsimp at *, rw p1, rw p2,
end

lemma P (X Y : ℕ × ℕ) : X = Y :=
begin
  ext,

end
</pre></div>

#### [ Scott Morrison (Jun 15 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128115379):
<p>The <code>ext</code> here does nothing, even though <code>apply pair.ext</code> succeeds.</p>

#### [ Simon Hudon (Jun 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128116141):
<p>Mario was suggesting we extend <code>ext</code> to support that kind behavior. I think that's doable. I think we'd only have to fix the <code>intro1</code> and change <code>&gt;&gt;</code> for <code>;</code></p>

#### [ Simon Hudon (Jun 15 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128116157):
<p>As you say, the intro is mandatory right now</p>

#### [ Simon Hudon (Jun 15 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128118149):
<p>I'll have a look</p>

#### [ Scott Morrison (Jun 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120340):
<p>Another direction to consider is the following:</p>
<div class="codehilite"><pre><span></span>meta def applicable_attribute : user_attribute := {
  name := `applicable,
  descr := &quot;A lemma that should be applied to a goal whenever possible.&quot;
}

run_cmd attribute.register `applicable_attribute

/- Try to apply one of the given lemmas, it succeeds if one of them succeeds. -/
meta def any_apply : list name → tactic name
| []      := failed
| (c::cs) := (mk_const c &gt;&gt;= apply &gt;&gt; pure c) &lt;|&gt; any_apply cs

meta def applicable : tactic name :=
do cs ← attribute.get_instances `applicable,
   (any_apply cs) &lt;|&gt; fail &quot;no @[applicable] lemmas could be applied&quot;
</pre></div>

#### [ Scott Morrison (Jun 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120349):
<p>I use this pretty widely: it's for marking lemmas which are so useful that you know they are meant to be applied whenever possible.</p>

#### [ Scott Morrison (Jun 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120358):
<p>(<code>subsingleton.elim</code> is an example)</p>

#### [ Scott Morrison (Jun 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120370):
<p>I guess there's no reason this can't just coexist with <code>ext</code>, but if you see some reason to try to combine them I'd be interested.</p>

#### [ Simon Hudon (Jun 15 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120736):
<p>That's interesting. I think I would like to preserve <code>ext</code> because it has such a precise meaning but it might be useful to mark all extensionality lemmas as applicable. Is there a way to make one attribute subsume the other?</p>

#### [ Scott Morrison (Jun 15 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120773):
<p>For me it's not really important that one subsumes the other: my intention is just that the default list of tactics for <code>tidy</code> tries <code>applicable</code> first, and then tries <code>ext</code>.</p>

#### [ Scott Morrison (Jun 15 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120833):
<p>(I've also got a tactic <code>semiapplicable</code>, which tries applying lemmas marked <code>semiapplicable</code>, only succeeding if it can fulfill any remaining parameters by current hypotheses. That one desperately needs a better name. :-)</p>

#### [ Scott Morrison (Jun 15 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120854):
<p>(I've been curious if a case will come up where it's valuable to try applying a <code>semiapplicable</code>, and then using <code>solve_by_elim</code> to fulfill remaining arguments, but I haven't run into this in the wild.)</p>

#### [ Mario Carneiro (Jun 15 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120917):
<p>extensionality lemmas are definitely not applicable</p>

#### [ Mario Carneiro (Jun 15 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120932):
<p>otherwise you would end up unfolding all your equalities on structures</p>

#### [ Simon Hudon (Jun 15 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120935):
<blockquote>
<p>(I've also got a tactic <code>semiapplicable</code>, which tries applying lemmas marked <code>semiapplicable</code>, only succeeding if it can fulfill any remaining parameters by current hypotheses. That one desperately needs a better name. :-)</p>
</blockquote>
<p>Your message raises an important question: what are the grammatical rules for smileys and closing brackets?</p>

#### [ Mario Carneiro (Jun 15 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128120965):
<p>(I prefer an additional space with the smiley to keep it clearly delimited :) )</p>

#### [ Simon Hudon (Jun 15 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121022):
<p>( Me too, but to avoid any ambiguity, I think I might start endorsing "turning your head" (-: )</p>

#### [ Simon Hudon (Jun 15 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121115):
<p>On the subject of <code>semiapplicable</code>, I think there's a pattern of tactics for killing the current goal and we ought to have a more systematic naming convention.</p>

#### [ Simon Hudon (Jun 15 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121331):
<p>Back to <code>ext</code>, if you call it as <code>ext x y z</code> and somewhere, product extensionality is applicable, the number of identifiers provided does not reflect the number of rules applied. If it was the last rule, there's no way to just decide to not apply that level of extensionality ... except if we call <code>ext x y, ext1 z</code>. Are we ok with that?</p>

#### [ Mario Carneiro (Jun 15 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121398):
<p>How about an optional depth limit like in <code>congr'</code></p>

#### [ Simon Hudon (Jun 15 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121505):
<p>Yes, good idea! Do you think we could use one of <code>with</code>, <code>in</code> or <code>at</code> to specify that limit?</p>

#### [ Mario Carneiro (Jun 15 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121759):
<p>lol our stockpile of prepositions is quite limited</p>

#### [ Simon Hudon (Jun 15 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121760):
<p>How about <code>ext x y z</code> without limit and <code>ext 3 with x y z</code> if we use a limit?</p>

#### [ Simon Hudon (Jun 15 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121829):
<p>Otherwise we could also go with <code>ext x y z { depth := 3 }</code></p>

#### [ Mario Carneiro (Jun 15 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128121841):
<p>I'm not sure that will parse</p>

#### [ Simon Hudon (Jun 15 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128122303):
<p>Yeah, I'm not sure how to make that work either actually</p>

#### [ Simon Hudon (Jun 15 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128137567):
<p>Here's what I have now:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span><span class="o">)</span>  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">X</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">Y</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">Y</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">ext</span> <span class="mi">1</span> <span class="k">with</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">guard_target</span> <span class="n">X</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">Y</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">admit</span> <span class="o">},</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">Y</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">ext</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">guard_target</span> <span class="o">(</span><span class="n">X</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">=</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">fst</span><span class="o">,</span> <span class="n">admit</span><span class="o">,</span>
    <span class="n">guard_target</span> <span class="o">(</span><span class="n">X</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">snd</span> <span class="bp">=</span> <span class="o">(</span><span class="n">Y</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">snd</span><span class="o">,</span> <span class="n">admit</span><span class="o">,</span> <span class="o">},</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">Y</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">ext</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">guard_target</span> <span class="n">X</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">Y</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">admit</span> <span class="o">},</span>
  <span class="n">trivial</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>How do you guys like that?</p>

#### [ Mario Carneiro (Jun 15 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128137735):
<p>LGTM</p>

#### [ Simon Hudon (Jun 15 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128138565):
<p>:) Good, it's coming up</p>

#### [ Scott Morrison (Jun 16 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145906):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, and if I just call <code>ext</code> with no arguments?</p>

#### [ Simon Hudon (Jun 16 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145918):
<p>Then may God have our souls</p>

#### [ Simon Hudon (Jun 16 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145970):
<p><span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span> But seriously, same behavior as before except it now considers extensionality on products as well</p>

#### [ Simon Hudon (Jun 16 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145979):
<p>Also, I fixed extensionality on functions. The attribute was applied to the tactic, not the lemma</p>

#### [ Scott Morrison (Jun 16 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145991):
<p>Excellent. And if I wrote something <code>@[extensionality] lemma ulift.ext {α : Type u₁} (X Y : ulift.{u₂} α) (w : X.down = Y.down) : X = Y</code> then just plain <code>ext</code> would apply this?</p>

#### [ Simon Hudon (Jun 16 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145995):
<p>Exactly</p>

#### [ Scott Morrison (Jun 16 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128145997):
<p>Yay, thanks!</p>

#### [ Simon Hudon (Jun 16 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146094):
<p><span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span></p>

#### [ Scott Morrison (Jun 16 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146162):
<p>What should I do with my PR that made <code>ext</code> fail if there were no extensionality lemmas to apply?</p>

#### [ Simon Hudon (Jun 16 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146230):
<p>Sorry, I completely spaced out. I should just have added on top of that</p>

#### [ Scott Morrison (Jun 16 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146241):
<p>No problem. I could send a PR to your PR, I guess. :-)</p>

#### [ Simon Hudon (Jun 16 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146254):
<p>Haha! Yeah! Let's see what actually happens with mine when there's no rules to be applied</p>

#### [ Scott Morrison (Jun 16 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146297):
<p>Also --- your commit is failing: &lt;<a href="https://travis-ci.org/leanprover/mathlib/builds/392889071?utm_source=github_status&amp;utm_medium=notification" target="_blank" title="https://travis-ci.org/leanprover/mathlib/builds/392889071?utm_source=github_status&amp;utm_medium=notification">https://travis-ci.org/leanprover/mathlib/builds/392889071?utm_source=github_status&amp;utm_medium=notification</a>&gt;</p>

#### [ Simon Hudon (Jun 16 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146370):
<p>The main branch is broken so I'm going to wait for it to be fixed first</p>

#### [ Simon Hudon (Jun 16 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/128146596):
<p>Actually, I'll just make sure the trouble is not because of <code>ext</code> ...</p>

#### [ Simon Hudon (Oct 06 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135291851):
<p>What is people's opinion of making lemmas like this one <code>extensionality</code> lemmas?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">subset_ext</span> <span class="o">{</span><span class="n">s₁</span> <span class="n">s₂</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s₁</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s₂</span><span class="o">)</span> <span class="bp">→</span> <span class="n">s₁</span> <span class="err">⊆</span> <span class="n">s₂</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135291905):
<p>Is the idea that <code>ext</code> would do the work of <code>subset_iff</code> automatically?</p>

#### [ Simon Hudon (Oct 06 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292050):
<p>Yes but only in one direction</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292169):
<p>I'm not sure about this. it makes it less clear to me what <code>extensionality</code> means</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292176):
<p>is there a specific sense of what kind of lemmas you want to allow here?</p>

#### [ Scott Morrison (Oct 06 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292245):
<p>I guess the idea is "proving things by breaking objects into their constituent parts". I'm on the fence. At first I'm tempted, but I'm not sure where it ends...</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292316):
<p>This also sounds like "unfold definitions" though which is a bit dangerous</p>

#### [ Simon Hudon (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292332):
<p>I think Scott's definition would make sense. I'm also unsure. One reason is that I'm not clear if those lemmas could be chained</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292336):
<p>Actually there is a tactic in this area I very much want, which does "definitional unfolding" minus the definitional part</p>

#### [ Scott Morrison (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292339):
<p>What do you mean?</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292342):
<p>I currently use <code>simp</code> for this but it could be much more deterministic and hence faster</p>

#### [ Scott Morrison (Oct 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292383):
<p>This sounds like the sort of thing that I don't know that I want :-)</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292385):
<p>many functions are "activated" by some argument in which case they simplify to something else</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292386):
<p>i.e. recursive definitions</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292395):
<p>If we had a mechanism for emulating call-by-name evaluation, then we could use it as a replacement for simp in these cases</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292400):
<p><code>simp</code> is also a bit too aggressive in places, e.g. reassociating and commuting additions which can block "computation"</p>

#### [ Simon Hudon (Oct 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292444):
<p>You could probably build it by using the <code>simp</code> machinery with only definitional lemmas</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292451):
<p>But that's the thing, I don't care about them being literally definitional equalities</p>

#### [ Simon Hudon (Oct 06 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292453):
<p>How would you select the lemmas?</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292454):
<p>An attribute</p>

#### [ Simon Hudon (Oct 06 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292459):
<p>So you need a new simp lemma</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292500):
<p>For example a corecursor applied to a constructor in a coinductive type</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292502):
<p>it's "like" a recursive definition but not definitional because lean didn't decide to support it out of the box</p>

#### [ Simon Hudon (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292503):
<p>I was actually about to use that as a counter example</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292510):
<p>I don't want to be tied to whatever lean decided to support out of the box</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292517):
<p>it's not extensible</p>

#### [ Simon Hudon (Oct 06 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292520):
<p>Yeah, I agree. I created a <code>pseudo_eqn</code> attribute for my corecursive definitions just for that purpose</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292561):
<p>Coq has a <code>cbv</code> tactic that has exactly this behavior</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292565):
<p>I asked for it a long time ago and I think <code>simp</code> was the response</p>

#### [ Simon Hudon (Oct 06 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292569):
<p>The issue with <code>simp</code> though is that if you apply it for </p>
<div class="codehilite"><pre><span></span><span class="n">codef</span> <span class="n">diverge</span> <span class="o">:</span> <span class="n">computation</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">think</span> <span class="n">diverge</span>
</pre></div>


<p>"unfolding" will get ugly.</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292572):
<p>but <code>cbv</code> has a much more restricted evaluation behavior that allows you to almost completely skip the "search" part</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292576):
<p>corecursors are values</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292581):
<p>they only simplify when you tell them to explicitly</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292584):
<p>even Coq does this with their builtin coinductives</p>

#### [ Simon Hudon (Oct 06 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292626):
<p>But Coq leaves in the <code>cofix</code> construct and the match statement which kind of blocks the unfolding</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292627):
<p>I should look up the specifics there though</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292636):
<p>not sure I follow</p>

#### [ Simon Hudon (Oct 06 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292687):
<p>We can also do very little search though. One way is caching but we can also enforce a naming scheme that gives us only one candidate every time.</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292708):
<p>I was thinking that when you register a new rule, it analyzes the structure of the lemma to figure out what the active parameter is so that it can have a decision tree based dispatch</p>

#### [ Simon Hudon (Oct 06 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292754):
<blockquote>
<p>not sure I follow</p>
</blockquote>
<p>One of the first difference I noticed between Lean and Coq is that in Lean, unfolding often introduces a match statement because case analysis is a different process than unfolding. It is similar with corecursion</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292758):
<p>i.e. if you say <code>n + 0 = n</code> and <code>n + succ m = succ (n + m)</code>, then it knows that it starts from <code>has_add.add</code>, checks the <code>nat.has_add</code> argument, then goes to the last parameter and uses one rule if <code>0</code> and another if <code>succ _</code></p>

#### [ Mario Carneiro (Oct 06 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292764):
<p>so there is no big search</p>

#### [ Simon Hudon (Oct 06 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292768):
<p>Yes, I agree with that idea</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292919):
<p>I think that many uses of <code>simp</code> are actually uses of <code>cbv</code>/<code>cbn</code></p>

#### [ Simon Hudon (Oct 06 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135292980):
<p>I think you're right</p>

#### [ Simon Hudon (Oct 06 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135293175):
<p>About corecursive definitions, I'm thinking of using a bound on the number of times they can be unfolded</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/135293734):
<p>You could also trigger them "in reverse", i.e. a destructor applied to a corecursor reduces</p>

#### [ Simon Hudon (Nov 30 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148876325):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  <span class="user-mention" data-user-id="110087">@Scott Morrison</span> I noticed that <code>ext</code> has a weird behavior where with <code>f g : a -&gt; b -&gt; c |- f = g</code> if you call <code>ext i</code> it will apply extensionality twice instead of only once. I believe it is a mistake that I made. Is this a valuable behavior for you guys?</p>

#### [ Simon Hudon (Nov 30 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148876615):
<p>I'm thinking of fixing it</p>

#### [ Reid Barton (Nov 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148878481):
<p>What exactly are you planning on changing the behavior to?</p>

#### [ Reid Barton (Nov 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148878498):
<p>My understanding is that currently, <code>ext</code> just applies as many extensionality lemmas as possible</p>

#### [ Reid Barton (Nov 30 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148878616):
<p>Tricky cases: <code>ext</code> lemmas which don't consume any of the names, or which produce multiple goals with different numbers of variables (does <code>ext</code> support this currently?)</p>

#### [ Simon Hudon (Nov 30 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148879897):
<p>About the tricky case: for the multiple goals scenario, it is currently broken and I'm going to fix that so that ext x y, when it produces multiple goals, will use the same list (x, y) in each goal.</p>

#### [ Simon Hudon (Nov 30 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880086):
<p>Currently, when <code>ext x</code> encounters an extensionality rule which does not consume names, it just keeps going until it can't anymore. For instance, with <code>f g : a -&gt; (b x c) |- f = g</code>, <code>ext x</code> will introduce <code>x</code> and use extensionality on pairs. I'd like to change that so that <code>ext x</code> only uses functional extensionality and <code>ext x _</code> will allow the pair extensionality to be used.</p>

#### [ Reid Barton (Nov 30 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880091):
<p>I guess the main thing is that currently <code>ext x</code> with an ext lemma that takes 1 name followed by an ext lemma that takes 0 names applies both, and that should not change</p>

#### [ Simon Hudon (Nov 30 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880114):
<p>Really? Why not?</p>

#### [ Reid Barton (Nov 30 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880135):
<p>Because there are like 1000 uses of <code>ext</code> already</p>

#### [ Reid Barton (Nov 30 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880150):
<p>and you can use <code>ext1</code> to apply one lemma</p>

#### [ Simon Hudon (Nov 30 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880156):
<p>In mathlib or other projects too? I can fix mathlib, no worries.</p>

#### [ Reid Barton (Nov 30 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880157):
<p>so IMO the current behavior makes sense in that case</p>

#### [ Simon Hudon (Nov 30 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148880236):
<p>The thing is that, when you want to use three extensionality lemmas and provide variable names for them but that a fourth is possible, you have to limit using numbers. I'd like to avoid that.</p>

#### [ Simon Hudon (Nov 30 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148881908):
<p>Here is what I did: <a href="https://github.com/leanprover/mathlib/pull/506" target="_blank" title="https://github.com/leanprover/mathlib/pull/506">https://github.com/leanprover/mathlib/pull/506</a></p>

#### [ Reid Barton (Nov 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148884473):
<p>Why not just add some new syntax for this other behavior that you want?</p>

#### [ Reid Barton (Nov 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148884498):
<p>I don't see how it can be worth changing the default behavior, which is easy to understand and probably what you want most of the time</p>

#### [ Reid Barton (Nov 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148884615):
<p>I didn't realize the syntax with <code>: n</code> existed. I'm not sure whether I've ever wanted it. I have used <code>ext1</code> to apply one extensionality lemma and not a second, but I don't know whether I've wanted to apply specifically 2 or more</p>

#### [ Mario Carneiro (Nov 30 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148891407):
<p>it's an upper bound not a lower bound</p>

#### [ Reid Barton (Nov 30 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892238):
<p>I meant "specifically apply a number N, where N &gt;= 2"</p>

#### [ Mario Carneiro (Nov 30 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892283):
<p>right, that's not what it does</p>

#### [ Mario Carneiro (Nov 30 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892294):
<p>it applies extensionality <em>up to</em> N times</p>

#### [ Reid Barton (Nov 30 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892399):
<p>Well I would only use it when I didn't want to apply more, right?</p>

#### [ Reid Barton (Nov 30 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148892405):
<p>It might as well be an exact number</p>

#### [ Simon Hudon (Nov 30 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893622):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Why do you think <code>ext x _</code> is a bad syntax? Having <code>ext x</code> apply extensionality even when you run out of names for the new variables is inconsistent with what <code>intros</code> does. And instead, you could be writing <code>ext x; ext</code></p>

#### [ Reid Barton (Nov 30 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893667):
<p>What is <code>ext x _</code> supposed to mean?</p>

#### [ Reid Barton (Nov 30 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893670):
<p>Anyways I don't think I said it was a bad syntax...?</p>

#### [ Reid Barton (Nov 30 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893719):
<p>Although I do possibly think it is one, depending on what it is supposed to mean...</p>

#### [ Reid Barton (Nov 30 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893770):
<p>What is bad is changing very basic and useful stuff unnecessarily</p>

#### [ Reid Barton (Nov 30 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893793):
<p>Also there's lots of stuff which takes a list of names and just makes up more if there aren't enough provided, like <code>cases</code></p>

#### [ Reid Barton (Nov 30 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148893850):
<p>So to me, the current behavior makes perfect sense</p>

#### [ Simon Hudon (Nov 30 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894062):
<p><code>ext x</code> would not use extensionality of product after functional extensionality because it runs out of names. <code>ext x _</code> would be to trigger extensionality of product by giving it a name it can throw out.</p>

#### [ Simon Hudon (Nov 30 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894153):
<p><code>ext</code> is more similar to <code>intros</code> than cases because, with cases, if you provide more names, it will not apply additional recursors.</p>

#### [ Reid Barton (Nov 30 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894263):
<p>That's pretty gross IMO</p>

#### [ Reid Barton (Nov 30 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894274):
<p>Also, your next problem will be how to apply one zero-argument extensionality lemma, when there is a second you could apply as well</p>

#### [ Reid Barton (Nov 30 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894288):
<p>I really don't understand why you want to make any change at all frankly</p>

#### [ Simon Hudon (Nov 30 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894290):
<p>We could make it more like <code>cases</code> (or actually <code>rcases</code>) by using syntax like <code>ext x ⟨ y, z ⟩</code> to apply extensionality (functional, then product, then functional) on <code>f g : a -&gt; (b -&gt; c x b -&gt; c) |- f = g</code></p>

#### [ Simon Hudon (Nov 30 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894363):
<blockquote>
<p>Also, your next problem will be how to apply one zero-argument extensionality lemma, when there is a second you could apply as well</p>
</blockquote>
<p>This is where I would need to resort to the <code>ext : n</code> syntax.</p>

#### [ Simon Hudon (Nov 30 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894477):
<blockquote>
<p>I really don't understand why you want to make any change at all frankly</p>
</blockquote>
<p>I think it looks ugly to have to write <code>ext x y z : 3</code> and it makes the meaning of <code>ext x y z</code> different from what you would assume. It doesn't mean apply extensionality three times. It means apply extensionality multiple times and the first three arguments should be named <code>x</code> <code>y</code> <code>z</code></p>

#### [ Reid Barton (Nov 30 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894511):
<p>How about making it mean "apply extensionality three times" then?</p>

#### [ Reid Barton (Nov 30 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894514):
<p>I've never used it and I didn't read the documentation carefully</p>

#### [ Reid Barton (Nov 30 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894526):
<p>Oh wait I misparsed</p>

#### [ Reid Barton (Nov 30 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894572):
<p>Why would someone think <code>ext x y z</code> means extensionality three times?</p>

#### [ Reid Barton (Nov 30 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894588):
<p>As you can probably tell, this whole conversation is very confusing to me</p>

#### [ Reid Barton (Nov 30 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894777):
<p>An extensionality lemma for a relation would consume two names, so the number of names would never be related to the number of lemmas applied anyways</p>

#### [ Simon Hudon (Nov 30 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894794):
<p>That's true</p>

#### [ Simon Hudon (Nov 30 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148894895):
<p>I'd like an easier way of getting <code>ext</code> to stop applying lemmas than <code>ext : n</code></p>

#### [ Reid Barton (Nov 30 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148895366):
<p>Okay, so how about making <code>ext ... : 0</code> or something mean "apply as few lemmas as possible to use all the names"?</p>

#### [ Reid Barton (Nov 30 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148895460):
<p>Or it's not that difficult to just use <code>: n</code>, and changing the default behavior just means that some other, probably equally common case (apply as many lemmas as possible) now needs a special syntax instead</p>

#### [ Simon Hudon (Nov 30 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148895661):
<p>For "as many lemmas as possible", we could go with <code>ext* x y z</code></p>

#### [ Simon Hudon (Dec 01 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/148897567):
<p>Or we could also do <code>ext x y z *</code> or <code>ext x y z ... </code></p>

#### [ Reid Barton (Dec 02 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150725070):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>  I think the current default behavior (as many lemmas as possible) is better. For one thing, <code>ext</code> is often used with no names.</p>

#### [ Kevin Buzzard (Dec 02 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150725075):
<p>That's true -- I often just type <code>ext</code> and it does exactly what I want it to do.</p>

#### [ Reid Barton (Dec 02 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150725087):
<p>(And in situations where you really don't need the names, because the whole proof is something like <code>by ext; simp</code>.)</p>

#### [ Simon Hudon (Dec 02 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150733721):
<p>I'm not suggesting removing that behavior of <code>ext</code>. That's one reason I compare it with <code>intros</code>. Without names, go nuts, apply <code>ext</code> (or <code>intro</code> ) to your heart's content. But with <code>ext a b c</code>, like with <code>intros a b c</code>, you only go so far as the provided identifiers allow you.</p>

#### [ Simon Hudon (Dec 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/150733730):
<p>Are you guys only concerned about <code>ext</code> or do you also depend on the case where you provide a few names?</p>

#### [ Reid Barton (Dec 07 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/151129575):
<blockquote>
<p>Are you guys only concerned about <code>ext</code> or do you also depend on the case where you provide a few names?</p>
</blockquote>
<p>Honestly, I have no idea. I just use it, and it normally does what I want. I haven't been keeping score of how many times it applied a zero-argument extensionality lemma that I wanted or didn't want.</p>

#### [ Reid Barton (Dec 07 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/151129677):
<p>This is a standard problem with <em>changing</em> behavior--it's hard to evaluate how useful the old behavior is, because you just use it implicitly, as a matter of course.</p>

#### [ Reid Barton (Dec 07 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extensionality/near/151129776):
<p>In this case, it is hard to imagine any compelling argument for changing the default behavior anyways.</p>


{% endraw %}
