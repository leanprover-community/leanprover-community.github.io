# Meet the community

The Lean community is rather diverse. We have users coming from computer
science as well as mathematics, and even a couple of people with a
physics background.
Most users are either students or work in academia, but there also some
data scientists and software engineers working in industry.

## The blog

You can get news from the community on our [blog](/blog/).

## The Lean Zulip chat

The main gathering point of our community is a
[Zulip chat instance](https://leanprover.zulipchat.com).
You can browse public discussions on the most popular "streams" without registering.
There is also a web-indexed [archive](https://leanprover-community.github.io/archive/),
with a less convenient interface.

We welcome you to register for the Zulip chat,
which will let you participate in the discussions.
Registering with your real name is preferred, but not required.
Starting by briefly introducing youself in the
[*new members* stream](https://leanprover.zulipchat.com/#narrow/stream/113489-new-members)
is also appreciated.

Questions from users at all levels of expertise are welcomed.
Asking your first questions in the new members stream will ensure the answers
won't asssume you know much about Lean. But you are welcome to use more specialized streams.
Please start new discussion topics rather than using unrelated existing topics.
If you need coding help, you may be asked to provide a "minimal working example"
([MWE](mwe.html)).
Also beware of [XY problems](https://mywiki.wooledge.org/XyProblem): try to give enough context.

To post a snippet of code inline, enclose it in single backticks: `` `my code here` ``.
If your code contains backticks itself, enclose it in more backticks than it contains:
``` `` my`code`contains`backticks `` ```.

Longer snippets should be enclosed between two lines containing three back-quotes, as in:
````md
```
def my_nat : n := 5
#check my_nat
```
````

You can use LaTeX using `$$` to enclose inline LaTeX and
````md
```math
my LaTeX code here
```
````

for displayed math.

## GitHub

The next gathering point after Zulip is GitHub, which hosts all the
[community repositories](https://github.com/leanprover-community).
In particular, the
[mathlib pull requests](https://github.com/leanprover-community/mathlib/pulls)
page is the right place to see our ongoing efforts.

If you want to participate in our projects then you can read our
[contributing guide](contribute/index.html).

## Community guidelines

We are devoted to developing an open and accepting community
that welcomes participation from everyone.
Behavior that is offensive, discriminatory, or aggressive
will not be tolerated in any form.
We adopt the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).
These guidelines apply to the
[Lean Zulip chat](https://leanprover.zulipchat.com/) 
and the [leanprover-community GitHub organization](https://github.com/leanprover-community/).

The [maintainer team](#maintainers) enforces this code of conduct.
Jeremy Avigad, Anne Baanen, and Simon Hudon serve as first points of contact
for reporting any concerns.
We also provide an [anonymous form](https://docs.google.com/forms/d/e/1FAIpQLSdEjlFqJQV65F-yzRHl-lyWAt7TSUW1axPiQK3RyV67iu1h6Q/viewform)
to report incidents that violate the community guidelines.

We encourage a policy of de-escalation in the presence of unwelcome behavior.
If you perceive someone acting in a way that violates our code of conduct,
please do not respond in the same way; instead, take action to correct the behavior,
such as reporting it to the moderators.

## Maintainers

Mathlib maintainers are community members who are actively
developing mathlib and reviewing pull requests.
Their number grows naturally when new users become
frequent contributors.

Maintainers have permission to merge pull requests to mathlib
and access to GitHub administration settings.
Otherwise they are community members like everyone else.
Community decisions are discussed and made in public channels.
In particular, everyone is encouraged to review pull requests
and to contribute to the [supporting tools](http://github.com/leanprover-community/)
for Lean and mathlib.

If you are interested in eventually joining the maintainer team,
we encourage you to participate as much as possible in the review process.
Please contact the current maintainers when you feel prepared.
