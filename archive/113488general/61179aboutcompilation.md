---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61179aboutcompilation.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [about compilation](https://leanprover-community.github.io/archive/113488general/61179aboutcompilation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 08 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147299477):
<p>why do we need to re-compile the file as well as all the files that depend on the file even if all we did is adding a space?</p>

#### [ Kenny Lau (Nov 08 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147299709):
<p>or if we just change proofs?</p>

#### [ Sebastian Ullrich (Nov 08 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147300005):
<p>Because the alternative is so complex that not a single ITP I know does otherwise</p>

#### [ Kenny Lau (Nov 08 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147300301):
<p>could you elaborate?</p>

#### [ Sebastian Ullrich (Nov 08 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147305164):
<p>For adding a space, the short story is that we should compare the old and new AST's contents to decide if there was a semantic change. But Lean 3 does not even have ASTs for full definitions.</p>

#### [ Sebastian Ullrich (Nov 08 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147305250):
<p>If you change a proof, that is an actual change that results in a different .olean file. So now you need some extra logic to tell dependent files that while the .olean file has changed, they shouldn't care about that.</p>

#### [ Sebastian Ullrich (Nov 08 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147305300):
<p>etc. pp.. It's not impossible, and we have at least discussed whether we could do something in that direction in Lean 4, but it's not at all trivial</p>

#### [ Kenny Lau (Nov 08 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147305319):
<p>what is AST?</p>

#### [ Sebastian Ullrich (Nov 08 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147305325):
<p>abstract syntax tree</p>

#### [ Kenny Lau (Nov 08 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147305521):
<p>what makes ITP different from ordinary programming languages that can do that?</p>

#### [ Kenny Lau (Nov 08 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147305525):
<p>(that's probably a stupid question)</p>

#### [ Johan Commelin (Nov 08 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147305750):
<p>Ordinary programming languages would recompile everything if you changed a "proof", because the don't have "proof"-irrelevance. All their function definitions are data.</p>

#### [ Sebastian Ullrich (Nov 08 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147306095):
<p>Incremental compilation is even harder in "ordinary languages" where all definitions live in the same mutually recursive context. The Rust people have been working on it for multiple years and are still not done.</p>

#### [ Bryan Gin-ge Chen (Nov 08 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147307938):
<p>Very naïve question, but why are the proofs stored in the .olean files? Since there is proof irrelevance, isn't it true that they won't be read again?</p>

#### [ Bryan Gin-ge Chen (Nov 08 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147308007):
<p>I guess you didn't say that the proofs are stored in the .olean files and perhaps it's not true. But then my question is why should changing proofs change the .olean files?</p>

#### [ Keeley Hoek (Nov 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147340884):
<p>The proofs are not needed, but they witness the fact that a proof exists. I think the idea with the olean files was something that could both have its program-parts executed, and be run through a Lean checker in order to check correctness.</p>

#### [ Sebastian Ullrich (Nov 09 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147357737):
<p>Yes, the proofs are consumed by external checkers. They could be move to a separate file, but it doesn't help much: Even just inserting a newline somewhere changes position information in the .olean file. So you really need a more sophisticated dependency system than on the file level.</p>

#### [ Simon Hudon (Nov 11 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147464338):
<p>I think the easiest thing to do would be to get a build system to hash the olean files and consider a change only when the olean's hash changes</p>

#### [ Simon Hudon (Nov 11 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/about%20compilation/near/147464339):
<p>Changing a proof would still trigger a rebuild but adding a space wouldn't</p>


{% endraw %}
