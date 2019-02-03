---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06254SpacemacsLeanLayer.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Spacemacs Lean Layer](https://leanprover-community.github.io/archive/113488general/06254SpacemacsLeanLayer.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Robert Kornacki (Oct 05 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135231987):
<p>Recently I just quickly put together a Spacemacs layer for lean which pretty much just rebinds lean-mode to be as expected for the Spacemacs vim crowd. Thought it'd be worth sharing for anyone else who's a Spacemacs user <a href="https://github.com/robkorn/spacemacs-lean-layer" target="_blank" title="https://github.com/robkorn/spacemacs-lean-layer">https://github.com/robkorn/spacemacs-lean-layer</a></p>

#### [ Sebastian Ullrich (Oct 05 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135232172):
<p><span class="user-mention" data-user-id="130312">@Robert Kornacki</span> Looks nice! Here's some more config from my .spacemacs file:</p>
<div class="codehilite"><pre><span></span>  (push &#39;lean-mode spacemacs-indent-sensitive-modes)

  (sp-local-pair &#39;lean-mode &quot;/-&quot; &quot;-/&quot;)
  (sp-local-pair &#39;lean-mode &quot;`&#39;&quot; nil :actions :rem)
  (sp-local-pair &#39;lean-mode &quot;⟨&quot; &quot;⟩&quot;)
  (sp-local-pair &#39;lean-mode &quot;«&quot; &quot;»&quot;)
  ;; etc, haven&#39;t bothered to complete the list yet
</pre></div>

#### [ Sebastian Ullrich (Oct 05 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135232212):
<p>I also use Spacemacs's standard <code>g d</code> for navigation</p>
<div class="codehilite"><pre><span></span>  (spacemacs|define-jump-handlers lean-mode (lean-find-definition :async t))
</pre></div>

#### [ Robert Kornacki (Oct 06 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135290857):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>  Ah, thanks for sharing! I've added all of your config to the layer since they are no-brainers to include. As I keep using lean and find the need to I'll most likely keep adding local-pairs overtime. If you or anyone else comes up with something else to add let me know or shoot me a pull request.</p>

#### [ Sebastian Ullrich (Oct 06 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135290872):
<p>Great, thanks!</p>


{% endraw %}
