---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75896syntaxsurprises.html
---

## Stream: [general](index.html)
### Topic: [syntax surprises](75896syntaxsurprises.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128299157):
The Lean 4 parser only understands `prelude`, `import`, and `theory` so far, but I've already learned something surprising: `noncomputable theory` can be used anywhere in a file (also, multiple times)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 19 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128299364):
Can you elucidate on what is surprising about that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128299761):
I assumed it only worked on the top of a file, since we usually use "theory" synonymously to "file".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 19 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300248):
Ah, `theory`, not `theorem`: I missed that. I also didn't know `theory` was a keyword.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 19 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300366):
I've only worked on computable theorems. Looking in the Lean 3 core library and mathlib, I see only `noncomputable theory` used. I don't see `theory` mentioned in the reference manual or TPIL. What purpose does `theory` serve?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300531):
`theory` is a command, like `theorem`. `noncomputable` is a modifier you can apply to either of them. The distinction doesn't really matter in Lean 3 since `theory` can only be used together with`noncomputable`, which marks the remainder of the file as noncomputable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 19 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300541):
which marks the *appropriate* remainder of the file as noncomputable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300547):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 19 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300549):
computable functions remain computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300685):
Perhaps we'll want to generalize `theory` in Lean 4, though I'm not sure whether there are many sensible combinations. Say, using `private theory`, then negating it using a new keyword `public` on a few declarations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 19 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128300690):
lean -- java remade

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 19 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128304668):
Oh funny, I've used `noncomputable theory` inside a section before and sort of expected it to be scoped, though there's no way I'd ever notice if it wasn't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308056):
wasn't there a Github issue the idea of introducing also `meta theory`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 19 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308151):
@**Sebastian Ullrich** what about changing `theory` to be only allowed at the file header, but extend `section` and `namespace` to take `meta`, `noncomputable`, `private`, `protected`, `public` modifiers?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308168):
how do you define file header?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308172):
currently `import` must be at the beginning

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308179):
@**Johannes Hölzl**  Yes, that's my plan right now :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308183):
Also, attributes on sections

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308187):
Nice!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308276):
@**Kenny Lau** Right now I've defined it as `prelude? (import ...)* (noncomputable theory)?`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308342):
are you going to regex the whole file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308362):
Of course, everyone knows you solve all problems with regexes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 19 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308375):
now you have 2...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 19 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308434):
modulo whitespace / comments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308458):
`repeat { all_goals { apply_regex } }`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 19 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128308841):
another purpose of theory could be to set parameters, or execute an imported command, like `mathlib theory`. This would setup certain notation, options, namespaces, version checks etc. I guess this could be also solved using `run_cmd`, but `theory` is a nice syntax. Also, what about moving `prelude` to `prelude theory`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128309035):
`prelude` should logically come before `import` since it suppreses the default imports. We could move `theory` to the front instead, I'm not sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 19 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128309284):
Okay, this makes sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128309423):
There shouldn't be any reason to restrict the modifiers applicable to `theory` in Lean 4, no. Though, in the examples so far, it sounded like applying something to `theory` or `section` simply distributes it to all contained declarations (even if, as Kenny pointed out, it will behave differently from e.g. an explicit `noncomputable`). Your `mathlib` example doesn't quite fit in that scheme.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 19 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128311123):
Will lean 4 allow for gathering the global file structure? For example: find the open section and namespace names; currently declared variables and parameters, notations and other `local` declarations; finding the "outline" of a given file, i.e. the tree of namespace and section blocks and the definitions in them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 19 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/syntax%20surprises/near/128311421):
You'll definitely get access to a concrete syntax tree of the entire file. You should also get access to more "dynamic" information like open namespaces (which could be influenced by a `run_cmd`), though it's less clear what that could look like

