#8. Create Courses table (cid, cname) where cid is a primary key and Student table
#(rollno, name, cid) where rollno is a primary key and cid is a foreign key


#query

from unicodedata import name


CREATE courses(
    cid int notnull unique primarykey;
    name varchar notnull;
    
    
)

CREATE student(
    rollno int noutnull unique primarykey;
    name varchar notnull;
    cid int not null foreighnkey;
    
    
)