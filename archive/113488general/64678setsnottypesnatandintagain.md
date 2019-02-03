---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64678setsnottypesnatandintagain.html
---

## Stream: [general](index.html)
### Topic: [sets not types? nat and int again](64678setsnottypesnatandintagain.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 27 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134728630):
<p>John Harrison suggests a return to set theory in this talk : <a href="http://aitp-conference.org/2018/slides/JH.pdf" target="_blank" title="http://aitp-conference.org/2018/slides/JH.pdf">http://aitp-conference.org/2018/slides/JH.pdf</a> . Some of what he said rings very true. I told a bunch of beginners over the summer to go and formalise some number theory, but the constant battle with coercions from nat to int to rat made everything far harder than it should be. One thing which particularly should be stressed was that I found on more than one occasion that mathematicians were <em>really surprised</em> that <code>5 / 2 = 2</code> for nat or int. This is very counter to the approach of "normal" mathematical software (sage etc) which in 99% of cases just makes a rational even if the inputs were integers. </p>
<p>I have said this before but I really want the inclusions nat to int to rat to be easier for the beginner. However I have had no experience with formalising in set theory and am not at all convinced that it is the answer either. My proposal is to educate mathematicians so that they know that subtraction is not what they think it is on nat, and division is not what they think it is on nat or int, and then to have a tactic which literally eats a name representing something of type nat and introduces a new variable which is an int, adds the hypothesis that the int is &gt;= 0 into the context and changes every occurrence of the old nat to the new int. And a similar one from nat/int to rat, with the hypothesis that the denominator is 1. I want the tactic to do all the donkeywork. </p>
<p>This term I hope to get a whole bunch of data concerning what mathematicians actually find difficult when they try to learn dependent type theory by doing basic mathematics questions and I am already pretty sure that the (coercion from nat to int) fact that<code> \u(m^n)=\u m^\u n</code> is probably not <code>refl</code> and might not even typecheck (actually it might be refl, I can't check right now) and that <code>\u(m-n)=\u m-\u n</code> is not even true will be high up on the list.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134738904):
<p>OK so here is a proposal. We create a new type which is the kind of number which a mathematician is used to using. Let's just call it <code>number</code>. For the sake of argument let's say it's just defined by <code>number := rat</code>, although <code>real</code> and <code>complex</code> would also be fine. <code>number</code> inherits everything from <code>rat</code> and so it's a totally ordered distrib and all the other things. And for <code>x : number</code> there's a typeclass <code>actually_an_integer x</code> with fields an integer and a proof that the coercion of the integer to rat is <code>x</code>, and similarly <code>actually_a_natural x</code>. Now you can have definitions like <code>number.nat.prime (x : number) [actually_a_natural x] := ...</code>I am envisaging a lot of theorems and definitions of this form being deduced automatically. I don't know to what extent I am living in cloud cuckoo land here. However, even if we have to port theorems by hand, the resulting user experience will hopefully be a darn sight better than my users faced with goals mentioning <code>neg_succ_of_nat</code>. I'd be very interested in feedback.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134738938):
<p>Oh -- the answer to "why?" is "for pedagogical purposes".</p>

#### [ Johan Commelin (Sep 27 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134742043):
<p>I can't give any feed back on the actual proposal. I do suggest that those typeclasses be called <code>is_nat</code> and <code>is_int</code>, for brevity and analogy with existing names.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134742305):
<p>Maybe <code>maths_rat</code> is the name for these rationals, and <code>math_real</code> etc etc. Stuff like "sum of two nats is a nat" can be done by typeclass inference I would imagine.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134745401):
<p>and "difference of two <code>is_nat</code>s is an <code>is_nat</code>" would <em>not</em> be an instance, because the difference would be an int.</p>

#### [ Kevin Buzzard (Sep 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134745472):
<p>This would make a "number" class which is far more aligned with the kind of numbers which mathematicians are used to.</p>

#### [ Andreas Swerdlow (Sep 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134746770):
<p>Might it be worth creating a “pedagogical” mathlib for things like this?</p>

#### [ Andreas Swerdlow (Sep 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134747033):
<p>Then we could avoid clogging up mathlib with several versions of the same thing</p>

#### [ Sebastian Ullrich (Sep 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134754586):
<p>A simpler solution may be to just rename the CS operators that do not correspond to their mathematical counterparts, e.g. go with <code>//</code> for truncated division as in Python, and <code>∸</code> for truncated subtraction</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134754728):
<p>we could certainly have <code>is_nat</code> and <code>is_int</code> typeclasses; they are valid in any type where <code>{nat,int}.cast</code> makes sense</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134754777):
<p>the big question: are they data?</p>

#### [ Mario Carneiro (Sep 27 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134754907):
<p>You could conceivably use them to do integer or rational calculations on nondecidable types</p>

#### [ Kevin Buzzard (Sep 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756208):
<p>I am assuming you can get data from the prop in this case</p>

#### [ Kevin Buzzard (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756234):
<p>(the prop being "this rational is definitely an integer, but I'm not telling you which")</p>

#### [ Mario Carneiro (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756275):
<p>certainly not</p>

#### [ Kevin Buzzard (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756289):
<p>it's just the numerator, right?</p>

#### [ Kevin Buzzard (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756303):
<p>Oh I see you're not talking about <code>rat</code></p>

#### [ Mario Carneiro (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756307):
<p>from rat, sure, but not from more interesting types like real</p>

#### [ Kevin Buzzard (Sep 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756309):
<p>gotcha</p>

#### [ Mario Carneiro (Sep 27 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756347):
<p>of course the lean version of <code>number</code> is just <code>A</code> where <code>A</code> has some niceness typeclass</p>

#### [ Kevin Buzzard (Sep 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134756459):
<p>I don't think Sebastian's solution will solve all of the problems I saw over the summer, although it would be a good way of reminding the students that something fishy is going on. Of course all divisions should have a weird dot on them because division by zero is not what mathematicians expect either :-) (not that any of them should be dividing by zero anyway...)</p>

#### [ Reid Barton (Sep 27 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134757204):
<p>It would also make it a bit easier to look at a goal involving a bunch of coercions and a subtraction and understand where the subtraction is happening, at least to the extent that we would know whether or not it is "real" subtraction.</p>

#### [ Leonardo de Moura (Sep 27 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134757867):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> You may find this classical paper relevant: <a href="https://lamport.azurewebsites.net/pubs/lamport-types.pdf" target="_blank" title="https://lamport.azurewebsites.net/pubs/lamport-types.pdf">https://lamport.azurewebsites.net/pubs/lamport-types.pdf</a><br>
Leslie, one of the authors, is now at MSR, and he still believes specification languages should be untyped. He has a system called TLA: <a href="https://lamport.azurewebsites.net/tla/tla.html" target="_blank" title="https://lamport.azurewebsites.net/tla/tla.html">https://lamport.azurewebsites.net/tla/tla.html</a></p>

#### [ Johan Commelin (Sep 27 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134762284):
<p>Newbie question: would "specification languages" be suitable for formalising mathematics? Or are they meant for other applications? (I thought Lamport mostly focused on hardware verification, but I might be way off the mark...)</p>

#### [ Bryan Gin-ge Chen (Sep 27 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134762697):
<p>I am also a newbie, but there appear to be a a few "mathematical" examples <a href="https://github.com/tlaplus/Examples" target="_blank" title="https://github.com/tlaplus/Examples">in the TLA+ "Examples" repo</a>. Most of the examples seem to be algorithmic in nature, but there are a few puzzles and also <a href="https://github.com/tlaplus/Examples/tree/master/specifications/sums_even" target="_blank" title="https://github.com/tlaplus/Examples/tree/master/specifications/sums_even">"Two proofs of the fact that x+x is even, for any natural number x."</a>.</p>

#### [ Chris Hughes (Sep 27 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134767673):
<p>What's the difference between operators and functions, which means operators over all sets are consistent?</p>

#### [ Simon Hudon (Sep 28 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sets%20not%20types%3F%20nat%20and%20int%20again/near/134807973):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> You can quantify over functions even if they are unapplied: they are objects. Operators aren't objects. You can't have sets of operators and you can't quantify over them. A bit like universes in Lean, they are a different beast from the rest.</p>


{% endraw %}
