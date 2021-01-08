# StockAnalysis
Focused on doing various different data explorations on stock data based on activity on different stock related subreddits on Reddit.


# Environment Setup
This project is designed to be run on CentOS 7. The following instructions are for setting up helpful tools on CentOS 7 to run and manage this project.

## Installing Eclipse
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

## Installing git command line
To install the `git` command line run the following commands in a terminal
```
yum -y install epel-release
yum -y install git
```
