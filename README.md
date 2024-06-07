
# <p style="text-align: center;">RBM: Business Case for Customer Booking App for Consultant Services</p>


![Logo]()

[Click here to view the live web application](https://rbm-app-0a2c6b74ea93.herokuapp.com/)


# Table of contents 

 1. [ User Experience (UX) ](#ux)
 2. [ Agile Methodology ](#agile-methodology)
 3. [ Design ](#design)
 4. [ Features ](#features)  
 5. [ Feature features](#feature-features)  
 6. [ Technology used ](#technology-used) 
 7. [ Testing ](#testing)  
 8. [ Bugs ](#known-bugs)  
 9. [ Deployment](#deployment)
 10. [ Resources ](#resources)  
 11. [ Credits and acknowledgements ](#credits)


# User Experience (UX)
Currently, there is a lack of efficient and user-friendly platforms for customers to book consultants and experts for project tasks. This results in time-consuming processes and potential delays in project delivery.

The goal of this website is to create a user-friendly platform that enables customers to easily book consultants and experts for specific project tasks, streamlining the process and enhancing customer experience. Customers will be able to browse available consultants and experts, select the ones suitable for their project needs, and book them directly through the app. The app will notify both the customer and the chosen consultant of the booking details, including the customer's address and all necessary information for the consultant to join the customer on-site, providing innovative solutions to meet customer needs and stay ahead of the competition in the industry.

## How it Works

- Booking Consultant: The website acts as a booking consultant, guiding clients through the process of finding the right expert for their requirements. Clients can input their needs, preferences, and desired skill sets into the platform, which then generates a curated list of experts who match those criteria.
Check the List of Experts: Once the client has specified their requirements, they can browse through the list of experts provided by the website. Each expert is accompanied by a detailed profile outlining their skills, experience, and areas of expertise.

- Find the Skillset You Need: Clients can easily filter and search through the list of experts to find the specific skillset they require. Whether it's for IT consulting, marketing strategies, legal advice, or any other expertise, clients can quickly identify the experts who possess the skills necessary to meet their needs.

- Get the Expert Right to Your Door: After selecting the desired expert, clients can proceed to book their services directly through the website. RBM ensures a seamless experience by handling all the logistics, including scheduling and coordination, to ensure that the expert arrives at the client's location promptly.
Next Morning Service: RBM prides itself on its swift service, offering clients the convenience of having the expert at their doorsteps as soon as the next morning after booking. This ensures that clients can receive timely assistance and support for their projects or tasks without any delays.

## Benefits:

- Improved customer experience through a seamless booking process.
- Enhanced efficiency by streamlining consultant selection and booking.
- Increased transparency with all relevant information provided upfront.
- Reduced administrative burden for both customers and consultants.
- Higher customer satisfaction leading to repeat business and referrals.

##### [ Back to Top ](#table-of-contents)

# Agile Methodology
In this project, I utilized GitHub for project management, harnessing its robust issue tracking system to effectively manage bugs. Adhering to Agile principles, we divided our work into multiple iterations, ensuring incremental progress and adaptability to evolving requirements. We embarked on two separate projects aimed at defining the optimal architecture and design. Through iterative development cycles, we refined our architectural decisions iteratively, prioritizing flexibility and scalability. Continuous feedback loops enabled us to gather insights, iterate on designs, and promptly address emerging challenges. By embracing Agile methodologies, we fostered collaboration and transparency among team members, facilitating smoother communication and alignment towards project goals. The iterative approach allowed us to incorporate stakeholder feedback iteratively, ensuring the final product met user expectations effectively. Through GitHub's project management features, we maintained visibility into project progress, enabling informed decision-making and timely adjustments. Our dedication to Agile practices and iterative development yielded a robust, adaptable project architecture and design that effectively met functional requirements and stakeholder expectations.

About the user stories, I created based on a Template, which acted as the skeleton for creating new user stories. Each user story would follow the convention:

**As a (role) I can (capability) so that (received_benefit)**


## MoSCoW Prioritization
I followed the MoSCoW Prioritization method for this project, with the following labels:

Must Haves: the 'required', critical components of the project. 

Should Haves: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.

Could Haves: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.

![Github Board]()


## User stories 

### Epics

- User registration and log in
- Booking appointments, edit and delete them
- Admin Panel 
- Maintain consistent design with responsiveness in mind

<!---- Add your user stories and must have, could have, and should have labels-->
| User Story | Priority | 
|----------------------------------------------------------------------------------------------------------------------------------|-------------|
|  #1 |As a **Admin** I can **update the about page content** so that **it is available on the site**|**COULD HAVE**|
|  #2 |As a **registered user** I want to **log in with my credentials** so that **so I can access to my account.**|**MUST HAVE**|
|  #3 |As a **user** I want to **see my booking list ** so that **I can edit an appointment**|**MUST HAVE**|
|  #4 |As a **user** I want to **see my booking list ** so that **I can delete an appointment**|**MUST HAVE**|
|  #5 |As a |**MUST HAVE**|
|  #6 |As a |**MUST HAVE**|
|  #7 |As a  |**MUST HAVE**|
|  #8 |As a|**SHOULD HAVE**|


##### [ Back to Top ](#table-of-contents)

# Design

## Color Scheme

The colours were selected with the intention of ......................................................................................................

## Wireframes

> Initial design planning

Early design stage of this project included making png versions of a homepage and login page prototypes. Thanks to that I could decide on the aesthetic choices before entering the coding stage.
The next stage of UX design planning was creating the basic wireframes using Linux Pencil and hand drawing.
Create minimalist and visual interface that is easy navigate. 

> Large to medium screens

- Home Page
The homepage has a hero image............................
<details>
<summary>Click to View Home Page wireframes</summary>

![Home Page]()
</details>

- Customer Profile 

<details>
<summary>Click to View Customer Profile wireframes</summary>

![Customer Profiles]()
</details>

- About page
Users can read about .....................................

<details>
<summary>Click to View About Page wireframes</summary>

![About Page]()
</details>


- Welcome Page
<details>
<summary>Click to Welcome Page wireframes</summary>

![Welcome Page]()
</details>

- Sign up Page

<details>
<summary>Click to Sign up Page wireframes</summary>

![Sign up Page]()
</details>

- Appointment page (Add an appointment)

<details>
<summary>Click to Add Bookings Page wireframes</summary>

![img]()
</details>

- Appointment page (Appointment list)

<details>
<summary>Click to View Appointment List wireframes</summary>

![img]()
</details>


> Small screens
<!-- Add titles and screenshots for small screens -->



## Data structure 
- After deciding on the kind of the project and features I wanted to implement I used a Draw io to plan the database structure.
- The above diagram is serving as an initial guide to indicate the types and relationships between data stored.

![img]()

## CRUD
CRUD functionality was implemented in booking an appointment:

- Create: An authenticated user can create a booking.
- Read: A user can read their own booked consultant list.
- Update: An authenticated user can edit and update their own booked consultant.
- Delete: An authenticated user can delete their own booked consultant.

In this proyect the feature "booking" has full CRUD functionality available.

Bookings can be deleted from Admin Panel. 

## Data Models

1. AllAuth User Model
- Django Allauth, the User model is the default user model provided by the Django authentication system

| User|            |   |
|----------|:-------------:|------:|
| id |  AutoField |
| username |  CharField|
| email|  EmailField   |   
| password | CharField | 

2. Booking Model 
- Full CRUD functionality is available to the user. <!--Change fields acording to the model-->

| Booking|            |   |
|----------|:-------------:|------:|
| id |  AutoField | PK|
| user |  CharField | FK
| first_name |  CharField   | 
| last_name | CharField |  
| email |  EmailField | 
| service|  CharField   |   FK |
| day | DateTime |    |
| time |  CharField |  |
| notes |  TextField |  |

<!--Add the rest of the models here-->



### Allauth User Model
The User model was built using Django's Allauth library

**All Users:**
- Are able to view the home page and the services provided (about page) 

**Registered Users Only:**
- Can book and appointment
- Can create, read, udpate and delete an appointment from their personal dashboard  (Front End CRUD functionality)

##### [ Back to Top ](#table-of-contents)

# Technology used 

- [Am I Responsive](https://ui.dev/amiresponsive) - Used to verify responsiveness of website on different devices.

- [Bootstrap v5.3.2](https://getbootstrap.com/) - Used to help with the responsiveness of the site and to aid the coding of some of the layout

- [Balsamiq](https://balsamiq.com/) - Used to create the wireframes during the design process

- [Cloudinary](https://cloudinary.com/) - Used for online static file storage.

- [CSS](https://en.wikipedia.org/wiki/CSS) - used for the main site design and layout.

- [Django](https://www.djangoproject.com/)- Used as the Python framework for the site.

- [ElephantSQL](https://www.elephantsql.com/) - Used as the Postgres database.

- [Favicon.io](https://favicon.io/) - Used to create and add the favicon to the browser tab

- [Font Awesome](https://fontawesome.com/) - Used to add icons to the site for aesthetic and UX purposes.

- [GitHub](https://github.com/) - Used to store the project code after being created in GitPod 

- [Gitpod](https://www.gitpod.io/) - Used to create, edit & preview the project's code

- [Google Fonts](https://fonts.google.com/) - Used to import the fonts into the style. 
css file which are used on all pages of the project.

- [Heroku](https://dashboard.heroku.com/)- Used for hosting the deployed back-end site.

- [HTML](https://en.wikipedia.org/wiki/HTML5) - used for the main site content.

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - used for user interaction on the site for automatically closing 
Django Messages and to handle the notification dropdown and notification delete functions.   

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - used as the back-end programming language.

- [PostgreSQL](https://www.postgresql.org/) - Used as the relational database management.

- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.

- [WAVE](https://wave.webaim.org/) - Used for Accessibility evaluation.

## Tools and settings
- Pyenv to manage different versions of python on the machine
- Virtualenv to create Python virtual environements
- Virtualwrapper to help to manage virtual environments
- Automation of repositories creation and and remote repositories with gh

## Infrastructure
- Building Docker images and setting up
- Using minikube with add-ons

##### [ Back to Top ](#table-of-contents)


# Features

## Nav Menu 
- The navigation bar appears on every page so users can easily navigate through the site and it is also fixed, so users don't need to go back to the top of the page is they want to move to a different page.
- Navbar's content changes depending on user authentication, so when the user hasnt log in, the nav bar will display links for 'Home page', 'About',   and 'Login/Register'
 
![img]()

- If the user is logged in, then the navbar will show links for pages that only authorized users can visit and use, they are: 'Book an appointment', 'Your appointments' and 'Logout'. Otherwise, the user will be given the option to 'Register' or 'Login'

![img]()

![img]()

- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

![img]()

## Hero Image

-Hero Image shows a large image of ........................, 

![img]()

## Home page:

- The homepage provides the links to booking and about us page.
- It can be accessed without signing in.

## Footer
- Just like the nav bar, the footer appears on every page and provides links to respective social media pages to provide the necessary informations in an easy way.
- Links are opened in a new tab to avoid dragging users from our site

![img]()

---------------

## Sign Up Page

- User can sign up to create their profile
- Registration allows users to book and appointment with the different consultants. Users are required to add their Email, Username and Password twice, to ensure the correct one is saved. If any field is not filled in appropriately then a display message is used to inform the user with how to procede to complete the form.
- A 'Forgot Password' page is also re-designed from the AllAuth templates but it's full functionality is not yet activated for this version.

![img]()


## Login Page
- User can log in to their account and update their informations
![img]()

## About section 

![img]()


## Book and appointment 
- User can pass their data to create a booking.
- The user may create, edit and delete their bookings, they are informed if a date/time is unavailable and they see a display message if their booking is saved.
- For creating a booking, the user is informed of the necessary fields to be filled in (*)
- A dropdown selection of 'Experts' is available. 
- Date and time is selectable via a calendar widget for date and dropdown selection menu displaying the hour slots from 9am to 6pm. 
- If a date/time combo is unavailable then the user is informed via warning message. 
- User feedback is delivered by message once a booking has been submitted and updated, message disappears after 5 seconds. 

![img](documentation/features/booking_add.PNG)

## List of user's appointments
- Dashboard only visible for Logged-In Users who have made a previous booking
![img]()

## Edit appointments
- When logged in, a edit icon will appear to allow users to modify and update their bookings if they wish.

![img]()

## Delete appointments
- When logged in, a trash icon will appear to allow users to delete their bookings if they wish.
- User can delete their account alltogether with all their data

![img]()

## Log Out
![img]()

![img]()

## Admin Panel

- To access the Admin panel the Admin user adds '/admin/' to the end of the URL to display https://...............................herokuapp.com/admin/. A username and password is requested. For this project, Admin approval is not needed so registered, logged-in users' have instant access to make a booking.

- Admin can control users bookings, via the Django Admin panel.

![img]()

##### [ Back to Top ](#table-of-contents)

# Feature Features
This is definitely a project I want to revisit in the future and add some extra features like:

- Enable the option to reset password
- 
- 

##### [ Back to Top ](#table-of-contents)

# Testing


## Manual testing

The site was tested manually across a range of devices to ensure all links and styling work correctly and to ensure responsiveness across a range of devices. All features on the page were tested, to ensure functionality was not impacted in any way. 

### Account Registration Tests
| Test |Result  |
|--|--|
| User can create profile | Pass |
| User can log into profile | Pass |
| User can log out of profile | Pass |
| Messages are displaying | Pass |
| Messages are dismissable by button and timeout | Pass |


### User Navigation Tests

| Test | Result  |
|--|--|
| User can easily navigate to Bookings | Pass |
| User can access About Us page| Pass|
| User access their account page|Pass|
| User can access the card content in About Us|Pass|
| SuperUser can access admin page|Pass|
| SuperUser can create a expert add skills add a flag for customer or expert admin page|Pass|


### Expert Booking and Profile Tests

| Test |Result  |
|--|--|
|User can make a booking | Pass |
|User can view all of their bookings | Pass |
|User can delete their booking | Pass |
|User can edit booking | Pass |
|User can make more than one booking | Pass |
|User can delete their account | Pass |
|User can edit their information | Pass |
|User can see the confirmation information | Pass |
|User can add skill from Admin interface the confirmation information | Pass |

### Account Authorisation Tests

| Test | Result  |
|--|--|
| Only Superuser can access admin page |Pass|
| Non authorised user  won't access booking page.......................| Pass |
| Non authorised user won't access .................| Pass|


## Validator testing

The website was tested using the tools made available by the World Wide Web Consortium, also known as "W3C".

The two tools used were the Markup Validation Service and the CSS Validation Service. Both tools were used to test the website by URL and also by direct input, with the results shown below.

No errors were returned for all HTML or CSS across all tests. Some warnings were displayed.

- HTML Validation by Direct Input

![img]()
     
- CSS Validation by Direct Input

![img]()


## Lighthouse Testing

A test in all pages was ran using Lighthouse within Google Chrome to verify performance and accessibility standards were met and to ensure best practices were followed.


### Homepage
![img]() 

### About page
![img]()

### Book an appointment page
![img]()

## Browser Compatibility

Testing was carried out on multiple browsers such as Google Chrome, Microsoft Edge, Mozilla Firefox, Brave,  Safari and Opera. Testing was carried out on an Apple iPhone, Apple iPhone 13, Samsung Galaxy S20 FE, Samsung Galaxy A51 and Apple iPad Pro................<!-- Add more or change devices-->


## Python compatibility
Django 5.03 and Python 3.12.0 October 2023

##### [ Back to Top ](#table-of-contents)

# Known bugs 

JavaScript filter on expert view is not taking into account an expert with multiple skills


##### [ Back to Top ](#table-of-contents)

# Deployment 
This project was deployed using Github and Heroku.
The live deployed application can be found deployed on [Heroku](https://rbm-app-0a2c6b74ea93.herokuapp.com/).


#### The deployment stage of the website should follow the steps below:


> Set up enviroment variables

- In the Django app editor create env.py in the top level
- In env.py import os
- In env.py set up necessary enviroment variables:
  - add a secret key using: os.environ['SECRET_KEY'] = 'your secret key'
  - for the database variable the line should include os.environ['DATABASE_URL']= 'Paste the database link in here'
  - in settings.py replace value of SECRET_KEY variable with os.environ.get('SECRET_KEY')
  - in settings.py change the value of DATABASES variable to 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
- In Django app's settings.py on top of the file add:

```
from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```

- Navigate to the "Settings" tab in Heroku.
- Open the "Config Vars" section and add DATABASE_URL as Key and the database link from app's env.py as Value
- Add SECRET_KEY for the Key value and the secret key value from env.py as the Value
- In the terminal migrate the models over to the new database connection
- In settings.py add the STATIC files settings as follows:

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```

- Change the templates directory in settings.py to: TEMPLARES_DIR = os.path.join(BASE_DIR, 'templates')
- In TEMPLATES variable change the 'DIRS' key to look like this: 'DIRS': [TEMPLARES_DIR],
- Add Heroku to the ALLOWED_HOSTS list (the format will be your-app-name.herokuapp.com, you can copy it from the Domains section in Settings tab in your Heroku app)
- If you haven't done that up to this point, then create in your Django app's code editor new top level folders: static and templates
- Create a new file on the top level directory - Procfile, remembering to use a capital letter
- Within the Procfile add following:

```
web: guincorn PROJECT_NAME.wsgi
``` 
- In the terminal, add the changed files, commit and push to GitHub

#### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository. You can do this with following steps:

- Log in to GitHub or create an account
- Enter this [repository link](https://github.com/Jean7667/RBM_APP)
- Select "Fork" from the top of the repository
- A copy of the repository should now be created in your own repository

#### Create a clone of this repository

Creating a clone enables you to make a copy of the current version of this repository to run the project locally. To do this follow steps below:

- Navigate to the GitHub Repository you want to clone
- Click on the <>Code button at the top of the list of files
- Select the "HTTPS" option on the "Local" tab and copy the URL it provides to the clipboard
- Navigate to your code editor and in the terminal change the directory to your chosen location 
- Type "git clone" and paste the GitHub repository's link
- Press enter and git will clone the repository for you


### ElephantSQL Database
This project uses ElephantSQL for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

Click Create New Instance to start a new database.
Provide a name (this is commonly the name of the project: tribe).
Select the Tiny Turtle (Free) plan.
You can leave the Tags blank.
Select the Region and Data Center closest to you.
Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API
This project uses the Cloudinary API to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.


### Heroku Deployment
This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:
Make sure DEBUG = False in the settings.py

Heroku needs two additional files in order to deploy properly.

Create a new file in the main directory called Procfile (do not use any extension for the name of this file)
The Procfile can be created with the following command:

echo web: gunicorn app_name.wsgi > Procfile
replace app_name with the name of your primary Django app name; the folder where settings.py is located

> Create the Heroku app

- Sign up / Log in to Heroku
- In Heroku Dashboard page select 'New' and then 'Create New App'
- Name a project (the app's name must be unique)
- Select EU as that was my region in the moment of creating the app
- Select "Create App"
- From the new app Settings, click Reveal Config Vars, and set your environment variables.
(Add table with keys!!)
- In the "Deploy" tab choose GitHub as the deployment method
- Connect your GitHub account/ find and connect your GitHub repository

Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
Once the build process is completed Heroku displays 'Your App Was Successfully Deployed'
Click 'Open App' to view the deployed live site.
- As my first 2 build attempts failed I needed to apply changes to my code (I forgot to set up the static files and templates) to successfully deploy on the 3rd time 

##### [ Back to Top ](#table-of-contents)

# Resources

- [Code Institute Full Stack Development course materials](https://codeinstitute.net/global/full-stack-software-development-diploma/?sitelink=FullStackDiploma-IRL&utm_term=code+institute&utm_campaign=CI+-+IRL+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=635725005315&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code+institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAgqGrBhDtARIsAM5s0_l13h8fkiqZeHnw16zshbX6svuL8YJNrw6G-RFdq03RQybQXLSoZiYaAjGqEALw_wcB) 
- [Django documentation](https://www.djangoproject.com/)
- [Bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Stack overflow](https://stackoverflow.com/)
- Multiple books and Youtube Videos.

##### [ Back to Top ](#table-of-contents)

# Credits

- Thank you to my mentor ......................... for his positive support, guidance and advice.
- Thanks to ....................................................................

##### [ Back to Top ](#table-of-contents)

--------------------------------------------------------------------------
<!--I dont know where to put this info, paste this in the correct place-->
---------------------------------------------------------------------------
### Authentication and profile management:

 
I used the UserAbstrat Model for this project 

The custom user model abstract in Django offers flexibility by allowing developers to tailor user models to specific project needs. It empowers customization of user attributes and authentication methods without altering the core Django framework. This abstraction enhances scalability, enabling seamless integration of additional features and third-party packages. Moreover, it promotes better code organization by centralizing user-related logic within the project. Additionally, the custom user model abstract facilitates adherence to security best practices by providing control over authentication mechanisms and user data storage.

https://learndjango.com/tutorials/django-custom-user-model
----------------------------------------------------------------------------