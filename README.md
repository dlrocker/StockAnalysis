# StockAnalysis
Focused on doing various different data explorations on stock data based on activity on different stock related subreddits on Reddit.

[![Stock Analysis Report package test status](https://github.com/dlrocker/StockAnalysis/workflows/python-package-and-test/badge.svg)](https://github.com/dlrocker/StockAnalysis/actions)

## Pre-Requisites
Prior to running this code you need:
- A development environment with Python 3.8
- Access to the Reddit API

All environment setup instructions are for CentoOS 7. For setting up access to the Reddit API,
follow the [Reddit API Access instructions](https://www.reddit.com/wiki/api).

## Running the program
To run the program after setting up your environment execute the following:
```
python3.8 reddit_connect.py -i <your_client_id> -s <your_client_secret> -u u/<reddit_username>
```
where
- `<your_client_id>` is the client ID is the 14-character string listed just 
	under `personal use script` for the desired [developed application found on your 
	users app page](https://www.reddit.com/prefs/apps/)
- `<your_client_secret>` is the client secret. It is the 27-character string listed
	adjacent to secret for the [developed application found on your 
	users app page](https://www.reddit.com/prefs/apps/)
- `u/<reddit_username>` is your Reddit username for which you have registered the app. Example: `u/fake_user`


## Environment Setup
This project is designed to be run on CentOS 7. The following instructions are for setting up helpful tools on CentOS 7 to run and manage this project.

## Installing Python
This project uses Python 3.8. In order to install Python 3.8 I recommended using my other GitHub repository for
installing and setting up software. 
- https://github.com/dlrocker/EnvironmentSetup

Download this repository and simply run
```
./setup.sh --python38
```

### Installing Eclipse
1. Download Eclipse from [the Eclipse website](https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2020-12/R/eclipse-inst-jre-linux64.tar.gz)
2. Open a terminal session
3. Switch to the `Downloads` folder where the Eclipse package was downloaded
4. Run the following commands
	```
	tar -xzvf eclipse-inst-jre-linux64.tar.gz
	sudo mv eclipse-installer /opt/
	```
5. Create the file `/usr/share/applications/eclipse.desktop` using an editor such as `vim` with the following contents:
	```
	[Desktop Entry]
	Name=Eclipse
	Type=Application
	Exec=/opt/eclipse-installer/eclipse-inst
	Terminal=false
	Icon=/opt/eclipse-installer/icon.xpm
	Comment=Integrated Development Environment
	NoDisplay=false
	Categories=Development;IDE;
	Name[en]=eclipse.desktop
	X-Desktop-File=Install-Version=0.22
	```
6. Run the following commands
	```
	sudo desktop-file-install /usr/share/applications/eclipse.desktop
	sudo ln -s /opt/eclipse-installer/eclipse-inst
	```
7. Once complete, you should be able to find and execute the Eclipse application by going to the `Applications` drop-down menu.

### Installing PyCharm
1. Download PyCharm from the [PyCharm Downloads page](https://www.jetbrains.com/pycharm/download/#section=linux). For this example
	I assume the downloaded file name is `pycharm-community-2020.3.2.tar.gz`
2. Unpack the downloaded `tar.gz` file to a permanent location. Example: `tar -xzf pycharm-community-2020.3.2.tar.gz -C /usr/share`
3. Create the file `/usr/share/applications/pycharm.desktop` with the following contents
	```
	[Desktop Entry]
	Name=PyCharm
	Type=Application
	Exec=/usr/share/pycharm-community-2020.3.2/bin/pycharm.sh
	Terminal=false
	Icon=/usr/share/pycharm-community-2020.3.2/bin/pycharm.png
	Comment=Python Development Environment
	NoDisplay=false
	Categories=Development;IDE;
	Version=3.2
	```

You should now be able to launch the PyCharm IDE from your Applications.
