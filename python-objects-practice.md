
# Exercise 1 - Short Answers

 1. What is the difference between a local variable and an object's attribute?
    
	
 2. What method is called when the object is created?
	
	
	
 3. If you have an object instance, obj, and you want to call its
    do_something() method (assuming it has one), how would you do this?

    



# Exercise 2 - Understanding Objects

 1. Write a class called `Address` that has two attributes: `number` and `street_name`.
    Make sure you have an an `__init__` method that initializes the object appropriately

    

 2. Consider the following code:
        
        class Clock(object):

		    def __init__(self, time):
		        self.time = time

		    def print_time(self):
		        time = '6:30'
		        print self.time

		 clock = Clock('5:30')
		 clock.print_time()        
		
	 - What does it print out?
	
	    
	
	 - Create a python file with the code above and run it.
	   Is that what you expected in 1 above? Why or why not?
	
	    
	
 3. Consider the following code:
	
        class Clock(object):

		    def __init__(self, time):
		        self.time = time

		    def print_time(self, time):
		        print time

		 clock = Clock('5:30')
		 clock.print_time('10:30')        

	 - What does the code print out? If you aren't sure, create a python file
	   and run it.
	
	    
    
     - What does this tell you about giving parameters the same
       name as object attributes?

        

 3. Consider the following code:

        class Clock(object):
        
            def __init__(self, time):
                self.time = time
        
            def print_time(self):
                print self.time
        
        
        nairobi_clock = Clock('5:30')
        cairo_clock = nairobi_clock
        cairo_clock.time = '10:30'
        nairobi_clock.print_time()
       

	 - What does the code print out? If you aren't sure, create a python file
	   and run it.

	    

     - Why does it print what it does? What is the relationship between
	   `nairobi_clock` and `cairo_clock`

        

