---
hide:
  - toc
  - navigation
---

<!-- <!DOCTYPE html> -->
<!-- <html lang="en"> -->
<!-- <head> -->
<!--     <meta charset="UTF-8"> -->
<!--     <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
<!--     <title>Staff</title> -->
<!-- 将样式提取到外部文件 --> 
<!--     <link rel="stylesheet" href="stylesheets/home.css"> -->
<!-- </head> -->
<!-- <body> -->
<!--     <div class="frosted-glass"> -->
<!--         <div>XJTU COMP402127</div> -->
<!--         <div>SPRING 2025</div> -->
<!--         <div>Introduction to Computer Systems</div> -->
<!--     </div> -->
<!--     <script> -->
<!--         // 动态设置背景图片，避免阻塞初始渲染 -->
<!--         document.addEventListener("DOMContentLoaded", () => { -->
<!--             document.body.style.backgroundImage = "url('./assets/background.png')"; -->
<!--         }); -->
<!--     </script> -->
<!-- </body> -->
<!-- </html> -->

# Introduction to Computer Systems (ICS)

Welcome to the XJTU-ICS course!
This course offers a programmer’s perspective on how computer systems execute programs
store data, and communicate with each other.

A key focus of the course is on **developing your system programming skills**.
To achieve this, the course includes 6 hands-on lab assignments,
which will help you strengthen your understanding of how systems operate at the code level.
These lab assignments make up approximately 50% of your final grade,
emphasizing the importance of practical programming in mastering the concepts covered in the course.

Enjoy!

**Prerequisites**: C Programming

**Textbook**: Randal E. Bryant and David R. O'Hallaron, [Computer Systems: A Programmer's Perspective](https://csapp.cs.cmu.edu/), Third Edition, Pearson, 2016

## Announcements
<!-- !!! info "Announcements for Week 15 :loudspeaker:" -->
<!---->
<!--     Please note the deadline and release date of labs: -->
<!--      -->
<!--     - Malloclab is due next Sunday (2025-06-03 23:59). Don't forget to submit. :warning: -->
<!--      -->
<!--     **DON'T CHEAT**. Big Brother is watching you! -->
<!--      -->
<!--     ~ XJTU-ICS Course Staff -->
<!---->

!!! info "Announcements for Week 6 :loudspeaker:"

    Enjoy [AttackLab](labs/lab3.md)! :smile:
    
    **DON'T CHEAT**. Big Brother is watching you!
    
    ~ XJTU-ICS Course Staff


<!-- !!! info "Announcements for Week 5 :loudspeaker:" -->
<!---->
<!--     Please note the deadline and release date of labs: -->
<!---->
<!--     - BombLab is due this Sunday (2026-04-05 23:59). Don't forget to submit. :warning: -->
<!---->
<!--     - AttackLab is released this Thursday (2026-04-02). Enjoy! :smile: -->
<!---->
<!--     **DON'T CHEAT**. Big Brother is watching you! -->
<!---->
<!--     ~ XJTU-ICS Course Staff -->

<!-- !!! info "Announcements for Week 4 :loudspeaker:" -->
<!---->
<!--     The deadline of [BombLab](labs/lab2.md) is extended to 2026-04-05. Enjoy! :smile: -->
<!---->
<!--     **DON'T CHEAT**. Big Brother is watching you! -->
<!---->
<!--     ~ XJTU-ICS Course Staff -->

<!-- !!! info "Announcements for Week 3 :loudspeaker:" -->
<!---->
<!--     Enjoy [BombLab](labs/lab2.md)! :smile: -->
<!---->
<!--     **DON'T CHEAT**. Big Brother is watching you! -->
<!---->
<!--     ~ XJTU-ICS Course Staff -->

<!-- !!! info "Announcements for Week 2 :loudspeaker:" -->
<!---->
<!--     Please note the deadline of datalab: -->
<!---->
<!--     - [DataLab](labs/lab1.md) is due this Sunday (2025-03-15 23:59). Don't forget to submit. :warning: -->
<!--     - [BombLab](labs/lab2.md) will be released this Thursday (2025-03-12). Enjoy! :smile: -->
<!---->
<!--     **DON'T CHEAT**. Big Brother is watching you! -->
<!---->
<!--     ~ XJTU-ICS Course Staff -->

<!-- !!! info "Announcements for Week 1 :loudspeaker:" -->
<!---->
<!--     Please note the release date of labs: -->
<!---->
<!--     - [Lab 0](labs/lab0.md) has been released. This lab is a prerequisite for all other labs. Please finish it in time! -->
<!--     - DataLab will be released this Thursday (2026-03-05). Enjoy! :smile: -->
<!---->
<!--     **DON'T CHEAT**. Big Brother is watching you! -->
<!---->
<!--     ~ XJTU-ICS Course Staff -->


## Getting Help

- [Piazza](https://piazza.com/stu.xjtu.edu.cn/spring2026/xjtuics)
- QQ group: 1076865018
- Office Hours
    - Danfeng Shan: 16:00-18:00, Every Thursday
    - Hao Li: TBD
    - TAs:

{{read_office_hour_csv("docs/static/data/office_hour.csv")}}

## Schedule

{{read_schedule_csv("docs/static/data/events.csv")}}
<!-- |  Week |     Date    | Lecture | Instructors | Reading | Labs |
| :---: | :---------: | :-----: | :---------: | :-----: | :--: |
|   1   | 2025-02-18  | Overview ( [:material-presentation-play: Slides](assets/slides/01-overview-class-rules.pdf){.md-button} ) | Hao Li && Danfeng Shan  |   1     |             |
|   1   | 2025-02-20  | Representing and Manipulating Information | Danfeng Shan | 2.1-2.3 | datalab out |
|   2   | 2025-02-25  | Machine-Level Representation of Programs: Basics | Danfeng Shan | 3.1-3.5 | |
|   2   | 2025-02-27  | Machine-Level Representation of Programs: Control | Danfeng Shan | 3.6 | |
|   3   | 2025-03-04  | Machine-Level Representation of Programs: Procedures | Danfeng Shan | 3.7 | |
|   3   | 2025-03-06  | Machine-Level Representation of Programs: Procedures | Danfeng Shan | 3.7 | datalab due, bomblab out |
|   4   | 2025-03-11  | Machine-Level Representation of Programs: Data | Danfeng Shan | 3.8-3.9 | |
|   4   | 2025-03-13  | Machine-Level Representation of Programs: Advanced |  Danfeng Shan | 3.10 | |
|   5   | 2025-03-18  | Machine-Level Representation of Programs: Advanced | Danfeng Shan | 3.10 | bomblab due, attacklab out |
|   5   | 2025-03-20  | The Memory Hierarchy                      |       Danfeng Shan      | 6.1-6.3 | |
|   6   | 2025-03-25  | Cache Memories                            |       Danfeng Shan       | 6.4-6.7 | |
|   6   | 2025-03-27  | Cache Memories                            |       Danfeng Shan       | 6.4-6.7 | attacklab due, cachelab out |
|   7   | 2025-04-01  | Code Optimization |  Hao Li | 5.1-5.6 | |
|   7   | 2025-04-03  | Code Optimization |  Hao Li | 5.7-5.11 | |
|   8   | 2025-04-08  | TBA |  Hao Li | | |
|   8   | 2025-04-10  | TBA |  Hao Li | | cachelab due |
|   9   | 2025-04-15  | TBA |  Hao Li | | |
|   9   | 2025-04-17  | TBA |  Hao Li | | |
|   10  | 2025-04-22  | TBA |  Hao Li | | |
|   10  | 2025-04-24  | TBA |  Hao Li | | |
|   11  | 2025-04-29  | TBA |  Hao Li | | |
|   11  | 2025-05-01  | No Lecture (Labour Day) |   | | |
|   12  | 2025-05-06  | TBA |  Hao Li | | |
|   12  | 2025-05-08  | TBA |  Hao Li | | |
|   13  | 2025-05-13  | TBA |  Hao Li | | |
|   13  | 2025-05-15  | TBA |  Hao Li | | |
|   14  | 2025-05-20  | TBA |  Hao Li | | |
|   14  | 2025-05-22  | TBA |  Hao Li | | |
|   15  | 2025-05-27  | Processor Architecture |  Danfeng Shan | 4.1-4.3 | |
|   15  | 2025-05-29  | Processor Architecture |  Danfeng Shan | 4.4-4.6 | |
|   16  | 2025-06-03  | Exam Review |  Danfeng Shan | | |
|   16  | 2025-06-05  | Exam Review |  Danfeng Shan | | | -->
