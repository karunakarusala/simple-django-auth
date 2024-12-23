                                                    # Simple Django Auth
                                                                                                    
Overview
This project is a simple e-commerce page built with Django that includes user authentication features like login, logout, and registration. The main page shows three product cards that are managed by an admin page. The products' data (like name, description, and image) can be updated via the Django admin interface.

The page also supports user login, registration, and logout functionality. After registration, users are redirected to the login page, and once logged in, they can access the home page with a logout option.

                          ------------------------------## Key Features: ----------------------------
E-commerce Page: Displays three product cards with data from the  admin panel.
Admin Panel: Manage product data through the Django admin interface (accessible at http://127.0.0.1:8000/admin/cricket/destination/).
Authentication: Login, logout, and registration features implemented using Django's built-in authentication system.
Media Files: Images are stored and displayed dynamically from the media folder.
Pages:
Home Page: Displays product cards and navigation options like "Login" and "Register".
Login Page: Users can log in with their credentials.
Register Page: Users can create a new account.
After Login: Redirects to the home page with a "Logout" button.
Admin Page: Accessible for admin users to manage product data at the given URL.


                             ----------------------------------## Setup:  ------------------------
Clone this repository to your local machine.
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Apply migrations to set up the database:
bash
Copy code
python manage.py migrate
To run the development server:
bash
Copy code
#python manage.py runserver


Access the application in your browser at http://127.0.0.1:8000/.
Images:
Admin Panel: Here you can manage the product data (images, names, and descriptions) in the admin interface.
Home Page: Shows the product cards and navigational links like Login/Logout/Register.

                         -----------------------------Authentication: --------------------------
The application uses Django's authentication system to handle user registration, login, and logout.
After registration, users will be redirected to the login page.
Upon successful login, users will be taken to the home page where they can log out.
python manage.py runserver
Access the application in your browser at http://127.0.0.1:8000/.
Images:
Admin Panel: Here you can manage the product data (images, names, and descriptions) in the admin interface.
Home Page: Shows the product cards and navigational links like Login/Logout/Register.
Authentication:
The application uses Django's authentication system to handle user registration, login, and logout.
After registration, users will be redirected to the login page.
Upon successful login, users will be taken to the home page where they can log out.
This README provides a clear and easy-to-understand overview of your project, making it simple for anyone to set up and use. You can add images as necessary by including the image paths or uploading them to the repository if needed.








