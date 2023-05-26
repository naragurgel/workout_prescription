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

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/43bf6ce1-ceed-48e4-a9b7-37d44b2303f7)

### Typography

-  typography has intuitive layout contribute to a clarity and ease of use throughout the website.
Montserrat-  Its clear letterforms and excellent readability make it suitable for important information and instructions related to workout plans. 
Roboto Condensed-  It is a condensed sans-serif font that offers a balance between professionalism and legibility. 

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/77e4bf28-36bb-4745-b160-f34d25200877)

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
> - icons
> - tables

### Frameworks

- Bootstrap: Firtly I opted to utilize Bootstrap for my website due to the desigh elements that they support, they also give a design that adapts to various devices. The ready-made templates and components provided invaluable time-saving advantages.

### Custom Styles

- I made some changes to the fonts, font sizes and colors of the fonts and background. It's all in the folder prescriptions/static/css/wp_styles.css

### Custom Javascript

- I made time duration of the alert message using JavaScript. It's in the folder prescriptions/templates/base.html

## Wireframes

- Desktop view unauthenticated user

![Desktop Unau](https://github.com/naragurgel/workout_prescription/assets/112726044/4e2a7e32-75cf-4fe8-8f2e-24a4bf6c1d30)

- Destop view authenticated user 

![Desk aut](https://github.com/naragurgel/workout_prescription/assets/112726044/c054c9ed-72be-48ff-a39d-5a1e9c8d6c53)

- Destop staff member logged 

![staff desk](https://github.com/naragurgel/workout_prescription/assets/112726044/f57eda13-b96c-4b8b-8133-5e6e3e375f9f)

- Mobile view unauthenticated user

![mobile un](https://github.com/naragurgel/workout_prescription/assets/112726044/bc254ae9-18d8-4c5a-aef0-f1e7c63b18ed)

- Mobile view authenticated user 

![mobile aut](https://github.com/naragurgel/workout_prescription/assets/112726044/109931b9-da95-45f4-9264-4e20de373d17)

- Staff member logged 

![mobile staff](https://github.com/naragurgel/workout_prescription/assets/112726044/df2100c7-b763-4d95-afca-f80c2343c913)

# Information Architecture
Workout prescription uses Django All Auth for user and roles management and has three custom models used to present workouts to users: 

- Exercise
- WorkoutItem
- Workout


## Entity Relationship Diagram

- User:

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/190690d0-4ce3-4f85-a13c-46e74989b0f6)

- Admin:

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/cd528559-4122-4c39-a9cf-6a6e8b476eba)

## Database Choice

Postgres because of the hosting capabilities of Heroku enables effortless deployment and expandability, and PostgreSQL stands out as one of the endorsed and suggested databases on the Heroku platform.

## Data Models

**Exercise model:**

- **name:** CharField with a maximum length of 200 characters. It represents the name of the exercise.

- [x] **Create**: If a staff user is logged in, they will see a menu option to add an exercise
- [x] **Read**: If a staff users is logged in, they can see exercises in the system on the Exercise List Page
- [x] **Update**: If a staff user is logged in, they will an option to update an exercise on the Exercises List Page
- [x] **Delete**: If a staff user is logged in, they will see an option to delete an exercise on the Exercises List Page.

ExerciseAdmin: This admin configuration is registered for the Exercise model so it can be touched in the Django admin by staff users too.

search_fields: It specifies that the name field should be searchable in the admin interface.

**WorkoutItem model:**

- **exercise:** ForeignKey to the Exercise model, with on_delete=models.CASCADE specified. It represents the exercise associated with the workout item.
- **reps:** PositiveIntegerField, representing the number of repetitions for the workout item.
- **sets:** PositiveIntegerField, representing the number of sets for the workout item.

- [x] **Create**: If a staff user is logged in, they will see a menu option to add an Item
- [x] **Read**: If a staff users is logged in, they can see Workout Items in the system on the Workout Items List Page
- [x] **Update**: If a staff user is logged in, they will an option to update an item on the Workout Items List Page
- [x] **Delete**: If a staff user is logged in, they will see an option to delete an item on the Workout Items List Page.

WorkoutItemAdmin: This admin configuration is registered for the WorkoutItem model, so staff users can interface with the model in the Django admin too.

search_fields: It specifies that the exercise field should be searchable in the admin interface.

**Workout model:**
- **owner:** ForeignKey to the built-in User model from django.contrib.auth.models, with related_name="user_id" and on_delete=models.CASCADE specified. It represents the owner of the workout.
- **name:** CharField with a maximum length of 250 characters. It represents the name of the workout.
- **instructions:** TextField with a maximum length of 1000 characters, allowing null values and blank values. It represents the instructions for the workout (optional).
- **exercises:** ManyToManyField to the WorkoutItem model. It represents the exercises included in the workout.

- [ ] **Create**: Creating workouts can only be done in the django admin at this time
- [x] **Read**: If a user is logged in, they will see workouts associated with their account on the Workout List page. They can also click on it to see a detailed view. Staff users will see a list of all workouts in the system.
- [ ] **Update**: Updating workouts can only be done in the django admin at this time.
- [x] **Delete**: Deleting workouts can only be done in the django admin at this time.


WorkoutAdmin: This admin configuration is registered for the Workout model so that staff users can do the Create, Update and Delete of workouts through the django admin interface.

list_display: It specifies that the admin interface should display the owner and name fields in the list view.
search_fields: It specifies that the name and owner fields should be searchable in the admin interface.
ordering: It specifies that the list of workouts should be ordered by the owner field.
## Entity Relationship Diagram

- User:

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/190690d0-4ce3-4f85-a13c-46e74989b0f6)

- Admin:

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/cd528559-4122-4c39-a9cf-6a6e8b476eba)

## Database Choice

Postgres because of the hosting capabilities of Heroku enables effortless deployment and expandability, and PostgreSQL stands out as one of the endorsed and suggested databases on the Heroku platform.

## Data Models

- Exercise Model

Fields:

name: CharField to store the name of the exercise.
Validation:

name is required and should be unique.
CRUD Operations:

Create: Admin can create a new exercise by providing a unique name.
Read: Admin can view the list of exercises.
Update: Admin can update the name of an existing exercise.
Delete: Admin can delete an exercise.

- Workout Model:

Fields:

owner: ForeignKey to link the workout to the admin user who owns it.
name: CharField to store the name of the workout.
Validation:

owner is required and linked to a valid admin user.
name is required and should be unique.

CRUD Operations:

Create: Admin can create a new workout by providing an owner and a unique name.
Read: Admin can view the list of workouts.
Update: Admin can update the owner or name of an existing workout.
Delete: Admin can delete a workout.

- Workout Item Model:

Fields:

workout: ForeignKey to link the workout item to the parent workout.
exercise: ForeignKey to link the workout item to the exercise.
reps: PositiveIntegerField to store the number of repetitions.
sets: PositiveIntegerField to store the number of sets.
Validation:

workout is required and linked to a valid workout.
exercise is required and linked to a valid exercise.
reps and sets should be positive integers.
CRUD Operations:

Create: Admin can create a new workout item by providing a workout, exercise, reps, and sets.
Read: Admin can view the list of workout items.
Update: Admin can update the workout, exercise, reps, or sets of an existing workout item.
Delete: Admin can delete a workout item.

 **Activities Model**

CRUD Operations:
Create: Create a exercise or a workout list to each user.

Read: The workout sheet is visibl on the workout list page and the user can have acess to his own workout by acessing the website.

Update: The workout can be updated when the staff menber wants to change anything on the prescription.

Delete: The workout or exercice can be deleted if a staff menber wants to change the workout prescriptions.

## CRUD Diagrams

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/523311dd-d57d-440a-ae0e-5cfc6769ec45)

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
- As a trainer, I want to delete a workout, so I can remove it from my list of saved workouts if it's no longer relevant.

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

In order to define a prioritized list of user stories for an minimal viable product based on the project goals, some scope reduction was performed to focus on the essential features within the available skill set. The main objective was to deliver a basic but functional version of the workout website. The prioritized user stories include functionalities such as viewing a list of exercises and workouts, creating new workouts, and searching for workouts by name. Additionally, the ability to create exercises and search for exercises by name were included. These core features were deemed essential to provide users with a basic experience of browsing on the workouts, while allowing the admin to manage exercises list. 

## Agile Tool

### User Story Example

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/b7f40e9a-aaa2-4b04-9595-adeed4aa97fc)

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

## Home Page (Visitor)

![Screenshare - 2023-05-24 4_44_14 PM](https://github.com/naragurgel/workout_prescription/assets/112726044/7e46eb8e-48e3-4fcc-ba50-d6583e4c25ea)

## Workout Page (Visitor)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/647a80c3-8bff-45ff-b2a4-9103cdac5e8c)

## Logged (Staff member)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/acb2ca41-5515-41e1-b7f6-93e75ab81855)

## Exercise List (Staff member)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/e910667b-2942-4046-83c5-5c155f6475a2)

## Add Exercise (Staff member)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/68b57d85-2beb-4275-8e0b-bb55aab092d9)

## Workout Item List (Staff member)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/6edd3b39-80bd-43dc-a668-9766c77c6604)

## Add Item (Staff member)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/6203f17b-4d99-4a39-b181-6700b0db3acf)

## Workout List (Staff member)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/c534c11d-51b1-459d-b8fe-1aaa3070c3a2)

## Workout (Registered user)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/18aec634-f8c7-462d-bd9e-e9a52a379436)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/92bd717a-c2f4-4fb2-9884-7be4751be75b)

## Sign in

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/d8a643f9-e9e6-4cc1-89b5-f8d4ba755798)

## Sign out

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/dde9697a-93c0-453a-8d53-9b83fb127166)

## Sign up

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/7fce0c50-eb3c-407a-98a0-f1766150c868)

## Implemented Features

### Header

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/7dbd466c-cbd3-4607-8677-615a7f1219f7)

### Footer

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/9116e6ee-11da-4728-87d1-b9f6bfc238e3)

### Main

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/fb7ff41a-86ba-4f2f-9e8c-430cdd20fce3)

### 404 error page

![404](https://github.com/naragurgel/workout_prescription/assets/112726044/9fb151df-2ff6-4091-a0a4-71fcfb66a497)

### 500 error page

![500](https://github.com/naragurgel/workout_prescription/assets/112726044/b5baf41b-0131-4aed-9185-2b6ad9a98e0b)

## unauthenticated

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/82b7e0a0-7087-4e06-8dcf-27180adb56f9)

###  general authenticated user

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/73aa2d43-5dd3-4f6e-95c9-00e585e8cb10)

### superuser authenticated -  The admin/superuser have full access to CRUD functionality.

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/d4aa1a61-06cf-47bf-aaec-d1f6f3e3ae50)

### not allowing users to create, read, update and delete information they shouldn't

There is no option to change the workout prescription for a regular user:

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/776329a1-b91f-44b0-9bb1-20e2b3f35097)

## Messages Display

### Confirmation messages

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/2631b655-8454-4823-8ccd-4c5cef12a836)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/c8014723-923b-4cc8-ab4a-8987a965b8f3)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/96c73504-5414-4a02-9198-3b76c6d86f36)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/26b8f51a-acec-45f5-b722-566c1cd87451)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/c1d88822-f45c-4814-80ed-46f6c058a60d)

### validation of form inputs

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/bf4eec54-eb73-4214-8f6e-57aaa3d53563)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/9d8716de-16dc-42b9-8a47-869174f04ef6)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/0d326d75-f9c0-4443-a779-f31d99971721)

### Sign Out/ Delete confirmations questions 

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/75968d48-290c-475e-acc8-99e2d00f98e3)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/e66b752f-b730-4c3a-9982-3c0bf8fb0ae4)

## Future Features

- Some options ready for workout sheet prescriptions 
- Videos for the user watch, theaching how to do the exercise corretly

## Testing

I have carried out the manual testing in order to guarantee the effectiveness and user-friendliness of the Workout Prescriptions website. To access the comprehensive testing results, kindly click on the provided link [here](https://github.com/naragurgel/workout_prescription/issues?q=is%3Aissue+is%3Aopen+label%3ATest_case).

## Manual Testing

**Manual Testing**

## Unauthenticated User
  1. Does not see staff options in navigation
  2. Does not see Logout options in navigation
  3. Cannot use a bookmark to add exercise
  4. Can not use a bookmark to update exercise
  5. Can not use a bookmark to delete exercise
  6. Can not use a bookmark to add WorkoutItem
  7. Can not use a bookmark to update WorkoutItem
  8. Can not use a bookmark to delete WorkoutItem
  9. Can not use a bookmark to see Workout List
  10. Can not use a bookmark to see a Workout Detail
  11. Can not use a bookmark for anything in Django Admin
  12. When not logged in, clicking on workout gives buttons to login/register
  13. Using a bookmark to logout page does nothing
  14. Click login takes user to login page
  15. Click signup takes user to registration page

## Footer 
  1. Footer link Twitter opens new tab
  2. Footer link Instagram opens new tab
  3. Footer link Facebok opnes new tab

## Sign Up
  1. All blanks & submit: user sees error to fill out username
  2. Fill out user name, rest blank & submit: user sees error to fill out password
  3. Valid form, username in system & submit: user sees error that the username is already registered
  4. Valid form, email in system & submit: user sees error that the email is already registered
  5. Valid form, passwords don't match: user sees error that passwords need to match
  6. Valid form, 'test' for password & submit: user sees error that password is too short
  7. Valid form, 'testtest' for password & submit: user sees error that password is too common
  8. Success full registration: user is taken to homepage, sees success message about logging in for about 3 seconds

## Login
  1. All blanks & submit: user sees error to fill out username
  2. Fill out user name, rest blank & submit: user sees error to fill out password
  3. Valid form, username not in system & submit: user sees error that the username is not registered
  4. Valid form, email not system & submit: user sees error that the email is not registered
  5. Valid form, passwords incorrect: user sees error that passwords is incorrect
  6. Success authentication: user is taken to homepage, sees success message about logging in for about 3 seconds

## Regular User Logged In
  1. Can not use a bookmark to add exercise
  2. Can not use a bookmark to update exercise
  3. Can not use a bookmark to delete exercise
  4. Can not use a bookmark to add WorkoutItem
  5. Can not use a bookmark to update WorkoutItem
  6. Can not use a bookmark to delete WorkoutItem
  7. Can not use a bookmark to see Workout List
  8. Can not use a bookmark to see a Workout Detail they don't own
  9. Can not use a bookmark to access django admin
  10. Does not see Sign Up in navigation
  11. Does not see Login in navigation
  12. Workout page shows special message to contact trainer if no workouts
  13. Workout page shows list of workouts for them if they have 1 or more
  14. Workout page with workouts links to workout details page
  15. Workout page doesn't have update and delete options
  16. Can use a bookmark to see a workout they own

## Staff User Logged In
  1. Can use a bookmark to add exercise
  2. Can use a bookmark to update exercise
  3. Can use a bookmark to delete exercise
  4. Can use a bookmark to add WorkoutItem
  5. Can use a bookmark to update WorkoutItem
  6. Can use a bookmark to delete WorkoutItem
  7. Can use a bookmark to see Workout List
  8. Can use a bookmark to see a Workout Detail they don't own
  9. Can use a bookmark to access django admin
  10. Sees Exercise List nav option
  11. Sees Add Exercise nav option
  12. Sees workout items list nav option
  13. Sees add item nav option
  14. Sees workout list option
  15. Sees logout option
  16. Upon logging in, sees message that they signed in and is on home page

## Sign out
  1. Clicking signout button on signout page logs user out & shows green message
  2. Menu options change to logged out state

## Exercise list Page
User is logged in as staff
  1. User sees list of exercises with delete and update options
  2. Click delete, deletes appropriate exercise
  3. Click update, takes user to appropriate update

## Add Exercise
User is logged in as staff
  1. Can use a bookmark to add exercise
  2. All blanks & submit: user sees error to fill out the input
  3. Submit a duplicate name: user sees error, the name must be unique 

## Workout Item list
User is logged in as staff
  1. User sees list of Workout Item with delete and update options
  2. User sees how many repetions and sets for each exercise 
  2. Click delete, deletes appropriate exercise
  3. Click update, takes user to appropriate update

## Add Exercise
User is logged in as staff
  1. Can use a bookmark to add details like sets and reps do the workout items
  2. User can see a dropdown with the exercises options added
  3. All blanks & submit: user sees error to fill out the input

## Workout List
User is logged in as staff
  1. User can sees the list of workout prescriptions and the owners 
  2. Can delete any ite from the list
  3. Can click on it and see the details like, sets, reps and instructions

## 404

## 500

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

-HTML, CSS, JAVASCRIPT, PYTHON,  DJANGO

## Frameworks, Libraries & Programs Used

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


