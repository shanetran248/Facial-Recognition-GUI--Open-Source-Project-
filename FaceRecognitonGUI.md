# Face Recognition With GUI 
We created code that deploys a front end website. The website serves as a GUI to neatly run the face_recognition tool as opposed to runnning it via the command line. The website is generated using the python3 program we created, faceapp.py, command from the terminal. The website allows the user to add any photo and the website will detect the person based on the information the user provides.

<img width="568" alt="Screenshot 2024-11-20 at 11 37 34 AM" src="https://github.com/user-attachments/assets/cbfc58cf-e77e-41b8-9dc9-6fc63a261142">
<p><br></p>
<img width="1369" alt="Screenshot 2024-11-20 at 11 37 52 AM" src="https://github.com/user-attachments/assets/26bd999b-103d-4bcd-9eac-ad310e26c0ad">
<p><br></p>
The GUI front end is compromised of a framework including 5 different folders- Static, Templates, Known_Persons, Unknown_Persons, and faceapp.py.
<p><br></p>
<p><strong>Static</strong></p>
The static folder contains the style.css file. The style.css program is a css script that gives the GUI its apperance. Its user a very neurtal color palette, inspired by the simple palette of the Apple website. The css program also sets the color's for all the feedback buttons as well. While not neccessary for the GUI to run, our team wanted to provide a good user experience and a visually appealing website does just that.
<p><br></p>
<p><strong>Templates</strong></p>
The templates folder contains the html code for the site. Similar to the style.css program, the html program was created to provide a good user expereince. Howeve,the html code is more important as it provides the design "structure" for the entire site. Without it, all that would display would be unappealing black text.
<p><br></p>
<p><strong>Known_Persons</strong></p>
The Known_Persons folder stores the user input data for when a user provides an image for a person they want to log. The faceapp.py program reads this folder during execution. Additionally, this folder saves the user image so theres no need for a user to reenter a photo multiple times. Lastly, the program code has protections to not accept anything other that image files for this field.
<p><br></p>
<p><strong>Unknown_Persons</strong></p>
The unknown_persons folder store the user input data for when a user provides an image for a person the want to log as unknown. The faceapp.py program reads this folder during excecution, The program has protections to not accept anything other than image files for this field.
