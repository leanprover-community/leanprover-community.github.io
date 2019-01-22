---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/73691QuestionsaboutLean4.html
---

## [Lean Together 2019](index.html)
### [Questions about Lean 4](73691QuestionsaboutLean4.html)

#### [Joseph Corneli (Jan 07 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572312):
"any chance of the tool you're presenting will allow us to reimplement parameters?"

#### [Joseph Corneli (Jan 07 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572327):
"I was hoping parameters would get sane... now I have more tactics to write"

#### [Joseph Corneli (Jan 07 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572342):
... I think we can make something better than parameters.  Reinterpret them.

#### [Joseph Corneli (Jan 07 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572360):
"Type reflection... what's going to happen?  Will we have type of expressions of a give type?"

#### [Joseph Corneli (Jan 07 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572413):
... Leo in Lean, past, present and future talks about this.

#### [Joseph Corneli (Jan 07 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572434):
"If you go back to 'how to port' - changes in the meta-interface.  We have some tactics in mathlib for example.  They need to be rewritten because the expression syntax changes?"

#### [Joseph Corneli (Jan 07 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572445):
"Something like local_const?"
... that's just a search and replace

#### [Joseph Corneli (Jan 07 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572475):
"Primitive projections..."

#### [Joseph Corneli (Jan 07 2019 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572549):
"Sugared version of let... let goes down into the kernel"
... you can come up with your own syntax, and now say let is just syntax for..."

#### [Joseph Corneli (Jan 07 2019 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572609):
... there are no foundational changes, except for primitive projection and mutual induction.  projection is more of an implementation detail.
... Lean 5???  Lean 4 is as general as we can make it.  There will not be a Lean 5 in the near future. 

"Lean 3 has failed? What's the definition of failure?"
... Getting issues at Github that you can't implement with the current system and getting frustrated with that.

"So, people asking Leo to make syntax changes..."

#### [Joseph Corneli (Jan 07 2019 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572706):
"Instead of waiting for completion of the project, could we use the new parser ...?"

... You can't use it without the macro expander.

"But if we wanted to have a beautiful HTML file... or a linter for code?"

... But you may still want information from the elaborator.  You'll need more information from just the syntax tree?

#### [Joseph Corneli (Jan 07 2019 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572743):
"We have a trend to move to cubical type checkers...?"

... no foundational changes in the logic.

"It is possible to embed cubical type theory... We can construct the syntax. "

... Embed things like Lean 3 HoTT did.

#### [Joseph Corneli (Jan 07 2019 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572813):
"There are some issues with the way coersions work..."

... we're not yet sure how they should work ideally.

#### [Sebastian Ullrich (Jan 07 2019 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154577969):
```quote
"Instead of waiting for completion of the project, could we use the new parser ...?"

... You can't use it without the macro expander.
```
 To expand (heh) on that, Lean's extensible syntax (in both Lean 3 and 4) means that you can't just throw the parser at an arbitrary Lean file. You first have to register all notations from the imports, then handle notations in the file, including scoping local notations to enclosing sections, etc...

#### [Koundinya Vajjha (Jan 07 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154579901):
No one asked the million dollar question? When is it coming out? :grinning_face_with_smiling_eyes:

#### [Johan Commelin (Jan 07 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154579931):
201X seems to be the default answer...

#### [Joseph Corneli (Jan 07 2019 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154580237):
So presumably later this year, see title of thread.

#### [Joseph Corneli (Jan 07 2019 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154580252):
er, title of Stream, rather

#### [Kevin Buzzard (Jan 07 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154592008):
I asked this directly to Sebastian and he said that 201X was not supposed to imply before 2020 -- it was just an unfortunate choice of notation.

#### [Simon Hudon (Jan 07 2019 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154603322):
@**Kevin Buzzard** That's a fair point. Before it's release, C++ 2011 was known as C++0x

