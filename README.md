# FitRush

# FitRush Shopping Website
FitRush is a Full-Stack Django E-commerce Web Application that allows users to purchase gym wear, fitness equipment, nutrition plans, and workout plans.
The platform also features new arrivals, deals, and clearance sales, providing a complete online fitness shopping experience.In here [FitRush]() is the live link of the website.

---

## Project Overview

FitRush is designed to:
- Sell gym clothing, equipment and books on nutrition.

- Offer nutrition and workout plans.

- Display new arrivals, deals, and clearance items.

- Allow users to add products to cart and checkout securely.

- Provide user accounts with order history.

- Enable admins to manage products and orders.

- Store media using AWS media storage.

---

## User Stories

### Customers
1. As a customer, I want to **create an account** so I can track my orders.
2. As a customer, I want to **log in securely** so that my personal details are tied to my account.  
3. As a customer, I want to **browse fitness products by category**.
4. As a user, I want to **view product details** including images, price, and description.
5. As a user, I want to **add items** to a shopping bag.
6. As a user, I want to **checkout securely**.
7. As a customer, I want to **view my orders** so that I can know if i want to keep shopping or not.
8. As a user, I want to **view my past orders**.
9. As a customer, I want to **receive confirmation/notification messages** when I order, update or cancel an order so that I know my action was successful.  
10. As a user, I want to **purchase workout and nutrition plans**.
11. As a user, I want to see **deals, clearance, and new arrivals**.
12. As a user, I want to **receive an email telling me verify my account** when signing up.
13. As a user, I want to **receive confirmation messages** after checkout.

### Fit Rush Staff/Admin
1. As the site owner/Admin, I want to **log in as an admin/staff** so that I can manage the site.  
2. As the site owner/Admin, I want to **add, update, or delete products**.
3. As the site owner/Admin, I want to **manage deals and clearance**.
4. As the site owner/Admin, I want to **upload images using AWS storage**
5. As the site owner/Admin, I want to **view and manage customer orders**.
6. As the site owner/Admin, I want to **display products links on the homepage**.

---

## User Goals

### First-Time Visitors
1. Understand what **FitRush offers** (gym wear, equipment, nutrition & workout plans).
2. Quickly find **products by category**.
3. View **deals, clearance items, and new arrivals**.
4. Trust the site through a **professional, modern design**.

### Registered Users/Customers
1. Create an account to **store personal details securely**.
2. Browse fitness products easily using **filters and categories**.
3. View **detailed product information** before purchasing.
4. Add products to a **shopping bag**.
5. Complete purchases through a **secure checkout process**.
6. View **order history** from their profile.

### Returning Customers
1. Quickly access **saved profile details**.
2. Review **past orders**.
3. Discover **new arrivals and deals**.
4. Make repeat **purchases** easily.

## Admin/Site Owner Goals
1. Add, update, and delete **products**.
2. Manage **deals, special offers and clearance items**.
3. Upload and manage **product images using AWS**.
4. View and manage **customer orders**.
5. Control site content from the **Django admin panel/Product management page**.

---

## Features

### Navigation & User Experience

+ **Fixed navigation bar with clear links to**:
    - Home
    - All Products
    - Nutrition & Fitness Products
    - Exercise Plans
    - Special Offers
    - Profile / Login
    - Shopping Bag

- Fully responsive design for mobile, tablet, and desktop devices.
- Consistent layout and styling across all pages.

+ **Products**

- Product listing pages displaying: 
    - Product images
    - Product Names
    - Prices
    - Ratings
-  Product detail pages including:
    - Product image
    - Detailed description
    - Size and quantity selection (where applicable)
    - Add to Bag functionality
    - Related products section

+ **Shopping Bag**

    - Add products to the bag.
    - Update quantities or remove items.
    - View running total and subtotal.
    - Shopping bag contents persist across sessions.

+ **Checkout**

    - Secure checkout process.
    - Order summary displayed before payment.
    - Collection of delivery and billing details.
    - Confirmation message displayed after successful checkout.

+ **User Accounts & Profiles**

    - User authentication using Django Allauth.
    - User profile page displaying personal details.
    - Order history available for logged-in users.
    - Secure handling of user data.

+ **Nutrition & Workout Plans**

    - Dedicated section for books on fitness plans.
    - Clear plan descriptions and pricing.
    - Purchase options integrated with checkout.

+ **Deals & Promotions**

    - Dedicated Deals page.
    - Clearance section for discounted products.

+ **Defensive Design**

    - Form validation across the site.
    - User-friendly error messages.
    - Prevention of invalid actions such as empty checkouts.
    - Feedback messages for user actions.

## Keyword Research – FitRush

Keyword research was carried out to improve the website’s SEO visibility and ensure the content aligns with what potential users are searching for online.

---

### 1. Brainstorm General Topics

The first step was identifying broad topics related to the FitRush brand and its offerings.

General topics identified:
- Fitness brand 
- Gym wear
- Fitness equipment
- Nutrition plans
- Workout plans
- Online fitness store
- Fitness deals and discounts

---

### 2. Brain Dump Possible Keywords for Each Topic

A list of possible keywords was generated for each general topic, focusing on how users might search for FitRush or similar fitness services.

**FitRush / Brand**
- FitRush
- Fit Rush fitness
- FitRush gym store
- FitRush fitness products

**Gym Wear**
- gym wear online
- fitness clothing
- men’s gym wear
- women’s gym wear
- workout clothes online

**Fitness Equipment**
- home gym equipment
- fitness equipment online
- gym equipment store
- affordable gym equipment

**Nutrition & Workout Plans**
- fitness nutrition plans
- workout plans online
- beginner workout plan
- muscle building meal plan

**Deals & Promotions**
- fitness deals
- gym wear discounts
- fitness clearance sale
- workout gear offers

---

### 3. Research Keywords Using Google Search

Each keyword idea was researched using Google Search to:
- Review autocomplete suggestions
- Analyze “People also search for” results
- Identify related search terms
- Understand user search intent

---

### 4. Short-Tail and Long-Tail Keyword Selection

A balanced mix of short-tail and long-tail keywords was selected.

#### Short-Tail Keywords
- FitRush
- gym wear
- fitness equipment
- workout plans
- nutrition plans

#### Long-Tail Keywords
- FitRush online fitness store
- buy gym wear online
- affordable fitness equipment
- beginner workout plans online
- fitness nutrition plans for beginners

---

## Technologies used

### Languages:

- [Python](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.

- [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.

- [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

### Frameworks and Libraries

- [Django](https://www.djangoproject.com/): python framework used to create all the logic.

### Databases:

- [SQLite](https://www.sqlite.org/): was used as a development database.

- [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.

### Other tools:

- [Git](https://git-scm.com/): the version control system used to manage the code.

- [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.

- [Gunicorn](https://gunicorn.org/): the webserver used to run the website.

- [Spycopg2](https://peps.python.org/pep-0249/): the database driver used to connect to the database.

- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.

- [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.

- [Heroku](https://www.heroku.com): the cloud platform used to host the website.

- [GitHub](https://github.com/): used to host the website's source code.

- [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.

- [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.

- [BootStrap](https://getbootstrap.com/): was used to get some css and html codes that were then customized.

- [Mailchimp](https://www.mailchimp.com): Was used to generate the newsletter.

- [AWS](https://aws.amazon.com/): was used to store the images and static files.

- [Stripe](https://stripe.com/ie): was used to accept payments online.

- [Wireframes.cc](https://wireframe.cc/): was used to create the sketch for the website.

- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.

- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.

- [Flake8](https://flake8.pycqa.org/en/latest/): was installed to validate Python code for the website.

## File Structure

```
FITRUSH/
├── bag/                # Shopping cart logic
├── checkout/           # Checkout & payment flow
├── fit_rush/           # Django project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── env.py
├── home/               # Homepage, hero banners
├── media/              # Uploaded images
├── products/           # Gym wear, equipment
├── profiles/           # User profiles & order history
├── static/
│   ├── css/
├── templates/
│   ├── allauth/
│   ├── errors/
│   ├── includes/
│   │    ├── main-nav.html
|   |    |--- mobile-top-header.html
│   |   ├──toasts/
│   ├── base.html
├── custom_storages.py
├── manage.py
├── requirements.txt
├── Procfile
├── README.md
├── TESTING.md
└── db.sqlite3
```
---

### Wireframes

### Desktop
- [Desktop Homepage Wireframe](documentation-images/homepage-desktop.png)
- [Desktop Productspage Wireframe](documentation-images/products-desktop.png)
- [Desktop Profilepage Wireframe](documentation-images/profile-desktop.png)

### Tablet
- [Tablets Homepage Wireframe](documentation-images/homepage-tablet.png)
- [Tablets Productspage Wireframe](documentation-images/products-tablet.png)
- [Tablets Profilepage Wireframe](documentation-images/profile-tablet.png)

### Mobile
- [Mobile Homepage Wireframe](documentation-images/homepage-mobile.png)
- [Mobile Productspage Wireframe](documentation-images/products-mobile.png)
- [Mobile Profilepage Wireframe](documentation-images/profile-mobile.png)

---

## Social
### Facebook
- [Screenshot Of Post](documentation-images/facebook-page-post.png)
- [Screenshot Of Page](documentation-images/facebook-full-page.png)

## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.

---

## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com/).
- The program can be reached by the [Link](https://dashboard.heroku.com/apps/fit-rush).

### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/kenneth2-3/FitRush).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/kenneth2-3/FitRush`

---

1. Install the dependencies:

    - Open the terminal window and type:
    - `pip3 install -r requirements.txt`


1. Create a `.gitignore` file in the root directory of the project where you should add env.py and __pycache__ files to prevent the privacy of your secret data.

1. Create a `.env` file. This will contain the following environment variables:

    ```python
    import os

      os.environ['SECRET_KEY'] = 'Add a secret key'
      os.environ['DATABASE_URL'] = 'will be used to connect to the database'
      os.environ['DEBUG'] = 'True'
    ```

    *During the development stage DEBUG is set to True, but it is vital to change it to False.*

1. Run the following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
1. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter the required information (your username, email and password).
1. Run the app with the following command in the terminal:
    - `python3 manage.py runserver`
1. Open the link provided in a browser to see the app.

1. If you need to access the admin page:
    - Add /admin/ to the link provided.
    - Enter your username and password (for the superuser that you have created before).
    - You will be redirected to the admin page.

---

## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Heroku](https://www.heroku.com): for the free hosting of the website.
- [AWS](https://aws.amazon.com/): for storing the images and static files.
- [Stripe](https://stripe.com/ie): for making payments secure and fast.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [BootStrap](https://getbootstrap.com/): for bringing projects to life with powerful JavaScript plugins.
- [Ebay](https://www.ebay.com/): for getting some of the images for free.
- [Amazon](https://www.amazon.ie/): fot getting some of the images used for free.
- [jQuery](https://jquery.com/): for providing varieties of tools to make standard HTML code look appealing.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [Code Institute](https://learn.codeinstitute.net/): For giving guides and videos to help with the website.

---

## Author

Kenneth Adanma

Thank you for shopping at Fit Rush!