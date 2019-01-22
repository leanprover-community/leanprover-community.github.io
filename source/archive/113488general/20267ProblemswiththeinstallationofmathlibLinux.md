---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20267ProblemswiththeinstallationofmathlibLinux.html
---

## [general](index.html)
### [Problems with the installation of mathlib (Linux)](20267ProblemswiththeinstallationofmathlibLinux.html)

#### [Bruno Bentzen (Oct 10 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135515887):
Hello,

I am trying to get mathlib working in a new package of mine. I did the following

  leanpkg new my_project
  cd my_project
  leanpkg add leanprover/mathlib

then I created a test.lean file with import group_theory.subgroup and then #check is_subgroup, and I run

  leanpkg build

but although I can see all .olean files in my_project/_target/deps/mathlib/group_theory/, I get the following error message in VS Code: 

"invalid import: group_theory.subgroup
 could not resolve import: group_theory.subgroup"

(although I heard that it is less crucial now, I also installed elan as described in https://github.com/leanprover/mathlib/blob/master/docs/elan.md).

After a few unsuccessful attempts, I decided to install mathlib globally instead with

  leanpkg install leanprover/mathlib

now I have all .olean files in ~/.lean/_target/deps/mathlib but I am still getting the same error.

Finally, I am using Ubuntu and VS Code works perfectly in other Lean projects without mathlib.

Any help would be greatly appreciated!

Best,
Bruno

#### [Bryan Gin-ge Chen (Oct 10 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135516395):
Hi Bruno, I'm guessing you didn't get any errors when you ran `leanpkg build` from the console? What happens if you run `lean test.lean` from the VS code console?

#### [Mario Carneiro (Oct 10 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135516646):
Make sure you have opened vscode to the folder "my_project"

#### [Bruno Bentzen (Oct 10 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135516827):
Hi Bryan and Mario! Thank you for your prompt response. I am sorry, I am a still a VS code newbie --- could you please tell me how do I run lean test.lean from the VS code console and how do I open VS code to the my_project folder?

#### [Bryan Gin-ge Chen (Oct 10 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135517351):
When you open VS Code, you can choose "Open folder" from the "File" menu, click on your `my_project` directory and press open.

To open a console in VS Code, choose "Terminal" from the "View" menu. That will open a terminal in the directory that you've opened in VS Code.

#### [Bruno Bentzen (Oct 10 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135519374):
Hi Bryan (and Mario), yes, opening the folder solved the issue! (I'm sorry for the silly question, by the way!)

#### [Scott Morrison (Oct 10 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135519800):
No problem! We're still sorting out the document and tutorials for these things, so it's great to have questions, so we know what needs to be said!

#### [Bruno Bentzen (Oct 10 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135519874):
I see, Scott! Thank you guys!

#### [Kevin Buzzard (Oct 10 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135520320):
```quote
Hi Bryan (and Mario), yes, opening the folder solved the issue! (I'm sorry for the silly question, by the way!)
```
It's not a silly question at all -- in fact it's a valuable data point! The community is currently desperately trying to get some comprehensible and failsafe instructions up and running.

#### [Bruno Bentzen (Oct 10 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problems%20with%20the%20installation%20of%20mathlib%20%28Linux%29/near/135522854):
I am glad to hear that, thanks Kevin! :)

