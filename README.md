# Creating_module_and_uploading_to_PYPI


This module is created for google sheet it helps google sheet csv file to take from google drive and plot graph for the desired column values.



First make a folder I named my folder as greenDeck_Task2. In this folder create another folder with whatever name of package in here I named it as plot_chart. Inside plot_chart folder one python file exist which I created with name “__init__.py”.
In here I wrote simple code to read google sheet and save as data frame I used pandas to read the file and store it in df variable. Then created function. Then I choose which column is going to be the x axis and which column is going to be y axis. Function plot_chart(x,y) takes two argument as x-axis and y-axis which will plot a graph 
 Creating the package files
I will now create a handful of files to package up this project and prepare it for distribution. Createating the new files listed below and place them in the project’s root directory like
---------greenDeck_Task2

|------plot_chart>
            
            -->------ __init__.py

|------LICENCE

|------README.txt

|------MANIFEST.in

|------CHANGELOG

|------setup.py

# Creating setup.py

setup.py is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include.

Open setup.py and enter the following content

import setuptools


with open("README.txt", "r") as fh:

    long_description = fh.read()
    


setuptools.setup(

    name="plot_chart_HSD", # Replace with your own username
    
    version="0.0.1",
    
    author="HSD",
    
    author_email="ashuhemantsingh@gmail.com",
    
    description="A basic operations with arithmetic operators",
    
    long_description=long_description,
    
    long_description_content_type="text/markdown",
    
    url="",
    
    packages=setuptools.find_packages(),
    
    classifiers=[
    
        "Programming Language :: Python :: 3",
        
        "License :: OSI Approved :: MIT License",
        
        "Operating System :: OS Independent",
        
    
    ],
    
    python_requires='>=3.6',
    
    

)

For more information on this please consider visiting https://packaging.python.org/tutorials/packaging-projects/ 
Creating README
Open README and enter the following content. If you want your own content you can customize this if you’d like
This is a simple graph plot which take csv file from googal sheet and plot.

# Creating a LICENSE

It’s important for every package uploaded to the Python Package Index to include a license. This tells users who install your package the terms under which they can use your package. I’m using license from MIT as bellow.

Copyright 2020 Hemant S D

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



# Generating distribution archives

The next step is to generate distribution packages for the package. These are archives that are uploaded to the Package Index and can be installed by pip.
Make sure you have the latest versions of setuptools and wheel installed:

python setup.py sdist bdist_wheel

the above command should be typed from greenDeck_Task2 folder which is our root folder.
This command should output a lot of text and once completed should generate two files in the dist directory one is .whl and other it .tar


# Uploading the distribution archives

The first thing you’ll need to do is register an account on Test PyPI. Test PyPI is a separate instance of the package index intended for testing and experimentation.To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages.
Now you’ll create a PyPI API token so you will be able to securely upload your project.
Go to https://test.pypi.org/manage/account/#api-tokens and create a new API token; don’t limit its scope to a particular project.Don’t close the page until you have copied and saved the token — you won’t see that token again.
Now that you are registered, you can use twine to upload the distribution packages. You’ll need to install Twine


python -m twine upload --repository testpypi dist/*


this is link where it can be installed

pip install -i https://test.pypi.org/simple/ plot-chart-HSD

# How to install library using pip

* go to command prompt and type pip install -i https://test.pypi.org/simple/ plot-chart-HSD
  This will install the package. 
  For this package to work, some recomended package which are
  -Matplotlib
  -pandas
  --this two package are needed
  get google_sheet file data from :https://docs.google.com/spreadsheets/d/1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc/edit#gid=0
  
 # How to Initialize the library and use it
  
 * first we need to go to google sheet and on right top corner, click Share. A pop-up will pop open here we need to select get link we want to make this share. if          anyone have link only they can use it. eg.: my link is "https://docs.google.com/spreadsheets/d/1jbcRvatx1DmtxWWwC7dcEwSyYOAxD0iFICGN33JoUSk/edit?usp=sharing"
    In this link we only want token or key. call it what you like anyone have link only they can access, eg. my link is key is:
    "1jbcRvatx1DmtxWWwC7dcEwSyYOAxD0iFICGN33JoUSk" every key can be found after "https://docs.google.com/spreadsheets/d/" and before "/edit?usp=sharing" the key
    looks like https://docs.google.com/spreadsheets/d/ KEY /edit?usp=sharing
           
    this key we will need as we write our script.
 *  in this repositry an example.py is given to see how it is written. 
------------------------------
