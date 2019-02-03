---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72316resolvinganame.html
---

## Stream: [general](index.html)
### Topic: [resolving a name](72316resolvinganame.html)

---


{% raw %}
#### [ Keeley Hoek (Sep 11 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714444):
<p>Say I've got <code>n : name</code>, which I get passed, but would like to be of type <code>my_type</code>.  I know I can use <code>t &lt;- infer_type n</code> to get the type of the identifier pointed to by <code>n</code>, and then can use an if to guard against the type being wrong. But I'd really like to do more and "cast" <code>n</code> to type <code>my_type</code>, getting some <code>inst : my_type</code> from <code>n</code>.  Would anyone be able to point me to a nice/any facility for doing this? (I've grepped for <code>cast</code> without success, is <code>mk_app</code> what I'm looking for?)</p>

#### [ Mario Carneiro (Sep 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714683):
<p>I don't quite understand the setup here. How does <code>my_type</code> relate to <code>n</code>?</p>

#### [ Keeley Hoek (Sep 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714858):
<p>Sorry: secretly in some file a user wrote <code>def foo : my_type := blah</code>, and then in tactic mode later on they called my code <code>cast_fn `(foo) </code>. So here <code>n = `foo</code>, and I'd like <code>cast_fn</code> to be of type <code>name -&gt; tactic my_type</code>.</p>

#### [ Keeley Hoek (Sep 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714912):
<p>Maybe my attempt at an MWE confused the issue. I'm getting a <code>name</code> in an attribute handler, and I expect what was annotated to be of a particular type. I'd like to get the actual thing that was annotated and call a function on it.</p>

#### [ Mario Carneiro (Sep 11 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714916):
<p><code>eval_expr</code> is what you want</p>

#### [ Keeley Hoek (Sep 11 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133714953):
<p>Right. So to invoke it, I only get to pass a single <code>expr</code>, so I figure I need to convert the name of the function I want to call into an <code>expr</code> and then create a <code>expr</code> which says "evaluate the function at the first <code>expr</code>". How can I build such an <code>expr</code>?</p>

#### [ Keeley Hoek (Sep 11 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715275):
<p>Ah. I think <code>eval_expr my_type (expr.app `(my_fn) n)</code> does the job!</p>

#### [ Keeley Hoek (Sep 11 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715292):
<p>Ok, so the point of <code>mk_app</code> is that I don't need to know the type beforehand? Right.</p>

#### [ Mario Carneiro (Sep 11 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715294):
<p><code>mk_const</code> will turn a name into an <code>expr</code></p>

#### [ Kevin Buzzard (Sep 11 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715409):
<p>This whole area is just screaming out for a small pdf or web page containing 10 very basic examples followed by 10 very basic questions.</p>

#### [ Patrick Massot (Sep 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133715483):
<p>What happened to <span class="user-mention" data-user-id="121918">@Edward Ayers</span>? He started to write such documentation and then vanished? Is there a meta-documentation curse?</p>

#### [ Keeley Hoek (Sep 11 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133722360):
<p>What does the <code>local</code> in <code>local attribute ...</code> mean?</p>

#### [ Kenny Lau (Sep 11 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133722435):
<p><a href="https://en.wikipedia.org/wiki/Scope_(computer_science)" target="_blank" title="https://en.wikipedia.org/wiki/Scope_(computer_science)">https://en.wikipedia.org/wiki/Scope_(computer_science)</a></p>

#### [ Kevin Buzzard (Sep 11 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133722660):
<p>I <em>think</em> it means "it's an attribute for this <code>.lean</code> file only" in this case, but I'm certainly not an expert.</p>

#### [ Johan Commelin (Sep 11 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133723327):
<p>Well, even "this <code>section</code> only"</p>

#### [ Keeley Hoek (Sep 11 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133730395):
<p>Haha thanks Kenny, I've written a fair few curly-braces in my time!</p>
<p>In that case does anyone know if the <code>before_unset</code> member of <code>user_attribute</code> is ever actually called when a <code>local</code> attribute is removed for the reason that a section has ended? It seems that it is not, which I find very strange.</p>

#### [ Keeley Hoek (Sep 11 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133730604):
<p>It seems that the none of mathlib and only one file in the lean library itself uses the feature, and this is in <code>library/init/meta/smt/ematch.lean</code> where <code>before_unset</code> is defined to do nothing anyway.</p>

#### [ Keeley Hoek (Sep 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133730914):
<p>It seems that <code>tactic.unset_attribute</code> does perform the unsetting... Perhaps this is a bug in lean?</p>

#### [ Sebastian Ullrich (Sep 11 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133746407):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> "Unsetting" an attribute means using <code>attribute [-simp] ...</code>, not just leaving the scope of a local attribute declaration</p>

#### [ Keeley Hoek (Sep 11 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/133746476):
<p>fair enough!</p>

#### [ Edward Ayers (Sep 17 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089643):
<p>Hi I've been on hols.</p>

#### [ Patrick Massot (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089683):
<p>Welcome back!</p>

#### [ Kevin Buzzard (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089684):
<p>We thought you were dead!</p>

#### [ Kevin Buzzard (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089686):
<p>We were worried</p>

#### [ Patrick Massot (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089692):
<p>Or worse than dead: decided to use another proof assistant</p>

#### [ Edward Ayers (Sep 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089697):
<p>I was flirting with Isabelle again a bit</p>

#### [ Johan Commelin (Sep 17 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089761):
<p>Lol, I knew that <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span> was coming...</p>

#### [ Johannes Hölzl (Sep 17 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089764):
<p>hehe</p>

#### [ Patrick Massot (Sep 17 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resolving%20a%20name/near/134089767):
<p>Scott, did we understand correctly what you learned in Dagstuhl?</p>


{% endraw %}
