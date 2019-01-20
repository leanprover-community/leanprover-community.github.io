---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: PRreviews/605unique.html
---

## [PR reviews](index.html)
### [#605 unique](605unique.html)

#### Johan Commelin (Jan 18 2019 at 16:43):
Travis is complaining about `ennreal` not being found, but my PR doesn't even come close to touching it. Is this another instance of corrupted caches?

#### Patrick Massot (Jan 18 2019 at 16:52):
Yes, our CI setup really doesn't like when we move files.

#### Kenny Lau (Jan 18 2019 at 22:40):
wow we have 600 PRs already!

