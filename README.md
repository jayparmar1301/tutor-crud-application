# tutor-crud-application

In this project I have performed CRUD operation on list of Tutor along with courses of tutor.

Install the requirement file
```
$pip install -r requirements.txt
```

Run the server
```
$python manage.py runserver
```

Database Description
------------
1) Tutor Info Table

DATA FIELD	| DATA TYPEAttempt 
--- | --- |
id	| INT
first_name	| VARCHAR (100)
last_name	| VARCHAR (100)
email |	VARCHAR (100)
tutor_skills	| VARCHAR (250)
tutor_exp |	INT 

2) Course Info Table

DATA FIELD	| DATA TYPEAttempt 
--- | --- |
id	| INT
course_name	| VARCHAR (100)
course_description	| VARCHAR (250)
course_duration |	INT 
tutor_id	| ForeignKey(Tutor Info Table)

Project Screen
------------
1) Homepage (List of Tutor)
<kbd> <img src="https://user-images.githubusercontent.com/43089083/163133296-23003e50-f9a8-4d05-8a6f-773b6b88677b.PNG" /> </kbd>



2) Add new Tutor
<kbd> <img src="https://user-images.githubusercontent.com/43089083/163133423-3d86869a-5499-4489-85dc-e782083559bd.PNG" /> </kbd>

3) Update Tutor Info
<kbd> <img src="https://user-images.githubusercontent.com/43089083/163133474-fdde2872-4ef3-45bb-ac93-0703e606327a.PNG" /> </kbd>


4) View courses of Tutor
<kbd> <img src="https://user-images.githubusercontent.com/43089083/163133581-a09c01ba-927a-4832-a417-ebc5c67c5d51.PNG" /> </kbd>


5) Add Courses of Tutor
<kbd> <img src="https://user-images.githubusercontent.com/43089083/163133504-ae97544c-d82a-4cb9-8d83-3aebfaa72b4f.PNG" /> </kbd>


6) Update Course info of Tutor
<kbd> <img src="https://user-images.githubusercontent.com/43089083/163133635-16bebe87-e2cc-40a3-99d7-06e157326a58.PNG" /> </kbd>

7) Error Message
<kbd> <img src="https://user-images.githubusercontent.com/43089083/163139767-c7b1756e-7887-4951-a5bb-c8e39135854a.png" /> </kbd>

