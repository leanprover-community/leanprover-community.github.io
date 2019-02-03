---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74341metagetalistofalldefinitioninafile.html
---

## Stream: [general](index.html)
### Topic: [(meta) get a list of all definition in a file](74341metagetalistofalldefinitioninafile.html)

---


{% raw %}
#### [ Zesen Qian (Aug 14 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130403):
<p>Hi, is it possible in meta-programming to get a list of all (non-meta) definitions in a file?</p>

#### [ Simon Hudon (Aug 14 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130541):
<p>Yes. There are three parts to this: listing (or folding over) the visible definitions, determining that they are from the current file and determining whether they are definitions.</p>

#### [ Zesen Qian (Aug 14 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130754):
<p>I guess the hard part is the first then. I browsed thorough tactic.lean and didn't find anything interesting.</p>

#### [ Simon Hudon (Aug 14 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130776):
<p>In <code>init.meta.environment</code>, you can find <code>environment.fold</code>. It doesn't give you a list but it lets you iterate over all the definitions of a file and accumulate them. <code>get_env</code> gives you the current environment and <code>in_current_file'</code> tells you if a given name is defined / declared in the current file and finally, you can look at the <code>declaration</code> data structure and see the <code>trusted</code> bit for <code>definition</code> and <code>constant</code>.</p>

#### [ Zesen Qian (Aug 14 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132130792):
<p>that is very helpful. Thanks!</p>

#### [ Simon Hudon (Aug 14 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%28meta%29%20get%20a%20list%20of%20all%20definition%20in%20a%20file/near/132131037):
<p>You're welcome!</p>


{% endraw %}
