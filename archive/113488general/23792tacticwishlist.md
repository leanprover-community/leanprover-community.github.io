---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23792tacticwishlist.html
---

## Stream: [general](index.html)
### Topic: [tactic wishlist](23792tacticwishlist.html)

---


{% raw %}
#### [ Koundinya Vajjha (Feb 01 2019 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157348532):
<p>Not sure if there's something like this in another stream - apologies if there is.  What tactics would you like to see written? (By tactics I also include broader metaprogramming constructs, not necessarily those which you would use to discharge proof obligations.)</p>

#### [ Koundinya Vajjha (Feb 01 2019 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157348681):
<p><span class="user-mention" data-user-id="116585">@Seul Baek</span>  told me he wanted to see a tactic to list lemmas in your current file which are unused by other lemmas. This helps in building theories which avoid spurious lemmas.</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157348715):
<p>The big missing tactics for me are <code>metis</code> and <code>omega</code>. <code>metis</code> is important for sledgehammer like operation, and is also useful as a standalone tool for fiddly goals. For <code>omega</code> there are various versions of <code>cooper</code> by Seul that can fill this role, but there is some work to be done to make them usable without a complicated setup and/or a PhD</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157348793):
<p>Most of the little tactics I can think of are already written and in mathlib</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157348828):
<p>Simon and I have been discussing the possibility of global analysis for linting and things, which could address your unused lemmas example</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157348911):
<p>but we are somewhat limited by what lean will give us here, unless we use an external tool like the olean viewer</p>

#### [ Koundinya Vajjha (Feb 01 2019 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157348921):
<p>How about documentation generation? Is there something for that?</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157348996):
<p>I'm not entirely sure what the story is there. <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Lean has some support for a leandoc tool but it's not all there; do you know what the commandline option actually does currently? Is lean 4 any different here?</p>

#### [ Sebastian Ullrich (Feb 01 2019 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157349124):
<p>I've never used it. This should really be an external tool written in Lean in Lean 4.</p>

#### [ Joseph Corneli (Feb 01 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157360566):
<p>How about a tactic to convert term-style proofs into tactic style proofs?</p>

#### [ Johan Commelin (Feb 01 2019 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157361590):
<p>The recent move of mathlib removed the old community-wiki on github. I don't know where to find it now, but it contained a couple of such wishlists.</p>

#### [ Simon Hudon (Feb 01 2019 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157364387):
<p>Are you referring to this: <a href="https://github.com/leanprover-fork/mathlib-backup/wiki" target="_blank" title="https://github.com/leanprover-fork/mathlib-backup/wiki">https://github.com/leanprover-fork/mathlib-backup/wiki</a></p>

#### [ Simon Hudon (Feb 01 2019 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157364641):
<p>I think we could move it to <code>leanprover-community</code></p>

#### [ Johan Commelin (Feb 01 2019 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157371140):
<p>Aaah, yes that's it. Should we just copy-paste it? Or is there some history that can/should be preserved?</p>

#### [ Simon Hudon (Feb 01 2019 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157373191):
<p>It can be preserved, I don't know if we want to. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> You seem to have authored a wiki page with nothing on it on <code>leanprover-community/mathlib</code>. Do you mind if we overwrite it with the one we have in the backup?</p>

#### [ Mario Carneiro (Feb 01 2019 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157380444):
<p>That's news to me. Go ahead and overwrite it, I don't think I have touched the wiki</p>

#### [ Simon Hudon (Feb 01 2019 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20wishlist/near/157384217):
<p>Thanks! I just did. <span class="user-mention" data-user-id="112680">@Johan Commelin</span> you should be able to see what you had before. Let me know if there's anything else to move from the old <code>leanprover-community/mathlib</code> (now located at <code>leanprover-fork/mathlib-backup</code>) to the new <code>leanprover-community/mathlib</code> (formerly <code>leanprover/mathlib</code>)</p>


{% endraw %}
