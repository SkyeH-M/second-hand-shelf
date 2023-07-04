# Second Hand Shelf

Second Hand Shelf is a second hand book selling website, users can browse books by genre, or by different filtering criteria like alphabetised title, year of release, language, price, or rating. They can also view specific offers like clearance items, or new releases. Basic functionality of the site is comprised of the user being able to register for an account, log in and out, and complete orders by paying and receiving a confirmation email. Additional functionality has been added for user experience and this will be discussed further on in the document.

![Image of my responsive site]()
[Link to the deployed site](https://second-hand-shelf-592f61246782.herokuapp.com/)

## Contents 

* [User Experience (UX)](#user-experience-ux)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Icons and Images](#icons-and-images)
  * [Features](#features)
  * [Accessibility](#accessibility)
  * [Wireframes](#wireframes)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

* [Deployment](#deployment)

* [Testing](#testing)
  * [Automated Testing](#automated-testing)
    * [W3 Nu HTML Validator](#w3-nu-html-validator)
    * [W3C CSS Validation Service](#w3c-css-validation-service)
    * [Wave](#wave-testing)
    * [Lighthouse](#lighthouse-testing)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)

* [Credits](#credits)
  * [Code Sections/Tutorials](#code-sectionstutorials)
  * [Media](#media)
  * [Text](#text)
  * [Acknowledgements](#acknowledgements)

## User Experience (UX)
### Project Goals
The main goal of Second Hand Shelf is to provide a functional ecommerce experience to simulate the ability for users to browse products, add them to their basket and to checkout and receive order confirmation via email.

* As a developer a focal goal was to improve on the basic functionality of an ecommerce website, this involved developing multiple additional features to improve user experience and extend the use of the site. These additional features are as follows:
  * Wishlist functionality
  * Rating and Review functionality for books
  * A contact form that sends users an email to confirm that their message has been received and will be responded to within 48 hours
  * Inspired by other second hand book shops like [World of Books](https://www.wob.com/en-gb) I created dynamic pricing whereby the price of a book differs depending on the quality of book selected
* As always accessibility was at the heart of the design and development of this site, ensuring that the site is easily accessible to all regardless of abilities. Not only is this the duty of developers but also encourages users with different abilities to be able to purchase items from the site, making this a business goal also

### User Stories
#### Viewing and Navigation
* View the website on a range of device sizes and have it be aesthetically pleasing and functional.
* View a range of books for sale.
* View individual product details.
* Easily view the total of my purchases at any time.
* View what books (if any) are in my wishlist
* View book reviews and ratings from other users
#### Registration and User Accounts
* Easily register for an account
* Easily login or logout
* Easily recover my password in case I forget it
* Receive an email confirmation after registering
* Have a personalised user profile
* Be able to easily contact the site owners and receive confirmation of my message
#### Sorting and Setting
* Sort the list of available books
* Sort by specific genre of book
* Search for a book by title or specific words in the blurb
* Easily see what I've searched for and the number of results found
* Be shown on the book details page whether a particular book is in my wishlist
#### Purchasing and Checkout
* Easily select the quantity of a book when purchasing it
* Easily select the quality of a book when purchasing it
* View items in my bag to be purchased
* Adjust the quantity of individual items in my bag
* Easily enter my payment information
* Feel my personal and payment information is safe and secure
* View an order confirmation after checkout
* Receive an email confirmation after checking out
#### Admin and Store Management
* Add books
* Edit/update a book
* Delete a book

## Design
### Colour Scheme

![Image of colour scheme](/docs/images/colour-palette.png)

The colour scheme of the Second Hand Shelf is primarily comprised of black, white and different shades of green.

* The background is white to ensure the site is clean and readable and that the users' focus is always on the colours of the products instead of them being distracted by a busy background
* The site text is predominately black and dark grey, again to ensure readability but also to provide enough contrast with the white background
* The green colours highlighted throughout the site were chosen to evoke feelings of reliability and affordability given that the site is for a second hand book shop

### Typography

[Google Fonts](https://fonts.google.com/) was used to import the fonts featured in the site, both fonts used are of the type sans-serif to maintain consistency

![Image of Stripe Element Font](/docs/images/inter-font.png)
* I used the font Inter for the stripe elements in the checkout page as it's clearly readable and dyslexia friendly which is especially important when users are trying to place an order

![Image of Body and Title Font](/docs/images/cabin-font.png)
* I chose the Cabin font for both the header and body of the site so that text is consistent and always readable. Having important text such as the Title and page headers displayed in uppercase helps to highlight information that the user should pay attention to

### Icons and Images

* All icons used throughout the site were provided by [FontAwesome](https://fontawesome.com/) as their style is aesthetically pleasing while being consistent and easily understandable
* I sourced an icon from [Flaticon](https://www.flaticon.com) that will be attributed in the credits section of this document. I then used [Favicon](https://favicon.io/) to convert this png to an icon file and imported that to my site. I installed a Favicon to help users distinguish this tab from others in their browser, the simple book related design and bright colours help to do this.
* All product images will be attributed in the credits section, along with the hero image on the home page
* The home page image serves to provide an aesthetically pleasing and colourful element to the page while making clear that this site is a bookshop 

### Features
The Second Hand Shelf is comprised of 12 core sections: Home page, Signup, Login, Profile, Wishlist, Products view, Book Detail, Book Reviews, Shopping Bag view, Checkout, Checkout Success, Contact Us

* All pages feature the main nav bar, on desktop this includes the title, search bar which can search for terms in book titles, blurbs or information like the author of a book. The My Account drop down features Product Management which is only accessible for the superuser (or site management) and can be used to add, edit, or delete products. The My Wishlist page, and My Profile pages can also be accessed through this dropdown, along with being able to log out if a user is logged in. The Contact form is accessible through the Contact Us icon, and the bag icon displays up to date bag total information which can be clicked to bring the user to the Shopping Bag page. The main navbar also features a Home page link for users on mobile, the All Books link to show all products which can filtered in the menu. Books by Genre allows users to select and view only books from specific genres, and the Special Offers button allows users to view the New Releases, and Clearance sections.
* Each page also includes a footer displaying copyright information and social media links for the site
* All pages on the site are responsive across multiples different screen sizes, on smaller screens like mobile phones the top navbar is condensed into a hamburger menu to ensure the screen isn't cluttered while maintaining the same functionality as that found on larger screens.
* For all actions a user performs on the site a pop up message will appear either confirming that their requested action has been successful or giving them details of the action they've just performed. For example, adding, removing, or altering a product in the shopping bag will all be accompanied by messages unique to the action performed.

| Section | Feature | Photograph or gif |
| --- | --- | --- |
| The Home page features an image of a book shop, along with cards that showcase different books or groups of books to encourage users to view the Clearance, and Horror/Mystery sections along with the Best Seller of the month | Upon loading the site users are greeted with the home page image which aims to draw their attention as the colours pop against the white background and this immediately conveys the purpose of the site as one that sells books | ![Home Image](/docs/images/home-image.png) |
| | The Home page displays 3 cards which feature different aspects of the products available, the Clearance section to encourage users to shop for deals, the Horror/Mystery section as it's a section I enjoy, and the Best Seller of the month. Each image is clickable and brings the user to the relevant section described in the text shown | ![Book Features](/docs/images/book-features.png) |
| The Sign Up page allows users to register for an account with the site | The sign up form encourages users who already have an account to sign in instead by showing both a text link and button to redirect users to the Log In page | ![Sign Up Form](/docs/images/sign-up.png)
| | The Sign Up form asks users to input their email address which must be unique to their account, choose a username which again must be unique to their account and has a maximum length set by Django as 150 characters. The username field permits users to use special characters, numbers and letters to allow for usernames to be unique if there's a large client base. The form then asks the user to set a password, confirm their password and click the Sign Up button. All fields on the Sign Up form are required and the user cannot click Sign Up without successfully filling in these fields. | |
| The Log In page allows users to log who have registered for an account to log in to their already existing account | It encourages users who do not yet have an account to register before attempting to log in by providing a text link to the Sign Up page | ![Sign In page](/docs/images/sign-in.png) | 
| | The Log In form asks users to input their username, or email and their password, if a username or password combination is entered that doesn't exist an error displays stating "The username and/or password you specified are not correct" | ![Log In error](/docs/images/username-password-error.png) |
| | There is a radio button with the text 'Remember me' that allows users to select whether they want their log in information to be saved for the next time they visit the site | ![Remember me box](/docs/images/remember-me.png) | 
| | Django comes with ready-made password reset functionality so users are able click a link stating they forgot their password. This redirects them to a page where they can enter their email address and an email with a link to reset their password is sent to their specified address | ![Password Reset](/docs/images/password-reset.png) |
| The Profile page includes sections for a user's default delivery information, and their order history | The Profile page allows users to input their default delivery information so this information can be saved to their account and autofill on the checkout page, this isn't only a quality of life change but might encourage more users to go through with a purchase if the system is quick and easy | ![Default Delivery Information](/docs/images/default-delivery.png) | 
| | The Profile page displays a user's order history with information including their order number, date and time of purchase, the items and quantities order, and their order total. When then order number is clicked it brings users to their order confirmation which is initially displayed after a purchase made been made | ![Order History](/docs/images/order-history.png) |
| The My Wishlist page allows users to view and edit their wishlist, though only if they are logged in | If a user has no items in their wishlist they are met with a message 'You currently have no books in your wishlist, click the button below to find your new favourite read...'. Along with a button that redirects users to the All Books page | ![No books in wishlist view](/docs/images/wishlist-empty.png) |
| | When a user has added an item to their wishlist they can view this book in their My Wishlist page, here the book cover image, title, author and blurb are displayed. The price on this page is displayed as the price for quality 'Great', with text explaining that qualities of 'Fair' and 'Good' will be reduced. There is also a button where users can remove this item from their wishlist. | ![Wishlist with book](/docs/images/wishlist.png) |
| The Products view shows all books available for sale, it allows users to filter by Genre or Special Offer and to sort by price, rating, alphabetised title, and alphabetised genre. | Clicking any of the genre/special offer buttons takes the user to a page that only displays books that match their request. The 'sort by...' box allows users to sort from low to high on price and rating, to let them find deals or the best books on the site | ![All Books view](/docs/images/all-books.png) |
| | The book pages (whether All Books or a filtered genre page) display books in cards with the book cover image, title, author, language, release year, price (for quality 'Great'), and the genre or special offer tag. If the book hasn't been rated or reviewed it stated 'No rating' but once reviews have been made it shows the average rating out of 5 aggregated across all users. For site managers like the superuser there are also edit and delete buttons for product stock control. Due to the amount of books displayed on each page there is a 'back to top' button to allow users to quickly and easily return to the top of the page | ![All Book Cards](/docs/images/all-books-card.png) |
| The Book Detail page is accessed when a user clicks on the title or image of a book on the All Books (or any genre/special offers) page. Each book detail page shows information about that book exclusively, along with letting users add it to their wishlist, add to their bag, or rate or review the book | This page displays the book's image, title, author, average rating (if this has been rated, otherwise it shows 'This book hasn't been rated yet'), a button to bring users down to the rating and review form, book length, year of release, price, tags, and blurb. If a user adds a book to their bag a message pops up confirming that this item has been added, and the bag icon in the navbar updates based on the price. | ![Book details page](/docs/images/book-details.png) |
| | The 'add to wishlist' button is featured prominantely above the cover image and when clicked adds the book to the user's My Wishlist page. If a book is in a user's wishlist this button changes it's text to say 'Remove from wishlist' to let users manage their wishlist without having to go into their Wishlist page | ![remove from wishlist](/docs/images/remove-from-wishlist.png) |
| | The site users dynamic pricing meaning that depending on the quality of book a user selects and adds to their bag the price will be different. A 'Great' quality item is full price, 'Good' quality has a 20% discount applied, and a 'Fair' quality is discounted by 40% due to the second hand nature of the shop. This pricing is calculated dynamically but accurate item and grand totals are presented throughout the site. Underneath the quality the user can adjust the quantity of books they wish to add to their bag, this field cannot be manipulated to be lower than 1 or higher than 99. | ![Example of dynamic pricing](/docs/images/dynamic-pricing.gif) |
| The Book Reviews section is found on each book detail page and both displays all existing reviews from users and has a form in which users can submit their own rating and review | If no reviews have been made for a book there is text which states 'This book has no reviews yet...'. If reviews have been left they are displayed in a row which differs depending on screen size and utilises a horizontal scroll bar to display all reviews cleanly and clearly. Each review card shows the username of the reviewer, the review date (where more recent reviews appear first) and the stars they awarded the book out of 5. It is mandatory that stars be awarded to leave a review but submitting a written review is optional, if a written review is left it is displayed under the star rating. For the user who wrote each review that is displayed there will be edit and delete buttons only visible and accessible to them. If a user clicks the edit button they are taken to a form that is pre-populated with the content of their original review. If a user clicks the delete button a modal pops up asking if they are sure they wish to delete this as it's irreversible. In addition only superusers can leave multiple reviews for each book (for development purposes) and users who attempt to leave multiple reviews for one book will be met with a message saying this cannot be done. | ![Book Review Section](/docs/images/book-reviews.png) |
| | The book review form itself is simple and lets users input a star rating and a written review (if they wish) before clicking the submit review button | There is a note telling users that they must add a star rating in order to submit the review, a star rating is left by hovering over the number star they wish to award the book. The written review field has a maximum character attribute of 3000 as if a written review becomes longer than the size of the review card a vertical scroll bar allows users to scroll through and read the full review without this cluttering the screen. | ![Book review form](/docs/images/book-review-form.png) |
| The Shopping Bag view is accessed by clicking the bag icon in the navbar, this page shows the current contents of the bag along with product information | If nothing is in the bag text stating 'Your bag is empty' will display along with a button encouraging users to keep shopping. When an item (or multiple) is added a success message is displayed in the top right corner of the screen to let users know that their book has been added to the bag. This message explains which book, in which quality and quantity has been added along with the price and a message that has calculated how much more the user would need to spend to get free delivery. | ![Add to bag success message](/docs/images/add-to-bag-success.png) |
| | After clicking the bag icon the user sees the contents of their bag, including the book image, title, author, quality and SKU. The quantity of the book selected can be altered here using the quantity input, if this is altered the subtotal adjusts accordingly, items can also be removed from the bag using the remove button. The bag total is displayed lower down the page along with the delivery cost and grand total, with another message stating how much more the user would need to spend to receive free delivery. From here the user can either click 'keep shopping' to return to the books page, or click 'secure checkout' to proceed to the checkout page | ![Shopping bag page](/docs/images/shopping-bag.png) |
| The checkout page shows an order summary and then asks the user to fill out the details, delivery, and payment form to complete their order | The order summary consists of the book cover image, title, author, quality, and quantity with it's subtotal. The Delivery cost and grand total are displayed again | ![Checkout Summary](/docs/images/checkout-summary.png) |
| | The checkout form is comprised of fields for Full Name, Email Address, Phone Number, Street Address, Town or City, Post Code, and a dropdown country selector. There is also a radio button where users can opt to save this delivery information to their profile if they're logged in. If a user has previously opted to save information to their profile this form will be auto populated. The payment field is at the bottom of the form where users can enter their card details, along with a buttons that either redirect the user back to their bag or complete their order with Stripe validating their details. There is also a message displayed in red underneath this 'Complete Order' button to warn users that their card is about to be charged, and how much. All required fields of the form must be entered for the 'Complete Order' button to be clicked and the order to be successfully processed. When the 'Complete Order' button is clicked a green overlay appears on screen with a spinning arrow circle to demonstrate that the order is being processed. | ![Checkout Form](/docs/images/checkout.png) |
| The checkout success, or thank you page is reached after an order has been processed and displays the order information | The page confirms that the order has gone through successfully and tells the user which email their confirmation will be sent to. A development example of this confirmation email is shown in the images section of this table, and upon deployment this will send the confirmation email to the users real email address | ![Order confirmation email](/docs/images/order-confirmation-email.png) |
| | The order success page confirms the following details: order number, order date, the item(s) ordered along with the quantity, the full delivery details provided, and the full billing information. Below this is a button encouraging users to 'Check out the latest deals' which would redirect them to the clearance page and new releases page| ![Order confirmation](/docs/images/order-confirmation.png) |
| The Contact form can be accessed whether a user is logged in or not, and simply asks users to fill in the following information: their name, email, subject line, and message, a button is shown below to allow users to submit their message | All fields in this form are required and the form cannot be submitted without all being filled in correctly | ![Contact Form](/docs/images/contact-form.png) |
| | The contact form is set up to send a confirmation email to the user with their their message subject, and content repeated back to them so they have a copy of the communication. The email also states the Second Hand Shelf will respond within 48 hours, but if the message is urgent a contact number is listed | ![Contact form confirmation](/docs/images/contact-confirmation.png) |

* Future Implementations:
  * Ideally, I would like to streamline the process for site managers to add products to the site, the form works fine with every detail being easily input apart from the book quality and price variable. Currently for any new book added to the site the manager must go into the store admin and create 3 quality attributes for the book, one for 'Great' quality with a price_factor of 1.0, one for 'Good' quality with a price_factor of 0.8, and one with 'Fair' quality with a price_factor of 0.6. This seems tedious, or at worst could be forgotten by management which may cause issues with the site
  * In the future I'd like to implement functionality whereby users could resell their own books through the site much like how a site manager would upload a product currently, however this was beyond the scope of my project
  * I also wanted to potentially add a 'My Reviews' page to the site where users can view their own reviews of different books without having to search through all the existing reviews from other users. In addition, functionality whereby users could like or comment on others' reviews would make the site more engaging and interactive

### Accessibility
FINISH !!!!!!!!
* Throughout the development of this site accessibility was a priority, semantic html, alt tags, and aria-labels are used wherever possible to assist screen readers. The fonts chosen are ones I believe to be dyslexia friendly and readable no matter what screen size the user is on.
* [Lighthouse Accessibility Score]() !!!! FINISH
* I used the [Ally Color Contrast Accessibility Validator](https://color.a11y.com/) to check for any colour contrast issues and received the following result
![ALLY result](/docs/images/ally.png)
* [WAVE](https://wave.webaim.org/) was utilised to test the web accessibility of each page on the site, the results of which are fully explored in the Automated Testing section further down in this document

### Wireframes
Before development began I designed wireframes to aid in the creation of my site, when these were created I didn't intend on including a contact form so unfortunately this is missing from the wireframes

* [Home Desktop](/docs/wireframes/D-Home.png)
* [Home mobile](/docs/wireframes/M-Home.png)
* [Sign Up Desktop](/docs/wireframes/D-Sign-up.png)
* [Sign Up Mobile](/docs/wireframes/M-Sign-up.png)
* [Log In Desktop](/docs/wireframes/D-Log-in.png)
* [Log In Mobile](/docs/wireframes/M-Log-in.png)
* [My Profile Desktop](/docs/wireframes/D-Profile.png)
* [My Profile Mobile](/docs/wireframes/M-Profile.png)
* [My Wishlist Desktop](/docs/wireframes/D-Wishlist.png)
* [My Wishlist Mobile](/docs/wireframes/M-Wishlist.png)
* [Products Desktop](/docs/wireframes/D-All-Books.png)
* [Products Mobile](/docs/wireframes/M-All-books.png)
* [Book Details Desktop](/docs/wireframes/D-Book-Detail-1.png)
* [Book Details Desktop part 2](/docs/wireframes/D-Book-Detail-2.png)
* [Book Details Mobile](/docs/wireframes/M-Book-detail-1.png)
* [Book Details Mobile](/docs/wireframes/M-Book-detail-2.png)
* [Shopping Bag Desktop](/docs/wireframes/D-Shopping-bag.png)
* [Shopping Bag Mobile](/docs/wireframes/M-Shopping-bag.png)
* [Checkout Desktop](/docs/wireframes/D-Checkout.png)
* [Checkout Mobile](/docs/wireframes/M-Checkout.png)
* [Checkout Success Desktop](/docs/wireframes/D-Checkout-success.png)
* [Checkout Success Mobile](/docs/wireframes/D-Checkout-success.png)

### Languages Used
* The Second Hand Shelf used HTML, CSS, Python, and JavaScript

### Frameworks, Libraries, and Programs Used
* [Adobe XD](https://helpx.adobe.com/uk/support/xd.html) was used to create the Wireframes seen above
* [ALLY](https://color.a11y.com/) was used to test for colour contrast issues on the site
* [AWS](https://aws.amazon.com/) to hold media files
* [Bootstrap](https://getbootstrap.com/) was utilised to create a core html structure similar to Boutique Ado so that my time could be spend on providing functionality
* [CI Python Linter](https://pep8ci.herokuapp.com/#)
* [Coolors](https://coolors.co/) to create my colour palette for this README document
* [ElephantSQL](https://www.elephantsql.com/) was used to host the database for this site
* [Favicon](https://favicon.io/) was utilised to create a Favicon for my site's browser tab
* [Font Awesome version 6](https://fontawesome.com/) was used for all icons seen across the site
* [Gifox](https://gifox.app/) was used to create a video/gif to demonstrate feature functionality for this readme document
* [Github](https://github.com/) was used to store the repository for this quiz project, with Github Pages hosting the site
* [Gitpod](https://www.gitpod.io/) is the environment in which this project was created and worked on
* Google Chrome Developer Tools was used as a debugging tool, and to help visualise the site in different screen sizes to ensure that user experience remained clean and efficient no matter the screen size
* [Google Fonts](https://fonts.google.com/) provided the links for both fonts used on the site, and aided in selecting fonts that are complimentary to one another
* [Heroku](https://www.heroku.com/?) was used in addition to Github as the deployment platform for this site due to the use of databases
* [Jigsaw W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate CSS used
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) was used as a templating language 
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) to test the quality and responsiveness of each page on the site
* [Tech Sini](https://techsini.com/multi-mockup/index.php) aided in the creation of a multi-device mockup image so that I could test the appearance and functionality of the site on multiple device sizes, and provided the image seen at the beginning of this document
* [WAVE](https://wave.webaim.org/) Web Accessibility Evaluation Tool was used to test my site against accessibility criteria.
* [W3C Markup Validator](https://validator.w3.org/) to validate HTML

### Deployment

The Second Hand Shelf is deployed using Heroku by the following steps:

Elephant SQL
1. Go to [ElephantSQL](https://www.elephantsql.com/) and either create an account or login via Github
2. Click the 'Create New Instance' button
3. Choose your plan (The Tiny Turtle free plan is acceptable), name your instance and leave the tags blank if you wish then click the 'Select Region' button
4. Select a data centre that is closest to you
5. Click the 'Review' button
6. Double check your details then click the 'Create Instance' button
7. Navigate to the ElephantSQL dashboard and click on the database instance name you provided for this project
8. In the URL section copy the database URL to your clipboard
9. We will shortly return to this tab so leave it open

Heroku
1. Log into Heroku and click the 'New' button, then the 'Create a new app' button
2. Enter a name for your app (this must be unique), choose the region that is closest to you and click the 'Create app' button
3. Click 'Reveal Config Vars'
4. Navigate back to your ElephantSQL tab and ensure the database URL is copied to your clipboard
5. On Heroku add a config var named 'DATABASE_URL' and paste your ElephantSQL database URL as the accompanying value, then click 'Add'
6. Add all other necessary environment variables to this config var section from your project's .env file apart from the DEVELOPMENT variable
7. Find the 'Deploy' tab for your app on Heroku and click it
8. In the Deployment method section click 'Connect to Github', type your repo name and click 'Connect'
9. Click 'Enable Automatic Deploys' to ensure that your Github repository and Heroku are synced if you make any further code or project changes
10. Click 'Deploy Branch' to let Heroku begin building the site
11. We must now initialise our empty database by clicking 'More' then 'Run console'
12. In the terminal that has appeared type 'from second-hand-bookshop import db' and click enter
13. Now type 'db.create_all()' and hit enter again
14. Type 'exit()' to exit the python terminal and close the console, our Heroku database will now contain the tables and columns created from our models.py files
15. Click the 'Open app' button to visit your built site

AWS
1. Navigate to [AWS](https://aws.amazon.com/), login or create an account if you don't already have one
2. Search for S3 in Services, and click the 'Create bucket' button
3. Enter a bucket name (this should relate to your heroku app name), select the region closest to you
4. Uncheck 'Block all public access' and acknowledge that the bucket will be public, click 'ACLs enabled' and 'Bucket owner preferred', click 'Create bucket'
5. Click the bucket instance you just created and navigate to the Properties tab
5. Scroll down to 'static website hosting' and click 'use this bucket to host a website'
6. Enter default values of index.html for the Index document, and error.html for the Error document then click 'Save'
7. On the Permissions tab paste the following code into the CORS configuration editor: 
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
8. Click 'Save'
9. Navigate to 'Bucket Policy' and select 'policy generator', the type of which is 'S3 Bucket Policy', type * into the Principal field, and select 'get object' for the action
10. Copy your arn from the Bucket Policy tab and paste this into the ARN field on the policy generator page, then click 'Add Statement', then 'Generate Policy'
11. Copy the code displayed to your clipboard and paste this into the Bucket Policy editor. Before saving add a '/*' to the end of the Resource key, then click 'Save'
12. Navigate to the 'Access Control List' tab, click 'edit' and enable List for Everyone (public access) and accept the warning box
13. From the AWS site search for 'IAM', click 'User Groups' and then click 'Create New Group'
14. Name this group something that makes sense for the logic of your project, I named this 'manage-second-hand-shelf', then click 'Create Group'
15. From the IAM dashboard click 'Policies' then 'Create Policy'
16. Click the 'JSON' tab and select 'import policy', search for 'S3' and import the 'AmazonS3FullAccess' policy
17. Find your arn from the Bucket Policy page in S3 and copy this, paste this into the 'Resource' key in the JSON tab instead of the '*' value. The format should be
"Resource": [
    'your_arn_here',
    'your_arn_here/*'
]
18. Click 'Review Policy', give it a name and description, e.g name: second-hand-shelf-policy, description: Access to S3 bucket for Second Hand Shelf static files
19. Click 'Create Policy'
20. Navigate back to the 'User Groups' page and click on the group you created
21. Click 'Attach Policy', search for the policy you just created and select it, then click 'Attach Policy'
22. Finally navigate to the 'Users' page and click 'Add User'

How to Fork the Second Hand Shelf
1. Login to your Github account
2. Navigate to the 'second-hand-bookshop' repository and click the 'Fork' button in the top right corner

How to Clone
1. Login to your Github account
2. Navigate to the 'second-hand-bookshop' repository
3. Click the green 'Code' button next to the 'Gitpod' button
4. Click 'Open with Github desktop'
5. Click the 'Choose...' button and navigate to a local path where you wish to store the cloned repository
6. Click the 'Clone' button

## Testing
### Automated Testing

### W3 Nu HTML Validator
The W3 Nu HTML Validator was used multiple times throughout development to ensure the HTML used was all up to industry standards, the results are as follows:

* [Home page](/docs/images/home-html.png)
* [Sign Up page](/docs/images/sign-up-html.png)
* [Log In page](/docs/images/login-html.png)
* [Product Management page](/docs/images/product-management-html.png)
* [Wishlist page](/docs/images/wishlist-html.png)
* [Profile page](/docs/images/profile-html.png)
* [Contact Us page](/docs/images/contact-html.png)
* [All Books page](/docs/images/all-books-html.png)
* [Book Detail page](/docs/images/book-detail-html.png)
* [Shopping Bag page](/docs/images/shopping-bag-html.png)
* [Checkout page](/docs/images/checkout-html.png)
* [Checkout Success page](/docs/images/checkout-success-html.png)

### W3C CSS Validation Service
The W3C CSS Validation Service was used to validate the two CSS files contained within the project, the results are as follows:

* [Base.css](/docs/images/base-css-validator.png)
* [Profile.css](/docs/images/profile-css-validator.png)

The only CSS warnings given were '-webkit-user-select', '-moz-user-select', and '-ms-user-select' are vendor extensions so I didn't feel these needed to be addressed as they don't comprise the quality of the css

### JS Hint
JS Hint was used to validate the JavaScript found throughout the project with the results being:

* [Profile](/docs/images/profile-JS-Hint.png)
* [Stripe](/docs/images/Stripe-JS-Hint.png)
* [Quality Price Calculator](/docs/images/quality-price-calculator-JS-Hint.png)
* [Quantity Input Calculator](/docs/images/quantity-input-calculator-JS-Hint.png)

No errors were found on any of the JavaScript files or exerpts used, the screenshots show 'One undefined variable' being listed for multiple files but doesn't provide an explanation of this, or which variable it thinks is undefined. For this reason, along with me manually checking each file I have chosen to ignore this warning

### Python Linter

The following files were tested with a [Python Linter](https://pep8ci.herokuapp.com/) to ensure PEP8 compliance, and all files apart from settings.py passed with no errors.

* [Bag contexts.py](/docs/images/bag-contexts.png)
* [Bag views.py](/docs/images/bag-views.png)
* [Bag urls.py](/docs/images/bag-urls.png)
* [Bookshop urls.py](/docs/images/bookshop-urls.png)
* [Bookshop settings.py](/docs/images/settings.png)
* settings.py in the Bookshop app was the only file to show line length warnings, these affected the AUTH_PASSWORD_VALIDATORS and were not created, or updated by myself so I have left them as Django intended
* [Checkout admin.py](/docs/images/checkout-admin.png)
* [Checkout context.py](/docs/images/checkout-context.png)
* [Checkout forms.py](/docs/images/checkout-forms.png)
* [Checkout models.py](/docs/images/checkout-models.png)
* [Checkout urls.py](/docs/images/checkout-urls.png)
* [webhook-handler.py](/docs/images/webhook-handler.png)
* [webhooks.py](/docs/images/webhooks.png)
* [Contact admin.py](/docs/images/contact-admin.png)
* [Contact forms.py](/docs/images/contact-forms.png)
* [Contact models.py](/docs/images/contact-models.png)
* [Contact urls.py](/docs/images/contact-urls.png)
* [Contact views.py](/docs/images/contact-views.png)
* [Home urls.py](/docs/images/home-urls.png)
* [Home views.py](/docs/images/home-views.png)
* [Products views.py](/docs/images/product-views.png)
* [Products admin.py](/docs/images/products-admin.png)
* [Products forms.py](/docs/images/products-forms.png)
* [Products models.py](/docs/images/products-models.png)
* [Products urls.py](/docs/images/products-urls.png)
* [Profile forms.py](/docs/images/profile-forms.png)
* [Profile urls.py](/docs/images/profile-urls.png)
* [Profile models.py](/docs/images/profiles-models.png)
* [Profile views.py](/docs/images/profiles-views.png)

### Wave Testing
* I assessed my site using WAVE before and after deployment to ensure there were no web accessibility issues present. The results of these tests are below:
* [Home page](/docs/images/WAVE-Home.png), the only warning present for the home page referred to a 'Skipped heading level' this relates to the page title being a h2, and the delivery banner being h1. If I altered this so that the title was a h1 and the delivery banner was lower I receive a warning about there not being a h1 heading on the mobile version of the page. Therefore, I am happy to leave this warning as it is
* [All Books page](/docs/images/Wave-all-books.png), there are 218 warnings listed as WAVE reported 2 warnings on the page which are multiplied by the number of books displayed. The warnings they raised are having a 'Redundant link' users can click the book cover image or the title to be taken to the book detail page, this is by design to give users choice. The other warning states that the price variable could be a 'Possible heading', I want the price variable to be a paragraph tag so that it fits in aesthetically with the book title, author, and other informational fields.
* [Book Detail page](/docs/images/Wave-book-detail.png) the only warning present here is a 'Suspicious link text' related to the 'Click here to Rate or Review' button, I feel as though this button text is clearly descriptive to users
* [Sign Up page](/docs/images/Wave-signin.png) 
* [Registration page](/docs/images/Wave-sign-up.png)
* [Contact page](/docs/images/Wave-contact.png)
* [Shopping Bag page](/docs/images/Wave-shopping-bag.png)
* [Checkout Confirmation page](/docs/images/WAVE-checkout-confirmation.png) The only warning presented for this page is a 'Redundant link' for the 'Check out the latest deals' button, I don't see where this link is being replicated, and the button is valuable for redirected users back to the products page
* Unfortunately I couldn't access pages that require the user to be logged in so I couldn't do WAVE testing on all pages but I have conducted manual testing on all pages.

### Lighthouse Testing
## Desktop

## Mobile

## Improvements Made

## Manual Testing
### Testing User Stories

| User Story | Was this met? | Evidence |
| --- | --- | --- |
| Viewing and Navigation | | |
| 1. Ensure the site is responsive across device sizes | Yes, the site was designed using a mobile first framework to ensure responsivity, all text is readable, and all functionality is available no matter the screen size | ![Responsivity Gif](/docs/images/responsivity.gif) |
| 2. View a large range of books for sale | Yes, There are over 100 products available on the site to ensure a wide range of books can be viewed and bought | ![Products count](/docs/images/products-count.png) |
| 3. View individual product details | Yes, a book's title or cover image can be clicked to bring a user to the product details page for that product | ![Product details page](/docs/images/product-details-view.gif) |
| 4. Easily view the total of purchases at any time | Yes, the shopping bag icon in the navbar automatically updates whenever a user adds or edits their shopping bag. A message giving a summary of the bag change also appears | ![View bag total](/docs/images/view-bag.png) |
| 5. View which books are in my wishlist | Yes, the wishlist is accessible from the navbar where users can view and manage their wishlist items, the button on book details to add a book to a users wishlist also changes to say 'remove from wishlist' when clicked to alert the user that this title is already in their wishlist | ![Remove from Wishlist button](/docs/images/remove-from-wishlist.png) |
| 6. View book reviews and ratings from other users | Yes, users can see reviews from all other users who have left them for each particular book, they also see an aggregated rating out of 5 comprised of the ratings from all users. You can see that for reviews submitted by another user there are no edit or delete buttons as only the reviewer themselves can perform these functions | ![User reviews](/docs/images/user-reviews.png) |
| Registration and User Accounts | | |
| 1. Easily register for an account | Yes, the registration process is quick and simple and the user is sent a verification email to validate their account | ![User Registration](/docs/images/sign-up.png) |
| 2. Easily login or logout | Yes, users can log in quickly and easily, with radio button functionality that allows users to select if they want their log in information to be stored for quicker log in next time | ![Log in](/docs/images/remember-me.png) |
| 3. Easily recover my password in case I forget it | Yes, on the log in page a user can click 'Forgot Password' and be brought to a page where they enter their email and are sent a password reset link. The image to the side of this shows the development version of this email, but once deployed this will be sent to a user's real email address | ![Password reset email](/docs/images/password-reset-email.png) |
| 4. Receive an email confirmation after registering | Yes, a user receives an email after submitting the registration form which provides a link for them to confirm their details and formally register their account | ![Confirm registration](/docs/images/confirm-registration.png) |
| 5. Have a personalised user profile | Yes, users can provide and update their default delivery information which makes checking out quicker and easier | ![User profile](/docs/images/default-delivery.png) |
| 6. Be able to contact site owners and receive confirmation of this | Yes, Users can submit the contact form whether they're logged in or not, upon submission a success message is displayed on screen alerting users that their message has been received. They are also sent a confirmation that their message was received with their message subject and content repeated to them along with information on when they can expect a response | ![Contact confirmation](/docs/images/contact-confirmation.png) |
| Sorting and Setting | | |
| 1. Sort the list of available books | Yes, Users can sort books by price, rating, language, and year of release from the main nav menu, on the All Books page users can also sort by price, rating, title and genre | ![Sorting](/docs/images/sorting.png) |
| 2. Sort books by genre | Yes, users can sort by Horror/Mystery, Modern Fiction, Classic Fiction along with Clearance, and New Releases, as this site was created for educational purposes only the choice of genres is limited but would be expanded if created for a client | ![Genres](/docs/images/genres.png) |
| 3. Search for a book by title or words in the blurb | Yes, users can search for books by title, author or words featured in the blurb as is evidenced in the image to the right. The search query 'help' is not featured in the titles of any of the books displayed but it is featured in the blurbs of them all | ![Search by title or keyword](/docs/images/search-by-word.png) |
| 4. Easily see what I've searched for and the number of results | Yes, the search query is quoted back to the user above the results and this message shows how many products matched that specific criteria | ![Products found](/docs/images/products-found.png) |
| 5. Be shown on the book details page whether a particular book is in my wishlist | Yes, the 'add to wishlist' button changes to a 'remove from wishlist' button when clicked the signify that it's been added/already in the user's wishlist | ![Wishlist on details page](/docs/images/remove-from-wishlist.png) |
| Purchasing and Checkout | | |
| 1. Easily select the quantity of a book when purchasing it | Yes, there is a quantity selector box on the book details page that can be used to adjust the quantity of a book added to the bag.  | ![Quantity selector](/docs/images/quantity-selector.png) |
| 2. Easily select the quality of a book when purchasing it | Yes, users can select the quality of book they wish to purchase on the book details page, the quality selected determines the price of the item. The quality they have chosen is reiterated to them in messages and on the order summary encase they want to change their mind | ![Quality selector](/docs/images/quality-selector.png) |
| 3. View items in my bag to be purchased | Yes, users can click the bag icon in the navbar to be taken to their shopping bag where a summary of their order is displayed. When an item is added to the bag a success message is shown to confirm this action and give an updated bag summary| ![Bag summary](/docs/images/shopping-bag.png) |
| 4. Adjust the quantity of individual items in my bag | Yes, on the 'Shopping Bag' page there is a quantity selector to allow users to change and update the quantities of individual books in their order | ![Bag quantity selector](/docs/images/bag-quantity-selector.png) |
| 5. Easily enter my payment information | Yes, users can simply enter their delivery information which when logged in can be saved and autofilled to expedite the process, then must enter their card number, expiry date, and CVC | ![Payment details](/docs/images/payment.png) |
| 6. Feel my personal and payment information is safe and secure | Yes, payment information is handled by Stripe with none of this information being stored in the site database. Stripe is a certified PCI (Payment Card Industry) Service Provider which shows users that their information is safe. Personal information stored by the site would not be sold or reused for any purpose beyond allowing the registration of users, and the completion of orders | |
| 7. View an order confirmation about checkout | Yes, upon the completion of the checkout users are redirected to a page that details their order confirmation and summary. This document is also available through the users Profile (if logged in) in their order history section | ![Order confirmation](/docs/images/order-confirmation.png) |
| 8. Receive an email confirmation after checking out | Yes, users receive an email confirmation as soon as checkout has been completed, this message includes basic information about the order | ![Order confirmation email](/docs/images/order-confirmation-email.png) |
| Admin and Store Management | | |
| 1. Be able to add books | Yes, if you are logged in as the superuser you can access the product management section which brings you to a form to add new books, if an image isn't provided for this new book a default will be uploaded | ![Add a book](/docs/images/add-a-book.png) |
| 2. Be able to edit/update a book | Yes, underneath each book in the all books and book detail pages there is an 'edit' button that when clicked brings the superuser to a pre-populated form whereby they can change any book information, including editing the price if there was a sale on | ![Edit/update a book](/docs/images/edit-a-book.png) |
| 3. Be able to delete a book | Yes, a superuser can delete a book by clicking the 'delete' button underneath books in the all books and book detail pages and after doing so they will see a confirmation message | ![Delete a book](/docs/images/delete-a-book.gif) |

### Full Testing

The Second Hand Shelf site has been continually tested throughout development, including both manual and automated testing as shown above in this document

* General:
  * All navbar links direct the user to the correct page when clicked and items like Product Management do not appear unless the superuser is logged in
  * All links throughout the site were tested and all bring users to the correct page or initiate the expected action
  * For all actions taken on the page (i.e logging in, adding a book to your bag) will trigger a message in the top right corner confirming the action has been registered
  * When a term is entered into the search bar and the search button is clicked it will display the products that match this query in terms of the title, author, or blurb
  * All social media links in the footer direct the user to a new page when clicked 
* Home page:
  * The navbar hamburger icon drops down the navbar menu when clicked on mobile/smaller screens and each dropdown within the navbar displays correctly with links bringing users to the correct pages
  * Each book feature when clicked links the user to the relevant page described on the feature card
* Login page:
  * Users must enter the correct username and password in order to login or they're met with an error message stating that this is not correct
  * The 'forgot password' link brings users to the correct page and they are sent an email with a link to reset their password
  * The 'remember me' radio button when clicked means that users log in information is saved for the next time they try to access their account
  * When a user logs in they're redirected to the home page
* Sign up page:
  * The email address must be in email format using a '@' symbol in order to submit the form, the email address must be entered the same way twice for validation to occur
  * The username must be unique and can only include letters, numbers, and the following symbols @, ., +, -, _, otherwise an error message will appear
  * The value of the password (again) field much match the value of the password field for the form to be submit
  * When the form is submit the user is sent an email to confirm and validate their account, when the link in this email is clicked the user is able to log in with their details
* My Account dropdown:
  * When Product Management is clicked it brings the superuser to the add book form where all required fields must be filled in to submit the form. The 'edit' and 'delete' links on the all books and book detail pages direct to the correct pages/actions and can only be accessed or seen by the superuser
  * Clicking 'add to wishlist' on the book detail page for a product adds this book to the user's wishlist which can be viewed by clicking the 'My Wishlist' tab, this also updates the button to say 'remove from wishlist'. When the remove from wishlist button is clicked the book is removed from the wishlist
  * If a user clicks the 'My Profile' link, enters their default delivery information and clicks 'update information' this information is saved and will be used to autofill the checkout details form
  * Each time a user who is logged in places an order it will appear in the order history section of the My Profile page, all information shown here is correct and clicking the order number brings the user to the order confirmation page shown when checkout was finalised
* Contact Us page:
  * The contact us page can be accessed regardless of whether a user is logged in, all fields are required and must be filled in to submit the form, the email address must be in a valid format or an error message will show
  * The content field has a maximum character limit of 2000 to allow users to submit a reasonably in depth message to the site owners. Any characters above 2000 will not be registered by the field
  * When the user clicks the 'send your message' button they are redirected to the home page with a success message appearing and an email being sent confirming their message has been received
* All Books page: 
  * Clicking all books in the navbar allows user to filter books based on price, rating, language, and year of release, or to view all books. By clicking 'all books' users can choose to view different genres (also possible from the navbar dropdown) or special offers. There's a 'sort by' dropdown where users can choose to sort from price, or rating, high to low, and title or genre alphabetically or in reverse. If a user chooses to sort by rating the rating given by other users determines a books position
  * The back to top button sits in the bottom right side of the screen and when clicked brings the user back to the top of the page
* Book detail page:
  * The book detail page features the 'add to wishlist' button which does as it suggests, and changes to 'remove from wishlist' when clicked
  * A button stating 'Click here to rate or review' brings users to the review section of the page
  * Choosing a book quality from the quality selector alters the price displayed based on internal calculations, and the quantity can be adjusted by using the quantity selector
  * The 'Add to bag' button adds an item in it's selected quality and quantity to the shopping bag and triggers a message confirming this action
  * Users must be logged in to rate or review a book
  * If there are no reviews for a book text describing this will be shown, otherwise all reviews left for that particular book are displayed with edit and delete buttons on each that are visible and accessible only to the user who submitted the review. If a user leaves a review then clicks 'edit' the review form will be pre-populated based on the details of their original review 
  * The star rating field logs the correct value according to how many stars are coloured in green when the user clicks the star they wish to rate the book 
  * The written review is optional and the form can therefore be submitted without this being filled in, though the star rating is required and the form will not submit without it
  * The written review field has a maximum length of 3000 characters to ensure users have as much freedom as possible in writing their review
  * A superuser can leave multiple reviews per book for development and testing purposes but other users are only permitted to leave 1 review per book, if they attempt to add another they are given a warning message
* Shopping Bag page:
  * If the user has nothing in their shopping bag the page will be empty aside from a message that states 'Your bag is empty' with a button encouraging the user to view the books on offer
  * When a book is added to the shopping bag a success message detailing the bag contents is shown, clicking either 'Secure checkout' or the bag icon brings the user to the shopping bag page. Here a summary is shown and users can adjust the quantity of items, or remove them, clicking 'Secure checkout' here brings user to the checkout page
* Checkout page:
  * If users are logged in and have saved information to via their profile the checkout details form will be pre-populated with this data, all required fields must be filled in in the correct format
  * Ticking the 'save this delivery information to my profile' radio box updates the saved information stored in the users profile
  * The correct information is displayed as calculated by the item quality and quantity in the bag
  * Clicking 'Complete order' when the form has been correctly filled out initates a spinning green overlay to indicate the order is being processed and then users are redirected to the checkout success page
* Checkout Success page:
  * The checkout success page displays a confirmation that the order has been processed along with an order summary featuring key information 
  * An email is sent to users confirming their order has been successfully processed

* Update:
  * After deploying the site I now have evidence that confirmation emails are sent to users' actual email addresses, the screenshots of these will be linked below:
  * [Registration Validation](/docs/images/confirm-your-email.png)
  * [Contact Form Confirmation](/docs/images/contact-confirmation-email.png)
  * [Order Confirmation](/docs/images/order-confirmation-real-email.png)

## Bugs 

| Bug | Has this been solved? | How? |
| --- | --- | --- |
| 1. When creating the Contact form I received an error stating 'cannot access local variable 'form' where it is not associated with a value' [e.g](/docs/bugs/bug1.png) | Yes | In contact views.py I defined a variable as contact = form.save() so I could access the form data and return/repeat this to the sender of the message in a confirmation email |
| 2. In the contact confirmation email entire form blocks were being returned and displayed to the user instead of just the input values like I intended, [e.g](/docs/bugs/bug2.png) | Yes | I realised I was using {{ form.name }} in the confirmation email txt file so I changed the Jinja template tag to {{ contact.name }} etc and the correct information was displayed |
| 3. The averagerating variable in my HTML templates displayed the average rating accurately but the admin value was a step behind. For example if I rated a book a 5, admin would show 0, then if I rated it a 3, admin would show 5 | Yes | I moved the code block 'product.averagerating = product.get_rating()' 'product.save()' after the review was initialised and saved within the add_book_review() function |
| 4. [This](/docs/bugs/bug4.png) bug occured when trying to checkout early on in development, the Stripe secret key and potentially other environment variables were not being loaded or accessed appropriately, preventing checkout | Yes | I created a .env file (which I ensured was covered by .gitignore) and declared my Stripe environment variables there, along with exporting them in the terminal and saving them to the Gitpod environment variables section |
| 5. [This](/docs/bugs/bug5.gif) bug rendered my quantity update button non-functional where if the quantity was altered and 'update' was clicked the page would refresh and revert back to the original quantity | Yes | I discovered that the placement of my text_quality code was potentially producing an additional quality parameter, [evidenced here](/docs/bugs/quantity-update-bug.png) and assigning the quality value from a string representing a number (on which calculations could be performed) to a string representing the text_quality value. I moved the relevant code and this became functional once again |
| 6. My most problematic and time-consuming bug was a bug related to the book quality being accurately logged and representing during and after checkout. As seen [here](/docs/bugs/bug6.png) in the admin an order would display the correct quality and price factor in the bag but after checkout was completed each book would be stored as a default quality of 'Great' meaning pricing was not being accurately calculated | Yes | With the help of tutor support I altered the book_quality field on my OrderLineItem model to a ForeignKey pointing to the Quality model so I could access it's price_factor field. I then overwrote the save function for the OrderLineItem model to calculate the lineitem_total by multiplying the product's full price by the relevant book quality price factor, multiplied by the quantity of items bought. I then had to calculate a quality_instance based on the product and it's price factor in order to save this to the OrderLineItem model so the price could be represented accurately in the checkout HTML templates |
| 7. After deploying my site to Heroku the Contact Form served a 'Server Error (500)' when the form was submit [e.g](/docs/bugs/contact-error.png). After setting DEBUG to True in Heroku Config Vars and settings.py I received the following [error message](/docs/bugs/contact-expanded-error.png) | Yes | I found [this](https://stackoverflow.com/questions/73462412/how-can-i-fix-not-enough-values-to-unpack-expected-2-got-1) post on StackOverflow which suggested to remove trailing commas from the 'if request.method == 'POST':' block and this resulted in the form being successfully submit and an email being received |

## Credits
### Code Sections/Tutorials
* For the automatically updating copyright date I used [Kerstin Martin's](https://kerstinmartin.com/blog/copyright-notice) blog post
* To position my footer properly I used [Matthew James Taylor's](https://matthewjamestaylor.com/bottom-footer#problem) Bottom Footer article and used Flexbox to accomplish this
* To develop my Contact model I took inspiration from Github user (and CI alumni) [ShonaOB](https://github.com/ShonaOB/terrariumsupplies/blob/main/communications/models.py) and adapted the functionality of this to fit my individual needs
* To develop the foundation of my wishlist functionality I used the [Very Academy](https://github.com/veryacademy/django-ecommerce-project/tree/main/Part-07%20Wish%20List) Django Ecommerce project Github repo as inspiration 
* For the book rating and review functionality I utilised Github user [SteinOveHelset's](https://github.com/SteinOveHelset/saulgadgets/tree/master/apps/store) SaulGadgets repo as a base and altered the design and functionality to fit the book review format, also adding defensive programming
* For the functionality of the star rating radio input itself I utilised [this](https://bbbootstrap.com/snippets/bootstrap-rate-your-experience-template-star-ratings-30972576) Bootstrap example and altered it to my needs

### Other Credits
* To establish the beginning of my products.json file I utilised the data from Github user Benoitvallon with his [100 Best Books](https://github.com/benoitvallon/100-best-books) project. I altered and formatted this json file to fit the needs of my project and added additional books to fill out different genres

### Media
* The Title, author, page length, language, year of release and blurb for each book not found within the 100 Best Books attributed above were sourced from [Goodreads](https://www.goodreads.com/) 
* The book cover images for Classic Fiction (those from the 100 Best Books) were sourced from Benoitvallon's Github repository
* All books in the Horror/Mystery section were sourced from [Waterstones](https://www.waterstones.com/)
* Images for the books in the Modern Fiction genre were sourced from Goodreads
* The book cover for the title 'Maggots Screaming' was sourced from [Goulish Books](https://perpetualpublishing.com/product/maggots-screaming/)
* The hero image on the Home page was sourced from Ugur Akdemir on [Unsplash](https://unsplash.com/photos/wBhsiYCkSIs)
* The icon used to create the Favicon for the site was sourced from [Flaticon](https://www.flaticon.com/free-icon/library_405692?term=book&page=1&position=61&origin=search&related_id=405692) created by Freepik
* All other text was created by myself (Skye Hillier-Milton) 

## Acknowledgements
* I'd like to acknowledge the authors of code sections and other helpful material credited above as without their work this project may not have achieved what it has
* I'd like to thank my college mentor Robert Mclaughlin, and my CI mentor Akshat Garg for their input and advice throughout the development of this project and throughout the course itself
* I'd finally like to acknowledge the work of multiple different members of the Code Institute Tutor Support who were vital in the resolving of several bugs, and the implementation of some functionality