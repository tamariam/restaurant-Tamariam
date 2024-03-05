# Restaurant Tamariam 
![amIresponsive](/docs/features/amiresponsive.png)


Welcome to the Django Restaurant Reservation Site! This web application empowers users to explore our restaurant's delightful menu and seamlessly make reservations online. Built on Django, a high-level Python web framework, this project aims to provide a comprehensive solution for managing restaurant reservations while offering an exceptional user experience.
Please check live  [URL](https://tamariamrestaurant-d81c96b3d785.herokuapp.com)


# Table of Contents

- [Planning and Design](#planning-and-design)
  - [Project-Goalss](#project-goals)
  - [User Stories and Epics](#user-stories-and-epics)
  - [Wireframes](#wireframes)
  - [Database Schema](#database-schema) 
  - [Design Elements](#design-elements)
   - [Typography](#typography)
- [Features](#features)
   - [Navigation Bar](#navigation-bar) 
   - [Homepage](#homepage)
   - [Footer](#footer)
   - [Account Managament](#account-managament)
   - [Menu](#menu)
   - [Booking Page](#booking-page)
- [Deployment](#dployment)
   - [Heroku Deployment](#heroku-deployment)
   - [ElephantSQL Database](#elephantsql-database)
   - [Cloudinary API](#cloudinary-api)
   - [Forking the Repository](#forking-the-repository)
   - [Cloning The Repository](#cloning-the-repository)
- [Testing](#testing)
  - [lighthouse Testing](#lighthouse-testing)



# Planning and Design

## Project Goals

The  primary goal  of the site is to create a seamless and user-friendly reservation experience for customers and staff members. We aim to streamline the process of booking a table, making it intuitive and efficient. Users should be able to easily choose their preferred date and time, enhancing their overall dining experience. The goal is to provide users with a visually appealing and informative interface where they can explore menu items and view descriptions.For administrators, the focus is on creating a powerful reservation management system. This includes tools to view, edit, and update reservations seamlessly.

## User Stories and epics

 I developed this project applying Agile methodology. Even though it's a solo project, I followed Agile principles to learn about flexible development and delivering small improvements over time. The project reflects my commitment to understanding modern software development approaches.
In adopting an Agile development approach, i start  creating epics which were broken down into user stories, each representing a specific feature. I utilized the MoSCoW prioritization (Must have, Should have, Could have, Won't have) to categorize and prioritize each user story based on its importance.

For better planning and estimation, I assigned labels and story points to each user story, considering factors such as time and difficulty. This approach helped me gauge the relative effort required for different tasks and maintain a clear sense of priority. Also every user story includes acceptance criteria and associated tasks.

Presented below is a compilation of completed and closed user stories for this project organized by epics.

 - Epic- Setting up working enviroment
   - As a developer I can **install Django and essential libraries**,
so that I can **quickly set up a robust development environment and kickstart my web projects with confidence**..
   - As a developer, my goal is to **establish a secure environment for managing confidential configuration variables**., so that **sensitive information remains confidential, allowing me to uphold the privacy of critical data within the system**.
   - As a developer I want to **deploy the website on Heroku** so that i can **test its functionality in a live environment and make the completed site accessible to the public**.

- Epic- User Experience
   - As a **site user** I want to **navigate through landing page** so that **i can easily access various sections**
   - As a **user** I can **register my account** so that I can **log in and log out** in my account.
   - As a **user** I can **login or logout** from my account so that i **can use all features of site.**
   - As a **logged in user** I can **view my details** so that i can **review and manage my personal information.**
   - As a **logged in user** I can **change my account details** so that i can **keep my personal info up to date.**
   - As a **logged in user** I can **change my password** so that I can **keep my account secure.**
   - As a **logged in user** I can **reset my password** so that **i can still login my account if i forget my password**
   - As a **user** I can **view Menu** so that i can **check available food choices**
   - As a **logged in user** I can **book a table** so that i can **reserve place in restaurant** for a specific time.
   - As a **Logged in user** I can **view my booking details** so that i can **make sure everything is correct**.
   - As a **logged in user** I can **change my bookings** so that i can **change any details of booking** if i need.
   - As a **logged in user** I can **cancel my existing booking** so that i **do not need to call to restaurant to cancel it.**

Please check all user storys[here](https://github.com/users/tamariam/projects/9)

## Wireframes
 I used [Balsamique](https://balsamiq.com/) to create wireframes for my project.These were adapted and improved upon throughout the development process.The wireframes encompass the main pages of the project, with each page extending the base HTML structure that includes navigation and footer elements Here are the wireframes for the main pages:

 <details>
  <summary>Homepage - Desktop (click to expand)</summary>

![Homepage - Desktop](/docs/wireframes/homepage-wireframe.png)

</details>

<details>
  <summary>Homepage - Tablet (click to expand)</summary>

![Homepage - Tablet](/docs/wireframes/Homepage-Tablet.png)

</details>

<details>
  <summary>Homepage - Mobile (click to expand)</summary>

![Homepage - Mobile](/docs/wireframes/Homepage-mobile.png)

</details>


<details>
  <summary>Profile-page-wireframe (click to expand)</summary>

![profile-page](/docs/wireframes/profile-page-wireframe.png)

</details>


<details>
  <summary>Signup-Wireframe (click to expand)</summary>

![SIgnup-Wirefreame](/docs/wireframes/signup-wireframe.png)

</details>

<details>
  <summary>Login-Wireframe (click to expand)</summary>

![login-Wirefreame](/docs/wireframes/login-wireframe.png)

</details>

<details>
  <summary>Menu-Wireframe-Desktop (click to expand)</summary>

![menu-Wirefreame-desktop](/docs/wireframes/menu-wireframe-desktop.png)

</details>

<details>
  <summary>Menu-Wireframe-Mobile (click to expand)</summary>

![menu-Wirefreame-mobile](/docs/wireframes/menu-wireframe-mobile.png)

</details>

<details>
  <summary>Booking-Wireframe (click to expand)</summary>

![Booking-Wirefreame](/docs/wireframes/booking-wireframe.png)

</details>



## Database Schema

![ERD-diagram](/docs/erd-diagram/erddiagram.png)

## Design Elements

### Typography  

This project incorporates carefully selected Google Fonts to enhance the visual appeal:
"Montserrat" with sans-serif as secondary font, "Lobster "
"Dancing Script".
The mix of these  fonts contributes to a visually engaging and invitind user experience.


# Features

## Navigation Bar

The project showcases a modern and responsive navigation bar,designed with bootstrap, enhancing user experience across various devices. Key features of the navigation bar include:

- Navbar Brand:
 - A centered brand link, titled "Tamariam," serves as a clickable link to the home page, ensuring a clear and prominent identity.
Navbar Toggler:

- A responsive toggle button is incorporated for smaller screens, enabling easy access to navigation links on mobile devices.
Navigation Links:

The navigation links consist of:
Home: Users are directed to the home page, with an 'active' indicator if the current page is the home page.
Menu: Navigates to the menu section.
Book: Provides a link to the booking section.

![Navigation - Desktop](/docs/features/navigation.png)

<details>
  <summary>Navigation - Mobile (click to expand)</summary>

![Navigation - Mobile](./docs/features/navigation-mobile.png)

</details>



## Homepage
The responsive homepage starts with a captivating background image, setting the mood for a delightful dining experience.
- the homepage includes essential information about the restaurant. This ensures that visitors not only enjoy the aesthetics but also gather key details about what makes place special.
- To enhance user experience, two prominent buttons are strategically placed:

  - Menu
  - Book a Table

![Homepage-desktop](/docs/features/homepage-desktop.png)

<details>
  <summary>Homepage - Tablet (click to expand)</summary>

![Homepage - Tablet](./docs/features/homepage-tablet.png)

</details>


 <details>
  <summary>Homepage - Mobile (click to expand)</summary>

![Homepage - mobile](./docs/features/homepage-mobile.png)

</details>


## Footer

The footer of  Tamariam Restaurant website provides essential information and additional ways to connect with restaurnt staff..

![Footer-detktop](/docs/features/footer-desktop.png)

 <details>
  <summary>Footer - Tablet (click to expand)</summary>

![Footer - Tablet](./docs/features/footer-tablet.png)

</details>

 <details>
  <summary>Footer - Mobile (click to expand)</summary>

![Footer-Mobile](./docs/features/footer-mobile.png)

</details>


## Account Managment
In my project, I utilized Django Allauth to implement a user-friendly and well-designed account management system.

 - Sign Up

The signup feature allows users to create a new account on the platform. Upon signing up, users are required to verify their email address for account activation. This feature is implemented using django-allauth.


![SIgnUp](/docs/features/signup.png)


  - Upon submitting the signup form, the system sends a verification link to the user's provided email address and users are redirected to a page confirming that a verification link has been sent to their email address.


![SIgnUp](/docs/features/signup-verify-email.png)


 - Login 
   - A registered user can log in to the page by clicking on the login button in the navigation menu. The user only needs to enter their username and password.

![login](/docs/features/login.png)

 Once logged in, a message will be displayed on the page to confirm that user is logged in.
  
![login-message](/docs/features/login-alert.png)

- logout
  - When a user is already logged in, they can access the logout option in the navigation menu. Upon clicking this option, the user will be prompted to confirm if they wish to log out. If the user confirms, they will be logged out, and an appropriate message will be displayed on the page to confirm that the user has been successfully logged out.


![logaut](/docs/features/logout.png)
![logout-message](/docs/features/logout-alert.png)


### Profile page
- Profile page allows logged-in users to oversee and update their profile information and bookings conveniently.It conists with three section:
  - Greeting and Profile Overview: Users are greeted with a personalized message and provided with an overview of the profile page instructions.
  - Profile Management Area: In this section, users can update their profile details.
  - Booking Management: Users can efficiently manage their bookings, including viewing, editing, or canceling them.

![logaut](/docs/features/profile-page.png)


### Update  Profile

  - Registered users have the ability to update their profile details by selecting the appropriate option from the profile page.When a user opts to modify their account, a form pre-filled with their existing information is presented. After submitting the updated details, the user's account is successfully modified.

![update-profile](/docs/features/update-profile.png)


After the profile is updated, a relevant message will be displayed on the page.


![update-message](/docs/features/update-alert.png)

- Change password 

  - Logged-in users also have the option to change their passwords if they wish. A link to facilitate password changes is provided on the update profile page. Upon clicking the link, users will be redirected to the change password page. After entering their current password, confirming the new one, and clicking the "Change Password" button, the password will be updated, and a relevant message will be displayed.


![change-password](/docs/features/change-password.png)
![update-message](/docs/features/changepassword-alert.png) 


- Password Reset

  - The password reset feature allows users to reset their passwords in case they forget them. This feature is also implemented using django-allauth.
If a user forgets their password, they can click on the "Forgot Password" link on the login page.Upon clicking the "Forgot Password" link, the user is redirected to the password reset page.On the password reset page, the user can enter their email address associated with their account and click the "Reset Password" button.

![reset-password](/docs/features/password-reset.png)

  - Clicking on the password reset link redirects the user to a page confirming that the password reset link has been sent to their email address.

  
![reset-password-sent](/docs/features/password-reset-sent.png)

  - The user follows the instructions in the email and clicks on the password reset link.
This action redirects the user to a page where they can enter a new password and confirm it.
After successfully resetting the password from the email, the user is redirected to a page confirming that their password has been successfully reset.


![reset-password-form](/docs/features/password-reset-form.png)

![reset-password-sent](/docs/features/password-reset-done.png)


###  My  bookings
- In the 'My Bookings' section, users can view details of their existing bookings, including the status of each booking. Additionally, users have the option to update or delete their bookings as needed.

![My-Bookings](/docs/features/booking-records.png)

- When there are no bookings, the 'My Bookings' section will display an appropriate message indicating that there are no bookings currently associated with the user's account.

![No-Bookings](/docs/features/no-bookings.png)

- When a user clicks on the 'Update' button in the 'My Bookings' section, they will be redirected to the update booking page. The form on this page is identical to the booking form, with the only difference being that the booking details are prepopulated with the current booking information. Users can then make changes to these details as needed.

The update booking system operates similarly to the booking system, ensuring that users cannot make duplicate bookings. Additionally, if the restaurant is fully booked or if the requested number of guests exceeds the maximum capacity, the user will be unable to proceed with the update request, and an appropriate message will be displayed to notify the user. Clicking the cancel button on the update booking form  will navigate the user back  to the profile page.


![update-Bookings](/docs/features/update-booking.png)

- When the user clicks 'Save' on the update booking form, a message will be displayed to notify the user that the booking details have been successfully updated.

![Booking-message](/docs/features/booking-updated-message.png)

### Delete booking

-  Upon navigating to the cancellation booking page, users will see the details of their booking, including the date, time, and number of guests. A confirmation message will prompt users to confirm their decision to proceed with deleting the booking record.Clicking the cancel button will navigate the user back  to the profile page.

![delete-booking](/docs/features/delete-booking-page.png)

 <details>
  <summary>Delete-booking - Mobile (click to expand)</summary>
  
![delete-Bookings](/docs/features/delete-booking-page-mobile.png)
</details>

After confirming the deletion, a message will be displayed to notify the user that the booking record has been successfully deleted.

![booking-deleted](/docs/features/booking-deleted-message.png).


- Delete account

  - Registered users have the option to delete their accounts at any time directly from the profile page by clicking the "Delete Account" button. Upon clicking, they will receive a warning indicating that confirming deletion will result in the loss of all their data. Users can either change their minds and click "Cancel" or, if they confirm deletion, their account will be permanently deleted.


![update-message](/docs/features/delete-account.png) 
![update-message](/docs/features/delete-alert.png) 


## Menu

Menu page provides a smooth navigation experience, particularly on mobile devices. Users can easily navigate through different sections of the menu using the navigation links.
To provide real-time information to our users, the menu page dynamically adjusts the display based on item availability. If a menu item is unavailable, it's clearly indicated as "Currently Unavailable" instead of displaying the price.The menu page showcases three types of dish courses: starters, mains, and desserts. Each course is presented with its name, price, and a visually appealing image, enhancing the overall user interface.

![Menu-Desktop-1](/docs/features/menu-desktop-1.png) 

![Menu-Desktop-2](/docs/features/menu-desktop-2.png) 


<details>
  <summary>Menu - Mobile (click to expand)</summary>

![Menu -Mobile](/docs/features/menu-mobile.png)

</details>


## Booking page

Upon clicking the "Book" button in the navbar or the "Book a Table" button on the home page, users will be directed to the booking page. Here, they can make reservations using a form that allows them to select the date, time, and number of guests for their booking. After submitting the form, users will receive a feedback message confirming their reservation submission.Clicking the cancel button will navigate the user back  to the Home page.

![Booking-Desktop](/docs/features/booking-page.png) 
![loginrequire](/docs/features/booking-submited-message.png)


 <details>
  <summary>Booking-page- Mobile (click to expand)</summary>

![Booking -Mobile](/docs/features/booking-page-mobile.png)

</details>

To access the booking page, users need to be logged in to their account. If you are not logged in, they  will be redirected to the login page. Upon redirection, a message will prompt you to either log in or register if you do not have an account yet. 

![login-require](/docs/features/loginrequire-message.png)


If the restaurant is fully booked on the requested date,  message will display indicating that no reservations are available for that specific date.

 ![fully-booked](/docs/features/fully-booked-message.png)


If the user already has a booking for a specific date and time, a message will be displayed to notify them that they cannot make another booking for the same date and time.

![double-booking](/docs/features/avoid-double-bookings.png)


If there are already approved bookings for the specified date, and the number of people the user intends to book exceeds the available capacity,  the  message will display indicating that they cannot book for that date.

![request-exceeds](/docs/features/booking-request-exceeds.png)


## Dashboard Page

The Staff Dashboard is made for  staf members to manage bookings.As a staff member logging in, you're directed to the home page initially. From there, you have the option to navigate to the dashboard from the menu. Once ypu are on  dashboard page  you can  review pending, approved, and rejected bookings. Additionally,  search functionality allows you to find bookings by name, date, or quickly check today's approved bookings.. 

![request-exceeds](/docs/features/staff-dashboard-all-displayed.png)

In cases where there are no bookings att all or there are no pending, approved, or rejected bookings, the dashboard displays appropriate text on the page instead of the booking lists. This ensures clarity for staff members, indicating that there are currently no bookings requiring action or review. By providing clear feedback, staff can easily understand the current status and focus on other tasks as necessary.

![request-exceeds](/docs/features/no-bookings-att-all.png)

![request-exceeds](/docs/features/no-approved-bookings.png)

Staff members have the authority to accept or reject pending bookings directly from the dashboard. Upon accepting or rejecting a booking, an immediate message displays on the page confirming the action. Simultaneously, the booking is promptly moved to the appropriate section - either the approved or rejected bookings list. Additionally, an email notification is automatically sent to the user, informing them of the updated status of their booking.


![request-exceeds](/docs/features/booking-approved-message.png)

![request-exceeds](/docs/features/booking-rejected-message.png)



If a staff member is searching for a specific booking by date, name, or today's bookings, they are redirected to another page dedicated to displaying the specific booking details. On this page, if the requested booking is found, its details are displayed. However, if no matching booking is found, appropriate text is displayed, providing feedback that the requested booking could not be found. This ensures a streamlined experience for staff members, allowing them to quickly locate specific bookings and providing clear feedback in cases where the requested booking is not available.

 <details>
  <summary>approved-bookings-by -date(click to expand)</summary>

![approved-bookings-by-date](./docs/features/approbved-bookings-by-date.png)

</details>

 <details>
  <summary>approved-bookings-by -name(click to expand)</summary>

![approved-bookings-by-name](./docs/features/approbved-bookings-by-name.png)

</details>

 <details>
  <summary>approved-bookings-for-today(click to expand)</summary>

![approved-bookings-for-today](./docs/features/approved-bookings-for-today.png)

</details>

 <details>
  <summary>no approved-bookings-by-date(click to expand)</summary>

![no-approved-bookings-by-date](./docs/features/no-bookings-for-date.png)

</details>

 <details>
  <summary>no approved-bookings-for-name(click to expand)</summary>

![no-approved-bookings-for-name](./docs/features/no-bookings-for-name.png)

</details>

 <details>
  <summary>no approved-bookings-today(click to expand)</summary>

![no-approved-bookings-today](./docs/features/no-approved-bookings-today.png)

</details>

This project is designed to enforce specific restrictions for different user roles. Staff members are explicitly prohibited from accessing the booking page. Should a staff member attempt to navigate to the booking page by clicking on the "Book" option in the menu, an appropriate message will promptly notify them of their restricted access, preventing them from proceeding further. This tailored approach ensures that each user role has distinct permissions aligned with their responsibilities, promoting a secure and efficient system environment.

![staff-not-allow](./docs/features/staff-not%20-allow-to%20-view-booking-page.png)


# Testing 

## Lighthouse testing

Chrome DevTools Lighthouse was used to test Performance, Accessibility, Best Practices and SEO.
- Desktop  Testing with [Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse)


 <details>
  <summary>lighthouse-Testing--Home-Desktop (click to expand)</summary>

![Footer-Desktop](./docs/testing/lighthouse/dekstop-home.png)

</details>


- Mobile  Testing with [Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse)

<details>
 <summary>lighthouse-Testing-Home-Mobile (click to expand)</summary>

![Footer-Mobile](./docs/testing/lighthouse/Mobile-Homepage.png)

</details>


### Account authentication testing with lighthouse:

<details>
  <summary>lighthouse-Testing-SignUp-Desktop (click to expand)</summary>

![Signup-Desktop](./docs/testing/lighthouse/signup-desktop.png)

</details>

<details>
  <summary>lighthouse-Testing-SignUp-Mobile (click to expand)</summary>

![Signup-Mobile](./docs/testing/lighthouse/signup-mobile.png)

</details>

<details>
  <summary>lighthouse-Testing-Verification-Sent(click to expand)</summary>

![verification-sent](./docs/testing/lighthouse/verification-sent.png)

</details>

<details>
  <summary>lighthouse-Testing-Confirm-Email-mobile (click to expand)</summary>

![confirm-email-mobile](./docs/testing/lighthouse/confirm-email-mobile.png)

</details>

<details>
  <summary>lighthouse-Testing-Confirm-Email-Desktop (click to expand)</summary>

![confirm-email-desktop](./docs/testing/lighthouse/confirm-email-desktop.png)

</details>

<details>
  <summary>lighthouse-Testing-Login-Mobile (click to expand)</summary>

![Login-Mobile](./docs/testing/lighthouse/login-mobile.png)

</details>

<details>
  <summary>lighthouse-Testing-Login-Desktop (click to expand)</summary>

![Login-Desktop](./docs/testing/lighthouse/login-desktop.png)

</details>

<details>
  <summary>lighthouse-Testing-Logout-Desktop (click to expand)</summary>

![Logout-Desktop](./docs/testing/lighthouse/logout-desktop.png)

</details>

<details>
  <summary>lighthouse-Testing-Logout-Mobile (click to expand)</summary>

![Logout-Mobile](./docs/testing/lighthouse/logout-mobile.png)

</details>


<details>
 <summary>lighthouse-Testing-Pofile-page-Desktop (click to expand)</summary>

![Profile-page-Desktop](./docs/testing/lighthouse/profile-page-lh-desktop.png)

</details>

<details>
 <summary>lighthouse-Testing-Pofile-page-Mobile (click to expand)</summary>

![Profile-page-Mobile](./docs/testing/lighthouse/profile-page-lh-mobile.png)

</details>

<details>
 <summary>lighthouse-Testing-Delete-account-Desktop (click to expand)</summary>

![Delete-account-Desktop](./docs/testing/lighthouse/delete-account-lh-desktop.png)

</details>

<details>
 <summary>lighthouse-Testing-Delete-account-Mobile (click to expand)</summary>

![Delete-account-Mobile](./docs/testing/lighthouse/delete-account-lh-mobile.png)

</details>

<details>
<summary>lighthouse-Testing-Update-profile-Desktop (click to expand)</summary>

![Update-Profile-Desktop](./docs/testing/lighthouse/updateprofile-desktop.png)

</details>


<details>
  <summary>lighthouse-Testing-Update-profile-Mobile (click to expand)</summary>

![Update-Profile-Mobile](./docs/testing/lighthouse/updateprofile-mobile.png)

</details>

  

<details>
  <summary>lighthouse-Testing-Logout-Desktop (click to expand)</summary>

![Logout-Desktop](./docs/testing/lighthouse/updateprofile-desktop.png)

</details>

<details>
  <summary>lighthouse-Testing-Change-Password-Mobile (click to expand)</summary>

![Change Password-Mobile](./docs/testing/lighthouse/changepassword-mobile.png)

</details>

<details>
  <summary>lighthouse-Testing-Change-Password-Desktop (click to expand)</summary>

![Change-Password-Desktop](./docs/testing/lighthouse/changepassword-desktop.png)

</details>

<details>
  <summary>lighthouse-Testing-Password-Reset-Mobile (click to expand)</summary>

![Password-Reset-Mobile](./docs/testing/lighthouse/passwordreset-mobile.png)

</details>

<details>
  <summary>lighthouse-Testing-Password-Reset-Desktop (click to expand)</summary>

![Password-Reset-Desktop](./docs/testing/lighthouse/passwordreset-desktop.png)

</details>


<details>
  <summary>lighthouse-Testing-Password-Reset-form-mobile (click to expand)</summary>

![Password-Reset-form-mobile](./docs/testing/lighthouse/password-reset-form-mobile.png)

</details>

<details>
  <summary>lighthouse-Testing-Password-Reset-form-desktop (click to expand)</summary>

![Password-Reset-form-desktop](./docs/testing/lighthouse/password-reset-form-desktop.png)

</details>

<details>
  <summary>lighthouse-Testing-succesfully-reset-password (click to expand)</summary>

![succesfully-reset-password](./docs/testing/lighthouse/succesfully-reset-password.png)

</details>


### Menu testing with lighthouse


<details>
  <summary>lighthouse-Testing-Menu-Desktop (click to expand)</summary>

![Menu-Desktop](./docs/testing/lighthouse/menu-desktop.png)

</details>


<details>
  <summary>lighthouse-Testing-Menu-Mobile (click to expand)</summary>

![menu-mobile](./docs/testing/lighthouse/menu-mobile.png)

</details>


### Booking page testing with lighthouse

<details>
<summary>lighthouse-Testing-Booking page-Desktop (click to expand)</summary>

![Booking-page-desktop](./docs/testing/lighthouse/booking-page-lh-desktop.png)

</details>

<details>
<summary>lighthouse-Testing-Booking page-Mobile (click to expand)</summary>

![Booking-page-Mobile](./docs/testing/lighthouse/booking-page-lh-mobile.png)

</details>

<details>
<summary>lighthouse-Testing-Update-Booking-Desktop (click to expand)</summary>

![Update-booking-desktop](./docs/testing/lighthouse/update-booking-lh-desktop.png)

</details>

<details>
<summary>lighthouse-Testing-Update-Booking-Mobile (click to expand)</summary>

![Update-booking-desktop](./docs/testing/lighthouse/update-booking-lh-mobile.png)

</details>

<details>
<summary>lighthouse-Testing-Delete-Booking-Desktop (click to expand)</summary>

![Delete-booking-desktop](./docs/testing/lighthouse/delete-booking-lh-desktop.png)

</details>

<details>
<summary>lighthouse-Testing-Delete-Booking-Mobile (click to expand)</summary>

![Delete-booking-Mobile](./docs/testing/lighthouse/delete-booking-lh-Mobile.png)

</details>


## staff dashboard testing with lighthouse


<details>
<summary>lighthouse-Testing-staff-dashboard-Mobile (click to expand)</summary>

![staff-dashboard-Mobile](./docs/testing/lighthouse/dahsboard-mobile.png)

</details>

<details>
<summary>lighthouse-Testing-staff-dashboard-Desktop (click to expand)</summary>

![staff-dashboard-Desktop](./docs/testing/lighthouse/dahsboard-Desktop.png)

</details>

<summary>approved-bookings-by-date-Desktop (click to expand)</summary>

![approved-bookings-by-date-Desktop](./docs/testing/lighthouse/search-by-date-desktop.png)

</details>

<summary>approved-bookings-by-Name-Mobile (click to expand)</summary>

![approved-bookings-by-date-Desktop](./docs/testing/lighthouse/search-by-name-mobile.png)

</details>




# Deployment

## Heroku Deployment


The project was deployed using [Heroku](https://id.heroku.com/login).

After account setup, deployment steps are as follows:

1. Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
2. App name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
3.Navigate to the settings tab and click **Reveal config vars**  and add the config vars necessary for the project:
 `CLOUDINARY_URL`(insert your own Cloudinary API key here )                        
 `DATABASE_URL`           (insert your own ElephantSQL database URL ) 
 `DISABLE_COLLECTSTATIC`  1 (temporary) 
 `SECRET_KEY`             (random secret key )                                  
 
 Also make sure you create Procfile and requirements.txt file.

4. Navigate to the **Deploy** section by clicking the "Deploy" tab in the navbar, Select **GitHub** as the deployment method and click **Connect to GitHub**.
5. Find the repository wehich you want to deploy and click on **connect**.
6. Find button **Deploy Branch** at the bottom of page.
7. After clicking **Deploy Branch** button it will take few minutes to deploy site and you will have ability to view it  clicking on **view** button.


##  ElephantSQL Database


This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To set up a database, please follow these steps:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on **Create New Instance**.
3. Enter a name for the instance.(project name)
4. Select **Tiny Turtle (Free)** free plan.
5. The "Tags" field can be left blank.
6. Click **Select Region**.
7. Select a data center near you.
8. Click **Review**, make sure that all details are correct and then click "Create instance".
9.Once created, click on the new database name, where you can view the database URL and Password.


## Cloudinary Api


[Cloudinary](https://cloudinary.com/) is used in this project to store media assets. 


Follow these steps to  create Cloudinary Api Key :


1. Login/sign up to Cloudinary.
2.On your Cloudinary  dashboard to view the **API Environment Variable**.




### Cloning the Repository

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/tamariam/restaurant-Tamariam)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
  `git clone https://github.com/tamariam/restaurant-Tamariam`  then press Enterr.


### Forking the Repository

To create a copy of the repository for viewing and editing without affecting the original repository you can fork the repository through the following steps:

1. In my repository[github repository](https://github.com/tamariam/restaurant-Tamariam) click on the "fork" tab in the top right corner.
2. Then click **create fork**  and it will fork the repository in your github account.
