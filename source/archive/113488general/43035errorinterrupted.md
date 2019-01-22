---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43035errorinterrupted.html
---

## [general](index.html)
### [error: interrupted](43035errorinterrupted.html)

#### [Reid Barton (Jun 02 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445373):
Does anyone know why this often happens when using jump-to-definition? (I'm in emacs if it matters.)

#### [Simon Hudon (Jun 02 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445391):
I get the same error.

#### [Simon Hudon (Jun 02 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445442):
I thought it might be a problem with `company-mode` but I wasn't able to find anything. Are you also on a Mac?

#### [Reid Barton (Jun 02 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445454):
Linux here

#### [Simon Hudon (Jun 02 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445516):
@**Sebastian Ullrich** also I think and I remember he didn't have the same error so I thought it might be because of mac. It must be something else

#### [Simon Hudon (Jun 02 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445523):
Are you well versed in Emacs Lisp?

#### [Reid Barton (Jun 02 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445624):
Not especially, but I would try to debug it if the issue is not already understood.

#### [Reid Barton (Jun 02 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445625):
It's quite irritating

#### [Simon Hudon (Jun 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446322):
it is indeed. I just added print statements in  `lean-find-definition` in `lean-mode` but I can't get it to fail now ... :/

#### [Simon Hudon (Jun 02 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446785):
Do you have:

```
(global-set-key (kbd "S-SPC") #'company-complete)
```

in your init file? I found a thread on the github repo (https://github.com/company-mode/company-mode/issues/69) that suggests replacing it with:

```
(define-key company-mode-map (kbd "S-SPC") #'company-complete)
```

It seems to help but the bug has been showing up inconsistently. Can you try it and tell me if it helps?

#### [Reid Barton (Jun 02 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446911):
I got `Symbol's value as variable is void: company-mode-map`

#### [Reid Barton (Jun 02 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446917):
Is that the right issue?

#### [Reid Barton (Jun 02 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446984):
okay, a `(require 'company)` fixed that

#### [Simon Hudon (Jun 02 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446986):
That's the one that helped me. Do you have `(require 'company)` before that line?

#### [Reid Barton (Jun 02 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446989):
Well, it's working at the moment, but it usually does after restarting emacs :)

#### [Reid Barton (Jun 02 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127447104):
Oh, it already stopped working

#### [Simon Hudon (Jun 02 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127447116):
Darn! I was hoping!

#### [Simon Hudon (Jun 02 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127447977):
In `lean-input.el`, in `lean-find-definition`, can you try adding print statements inside the lambda expression? Like this:

```elisp
(defun lean-find-definition ()
  "Jump to definition of thing at point"
  (interactive)
  (lean-get-info-record-at-point
   (lambda (info-record)
     (print "begin")
     (-if-let (source-record (plist-get info-record :source))
         (apply #'lean-find-definition-cont source-record)
       (-if-let (id (plist-get info-record :full-id))
           (message "no source location available for %s" id)
         (message "unknown thing at point")))
     (print "end"))))
```

#### [Reid Barton (Jun 02 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127448179):
Well... I tried adding those and it's working again.
Did editing the `.el` file cause emacs to reload the mode automatically?

#### [Simon Hudon (Jun 02 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127448391):
I don't know. I wonder if the printing introduces a delay. Let's try removing the print statements

#### [Reid Barton (Jun 02 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127448441):
Unfortunately I finished proving the thing I was trying to prove

#### [Simon Hudon (Jun 02 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127448556):
I guess we'll never know

#### [Sebastian Ullrich (Jun 02 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127456608):
This is a known issue (to me :) ) where go-to-definition doesn't work while the goal display is open

#### [Simon Hudon (Jun 02 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127462600):
That's very good to know! Is this on the emacs side or on the Lean side?

#### [Sebastian Ullrich (Jun 03 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127510537):
That requests are interrupted by unrelated requests is an issue with the Lean server. But lean-mode could try to work around that by not sending a goal request directly after a find definition request.

#### [Simon Hudon (Jun 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127511362):
Do you think if we set a timer for masking requests for half a second after find definition that might be good enough?

#### [Sebastian Ullrich (Jun 03 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127511592):
It should be sufficient to suppress the next execution of `lean-show-goal--handler` after `lean-find-definition` has run, probably?

#### [Simon Hudon (Jun 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127514811):
That seems to be enough. Do you want a PR for it?

#### [Sebastian Ullrich (Jun 03 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127514912):
Sure, thanks

#### [Simon Hudon (Jun 03 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127515061):
Done

