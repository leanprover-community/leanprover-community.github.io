---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00960Rustverificationworkinggroup.html
---

## Stream: [general](index.html)
### Topic: [Rust verification working group](00960Rustverificationworkinggroup.html)

---


{% raw %}
#### [ Simon Hudon (Apr 15 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125118534):
<p>Did anybody else see this:</p>
<p><a href="https://github.com/rust-lang-nursery/wg-verification" target="_blank" title="https://github.com/rust-lang-nursery/wg-verification">https://github.com/rust-lang-nursery/wg-verification</a><br>
<a href="https://gitter.im/rust-lang/wg-verification" target="_blank" title="https://gitter.im/rust-lang/wg-verification">https://gitter.im/rust-lang/wg-verification</a></p>
<p>There seems to be an official verification working group for Rust. It might be a great opportunity to promote Lean</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125119134):
<p>I think Lean is not quite there yet :(. (Mostly due to stability.)</p>

#### [ Simon Hudon (Apr 15 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125119986):
<p>You think we should just wait before getting started in that direction?</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120025):
<p>I do. I have a feeling that Rust wants something more... ready?</p>

#### [ Simon Hudon (Apr 15 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120032):
<p>That makes sense but my impression from the group is that there is a wide variety of approaches. The Iris / RustBelt project seems to be the major one but they seem to encourage diversity rather than try to settle on a single verification approach</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120079):
<p>Perhaps you're right. I think Jared contributes to Rust so mayhap he's already brought it to their attention then?</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120083):
<p>Btw, in spite of the fact that I've been writing Lean exclusively for a few months now (and dropping Coq), if I were to start an industrial project right now I would choose Coq.</p>

#### [ Simon Hudon (Apr 15 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120135):
<p>That makes sense. The infrastructure is far more mature. I think it will take a while for Lean to catch up. It seems to me that 1) it can happen and 2) when / if it does, Lean will be a more approachable solution to start hacking with.</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120175):
<p>I completely agree. Really the notation is just more important than the Coq community realizes and Lean has just the right amount (as opposed to Agda who have gone <em>way</em> too far in the notational direction).</p>

#### [ Simon Hudon (Apr 15 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120226):
<p>I agree. I feel like organizing the libraries around type classes instead of module / functor also makes them far more usable.</p>

#### [ Simon Hudon (Apr 15 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120232):
<p>I guess the point of already starting on verification project is slowly catching up to the Coq infrastructure</p>

#### [ Simon Hudon (Apr 15 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120236):
<p>I wonder if it's realistic to hope for a sort of FFI between Lean and Coq</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120237):
<p>Typeclasses are sweet. Also I've grown accustomed to using the decidable trick to use the same function in decidable and potentially undecidable contexts. It's so awkward to always do <code>if band</code> in Coq. (Although I believe Lean wants to actually drop this particular use case? Which is saddening.)</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120280):
<p>I want FFI to C, Idris style.</p>

#### [ Simon Hudon (Apr 15 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120286):
<blockquote>
<p>It's so awkward to always do if band in Coq.</p>
</blockquote>
<p>YES! It took me a while to appreciate that but it's incredible.</p>

#### [ Simon Hudon (Apr 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120332):
<blockquote>
<p>Although I believe Lean wants to actually drop this particular use case?</p>
</blockquote>
<p>Are you referring to <code>ite</code> taking a <code>bool</code> instead of a decidable <code>Prop</code>? I think all that it will do is shift the use of <code>decidable</code> from <code>ite</code> to the coercion from your proposition to bool. I think it's too useful and pretty to drop.</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120335):
<p>Oh, yes I was referring to that but clearly I had misunderstood then.</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120336):
<p>So we're keeping the trick.</p>

#### [ Simon Hudon (Apr 15 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120377):
<blockquote>
<p>I want FFI to C, Idris style.</p>
</blockquote>
<p>Multiple FFIs might be required. Specifically, a FFI to Coq would be really cool if it allowed us to reuse Coq theorems and tactics. That might mean we can use Iris in Lean for example.</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120382):
<p>Give me Omega finally :).</p>

#### [ Simon Hudon (Apr 15 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120383):
<p>:D</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120430):
<p>It might seem primitive but it even solves goals that I don't find immediately obvious once the set of (in)equalities is big enough.</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120438):
<p>Can't wait to see what Lean 7 will bring.</p>

#### [ Simon Hudon (Apr 15 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120440):
<p>Why Lean 7?</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120490):
<p>Why not 7 :)? We're at 4 soon!</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120492):
<p>Surely 7 will be better than 6.</p>

#### [ Simon Hudon (Apr 15 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120494):
<p>I hear it won't be quite as good as 8 or 9 ...</p>

#### [ Moses Schönfinkel (Apr 15 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120496):
<p>Yeah but I think 7 strikes the right balance between the wait time and quality.</p>

#### [ Simon Hudon (Apr 15 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125120536):
<p>Makes sense ... plus: it's a prime number, it's bound to be of prime quality too :D</p>

#### [ Sean Leather (Apr 17 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125185304):
<p>Folks, you need to slow down. Wait until Lean 4 is unfinished before starting on the next version.</p>

#### [ Johan Commelin (Apr 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125186087):
<p>But Lean 4 is currently unfinished!</p>

#### [ Sean Leather (Apr 17 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rust%20verification%20working%20group/near/125186180):
<p>Ah ha. Therein lies the quandary...</p>


{% endraw %}
