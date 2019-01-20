---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: PRreviews/510oppositecategories.html
---

## [PR reviews](index.html)
### [#510 opposite categories](510oppositecategories.html)

#### Johan Commelin (Dec 20 2018 at 08:39):
@**Scott Morrison|110087** I saw you fixed some stuff, but Travis is still complaining... If you don't have time for this, just let me know, and I'll try to take a look.

#### Scott Morrison (Dec 20 2018 at 09:24):
Think I've got it now. That intermediate commit was just getting work from my office computer to my laptop.

#### Johan Commelin (Dec 22 2018 at 14:49):
@**Mario Carneiro** I get that you don't like the idea of making `op` irreducible. So what is the best way forward? Just now I had to compose two arrows `f` and `g`, but `f` lived in the opposite category... so Lean complained. I would love to just write `f.unop` and move on. What do you think is the best solution?

#### Mario Carneiro (Dec 22 2018 at 14:50):
you can have `unop` without making `op` irreducible

#### Johan Commelin (Jan 17 2019 at 15:34):
@**Mario Carneiro** Would you welcome a PR that puts `op` and `unop` throughout the library without making `op` irreducible?

#### Mario Carneiro (Jan 17 2019 at 16:47):
sure

#### Scott Morrison (Jan 19 2019 at 12:27):
Ok, #510 no longer actually makes `opposite` irreducible. This PR has some useful cleanup in other category_theory files, as well.

