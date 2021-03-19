# barebone_ds
A barebone DS repo with docker (cpu+gpu)



+++++++++++++++++++++++++++++++++++++++++++++++++++++

EFS

It is recommended to use amazon EFS to simplify connection to embeddings
1) When creating a new EFS, make sure that it allows network connections. 
open port 2049
make sure efs security is same as ec2 instance!

2) There is known issues when mounting the EFS to new instance (ubuntu)

```
sudo apt-get update
sudo apt-get install -y git binutils make
git clone https://github.com/aws/efs-utils
cd efs-utils
make deb
sudo apt-get install -y ./build/amazon-efs-utils*deb
```

if any of the steps about complains about lock, do these:

```
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock*
sudo rm /var/lib/dpkg/updates/*
```

+++++++++++++++++++++++++++++++++++++++++++++++++++++

GIT

```
cp /home/ubuntu/efs/ssh/github_key.pem ~/.ssh/id_rsa     
ssh-keyscan github.com >> ~/.ssh/known_hosts                  
chmod 644 ~/.ssh/known_hosts                                  
chmod 600 ~/.ssh/id_rsa                                       
ssh -T git@github.com     
```

to clone:
> git clone git@github.com:username/repo_name.git

+++++++++++++++++++++++++++++++++++++++++++++++++++++

VSCODE 
install "remote ssh" extension

```
Host "rememberable name"
  HostName 123.123.123.123
  User ubuntu
  IdentityFile  "c:/absolute/path/to/key.pem"
  Port 22
```
  
++++++++++++++++++++++++++++++++++++++++++++++++++++++



DOCKER

for shared folder, on windows use the "/e/WORK/ML/data/" format and git bash

from the root folder:

### activate docker
sudo systemctl unmask docker
sudo systemctl start docker

$ docker-compose build <SERVICE_NAME>            ==> barebone_ds_cpu / barebone_ds_gpu

$ docker run -it -p 8080:8080 --name my-container --user root -v //path/to/embedding/:/root/opt -v /${PWD}:/root/main bareboneds_barebone_ds_cpu
(for windows might need to do 'winpty docker run ...')


on AWS to run with GPU, use:

> --gpus all (https://towardsdatascience.com/how-to-set-up-docker-for-deep-learning-on-aws-bce751eaf662) => this worked for me

or

> --runtime=nvidia  (https://wadehuang36.github.io/2019/05/29/a-easy-way-to-use-nvidia-docker-on-aws.html)

for example:
$ docker run -it --gpus all -p 8080:8080 --name container-name --user root -v //path/to/embedding/:/root/opt -v /${PWD}:/root/main image_name

use run_notebook to open jupyter, it will open on 127.0.0.1:8080

attach VSCODE to a running container:

1) open vscode on empty folder and in terminal run this command:

> ssh -i test-key.pem -NL localhost:45312:/var/run/docker.sock ubuntu@18.191.237.1

2) File => Prefences => Settings => Workspace => docker.host, insert: tcp://localhost:45312
3) On the sidebar, click docker icon. You should see the container on remote host. Right click and attach to container.


++++++++++++++++

to use with vscode follow:
https://www.analyticsvidhya.com/blog/2020/08/docker-based-python-development-with-cuda-support-on-pycharm-and-or-visual-studio-code/
"Setting up Visual Studio Code" section
