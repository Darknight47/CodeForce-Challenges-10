"""

------------------- Link for the challenge: https://codeforces.com/problemset/problem/835/A -------------------------------

Two boys decided to compete in text typing on the site "Key races". During the competition, they have to type a text consisting of s characters. 
The first participant types one character in v1 milliseconds and has ping t1 milliseconds. The second participant types one character in v2 milliseconds and has ping t2 milliseconds.

If connection ping (delay) is t milliseconds, the competition passes for a participant as follows:

Exactly after t milliseconds after the start of the competition the participant receives the text to be entered.
Right after that he starts to type it.
Exactly t milliseconds after he ends typing all the text, the site receives information about it.
The winner is the participant whose information on the success comes earlier. If the information comes from both participants at the same time, it is considered that there is a draw.

Given the length of the text and the information about participants, determine the result of the game.

Input
The first line contains five integers s, v1, v2, t1, t2 (1 ≤ s, v1, v2, t1, t2 ≤ 1000) — the number of characters in the text, 
the time of typing one character for the first participant, the time of typing one character for the the second participant, 
the ping of the first participant and the ping of the second participant.

Output
If the first participant wins, print "First". If the second participant wins, print "Second". In case of a draw print "Friendship".

Input:
5 1 2 1 2

Output:
First
"""

chars, v1, v2, t1, t2 = map(int, input().split())
first = (chars * v1) + (2 * t1)
second = (chars * v2) + (2 * t2)
if(first < second):
    print("First")
elif(second < first):
    print("Second")
else:
    print("Friendship")