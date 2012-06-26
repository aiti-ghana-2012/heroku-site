# Lab 6
## Python Objects

Steps:

 1. __Sign in to github__ and go to the AITI repository for this lab:
    [www.github.com/aiti-ghana-2012/Lab_Python_06](http://www.github.com/aiti-ghana-2012/Lab_Python_06)

 3. In the upper right hand corner of the screen, click the ![Fork](/static/images/github-fork-button.jpg) button.
    This makes a copy of the lab by creating a repository on your github account.

 5. On the machine on which you are working, open up the `Terminal`
    application. There are a couple of ways that you can do this.
    You can find it in the `Applications` folder of Ubuntu, or you
    can press `Ctrl-Alt-T` which is a very convenient Ubuntu shortcut
    for opening up a terminal window.

 6. Use `cd` to go to the directory `Documents/{{ your username }}`. If this directory does not exist, create it
    using `mkdir`, then switch to it.

 4. Ok - now use `git` to __Clone__ the repository that you created in step 2 to the machine that you are working on.
    The command for this will be 

    `git clone https://github.com/{{ your user name }}/Lab_Python_06.git`.

    (where your should substitute `{{ your user name}}` for your github username)


 7. Add the `instructors` remote _now_ using the command
    
    `git add remote instructors https://github.com/aiti-ghana-2012/Lab_Python_06.git`

    so that when we publish solutions and tests you just have to do a `git pull instructors master`

 5. You now have a copy of your lab on the computer that you are working on!
    Follow the instructions in the file `Lab06.pdf` to start this lab.



## Useful Documentation:
 - Objects and Classes [http://docs.python.org/tutorial/classes.html](http://docs.python.org/tutorial/classes.html)
 - datetime [http://docs.python.org/library/datetime.html](http://docs.python.org/library/datetime.html)