---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/15266emacstipfilladapt.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [emacs tip: filladapt](https://leanprover-community.github.io/archive/113489newmembers/15266emacstipfilladapt.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Joseph Corneli (Aug 07 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131036154):
<p>I had run into an <a href="https://github.com/leanprover/lean-mode/issues/7" target="_blank" title="https://github.com/leanprover/lean-mode/issues/7">issue</a> with filling block comments in lean-mode.</p>
<p>The problem is solved with</p>
<div class="codehilite"><pre><span></span>(require &#39;filladapt)
(add-hook &#39;lean-mode-hook #&#39;filladapt-mode)
</pre></div>


<p>Maybe that's helpful for someone.</p>

#### [ Joseph Corneli (Aug 07 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131036263):
<p>... oh, but maybe I spoke too soon, since by default that screws up the fill behavior for <code>--</code> style comments.</p>

#### [ Joseph Corneli (Aug 07 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131036781):
<p>OK, adding one line to the relevant token table fixed it:</p>
<div class="codehilite"><pre><span></span>(setq filladapt-token-table
      &#39;((&quot;^&quot; beginning-of-line)
        (&quot;&gt;+&quot; citation-&gt;)
        (&quot;\\(\\w\\|[0-9]\\)[^&#39;`\&quot;&lt;
]*&gt;[    ]*&quot; supercite-citation)
        (&quot;;+&quot; lisp-comment)
        ;; Added this line
        (&quot;--&quot; lisp-comment)
        (&quot;#+&quot; sh-comment)
        (&quot;%+&quot; postscript-comment)
        (&quot;///*&quot; c++-comment)
        (&quot;@c[   ]&quot; texinfo-comment)
        (&quot;@comment[     ]&quot; texinfo-comment)
        (&quot;\\\\item[     ]&quot; bullet)
        (&quot;[0-9]+\\.[    ]&quot; bullet)
        (&quot;[0-9]+\\(\\.[0-9]+\\)+[   ]&quot; bullet)
        (&quot;[A-Za-z]\\.[  ]&quot; bullet)
        (&quot;(?[0-9]+)[    ]&quot; bullet)
        (&quot;(?[A-Za-z])[  ]&quot; bullet)
        (&quot;[0-9]+[A-Za-z]\\.[    ]&quot; bullet)
        (&quot;(?[0-9]+[A-Za-z])[    ]&quot; bullet)
        (&quot;[-~*+]+[  ]&quot; bullet)
        (&quot;o[    ]&quot; bullet)
        (&quot;[     ]+&quot; space)
        (&quot;$&quot; end-of-line)))
</pre></div>

#### [ Simon Hudon (Aug 07 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131046804):
<p>I've created a repo for user contributions to <code>lean-mode</code>: <a href="https://github.com/leanprover-community/lean-mode-contrib" target="_blank" title="https://github.com/leanprover-community/lean-mode-contrib">https://github.com/leanprover-community/lean-mode-contrib</a></p>
<p>That might be a good place to put it</p>

#### [ Joseph Corneli (Aug 07 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131055013):
<p>OK I'll try to tidy up and send there. Thanks!</p>

#### [ Simon Hudon (Aug 07 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/emacs%20tip%3A%20filladapt/near/131063330):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>


{% endraw %}
