<pre>input:
target (over target will burst)
startingHand (starting point)

output:
probability of burst

if startingHand < target - 4, the delear must keep drawing cards

ex:
target = 21 startingHand = 15
21 - 4 = 17

15 < 17
dealer must draw
if 15 + x >= 17
they can stop (won't burst)

21 - 15 = 6
2 - 6 win
> 6 burst
7 - 10 burst
7, 8, 9, 10
4 / 10 = 0.4

if 1:
1 / 10 = 0.1
15 + 1 = 16
16 < 17
must draw
1 - 5: win
> 5 : burst
6, 7, 8, 9, 10
5 / 10 = 0.5

target = 21, startingHand = 14
21 - 4 = 17
if 1:
startingHand = 15
if 1:
startingHand = 16
0.1 * 0.1 * 0.5
0.1 * 0.4

if 2:
startingHand = 16
1 / 10 = 0.1
0.1 * 0.5

0.3 + 0.05 + 0.04 + 0.005 = 0.395</pre>