---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/44625Guineapigswanted.html
---

## Stream: [Lean Together 2019](https://leanprover-community.github.io/archive/179818LeanTogether2019/index.html)
### Topic: [Guinea pigs wanted!](https://leanprover-community.github.io/archive/179818LeanTogether2019/44625Guineapigswanted.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Gabriel Ebner (Jan 11 2019 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154915324):
<p>Due to popular demand, I hacked up something in the vscode extension.  Interested victims can now build the git version of the extension and try out ctrl+shift+p "open documentation view" and then try "try it!".</p>

#### [ Bryan Gin-ge Chen (Jan 11 2019 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154924079):
<p>This is cool! I did miss having a button or command to navigate "back" in the history of the documentation viewer. Adding that might involve having to write a history feature, though. An alternative might be just to add links at the top of the webview to the manual and TPIL and to  somehow change the CSS so that the section navigation sidebar is more accessible, since for me the editor width is usually narrow enough that I have to scroll to the bottom to see it.</p>

#### [ Patrick Massot (Jan 11 2019 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154946429):
<p>When I launch the debugger mode to use this new feature it tells me "Activating extension 'jroesch.lean' failed: Cannot find module 'axios'."</p>

#### [ Patrick Massot (Jan 11 2019 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154946671):
<p>Oh, I forgot to <code>npm install</code>, sorry about the noise</p>

#### [ Patrick Massot (Jan 11 2019 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154947031):
<p>It is awesome <span class="emoji emoji-1f62e" title="open mouth">:open_mouth:</span></p>

#### [ Patrick Massot (Jan 11 2019 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154947296):
<p>I agree with Bryan that it would be even better with a navigation history. But more importantly it would be much better if the hardcoded  list of books could be extended by typing in urls. This way Kevin (who is already using Sphynx) could tell people to try his url. It would be also very nice to allow using a local download so that we can continue learning Lean offline</p>

#### [ Patrick Massot (Jan 11 2019 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154947751):
<p>For people who didn't follow the story, I should add that this feature is something I've requested on the bus this morning around 8:45. Then Gabriel attended the documentation discussion sessions between 9 and 10:30, when I requested it again, and was seconded by popular clamor. And this was added to the VScode extension at 13:59. That's how efficient Gabriel is.</p>

#### [ Mario Carneiro (Jan 11 2019 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154948170):
<p>Can someone say what the feature does?</p>

#### [ Patrick Massot (Jan 11 2019 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/154948276):
<p>It open either TPIL or the reference manual in VScode, as you would see it online. But when you click the little "Try it!" links it opens the Lean file in VScode which then uses your local install of Lean instead of the javascript one!</p>

#### [ Patrick Massot (Jan 14 2019 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/Guinea%20pigs%20wanted%21/near/155090073):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> if you need more guinea pigs then I guess you should ask on the general stream</p>


{% endraw %}
