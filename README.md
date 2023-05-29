# Workout_Prescription

- This is a website that offers a variety of fitness programs to help you achieve your health and fitness goals. Whether you're looking to lose weight, build muscle, or simply improve your overall health. The trainers create personalized training programs tailored to your individual needs and goals.
- The user can access a personalized workout plan from anywhere with an internet connection, at any time that suits the schedule.

## Live Site 

- [Heroku](https://workout-prescriptions.herokuapp.com/)

## Repository

- [Github](https://github.com/naragurgel/workout_prescription)

## Author

Nara Gurgel

# Table of Contents

# Table of contents

- [UX](#ux)
  - [Target Audience](#target-audience)
  - [Design Choices](#design-choices)
  - [Wireframes](#wireframes)
- [Information Architecture](#information-architecture)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Choice](#database-choice)
  - [Data Models](#data-models)
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
- [Features](#features)
  - [Home Page (Visitor)](#home-page-visitor)
  - [Workout Page (Visitor)](#workout-page-visitor)
  - [Logged (Staff member)](#logged-staff-member)
  - [Exercise List (Staff member)](#exercise-list-staff-member)
  - [Add Exercise (Staff member)](#add-exercise-staff-member)
  - [Workout Item List (Staff member)](#workout-item-list-staff-member)
  - [Add Item (Staff member)](#add-item-staff-member)
  - [Workout List (Staff member)](#workout-list-staff-member)
  - [Workout (Registered user)](#workout-registered-user)
  - [Sign in](#sign-in)
  - [Sign out](#sign-out)
  - [Sign up](#sign-up)
  - [Implemented Features](#implemented-features)
  - [Unauthenticated user](#unauthenticated-user)
  - [Messages Display](#messages-display)
  - [Future Features](#future-features)
  - [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Unauthenticated User](#unauthenticated-user)
  - [Footer](#footer)
  - [Sign Up](#sign-up)
  - [Login](#login)
  - [Regular User Logged In](#regular-user-logged-in)
  - [Staff User Logged In](#staff-user-logged-in)
  - [Sign out](#sign-out)
  - [Exercise list Page](#exercise-list-page)
  - [Add Exercise](#add-exercise)
  - [Workout Item list](#workout-item-list)
  - [Add Exercise](#add-exercise)
  - [Workout List](#workout-list)
  - [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Validation Testing](#validation-testing)
  - [Defects](#defects)
  - [Defects of Note](#defects-of-note)
  - [Outstanding Defects](#outstanding-defects)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Deployment](#deployment)
  - [Fork and Clone the Repository](#fork-and-clone-the-repository)
- [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)
  
# UX

## Target Audience

- The Workout prescriptions page is designed for both men and women of various age groups who are interested in maintaining a healthy and active lifestyle. These users are typically health-conscious, fitness enthusiasts, and may have specific interests such as weight loss, muscle building, or overall well-being.

## Design Choices

 - The website will prioritize intuitive navigation and clear communication of workout instructions. The simplicity of the design ensures a user-friendly interface, allowing users to easily navigate and engage with their workout plans without distractions.

### Colors

- Color scheme predominantly consisting of tons of black, green and white. The use of black provides a sense of professionalism, green refreshing and energetic touch, symbolizing growth and vitality, aligning with the health and wellness focus of the website. White is promoting a visually calming experience. 

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/112e6367-cb1a-4b05-ae5c-b7704753d51c)

### Typography

-  The typography has intuitive layout contribute to a clarity and ease of use throughout the website.
Montserrat-  Its clear letterforms and excellent readability make it suitable for important information and instructions related to workout plans. 
Roboto Condensed-  It is a condensed sans-serif font that offers a balance between professionalism and legibility. 

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/77e4bf28-36bb-4745-b160-f34d25200877)

### Images

The reason for the cover photo to be dumbbells is mainly because dumbbells are an iconic symbol of strength training and fitness, which is the website's focus. The photo of dumbbells creates an immediate visual association with exercise, motivating and inspiring users to engage in their prescribed workouts and pursue a healthier lifestyle.

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
> - Dropdown

### Frameworks

- Bootstrap: I opted to utilize Bootstrap for my website due to the design elements that it supports. It also has a design that adapts to various devices. The ready-made templates and components provided invaluable time-saving advantages.

### Custom Styles

- I made some changes to the fonts, font sizes and colors of the fonts and background. It's all in the folder **[CSS](prescriptions/static/css/wp_styles.css)**

### Custom Javascript

- I made time duration of the alert message using JavaScript. It's in the folder **[Base](prescriptions/templates/base.html)**

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

 **Activities Model**

CRUD Operations:
Create: Create a exercise or a workout list to each user.

Read: The workout sheet is visible on the workout list page and the user can have acess to his own workout by acessing the website.

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

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/c841b5fb-03da-4fe0-80ea-8b494ce11346)

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

- On the homepage of the Workout Prescription website, you will be able to visualize the welcome message and the hero image. You will also see the buttons to login or sign up. 

![ezgif com-crop](https://github.com/naragurgel/workout_prescription/assets/112726044/b29efdb8-b525-4c78-afe0-eeff96d3bc97)

## Workout Page (Visitor)

- There is a section for Workout but to actually see the workouts, you must be registered.

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/c9510c32-2572-452d-8f9f-a90798537fbe)

## Logged (Staff member)

- If you log in as a staff member, you will be able to see sections like 'Exercises List", "Add Exercise", "Workout Item List", "Add Item" and "Workout List". There is a button to logout.

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/4165f3c3-f110-4cea-b6d5-612138231334)

## Exercise List (Staff member)

- Where you can find the list of exercises added, which you can delete and update.

Desktop:
![image](https://github.com/naragurgel/workout_prescription/assets/112726044/e910667b-2942-4046-83c5-5c155f6475a2)

Mobile:
![image](https://github.com/naragurgel/workout_prescription/assets/112726044/989cd904-7bf6-4d13-b55f-148f9be413d3)

## Add Exercise (Staff member)

- Where you can add an item to the list of exercices. 

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/60a8be4d-dff3-4f03-8be3-86d71ee62756)

## Workout Item List (Staff member)

- Where you can find the list of exercises added, with details like how many reps and sets, you also can delete and update.

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/1ace676d-cce3-4445-9f75-97f8622ded25)

## Add Item (Staff member)

- Where you can add details to the exercices added before. 

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/332d436f-bfd8-4c58-bb4b-b3a3a10b5ce7)

## Workout List (Staff member)

- You will be able to see the list of workout sheets, with names and owners; if you click on it, you will be redirected to the details of the workout (it's the same page as the workout registered user below)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/3c79217e-fd60-488a-bc6d-f5869d3a903b)

## Workout (Registered user)

- The user can access the workout sheet if the user is registered. Clicking on the workout name they will be redirected to the workout details. 

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/3a7c59a2-12d8-4d25-a391-92ea2a4bd327)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/d1685a30-23ef-4760-983e-885ae86c9390)

## Sign in

- Where the user can be authenticated and have access to their account.

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/684628a3-23e2-4fc2-90d3-210f8923da37)

## Sign out

- Sign out of the account.

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/fca6f33f-7d05-440f-8c89-5b237c405d24)

## Sign up

-Where the visitor could sign up to get prescriptions.

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/46882d83-4e5f-4e5f-a59e-14486eeb9cb5)

## Implemented Features

### Header

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/0a9aa61a-500e-4b50-89d4-3e791a051771)

### Footer

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/f9a16891-1b6c-423a-99b8-5e8a8041091d)

### Main

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/4028cbf0-55e0-4a81-8935-2f8979095a6a)

### 404 error page

![404](https://github.com/naragurgel/workout_prescription/assets/112726044/2c08f2d2-d55e-4701-bd85-3f71f4576cfa)

### 500 error page

![500](https://github.com/naragurgel/workout_prescription/assets/112726044/b1126c5c-20bc-449a-be7f-af83bdf2e63a)

### 403 error page

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/0ab310b5-4f4d-425b-8144-2e3eaa9d9400)

## Unauthenticated user

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/77cc25ed-026c-489f-87a3-36961a8cfa9d)

### Superuser authenticated -  The admin/superuser have full access to CRUD functionality.

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/d4aa1a61-06cf-47bf-aaec-d1f6f3e3ae50)

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

## Compatibility and Responsive Testing

| Tool/Device    | Browser | OS          | Viewport       |
|----------------|---------|-------------|----------------|
| Iphone 13      | Safari  | V16.3       |  390 x 664 px  |
| Iphone 12      | Safari  | V14.1       |  390 x 664 px  |
| OnePlus        | Chrome  | v9.0        |   412 x 757 px |
| Samsung Galaxy | Firefox | v12.0       |   384 x 702 px |
| Google Pixel   | Chrome  | v13.0       |   412 x 796 px |
| Ipad Pro       | Safari  | v16.2       | 1024 x 1292 px |
| Windows PC     | Edge    | Windowns 11 | 1336 x 667 px  |
| Mac PC         | Safari  | Safari 15.6 | 1336 x 667 px  |
| Windows PC     | Chrome  | Chrome      | 1336 x 667 px  |

## Accessibility Testing

### Accessibility Audits

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/28a8614e-11e6-4a5a-b254-5eb562c077a9)

## Validation Testing
### CSS Validation
[**Style.css](https://github.com/naragurgel/workout_prescription/blob/main/static/css/wp_styles.css)**

![CSS](https://github.com/naragurgel/workout_prescription/assets/112726044/ea788cc7-7d9c-488d-bdbd-32ab1c42a394)

### HTML Validation

**[Home page](https://github.com/naragurgel/workout_prescription/blob/main/templates/index.html)**

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/fe321ffd-d2a8-437a-8e9e-c43e3d171a4a)

**[Workout page](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/templates/workout/list.html)**

![workout sheet](https://github.com/naragurgel/workout_prescription/assets/112726044/aba7bd52-8838-49ec-b275-b73197eae038)

**[Confirm delete](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/templates/workout/confirm_delete.html)**

![confirm delete](https://github.com/naragurgel/workout_prescription/assets/112726044/2bc7e15a-d619-476c-a708-20f3663ce731)

**[Exercices](https://github.com/naragurgel/workout_prescription/tree/main/prescriptions/templates/exercise)**

![exerci list](https://github.com/naragurgel/workout_prescription/assets/112726044/aa1edf63-47e9-4d25-891c-f14ebd0e1d8d)

**[Workout Item](https://github.com/naragurgel/workout_prescription/tree/main/prescriptions/templates/workout_item)**

![workoutitemlist](https://github.com/naragurgel/workout_prescription/assets/112726044/43d6af9a-e92d-4cc6-a44e-3b20dcc9a295)

**[Workout admin](https://github.com/naragurgel/workout_prescription/tree/main/prescriptions/templates/workout)**

![workout sheet](https://github.com/naragurgel/workout_prescription/assets/112726044/0603434f-89a0-48e2-9e41-1540c187dbf5)

### JavaScript Validation

**[Home page](https://github.com/naragurgel/workout_prescription/blob/main/templates/base.html)**

![JS](https://github.com/naragurgel/workout_prescription/assets/112726044/7d64769a-fe03-4884-b365-63b2aabecd8c)

### Python Validation

**[Exercise](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/views/exercise.py)**

![models exerc](https://github.com/naragurgel/workout_prescription/assets/112726044/dca4f5ac-d5e7-4a0a-9bcc-ee7fe448da92)

**[Homepage](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/views/homepage.py)**

![models homepage](https://github.com/naragurgel/workout_prescription/assets/112726044/179524cc-7ec4-410d-97d4-cecf858b7398)

**[Workout Item](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/views/workout_item.py)**

![models workout item](https://github.com/naragurgel/workout_prescription/assets/112726044/b2f220e3-4e5f-4a7b-ac3b-d5e0afd83f33)

**[Workout](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/views/workout.py)**

![models workout](https://github.com/naragurgel/workout_prescription/assets/112726044/00a4b5f8-1b01-4d75-9545-2d8b946c2b3d)

**[Admin](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/admin.py)**

![admin py](https://github.com/naragurgel/workout_prescription/assets/112726044/16cb1dc3-2d88-4aab-bc58-32190ef8c532)

**[Apps](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/apps.py)**

![apps py](https://github.com/naragurgel/workout_prescription/assets/112726044/a26bde14-6b81-4488-9d3d-b0af40ac79f8)

**[Forms](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/forms.py)**

![forms py](https://github.com/naragurgel/workout_prescription/assets/112726044/49c3d096-7597-4020-8696-407d49015417)

**[Models](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/models.py)**

![models py](https://github.com/naragurgel/workout_prescription/assets/112726044/2ee8ce68-62c8-4aac-98b2-66e8232a3b79)

**[URL's](https://github.com/naragurgel/workout_prescription/blob/main/prescriptions/urls.py)**

![url py](https://github.com/naragurgel/workout_prescription/assets/112726044/eb976e82-4674-4400-8247-cef5ab3cecfe)

![image](https://github.com/naragurgel/workout_prescription/assets/112726044/eeec32e5-ce68-445b-981a-004a49203366)

**[Settings](https://github.com/naragurgel/workout_prescription/blob/main/workout_prescription/settings.py)**

![settings py](https://github.com/naragurgel/workout_prescription/assets/112726044/61ddf30c-5f3b-4bf9-9e1e-b328a58dbda8)

**[wsgi](https://github.com/naragurgel/workout_prescription/blob/main/workout_prescription/wsgi.py)**

![wsgi py](https://github.com/naragurgel/workout_prescription/assets/112726044/3bd77af3-f84a-49aa-a6ff-aff33ad3f558)

**[Manage](https://github.com/naragurgel/workout_prescription/blob/main/manage.py)**

![manage py](https://github.com/naragurgel/workout_prescription/assets/112726044/95a43622-e7cc-4c8a-95d5-a7864c60efb9)

## Defects
I've made **[miletones](https://github.com/naragurgel/workout_prescription/milestones)** to group all the defects and make them easier to been finded.

## Defects of Note

You can find the defects I had and the full description on the link below:

- **[Footer:](https://github.com/naragurgel/workout_prescription/issues/29)**
The footer was moving up and down accordingly with the page content.

- **[Style:](https://github.com/naragurgel/workout_prescription/issues/30)**
The Heroku was not deploying the CSS file.

- **[Sign up:](https://github.com/naragurgel/workout_prescription/issues/31)**
When a new user was tying the email and submitting the page was showing a error

## Outstanding Defects


# Technologies Used

| JavaScript               | JavaScript played a vital role in providing dynamic interactivity to the messages.                                                                                          |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Python                   | Python is a versatile programming language that was extensively utilized to write all the code in the application.                                                          |
| Django                   | Django is a powerful Python web framework used for efficient development, handling database interactions, and implementing secure authentication in the project.            |
| PostgreSQL               | PostgreSQL was utilized to store and manage the project's data efficiently.                                                                                                 |
| Bootstrap                | Bootstrap was employed to ensure a responsive design, making the website adapt seamlessly to different screen sizes and devices.                                            |
| Font Awesome             | Font Awesome was utilized to enhance the overall design of the website by providing a collection of icons that could be easily integrated.                                  |
| GitHub                   | GitHub served as the primary development environment, facilitating code management and effective tracking of changes made to the project.                                   |
| Heroku                   | Heroku was utilized as the deployment platform for the website, making it accessible to users over the internet.                                                            |
| Google Developer Tools   | Google Developer Tools, specifically DevTools, played a crucial role in bug detection, testing the website's responsiveness, and resolving issues across different devices. |
| Jigsaw                   | Jigsaw was utilized to validate CSS code, ensuring its compliance with the specified standards and best practices.                                                          |
| CI's pep8                | CI's pep8 tool was used to validate all Python code, ensuring adherence to coding standards and maintaining consistency throughout the project.                             |
| Coloors                  | Coloors was utilized as a tool to generate a color palette for the website design.                                                                                          |
| W3 HTML                  | W3 HTML to validate the HTML code, ensuring its correctness and compliance with web standards.                                                                              |
| Jshint                   | Jshint was used to validate JavaScript code, ensuring its quality, identifying potential errors, and promoting best practices.                                              |
| Cloudinary               | Cloudinary was utilized as a cloud-based storage service to store and manage all static files and images used in the project.                                               |
| Mermaid                  | Mermaid was used to create diagrams, providing a visual representation of various aspects of the project's architecture and workflow.                                       |
| Gitpod                   | Gitpod provided an online development environment.                                                                                                                          |
| Markdown Table Generator | Markdown Table Generator was utilized as a tool to create tables in Markdown format, simplifying the process of generating well-formatted tables.                           |
| AmIResponsive            | AmIResponsive was used to generate screenshots of the website in various device sizes, providing a quick visual assessment of its responsiveness and compatibility.         |
| Balsamiq                 | Balsamiq served as a wireframing tool, enabling the creation of visual representations of the website layout and structure, aiding in the design process.                   |
| Lighthouse               | Lighthouse, a web performance testing tool, was used to assess the accessibility and performance of the website.                                                            |

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
### Prerequisites
To run this project, you need a CLOUDINARY_URL:
1. **Cloudinary Account:**
- Create an account on [Cloudinary](https://cloudinary.com/users/register_by_email) if you don't have one.
- Access the Cloudinary dashboard.
2. **Obtain API Key and Secret URL:**
- In the Cloudinary dashboard, navigate to your account settings.
- Look for the section related to API credentials or environments variable.
- Locate the API Key and Secret URL.
- Copy the API Key and Secret URL, as you will need them to configure the application.
3. **Set Environmental Variables:**
- Once you have obtained the API Key and Secret URL, you need to set them as environmental variables in your development environment.
- Depending on your operating system and development environment, the steps to set environmental variable may vary.

### Forking the Github Repository

To make a copy or ‘fork’ the repository:

1. Login to your own GitHub account
2. Navigate to [my repository](https://github.com/naragurgel/workout_prescription)
3. In the top right corner of the page, click 'fork' option to create and copy of the original

### Making a Local Clone

1. Under the repository name, click on the ‘code’ tab
2. In the clone box, HTTPS tab, click on the clipboard icon 
3. In your IED open GitBash
4. Changed the current working directory to the location you want the cloned directory to be made
5. Type ‘git clone’ and then paste the URL copied from GitHub
6. Press enter and the local clone will be created 

### Production Deployment

To get started with local development in GitPod or your preferred IDE, follow these steps:

1. Install the GitPod Chrome extension from the Chrome Web Store.
- [GitPod Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki)

2. Once the extension is installed, navigate to your forked repository on GitHub.
3. Click on the green "GitPod" button to open the repository in GitPod.
4. After the workspace is created, you can start the development process.
5. Install the Python packages by running the following command in the terminal:
- **pip3 install -r requirements.txt**
6. Create an **'env.py** file in the project's root directory to store your environment variables.
7. In the **'env.py** file, add the following variables, but make sure not to disclose real values:
- **SECRET_KEY=<YOUR_VALUE>**
- **CLOUDINARY_URL=<YOUR_VALUE>**
- **DATABASE_URL=<YOUR_VALUE>**
8. Apply databse migrations to set up the database by running the following command:
- **python3 manage.py migrate**
9. Create a superuser account that allows you add and inspect data via Django admin by running the following command:
- **python3 manage.py createsuperuser**
10. Start the server by running the following command:
- **python3 manage.py runserver**
11. Now you can access the application by opening the provided URL in your browser.

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

To keep the main reposotory for this project clean, please fork the repostiory into your own account. GitHub has [forking directions](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) but here's what you might do:
1. login to your own gitHub account
2. navigate to [my repository](https://github.com/naragurgel/workout_prescription)
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

# Credits

This workout prescription project was created with help, support, and resources from the following:

- **[Stack Overflow](https://stackoverflow.com/)**: A valuable resource for finding solutions to coding challenges and getting insights from the developer community.
- **[Pexels](https://www.pexels.com/)**: A platform that provided high-quality royalty-free images used in the project.
- **[Font Awesome](https://fontawesome.com/)**: for the variety of icons available.
- **[Bootstrap](https://getbootstrap.com/)**: For the responsive design and also great style.
- **[MDN Web Docs](https://developer.mozilla.org/en-US/)**: Another page for resource for finding solutions to coding challenges and getting insights from the developer community.
- **[Code Institute](https://learn.codeinstitute.net/)**: Platform that offered informative content, tutorials, and projects that helped in developing and structuring this workout prescription website.
- [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
- **Modules and Libraries**: Various modules and libraries were utilized throughout the development process, including Django, Mermaid, and more. These modules and libraries greatly contributed to the functionality and aesthetics of the website.

A special thanks to the mentors, tutors and fellow learners at Code Institute for their guidance and support during the project's development.

## Media

**[Pexels](https://www.pexels.com/)** - The homepage Image was taken from Pexels.
**[Font Awesome](https://fontawesome.com/)** - The icons was taken from Font Awesome.

## Acknowledgments

- Code Institute walkthrough project 'I think Therefore I blog', which was where I had the initial ideas of how to start my project.
- Mentor: Malia - Since the first project, always supporting me in the best way, helping with doubts and showing the best ways to develop the project
- Team of tutors that helped me with the bug that was not deploying to my site on heroku, they were super helpful and dedicated until we managed to find a solution.
- My friend Gustavo Chahm, who is already a senior software developer,he answered many doubts that I had, he showed me the best ways to develop the site, always explaining everything with clarity and patience

