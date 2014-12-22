#Nexus 5 Status - India
> [http://www.nexus5status.in](http://www.nexus5status.in) (**NOW DEFUNCT**) 

##Why?
We all love our nexii (?) and we'd love to get our hands on it. Firstly, it is great that the Great google gods have even listed the device on the Indian Google Play Store. This is a website that simply says if the nexus is available in the Indian play store or not. 

**This was built _purely_ as a way for me to learn some technologies and in sheer anticipation of the Nexus 5**

##Can't i just go over the play store to find that?
Sure, you can. I just set up a place where you can get that information quickly and irrespective of where you are (Google play stores are location specific)

##How does it work?
Every 2 seconds, a simple crawler goes up to the play store website and scraps the information. It looks for a div with a class of `not-available` and if that is found, the phone is not yet out on the play store. If that information isn't found, then it means that the phone is ready for purchase. 

**If having a crawler is wrong, please contact me and i will take it down immediately.**

##Installation
1. Clone the repo
* `virtualenv env`
* `pip install -r requirements.txt`
* In `getDataViaCron.sh` set the `DIR` variable to the directory in which the project is cloned
* `./getDataViaCron.sh` to set up the intial `data.dat` file to which the dumps go to
* Set up your crontab and add the entry prescribed in the `crontab` file. Replace `PATH_TO_SH` with the fully qualified path to `getDataViaCron.sh`
* `python app.py`

##TODO
* Chrome extension (?)
* Make the current information store into a document store instead of a file (see `getDataViaCron.sh`)
* Make the entire setup configuration based
* Change the rendering to a template model
