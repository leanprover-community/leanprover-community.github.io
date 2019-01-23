---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/15266emacstipfilladapt.html
---

## Stream: [new members](index.html)
### Topic: [emacs tip: filladapt](15266emacstipfilladapt.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joseph Corneli (Aug 07 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131036154):
I had run into an [issue](https://github.com/leanprover/lean-mode/issues/7) with filling block comments in lean-mode.

The problem is solved with
```
(require 'filladapt)
(add-hook 'lean-mode-hook #'filladapt-mode)
```
Maybe that's helpful for someone.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joseph Corneli (Aug 07 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131036263):
... oh, but maybe I spoke too soon, since by default that screws up the fill behavior for `--` style comments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joseph Corneli (Aug 07 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131036781):
OK, adding one line to the relevant token table fixed it:

```
(setq filladapt-token-table
      '(("^" beginning-of-line)
        (">+" citation->)
        ("\\(\\w\\|[0-9]\\)[^'`\"< 	
]*>[ 	]*" supercite-citation)
        (";+" lisp-comment)
        ;; Added this line
        ("--" lisp-comment)
        ("#+" sh-comment)
        ("%+" postscript-comment)
        ("///*" c++-comment)
        ("@c[ 	]" texinfo-comment)
        ("@comment[ 	]" texinfo-comment)
        ("\\\\item[ 	]" bullet)
        ("[0-9]+\\.[ 	]" bullet)
        ("[0-9]+\\(\\.[0-9]+\\)+[ 	]" bullet)
        ("[A-Za-z]\\.[ 	]" bullet)
        ("(?[0-9]+)[ 	]" bullet)
        ("(?[A-Za-z])[ 	]" bullet)
        ("[0-9]+[A-Za-z]\\.[ 	]" bullet)
        ("(?[0-9]+[A-Za-z])[ 	]" bullet)
        ("[-~*+]+[ 	]" bullet)
        ("o[ 	]" bullet)
        ("[ 	]+" space)
        ("$" end-of-line)))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 07 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131046804):
I've created a repo for user contributions to `lean-mode`: https://github.com/leanprover-community/lean-mode-contrib

That might be a good place to put it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joseph Corneli (Aug 07 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131055013):
OK I'll try to tidy up and send there. Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 07 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131063330):
:+1:

