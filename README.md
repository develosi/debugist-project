# Debugist Project

![The Debugist App shown on a variety of screen sizes](.png)

Visit the deployed site: [Debugist](https://debugist-project.herokuapp.com/) 

The Debugist App is a simple task manager tool specifically designed for the management of debugging and testing your apps and websites. 

It can be hard to keep track of what testing needs to be done for each project build and also what specific tests need to be carried per code base or package used. 

With Debugist each project can be set up by an “admin” user and then multiple members of a team can log in and add or delete certain debugging and testing tasks when required. 

Having wanting to keep track of all the testing requirements for my own projects, I thought creating a debugging and testing task manager tool would be beneficial for myself and for others. 

At present the app is set up as a proof of concept to allow an admin user to be able to log in to create and delete projects, while normal users can log in and create or delete tasks to be completed for those projects. 

Admin log in details are: 

Username: admin

Password: 12345 

Anyone can create a normal user account by registering a username and password, both of which need to be at least five characters long. 

In its current form the app is just a proof of concept with many features missing that I would like to add. I have detailed out these possible future features later on in this README file. Debugist was created as my third milestone project for the Code Institute Level 5 Diploma in Web Application Development.

---

## Contents 

* [User Experience](#User-Experience) 
* [User Stories](#User-Stories) 
* [Design](#Design) 
* [Colour Scheme](#Colour-Scheme) 
* [Typography](#Typography) 
* [Wireframes](#Wireframes) 
* [Database Schema](#Database-Schema)
* [Development Build Process](#Development-Build-Process)
* [Features](#Features) 
* [App Pages](#App-Pages)
* [Future Development](#Future-Development) 
* [Accessibility](#Accessibility) 
* [Technologies Used](#Technologies-Used) 
* [Deployment](#Deployment)
* [How to Fork](#How-to-Fork) 
* [How to Clone](#How-to-Clone)
* [Testing](#Testing) 
* [Credits](#Credits)

---

## User Experience 

### User Stories 

#### First time Visitor Goals 

* I want to access and see the current list of outstanding debugging/testing tasks to be completed.
* I want the app to be functional, easy to use and responsive on my device.
* I want the app to be simple in its layout, easy to understand and navigate.

#### Returning Visitor Goals

* I want to be able to create, update and delete the current list of outstanding debugging/testing tasks to be completed.

#### Frequent Visitor Goals

* I want to be able to quickly see the current list of outstanding tasks and also what progress has been done on them.
* I want the project manager to have admin access so new projects can be created or old ones deleted. 
* I want to be able to assign tasks to specific users and receive notifications when tasks are overdue. 

---

## Design

### Colour Scheme

I wanted to keep the colour scheme to be simple yet fun as the main focus for the user will be on the current projects and tasks rather than the app itself. 

The backgrounds are kept to white and greys to maintain a clean simple dashboard interface.

I used pink and teal as accent colours to contrast well against the white and grey backgrounds and card sections. 

The red was only used on the delete buttons so that these would stand out and ensure that the user only selected them when they were sure to use them. 

I wanted to make sure that the contrast of the colours was very well defined throughout the app, I used the recommended colours built into the Materialize CSS framework to maintain constancy and ensure that the colour spectrum would also work for users with colour blindness.  

![Colour Scheme](colourScheme.png) 

### Typography

Roboto 2.0 font was used throughout the app.

This font works well for the app design as it is simple and easy to read. 

League Spartan font was used for the logo design. 

![Font Example](Font.jpeg)

### Wireframes

Wireframes were created using Balsamiq software for desktop, mobile and tablet.

![Desktop Version Wireframes](wireframesMergedDesktop.jpeg)
![Mobile Version Wireframes](wireframesMergedMobile.png)
![Tablet Version Wireframes](wireframesMergedTablet.png)

### Database Schema 

![Database Schema](schema.jpeg)

### Development Build Process

The build process of the app was completed in small incremental sections. 
This can be observed in the git commits catalogued within the Github repository that can be found here:
[Repository Commits](https://github.com/develosi/debugist-project/commits/main)

Testing was carried out during the build, all testing documentation can be found at: [TESTING.md](TESTING.md)

### Features

The Debugist app is made up of 10 pages and they all have content on them taken from the Base Template.

* Home Page which is the same as Tasks Page
* Register Page
* Login Page 
* Profile Page
* Add Task Page
* Edit Task Page
* Projects Page
* Add Project Page
* Edit Project Page

### App Pages 

All Pages in the app are responsive and have a favicon of the Debugist Logo:

![Debugist Favicon](documentation/images/faviconImage.png) 

#### Base Template 

All pages throughout the app have these base template elements on them. The content for these sections is taken from the Base Template HTML page. 

![Top Nav Bar Section](documentation/images/.png)

![Mobile Side Nav Bar Section](documentation/images/.png)

![Footer Section](documentation/images/.png)

#### The Home Page which is also the same as the Tasks Page

The Tasks/Home page shows all current outstanding tasks to be completed. The user can edit or delete these tasks.  

The user can add a new task by clicking on the Add Task button which is animated. 

![Tasks/Home Page](documentation/images/.png)

#### Register Page

The user can register for an account. 

![Register Page](documentation/images/.png)

#### Login Page 

A user that already has an account can log in. 

![Login Page](documentation/images/.png)

#### Profile Page

The user can access the profile page, no content has been produced for the profile section yet. 

![Profile Page](documentation/images/.png)

#### Add Task Page

The user can add a new task by completing the form and clicking on the plus symbol. 

![Add Task Page](documentation/images/.png)

#### Edit Task Page

The user can edit the task by completing the form and clicking on the plus symbol. 

![Edit Task Page](documentation/images/.png)

#### Projects Page

The user can view all current projects. 

![Projects Page](documentation/images/.png)

#### Add Project Page

If the admin is logged in they can add a new project.

![Add Project Page](documentation/images/.png)

#### Edit Project Page

If the admin is logged in they can edit a projects name. 

![Edit Project Page](documentation/images/.png)

#### Future Development

In future development and implementations I would like to add the following:

* Give users the option to assign tasks to other users.
* Show which tasks were created by which user.
* Ability to search for tasks and projects. 
* Offer tasks broken down into sections as an option so a user can show progress within a task that is not yet fully complete. 
* Add a more secure log in section that includes email of the user. 
* Ability to sort tasks by other options such as timeframe, urgency or alphabetically. 
* Main home page should be a standard landing page without yet showing any tasks before a user is logged in.
* Ability to create organisations so that you can only see projects or tasks associated with your organisation or team. 