#1. Create a table (student) with 3 columns (rollno, name, course).

from enum import unique
from unicodedata import name

#query
create student(
    
    rollno int notnull unique;
    name varchar notnull;
    coure varchar nounull;
    
    );
