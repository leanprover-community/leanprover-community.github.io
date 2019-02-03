---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/60837mergingintomathlib.html
---

## Stream: [kbb](https://leanprover-community.github.io/archive/141825kbb/index.html)
### Topic: [merging into mathlib](https://leanprover-community.github.io/archive/141825kbb/60837mergingintomathlib.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 24 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134535620):
<p>Clearly some parts of <code>kbb</code> are not mathlib-ready, but other parts are.</p>

#### [ Johan Commelin (Sep 24 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134535629):
<p>I think we should try to get those merged into mathlib.</p>

#### [ Johan Commelin (Sep 24 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134535659):
<p>For example, the remainder of the file on matrices. The monoid stuff, and determinants should also be merge-ready, I think.</p>

#### [ Johan Commelin (Sep 24 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134535744):
<p>I'll try to work on this when I'm back home. This is a mental note for me, and a hint for others to possible help with this (-;</p>

#### [ Johannes Hölzl (Sep 24 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134539311):
<p>I will merge the PID -&gt; UFD part</p>

#### [ Kevin Buzzard (Sep 25 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134579577):
<p>Just to note here that Chris defined log as the unique inverse of exp yesterday, and proved exp log = id, log exp = id on the appropriate domains. <span class="user-mention" data-user-id="110044">@Chris Hughes</span> Is this file publically accessible?</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134579668):
<p>Nice! Is this the real version or the complex version?</p>

#### [ Kevin Buzzard (Sep 25 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134579688):
<p>real single-valued log from positive reals to reals</p>

#### [ Chris Hughes (Sep 25 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134621012):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Yes it is, on the <code>exp</code> branch of community mathlib.</p>

#### [ Johan Commelin (Sep 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134727322):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Do you want to PR the category of matrices? Or would you like me to do it (from community mathlib)?</p>

#### [ Johan Commelin (Sep 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134727341):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Do you want to PR determinants? Or would you like me to do it (from community mathlib)?</p>

#### [ Scott Morrison (Sep 27 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134727401):
<p>I'm certainly happy if you want to do it. :-) I have a lot of open PRs at the moment...</p>

#### [ Scott Morrison (Sep 27 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134727903):
<p>I do kind of like the </p>
<div class="codehilite"><pre><span></span>def free_module (α : Type v) [semiring α] : Type := ℕ
instance : category (free_module α) :=
{ hom  := λ m n, matrix (fin m) (fin n) α, ... }
</pre></div>


<p>It's somehow alien and familiar at the same time.</p>

#### [ Mario Carneiro (Sep 27 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134728028):
<p>I changed it to a large category over fintypes, what do you think?</p>

#### [ Johan Commelin (Sep 27 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134729544):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> You also deleted a bunch of stuff on diagonal matrices, I think. Was that intentional?</p>

#### [ Mario Carneiro (Sep 27 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134729550):
<p>it all moved to mathlib</p>

#### [ Johan Commelin (Sep 27 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134729823):
<p>Hmmm, but not community mathlib...</p>

#### [ Mario Carneiro (Sep 27 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134729915):
<p>huh? just update master in that case</p>

#### [ Chris Hughes (Sep 27 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134730013):
<p>Or update the matrix branch</p>

#### [ Johan Commelin (Sep 27 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134732181):
<p>Aaah, I see what went wrong (and I was afk for 30 minutes)</p>

#### [ Johan Commelin (Sep 27 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134732188):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is there a reason why you didn't merge scalar matrices?</p>

#### [ Johan Commelin (Sep 27 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134732197):
<p>Do you think they are not useful enough, because <code>diagonal</code> easily covers those cases?</p>

#### [ Kenny Lau (Sep 27 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134763925):
<blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Do you want to PR determinants? Or would you like me to do it (from community mathlib)?</p>
</blockquote>
<p>please do it</p>

#### [ Johan Commelin (Sep 27 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134764034):
<p>I'll do it tomorrow</p>

#### [ Mario Carneiro (Sep 27 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134775734):
<p>Aren't there two different definitions of permutation sign (one over <code>fin n</code>, one over a fintype) right now? I think one was developed in kbb by Kenny and the other was in a mathlib PR by Chris</p>

#### [ Kenny Lau (Sep 28 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134794434):
<blockquote>
<p>I'll do it tomorrow</p>
</blockquote>
<p>the same time as when everyone does everything :p</p>

#### [ Johan Commelin (Sep 28 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134795246):
<p>I promise!</p>

#### [ Johan Commelin (Sep 28 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134809097):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Done.</p>

#### [ Chris Hughes (Sep 28 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134810968):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> <span class="user-mention" data-user-id="110064">@Kenny Lau</span> fintype perm is in mathlib now by the way, I imagine you need that.</p>

#### [ Johan Commelin (Sep 28 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134811181):
<p>Aah, I just dumped Kenny's <code>sym</code> into the PR. Does this mean that stuff is duplicated?</p>

#### [ Chris Hughes (Sep 28 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134811214):
<p>Probably</p>

#### [ Chris Hughes (Sep 28 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/merging%20into%20mathlib/near/134811260):
<p>Kenny did sign and stuff, which is also in mathlib.</p>


{% endraw %}
