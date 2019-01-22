---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00190recordstub.html
---

## [general](index.html)
### [record stub](00190recordstub.html)

#### [Reid Barton (Oct 20 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136169584):
The hole command to create a record stub is really nice!
Can any emacs gurus (@**Simon Hudon**?) tell me how I can write an emacs command that will insert `{! !}` at the point, navigate inside it (if necessary), and then invoke the Instance Stub hole command?

#### [Simon Hudon (Oct 20 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183553):
Sure :) Let's go step by step. In your configuration file (`.emacs` or `.emacs.d/init.el`), create a function, let's say:

```emacs-lisp
(defun lean-insert-stub ()
  (print "hello world"))
```

#### [Simon Hudon (Oct 20 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183684):
You can change it a little so that you can invoke it from anywhere in emacs:

```emacs-lisp
(defun lean-insert-stub ()
  (interactive)
  (print "hello world"))
```

Then, you just need `M-x lean-insert-stub` to invoke it.

#### [Simon Hudon (Oct 20 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183728):
And if you want it to actually do something: 

```emacs-lisp
(defun lean-insert-stub ()
  (interactive)
  (insert "{!  !}"))
```

#### [Reid Barton (Oct 20 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183809):
I tried having it call `(lean-hole)` next but I got an error even though repositioning the cursor after the insert isn't necessary interactively

#### [Reid Barton (Oct 20 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183855):
```
error in lean-server command handler: (wrong-type-argument number-or-marker-p nil)
Server response was:
```

#### [Simon Hudon (Oct 20 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183867):
I'm looking at `lean-hole--command` instead

#### [Reid Barton (Oct 20 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183935):
It kind of looks like the lean mode is not designed to handle selecting a hole command non-interactively, in terms of the code structure

#### [Reid Barton (Oct 20 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136184005):
Am I supposed to locally set this thing `completing-read-function`? Is that the "emacs way"?

#### [Reid Barton (Oct 20 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136184014):
not that that helps, when it is not getting that far yet

#### [Simon Hudon (Oct 20 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136184074):
Yeah, now that I look more closely, it's not obvious

#### [Simon Hudon (Oct 20 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136184663):
To be fair, I'm still new to emacs. Maybe @**Sebastian Ullrich** can shed some light. What I got so far is:

```emacs-lisp
(defun lean-insert-stub ()
  (interactive)
  (insert "{!  !}")
  (forward-char -3)
  (let ((p (point)))
  (let ((start-pos p)
        (end-pos p))
    (let ((start-marker (make-marker))
          (end-marker (make-marker)))
      (set-marker start-marker start-pos (current-buffer))
      (set-marker end-marker end-pos (current-buffer))
      (lean-hole--command "Instance Stub" start-marker end-marker))))
  )
```

which I built from copying bits from `lean-hole`

