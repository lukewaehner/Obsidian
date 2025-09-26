## Why use it?

If you want to work as a software engineer for a large company, these are the things you have to know.

If you missed out on getting a degree in computer science, like I did, this will catch you up and save four years of your life.

When I started this project, I didn't know a stack from a heap, didn't know Big-O anything, or anything about trees, or how to
traverse a graph. If I had to code a sorting algorithm, I can tell ya it would have been terrible.
Every data structure I had ever used was built into the language, and I didn't know how they worked
under the hood at all. I never had to manage memory unless a process I was running would give an "out of
memory" error, and then I'd have to find a workaround. I used a few multidimensional arrays in my life and
thousands of associative arrays, but I never created data structures from scratch.

It's a long plan. It may take you months. If you are familiar with a lot of this already it will take you a lot less time.

**[⬆ back to top](#table-of-contents)**

## How to use it

Everything below is an outline, and you should tackle the items in order from top to bottom.

I'm using GitHub's special markdown flavor, including tasks lists to track progress.
  - [More about GitHub-flavored markdown](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown)

### If you don't want to use git

On this page, click the Code button near the top, then click "Download ZIP". Unzip the file and you can work with the text files.

If you're open in a code editor that understands markdown, you'll see everything formatted nicely.

![How to download the repo as a zip file](https://d3j2pkmjtin6ou.cloudfront.net/how-to-download-as-zip.png)

### If you're comfortable with git

Create a new branch so you can check items like this, just put an x in the brackets: [x]

1. ***Fork the GitHub repo:*** `https://github.com/jwasham/coding-interview-university` by clicking on the Fork button.

    ![Fork the GitHub repo](https://d3j2pkmjtin6ou.cloudfront.net/fork-button.png)

2. Clone to your local repo:

    ```bash
    git clone https://github.com/<YOUR_GITHUB_USERNAME>/coding-interview-university.git
    cd coding-interview-university
    git remote add upstream https://github.com/jwasham/coding-interview-university.git
    git remote set-url --push upstream DISABLE  # so that you don't push your personal progress back to the original repo
    ```

3. Mark all boxes with X after you completed your changes:

    ```bash
    git commit -am "Marked personal progress"
    git pull upstream main  # keep your fork up-to-date with changes from the original repo

    git push # just pushes to your fork
    ```

**[⬆ back to top](#table-of-contents)**

## Don't feel you aren't smart enough

- Successful software engineers are smart, but many have an insecurity that they aren't smart enough.
- The following videos may help you overcome this insecurity:
    - [The myth of the Genius Programmer](https://www.youtube.com/watch?v=0SARbwvhupQ)
    - [It's Dangerous to Go Alone: Battling the Invisible Monsters in Tech](https://www.youtube.com/watch?v=1i8ylq4j_EY)

**[⬆ back to top](#table-of-contents)**

## A Note About Video Resources

Some videos are available only by enrolling in a Coursera or EdX class. These are called MOOCs.
Sometimes the classes are not in session so you have to wait a couple of months, so you have no access.

It would be great to replace the online course resources with free and always-available public sources,
such as YouTube videos (preferably university lectures), so that you people can study these anytime,
not just when a specific online course is in session.

**[⬆ back to top](#table-of-contents)**

## Choose a Programming Language

You'll need to choose a programming language for the coding interviews you do,
but you'll also need to find a language that you can use to study computer science concepts.

Preferably the language would be the same, so that you only need to be proficient in one.

### For this Study Plan

When I did the study plan, I used 2 languages for most of it: C and Python

* C: Very low level. Allows you to deal with pointers and memory allocation/deallocation, so you feel the data structures
    and algorithms in your bones. In higher-level languages like Python or Java, these are hidden from you. In day-to-day work, that's terrific,
    but when you're learning how these low-level data structures are built, it's great to feel close to the metal.
    - C is everywhere. You'll see examples in books, lectures, videos, *everywhere* while you're studying.
    - [The C Programming Language, 2nd Edition](https://www.amazon.com/Programming-Language-Brian-W-Kernighan/dp/0131103628)
        - This is a short book, but it will give you a great handle on the C language and if you practice it a little
            you'll quickly get proficient. Understanding C helps you understand how programs and memory work.
        - You don't need to go super deep in the book (or even finish it). Just get to where you're comfortable reading and writing in C.
* Python: Modern and very expressive, I learned it because it's just super useful and also allows me to write less code in an interview.

This is my preference. You do what you like, of course.

You may not need it, but here are some sites for learning a new language:
- [Exercism](https://exercism.org/tracks)
- [Codewars](http://www.codewars.com)
- [HackerEarth](https://www.hackerearth.com/for-developers/)
- [Scaler Topics (Java, C++)](https://www.scaler.com/topics/)
- [Programiz PRO Community Challenges)](https://programiz.pro/)

### For your Coding Interview

You can use a language you are comfortable in to do the coding part of the interview, but for large companies, these are solid choices:

- C++
- Java
- Python

You could also use these, but read around first. There may be caveats:

- JavaScript
- Ruby

Here is an article I wrote about choosing a language for the interview:
[Pick One Language for the Coding Interview](https://startupnextdoor.com/important-pick-one-language-for-the-coding-interview/).
This is the original article my post was based on: [Choosing a Programming Language for Interviews](https://web.archive.org/web/20210516054124/http://blog.codingforinterviews.com/best-programming-language-jobs/)

You need to be very comfortable in the language and be knowledgeable.

Read more about choices:
- [Choose the Right Language for Your Coding Interview](http://www.byte-by-byte.com/choose-the-right-language-for-your-coding-interview/)

[See language-specific resources here](programming-language-resources.md)

**[⬆ back to top](#table-of-contents)**

## Books for Data Structures and Algorithms

This book will form your foundation for computer science.

Just choose one, in a language that you will be comfortable with. You'll be doing a lot of reading and coding.

### Python

- [Coding Interview Patterns: Nail Your Next Coding Interview](https://geni.us/q7svoz) (**Main Recommendation**)
    - An insider’s perspective on what interviewers are truly looking for and why.
    - 101 real coding interview problems with detailed solutions.
    - Intuitive explanations that guide you through each problem as if you were solving it in a live interview.
    - 1000+ diagrams to illustrate key concepts and patterns.	

### C

- [Algorithms in C, Parts 1-5 (Bundle), 3rd Edition](https://www.amazon.com/Algorithms-Parts-1-5-Bundle-Fundamentals/dp/0201756080)
    - Fundamentals, Data Structures, Sorting, Searching, and Graph Algorithms

### Java

Your choice:

- Goodrich, Tamassia, Goldwasser
    - [Data Structures and Algorithms in Java](https://www.amazon.com/Data-Structures-Algorithms-Michael-Goodrich/dp/1118771338/)
- Sedgewick and Wayne:
    - [Algorithms](https://www.amazon.com/Algorithms-4th-Robert-Sedgewick/dp/032157351X/)
    - Free Coursera course that covers the book (taught by the authors!):
        - [Algorithms I](https://www.coursera.org/learn/algorithms-part1)
        - [Algorithms II](https://www.coursera.org/learn/algorithms-part2)

### C++

Your choice:

- Goodrich, Tamassia, and Mount
    - [Data Structures and Algorithms in C++, 2nd Edition](https://www.amazon.com/Data-Structures-Algorithms-Michael-Goodrich/dp/0470383275)
- Sedgewick and Wayne
    - [Algorithms in C++, Parts 1-4: Fundamentals, Data Structure, Sorting, Searching](https://www.amazon.com/Algorithms-Parts-1-4-Fundamentals-Structure/dp/0201350882/)
    - [Algorithms in C++ Part 5: Graph Algorithms](https://www.amazon.com/Algorithms-Part-Graph-3rd-Pt-5/dp/0201361183/)

**[⬆ back to top](#table-of-contents)**

## Interview Prep Books

Here are some recommended books to supplement your learning.

- [Coding Interview Patterns: Nail Your Next Coding Interview](https://geni.us/q7svoz)

- [Programming Interviews Exposed: Coding Your Way Through the Interview, 4th Edition](https://www.amazon.com/Programming-Interviews-Exposed-Through-Interview/dp/111941847X/)
    - Answers in C++ and Java
    - This is a good warm-up for Cracking the Coding Interview
    - Not too difficult. Most problems may be easier than what you'll see in an interview (from what I've read)

- [Cracking the Coding Interview, 6th Edition](http://www.amazon.com/Cracking-Coding-Interview-6th-Programming/dp/0984782850/)
    - answers in Java

### If you have tons of extra time:

Choose one:

- [Elements of Programming Interviews (C++ version)](https://www.amazon.com/Elements-Programming-Interviews-Insiders-Guide/dp/1479274836)
- [Elements of Programming Interviews in Python](https://www.amazon.com/Elements-Programming-Interviews-Python-Insiders/dp/1537713949/)
- [Elements of Programming Interviews (Java version)](https://www.amazon.com/Elements-Programming-Interviews-Java-Insiders/dp/1517435803/)
        - [Companion Project - Method Stub and Test Cases for Every Problem in the Book](https://github.com/gardncl/elements-of-programming-interviews)

**[⬆ back to top](#table-of-contents)**

## Don't Make My Mistakes

This list grew over many months, and yes, it got out of hand.

Here are some mistakes I made so you'll have a better experience. And you'll save months of time.

### 1. You Won't Remember it All

I watched hours of videos and took copious notes, and months later there was much I didn't remember. I spent 3 days going
through my notes and making flashcards, so I could review. I didn't need all of that knowledge.

Please, read so you won't make my mistakes:

[Retaining Computer Science Knowledge](https://startupnextdoor.com/retaining-computer-science-knowledge/).

### 2. Use Flashcards

To solve the problem, I made a little flashcard site where I could add flashcards of 2 types: general and code.
Each card has a different formatting. I made a mobile-first website, so I could review on my phone or tablet, wherever I am.

Make your own for free:

- [Flashcards site repo](https://github.com/jwasham/computer-science-flash-cards)

**I DON'T RECOMMEND using my flashcards.** There are too many and most of them are trivia that you don't need.

But if you don't want to listen to me, here you go:
- [My flash cards database (1200 cards)](https://github.com/jwasham/computer-science-flash-cards/blob/main/cards-jwasham.db):
- [My flash cards database (extreme - 1800 cards)](https://github.com/jwasham/computer-science-flash-cards/blob/main/cards-jwasham-extreme.db):

Keep in mind I went overboard and have cards covering everything from assembly language and Python trivia to machine learning and statistics.
It's way too much for what's required.

**Note on flashcards:** The first time you recognize you know the answer, don't mark it as known. You have to see the
same card and answer it several times correctly before you really know it. Repetition will put that knowledge deeper in
your brain.

An alternative to using my flashcard site is [Anki](http://ankisrs.net/), which has been recommended to me numerous times.
It uses a repetition system to help you remember. It's user-friendly, available on all platforms, and has a cloud sync system.
It costs $25 on iOS but is free on other platforms.

My flashcard database in Anki format: https://ankiweb.net/shared/info/25173560 (thanks [@xiewenya](https://github.com/xiewenya)).

Some students have mentioned formatting issues with white space that can be fixed by doing the following: open the deck, edit the card, click cards, select the "styling" radio button, and add the member "white-space: pre;" to the card class.

### 3. Do Coding Interview Questions While You're Learning

THIS IS VERY IMPORTANT.

Start doing coding interview questions while you're learning data structures and algorithms.

You need to apply what you're learning to solve problems, or you'll forget. I made this mistake.

Once you've learned a topic, and feel somewhat comfortable with it, for example, **linked lists**:
1. Open one of the [coding interview books](#interview-prep-books) (or coding problem websites, listed below)
2. Do 2 or 3 questions regarding linked lists.
3. Move on to the next learning topic.
4. Later, go back and do another 2 or 3 linked list problems.
5. Do this with each new topic you learn.

**Keep doing problems while you're learning all this stuff, not after.**

You're not being hired for knowledge, but how you apply the knowledge.

There are many resources for this, listed below. Keep going.

### 4. Focus

There are a lot of distractions that can take up valuable time. Focus and concentration are hard. Turn on some music
without lyrics and you'll be able to focus pretty well.

**[⬆ back to top](#table-of-contents)**

## What you won't see covered

These are prevalent technologies but not part of this study plan:

- Javascript
- HTML, CSS, and other front-end technologies
- SQL

**[⬆ back to top](#table-of-contents)**

## The Daily Plan

This course goes over a lot of subjects. Each will probably take you a few days, or maybe even a week or more. It depends on your schedule.

Each day, take the next subject in the list, watch some videos about that subject, and then write an implementation
of that data structure or algorithm in the language you chose for this course.

You can see my code here:
 - [C](https://github.com/jwasham/practice-c)
 - [C++](https://github.com/jwasham/practice-cpp)
 - [Python](https://github.com/jwasham/practice-python)

You don't need to memorize every algorithm. You just need to be able to understand it enough to be able to write your own implementation.

**[⬆ back to top](#table-of-contents)**

## Coding Question Practice

    Why is this here? I'm not ready to interview.

[Then go back and read this.](#3-do-coding-interview-questions-while-youre-learning)

Why you need to practice doing programming problems:
- Problem recognition, and where the right data structures and algorithms fit in
- Gathering requirements for the problem
- Talking your way through the problem like you will in the interview
- Coding on a whiteboard or paper, not a computer
- Coming up with time and space complexity for your solutions (see Big-O below)
- Testing your solutions

There is a great intro for methodical, communicative problem-solving in an interview. You'll get this from the programming
interview books, too, but I found this outstanding:
[Algorithm design canvas](http://www.hiredintech.com/algorithm-design/)

Write code on a whiteboard or paper, not a computer. Test with some sample inputs. Then type it and test it out on a computer.

If you don't have a whiteboard at home, pick up a large drawing pad from an art store. You can sit on the couch and practice.
This is my "sofa whiteboard". I added the pen in the photo just for scale. If you use a pen, you'll wish you could erase.
Gets messy quickly. **I use a pencil and eraser.**

![my sofa whiteboard](https://d3j2pkmjtin6ou.cloudfront.net/art_board_sm_2.jpg)

**Coding question practice is not about memorizing answers to programming problems.**

**[⬆ back to top](#table-of-contents)**

## Coding Problems

Don't forget your key coding interview books [here](#interview-prep-books).

Solving Problems:
- [How to Find a Solution](https://www.topcoder.com/thrive/articles/How%20To%20Find%20a%20Solution)
- [How to Dissect a Topcoder Problem Statement](https://www.topcoder.com/thrive/articles/How%20To%20Dissect%20a%20Topcoder%20Problem%20Statement%20Content)

Coding Interview Question Videos:
- [IDeserve (88 videos)](https://www.youtube.com/playlist?list=PLamzFoFxwoNjPfxzaWqs7cZGsPYy0x_gI)
- [Tushar Roy (5 playlists)](https://www.youtube.com/user/tusharroy2525/playlists?shelf_id=2&view=50&sort=dd)
    - Super for walkthroughs of problem solutions
- [Nick White - LeetCode Solutions (187 Videos)](https://www.youtube.com/playlist?list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-)
    - Good explanations of the solution and the code
    - You can watch several in a short time
- [FisherCoder - LeetCode Solutions](https://youtube.com/FisherCoder)

Challenge/Practice sites:
- [LeetCode](https://leetcode.com/)
    - My favorite coding problem site. It's worth the subscription money for the 1-2 months you'll likely be preparing.
    - See Nick White and FisherCoder Videos above for code walk-throughs.
- [HackerRank](https://www.hackerrank.com/)
- [TopCoder](https://www.topcoder.com/)
- [Codeforces](https://codeforces.com/)
- [Codility](https://codility.com/programmers/)
- [Geeks for Geeks](https://practice.geeksforgeeks.org/explore/?page=1)
- [AlgoExpert](https://www.algoexpert.io/product)
    - Created by Google engineers, this is also an excellent resource to hone your skills.
- [Project Euler](https://projecteuler.net/)
    - very math-focused, and not really suited for coding interviews

**[⬆ back to top](#table-of-contents)**

## Let's Get Started

Alright, enough talk, let's learn!

But don't forget to do coding problems from above while you learn!