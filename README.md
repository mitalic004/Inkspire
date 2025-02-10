# Inkspire

<p align="center">
| <a href="https://github.com/mitalic004/Inkspire" target="_blank">Live Project</a> |
</p>

<a id="overview"></a>
## Overview
Inkspire is a assessed portfolio project developed as part of the Code Institute Full Stack Software Developer Bootcamp, with the intention of demonstrating proficiency in Python, Django [] to create a responsive website.

The intention of this project was to create an interactive website for []

The users can register an account and login to []

![Responsive Mockup]()


## Contents
- [Overview](#overview)
- [UX](#user-experience)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
- [Design](#design)
  - [Topography](#topography)
  - [Colour Scheme](#colour-scheme)
- [Features](#features)
- [Agile](#agile)
- [Testing](#testing)
  - [Verification & Validation](#valid-test)
  - [Manual Testing](#manual-test)
  - [Automated Testing](#auto-test)
  - [Known Bugs](#bugs)
- [Future Features](#future-features)
- [AI Implementation](#ai-implementation)
  - [Use Cases & Reflections](#ai-use)
  - [Code Creation](#ai-code)
  - [Debugging](#ai-debug)
  - [Performance and UX Optimization](#ai-optimization)
  - [Automated Unit Testing](#ai-test)
  - [Overall Impact](#ai-impact)
- [Technology Used](#tech-used)
- [Deployment](#deployment)
  - [Security Measures](#security)
- [Credits](#credits)


<a id="user-experience"></a>
## UX (User Experience)

<a id="user-stories"></a>
### User Stories
- As a user I can view the landing page so that access the website.
- As a user I can register an account and login to the site so that view posts.
- As a user I can view a list of posts so that I can select which post I want to view.
- As a user I can click on a post so that I can view the whole post.
- As a user I can view comments on an individual post so that I can read opinions on the post.
- As a user I can leave comments on a post so that I can share my opinion about the post.
- As a user I can edit or delete my comments so that change my comments.
- As an admin I can create, read, update and delete posts so that I can manage the content on the website.
- As an admin I can create draft posts so that I can finish writing the content later.
- As an admin I can delete any comments so that I can moderate the website.
- As a user I can submit content so that it will be displayed on the website.

<hr>

<a id="wireframes"></a>
### Wireframes
Wireframes for all pages of the website were created before coding began. Versions for desktop, tablet and mobile size were created to reflect the responsive design expected. 

For the most part, the designs remained consistent with the implementation, but some changes were made - they will be shown and explained below.

- Landing Page
  - The homepage has stayed mostly the same as the wireframe.

![Homepage Desktop](assets/images-readme/Wireframe-Homepage-Desktop.png)

![Homepage Tablet & Mobile](assets/images-readme/Wireframe-Homepage-TabletMobile.png)

- 2 Page
  - AA

![2 Desktop]()

![2 Tablet & Mobile]()

- 3 Page
  - AA
  
![3 Desktop]()

![3 Tablet & Mobile]()


<a id="design"></a>
## Design

<a id="topography"></a>
### Typography

The project used two sans-serif fonts which were implemented via [Google Fonts](https://fonts.google.com).

- [Overlock](https://fonts.google.com/specimen/Overlock) was used as the main logo and heading font to make it stand out and fit with the theme of the website.
- [Lato](https://fonts.google.com/specimen/Lato) was used for all the links and main content of the website to ensure easy readability.

<hr>

<a id="colour-scheme"></a>
### Colour Scheme

The colours used were taken from [Coolors](https://coolors.co/). Contrasting colours were used for the background, text and other elements (like buttons and info cards) to make the website easier to read and interact with. Some colours were not used in the final implementation, as they did not contrast enough to provide a suitable user experience.

6A513B Coffee:		
- `#01161E` (Rich Black) used for: header & footer backgrounds, main font
- `#003052` (Prussian Blue) used for: main background, button background
- `#A50021` (Madder) used for: hyperlinks
- `#F1E9D2` (Parchment) used for: post background, header & footer font, homepage headings font, button text
- `#DACDB2` (Dun) used for: comment reply background
- `#C3B091` (Khaki) used for: comment background
- `#4B3621` (Cafe Noir) used for: selected button

![Colour Palette](assets/images-readme/Colour-Palette.png)


<a id="features"></a>
## Website Features

The website consists of three pages with distinct sections to ensure a good user experience. All features on the website were implemented using a combination of HTML5, CSS (including Bootstrap) and JavaScript and are responsive on multiple device sizes in accordance with appropriate breakpoints. 

- Header Navigation Bar
  - A sticky navigation bar on all pages with the logo and website title which redirects to the homepage
  - Links to other pages on the website

![Navigation Bar](assets/images-readme/NavBar.png)

- Feature
  - Explaination

![FeatImg]()

- Footer
  - Copyright details
  - Links to GitHub repository and social media sites

![Footer](assets/images-readme/Footer.png)

<a id="agile"></a>
## Agile
[Project Board Link](https://github.com/users/mitalic004/projects/2)


<a id="testing"></a>
## Testing
Validation of HTML/CSS/JavaScript, Lighthouse Audits, Bugs

<a id="valid-test"></a>
### Verification & Validation
#### Google Lighthouse Testing

Good scores were achieved for both Desktop and Mobile when passing through the official [Google Lighthouse](https://pagespeed.web.dev/)

- Desktop
![Desktop Results](assets/images-readme/Lighthouse_Desktop.png)

- Mobile
![Mobile Results](assets/images-readme/Lighthouse_Mobile.png)

<hr>

#### Validation Testing

- HTML
  - Some error were returned when passing through the official [W3C validator](https://validator.w3.org/nu/)
  - These could not be addressed in the time available

![HTML Validation Homepage](assets/images-readme/HTMLValidation_Home.png)
![HTML Validation Enquiry](assets/images-readme/HTMLValidation_Enquiry.png)

- CSS
  - One error was found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)

![CSS Validation](assets/images-readme/CSSValidation.png)

<hr>

- JavaScript
  - No errors were found when passing through the official [JSHint validator](https://jshint.com/)
  - Some warnings were made, but most were regarding different versions of JavaScript

![JavaScript Validation](assets/images-readme/JSValidation.png)

<hr>

- Python
  - No errors were found when passing through the [JSHint validator](https://jshint.com/)

![Python Validation](assets/images-readme/PythonValidation.png)

<hr>

<a id="manual-test"></a>
### Manual Testing
| Function | Expected Outcome | Does it work? |
| ----------- | ----------- | ----------- |
| General - Header | The header is displayed at the top of the page and sticks there. | Yes |
| General - Logo Link | The logo and title direct the user to the homepage when clicked. | Yes |
| General - NavBar | The NavBar links direct the user to the relevant pages when clicked. | Yes |
| General - NavBar Login | The Login link opens a pop-up when clicked. | Yes |
| General - Login | The Login pop-up allows the user to sign in or register. | Yes |
| General - Login Validation | The Login pop-up validates user's input if they sign in. | Yes |
| General - Login Registration Link | The Login pop-up redirects the user to the Registration page if the button is clicked. | Yes |
| General - Account Dropdown | When logged in, an account dropdown menu will appear with borrowed and favourited books listed. | Yes |
| General - Page Reset | The page reloads after logging out. | Yes |
| General - Footer | The footer is displayed at the bottom of the page and shows social media links and a copyright. | Yes |
| General - Footer Links | The social media links direct the user to the relevant websites when clicked. | Yes |
| General - Footer Links New Page | The social media links open in new pages. | Yes |
| General - Responsivity | The website is responsive and changes format depending on the device size. | Yes |
| Homepage - Hero Section | The Jumbrotron is displayed with a background image, text overlay and Borrow and Favourite buttons. | Yes |
| Homepage - Hero Section Buttons | The Borrow and Favourite buttons work as intended when clicked. | Yes |
| Homepage - Info Cards | The cards are displayed side by side with book titles and images. | Yes |
| Homepage - Info Cards Hover | The cards are expanded to show a short description and Borrow and Favourite buttons when hovered over. | Yes |
| Registration - Display Fields | The relevant fields are all visible and can be interacted with. | Yes |
| Registration - Input Validation | The text boxes validates the user's input to ensure data is in the correct format. | Yes |
| Registration - Submit Pop-Up | The button displays a pop-up when clicked to inform the user their details have been submitted. | Yes |
| Enquiry - Display Fields | The relevant fields are all visible and can be interacted with. | Yes |
| Enquiry - Input Validation | The text boxes validates the user's input to ensure data is in the correct format. | Yes |
| Enquiry - Submit Success | The page will show a success message to inform the user the query has been sent. | Yes |
| Enquiry - Submit Email | The query is be sent to a dummy email after it is submitted. | Yes |
| Enquiry - Form Reset | The form resets after returning from the submit page. | Yes |
| Kids Page - Opens Short Story | The page opens a short story when the title is clicked. | Yes |
| Kids Page - Page Buttons Work | The page turns to a new page when the relevant buttons are clicked. | Yes |
| Kids Page - Read Aloud Button | The page reads the story aloud and stops playing when the relevant button is clicked. | Yes |

<hr>

<a id="auto-test"></a>
### Automated Testing

<hr>

<a id="bugs"></a>
### Known Bugs
- 


<a id="future-features"></a>
## Future Features

- As a user I can like posts so that I can view them later.
- As a user I can view an account page so that I can see my account details.
- As a user I can search for post titles so that I can find specific posts.
- As a user I can click the author name so that I can see other posts by the same author.


<a id="ai-implementation"></a>
## AI Implementation

<a id="ai-use"></a>
### Use Cases & Reflections

<a id="ai-code"></a>
### Code Creation

<a id="ai-debug"></a>
### Debugging

<a id="ai-optimization"></a>
### Performance and UX Optimization

<a id="ai-test"></a>
### Automated Unit Testing

<a id="ai-impact"></a>
### Overall Impact



<a id="tech-used"></a>
## Technologies Used

### Technologies & Languages

- HTML5
- CSS
- JavaScript
- Python
- Git Version Control
- GitHub

<hr>

### Libraries & Frameworks

- Bootstrap
- Django
- Google Fonts
- Font Awesome

<hr>

### Tools & Programs

- Balsamiq
- LucidCharts
- Web3Forms
- Microsoft Copilot

<a id="deployment"></a>
## Deployment

### GitHub
- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - [Inkspire, https://github.com/mitalic004/Inkspire](https://github.com/mitalic004/Inkspire)

<hr>

<a id="security"></a>
### Security Measures

<a id="credits"></a>
## Credits

### Code

The project brief and primary learning and README.md template was supplied by [Code Institute](https://codeinstitute.net/).

Supplementary learning resources which were referenced throughout the project are listed below:

- I Think Therefore I Blog Walkthrough Project by Code Institute
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Web3Forms](https://docs.web3forms.com/)
- [Microsoft Copilot](https://copilot.microsoft.com/)

<hr>

### Content 

- The text, some images and content included in the website was generated using Microsoft Copilot AI
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- The fonts were taken from [Google Fonts](https://fonts.google.com/)
- The colours were taken from [Coolors](https://coolors.co/)

<hr>

### Media

- The story cover images were taken from sources on [Pixabay](https://pixabay.com/):
  - [CDD20](https://pixabay.com/users/cdd20-1193381/)
  - [betidraws](https://pixabay.com/users/23986844/)
  - [camiladenleschi](https://pixabay.com/users/camiladenleschi-1542038/)
- Some images used for the website page are genereated using Microsoft Copilot AI
