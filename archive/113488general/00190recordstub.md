---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00190recordstub.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [record stub](https://leanprover-community.github.io/archive/113488general/00190recordstub.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Oct 20 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136169584):
<p>The hole command to create a record stub is really nice!<br>
Can any emacs gurus (<span class="user-mention" data-user-id="110026">@Simon Hudon</span>?) tell me how I can write an emacs command that will insert <code>{! !}</code> at the point, navigate inside it (if necessary), and then invoke the Instance Stub hole command?</p>

#### [ Simon Hudon (Oct 20 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183553):
<p>Sure :) Let's go step by step. In your configuration file (<code>.emacs</code> or <code>.emacs.d/init.el</code>), create a function, let's say:</p>
<div class="codehilite"><pre><span></span><span class="p">(</span><span class="nb">defun</span> <span class="nv">lean-insert-stub</span> <span class="p">()</span>
  <span class="p">(</span><span class="nf">print</span> <span class="s">&quot;hello world&quot;</span><span class="p">))</span>
</pre></div>

#### [ Simon Hudon (Oct 20 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183684):
<p>You can change it a little so that you can invoke it from anywhere in emacs:</p>
<div class="codehilite"><pre><span></span><span class="p">(</span><span class="nb">defun</span> <span class="nv">lean-insert-stub</span> <span class="p">()</span>
  <span class="p">(</span><span class="k">interactive</span><span class="p">)</span>
  <span class="p">(</span><span class="nf">print</span> <span class="s">&quot;hello world&quot;</span><span class="p">))</span>
</pre></div>


<p>Then, you just need <code>M-x lean-insert-stub</code> to invoke it.</p>

#### [ Simon Hudon (Oct 20 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183728):
<p>And if you want it to actually do something: </p>
<div class="codehilite"><pre><span></span><span class="p">(</span><span class="nb">defun</span> <span class="nv">lean-insert-stub</span> <span class="p">()</span>
  <span class="p">(</span><span class="k">interactive</span><span class="p">)</span>
  <span class="p">(</span><span class="nf">insert</span> <span class="s">&quot;{!  !}&quot;</span><span class="p">))</span>
</pre></div>

#### [ Reid Barton (Oct 20 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183809):
<p>I tried having it call <code>(lean-hole)</code> next but I got an error even though repositioning the cursor after the insert isn't necessary interactively</p>

#### [ Reid Barton (Oct 20 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183855):
<div class="codehilite"><pre><span></span>error in lean-server command handler: (wrong-type-argument number-or-marker-p nil)
Server response was:
</pre></div>

#### [ Simon Hudon (Oct 20 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183867):
<p>I'm looking at <code>lean-hole--command</code> instead</p>

#### [ Reid Barton (Oct 20 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136183935):
<p>It kind of looks like the lean mode is not designed to handle selecting a hole command non-interactively, in terms of the code structure</p>

#### [ Reid Barton (Oct 20 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136184005):
<p>Am I supposed to locally set this thing <code>completing-read-function</code>? Is that the "emacs way"?</p>

#### [ Reid Barton (Oct 20 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136184014):
<p>not that that helps, when it is not getting that far yet</p>

#### [ Simon Hudon (Oct 20 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136184074):
<p>Yeah, now that I look more closely, it's not obvious</p>

#### [ Simon Hudon (Oct 20 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/record%20stub/near/136184663):
<p>To be fair, I'm still new to emacs. Maybe <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> can shed some light. What I got so far is:</p>
<div class="codehilite"><pre><span></span><span class="p">(</span><span class="nb">defun</span> <span class="nv">lean-insert-stub</span> <span class="p">()</span>
  <span class="p">(</span><span class="k">interactive</span><span class="p">)</span>
  <span class="p">(</span><span class="nf">insert</span> <span class="s">&quot;{!  !}&quot;</span><span class="p">)</span>
  <span class="p">(</span><span class="nf">forward-char</span> <span class="mi">-3</span><span class="p">)</span>
  <span class="p">(</span><span class="k">let</span> <span class="p">((</span><span class="nv">p</span> <span class="p">(</span><span class="nf">point</span><span class="p">)))</span>
  <span class="p">(</span><span class="k">let</span> <span class="p">((</span><span class="nv">start-pos</span> <span class="nv">p</span><span class="p">)</span>
        <span class="p">(</span><span class="nv">end-pos</span> <span class="nv">p</span><span class="p">))</span>
    <span class="p">(</span><span class="k">let</span> <span class="p">((</span><span class="nv">start-marker</span> <span class="p">(</span><span class="nf">make-marker</span><span class="p">))</span>
          <span class="p">(</span><span class="nv">end-marker</span> <span class="p">(</span><span class="nf">make-marker</span><span class="p">)))</span>
      <span class="p">(</span><span class="nf">set-marker</span> <span class="nv">start-marker</span> <span class="nv">start-pos</span> <span class="p">(</span><span class="nf">current-buffer</span><span class="p">))</span>
      <span class="p">(</span><span class="nf">set-marker</span> <span class="nv">end-marker</span> <span class="nv">end-pos</span> <span class="p">(</span><span class="nf">current-buffer</span><span class="p">))</span>
      <span class="p">(</span><span class="nv">lean-hole--command</span> <span class="s">&quot;Instance Stub&quot;</span> <span class="nv">start-marker</span> <span class="nv">end-marker</span><span class="p">))))</span>
  <span class="p">)</span>
</pre></div>


<p>which I built from copying bits from <code>lean-hole</code></p>


{% endraw %}
