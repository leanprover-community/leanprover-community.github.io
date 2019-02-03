---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/14315431applytoadditiverecursively.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#431 apply `to_additive` recursively](https://leanprover-community.github.io/archive/144837PRreviews/14315431applytoadditiverecursively.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 30 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23431%20apply%20%60to_additive%60%20recursively/near/148869284):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Somehow I missed this PR, but it looks awesome! Kudos <span class="emoji emoji-1f419" title="octopus">:octopus:</span> <span class="emoji emoji-1f389" title="tada">:tada:</span> <br>
Too bad that Travis is saying that there is some error:</p>
<div class="codehilite"><pre><span></span>The command &quot;leanpkg test&quot; exited with 1.
20.65s$ lean --recursive --export=mathlib.txt
/home/travis/build/leanprover/mathlib/data/finsupp.lean:246:0: error: type mismatch at application
  @prod.equations._eqn_1 α β γ (@add_monoid.to_has_zero β _inst_3) _inst_4
term
  _inst_4
has type
  add_comm_monoid γ
but is expected to have type
  comm_monoid γ
&lt;unknown&gt;:1:1: error: type mismatch at application
  finsupp.prod.equations._eqn_1 α β γ (add_monoid.to_has_zero β _inst_3) _inst_4
term
  _inst_4
has type
  add_comm_monoid γ
but is expected to have type
  comm_monoid γ
</pre></div>

#### [ Simon Hudon (Nov 30 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23431%20apply%20%60to_additive%60%20recursively/near/148869890):
<p>Thanks :) I have put it on hold for now. There was a strange rabbit hole right in the model. I'll see if I can get back to it next time I need to procrastinate</p>


{% endraw %}
