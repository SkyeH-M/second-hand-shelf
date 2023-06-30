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
| The Book Detail page

