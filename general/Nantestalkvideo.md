---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: general/Nantestalkvideo.html
---

## [general](index.html)
### [Nantes talk video](Nantestalkvideo.html)

#### Patrick Massot (Jan 18 2019 at 12:52):
The maths department in Nantes uploaded the video of the Lean talk I gave in November at http://media.math.sciences.univ-nantes.fr/fr/node/801 It's in French and the most interesting part was also in my Amsterdam talk, but it could still be useful for people who intend to give talks presenting Lean to mathematicians.

#### Kevin Buzzard (Jan 18 2019 at 13:27):
Thanks a lot for posting this Patrick. I hope to be finding myself in this sort of position many times in the future.

#### Kevin Buzzard (Jan 18 2019 at 18:47):
I'm watching this video now. After you typed `split` in the function proof, how did you get `{ sorry}` x 2 to appear instantly?

#### Patrick Massot (Jan 18 2019 at 18:50):
User code snippet

#### Patrick Massot (Jan 18 2019 at 18:51):
In my `~/.config/Code/User/snippets/lean.json` I see:

#### Patrick Massot (Jan 18 2019 at 18:51):
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

#### Patrick Massot (Jan 18 2019 at 18:52):
Do you understand enough French to understand me, or are following only through Lean?

#### Johan Commelin (Jan 18 2019 at 18:56):
Kevin gave math talks in French!

#### Kevin Buzzard (Jan 18 2019 at 19:06):
My French is good enough to understand what you're saying. The camera is off now though -- in your group theory proof I can't see the first four or five characters of every line in the VS Code.

#### Patrick Massot (Jan 18 2019 at 19:07):
I forgot, you can talk about "une groupe"!

#### Kevin Buzzard (Jan 18 2019 at 19:08):
:-/

