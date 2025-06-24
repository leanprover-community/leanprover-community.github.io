# LaTeX examples

This test page collects several examples of LaTeX in Markdown. This is used
for development purposes only.

Compare: <https://math.meta.stackexchange.com/revisions/9386/164>

## Examples from doc-gen issues

From [doc-gen#10](https://github.com/leanprover-community/doc-gen/issues/10), what if I put $f[*a,*b](cd)$ in TeX? $g_{x_0}(y)$ ?

From [doc-gen#62](https://github.com/leanprover-community/doc-gen/issues/62):

- might denote $R[X_i : i \in \sigma]$.
- Example: $x \in \sigma$ and separately `y`
- Example: $x \in \sigma$ and separately `s`
- Example: $x \in \sigma$ and separately `sigm`
- Example: $x \in \sigma$ and separately `simg`
- Example: separately `s` and $x \in \sigma$

Example from [dynamics.circle.rotation_number.translation_number](https://github.com/leanprover-community/mathlib/blob/c35672bbe581370c345d0862c078fbbbe1258fb3/src/dynamics/circle/rotation_number/translation_number.lean#L641):

For any `x : ℝ` the sequence $\frac{f^n(x)-x}{n}$ tends to the translation number of `f`.
In particular, this limit does not depend on `x`.

## [mathlib#3776](https://github.com/leanprover-community/mathlib/pull/3776)

[Before PR](https://github.com/leanprover-community/mathlib/blob/d61bd4ae29222280e1b6dec421c840fb83c30438/src/algebra/classical_lie_algebras.lean#L45) (has a stray `cc`), line spacing too large:

$$
  J = \left[\begin{align}{cc}
              0_l & 1_l\\\\
              1_l & 0_l
            \end{align}\right]
$$

[After PR](https://github.com/leanprover-community/mathlib/blob/0166d0baa856ca4c3d516025105cfe8f912f48dc/src/algebra/classical_lie_algebras.lean#L46), line spacing too large:

$$
  J = \left[\begin{array}{cc}
              0_l & 1_l\\\\
              1_l & 0_l
            \end{array}\right]
$$

Actually fixed:

$$
  J = \left[\begin{array}{cc}
              0_l & 1_l\\
              1_l & 0_l
            \end{array}\right]
$$


## [mathlib#6175](https://github.com/leanprover-community/mathlib/pull/6175)

[Before PR](https://github.com/leanprover-community/mathlib/blob/c70feebd43e143d81a695f7d7e5b21e5892286e8/src/analysis/analytic/basic.lean#L626) (renders correctly):

If a function is analytic in a disk `D(x, R)`, then it is analytic in any disk contained in that
one. Indeed, one can write
$$
f (x + y + z) = \sum_{n} p_n (y + z)^n = \sum_{n, k} \binom{n}{k} p_n y^{n-k} z^k
= \sum_{k} \Bigl(\sum_{n} \binom{n}{k} p_n y^{n-k}\Bigr) z^k.
$$
The corresponding power series has thus a `k`-th coefficient equal to
$\sum_{n} \binom{n}{k} p_n y^{n-k}$. In the general case where `pₙ` is a multilinear map, this has
to be interpreted suitably: instead of having a binomial coefficient, one should sum over all
possible subsets `s` of `fin n` of cardinal `k`, and attribute `z` to the indices in `s` and
`y` to the indices outside of `s`.
In this paragraph, we implement this. The new power series is called `p.change_origin y`. Then, we
check its convergence and the fact that its sum coincides with the original sum. The outcome of this
discussion is that the set of points where a function is analytic is open.


[After PR](https://github.com/leanprover-community/mathlib/blob/676836509e16e6b6d3baf1354594658257f687bd/src/analysis/analytic/basic.lean#L626) (with two backslashes before `sum` as a workaround; should be broken):

If a function is analytic in a disk `D(x, R)`, then it is analytic in any disk contained in that
one. Indeed, one can write
$$
f (x + y + z) = \\sum_{n} p_n (y + z)^n = \\sum_{n, k} \binom{n}{k} p_n y^{n-k} z^k
= \\sum_{k} \Bigl(\\sum_{n} \binom{n}{k} p_n y^{n-k}\Bigr) z^k.
$$
The corresponding power series has thus a `k`-th coefficient equal to
$\\sum_{n} \binom{n}{k} p_n y^{n-k}$. In the general case where `pₙ` is a multilinear map, this has
to be interpreted suitably: instead of having a binomial coefficient, one should sum over all
possible subsets `s` of `fin n` of cardinal `k`, and attribute `z` to the indices in `s` and
`y` to the indices outside of `s`.

## Line spacing tests

(math.stackexchange.com results given above each example)

---

Renders OK ✅:
$\alpha
\alpha$

---

Should not render ❌:
$\alpha

\alpha$

---

Should not render ❌:
$$\alpha

\alpha$$

---

Should not render ❌:
$$

\alpha
\alpha

$$

---

Renders OK ✅:
$$ \alpha\alpha
$$

---

Renders OK ✅:
$$
\alpha\alpha
[hi](345)
b
$$

---

Should not render ❌:
$$ \alpha\alpha [hi](https://github.com) \beta

$$

---

Renders OK ✅:
\begin{align}
\begin{matrix}
a & b & c
\end{matrix}
\end{align}

---

Only the inner matrix environment should render:
\begin{align}

[hi](https://github.com)
\begin{matrix}
a & b & c
\end{matrix}
\end{align}

---

Should not render ❌:
\begin{align}

\begin{matrix}

a & b & c
\end{matrix}
\end{align}

---

Renders OK ✅:

hi there \begin{align} 3 \\ 3 \end{align}

---

Should not render ❌:
\begin{align}
\end{blah}

---

Should not render ❌:
\begin{align}
[link](https://github.com) { {\alpha}
\end{align}

## Nested environments

From <http://web.archive.org/web/20120617014306/http://www.st.fmph.uniba.sk/~kiselak1/pdfka/tex/latexMath_align.pdf>

\begin{align}T(n) & \leq 2(c\lfloor n/2 \rfloor \lg( \lfloor n/2 \rfloor )) + n \\T(n) & \leq 2(cn/2) \lg(n/2) + n \\T(n) & = cn (\lg n - 1) + n \\T(n) & \leq cn \lg n\end{align}

\begin{align}
T(n) & \leq 2(c\lfloor n/2 \rfloor \lg( \lfloor n/2 \rfloor )) + n \\
T(n) & \leq 2(cn/2) \lg(n/2) + n \\
T(n) & = cn (\lg n - 1) + n \\
T(n) & \leq cn \lg n
\end{align}

\begin{gather}
\begin{aligned}T(n) & \leq 2(c\lfloor n/2 \rfloor \lg( \lfloor n/2 \rfloor )) + n \\T(n) & \leq 2(cn/2) \lg(n/2) + n \\T(n) & = cn (\lg n - 1) + n \\T(n) & \leq cn \lg n\end{aligned}\end{gather}

\begin{gather}
\begin{aligned}
T(n) & \leq 2(c\lfloor n/2 \rfloor \lg( \lfloor n/2 \rfloor )) + n \\
T(n) & \leq 2(cn/2) \lg(n/2) + n \\
T(n) & = cn (\lg n - 1) + n \\
T(n) & \leq cn \lg n
\end{aligned}
\end{gather}

\begin{align}\begin{aligned}T(n) & \leq 2(c\lfloor n/2 \rfloor \lg( \lfloor n/2 \rfloor )) + n \\T(n) & \leq 2(cn/2) \lg(n/2) + n \\T(n) & = cn (\lg n - 1) + n \\T(n) & \leq cn \lg n\end{aligned}\end{align}


## MathJax basic tutorial and quick reference

From <https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference>

(Deutsch: [MathJax: LaTeX Basic Tutorial und Referenz](https://www.mathelounge.de/509545/mathjax-latex-basic-tutorial-und-referenz-deutsch))

1. To see how any formula was written in any question or answer, including this one, right-click on the expression it and choose "Show Math As > TeX Commands". (When you do this, the '$' will not display. Make sure you add these. See the next point. There are also [other possibilities](https://math.meta.stackexchange.com/q/659) how to view the code for the formula or the whole post.)

2. **For inline formulas, enclose the formula in `$...$`.  For displayed formulas, use `$$...$$`.**
These render differently. For example,
type
`$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$`
to show $\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$ (which is inline mode) or  type
`$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$`
to show
$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$
(which is display mode).

3. For **Greek letters**, use `\alpha`, `\beta`, …, `\omega`: $\alpha, \beta, … \omega$.  For uppercase, use `\Gamma`, `\Delta`, …, `\Omega`: $\Gamma, \Delta, …, \Omega$. Some Greek letters have variant forms:
`\epsilon \varepsilon` $\epsilon$, $\varepsilon$, `\phi \varphi` $\phi$, $\varphi$, and others.

4. For **superscripts and subscripts**, use `^` and `_`.  For example, `x_i^2`: $x_i^2$, `\log_2 x`: $\log_2 x$.

5. **Groups**. Superscripts, subscripts, and other operations apply only to the next “group”. A “group” is either a single symbol, or any formula surrounded by curly braces `{`…`}`.  If you do `10^10`, you will get a surprise: $10^10$. But `10^{10}` gives what you probably wanted: $10^{10}$. Use curly braces to delimit a formula to which a superscript or subscript applies: `x^5^6` is an error; `{x^y}^z` is ${x^y}^z$, and `x^{y^z}` is $x^{y^z}$. Observe the difference between `x_i^2` $x_i^2$ and `x_{i^2}` $x_{i^2}$.

6. **Parentheses** Ordinary symbols `()[]` make parentheses and brackets $(2+3)[4+4]$. Use `\{` and `\}` for curly braces $\{\}$.

    These do *not* scale with the formula in between, so if you write `(\frac{\sqrt x}{y^3})` the parentheses will be too small: $(\frac{\sqrt x}{y^3})$. Using `\left(`…`\right)` will make the sizes adjust automatically to the formula they enclose: `\left(\frac{\sqrt x}{y^3}\right)` is $\left(\frac{\sqrt x}{y^3}\right)$.

   `\left` and`\right` apply to all the following sorts of parentheses: `(` and `)` $(x)$, `[` and `]` $[x]$, `\{` and `\}` $\{ x \}$, `|` $|x|$, `\vert` $\vert x \vert$, `\Vert` $\Vert x \Vert$, `\langle` and `\rangle` $\langle x \rangle$, `\lceil` and `\rceil` $\lceil x \rceil$, and `\lfloor` and `\rfloor` $\lfloor x \rfloor$. `\middle` can be used to add additional dividers. There are also invisible parentheses, denoted by `.`: `\left.\frac12\right\rbrace` is $\left.\frac12\right\rbrace$.

    If manual size adjustments are required:
`\Biggl(\biggl(\Bigl(\bigl((x)\bigr)\Bigr)\biggr)\Biggr)` gives
$\Biggl(\biggl(\Bigl(\bigl((x)\bigr)\Bigr)\biggr)\Biggr)$.

1. **Sums and integrals** `\sum` and `\int`; the subscript is the lower limit and the superscript is the upper limit, so for example `\sum_1^n` $\sum_1^n$. Don't forget `{`…`}` if the limits are more than a single symbol.  For example, `\sum_{i=0}^\infty i^2` is $\sum_{i=0}^\infty i^2$. Similarly, `\prod` $\prod$, `\int` $\int$, `\bigcup` $\bigcup$, `\bigcap` $\bigcap$, `\iint` $\iint$, `\iiint` $\iiint$, `\idotsint` $\idotsint$.

2. **Fractions** There are [three ways to make these](https://math.meta.stackexchange.com/q/12978/3111). `\frac ab` applies to the next two groups, and produces $\frac ab$; for more complicated numerators and denominators use `{`…`}`: `\frac{a+1}{b+1}` is $\frac{a+1}{b+1}$. If the numerator and denominator are complicated, you may prefer `\over`, which splits up the group that it is in: `{a+1\over b+1}` is ${a+1\over b+1}$.
Using `\cfrac{a}{b}` command is useful for continued fractions $\cfrac{a}{b}$, more details for which [are given in this sub-article](https://math.meta.stackexchange.com/a/5058/3111).

1. **Fonts**

  * Use `\mathbb` or `\Bbb` for "blackboard bold": $\mathbb{CHNQRZ}$.
  * Use `\mathbf` for boldface: $\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$  $\mathbf{abcdefghijklmnopqrstuvwxyz}$.
    * For expression based characters, use `\boldsymbol` instead: $\boldsymbol{\alpha}$
  * Use `\mathit` for italics: $\mathit{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ $\mathit{abcdefghijklmnopqrstuvwxyz}$.
  * Use `\pmb` for boldfaced italics: $\pmb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ $\pmb{abcdefghijklmnopqrstuvwxyz}$.
  * Use `\mathtt` for "typewriter" font: $\mathtt{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ $\mathtt{abcdefghijklmnopqrstuvwxyz}$.
  * Use `\mathrm` for roman font: $\mathrm{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$  $\mathrm{abcdefghijklmnopqrstuvwxyz}$.
  * Use `\mathsf` for sans-serif font: $\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$  $\mathsf{abcdefghijklmnopqrstuvwxyz}$.
  * Use `\mathcal` for "calligraphic" letters: $\mathcal{ ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
  * Use `\mathscr` for script letters: $\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
  * Use `\mathfrak` for "Fraktur" (old German style) letters: $\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ} \mathfrak{abcdefghijklmnopqrstuvwxyz}$.

10. **Radical signs / roots** Use `sqrt`, which adjusts to the size of its argument: `\sqrt{x^3}` $\sqrt{x^3}$; `\sqrt[3]{\frac xy}` $\sqrt[3]{\frac xy}$. For complicated expressions, consider using `{...}^{1/2}` instead.

11. Some **special functions** such as "lim", "sin", "max", "ln", and so on are normally set in roman font instead of italic font. Use `\lim`, `\sin`, etc. to make these: `\sin x` $\sin x$, not `sin x` $sin x$. Use subscripts to attach a notation to `\lim`: `\lim_{x\to 0}` $$\lim_{x\to 0}$$ Nonstandard function names can be set with `\operatorname{foo}(x)` $\operatorname{foo}(x)$.

12. There are a very large number of **special symbols and notations**, too many to list here; see [this shorter listing](http://pic.plover.com/MISC/symbols.pdf), or [this exhaustive listing](https://www.ctan.org/tex-archive/info/symbols/comprehensive/symbols-a4.pdf). Some of the most common include:
  * `\lt \gt \le \leq \leqq \leqslant \ge \geq \geqq \geqslant \neq` $\lt$, $\gt$, $\le$, $\leq$, $\leqq$, $\leqslant$, $\ge$, $\geq$, $\geqq$, $\geqslant$, $\neq$.  You can use `\not` to put a slash through almost anything: `\not\lt` $\not\lt$ but it often looks bad.
  * `\times \div \pm \mp` $\times$, $\div$, $\pm$, $\mp$. `\cdot` is a centered dot: $x\cdot y$
  * `\cup \cap \setminus \subset \subseteq \subsetneq \supset \in \notin \emptyset \varnothing` $\cup$, $\cap$, $\setminus$, $\subset$, $\subseteq$, $\subsetneq$, $\supset$, $\in$, $\notin$, $\emptyset$, $\varnothing$
  * `{n+1 \choose 2k}` or `\binom{n+1}{2k}` ${n+1 \choose 2k}$
  * `\to \rightarrow \leftarrow \Rightarrow \Leftarrow \mapsto` $\to$, $\rightarrow$, $\leftarrow$, $\Rightarrow$, $\Leftarrow$, $\mapsto$
  * `\land \lor \lnot \forall \exists \top \bot \vdash \vDash` $\land$, $\lor$, $\lnot$, $\forall$, $\exists$, $\top$, $\bot$, $\vdash$, $\vDash$
  * `\star \ast \oplus \circ \bullet` $\star$, $\ast$, $\oplus$, $\circ$, $\bullet$
  * `\approx \sim \simeq \cong \equiv \prec \lhd \therefore` $\approx$, $\sim $, $\simeq$, $\cong$, $\equiv$, $\prec$, $\lhd$, $\therefore$
  * `\infty \aleph_0` $\infty\, \aleph_0$ `\nabla \partial` $\nabla$, $\partial$ `\Im \Re` $\Im$, $\Re$
  * For modular equivalence, use `\pmod` like this: `a\equiv b\pmod n` $a\equiv b\pmod n$.
  * For the binary mod operator, use `\bmod` like this: `a\bmod 17` $a\bmod 17$.
  * Avoid using `\mod`, as it produces extra space: compare the above with `a\mod 17` $a\mod 17$.
  * `\ldots` is the dots in $a_1, a_2, \ldots ,a_n$ `\cdots` is the dots in  $a_1+a_2+\cdots+a_n$
  * Script lowercase l is `\ell` $\ell$.

  [Detexify](http://detexify.kirelabs.org/classify.html) lets you draw a symbol on a web page and then lists the $\TeX$ symbols that seem to resemble it.  These are not guaranteed to work in MathJax but are a good place to start.  To check that a command is supported, note that MathJax.org maintains a [list of currently supported $\LaTeX$ commands](http://docs.mathjax.org/en/latest/tex.html#supported-latex-commands), and one can also check Dr. Carol JVF Burns's page of [$\TeX$ Commands Available in MathJax](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm).

13. **Spaces** MathJax usually decides for itself how to space formulas, using a complex set of rules. Putting extra literal spaces into formulas will not change the amount of space MathJax puts in: `a␣b` and `a␣␣␣␣b` are both $a    b$. To add more space, use `\,` for a thin space $a\,b$; `\;` for a wider space $a\;b$.  `\quad` and `\qquad` are large spaces: $a\quad b$, $a\qquad b$.

  To set plain text, use `\text{…}`: $\{x\in s\mid x\text{ is extra large}\}$. You can nest `$…$` inside of `\text{…}`, for example to access spaces.

14. **Accents and diacritical marks** Use `\hat` for a single symbol $\hat x$, `\widehat` for a larger formula $\widehat{xy}$. If you make it too wide, it will look silly. Similarly, there are `\bar` $\bar x$ and `\overline` $\overline{xyz}$, and `\vec` $\vec x$ and `\overrightarrow` $\overrightarrow{xy}$ and `\overleftrightarrow` $\overleftrightarrow{xy}$. For dots, as in $\frac d{dx}x\dot x =  \dot x^2 +  x\ddot x$,  use `\dot` and `\ddot`.

15. Special characters used for MathJax interpreting can be escaped using the `\` character: `\$` $\$$, `\{` $\{$, `\_` $\_$, etc. If you want `\` itself, you should use `\backslash` (symbol) or `\setminus` ([binary operation](https://tex.stackexchange.com/a/511332)) for $\backslash$, because `\\` is for a new line.

(Tutorial ends here.)

-------------

It is important that this note be reasonably short and not suffer from too much bloat. To include more topics, please create short addenda and post them as answers instead of inserting them into this post.

Contents
---
Alphabetical list of links to To MathJax Topics, by title:

 - [Absolute values and norms](https://math.meta.stackexchange.com/a/15078/161490) • [Additional symbolic decorations](https://math.meta.stackexchange.com/a/13081/161490) • [Aligning Equations][3]
 - [Alternative Ways of Writing in LaTeX](https://math.meta.stackexchange.com/a/27910/161490) • [Annotations of reasoning](https://math.meta.stackexchange.com/a/21258/161490) • [Arbitrary operators](https://math.meta.stackexchange.com/a/15077/161490)
 - [Arrays](https://math.meta.stackexchange.com/a/5044/161490) • [Big braces](https://math.meta.stackexchange.com/a/11423/161490) • [Colors](https://math.meta.stackexchange.com/a/10116/161490)
 - [Commutative diagrams](https://math.meta.stackexchange.com/a/16888/161490) • [Continued fractions](https://math.meta.stackexchange.com/a/5058/161490) • [Crossing things out](https://math.meta.stackexchange.com/a/13183/161490)
 - [Definitions by cases (piecewise functions)](https://math.meta.stackexchange.com/a/5025/161490) • [Degree symbol](https://math.meta.stackexchange.com/a/19678/161490) • [Display style](https://math.meta.stackexchange.com/a/25054/161490)
 - [Equation numbering](https://math.meta.stackexchange.com/a/27793/161490) • [Fussy spacing issues](https://math.meta.stackexchange.com/a/5057/161490) • [Highlighting expressions](https://math.meta.stackexchange.com/a/22395/161490)
 - [Left and right arrows](https://math.meta.stackexchange.com/a/13310/161490) • [Limits](https://math.meta.stackexchange.com/a/12850/161490) • [Linear programming](https://math.meta.stackexchange.com/a/27756/161490)
 - [Long division](https://math.meta.stackexchange.com/a/21096/161490) • [Math Programming][2] • [Matrices][1]
 - [Markov Chains](https://math.meta.stackexchange.com/a/31141/161490) • [Mixing code and MathJax formatting on lines](https://math.meta.stackexchange.com/a/25251/161490) • [The \newcommand function](https://math.meta.stackexchange.com/a/11638/161490)
 - [Numbering Equations][4] • [Overlaying Symbols](https://math.meta.stackexchange.com/a/32210/736802) • [Packs of cards](https://math.meta.stackexchange.com/a/22516/161490)
 - [Symbols](https://math.meta.stackexchange.com/a/11284/161490)
• [System of equations](https://math.meta.stackexchange.com/a/6267/161490) • [Tables](https://math.meta.stackexchange.com/a/29979/161490)
 - [Tags and references](https://math.meta.stackexchange.com/a/11491/161490) • [Tensor indices](https://math.meta.stackexchange.com/a/30661/161490) • [Units](https://math.meta.stackexchange.com/a/27212/161490)
 - [Vertical spacing](https://math.meta.stackexchange.com/a/25048/161490)

  [1]: https://math.meta.stackexchange.com/a/5023/676335
  [2]: https://math.meta.stackexchange.com/a/27756/676335
  [3]: https://math.meta.stackexchange.com/a/5024/676335
  [4]: https://math.meta.stackexchange.com/a/11491/676335
  [5]: https://math.meta.stackexchange.com/a/29979/676335

## Aligned equations

<https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference/5024#5024>

Often people want a series of equations where the equals signs are aligned.  To get this, use `\begin{align}…\end{align}`.  Each line should end with `\\`, and should contain an ampersand at the point to align at, typically immediately before the equals sign.

For example,

\begin{align}
\sqrt{37} & = \sqrt{\frac{73^2-1}{12^2}} \\
 & = \sqrt{\frac{73^2}{12^2}\cdot\frac{73^2-1}{73^2}} \\
 & = \sqrt{\frac{73^2}{12^2}}\sqrt{\frac{73^2-1}{73^2}} \\
 & = \frac{73}{12}\sqrt{1 - \frac{1}{73^2}} \\
 & \approx \frac{73}{12}\left(1 - \frac{1}{2\cdot73^2}\right)
\end{align}

is produced by


    \begin{align}
\sqrt{37} & = \sqrt{\frac{73^2-1}{12^2}} \\
 & = \sqrt{\frac{73^2}{12^2}\cdot\frac{73^2-1}{73^2}} \\
 & = \sqrt{\frac{73^2}{12^2}}\sqrt{\frac{73^2-1}{73^2}} \\
 & = \frac{73}{12}\sqrt{1 - \frac{1}{73^2}} \\
 & \approx \frac{73}{12}\left(1 - \frac{1}{2\cdot73^2}\right)
\end{align}

The usual `$$` marks that delimit the display may be omitted here.


## Definitions by cases (piecewise functions)

<https://math.meta.stackexchange.com/a/5025>

Use `\begin{cases}…\end{cases}`.  End each case with a `\\`, and use `&` before parts that should be aligned.

For example, you get this:

$$f(n) =
\begin{cases}
n/2,  & \text{if $n$ is even} \\
3n+1, & \text{if $n$ is odd}
\end{cases}$$

by writing this:

      f(n) =
    \begin{cases}
n/2,  & \text{if $n$ is even} \\
3n+1, & \text{if $n$ is odd}
\end{cases}

The brace can be moved to the right:
$$
\left.
\begin{array}{l}
\text{if $n$ is even:}&n/2\\
\text{if $n$ is odd:}&3n+1
\end{array}
\right\}
=f(n)
$$
by writing this:

    \left.
    \begin{array}{l}
\text{if $n$ is even:}&n/2\\
\text{if $n$ is odd:}&3n+1
\end{array}
    \right\}
    =f(n)

To get a larger vertical space between cases we can use `\\[2ex]` instead of `\\`. For example, you get this:

$$f(n) =
\begin{cases}
\frac{n}{2},  & \text{if $n$ is even} \\[2ex]
3n+1, & \text{if $n$ is odd}
\end{cases}$$

by writing this:

    f(n) =
    \begin{cases}
\frac{n}{2},  & \text{if $n$ is even} \\[2ex]
3n+1, & \text{if $n$ is odd}
\end{cases}

(An ‘ex’ is a length equal to the height of the letter `x`; `2ex` here means the space should be two exes high.)

## Matrices

<https://math.meta.stackexchange.com/a/5023/>

1. Use `$$\begin{matrix}…\end{matrix}$$`  In between the `\begin` and `\end`, put the matrix elements. End each matrix row with `\\`, and separate matrix elements with `&`.  For example,

        $$
        \begin{matrix}
        1 & x & x^2 \\
        1 & y & y^2 \\
        1 & z & z^2 \\
        \end{matrix}
$$

    produces:

$$
        \begin{matrix}
        1 & x & x^2 \\
        1 & y & y^2 \\
        1 & z & z^2 \\
        \end{matrix}
$$

  MathJax will adjust the sizes of the rows and columns so that everything fits.

2. To add brackets, either use `\left…\right` as in section 6 of the tutorial, or replace `matrix` with `pmatrix` $\begin{pmatrix}1&2\\3&4\\ \end{pmatrix}$, `bmatrix` $\begin{bmatrix}1&2\\3&4\\ \end{bmatrix}$, `Bmatrix` $\begin{Bmatrix}1&2\\3&4\\ \end{Bmatrix}$, `vmatrix` $\begin{vmatrix}1&2\\3&4\\ \end{vmatrix}$, `Vmatrix` $\begin{Vmatrix}1&2\\3&4\\ \end{Vmatrix}$.

3. Use `\cdots` $\cdots$ `\ddots` $\ddots$ `vdots` $\vdots$ when you want to omit some of the entries:

     $$\begin{pmatrix}
     1 & a_1 & a_1^2 & \cdots & a_1^n \\
     1 & a_2 & a_2^2 & \cdots & a_2^n \\
     \vdots  & \vdots& \vdots & \ddots & \vdots \\
     1 & a_m & a_m^2 & \cdots & a_m^n
     \end{pmatrix}$$


4. For horizontally "augmented" matrices, put parentheses or brackets around a suitably-formatted table; see [arrays](http://meta.math.stackexchange.com/a/5044/) below for details.  Here is an example:

  $$ \left[\begin{array}{cc|c}
  1&2&3\\
  4&5&6
  \end{array}\right] $$

  is produced by:

        $$ \left[
    \begin{array}{cc|c}
      1&2&3\\
      4&5&6
    \end{array}
\right] $$

  The `cc|c` is the crucial part here; it says that there are three centered columns with a vertical bar between the second and third.

5. For vertically "augmented" matrices, use `\hline`. For example

$$
\begin{pmatrix}
a & b \\
c & d\\
\hline
1 & 0\\
0 & 1
\end{pmatrix}
$$
is produced by

    $$
      \begin{pmatrix}
        a & b\\
        c & d\\
      \hline
        1 & 0\\
        0 & 1
      \end{pmatrix}
    $$


6. For small inline matrices use `\bigl(\begin{smallmatrix} ... \end{smallmatrix}\bigr)`, e.g.  $\bigl( \begin{smallmatrix} a & b \\ c & d \end{smallmatrix} \bigr)$ is produced by:

         $\bigl( \begin{smallmatrix} a & b \\ c & d \end{smallmatrix} \bigr)$

## From `tactic_writing.md`

* `return`: produce a value in the monad (type: `A → m A`)
* `ma >>= f`: get the value of type `A` from `ma : m A` and pass it to `f : A → m B`. Alternate
  syntax: `do a ← ma, f a`
* `f <$> ma`: apply the function `f : A → B` to the value in `ma : m A` to get a `m B`. Same as
  `do a ← ma, return (f a)`
* `ma >> mb`: same as `do a ← ma, mb`; here the return value of `ma` is ignored and then `mb` is
  called. Alternate syntax: `do ma, mb`
* `mf <*> ma`: same as `do f ← mf, f <$> ma`, or `do f ← mf, a ← ma, return (f a)`
* `ma <* mb`: same as `do a ← ma, mb, return a`
* `ma *> mb`: same as `do ma, mb`, or `ma >> mb`. Why two notations for the same thing? Historical
  reasons.
* `pure`: same as `return`. Again, historical reasons.
* `failure`: failed value (specific monads usually have a more useful form of this, like `fail` and
  `failed` for tactics).
* `ma <|> ma'` recover from failure: runs `ma` and if it fails then runs `ma'`.
* `a $> mb`: same as `do mb, return a`
* `ma <$ b`: same as `do ma, return b`
