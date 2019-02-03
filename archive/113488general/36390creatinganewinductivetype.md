---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36390creatinganewinductivetype.html
---

## Stream: [general](index.html)
### Topic: [creating a new inductive type](36390creatinganewinductivetype.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 16 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123817890):
<p>What happens to the underlying system when a new inductive type <code>X</code> is created in Lean? A new axiom seems to appear, namely the eliminator for the type -- <code>X.rec</code>. Is that right? A new axiom appears? Is that the only new axiom that appears, and all of the other stuff I see when I type <code>#print prefix X</code> is always deducible from <code>X.rec</code>? I see that occasionally other stuff is used, like <code>and</code> or <code>eq.rec</code> or propext. Is it possible to list exactly which functions are used when creating these new facts? I am trying to get to the bottom of the difference between equality and definitional equality and I think one main difference is these random axioms that seem to appear every time to create a new type.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123817958):
<p>For example I think a+(b+c)=(a+b)+c for nats isn't a defeq, it's a theorem, and the reason seems to be that the proof uses induction on c, which uses nat.rec, which seems to be a way of proving that things are equal other than by definitional equality.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123817965):
<p>Have I got all this sort-of straight?</p>

#### [ Simon Hudon (Mar 16 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818103):
<p>Something seems to be missing</p>

#### [ Simon Hudon (Mar 16 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818155):
<p>I think <code>a + succ b = succ (a + b)</code> is a definitional equality despite relying on rec</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818821):
<p>Why does this rely on rec?</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818829):
<p>Isn't it just the definition of addition?</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818876):
<p>oh</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818886):
<p><code>#print nat.add._main</code> was rather more complex than I had expected</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818959):
<p>This is funny because the definition of <code>nat.add</code> in <code>core.lean</code> seems to be the standard one</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123818963):
<p>Oh it somehow relies on everything either being zero or a succ</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819077):
<p>Somehow this is OK. We are defining <code>nat.add</code> using what might be called the equation compiler, and internally Lean has to make sense of this definition. Hmm. Maybe what is going on is that I don't understand the definition of defeq that Lean uses in practice.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819159):
<p>The definition of <code>nat.add_main</code> looks like a mess to me, but <code>nat.add.equations._eqn_2</code> is the assertion that <code>a+succ b = succ(a+b)</code>. The proof isn't rfl though.</p>

#### [ Simon Hudon (Mar 17 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819164):
<p>If you use <code>nat.rec f (succ n)</code> it looks to me like Lean treats it as definitionally equal to <code>f n</code></p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819208):
<p>Is this just some weirdness with nat though, because it's such a primitive object?</p>

#### [ Simon Hudon (Mar 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819230):
<blockquote>
<p>The proof isn't rfl though.</p>
</blockquote>
<p>I don't think that equations get labelled as <code>rfl</code></p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819316):
<p>you'd think <code>rec</code> wouldn't be part of defeq but it's common in type theory settings to include delta reduction as part of it</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819329):
<p>I just rolled my own nat and nat.add and the same happens, it's not something specific to nat</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819396):
<p>Maybe this is iota reduction</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819400):
<p>Why did you guys choose such weird names for all these reductions?</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819467):
<p>most people regard alonzo church as a mathematician :)</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819516):
<p>OK so I am going to say that the reason a + succ b = succ (a+b) is a defeq despite relying on nat.rec is that the entire definition of add relies on nat.rec, and nonetheless they're defeq because of iota reduction. I knew what none of this stuff meant a few months ago though so if this isn't right then I hope someone lets me know.</p>

#### [ Simon Hudon (Mar 17 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819519):
<p>Funny ... and they regard Turing as a sort of computer scientist. They pretty much did the same things</p>

#### [ Simon Hudon (Mar 17 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819539):
<blockquote>
<p>you'd think <code>rec</code> wouldn't be part of defeq but it's common in type theory settings to include delta reduction as part of it</p>
</blockquote>
<p>Isn't delta reduction about definitions? If <code>rec</code> is a constant, it doesn't have a definition ... what am I missing?</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819601):
<p>According to Wikipedia Church was a mathematician and logician, so maybe he was being a logician at that point</p>

#### [ Simon Hudon (Mar 17 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819615):
<p>Haha! Your honor is safe then!</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819618):
<p>I am only going on the Lean reference manual, but delta reduction seems to say that if I define something without using matching then I can just substitute and I'm still defeq.</p>

#### [ Simon Hudon (Mar 17 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819623):
<p>Do mathematicians regard logicians in a similar way in which they regard philosophers?</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819624):
<p>Using matching is implicitly using what seems to be called iota reduction</p>

#### [ Simon Hudon (Mar 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819669):
<p>That's what I'm going with as well</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819674):
<p>No, philosophers aren't doing maths at all. Logicians are doing stuff which some people would say was maths but most maths departments don't have any</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819680):
<blockquote>
<blockquote>
<p>you'd think <code>rec</code> wouldn't be part of defeq but it's common in type theory settings to include delta reduction as part of it</p>
</blockquote>
<p>Isn't delta reduction about definitions? If <code>rec</code> is a constant, it doesn't have a definition ... what am I missing?</p>
</blockquote>
<p>i'd have to check. i make no guarantees on whatever i remember about the lambda calculus</p>

#### [ Simon Hudon (Mar 17 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819693):
<p>Let me compress the path for you: <a href="https://leanprover.github.io/reference/expressions.html#computation" target="_blank" title="https://leanprover.github.io/reference/expressions.html#computation">https://leanprover.github.io/reference/expressions.html#computation</a></p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819710):
<p>I was suggesting that you can't use delta reduction to prove a + succ b = succ (a + b) because the definition of + depends on how the inductive type inputs were born</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819773):
<p>so I am not sure + is a "defined constant".</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819781):
<p>However + does sound a lot like a function defined by recursion on an inductive type</p>

#### [ Reid Barton (Mar 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819796):
<p><code>+</code> is a defined constant, its definition is going to be something like <code>nat.rec [...]</code> or possibly <code>lam a b, nat.rec [...]</code></p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819797):
<p>and a + succ b does sound a lot like the function "a +" being applied to an element given by an explicit constructor</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819803):
<p>Oh!</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819850):
<p>Right, this also makes sense.</p>

#### [ Reid Barton (Mar 17 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819859):
<p>Then maybe (a) beta reduction(s) will apply to cancel the lambdas with the arguments, and then finally iota reduction will apply to <code>nat.rec</code>.</p>

#### [ Reid Barton (Mar 17 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819870):
<p>(At least, this is my understanding without actually checking the definitions.)</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819871):
<p>What is the point of iota-reduction then?</p>

#### [ Simon Hudon (Mar 17 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819872):
<p>That would be my thought as well. So the remaining question is: is iota reduction part of the def_eq definition?</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819875):
<p><code>ι-reduction : When a function defined by recursion on an inductive type is applied to an element given by an explicit constructor, the result ι-reduces to the specified function value</code></p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819877):
<p>from the reference manual</p>

#### [ Reid Barton (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819920):
<p>I think it's the rule that, after expanding the definition of <code>+</code> and then substituting the arguments, allows one to replace <code>nat.rec [...] (succ [...])</code> by something simpler.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819923):
<p>Oh so it only explicitly applies to the recursor?</p>

#### [ Simon Hudon (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819924):
<p>That sounds relevant doesn't it? I think here, "recursion" and "pattern matching" are synonymous</p>

#### [ Reid Barton (Mar 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819925):
<p>And I think that has been paraphrased into a higher-level form in the lean documentation</p>

#### [ Reid Barton (Mar 17 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819928):
<p>i.e. what Simon said.</p>

#### [ Reid Barton (Mar 17 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819938):
<p>(But I've never encountered the phrase "iota reduction" outside the context of lean, so I am guessing a bit.)</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819941):
<p>At the end of the day it all adds up to the same thing -- a + succ b = succ (a + b) is defeq despite relying on nat.rec</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123819999):
<p>Google led me to some pages about CIC:</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820002):
<p>" A specific conversion rule is associated to the inductive objects in the environment. We shall give later on (section 4.5.4) the precise rules but it just says that a destructor applied to an object built from a constructor behaves as expected. This reduction is called iota-reduction and is more precisely studied in [103, 117]."</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820012):
<p>This seems to say more explicitly that iota reduction is exactly how you prove that <code>blah.rec</code> is defeq to something else</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820089):
<p>On the other hand, the manual doesn't seem to give a definition of "what Lean uses for defeq" other than observing that (a) it's not the actual definition of defeq (proof: Lean's defeq isn't transitive) and (b) I think they're saying it's decidable (and actual defeq isn't).</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820142):
<p>So some of these reductions are from lambda calculus and iota reduction has just been tagged on afterwards as something coming from CIC it seems to me.</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820143):
<p>yes, lean and coq are CIC + extras</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820144):
<p>and we don't know what Lean is doing.</p>

#### [ Reid Barton (Mar 17 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820145):
<p>Yes--specifically <code>blah.rec</code> applied to a constructor.<br>
This will also go by names like "the elimination rule for the constructor"</p>

#### [ Simon Hudon (Mar 17 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820214):
<blockquote>
<p>Yes--specifically <code>blah.rec</code> applied to a constructor.<br>
This will also go by names like "the elimination rule for the constructor"</p>
</blockquote>
<p>I don't get what you're responding to</p>

#### [ Reid Barton (Mar 17 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820230):
<p>To </p>
<blockquote>
<p>iota reduction is exactly how you prove that blah.rec is defeq to something else</p>
</blockquote>

#### [ Andrew Ashworth (Mar 17 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820232):
<p>the extras that are added to CIC make defeq not transitive</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820296):
<p>and it has something something to do with how you can go from an inductively defined proposition to a Type</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820300):
<p>but we don't want to do without because classical reasoning is so convenient</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820304):
<p>so little bits are stuck on here and there and we sort of politely ignore it</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820344):
<p>is my terrible understanding of the base theory</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820351):
<p>if you go completely constructive you get HoTT and you may then hop on voevodsky's bandwagon</p>

#### [ Kevin Buzzard (Mar 17 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820406):
<blockquote>
<p>the extras that are added to CIC make defeq not transitive</p>
</blockquote>
<p>My reading of section 3.7 of the manual is that "true defeq" is transitive by definition, and "Lean defeq" is not.</p>

#### [ Andrew Ashworth (Mar 17 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820407):
<p>yup, that's my understanding as well</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820577):
<p>So implicit in the reference manual is a description of two terms which have different weak head normal forms but which can be proved equal using rfl.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820591):
<div class="codehilite"><pre><span></span>def R (x y : unit) := false
def accrec := @acc.rec unit R (λ_, unit) (λ _ a ih, ()) ()
example (h) : accrec h = accrec (acc.intro _ (λ y, acc.inv h)) := rfl
example (h) : accrec h = accrec (acc.intro _ (λ y, acc.inv h)) :=
begin
conv begin
to_rhs,
whnf,
end,
conv begin
to_lhs,
whnf,
end,
admit,
end
</pre></div>

#### [ Kevin Buzzard (Mar 17 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820594):
<p>rfl works, but if you reduce both terms to weak head normal form then you see they are different.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820760):
<p>So I am at a loss as to what Lean's definition of defeq is, but I understand it a lot better after this chat.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820768):
<p>Looking back at the proof of associativity of nat.add it's interesting to actually try and point at exactly what stops the argument being rfl.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820807):
<p>You prove it by induction on c; the zero case is rfl</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820815):
<p>and the inductive step is a bunch of rfls up to <code>a+(b+c)=(a+b)+c -&gt; nat.succ (a+(b+c))=nat.succ((a+b)+c)</code></p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820823):
<p>but the inductive hypothesis isn't rfl, it's an assumption because we're using nat.rec</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820867):
<p>and in particular we can't deduce associativity from this iota-reduction thing because even though c is either zero or a succ, in the succ case we need more than a case split, we need induction.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820872):
<p>It seems to me that it's this one point which stops associativity being defeq</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123820994):
<p>On the other hand you can chase this back to congr_arg and hence to eq.subst and eq.rec</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123821066):
<p>Somehow this is not relevant.</p>

#### [ Reid Barton (Mar 17 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123821246):
<p>More simply, you might consider the relationship between <code>(p.1, p.2)</code> and <code>p</code></p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822140):
<p>Also the coq page I was looking at seems to be saying that iota reduction says that a definition by cases can be reduced to its value for a given constructor when applied to a term constructed using this constructor.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822158):
<p>This seems to be weaker than what it says in the Lean reference manual, which seems to imply that general definitions by recursion (like the definition of nat.add) can be iota-reduced.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822746):
<p>So looking at what the manual says about inductive types, it seems that the answer to my original question is that what is added is the type, the constructors, and the recursor, and then everything else is worked out from this. And it also seems to say that iota reduction is fine for eliminating <code>X.rec</code>.</p>

#### [ Kevin Buzzard (Mar 17 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822757):
<p>For example I think <code>(a,b).1=a</code> is rfl</p>

#### [ Kevin Buzzard (Mar 17 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822798):
<p>but is <span class="user-mention" data-user-id="110032">@Reid Barton</span> suggesting that <code>p=(p.1,p.2)</code> is not? It doesn't seem to be.</p>

#### [ Reid Barton (Mar 17 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822800):
<p>Yes and yes (the latter is not definitionally equal)</p>

#### [ Kevin Buzzard (Mar 17 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822801):
<p>Do you know Lean's definition of definitionally equal?</p>

#### [ Reid Barton (Mar 17 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123822807):
<p>Not really, no.</p>

#### [ Reid Barton (Mar 17 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123823460):
<p>I just have some bits of type theory knowledge cobbled together from various sources.</p>

#### [ Mario Carneiro (Mar 17 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123825965):
<p>Aah, you really should see this paper I'm working on</p>

#### [ Mario Carneiro (Mar 17 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating%20a%20new%20inductive%20type/near/123825973):
<p>I basically lay all of this out in precise (too precise, probably) detail</p>


{% endraw %}
