---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71749functiontopitype.html
---

## Stream: [general](index.html)
### Topic: [function to pi type](71749functiontopitype.html)

---


{% raw %}
#### [ Johan Commelin (May 23 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967340):
<p>Newbie alert! I can't find anything in PIL or TPIL on how to construct a function to a Pi type. If I have <code>Y : I \to Type</code> and <code>f : \Pi i, X \to Y i</code>, how do I turn this into <code>X \to (\Pi i, Y i)</code>?</p>

#### [ Johan Commelin (May 23 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967345):
<p>Context: I want to prove that the latter function is continuous if all the <code>f i</code> are continuous.</p>

#### [ Kevin Buzzard (May 23 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967387):
<p>use lambda?</p>

#### [ Johan Commelin (May 23 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967399):
<p>O.o... lol</p>

#### [ Kevin Buzzard (May 23 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967416):
<p><code>example (I : Type) (X : Type) (Y : I → Type) (f : Π (i : I), X → Y i) : X → (Π i, Y i) := λ x, λ i, f i x</code></p>

#### [ Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967457):
<p>Pi and structures are the only way of defining types</p>

#### [ Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967458):
<p>and then lambda and <code>{ }</code> are the only way of defining terms</p>

#### [ Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967459):
<p>or something</p>

#### [ Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967461):
<p>Pi and inductive types</p>

#### [ Kevin Buzzard (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967463):
<p>lambda and mk</p>

#### [ Kevin Buzzard (May 23 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967477):
<p>Can one say that lambda is some sort of a constructor for Pi types?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967478):
<p>Or is that abuse of language?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967530):
<p>Come to think of it, I am not sure I used a single inductive type in the whole scheme thing which wasn't a structure</p>

#### [ Sebastian Ullrich (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967541):
<p>Did you use <code>nat</code>? <span class="emoji emoji-1f61b" title="stuck out tongue">:stuck_out_tongue:</span></p>

#### [ Mario Carneiro (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967546):
<p>no, in the type theory literature that's common</p>

#### [ Kevin Buzzard (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967549):
<p>I mean</p>

#### [ Kevin Buzzard (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967560):
<p>actually I don't think I did use nat</p>

#### [ Mario Carneiro (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967561):
<p>lambda is the intro rule for pi, and application is the elim form</p>

#### [ Kevin Buzzard (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967567):
<p>but what I meant to say was that I rolled my own structures many times</p>

#### [ Kevin Buzzard (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967572):
<p>but they were all structures</p>

#### [ Kevin Buzzard (May 23 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967576):
<p>Sebastian's comment is interesting</p>

#### [ Mario Carneiro (May 23 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967618):
<p>There are tons of interesting inductive types beyond nat</p>

#### [ Kevin Buzzard (May 23 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967624):
<p>because how can a mathematician be doing anything if they're not using the basic math type, namely nat</p>

#### [ Mario Carneiro (May 23 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967626):
<p>the primitive recursive functions are obviously defined inductively</p>

#### [ Kevin Buzzard (May 23 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967639):
<p>but I think this maybe shows some disconnect between what the CS people think maths is, and what the maths people think it is</p>

#### [ Kevin Buzzard (May 23 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967643):
<p>e.g. Mario saying "w00t I did some more Matiyesevich" and Patrick responding "when will you get back to math"</p>

#### [ Mario Carneiro (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967687):
<p>I'm mentioning that because it's fresh on my mind</p>

#### [ Patrick Massot (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967690):
<p>That answer was mostly a joke</p>

#### [ Mario Carneiro (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967691):
<p>your scheme stuff is a bit too category-theoretic so have good examples</p>

#### [ Patrick Massot (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967693):
<p>I understand that Mario think Matiyesevich is math</p>

#### [ Kevin Buzzard (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967694):
<p>My scheme stuff is central to what a mathematician thinks that mathematics is</p>

#### [ Mario Carneiro (May 23 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967696):
<p>unless you consider freely generated stuff to be inductive</p>

#### [ Kevin Buzzard (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967697):
<p>and Patrick and I know well that most people in our departments would not have a clue about the Matiyesevich stuff</p>

#### [ Mario Carneiro (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967701):
<p>it's obviously not all of math though</p>

#### [ Kevin Buzzard (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967707):
<p>"a bit too category-theoretic" -- this is a very weird thing to day</p>

#### [ Kevin Buzzard (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967710):
<p>Essentially nobody in my department is interested in categories</p>

#### [ Mario Carneiro (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967711):
<p>it helps to look at more "concrete" areas, actual constructions and not constraints</p>

#### [ Kevin Buzzard (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967712):
<p>but many are interested in schemes</p>

#### [ Mario Carneiro (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967714):
<p>constraints tend to be noninductive</p>

#### [ Kenny Lau (May 23 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967718):
<blockquote>
<p>Essentially nobody in my department is interested in categories</p>
</blockquote>
<p>johannes nicaise is</p>

#### [ Mario Carneiro (May 23 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967720):
<p>so not "definition of scheme" but "X is a scheme"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967771):
<p>Johannes knows what a category is, like most of us do</p>

#### [ Kevin Buzzard (May 23 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967777):
<p>but Johannes does not study them in their own right, like most of us don't</p>

#### [ Kevin Buzzard (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967780):
<p>For most of us it's just a language</p>

#### [ Patrick Massot (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967784):
<p>Today's milestone is of type "X is a scheme"</p>

#### [ Mario Carneiro (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967791):
<p>honestly I still have only the foggiest idea of what you guys actually do</p>

#### [ Kevin Buzzard (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967793):
<p>I know</p>

#### [ Mario Carneiro (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967796):
<p>I do all this math and you guys just say "oh that CS guy"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967799):
<p>doing that CS stuff</p>

#### [ Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967843):
<p>This is one of the big reasons why this stuff isn't more popular</p>

#### [ Patrick Massot (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967846):
<p>So let's gather at the end of August and discuss that</p>

#### [ Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967848):
<p>Mario, I honestly think that if we wrote the definition of a perfectoid space in Lean</p>

#### [ Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967850):
<p>then some mathematicians would go "wooah"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967854):
<p>and your honest opinion might be "it's just a definition"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967856):
<p>but it is an extremely fashionable definition</p>

#### [ Kevin Buzzard (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967859):
<p>and a very delicate one</p>

#### [ Mario Carneiro (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967868):
<p>I have no clue why I should care about perfectoid spaces, besides the societal stuff</p>

#### [ Kevin Buzzard (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967870):
<p>And people like me prove basic lemmas about perfectoid spaces</p>

#### [ Kevin Buzzard (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967872):
<p>and get them published in good journals</p>

#### [ Kevin Buzzard (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967883):
<p>If you want to get a post-doc</p>

#### [ Johan Commelin (May 23 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967884):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> That's a very long story... but people are interested in them because they help us make progress on the Langlands programme</p>

#### [ Kevin Buzzard (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967921):
<p>then you have to impress the right people</p>

#### [ Kevin Buzzard (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967931):
<p>but the right people in which discipline?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967933):
<p>And there is a big disconnect here</p>

#### [ Johan Commelin (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967935):
<p>And people are interested in Langlands because... well, he just won the Abel prize for his impact on maths...</p>

#### [ Mario Carneiro (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967938):
<p>I want to see it develop more inline with the history - starting concrete and tending towards abstraction as things get more complicated</p>

#### [ Johan Commelin (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967940):
<p>Langlands program pervades modern number theory and geometry</p>

#### [ Kevin Buzzard (May 23 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967942):
<p>The Langlands Philosophy is arguably one of the central problems in maths and definitely one of the central problems in number theory</p>

#### [ Johan Commelin (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967945):
<p>It places Fermat's Last Theorem in a bigger picture</p>

#### [ Mario Carneiro (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967951):
<p>So maybe we should start with fermat's last theorem</p>

#### [ Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967952):
<p>And you CS guys have made 0 progress with it</p>

#### [ Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967955):
<p>FLT is really old</p>

#### [ Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967957):
<p>it's all been done</p>

#### [ Mario Carneiro (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967958):
<p>not in lean</p>

#### [ Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967960):
<p>it would take a decade to formalise</p>

#### [ Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967963):
<p>by which time it would be even older</p>

#### [ Johan Commelin (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967968):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Yes, but to do FLT, you have to define a scheme</p>

#### [ Kevin Buzzard (May 23 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126967969):
<p>and <em>nobody would care</em></p>

#### [ Mario Carneiro (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968009):
<p>but then it would be motivated</p>

#### [ Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968010):
<p>Proof that nobody would care: I went around and asked a bunch of people if they would care</p>

#### [ Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968014):
<p>and they said no</p>

#### [ Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968018):
<p>_you_ would be motivated</p>

#### [ Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968019):
<p>no mathematician would care</p>

#### [ Mario Carneiro (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968024):
<p>I think everyone wants motivation</p>

#### [ Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968026):
<p>Defining a perfectoid space in Lean is 1000 times easier</p>

#### [ Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968029):
<p>and _some_ mathematicians would care</p>

#### [ Kevin Buzzard (May 23 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968033):
<p>I mean, a non-trivial percentage would notice</p>

#### [ Mario Carneiro (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968038):
<p>Even just setting up a foundation for FLT would be tremendously satisfying for me</p>

#### [ Johan Commelin (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968039):
<p>Well, if FLT is formalised, then certainly lots of other modern stuff will be easily formalisable</p>

#### [ Johan Commelin (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968044):
<p>So it still would be a major milestone</p>

#### [ Kevin Buzzard (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968046):
<p>because Peter Scholze is probably going to get a Fields Medal</p>

#### [ Kevin Buzzard (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968052):
<blockquote>
<p>Even just setting up a foundation for FLT would be tremendously satisfying for me</p>
</blockquote>
<p>Well then you need to start caring about schemes</p>

#### [ Mario Carneiro (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968053):
<p>I'm all about the library building, making impossible goals feasible</p>

#### [ Johan Commelin (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968055):
<blockquote>
<p>Even just setting up a foundation for FLT would be tremendously satisfying for me</p>
</blockquote>
<p>What do you mean with that?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968057):
<p>The reason FLT is impossible</p>

#### [ Johan Commelin (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968060):
<p>Formalising the statement of the modularity theorem?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968063):
<p>is because you say that Cauchy Integral Formula is hard</p>

#### [ Mario Carneiro (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968080):
<p>FLT is in a whole language of its own, let's get that theory</p>

#### [ Kevin Buzzard (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968104):
<p>But that is a drop in an ocean of analysis</p>

#### [ Kevin Buzzard (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968109):
<p>all of which needs to be done to prove the trace formula</p>

#### [ Kevin Buzzard (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968112):
<p>which in every known proof of FLT is an essential prerequisite</p>

#### [ Johan Commelin (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968113):
<blockquote>
<p>FLT is in a whole language of its own, let's get that theory</p>
</blockquote>
<p>What do you mean with that?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968118):
<p>Mario -- like Johan I don't understand what you're saying</p>

#### [ Mario Carneiro (May 23 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968119):
<p>I like to formalize "essential prerequisites"</p>

#### [ Johan Commelin (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968123):
<p>Statements or proofs?</p>

#### [ Mario Carneiro (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968131):
<p>both?</p>

#### [ Johan Commelin (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968133):
<p>Great</p>

#### [ Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968134):
<p>Well you can spend two years formalising Cauchy Integral Formula and then basic stuff about integration on complex manifolds</p>

#### [ Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968136):
<p>and no mathematician will care</p>

#### [ Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968140):
<p>and after all that</p>

#### [ Johan Commelin (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968141):
<p>Schemes are epsilon-th prerequisite for FLT</p>

#### [ Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968147):
<p>you will proudly be able to formalise the statement of the trace formula</p>

#### [ Kevin Buzzard (May 23 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968149):
<p>and no mathematician will care</p>

#### [ Kevin Buzzard (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968196):
<p>because we proved it in the 1960s for SL_2</p>

#### [ Kevin Buzzard (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968199):
<p>like the odd order theorem</p>

#### [ Kevin Buzzard (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968208):
<p>and that's what we need</p>

#### [ Kevin Buzzard (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968212):
<p>There is your major obstacle for proving FLT</p>

#### [ Mario Carneiro (May 23 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968215):
<p>and then you will have a demo where you show people how to work with basic calculus and it won't be a barrier anymore</p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968222):
<p>And then 10 years later we have a proof of a 35-year-old theorem</p>

#### [ Mario Carneiro (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968224):
<p>it's not about impressing people with the statements, it's about making regular stuff pain free</p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968227):
<p>and you have seen how this turns out</p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968228):
<p><em>No</em></p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968230):
<p>it is about impressing people</p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968232):
<p>because that's where the jobs are</p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968237):
<p>and that's where the money is</p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968240):
<p>that's where the funding is</p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968243):
<p>that's how you get promotions</p>

#### [ Mario Carneiro (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968247):
<p>It's not what they want, it's what they need</p>

#### [ Kevin Buzzard (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968248):
<p>that's how you get money to support your family</p>

#### [ Andrew Ashworth (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968250):
<p>i'm curious if MSR has any work on this; I know they want to prove certain properties of encryption protocols</p>

#### [ Mario Carneiro (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968293):
<p>so you have to split your effort between flashy stuff and foundations</p>

#### [ Kevin Buzzard (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968298):
<p>I absolutely agree that in a perfect world we should all just drop what we're doing and prove the trace formula and tell mathematicians to stop producing more maths</p>

#### [ Kevin Buzzard (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968301):
<p>but that won't happen</p>

#### [ Mario Carneiro (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968308):
<p>I don't think it need be so dichotomous</p>

#### [ Johan Commelin (May 23 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968309):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> FLT will never be formalised if it takes one of the leading number theorists of our time over 3 months to formalise the definition of the most basic gadget in the proof</p>

#### [ Kevin Buzzard (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968317):
<p>or even me</p>

#### [ Johan Commelin (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968320):
<p>Really, defining a scheme takes less then an hour in "Introduction to algebraic geometry"</p>

#### [ Mario Carneiro (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968322):
<p>Right, so I will formalize the most basic gadgets and then leading number theorists won't have to</p>

#### [ Mario Carneiro (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968329):
<p>or kevin</p>

#### [ Kevin Buzzard (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968332):
<p>Why not take a break from your formalizing basic gadgets</p>

#### [ Johan Commelin (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968335):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> They will get hopelessly stuck on whatever comes after the basics</p>

#### [ Kevin Buzzard (May 23 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968336):
<p>and formalize a fancy one with me</p>

#### [ Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968378):
<p>and let's see the reaction</p>

#### [ Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968382):
<p>Or</p>

#### [ Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968383):
<p>if that's too fancy</p>

#### [ Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968385):
<p>then formalize manifolds with Patrick</p>

#### [ Patrick Massot (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968386):
<p>Kevin did formalize the basic gadget. Now you have the opportunity to do it right, and I'm sure that would be immensely instructive</p>

#### [ Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968387):
<p>because at least that's an important object</p>

#### [ Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968390):
<p>(manifolds)</p>

#### [ Kevin Buzzard (May 23 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968394):
<p>and people in maths departments use them</p>

#### [ Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968402):
<p>as opposed to Diophantine sets</p>

#### [ Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968406):
<p>which are just some niche thing</p>

#### [ Mario Carneiro (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968409):
<p>which will get me publishing</p>

#### [ Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968412):
<p>in your CS world</p>

#### [ Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968413):
<p>That's the problem</p>

#### [ Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968415):
<p>we seem to live in two different worlds</p>

#### [ Mario Carneiro (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968418):
<p>well we've all got mouths to feed</p>

#### [ Kevin Buzzard (May 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968419):
<p>You need your papers</p>

#### [ Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968460):
<p>and if the CS guys like the Diophantine set stuff</p>

#### [ Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968464):
<p>than that's what they're going to get</p>

#### [ Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968467):
<p>but the problem with this approach</p>

#### [ Johan Commelin (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968469):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> You have incredible skills. But atm mathematicians are really unable to use Lean, (except for a couple weirdo nerds like Kevin, Patrick, Scott and me). We really hope that you will help us build the bridge that the regular mathematicians need.</p>

#### [ Patrick Massot (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968470):
<p>How is it possible that formalizing Diophantine sets could give you a paper but formalize schemes couldn't?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968472):
<p>is that the mathematicians will continue to not give a shit</p>

#### [ Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968476):
<p>Patrick, I was going to write something very short</p>

#### [ Mario Carneiro (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968479):
<p>I can't publish in a math journal, unless I stop formalizing</p>

#### [ Kevin Buzzard (May 23 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968480):
<p>but honestly let's face it</p>

#### [ Mario Carneiro (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968486):
<p>math journals don't care about that</p>

#### [ Kevin Buzzard (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968487):
<p>whatever would I do with a two page paper saying "I wrote down a trivial definition, it took three months, here are some of the interesting problems I ran into"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968488):
<p>for sure maths journals don't care</p>

#### [ Patrick Massot (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968490):
<p>Why not publishing about formalization of schemes in a CS journal?</p>

#### [ Kevin Buzzard (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968491):
<p>and from a CS point of view all I did was formalise a definition</p>

#### [ Mario Carneiro (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968493):
<p>CS journals care, but they also care about CS things</p>

#### [ Kevin Buzzard (May 23 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968495):
<p>I am in a privileged position that I can just do what I like</p>

#### [ Kevin Buzzard (May 23 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968535):
<p>so I did something I thought was important</p>

#### [ Johan Commelin (May 23 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968536):
<p>Right, so we need a new journal "Formalisations in Geometry and Number Theory"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968537):
<p>That can happen</p>

#### [ Kevin Buzzard (May 23 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968538):
<p>journals are not hard to start</p>

#### [ Patrick Massot (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968543):
<p>As I wrote earlier, I think the really interesting thing to write about would be the whole process starting with an optimistic mathematician knowing nothing about DTT and ending with a usable formalization</p>

#### [ Kevin Buzzard (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968548):
<p>That was the story I was going to write</p>

#### [ Kevin Buzzard (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968551):
<p>except I can't imagine it's usable yet</p>

#### [ Patrick Massot (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968553):
<p>Yes, because it's not done yet</p>

#### [ Kevin Buzzard (May 23 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968554):
<p>Mario -- I hope you understand that none of this is an implicit criticism of what you do</p>

#### [ Kevin Buzzard (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968596):
<p>it is general frustration</p>

#### [ Patrick Massot (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968597):
<p>It lacks the stage where Mario or Johannes enters the game seriously</p>

#### [ Kevin Buzzard (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968603):
<p>about the state of things</p>

#### [ Patrick Massot (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968613):
<p>It's not only frustration, it's also excitement about what could be</p>

#### [ Kevin Buzzard (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968617):
<p>that too</p>

#### [ Kevin Buzzard (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968618):
<p>but somehow the right people don't exist yet</p>

#### [ Patrick Massot (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968619):
<p>If you would accept to play this game</p>

#### [ Mario Carneiro (May 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968622):
<p>The thing is, the things I enjoy are useful to others, but not really publishable results for the most part</p>

#### [ Mario Carneiro (May 23 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968637):
<p>I just have to make sure to stay somewhat on task</p>

#### [ Patrick Massot (May 23 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968640):
<p>How did Assia got her job then? I think she always formalized math</p>

#### [ Mario Carneiro (May 23 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968646):
<p>I think she's my hero</p>

#### [ Johan Commelin (May 23 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968698):
<p>Well, and there is Tom Hales of course. He knows everything about FLT and about formalisation.</p>

#### [ Patrick Massot (May 23 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968702):
<p>Then why don't you start reading that scheme repository?</p>

#### [ Johan Commelin (May 23 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968703):
<p>Still he did not formalise any algebraic geometry or anything in the direction of Langlands yet</p>

#### [ Patrick Massot (May 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968746):
<p>I guess Hales knows too much, this prevents him from enjoying Kevin's optimism</p>

#### [ Patrick Massot (May 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968748):
<p>Naive optimism is a very important math skill</p>

#### [ Patrick Massot (May 23 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968758):
<p>I don't think I was ever able to prove anything without first hugely underestimating the difficulty</p>

#### [ Mario Carneiro (May 23 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968822):
<p>Also Johannes and I will be working at the university of Hanoi with Tom on a lean summer school</p>

#### [ Patrick Massot (May 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968829):
<p>I think your hero would write "Scheme theory done right in Lean"</p>

#### [ Mario Carneiro (May 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968832):
<p>As I understand it many of the folks involved in Flyspeck are there, so it should be interesting</p>

#### [ Patrick Massot (May 23 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126968887):
<p>I fear Hanoi is a bit too far for me</p>

#### [ Andrew Ashworth (May 23 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969103):
<p>ooh, Flyspeck looks interesting! So they proved the optimal packing of balls in 3d space</p>

#### [ Andrew Ashworth (May 23 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969117):
<p>Please don't pressure Mario too hard :) For his future career prospects, all the money in formal verification comes from the large software companies</p>

#### [ Patrick Massot (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969185):
<p>It's not 100% true</p>

#### [ Patrick Massot (May 23 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969194):
<p>Since Assia is a counter-example for instance</p>

#### [ Andrew Ashworth (May 23 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969264):
<p>I'm not aware of very many other mathematicians outside of Assia who get to work on computer formalized math... whereas, Intel, Amazon, Microsoft, Facebook etc. all have teams of people who do this. Not to mention the smaller companies like Galois and others who do contract work in the field</p>

#### [ Kevin Buzzard (May 23 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969378):
<p>I want to bring computer formalized maths to mathematics departments</p>

#### [ Kevin Buzzard (May 23 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969384):
<p>because I think mathematicians don't know what they're missing</p>

#### [ Kevin Buzzard (May 23 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969386):
<p>both in terms of it making their lives better</p>

#### [ Kevin Buzzard (May 23 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969387):
<p>and in terms of the fact that some of their arguments are incomplete and they need to be told</p>

#### [ Patrick Massot (May 23 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969392):
<p>I know what they are missing: a - b + b may or may not be equal to a</p>

#### [ Kevin Buzzard (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969434):
<p>They are not missing that</p>

#### [ Kevin Buzzard (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969439):
<p>that - sign is not a mathematician's minus</p>

#### [ Kevin Buzzard (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969440):
<p>I see it and I see "-^*"</p>

#### [ Patrick Massot (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969442):
<p>Formalized math in maths departments may be a dream too far away. But we only need two INRIA positions: one for Mario and one for Johannes</p>

#### [ Kevin Buzzard (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969443):
<p>with the footnote "this is a different minus, don't expect it to be sensible"</p>

#### [ Mario Carneiro (May 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969446):
<p>actually it's a dot over, not a star</p>

#### [ Andrew Ashworth (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969453):
<p>Not even a Field's medalist in Vovoedsky could get mathematicians interested in DTT...</p>

#### [ Johan Commelin (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969457):
<p>Because he didn't formalise any AG (= Algebraic Geometry)</p>

#### [ Johan Commelin (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969458):
<p>He completely changed fields</p>

#### [ Kevin Buzzard (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969462):
<p>In fact you could see this in his Cambridge talk</p>

#### [ Johan Commelin (May 23 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969463):
<p>I don't think he even formalised the definition of a scheme in all those years</p>

#### [ Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969510):
<p>He got interested in formal proof verification because he was worried about bugs in his proofs</p>

#### [ Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969516):
<p>but then he decided that DTT or whatever wasn't right for him</p>

#### [ Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969518):
<p>so he invented a new thing</p>

#### [ Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969519):
<p>with yet another bloody definition of =</p>

#### [ Mario Carneiro (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969520):
<p>When you do HoTT though, everything is "more" than what's written</p>

#### [ Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969522):
<p>and then all of a sudden there were lots of interesting questions</p>

#### [ Kevin Buzzard (May 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969524):
<p>and then oops</p>

#### [ Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969525):
<p>who cares about Bloch-Kato any more</p>

#### [ Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969530):
<p>and he explicitly said this in his Cambridge talk</p>

#### [ Mario Carneiro (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969531):
<p>and you get distracted by all the homotopy implications of your definition and never get around to the original goal</p>

#### [ Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969532):
<p>"So how is Bloch-Kato doing?"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969534):
<p>"Well, not very well"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969535):
<p>"I'm pretty sure it's right"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969536):
<p>"and nobody is working on that right now"</p>

#### [ Kevin Buzzard (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969538):
<p>exactly</p>

#### [ Mario Carneiro (May 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969541):
<p>formalizing a scheme in HoTT feels like the wrong application of a tool</p>

#### [ Mario Carneiro (May 23 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969584):
<p>because you have no interest in the HoTT stuff, it's just a classical definition</p>

#### [ Patrick Massot (May 23 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969586):
<p>Recently I heard someone claiming a proof of this Simpson conjecture that was missing in order to fix that broken Voevodsky paper that started it all</p>

#### [ Johan Commelin (May 23 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969588):
<p>True</p>

#### [ Patrick Massot (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969596):
<p><a href="https://ncatlab.org/nlab/show/Simpson%27s+conjecture" target="_blank" title="https://ncatlab.org/nlab/show/Simpson%27s+conjecture">https://ncatlab.org/nlab/show/Simpson%27s+conjecture</a></p>

#### [ Johan Commelin (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969597):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Unless HoTT helps you to turn <em>math</em>-trivial stuff into <em>formally</em>-trivial stuff.</p>

#### [ Mario Carneiro (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969602):
<p>I like lean because it's not trying to be "more" like this, it's exactly what you are trying to say</p>

#### [ Johan Commelin (May 23 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/function%20to%20pi%20type/near/126969603):
<p>I think Voevodsky thought very hard about transport of structure. And that led him to HoTT</p>


{% endraw %}
