# desktop-password-generator
This is the desktop password generator which allows to generate as many passwords as needed with as many symbols as needed. The exact number of passwords and symbols can be determined by user.

Composition of files in the project: 

    - design_password.py - description of the used elements such as buttons, text fields, labels and the main window.
    - icon.png - the icon which is used in the window program in the name of the program.
    - project.py - the main file with the program and its description and logic.
    - test_project.py - the test file where functions from the project.py is tested using pytest.
    - complaints_number_*.txt (optional) - the text file created after the pressed button "Life is hard". The file may be deleted.
    - requirements.txt - the file with necessary modules which should be installed.

About the interface: there is an icon in the left corner of the window program which is a file "icon.png". There is a name "Password Generator" at the top of the window. The program launches in the full view mode by default. It is the function "toggle_fullscreen" in the file project.py which is responsible for this launch by default.

Inside of the window program there are 2 number field where user can enter the number of passwords to generate and the number of desired symbols in these passwords. Fields are for numbers and it won't work with empty fields or filled with characters which will be said with the red text "Passwords are null" below the Generate button. After the number of passwords and the number of symbols are entered it is necessary to press the button "Generate" to generate password. The result will be put in the text area below the "Results" label. Afterward passwords may be copy from that area in the necessary place. In the file project.py functions "btn_clicked", "password", and "on_click" are responsible for the program logic and changing texts. 

There is a button "Life is hard" which creates and opens in a text editor installed by default a text file with the first row "Tell me about it here. Safe space". Sometimes anyone may feel owerwhelmed and it is possible to write anything in this file if necessary. The file will be saved in the same directory as the project is. The function "complaints" in the project.py is responsible for creating of this file. The name of this file will be generating as "complaints_number_*.txt", where "*" is a random number from 0 to 100. If after the presssing the button "Life is hard" nothing has happened, probably the file with this name already exists. Try to press the button again or to delete existing files.

There is a button "Get bored" which finds a random article on wikipedia website and opens it in a web browser. The button may work multiple times. The function "get_bored" sends a GET request and opens this url using the default browser.

The button "Exit" closes the program.

    ## How to Run 🚀

    - Install the required dependencies: pip install -r requirements.txt
    - Run command in the project directory: python .\project.py
