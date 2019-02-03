---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/73691QuestionsaboutLean4.html
---

## Stream: [Lean Together 2019](index.html)
### Topic: [Questions about Lean 4](73691QuestionsaboutLean4.html)

---


{% raw %}
#### [ Joseph Corneli (Jan 07 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572312):
<p>"any chance of the tool you're presenting will allow us to reimplement parameters?"</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572327):
<p>"I was hoping parameters would get sane... now I have more tactics to write"</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572342):
<p>... I think we can make something better than parameters.  Reinterpret them.</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572360):
<p>"Type reflection... what's going to happen?  Will we have type of expressions of a give type?"</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572413):
<p>... Leo in Lean, past, present and future talks about this.</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572434):
<p>"If you go back to 'how to port' - changes in the meta-interface.  We have some tactics in mathlib for example.  They need to be rewritten because the expression syntax changes?"</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572445):
<p>"Something like local_const?"<br>
... that's just a search and replace</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572475):
<p>"Primitive projections..."</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572549):
<p>"Sugared version of let... let goes down into the kernel"<br>
... you can come up with your own syntax, and now say let is just syntax for..."</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572609):
<p>... there are no foundational changes, except for primitive projection and mutual induction.  projection is more of an implementation detail.<br>
... Lean 5???  Lean 4 is as general as we can make it.  There will not be a Lean 5 in the near future. </p>
<p>"Lean 3 has failed? What's the definition of failure?"<br>
... Getting issues at Github that you can't implement with the current system and getting frustrated with that.</p>
<p>"So, people asking Leo to make syntax changes..."</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572706):
<p>"Instead of waiting for completion of the project, could we use the new parser ...?"</p>
<p>... You can't use it without the macro expander.</p>
<p>"But if we wanted to have a beautiful HTML file... or a linter for code?"</p>
<p>... But you may still want information from the elaborator.  You'll need more information from just the syntax tree?</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572743):
<p>"We have a trend to move to cubical type checkers...?"</p>
<p>... no foundational changes in the logic.</p>
<p>"It is possible to embed cubical type theory... We can construct the syntax. "</p>
<p>... Embed things like Lean 3 HoTT did.</p>

#### [ Joseph Corneli (Jan 07 2019 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154572813):
<p>"There are some issues with the way coersions work..."</p>
<p>... we're not yet sure how they should work ideally.</p>

#### [ Sebastian Ullrich (Jan 07 2019 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154577969):
<blockquote>
<p>"Instead of waiting for completion of the project, could we use the new parser ...?"</p>
<p>... You can't use it without the macro expander.</p>
</blockquote>
<p>To expand (heh) on that, Lean's extensible syntax (in both Lean 3 and 4) means that you can't just throw the parser at an arbitrary Lean file. You first have to register all notations from the imports, then handle notations in the file, including scoping local notations to enclosing sections, etc...</p>

#### [ Koundinya Vajjha (Jan 07 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154579901):
<p>No one asked the million dollar question? When is it coming out? <span class="emoji emoji-1f601" title="grinning face with smiling eyes">:grinning_face_with_smiling_eyes:</span></p>

#### [ Johan Commelin (Jan 07 2019 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154579931):
<p>201X seems to be the default answer...</p>

#### [ Joseph Corneli (Jan 07 2019 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154580237):
<p>So presumably later this year, see title of thread.</p>

#### [ Joseph Corneli (Jan 07 2019 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154580252):
<p>er, title of Stream, rather</p>

#### [ Kevin Buzzard (Jan 07 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154592008):
<p>I asked this directly to Sebastian and he said that 201X was not supposed to imply before 2020 -- it was just an unfortunate choice of notation.</p>

#### [ Simon Hudon (Jan 07 2019 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Questions%20about%20Lean%204/near/154603322):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> That's a fair point. Before it's release, C++ 2011 was known as C++0x</p>


{% endraw %}
