# OVERVIEW



# GUIDE's Table of Contents
- [Workout_Prescription](#workout_prescription)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Author](#author)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [Target Audience](#target-audience)
  - [Design Choices](#design-choices)
    - [Colors](#colors)
    - [Typography](#typography)
    - [Images](#images)
    - [Design Elements](#design-elements)
    - [Animations and Transitions](#animations-and-transitions)
    - [Frameworks](#frameworks)
    - [Custom Styles](#custom-styles)
    - [Custom Javascript](#custom-javascript)
  - [Wireframes](#wireframes)
- [Information Architecture](#information-architecture)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Choice](#database-choice)
  - [Data Models](#data-models)
  - [CRUD Diagrams](#crud-diagrams)
- [Agile Process](#agile-process)
  - [Project Goals](#project-goals)
  - [Initial User Stories](#initial-user-stories)
  - [Feasibility vs Importance](#feasibility-vs-importance)
  - [Scope](#scope)
  - [Agile Tool](#agile-tool)
    - [User Story Example](#user-story-example)
    - [Epic Stories](#epic-stories)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Future Features](#future-features)
  - [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
  - [Accessibility Testing](#accessibility-testing)
    - [Accessibility Audits](#accessibility-audits)
    - [Keyboard Navigation](#keyboard-navigation)
    - [Chrome Vox Reader](#chrome-vox-reader)
  - [Core Web Vitals](#core-web-vitals)
  - [Validation Testing](#validation-testing)
    - [CSS Validation](#css-validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [JSON Validation](#json-validation)
  - [Automated Testing](#automated-testing)
  - [Defects](#defects)
  - [Defects of Note](#defects-of-note)
  - [Outstanding Defects](#outstanding-defects)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Deployment](#deployment)
  - [Prerequisites](#prerequisites)
  - [Fork and Clone the Repository](#fork-and-clone-the-repository ) 
  - [Local Deployment](#local-deployment)
  - [production Deployment](#production-deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)
  
====================================== The Sections you Fill in are below ==============================

# Workout_Prescription

- A website that offers a variety of fitness programs to help you achieve your health and fitness goals. Whether you're looking to lose weight, build muscle, or simply improve your overall health. The trainers create personalized training programs tailored to your individual needs and goals.
- The user can access a personalized workout plan from anywhere with an internet connection, at any time that suits the schedule.
- Include a picture of site that shows it in responsive states and links to deployed code: https://ui.dev/amiresponsive

## Live Site 

- https://workout-prescription.herokuapp.com/

## Repository

- https://github.com/naragurgel/workout_prescription

## Author

Nara Gurgel

# Table of Contents
🚀 **merit & beyond**

Generate after readme is complete by copying and pasting your readme from this point & below into this tool:
- [mardown table of contents generator](https://luciopaiva.com/markdown-toc/)
**NOTE:** It does have some bugs if you have dashes or trailing spaces in your headers, so make sure all these WORK!

# UX

## Target Audience

- The Workout prescriptions page is designed for both men and women of various age groups who are interested in maintaining a healthy and active lifestyle. These users are typically health-conscious, fitness enthusiasts, and may have specific interests such as weight loss, muscle building, or overall well-being.

## Design Choices

 - The website will prioritize intuitive navigation and clear communication of workout instructions. The simplicity of the design ensures a user-friendly interface, allowing users to easily navigate and engage with their workout plans without distractions.

### Colors

- Color scheme predominantly consisting of tons of black, green and white. The use of black provides a sense of professionalism, green refreshing and energetic touch, symbolizing growth and vitality, aligning with the health and wellness focus of the website. White is promoting a visually calming experience. 
- include a screenshot of your pallet using a tool like coolors.co

### Typography

-  typography has intuitive layout contribute to a clarity and ease of use throughout the website.
Montserrat-  Its clear letterforms and excellent readability make it suitable for important information and instructions related to workout plans. 
Roboto Condensed-  It is a condensed sans-serif font that offers a balance between professionalism and legibility. 
- include screenshots of fonts used and links to the appropriate website ex) https://fonts.google.com/specimen/Raleway

### Images

The reason for the cover photo to be dumbbells is mainly because dumbbells are a iconic symbol of strength training and fitness, which is the website's focus. The photo of dumbbells creates an immediate visual association with exercise, motivating and inspiring users to engage in their prescribed workouts and pursue a healthier lifestyle.

### Design Elements

> - desktop navigation
> - mobile navigation
> - footer
> - containers/cards
> - buttons
> - text input
> - textarea inputs
> - modals/layers
> - pagination
> - images
> - tooltips
> - icons

### Frameworks

- Bootstrap: Firtly I opted to utilize Bootstrap for my website due to the desigh elements that they support, they also give a design that adapts to various devices. The ready-made templates and components provided invaluable time-saving advantages.

### Custom Styles

- I made some changes to the fonts, font sizes and colors of the fonts and background. It's all in the folder prescriptions/static/css/wp_styles.css

### Custom Javascript

- I made time duration of the alert message using JavaScript. It's in the folder prescriptions/templates/base.html

## Wireframes


# Information Architecture

For the Workout Prescription website, I have created a admin model to CREATE, UPDATE and DELETE the exercices and details in each workout prescription. The structured is:

- 
## Entity Relationship Diagram
🚨**Required** 

 [draw.io](https://app.diagrams.net/) is a free tool that can help you draw up an ERD concerning your custom model.

Wade Williams wrote a great [blog]( https://wadewilliams.com/technology-software/generating-erd-for-django-applications/) on how to add a django extension to auto create an ERD. 

You can always draw one out by hand or in google sheets. 

## Database Choice

Postgres because of the hosting capabilities of Heroku enables effortless deployment and expandability, and PostgreSQL stands out as one of the endorsed and suggested databases on the Heroku platform.

## Data Models

Fields:

- owner (ForeignKey to User model): Represents the owner/user associated with the workout.
- name (CharField): Represents the name of the workout. It has a maximum length of 250 characters and must be unique.
- instructions (TextField): Represents the instructions for the workout. It has a maximum length of 1000 characters and can be null or blank.
- exercises (ManyToManyField to WorkoutItem model): Represents the exercises associated with the workout.
Validations:

- owner: A required field, as it represents the owner/user associated with the workout.
- name: A required field that must be unique and has a maximum length of 250 characters.

Related Code:

In the repository, you can find the code related to the CREATE, READ, UPDATE, and DELETE operations for this model in the following files:
- models.py: Contains the definition of the Workout Data Model and its fields.
- views.py: Includes the logic for handling the CRUD operations associated with this model.

 **Activities Model**

CRUD Operations:
Create: Create a exercise or a workout list to each user.

Read: The workout sheet is visibl on the workout list page and the user can have acess to his own workout by acessing the website.

Update: The workout can be updated when the staff menber wants to change anything on the prescription.

Delete: The workout or exercice can be deleted if a staff menber wants to change the workout prescriptions.

## CRUD Diagrams
🚀 **merit & beyond**

You can also have CRUD diagrams to show the accessors visually how the model is
used in your site.

I used [draw.io](https://app.diagrams.net/) and hooked it up to my google drive to create the screenshot below

> ![image](https://user-images.githubusercontent.com/23039742/154406188-c9beb57a-2fd1-4f26-a8ed-bee320e46e3d.png)

# Agile Process

## Project Goals

The purpose of the workout prescription website is to provide a comprehensive platform for individuals to access personalized and effective workout plans tailored to their specific fitness goals, preferences, and medical conditions.

For users:

- some just come and read the benefits related to the workout prescriptions online.
- some users are registered, so they receive a online prescription

For administrators:

- the personal trainers are administrating the site (adding, updating & deleting models)

## Initial User Stories

- As a website visitor, I want to be able to create a user profile so that I can access personalized workout prescriptions.
- As a user, I want the website to offer a variety of workout options, including cardio, strength training, and flexibility exercises, so that I can have a well-rounded fitness routine.
- As a user with specific health conditions, I want the website to offer workout recommendations tailored to my needs, so that I can exercise without compromising my health.
- As a user, I want the website to provide a variety of workout routines and exercises, so that I can keep my workouts interesting.
- As a coach, I want to have the option to customize all workout plan by adding or removing specific exercises, so that I can tailor it to my preferences and user's needs.
- As an trainer, I want to be able to create and manage the available workouts in the system.
- As a trainer, I want to be able to assign workout prescriptions to my clients so that I can help them reach their fitness goals.
- As a user, I want to check sets, reps, rest time for each exercise in my workout prescription.
- As a user, I want to visit the website to receive personalized exercise plans and guidance, so that I can achieve my fitness goals effectively
- As a user, I want to log in to my account so that I can securely access my workout prescription personalized information.
- As a user, I want to have a user-friendly interface that guides me through the website to register and to acess my workout.

## Feasibility vs Importance
🚀 **merit & beyond**

To scope the project for a MVP (minimally viable product) a feasibility analysis was done.

The features in the table below have been taken from the user stories above. Generic features found in most websites
will also be implemented such as nav-bar, footer, obvious website purpose etc.

| Opportunity/Feature | Feasibility/Viability (score out of 5) | PurposeLevel of Importance (score out of 5) | In Or Out |
|---------------------|----------------------------------------|---------------------------------------------|-----------|
|                     |                                        |                                             |           |
|                     |                                        |                                             |           |
|                     |                                        |                                             |           |
|                     |                                        |                                             |           |

> You should discuss the outcome of what you will be dropping based on the outcome. Making a scatter plot of the scores and coloring the dot 

## Scope
🚀 **merit & beyond**

Now you have to talk about the scope to reduce things more, you don't necessarily need all the bells and whistles, they could be beyond your skill set. Think basic stuff. Write a paragraph to sum up how you morphed the project goals into a prioritized list of user stories that would be delivered as an MVP (minimal viable product).

## Agile Tool
🚨**Required** 

You are required to use an agile tool to track user stories through the development process. You could use a spreadsheet, JIRA, or another tool, and CI taught you how to use GitHub Issues to write your user stories.The website aims to empower users by offering a convenient and accessible resource that guides them in achieving their desired fitness outcomes, whether it's weight loss, muscle gain, improved cardiovascular health, or overall well-being. 

- State what tool you used (GitHub, Jira, Rally, Trello, a spreadsheet)
- Include a link to the tool's product/progress board
- Include a screenshot of the tool's product/progress board

Lessons on how to use gitHub for a product board can be found in the LMS system under:  
- Principles of Agile Development > 
  - Common Agile Practices > 
    - Product Backlog

### User Story Example
🚨**Required** 

- include a screenshot of a user story with all it's details

If you made a template, call that out and provide:
- link to template
- screenshot of template

### Epic Stories
🚀 **merit & beyond**

If you want a chance at  **DISTINCTION**, you need to have epic stories to stories with tasks.

Example:
EPIC: Navigation As a user, I want to have easy to see navigation on the page, so I can intuitively interact with the site without getting frustrated both on mobile and desktop devices.

USER STORY: Navigation: Unauthenticated user: As an unauthenticated user I want to see what the site is about, and easily figure out how access more information. 

Tasks:
- [ ] Build Template so information in one spot
- [ ] Rough in Logo
- [ ] Add in Register/Login/Forgot Password
- [ ] Add Main List Page
- [ ] Rough in CSS

Acceptance Criteria
- [ ] navigation sticks in view as user scrolls
- [ ] looks good on mobile
- [ ] looks good on desktop
- [ ] links work & go where expect
- [ ] passes accessibility

**What to keep in this section**
- screenshot of epic story
- EPIC TEMPLATE screenshot
- link to EPIC TEMPLATE


# Features
🚨**Required** 

In this section, you should go over the different parts of your project, and describe each in a sentence or so and how they tie into  your user stories.

## Implemented Features
🚨**Required** 

It's easiest to break this section down into the header, footer, and each page/layer/signification section of your website. Call out any differences for mobile vs desktop presentations, include a screenshot of the implemented feature.

Don't forget your custom 404 error page

Don't forget the 3 phases of navigation:
- unauthenticated
- general authenticated user
- superuser authenticated

And don't forget Defensive programming bits
- validation of form inputs
- not allowing users to create, read, update and delete information they shouldn't

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

## Future Features
🚀 **merit & beyond**

Use this section to discuss plans for additional features to be implemented in the future

If you end up not developing some features you hoped to implement, you can include those in this section too.

## Testing
🚨**Required** 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the Features section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

**At this point, you should use gitHub Issues Templates** to track test cases and defects. Here's a [document](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit#heading=h.3kdbr3tqbzi) I put together for this process.


## Manual Testing
🚨**Required** 

For any scenarios that have not been automated, test the user stories/features manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios in markdown such as:

**Manual Testing For Contact Form**
1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

Or you can use markdown check boxes and write them up per feature:

**Manual Testing For Contact Form**
- [x] try to submit 
- [x] Try to submit the empty form and verify that an error message about the required fields appears
- [x] Try to submit the form with an invalid email address and verify that a relevant error message appears
- [x] Try to submit the form with all inputs valid and verify that a success message appears.
- [x] no console errors
- [x] submit goes to code institute data dump page in new tab
- [x] looks good on mobile (one column)
- [x] looks good on tablet (two columns)
- [x] looks good on desktop (two columns but not SUPER HUGE)

Or you can use a spreadsheet
    
Here is a [Manual Testing Template](https://docs.google.com/spreadsheets/d/1vc1IVL-ydQwWeWMqnk_GRox6HE6qxDLpchGse8Crayo/edit#gid=296578096) that you can use as a starting point to keep track of your testing efforts. Make a copy of it in your own account and update as needed to reflect the browsers you are testing and features.  

It's ok to spot check specific functionality across devices and browsers but each page should be viewed as a whole for each device/browser combo at least once.

A quick way to check if items are exceeding the screen width of a project is to run this javascript in the console for various screen emulations:

```
var docWidth = document.documentElement.offsetWidth;
[].forEach.call(document.querySelectorAll('*'),function(el){if(el.offsetWidth > docWidth){console.log(el);}});
```

## Compatibility and Responsive Testing
🚨**Required** 

>To save time, you can create this type of table in [markdown table generator](https://www.tablesgenerator.com/markdown_tables)
>
>As of Feb 14, 2022 CI students can take advantage of the Student Developer Pack where you have access to great things like [browserstack](https://education.github.com/pack/offers/#browserstack) You should have received an email about how to activate your student Developer Pack, here's a [slack](https://code-institute-room.slack.com/archives/C0L316Z96/p1644946870567999) with details if you can't find it in the associated thread.


Minimally you should use dev tools and emulators to try to test you site on various screen sizes and browsers and note it in a table:

I ensured my site was worked well, and looked nice on a variety of devices & browsers as noted in the table below:

| TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
|-------------------------------|-------------|------------|---------------|
| real phone: motog6            | chrome 78   | android 8  | XS 360 x 640  |
| browser stack: iPhone5s       | safari  13  | iOs        | XS 320 x 568  |
| dev tools emulator: pixel 2   | firefox  69 | android 8  | SM 411 x 731  |
| browserstack: iPhone 10x      | Chrome 78   | iOs 11     | SM 375 x 812  |
| browserstack: nexus 7 - vert  | Chrome 78   | android 7  | M 600 x 960   |
| real tablet: ipad mini - vert | safari  13  | iOs 6      | M 768 x 1024  |
| browserstack: nexus 7 - horiz | firefox 69  | android 7  | LG 960 x 600  |
| chrome emulator: ipad - horiz | safari 13   | iOs        | LG 1024 x 768 |
| browserstack windows PC       | Chrome 78   | windows 10 | XL 1920 x 946 |
| real computer: mac book pro   | safari 12.1 | Mohave     | XL 1400 x 766 |
| browserstack windows pc       | IE Edge 88  | windows 10 | XL 1920 x 964 |


🚀 **merit & beyond**
Document why you chose the devices:

1. Visit https://gs.statcounter.com/browser-market-share to figure out the most popular browsers & operating system combos seen across the web for the geographic region, and platform(s) and screen sizes you expect your users to belong to. 

2. Include a sentence about why you chose the combinations you did.

3. Create a table that lists out what devices, browsers, and operating system you tested your application on and a brief description of why you chose the mixture you did. The point is to prove that you looked at the site across various browsers, operating systems, and viewport breakpoints.

4. if you can't find the browser/device/OS combinations you want on Browserstack with your GitHub student webpack (or you didn't activate that in time), note what you'd ideally test on then what you ended up testing on as a compromise. 

5. Build a table to summarize the choices you made [markdown table generator](https://www.tablesgenerator.com/markdown_tables)

The combinations above were chosen because of the following information I gathered  from [ga.statcounter.com]( https://gs.statcounter.com/browser-market-share) for the US from Aug-Oct 2021:
**browser Version Market Share**:
  - safari iphone: 26.32%
  - chrome for android: 21.32%
  - Chrome 105.0: 15.77%
  - Chrome 104.0: 6.28%
  - Edge 105: 4.99%
  - Safari 15.6 3.76%
**browser Market Share**
  - chrome: 50.28%
  - Safari: 34.65%
  - Edge: 6.37%
  - Firefox: 3.52%
  - Samsung Internet: 2.04%
  - Opera: 0.89%
**platform breakdown**
  - mobile: 51.26%
  - desktop: 45.73%
  - tablet: 2.97%
  - console: 0.03%

## Accessibility Testing
🚨**Required** 

Accessibility testing is aimed to make sure that those with visual or physical disabilities can still browse your website. Some users have had strokes or accidents that make it difficult to use a mouse, so they use keyboard keys to tab through sites. Others use screen readers that rely on HTML tags to help the user navigate quickly through the site to find information they want, others have color blindness or contrast issues. It's the law to provide services 
Here's a [site](https://www.w3.org/WAI/fundamentals/accessibility-intro/#:~:text=Accessibility%20is%20Important%20for%20Individuals%2C%20Businesses%2C%20Society,-The%20Web%20is&text=That%20is%2C%20the%20accessibility%20barriers,older%20people) where you can learn more about accessibility and the internet.

### Accessibility Audits
🚨**Required** 

Accessibility audits run through the HTML and determine if the parts of the WCAG (web content accessibility guidelines ) that are implemented through HTML tags and attributes are present. They can do some checking for low vision/contrast stuff too.

You should run your deployed website pages through  at least on auditing tool. lighthouse's audit to check performance, accessibility, best practices and SEO scores. You should aim to get 85 or higher score on accessibility. 

**You should fix issues associated with:**
- contrast 
- aria labels
- alt text
- large images
- skewed images

**Lighthouse**
https://web.dev/measure/  If you have lower scores, read the report and follow the links to address the flagged issues. You can run this tool from Chrome Dev Tools too against your local machine, but chrome extensions can sometimes give you missing alt text on things like the grammarly plug in tracking pixel.

You want a score in the green for accessibility and should look at ways to get it to 100.


**[WAVE chrome](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh?hl=en-US) extension**
Wave is developed by webaim.org and does a bit better at contrast issues and uses 2.1 guidelines

**Contrast Checkers**
- https://webaim.org/resources/contrastchecker/
- https://color.a11y.com/

### Keyboard Navigation
🚀 **merit & beyond**

Another way to accessibility test your site is to try to click on the browser URL and see what happens if you use the tab, arrow and enter keys. Does it work well or does the user get stuck? Check this in a couple browsers as the focus & active outlines are typically styled by the browser

The expected results for various keyboard entries and field types can be found [here](https://webaim.org/techniques/keyboard/#testing)

You can take a video of this testing if you want and convert it to a gif and paste that into your readme. Record something to yourself in a Slack direct message, then download it. Then you can use https://cloudconvert.com/mp4-to-gif to convert the mp4 to a gif and just paste it into the readme via GiHu, and it'll resolve itself.

### Chrome Vox Reader
🚀 **merit & beyond**

If you are really ambitious, you can use the [VoxReader](https://chrome.google.com/webstore/detail/screen-reader/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en) extension in chrome to see what your site sounds like on a screen reader. It really drives home the need for good aria-labels & semantic HTML.

## Core Web Vitals
🚀 **merit & beyond**

SEO is greatly impacted by your core web vitals. The readout from https://web.dev/measure/ which is essentially a lighthouse audit gives your site scores in 4 categories. Ideally you want your site to be in the green for all 4 scores. web.dev has dedicated servers to test deployed sites without extensions that skew the results, so it's best to get results from this site.
 You should talk about the results for each section pay attention to 

## Validation Testing
🚨**Required** 

In this section you should write up any websites you used to validate your code and include screenshots.

**Validation issues are an automatic failure** You should run these about 3 times:
- when you first deploy your site
- just when you think you are done testing
- right before you submit because 😼, ⚽, 🐶 & 👼 can eliminate a closing tag or curly bracket without you noticing.

### CSS Validation
🚨**Required** 

The [Jigsaw validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

> If you only have one CSS file, you can just run the validator through one deployed page URL, if you have custom CSS for different pages, make sure you hit those different URLS, or do direct input on each file.

Include a screenshot for each CSS file which includes the Green no ERRORS bar, two check marks:

**styles.css**
![img.png](documentation/images/css-validation.png)

### HTML Validation
🚨**Required** 

The **[W3 HTML Validator](https://validator.w3.org/)** was used to validate HTML by coping the page source as a direct input.

> For each view you wrote, you should validate the HTML and have a test case for it linked to from here
> NOTE: You may need to right-click to view the source of each page and paste that into the validator if you need to go through authentication to get to the page.

### JavaScript Validation
🚨**Required** 

The **[Jshint validator](https://jshint.com)** was used to validate each JS file.

> for each .js file, copy the code and paste it into this site, and have a test case for it linked to from here. You can have warnings, but no errors.
> if using ES6, add this before pasting in your file: `/*jshint esversion: 6 */ `, similarly you can update it to 7 if you see warnings about ES7 syntax `/*jshint esversion: 7 */ `

### Python Validation
🚨**Required** 

**[CI's pep8 tool](https://pep8ci.herokuapp.com/)** was used to validate each .py file created.

> for each .py file you created, copy the source code and paste it into this site, and have a test case for it linked to from here.
> include a screenshot of results in the test case showing NO ERRORS. (you should do this for all .py files in your repo

**run.py**

![image](https://user-images.githubusercontent.com/23039742/212106175-36b2f18a-7c75-458d-94dd-9886e81c71f3.png)

Ideally you would have no errors remaining outside of line too long which you can fix by 

adding
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

Note any errors or warnings you are ignoring and why.

### JSON Validation
🤷‍ **Required if you made some files** 
The **[JSONLINT validatior](https://jsonlint.com/)** was used to validate JSON files.

> for each .json file, you should copy the code and paste it into this site, and have a test case for it linked to from here.

## Automated Testing
🚀 **merit & beyond**

If you managed to write jasmine tests or some django tests, note those files out here and how to run them. I only did this in my last project as I didn't have the time or energy to learn how to write tests. https://github.com/maliahavlicek/ms4_challenger/blob/master/documentation/TESTING.md is my write-up about those and how I ran them, but a simple test I'd recommend is authentication and any views you limit to superusers or logged-in users:

https://github.com/maliahavlicek/ms4_challenger/blob/master/challenges/tests/test_views.py

## Defects
🚨**Required** 

At this point you need to be using GITHUB's Issues to track these as it helps you with the AGILE process requirement and it's really easy to copy/paste screenshots in and then write up how you closed them.

[Here's a brief overview](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit#heading=h.542xzc8ufx4x) I put together on how to do this.

This what my custom bug template looks like in the UX
![image](https://user-images.githubusercontent.com/23039742/165650359-a352d64e-b128-473d-ab60-7df0568a44df.png)

- provide a link to the issues link in GitHub
- if you made a custom template include a screenshot
- if you made a custom template include a link to the template

## Defects of Note
🚀 **merit & beyond**

Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and link to them directly here. The accessors really like to know the struggle is real and that by doing this you picked up more skills.

## Outstanding Defects
🚨**Required** 

It's ok to not resolve all the defects you found as long as:
- it does not impact a user from completing a vital function on the website
- it only affects a very small subset of users
- is an extreme edge case that very few users would try
- there is an open issue against a framework, browser or technology used

If you know of something that isn't quite right, create an issue and link to it here and explain why you chose not to resolve it. 

Sometimes it's as simple, word wrapping issue that makes the site look odd at a certain screensize that you just didn't have time to fix due to the impending deadline it's best to mention it but note why you allowed it to go live: "Yes it looks odd, but it doesn't impact core functionality of the site." than to let the accessors think you didn't notice it. 


# Technologies Used
🚀 **merit & beyond**

This section just summarizers tools and programming languages you used.

## Languages
🚀 **merit & beyond**

-write bullet points for the languages you used (HTML, CSS, JAVASCRIPT, PYTHON,  DJANGO)

## Frameworks, Libraries & Programs Used
🚀 **merit & beyond**

List out the tools you used with a link and a short description (this helps others figure out where to get the bonus points & reminds you what you used for your next project
- Balsamiq
- Coolors.co
- fontawesome
- gitpod
- github
- google fonts
- font awesome
- amiresponsive
- table of contents creator
- markdown table generator



# Deployment
🚨**Required** 

## Prerequisits
🚀 **merit & beyond**

If the user is required to have certain keys and credentials you should include this section with directions on how to get the necessary information. ex)

1. **Gmail Account:** In order to have verification and forgot password emails sent to registered users you need a
   google account. 
  - [create a gmail accoount](https://accounts.google.com/signup) 
  - [downgrade to less secure](https://myaccount.google.com/lesssecureapps?pli=1) after you are signed into the gmail account, downgrade to less secure
2. **Couldinary URL**
  - [create an account](https://cloudinary.com/)
  - go to the dashboard and copy your API environmental variable
   
    <img width="1230" alt="image" src="https://user-images.githubusercontent.com/23039742/213839829-b4f349b3-419d-4ea2-bbca-90cf3c663bba.png">     
 
## Fork and Clone the Repository
🚀 **merit & beyond**
To keep the main reposotory for this project clean, please fork the repostiory into your own account. GitHub has [forking directions](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) but here's what you might do:
1. login to your own gitHub account
2. navigate to [my repository](URL OF YOUR LIVE REPOSITORY)
3. In the top right corner of the page, click fork 

![image](https://user-images.githubusercontent.com/23039742/213840378-e785eaa0-712b-468c-bcda-64fde56eae44.png)

4. set yourself as the owner
5. change the name of the repo if you want
6. add a description if you want
7. choose what to copy, typicall the main branch only
8. click the snazy green button

![image](https://user-images.githubusercontent.com/23039742/213840549-5bef12ae-198e-412b-84b6-0cc718b6fa1d.png)

9. To get files to your local environment, you need to clone it: click the code button
10. Copy the url as needed (here's gitHub instructions)[https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository}



## Development Deployment 
🚨**Required** 

This section should describe the process someone would have to go through to get the local working in GitPod, or your preferred IDE. Start from installing the chrome extension then clicking the green gitpod button in THEIR FORKED repository, the enumerate the steps to walk them through the process as if they were brand new to this proccess. **Include screenshots** where applicable.

**Key points to cover** 
- Install required python packages: `pip3 install -r requirements.txt`
- Create env.py
- What to put in the env.py, don’t disclose real values
>  - EMAIL_HOST_PASSWORD=<YOUR_VALUE>
>  - DEFAULT_FROM_EMAIL=<YOUR_VALUE>
>  - EMAIL_USERNAME=<YOUR_VALUE>
>  - SECRET_KEY=<YOUR_VALUE>
>  - CLOUDINARY_URL=<YOUR_VALUE>
>  - DEV=True
- Apply Database Migrations so the database starts up `python3 manage.py migrate`
- Create a super user so you can add and inspect things via django admin  `python3 manage.py createsuperuser`
- Preload data: Sometimes you might want to include steps to create data in the admin or preload a data dump [coderwall blog](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata) has examples on how to dump data and load it which saves a bunch of time when deploying the application from a local database to a hosted database but you don’t  have to do this step
- Start the server `python3 manage.py runserver`


## Production Deployment
🚨**Required** 

This section should describe the process you went through to deploy the project to a server where anyone can access the url without your machine running. This is typically Heroku. **Include screenshots** if you think they would make the process easier. Start with getting an heroku account and then setting up databases and other packages.

If you have project settings required for Heroku, provide a table of the keys and values. Do not share your personal
keys but either cut them out of the screenshot or say <YOUR_VALUE> and include links on how the user would obtain such
values.

**Key points to cover** 
- cerating new app
- setting app name
- setting region
- entering dreaded billing info
- subscribing to a plan
- setting up db
- adding environmental values- have a list or table so user has less chance of typos
>  - EMAIL_HOST_PASSWORD
>  - DEFAULT_FROM_EMAIL
>  - EMAIL_USERNAME
>  - SECRET_KEY
>  - CLOUDINARY_URL
>  - COLLECT_STATIC
- adding build packages
- deploy
- gitHub connection
- auto vs manul deploy
- monotior logs

# Credits

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc
that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things.
Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did.

- [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
- The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

## Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

## Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site.
This includes attribution for icons if they came from font awesome or other sites, give them credit.

## Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.


