---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06254SpacemacsLeanLayer.html
---

## Stream: [general](index.html)
### Topic: [Spacemacs Lean Layer](06254SpacemacsLeanLayer.html)

---

#### [Robert Kornacki (Oct 05 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135231987):
Recently I just quickly put together a Spacemacs layer for lean which pretty much just rebinds lean-mode to be as expected for the Spacemacs vim crowd. Thought it'd be worth sharing for anyone else who's a Spacemacs user https://github.com/robkorn/spacemacs-lean-layer

#### [Sebastian Ullrich (Oct 05 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135232172):
@**Robert Kornacki** Looks nice! Here's some more config from my .spacemacs file:
```
  (push 'lean-mode spacemacs-indent-sensitive-modes)

  (sp-local-pair 'lean-mode "/-" "-/")
  (sp-local-pair 'lean-mode "`'" nil :actions :rem)
  (sp-local-pair 'lean-mode "⟨" "⟩")
  (sp-local-pair 'lean-mode "«" "»")
  ;; etc, haven't bothered to complete the list yet
```

#### [Sebastian Ullrich (Oct 05 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135232212):
I also use Spacemacs's standard `g d` for navigation
```
  (spacemacs|define-jump-handlers lean-mode (lean-find-definition :async t))
```

#### [Robert Kornacki (Oct 06 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135290857):
@**Sebastian Ullrich**  Ah, thanks for sharing! I've added all of your config to the layer since they are no-brainers to include. As I keep using lean and find the need to I'll most likely keep adding local-pairs overtime. If you or anyone else comes up with something else to add let me know or shoot me a pull request.

#### [Sebastian Ullrich (Oct 06 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Spacemacs%20Lean%20Layer/near/135290872):
Great, thanks!

