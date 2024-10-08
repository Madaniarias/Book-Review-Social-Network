![Fotor_AI](https://user-images.githubusercontent.com/111761417/232278862-5e8ad3b2-8f65-4f0c-889e-673146aeb508.png)
<sub>Generated by Fotor with the promp "Books allow us to explore far and beyond"

# UNIT 4: A BOOK REVIEW SOCIAL NETWORK FOR HIGH SCHOOL ENGLISH CLASSES.

**Table of Contents**
1. [Criteria A: Planning](#criteria-a-planning)
   * [Problem definition](#problem-definition)
   * [Rationale for Proposed Solution](#rationale-for-proposed-solution)
   * [Design statement](#design-statement)
   * [Success Criteria](#success-criteria)
2. [Criteria B: Design](#criteria-b-design)
    * [Record of Tasks](#record-of-tasks)
    * [System diagram](#system-diagram)
    * [Wireframe](#wireframe)
    * [Flow Diagrams](#flow-diagrams)
    * [ER Diagrams](#er-diagrams)
    * [UML Diagrams](#uml-diagrams)
    * [Test Plan](#test-plan)
3. [Criteria C: Development](#criteria-c-development)
   * [Existing Tools](#existing-tools)
   * [Techniques Applied](#techniques-applied)
   * [Computational Thinking](#computational-thinking)
4. [Criteria D: Functionality](#criteria-d-functionality)
   * [Sources](#sources)
   * [Appendix](#appendix)

## Criteria A: Planning

## Problem definition

I am High School Student in an International School in Japan who attends an English Literature class. The class requires active discussion and exchange of ideas about the books read for the course. I am asked to manually create a personal portfolio and add my thoughts in it after the discussions in class, however at the moment this method has become too time consuming for me, tedious and hard to keep track off. It is also difficult for me to find important information when studying and is hard to catch up when I miss a class. Additionally, I have spoken with my classmates which have agreed about it being an issue for most students in the class and including motivation as one of their issues too. After a brainstorm session (shown in Appendix section 1), I've concluded that I am in need of a Social Network that allows me to post my ideas and have class discussion in an organized manner. Additionally, it is important to consider that the client's budget is limited.

## Rationale for Proposed Solution
  
Considering the clients requirements an adequate solution includes a Social Network that allows to post ideas and have class discussion in an organized manner. For this application it may adequate to consider a properly styled and formated website that can receieve data from the users and store it into databases. Considering the budgetary constrains of the client, the software tools that I propose for this solution are SQLite, Flask, HTML, CSS and Python. This tools will complement each other to fulfill the success criteria set by the client. Firstly, Flask is a web development framework that we will use to create and host the server for the Book Review webiste and allow us to use Python, HTML and CSS altogether. Secondly, I will be using the software tool Python 3.10.7. Python is free and platform-independent. That is, if you write the code on one of the Windows, Mac, or Linux operating systems, then you can run the same code on the other OS with no need for any changes so it can be run. Nevertheless, requieres a lot of memory[^1]. Thirdly, I will be using CSS which stands for Cascading Style Sheets. CSS is a design language that makes a website look more appealing than just plain or uninspiring pieces of text [^2]. Considering the use of CSS might be relevant for the user as she wants to share her ideas in an organized manner and CSS allows to style the page for a more clean look. Lastly, we will be considering the use of HTML when buiding the Social Network. HTML stands for HyperText Markup Language. It is a standard markup language for web page creation. It allows the creation and structure of sections, paragraphs, and links using HTML elements (the building blocks of a web page) such as tags and attributes [^3]. Considering the use of HTML might be relevant for the user has she want a space to share ideas, where users will be posting about the books read in class. HTML will help layout all of the information shared in the Social Network. Lastly, SQLite is 
  
## Design statement

I will design and make a Book Review Social Network called LitPals for a highschool student. LitPals will be about creating a discussed-based Social Network for her English class and will be constructed using the software Python 3.10.7, Flask, HTML, SQLite and CSS. It will take about 3 weeks to make and will be evaluated according to the criteria below.

## Success criteria
  
1. Litpals displays the posts organized by book from the class reading list. [issue: "...tedious and hard to keep track off..."]
2. Litpals allows the user to create a post for every book in the class reading list. [issue: "...requires active discussion and exchange of ideas about the books read for the course..."]
3. Litpals provides a profile with a section to see the user's information and see all posts made by the user. [issue:　"...difficult for me to find important information when studying..."]
4. Litpals provides some statistics to display the top 3 commenters in LitPals [issue: "...motivation as one of their issues too..."]
5. Litpals provides a search bar to identify keywords within a book discussion. [issue: "...hard to keep track off..."]
6. Litpals displays the date a post was made. [issue: "...hard to catch up when I miss a class..."]

# Criteria B: Design

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1      | Planning: First meeting with client |  Getting a sense of what is the problem and the needs of the client. Start to get a deeper understanding of how does the desire interface looks for the client. Note taking on the meeting.  | 6min                  | April 18 | A
| 2      | Analysis of planning meeting | Taking information learnt form the first meeting with the client to see what was understood from the developer part and present next meeting with client to confirm if the information was understood correctly. |  10 min  | April 18 | A
| 3      | Planning: Brainstorming session | Talking to the community the client is enagaged with and that will also be users of the social network. Getting a sense of what is the problem and the needs of the client and the problem in the community (target audience of the Social Network). Go together through the information again and understand can be made and what cannot. Note taking on the meeting | 5 min | April 18 | A
| 4      | Analysis of planning meeting | Taking information learnt form the second meeting with the client to see what was understood from the developer part and present next meeting with client to confirm if the information was understood correctly. | 15 min | April 19 | A
| 5      | Problem definition | After the meetings with the client, establish the problem that the project is going to be solving specifically and what are the main needs of the client | 20 min | April 20 | A
| 6      | Planning: Establishing Success criteria | Taking into account the problem definition previously established, meet with the client once again to establish the success criteria for the habit tracker. Establish where the primary focus should be when developing th application to satisfy the client's neccesities | 10 min | April 20 | A
| 7      | Planning: Supervisor checks success criteria | After meeting with the client, show draft version of the succes criteria and got feedback on improvement | 20 min | April 20 | A 
| 8      | Design statement | Taking into account the previously approved succes criteria and problem definition, explain in a consice and clear manner the purpose of the project to the client | 5 min | April 20 | A
| 9      | Rationale for Proposed Solution | Analize the design statement, success criteria and client's needs and determine which tools best suit the development of LitPals (Book Review Social Network) | 20 min | April 21 | A
| 10     | System Diagram | Draw the system diagram for LitPals (Book Review Social Network) to have a clear idea of the hardware and software requirements for the proposed solution. | 30 min | April 22 |  B
| 11     | Wireframe | Draw the wireframe for LitPals (Book Review Social Network) to have a clear idea of the design of the screens and functionality for the proposed solution. | 45 min | April 23 |  B
| 12     | Planning: Design approval by client | Meet with client and show and explain wireframe diagram and got approval for LitPals (Book Review Social Network) design. | 40 min | April 24 | B
| 13     | ER Diagrams | Draw the ER Diagram for LitPals (Book Review Social Network) to have a clear idea of the tables needed in the database for the proposed solution. | 15 min | April 25 | B
| 14     | Create Hashing system | Code the hashing system for password protection using 'sha256' to encrypt password and check password in login and registration for LitPals (Book Review Social Network). | 45 min | April 26 | C
| 15     | Alpha Testing | Test the code for the hashing system. | 2 min | April 26 |  C
| 16     | Create the style for login page | Use CSS (Cascading Style Sheets) to create the design and visuals of the login screen. Add text fields to enter information such as email and password. Create buttons to Login and Resgiter. Create "LitPals" title. Add a bookshelf design next to login | 120 min | April 26 | C
| 17     | Fix style of login page | Fix placing of the text fields, buttons and title in the Graphical user interface to get a more clean login screen and for the login form to fit with the bookshelf animation. | 100 min | April 26 | C
| 18     | Create the style for Register page | Use CSS (Cascading Style Sheets) to create the design and visuals of the register screen. Add text fields to enter information such as username, password and check password. Create buttons to go back to login and finalize registration. Create  "LitPals" title and "Register" subtitle. | 80 min | April 26 | C
| 19     | Create database handler class | Create class named database_handler that provides methods to interact with a SQLite database. This class provides a simple interface for interacting with a SQLite database, including querying the database, inserting or modifying data, and creating tables. This will later be used to save overall information managed in LitPals (Book Review Social Network). | 50 min | April 29 | C
| 20     | Create code for Login system | Code the login system for user to login to Main screen and access LitPals (Book Review Social Network). | 125 min | April 29 | C
| 21     | Create code for registration system | Code the resgistration system for user to be added to the database and be able to log in to LitPals (Book Review Social Network). Use SQLite queries in the python code to create the database to save new user's information.| 35 min | April 29 | C
| 22     | Create password policy and error page display | Code a password policy that established certain requirements for the user when registering. Additionally, pages were created to indicate the user when the information was not correctly entered as required. In this error pages, possible mistakes being made by the user are pointed out and how to fix them. | 25 min | April 29 | C
| 23     | Create the style of the Main Screen | Use CSS to create the design and visuals of the Main screen. Create interactive bookshelf that divides posts for each book. Add buttons for profile, statistic and log out function | 20 min | May 3 | C
| 24     | Creating New Post Form page per book| Create a form where the user can indicate the username, topic and post text. Create the style anf format of the page with HTML and CSS. Repeat the same step for each book (4). | 70 min | May 3 | C
| 25     | Creating databases for New Post Form per book | Create a databases (4) to save the posts created within each specific book. Use SQLite queries in the python code to create the databases. | 5 min | May 4 | C
| 26     | Create style for the "View Posts" Page per book | Create style for the page were posts of the respectove book are going to be shown. | 30 min | May 5 | C
| 27     | Create code for the "View Posts" Page per book | Connect the posts databases of each book to the View Posts page so information is correctly displayed. | 130 min | May 5 | C
| 28     | Create style for the "Stats" Page | Create a ranking with some emojis and colors. Put the person who commented the most with a bigger font.| 15 min | May 5 | C
| 29     | Create code for the "Stats" Page | Create a ranking by taking from the database the people who commented the most and displaying with the Css previously done. | 10 min | May 5 | C
| 30     | Create style for "Profile" page | Create the user's profile. Add a table to display user's information. Add a button that will later take the user to see their own posts | 100 min | May 6 | C
| 31     | Create style for "Profile" page | Create the user's profile. Connect the database to acces the users information a table to display it in the table previosly created. | 50 min | May 6| C
| 32     | Create "Log Out" function and button | Create a button in the main screen and whne pressed connect it to the login screen back again. This will function as a log out function. | 20 min | May 6 | C
| 33     | Alpha testing | Test the code for the different functionalities created for LitPals. | 20 min | May 8 | C
| 34    | Meeting and Beta testing by client | Meet with the client and let them test LitPals. Get feedback on possible improvements/fixes. | 30 min | May 8 | C
| 35     | Fix errors | Modify following the feedback given in the beta testing session with the user | 120 | May 10 | C
| 36     | Alpha testing | Test the code for the different functionalities created for LitPals after the feedback was implemented. | 15 min | March 9 | C
| 38     | Final approval by client | Obtain approval by the client on the overall development of Litpals | 20 min | May 10| C
| 39     | Flow diagrams | Draw the flow diagrams for some of the important function inside the code for Litpals. | 90 min | May 10 | C
| 40     | UML Diagram | Draw the UML diagrams for the screen structure and internal functionality for Litpals. | 40 min | May 10 | C
  
# SYSTEM DIAGRAM
  
![image](https://github.com/Madaniarias/Unit4_rep/assets/111761417/31ba687f-8e47-4870-8d87-daa779dbe041)
<sub>FIG 1. System Diagram is divided in Keyboard and Screen (Connected). Following by the computer (MacBook Air) and Processor (Dual-Core Intel Core i5 1.8GHz 8GB. Next, the Operating System (OS: MacOS 12.5 (21G72). Within the Flask Server, the software being used is Python 3.10.7. Operating inside the software, there is the 2 python files (app.py and my_library.py). Additionally we have a templates file that includes all the html for LitPals and a static file that includes all the css for LitPals. Lastly, this is connected to the database engine SQLite. There is one database (social_net.db) with 2 tables inside (user and forum_posts).
  
# WIREFRAME DIAGRAM
 
<sub>FIG 2. In progress...
  
# FLOW DIAGRAMS
  
 <sub>FIG 5. In progres... 
  
# ER DIAGRAMS
  
<sub>FIG 6. In progres...
  
# UML DIAGRAMS
  
<sub>FIG 7. In progres...

# TEST PLAN
  
| Test No | Type of Test                                                |  Date                                                                                               | Procedure | Expected Outcome | |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Functional: Testing the registration system for LitPals | April 28 | Run LitPals > Click on the register button in the Log in screen > Fill the text fields with username, password and checked password. > Click on the register button on the register screen > Close LitPals by clicking the log out button > Locate social_net.db database > Find in the main file the user table > Click on user table to open a tab to see the contents of the table > Confirm wether the information inputed in the registration screen has been saved in the user table in the social_net.db database or not | The new user information will be added in the user table in the database social_net.db when following the described procedure.
| 2.      | Functional: Testing the "New Post" system for LitPals  | May 5 | Run LitPals > Fill the text fields with username and password in the login screen > Click on the login button in the Log in Screen > Click on the "New Post" button on the Main Screen > Fil in the form the fields of username, book title, topic and post text > Click save post > Close LitPals by clicking the log out button > Locate social_net.db database > Find in the main file the forum_posts table > Click on forum_posts table to open a tab to see the contents of the table > Confirm wether the information inputed in the registration screen has been saved in the user table in the social_net.db database or not | The posts will added in the forum_posts table in the database social_ nnet.db when following the described procedure.
| 3.      | Functional: Testing the MyPosts button on the Profile Screen to see if the posts are being filtered correctly | May 7 | Run LitPals > Fill the text fields with username and password in the login screen > Click on the login button in the Log in Screen >  Click on the Profile button on the main screen > lick on the My Posts button on the Profile screen > Look at the posts that show up in that section > Locate social_net.db database > Find in the main file the forum_posts table > Click on forum_posts to open a tab to see the contents of the table > Confirm wether the information that showed in the MY posts screen was only from the user that was logged in at that moment. | Only posts made by the user that is logged in at the moment shousl souls up in My posts Screen in The Profile.
| 4       | Non-functional: Capabilty for the user to understand LiPals login and registration system independently | May 1| Run LitPals > Give the user only the instruction of registering and then login in to the into LitPals without further explanation on how the login and registration system works > see how much does it take the user to figure the registration and login system. | The user will register and login in less than 2 min.
| 5.      | Non-functional: Capabilty for the user to understand hos to make a new posts in LitPals independently | May 5 | Run LitPals > Give the user only the instruction of creating a new post for the book of their preference form the class reading list without further explanation on how to create a new post > see how much does it take the user to figure how to create a new post in LitPals | The user will register the crreate a new post in less than 5 min.
| 6.      | Non-functional: Capabilty for the user to understand how to use the search bar created for LitPals | May 9 | Run LitPals > Give the user only the instruction of locating the word "shadow" within the book In Praise of Shadows discussion > see how much does it take the user to figure how to search up the word "shadow" within the book In Praise of Shadows discussion | The user will figure out how to use the serach bar in less than 30 seconds. 
  
# Criteria D: Functionality

### VIDEO IN GOOGLE DRIVE FOLDER

  
# Sources
[^1]: “Advantages of Python | Disadvantages of Python.” Python Geeks, 25 June 2021, pythongeeks.org/advantages-disadvantages-of-python/.
[^2]: User, Devmountain. “What Is CSS and Why Should You Use It?” Devmountain, 22 Apr. 2019, devmountain.com/blog/what-is-css-and-why-use-it/.
[^3]: Astari S. “What Is HTML? The Basics of Hypertext Markup Language Explained.” Hostinger Tutorials, 15 Nov. 2018, www.hostinger.com/tutorials/what-is-html.
[^4]: 
[^5]:
