---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09501Tacticblockcachingexample.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Tactic block caching example](https://leanprover-community.github.io/archive/113488general/09501Tacticblockcachingexample.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Feb 02 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157414492):
<p>Hey everyone, first day back (after a whiiile) and I finally put together an example for the tactic-block caching stuff that people can try out. All you have to do is clone <a href="https://github.com/khoek/leancache-example.git" target="_blank" title="https://github.com/khoek/leancache-example.git">https://github.com/khoek/leancache-example.git</a> (and make sure you have elan), and examine the <code>somemaths-xxx.lean</code> file in <code>src</code>. The files in there are shamelessly stolen from <code>lean-category-theory</code> and has a few statements which take a full 1- or 2-seconds to recompile normally (at least on my machine). You can turn caching on and off in the file by including <code>tactic.tcache.enable</code> (as stated there), as well as clear the cache and/or turn on some tracing to compare the performance with and without caching the proofs.</p>
<p>Full disclosure: <code>leancache</code> as implemented uses a 50-line changed fork of lean <code>3.4.2</code> (which will be auto-fetched by elan and is why it's necessary). It doesn't have to do this at all (as in, I've got an implementation which runs in vanilla lean too), but using the fork leads to a factor of 500-1000 performance speedup, so I think it's a pretty good idea. This is compared to a simple in-lean serializer which is also in that repo and I can explain how to try out if people want.</p>

#### [ Keeley Hoek (Feb 02 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157414494):
<p>To be clear, the fork just provides IO and serializing help, and does not have anything to do with saving and restoring the proofs. The addition to lean in the fork is simply the following: I add two functions in the <code>io</code> namespace called <code>io.serialize</code> and <code>io.deserialize</code> which write and read an <code>expr</code> to a file (respectively). This lets us leverage lean's already existing serialization facility (which is C++ and fast), and also avoids problems doing IO inside lean, especially manipulating char buffers which it turns out is very difficult and definitely hacky if you don't want to be slow (I've spent quite a lot of time trying to get this latter thing fast actually, but my attempts have been quite fruitless compared to just using the existing C++ code).</p>

#### [ Mario Carneiro (Feb 02 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157414564):
<p>aha, this sounds similar to my own experience with the olean reader in lean</p>

#### [ Mario Carneiro (Feb 02 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157414565):
<p>deserialization is still hella slow</p>

#### [ Keeley Hoek (Feb 02 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157414683):
<p>Yeah... :( Turns out (at least for me) parsing using a string.iterator is slower that using pattern-matching to munch byte-by-byte, too!</p>

#### [ Mario Carneiro (Feb 02 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157414803):
<p>I should mention that with the recent move for mathlib I've returned to seriously considering a lean fork (a.k.a LTS for lean 3)</p>

#### [ Keeley Hoek (Feb 02 2019 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157415350):
<p>Mario... if we did that... god forbid we would be able to do all this new stuff... legit-ly</p>

#### [ Keeley Hoek (Feb 02 2019 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157415351):
<p>:D</p>

#### [ Kevin Buzzard (Feb 02 2019 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157415641):
<p>My impression is that when 3.4.2 came out, the community (at least those at my end) just upgraded Lean and got on with it. In fact the moment mathlib head switched to 3.4.2 the users basically had no choice, but with elan the upgrade procedure can be pretty painless, and Scott's videos seem to make sense to people.</p>

#### [ Chris Hughes (Feb 02 2019 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20block%20caching%20example/near/157421915):
<p>With elan you don't even notice the change.</p>


{% endraw %}
