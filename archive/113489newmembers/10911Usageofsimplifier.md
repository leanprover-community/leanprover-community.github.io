---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/10911Usageofsimplifier.html
---

## Stream: [new members](index.html)
### Topic: [Usage of simplifier](10911Usageofsimplifier.html)

---


{% raw %}
#### [ AHan (Nov 02 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Usage%20of%20simplifier/near/136979706):
<p>Although having read the simplifier in the tutorial: Theorem Proving in Lean and the The Lean Reference Manual<br>
I'm still not quite understand when to use simplifier and why or why can't simp succeed in some cases,</p>
<p><a href="https://gist.github.com/potsrevennil/0cbf2204a8a16daa6eab367f153be748#file-primefield-lean-L60" target="_blank" title="https://gist.github.com/potsrevennil/0cbf2204a8a16daa6eab367f153be748#file-primefield-lean-L60">https://gist.github.com/potsrevennil/0cbf2204a8a16daa6eab367f153be748#file-primefield-lean-L60</a><br>
Take a self-defined prime field for an example, when I'm trying to prove the well-definedness of the addition of the field,. Since in the line 60 and 61, it's kind of redundant, I'm thinking of using simplifier to simplify the code. Anyway I couldn't succeed...</p>

#### [ Johan Commelin (Nov 02 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Usage%20of%20simplifier/near/136980681):
<p><span class="user-mention" data-user-id="133545">@AHan</span> This is not answering your question, but why do you include <code>% p</code> in your definition of addition. If would just use <code>of_int (m + n)</code>. It will make a lot of proofs that come afterwards a lot easier.</p>

#### [ AHan (Nov 02 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Usage%20of%20simplifier/near/136981329):
<p>oh yeah! You're right!<br>
I didn't notice this since I defined the addition before the equivalence....</p>

#### [ AHan (Nov 02 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Usage%20of%20simplifier/near/136981596):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  It did simplify a lot ! Totally get rid of the redundant part that I mentioned! (Though still confuse about the usage of simplifier) Thank you very much!!</p>


{% endraw %}
