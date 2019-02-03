---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91514notation.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [∃ notation](https://leanprover-community.github.io/archive/113488general/91514notation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 25 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%E2%88%83%20notation/near/130270397):
<p>I've been encouraging my students to answer their own questions by showing them again and again how to unravel the things they write and see using Lean. But I came unstuck yesterday with <code>∃</code>. It's a random unicode character, so it's going to be notation. I know the answer -- it's going to be <code>Exists</code>. But <code>#print notation ∃</code> doesn't tell me this -- it just says <code> `∃`:1024 binders `,`:0 (scoped 0) := #0` </code> and I read this as saying "this is fancy notation using some tricks, but I'm not going to tell you exactly how it expands" (note that <code>Exists</code> is not mentioned explicitly in the output). Ali Sever just pointed out to me that if you actually _use_ the notation, i.e. write <code>example : ∃ n : ℕ, n = 0 := sorry</code> and then right-click on <code>∃</code> with the cursor to the left of the symbol (note: cursor on the right doesn't seem to work!) then it takes you to the definition of <code>Exists</code> and, fortunately, the notation is defined a few lines below, so you are likely to spot it (although I guess in theory the notation could have been defined somewhere completely different). Am I missing a trick? I was expecting some kind of way of going from the <code>∃</code> symbol in a lean file to the exact line <code>notation `∃` binders `, ` r:(scoped P, Exists P) := r</code> and this is what I can't find.</p>

#### [ Patrick Massot (Jul 25 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%E2%88%83%20notation/near/130270551):
<p>I don't know the answer, but let me point out the right vs left cursor position is not specific to single character notation. Hitting F12 never works if cursor is at the end of a word.</p>


{% endraw %}
