---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91514notation.html
---

## Stream: [general](index.html)
### Topic: [∃ notation](91514notation.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%E2%88%83%20notation/near/130270397):
I've been encouraging my students to answer their own questions by showing them again and again how to unravel the things they write and see using Lean. But I came unstuck yesterday with `∃`. It's a random unicode character, so it's going to be notation. I know the answer -- it's going to be `Exists`. But `#print notation ∃` doesn't tell me this -- it just says `` `∃`:1024 binders `,`:0 (scoped 0) := #0` `` and I read this as saying "this is fancy notation using some tricks, but I'm not going to tell you exactly how it expands" (note that `Exists` is not mentioned explicitly in the output). Ali Sever just pointed out to me that if you actually _use_ the notation, i.e. write `example : ∃ n : ℕ, n = 0 := sorry` and then right-click on `∃` with the cursor to the left of the symbol (note: cursor on the right doesn't seem to work!) then it takes you to the definition of `Exists` and, fortunately, the notation is defined a few lines below, so you are likely to spot it (although I guess in theory the notation could have been defined somewhere completely different). Am I missing a trick? I was expecting some kind of way of going from the `∃` symbol in a lean file to the exact line ``notation `∃` binders `, ` r:(scoped P, Exists P) := r`` and this is what I can't find.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%E2%88%83%20notation/near/130270551):
I don't know the answer, but let me point out the right vs left cursor position is not specific to single character notation. Hitting F12 never works if cursor is at the end of a word.


{% endraw %}
