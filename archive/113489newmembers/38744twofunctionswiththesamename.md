---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/38744twofunctionswiththesamename.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [two functions with the same name](https://leanprover-community.github.io/archive/113489newmembers/38744twofunctionswiththesamename.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ali Sever (Aug 10 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229114):
<p>Is there a reason why lean doesn't let me make two functions with the same name? Even if they take different arguments?</p>

#### [ Chris Hughes (Aug 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229303):
<p>It's confusing, and could even lead to people thinking they've proved something, when they've actually proved something about a function with the same name. You can always use namespaces.</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229312):
<p>You can have two functions in different namespaces with the same name, where both namespaces are open at once, and lean will use the type to disambiguate</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229383):
<p>The basic reason why is because lean needs a name for the function, one that is not ambiguous, and if you overload it what will that name be? How can you refer to it precisely?</p>

#### [ Ali Sever (Aug 10 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229559):
<p>I know I should be using Pi types for this sort of thing, but my two functions take in a different amount of arguments, so I think I might have to use if then else.</p>

#### [ Mario Carneiro (Aug 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229802):
<p>You can also use default values and optional arguments to make a single definition have varying number of arguments</p>

#### [ Kevin Buzzard (Aug 10 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131233997):
<p>Also note that <code>+</code> is kind of like several functions with the same name -- and looking at the types of the inputs is exactly how Lean decides which function to actually use.</p>


{% endraw %}
