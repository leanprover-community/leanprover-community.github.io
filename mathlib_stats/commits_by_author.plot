set terminal png transparent size 640,240
set size 1.0,1.0

set terminal png transparent size 640,480
set output 'commits_by_author.png'
set key left top
set yrange [0:]
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"
set grid y
set ylabel "Commits"
set xtics rotate
set bmargin 6
plot 'commits_by_author.dat' using 1:2 title "Mario Carneiro" w lines, 'commits_by_author.dat' using 1:3 title "Johannes Hölzl" w lines, 'commits_by_author.dat' using 1:4 title "Chris Hughes" w lines, 'commits_by_author.dat' using 1:5 title "Scott Morrison" w lines, 'commits_by_author.dat' using 1:6 title "Simon Hudon" w lines, 'commits_by_author.dat' using 1:7 title "Reid Barton" w lines, 'commits_by_author.dat' using 1:8 title "Rob Lewis" w lines, 'commits_by_author.dat' using 1:9 title "sgouezel" w lines, 'commits_by_author.dat' using 1:10 title "Johan Commelin" w lines, 'commits_by_author.dat' using 1:11 title "Yury G. Kudryashov" w lines, 'commits_by_author.dat' using 1:12 title "Patrick Massot" w lines, 'commits_by_author.dat' using 1:13 title "Floris van Doorn" w lines, 'commits_by_author.dat' using 1:14 title "Kenny Lau" w lines, 'commits_by_author.dat' using 1:15 title "Sean Leather" w lines, 'commits_by_author.dat' using 1:16 title "Kevin Buzzard" w lines, 'commits_by_author.dat' using 1:17 title "Jeremy Avigad" w lines, 'commits_by_author.dat' using 1:18 title "kckennylau" w lines, 'commits_by_author.dat' using 1:19 title "Keeley Hoek" w lines, 'commits_by_author.dat' using 1:20 title "Minchao Wu" w lines, 'commits_by_author.dat' using 1:21 title "Minchao" w lines
