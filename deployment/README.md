# Deployment

Contained in this directory are scripts and configuration files use to deploy this project onto a single node CentOS 8 Stream OS. 

If running as a sudo user, then you must setup the user you are going to run as to be able to execute commands without requiring the privilaged user password. To do this, open `/etc/sudoers` using a text editor (such as `vim`) and add the following line to the file
```
<install_user> ALL=(ALL) NOPASSWD:ALL
```
Where `<install_user>` is the priviladed user with sudo permissions that will be used for the installaition.

Once complete, run the following commands to do the installtion:
```
sudo ./install.sh
```
