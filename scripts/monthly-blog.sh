#!/bin/bash

usage () {
echo "Usage: monthly-blog.sh YYYY M path/to/mathlib"
echo ""
echo "Where YYYY is a 4-digit year, and M is the number of the month."
echo "Example: monthly-blog.sh 2021 8 ~/mathlib"
echo "It is important that M is a natural number between 1 and 12."
echo "Do not write 08 to denote August. Write 8 instead."
echo ""
echo "Important: make sure that the mathlib clone is clean,"
echo "and points to an up-to-date copy of master."
}

year=$1
month=$2
mathlib=$3

# 1-indexed arrays
monthnames_uc=("NaM" "Jan" "Feb" "Mar" "Apr" "May" "Jun" "Jul" "Aug" "Sep" "Oct" "Nov" "Dec")
monthnames_lc=("NaM" "jan" "feb" "mar" "apr" "may" "jun" "jul" "aug" "sep" "oct" "nov" "dec")

echo "---"
echo "author: 'Mathlib community'"
echo "category: 'month-in-mathlib'"
echo "date: $(date --rfc-3339=sec)"
echo "description: ''"
echo "has_math: true"
echo "link: ''"
echo "slug: month-in-mathlib-${monthnames_lc[$month]}-$year"
echo "tags: ''"
echo "title: This month in mathlib (${monthnames_uc[$month]} $year)"
echo "type: text"
echo "---"

echo ""

pushd $mathlib > /dev/null

git log --pretty=oneline --abbrev-commit --since="1 ${monthnames_uc[$month]} $year" | tac |
sed 's|\([^ ]*\) \(.*\) (#\([0-9]*\))|* [PR #\3](https://github.com/leanprover-community/mathlib/pull/\3) :: \2|'

popd > /dev/null

