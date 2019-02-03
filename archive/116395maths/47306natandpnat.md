---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/47306natandpnat.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [nat and pnat](https://leanprover-community.github.io/archive/116395maths/47306natandpnat.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168435):
<p>Should I not be using these functions:</p>

#### [ Kevin Buzzard (May 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168436):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">plus_to_nat</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="kn">definition</span> <span class="n">nat_to_plus</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span>

<span class="c1">-- example (n : ℕ+) : nat_to_plus (plus_to_nat n) = n := by simp -- fails</span>
</pre></div>

#### [ Kevin Buzzard (May 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168437):
<p>Not only are we no longer refl, we are not even simp apparently</p>

#### [ Kevin Buzzard (May 27 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168438):
<p>Is that because simp won't unfold my definition by default?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168444):
<p>I am trying to make working with pnat easier. Nobody like a subtype.</p>

#### [ Kevin Buzzard (May 27 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168445):
<p>But I really want it to be easy to work with</p>

#### [ Kevin Buzzard (May 27 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168492):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="kn">definition</span> <span class="n">plus_to_nat</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="kn">definition</span> <span class="n">nat_to_plus</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ+</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat_to_plus</span> <span class="o">(</span><span class="n">plus_to_nat</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="n">unfold</span> <span class="n">nat_to_plus</span> <span class="n">plus_to_nat</span><span class="o">,</span> <span class="c1">-- still need to do this</span>
<span class="n">simp</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>What am I doing wrong? Should those functions not have names and I am expected to always use coercion?</p>

#### [ Mario Carneiro (May 27 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168493):
<p>The functions have names</p>

#### [ Mario Carneiro (May 27 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168494):
<p>Have you looked at <code>pnat.lean</code>?</p>

#### [ Kevin Buzzard (May 27 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168854):
<p>I have</p>

#### [ Kevin Buzzard (May 27 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168860):
<p>Oh I see, you're saying don't make new names for old functions</p>

#### [ Kevin Buzzard (May 27 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168862):
<p>because the old ones will have been made better</p>

#### [ Mario Carneiro (May 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168873):
<p>By the way I'm revising pnat right now</p>

#### [ Mario Carneiro (May 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168877):
<p>to remove that funny coercion</p>

#### [ Kevin Buzzard (May 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168938):
<p>So am I supposed to refer to these functions as <code>coe_nat_pnat</code> and <code>coe_pnat_nat</code> if I ever talk about them?</p>

#### [ Kevin Buzzard (May 27 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168954):
<p>wait those aren't the functions</p>

#### [ Kevin Buzzard (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127168998):
<p><code>nat.to_pnat'</code> and <code>subtype.val</code> are the rather unsexy  names of the functions</p>

#### [ Kevin Buzzard (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169005):
<p>Is the idea behind coercion that I do not ever mention these names?</p>

#### [ Mario Carneiro (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169006):
<p>yes</p>

#### [ Mario Carneiro (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169012):
<p><code>nat.to_pnat'</code> is going to be used instead of the coercion</p>

#### [ Mario Carneiro (May 27 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169014):
<p>but the other coercion will stay</p>

#### [ Kevin Buzzard (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169016):
<p>and what happens when I end up with <code>↑↑↑↑↑n</code>?</p>

#### [ Mario Carneiro (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169024):
<p>what are those coercions?</p>

#### [ Kevin Buzzard (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169025):
<p>Oh -- you're removing the instance?</p>

#### [ Kevin Buzzard (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169029):
<p>the coercion from nat to pnat?</p>

#### [ Mario Carneiro (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169032):
<p>yes</p>

#### [ Kevin Buzzard (May 27 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169033):
<p>Oh great</p>

#### [ Kevin Buzzard (May 27 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169080):
<p>you will really break Reid's code which I'm trying to maintain :-)</p>

#### [ Kevin Buzzard (May 27 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169084):
<p>I can't help but think that this is good though</p>

#### [ Kevin Buzzard (May 27 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169093):
<p>So you'll replace it with a dependent coercion which typechecks but when it actually runs it will ask the type class resolution system for a proof that n &gt; 0?</p>

#### [ Kevin Buzzard (May 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169136):
<p>and then the coercion from pnat to nat to pnat will become refl</p>

#### [ Kevin Buzzard (May 27 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169140):
<p>or some other cool new system</p>

#### [ Kevin Buzzard (May 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169144):
<p>I don't know if the typeclass resolution system will be the right thing</p>

#### [ Kevin Buzzard (May 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169149):
<p>I want it to check the properties of all the pnats it can see :-)</p>

#### [ Kevin Buzzard (May 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169152):
<p>and then use known lemmas like a&gt;0 and b&gt;0 implies a+b&gt;0</p>

#### [ Kevin Buzzard (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169187):
<p>Can it work like that? That's how it works in a mathematician's head</p>

#### [ Mario Carneiro (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169193):
<p>that is not at all what I'm suggesting :)</p>

#### [ Kevin Buzzard (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169194):
<p>thought not</p>

#### [ Mario Carneiro (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169195):
<p>I'm just removing the nat_pnat coercion, that's it</p>

#### [ Kevin Buzzard (May 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169196):
<p>less ambitious</p>

#### [ Mario Carneiro (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169204):
<p>there is a coercion that asks dec_trivial for the positivity proof</p>

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169205):
<p>What is stopping my idea above being built into Lean 7?</p>

#### [ Mario Carneiro (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169206):
<p>that's <code>nat.to_pnat</code></p>

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169207):
<p>Oh yeah I saw that</p>

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169208):
<p>you fill in the hole with a tactic</p>

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169209):
<p>I see</p>

#### [ Mario Carneiro (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169211):
<p>it could ask some other tactic, like simp</p>

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169213):
<p>so at some point you might want to get hold of a proof</p>

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169215):
<p>and you have loads of options</p>

#### [ Mario Carneiro (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169217):
<p>and then it would do some kind of a+b&gt;0 thing</p>

#### [ Kevin Buzzard (May 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169218):
<p>you could ask the type class dude</p>

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169258):
<p>or a tactic</p>

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169264):
<p>or you could pester the user</p>

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169267):
<p>But I'm a busy guy and I don't want to be pestered</p>

#### [ Mario Carneiro (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169268):
<p>But I hope that people provide a positivity proof of a+b just by adding a b : pnat</p>

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169272):
<p>Yes</p>

#### [ Kevin Buzzard (May 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169274):
<p>so in some sense my example was not good</p>

#### [ Mario Carneiro (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169276):
<p>as long as you stay in pnat world it's all good</p>

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169277):
<p>but how about "n^2 + 1 : pnat"</p>

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169280):
<p>if n is a nat</p>

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169283):
<p>A mathematician would be able to do that</p>

#### [ Mario Carneiro (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169284):
<p>that's <code>succ_pnat</code></p>

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169286):
<p>damn you</p>

#### [ Kevin Buzzard (May 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169288):
<p>What about (n + 4 + n : pnat)</p>

#### [ Mario Carneiro (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169326):
<p>but I think there is space for add_pnat_left : N -&gt; N+ -&gt; N+</p>

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169327):
<p>A mathematician could do that</p>

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169331):
<p>what about (4 + n : pnat)</p>

#### [ Mario Carneiro (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169333):
<p>that would cover your example</p>

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169334):
<p>I see</p>

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169335):
<p>But can we get the coercion to do it?</p>

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169337):
<p>Why is the coercion system part of type class resolution?</p>

#### [ Kevin Buzzard (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169339):
<p>could it be its own system?</p>

#### [ Mario Carneiro (May 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169341):
<p>no, the old coercion did that by cheating</p>

#### [ Mario Carneiro (May 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169346):
<p>you can still use <code>nat.to_pnat'</code> if you don't want to be bothered</p>

#### [ Kevin Buzzard (May 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169347):
<p>So how do I get (4 + n : pnat) to work?</p>

#### [ Mario Carneiro (May 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169349):
<p>(4+n).to_pnat'</p>

#### [ Kevin Buzzard (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169395):
<p>But that's bad</p>

#### [ Kevin Buzzard (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169398):
<p>because the value is now not defeq to 4+n</p>

#### [ Mario Carneiro (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169400):
<p>Really there's no need to use <code>to_pnat</code> unless you care that the nat component is defeq to the given arg</p>

#### [ Kevin Buzzard (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169401):
<p>`to_pnat' is not the function I had in mind</p>

#### [ Mario Carneiro (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169403):
<p>the point is that it works when the input made sense</p>

#### [ Kevin Buzzard (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169405):
<p>The function I had in mind sends <code>4 + n</code> to a pnat whose value is 4 + n</p>

#### [ Mario Carneiro (May 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169406):
<p>it's like nat.sub</p>

#### [ Kevin Buzzard (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169408):
<p>We are missing a function</p>

#### [ Kevin Buzzard (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169448):
<p>That's what causes the problem</p>

#### [ Kevin Buzzard (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169449):
<p>Definitional equality is so important to you guys</p>

#### [ Kevin Buzzard (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169451):
<p>and I don't want to throw it away here</p>

#### [ Mario Carneiro (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169453):
<p>that function exists too</p>

#### [ Mario Carneiro (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169454):
<p>that's <code>nat.to_pnat</code></p>

#### [ Mario Carneiro (May 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169457):
<p>that's why there's two versions</p>

#### [ Mario Carneiro (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169463):
<p>or just <code>pnat.mk</code></p>

#### [ Mario Carneiro (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169464):
<p>i.e. the constructor</p>

#### [ Kevin Buzzard (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169466):
<p><code>example (n : ℕ) : ℕ+ := nat.to_pnat (4 + n)</code></p>

#### [ Kevin Buzzard (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169467):
<div class="codehilite"><pre><span></span><span class="n">exact</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">type</span> <span class="n">mismatch</span><span class="o">,</span> <span class="n">given</span> <span class="n">expression</span> <span class="n">has</span> <span class="n">type</span>
  <span class="n">true</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">as_true</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="err">⊢</span> <span class="n">as_true</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="err">⊢</span> <span class="mi">4</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span>
</pre></div>

#### [ Mario Carneiro (May 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169471):
<p>but that one gives you a proof obligation</p>

#### [ Kevin Buzzard (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169472):
<p>But 4 + n &gt; 0 is true by schookid</p>

#### [ Mario Carneiro (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169510):
<p>and you'd better prove it</p>

#### [ Kevin Buzzard (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169513):
<p>It's true by schoolkid</p>

#### [ Mario Carneiro (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169514):
<p><code>nat.to_pnat (4 + n) (by schoolkid)</code></p>

#### [ Kevin Buzzard (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169516):
<p>I really want this schoolkid tactic</p>

#### [ Kevin Buzzard (May 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169517):
<p>Mathematicians want to pass over schoolkid stuff without any comment</p>

#### [ Kevin Buzzard (May 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169518):
<p>I see</p>

#### [ Mario Carneiro (May 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169524):
<p>the scope of things you could write there is unbounded</p>

#### [ Mario Carneiro (May 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169527):
<p>At some point you have to actually prove things</p>

#### [ Mario Carneiro (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169572):
<p>If you don't care to prove that statement, you can use <code>(4+n).to_pnat'</code></p>

#### [ Kevin Buzzard (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169574):
<p>rofl</p>

#### [ Mario Carneiro (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169575):
<p>unless it's an important definition you are going to unfold later, I doubt you will even notice the difference</p>

#### [ Kevin Buzzard (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169576):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">pnat</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">nat</span><span class="bp">.</span><span class="n">to_pnat</span> <span class="c1">-- chaos ensues</span>
</pre></div>

#### [ Kevin Buzzard (May 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169578):
<p>I think #check might have dealt with that one better</p>

#### [ Kevin Buzzard (May 27 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169586):
<p>Is that a bug?</p>

#### [ Kevin Buzzard (May 27 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169587):
<p><code>#check @nat.to_pnat</code> works fine</p>

#### [ Kevin Buzzard (May 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169627):
<p>you went for exact_dec_trivial??</p>

#### [ Kevin Buzzard (May 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169628):
<p>Not even simp?</p>

#### [ Kevin Buzzard (May 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169631):
<p><code>def to_pnat (n : ℕ) (h : n &gt; 0 . tactic.exact_dec_trivial) : ℕ+ := ⟨n, h⟩</code></p>

#### [ Mario Carneiro (May 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169632):
<p>Those are incomparable tactics</p>

#### [ Kevin Buzzard (May 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169634):
<p>I think you should use sledgehammer</p>

#### [ Kevin Buzzard (May 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169639):
<p>We want this coercion to <em>work</em>!</p>

#### [ Kevin Buzzard (May 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169644):
<p><code>to_pnat</code> : 3/10. Must try harder to coerce.</p>

#### [ Mario Carneiro (May 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169645):
<p>this is a basic function, it's not my job to select my favorite finishing tactic and introduce dependencies early in the development</p>

#### [ Kevin Buzzard (May 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169689):
<p>Dependencies?!</p>

#### [ Kevin Buzzard (May 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169692):
<p>We want it to <em>work</em>!</p>

#### [ Kevin Buzzard (May 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169695):
<p>So in fact you are suggesting that I should write "mathematicians mode"</p>

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169700):
<p>where we put the coercion back but we use by schoolkid</p>

#### [ Mario Carneiro (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169703):
<p>The thing about auto params is that they can't be changed later</p>

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169704):
<p>right</p>

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169706):
<p>I am seriously suggesting a "mathematicians overlay"</p>

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169707):
<p>I was thinking about this earlier when chatting to Kenny and Chris</p>

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169708):
<p>So there's a coercion from nat to pnat</p>

#### [ Kevin Buzzard (May 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169709):
<p>(although it might not last long)</p>

#### [ Kevin Buzzard (May 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169748):
<p>and so of course my first question is "what the hell are you going to do with zero"</p>

#### [ Kevin Buzzard (May 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169749):
<p>because of course you can use nat.rec to define it, and succ n goes to succ n together with the proof that succ n &gt; 0</p>

#### [ Kevin Buzzard (May 27 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169752):
<p>and 0 goes to...this is just stupid</p>

#### [ Kevin Buzzard (May 27 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169755):
<p>So I think you should send 0 to 37</p>

#### [ Kenny Lau (May 27 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169756):
<p><code>nat -&gt; option pnat</code> problem solved</p>

#### [ Kevin Buzzard (May 27 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169757):
<p>I think that that's a much better instance for the coercion because I think it better represents what is happening</p>

#### [ Kevin Buzzard (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169797):
<p>At the places it was supposed to be defined, it does what it is supposed to do</p>

#### [ Kevin Buzzard (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169800):
<p>and it sends everything else to 37</p>

#### [ Mario Carneiro (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169803):
<p>That's a weird option for a <em>coercion</em></p>

#### [ Kevin Buzzard (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169807):
<p>I don't see why it's any weirder than 1</p>

#### [ Mario Carneiro (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169808):
<p>It's not even making a pnat?</p>

#### [ Andrew Ashworth (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169809):
<p>how often do you move between nat and pnat? I feel like most people, once working with pnats, will continue to deal only in pnats</p>

#### [ Kevin Buzzard (May 27 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169812):
<p>Oh sorry</p>

#### [ Kevin Buzzard (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169814):
<p>I'll make it a pnat, sure</p>

#### [ Andrew Ashworth (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169819):
<p>in that case explicitly providing the proof obligation <code>n &gt; 0</code> is not such a burden</p>

#### [ Mario Carneiro (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169820):
<p>Of course pnat is inhabited, so we can use iget on that...</p>

#### [ Kevin Buzzard (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169821):
<p>but I just want to make the point that if you're coercing then you'd better realise that if you do this on 0 then you just did something stupid</p>

#### [ Mario Carneiro (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169822):
<p>OF COURSE</p>

#### [ Kevin Buzzard (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169824):
<p>But I think that if the coercion did that</p>

#### [ Kevin Buzzard (May 27 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169825):
<p>then I think it would force people to write better code</p>

#### [ Kevin Buzzard (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169828):
<p>because they wouldn't do the lazy junk theorem thing which you do</p>

#### [ Mario Carneiro (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169833):
<p>coercions don't have that luxury</p>

#### [ Kevin Buzzard (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169872):
<p>oh really</p>

#### [ Kenny Lau (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169873):
<div class="codehilite"><pre><span></span>def coe (n):
  assert (n &gt; 0)
  return [code]
</pre></div>

#### [ Mario Carneiro (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169874):
<p>They are functions A -&gt; B, where the user gets to pick A and B</p>

#### [ Kenny Lau (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169875):
<p>Python style</p>

#### [ Kenny Lau (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169878):
<p>we should have errors in Lean</p>

#### [ Mario Carneiro (May 27 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169882):
<p>That's called monadic programming</p>

#### [ Mario Carneiro (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169885):
<p>mathematicians don't want to deal with that</p>

#### [ Kevin Buzzard (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169889):
<p>so I'm sending nat to pnat, where everything positive goes to the correct thing (including defeq) and 0 goes to 37</p>

#### [ Mario Carneiro (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169891):
<p>sure</p>

#### [ Kevin Buzzard (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169892):
<p>because then <em>none</em> of the junk theorems would work</p>

#### [ Kenny Lau (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169893):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I think you want something like <code>nat.rec 37 id</code> where you replace <code>id</code> with the appropriate thing so it works <code>defeq</code></p>

#### [ Kevin Buzzard (May 27 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169894):
<p>and you would be forced to carry around the proof that n &gt; 0 properly</p>

#### [ Mario Carneiro (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169895):
<p>I don't think I prove any junk theorems about to_pnat'</p>

#### [ Kevin Buzzard (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169935):
<p>no but that's why you computer scientists tell us that functions should be total</p>

#### [ Mario Carneiro (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169936):
<p>but I think you are making an issue where none exists here</p>

#### [ Kevin Buzzard (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169938):
<p>I am suggesting that real.sqrt should send all negative reals to 37</p>

#### [ Mario Carneiro (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169939):
<p>There are options available, pick your favorite</p>

#### [ Kevin Buzzard (May 27 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169940):
<p>I think that 0 is the worst option</p>

#### [ Kenny Lau (May 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169946):
<blockquote>
<p>because then <em>none</em> of the junk theorems would work</p>
</blockquote>
<p>except the one which says <code>(0 : pnat) = 37</code> :P</p>

#### [ Kevin Buzzard (May 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169948):
<p>because it maximises the chance that the human prover doesn't spot their error</p>

#### [ Mario Carneiro (May 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169950):
<p>Don't worry, they will notice</p>

#### [ Mario Carneiro (May 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169952):
<p>you can't finish the proof if your model is wrong</p>

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169989):
<p>That one time you take a square root and you forget to check the argument was non-negative</p>

#### [ Mario Carneiro (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169992):
<p>then your theorem fails</p>

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169993):
<p>you will discover this the very next time you try and use the square root</p>

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169995):
<p>that's the point</p>

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169997):
<p>it fails earlier</p>

#### [ Mario Carneiro (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127169998):
<p>and you come here and ask about it</p>

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170001):
<p>which is a good thing</p>

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170002):
<p>not me asking :-)</p>

#### [ Kevin Buzzard (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170003):
<p>the failure</p>

#### [ Mario Carneiro (May 27 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170004):
<p>but composition is a really nice way to write expressions, and I don't want to lose it</p>

#### [ Kevin Buzzard (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170011):
<p>because the error says "x isn't 37" and I look at it and think "37? What the...Oh! I didn't check it wasn't negative!"</p>

#### [ Kenny Lau (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170012):
<p>lol 37</p>

#### [ Mario Carneiro (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170013):
<p>Obviously removing the coercion solves all these problems</p>

#### [ Kenny Lau (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170014):
<p>as if x&lt;0 is decidable</p>

#### [ Kevin Buzzard (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170015):
<p>It _has_ to be 37</p>

#### [ Kenny Lau (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170016):
<p>they won't ever give 37 to you</p>

#### [ Kenny Lau (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170017):
<p>x&lt;0 is not decidable</p>

#### [ Mario Carneiro (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170018):
<p>yes it is, it's false</p>

#### [ Kevin Buzzard (May 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170019):
<p>rofl you should have seen the original version of complex.lean</p>

#### [ Kevin Buzzard (May 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170048):
<p>I had to prove it was inhabited</p>

#### [ Kevin Buzzard (May 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170060):
<p>but I changed it before I made the PR</p>

#### [ Kevin Buzzard (May 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170061):
<p>You're right, I'd never have got away with it</p>

#### [ Mario Carneiro (May 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170069):
<p>When I removed the coercion, there was one place where it appeared in mathlib</p>

#### [ Mario Carneiro (May 27 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170119):
<p>I had to define a positive sequence that converged to zero, and used (n:ℕ+)⁻¹</p>

#### [ Mario Carneiro (May 27 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127170127):
<p>I think that's a good example of use, since it doesn't matter what the value is at zero, it's just a value</p>

#### [ Johan Commelin (May 27 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127172155):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'm a bit confused. With division by zero, or subtraction of nat's you say "just get over it, there is a footnote explaining some edge cases". Why isn't that enough here? Why don't you want to define <code>x / 0</code> as 37? (I actually prefer 57, since that is Grothendieck's prime...)</p>

#### [ Johan Commelin (May 27 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127172198):
<p>Or similarly <code>(3 : nat) - (5 : nat)</code>. That should also be <code>57</code>, I think...</p>

#### [ Kenny Lau (May 28 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127180246):
<p><a href="https://github.com/leanprover/mathlib/blob/master/data/pnat.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/pnat.lean">https://github.com/leanprover/mathlib/blob/master/data/pnat.lean</a></p>

#### [ Kenny Lau (May 28 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127180248):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> congratulations, it has been removed</p>

#### [ Kevin Buzzard (May 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat%20and%20pnat/near/127188139):
<p>Maybe one day it will come back with super powers</p>


{% endraw %}
