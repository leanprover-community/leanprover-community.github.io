---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42445Nantestalkvideo.html
---

## [general](index.html)
### [Nantes talk video](42445Nantestalkvideo.html)

#### [Patrick Massot (Jan 18 2019 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156362257):
The maths department in Nantes uploaded the video of the Lean talk I gave in November at http://media.math.sciences.univ-nantes.fr/fr/node/801 It's in French and the most interesting part was also in my Amsterdam talk, but it could still be useful for people who intend to give talks presenting Lean to mathematicians.

#### [Kevin Buzzard (Jan 18 2019 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156363763):
Thanks a lot for posting this Patrick. I hope to be finding myself in this sort of position many times in the future.

#### [Kevin Buzzard (Jan 18 2019 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386051):
I'm watching this video now. After you typed `split` in the function proof, how did you get `{ sorry}` x 2 to appear instantly?

#### [Patrick Massot (Jan 18 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386271):
User code snippet

#### [Patrick Massot (Jan 18 2019 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386293):
In my `~/.config/Code/User/snippets/lean.json` I see:

#### [Patrick Massot (Jan 18 2019 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386309):
```json
"Split": {
        "prefix": "split",
        "body": [
		  "split,",
		  "{ $0",
		  "  sorry },",
		  "{ ",
		  "  sorry },"
        ],
        "description": "Split tactic"
        },
```

#### [Patrick Massot (Jan 18 2019 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386380):
Do you understand enough French to understand me, or are following only through Lean?

#### [Johan Commelin (Jan 18 2019 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156386670):
Kevin gave math talks in French!

#### [Kevin Buzzard (Jan 18 2019 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156387286):
My French is good enough to understand what you're saying. The camera is off now though -- in your group theory proof I can't see the first four or five characters of every line in the VS Code.

#### [Patrick Massot (Jan 18 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156387316):
I forgot, you can talk about "une groupe"!

#### [Kevin Buzzard (Jan 18 2019 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Nantes%20talk%20video/near/156387422):
:-/

