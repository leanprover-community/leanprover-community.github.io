---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/38744twofunctionswiththesamename.html
---

## Stream: [new members](index.html)
### Topic: [two functions with the same name](38744twofunctionswiththesamename.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Aug 10 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229114):
Is there a reason why lean doesn't let me make two functions with the same name? Even if they take different arguments?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229303):
It's confusing, and could even lead to people thinking they've proved something, when they've actually proved something about a function with the same name. You can always use namespaces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229312):
You can have two functions in different namespaces with the same name, where both namespaces are open at once, and lean will use the type to disambiguate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229383):
The basic reason why is because lean needs a name for the function, one that is not ambiguous, and if you overload it what will that name be? How can you refer to it precisely?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Aug 10 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229559):
I know I should be using Pi types for this sort of thing, but my two functions take in a different amount of arguments, so I think I might have to use if then else.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131229802):
You can also use default values and optional arguments to make a single definition have varying number of arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 10 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/two%20functions%20with%20the%20same%20name/near/131233997):
Also note that `+` is kind of like several functions with the same name -- and looking at the types of the inputs is exactly how Lean decides which function to actually use.


{% endraw %}
