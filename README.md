# Second Hand Shelf

Second Hand Shelf is a second hand book selling website, users can browse books by genre, or by different filtering criteria like alphabetised title, year of release, language, price, or rating. They can also view specific offers like clearance items, or new releases. Basic functionality of the site is comprised of the user being able to register for an account, log in and out, and complete orders by paying and receiving a confirmation email. Additional functionality has been added for user experience and this will be discussed further on in the document.

![Image of my responsive site]()
[Link to the deployed site]()

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
  * [Local Deployment](#local-deployment)

* [Testing](#testing)
  * [Automated Testing](#automated-testing)
    * [W3 Nu HTML Validator](#w3-nu-html-validator)
    * [W3C CSS Validation Service](#w3c-css-validation-service)
    * [Wave](#wave-testing)
    * [Lighthouse](#lighthouse-testing)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)

* [Credits](#credits)
  * [Code Sections](#code-sections)
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
* Sort multiple categories of books simultaneously
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
| | The book review form itself is simple and lets users input a star rating and a written review (if they wish) before clicking the submit review button | There is a note telling users that they must add a star rating in order to submit the review, a star rating is left by hovering over the number star they wish to award the book. The written review field does not have a maximum character attribute as if a written review becomes longer than the size of the review card a vertical scroll bar allows users to scroll through and read the full review without this cluttering the screen. | ![Book review form](/docs/images/book-review-form.png) |
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
* Lighthouse
* Ally
* WAVE

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
* [Python Checker](https://www.pythonchecker.com/) to ensure PEP8 compliance for Python code
* [Tech Sini](https://techsini.com/multi-mockup/index.php) aided in the creation of a multi-device mockup image so that I could test the appearance and functionality of the site on multiple device sizes, and provided the image seen at the beginning of this document
* [WAVE](https://wave.webaim.org/) Web Accessibility Evaluation Tool was used to test my site against accessibility criteria.
* [W3C Markup Validator](https://validator.w3.org/) to validate HTML

