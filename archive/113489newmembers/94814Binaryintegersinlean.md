---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/94814Binaryintegersinlean.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Binary integers in lean](https://leanprover-community.github.io/archive/113489newmembers/94814Binaryintegersinlean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ cbailey (Nov 15 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147753615):
<p>WRT reasoning about programs, Is there any reason to use the binary integer representations in Mathlib ala ZArith in Lean outside of reasoning about bitwise operations? It says in the comments that their use is discouraged since Lean doesn't share Coq's reliance on kernel reduction; does Lean have some evaluation strategy for making functions written with Z and N run in non-linear time? Thanks for any help!</p>

#### [ Kenny Lau (Nov 15 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147764557):
<p>so if you try to use <code>norm_num</code> to prove that <code>10+11=21</code> for real numbers, they use bitwise addition</p>

#### [ Andrew Ashworth (Nov 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147768966):
<p>Lean's kernel has special optimized versions of nat and int when used with <code>#eval</code></p>

#### [ Andrew Ashworth (Nov 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147768982):
<p>iirc</p>

#### [ Andrew Ashworth (Nov 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147769022):
<p>if you're trying to do meta-programming or reflection, then use zarith</p>

#### [ cbailey (Nov 15 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Binary%20integers%20in%20lean/near/147780590):
<p>Thank you.</p>


{% endraw %}
