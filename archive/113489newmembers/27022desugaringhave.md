---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/27022desugaringhave.html
---

## Stream: [new members](index.html)
### Topic: [desugaring have](27022desugaringhave.html)

---


{% raw %}
#### [ Olli (Sep 02 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226383):
<p><a href="https://gist.github.com/luxbock/f0c19afd8d88fef9c13814ba072b9eb5" target="_blank" title="https://gist.github.com/luxbock/f0c19afd8d88fef9c13814ba072b9eb5">https://gist.github.com/luxbock/f0c19afd8d88fef9c13814ba072b9eb5</a></p>
<p>Can anyone explain what I'm doing wrong? I tried adding parentheses in different places but couldn't make it work</p>

#### [ Etienne Laurin (Sep 02 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226658):
<p>I think you need to add parenthesis around <code>(and.right h)</code> and  <code>(and.left h)</code></p>

#### [ Reid Barton (Sep 02 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226707):
<p>In this case around and.left h</p>

#### [ Reid Barton (Sep 02 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226708):
<p>You need parentheses around the argument of a function. <code>f x y</code> means <code>(f x) y</code></p>

#### [ Olli (Sep 02 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133226719):
<p>thanks, yeah that did it</p>

#### [ Olli (Sep 04 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133333637):
<p><a href="https://gist.github.com/luxbock/0e19b04aaca49ccf18e5df060d2d3e8e" target="_blank" title="https://gist.github.com/luxbock/0e19b04aaca49ccf18e5df060d2d3e8e">https://gist.github.com/luxbock/0e19b04aaca49ccf18e5df060d2d3e8e</a></p>
<p>same as last time, except now I feel fairly confident that I should have got this right, but I don't understand why it's not able to infer the right types for the disjunction. I realize this is probably not how you'd ever write things, but nevertheless am I doing something wrong here?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133336029):
<p>I get a gazillion errors when I copy paste</p>

#### [ Kevin Buzzard (Sep 04 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133336459):
<p>but apart from that, as I'm sure you know, the problem is that <code>or.inl hq</code> doesn't have enough information to know it's a proof of <code>q or r</code>.</p>

#### [ Kevin Buzzard (Sep 04 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133336492):
<p>Here are two ways to fix it: for the first error, replace the offending line with <code>and.intro hp (@or.inl q r hq))</code> i.e. use the <code>@</code> trick and tell Lean the implicit variables yourself</p>

#### [ Kevin Buzzard (Sep 04 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133336556):
<p>For the second line, you could write <code>and.intro hp (or.inr hr : q ∨ r))</code> , i.e. tell Lean the type you want it to be.</p>

#### [ Olli (Sep 05 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133358915):
<p>thanks, that does indeed work.</p>
<p>The reason I find this confusing is because based on reading the tutorial, I thought that <code>have</code> would desugar as I wrote it. It should have all the same information compared writing it with <code>have</code>.</p>

#### [ Kevin Buzzard (Sep 05 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133360074):
<p>My non-expert guess as to what is going on is this. Lean sometimes doesn't have enough information to work out what the type of something is (e.g. when you type <code>or.inr hr</code>). When this happens it inserts a metavariable instead (e.g. <code>?m_1[hpr, _, _]</code>). You talk about desugaring, but I think the process which is behaving differently in the two cases is the elaboration process, when these metavariables get solved. Elaboration is a complicated thing and depends on a lot of stuff going on in the background, for example whether various terms are tagged <code>elab_simple</code> or <code>elab_as_eliminator</code> or whatever -- even changing the way you apply a function <code>f {a} b</code> from <code>f b</code> to <code>@f _ b</code> can (and often does) change the elaboration strategy. In short, I don't think this is about desugaring, it's about the complex elaboration process which goes on behind the scenes after that.</p>

#### [ Olli (Sep 05 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/desugaring%20have/near/133365624):
<p>yeah it was a good exercise to do, because I learned something from it</p>


{% endraw %}
