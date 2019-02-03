---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71101extendpresheaffrombasis.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [extend presheaf from basis](https://leanprover-community.github.io/archive/116395maths/71101extendpresheaffrombasis.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 10 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135529957):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Somehow this is not doing what I hoped:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">presheaves</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">sheaves</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="kn">open</span> <span class="n">category_theory</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">}}</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒱</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span> <span class="n">w</span><span class="o">}</span> <span class="n">V</span><span class="o">]</span> <span class="o">[</span><span class="n">has_limits</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span> <span class="n">w</span><span class="o">}</span> <span class="n">V</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒱</span>

<span class="n">def</span> <span class="n">extend</span> <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">B</span> <span class="n">V</span><span class="o">)</span> <span class="o">:</span>
<span class="n">presheaf</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="n">V</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">limit</span> <span class="o">((</span><span class="n">full_subcategory_embedding</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">U&#39;</span> <span class="o">:</span> <span class="n">B</span><span class="o">,</span> <span class="n">U&#39;</span><span class="bp">.</span><span class="mi">1</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">))</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
  <span class="n">map&#39;</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Oct 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530007):
<p>The embedding is complaining about universes. I don't get why.</p>

#### [ Scott Morrison (Oct 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530180):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, I'm just guessing here, but there are universe constraints in taking limits.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530263):
<p>I don't know anything about your errors but even seeing that you're daring to write this sort of code -- "extending a presheaf from a basis might be possible" -- makes me quite excited for the future.</p>

#### [ Scott Morrison (Oct 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530292):
<p>In particular, the index category is meant to be a category.{v v}, and the target category is meant to be a category.{u v}.</p>

#### [ Scott Morrison (Oct 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530306):
<p>If you don't satisfy those constraints to begin with, you're going to have to ulift.</p>

#### [ Scott Morrison (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530319):
<p>Me too, by the way --- I'm very excited to see things like this work!</p>

#### [ Johan Commelin (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530322):
<p>But it is looking for some <code>Type w</code>. I really don't know where it is getting that from?</p>

#### [ Johan Commelin (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530326):
<p>Do you have comma categories somewhere?</p>

#### [ Kevin Buzzard (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530327):
<p>One thing which might be obvious to everyone already is that of course when you extend, you don't literally "extend", you define a new object on all open sets, and its values on basic open sets are isomorphic to, but not defeq to, the values taken by the old object.</p>

#### [ Johan Commelin (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530330):
<p>I just want the category of opens contained in <code>U</code>.</p>

#### [ Johan Commelin (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530334):
<p>Maybe you already have this somewhere...</p>

#### [ Johan Commelin (Oct 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530386):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Do you want me to include the scare-quotes in the definition <span class="emoji emoji-1f606" title="lol">:lol:</span> ?</p>

#### [ Kevin Buzzard (Oct 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530402):
<p>I am just being reminded of the nightmares I had when doing sheaves by hand in the schemes project.</p>

#### [ Scott Morrison (Oct 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531230):
<p>Sorry, I will try to look at this soon. I'm working on installation instructions, still. :-)</p>

#### [ Scott Morrison (Oct 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531457):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> , is that code available somewhere? I'd like to look at the universe issue.</p>

#### [ Scott Morrison (Oct 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531508):
<p>(universes scare the bejeebus out of me, and I'm perpetually terrified that someone is going to discover I've still got them wrong in the category theory library)</p>

#### [ Reid Barton (Oct 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531525):
<p>You have made V a category.{v w} which means you can only form limits of size w</p>

#### [ Scott Morrison (Oct 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531577):
<p>(phew, that's Reid agreeing with me... my heart rate is dropping again. :-)</p>

#### [ Johan Commelin (Oct 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135532719):
<p>Hmmm, let me take another look.<br>
<span class="user-mention" data-user-id="110087">@Scott Morrison</span> All the code I have is what I posted above.</p>

#### [ Johan Commelin (Oct 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533061):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I still don't get what is wrong with my code.</p>

#### [ Johan Commelin (Oct 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533127):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Here is a snippet that is probably useful for <code>over.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">over</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒞</span>

<span class="n">def</span> <span class="n">over</span><span class="bp">.</span><span class="n">forget</span> <span class="o">(</span><span class="n">Z</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">:</span> <span class="n">over</span> <span class="n">Z</span> <span class="err">⥤</span> <span class="n">C</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span><span class="o">,</span> <span class="n">X</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
  <span class="n">map&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">X</span> <span class="n">Y</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span><span class="bp">.</span><span class="mi">1</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">over</span>
</pre></div>

#### [ Scott Morrison (Oct 10 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533245):
<p>Thanks, I added <code>over.forget</code>.</p>

#### [ Johan Commelin (Oct 10 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533671):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Ok, so I should take <code>X : Top.{w}</code>. It is important that I don't take <code>Top.{u}</code>. Can you explain why?</p>

#### [ Scott Morrison (Oct 10 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533722):
<blockquote>
<p>Reid Barton: You have made V a category.{v w} which means you can only form limits of size w</p>
</blockquote>

#### [ Johan Commelin (Oct 10 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533800):
<p>Ok... I don't think I care too much. It is a bit tricky to get right. I wouldn't mind if Lean just scaled everything into the right universe. But I guess that brings some tradeoff in foundations that I don't understand.</p>

#### [ Johan Commelin (Oct 10 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534835):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> May we <em>please</em> have presheaves be contravariant. My head is breaking without the <code>op</code>s.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534843):
<p>no problem</p>

#### [ Scott Morrison (Oct 10 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534855):
<p>We need to make a PR to mathlib to fix this, right?</p>

#### [ Johan Commelin (Oct 10 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534862):
<p>No, presheaves aren't in mathlib</p>

#### [ Johan Commelin (Oct 10 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534868):
<p>Or did you break the definition of <code>open_set</code>?</p>

#### [ Scott Morrison (Oct 10 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534920):
<p>Yes :-)</p>

#### [ Johan Commelin (Oct 10 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534931):
<p>Aaah, ok. Hmmz.</p>

#### [ Johan Commelin (Oct 10 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534940):
<p>Well... yes. Then we need a PR.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534954):
<p>Regarding automating the copy-and-paste: I really doubt this can work in most of my cases here, where the rewrites are occurring in auto_params for structure fields.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534963):
<p>The tactic <code>obviously</code> doesn't even appear.</p>

#### [ Johan Commelin (Oct 10 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535588):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I'm stuck on</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="o">(</span><span class="n">U₁</span> <span class="err">⟶</span> <span class="n">U₂</span><span class="o">)</span> <span class="bp">→</span> <span class="n">U₂</span><span class="bp">.</span><span class="n">s</span> <span class="err">⊆</span> <span class="n">U₁</span><span class="bp">.</span><span class="n">s</span>
</pre></div>


<p>After that we have extended presheaves.</p>

#### [ Johan Commelin (Oct 10 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535607):
<p>That goal looks like very trivial. But I don't know how to extract the inclusion from the hom.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535652):
<p>try <code>intro</code>, then <code>cases</code>?</p>

#### [ Johan Commelin (Oct 10 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535661):
<p>Aah <code>cases</code>.</p>

#### [ Scott Morrison (Oct 10 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535664):
<p>or commit something I can poke at</p>

#### [ Scott Morrison (Oct 10 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535697):
<p>remember that hom there is probably some ulift plift gadget</p>

#### [ Scott Morrison (Oct 10 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535704):
<p>to turn a Prop into a Type at whatever universe you're living in</p>

#### [ Johan Commelin (Oct 10 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535763):
<p>Right, it's working now. Except that it couldn't figure out <code>comp'</code> on its own <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Johan Commelin (Oct 10 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535779):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">presheaves</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">sheaves</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="kn">open</span> <span class="n">category_theory</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">section</span> <span class="n">extend</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="bp">.</span><span class="o">{</span><span class="n">w</span><span class="o">}}</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒱</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span> <span class="n">w</span><span class="o">}</span> <span class="n">V</span><span class="o">]</span> <span class="o">[</span><span class="n">has_limits</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span> <span class="n">w</span><span class="o">}</span> <span class="n">V</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒱</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)}</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="o">((</span><span class="bp">λ</span> <span class="n">U</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">,</span> <span class="n">U</span><span class="bp">.</span><span class="n">s</span><span class="o">)</span> <span class="err">&#39;&#39;</span> <span class="n">B</span><span class="o">))</span>

<span class="n">def</span> <span class="n">extend</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">B</span> <span class="n">V</span><span class="o">)</span> <span class="o">:</span>
<span class="n">presheaf</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="n">V</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">limit</span> <span class="o">((</span><span class="n">full_subcategory_embedding</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">U&#39;</span> <span class="o">:</span> <span class="n">B</span><span class="o">,</span> <span class="n">U&#39;</span><span class="bp">.</span><span class="mi">1</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">))</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
  <span class="n">map&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="n">ι</span><span class="o">,</span>
    <span class="n">limit</span><span class="bp">.</span><span class="n">lift</span> <span class="o">(</span><span class="n">full_subcategory_embedding</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">U&#39;</span> <span class="o">:</span> <span class="err">↥</span><span class="n">B</span><span class="o">),</span> <span class="n">U&#39;</span><span class="bp">.</span><span class="n">val</span> <span class="err">⊆</span> <span class="n">U₂</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span>
    <span class="o">{</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">limit</span> <span class="o">(</span><span class="n">full_subcategory_embedding</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">U&#39;</span> <span class="o">:</span> <span class="err">↥</span><span class="n">B</span><span class="o">),</span> <span class="n">U&#39;</span><span class="bp">.</span><span class="n">val</span> <span class="err">⊆</span> <span class="n">U₁</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
      <span class="n">π</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="k">begin</span> <span class="n">dsimp</span><span class="o">,</span>
      <span class="n">refine</span> <span class="n">limit</span><span class="bp">.</span><span class="n">π</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">U</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="n">U</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_⟩</span> <span class="err">≫</span> <span class="bp">_</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">cases</span> <span class="n">ι</span><span class="o">,</span> <span class="n">cases</span> <span class="n">ι</span><span class="o">,</span> <span class="n">exact</span> <span class="n">ι</span> <span class="o">},</span>
      <span class="o">{</span> <span class="n">exact</span> <span class="mi">𝟙</span> <span class="bp">_</span> <span class="o">}</span> <span class="kn">end</span> <span class="o">}</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">extend</span>
</pre></div>

#### [ Scott Morrison (Oct 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537106):
<p>Perhaps giving a name to <code>full_subcategory_embedding ...</code> will make this look nicer.</p>

#### [ Scott Morrison (Oct 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537134):
<p>I'd be curious to see that goals after <code>tidy</code> on <code>comp'</code>.</p>

#### [ Scott Morrison (Oct 10 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537207):
<p>I wonder if we need some extra help for posets here.</p>

#### [ Johan Commelin (Oct 10 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537749):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Here is what I have now:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">presheaves</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">sheaves</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="kn">open</span> <span class="n">category_theory</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">limits</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">section</span> <span class="n">under_set</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}}</span>

<span class="n">def</span> <span class="n">under_set</span> <span class="o">(</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">))</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">B</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">U&#39;</span> <span class="o">:</span> <span class="n">B</span><span class="o">,</span> <span class="n">U&#39;</span><span class="bp">.</span><span class="mi">1</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">)</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">{</span><span class="n">U</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">category</span> <span class="o">(</span><span class="n">under_set</span> <span class="n">B</span> <span class="n">U</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">under_set</span><span class="bp">;</span> <span class="n">apply_instance</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span><span class="o">)</span>

<span class="n">def</span> <span class="n">under_set</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">ι</span> <span class="o">:</span> <span class="n">U₁</span> <span class="err">⟶</span> <span class="n">U₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">under_set</span> <span class="n">B</span> <span class="n">U₂</span> <span class="err">⥤</span> <span class="n">under_set</span> <span class="n">B</span> <span class="n">U₁</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">U</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="n">U</span><span class="bp">.</span><span class="mi">2</span> <span class="n">ι</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">map&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">U&#39;</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="o">:</span> <span class="n">under_set</span> <span class="n">B</span> <span class="n">U</span> <span class="err">⥤</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">full_subcategory_embedding</span> <span class="o">(</span><span class="n">under_set</span> <span class="n">B</span> <span class="n">U</span><span class="o">)</span>

<span class="kn">end</span> <span class="n">under_set</span>

<span class="kn">section</span> <span class="n">extend</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}}</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="err">𝒱</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">V</span><span class="o">]</span> <span class="o">[</span><span class="n">has_limits</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">V</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒱</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">))</span>
<span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="o">((</span><span class="bp">λ</span> <span class="n">U</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">,</span> <span class="n">U</span><span class="bp">.</span><span class="n">s</span><span class="o">)</span> <span class="err">&#39;&#39;</span> <span class="n">B</span><span class="o">))</span>

<span class="n">def</span> <span class="n">extend</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">B</span> <span class="n">V</span><span class="o">)</span> <span class="o">:</span>
<span class="n">presheaf</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="n">V</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">limit</span> <span class="o">((</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
  <span class="n">map&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="n">ι</span><span class="o">,</span>
    <span class="n">limit</span><span class="bp">.</span><span class="n">lift</span> <span class="o">((</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₂</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span>
    <span class="o">{</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">limit</span> <span class="o">((</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₁</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
      <span class="n">π</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">limit</span><span class="bp">.</span><span class="n">π</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">U</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="n">U</span><span class="bp">.</span><span class="mi">2</span> <span class="n">ι</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⟩</span> <span class="err">≫</span> <span class="o">(</span><span class="mi">𝟙</span> <span class="bp">_</span><span class="o">)</span>
       <span class="o">}</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">extend</span>
</pre></div>

#### [ Johan Commelin (Oct 10 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537756):
<p>Goal is:</p>
<div class="codehilite"><pre><span></span><span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">there</span> <span class="n">are</span> <span class="n">unsolved</span> <span class="n">goals</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="o">,</span>
<span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="err">𝒱</span> <span class="o">:</span> <span class="n">category</span> <span class="n">V</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">has_limits</span> <span class="n">V</span><span class="o">,</span>
<span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">),</span>
<span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">B</span><span class="o">}</span> <span class="n">V</span><span class="o">,</span>
<span class="n">U₁</span> <span class="n">U₂</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">,</span>
<span class="n">ι</span> <span class="o">:</span> <span class="n">U₁</span> <span class="bp">≤</span> <span class="n">U₂</span><span class="o">,</span>
<span class="n">j_val_val</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">,</span>
<span class="n">j_val_property</span> <span class="o">:</span> <span class="n">j_val_val</span> <span class="err">∈</span> <span class="n">B</span><span class="o">,</span>
<span class="n">j_property</span> <span class="o">:</span> <span class="bp">⟨</span><span class="n">j_val_val</span><span class="o">,</span> <span class="n">j_val_property</span><span class="bp">⟩</span> <span class="err">∈</span> <span class="n">under_set</span> <span class="n">B</span> <span class="n">U₂</span><span class="o">,</span>
<span class="n">j&#39;_val_val</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">,</span>
<span class="n">j&#39;_val_property</span> <span class="o">:</span> <span class="n">j&#39;_val_val</span> <span class="err">∈</span> <span class="n">B</span><span class="o">,</span>
<span class="n">j&#39;_property</span> <span class="o">:</span> <span class="bp">⟨</span><span class="n">j&#39;_val_val</span><span class="o">,</span> <span class="n">j&#39;_val_property</span><span class="bp">⟩</span> <span class="err">∈</span> <span class="n">under_set</span> <span class="n">B</span> <span class="n">U₂</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="n">j_val_val</span> <span class="bp">≤</span> <span class="n">j&#39;_val_val</span>
<span class="err">⊢</span> <span class="n">limit</span><span class="bp">.</span><span class="n">π</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₁</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="bp">⟨⟨</span><span class="n">j_val_val</span><span class="o">,</span> <span class="n">j_val_property</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="err">≫</span>
      <span class="n">functor</span><span class="bp">.</span><span class="n">map</span> <span class="n">F</span> <span class="o">(</span><span class="n">functor</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₂</span><span class="o">)</span> <span class="o">{</span><span class="n">down</span> <span class="o">:=</span> <span class="o">{</span><span class="n">down</span> <span class="o">:=</span> <span class="n">f</span><span class="o">}})</span> <span class="bp">=</span>
    <span class="n">limit</span><span class="bp">.</span><span class="n">π</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₁</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="bp">⟨⟨</span><span class="n">j&#39;_val_val</span><span class="o">,</span> <span class="n">j&#39;_val_property</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">_⟩</span>
</pre></div>

#### [ Johan Commelin (Oct 10 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135542499):
<p>Here is a version where the auto_param gets the job done:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">extend</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">B</span> <span class="n">V</span><span class="o">)</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="n">V</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">obj</span>  <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">limit</span> <span class="o">((</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
  <span class="n">map&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="n">ι</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="n">rw</span> <span class="k">show</span> <span class="n">limit</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₂</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="bp">=</span> <span class="n">limit</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">map</span> <span class="n">B</span> <span class="n">ι</span> <span class="err">⋙</span> <span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₁</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">),</span>
      <span class="k">by</span> <span class="n">congr</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">limit</span><span class="bp">.</span><span class="n">pre</span> <span class="o">((</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₁</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">map</span> <span class="n">B</span> <span class="n">ι</span><span class="o">),</span>
    <span class="kn">end</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Oct 10 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135542532):
<p>I still don't like the <code>rw show</code>, but I don't know how to get rid of it.</p>

#### [ Patrick Massot (Oct 10 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135542709):
<p>Don't we have a gentleman agreement that any use of Scott's category theory must begin with a local notation reintroducing the proper composition symbol everywhere?</p>

#### [ Johan Commelin (Oct 10 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135543280):
<p><span class="emoji emoji-1f606" title="lol">:lol:</span> I didn't think about it. Sorry...</p>

#### [ Johan Commelin (Oct 10 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135546628):
<p>And we now have:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="err">Γ</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w₁</span><span class="o">}</span> <span class="o">[</span><span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">w₁</span> <span class="n">w₂</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">C</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">C</span> <span class="n">V</span><span class="o">)</span> <span class="o">:</span> <span class="n">V</span> <span class="o">:=</span> <span class="n">F</span><span class="bp">.</span><span class="n">obj</span> <span class="n">U</span>

<span class="kn">lemma</span> <span class="n">extend_val</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">B</span> <span class="n">V</span><span class="o">}</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="err">Γ</span> <span class="n">U</span> <span class="o">(</span><span class="n">extend</span> <span class="n">F</span><span class="o">)</span> <span class="bp">=</span> <span class="n">limit</span> <span class="o">((</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">lemma</span> <span class="n">extend_val_basic_open</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">presheaf</span> <span class="n">B</span> <span class="n">V</span><span class="o">}</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">B</span><span class="o">)</span> <span class="o">:</span> <span class="err">Γ</span> <span class="n">U</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">extend</span> <span class="n">F</span><span class="o">)</span> <span class="err">≅</span> <span class="err">Γ</span> <span class="n">U</span> <span class="n">F</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">extend_val</span><span class="bp">;</span> <span class="n">exact</span>
<span class="o">{</span> <span class="n">hom</span> <span class="o">:=</span> <span class="n">limit</span><span class="bp">.</span><span class="n">π</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="o">(</span><span class="n">U</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="bp">⟨</span><span class="n">U</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">inv</span> <span class="o">:=</span> <span class="n">limit</span><span class="bp">.</span><span class="n">lift</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="o">(</span><span class="n">U</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span>
  <span class="o">{</span> <span class="n">X</span> <span class="o">:=</span> <span class="err">Γ</span> <span class="n">U</span> <span class="n">F</span><span class="o">,</span>
    <span class="n">π</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U&#39;</span><span class="o">,</span> <span class="n">F</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">ulift</span><span class="bp">.</span><span class="n">up</span> <span class="o">(</span><span class="n">plift</span><span class="bp">.</span><span class="n">up</span> <span class="n">U&#39;</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="o">}</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Oct 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135546669):
<p>That latter thing is really slow )-; But I don't see how to speed it up.</p>

#### [ Patrick Massot (Oct 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135546721):
<p>Lots of proofs are provided in the background</p>

#### [ Johan Commelin (Oct 10 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135546842):
<blockquote>
<p>elaboration: tactic execution took 16.8s<br>
num. allocated objects:  146<br>
num. allocated closures: 146<br>
16762ms   100.0%   tactic.seq<br>
16762ms   100.0%   tactic.step<br>
16762ms   100.0%   tactic.istep._lambda_1<br>
16762ms   100.0%   tactic.istep<br>
16762ms   100.0%   scope_trace<br>
16762ms   100.0%   interaction_monad.monad._lambda_9<br>
16759ms   100.0%   all_goals_core<br>
16759ms   100.0%   tactic.interactive.exact<br>
16759ms   100.0%   _private.3346078393.all_goals_core._main._lambda_2<br>
16759ms   100.0%   tactic.all_goals<br>
16756ms   100.0%   tactic.to_expr<br>
    3ms     0.0%   rw_core<br>
    3ms     0.0%   tactic.exact<br>
    3ms     0.0%   _private.3200700535.rw_goal._lambda_4<br>
    3ms     0.0%   _private.3200700535.rw_goal._lambda_2<br>
    3ms     0.0%   interaction_monad.orelse'<br>
    3ms     0.0%   tactic.rewrite_target<br>
    3ms     0.0%   interactive.loc.apply<br>
    3ms     0.0%   tactic.interactive.propagate_tags<br>
    3ms     0.0%   _interaction._lambda_2<br>
    2ms     0.0%   tactic.rewrite<br>
    2ms     0.0%   tactic.rewrite_core<br>
    1ms     0.0%   tactic.replace_target<br>
    1ms     0.0%   tactic.mk_eq_mpr</p>
</blockquote>

#### [ Johan Commelin (Oct 10 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135558576):
<p>The next step would be to define sheaves on a basis, and show that their extensions are sheaves on the space.</p>

#### [ Johan Commelin (Oct 10 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135558620):
<p>I have the vague feeling that maybe we just want a general statement about sites.</p>

#### [ Johan Commelin (Oct 10 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135558749):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Do you know if the inclusion of a basis <code>B</code> into <code>open_set X</code> is some sort of geometric morphism?</p>

#### [ Johan Commelin (Oct 10 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135558814):
<p>If so, then I'dd rather just start attacking the general case...</p>

#### [ Reid Barton (Oct 10 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559318):
<p>I've never learned these topos theory words</p>

#### [ Johan Commelin (Oct 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559476):
<p>It seems that the answer might be yes... so now we want topos theory in mathlib <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Johan Commelin (Oct 10 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559723):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Did you ever do things with Kan extensions in your library?</p>

#### [ Reid Barton (Oct 10 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559838):
<p>Nope, near the top of my list for post-colimits.</p>

#### [ Johan Commelin (Oct 10 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559851):
<p>Ok... cool. How close do you think this is to being mathlib-ready?</p>

#### [ Reid Barton (Oct 10 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559913):
<p>Which?</p>

#### [ Johan Commelin (Oct 10 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559924):
<p>Kan extensions</p>

#### [ Reid Barton (Oct 10 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559937):
<p>Oh, I haven't actually started on them at all yet.</p>

#### [ Johan Commelin (Oct 10 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559940):
<p>If Scott's limit and colimit stuff is in mathlib. Would that be a follow-up PR? Or would you need other stuff before that?</p>

#### [ Reid Barton (Oct 10 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560032):
<p>Are you going to need general Kan extensions? Or just extending a functor on C to presheaves on C</p>

#### [ Johan Commelin (Oct 10 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560067):
<p>The latter is good enough</p>

#### [ Reid Barton (Oct 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560069):
<p>I see. We may want adjunctions, too.</p>

#### [ Johan Commelin (Oct 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560073):
<p>We do</p>

#### [ Johan Commelin (Oct 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560089):
<p>But I guess that will be the third PR that Scott has on his list (-;</p>

#### [ Reid Barton (Oct 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560110):
<p>In order to state the characterization of Kan extension as left adjoint to restriction</p>

#### [ Reid Barton (Oct 10 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560152):
<p>I guess we can define them without that though</p>

#### [ Reid Barton (Oct 10 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560168):
<p>:plane: but should be back online in not too long</p>

#### [ Johan Commelin (Oct 10 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560185):
<p>Good luck!</p>

#### [ Patrick Massot (Oct 10 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135561537):
<blockquote>
<p>Nope, near the top of my list for post-colimits.</p>
</blockquote>
<p>What about formalizing what you told us about reflective subcategory?</p>

#### [ Johan Commelin (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135561999):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Hmmm, a topological basis doesn't give a site. You don't have intersections = products. So the generalisation doesn't apply. Too bad.</p>

#### [ Reid Barton (Oct 10 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135562984):
<p>Reflective subcategories are in the same bulleted list in my notes. I forget which one is listed first :)</p>

#### [ Patrick Massot (Oct 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135563212):
<p>Perfectoid spaces vote for reflexive subcategories first</p>

#### [ Kevin Buzzard (Oct 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135567536):
<blockquote>
<p>Aah <code>cases</code>.</p>
</blockquote>
<p>You needed that for that <code>option</code> question yesterday too. It works for any inductive type.</p>

#### [ Scott Morrison (Oct 11 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135572559):
<p>Hmm, your profiling output is not very helpful, because everything is hidden behind the <code>to_expr</code> that <code>exact</code> is calling.</p>

#### [ Scott Morrison (Oct 11 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135572563):
<p>Is it possible to make another lemma for the <code>exact</code>?</p>

#### [ Scott Morrison (Oct 11 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135572602):
<p>(Also, this is fabulous.)</p>

#### [ Kevin Buzzard (Oct 11 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135572927):
<p>I've been really busy over the last couple of days -- but have you (<span class="user-mention" data-user-id="112680">@Johan Commelin</span> ) just extended a presheaf from a basis and then shown that the restriction back to the basis is isomorphic to the original presheaf, in about 10 lines? Heh, I guess you should really have shown that the restriction was isomorphic as a presheaf on the basis to F ;-) But still -- who cares if it's slow, it's a small number of lines and that feels right to a mathematician.</p>

#### [ Reid Barton (Oct 11 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135583396):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I finally looked at your actual code (too many missing Unicode characters on my phone to be practical) and I think you can use something called <code>limit.pre</code> or similar to simplify your <code>extend</code> even further.<br>
If you have a diagram <code>X : J -&gt; C</code> and a functor <code>F : I -&gt; J</code> then you get an induced map <code>lim_I X -&gt; lim_J (X \o F)</code> and this map is called <code>limit.pre</code>.<br>
If you have a map <code>a -&gt; b</code> in <code>C</code> then you get a functor <code>C/a -&gt; C/b</code> and I think your <code>extend</code> is <code>limit.pre</code> of this functor.</p>

#### [ Johan Commelin (Oct 11 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584496):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> I'm sorry, I think you have been looking at old code. The new code already uses <code>limit.pre</code>: <a href="https://github.com/jcommelin/lean-perfectoid-spaces/blob/huber_tate/src/for_mathlib/presheaves.lean" target="_blank" title="https://github.com/jcommelin/lean-perfectoid-spaces/blob/huber_tate/src/for_mathlib/presheaves.lean">https://github.com/jcommelin/lean-perfectoid-spaces/blob/huber_tate/src/for_mathlib/presheaves.lean</a></p>

#### [ Johan Commelin (Oct 11 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584509):
<p>It isn't as nice as I wish. I would like to get rid of the ugly <code>rw, congr, exact</code>.</p>

#### [ Reid Barton (Oct 11 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584558):
<p>Ah, I see. I think maybe I missed the <code>limit.pre</code> in there, indeed</p>

#### [ Reid Barton (Oct 11 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584570):
<p>I guess <code>convert</code> might be slightly better?</p>

#### [ Reid Barton (Oct 11 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584573):
<p>change <code>exact</code> to <code>convert</code> and move it first, then see what happens?</p>

#### [ Reid Barton (Oct 11 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584578):
<p>I'm a little confused how <code>congr</code> proved something without producing any new goals</p>

#### [ Johan Commelin (Oct 11 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584579):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Yes, I did. Isn't it delightful? But proving that the extension of a sheaf is a sheaf will be a lot harder.</p>

#### [ Johan Commelin (Oct 11 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584624):
<blockquote>
<p>change <code>exact</code> to <code>convert</code> and move it first, then see what happens?</p>
</blockquote>
<p>I think that didn't work: deterministic timeout or something.</p>

#### [ Johan Commelin (Oct 11 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584627):
<p>In some sense it was really brittle.</p>

#### [ Reid Barton (Oct 11 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584637):
<p>Odd</p>

#### [ Johan Commelin (Oct 11 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584645):
<p>That file doens't need anything from the perfectoid project. So if you want to hack on it, you can just copy-paste it.</p>

#### [ Johan Commelin (Oct 11 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584814):
<p>Of course you need Scott's libs</p>

#### [ Reid Barton (Oct 11 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135619434):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I was able to replace the whole <code>map'</code> field by</p>
<div class="codehilite"><pre><span></span><span class="n">map&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="n">ι</span><span class="o">,</span> <span class="n">limit</span><span class="bp">.</span><span class="n">pre</span> <span class="o">((</span><span class="n">under_set</span><span class="bp">.</span><span class="n">embedding</span> <span class="n">B</span> <span class="n">U₁</span><span class="o">)</span> <span class="err">⋙</span> <span class="n">F</span><span class="o">)</span> <span class="o">(</span><span class="n">under_set</span><span class="bp">.</span><span class="n">map</span> <span class="n">B</span> <span class="n">ι</span><span class="o">)</span>
</pre></div>


<p>Everything is quite slow in the editor, I believe because there are errors in the imports (stuff under <code>category_theory.limits</code>)</p>

#### [ Johan Commelin (Oct 11 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135629183):
<p>Cool! Thanks a lot. Somehow I think I got deterministic timeouts when I tried that. Maybe it is related to the errors in the imports that you mentioned.</p>

#### [ Reid Barton (Oct 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135629306):
<p>My understanding is that <code>lean --make</code> doesn't write out <code>.olean</code> files when the build was unsuccessful, which means if your imports have errors then lean in the editor will be much slower.</p>

#### [ Reid Barton (Oct 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135629362):
<p>It looks like the errors are rather trivial in this case (some tactics failed because there were no goals remaining) but I didn't try to just fix them because they are in lean-category-theory</p>

#### [ Johan Commelin (Oct 12 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135659126):
<p>Ok, now it worked for me as well.</p>

#### [ Johan Commelin (Oct 15 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135813243):
<p>I think the following is pretty ugly:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)}</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="o">((</span><span class="bp">λ</span> <span class="n">U</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">,</span> <span class="n">U</span><span class="bp">.</span><span class="n">s</span><span class="o">)</span> <span class="err">&#39;&#39;</span> <span class="n">B</span><span class="o">))</span>
</pre></div>


<p>Does this mean that I should define <code>is_basis</code> for <code>B</code> directly? It feels like duplicating a lot of stuff. Is this the curse of bundling?</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135813787):
<p>I don't understand what you are trying to do</p>

#### [ Johan Commelin (Oct 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135813797):
<p>I'm trying to say that a collection of open sets is a basis. But the open sets are bundled.</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135813997):
<p>I guess you can write <code>open_set.s</code> instead of the lambda</p>

#### [ Johan Commelin (Oct 15 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814020):
<p>Ok, and would that be the <em>morally correct</em> way? Or should I "develop the theory of a basis of bundled open sets"?</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814069):
<p>I'm not sure if you want the forward image or preimage yet, but I think this is what you want</p>

#### [ Johan Commelin (Oct 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814235):
<p>Well, you could redefine <code>is_basis</code> for a set of opens, right? Something like</p>
<div class="codehilite"><pre><span></span><span class="err">\</span><span class="k">forall</span> <span class="n">U</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">,</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">U&#39;</span> <span class="err">∈</span> <span class="n">B</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U&#39;</span> <span class="bp">∧</span> <span class="n">U&#39;</span> <span class="err">⊆</span> <span class="n">U</span>
</pre></div>

#### [ Mario Carneiro (Oct 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814375):
<p>I would define <code>open_set.is_basis</code> using the image formulation, and then prove that version as a theorem</p>

#### [ Johan Commelin (Oct 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814380):
<p>Ok, thanks.</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814394):
<p>also that's not the right condition</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814398):
<p>the exists is satisfied by <code>U</code></p>

#### [ Johan Commelin (Oct 15 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814450):
<p>No, <code>U</code> is not <code>∈ B</code>. (In general.)</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814452):
<p>oh... but what about intersections?</p>

#### [ Johan Commelin (Oct 15 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814458):
<p>What's with them?</p>

#### [ Mario Carneiro (Oct 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814475):
<p>a basis should be closed under intersection (ish)</p>

#### [ Johan Commelin (Oct 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814486):
<p>Oooo... maybe. I'll see when I start proving things (-;</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814491):
<p>This just says B covers the space</p>

#### [ Johan Commelin (Oct 15 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814542):
<p>It says that <code>B</code> covers every open.</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814567):
<p>oh, actually I think you have the intersection property then</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814672):
<p>if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi><mo separator="true">,</mo><mi>V</mi><mo>∈</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">U, V \in B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.22222em;">V</span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∈</mo><mi>U</mi><mo>∩</mo><mi>V</mi></mrow><annotation encoding="application/x-tex">x \in U \cap V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.72243em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mbin">∩</span><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span>, then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi><mo>∩</mo><mi>V</mi></mrow><annotation encoding="application/x-tex">U\cap V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mbin">∩</span><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span> is open so you can find <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>∈</mo><mi>W</mi><mo>∈</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">x\in W\in B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.72243em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.13889em;">W</span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>W</mi><mo>⊆</mo><mi>U</mi><mo>∩</mo><mi>V</mi></mrow><annotation encoding="application/x-tex">W\subseteq U\cap V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">W</span><span class="mrel">⊆</span><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mbin">∩</span><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span></p>

#### [ Johan Commelin (Oct 15 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814712):
<p>That looks good, right?</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135815120):
<p>yeah</p>

#### [ Mario Carneiro (Oct 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135815128):
<p>actually now I recall Kevin saying that this was the obvious definition and he was confused by mathlib's</p>

#### [ Johan Commelin (Oct 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135826125):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Proving that the two definitions are equivalent is a major headache. I feel like we are missing an induction principle for generated topologies. But maybe it is <em>me</em> who is missing it.</p>

#### [ Johan Commelin (Oct 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135826813):
<div class="codehilite"><pre><span></span><span class="c1">-- set.lean</span>
<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span>
<span class="n">def</span> <span class="n">sUnion</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span><span class="n">t</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">t</span> <span class="err">∈</span> <span class="n">a</span><span class="o">}</span>
<span class="kn">prefix</span> <span class="bp">`</span><span class="err">⋃₀</span><span class="bp">`</span><span class="o">:</span><span class="mi">110</span> <span class="o">:=</span> <span class="n">sUnion</span>
</pre></div>


<p>Does this mean that we can't use <code>⋃₀</code> to take the union of <code>Us : set (open_set X)</code>? Or can/should I overload notation?</p>

#### [ Johan Commelin (Oct 15 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135827571):
<p>I would expect that this notation is meaningful for every type that has a union-operator.</p>

#### [ Kenny Lau (Oct 15 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828259):
<p>try it wthout 0?</p>

#### [ Johan Commelin (Oct 15 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828350):
<p>That gives a weird error: <code>invalid expression starting at 27:51</code></p>

#### [ Johan Commelin (Oct 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828554):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> How is this supposed to work? I tried</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">is_basis_iff₁</span> <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">:</span>
<span class="n">is_basis</span> <span class="n">B</span> <span class="bp">↔</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">},</span> <span class="bp">∃</span> <span class="n">Us</span> <span class="err">⊆</span> <span class="n">set</span> <span class="n">B</span><span class="o">,</span> <span class="n">U</span> <span class="bp">=</span> <span class="err">⋃</span> <span class="n">U&#39;</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">,</span> <span class="n">U&#39;</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Clearly this is not what Lean wants to see...</p>

#### [ Kenny Lau (Oct 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828610):
<p>you need : not \in</p>

#### [ Kenny Lau (Oct 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828619):
<p>and it’s called bUnion</p>

#### [ Johan Commelin (Oct 15 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828914):
<p>Right, so for this we need a lattice structure on <code>open_set</code>. Which we will need at some point anyway.</p>

#### [ Johan Commelin (Oct 15 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135837316):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I know you are busy. Just posting this in case you have a couple of minutes where you are bored <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span> </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">topological_spaces</span>
<span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">lattice</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">tactics</span><span class="bp">.</span><span class="n">obviously</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">open</span> <span class="n">category_theory</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span>

<span class="kn">namespace</span> <span class="n">open_set</span>
<span class="kn">open</span> <span class="n">topological_space</span> <span class="n">lattice</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}}</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">back</span><span class="o">]</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_open_inter</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">back</span><span class="o">]</span> <span class="n">is_open_union</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">back</span><span class="o">]</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">is_open</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_inter</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">inter</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">V</span><span class="o">,</span> <span class="bp">⟨</span> <span class="n">U</span><span class="bp">.</span><span class="n">s</span> <span class="err">∩</span> <span class="n">V</span><span class="bp">.</span><span class="n">s</span><span class="o">,</span> <span class="k">by</span> <span class="n">obviously</span> <span class="bp">⟩</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_union</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">union</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">V</span><span class="o">,</span> <span class="bp">⟨</span> <span class="n">U</span><span class="bp">.</span><span class="n">s</span> <span class="err">∪</span> <span class="n">V</span><span class="bp">.</span><span class="n">s</span><span class="o">,</span> <span class="k">by</span> <span class="n">obviously</span> <span class="bp">⟩</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">lattice</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span> <span class="o">{</span>
  <span class="n">sup</span> <span class="o">:=</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">has_union</span><span class="bp">.</span><span class="n">union</span><span class="o">,</span>
  <span class="n">inf</span> <span class="o">:=</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">has_inter</span><span class="bp">.</span><span class="n">inter</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">U₁</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">U₂</span><span class="bp">;</span> <span class="n">tidy</span><span class="o">,</span>
  <span class="n">le_sup_left</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">intros</span> <span class="n">U₁</span> <span class="n">U₂</span><span class="o">,</span> <span class="n">cases</span> <span class="n">U₁</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">U₂</span><span class="o">,</span> <span class="n">tidy</span><span class="o">,</span> <span class="kn">end</span><span class="o">,</span>
  <span class="n">le_sup_right</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">sup_le</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">inf_le_left</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">inf_le_right</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">le_inf</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="bp">..</span><span class="n">open_set</span><span class="bp">.</span><span class="n">preorder</span> <span class="o">}</span><span class="bp">;</span> <span class="n">tidy</span>
</pre></div>


<p>What incantations do I need to get <code>tidy</code> up to speed?</p>

#### [ Johannes Hölzl (Oct 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135837545):
<p>I guess you need the rules how <code>union</code> and <code>intersection</code> behave under <code>subset</code>, like <code>set.subset_union_left</code>. So try add this as <code>back</code>.</p>

#### [ Mario Carneiro (Oct 15 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135839090):
<p>hey <span class="user-mention" data-user-id="110064">@Kenny Lau</span>, I see a galois insertion...</p>

#### [ Reid Barton (Oct 15 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135839344):
<p>Do we have an emoji for galois insertion</p>

#### [ Johan Commelin (Oct 15 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135839838):
<p>Thanks, I'll try that tomorrow.</p>

#### [ Kevin Buzzard (Oct 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135842162):
<blockquote>
<p>Do we have an emoji for galois insertion</p>
</blockquote>
<p>So we need to choose one, right? People should vote on Reid's question.</p>

#### [ Johan Commelin (Oct 16 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881584):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I implemented Johannes suggestion. Now I have the following bunch of code:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span><span class="bp">.</span><span class="n">topological_spaces</span>
<span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">lattice</span>
<span class="kn">import</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">tactics</span><span class="bp">.</span><span class="n">obviously</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">open</span> <span class="n">category_theory</span>
<span class="kn">open</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">examples</span>

<span class="kn">namespace</span> <span class="n">open_set</span>
<span class="kn">open</span> <span class="n">topological_space</span> <span class="n">lattice</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="bp">.</span><span class="o">{</span><span class="n">v</span><span class="o">}}</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">back</span><span class="o">]</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_open_inter</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">back</span><span class="o">]</span> <span class="n">is_open_union</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">back</span><span class="o">]</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">is_open</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">back</span><span class="o">]</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset_union_left</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">back</span><span class="o">]</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset_union_right</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_inter</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">inter</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">V</span><span class="o">,</span> <span class="bp">⟨</span> <span class="n">U</span><span class="bp">.</span><span class="n">s</span> <span class="err">∩</span> <span class="n">V</span><span class="bp">.</span><span class="n">s</span><span class="o">,</span> <span class="k">by</span> <span class="n">obviously</span> <span class="bp">⟩</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_union</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">union</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">V</span><span class="o">,</span> <span class="bp">⟨</span> <span class="n">U</span><span class="bp">.</span><span class="n">s</span> <span class="err">∪</span> <span class="n">V</span><span class="bp">.</span><span class="n">s</span><span class="o">,</span> <span class="k">by</span> <span class="n">obviously</span> <span class="bp">⟩</span> <span class="o">}</span>

<span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">has_union</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">has_union</span><span class="bp">.</span><span class="n">equations</span><span class="bp">._</span><span class="n">eqn_1</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">lattice</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span> <span class="o">{</span>
  <span class="n">sup</span> <span class="o">:=</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">has_union</span><span class="bp">.</span><span class="n">union</span><span class="o">,</span>
  <span class="n">inf</span> <span class="o">:=</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">has_inter</span><span class="bp">.</span><span class="n">inter</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">U₁</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">U₂</span><span class="bp">;</span> <span class="n">tidy</span><span class="o">,</span>
  <span class="n">le_sup_left</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">tidy</span><span class="o">,</span> <span class="kn">end</span><span class="o">,</span>
  <span class="n">le_sup_right</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">intros</span> <span class="n">U₁</span> <span class="n">U₂</span><span class="o">,</span> <span class="n">cases</span> <span class="n">U₁</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">U₂</span><span class="o">,</span> <span class="n">tidy</span><span class="o">,</span> <span class="kn">end</span><span class="o">,</span>
  <span class="n">sup_le</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">inf_le_left</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">inf_le_right</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">le_inf</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="bp">..</span><span class="n">open_set</span><span class="bp">.</span><span class="n">preorder</span> <span class="o">}</span><span class="bp">;</span> <span class="n">tidy</span>
</pre></div>

#### [ Johan Commelin (Oct 16 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881631):
<p>The <code>tidy</code> in the proof of <code>le_sup_left</code> leaves me with the following goal:</p>
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="n">Top</span><span class="o">,</span>
<span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">,</span>
<span class="n">a_1</span> <span class="o">:</span> <span class="n">X</span><span class="bp">.</span><span class="n">α</span><span class="o">,</span>
<span class="n">a_2</span> <span class="o">:</span> <span class="n">a_1</span> <span class="err">∈</span> <span class="n">a</span><span class="bp">.</span><span class="n">s</span>
<span class="err">⊢</span> <span class="n">a_1</span> <span class="err">∈</span> <span class="n">a</span><span class="bp">.</span><span class="n">s</span> <span class="bp">∨</span> <span class="n">a_1</span> <span class="err">∈</span> <span class="n">b</span><span class="bp">.</span><span class="n">s</span>
</pre></div>

#### [ Johan Commelin (Oct 16 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881644):
<p>Ooh wait! Does this mean that I have to mark <code>or.inl</code> with <code>[back!]</code> or something like that?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881646):
<p>Does <code>@[simp] instance : has_union (open_set X)</code> do the same as <code>attribute [simp] open_set.has_union.equations._eqn_1</code>?</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881700):
<p>or.inl is not a good <code>back!</code> lemma</p>

#### [ Johan Commelin (Oct 16 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881711):
<p>Hmmm, why not?</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881757):
<p>because it will try to prove everything by the left disjunct</p>

#### [ Johan Commelin (Oct 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881760):
<p>Only if the assumptions are satisfied, right?</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881761):
<p>not with the <code>!</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881768):
<p>I think <code>simp</code> should work</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881773):
<p>because it will turn the goal into <code>true \/ ...</code> and then <code>true</code></p>

#### [ Johan Commelin (Oct 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881774):
<p>Well, it doesn't. Because <code>tidy</code> would try that.</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881775):
<p>did you see if <code>simp * at *</code> works by hand?</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881777):
<p>what about <code>simp *</code>?</p>

#### [ Johan Commelin (Oct 16 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881838):
<p>Ok, that works. Is that a bug in <code>tidy</code>?</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881911):
<p>or a bug in <code>simp * at *</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881952):
<p>wait, which is "that"</p>

#### [ Kevin Buzzard (Oct 16 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881966):
<p>I have a very unclear idea about what all these things like <code>tidy</code> and <code>obviously</code> and <code>backwards_reasoning</code> do. It seems to me that they "all do the same thing" -- they just "try a bunch of stuff like simp and split and stuff". Does <code>tidy</code> have a sufficiently formal specification that one can ask if there is a "bug" in it? Do you actually mean "let's make <code>tidy</code> try more stuff"?</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881994):
<p><code>back</code> has a "spec", but you are right about the others</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882015):
<p><code>obviously</code> is <code>tidy</code> + <code>rewrite_search</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882019):
<p>which is that graph thing that Keeley Hoek did</p>

#### [ Johan Commelin (Oct 16 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882029):
<p><code>simp *</code> worked. I would imagine that <code>tidy</code> should try that as well. Of course it is not a bug in the strict sense; but I meant a "bug" in the sense that it would be a nice feature to add to <code>tidy</code>.</p>

#### [ Mario Carneiro (Oct 16 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882030):
<p><code>tidy</code> is just a kitchen sink tactic right now, although I understand it is loosely based on the Gowers-Ganesalingam prover</p>

#### [ Johan Commelin (Oct 16 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882245):
<p>I'm struggling with finding  a statement that type checks. I just proved that <code>open_set X</code> has a lattice structure. Now I want to take a union of a bunch of opens. What should I tell Lean to make sense of this?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">is_basis_iff₁</span> <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">:</span>
<span class="n">is_basis</span> <span class="n">B</span> <span class="bp">↔</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">},</span> <span class="bp">∃</span> <span class="n">Us</span> <span class="err">⊆</span> <span class="n">set</span> <span class="n">B</span><span class="o">,</span> <span class="n">U</span> <span class="bp">=</span> <span class="err">⋃</span> <span class="n">U&#39;</span> <span class="o">:</span> <span class="n">Us</span><span class="o">,</span> <span class="n">U&#39;</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johan Commelin (Oct 16 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882253):
<p>Currently it doesn't like the <code>⋃</code> symbol.</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882319):
<p>use the sup symbol</p>

#### [ Kevin Buzzard (Oct 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882321):
<p>Isn't there <code>union</code> and <code>Union</code> and <code>bUnion</code> and <code>sUnion</code> or something? Usage depends on whether you're taking a union of two things, or a set of things, or a type of things etc. One of them is that big union symbol -- aren't there other notations too though? I can never remember which is which here.</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882324):
<p>most of the union/inter notation is specific to <code>set</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882364):
<p>the generic version is <code>Sup</code> and <code>Inf</code></p>

#### [ Johan Commelin (Oct 16 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882367):
<p>Ok, I see. So for everything else we want to use lattice notation?</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882369):
<p>yes</p>

#### [ Johan Commelin (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882385):
<p>And turning something into a lattice doesn't automatically give you a <code>has_Sup</code>. Is that on purpose?<br>
I don't know anything about lattices.</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882386):
<blockquote>
<p><code> ∃ Us ⊆ set B, </code></p>
</blockquote>
<p>what should this mean?</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882393):
<p>a complete lattice, not a lattice</p>

#### [ Johan Commelin (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882394):
<p>That there is a bunch of basic opens such that...</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882398):
<p>lattice just gives you binary sup</p>

#### [ Johan Commelin (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882399):
<p>Ok, so I should prove that <code>open_set</code> is a complete lattice.</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882437):
<p>yes</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882443):
<p>again, galois insertion should make it easy</p>

#### [ Johan Commelin (Oct 16 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882525):
<p>I propose <span class="emoji emoji-1f504" title="return">:return:</span> for galois connections and adjunctions. I don't understand the <span class="emoji emoji-1f3c0" title="basketball">:basketball:</span> symbol. Maybe it's because I'm Dutch <span class="emoji emoji-1f606" title="lol">:lol:</span></p>

#### [ Johan Commelin (Oct 16 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882544):
<p>Ok, I have no idea what boilerplate I should write for that Galois insertion. What is the best way to find this out?</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882677):
<p>you need a pair of functions with a galois connection, from the complete lattice to the type you want a complete lattice structure on, and one round trip should be the identity</p>

#### [ Kevin Buzzard (Oct 16 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882881):
<p>The basketball was the only emoji I found which looked like anything being inserted into anything, that's all</p>

#### [ Kevin Buzzard (Oct 16 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882927):
<p>I didn't even look for an emoji of something being connected to something</p>

#### [ Johan Commelin (Oct 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882938):
<p>Ok, so one of the maps is <code>open_set.s</code> and the other is ?? the interior? Or the smallest open containing some set <code>S</code>?</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882948):
<p>interior, certainly</p>

#### [ Johan Commelin (Oct 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882949):
<p>Brainfart, that doesn't even make sense. So it should be the interior.</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883011):
<p>actually I'm a bit worried you will end up the wrong way around, i.e. you will get the <code>u</code> function being injective instead of the <code>l</code> function</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883021):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> How do you want to do galois coinsertions?</p>

#### [ Johan Commelin (Oct 16 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883518):
<p>Ok, so <code>l = interior</code> and <code>u = open_set.s</code>. Is this good or bad news for our complete_lattice?</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883614):
<p>try to prove galois insertion?</p>

#### [ Johan Commelin (Oct 16 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883814):
<p>Oops, I switched <code>l</code> and <code>u</code>. I still find those names confusing... Ok, so it is going to be a <code>coinsertion</code>.</p>

#### [ Johan Commelin (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884099):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is the Galois connection enough to get the complete lattice structure? Or do I need to work out <code>galois_coinsertion</code> first? I really don't know the maths here.</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884124):
<p>the insertion is important</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884128):
<p>it is basically making an order embedding</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884134):
<p>and you pull the relation back along that</p>

#### [ Johan Commelin (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884143):
<p>You mean coinsertion?</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884151):
<p>that too</p>

#### [ Johan Commelin (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884171):
<p>Hmmm, I will try to dualize all the stuff about <code>insertion</code>s.</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884173):
<p>it should work just as well, it will just pull a lattice from left to right instead of right to left</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884175):
<p>or vice versa</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884179):
<p>you know, just put co everywhere</p>

#### [ Johannes Hölzl (Oct 16 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884238):
<p>look into how it is done for <code>filter</code>. Here I use <code>dual_order</code> to get the other way round</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884245):
<p>I was just about to suggest that</p>

#### [ Johannes Hölzl (Oct 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884258):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">gi_generate</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">@</span><span class="n">galois_insertion</span> <span class="o">(</span><span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">))</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">filter</span> <span class="n">α</span><span class="o">))</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">filter</span><span class="bp">.</span><span class="n">generate</span> <span class="n">filter</span><span class="bp">.</span><span class="n">sets</span>
</pre></div>

#### [ Mario Carneiro (Oct 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884260):
<p>but filter is dualized on only one side</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884275):
<p>I guess a coinsertion is dualized on both sides</p>

#### [ Johannes Hölzl (Oct 16 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884308):
<p>is it enough to add <code>order_dual</code> on both sides?</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884341):
<p>I wonder whether we want a separate definition though since otherwise the names will be even more confusing than they already are</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884361):
<p>plus <code>galois_coinsertion</code> should extend <code>galois_connection</code> with no duals</p>

#### [ Mario Carneiro (Oct 16 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884413):
<p>do we know that <code>galois_connection</code> is self-dual?</p>

#### [ Johannes Hölzl (Oct 16 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884424):
<p>to its symmetric form:</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="kn">lemma</span> <span class="n">dual</span> <span class="o">[</span><span class="n">pα</span> <span class="o">:</span> <span class="n">preorder</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">pβ</span> <span class="o">:</span> <span class="n">preorder</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">gc</span> <span class="o">:</span> <span class="n">galois_connection</span> <span class="n">l</span> <span class="n">u</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">@</span><span class="n">galois_connection</span> <span class="o">(</span><span class="n">order_dual</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">order_dual</span> <span class="n">α</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">u</span> <span class="n">l</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="o">(</span><span class="n">gc</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>
</pre></div>

#### [ Johannes Hölzl (Oct 16 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884427):
<p>in <a href="https://github.com/leanprover/mathlib/blob/master/order/galois_connection.lean#L160" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/order/galois_connection.lean#L160">https://github.com/leanprover/mathlib/blob/master/order/galois_connection.lean#L160</a></p>

#### [ Kevin Buzzard (Oct 16 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884663):
<p>then it should just be called <code>galois_nnection</code></p>

#### [ Kevin Buzzard (Oct 16 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884719):
<p>it's shorter</p>

#### [ Johan Commelin (Oct 16 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884777):
<p>Aaahrg, all those design decisions. Is there a choice procedure for such design decisions?<br>
I think we should make the same choice as for the <code>limit</code> vs <code>colimit</code> story in category theory.</p>

#### [ Johan Commelin (Oct 16 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884833):
<p>So we just copy-paste all the code and dualize it. Right?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884837):
<p>[or write a tactic which generates the code for you...]</p>

#### [ Johannes Hölzl (Oct 16 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884873):
<p>usually you copy all statements from the Galois insertion anyway. I don't see a problem to use a Galois insertion and <code>dual_order</code> twice. You only want to use it to get the complete lattice, afterwards you don't care anymore.</p>

#### [ Johan Commelin (Oct 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135887809):
<p>Ok, now I've got</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">interior</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">interior</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">is_open</span> <span class="o">:=</span> <span class="n">is_open_interior</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">gc</span> <span class="o">:</span> <span class="n">galois_connection</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="n">interior</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">U</span> <span class="n">s</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">interior_maximal</span> <span class="n">h</span> <span class="n">U</span><span class="bp">.</span><span class="n">is_open</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">le_trans</span> <span class="n">h</span> <span class="n">interior_subset</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">gco</span> <span class="o">:</span> <span class="n">galois_coinsertion</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="n">interior</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">choice</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span> <span class="n">interior</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">gc</span> <span class="o">:=</span> <span class="n">gc</span><span class="o">,</span>
  <span class="n">u_l_le</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">interior_subset</span><span class="o">,</span>
  <span class="n">choice_eq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">U₁</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">U₂</span><span class="bp">;</span> <span class="n">tidy</span><span class="o">,</span>
   <span class="bp">..</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">preorder</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">complete_lattice</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="n">galois_coinsertion</span><span class="bp">.</span><span class="n">lift_complete_lattice</span> <span class="n">gco</span>

<span class="n">def</span> <span class="n">univ</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span><span class="o">,</span>
  <span class="n">is_open</span> <span class="o">:=</span> <span class="n">is_open_univ</span> <span class="o">}</span>
</pre></div>


<p>I guess that this definition of <code>univ</code> is not correct? Should it be a theorem about <code>⊤</code> somehow?</p>

#### [ Johan Commelin (Oct 16 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135894415):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Those <code>order_dual</code>s are completely blowing up my brain. Does this look good or am I missing something?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">interior</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">interior</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">is_open</span> <span class="o">:=</span> <span class="n">is_open_interior</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">gc</span> <span class="o">:</span> <span class="n">galois_connection</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="n">interior</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">U</span> <span class="n">s</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">interior_maximal</span> <span class="n">h</span> <span class="n">U</span><span class="bp">.</span><span class="n">is_open</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">le_trans</span> <span class="n">h</span> <span class="n">interior_subset</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">gi</span> <span class="o">:</span> <span class="bp">@</span><span class="n">galois_insertion</span> <span class="o">(</span><span class="n">order_dual</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">order_dual</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">choice</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span> <span class="n">interior</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">gc</span> <span class="o">:=</span> <span class="n">galois_connection</span><span class="bp">.</span><span class="n">dual</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">gc</span><span class="o">,</span>
  <span class="n">le_l_u</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">interior_subset</span><span class="o">,</span>
  <span class="n">choice_eq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">U₁</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">U₂</span><span class="bp">;</span> <span class="n">tidy</span><span class="o">,</span>
   <span class="bp">..</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">preorder</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">complete_lattice</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">galois_insertion</span><span class="bp">.</span><span class="n">lift_complete_lattice</span> <span class="o">(</span><span class="n">order_dual</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">order_dual</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="bp">_</span> <span class="n">gi</span>
</pre></div>

#### [ Johannes Hölzl (Oct 16 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135894662):
<p>looks good to me. Is there something wrong?</p>

#### [ Johan Commelin (Oct 16 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135894967):
<p>Yes, I'm getting the dual order.</p>

#### [ Johan Commelin (Oct 16 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135894982):
<p>So now I need a function that takes an order, and flips it around.</p>

#### [ Johan Commelin (Oct 16 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895221):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Is there a way to unfold something only once?</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895354):
<p>hm, <code>rw [h] {occs := occurrences.pos [1]}</code> is the only thing I know</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895452):
<p>for the dual, lets take a look at filters again:</p>
<div class="codehilite"><pre><span></span><span class="kn">private</span> <span class="n">def</span> <span class="n">original_complete_lattice</span> <span class="o">:</span> <span class="n">complete_lattice</span> <span class="o">(</span><span class="n">filter</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">order_dual</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">complete_lattice</span> <span class="bp">_</span> <span class="o">(</span><span class="n">gi_generate</span> <span class="n">α</span><span class="o">)</span><span class="bp">.</span><span class="n">lift_complete_lattice</span>
</pre></div>

#### [ Johan Commelin (Oct 16 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895460):
<p>I hacked around it like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">complete_lattice</span><span class="bp">.</span><span class="n">order_dual</span> <span class="o">:</span> <span class="n">complete_lattice</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">))</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">galois_insertion</span><span class="bp">.</span><span class="n">lift_complete_lattice</span> <span class="o">(</span><span class="n">order_dual</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">order_dual</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="bp">_</span> <span class="n">gi</span>

<span class="kn">lemma</span> <span class="n">order_dual_order_dual</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="n">order_dual</span> <span class="o">(</span><span class="n">order_dual</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">complete_lattice</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">foo</span> <span class="o">:</span> <span class="n">complete_lattice</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">))),</span>
  <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">order_dual_order_dual</span> <span class="n">at</span> <span class="n">foo</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">foo</span>
<span class="kn">end</span>
</pre></div>


<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I am not so sure that the coinsertions are useless. This is causing me quite some pain...</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895503):
<p><code>order_dual.lattice.complete_lattice</code> does what you want</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895514):
<p>and it doesn't have the <code>rw</code> problem</p>

#### [ Johan Commelin (Oct 16 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895594):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I don't see how to apply it. It can only put orders on <code>order_dual _</code>, it can't go the other way.</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895688):
<p>you are sure it doesn't work? <code>preorder (order_dual (order_dual A)) = preorder A</code> should be (in your case) by definition</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895698):
<p>can you put your theory on a gist?</p>

#### [ Johan Commelin (Oct 16 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896091):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Voila: <a href="https://gist.github.com/jcommelin/c9d04b7770f89a0fadc11aae5ca90d87" target="_blank" title="https://gist.github.com/jcommelin/c9d04b7770f89a0fadc11aae5ca90d87">https://gist.github.com/jcommelin/c9d04b7770f89a0fadc11aae5ca90d87</a><br>
This is what I have so far.</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896557):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U₁</span> <span class="n">U₂</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">U₁</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">U₂</span><span class="bp">;</span> <span class="n">tidy</span><span class="o">,</span>
   <span class="bp">..</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">preorder</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">complete_lattice</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">order_dual</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">complete_lattice</span> <span class="bp">_</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">galois_insertion</span><span class="bp">.</span><span class="n">lift_complete_lattice</span> <span class="o">(</span><span class="n">order_dual</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">order_dual</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="bp">_</span> <span class="n">gi</span><span class="o">)</span>
</pre></div>


<p>now you have the dual</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896558):
<p>is this what you want?</p>

#### [ Johan Commelin (Oct 16 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896566):
<p>I think it is. Let me try.</p>

#### [ Johan Commelin (Oct 16 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896627):
<p>But this still isn't proved by <code>rfl</code>:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">Lub_s</span> <span class="o">{</span><span class="n">Us</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">:</span> <span class="o">(</span><span class="err">⨆</span> <span class="n">U</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">,</span> <span class="n">U</span><span class="o">)</span><span class="bp">.</span><span class="n">s</span> <span class="bp">=</span> <span class="err">⋃₀</span> <span class="o">(</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="err">&#39;&#39;</span> <span class="n">Us</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>


<p>And I think that with coinsertions it could have been <code>rfl</code>, right?</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896694):
<p>only if you setup <code>choice</code> correctly</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896728):
<p>and this is also with insertion a <code>rfl</code></p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896788):
<p>so, no <code>coinsertion</code> doesn't give you a rfl by default. It will only be a <code>rfl</code> when you use the proof in <code>choice</code> to construct <code>rfl</code> data. And since <code>insertion</code> and <code>coinsertion</code> are just dual, it works also with insertion.</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896817):
<p>So what you need to do:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">gi</span> <span class="o">:</span> <span class="bp">@</span><span class="n">galois_insertion</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">))</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">))</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">choice</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span> <span class="n">interior</span> <span class="n">s</span><span class="o">,</span>
  <span class="n">gc</span> <span class="o">:=</span> <span class="n">galois_connection</span><span class="bp">.</span><span class="n">dual</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">gc</span><span class="o">,</span>
  <span class="n">le_l_u</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">interior_subset</span><span class="o">,</span>
  <span class="n">choice_eq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>
</pre></div>


<p>Instead of <code>choice := λ s _, interior s,</code> you need to write something like:<br>
<code>choice := λ s _, (s, proof that s is open),</code></p>

#### [ Johan Commelin (Oct 16 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896890):
<p>Huuh, but <code>s</code> isn't open.</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896917):
<p>yes it is, the <code>_</code> is actually a proof from which you can show that it is open</p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896964):
<p>it says: <code>interior s = s</code></p>

#### [ Johannes Hölzl (Oct 16 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896994):
<p>then you also need to adapt your <code>choice_eq</code> proof accordingly</p>

#### [ Johan Commelin (Oct 16 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135897076):
<p>Ok, I see. I'll try to do this.</p>

#### [ Johan Commelin (Oct 16 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135897497):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Sorry, but the following still doesn't work:</p>
<div class="codehilite"><pre><span></span><span class="k">have</span> <span class="n">foo</span> <span class="o">:</span> <span class="o">(</span><span class="n">Sup</span> <span class="n">Us</span><span class="o">)</span><span class="bp">.</span><span class="n">s</span> <span class="bp">=</span> <span class="n">Sup</span> <span class="o">(</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="err">&#39;&#39;</span> <span class="n">Us</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Johannes Hölzl (Oct 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898099):
<p>you should get:</p>
<div class="codehilite"><pre><span></span><span class="k">have</span> <span class="n">foo</span> <span class="o">:</span> <span class="o">(</span><span class="n">Sup</span> <span class="n">Us</span><span class="o">)</span><span class="bp">.</span><span class="n">s</span> <span class="bp">=</span> <span class="o">(</span><span class="err">⨆</span><span class="n">a</span><span class="err">∈</span><span class="n">Us</span><span class="o">,</span> <span class="n">a</span><span class="bp">.</span><span class="n">s</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Johan Commelin (Oct 16 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898427):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> That gives me</p>
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">field</span> <span class="kn">notation</span><span class="o">,</span> <span class="n">type</span> <span class="n">is</span> <span class="n">not</span> <span class="n">of</span> <span class="n">the</span> <span class="n">form</span> <span class="o">(</span><span class="n">C</span> <span class="bp">...</span><span class="o">)</span> <span class="n">where</span> <span class="n">C</span> <span class="n">is</span> <span class="n">a</span> <span class="kn">constant</span>
  <span class="n">a</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="err">?</span><span class="n">m_1</span>
</pre></div>


<p>I now have the following ugly proof myself:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">Sup_s</span> <span class="o">{</span><span class="n">Us</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">:</span> <span class="o">(</span><span class="n">Sup</span> <span class="n">Us</span><span class="o">)</span><span class="bp">.</span><span class="n">s</span> <span class="bp">=</span> <span class="err">⋃₀</span> <span class="o">(</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="err">&#39;&#39;</span> <span class="n">Us</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="bp">@</span><span class="n">galois_connection</span><span class="bp">.</span><span class="n">l_Sup</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="n">interior</span> <span class="o">(</span><span class="n">gc</span><span class="o">)</span> <span class="n">Us</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">sUnion_image</span><span class="o">]</span>
</pre></div>

#### [ Johannes Hölzl (Oct 16 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898448):
<p>what about <code>have foo : (Sup Us).s = (⨆a∈Us, open_set.s a) := rfl</code></p>

#### [ Johan Commelin (Oct 16 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898745):
<p>Still fails:</p>
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">type</span> <span class="n">ascription</span><span class="o">,</span> <span class="n">term</span> <span class="n">has</span> <span class="n">type</span>
  <span class="err">?</span><span class="n">m_2</span> <span class="bp">=</span> <span class="err">?</span><span class="n">m_2</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="o">(</span><span class="n">Sup</span> <span class="n">Us</span><span class="o">)</span><span class="bp">.</span><span class="n">s</span> <span class="bp">=</span> <span class="err">⨆</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">Us</span><span class="o">),</span> <span class="n">a</span><span class="bp">.</span><span class="n">s</span>
</pre></div>

#### [ Johannes Hölzl (Oct 16 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898976):
<p>how does your <code>gi</code> look like?</p>

#### [ Johan Commelin (Oct 16 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135899032):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">gi</span> <span class="o">:</span> <span class="bp">@</span><span class="n">galois_insertion</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">))</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">))</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">choice</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span> <span class="n">hs</span><span class="o">,</span> <span class="o">{</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">s</span><span class="o">,</span> <span class="n">is_open</span> <span class="o">:=</span> <span class="n">interior_eq_iff_open</span><span class="bp">.</span><span class="n">mp</span> <span class="err">$</span> <span class="n">le_antisymm</span> <span class="n">interior_subset</span> <span class="n">hs</span> <span class="o">},</span>
  <span class="n">gc</span> <span class="o">:=</span> <span class="n">galois_connection</span><span class="bp">.</span><span class="n">dual</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">gc</span><span class="o">,</span>
  <span class="n">le_l_u</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">interior_subset</span><span class="o">,</span>
  <span class="n">choice_eq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span> <span class="n">hs</span><span class="o">,</span> <span class="n">le_antisymm</span> <span class="n">interior_subset</span> <span class="n">hs</span> <span class="o">}</span>
</pre></div>

#### [ Johannes Hölzl (Oct 16 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900200):
<p>hm</p>
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">complete_lattice</span>
</pre></div>


<p>somewhere <code>set</code> gets unfolded and the <code>pi</code> instance is used. Then we get different <code>Sup</code> and <code>Inf</code>.</p>

#### [ Reid Barton (Oct 16 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900203):
<p>Kudos to the individual who came up with <span class="emoji emoji-1f52b" title="gun">:gun:</span> for Galois insertion btw</p>

#### [ Johan Commelin (Oct 16 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900316):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> Hmmm... I think I'm giving up on debugging this. It is too annoying. If you feel like debugging it, I haven't made much progress since my gist.</p>

#### [ Johannes Hölzl (Oct 16 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900464):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">complete_lattice</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">order_dual</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">complete_lattice</span> <span class="bp">_</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">galois_insertion</span><span class="bp">.</span><span class="n">lift_complete_lattice</span>
    <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">))</span> <span class="o">(</span><span class="n">order_dual</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">))</span> <span class="bp">_</span> <span class="n">interior</span> <span class="o">(</span><span class="bp">@</span><span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">X</span><span class="o">)</span> <span class="bp">_</span> <span class="n">gi</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">Sup_s</span> <span class="o">{</span><span class="n">Us</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">open_set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">:</span> <span class="o">(</span><span class="n">Sup</span> <span class="n">Us</span><span class="o">)</span><span class="bp">.</span><span class="n">s</span> <span class="bp">=</span> <span class="err">⨆</span><span class="n">s</span><span class="err">∈</span><span class="n">Us</span><span class="o">,</span> <span class="n">open_set</span><span class="bp">.</span><span class="n">s</span> <span class="n">s</span> <span class="o">:=</span>
<span class="n">rfl</span>
</pre></div>


<p>this works</p>

#### [ Johannes Hölzl (Oct 16 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900784):
<p><code>(order_dual (set _))</code> is already enough. Then the elaborator finds the right instance, instead of the instance for <code>X -&gt; Prop</code></p>

#### [ Johan Commelin (Oct 16 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900908):
<p>Ok, so my instance is wrong... hmmzzz. Thanks for finding this bug!</p>

#### [ Alex J. Best (Oct 16 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135907294):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>  Thanks, after trying to teach myself some lean on the side and lurking here a lot without doing anything I'm glad someone found my first "contribution" as funny as I did</p>

#### [ David Michael Roberts (Oct 17 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135958522):
<blockquote>
<p>then it should just be called <code>galois_nnection</code></p>
</blockquote>
<p>or a cogalois-nnection (sorry)</p>


{% endraw %}
