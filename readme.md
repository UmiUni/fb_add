Logical Plan

Open browser and ide / terminal side by side
 
Go to big boss Chaoran's friend page 

Start the program. It will first find all _add friend_ button. 
For each button it checks if the Name to the left of the button is Chinese, if yes it click the _add friend_ button.

TO-DO
- Go to Chaoran's friend home page and recurse on that friend's friend page.
    - done, friend traversal implemented as BFS
- Check if Chinese implement as substring match using user id.
- Randomization
    - movement, i.e. all the magic numbers
    - type in address bar, random wrong chars / key stroke frequency
    - mix type in address bar & paste the copied string
    - different ways of mouse movement
    - add a random amount of friends
- Stress test.
    - when the memory limit is reached, write out the friendId list and restart with one of them as new seed. Keep a seed list as well. 
- Fail safe
    - raise Exception after each step so as to stop wild behavior 
    - window cannot be covered, e.g. by a prompt.

Implementation 

- Find _add friend_ button: implemented as find the squares with the special ratio. 
- Find _name box_ : implemented as move a relative distance from the center because the box element on the website is fixed.
- Check if Chinese: implemented as using Google's OCR tool butbrowser resolution > 125%.
- Collect friend's friend page: implemented as right click and use pywin32 to read from clipboard, so *machine dependent*
- Go to next friend's friend page: implemented as switch focus to address bar and type in the chars.

Problem & Assumption

- Two windows run at front all the time; one terminal one browser.

