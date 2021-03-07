## Welcome to SE Lab Project "Factory Simulation":

---
### Login Window:
This Window allows a User to Login after they have provided their  
correct Username and Password. If Wrong credentials are provided  
then an Error Message will be displayed

![Login Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Login.png)

**SignUp Button:** This button opens up *"The SignUp Window"*.  
**Forgot Password:** Clicking here opens up *"The Forgot Password Window"*.

---
### SignUp Window:
This Window allows a New User to create an account by providing  
their details and *The Secret Key*. The Secret Key is given by the Admin  
so that not anyone can come and make account and access anything.

If Incorrect Secret Key is provided then an Error message will be displayed.

![SignUp Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/SignUp.png)

**Submit Button:** After filling the details clicking here will create your account.  
**Back Button:** Clicking here will allow us to go back to *"Login Window"*.

---
### Forgot Password Window:
In this Window we need to provide our Email_ID, using which we created  
our account, and our Password will be sent to that Email_ID.

If Incorrect Email_ID is provided then an Error Message is displayed.

![Forgot Password Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Forgot_Password.png)

**Send Button:** After providing the Email_ID, clicking will send our password  
to our Email_ID.  
**Back Button:** Clicking here will allow us to go back to *"Login Window"*

---
### Home Window:
This Window allows us to access the Machine Database, the Adjuster  
Database and the Maintenance Table. We also have access to File Menu,  
Settings Menu and Admin Settings(Only for Admin).

Below we have the Status Bar displaying the current User.

![Home Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Home.png)

**Machine Button:** Opens the *"Machine Window"* and gives access to the Machine Database.  
**Adjuster Button:** Opens the *"Adjuster Window"* and gives access to the Adjuster Database.  
**Maintenance Button:** Opens the *"Maintenance Window"* and gives access to the Maintenance Table.  

**File Menu:**  
* Machine: Same as Machine Button.
* Adjuster: Same as Adjuster Button.
* Maintenance: Same as Maintenance Button.
* Logout: Closes *"Home Window"* and opens *"Login Window"*.
* Exit: Closes the Program.

**Setting Menu:**
* User Details: Opens *"The User Details Window"*.
* Change Password: Opens *"The Change Password Window"*.

**Admin Settings Menu:**
* All User Details: Opens *"The All User Details Window"*.
* Change Secret Key: Opens *"The Change Secret Key Window"*.

---
### User Details Window:
This Window displays the details of the Current User and allows  
the User to change the details. 

![User Details Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/User_Details.png)

**Change Button:** Allows the User to edit his/her details.  
**Save Button:** Allows the User to Save the changes made.  
**Back Button:** Takes the User back to *"Home Window"*.

---
### Change Password Window:
This Window allows the User to change his/her Password.  
The User needs to first provide the Current Password, then  
type in the New Password and finally Confirm the New Password.

An Error Message will be displayed if the User does not type  
the correct Current Password or the New Password and Confirm   
Password does not match.

![Change Password Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Change_Password.png)

**Save Button:** Changes the User's Password  
**Back Button:** Takes the User back to *"Home Window"*.

---
### All User Details Window:
This Window is accessible only to the Admin and here the Admin  
can see the details of all the Users having account.

![All User Details Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/All_User_Details.png)

**Remove Button:** After selecting a particular User, allows the Admin 
to remove that particular User.
**Back Button:** Takes the User back to *"Home Window"*.

---
### Change Secret Key Window:
This Window is accessible only to the Admin.  
It allows the Admin to change his/her Password.  
The User needs to first provide the Current Secret Key, then  
type in the New Secret key and finally Confirm the New Secret Key.

An Error Message will be displayed if the Admin does not type  
the correct Current Secret Key or the New Secret Key and Confirm   
Secret Key does not match.

![Change Secret Key Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Change_Secret_Key.png)

**Forgot Secret key Button:** Opens *"Forgot Secret Key Window"*  
**Save Button:** Changes the Secret Key  
**Back Button:** Takes the User back to *"Home Window"*.

---
### Forgot Secret Key Window:
In this Window Admin needs to provide his/her Email_ID, using which he/she   
created his/her account, and the Secret Key will be sent to that Email_ID.

If Incorrect Email_ID is provided then an Error Message is displayed.

![Forgot Secret Key Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Forgot_Secret_Key.png)

**Send Button:** After providing the Email_ID, clicking will send the Secret Key  
to Admin's Email_ID.  
**Back Button:** Clicking here will allow us to go back to *"Change Secret Key Window"*

---
### Machine Window:
This Window allows the User to manipulate the Machine Table.  
The User can Insert, Search, Update and Delete records.

![Machine Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Machine.png)

**Insert Button:** Opens *"Machine Insert Window"*  
**Search Button:** Opens *"Machine Search Window"*  
**Update Button:** Opens *"Machine Update Window"*  
**Delete Button:** Opens *"Machine Delete Window"*  
**Back Button:** Takes the User back to *"Home Window"*.

---
### Adjuster Window:
This Window allows the User to manipulate the Adjuster Table.  
The User can Insert, Search, Update and Delete records.

![Adjuster Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Adjuster.png)

**Insert Button:** Opens *"Adjuster Insert Window"*  
**Search Button:** Opens *"Adjuster Search Window"*  
**Update Button:** Opens *"Adjuster Update Window"*  
**Delete Button:** Opens *"Adjuster Delete Window"*  
**Back Button:** Takes the User back to *"Home Window"*.



