# Breathe Sauna




## Project Overview

[Breathe Sauna](https://court-pencil.github.io//)

Breathe Sauna Booking System is a full-stack Django web application that allows users to register, log in, and book time slots for a sauna session. The system is designed to provide a smooth booking experience while enforcing important business rules such as preventing double bookings and exceeding sauna capacity.

Users can view sauna information, create bookings, and manage their reservations through a secure authentication system. Administrators can manage availability, time slots, and bookings through Django’s built-in admin panel.
![image of website on all screen sizes](src/docs/)

## Project Rationale
This project was created to simulate a real-world booking system for a small business. Many booking systems are overly complex for single-location services. This project focuses on creating a streamlined, user-friendly experience that allows customers to reserve sessions quickly and reliably.

The application demonstrates backend development using Django, relational database design, form validation, authentication workflows, and responsive frontend design using Bootstrap.


[Contents]()

- [User Goals](#user-goals)
- [User Stories](#user-stories)
- [Website Goals and Objectives](#website-goals-and-objectives)
- [Wireframes](#wireframes)
- [Design Choices](#design-choices)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Images](#images)
  - [Responsiveness](#responsiveness)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [StartScreen](#start-screen)
    - [Quiz questions](#quiz-questions)
    - [Real time feedback](#real-time-feedback)
    - [Score tracking](#score-tracking)
    - [Replay Button](#replay-again)
    - [Thematic styling](#thematic-styling)
    - [End Screen](#end-screen)
  - [Future Enhancements](#future-enhancements)
- [Technologies Used](#tech-used)
  - [Languages](#languages)
  - [Libraries & Framework](#libraries-framework)
  - [Tools](#tools)
- [Testing](#testing)
  - [Bugs Fixed](#bugs-fixed)
  - [Responsiveness Tests](#responsiveness-tests)
  - [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [Javascript](#javascript)
  - [User Story Testing](#user-story-testing)
  - [Feature Testing](#feature-testing)
  - [Acessibility Testing](#acessibility-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Brower Testing](#browser-testing)
- [Deployment](#deployment)
  - [To deploy the project](#deploy-project)
  - [To fork the project](#fork-project)
  - [To clone the project](#clone-project)
- [Credits](#credits)

## User Goals

- Book a sauna session quickly and easily

- View available time slots clearly

- Prevent accidental double bookings

- Receive confirmation feedback after booking

- Manage personal bookings

- Access the system on any device

- Use a secure login and registration system


## User Stories

- As a user, I want to create an account so I can book sauna sessions.

- As a user, I want to log in securely so my bookings are private.

- As a user, I want to see available time slots so I can choose a suitable session.

- As a user, I want to avoid booking conflicts so my reservation is guaranteed.

- As a user, I want to cancel bookings if my plans change.

- As a user, I want the site to work on mobile devices.

## Website Goals and Objectives

- Provide a simple and reliable booking system

- Prevent scheduling conflicts

- Offer clear and intuitive navigation

- Maintain strong security practices

- Deliver responsive performance across devices

- Provide admin tools for business management


## Target Audience

- Individuals booking personal wellness sessions

- Small sauna or spa businesses

- Users seeking a simple reservation system


## Wireframes /////////////////


### UX Design



![Wireframe-Mobile](src/docs/)
![Wireframe-Tablet](src/docs/)
![Wireframe-Desktop](src/docs/)

## Design Choices

### Typography

The primary font used throughout the project is **Merriweather Sans**. This typeface was chosen for its clean, modern appearance and high readability across different screen sizes. Merriweather Sans balances professionalism with warmth, which aligns with the calm and welcoming atmosphere expected from a wellness-focused sauna brand.

The font performs well on both desktop and mobile devices, ensuring text remains legible in booking forms, navigation menus, and informational content. Its simple sans-serif structure reduces visual clutter and improves accessibility, making it easier for users to scan and understand important booking information quickly.



### Colour Scheme


The colour palette was designed to reflect the natural, calming environment associated with sauna experiences. Warm earthy browns were selected to represent wood and heat, reinforcing the physical materials and atmosphere of a traditional sauna. These tones are paired with soft neutral greys and muted green accents to evoke relaxation, balance, and nature.

This combination creates a calm and inviting visual identity that supports the wellness theme of the application. The colours are intentionally subdued to reduce visual strain and maintain a soothing user experience.


### Colour Psychology

The colour palette was chosen deliberately to reflect the emotional experience associated with sauna and wellness environments.

**Warm earthy browns** are strongly connected to feelings of warmth, comfort, and stability. These tones mimic natural wood and heat, which are core visual elements of traditional saunas. Psychologically, brown creates a sense of grounding and safety, helping users feel relaxed and secure while interacting with the booking system.

**Soft neutral tones** were included to balance the warmth of the browns. Neutral colours reduce visual fatigue and create a calm background that allows important interface elements, such as buttons and forms, to stand out clearly. This contributes to a stress-free browsing experience.

The **muted green accent** introduces an association with nature, health, and renewal. Green is widely linked to wellbeing and relaxation, reinforcing the spa-like atmosphere of the project. It subtly suggests freshness and rejuvenation, which aligns with the purpose of a sauna experience.

Together, these colours create a harmonious palette that promotes calmness, warmth, and trust. The psychological effect supports the project’s goal of providing a soothing and welcoming user experience, rather than an overstimulating or distracting interface.

![Coolors scheme](docs\sauna-colour-scheme.png)

I used [Contrast Grid](https://contrast-grid.eightshapes.com/ "Contrast Grid") to check effective color pairings that support readability and to identify combinations that may hinder legibility due to insufficient contrast or visual discomfort.

![Colour contrast grid](docs\colour-contrast-grid.png)




### Responsiveness

My App is responsive to all screen sizes. 
| Breakpoint | Class infix | Dimensions | | |
|-------------------|-------------|------------|---|---|
| Extra small | None | <576px | | |
| Small | sm | ≥576px | | |
| Medium | md | ≥768px | | |
| Large | lg | ≥992px | | |
| Extra large | xl | ≥1200px | | |
| Extra extra large | xxl | ≥1400px | | |


## Features


The Breathe Sauna website provides a clean, intuitive booking interface that allows users to quickly reserve sauna sessions. The layout is designed to minimise friction and guide users smoothly from browsing information to completing a booking.

The system uses a mobile-first responsive design, ensuring the booking experience works seamlessly across phones, tablets, and desktops.


## Existing Features

### User Authentication

Secure registration and login using Django’s built-in authentication system. Only logged-in users can create and manage bookings, protecting user data and preventing unauthorised access.


### Sauna Information Page

A dedicated sauna information page displays details such as capacity, description, and price. This gives users a clear understanding of what they are booking before committing.

### Real time feedback

When users attempt to create a booking, the system immediately checks for:

Past date selections

Double bookings

Capacity limits

Clear error messages are displayed if a rule is violated, helping users correct mistakes instantly.

### Booking System

Users can create bookings by selecting an available date and time slot. The form validates user input and prevents invalid reservations.

### My Bookings Dashboard

Users can view all their upcoming bookings in a personal dashboard. From here they can manage or cancel reservations easily.

### Admin Management Panel

Administrators can manage:

Sauna details

Available time slots

User bookings

User accounts

This allows full control over the booking system without modifying code.

### Responsive Design

The interface adapts smoothly to different screen sizes using Bootstrap, ensuring accessibility and usability across devices.

## Future Enhancements

### Online Payment Integration

Users could pay for their booking during checkout using a secure payment gateway, streamlining the reservation process.

### Email Booking Confirmations

Automatic confirmation emails could be sent after successful bookings, improving communication and professionalism.

###  Booking Reminders

Automated reminder notifications could reduce missed appointments.


## Technologies Used

### Languages

- HTML
- CSS
- Python

### Libraries & Framework

- [Google Fonts](https://fonts.google.com/selection)
- Django
- Bootstrap
- Django Crispy Forms



### Tools

- [Github](https://github.com/)
- [Balsamiq](https://balsamiq.com/)
- [W3C HTML Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [WAVE Accessibility Tool](https://wave.webaim.org/ "WAVE Accessibility Tool")
- [Am I Responsive](https://ui.dev/amiresponsive "Am I responsive")
- [PostgreSQL](https://www.postgresql.org/)

## Testing

## Bugs

### Responsiveness Tests



| Device / Screen Size | Expected Behaviour                      | Actual Result                                     | Pass/Fail | Notes             |
|----------------------|-----------------------------------------|---------------------------------------------------|-----------|-------------------|
| iPhone SE            | Layout fits screen, buttons easy to tap | Works as expected                                 | Pass      |                   |
| iPhone 12            | No overflow, text readable              | Works as expected                                 | Pass      |                   |
| Pixel 7              | Buttons scale correctly, no clipping    | Works as expected                                 | Pass      |                   |
| iPad mini            | Layout expands but stays centred        | Works as expected                                 | Pass      |                   |
| iPad Pro             | Content does not stretch too wide       | opposite problem little too small on the screen   | Fail      | Working in progress |
| Nest Hub             | Fully readable, centred content         | Works as expected                                 | Pass      |                   |
| Next Hub Max         | Max-width applied, UI stable            | Works as expected, little too small on the screen | Fail      | Work in progress |


## Manual Testing ()




### User Story BDD Testing

---

### User Story 1 — Register an account

| Category | Details |
|---------|---------|
| **User Story** | As a user, I want to create an account so I can book sauna sessions. |
| **Scenario** | Account registration |
| **Given** | The user is on the registration page |
| **When** | They enter valid details and submit the form |
| **Then** | A new account is created and the user is redirected with a success message |
| **Result** | Pass |
| **Evidence** | [Screenshot of successful registration](docs/user-story-register.png) |

---

### User Story 2 — Log in securely

| Category | Details |
|---------|---------|
| **User Story** | As a user, I want to log in securely so I can access my bookings. |
| **Scenario** | User login |
| **Given** | The user has a registered account |
| **When** | They enter correct login credentials |
| **Then** | They are logged in and redirected to the dashboard/home page |
| **Result** | Pass |
| **Evidence** | [Screenshot of login success](docs/user-story-login.png) |

---

### User Story 3 — Book a sauna session

| Category | Details |
|---------|---------|
| **User Story** | As a user, I want to book an available sauna time slot so I can reserve a session. |
| **Scenario** | Creating a booking |
| **Given** | The user is logged in and on the booking page |
| **When** | They select a valid date and time slot and submit the form |
| **Then** | The booking is saved and confirmation is displayed |
| **Result** | Pass |
| **Evidence** | [Screenshot of successful booking](docs/user-story-booking.png) |

---

### User Story 4 — Prevent double bookings

| Category | Details |
|---------|---------|
| **User Story** | As a user, I want the system to prevent double bookings so my reservation is guaranteed. |
| **Scenario** | Attempt duplicate booking |
| **Given** | A time slot is already booked |
| **When** | The user attempts to book the same slot |
| **Then** | An error message is displayed and the booking is rejected |
| **Result** | Pass |
| **Evidence** | [Screenshot of booking validation error](docs/user-story-duplicate.png) |

---

### User Story 5 — View and manage bookings

| Category | Details |
|---------|---------|
| **User Story** | As a user, I want to view and cancel my bookings so I can manage my schedule. |
| **Scenario** | Viewing personal bookings |
| **Given** | The user is logged in |
| **When** | They navigate to the “My Bookings” page |
| **Then** | All their bookings are displayed clearly |
| **Scenario** | Cancelling a booking |
| **Given** | A booking exists |
| **When** | The user clicks cancel/delete |
| **Then** | The booking is removed and a confirmation message appears |
| **Result** | Pass |
| **Evidence** | [Screenshot of bookings dashboard](docs/user-story-dashboard.png) |

---

### User Story 6 — Accessible on any device

| Category | Details |
|---------|---------|
| **User Story** | As a user, I want to access the booking system on any device so I can book anywhere. |
| **Scenario** | Responsive layout |
| **Given** | The site is opened on different screen sizes |
| **When** | The display changes between mobile, tablet, and desktop |
| **Then** | All elements remain readable and functional |
| **Result** | Pass |
| **Evidence** | [Responsive screenshots](docs/all-screen-sizes-image.png) |




## Code Validation

### CSS

I have used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).  
![Screenshot of CSS validation test](src/docs/)
![Screenshot of CSS validation test](src/docs)

### HTML

I have used [W3C HTML Validation Service](https://validator.w3.org/). The tests came back with no errors. There were 3 info messages about trailing slash on void elements, but that doesn't indicate any problems, just showing best practices. Having used Vite for my React.js app, I have not changed the trailing slashes on the index HTML, as it was set up that way and doesn't pose any problems to the functioning of the app.

![HTML Validation image](src/docs/)
![HTML Validation image](src/docs/)

### Javascript 




## Accessibility Testing

I used the web accessibilty evalution tool [WAVE](https://wave.webaim.org/) to test if my quiz app is accessible to people with diverse needs. One alert was raised, because this is a single page application there are no defined page regions to support improved navigation for assistive technologies. I also used the colour contrast checker on WAVE's site for additional checking.

![WAVE](src/docs/)
![WAVE](src/docs/)
![WAVE](src/docs/)


## Feature Testing

This website was extensively tested for functionality using Chrome developer tools.

## Lighthouse Testing

The Breathe Sauna Project has been tested in Chrome Dev Tools using Lighthouse Testing tool, which inspects and scores the website for the following criteria. I generated two sets of lighthouse reports, one for mobile and one for desktop. 

- Performance - how quickly a website loads and how quickly users can access it.
- Accessibility - test analyses how well people who use assistive technologies can use your website.
- Best Practices - checks whether the page is built on the modern standards of web development.  
- SEO - checks if the website is optimised for search engine result rankings.

## Mobile chrome Dev tools testing:
![lighthouse testing image index](src/docs/)
 

## Desktop chrome Dev tools testing:
![lighthouse testing image index](src/docs/)
 
## Known Issues / Limitations


## Deployment

### Deploying to Heroku

The **Breathe Sauna Booking System** was deployed using **Heroku**, a cloud platform that allows Django applications to run in a production environment.

---

### Prerequisites

Before deployment, ensure the following are set up:

- A Heroku account
- Git installed
- Heroku CLI installed
- A PostgreSQL database configured
- A `requirements.txt` file
- A `Procfile`
- Environment variables stored securely

---

### Step 1: Prepare the Project for Deployment

#### 1. Install Gunicorn

Gunicorn is a production web server required by Heroku.

```
pip install gunicorn
```

Update requirements:

```
pip freeze > requirements.txt
```

---

#### 2. Create a Procfile

In the root directory of the project, create a file named:

```
Procfile
```

Add the following line:

```
web: gunicorn breathe_config.wsgi
```

(This tells Heroku how to run your Django app.)

---

#### 3. Update Settings for Production

In `settings.py`:

- Set `DEBUG = False`
- Add your Heroku app URL to `ALLOWED_HOSTS`
- Configure environment variables using `.env` or Heroku config vars

Example:

```
ALLOWED_HOSTS = ["your-app-name.herokuapp.com"]
```

---

### Step 2: Create Heroku App

Login to Heroku:

```
heroku login
```

Create a new app:

```
heroku create your-app-name
```

---

### Step 3: Add PostgreSQL Database

```
heroku addons:create heroku-postgresql:hobby-dev
```

Heroku automatically sets the database URL environment variable.

---

### Step 4: Deploy to Heroku

Commit your changes:

```
git add .
git commit -m "Prepare for Heroku deployment"
```

Push to Heroku:

```
git push heroku main
```

---

### Step 5: Run Migrations

```
heroku run python manage.py migrate
```

Create a superuser:

```
heroku run python manage.py createsuperuser
```

---

### Step 6: Open the App

```
heroku open
```

Your application is now live.

---

### Redeploying After Changes

Any time updates are made:

```
git add .
git commit -m "Update project"
git push heroku main
```

Heroku automatically rebuilds and redeploys the app.

---

### To Fork the Project

Forking the repository creates a personal copy for experimentation or development.

- Log in to GitHub
- Navigate to the repository
- Click **Fork** (top right)
- The project is copied to your account

---

### To Clone the Project

- Log in to GitHub
- Open the repository page
- Click **Code**
- Copy the repository URL
- In your terminal:

```
git clone <repository-url>
```

- Open the project in your IDE


## Credits

- Code inspiration and learning content:
- Visual content:
  - [Coolors](https://coolors.co/)
  - [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23F2F2F2%0D%0A%23DDDDDD%0D%0A%23CCCCCC%0D%0A%23888888%0D%0A%23404040%2C%20Charcoal%0D%0A%23000000%2C%20Black%0D%0A%232F78C5%2C%20Effective%20on%20Extremes%0D%0A%230F60B6%2C%20Effective%20on%20Lights%0D%0A%23398EEA%2C%20Ineffective%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp)
  - [Pexels](https://www.pexels.com/)
  - [Unsplash](https://unsplash.com/)

- learning content:

  
 