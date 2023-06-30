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
The Second Hand Shelf is comprised of 12 core sections: Home page, Login, Signup, Profile, Wishlist, Products view, Book Detail, Book Reviews, Shopping Bag view, Checkout, Checkout Success, Contact

| Section | Feature | Photograph or gif |
| --- | --- | --- |
| The Home page features an image of a book shop

