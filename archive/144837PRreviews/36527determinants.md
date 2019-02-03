---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/36527determinants.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [determinants](https://leanprover-community.github.io/archive/144837PRreviews/36527determinants.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Oct 07 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135357675):
<p>I did some tidying on the determinants PR. I got rid of all the relics of <code>Sym</code> that weren't actually used for determinants - It's now only a 130 line Pr, versus 481. I also made the proofs hopefully more readable, if longer. Result is here <a href="https://github.com/leanprover/mathlib/compare/master...dorhinj:determinants2?expand=1" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...dorhinj:determinants2?expand=1">https://github.com/leanprover/mathlib/compare/master...dorhinj:determinants2?expand=1</a></p>

#### [ Chris Hughes (Oct 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135357687):
<p>Old version <a href="https://github.com/leanprover/mathlib/pull/378/files" target="_blank" title="https://github.com/leanprover/mathlib/pull/378/files">https://github.com/leanprover/mathlib/pull/378/files</a></p>

#### [ Mario Carneiro (Oct 08 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135371096):
<p>is it PR'd? I want</p>

#### [ Johan Commelin (Oct 08 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135384959):
<p>So now we have determinants, but we don't know that it is a monoid hom. For this we need <a href="https://github.com/leanprover/mathlib/pull/375" target="_blank" title="https://github.com/leanprover/mathlib/pull/375">https://github.com/leanprover/mathlib/pull/375</a></p>

#### [ Mario Carneiro (Oct 08 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385095):
<p>I don't understand why that thing is called the <code>free_module</code></p>

#### [ Johan Commelin (Oct 08 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385119):
<p>Should I just remove that code for now?</p>

#### [ Johan Commelin (Oct 08 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385131):
<p>The bit on scalar matrices is more important to me</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385179):
<p>Why do we need it? Like I said <code>diagonal</code> subsumes it</p>

#### [ Johan Commelin (Oct 08 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385205):
<p>I think it is nice to have</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385217):
<p>We also have <code>a * I</code></p>

#### [ Mario Carneiro (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385228):
<p>which is the way the rest of the world notates this</p>

#### [ Johan Commelin (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385242):
<p>Hmm... ok</p>

#### [ Johan Commelin (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385245):
<p>I don't really care</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385257):
<p>I'm trying to understand what is needed</p>

#### [ Johan Commelin (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385302):
<p>What is needed is that <code>det</code> is a monoid hom</p>

#### [ Mario Carneiro (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385306):
<p>That PR doesn't say anything about monoid homs</p>

#### [ Johan Commelin (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385314):
<p>No, but <code>det_one</code> uses <code>det_scalar</code></p>

#### [ Johan Commelin (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385319):
<p>That stuff was commented out in my <code>det</code> PR</p>

#### [ Johan Commelin (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385325):
<p>I don't know if Chris preserved those comments. Let me check</p>

#### [ Johan Commelin (Oct 08 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385343):
<p>No, those are gone</p>

#### [ Chris Hughes (Oct 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135386346):
<p>We have <code>det_one</code> so it is proven to be a monoid hom. Are monoid Homs defined yet?</p>

#### [ Johan Commelin (Oct 08 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135386450):
<p>Yes they are</p>

#### [ Johan Commelin (Oct 08 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135386455):
<p>So my new PR is a 4-liner.</p>


{% endraw %}
