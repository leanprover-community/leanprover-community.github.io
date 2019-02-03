---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36524matrixupdates.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [matrix updates](https://leanprover-community.github.io/archive/116395maths/36524matrixupdates.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Sep 11 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133716760):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I worked a bit on matrices on the side. I don't know if you'll be happy with the differences with <a href="https://github.com/leanprover/mathlib/pull/334" target="_blank" title="https://github.com/leanprover/mathlib/pull/334">#334</a>, so I PR'd <a href="https://github.com/leanprover-community/mathlib/pull/2" target="_blank" title="https://github.com/leanprover-community/mathlib/pull/2">#2</a> to your branch on <code>leanprover-community/mathlib</code>. Let me know what you think.</p>

#### [ Sean Leather (Sep 11 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133716918):
<p>BTW, to view the diff while ignoring whitespace changes, see <a href="https://github.com/leanprover-community/mathlib/pull/2/files?w=1" target="_blank" title="https://github.com/leanprover-community/mathlib/pull/2/files?w=1">https://github.com/leanprover-community/mathlib/pull/2/files?w=1</a> . There are still a lot of changes. <span class="emoji emoji-1f615" title="concerned">:concerned:</span> But I believe all of the major stuff that was in your original PR is still there.</p>

#### [ Johan Commelin (Sep 11 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133720033):
<p>Cool, so now matrices are even a ring. Nice work Sean!</p>

#### [ Johan Commelin (Sep 11 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133720056):
<p>I agree that the diff looks a bit daunting. But I think that is mostly because of some syntactic changes that don't represent a very big change in mathematics.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133721556):
<p>I am completely happy with any changes. I am just tired of matrices not being in Lean (as are some of my "clients", as Mario once referred to them).</p>

#### [ Kevin Buzzard (Sep 11 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133722723):
<p>PS <span class="user-mention" data-user-id="112680">@Johan Commelin</span> Ellen proved they were a ring :P . <span class="user-mention" data-user-id="110045">@Sean Leather</span> I should also add -- thanks a lot!</p>

#### [ Sean Leather (Sep 11 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133723059):
<p>Yes, all the credit should go to people who worked on it before me. I just build on the shoulders of giants. Also, I think the <code>fintype</code> idea was due to Johannes and Johan. Since Kevin is happy, I merged the PR.</p>

#### [ Johan Commelin (Sep 12 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/matrix%20updates/near/133778267):
<p>Somehow Travis is now failing (and it is not a timeout). It didn't receive any output for 10min.</p>


{% endraw %}
