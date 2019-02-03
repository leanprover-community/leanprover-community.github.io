---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25766Userdefinableoptions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [User definable options](https://leanprover-community.github.io/archive/113488general/25766Userdefinableoptions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Joe Hendrix (Jan 12 2019 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/154955190):
<p>Is there a way that I can set user definable options that can be parsed by tactics?  I have some proofs that take a while to run, and I'd like to be able to have an option at the file or lean package level that let me configure whether they ran or not.  e.g., during interactive development I disable proofs I'm not actually working on, but in a regression test they are enabled.<br>
I noticed within a single run of the tactic monad, I can set custom option names (e.g., <code>set_options (opt.set_bool "enable_unsafe_tac" tt)</code>), but the value doesn't appear to show up in tactics farther down the file.  The set_option command also doesn't allow custom options.</p>

#### [ Sebastian Ullrich (Jan 12 2019 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/154982882):
<p><code>set_option</code> accepts only built-in options, but using the <code>set_options</code> primitive should work. Did you execute that code in a <code>run_command</code>?</p>

#### [ Joe Hendrix (Jan 22 2019 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156639542):
<p>Sorry for the delay; I didn't see this until today.  Here's a sample script:</p>
<div class="codehilite"><pre><span></span>open tactic

meta
def get_my_opt : tactic unit := do
  o ← get_options,
  trace (repr (o.get_bool &quot;foo&quot; ff))

meta
def set_my_opt : tactic unit := do
  o ← get_options,
  set_options (o.set_bool &quot;foo&quot; tt),
  get_my_opt

run_cmd get_my_opt
run_cmd set_my_opt
run_cmd get_my_opt
</pre></div>


<p>The output I get is:</p>
<div class="codehilite"><pre><span></span>ff
tt
ff
</pre></div>


<p>So <code>set_options</code> works in the current command, but the option is forgotten in subsequent commands.</p>

#### [ Sebastian Ullrich (Jan 22 2019 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156642096):
<p>Ah, that's too bad. You may want to fake the option with a custom attribute (which can be set globally or locally, but unset only locally). I'm not aware of a better solution.</p>

#### [ Joe Hendrix (Jan 22 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156643580):
<p>Thanks, that seems to work well.</p>

#### [ Mario Carneiro (Jan 22 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156644445):
<p>Is this improving in lean 4? More generally, it would be nice if there was a way to persist arbitrary data across different commands. Does everything have to go via adding defs to the environment?</p>

#### [ Joe Hendrix (Jan 23 2019 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/User%20definable%20options/near/156665743):
<p>I could see use cases for persisting data, but I also think it's important that tactics could be run concurrently, and the results cached.  Given that goal, <code>set_options</code> behavior  doesn't seem to surprising.<br>
In Haskell, you can define package level options and use them to define constants that can be checked at compile time (via CPP).  That's what I was hoping for here, so I could pass a flag to build or configure that controlled whether an axiom was allowed to be used.  The attribute trick doesn't seem too bad though.</p>


{% endraw %}
