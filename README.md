
# string_builder
A small python library for efficient string building and concatenation   


**Installation**
you can install this repo py pip

    pip install StringBuilder


**Introduction**

python have a small issue when it comes 
to string concatenation, this library aims to solve this problem 

**The problem**

when you append strings using + (ex:  a += b), python behind the scenes creates a new string with the size of a + the size of b and copy the content of a and b byte by byte into the new string then make the a points to the new string, so the time complexity of single addition would be O(|a| + |b|)

[this guy](https://waymoot.org/home/python_string/) have wrote a good article about this problem and how to tackle it 

**The solution**

A Good solution for this problem is to create a list and append the strings you want, then use `"".join(list)` convert the list to string, this will tackle this problem in amortized linear time because `list.append()` use table doubling


**How to use it**

first create a **StringBuilder** instance 

    from string_builder import StringBuilder
    sb = StringBuilder()

then append the sub_strings you want 

    sb.append(sub_string)

you can replace or delete parts from the string
		

    sb.replace (new, old)
    sb.delete (start, end) 

to get the final string 
	

    sb.build()
    #or 
    sb.to_string()

 

pull requests are welcomed 

this is an alpha version (under testing)
