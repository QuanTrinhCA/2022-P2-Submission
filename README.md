# [Problem B: Morse Numbers](https://nbhspc22.kattis.com/contests/nbhspc22/problems/nbhspc22.morsenumbers)

Morse code was used in the 1800s to send telegraph messages. While Morse code can be used to send messages with both letters and digits, we will focus on sending messages that are numbers (sequences of digits, with spaces between numbers).

Each decimal digit in Morse code is encoded into a sequence of dits and dashes. Each dit is a sound that takes 1 unit of time to send, and each dash is a sound that takes 3 units. Between consecutive symbols (dits or dashes) from the same digit, there is 1 unit of silence. Also, there is a silence lasting 3 units between two digits in the same number. The space between two numbers is represented by 7 units of silence.

Given a message that is a sequence of numbers, your job is to determine the total number of time units to transmit that message.

The Morse code for digits is as follows:

<img width="217" alt="image" src="https://github.com/QuanTrinhCA/2022-P2-Submission/assets/44539970/089d7e3c-c420-43d5-8fad-c12e8603c459">

## Input
The input is two lines. The first has a single positive integer, N, between 1 and 20, inclusive. It represents the number of integers making up the message. The second line holds the message. It consists of N integers between 0 and 999999999, inclusive. A single space separates each integer in the message. There is only one integer (zero) that starts with a leading 0.

## Output
The output is a positive number, representing the number of time units to transmit the message.

## Sample Input 1
```
1
5
```

## Sample Output 1
```
9
```

## Sample Input 2
```
3
2022 4 28
```

## Sample Output 2
```
131
```
