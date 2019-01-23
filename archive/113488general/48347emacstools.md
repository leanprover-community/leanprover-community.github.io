---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48347emacstools.html
---

## Stream: [general](index.html)
### Topic: [emacs tools](48347emacstools.html)

---


{% raw %}
#### [ Simon Hudon (Jun 03 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127482729):
Is it possible in emacs lisp to use `lean-server-session-send-command` to get the text of a definition? Failing that, is it possible to use it with the command `'info` to get the line info of the next command in the file that contains it? I'm trying to create a command to display the definition of the symbol the cursor is currently on.

#### [ Sebastian Ullrich (Jun 03 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127510536):
No, I can't think of any way to do that

#### [ Simon Hudon (Jun 03 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127511408):
What I ended up doing is use the list of keywords in `lean-syntax` and only keep the ones that are commands, use `lean-find-definition` to find the location of the definition and `re-search-forward` to find the next command. That's pretty primitive because it doesn't account for user command but it might just be good enough.

#### [ Sebastian Ullrich (Jun 03 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127511513):
Good enough I guess :)

#### [ Simon Hudon (Jun 04 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127518889):
I'm wondering if it would be more useful to just go with find definition and have an option to go back. What do you think? The easiest way to do it is provide one slot memory for finding definition but it would be nicer to have many slots. I just don't want it to grow without bounds.

#### [ Reid Barton (Jun 04 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519166):
How about setting the mark to the old location if the definition is in the same file?

#### [ Simon Hudon (Jun 04 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519210):
What does that solve?

#### [ Reid Barton (Jun 04 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519219):
then you can C-x C-x to go back

#### [ Reid Barton (Jun 04 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519227):
for example, isearch (C-s) does this

#### [ Simon Hudon (Jun 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519340):
Ah I see! But then when you go to another file, you have a different shortcut than when you stay in the same file

#### [ Reid Barton (Jun 04 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519418):
Apparently there's also C-x C-SPC which will pop marks off a global stack, between files

#### [ Reid Barton (Jun 04 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519469):
So that would always work as a "go back" key

#### [ Reid Barton (Jun 04 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519533):
https://stackoverflow.com/questions/4918707/in-emacs-how-to-go-back-to-previous-line-position-after-using-semantic-jump-to

#### [ Simon Hudon (Jun 04 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519595):
Nice! So you suggest that in `lean-find-definition` (which is called when you press `M-.`) I first push the mark and then set the mark to `(point)` and then the user will simply have access to those features?

#### [ Simon Hudon (Jun 04 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519597):
Is there a limit to the number of slots on that stack?

#### [ Reid Barton (Jun 04 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519603):
I don't know. I just found out the limit is more than one :simple_smile:

#### [ Reid Barton (Jun 04 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519650):
I think you just need to call `(push-mark)` before doing the navigation

#### [ Reid Barton (Jun 04 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519710):
```
mark-ring-max is a variable defined in ‘simple.el’.
Its value is 16

Documentation:
Maximum size of mark ring.  Start discarding off end if gets this big.
```

#### [ Simon Hudon (Jun 04 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519766):
```quote
I think you just need to call `(push-mark)` before doing the navigation
```
Inside of `lean-mode` or as a user of `lean-mode`?

#### [ Reid Barton (Jun 04 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519772):
`lean-find-definition` should call it (I guess, haven't looked at the code)

#### [ Reid Barton (Jun 04 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519825):
Hmm. I see there is already this, in `lean-find-definition-cont`
```elisp
(cl-defun lean-find-definition-cont (&key file line column)
  (when (fboundp 'xref-push-marker-stack) (xref-push-marker-stack))
...
```

#### [ Simon Hudon (Jun 04 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519832):
This is so nice! It's working very well!

#### [ Simon Hudon (Jun 04 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519836):
Thanks!

#### [ Simon Hudon (Jun 04 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519894):
I can PR it if you'd like to have it too

#### [ Reid Barton (Jun 04 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519900):
Yes please

#### [ Reid Barton (Jun 04 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519907):
I've been wanting this feature too, but the mark thing just occurred to me now

#### [ Reid Barton (Jun 04 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519969):
It looks like maybe M-, already does the same thing? but I have that mapped to autocomplete

#### [ Simon Hudon (Jun 04 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127520133):
You're right! I undid my changes and `M-.` `M-.` `M-,` `M-,` brings me back to the beginning. It looks like my pull request will be the empty set. I hope it's approved!


{% endraw %}
