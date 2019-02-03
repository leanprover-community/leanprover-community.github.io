---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84434addingadefinition.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [adding a definition](https://leanprover-community.github.io/archive/113488general/84434addingadefinition.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Sep 14 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133939240):
<p>I'd like implement a <code>[user_command]</code> which adds a definition to the environment at the place where the <code>[user_command]</code> is executed. Of course, there is <code>environment.add</code>, but I have to build a <code>declaration</code> and in particular pass a <code>name</code>. This won't act the same way as writing <code>def blah : type = foo ...</code> on that line because the latter will have a "full name" <code>me.my_namespace.blah</code> if this all goes on inside <code>namespace me.my_namespace</code>. Is there a way to fix this: either to get the current namespace, or to make a declaration as if it happened using a <code>def</code>?</p>

#### [ Mario Carneiro (Sep 14 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133939576):
<p><span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span></p>

#### [ Mario Carneiro (Sep 14 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133939698):
<p>there is a command <code>get_current_definition</code> that tells you the name of the currently elaborating definition, from which you can derive the namespaces, but it doesn't work in a user command</p>

#### [ Keeley Hoek (Sep 14 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133942021):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Hallelujah! According to the source code (see <code>src/library/tactic/tactic_state.cpp</code>), it turns out that the first element returned by <code>open_namespaces</code> is <em>always</em> the namespace of the current line, as long as you're in a command! WHOOP WHOOP</p>

#### [ Keeley Hoek (Sep 14 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133942101):
<p>*as long as youre being run in <em>some</em> namespace, but of course there is a hack to check if this is the case...</p>

#### [ Scott Morrison (Sep 14 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133943119):
<p>This will probably all break again in <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span>, but I guess we'll cope. :-)</p>

#### [ Keeley Hoek (Sep 14 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133947033):
<p>Ok I was wrong again because my "easy hack" to check you're in the default namespace doesn't work and I can't fix it. But, I just discovered <code>with_input command_like</code> in the <code>lean.parser</code> monad. It's a backdoor into.... everything! So I can just emit <code>def blah : type = blah</code> from the command!</p>

#### [ Keeley Hoek (Sep 14 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133947101):
<p>---no silly hack required!</p>

#### [ Scott Morrison (Sep 14 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133947786):
<p>oooh... can we add <code>rfl</code> lemmas from commands using this??</p>

#### [ Keeley Hoek (Sep 14 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948698):
<p>Yes, you can do anything</p>

#### [ Keeley Hoek (Sep 14 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948710):
<p>It saves the current parser state, then literally hands a string to the parser as if it was the next line of the file, then restores it</p>

#### [ Keeley Hoek (Sep 14 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948714):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span></p>

#### [ Keeley Hoek (Sep 14 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948766):
<p>Ill cook up a demo</p>

#### [ Scott Morrison (Sep 14 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948866):
<p>I've been wanting to do that for a while; I have lots of boilerplate <code>rfl</code> lemmas that just repeat a structure field.</p>

#### [ Scott Morrison (Sep 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133948933):
<p>I do wonder whether this is a good idea, considering <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span>, but I'm still tempted.</p>

#### [ Keeley Hoek (Sep 14 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133949017):
<p>when it comes time we could always turn on printing what the command outputs and go and replace them with their content<br>
or every write a script to if there are lots</p>

#### [ Keeley Hoek (Sep 14 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133949024):
<p>what needs to go in and what needs to come out?</p>

#### [ Scott Morrison (Sep 14 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133949122):
<p>Here's a prototypical example:</p>
<div class="codehilite"><pre><span></span>def equivalence_inverse (F : C ⥤ D) [full F] [faithful F] [ess_surj F] : D ⥤ C :=
{ obj  := λ X, F.obj_preimage X,
  map&#39; := λ X Y f, F.preimage ((F.fun_obj_preimage_iso X).hom ≫ f ≫ (F.fun_obj_preimage_iso Y).inv),
  map_id&#39; := λ X, begin apply F.injectivity, obviously, end,
  map_comp&#39; := λ X Y Z f g, begin apply F.injectivity, obviously, end }.

-- FIXME pure boilerplate...
@[simp] private lemma equivalence_inverse_map
  (F : C ⥤ D) [full F] [faithful F] [ess_surj F]
  {X Y : D} (f : X ⟶ Y) : (equivalence_inverse F).map f = F.preimage ((F.fun_obj_preimage_iso X).hom ≫ f ≫ (F.fun_obj_preimage_iso Y).inv) := rfl.
</pre></div>

#### [ Scott Morrison (Sep 14 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133949131):
<p>I would like to write: <code>generate_rfl_lemma equivalence_inverse map</code></p>

#### [ Keeley Hoek (Sep 14 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951214):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> ok I think I can do that, just sorry, who is getting rid of the primes on (e.g.) <code>map'</code>? I've always wondered</p>

#### [ Scott Morrison (Sep 14 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951439):
<p>Yeah, that's a real hack. Unfortunately sometimes it's necessary to state something, and then restate it. (e.g. to clean up the mess that autoparam leaves, or to restate something using a coercion that can only be introduced later).</p>

#### [ Scott Morrison (Sep 14 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951460):
<p>The "convention" is now to at first name the declaration with a prime at the end of the name, and then to remove it for the "real" declaration.</p>

#### [ Scott Morrison (Sep 14 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951479):
<p>The <code>restate_axiom</code> user command does this.</p>

#### [ Scott Morrison (Sep 14 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951533):
<p>If it's not given an explicit new name, it inspects the old name, removes a prime if it finds one, and otherwise adds "_lemma".</p>

#### [ Keeley Hoek (Sep 14 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951769):
<p>And so you have to prove that what is generated is actually equal to what was there originally all the time?</p>

#### [ Keeley Hoek (Sep 14 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951865):
<p>Also, sorry going to cook it up now, just writing library functions and testing they work<br>
The only quirk is that when there is an attribute error, the red line appears on the first line of the file.... But I think there is a way to fix that maybe</p>

#### [ Keeley Hoek (Sep 14 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133951895):
<p>but we also have a command <code>suggestion category_theory</code> now</p>

#### [ Keeley Hoek (Sep 14 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133964431):
<p>I don't even think we need my thing to do this actually Scott, since we could always just put the lemma in the same namespace as wherever the parameter (e.g. <code>equivalence_inverse</code>) lives</p>

#### [ Keeley Hoek (Sep 14 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20a%20definition/near/133966107):
<p>I think I should talk to you more about what exactly it should do, since it seems hard to decide whether for example <code>{X Y : D}</code> in the above example should have curly brackets instead of parentheses.</p>


{% endraw %}
