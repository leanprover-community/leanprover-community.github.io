---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33061Documentationstrings.html
---

## [general](index.html)
### [Documentation strings](33061Documentationstrings.html)

#### [Joe Hendrix (Aug 06 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation strings/near/131003087):
Is there a convention in Lean for attaching documentation to specific declarations as in Haddock or Javadoc?

#### [Reid Barton (Aug 06 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation strings/near/131003136):
Yes. use `---` or `/-- ... -/`

#### [Joe Hendrix (Aug 06 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation strings/near/131003264):
Does that show up in the Emacs or VSCode interfaces?  I'm using the emacs interface primarily.

#### [Joe Hendrix (Aug 06 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation strings/near/131003391):
Surprisingly, I get an error `command expected` when I use the `/-- ... -/` syntax in front of a record field name.  So it seems like there is some parsing.

#### [Simon Hudon (Aug 06 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation strings/near/131003541):
In emacs, it should show you the doc string in the minibuffer. 

```quote
Surprisingly, I get an error command expected when I use the /-- ... -/ syntax in front of a record field name.
```

I think they are only allowed on declarations (`theorem`, `def`, `constant`, etc) and not on their components.

#### [Joe Hendrix (Aug 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation strings/near/131003709):
Thanks!  I see it now.

#### [Mario Carneiro (Aug 06 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documentation strings/near/131004824):
for other places in a definition you should just use normal comments (`--` or `/- -/`), not doc comments

