# Lab 0
## Getting Github Set Up


Steps:

 1. Go to github: [www.github.com](http://www.github.com) and sign up
    for a free account.

 2. __Sign in to github__ and go to the AITI repository for this lab:
    [www.github.com/aiti-ghana-2012/git-and-bash-lab](http://www.github.com/aiti-ghana-2012/git-and-bash-lab)

 3. In the upper right hand corner of the screen, click the ![Fork](/static/images/github-fork-button.jpg) button.
    This makes a copy of the lab by creating a repository on your github account.

 5. On the machine on which you are working, open up the `Terminal`
    application. There are a couple of ways that you can do this.
    You can find it in the `Applications` folder of Ubuntu, or you
    can press `Ctrl-Alt-T` which is a very convenient Ubuntu shortcut
    for opening up a terminal window.

 6. Find out what directory you are in using the `pwd` command.

 8. Use the command `ls` to view the contents of that Directory

 7. Change to the directory called `Documents` using the command `cd Documents`.
    
    (if you don't have one of those directories, raise your hand!)

 8. use `mkdir` to create a directory which has a name that is the same as your github account.
    For example I would type `mkdir louissobel`

 9. use `cd` to move into the directory that you just created

 4. Ok - now use `git` to __Clone__  the repository that you created in step 3 to the machine that you are working on.
    The command for this will be 

    `git clone https://github.com/{{ your user name }}/git-and-bash-lab.git`.
    

    (where your should substitute `{{ your user name}}` for the github username that you chose
    is step 1, mine, for example, is louissobel)

 5. You now have a copy of your lab on the computer that you are working on!
    Follow the instructions in the file `lab-instructions.pdf` to finish up this lab.