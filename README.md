## Table of content
1) Installation
2) Screenshots
3) Usage

## Conversion Pdf to CSV
First Convert The pdf to csv using fitz from the Code in the convertor.py code

## Installation
Create a database named 'bonds' in SQL.
You are provided with sql dump import the dump into the MySQL.

Create a user in SQL using the command below. 
CREATE USER 'testing'@'%' IDENTIFIED BY 'password'; 
GRANT ALL PRIVILEGES ON . TO 'testing'@'%' WITH GRANT OPTION;

Open terminal, and install flask and flask-mysqldb by following command. pip install Flask Flask-MySQLdb
Open the main.py file, on the first line of code write your MYSQL password as string.
Run the main.py file, website will be live on localhost.
Visit the link which appears in the terminal to open the website.


## ScreenShots

![image](https://github.com/RishankSoni/DCC/assets/143333903/0b7900a4-3331-4d60-ad4a-879e34ed692b)
Main page of website
![image](https://github.com/RishankSoni/DCC/assets/143333903/e2ba28e1-74dd-48af-8587-be31c01955de)
Drop down for filtering the data
![image](https://github.com/RishankSoni/DCC/assets/143333903/f102630c-4a70-4bda-be77-b0576e5d082e)
Database shown after searching for Name of political party
![image](https://github.com/RishankSoni/DCC/assets/143333903/dee42f61-92e3-468c-866d-1d0e7d9c2638)
Database shown after searching for Name of company
![image](https://github.com/RishankSoni/DCC/assets/143333903/5a22198e-7007-43d8-af20-cdcd11f8bd78)
Table of after searching name of company
![image](https://github.com/RishankSoni/DCC/assets/143333903/693ed964-e319-4846-9b1b-b35ae4037f7d)
![image](https://github.com/RishankSoni/DCC/assets/143333903/6e3c01b6-a8f1-4fa1-831b-c8fb0456526e)
Graph of the above company

![image](https://github.com/RishankSoni/DCC/assets/143333903/f72771ab-a6db-4d5d-9aa4-a344b5de6235)
Table of after searching name of company
![image](https://github.com/RishankSoni/DCC/assets/143333903/35fa2892-5405-4555-ab14-482183ed0b5f)
![image](https://github.com/RishankSoni/DCC/assets/143333903/13d2544f-cbdd-42da-9810-8f81afc2cdec)
Graph for above party name
![image](https://github.com/RishankSoni/DCC/assets/143333903/d14035ab-2549-467b-9a97-9acc271e7fa0)
![image](https://github.com/RishankSoni/DCC/assets/143333903/ff615b43-9830-4e3a-aa57-c63002275f6f)
Which party got donation from which company
![image](https://github.com/RishankSoni/DCC/assets/143333903/2bcec7c4-92a7-46bf-b168-141354b30885)
Which company donated to which party
![image](https://github.com/RishankSoni/DCC/assets/143333903/3599edac-77d8-4f16-ad10-253608219210)
pie chart for the all parties
![image](https://github.com/RishankSoni/DCC/assets/143333903/5c3edb7f-45c9-4d00-8e87-8b3426e2eab1)
![image](https://github.com/RishankSoni/DCC/assets/143333903/670469ce-1eb9-46b3-8b92-c2bd9e0be453)
Extra feature showing polar chart for each

## Usage
1) The first filter search bar you can filter accodring to data coloumn you to filter with.
2) In second dropdown, you can find the data of a particular individual or a company. a. This data include the number of bonds and total money given each year. b. A bar chart showing the total amount for comparision and a also to show number of bonds c. The bar char also have a download button to save the chart as .png locally.
3) In third dropdown, you can find the data of the particular political party. a. This data include the number of bonds and total money encashed each year. b. A bar chart showing the total amount for comparision. and also how many bond the party got c. The bar char also have a download button to save the chart as .png locally.
4) In the fourth part, you will select a political party you will all the company it got donation from, you will get alluvial diagram and total sum each, the diagram also have a download button to save the chart as .png locally.
5) In the fifth part, you will select a company will all the party it donated for, you will get alluvial diagram and total sum each the diagram also have a download button to save the chart as .png locally.
6) Here is a button for 'Get Pie' that shows the pie chart of the total money the political parties took in the total data provided the pie chart also have a download button to save the chart as .png locally.
7) As an extra feature I have added a polar chart of which company donated to which part how much it donated for each party.
8) Each result page has a robust search bar, from which you can search for all the matches in the results obtained from the above searches.




