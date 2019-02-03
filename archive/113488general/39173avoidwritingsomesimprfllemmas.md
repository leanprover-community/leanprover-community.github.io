---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39173avoidwritingsomesimprfllemmas.html
---

## Stream: [general](index.html)
### Topic: [avoid writing (some?) simp-rfl lemmas](39173avoidwritingsomesimprfllemmas.html)

---


{% raw %}
#### [ Johan Commelin (Nov 27 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148623451):
<p>I've brought this up before, but I'dd really hope that there is a way to get rid of blocks like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">simp</span>

<span class="kn">section</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">comma</span> <span class="n">L₂</span> <span class="n">R</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">L₁</span> <span class="err">⟹</span> <span class="n">L₂</span><span class="o">}</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_left_obj_left</span>  <span class="o">:</span> <span class="o">((</span><span class="n">map_left</span> <span class="n">R</span> <span class="n">l</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span>  <span class="bp">=</span> <span class="n">X</span><span class="bp">.</span><span class="n">left</span>                <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_left_obj_right</span> <span class="o">:</span> <span class="o">((</span><span class="n">map_left</span> <span class="n">R</span> <span class="n">l</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">right</span> <span class="bp">=</span> <span class="n">X</span><span class="bp">.</span><span class="n">right</span>               <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_left_obj_hom</span>   <span class="o">:</span> <span class="o">((</span><span class="n">map_left</span> <span class="n">R</span> <span class="n">l</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">hom</span>   <span class="bp">=</span> <span class="n">l</span><span class="bp">.</span><span class="n">app</span> <span class="n">X</span><span class="bp">.</span><span class="n">left</span> <span class="err">≫</span> <span class="n">X</span><span class="bp">.</span><span class="n">hom</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_left_map_left</span>  <span class="o">:</span> <span class="o">((</span><span class="n">map_left</span> <span class="n">R</span> <span class="n">l</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span>  <span class="bp">=</span> <span class="n">f</span><span class="bp">.</span><span class="n">left</span>                <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_left_map_right</span> <span class="o">:</span> <span class="o">((</span><span class="n">map_left</span> <span class="n">R</span> <span class="n">l</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">right</span> <span class="bp">=</span> <span class="n">f</span><span class="bp">.</span><span class="n">right</span>               <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">end</span>

<span class="kn">section</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">comma</span> <span class="n">L</span> <span class="n">R₁</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="err">⟶</span> <span class="n">Y</span><span class="o">}</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">R₁</span> <span class="err">⟹</span> <span class="n">R₂</span><span class="o">}</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_right_obj_left</span>  <span class="o">:</span> <span class="o">((</span><span class="n">map_right</span> <span class="n">L</span> <span class="n">r</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span>  <span class="bp">=</span> <span class="n">X</span><span class="bp">.</span><span class="n">left</span>                 <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_right_obj_right</span> <span class="o">:</span> <span class="o">((</span><span class="n">map_right</span> <span class="n">L</span> <span class="n">r</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">right</span> <span class="bp">=</span> <span class="n">X</span><span class="bp">.</span><span class="n">right</span>                <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_right_obj_hom</span>   <span class="o">:</span> <span class="o">((</span><span class="n">map_right</span> <span class="n">L</span> <span class="n">r</span><span class="o">)</span><span class="bp">.</span><span class="n">obj</span> <span class="n">X</span><span class="o">)</span><span class="bp">.</span><span class="n">hom</span>   <span class="bp">=</span> <span class="n">X</span><span class="bp">.</span><span class="n">hom</span> <span class="err">≫</span> <span class="n">r</span><span class="bp">.</span><span class="n">app</span> <span class="n">X</span><span class="bp">.</span><span class="n">right</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_right_map_left</span>  <span class="o">:</span> <span class="o">((</span><span class="n">map_right</span> <span class="n">L</span> <span class="n">r</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">left</span>  <span class="bp">=</span> <span class="n">f</span><span class="bp">.</span><span class="n">left</span>                 <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">map_right_map_right</span> <span class="o">:</span> <span class="o">((</span><span class="n">map_right</span> <span class="n">L</span> <span class="n">r</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">right</span> <span class="bp">=</span> <span class="n">f</span><span class="bp">.</span><span class="n">right</span>                <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">simp</span>
</pre></div>

#### [ Johan Commelin (Nov 27 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148623511):
<p>You define a new category, and afterwards you have to state pages of trivialities. There must be some structure to this, which we can abuse, so that automation just does this for us. Has there been any thought in this direction?</p>

#### [ Reid Barton (Nov 27 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635044):
<p>You can put <code>@[simp]</code> on the thing you defined (I guess <code>map_left</code>, <code>map_right</code>)</p>

#### [ Johan Commelin (Nov 27 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635271):
<p>Is that good practice? I thought it was some how considered evil, because it marked too much as <code>simp</code>?</p>

#### [ Mario Carneiro (Nov 27 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635344):
<p>it's probably not what you want, because then it will unfold even when it is not being projected</p>

#### [ Johan Commelin (Nov 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635439):
<p>Aha, so I want <code>derive simp-projections</code></p>

#### [ Johan Commelin (Nov 27 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635440):
<p>Is that possible?</p>

#### [ Mario Carneiro (Nov 27 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635603):
<p>in theory</p>

#### [ Mario Carneiro (Nov 27 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635672):
<p>it gets complicated with nested structures, but you could inspect the definition for a structure instance and extract the parts</p>

#### [ Mario Carneiro (Nov 27 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635680):
<p>this would basically be the same thing that the equation compiler does</p>

#### [ Johan Commelin (Nov 27 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/avoid%20writing%20%28some%3F%29%20simp-rfl%20lemmas/near/148635832):
<p>I see. I hope someone with a lot of tactic-fu will pop up and write something like this (-;</p>


{% endraw %}
