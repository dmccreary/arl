# GPU Server Ubuntu 19.10 Notes

Install stuff that should have been installed by default

Step General Server Configuration Cleanup
First we will get an updated dependency graph.  They will get the distribution updates.  Next, we install the Cromium browser.  Then we install git, ssh and avahi and enable them and make sure that ssh and avahi startup when the server boots.

$ sudo apt update
$ sudo apt-get dist-upgrade
$ sudo apt-get install chromium-browser 
$ sudo apt install git

$ sudo apt install openssh-server
$ sudo systemctl enable ssh
$ sudo systemctl start ssh
# configure firewall to allow ssh traffic
$ sudo ufw allow ssh

Then verify you can log in from a remote ssh.

$ sudo apt-get install -y avahi-daemon
$ sudo systemctl enable avahi-daemon
$ sudo systemctl start avahi-daemon


Fix the host name:
$ sudo vi /etc/hostname
Change it to be arlX where X is the nth server in you group
$ sudo vi /etc/hosts
Change the name of the host there also
$ sudo reboot

Installing the Nginx web server
If your server is being used as the system that displays the event leaderboard information, then you will need to install the nginx web server.

$ sudo apt update
$ sudo apt-get install nginx

$ sudo systemctl enable nginx
$ sudo systemctl start nginx
# configure firewall to allow web traffic
$ sudo ufw allow ssh

Install Samba File Sharing Service

sudo apt install samba
sudo systemctl enable smbd
sudo ufw allow 'Samba'
https://phoikoi.io/2018/05/15/samba-avahi-bonjour-mac-visible.html
Getting the right Nvidia Drivers Installed
The hardest part was the fact that when I did a google on install Nvidia drivers I got instruction from the last 10 years.  You need to get instructions for the exact release!

How to install the NVIDIA drivers on Ubuntu 19.10 Eoan Ermine Linux
https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-19-10-eoan-ermine-linux

$ ubuntu-drivers devices
== /sys/devices/pci0000:00/0000:00:03.1/0000:09:00.0 ==
modalias : pci:v000010DEd00001E07sv000010DEsd000012A4bc03sc00i00
vendor   : NVIDIA Corporation
model    : TU102 [GeForce RTX 2080 Ti Rev. A]
driver   : nvidia-driver-435 - distro non-free recommended
driver   : nvidia-driver-430 - distro non-free
driver   : xserver-xorg-video-nouveau - distro free builtin

== /sys/devices/pci0000:00/0000:00:01.2/0000:02:00.0/0000:03:04.0/0000:05:00.0 ==
modalias : pci:v00008086d00002723sv00008086sd00000084bc02sc80i00
vendor   : Intel Corporation
manual_install: True
driver   : backport-iwlwifi-dkms - distro free

$ sudo ubuntu-drivers autoinstall
… lots of text 

Verify the Nvidia Drivers were installed correctly
$ nvidia-smi
Mon Dec 30 14:11:27 2019
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 435.21       Driver Version: 435.21       CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 208...  Off  | 00000000:09:00.0  On |                  N/A |
| 41%   29C    P8    20W / 260W |    307MiB / 11016MiB |      1%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1069      G   /usr/lib/xorg/Xorg                            18MiB |
|    0      2849      G   /usr/lib/xorg/Xorg                            78MiB |
|    0      3059      G   /usr/bin/gnome-shell                         131MiB |
|    0      6916      G   ...equest-channel-token=122950334825305367    24MiB |
+-----------------------------------------------------------------------------+

Install Miniconda
    2  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    3  bash ./Miniconda3-latest-Linux-x86_64.sh
    8  mkdir projects
    9  cd projects/
   10  git clone https://github.com/autorope/donkeycar
   
Open and new shell and verify that conda is in your path
$ which conda
/home/arl/miniconda3/bin/conda

#
# To activate this environment, use
#
#     $ conda activate donkey
#
# To deactivate an active environment, use
#
#     $ conda deactivate

$ conda activate donkey
(donkey) arl@arl2:~/projects/donkeycar$ pip install -e .[pc]
Obtaining file:///home/arl/projects/donkeycar
Requirement already satisfied: numpy in /home/arl/miniconda3/envs/donkey/lib/python3.7/site-packages (from 

Installing Tensorflow GPU
Now we are ready to install Tensorflow GPU in the conda environment

conda install tensorflow-gpu==1.13.1
