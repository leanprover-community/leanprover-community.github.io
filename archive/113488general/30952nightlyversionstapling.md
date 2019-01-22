---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30952nightlyversionstapling.html
---

## [general](index.html)
### [nightly version stapling](30952nightlyversionstapling.html)

#### [Sebastian Ullrich (Mar 04 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/123270930):
sneak peek: https://github.com/leanprover/lean-nightly/releases

#### [Mario Carneiro (Mar 04 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/123271176):
cool! Are you autogenerating the chglog diffs?

#### [Sebastian Ullrich (Mar 05 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/123278141):
Yep!

#### [Sebastian Ullrich (Mar 26 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124221663):
After wasting hours and hours of cloud build time on fixing broken bash scripts, the pre-monad-PR nightly has finally landed for all platforms: https://github.com/leanprover/lean-nightly/releases/tag/nightly-2018-03-19
Now building the latest commit. Regular daily (well, nightly) builds should work starting tomorrow.

#### [Sebastian Ullrich (Mar 26 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124224825):
Monad nightly: https://github.com/leanprover/lean-nightly/releases

#### [Simon Hudon (Mar 26 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124224904):
Nice! Thanks for doing it!

#### [Sebastian Ullrich (Mar 26 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124225247):
So feel free to discuss now how leanpkg should interact with all that :)

#### [Simon Hudon (Mar 26 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124226089):
*stretches* alrighty!

#### [Simon Hudon (Mar 26 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124226137):
For starter, it might be good to have a separate `leanpkg` project with a separate way of installing it.

#### [Simon Hudon (Mar 26 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124226267):
Then I think we should have a field in `leanpkg.toml`

#### [Simon Hudon (Mar 26 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229253):
I think in general we should be able to choose a version of Lean (in the project file) and have the version of the packages worked out for us. The most difficult part would be to let multiple versions of Lean exist on your system. I recognize that we talked about this before but this might be a good time to separate `leanpkg` and `lean`

#### [Simon Hudon (Mar 26 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229281):
Or ... that would mean install a "master" version of Lean which `leanpkg` uses  as its interpreter and then curate a collection of nightlies

#### [Sebastian Ullrich (Mar 26 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229353):
Yes, in absence of a native backend that may be the best solution. Though nightly releases may lose their importance until Lean 4 is merged into master.

#### [Sebastian Ullrich (Mar 26 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229424):
Note that you can now store a nightly version string in the `lean_version` config variable, and leanpkg will warn you about a mismatch

#### [Simon Hudon (Mar 26 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229488):
That's nice to know! Can you give me an example of the syntax?

#### [Sebastian Ullrich (Mar 26 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229527):
`lean_version = "nightly-2018-03-26"`, same string as in the release names and tags

#### [Simon Hudon (Mar 26 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229613):
Nice! What I've been using lately is a file called `lean_version` with the exact hash that my project is using. Travis uses it to compile the right version of Lean and I have git hooks that block commits if that version doesn't match my system's version

#### [Sebastian Ullrich (Mar 26 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229664):
> have the version of the packages worked out for us 

I believe this part isn't exactly trivial either. Do we grep through the repository for a commit with a fitting leanpkg.toml, or do we use tags for that (certainly not branches like for the stable releases)? What if there is no commit for that exact nightly?

#### [Simon Hudon (Mar 26 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229679):
I assume if `mathlib` was to be tagged with the nightly it was built with, upgrade would upgrade to the right version

#### [Simon Hudon (Mar 26 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229757):
You're right

#### [Simon Hudon (Mar 26 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229814):
It might require discipline from the maintainers so that if they skip versions, they still tag a commit that will build with that version. That sounds cumbersome

#### [Simon Hudon (Mar 26 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229845):
The other possibility is to work in one of two modes: flexible or strict. In a strict mode, you ask leanpkg what is the latest nightly that all your dependencies work with and you upgrade to that one

#### [Simon Hudon (Mar 26 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124229914):
Flexible would be a more relaxed form of that rule ... or just say "screw it" and get something that works with a more recent version of Lean and hope for the best

#### [Andrew Ashworth (Mar 26 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124235668):
ahh, versioning. i just read a blog post about it in go https://blog.golang.org/versioning-proposal

#### [Simon Hudon (Mar 26 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124236309):
I've been trying to come up with a sensible notion of semantic versioning for Lean but the `meta` language usually doesn't fit in well

#### [Sebastian Ullrich (Mar 30 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124423475):
@**Mario Carneiro** What do you think would be a realistic Lean versioning scheme for mathlib? Store the nightly version in the toml/a tag, then upgrade only when important upstream fixes/features are available?

#### [Mario Carneiro (Mar 30 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124423579):
I think that's a fine idea. Assuming that old nightlies are now tracked, which it sounds like is working now, we could just put an appropriate nightly or lean git commit hash in the `lean_version` field or wherever, and update it when mathlib updates to lean

#### [Sebastian Ullrich (Mar 30 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124423654):
Yea, see https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/nightly.20version.20stapling/near/124229424

#### [Mario Carneiro (Mar 30 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124423741):
Oh, nice, days are nicer than hashes for this

#### [Mario Carneiro (Mar 30 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124423762):
So we can implement this in mathlib now?

#### [Sebastian Ullrich (Mar 30 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124423925):
Yep, you can manually set that field right now and leanpkg will warn people about any mismatch

#### [Sebastian Ullrich (Mar 30 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424040):
The only thing missing is a tool that automates that and setting up the correct Lean version. I've almost accidentally started a Twitter thread about that: https://twitter.com/derKha/status/979385452506550272

#### [Mario Carneiro (Mar 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424138):
`leanup` makes me giggle

#### [Sebastian Ullrich (Mar 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424217):
I feel like most puns/connotations are completely flying over my head :)

#### [Mario Carneiro (Mar 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424224):
But I'm confused why this is distinct from `leanpkg`

#### [Sebastian Ullrich (Mar 30 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424294):
See https://twitter.com/derKha/status/979422420653297666

#### [Mario Carneiro (Mar 30 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424321):
so it's a bootstrapping issue?

#### [Sebastian Ullrich (Mar 30 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424513):
More like a "our current interpreter and object file format aren't exactly standalone and also calling out to `curl` isn't very platform independent" issue

#### [Sebastian Ullrich (Mar 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424525):
I.e. "probably the wrong tool for the job"

#### [Mario Carneiro (Mar 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424541):
What's wrong with having separate install instructions for each platform, as long as you can keep it to one line for each?

#### [Sebastian Ullrich (Mar 30 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424643):
It's not install instructions, the tool is supposed to download the correct Lean version by itself

#### [Sebastian Ullrich (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424767):
The current leanpkg code is already quite ham-fisted in a few ways, it's really not fun to program with such a minimal API

#### [Mario Carneiro (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424784):
What has a minimal API here? Lean or leanpkg?

#### [Sebastian Ullrich (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424789):
Lean

#### [Sebastian Ullrich (Mar 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424838):
Like... the most basic string functions

#### [Mario Carneiro (Mar 30 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424894):
There are a lot of list functions, can those be repurposed? Or do they have to be implemented in C

#### [Mario Carneiro (Mar 30 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124424899):
I'd be happy to write what I can in lean, but I lack some necessary primitives

#### [Sebastian Ullrich (Mar 30 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124425386):
Thanks, but that still leaves the other two issues... I suppose we could bundle wget for Windows with it if we really wanted to

#### [Andrew Ashworth (Mar 30 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124425428):
do you enjoy working on leanpkg? a quick and dirty solution is to use a cross-platform package manager that already exists

#### [Sebastian Ullrich (Mar 30 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124425501):
I guess I don't exactly... but I believe even the current leanpkg satisfies our specific needs better than a generic package manager ever could

#### [Sebastian Ullrich (Mar 30 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124429614):
For another example, we'll probably have to parse the JSON returned from Github's Releases API

#### [Sebastian Ullrich (Mar 30 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124429810):
@**Gabriel Ebner** Thoughts?

#### [Gabriel Ebner (Mar 31 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124453211):
`leanup` sounds reasonable to me.  I agree that it should be separately distributed.  It could even provide `lean` and `leanpkg` executables that automatically use the correct version depending on the `leanpkg.toml` (or download them if necessary).  Then we wouldn't even need to change any tooling that already uses `lean` or `leanpkg`.

#### [Gabriel Ebner (Mar 31 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124453262):
In the long run, I think it should be written in Lean as well.  With code generation on the horizon, this shouldn't pose a problem for distribution.  And API-wise I guess there is some demand for networking functionality in Lean anyhow.  Parsing JSON is the easiest part, we have parser combinators. :smile:

#### [Gabriel Ebner (Mar 31 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124453308):
For now, I believe that a rust implementation is fine.  It's probably even easier to distribute than a python script.

#### [Gabriel Ebner (Mar 31 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124453355):
There should probably be a way to use local git builds via leanup as well.

#### [Gabriel Ebner (Mar 31 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124453450):
Since we switched to static linking, the nightlies even work on NixOS.  So no complaints from my sides.  And if we switch back to dynamic linking, I'll just PR what we do in rustup: https://github.com/NixOS/nixpkgs/blob/599a2238386b6f1f293f888d068122b46e1bde23/pkgs/development/tools/rust/rustup/0001-dynamically-patchelf-binaries.patch

#### [Sebastian Ullrich (Mar 31 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124457614):
> In the long run, I think it should be written in Lean as well. 

I agree.

> It's probably even easier to distribute than a python script.

Exactly, that was my main motivation.

> There should probably be a way to use local git builds via leanup as well. 

Yes, though I'm not yet sure what it should look like.

#### [Sebastian Ullrich (Mar 31 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124457707):
> Then we wouldn't even need to change any tooling that already uses `lean` or `leanpkg`. 

Right, though then I'd like to "hijack" `leanpkg configure` etc to also take care of setting up the correct Lean version.  I'm really not sure if that would be less confusing than telling people to use `leanup configure` instead of `leanpkg configure`.

#### [Gabriel Ebner (Mar 31 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124457812):
> I'd like to "hijack" leanpkg configure etc to also take care of setting up the correct Lean version.

My suggestion was to hijack *everything*, i.e., even if you call just `lean`, then `leanup`automatically determines the correct version in the background, downloads the binaries, and then runs the correct `lean` binary.

#### [Gabriel Ebner (Mar 31 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124457851):
I think that's the easiest solution to support multiple lean versions in the editors.

#### [Sebastian Ullrich (Mar 31 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124457954):
Okay, bad example. What I meant was hijacking and changing the _semantics_ of e.g. `leanpkg add/upgrade` so that they respect nightly versions

#### [Gabriel Ebner (Mar 31 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124458003):
I think *everything* should respect the nightly versions.  That is, when you run `lean`, `leanup` looks for a `leanpkg.toml`, checks the `version` field, and then executes the correct `lean` executable.  How else would you work with two packages that require different Lean versions?

#### [Gabriel Ebner (Mar 31 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124458047):
Or did you mean that `leanpkg upgrade` upgrades the version field as well?

#### [Sebastian Ullrich (Mar 31 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124458342):
No, I think there should be a separate command for upgrading the Lean version (just on `leanup` or should it be injected into `leanpkg` too??). I was thinking of `leanpkg upgrade` looking at the dependencies' Lean versions when deciding which commit to upgrade to. But perhaps that isn't really necessary - when `leanpkg` warns you that the Lean versions are out of sync when building an upgraded package, perhaps you're just supposed to run `lean-upgrade` afterwards.

#### [Gabriel Ebner (Mar 31 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124458442):
Ah, I see what you're talking about.  This is hard.  I don't think leanpkg warns you at the moment if one of the dependencies' Lean version is wrong.  It's also not clear which nightly version to pick (the one for dependency A, or the one for dependency B, or their maximum??).  If `leanpkg` however adjusts the `version` field correctly, then everything would just work with my proposal.

#### [Sebastian Ullrich (Mar 31 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124458483):
I.e. our main goal should be reproducibility when not touching the leanpkg.toml file. But when you want to upgrade either your Lean nightly version or a dependency's version, we probably shouldn't try to be "clever" but just jump to the upstream head of everything.

#### [Sebastian Ullrich (Mar 31 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124458570):
> I don't think leanpkg warns you at the moment if one of the dependencies' Lean version is wrong. 

Right. This would work automatically when we start building dependencies eagerly on `configure`.

#### [Mario Carneiro (Apr 02 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124508035):
@**Sebastian Ullrich** How can you tell what lean commit a nightly corresponds to? The bot botson commit doesn't say the commit hash anymore (and is now Leo?)

#### [Sebastian Ullrich (Apr 02 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124518628):
Yes, Leo is now a bot :laughing:

#### [Sebastian Ullrich (Apr 02 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124518667):
The commit hash is next to the release description https://github.com/leanprover/lean-nightly/releases

#### [Sebastian Ullrich (Apr 02 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124518811):
Not sure why I removed it from the cmdline output...

#### [Sebastian Ullrich (Apr 02 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124519318):
If anyone's wondering where the Windows nightlies are: Apparently you have to ask the AppVeyor guys personally to enable cron builds...

#### [Kenny Lau (Apr 02 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124519322):
I'm more wondering when will the mathlib have a tick mark

#### [Patrick Massot (Apr 02 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124530618):
Does anyone know a working combination of Lean nightly + mathlib which includes the `wlog` tactic?

#### [Patrick Massot (Apr 02 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124530628):
linux nighly of course

#### [Scott Morrison (Apr 08 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785403):
so... leanpkg now helpfully says things like: ` WARNING: Lean version mismatch: installed version is master, but package requires nightly-2018-04-06`.

#### [Scott Morrison (Apr 08 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785409):
Is there any automatic help installing the right version of Lean? (Or do I need to learn how to install nightlies, after happily working off master all this time?)

#### [Simon Hudon (Apr 08 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785503):
Sorry not answering your question but: is the warning about one of your dependencies or about your own package?

#### [Scott Morrison (Apr 08 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785504):
Attempting to learn how to install nightlies...
1) The first google result for "lean nightly" is the rather unhelpful <https://github.com/leanprover/lean-nightly>.
2) I downloaded the latest Lean nightly from <https://leanprover.github.io/download/>, but there's no way to determine which date it's from, and it still gives the same error.

#### [Scott Morrison (Apr 08 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785505):
@**Simon Hudon**  --- sorry, should have specified this is trying to compile mathlib.

#### [Scott Morrison (Apr 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785545):
Am I meant to be installing nightlies from somewhere else?

#### [Simon Hudon (Apr 08 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785553):
Thanks! I can help if you just need help installing nightlies

#### [Scott Morrison (Apr 08 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785590):
Ah, I found <https://github.com/leanprover/lean-nightly/releases>.

#### [Simon Hudon (Apr 08 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785594):
Often, I just leech off of Mario's knowledge and look at `mathlib`'s travis file for that kind of stuff

#### [Scott Morrison (Apr 08 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785595):
The main README.md for that repository desperately needs to contain a link to the releases page.

#### [Scott Morrison (Apr 08 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785656):
(I've just made a pull request.)

#### [Simon Hudon (Apr 08 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124785744):
To lean-nightly? It hasn't crossed the ocean yet, it seems. I don't see it

#### [Kevin Buzzard (Apr 08 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124793413):
I fixed the leanpkg warnings for one of my projects by changing the obvious line in `leanpkg.toml` to `lean_version = "nightly-2018-04-02"`

#### [Scott Morrison (Apr 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124795679):
Is anyone using a lean-nightly on OS X? When I try to use lean from a nightly, I just get:
````
dyld: Library not loaded: /usr/local/opt/gmp/lib/libgmp.10.dylib 
````

#### [Scott Morrison (Apr 08 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124795682):
I'm pretty sure `gmp` is installed; plenty of other things are using it.

#### [Scott Morrison (Apr 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124795747):
It seems for me that file is at `/opt/local/lib/libgmp.10.dylib` instead.

#### [Scott Morrison (Apr 08 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124795748):
Is this some homebrew vs macports incompatibility?

#### [Scott Morrison (Apr 08 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124795999):
Yup, with `gmp` provided by homebrew instead of macports, everything works.

#### [Sebastian Ullrich (Apr 11 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124950344):
In case you haven't seen the mathlib commits: https://github.com/Kha/elan

#### [Patrick Massot (Apr 11 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124950367):
Thank you very much!

#### [Patrick Massot (Apr 11 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124950381):
Is this something we can already try?

#### [Patrick Massot (Apr 11 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124950459):
What does elan mean? Apart from being an anagram of lean?

#### [Sebastian Ullrich (Apr 11 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124950791):
élan :) . Not an acronym... yet

#### [Sebastian Ullrich (Apr 11 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124950868):
There may be some bugs and missing features, but I do believe it's usable already. mathlib's Travis config is now using it.

#### [Patrick Massot (Apr 11 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124950938):
Is there any kind of documentation?

#### [Patrick Massot (Apr 11 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124950945):
apart from mathlib travis?

#### [Sebastian Ullrich (Apr 11 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951075):
The individual commands are documented inside the tool, and, as the readme hopefully implies, you shouldn't even need to worry about those if you just want to use the right version of `leanpkg` for a package. Doc contributions are welcome, you guys seem to be very prolific in that.

#### [Patrick Massot (Apr 11 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951417):
`error: invalid channel name 'master' in 'lean-scratchpad/leanpkg.toml'
info: caused by: invalid toolchain name: 'master'`

#### [Patrick Massot (Apr 11 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951429):
This is what I get when I try `leanpkg upgrade` after installing elan

#### [Sebastian Ullrich (Apr 11 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951521):
Right, `lean_version = "master"` used to be a thing... the preferred way is to set a specific nightly there now, but I guess we should still make `master` default to the `nightly` channel.

#### [Patrick Massot (Apr 11 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951580):
what would be the syntax to specify a nightly?

#### [Patrick Massot (Apr 11 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951588):
What if my specification is: whatever nightly works with that given mathlib version?

#### [Sebastian Ullrich (Apr 11 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951743):
Then you should copy the version from mathlib's config in your `_target` dir. I have plans to document how to deal with `elan` and `leanpkg upgrade`, but I first need to change `leanpkg` for that.

#### [Sebastian Ullrich (Apr 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951842):
Btw, you can also select toolchains like this: `leanpkg +nightly ...`

#### [Patrick Massot (Apr 11 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951850):
Ok, let me check my understanding. Currently this helps if I have different projects requiring different versions of Lean. But it does not help me if I have one project and I want to upgrade Lean+mathlib while keeping them in a consistent state?

#### [Patrick Massot (Apr 11 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951910):
Or does it?

#### [Patrick Massot (Apr 11 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951913):
I'm confused and I need to sleep

#### [Patrick Massot (Apr 11 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124951965):
Need to teach how to prove existence of https://www.youtube.com/watch?v=RYH_KXhF1SY tomorrow morning

#### [Sebastian Ullrich (Apr 11 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124952037):
It doesn't help you with selecting the best nightly version suitable for all your dependencies (which gets complicated with more than one dependency) _yet_. It does help you to then download and install that version after you've changed your leanpkg.toml.

#### [Patrick Massot (Apr 11 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124952065):
Yes, it seems it did that

#### [Patrick Massot (Apr 11 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124952116):
Any reson why leanpkg uses `upgrade` and elan uses `update`?

#### [Patrick Massot (Apr 11 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124952123):
Now I'm bound to hit the wrong one at least half the time

#### [Sebastian Ullrich (Apr 11 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124952211):
Heh, I guess you're right. I didn't name either of them and am open to changing one of them.

#### [Patrick Massot (Apr 11 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124952284):
I have a slight preference for upgrade, because it's what apt uses when you actually want some change to installed stuff. But I wouldn't mind having update

#### [Simon Hudon (Apr 12 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124952922):
I'm really excited to see Elan happen!

#### [Simon Hudon (Apr 12 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124952934):
I tried to install it and got the following:

```
info: downloading component 'lean'
 18.1 MiB /  18.1 MiB (100 %) 210.8 KiB/s ETA:   0 s                
info: installing component 'lean'
info: rolling back changes
error: failed to extract package
info: caused by: invalid gzip header
```

#### [Sebastian Ullrich (Apr 12 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953252):
Huh, that's a new one. OS X?

#### [Simon Hudon (Apr 12 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953261):
Yes! Sorry, I should have said that

#### [Sebastian Ullrich (Apr 12 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953304):
Oops, I thought we were using `.tar.gz` for OS X instead of `.zip` :laughing:

#### [Simon Hudon (Apr 12 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953379):
tsk tsk

#### [Simon Hudon (Apr 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953406):
On a slightly related note: any chance that `leanpkg` will get some `flycheck` support in the future?

#### [Sebastian Ullrich (Apr 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953415):
What do you mean by that? The `leanpkg.toml`?

#### [Simon Hudon (Apr 12 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953546):
I mean when you call `leanpkg build`, get the errors that you get in the flycheck error list buffer

#### [Sebastian Ullrich (Apr 12 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953611):
Shouldn't it show the same errors already...? Or do you mean the format...?

#### [Sebastian Ullrich (Apr 12 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953693):
Okay, I'll have to fix OS X (and Windows) support tomorrow. The crazy thing is, the `elan` OS X release builds actually use `.tar.gz`. I took that from a CI template.

#### [Simon Hudon (Apr 12 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953770):
Let me take you through a use case. I'm editting foo.lean which imports foobar.lean, bar.lean, barfoo.lean foo.lean, etc. I upgrade Lean and then mathlib and my project no longer type check so I do `M-x lean-leanpkg-build` to find the first thing that breaks and follow the series of breakages until I fixed everything. I want to fix stuff in the topological order of imports so that I don't have to fix the same file twice.

#### [Simon Hudon (Apr 12 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124953772):
Thanks!

#### [Sebastian Ullrich (Apr 12 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124996475):
I believe I fixed elan, hopefully? 🙂 /cc @**Simon Hudon** @**Kenny Lau**

#### [Kenny Lau (Apr 12 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124996524):
[link to convo](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib.20nightly.20dependence)

#### [Kenny Lau (Apr 12 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124996539):
```
$ curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh
info: downloading installer
sh: line 105: unzip: command not found
chmod: cannot access '/tmp/tmp.DIauNKqwfZ/elan-init.exe': No such file or directory
elan: command failed: chmod u+x /tmp/tmp.DIauNKqwfZ/elan-init.exe

#### [Simon Hudon (Apr 12 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124996610):
It now works! Thanks!

#### [Kenny Lau (Apr 12 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124996618):
i guess i have to turn on the linux subsystem in windows, wait

#### [Simon Hudon (Apr 12 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124996911):
I just tried `install nightly` and got the following:

```
$ elan toolchain install nightly
 51.3 KiB /  51.3 KiB (100 %)  40.5 KiB/s ETA:   0 s                
info: downloading component 'lean'
 16.8 MiB /  16.8 MiB (100 %) 176.8 KiB/s ETA:   0 s                
info: installing component 'lean'

  nightly-x86_64-apple-darwin installed - (error reading lean version)
```

#### [Simon Hudon (Apr 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/124999701):
Lean seems sort of installed but here is what happens when I try to call it:

```
$ lean -v
error: command failed: 'lean'
info: caused by: Permission denied (os error 13)
```

#### [Sebastian Ullrich (Apr 12 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125003682):
@**Simon Hudon** But the initial stable installation worked o.o? What are the permissions on `~/.elan/toolchains/nightly-*/bin/lean`?

#### [Simon Hudon (Apr 12 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125004215):
Actually when installing elan, I also get trouble from `stable`:

```

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
1

info: downloading component 'lean'
 18.1 MiB /  18.1 MiB (100 %) 136.0 KiB/s ETA:   0 s                 
info: installing component 'lean'
info: default toolchain set to 'stable'

  stable installed - (error reading lean version)


Elan is installed now. Great!
```

But I can call Lean: `lean -v`

```
$ lean -v 
Lean (version 3.3.1, commit d36b859c6579, RELEASE)
```

#### [Simon Hudon (Apr 12 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125004376):
To answer your question, here are the permission on `lean`:

```
$ ls -la ~/.elan/toolchains/nightly-*/bin/lean
-rw-r--r--  1 simon  staff  12248272 12 Apr 17:04 /Users/simon/.elan/toolchains/nightly-x86_64-apple-darwin/bin/lean
```

#### [Sebastian Ullrich (Apr 13 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125006764):
@**Simon Hudon** Thanks, this should be fixed in 0.3.2. You can `elan self update` in a few minutes and reinstall the broken toolchains after removing them, or you can just do `chmod u+x ~/.elan/toolchains/*/bin/*` yourself of course.

#### [Simon Hudon (Apr 13 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125006775):
Thanks!

#### [Sebastian Ullrich (Apr 13 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125006927):
@**Kenny Lau** What prompt were you using for that (mingw/cygwin/git bash)? Can't you install unzip there?

#### [Sebastian Ullrich (Apr 13 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125007026):
I'm not sure what the best Windows installation method would be. Perhaps it's just "download the latest Windows release, unpack it and run the exe in a cmd prompt"?

#### [Andrew Ashworth (Apr 13 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125008079):
i think all the options for non-technical users kinda stink on windows, beyond vending a self-extracting zip or exe

#### [Simon Hudon (Apr 13 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125008355):
Which commit does `stable` correspond to?

#### [Kenny Lau (Apr 13 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125014147):
@**Sebastian Ullrich** my antivirus goes into panic mode when i try to elan

#### [Sebastian Ullrich (Apr 13 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125022137):
@**Kenny Lau** Gah. I don't think I can help with that.

#### [Sebastian Ullrich (Apr 13 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125022193):
@**Simon Hudon** The latest release at https://github.com/leanprover/lean/releases. Hopefully it should also be displayed by now?

#### [Sebastian Ullrich (Apr 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125084643):
Huh, turns out elan can actually be installed by [double-clicking it](/user_uploads/3121/aTr--iw7q3zuQPTrImdZX9-x/pasted_image.png) on Windows

#### [Sebastian Ullrich (Apr 14 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125084646):
So I think we're fine :)

#### [Mario Carneiro (Apr 14 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125084833):
How does elan setup differ from previous leanpkg setup layout? I.e. locations of lean and leanpkg and installed repos

#### [Sebastian Ullrich (Apr 14 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125084932):
The package and Lean root layout is the same. The only difference is that the binaries in `~/.elan/bin` are just shims pointing to a spefic Lean root in `~/.elan/toolchains`.

#### [Sebastian Ullrich (Apr 15 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nightly version stapling/near/125107319):
Windows nightlies _finally_ working now https://github.com/leanprover/lean-nightly/releases/tag/nightly-2018-04-14

