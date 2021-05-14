**This contains differnt python scripts which help with qualty of life for a terminal user**


# **Pomodora**

***Usage***:\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; pomodora [options] COMMAND [ARGS]

***Options***: \
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; --help Show this message and exit
          
***Commands***:\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; start \
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  *Options*:    --message, -m Text     default = "Success"\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; stats\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; *Options* :    --help Shows this message and quits\&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 


# **Making them executable globally**

**Step 1:**\
&nbsp; &nbsp; Obtain address of the script by using terminal command\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ``` which pomodora ``` \
&nbsp; &nbsp; You will get a address like "/home/$USER/scripts/venv/bin/pomodora"\

\
**Step 2:**\
&nbsp; &nbsp; Now Create a folder "bin"(name your preference) in home directory and add Symlink of script to it\
&nbsp; &nbsp; &nbsp; &nbsp; ` ln -s /home/$USER/scripts/venv/bin/pomodora /home/user/bin ` \
&nbsp; &nbsp; This will create a shortcut of pomodora in bin\
\
**Step 3:**\
&nbsp; &nbsp; Now open .bashrc file through an editor and add the bin path to it\
```
$ nano ~/.bashrc

# Add the following to the end of your .bashrc file while using nano
# or your text editor of choice:

export PATH="/home/$USER/bin:$PATH" 

```
**Now you can use the script as a command in terminal**
