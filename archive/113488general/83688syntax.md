---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83688syntax.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [syntax](https://leanprover-community.github.io/archive/113488general/83688syntax.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jun 04 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544480):
<p>Fun fact: <code>notation</code> applies even in <code>namespace</code> commands, so if you write <code>notation `foo` := bar</code> and then <code>namespace foo</code> it means <code>namespace bar</code></p>

#### [ Simon Hudon (Jun 04 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544555):
<p>Cool! :)</p>

#### [ Simon Hudon (Jun 04 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544571):
<p>I don't know if that's a good thing but I was properly surprised when I realized what you meant</p>

#### [ Reid Barton (Jun 04 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544624):
<p>If you don't want this to happen (like I didn't) then you can write <code>namespace «foo»</code></p>

#### [ Simon Hudon (Jun 04 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544649):
<p>Curiously enough, it also works on binders: <code>∀ foo, f foo</code> actually means <code>∀ bar, f bar</code> which is inconvenient when the notation is a short hand for an expression, not an identifier</p>

#### [ Simon Hudon (Jun 04 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544653):
<p>Thanks for the fix</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544833):
<p>o.O</p>

#### [ Simon Hudon (Jun 04 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544900):
<p>I take it that's unintended behavior?</p>

#### [ Reid Barton (Jun 04 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127544969):
<p>(I was actually using <code>local notation</code>, in case that matters)</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545111):
<p>I get "identifier expected" in both cases</p>
<div class="codehilite"><pre><span></span>constants foo bar : Type
local notation `foo` := bar
#check ∀ foo, foo
namespace foo
</pre></div>

#### [ Reid Barton (Jun 04 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545171):
<p>Oh, I might have jumped to conclusions.<br>
What actually happened was that I was inside <code>namespace foo</code> and then I defined <code>foo</code> as local notation for something, and then <code>end foo</code> stopped working.</p>

#### [ Reid Barton (Jun 04 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545183):
<p>with some error like "identifier expected"</p>

#### [ Simon Hudon (Jun 04 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545332):
<p>Yes, you're right. That's what happens for me too. Sorry about the confusion</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545397):
<p>I see. This will probably be fixed in Lean 4 automatically since we will be using a parser combinator without a scanner, so we can skip notations where we only want to parse identifiers.</p>

#### [ Simon Hudon (Jun 04 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545431):
<p>How is that going by the way?</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545680):
<p>Let's... say that we're transitioning from the planning phase to the implementation phase (parser, compiler, and other refactorings)</p>

#### [ Simon Hudon (Jun 04 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax/near/127545899):
<p>Exciting :D I can't wait to see where that will end up!</p>


{% endraw %}
