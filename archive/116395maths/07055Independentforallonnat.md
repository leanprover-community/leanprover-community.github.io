---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/07055Independentforallonnat.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Independent forall on nat](https://leanprover-community.github.io/archive/116395maths/07055Independentforallonnat.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Aug 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130859554):
<p>Are there any known independent propositions of the form <code>∀ x : ℕ, p x </code>, where <code>p</code> is a decidable predicate?</p>

#### [ Kevin Buzzard (Aug 03 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130860599):
<p>My vague understanding of Friedman's work is that he comes up with statements about finite objects which are independent of ZFC, but they can be typically proved using large cardinal axioms. But are you talking about independence in Lean + the three usual axioms, which I think is a much stronger statement?</p>

#### [ Chris Hughes (Aug 03 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130860948):
<p>more or less yes. Does independence in ZFC not imply independence in lean?</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130861681):
<p>No, of course Con(ZFC) is independent of ZFC and provable in lean</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130861700):
<p>But Con(lean) can be expressed as a Pi01 sentence, i.e. as <code>∀ x : ℕ, p x</code> where <code>p</code> is decidable</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130861795):
<p>I don't know if any of the "cheap shot" independent statements like <code>N = Z</code> can be written as arithmetic statements</p>

#### [ Kevin Buzzard (Aug 03 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862188):
<p><a href="http://www.ams.org/notices/200604/fea-davis.pdf" target="_blank" title="http://www.ams.org/notices/200604/fea-davis.pdf">http://www.ams.org/notices/200604/fea-davis.pdf</a></p>

#### [ Kevin Buzzard (Aug 03 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862251):
<p>This seems to give arguments which prove that p exists without explicitly writing it down, and perhaps it's possible to explicitly write it down but when you've finished it will be pretty horrible</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862424):
<p>There are already lean predicates which will suffice to state this result with an exists</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862584):
<p>specifically, <code>evaln k e 0</code> in the <code>computability</code> lib will evaluate a partial recursive function <code>e</code> for <code>k</code> steps, so there is some <code>e</code> for which <code>\lam n, (evaln n e 0).is_none</code> satisfies the conditions (using a partial recursive function that searches for a contradiction in lean)</p>

#### [ Kevin Buzzard (Aug 03 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862738):
<p>My impression is that this e will be huge though. My impression is that Friedman is actually writing down some precise statements about graphs which are explicit examples of p if independence in ZFC is what you're looking for. See for example the last result in the linked paper. He's quantifying over three variables not one but you just choose a computable bijection between N^3 and N to fix this</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862758):
<p>sure, the encoding isn't optimized for size</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862820):
<p>it's about as complicated as it is to describe a proof system like lean or ZFC+inaccessibles or anything of higher consistency strength</p>

#### [ Kevin Buzzard (Aug 03 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862821):
<p>Of course all this assumes lean/ZFC/whatever we're talking about is consistent. I guess you'll have to wait for some Tarski version of Friedman to come along before you can see an explicit and comprehensible p for Lean...</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862835):
<p>I think some of Friedman's work has the consistency strength of some weakly Mahlo cardinals which is more than enough</p>

#### [ Kevin Buzzard (Aug 03 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862913):
<p>Oh so maybe there's hope with some weird statement about finite graphs</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130862978):
<p>I was somewhat disillusioned with Friedman's claims of "simplicity" when it turned out (in Scott Aaronson's project <a href="https://www.scottaaronson.com/blog/?p=2725" target="_blank" title="https://www.scottaaronson.com/blog/?p=2725">https://www.scottaaronson.com/blog/?p=2725</a> to build a TM whose halting is independent of ZFC) that it's cheaper to just build a tiny metamath verifier than to define some of Friedman's combinatorial objects</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130863138):
<p>If you are only going for "explicit and comprehensible", not size from scratch, it's not so bad at all. It is certainly easier than defining schemes</p>

#### [ Mario Carneiro (Aug 03 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130863454):
<blockquote>
<p>this e will be huge though</p>
</blockquote>
<p>It occurs to me that I don't know what you mean by "huge" here. This number is huge the same way Graham's number is huge: it is numerically very large, but its description is relatively compact. Since you usually aren't working from scratch in lean anyway, but are building up a language as you go, it's perfectly reasonable to get "explicit and comprehensible" by judicious use of sensibly named definitions while still producing a numerically huge result. But I don't see why this should matter to a mathematician</p>

#### [ Kevin Buzzard (Aug 03 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130863916):
<p>I just mean "irritating to write down explicitly" :-)</p>

#### [ Kevin Buzzard (Aug 04 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130865143):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> so the basic trick is to make <code>p n</code> equal to a statement something like "if you write n in base 256 and then interpret the resulting list of numbers as a text file, then this text file is not a proof of X in Lean" where X is carefully chosen. But then you have to build a lean parser etc all within p, and also to get exactly what you ask you need to do some other trickery with computable functions too to actually get this trick to work</p>

#### [ Mario Carneiro (Aug 04 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130865344):
<p>yikes, that's an extreme solution</p>

#### [ Mario Carneiro (Aug 04 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130865398):
<p>I was thinking more along the lines of formalizing a syntax for a dependent type theory like lean, not the real lean language which has lots of irrelevant garbage. It would look a lot like formalizing that paper of mine</p>

#### [ Mario Carneiro (Aug 04 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Independent%20forall%20on%20nat/near/130865404):
<p>Except easier because there are much simpler languages with the same consistency strength</p>


{% endraw %}
