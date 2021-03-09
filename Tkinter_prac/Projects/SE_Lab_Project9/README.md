## Welcome to SE Lab Project "Factory Simulation":
This Project Simulates a Factory with Machines, which can fail due to  
some issue, and Adjusters which fixes those issues to keep the Machines Running.  
Finally, The Service Manager maintains and manages everything.

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

**Send Button:** After providing the Email_ID, clicking will send our password to our Email_ID.  
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

**Remove Button:** After selecting a particular User, allows the Admin to remove that particular User.
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

**Send Button:** After providing the Email_ID, clicking will send the Secret Key to Admin's Email_ID.  
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

---
### Maintenance Window:
This Window allows the User to view the Maintenance Table.
Here the User can view which Machine is under maintenance and is  
being fixed by which Adjuster.

![Maintenance Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Maintenance.png)

**Back Button:** Takes the User back to *"Home Window"*.

---
### Machine Insert Window:
This Window lets us Insert Data into the Machine Table.  
The User fill in the details and click the submit button to  
add the record inside the table.

![Machine Insert Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Machine_Insert.png)

**Submit Button:** Inserts the Data filled into the Machine Table.  
**Back Button:** Takes the User back to *"Machine Window"*.

---
### Machine Search Window:
This Window allows the User to search for a particular Machine.  
We have to first select the *Search by* option, then type the  
search value and finally click on the *Search Button* to display  
searched Machine.

We can also display everything inside the Machine Table by Clicking  
the *Show All Button*.

Finally, we can change status of Machine by selecting the particular  
record and pressing the *Change Status Button*.

![Machine Search Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Machine_Search.png)

**Search Button:** Allows us to make searches based on our search value.  
**Show All Button:** Displays every record in Machine Table.  
**Change Status Button:** Changes the Status of the Machine which was selected.  
**Back Button:** Takes the User back to *"Machine Window"*.

---
### Machine Update Window:
This Window allows the User to Update a record in the Machine Table.  
We first type in the OID of the record which we are interested in  
updating, then we press the *Show Button* to display the details.

Now we can update the record by editing the Entry Fields.   
Finally, pressing the *Update Button* will update the record.

![Machine Update Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Machine_Update.png)

**Show Button:** Displays the record details for the corresponding OID value provided.  
**Update Button:** Updates the record.   
**Back Button:** Takes the User back to *"Machine Window"*.

---
### Machine Delete Window:
This Window allows the User to Delete a record in the Machine Table.  
The User provides the OID value for the record to be Deleted and  
pressing the *Delete Button* deletes the record.

![Machine Delete Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Machine_Delete.png)

**Delete Button:** Deletes the record for which OID was provided.  
**Back Button:** Takes the User back to *"Machine Window"*.

---
### Adjuster Insert Window:
This Window lets us Insert Data into the Adjuster Table.  
The User fill in the details and click the submit button to  
add the record inside the table.

![Adjuster Insert Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Adjuster_Insert.png)

**Submit Button:** Inserts the Data filled into the Adjuster Table.  
**Back Button:** Takes the User back to *"Adjuster Window"*.

---
### Adjuster Search Window:
This Window allows the User to search for a particular Adjuster.  
We have to first select the *Search by* option, then type the  
search value and finally click on the *Search Button* to display  
searched Adjuster.

We can also display everything inside the Adjuster Table by Clicking  
the *Show All Button*.

Finally, we can change status of Adjuster by selecting the particular  
record and pressing the *Change Status Button*.  
Firstly, status will change to "Busy" only when there is a Machine with Status   
"Failure", and the Machine Type and Adjuster Expertise should match. Secondly,    
status will change to "Idle" if initially it was "Busy".

![Adjuster Search Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Adjuster_Search.png)

**Search Button:** Allows us to make searches based on our search value.  
**Show All Button:** Displays every record in Adjuster Table.  
**Change Status Button:** Changes the Status of the Adjuster which was selected.  
**Back Button:** Takes the User back to *"Adjuster Window"*.

---
### Adjuster Update Window:
This Window allows the User to Update a record in the Adjuster Table.  
We first type in the OID of the record which we are interested in  
updating, then we press the *Show Button* to display the details.

Now we can update the record by editing the Entry Fields.   
Finally, pressing the *Update Button* will update the record.

![Adjuster Update Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Adjuster_Update.png)

**Show Button:** Displays the record details for the corresponding OID value provided.  
**Update Button:** Updates the record.   
**Back Button:** Takes the User back to *"Adjuster Window"*.

---
### Adjuster Delete Window:
This Window allows the User to Delete a record in the Adjuster Table.  
The User provides the OID value for the record to be Deleted and  
pressing the *Delete Button* deletes the record.

![Adjuster Delete Window](https://raw.githubusercontent.com/debroglie27/tensorEnv/main/Tkinter_prac/Projects/SE_Lab_Project9/FrontEnd_Images/Adjuster_Delete.png)

**Delete Button:** Deletes the record for which OID was provided.  
**Back Button:** Takes the User back to *"Adjuster Window"*.

---
## THE END 
### Thank You for reading through The Project.