---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47066Listofleanrepositories.html
---

## Stream: [general](index.html)
### Topic: [List of lean repositories](47066Listofleanrepositories.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 08 2019 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/List%20of%20lean%20repositories/near/154635935):
At bim.shef.ac.uk/lean I have placed a list of the 293 github repositories using Lean, which may be of interest.  I have code to update it automatically using the github API, and at some point I will schedule that to run regularly.  By hand I have divided the repositories into crude categories: maths, computer science, teaching, infrastructure, obsolete and scratch space.  There are various extensions that one could think of:
1. One could attach comments to the list.  I have a very basic framework for that but have not used it yet.
1. One could attach more structured metadata, such as codes from the Mathematics Subject Classification, links to relevant papers in the arxiv or pages on Wikipedia etc
1. One could automatically clone everything and attempt to build it.  Probably lots of builds would fail.
1. One could build an unintelligent text-based search engine.
1. One could ask Lean to parse everything and build a more intelligent search engine based on the parse tree.  I don't know how to ask Lean to give me the parse tree.  I don't know whether there is code that can be stolen from the VS Code extension to help with this.
1. One could try to convert the Lean code to HTML with syntax highlighting and  links, as with coqdoc.  Again, I do not know whether there is existing code that  could help with that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joseph Corneli (Jan 08 2019 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/List%20of%20lean%20repositories/near/154647072):
```quote
At bim.shef.ac.uk/lean I have placed a list of the 293 github repositories using Lean, which may be of interest.   I have code to update it automatically using the github API, and at some point I will schedule that to run regularly. 
```
Nice - perhaps a good idea to create a repo for people to contribute features like the 1-6 on your list?


{% endraw %}
