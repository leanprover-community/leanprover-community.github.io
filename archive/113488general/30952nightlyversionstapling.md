---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30952nightlyversionstapling.html
---

## Stream: [general](index.html)
### Topic: [nightly version stapling](30952nightlyversionstapling.html)

---


{% raw %}
#### [ Sebastian Ullrich (Mar 04 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/123270930):
<p>sneak peek: <a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a></p>

#### [ Mario Carneiro (Mar 04 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/123271176):
<p>cool! Are you autogenerating the chglog diffs?</p>

#### [ Sebastian Ullrich (Mar 05 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/123278141):
<p>Yep!</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124221663):
<p>After wasting hours and hours of cloud build time on fixing broken bash scripts, the pre-monad-PR nightly has finally landed for all platforms: <a href="https://github.com/leanprover/lean-nightly/releases/tag/nightly-2018-03-19" target="_blank" title="https://github.com/leanprover/lean-nightly/releases/tag/nightly-2018-03-19">https://github.com/leanprover/lean-nightly/releases/tag/nightly-2018-03-19</a><br>
Now building the latest commit. Regular daily (well, nightly) builds should work starting tomorrow.</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124224825):
<p>Monad nightly: <a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a></p>

#### [ Simon Hudon (Mar 26 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124224904):
<p>Nice! Thanks for doing it!</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124225247):
<p>So feel free to discuss now how leanpkg should interact with all that :)</p>

#### [ Simon Hudon (Mar 26 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124226089):
<p><em>stretches</em> alrighty!</p>

#### [ Simon Hudon (Mar 26 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124226137):
<p>For starter, it might be good to have a separate <code>leanpkg</code> project with a separate way of installing it.</p>

#### [ Simon Hudon (Mar 26 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124226267):
<p>Then I think we should have a field in <code>leanpkg.toml</code></p>

#### [ Simon Hudon (Mar 26 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229253):
<p>I think in general we should be able to choose a version of Lean (in the project file) and have the version of the packages worked out for us. The most difficult part would be to let multiple versions of Lean exist on your system. I recognize that we talked about this before but this might be a good time to separate <code>leanpkg</code> and <code>lean</code></p>

#### [ Simon Hudon (Mar 26 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229281):
<p>Or ... that would mean install a "master" version of Lean which <code>leanpkg</code> uses  as its interpreter and then curate a collection of nightlies</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229353):
<p>Yes, in absence of a native backend that may be the best solution. Though nightly releases may lose their importance until Lean 4 is merged into master.</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229424):
<p>Note that you can now store a nightly version string in the <code>lean_version</code> config variable, and leanpkg will warn you about a mismatch</p>

#### [ Simon Hudon (Mar 26 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229488):
<p>That's nice to know! Can you give me an example of the syntax?</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229527):
<p><code>lean_version = "nightly-2018-03-26"</code>, same string as in the release names and tags</p>

#### [ Simon Hudon (Mar 26 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229613):
<p>Nice! What I've been using lately is a file called <code>lean_version</code> with the exact hash that my project is using. Travis uses it to compile the right version of Lean and I have git hooks that block commits if that version doesn't match my system's version</p>

#### [ Sebastian Ullrich (Mar 26 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229664):
<blockquote>
<p>have the version of the packages worked out for us </p>
</blockquote>
<p>I believe this part isn't exactly trivial either. Do we grep through the repository for a commit with a fitting leanpkg.toml, or do we use tags for that (certainly not branches like for the stable releases)? What if there is no commit for that exact nightly?</p>

#### [ Simon Hudon (Mar 26 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229679):
<p>I assume if <code>mathlib</code> was to be tagged with the nightly it was built with, upgrade would upgrade to the right version</p>

#### [ Simon Hudon (Mar 26 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229757):
<p>You're right</p>

#### [ Simon Hudon (Mar 26 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229814):
<p>It might require discipline from the maintainers so that if they skip versions, they still tag a commit that will build with that version. That sounds cumbersome</p>

#### [ Simon Hudon (Mar 26 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229845):
<p>The other possibility is to work in one of two modes: flexible or strict. In a strict mode, you ask leanpkg what is the latest nightly that all your dependencies work with and you upgrade to that one</p>

#### [ Simon Hudon (Mar 26 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124229914):
<p>Flexible would be a more relaxed form of that rule ... or just say "screw it" and get something that works with a more recent version of Lean and hope for the best</p>

#### [ Andrew Ashworth (Mar 26 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124235668):
<p>ahh, versioning. i just read a blog post about it in go <a href="https://blog.golang.org/versioning-proposal" target="_blank" title="https://blog.golang.org/versioning-proposal">https://blog.golang.org/versioning-proposal</a></p>

#### [ Simon Hudon (Mar 26 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124236309):
<p>I've been trying to come up with a sensible notion of semantic versioning for Lean but the <code>meta</code> language usually doesn't fit in well</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124423475):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What do you think would be a realistic Lean versioning scheme for mathlib? Store the nightly version in the toml/a tag, then upgrade only when important upstream fixes/features are available?</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124423579):
<p>I think that's a fine idea. Assuming that old nightlies are now tracked, which it sounds like is working now, we could just put an appropriate nightly or lean git commit hash in the <code>lean_version</code> field or wherever, and update it when mathlib updates to lean</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124423654):
<p>Yea, see <a href="#narrow/stream/113488-general/subject/nightly.20version.20stapling/near/124229424" title="#narrow/stream/113488-general/subject/nightly.20version.20stapling/near/124229424">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/nightly.20version.20stapling/near/124229424</a></p>

#### [ Mario Carneiro (Mar 30 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124423741):
<p>Oh, nice, days are nicer than hashes for this</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124423762):
<p>So we can implement this in mathlib now?</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124423925):
<p>Yep, you can manually set that field right now and leanpkg will warn people about any mismatch</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424040):
<p>The only thing missing is a tool that automates that and setting up the correct Lean version. I've almost accidentally started a Twitter thread about that: <a href="https://twitter.com/derKha/status/979385452506550272" target="_blank" title="https://twitter.com/derKha/status/979385452506550272">https://twitter.com/derKha/status/979385452506550272</a></p>
<div class="inline-preview-twitter"><div class="twitter-tweet"><a href="https://twitter.com/derKha/status/979385452506550272" target="_blank"><img class="twitter-avatar" src="https://uploads.zulipusercontent.net/eed2c5a7af22b4ad0091fa38a5bef677be9295f1/687474703a2f2f7062732e7477696d672e636f6d2f70726f66696c655f696d616765732f3739313833303132353830393530303136302f344e5a62634475635f6e6f726d616c2e6a7067"></a><p>Naming suggestions for an application that downloads and manages your installed Lean versions (think rustup)?</p><span>- Sebastian Ullrich (@derKha)</span></div></div>

#### [ Mario Carneiro (Mar 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424138):
<p><code>leanup</code> makes me giggle</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424217):
<p>I feel like most puns/connotations are completely flying over my head :)</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424224):
<p>But I'm confused why this is distinct from <code>leanpkg</code></p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424294):
<p>See <a href="https://twitter.com/derKha/status/979422420653297666" target="_blank" title="https://twitter.com/derKha/status/979422420653297666">https://twitter.com/derKha/status/979422420653297666</a></p>
<div class="inline-preview-twitter"><div class="twitter-tweet"><a href="https://twitter.com/derKha/status/979422420653297666" target="_blank"><img class="twitter-avatar" src="https://uploads.zulipusercontent.net/eed2c5a7af22b4ad0091fa38a5bef677be9295f1/687474703a2f2f7062732e7477696d672e636f6d2f70726f66696c655f696d616765732f3739313833303132353830393530303136302f344e5a62634475635f6e6f726d616c2e6a7067"></a><p><a href="https://twitter.com/graydon_pub" target="_blank" title="https://twitter.com/graydon_pub">@graydon_pub</a> I think I agree with you, but in our case the package manager is written in Lean. Since we still lack good FFI for e.g. downloading files, or even native compilation, I'm inclined to write the meta installer in Rust for now. Not rewriting the kernel in Lean either anytime soon...</p><span>- Sebastian Ullrich (@derKha)</span></div></div>

#### [ Mario Carneiro (Mar 30 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424321):
<p>so it's a bootstrapping issue?</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424513):
<p>More like a "our current interpreter and object file format aren't exactly standalone and also calling out to <code>curl</code> isn't very platform independent" issue</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424525):
<p>I.e. "probably the wrong tool for the job"</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424541):
<p>What's wrong with having separate install instructions for each platform, as long as you can keep it to one line for each?</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424643):
<p>It's not install instructions, the tool is supposed to download the correct Lean version by itself</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424767):
<p>The current leanpkg code is already quite ham-fisted in a few ways, it's really not fun to program with such a minimal API</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424784):
<p>What has a minimal API here? Lean or leanpkg?</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424789):
<p>Lean</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424838):
<p>Like... the most basic string functions</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424894):
<p>There are a lot of list functions, can those be repurposed? Or do they have to be implemented in C</p>

#### [ Mario Carneiro (Mar 30 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124424899):
<p>I'd be happy to write what I can in lean, but I lack some necessary primitives</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124425386):
<p>Thanks, but that still leaves the other two issues... I suppose we could bundle wget for Windows with it if we really wanted to</p>

#### [ Andrew Ashworth (Mar 30 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124425428):
<p>do you enjoy working on leanpkg? a quick and dirty solution is to use a cross-platform package manager that already exists</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124425501):
<p>I guess I don't exactly... but I believe even the current leanpkg satisfies our specific needs better than a generic package manager ever could</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124429614):
<p>For another example, we'll probably have to parse the JSON returned from Github's Releases API</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124429810):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Thoughts?</p>

#### [ Gabriel Ebner (Mar 31 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124453211):
<p><code>leanup</code> sounds reasonable to me.  I agree that it should be separately distributed.  It could even provide <code>lean</code> and <code>leanpkg</code> executables that automatically use the correct version depending on the <code>leanpkg.toml</code> (or download them if necessary).  Then we wouldn't even need to change any tooling that already uses <code>lean</code> or <code>leanpkg</code>.</p>

#### [ Gabriel Ebner (Mar 31 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124453262):
<p>In the long run, I think it should be written in Lean as well.  With code generation on the horizon, this shouldn't pose a problem for distribution.  And API-wise I guess there is some demand for networking functionality in Lean anyhow.  Parsing JSON is the easiest part, we have parser combinators. <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Gabriel Ebner (Mar 31 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124453308):
<p>For now, I believe that a rust implementation is fine.  It's probably even easier to distribute than a python script.</p>

#### [ Gabriel Ebner (Mar 31 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124453355):
<p>There should probably be a way to use local git builds via leanup as well.</p>

#### [ Gabriel Ebner (Mar 31 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124453450):
<p>Since we switched to static linking, the nightlies even work on NixOS.  So no complaints from my sides.  And if we switch back to dynamic linking, I'll just PR what we do in rustup: <a href="https://github.com/NixOS/nixpkgs/blob/599a2238386b6f1f293f888d068122b46e1bde23/pkgs/development/tools/rust/rustup/0001-dynamically-patchelf-binaries.patch" target="_blank" title="https://github.com/NixOS/nixpkgs/blob/599a2238386b6f1f293f888d068122b46e1bde23/pkgs/development/tools/rust/rustup/0001-dynamically-patchelf-binaries.patch">https://github.com/NixOS/nixpkgs/blob/599a2238386b6f1f293f888d068122b46e1bde23/pkgs/development/tools/rust/rustup/0001-dynamically-patchelf-binaries.patch</a></p>

#### [ Sebastian Ullrich (Mar 31 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124457614):
<blockquote>
<p>In the long run, I think it should be written in Lean as well. </p>
</blockquote>
<p>I agree.</p>
<blockquote>
<p>It's probably even easier to distribute than a python script.</p>
</blockquote>
<p>Exactly, that was my main motivation.</p>
<blockquote>
<p>There should probably be a way to use local git builds via leanup as well. </p>
</blockquote>
<p>Yes, though I'm not yet sure what it should look like.</p>

#### [ Sebastian Ullrich (Mar 31 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124457707):
<blockquote>
<p>Then we wouldn't even need to change any tooling that already uses <code>lean</code> or <code>leanpkg</code>. </p>
</blockquote>
<p>Right, though then I'd like to "hijack" <code>leanpkg configure</code> etc to also take care of setting up the correct Lean version.  I'm really not sure if that would be less confusing than telling people to use <code>leanup configure</code> instead of <code>leanpkg configure</code>.</p>

#### [ Gabriel Ebner (Mar 31 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124457812):
<blockquote>
<p>I'd like to "hijack" leanpkg configure etc to also take care of setting up the correct Lean version.</p>
</blockquote>
<p>My suggestion was to hijack <em>everything</em>, i.e., even if you call just <code>lean</code>, then <code>leanup</code>automatically determines the correct version in the background, downloads the binaries, and then runs the correct <code>lean</code> binary.</p>

#### [ Gabriel Ebner (Mar 31 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124457851):
<p>I think that's the easiest solution to support multiple lean versions in the editors.</p>

#### [ Sebastian Ullrich (Mar 31 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124457954):
<p>Okay, bad example. What I meant was hijacking and changing the _semantics_ of e.g. <code>leanpkg add/upgrade</code> so that they respect nightly versions</p>

#### [ Gabriel Ebner (Mar 31 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124458003):
<p>I think <em>everything</em> should respect the nightly versions.  That is, when you run <code>lean</code>, <code>leanup</code> looks for a <code>leanpkg.toml</code>, checks the <code>version</code> field, and then executes the correct <code>lean</code> executable.  How else would you work with two packages that require different Lean versions?</p>

#### [ Gabriel Ebner (Mar 31 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124458047):
<p>Or did you mean that <code>leanpkg upgrade</code> upgrades the version field as well?</p>

#### [ Sebastian Ullrich (Mar 31 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124458342):
<p>No, I think there should be a separate command for upgrading the Lean version (just on <code>leanup</code> or should it be injected into <code>leanpkg</code> too??). I was thinking of <code>leanpkg upgrade</code> looking at the dependencies' Lean versions when deciding which commit to upgrade to. But perhaps that isn't really necessary - when <code>leanpkg</code> warns you that the Lean versions are out of sync when building an upgraded package, perhaps you're just supposed to run <code>lean-upgrade</code> afterwards.</p>

#### [ Gabriel Ebner (Mar 31 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124458442):
<p>Ah, I see what you're talking about.  This is hard.  I don't think leanpkg warns you at the moment if one of the dependencies' Lean version is wrong.  It's also not clear which nightly version to pick (the one for dependency A, or the one for dependency B, or their maximum??).  If <code>leanpkg</code> however adjusts the <code>version</code> field correctly, then everything would just work with my proposal.</p>

#### [ Sebastian Ullrich (Mar 31 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124458483):
<p>I.e. our main goal should be reproducibility when not touching the leanpkg.toml file. But when you want to upgrade either your Lean nightly version or a dependency's version, we probably shouldn't try to be "clever" but just jump to the upstream head of everything.</p>

#### [ Sebastian Ullrich (Mar 31 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124458570):
<blockquote>
<p>I don't think leanpkg warns you at the moment if one of the dependencies' Lean version is wrong. </p>
</blockquote>
<p>Right. This would work automatically when we start building dependencies eagerly on <code>configure</code>.</p>

#### [ Mario Carneiro (Apr 02 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124508035):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> How can you tell what lean commit a nightly corresponds to? The bot botson commit doesn't say the commit hash anymore (and is now Leo?)</p>

#### [ Sebastian Ullrich (Apr 02 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124518628):
<p>Yes, Leo is now a bot <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Sebastian Ullrich (Apr 02 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124518667):
<p>The commit hash is next to the release description <a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a></p>

#### [ Sebastian Ullrich (Apr 02 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124518811):
<p>Not sure why I removed it from the cmdline output...</p>

#### [ Sebastian Ullrich (Apr 02 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124519318):
<p>If anyone's wondering where the Windows nightlies are: Apparently you have to ask the AppVeyor guys personally to enable cron builds...</p>

#### [ Kenny Lau (Apr 02 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124519322):
<p>I'm more wondering when will the mathlib have a tick mark</p>

#### [ Patrick Massot (Apr 02 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124530618):
<p>Does anyone know a working combination of Lean nightly + mathlib which includes the <code>wlog</code> tactic?</p>

#### [ Patrick Massot (Apr 02 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124530628):
<p>linux nighly of course</p>

#### [ Scott Morrison (Apr 08 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785403):
<p>so... leanpkg now helpfully says things like: <code> WARNING: Lean version mismatch: installed version is master, but package requires nightly-2018-04-06</code>.</p>

#### [ Scott Morrison (Apr 08 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785409):
<p>Is there any automatic help installing the right version of Lean? (Or do I need to learn how to install nightlies, after happily working off master all this time?)</p>

#### [ Simon Hudon (Apr 08 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785503):
<p>Sorry not answering your question but: is the warning about one of your dependencies or about your own package?</p>

#### [ Scott Morrison (Apr 08 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785504):
<p>Attempting to learn how to install nightlies...<br>
1) The first google result for "lean nightly" is the rather unhelpful &lt;<a href="https://github.com/leanprover/lean-nightly" target="_blank" title="https://github.com/leanprover/lean-nightly">https://github.com/leanprover/lean-nightly</a>&gt;.<br>
2) I downloaded the latest Lean nightly from &lt;<a href="https://leanprover.github.io/download/" target="_blank" title="https://leanprover.github.io/download/">https://leanprover.github.io/download/</a>&gt;, but there's no way to determine which date it's from, and it still gives the same error.</p>

#### [ Scott Morrison (Apr 08 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785505):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>  --- sorry, should have specified this is trying to compile mathlib.</p>

#### [ Scott Morrison (Apr 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785545):
<p>Am I meant to be installing nightlies from somewhere else?</p>

#### [ Simon Hudon (Apr 08 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785553):
<p>Thanks! I can help if you just need help installing nightlies</p>

#### [ Scott Morrison (Apr 08 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785590):
<p>Ah, I found &lt;<a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a>&gt;.</p>

#### [ Simon Hudon (Apr 08 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785594):
<p>Often, I just leech off of Mario's knowledge and look at <code>mathlib</code>'s travis file for that kind of stuff</p>

#### [ Scott Morrison (Apr 08 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785595):
<p>The main README.md for that repository desperately needs to contain a link to the releases page.</p>

#### [ Scott Morrison (Apr 08 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785656):
<p>(I've just made a pull request.)</p>

#### [ Simon Hudon (Apr 08 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124785744):
<p>To lean-nightly? It hasn't crossed the ocean yet, it seems. I don't see it</p>

#### [ Kevin Buzzard (Apr 08 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124793413):
<p>I fixed the leanpkg warnings for one of my projects by changing the obvious line in <code>leanpkg.toml</code> to <code>lean_version = "nightly-2018-04-02"</code></p>

#### [ Scott Morrison (Apr 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124795679):
<p>Is anyone using a lean-nightly on OS X? When I try to use lean from a nightly, I just get:</p>
<div class="codehilite"><pre><span></span>dyld: Library not loaded: /usr/local/opt/gmp/lib/libgmp.10.dylib
</pre></div>

#### [ Scott Morrison (Apr 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124795682):
<p>I'm pretty sure <code>gmp</code> is installed; plenty of other things are using it.</p>

#### [ Scott Morrison (Apr 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124795747):
<p>It seems for me that file is at <code>/opt/local/lib/libgmp.10.dylib</code> instead.</p>

#### [ Scott Morrison (Apr 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124795748):
<p>Is this some homebrew vs macports incompatibility?</p>

#### [ Scott Morrison (Apr 08 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124795999):
<p>Yup, with <code>gmp</code> provided by homebrew instead of macports, everything works.</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124950344):
<p>In case you haven't seen the mathlib commits: <a href="https://github.com/Kha/elan" target="_blank" title="https://github.com/Kha/elan">https://github.com/Kha/elan</a></p>

#### [ Patrick Massot (Apr 11 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124950367):
<p>Thank you very much!</p>

#### [ Patrick Massot (Apr 11 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124950381):
<p>Is this something we can already try?</p>

#### [ Patrick Massot (Apr 11 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124950459):
<p>What does elan mean? Apart from being an anagram of lean?</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124950791):
<p>élan :) . Not an acronym... yet</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124950868):
<p>There may be some bugs and missing features, but I do believe it's usable already. mathlib's Travis config is now using it.</p>

#### [ Patrick Massot (Apr 11 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124950938):
<p>Is there any kind of documentation?</p>

#### [ Patrick Massot (Apr 11 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124950945):
<p>apart from mathlib travis?</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951075):
<p>The individual commands are documented inside the tool, and, as the readme hopefully implies, you shouldn't even need to worry about those if you just want to use the right version of <code>leanpkg</code> for a package. Doc contributions are welcome, you guys seem to be very prolific in that.</p>

#### [ Patrick Massot (Apr 11 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951417):
<p><code>error: invalid channel name 'master' in 'lean-scratchpad/leanpkg.toml'
info: caused by: invalid toolchain name: 'master'</code></p>

#### [ Patrick Massot (Apr 11 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951429):
<p>This is what I get when I try <code>leanpkg upgrade</code> after installing elan</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951521):
<p>Right, <code>lean_version = "master"</code> used to be a thing... the preferred way is to set a specific nightly there now, but I guess we should still make <code>master</code> default to the <code>nightly</code> channel.</p>

#### [ Patrick Massot (Apr 11 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951580):
<p>what would be the syntax to specify a nightly?</p>

#### [ Patrick Massot (Apr 11 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951588):
<p>What if my specification is: whatever nightly works with that given mathlib version?</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951743):
<p>Then you should copy the version from mathlib's config in your <code>_target</code> dir. I have plans to document how to deal with <code>elan</code> and <code>leanpkg upgrade</code>, but I first need to change <code>leanpkg</code> for that.</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951842):
<p>Btw, you can also select toolchains like this: <code>leanpkg +nightly ...</code></p>

#### [ Patrick Massot (Apr 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951850):
<p>Ok, let me check my understanding. Currently this helps if I have different projects requiring different versions of Lean. But it does not help me if I have one project and I want to upgrade Lean+mathlib while keeping them in a consistent state?</p>

#### [ Patrick Massot (Apr 11 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951910):
<p>Or does it?</p>

#### [ Patrick Massot (Apr 11 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951913):
<p>I'm confused and I need to sleep</p>

#### [ Patrick Massot (Apr 11 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124951965):
<p>Need to teach how to prove existence of <a href="https://www.youtube.com/watch?v=RYH_KXhF1SY" target="_blank" title="https://www.youtube.com/watch?v=RYH_KXhF1SY">https://www.youtube.com/watch?v=RYH_KXhF1SY</a> tomorrow morning</p>
<div class="youtube-video message_inline_image"><a data-id="RYH_KXhF1SY" href="https://www.youtube.com/watch?v=RYH_KXhF1SY" target="_blank" title="https://www.youtube.com/watch?v=RYH_KXhF1SY"><img src="https://i.ytimg.com/vi/RYH_KXhF1SY/default.jpg"></a></div>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124952037):
<p>It doesn't help you with selecting the best nightly version suitable for all your dependencies (which gets complicated with more than one dependency) _yet_. It does help you to then download and install that version after you've changed your leanpkg.toml.</p>

#### [ Patrick Massot (Apr 11 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124952065):
<p>Yes, it seems it did that</p>

#### [ Patrick Massot (Apr 11 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124952116):
<p>Any reson why leanpkg uses <code>upgrade</code> and elan uses <code>update</code>?</p>

#### [ Patrick Massot (Apr 11 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124952123):
<p>Now I'm bound to hit the wrong one at least half the time</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124952211):
<p>Heh, I guess you're right. I didn't name either of them and am open to changing one of them.</p>

#### [ Patrick Massot (Apr 11 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124952284):
<p>I have a slight preference for upgrade, because it's what apt uses when you actually want some change to installed stuff. But I wouldn't mind having update</p>

#### [ Simon Hudon (Apr 12 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124952922):
<p>I'm really excited to see Elan happen!</p>

#### [ Simon Hudon (Apr 12 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124952934):
<p>I tried to install it and got the following:</p>
<div class="codehilite"><pre><span></span>info: downloading component &#39;lean&#39;
 18.1 MiB /  18.1 MiB (100 %) 210.8 KiB/s ETA:   0 s
info: installing component &#39;lean&#39;
info: rolling back changes
error: failed to extract package
info: caused by: invalid gzip header
</pre></div>

#### [ Sebastian Ullrich (Apr 12 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953252):
<p>Huh, that's a new one. OS X?</p>

#### [ Simon Hudon (Apr 12 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953261):
<p>Yes! Sorry, I should have said that</p>

#### [ Sebastian Ullrich (Apr 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953304):
<p>Oops, I thought we were using <code>.tar.gz</code> for OS X instead of <code>.zip</code> <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Simon Hudon (Apr 12 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953379):
<p>tsk tsk</p>

#### [ Simon Hudon (Apr 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953406):
<p>On a slightly related note: any chance that <code>leanpkg</code> will get some <code>flycheck</code> support in the future?</p>

#### [ Sebastian Ullrich (Apr 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953415):
<p>What do you mean by that? The <code>leanpkg.toml</code>?</p>

#### [ Simon Hudon (Apr 12 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953546):
<p>I mean when you call <code>leanpkg build</code>, get the errors that you get in the flycheck error list buffer</p>

#### [ Sebastian Ullrich (Apr 12 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953611):
<p>Shouldn't it show the same errors already...? Or do you mean the format...?</p>

#### [ Sebastian Ullrich (Apr 12 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953693):
<p>Okay, I'll have to fix OS X (and Windows) support tomorrow. The crazy thing is, the <code>elan</code> OS X release builds actually use <code>.tar.gz</code>. I took that from a CI template.</p>

#### [ Simon Hudon (Apr 12 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953770):
<p>Let me take you through a use case. I'm editting foo.lean which imports foobar.lean, bar.lean, barfoo.lean foo.lean, etc. I upgrade Lean and then mathlib and my project no longer type check so I do <code>M-x lean-leanpkg-build</code> to find the first thing that breaks and follow the series of breakages until I fixed everything. I want to fix stuff in the topological order of imports so that I don't have to fix the same file twice.</p>

#### [ Simon Hudon (Apr 12 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124953772):
<p>Thanks!</p>

#### [ Sebastian Ullrich (Apr 12 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124996475):
<p>I believe I fixed elan, hopefully? <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span> /cc <span class="user-mention" data-user-id="110026">@Simon Hudon</span> <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Kenny Lau (Apr 12 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124996524):
<p><a href="#narrow/stream/113488-general/topic/mathlib.20nightly.20dependence" title="#narrow/stream/113488-general/topic/mathlib.20nightly.20dependence">link to convo</a></p>

#### [ Kenny Lau (Apr 12 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124996539):
<div class="codehilite"><pre><span></span>$ curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh
info: downloading installer
sh: line 105: unzip: command not found
chmod: cannot access &#39;/tmp/tmp.DIauNKqwfZ/elan-init.exe&#39;: No such file or directory
elan: command failed: chmod u+x /tmp/tmp.DIauNKqwfZ/elan-init.exe
</pre></div>

#### [ Simon Hudon (Apr 12 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124996610):
<p>It now works! Thanks!</p>

#### [ Kenny Lau (Apr 12 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124996618):
<p>i guess i have to turn on the linux subsystem in windows, wait</p>

#### [ Simon Hudon (Apr 12 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124996911):
<p>I just tried <code>install nightly</code> and got the following:</p>
<div class="codehilite"><pre><span></span>$ elan toolchain install nightly
 51.3 KiB /  51.3 KiB (100 %)  40.5 KiB/s ETA:   0 s
info: downloading component &#39;lean&#39;
 16.8 MiB /  16.8 MiB (100 %) 176.8 KiB/s ETA:   0 s
info: installing component &#39;lean&#39;

  nightly-x86_64-apple-darwin installed - (error reading lean version)
</pre></div>

#### [ Simon Hudon (Apr 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/124999701):
<p>Lean seems sort of installed but here is what happens when I try to call it:</p>
<div class="codehilite"><pre><span></span>$ lean -v
error: command failed: &#39;lean&#39;
info: caused by: Permission denied (os error 13)
</pre></div>

#### [ Sebastian Ullrich (Apr 12 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125003682):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> But the initial stable installation worked o.o? What are the permissions on <code>~/.elan/toolchains/nightly-*/bin/lean</code>?</p>

#### [ Simon Hudon (Apr 12 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125004215):
<p>Actually when installing elan, I also get trouble from <code>stable</code>:</p>
<div class="codehilite"><pre><span></span>1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
1

info: downloading component &#39;lean&#39;
 18.1 MiB /  18.1 MiB (100 %) 136.0 KiB/s ETA:   0 s
info: installing component &#39;lean&#39;
info: default toolchain set to &#39;stable&#39;

  stable installed - (error reading lean version)


Elan is installed now. Great!
</pre></div>


<p>But I can call Lean: <code>lean -v</code></p>
<div class="codehilite"><pre><span></span>$ lean -v
Lean (version 3.3.1, commit d36b859c6579, RELEASE)
</pre></div>

#### [ Simon Hudon (Apr 12 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125004376):
<p>To answer your question, here are the permission on <code>lean</code>:</p>
<div class="codehilite"><pre><span></span>$ ls -la ~/.elan/toolchains/nightly-*/bin/lean
-rw-r--r--  1 simon  staff  12248272 12 Apr 17:04 /Users/simon/.elan/toolchains/nightly-x86_64-apple-darwin/bin/lean
</pre></div>

#### [ Sebastian Ullrich (Apr 13 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125006764):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Thanks, this should be fixed in 0.3.2. You can <code>elan self update</code> in a few minutes and reinstall the broken toolchains after removing them, or you can just do <code>chmod u+x ~/.elan/toolchains/*/bin/*</code> yourself of course.</p>

#### [ Simon Hudon (Apr 13 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125006775):
<p>Thanks!</p>

#### [ Sebastian Ullrich (Apr 13 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125006927):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> What prompt were you using for that (mingw/cygwin/git bash)? Can't you install unzip there?</p>

#### [ Sebastian Ullrich (Apr 13 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125007026):
<p>I'm not sure what the best Windows installation method would be. Perhaps it's just "download the latest Windows release, unpack it and run the exe in a cmd prompt"?</p>

#### [ Andrew Ashworth (Apr 13 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125008079):
<p>i think all the options for non-technical users kinda stink on windows, beyond vending a self-extracting zip or exe</p>

#### [ Simon Hudon (Apr 13 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125008355):
<p>Which commit does <code>stable</code> correspond to?</p>

#### [ Kenny Lau (Apr 13 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125014147):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> my antivirus goes into panic mode when i try to elan</p>

#### [ Sebastian Ullrich (Apr 13 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125022137):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Gah. I don't think I can help with that.</p>

#### [ Sebastian Ullrich (Apr 13 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125022193):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> The latest release at <a href="https://github.com/leanprover/lean/releases" target="_blank" title="https://github.com/leanprover/lean/releases">https://github.com/leanprover/lean/releases</a>. Hopefully it should also be displayed by now?</p>

#### [ Sebastian Ullrich (Apr 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125084643):
<p>Huh, turns out elan can actually be installed by <a href="/user_uploads/3121/aTr--iw7q3zuQPTrImdZX9-x/pasted_image.png" target="_blank" title="pasted_image.png">double-clicking it</a> on Windows</p>
<div class="message_inline_image"><a href="/user_uploads/3121/aTr--iw7q3zuQPTrImdZX9-x/pasted_image.png" target="_blank" title="double-clicking it"><img src="/user_uploads/3121/aTr--iw7q3zuQPTrImdZX9-x/pasted_image.png"></a></div>

#### [ Sebastian Ullrich (Apr 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125084646):
<p>So I think we're fine :)</p>

#### [ Mario Carneiro (Apr 14 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125084833):
<p>How does elan setup differ from previous leanpkg setup layout? I.e. locations of lean and leanpkg and installed repos</p>

#### [ Sebastian Ullrich (Apr 14 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125084932):
<p>The package and Lean root layout is the same. The only difference is that the binaries in <code>~/.elan/bin</code> are just shims pointing to a spefic Lean root in <code>~/.elan/toolchains</code>.</p>

#### [ Sebastian Ullrich (Apr 15 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly%20version%20stapling/near/125107319):
<p>Windows nightlies _finally_ working now <a href="https://github.com/leanprover/lean-nightly/releases/tag/nightly-2018-04-14" target="_blank" title="https://github.com/leanprover/lean-nightly/releases/tag/nightly-2018-04-14">https://github.com/leanprover/lean-nightly/releases/tag/nightly-2018-04-14</a></p>


{% endraw %}
