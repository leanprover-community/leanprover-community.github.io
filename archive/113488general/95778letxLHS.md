---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95778letxLHS.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [let x = LHS](https://leanprover-community.github.io/archive/113488general/95778letxLHS.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756807):
<p>As sometimes happens, my goal is currently <code>FPTB.res BU _ _ s = si i</code> and my proof that these two things are equal is going to involve showing that they're both the unique object with some property. I am in tactic mode. I need to hence feed both sides into a bunch of machinery (the proofs that each side has the property are quite different). The underscores are proofs. I want to write "now let x be the left hand side" just to make things easier to handle, but the proof terms are probably nightmares. I am hoping there's a cute one-liner which lets me do this, based on the fact that I sometimes use <code>to_lhs</code> in conv mode. But I don't think <code>to_lhs</code> exists in tactic mode.</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756812):
<p>does <code>let x := FPTB.res BU _ _ s</code> work?</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756868):
<p>Here's a cute one-liner: <code>show let x := _ in x = si i, intro x</code></p>

#### [ Andrew Ashworth (Apr 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756914):
<p>can you do the same sort of thing with generalize?</p>

#### [ Andrew Ashworth (Apr 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124756961):
<p>i don't have lean on this computer so i can't check myself</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757001):
<p>It's not a bad idea, but no, <code>generalize</code> does not introduce let binders, only regular variables</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757008):
<p>The best part about <code>generalize</code> with <code>let</code> is that it doesn't suffer the same problems with type incorrectness as <code>generalize</code> itself, since the replacement is definitional</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757409):
<blockquote>
<p>does <code>let x := FPTB.res BU _ _ s</code> work?</p>
</blockquote>
<p>It works in the sense that no error appears, but all of a sudden I have 4 goals not 1.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757449):
<blockquote>
<p>Here's a cute one-liner: <code>show let x := _ in x = si i, intro x</code></p>
</blockquote>
<p><code>show tactic failed</code></p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757454):
<p>and what if both sides had suppressed-proofs?</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757455):
<p>This is hardly a serious issue, I mean I could turn proofs on and just copy what it said I guess...</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757456):
<p>What order are the goals? <code>let x := FPTB.res BU _ _ s, show x = si i</code> should kill most of the auxiliary goals</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757495):
<p>you should be able to do this by unification, no need to copy down those proofs</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757498):
<p>does <code>change</code> give a better error message than <code>show</code> in the one-liner?</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757505):
<p>wooah one of my proofs is cool</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757506):
<p><code>sheaf_property._proof_6 U β Ui Hcover i</code></p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757507):
<blockquote>
<p>you should be able to do this by unification, no need to copy down those proofs</p>
</blockquote>
<p>I like your way of thinking</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757596):
<p>This seems to work in my mockup example:</p>
<div class="codehilite"><pre><span></span>example (LHS RHS : nat) : LHS = RHS :=
begin
  let x, show x = RHS,
end
</pre></div>

#### [ Kevin Buzzard (Apr 07 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757597):
<p><code>change let x := _ in x = si i</code> -&gt; <code> don't know how to synthesize placeholder [some term involving all the proofs = si i]</code></p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757642):
<p><code>let x := FPTB.res BU _ _ s, show x = si i</code> -- this is the answer</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757643):
<p>The whole definition of the <code>let</code> is optional since it is inferred by the <code>show</code></p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757644):
<p>Sorry so slow, one of my monitors just died, so it's like I'm back in 2015 with only one screen</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757650):
<p>I might steal one of the kids' monitors, they're all still in bed</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757690):
<p><code>let x := _, show x = si i</code> -- this is the best answer</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757691):
<p>but it's a hack because what if the RHS had also been full of implicit proofs?</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757692):
<p>but it'll do for now -- thanks :-)</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757693):
<p>I bet even <code>let x, show x =  _</code> works</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757698):
<p>Indeed it does.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757699):
<p><code>let x,</code></p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757700):
<p>wtf?</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757701):
<p>All parts of a <code>let</code> or <code>have</code> are optional</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757702):
<p>you can even just <code>have,</code></p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757741):
<p>It's the := being optional I didn't know about :-)</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757742):
<p>I'm sure you are familiar with omitting <code>:=</code> in a <code>have x : property,</code> tactic</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757743):
<p>I guess so</p>

#### [ Kevin Buzzard (Apr 07 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757750):
<p>thanks!</p>

#### [ Mario Carneiro (Apr 07 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757751):
<p>Note that this only works in tactic mode, in term mode it's not so flexible</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757790):
<p>I was tempted to go into conv mode and use to_lhs</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757794):
<p>but was scared that if I had to do anything at all in conv mode then I would fail</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757795):
<p>e.g. prove something</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757796):
<p>This way is a much better way.</p>

#### [ Mario Carneiro (Apr 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757797):
<p>Show is <em>super</em> useful, don't underestimate the power of unification with <code>_</code></p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757806):
<p>Yes, that was the insight.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757845):
<p>That I could use unification to fill in the holes.</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757846):
<p>I just wanted to copy them</p>

#### [ Sebastian Ullrich (Apr 07 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757847):
<p>Only thing missing is allowing metavariables instead of <code>_</code> that can be referenced afterwards :)</p>

#### [ Mario Carneiro (Apr 07 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757894):
<p>You can still achieve most of this with unification</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757898):
<p>Summary for casual readers: <code>let x, show x = _</code> works for me and answers the original question -- it lets <code>x</code> be the left hand side of a goal of the form <code>X = Y</code>. It looks powerful enough to work in great generality.</p>

#### [ Mario Carneiro (Apr 07 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757899):
<p>Do you know why my <code>show let</code> solution failed? Looks like the type checking complained too early</p>

#### [ Kevin Buzzard (Apr 07 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124757985):
<p>Hmm -- <code>change let x := _ in x = si i</code> actually gives <code> don't know how to synthesize placeholder; context = blah blah blah, ⊢ ?m_1</code></p>

#### [ Sebastian Ullrich (Apr 07 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124758074):
<p>I think <code>let</code> checking the value independent from the body is a feature</p>

#### [ Mario Carneiro (Apr 07 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124758124):
<p>fair enough - I forgot that <code>change</code> doesn't create metavariables but only unifies. <code>let x,</code> has the behavior I intended and also unifies properly in the <code>show</code> line, so I guess it's fine</p>

#### [ Chris Hughes (Apr 11 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124940592):
<blockquote>
<p>I bet even <code>let x, show x =  _</code> works</p>
</blockquote>
<p>Is there a version of this trick for term mode, when I want to rw something in a hypothesis and not my goal?</p>

#### [ Mario Carneiro (Apr 11 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124944250):
<p>You can rw in a hypothesis in term mode by using <code>eqn ▸ h</code> in place of <code>h</code> wherever it gets used. (You may need <code>eqn</code> or <code>eqn.symm</code> depending on orientation of the equation.)</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947124):
<p>This came up with me specifically because I could not use rw because I only wanted to rewrite a certain term on the LHS, and it showed up on both sides.</p>

#### [ Chris Hughes (Apr 11 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947190):
<p>conv!</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947296):
<p>Actually I am lying, I remember now, it was because there were suppressed proofs everywhere.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947332):
<p>Although in the unfolding carefully thread the issue is raised about what happens when conv mode doesn't have the tactics you want.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947352):
<p>Conversely, did you see the transitive trick?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947516):
<p>Maybe you can let <code>y := RHS</code>, then rewrite in the hypothesis to get <code>LHS = y</code> and then just rw on the hypothesis (<code>rw ... at H</code> works)</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947526):
<p>(or the triangle business)</p>

#### [ Patrick Massot (Apr 11 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20x%20%3D%20LHS/near/124947837):
<p>All this discussion is probably worth a new tips and tricks file in <code>mathlib/docs/extras/</code></p>


{% endraw %}
