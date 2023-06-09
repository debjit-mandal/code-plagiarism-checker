#  Code Plagiarism Checker 
**A  basic code plagiarism checker made using Python**

useIt uses the `difflib` module to compare the similarity between two code files. 

It calculates a similarity score based on the number of matching lines and outputs a plagiarism percentage.

**Note:** It may not detect plagiarism in cases where there are significant modifications to the code structure or different coding styles.

**To run this code locally:**

`git clone https://github.com/debjit-mandal/code-plagiarism-checker`

`cd code-plagiarism-checker`

`python main.py`

**Note:** For example purpose I have added two file **file1.py** & **file2** . You can change it according to your needs. Also remember to change the formula of

    similarity_percentage = (similarity / 2.0) * 100
    
 to
 
     similarity_percentage = (similarity / No. of files) * 100
    
Feel free to suggest any kind of improvements.
