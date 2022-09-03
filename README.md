# real-estate-cadastre-parser

Parser for Cadastre of real estate of Slovakia. Use it to get useful data from cica.vugk.sk

# Introduction
Dear user, in this repository I published my Open Source project. You are free to download this program and use it for your purposes. Purposes can be commercial or personal or anything else. 

Use this tool to find people in Slovakia, who already have a real estate mortgage in Slovakia, and probably you would like to offer these people more beneficial mortgage.

This program will generate you a CSV file with names and mortgages from HTML files downloaded from website https://cica.vugk.sk/LV_vyber.aspx.

# What is it? What can I use it for?

Let me briefly give you an example of how the program can be used.

1. Visit website CICA (https://cica.vugk.sk/LV_vyber.aspx).

2. Select relevant items in formular and click "Vytvor LV" ("Create list of property"):

![image](https://user-images.githubusercontent.com/32093806/188265598-bf1ba294-7fa7-4bab-b010-e53d9f5ea42b.png)

3. There you will have A LOT OF information:

![image](https://user-images.githubusercontent.com/32093806/188265663-e32ab896-3ce2-467e-899a-eca8de16e985.png)

4. Save the entire page with Ctrl + S:

![image](https://user-images.githubusercontent.com/32093806/188265688-3c14e66e-1382-477f-b147-cee8fe2bc0da.png)

5. Now the most interesting part. Open the folder where you have downloaded the program from this repository.

![image](https://user-images.githubusercontent.com/32093806/188265921-a95db284-6335-45af-9c58-f4c36e53850d.png)

6. You should have Python 3.9 installed on your computer to run (actually I don't give a fuck how exactly you will run the script, you already have the script so work a little with your brains and try to use it somehow, as my grandpa said - if a human want he will find a way to reach the goal).

7. Install all the neccessary modules:
- xmltojson
- pandas
- (maybe) json
- (maybe) argparse

8. Run the program through the command line with the following command (it is abstract, transform it to your needs):
`D:\Other\Projects\real_estate_parser\ve\Scripts\python.exe D:/Other/Projects/tolan/main.py --path "D:\Other\Projects\real_estate_parser\lists_of_property\LV 10073.html" --output "D:\Other\Projects\real_estate_parser\output 10073.csv"`

9. If you are a lucky guy you will receive a CSV file with parsed data:

![image](https://user-images.githubusercontent.com/32093806/188267821-10d5aed7-a371-45d4-98b5-de01b03341aa.png)

10. Open Excel (hope you have Excel, or any another alternative), create new blanc document:

![image](https://user-images.githubusercontent.com/32093806/188267854-9a5a7dee-1ec1-4872-a71e-87414ad077d7.png)

11. Go to "Data" and select "From Text/CSV"

12. Select the newly generated file "output LV 10073.csv" (file name is abstractive, you can have it different) and import the data.

![image](https://user-images.githubusercontent.com/32093806/188267932-61b9f3fb-95e7-4f3b-aa9a-d4e6c7aed94d.png)

13. Press "Load":

![image](https://user-images.githubusercontent.com/32093806/188267953-ac2dca92-70ae-43e4-be8f-484451ff4451.png)

14. Enjoy your data:

![image](https://user-images.githubusercontent.com/32093806/188268193-3bd80d5e-1b63-47e9-a8df-f393c1e7a4f4.png)

# Command line arguments

## --path
You can specify the file you want to process or the directory containing all the files with argument **--path**. Example:
`python main.py --path "C://lists_of_properties/list1.html"`

## --all
Include this argument if you want to process all the files in the directory specified by argument "--path". Example:

`python main.py --path "C://lists_of_properties/" --all`

## --output
Specify this argument to choose the output file name. Default output file name is "./output.csv". Example:

`python main.py --path "C://lists_of_properties/" --all --output "C://lists_of_properties/output.csv"`

# Contacts

Once again, do with the script absolutely anything you want, I am just giving you a tool.

If you have any questions, feel free to contact me directly ssssstas30@gmail.com - Stanislav Marochok.
