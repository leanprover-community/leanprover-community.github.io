---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/81623pfilter.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [pfilter](https://leanprover-community.github.io/archive/116395maths/81623pfilter.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johannes Hölzl (Nov 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/pfilter/near/147287895):
<p>@Mario</p>
<blockquote>
<p>I'm going to sleep now, but I've got something for you guys to puzzle over tomorrow: <a href="https://github.com/leanprover/mathlib/compare/master...leanprover-community:pfilter" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...leanprover-community:pfilter">leanprover-community/pfilter</a> is beginning work on generalizing filters to preorders. <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> if you have any ideas for how all your lifting and monad stuff works when separating the two levels of sets out, I'd like to hear it. I have not figured out what the new version of <code>join</code> has to do with the old one (which has a different type - <code>filter (filter A)</code> becomes <code>pfilter (set (pfilter A))</code> which is not obviously related to <code>pfilter (pfilter A)</code>, which is something new).</p>
</blockquote>
<p>I would be surprised if the monads on <code>filter</code> and <code>pfilter</code> are related. For me the monad of filter is not what is expected (one gets the wrong products), but <code>applicative</code> is a nice structure. I don't know about <code>pfilter</code>...</p>


{% endraw %}
